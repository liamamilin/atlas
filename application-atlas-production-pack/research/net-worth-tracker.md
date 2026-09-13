# Research Notes — Net Worth Tracker

Research date: 2026-09-08

## Research Goal

Understand what a **Net Worth Tracker** is as an Application Type: what its central records are, how values enter and stay current, what is computed and displayed, how the Type relates to the surrounding personal-finance leaves (Personal Finance Management, Budgeting, Expense Tracking, Debt Management, Portfolio Management), and where the Type's boundary actually sits given that many PFM products ship a net worth view.

## Initial Boundary (pre-research hypothesis)

- Core use: track a person's (or household's) total wealth — assets minus liabilities — as a current figure and as a trend over time.
- Users: individuals and households; sometimes advisors/professionals granted access.
- Nearest neighbors: Personal Finance Management Application (flow-centric), Budgeting Application (planned flows), Expense Tracking Application (recorded flows), Debt Management Application (liability-side with payoff plans), Portfolio Management System (investment holdings, professional seat), Retirement Planning Application (future projections), Crypto Wallet / DeFi Portfolio (asset-class-specific), Wealth Management Platform (advisor seat).
- Hypothesized discriminator: **stock vs flow** — a Net Worth Tracker organizes around the balance sheet (what you own and owe at a point in time); PFMs organize around money movement.
- Unknowns going in: Is there a standalone market for net-worth-first products, or is net worth always a feature inside PFMs? How do products value non-traded assets? What lifecycle do asset records have?

## Research Questions

1. What is the unit of record — an account, an asset, or the balance sheet itself?
2. How do values enter the system: bank/brokerage aggregation, market tickers, automated estimates (property, vehicles), manual entry?
3. How do assets and liabilities relate to each other (e.g., mortgage ↔ home equity)?
4. What does the application compute and display: headline number, composition, history over time?
5. What lifecycle do records have: value updates, stale/refresh reminders, sale/close-out, archiving?
6. Who participates: single person, household/partner, advisor/professional? How is sharing controlled?
7. Where is the line between a standalone Net Worth Tracker and a PFM that includes a net worth view?
8. Which capabilities are defining, which are common mature structure, which are variants, which are vendor-specific?

## Representative Products

Selected for market representativeness, documentation quality, differing product philosophy, and differing customer tier:

| Product | Philosophy | Tier | Evidence depth |
|---|---|---|---|
| Kubera | Net-worth-first "personal balance sheet"; explicitly not a budgeting app; affluent/prosumer | paid subscription | **Tier-1 help center** (Help Scout; ~146 articles across Basics/Intermediate/Pro/Connectivity) + product page |
| Empower (Personal Dashboard) | Investment-led free wealth dashboard; net worth as one "financial tool"; advisory upsell | free dashboard + paid advisory | **Tier-2 product pages** (Net Worth tool page) |
| Monarch Money | Full PFM ("track, budget, plan, manage") where net worth is a headline dashboard view | consumer subscription | **Tier-1 help center** (Zendesk) + product page |
| Copilot Money | Mobile-first consumer PFM; net worth presented as the "all your money, one screen" view | consumer subscription | **Tier-1 help center** (Intercom) + product page |

## Sources

Fetched 2026-09-08 (all official):

- Kubera — homepage https://www.kubera.com/ ; help center root https://help.kubera.com/ ; Basics category https://help.kubera.com/category/6-new-to-kubera ; Intermediate category https://help.kubera.com/category/14-portfolio-tracking ; articles: "How do I add assets to Kubera?" (/article/5), "How do I link a mortgage to my home to see my equity?" (/article/95), "Mark as Stale…" (/article/46)
- Empower — homepage https://www.empower.com/ ; Net Worth tool page https://www.empower.com/tools/net-worth
- Monarch Money — homepage https://www.monarchmoney.com/ ; help center https://help.monarch.com/hc/en-us ; Product Feature Guides category; "Using Reports" article (/hc/en-us/articles/21846787088916-Using-Reports)
- Copilot Money — homepage https://copilot.money/ ; help center https://help.copilot.money/ ; "Dashboard Tab Overview" (/en/articles/6045480-dashboard-tab-overview)

## Product A — Kubera

### Key observations (evidence layer A unless noted)

**Self-positioning (homepage).** "The Balance Sheet for those who keep the 1%". "Kubera puts everything you own and owe on one page, so the person with the complete picture of your wealth is you." Pricing pitch is anti-advisor ("$250 a year, not 1% of your wealth"), and an explicit prompt template fed to AI assistants says: "Not a budgeting app. Not an advisor pitch." The product's own vocabulary is *balance sheet*, *net worth tracking* ("Kubera makes tracking your net worth fun"), *portfolio*, *assets and debts*.

**Unit of record = the personal balance sheet, implemented as a sheet/table.** The help center instructs: "Add, rename and rearrange the sheets. Create sections within the sheets." and "Enter all the assets that can't be 'connected' as manual entries… Just like in an Excel spreadsheet" (Mark as Stale article). Rows are assets and debts; sheets/sections organize them. There is no ledger of transactions as the primary object — the primary object is a valued row on a balance sheet.

**How values enter (add-assets article, direct).** Multiple entry mechanisms per asset type:
- Connect bank and brokerage accounts "to get the latest values and holdings automatically" (aggregators; "runs multiple aggregators, local and global, and picks the best connector for each of your institutions").
- Ticker lookup for stocks/funds and crypto ("track your live positions using stocks & fund tickers"; "Lookup for your Crypto Coin symbols and add them") — position quantity × live market price.
- Real estate: "Enter the address or the Zillow URL to get the latest estimated market price (US Only). For non US, just insert a new row and enter the value manually."
- Vehicles: "Enter the VIN number to get the latest estimated market price of your vehicles (US & Canada Only)."
- Internet domains: "Enter your internet domains to get their latest estimated market value."
- Everything else: manual rows, with cost encouraged ("If possible, enter cost of your assets as well. If you only know the cost, enter it as the value.")
- Multi-currency: "Enter any currency (EUR 100, INR 100) in the value fields and it'll convert to your portfolio currency. You can also enter crypto tickers (BTC 1, ETH 20) and stock tickers."
- Asset breadth claim: "Gold, Real Estate, Vehicles, Jewelry, Watches, anything… Live price feeds plus AI appraiser keep every asset current. If you can own it, Kubera can track it." Digital assets (exchanges, wallets, DeFi, NFTs, staking, lending) and private/LP positions (committed capital, calls, distributions, IRR) are first-class asset types.

**Asset–liability relation (mortgage-linking article, direct).** Debts live in a "Debts section". A home asset has a "Mortgage Balance" field that can be linked to a home loan ("link a mortgage to my home to see my equity"); multiple loans can be linked; manual loan entry is also possible and "will get added to Debts as a manual entry". So equity is derivable: asset value minus linked liabilities.

**Value lifecycle (Mark as Stale article, direct).** Manual rows are "updated periodically… Just like in an Excel spreadsheet. Every update to the value is saved in the history of the asset." A row can be marked "Stale" (visually distinct) as a reminder to refresh; scheduling can auto-mark manual rows stale periodically (weekly/monthly/yearly) with a reminder email; a sheet-level default schedule exists for the first sheet. Separate article covers correcting the value of an asset *for a past date* — i.e., value history is editable and dated. Another article covers marking the sale of a manual asset and closing it out; archived assets are a state (deletable).

**Classification & structure.** Assets can be assigned an "Asset Class" (article 140). Holdings can be surfaced "on to the assets table" (article 54). Ownership share per asset ("Portfolio Share %", article 108), ownership tags across people/trusts/entities, and nested portfolios (per person/trust/entity with independent views and access control) exist for complex wealth (Black tier features).

**Computed views.** "Real-Time Reporting: See how your investments grow over time. Get a snapshot of your portfolio allocations from multiple dimensions." "Recap — View Portfolio Trends, Allocations & Performance" (article 114). IRR and CAGR supported (articles 79, 83). Investable Assets is a defined sub-figure (article 47). Cash across accounts + "Cash forecasting" for liquidity. "Fast Forward" runs scenarios on the balance sheet ("sell the company, buy the house, fund the trust and watch the balance sheet respond"; inflation rule). "Tax Estimate" on unrealized gain. Net worth can even be displayed in Bitcoin ("View your net worth in Bitcoin if you like").

**Participation.** "Multiplayer — Share portfolios with family, assistants, advisors, accountants… Granular access control decides who sees what and how much." Family/team invites (article 116). "Dead Man's Switch" delivers the portfolio to chosen beneficiaries after prolonged silence. "Proof of Wealth" produces a self-attested, Kubera-verified statement. "Club Benchmarks" compares allocations against aggregated anonymized peers.

**Pricing (L3).** $250/yr Essentials; $2,500/yr Black (complex multi-entity wealth: ownership tags, nested portfolios, guided onboarding). White-label starting $300/mo.

## Product B — Empower (Personal Dashboard)

### Key observations (evidence layer A for the tool page; B for dashboard-in-practice)

**Net Worth is a named, official tool.** The individuals site lists "Financial tools": Retirement Planner, **Net Worth**, Budgeting & Cash Flow, Portfolio Analysis, Savings Planner, Debt Paydown, Emergency Fund, Transactions. Net Worth page tagline: "Knowing your net worth is worth it — See where you stand to get where you want to be."

**Definition stated verbatim (Tier 2).** "Your net worth is the value of your assets minus your liabilities. Use it to: Monitor and improve your financial health. View a full picture of your assets and liabilities. See the impact of paying down debt or saving more." Framed as "Your vital sign for better financial outcomes."

**Ownership and accounts.** "Take stock of what you own and what you owe"; "Gain a clear picture of your debts and assets"; "Look at all your accounts in one place." Homepage: "Securely connect all your accounts in one place — Because getting good at money starts when you see the full picture of your investments, cash, credit, and other accounts."

**Type posture.** The net worth view is one surface of a broader wealth ecosystem whose revenue engine is advisory (Personal Strategy at $100k+ invested, Private Client at $1M+; advisory fees on managed assets). The free dashboard (aggregation + tools) is the acquisition layer. So Empower evidences the *investment-led* pole: net worth is the headline "vital sign", investments get the deepest treatment (Portfolio Analysis), and flows tools (Budgeting & Cash Flow, Transactions) sit alongside.

## Product C — Monarch Money

### Key observations (evidence layer A for help center/product page)

**Positioning: full PFM.** "Track, Budget, Plan and Manage Money in One Place"; "Your home base for money clarity". Features: Track, Budget, Collaborate, Plan. WSJ/Forbes quotes position it as a budgeting app. Yet its Net Worth section is prominent: "**Net Worth — All your accounts, in one place**: Connect all your bank accounts, credit cards, loans, real estate, and investments to see your entire financial picture in one place."

**Net worth as dashboard headline (B).** "Know where you stand — From your net worth to day-to-day spending and cash flow, feel confident about where you're at." Homepage Reports blurb: "Whether you're tracking spending trends, income, or net worth over time…" — though the fetched help article on Reports documents Cash Flow/Spending/Income tabs (flow-oriented charts: Sankey, Trend Bars, Pie, Breakdown, Treemap); net worth over time lives on the Dashboard rather than the documented Reports tabs (based on fetched pages; not exhaustively verified).

**Connectivity (A).** "Monarch syncs with multiple financial data providers, more than other apps, to connect with 13,000+ financial institutions" (vendor claim). Help center has a large "Financial Accounts & Connectivity" category plus connection-status tooling.

**Participation (A).** "Invite your partner to see your full picture… collaborate with your partner or professional at no extra cost"; "When you and your partner both sync your accounts, you'll get a shared view of your finances." A Professionals Program category exists in the help center (advisor/professional access), and a Professional Directory is linked.

**Adjacent machinery (A).** Budgets, Goals ("Pay Down" / "Save Up" goals), recurring/subscription detection, transactions with review workflow, credit score, bill sync, estate-planning integration (Trust & Will), forecasting. All flow/plan machinery — the balance sheet is one surface of it.

## Product D — Copilot Money

### Key observations (evidence layer A for help center; A for marketing claims)

**Net worth as a marketing pillar (A).** "Track spending, budgets, investments & net worth all in one beautifully designed place." "**All your money, one screen** — Stocks, crypto, your house. No need to jump between five different apps to see your net worth." Screenshot shows a total balance with per-account balances and % changes over a window ("3m balance change") across brokerage/exchange/robo accounts. Real estate: "Type in your address. We'll track what your place is worth." — add a real-estate account by pasting a Zillow URL (same AVM-via-address pattern as Kubera). Allocation chart ("Too much crypto? Not enough bonds?") and live performance estimates for holdings.

**Where the center of gravity actually is (A).** The help center's "Dashboard Tab Overview" documents a spending-first dashboard: Free-to-Spend graph, To Review transactions, Budgets, Upcoming recurrings, Net This Month. Top-level tabs: Accounts, Cash Flow, Categories, Goals, Investments, Recurrings, Transactions (+ Dashboard). Net worth/balance is surfaced through Accounts and the "all your money" screen; budgeting and transactions dominate the daily loop.

**Type posture.** Copilot evidences the *mobile consumer PFM* pole: net worth is a first-class view ("see your net worth" is a listed capability) but the organizing loop is monthly spending/budgeting.

## Cross-product Comparison

| Dimension | Kubera | Empower | Monarch | Copilot |
|---|---|---|---|---|
| Net worth = assets − liabilities as headline | ✔ (entire product; even BTC-denominated) | ✔ (stated verbatim as the tool's definition) | ✔ (dashboard headline, shared household view) | ✔ ("all your money, one screen") |
| Balance sheet (assets AND debts incl. non-financial) | ✔ core (sheets of asset/debt rows; "everything you own and owe") | ✔ (assets and liabilities picture) | ✔ (bank, credit cards, loans, real estate, investments) | ✔ (stocks, crypto, house) |
| Bank/brokerage aggregation | ✔ (multiple aggregators; fallbacks) | ✔ | ✔ (multi-provider, 13k+ institutions claim) | ✔ |
| Market-priced positions via tickers | ✔ (stocks, funds, crypto) | ✔ (investments focus) | ✔ (investments holdings) | ✔ (live estimates) |
| Automated estimates for non-traded assets | ✔ (address/Zillow, VIN, domains, AI appraiser) | not evidenced on fetched pages | ✔ ("real estate" listed as connectable; mechanism not detailed on fetched pages) | ✔ (Zillow URL) |
| Manual entries for un-connectable assets | ✔ (explicit; cost encouraged) | not evidenced on fetched pages | ✔ (manual holdings documented for investments) | ✔ (manual real-estate account) |
| Asset ↔ liability linking (equity) | ✔ (mortgage linked to home) | not evidenced | not evidenced on fetched pages | not evidenced |
| Value history / trend over time | ✔ (per-asset history; Recap trends) | ✔ ("see the impact of paying down debt or saving more") | ✔ ("net worth over time") | ✔ (balance change over window) |
| Record lifecycle (stale/sale/archive) | ✔ (Mark as Stale + schedules; sale close-out; archive) | not evidenced | not evidenced | not evidenced |
| Household/partner sharing | ✔ (multiplayer + granular access; paid) | not evidenced | ✔ (partner collaboration included; professionals program) | not evidenced |
| Budget/transaction machinery | ✘ (explicitly not a budgeting app) | ✔ (Budgeting & Cash Flow, Transactions) | ✔ (core of product) | ✔ (core of product) |
| Investment analytics | ✔ (IRR/CAGR, allocation, Recap) | ✔ (Portfolio Analysis) | ✔ (Investments section) | ✔ (performance, allocation) |
| Planning/scenarios | ✔ (Fast Forward; cash forecasting) | ✔ (Retirement Planner) | ✔ (Goals, forecasting) | ✔ (Goals) |
| Complex structures (entities/trusts/ownership) | ✔ (ownership tags, nested portfolios, share %) | ✘ (personal) | ✘ (household) | ✘ (personal) |
| Estate/legacy features | ✔ (Dead Man's Switch) | not evidenced | ✔ (Trust & Will integration) | ✘ |

Evidence layers: rows marked ✔ are Layer A for the named product; generalizing to the Type requires the B/C reasoning below.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A Net Worth Tracker is a person-side application whose defining core is exactly three jointly-held structures:

1. **The personal balance sheet as the unit of record.** The person's own assets and liabilities are held as individually identified records, each carrying a money value. Both sides are required: without liabilities it is an investment/portfolio tracker; without non-debt assets it is a debt tracker. The records are the person's own holdings — the person is both subject and audience.
2. **The computed net worth figure.** The application synthesizes the records into a single assets-minus-liabilities figure, kept current, as its headline output. Without the computation it is an account list / aggregator, not a net worth tool.
3. **Net worth as a time series.** Values are refreshed (automatically or by hand) and history accumulates, so the figure can be read as a level *and a direction* across time. Without it, the product is a one-shot calculator or a static snapshot.

Remove-test: 1 alone = asset list; 2 alone = calculator; 3 alone = guess at wealth; 1+2 without 3 = static snapshot (spreadsheet filled once); 1+3 without 2 = un-aggregated account feed; 2+3 without 1 = a number with nothing behind it.

**Historical / market-sample check (§24 applied).** A paper household balance-sheet ledger (assets on one side, liabilities on the other, totals struck and re-struck periodically) satisfies all three legs — no bank aggregation, no automatic valuation, no cloud, no goals. The ubiquitous personal-finance spreadsheet ("net worth" tab updated monthly/annually) satisfies all three legs. Older platform-native "my accounts" summaries with a balance total satisfy thinly (records + computation; trend only if history is kept). Therefore **bank connectivity, automated market data, estimated valuations, and sharing are NOT definitional** — they are the modern substrate, not the invariant.

### L1 — Common Mature Structure (evidence: cross-product B)

- **Account connectivity** — linking banks, brokerages, credit cards, loans (all four products in some form) so balances and holdings arrive without manual entry.
- **Market-priced positions** — securities/crypto valued from live prices via tickers or connected holdings (all four).
- **Estimated valuations for non-traded assets** — property via address/AVM data, vehicles via VIN, in the products that document it (Kubera, Copilot; Monarch lists real estate as connectable; Empower not evidenced on fetched pages). Region-limited (US/US+Canada in the sampled implementations).
- **Manual entry** — for anything un-connectable; encouraged with cost/estimate as fallback value (explicit in Kubera; manual investment holdings in Monarch).
- **Composition & classification** — breakdown of net worth into asset classes/categories (cash, investments, property, other; debts) — Kubera asset classes, Empower/Monarch/Copilot breakdowns.
- **Asset–liability linking → equity** — evidenced (Kubera mortgage↔home); plausibly common but only single-product evidenced on fetched pages → treat as common-with-note, not defining.
- **History & trends** — net worth over time at portfolio level (all four) and per-asset value history (Kubera explicit).
- **Drill-down** — per-account/per-asset detail behind the headline.

### L2 — Variant / Optional Structure

- **Product philosophy poles**: net-worth-first wealth dashboard (Kubera) vs investment-led dashboard with advisory upsell (Empower) vs PFM with net worth as one view (Monarch, Copilot) vs the thin spreadsheet/manual pole (no product in sample; historical check).
- **Flow machinery** (budgets, transactions, cash flow, goals) — present in the PFM pole, absent in the net-worth-first pole; boundary-zone capability.
- **Investment analytics** — IRR/CAGR, allocation, performance (depth varies).
- **Scenario/planning** — retirement projections, what-if on the balance sheet.
- **Participation** — partner/household sharing (Monarch included-by-default; Kubera paid/granular), advisor/professional access (Monarch professionals program; Kubera sharing).
- **Complex wealth structures** — entities, trusts, ownership shares, nested portfolios (Kubera; affluent segment).
- **Multi-currency** (Kubera explicit; expat segment).
- **Estate/legacy** — beneficiary delivery (Kubera), estate-planning integration (Monarch).
- **Liquidity view** — cash across accounts, forecasting (Kubera).

### L3 — Vendor-specific (research notes only)

- Kubera: sheet/spreadsheet metaphor with stale-marking and scheduled reminders; Dead Man's Switch; Proof of Wealth; Club Benchmarks; Web Sync browser extension; AI Appraiser; File Import; MCP/AI-assistant integration; Bitcoin-denominated net worth; pricing ($250 / $2,500 tiers; white-label).
- Empower: "financial vital sign" framing; free-dashboard-as-funnel into advisory (Personal Strategy $100k+, Private Client $1M+); award-quote marketing.
- Monarch: Sankey/flow report suite; Goals 3.0; Trust & Will partnership; 13,000+ institution claim; Professionals Directory.
- Copilot: AI transaction tagging, rollover budgets, Apple-ecosystem-first apps, referral credits.

## Vendor-specific Findings

- Kubera's sheet metaphor and stale-reminder machinery are its signature implementation of the *keep values current* problem; nothing in other sampled products evidences the same mechanics (Monarch/Copilot rely on aggregation freshness; manual-update reminders not evidenced). Product-specific.
- Kubera's complex-wealth tier (entities, nested portfolios, ownership %) addresses a segment the consumer PFMs do not appear to serve. Product/segment-specific.
- Empower's advisory funnel and Monarch's professionals program are business-model features, not Type structure.
- Copilot's Dashboard tab being spending-centric is a product choice; its net worth capability is asserted on the product page rather than in the fetched help article.

## Rejected Findings (considered and rejected from the defining core)

- **Bank/brokerage connectivity is definitional** — rejected: paper/spreadsheet trackers satisfy the Type without it; connectivity is how modern products populate values, not what makes them net worth trackers.
- **Automated valuation (AVM/AI appraiser) is definitional** — rejected: single-era implementation; region-limited even today (US-centric in sampled implementations); manual valuation is the older, still-valid path.
- **Budgeting/transactions are part of the Type** — rejected: Kubera explicitly refuses them and remains a full net worth product; they belong to the PFM pole of the boundary.
- **Goals/targets are definitional** — rejected: present in Monarch/Copilot/Empower as plan machinery; absent from the net-worth-first pole; single-sided evidence.
- **Household sharing is definitional** — rejected: present across sample but absent from historical/single-user implementations; participation model varies.
- **"Net worth" needs a currency/display convention (e.g., single-currency totals)** — rejected: multi-currency is a variant; single-currency default is implementation.
- **Investment performance analytics (IRR/CAGR) are definitional** — rejected: only meaningful for the traded-asset subset; the Type also covers non-financial assets and debts.

## Boundary Findings

- **vs Personal Finance Management Application — the critical boundary.** In the sample, two of four products (Monarch, Copilot) are full PFMs that include a net worth view; one (Empower) is an investment-led dashboard; only Kubera is net-worth-first. Criterion that holds: a Net Worth Tracker organizes the person's financial world around the **balance sheet (stock)**; a PFM organizes around **money movement (flows)** — transactions, budgets, cash flow — with net worth as one derived view. If flow machinery is removed from Monarch/Copilot, the net worth layer survives as this Type; if the balance sheet is removed from Kubera, nothing remains. **Taxonomy flag:** net worth tracking is a *standard capability* of mature PFMs; the standalone Type is justified by the net-worth-first pole (products whose organizing center is the balance sheet and which omit flow machinery entirely). Joint review with personal-finance-management-application recommended.
- **vs Budgeting Application** — planned/allocated future flows vs stock of wealth. Same person, different organizing object.
- **vs Expense Tracking Application** — recorded past flows vs stock.
- **vs Debt Management Application** — consistent with that pass's forward flag: NWT holds liabilities as *snapshot balances* feeding a wealth figure; Debt Management holds them as *payoff projects* with a plan engine. A debt record appears in both with different organizing purpose.
- **vs Portfolio Management System / Retail Trading Platform** — PMS is holdings+performance of *investment portfolios* (often professional seat, institutional semantics: attribution, benchmarks, risk); NWT spans the whole personal balance sheet including cash, property, vehicles, personal liabilities. Empower's Portfolio Analysis vs its Net Worth tool exhibits the seam inside one product.
- **vs Retirement Planning Application** — projections of a future state vs the current stock and its history.
- **vs Crypto Wallet / DeFi Portfolio Application** — asset-class-specific custody/interaction vs whole-wealth record-keeping (crypto appears in NWTs as priced positions, not as wallets).
- **vs Wealth Management Platform / Financial Advisor Platform** — advisor-side seat (institution manages clients' wealth) vs person-side seat. Empower shows both seats in one company (dashboard = person-side; EAG advisory = advisor-side).
- **vs Estate Planning Application** — recording what exists vs structuring its disposition; Kubera's Dead Man's Switch and Monarch's Trust & Will integration are adjacency, not identity.
- **vs Digital/Mobile Banking Application** — bank-side single-institution balance view vs person-side cross-institution balance sheet.
- **"去掉什么就变成另一个 Type" 判据**: remove the liabilities side → Portfolio/investment tracker; remove the assets side → Debt tracker; remove the computed total → account aggregator; remove time/history → calculator; add flows as the organizing object → PFM.

## Uncertainties

- Monarch's net-worth-over-time reporting: marketing mentions it; the fetched Reports help article documents only flow-oriented tabs. Net worth view placement (Dashboard vs Reports) not fully pinned. Assertions kept generic.
- Empower's non-traded-asset handling (property/vehicles) not evidenced on fetched pages — the dashboard may or may not support manual real-estate entries; not asserted.
- Copilot's net worth mechanics (per-asset history, liability side handling) come from product-page claims; help-center detail on the net worth view was not fetched. Assertions kept at claim level.
- Sharing in Empower/Copilot not evidenced; not asserted.
- App-store-only trackers (numerous mobile "net worth tracker" apps) and advisor/family-office tools were not sampled; the spreadsheet/manual pole is a historical reconstruction, not product-documented.
- Aggregation failure modes (broken connections, stale feeds) are acknowledged in Kubera's help ("Why do my bank and brokerage connections keep dropping?") but routine handling across products was not researched.

## Final Synthesis

The Net Worth Tracker is the **person-side balance-sheet application**: it holds what the person owns and owes as valued records, computes the single assets-minus-liabilities figure that names the Type, and keeps that figure over time so wealth has a level and a direction. Everything else in the market — aggregation, live prices, property estimates, budgets, goals, advisors, entities, estate hand-off — is substrate or segment machinery layered on that core. The Type's sharpest edge is against the PFM: same person, same data plumbing, but a Net Worth Tracker's world is organized around the stock of wealth, while a PFM's world is organized around its flow. The market realizes the Type across a gradient — net-worth-first products (Kubera), investment-led dashboards (Empower), and PFMs carrying the balance sheet as one view (Monarch, Copilot) — which is exactly why the boundary flag for the PFM leaf is worth a joint review.
