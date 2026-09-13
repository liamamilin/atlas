# Research Notes — Robo-advisor

## Research Goal

Understand what a Robo-advisor actually is as an Application Type: what objects exist inside it, what the user does vs. what the service does, how the onboarding→management loop works, and where its boundary lies against adjacent financial types (brokerage platform, financial advisor platform, portfolio management system, retirement planning, PFM, algorithmic trading, retail trading).

## Initial Boundary

- Working hypothesis: a consumer investing service where the service (not the user) constructs and continuously maintains a diversified portfolio on the user's behalf, based on a recorded investor profile; the user funds, monitors, and adjusts, but does not make per-security decisions as the primary mode.
- Nearest confusion risks: Brokerage Platform (self-directed trading), Financial Advisor Platform (human advisor operates), Portfolio Management System (institutional operator tool), Retirement Planning Application (projection without execution), PFM (tracking without investing), Algorithmic Trading Platform (user-authored strategy), Retail Trading Platform (self-directed decisions), Wealth Management Platform (advisor-led comprehensive).
- Prior passes left explicit joint-review notes: retirement-planning-application ("portfolio construction/execution = robo-advisor"), brokerage-platform ("robo appears as a mode over the same account, run by a separate registered-adviser entity"), retail-trading-platform ("when the vendor's algorithm decides and rebalances, the mode crosses toward robo-advisor"), portfolio-management-system ("robo productizes portfolio construction for consumers"), financial-advisor-platform ("consumer self-service automated advice vs advisor-operated practice system"), algorithmic-trading-platform ("robo's strategy is the vendor's product; the user is an investor, not a strategy author").

## Research Questions

1. RQ1 — What is the core object model? (investor profile, goal, risk score, model portfolio, managed account, holdings, rebalancing)
2. RQ2 — What exactly happens at onboarding? What does the questionnaire capture, and what does it produce?
3. RQ3 — What does the service do continuously without user action? (rebalancing, dividend reinvestment, tax management)
4. RQ4 — What does the user do after onboarding? (deposits, withdrawals, portfolio changes, monitoring)
5. RQ5 — What account wrappers exist? (taxable, retirement, custodial, education; regional variants)
6. RQ6 — How is the service priced, and how do no-fee models sustain themselves?
7. RQ7 — Where does human help enter a self-service product?
8. RQ8 — Where exactly do the seams run vs brokerage / advisor platform / PMS / retirement planning / PFM / algo trading / retail trading?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers + regional spread:

1. **Betterment** — US pure-play, goal-based philosophy, advice+management, Premium human tier
2. **Wealthfront** — US pure-play, automation-first philosophy, risk-score-driven, planning tools
3. **Schwab Intelligent Portfolios** — brokerage-embedded robo, no-advisory-fee model, deepest public FAQ documentation
4. **Acorns** — micro-investing / spare-change mass-market variant, subscription pricing
5. **Wealthsimple** — Canada, regional check (different registered-account wrappers, tiered AUM fees)

## Sources

Research date: 2026-09-07. All Layer-A observations below come from live fetches of official vendor pages.

- Betterment — https://www.betterment.com/about , https://www.betterment.com/investing (fetched OK)
- Wealthfront — https://support.wealthfront.com/hc/en-us , https://www.wealthfront.com/investing , https://www.wealthfront.com/methodology (fetched OK)
- Charles Schwab — https://www.schwab.com/intelligent-portfolios (fetched OK; includes full FAQ + competitor comparison table)
- Acorns — https://www.acorns.com/ , https://www.acorns.com/invest/ (fetched OK; /investing/ 404'd, root + /invest/ used)
- Wealthsimple — https://www.wealthsimple.com/en-ca/managed-investing (redirected to /en-ca/invest, fetched OK)

Not fetched (recorded as limitation): Betterment pricing page, Wealthfront methodology white papers (research.wealthfront.com PDFs), Acorns support center articles, Wealthsimple help center. Fee percentages for Betterment/Wealthfront/Fidelity Go/E*TRADE are known only via Schwab's comparison table (competitor snapshot dated 12/1/25) — treated as secondhand; no precise fee numbers asserted in the final document.

## Product Observations

### Betterment (Layer A — directly observed)

- Positioning: "Automated investing … all trading, rebalancing, and tax management done for you."
- "We build an investing portfolio around what you want to accomplish, whether that's retirement or simply building wealth." Goal-based philosophy; goal examples: wedding, education, home, wealth building.
- "Expert-managed: our in-house Investing Team regularly monitors, analyzes, and updates portfolios."
- Goal tracker, all-in-one dashboard, retirement planning tools.
- Accounts: individual investing, Traditional/Roth/SEP IRA, 401(k) rollover, Solo 401(k), trust, crypto (managed portfolio of Bitcoin/Ethereum ETFs), Cash Reserve, Checking.
- Premium tier: "1:1 advice from a CFP® along with exclusive benefits, investing options."
- Custom portfolios: "Pick your own stocks and ETFs while we handle the rest."
- Also offers self-directed investing (trade stocks and ETFs) as a separate mode.
- Entity structure (disclosure): advisory = Betterment LLC, SEC-registered investment adviser; "internet-based advisory services are designed to assist clients in achieving discrete financial goals"; brokerage/custody = Betterment Securities + Apex Clearing Corporation; checking via partner bank; 401(k) admin = Betterment for Business.

### Wealthfront (Layer A — directly observed)

- Product name: "Automated Investing Account." "We build and automatically manage a globally diversified portfolio for you in one account, utilizing low-cost index funds."
- Onboarding: "just answer a few questions and we'll build you a diversified portfolio of index funds based on your situation and goals."
- Continuous automation: "Our automation ensures your portfolio stays balanced to your risk level, dividends are reinvested, and everything runs smoothly in the background."
- Composite risk score ranges 0.5–10 (performance disclosures reference "a composite risk score of 9").
- Tax-Loss Harvesting ("in 2012 we pioneered automation with the goal to do just this"); direct indexing for accounts over $100,000 (replaces US-equities ETF with individual stocks + completion ETFs).
- Customization: "change allocation weights and even add, remove and swap ETFs of your choosing. We'll continue to manage your investments for you."
- FAQ topics: setup complexity, choosing own investments, withdrawals, cost, TLH, funding, account transfers, insurance, retirement/education use, ownership types.
- Support-center categories: Investment Accounts, Cash Accounts, Home Lending, Portfolio Line of Credit, Taxes, Financial Planning, Profile & Settings.
- 529 education plan; Portfolio Line of Credit (margin lending against the portfolio).
- Entity structure (disclosure): "Wealthfront Software LLC offers a software-based financial advice engine that delivers automated financial planning tools"; investment management/advisory = Wealthfront Advisers LLC (SEC RIA); cash account = Wealthfront Brokerage LLC (FINRA/SIPC).
- Portfolio families (methodology page): Classic, Socially Responsible, Automated Bond, Automated Bond Ladder, S&P 500 Direct, Nasdaq-100 Direct, 529.
- Positioning: "Managed by us, built for you"; "Managed automatically, so you don't need to talk to anyone."

### Schwab Intelligent Portfolios (Layer A — directly observed; richest operational FAQ)

- "Our robo-advisor builds, monitors, and automatically rebalances a diversified portfolio based on your goals."
- Documented 3-step flow: (1) "Complete a short questionnaire to establish your goals, risk tolerance, and timeline." (2) "Get a diversified portfolio of ETFs chosen by experts." (3) "Our robo-advisor monitors your portfolio daily and automatically rebalances it as needed."
- Portfolio system: more than 80 portfolio variations, drawn from about 50 ETFs spanning about 20 asset classes, 3 investment strategies (Global / US Focused / Income Focused), 6 risk profiles (Conservative → Aggressive Growth).
- Goals served: retirement, college, vacations, building long-term wealth, sustainable income stream.
- Rebalancing mechanics (FAQ): "Your portfolio won't trade every day, however we perform daily check-ins. When an asset class exceeds its allocated portion in your portfolio, the excess ETF shares are sold, and the proceeds are used to buy positions that have fallen below their target percentage; this keeps your portfolio consistent with your Investor Profile." "In a normal environment, rebalancing happens a few times per year." "Portfolio allocations are not adjusted tactically based on short-term views about the markets."
- Tax-loss harvesting: available for taxable portfolios with $50,000+ invested assets, opt-in, automated, wash-sale avoidance; no additional fee.
- Cash allocation: portion of portfolio swept to FDIC-insured deposit accounts at Schwab Bank; interest rate set monthly.
- Revenue model (disclosed): no advisory fee, no commissions; revenue from (a) Schwab ETF management fees (affiliate CSIM), (b) cash deposits at Schwab Bank, (c) order-flow revenue. "Schwab does not charge an advisory fee for the SIP Program in part because of the revenue Schwab Bank generates from the cash allocation."
- ETF selection criteria (FAQ): exclude inverse/leveraged/actively-managed/single-country/very-new ETFs; require sufficient AUM, index tracking consistency, low expense ratios; quarterly monitoring, annual review.
- Accounts: taxable (Individual, Joint Tenant, Tenants in Common, Community Property, Custodial, Revocable Living Trust) + tax-advantaged (Traditional/Roth/Rollover/Inherited/SEP/SIMPLE IRA).
- Enrollment of an existing Schwab account: questionnaire → portfolio recommendation → enroll → existing holdings liquidated → invested within 3–5 days.
- Withdrawals: request transfer anytime; if the amount exceeds the cash allocation, ETFs are sold and funds settle in 4–6 business days; portfolio rebalances after withdrawal; withdrawal below the TLH minimum makes the account TLH-ineligible.
- Minimum: $5,000. 24/7 live support from US-based service professionals. Premium tier adds guidance; Intelligent Income variant targets sustainable income.
- Comparison table (competitor snapshot as of 12/1/25): Betterment Digital 0.25%, Wealthfront 0.25%, Fidelity Go no advisory fee under $25k / 0.35% above, E*TRADE Core Portfolios 0.30%.
- Portfolio management provided by Charles Schwab Investment Management, Inc. (CSIM), a registered investment adviser affiliate — the robo runs on a separate RIA entity over the brokerage relationship.

### Acorns (Layer A — directly observed)

- "Sign up in minutes, we'll recommend an investment portfolio for your money goals, and you can set automated investments starting with spare change."
- Round-Ups®: link credit/debit cards → spare change from every purchase set aside → invested once it reaches at least $5.
- Automatic Recurring Investments ("set your recurring investments… try $5 a day"); Automatic Portfolio Rebalancing ("We'll adjust your Base portfolio as needed to help keep your allocations on track with your long-term money goals"); Automatic Dividend Reinvesting.
- Portfolio recommendation based on "your age, time horizon, income, goals, and risk tolerance."
- Five Core portfolios, ETF-based (documented holdings include VOO, IJH, IJR, IXUS, ISTB, AGG, ESG variants, optional Bitcoin-linked ETF); range "from aggressive (all stocks) to conservative (all bonds)."
- Portfolio switching: "You may switch portfolios after registration without a charge or penalty from Acorns. However, changing portfolios with any investment account may cause a taxable event."
- Custom Portfolios: the Invest portfolio splits into a Base Portfolio (expert-built, the diversified foundation) + Custom Portfolio (user-chosen stocks/ETFs, up to 50% of the total).
- Subscription pricing (monthly plans, minimum $4/mo) instead of AUM fee.
- Accounts: Invest (taxable brokerage), Later (IRA), Early (UGMA/UTMA custodial for kids), Checking & Emergency Savings, Earn (cashback invested).
- Entities: Acorns Advisers LLC (SEC RIA), Acorns Securities LLC (broker-dealer, FINRA/SIPC).
- SIPC protection up to $500,000 on Invest/Later/Early.

### Wealthsimple (Layer A — directly observed; regional check, Canada)

- Managed portfolios: Classic ("low-fee, diversified, and as aggressive (or not) as you need") and Summit (private markets, long-term growth, "zero maintenance").
- Canadian registered-account wrappers: FHSA, RRSP, RRIF, non-registered, RESP, LIRA, spousal RRSP, TFSA.
- Tiered management fees on managed investing accounts by asset level (Core from $1 in assets; Premium at $100k; Generation at $500k, with lower fee rates at higher tiers).
- Advisors available ("Advisors can make sure your money is doing more than enough"); household feature (joint management with a partner); portfolio line of credit (borrow up to 35% of investment value).
- Self-directed trading ($0 commission) also exists alongside managed investing.

## Cross-product Comparison

| Dimension | Betterment | Wealthfront | Schwab IP | Acorns | Wealthsimple |
|---|---|---|---|---|---|
| Delegated managed portfolio | ✓ | ✓ | ✓ | ✓ | ✓ |
| Profile-driven allocation | goals-based | risk score (0.5–10) + situation | goals + risk tolerance + timeline → 80+ variations | age/horizon/income/goals/risk → 5 core portfolios | risk-based Classic/Summit |
| Automated rebalancing | ✓ | ✓ | ✓ (daily check-ins, drift-triggered) | ✓ | ✓ |
| Dividend reinvestment | ✓ ("reinvesting") | ✓ (explicit) | not stated on fetched page | ✓ (explicit) | not stated on fetched page |
| ETF model portfolios | ✓ | ✓ | ✓ (~50 ETFs) | ✓ | ✓ |
| Tax-loss harvesting | ✓ | ✓ (pioneer claim) | ✓ opt-in, $50k+ | not offered on fetched pages | not stated |
| Human help | Premium CFP 1:1 | certified professionals | 24/7 support + Premium | 24/7 support | advisors |
| User customization | custom portfolios | weights + ETF swaps | — | Custom ≤50% + Base | — |
| Self-directed mode alongside | ✓ | — | ✓ (same firm, different product) | — | ✓ |
| Pricing model | AUM % (0.25% per Schwab table) | AUM % (0.25% per Schwab table) | no advisory fee (cash + in-house ETF + order flow revenue) | subscription (min $4/mo) | tiered AUM % |
| Account wrappers | taxable, IRA family, Solo 401k, trust | taxable, IRA, 529 | taxable family, IRA family, custodial, trust | taxable, IRA, UGMA/UTMA | TFSA/RRSP/RRIF/RESP/FHSA/LIRA (CA) |
| Adjacent banking/credit | Cash Reserve, Checking | Cash Account, PLOC, Home Lending | Schwab Bank sweep | Checking, Emergency Savings, Earn | chequing, PLOC |
| Region | US | US | US | US | Canada |

Reading: the delegated managed portfolio + profile-driven allocation + automated maintenance + self-service relationship is present in all five. Everything else varies: fee model (three distinct models observed), TLH (3/5, US-only), human advice depth, customization degree, wrappers (jurisdiction-dependent), adjacent banking.

## Canonical Model

### L0 — Defining Invariant (all five products; remove any one → different Type)

1. **Delegated managed portfolio** — the user's invested money is held in an account whose portfolio the service constructs and maintains. The user does not make per-security buy/sell decisions as the primary mode. Remove → brokerage / retail trading platform.
2. **Profile-driven allocation** — the portfolio is selected from the service's model portfolios by a recorded investor profile (risk tolerance, time horizon, optionally named goals) captured through onboarding. This is the "advice" act, systematized. Remove → a plain fund or a brokerage account.
3. **Automated ongoing maintenance** — the service monitors the portfolio and rebalances it automatically to keep it aligned with the target allocation, without per-action user involvement. Remove → a one-time recommendation tool or self-directed investing.
4. **Self-service consumer relationship** — the user onboards, funds, monitors, and adjusts through the product itself; no human advisor is required to operate the account. Remove → financial advisor platform / wealth management.

### L1 — Common Mature Structure (present in most/all sampled products, not definitional)

- ETF-based diversified model portfolios (low-cost index funds as the dominant implementation vehicle)
- Onboarding questionnaire → recommended portfolio (the universal entry act)
- Automatic dividend reinvestment (explicit in 3/5 fetched pages; not stated for Schwab/Wealthsimple on fetched pages — common, not verified universal)
- Recurring and one-time deposits; withdrawals (with cash-first-then-sell mechanics documented at Schwab)
- Performance/portfolio dashboard
- Multiple account wrappers (taxable + retirement at minimum)
- Human help channel (support chat/phone; premium advice tiers)
- Goal tracking / planning projections (retirement and goal tools)
- Portfolio switching / risk-level adjustment after onboarding
- Transfer-in of existing accounts (401(k) rollover support documented at Betterment/Schwab)

### L2 — Variant / Optional Structure

- Tax-loss harvesting (US taxable accounts; thresholds and opt-in vary; absent in some products)
- Direct indexing (high-balance tiers)
- User customization layers (custom portfolios, ETF swaps, Base+Custom splits)
- Micro-investing / spare-change funding (round-ups)
- Pricing model: AUM % vs subscription vs no-advisory-fee (funded by cash allocation + in-house fund revenue + order flow)
- Cash management / checking / high-yield cash (adjacent banking overlay)
- Portfolio line of credit / margin borrowing against the managed portfolio
- SRI/ESG portfolio families; crypto portfolios; bond ladders; private-markets portfolios
- Education accounts (529 US; RESP Canada); custodial accounts
- Regional registered-account wrappers (IRA/401k US vs TFSA/RRSP/RESP/FHSA Canada)
- Income/decumulation modes (sustainable income stream variants)
- Hybrid human-advice tiers (CFP 1:1, guidance tiers)
- Self-directed trading alongside the managed mode (convergence pattern)

### L3 — Vendor-specific (kept out of the final document)

- Schwab: cash allocation swept to Schwab Bank as disclosed revenue source; ~50-ETF universe; 80+ variations; 6 risk profiles; 3 strategies; $5,000 minimum; TLH $50k+ opt-in; Intelligent Income; enrollment liquidation 3–5 days; withdrawal settlement 4–6 business days; sweep rate set monthly off SWGXX yield.
- Wealthfront: composite risk score 0.5–10; direct indexing $100k+; Portfolio Line of Credit; Home Lending; 529 administered via Nevada program; portfolio family names (Classic, S&P 500 Direct, Nasdaq-100 Direct, Automated Bond Ladder); "pioneered TLH in 2012" claim.
- Betterment: goal-slice structure; two-way IRA/taxable coordination; Premium CFP tier; securities lending; Cash Reserve/Checking via nbkc; Betterment at Work 401(k); concierge rollover support.
- Acorns: Round-Ups® trademark with ≥$5 accumulation threshold; subscription plans (min $4/mo); exactly 5 Core portfolios; Base+Custom 50% cap; Later IRA match promotions; Early kids' debit card ecosystem.
- Wealthsimple: tier names (Core/Premium/Generation) with asset thresholds; Summit private-markets portfolio; household joint management; borrow up to 35% PLOC; Canadian wrapper set.

## Historical / Market-Sample Check

- First-generation robo-advisors (Betterment 2010, Wealthfront 2011, Nutmeg 2011 UK) already embodied questionnaire → model portfolio → automated rebalancing; the definition does not depend on any post-2015 feature.
- Regional: Wealthsimple (Canada) fits the core with entirely different account wrappers — wrappers are variant, not invariant.
- No mobile dependency: all sampled products are web+app; the core loop predates and survives without any specific surface.
- ETF is implementation, not invariant: the model portfolio could in principle be built from other pooled vehicles; the invariant is the managed model portfolio, not its fund type.
- TLH not required: Acorns (no TLH on fetched pages) and Schwab base program (opt-in, threshold) satisfy the core without it.
- Named goals not required: Wealthfront's core account is risk-score-driven; goals appear in planning surfaces. Profile-driven allocation is the invariant; goal framing is common.
- Pre-software analog check: a human advisor's managed model-portfolio account shares delegation + profile-driven allocation, but fails self-service + automated maintenance — correctly excluded (that is the financial advisor / wealth management world). A target-date fund shares delegation + profile-driven (by date) allocation + auto-maintenance, but is a security, not an application — the robo-advisor is the application layer (account, onboarding, funding, monitoring, advice surface) wrapped around managed model portfolios. Both checks sharpen, rather than break, the definition.

## Vendor-specific Findings

See L3 above. Notable structural pattern: in every sampled product the advisory function is performed by a distinct SEC-registered investment adviser entity (Betterment LLC, Wealthfront Advisers, CSIM for Schwab, Acorns Advisers), separate from the broker-dealer/custody entity. This is a regulatory-structure pattern of the US market, not a defining property of the Type.

## Boundary Findings

1. **vs Brokerage Platform**: the seam is decision authority. Self-directed order entry = brokerage; delegated construction+maintenance = robo-advisor. Convergence is real and bidirectional: brokerages embed robos as a mode over the same account (Schwab Intelligent Portfolios, run by affiliate RIA CSIM), and robos add self-directed modes (Betterment self-directed, Wealthsimple trade). The robo mode is consistently operated by a separate registered-adviser entity. Boundary holds: the Type is defined by the managed-service loop, not by the account.
2. **vs Financial Advisor Platform**: consumer self-service vs advisor-operated practice system. Hybrid advice tiers (Betterment Premium, Schwab Premium, Wealthsimple advisors) sit between but do not collapse the boundary — the account remains self-service-operated.
3. **vs Portfolio Management System**: same rebalancing engine concept, opposite side of the market — consumer product vs institutional operator tool; thousands of client portfolios vs the firm's book; user is the investor vs the portfolio manager.
4. **vs Retirement Planning Application**: execution vs projection. Robos embed retirement planners (Betterment retirement tools, Wealthfront planning, Schwab planning calculators) — capability overlap, different object of record (managed portfolio vs household plan). Joint-review note from retirement-planning-application pass discharged here: boundary held structurally.
5. **vs PFM**: investing vs tracking/budgeting; robos' banking overlays (cash, checking) are adjacent, not core.
6. **vs Algorithmic Trading Platform**: vendor-authored strategy consumed by investors vs user-authored strategy operated by traders. Both "automate," but authorship and audience differ.
7. **vs Retail Trading Platform**: delegation vs self-direction; sampled brokerages host managed modes as add-ons while the self-directed loop remains their center.
8. **vs Wealth Management Platform**: automated self-service vs advisor-led comprehensive practice; the robo is the low-touch pole of the advice spectrum.
9. **vs target-date/index funds (non-software)**: a fund is a security; the robo-advisor is the application layer around managed model portfolios (account relationship, onboarding, funding rails, monitoring, advice surfaces). A robo account may hold the very same ETFs a self-directed investor could buy — the difference is the managed service relationship, not the holdings.

"去掉什么就变成另一个 Type" 判据：去掉委托（用户自选）→ Brokerage/Retail Trading；去掉自动化维护（一次性建议）→ 建议工具/顾问平台；去掉自助（人工操作）→ Financial Advisor Platform；去掉 profile 驱动（无建议）→ 普通托管账户。

## Uncertainties

- Exact fee percentages for Betterment/Wealthfront/Fidelity Go/E*TRADE rest on Schwab's competitor snapshot (12/1/25), not on those vendors' own pricing pages — no precise numbers asserted in the final document.
- Wealthfront risk-score→portfolio mapping details live in white papers not fetched; only the 0.5–10 range is directly observed.
- Rebalancing drift thresholds/bands not documented on fetched pages; only Schwab's qualitative mechanics ("exceeds its allocated portion", "a few times per year" normally) are observed.
- Dividend reinvestment verified explicit at Betterment/Wealthfront/Acorns; not stated on fetched Schwab/Wealthsimple pages — treated as common, not universal.
- Minimums observed: Schwab $5,000; Wealthfront "as little as $500"; Acorns spare-change entry. Betterment minimum not observed. Written qualitatively.
- Withdrawal mechanics detailed only at Schwab (cash-first, then sell, 4–6 business days); generalized cautiously.
- Acorns support-center articles and Wealthsimple help center not fetched; Acorns observations rest on marketing+FAQ pages (still product-official, Layer A for what they state).

## Final Synthesis

A Robo-advisor is a consumer investing application in which the service, not the user, constructs and continuously maintains a diversified portfolio in the user's account. The defining loop: onboarding captures an investor profile (risk tolerance, horizon, optionally goals) → the service maps it to one of its model portfolios → the user funds the account → the service automatically maintains the portfolio (rebalancing, dividend reinvestment, optionally tax management) → the user deposits, withdraws, monitors, and adjusts the profile/portfolio over time. The user's decisions are delegated at the portfolio level; the service's decisions are systematized at the profile level. Everything else — ETF implementation, tax-loss harvesting, goal tooling, human advice tiers, banking overlays, pricing model, account wrappers, customization layers — is common mature structure or variant, not definition. The Type sits at the low-touch pole of the advice spectrum, between self-directed trading (user decides) and advisor-led wealth management (human decides), and is increasingly offered as a mode inside brokerage ecosystems while remaining structurally distinct from them.
