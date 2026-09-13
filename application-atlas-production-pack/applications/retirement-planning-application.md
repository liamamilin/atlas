# Retirement Planning Application

## Overview

A **Retirement Planning Application** is a personal financial projection application. It holds a household's finances as a persistent **plan**, projects that plan year-by-year from today through retirement and onward to an end-of-life horizon, and evaluates whether projected resources will cover projected needs — answering the question *"will the money last, and what can I change to improve the answer?"*

The defining structure is small:

```text
Household plan (anchored to a retirement point in time)
└── Projection across the accumulation → decumulation transition
    └── Sufficiency evaluation ("am I on track?")
```

Everything else commonly associated with these products — Monte Carlo simulation, linked accounts, Social Security explorers, tax-optimization tooling, advisor dashboards — is widespread in current products but is not part of what makes the product a retirement planner. Older spreadsheet-based planners, non-US products built around different pension systems, and advisor-operated planning platforms all satisfy the same core without any of those specifics.

## Users & Context

**Primary users** are individuals and couples planning their own retirement. They span a wide age range:

- early- and mid-career savers deciding how much to save and when financial independence or early retirement becomes possible
- pre-retirees approaching the end of their working years, making the consequential decisions: when to retire, when to claim government benefits, how to convert savings into income
- recent retirees managing withdrawals and annual spending against their remaining horizon

**Secondary users** are financial advisors, coaches, and planners who operate plans on a client's behalf — some products are packaged specifically for this tier, with client rosters and permissioned access. Many consumer products also wrap the planning engine in a human support layer (coaching, classes, advisor referral).

Typical sessions are *reflective and decision-driven* rather than transactional: a user opens the product when a major question arises (retire at 60 or 65? downsize the house? take a part-time job?) or for periodic maintenance after a life change (raise, inheritance, market downturn, new dependent). There is nothing to buy, trade, or file inside the planner itself; the output of a session is a better-understood decision, which the user then executes elsewhere.

## Core Model

### The Defining Core

**The plan** is the central artifact: a persistent, editable model of one household's financial life. It is not a form filled once — it lives across years and is updated as circumstances change. A plan contains four families of content:

1. **Household profile** — the people (individual or couple), their current ages, the intended **retirement point** (an age or date), and a **longevity assumption** (an end-of-life age the plan must survive to). These three anchors — today, retirement, end of life — define the plan's horizon and split it into two phases: **accumulation** (working years: saving and growing) and **decumulation** (retirement years: drawing down). The transition between them is the axis the entire Application Type is organized around.

2. **Resources** — what the household has and will receive:
   - *assets and accounts*: investment and retirement accounts, cash, real estate — mature products commonly organize them by **tax treatment**, because the tax character of each bucket constrains how it can later be used
   - *debts*: mortgages and other liabilities
   - *income streams*: employment income now, and pensions, government retirement benefits, annuities, rental income, or windfalls later

3. **Needs** — what the household will spend: recurring living expenses (inflation-adjusted over a multi-decade horizon), healthcare, and one-time goals or life events — a home purchase, college costs, a relocation, a travel sabbatical.

4. **Assumptions** — the futures the projection runs under: investment returns, inflation, and how long the money must last.

**The projection engine** turns the plan into a year-by-year trajectory: for each year from today to the longevity age, it computes balances, income, expenses, contributions or withdrawals, and — in deeper products — taxes. During accumulation the trajectory generally rises through saving; at retirement it inverts as withdrawals plus benefit income cover spending.

**The sufficiency evaluation** compares the trajectory against the household's needs across the whole horizon and renders a verdict — commonly expressed as a **chance of success** (a probability, derived by running the plan against many simulated market futures) or a **readiness estimate**. Some products also surface the derived number the verdict implies: a *safe annual spending* level the plan can sustain in retirement.

**Scenarios** are alternate versions of the plan. A user duplicates the plan, changes one or a few levers (retire two years later, spend more, weather a downturn), and compares outcomes side by side. Scenario exploration — not just reading the single verdict — is where most planning value is realized.

### Standard Capabilities

Capabilities shared by mature products (what makes the core practical, without defining the Type):

- **Account and asset inventory** with per-account balances, growth settings, and commonly tax-bucket grouping
- **Income stream modeling** — employment income through a chosen retirement date; later-life income from benefits, pensions, annuities, rentals
- **Expense and goal modeling** — recurring spending, healthcare, dated one-time events on a life timeline
- **Government benefit estimation** — in the US, Social Security benefit estimates and claiming-age choices; equivalent national systems elsewhere
- **Withdrawal / decumulation setup** — specifying how accounts are drawn to cover retirement spending
- **What-if scenarios** with side-by-side comparison
- **Progress tracking** — journaling actual balances and comparing them against the projection

### One Structure, Many Implementations

The core model is conceptual. Realizations differ:

```text
Concept:              Sufficiency verdict
Realizations:         Monte Carlo probability of success, readiness score, funded-status gauge

Concept:              Government retirement benefit
Realizations:         Social Security estimation (US), national pension presets (other countries)

Concept:              Tax-aware account buckets
Realizations:         taxable / tax-deferred / tax-free groupings, country-specific account types

Concept:              Uncertainty
Realizations:         simulated market scenarios, historical return sequences, fixed conservative assumptions
```

A reader who has only seen one realization (say, a US Monte Carlo planner) should still recognize a spreadsheet-era planner or a country-specific planner from the core model alone.

## How It Works

### 1. Build the plan

```text
Enter or link accounts and assets
→ add income sources (now and expected in retirement)
→ add recurring expenses, healthcare costs, and dated goals/life events
→ set the retirement point, the longevity assumption, and market/inflation assumptions
→ the plan becomes a complete, persistent model of the household's future
```

Some products pull account balances automatically through account aggregation; others are built deliberately on manual entry. The plan works either way — completeness matters more than the plumbing.

### 2. Run the projection and read the verdict

```text
Run projection
→ year-by-year trajectory of net worth, income, spending (and often taxes)
→ sufficiency verdict: probability of success / readiness estimate
→ shortfalls, if any, show where and when the plan breaks
```

### 3. Explore what-if scenarios

```text
Duplicate the plan
→ change levers: retirement age, spending level, savings rate, one-time events
→ compare the scenarios' trajectories and verdicts side by side
→ keep the variant that reflects the life the household actually wants
```

### 4. Test decisions before making them

Mature products provide targeted tools for the highest-impact retirement decisions:

- **when to claim government benefits** — comparing claiming ages in terms of lifetime benefit
- **how to convert savings into retirement income** — withdrawal setup, safe-spending guidance, drawdown ordering across accounts
- **how to reduce lifetime taxes** — in deeper products, exploring strategies such as converting between tax buckets in low-income years, or timing asset sales

### 5. Maintain the plan

```text
Life changes → update the plan
→ projection and verdict recompute
→ actual balances can be journaled against the projection over time
→ the plan remains a living artifact, not a one-time calculation
```

### Capability tiers

- **Defining core** — household plan anchored to a retirement point; multi-decade projection across accumulation into decumulation; sufficiency evaluation; scenario exploration.
- **Standard capabilities** — account/income/expense/goal modeling, benefit estimation, withdrawal setup, progress tracking, side-by-side scenario comparison.
- **Optional / variant** — Monte Carlo or historical simulation, tax-optimization machinery, estate/legacy estimation, advisor-facing packaging, AI assistance, education content, regional benefit systems.

## Interfaces

Described conceptually; names and layouts vary by product.

### Dashboard

The user's entry surface and the home of the verdict.

- typical information: sufficiency verdict, net-worth trajectory, savings rate, current vs projected tax position, data-completeness signals
- primary actions: review standing, jump into the plan editor, open scenarios

### Plan editor

Where the plan is built and maintained, usually organized by category.

- typical information: accounts and assets, income streams, expenses and goals, profile ages and assumptions — one editing surface per category
- primary actions: add/edit/remove entries, link accounts or enter balances, set dates and amounts

### Projection view

The visualization of the future.

- typical information: net worth over time, income vs expenses, often a per-year drill-down showing taxes, cash flow, and withdrawals for a single simulated year
- primary actions: inspect a year, toggle phase views, examine shortfall points

### Scenario comparison

- typical information: parallel trajectories and verdicts for each scenario, with the differing levers highlighted
- primary actions: create a scenario from the plan, adjust levers, compare, promote a scenario to the working plan

### Decision explorers

Targeted surfaces for claiming, conversion, withdrawal, and safe-spending decisions.

- typical information: the decision's options and each option's effect on the plan's long-run outcome
- primary actions: adjust the choice, apply it to the plan

### Progress view

- typical information: actual balances and cash flow over time, plotted against the original projection
- primary actions: update balances, journal notes, review drift from plan

## Important Rules / Behaviors

### The verdict is assumption-dependent

The sufficiency number is only as good as its assumptions. Small changes in return, inflation, or longevity assumptions can swing the outcome materially; this is why uncertainty-aware products run many market futures instead of one, and why the verdict is a probability or an estimate rather than a promise. A high verdict is confidence, not a guarantee; a low verdict is a signal about where to focus, not a failure.

### Tax location shapes decumulation

Assets sitting in differently taxed buckets are not interchangeable at withdrawal time. The order and manner of drawing them changes the household's tax bill, which is why mature products track bucket composition and offer withdrawal/conversion tooling. This makes the tax character of money a structural dimension of the plan, not a cosmetic detail.

### Statutory rules constrain timing

Government benefit claiming and access to retirement-account money are governed by rules in the household's jurisdiction; products encode these rules so that projections and decision tools respect them. Which rules apply, and their specifics, vary by country — the planning logic is general, the statutory layer is regional.

### Data completeness drives plan quality

An unentered account or an ignored expense silently degrades the verdict. Products commonly surface plan-completeness signals and prompt the user to fill gaps; a plan is only as honest as its inputs.

### Scenarios protect the base plan

Experimentation is done on copies. The user's working plan is not overwritten by what-if exploration; a scenario is promoted deliberately if the household adopts it.

### The plan is living

Projections made once go stale as balances, incomes, and lives change. The recurring maintenance loop — update, re-project, compare against reality — is the behavioral heart of the Type, and products actively cultivate it.

## Variants

- **Standalone dedicated planners** — the plan is the whole product (consumer-first specialists, deep planning depth).
- **Ecosystem-embedded planners** — a planning module inside a personal-finance, brokerage, or wealth platform, fed by linked accounts and flanked by budgeting, net-worth, and portfolio tools; a common path is free planner → managed-money upsell.
- **Advisor-facing planning platforms** — the same engine packaged for professionals: client rosters, invite-and-permission control over client plans, advisor dashboards, asset-under-advisement reporting.
- **Simulation philosophies** — Monte Carlo market simulation, historical-sequence backtesting, deterministic fixed assumptions; many products combine several.
- **Data posture** — aggregation-linked (balances auto-refresh) versus manual-entry products, some of which treat "no account linking" as a privacy philosophy.
- **Depth poles** — free one-shot retirement calculators (the degenerate entry form: one projection pass, no persistent plan or maintenance loop) at one end; deep tax-optimized, per-year-detailed planners at the other.
- **Regional regimes** — US-centric products built around Social Security and domestic tax buckets; internationally oriented products shipping country tax presets and account types; region-dedicated planners built around a single national pension system.
- **Audience emphasis** — near-retiree deep planning versus early-career / financial-independence planning built on milestones (defining one's own independence number, multi-phase retirement, sabbaticals).
- **Optional extensions** — estate/legacy value estimation, education libraries and classes, human coaching and advisor referral, AI assistants that answer questions against the plan's data.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Personal Finance Management Application | adjacent, frequently merged | PFM's artifact is the **present**: accounts, budgets, transactions. Remove the future projection and sufficiency verdict and the product becomes PFM. Ecosystems often ship both; the planner remains the projection artifact. |
| Robo-advisor | adjacent, capability overlap | A robo-advisor's object is the **managed portfolio** (construction, rebalancing, execution). Retirement projections inside it are a capability of this Type. Remove portfolio management and trade execution → this Type. |
| Wealth Management Platform / Financial Advisor Platform | container / channel | Advisor practice systems span portfolios, reporting, and client communication; the plan-projection module within them is this Type. Advisor-facing planning platforms are this Type packaged for professionals. |
| Pension Administration Platform | different subject | Pension administration keeps **institutional** scheme and member records on the employer/scheme side. The retirement planner models the household's own future. Different user, different objects, different rules. |
| Budgeting Application | different horizon | Budgeting controls near-term cash flow; the planner projects decades. Budget numbers may feed the plan, but the artifacts are distinct. |
| Tax Preparation Application | different time direction | Tax preparation files **past-year** returns; the planner projects forward-looking lifetime tax surfaces. Only the projection machinery overlaps. |
| Estate Planning Application | different artifact | Estate planning produces legal instruments (wills, trusts). A retirement planner may *estimate* the value of the estate as a projection output, but produces no instruments. |
| Financial Modeling Application (FP&A) | name collision only | FP&A models **organizations**; this Type models a household. No real-world confusion. |

The most important boundary is with Personal Finance Management: the two are commercially intertwined, yet structurally separable — one tracks what *is*, the other projects what *will be*. The second-most important is with the robo-advisor: planning without managing, managing without planning, and the recurring pattern of one embedded inside the other.

## Representative Products

- **Boldin** (formerly NewRetirement) — consumer-first dedicated retirement planner; plan-and-scenario loop with Monte Carlo verdicts, benefit-claiming and conversion explorers, safe-spending guidance
- **ProjectionLab** — simulation-first planner with a manual-entry (no-linking) philosophy, historical backtesting alongside Monte Carlo, international tax presets, and an advisor tier
- **Empower (Retirement Planner)** — a planning tool embedded in a personal-finance/wealth ecosystem, fed by account aggregation, with advisory escalation

The core model was checked against non-embedded realizations (spreadsheet-era and spreadsheet-style planners), advisor-operated planning, and internationally oriented products to avoid over-fitting the definition to the current US consumer Monte Carlo pattern.

## Sources

Research date: **2026-09-07**

- Boldin Help Center — https://help.boldin.com/ (including "What It Is, How You Use It, How It Helps You" and "See Where You Stand with Boldin")
- ProjectionLab — https://projectionlab.com/ and https://projectionlab.com/advisors
- Empower — Retirement Planner — https://www.empower.com/tools/retirement-planner

> Sourcing limitation: operational help documentation for Empower's planner, and the planning surfaces of Fidelity, Pralana, and RightCapital, could not be fetched from the research environment on 2026-09-07. Claims about those products are limited to what their reachable official pages state; no mechanics were inferred for them. Simulation-method claims in this document are drawn from products whose documentation was directly reachable.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
