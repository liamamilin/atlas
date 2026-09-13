# Robo-advisor

## Overview

A **Robo-advisor** is a consumer investing application in which the service — not the user — constructs and continuously maintains a diversified investment portfolio in the user's account. The user records an investor profile (risk tolerance, time horizon, and often named goals), the service maps that profile to one of its model portfolios, the user funds the account, and the service then keeps the portfolio aligned automatically. The user's decisions are delegated at the portfolio level; the service's decisions are systematized at the profile level.

The defining core is small:

```text
Investor profile (captured at onboarding)
└── Model portfolio selected by the service
    └── Managed account funded by the user
        └── Automated ongoing maintenance (rebalancing)
```

Everything else commonly associated with the category — ETF portfolios, tax-loss harvesting, goal trackers, human advice tiers, cash accounts, spare-change investing — is widespread but not what makes the product a robo-advisor. The Type occupies the low-touch pole of the advice spectrum: between self-directed trading (the user decides every trade) and advisor-led wealth management (a human decides for the client).

## Users & Context

The primary user is an individual investor who wants their money invested and kept on track without making investment decisions themselves — first-time investors, savers converting cash into long-term investments, retirement savers rolling over employer plans, and hands-off index investors.

Typical reasons to open the application:

- start investing without learning to pick securities
- put savings on an automated, diversified long-term track
- consolidate a 401(k) or IRA rollover into a managed portfolio
- save toward a named goal (retirement, a home, education, wealth building)
- keep an existing portfolio balanced without doing the rebalancing trades

The relationship is self-service by design: the user onboards, funds, monitors, and adjusts through the product. Human help exists in most products — support channels for everyone, and premium advice tiers for those who want it — but no human operator is required for the account to function. The work environment is web and mobile apps; the account sits at a custodian, and the advisory function is typically performed by a registered investment adviser entity separate from the brokerage/custody entity.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product stops being a robo-advisor:

- **Delegated managed portfolio** — the user's invested money is held in an account whose portfolio the service constructs and maintains. The user does not make per-security buy/sell decisions as the primary mode. Without this, the product is a brokerage or trading platform.
- **Profile-driven allocation** — the portfolio is selected from the service's model portfolios based on a recorded investor profile: risk tolerance, time horizon, and often goals, income, or age. This is the "advice" act, systematized into software. Without it, the product is a plain fund or an account without advice.
- **Automated ongoing maintenance** — the service monitors the portfolio and rebalances it automatically to keep it aligned with the target allocation, without per-action user involvement. Without it, the product is a one-time recommendation tool.
- **Self-service consumer relationship** — the user operates the account through the product itself. Without it, the product is an advisor-operated practice system.

### Standard Capabilities

Mature products carry most of the following. They make the robo-advisor practical; they do not define it.

- **Model portfolio system** — a curated set of diversified portfolios spanning a risk spectrum (conservative to aggressive), typically built from low-cost index ETFs across stocks, bonds, and cash. The service's investment team maintains the underlying fund selection and allocation models.
- **Onboarding questionnaire** — the entry act that captures the investor profile and produces a portfolio recommendation.
- **Automatic dividend reinvestment** — payouts are reinvested rather than held as cash (explicit in several sampled products; not verified in all).
- **Deposits and withdrawals** — one-time and recurring contributions (scheduled transfers, and in some products spare-change round-ups), plus withdrawals on request.
- **Portfolio dashboard** — current holdings, allocation vs. target, performance over time, account value.
- **Multiple account wrappers** — taxable accounts plus retirement accounts (IRAs and rollovers in the US; registered accounts such as RRSP/TFSA/RESP in Canada), often custodial, trust, and education accounts.
- **Portfolio adjustment** — the user can change risk level or switch portfolios after onboarding, typically without penalty from the service (though it may trigger a taxable event).
- **Human help channel** — support chat/phone for all users; premium tiers add access to human advisors or planners.
- **Planning and projection tools** — retirement and goal projections layered on top of the managed account.
- **Account transfer-in** — support for rolling over or transferring existing accounts into the managed program.

### One Structure, Many Implementations

The core model is conceptual. Implementations vary:

```text
Concept:            Investor profile
Implementations:    risk questionnaire, composite risk score, goal-based slices,
                    age/horizon/income inputs

Concept:            Model portfolio
Implementations:    ETF baskets, index-fund allocations, ESG variants,
                    bond ladders, direct-indexing stock sleeves

Concept:            Funding
Implementations:    bank transfers, recurring schedules, round-ups of spare change,
                    rollovers and in-kind transfers

Concept:            Pricing
Implementations:    percentage-of-assets fee, flat subscription,
                    no advisory fee funded by cash allocation and in-house funds
```

## How It Works

### Onboard: profile → recommendation

```text
Create account
→ complete the questionnaire (goals, risk tolerance, time horizon, situation)
→ service recommends a model portfolio
→ review the proposed allocation
→ accept and open the managed account
```

The questionnaire is the advice engine's input. Answers map to a portfolio on the service's risk spectrum; the recommendation is presented with its target allocation before the user commits.

### Fund: money enters the managed account

```text
Link a bank / set a funding source
→ make an initial deposit (or set up recurring deposits)
→ service invests the cash into the target portfolio
→ optionally transfer in existing accounts (rollover, ACAT-style transfer)
```

Some products invest deposits immediately; others batch. Transfers of existing accounts follow the custody system's transfer mechanics.

### Maintain: the service keeps the portfolio on target

```text
Markets move, contributions arrive, dividends pay out
→ service monitors the portfolio continuously
→ when allocations drift from target, it rebalances automatically
→ dividends are reinvested
→ where offered, tax-management trades run in the background
```

This is the loop that distinguishes the Type: maintenance happens without the user requesting it. Rebalancing is systematic — restoring target weights when allocations drift — not tactical market timing. The service's investment team maintains the model portfolios and fund selection at the program level; individual client portfolios are managed by the automation.

### Adjust and monitor: the user's ongoing role

```text
Deposit more / schedule contributions
→ watch performance on the dashboard
→ change risk level or switch portfolio (if circumstances change)
→ withdraw funds when needed
→ update profile information over time
```

Withdrawals are requested through the product. Where the account holds a cash portion, a withdrawal exceeding it may require selling holdings and waiting for settlement (mechanics documented in detail by one sampled product; others were not verified on this pass). After a withdrawal the portfolio is rebalanced back to target.

### Core vs Common vs Optional

**Defining core** — without these, not a robo-advisor:

- delegated managed portfolio
- profile-driven allocation
- automated ongoing maintenance (rebalancing)
- self-service consumer relationship

**Standard capabilities** — present in most mature products:

- model portfolio system, onboarding questionnaire, dividend reinvestment
- deposits/withdrawals, dashboard, multiple account wrappers
- portfolio adjustment, human help channel, planning tools, transfer-in

**Common variants / optional** — depends on market, segment, jurisdiction:

- tax-loss harvesting (taxable accounts; thresholds and opt-in vary; jurisdiction-dependent)
- direct indexing at high balances
- user customization (custom portfolios, ETF swaps)
- spare-change micro-investing
- cash management / checking overlays; portfolio lines of credit
- ESG/SRI, crypto, bond-ladder, private-markets portfolio families
- income/decumulation modes
- hybrid human-advice tiers
- self-directed trading alongside the managed mode

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Onboarding questionnaire

The advice engine's front door. A guided flow collecting goals, risk tolerance, time horizon, and financial situation; ends in a recommended portfolio with its target allocation shown before commitment.

### Portfolio dashboard

The primary ongoing surface.

- current account value, holdings, allocation vs. target
- performance over time, contributions, earnings
- primary actions: deposit, withdraw, view details

### Goal / planning views

Projections tying the managed portfolio to named goals (retirement, education, a purchase); typically show progress and projected outcomes under assumptions.

### Account management

Account wrappers, beneficiaries, statements and tax documents, transfer/rollover initiation, profile settings.

### Funding / transfers

Bank-linking, recurring contribution schedules, round-up configuration where offered, withdrawal requests.

### Support / advice access

Chat and phone support; in premium tiers, scheduling or messaging with human advisors or planners.

## Important Rules / Behaviors

### The user delegates, the service executes

The structural rule of the Type: the user does not place individual trades in the managed mode. Buy/sell decisions inside the portfolio are made by the service's automation within the chosen model. Customization features (where offered) let users shape the portfolio, but the service continues to manage and rebalance it.

### Rebalancing is systematic, not tactical

The automation restores target allocations when they drift; it does not reposition the portfolio based on short-term market views. Model-portfolio changes come from the service's investment team at the program level, not per-client.

### Portfolio changes can be taxable events

Switching portfolios or receiving certain service-driven trades in a taxable account may realize gains or losses. Products flag this; tax-management features exist precisely to manage it, and are typically limited to taxable accounts, often with balance thresholds and opt-in.

### Withdrawals interact with the portfolio

Withdrawals are requested through the product and can interact with the managed portfolio: where the account holds a cash portion, a withdrawal larger than that portion may require selling holdings, which introduces a settlement wait (documented in detail by one sampled product; timing varies). Afterwards the portfolio is rebalanced back to target — a direct consequence of automated maintenance. Withdrawals can also affect eligibility for optional features (for example, dropping below a feature's balance threshold).

### Suitability gates the recommendation

The recommendation is produced from the recorded profile; products treat the questionnaire as the basis of their advisory duty. Changing answers changes the recommendation. The service manages to the profile on record — keeping it current is part of the user's role.

### Fees attach to the relationship, not to trades

Whatever the pricing model (assets-based, subscription, or no-advisory-fee), the user does not pay per-trade commissions in the managed mode; underlying fund expenses still apply, and no-fee models are funded through other revenue (cash allocations, in-house funds, order flow) that products disclose.

## Variants

- **Pure-play goal-based** — the account is organized around named goals, each a managed slice (wedding, home, retirement).
- **Pure-play automation-first** — a single managed account driven by a risk score, with planning tools alongside.
- **Brokerage-embedded** — the robo as a program inside a larger brokerage, often over the same account relationship, operated by an affiliated adviser entity; sometimes with no advisory fee funded by cash allocation and in-house funds.
- **Micro-investing** — spare-change round-ups and very small recurring amounts as the funding model; subscription pricing; mass-market onboarding.
- **Regional registered-wrapper variants** — the same core loop wrapped in jurisdiction-specific tax-advantaged accounts (IRAs/401(k)s in the US; RRSP/TFSA/RESP/FHSA in Canada).
- **Hybrid advice tiers** — the self-service core plus human advisors at premium tiers.
- **Income/decumulation variants** — programs tuned for drawing sustainable income rather than accumulating.
- **Convergence variants** — robos adding self-directed trading, and brokerages adding managed modes; the two Types increasingly coexist inside one brand while remaining structurally distinct.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Brokerage Platform | user places self-directed orders; the robo-advisor's defining property is that the service decides and maintains. Convergence: brokerages embed robos as a mode; robos add self-directed modes |
| Retail Trading Platform | self-directed decisions by the individual; delegation of decisions is the robo's edge |
| Financial Advisor Platform | advisor-operated practice system; the robo-advisor is consumer self-service. Hybrid advice tiers sit between |
| Wealth Management Platform | advisor-led comprehensive management; the robo-advisor is the low-touch, automated pole of the same spectrum |
| Portfolio Management System | institutional operator tool for human-run portfolios; similar rebalancing engine, opposite user and object population |
| Retirement Planning Application | projection and sufficiency planning without execution; robos embed planners as a capability, but their object of record is the managed portfolio |
| Personal Finance Management Application | tracking and budgeting of what is; no managed portfolio or execution |
| Algorithmic Trading Platform | user-authored strategy executed for a trader; the robo's strategy is the vendor's product consumed by an investor |
| Target-date / index funds (non-software) | a fund is a security; the robo-advisor is the application layer — account, onboarding, funding, monitoring, advice surfaces — wrapped around managed model portfolios |

The most important boundary is with the Brokerage Platform, because the two converge in the market: the structural test is decision authority — who constructs and maintains the portfolio. The second is with the Financial Advisor Platform: whether a human operates the relationship or the user self-serves.

## Representative Products

- Betterment — pure-play, goal-based, US
- Wealthfront — pure-play, automation-first, US
- Schwab Intelligent Portfolios — brokerage-embedded, no-advisory-fee model, US
- Acorns — micro-investing / spare-change, subscription pricing, US
- Wealthsimple — managed investing in Canada (regional check: different registered-account wrappers, tiered fees)

The core model was checked against the first generation of robo-advisors (which already embodied questionnaire → model portfolio → automated rebalancing) and against a non-US sample, so the definition does not depend on any single era, region, or feature set.

## Sources

Research date: **2026-09-07**

- Betterment — https://www.betterment.com/about , https://www.betterment.com/investing
- Wealthfront — https://www.wealthfront.com/investing , https://www.wealthfront.com/methodology , https://support.wealthfront.com/hc/en-us
- Charles Schwab — https://www.schwab.com/intelligent-portfolios (program page with operational FAQ)
- Acorns — https://www.acorns.com/ , https://www.acorns.com/invest/
- Wealthsimple — https://www.wealthsimple.com/en-ca/invest

> Sourcing limitation: vendor pricing pages, methodology white papers, and some help-center articles were not fetched. Fee percentages for non-Schwab products are known only through a competitor's published comparison table, so this document states fee models qualitatively (assets-based / subscription / no-advisory-fee) without asserting specific rates. Rebalancing trigger thresholds and per-product minimums are likewise described qualitatively; where a mechanic is documented for one product only (e.g., withdrawal settlement timing), it is not generalized.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
