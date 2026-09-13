# Research Notes — Retirement Planning Application

Research date: **2026-09-07**
Methodology: v1.1 (update-v1)

## Research Goal

Understand what a Retirement Planning Application actually is as an Application Type: what objects exist inside it, what users do with them, how the planning loop works, and where its boundary lies against adjacent financial types (PFM, robo-advisor, pension administration, calculators, advisor platforms).

## Initial Boundary Hypothesis

- Core purpose: model a person's/household's finances from today through retirement and evaluate whether resources will last.
- Likely users: individuals/households planning their own retirement; secondary: advisors using planning tools for clients.
- Nearest neighbors: Robo-advisor, Wealth Management Platform, Financial Advisor Platform, Personal Finance Management Application, Budgeting Application, Pension Administration Platform, Net Worth Tracker, Tax Preparation Application, Estate Planning Application.
- Suspected confusion: (1) consumer retirement *calculators* (one-shot) vs persistent planning applications; (2) advisor-facing planning platforms vs consumer self-service planners; (3) the fact that many realizations are embedded modules of PFM/brokerage/robo ecosystems.
- Unknowns: exact shape of the plan object, projection mechanics (deterministic vs Monte Carlo), decumulation tooling depth, regional breadth.

## Research Questions

1. RQ1 — What is the central artifact (the "plan") and what does it contain?
2. RQ2 — What inputs does the user configure (household profile, accounts, income streams, expenses, assumptions)?
3. RQ3 — How does the projection engine work (deterministic vs Monte Carlo vs historical backtesting; horizons; accumulation → decumulation)?
4. RQ4 — What outputs does the system produce (sufficiency verdicts, trajectories, per-year detail)?
5. RQ5 — How do scenarios / what-if exploration work?
6. RQ6 — How are decumulation, government benefits, and taxes modeled?
7. RQ7 — How do consumer self-service and advisor-facing tiers differ?
8. RQ8 — What are the boundaries vs robo-advisor / PFM / pension admin / one-shot calculators?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| Boldin (formerly NewRetirement) | consumer-first dedicated retirement planner; plan-centric, US-centric | deepest consumer planning loop; rich official help center (Tier 1) |
| ProjectionLab | modern indie planner; simulation-first, manual-entry, FIRE audience + advisor Pro tier | different philosophy (no account linking); international presets; advisor packaging |
| Empower — Retirement Planner | planning tool embedded in a PFM/wealth-management ecosystem; aggregation-based | embedded realization of the Type; different customer funnel (free tool → advisory) |

Attempted but unreachable: Fidelity (retirement planning pages — 403 on two URLs), Pralana Consulting (timeout), RightCapital support (transport error). Fallback tier-4 evidence (advisor-facing planning) obtained from ProjectionLab's advisor product page.

## Sources

Fetched 2026-09-07:

- Boldin Help Center home — https://help.boldin.com/ (Tier 1: collection taxonomy)
- Boldin — "What It Is, How You Use It, How It Helps You" — https://help.boldin.com/en/articles/15312417 (Tier 1)
- Boldin — "See Where You Stand with Boldin" — https://help.boldin.com/en/articles/15312392 (Tier 1)
- ProjectionLab — product homepage — https://projectionlab.com/ (Tier 2)
- ProjectionLab — Advisors page — https://projectionlab.com/advisors (Tier 2)
- Empower — Retirement Planner product page — https://www.empower.com/tools/retirement-planner (Tier 2)
- Empower — site root /planning nav confirming tool set — https://www.empower.com/planning (Tier 2)

Unreachable / abandoned (fail-fast rule):

- https://docs.projectionlab.com/ — transport error (1 attempt); help center not separately fetched
- https://www.fidelity.com/retirement/planning and /calculators-tools/retirement-planning-calculator — 403 (2 attempts)
- https://www.pralanaconsulting.com/ — timeout (1 attempt)
- https://support.rightcapital.com/ — transport error (1 attempt)

Evidence layers used below: **A** = directly observed on an official source of a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### Boldin (formerly NewRetirement) — Evidence A (Tier 1 help center)

Self-positioning: "an all-in-one financial planning platform built for people who are serious about their financial wellness… like a fitness platform, but for your financial life"; "not a one-time calculation. A lifelong habit."

Key observations:

- **Plan as central artifact.** User "enters your data… builds a plan": accounts and assets (entered *or linked*), income sources, expected expenses, retirement goals. A "digital coach tracks your plan accuracy and tells you exactly what to add next" — data-completeness is a first-class concern.
- **Projection engine.** "Runs thousands of market scenarios to calculate your retirement chance of success — the likelihood that your plan funds your goals all the way through your lifetime. It projects your net worth, your income, your tax bill, and your estate value, year by year, all the way to your longevity age. And it updates in real time as your life changes."
- **Sufficiency verdict.** "Retirement Chance of Success" — Monte-Carlo-derived; vendor guidance: "we consider 80% or higher strong… it's a signal, not a verdict."
- **What-if scenarios.** "Scenarios let you duplicate your plan and model 'what ifs' — retiring earlier, spending more, weathering a market downturn — and compare outcomes side by side." Scenario collection: "Create and compare up to 10 scenarios in PlannerPlus" (plan-tier dependent).
- **Input domains (help-center collections).** Accounts and Assets (enter and link — 55 articles), Home and Real Estate (primary residence, relocations), Expenses (recurring and healthcare), Income (work, real-estate rental, annuities, pensions, windfalls), Social Security (benefit estimation), Debts, Money Flows ("move money around in your plan"), Roth Conversions.
- **Decision explorers.** Social Security Explorer ("find the claiming strategy that maximizes your lifetime benefit"); Roth Conversion Explorer ("when and how much to convert to reduce your lifetime tax bill"); Spending Guardrails ("how much you can safely spend each year [in retirement] without running your plan dry").
- **Tax layer.** Tax allocation (assets across taxable / tax-deferred / tax-free accounts); lifetime taxes ("total you're projected to pay across your lifetime"); current vs projected-retirement tax-rate comparison; savings rate as a readiness lever.
- **Readout surfaces.** Chance of success, safe spending target, net worth, tax allocation, lifetime taxes, tax rate, savings rate — framed as a dashboard of numbers that "tell a story."
- **Human + AI support.** Boldin AI (answers questions against plan data); educational library; live classes; community; paid coaching; referral to fee-only financial advisors.
- **Living plan posture.** "Your plan is a living document… update your data as your life changes."

### ProjectionLab — Evidence A (Tier 2 product pages)

Self-positioning: "Build Financial Plans You Love — simulate your financial future"; "more than a retirement calculator"; created with strong FIRE (financial independence) orientation; "You are not the product."

Key observations:

- **Plan/simulation model.** "Build a living model of your whole life's finances and discover the spectrum of possible outcomes." Milestones ("define the milestones that matter… your personal definition of financial independence and when you would like to retire"), life events (buying a home, part-time work, travel sabbaticals), "plan as a couple."
- **Dual simulation philosophy.** "Backtest against historical data" *and* "custom Monte Carlo simulations"; "gauge your chance of success"; probability histogram of outcomes by age.
- **Manual-entry posture.** "🔒No link to your accounts" is a *stated feature* — the model is built from user-entered accounts, account types, contribution orders, drawdown options, portfolio blends. Multiple testimonials cite the no-linking philosophy.
- **Per-year detail.** "Drill into each simulated year in detail — analyze estimated taxes, cash-flow, drawdown, and more"; cash-flow visualized as Sankey diagrams.
- **Tax machinery.** Tax analytics: estimated taxes per simulated year, marginal rates, effective brackets; strategies: Roth conversions, capital-gain harvesting, drawdown order optimization; targeting federal brackets / IRMAA cliffs / ACA limits (US statutory surfaces); 72t (SEPP) distributions.
- **Optimizer.** "Test hundreds of strategies in seconds. Optimize coordinates Roth conversions, capital gain harvesting, drawdown order, and more… apply a strategy in one click."
- **Progress tracking.** "Journal and visualize your actual progress over time and compare against your initial projections."
- **Estate/legacy.** "Model estate planning and what you leave behind — model your net legacy and estimate estate taxes."
- **Regional breadth.** Display currency choice; "growing list of international tax presets and account types, including Canada, the United Kingdom, Australia, Germany, the Netherlands, and more."
- **Tiering.** Free tier = basic retirement projections; Premium = tax estimation, cash-flow projections, tax optimization, withdrawal strategies, flexible spending, tax analytics, estate planning.
- **Advisor tier.** Pro for financial advisors: client plans, "seamlessly switch between the Pro Dashboard and client accounts," invite links, client profiles, "control whether clients can edit on their own," "track Assets Under Advisement (AUA) and client net worth," Advisor Directory listing.

### Empower — Retirement Planner — Evidence A (Tier 2 product page only)

Self-positioning: "Beyond a calculator, test-drive what retirement could look like." One tool inside a tool family (Net Worth, Budgeting & Cash Flow, Portfolio Analysis, Savings Planner, Debt Paydown, Emergency Fund, Transactions) atop linked accounts ("securely connect all your accounts… investments, cash, credit").

Key observations (only what the fetched page states):

- **Goals + spending timeline.** "See exactly how much you'll need to pursue goals like dream vacations, college for your loved ones"; a timeline showing "future spending goals, income sources, and major financial life events."
- **Retirement-age experimentation.** "Test-drive what retirement could look like at different ages" — the scenario axis made explicit.
- **Retirement income plan.** "Set up retirement withdrawals to balance daily expenses with other goals."
- **Readiness estimate.** Dashboard "showing projected retirement savings, income sources, spending goals, and estimated retirement readiness."
- **Aggregation-based data posture.** "Connect my accounts" as the primary onboarding action (contrast with ProjectionLab's stated no-linking).
- **Human escalation.** "Financial professionals are ready to create and adjust your plan" (advisory upsell with stated asset thresholds elsewhere on the site).

**Limitation:** operational help-center documentation for Empower's planner was not reachable in this pass; deeper mechanics (simulation method, assumption controls) are **not asserted** from this product.

## Cross-product Comparison

| Aspect | Boldin | ProjectionLab | Empower Retirement Planner |
|---|---|---|---|
| Central artifact | Plan (household data + goals + assumptions); scenarios are plan duplicates | Plan = living life model with milestones/events; scenarios | Retirement plan assembled from linked accounts + inputs |
| Household subject | Person/couple/household | Person/couple ("plan as a couple") | Household (family goals e.g. college) |
| Data posture | Link accounts **or** manual | Manual only (no-linking as philosophy) | Account aggregation |
| Resource inputs | Accounts/assets, real estate, debts | Accounts by type, portfolio blends | Accounts (linked), savings |
| Income streams | Work, rental, annuities, pensions, windfalls, Social Security | Income sources incl. rental (evidenced) | Income sources (evidenced generically) |
| Spending model | Recurring + healthcare expenses, goals | Expenses, life events, flexible spending | Spending goals on a timeline |
| Projection | Year-by-year to longevity age: net worth, income, taxes, estate value | Year-by-year, per-year drill-down (taxes/cash flow/drawdown); historical backtest + Monte Carlo | Projected retirement savings (method not asserted) |
| Sufficiency verdict | Retirement Chance of Success (Monte Carlo) | Chance of Success (Monte Carlo; outcome histogram by age) | "Estimated retirement readiness" |
| Uncertainty treatment | "Thousands of market scenarios" | Monte Carlo + historical sequences | Not asserted |
| Scenario/what-if | Duplicate plan, compare side by side | Scenarios + multi-condition milestones as decision trees | Different retirement ages |
| Decumulation tooling | Spending Guardrails (safe annual spending) | Drawdown order, withdrawal strategies, 72t/SEPP, drawdown optimization | "Set up retirement withdrawals" |
| Tax depth | Allocation across tax buckets, lifetime taxes, Roth Conversion Explorer | Brackets, marginal/effective rates, Roth conversions, gain harvesting, IRMAA/ACA targets | Not asserted |
| Government benefits | Social Security estimation + claiming explorer | Regional presets (CA/UK/AU/DE/NL…) | Not asserted |
| Progress vs plan | "Living document," habit framing, plan-accuracy coach | Journal actuals vs projections | Not asserted |
| Estate/legacy | Estate value projected | Net legacy + estate-tax estimation | Not asserted |
| Advisor/human layer | Coaching + fee-only advisor referral; AI assistant | Advisor Pro (client rosters, permissions, AUA, directory) | "Financial professionals… create and adjust your plan" |
| Regional focus | US (Social Security, Roth) | US default + international presets | US |

### Stable commonalities (Layer B)

1. A **personal/household plan** as a persistent, editable artifact — not a one-shot form.
2. A **planning horizon anchored at a retirement point** and running to an end-of-life/longevity assumption — spanning both accumulation and decumulation.
3. A **year-by-year projection engine** over resources (assets, income streams) and needs (spending, goals, life events).
4. A **sufficiency verdict** answering "will the money last / am I on track" — realized as chance-of-success (Monte Carlo) or a readiness estimate.
5. **Scenario / what-if exploration** by varying retirement timing, spending, and one-time events — with side-by-side comparison.
6. **Decumulation support** — converting assets into retirement income (withdrawal setup; safe-spending guidance; drawdown ordering).
7. **Tax treatment of money as a modeling dimension** (buckets/brackets/conversions) — depth varies.
8. **Living-plan maintenance** — updating data and comparing progress against the plan over time.
9. **Optional human layer** — coaching, advisor referral, or advisor-facing tooling.

### Differences (segment/vendor, not Type-defining)

- Data posture (aggregation vs manual) — posture, not structure.
- Simulation philosophy (Monte Carlo vs historical backtesting vs deterministic; Empower's method unverified).
- Tax machinery depth and regional statutory surfaces.
- Audience emphasis (near-retiree vs FIRE/early-career).
- Packaging (standalone vs ecosystem-embedded vs advisor platform).

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

> A Retirement Planning Application is a personal financial projection application whose defining core is: **(1) a persistent household plan anchored to a retirement point in time** (retirement age/date, horizon to an end-of-life assumption), **(2) a projection of resources and needs year-by-year across the accumulation → decumulation transition**, and **(3) a sufficiency evaluation** answering whether projected resources cover projected needs across that horizon.

Three properties. Remove the retirement anchor → generic long-horizon forecasting, not retirement planning. Remove the multi-decade projection → present-state tracking (a different Type: PFM). Remove sufficiency evaluation → a bare chart generator, not a planning tool.

Deliberately NOT in L0: Monte Carlo, account linking, tax-optimized withdrawals, Social Security/claiming machinery, scenario libraries, advisor surfaces, education content, AI.

### L1 — Common Mature Structure

- household/person profile (ages, retirement timing, longevity assumption)
- resource inventory: accounts/assets — commonly organized by tax treatment — plus debts and real estate
- income streams: employment income, pensions/government benefits, annuities, rental income, windfalls
- spending model: recurring expenses, healthcare, one-time goals/life events
- projection readouts: net-worth trajectory, income vs expenses, shortfall detection
- sufficiency metric (probability of success / readiness score)
- scenario duplication and side-by-side comparison
- decumulation guidance (withdrawal setup / safe spending)
- progress tracking of actuals vs plan

### L2 — Variant / Optional Structure

- data posture: account aggregation vs manual entry (both are whole-product philosophies)
- uncertainty treatment: Monte Carlo vs historical backtesting vs deterministic assumptions
- tax depth: bucket allocation, lifetime-tax projection, conversion/harvesting optimization
- government-benefit machinery depth and regionalization (US Social Security; international tax presets)
- estate/legacy modeling
- advisor-facing packaging (client rosters, permissions, AUA tracking, advisor directories)
- human support layer (coaching, advisor referral)
- education content, AI assistants
- embedding: standalone product vs module of PFM/brokerage/wealth ecosystems
- audience emphasis: near-retiree vs FIRE/early-career; free-tier gating

### L3 — Vendor-specific (research notes only)

- Boldin: "Retirement Chance of Success" naming + 80%-strong guidance; PlannerPlus 10-scenario cap; Social Security Explorer / Roth Conversion Explorer / Spending Guardrails as branded tools; "digital coach" plan-accuracy tracking; Boldin AI.
- ProjectionLab: Sankey cash-flow diagrams; multi-condition milestones as decision trees; black-swan event modeling; bracket/IRMAA/ACA targeting; 72t (SEPP) surface; lifetime pricing tier; Advisor Directory; specific country preset list.
- Empower: tool-family framing (Retirement Planner as one of ~8 financial tools); advisory upsell thresholds (Personal Strategy $100k / Private Client $1M); "estimated retirement readiness" dashboard framing; NerdWallet/Forbes award claims.
- Empower simulation method: **unverified in this pass** — do not generalize.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Pre-software / spreadsheet-era planning:** paper retirement worksheets and spreadsheet planners carry household profile, retirement age, projected balances, and a "will it last" check — all three L0 properties hold without Monte Carlo, aggregation, or tax optimization. Passes.
- **Regional:** a planner built around a non-US pension system (or ProjectionLab's international presets) still satisfies L0; Social Security machinery is L2. Passes.
- **Advisor-native planning platforms** (advisor builds the plan on the client's behalf) — same artifact, different operator. L0 holds. Passes.
- **One-shot retirement calculators:** a single-page calculator satisfies properties (1)(2)(3) degenerately at the moment of calculation but lacks the persistent plan and the maintenance loop; treated as the degenerate/entry form of the Type rather than a separate Type (the persistent-plan seam is documented in the final document).

Conclusion: L0 is not over-fitted to the current US consumer-Monte-Carlo implementation.

## Vendor-specific Findings

See L3 above. Additionally: ProjectionLab markets "no link to your accounts" as a privacy philosophy — an anti-feature positioning that confirms account aggregation is *not* definitional. Empower's planner is one tool in a family that includes budgeting/net-worth/debt tools — confirming ecosystem embedding as a packaging variant.

## Boundary Findings

| Neighbor | Relationship | Seam ("remove what → becomes the other") |
|---|---|---|
| Personal Finance Management Application | adjacent, often merged | PFM's artifact is the present state (accounts, budgets, transactions). Remove the future projection + sufficiency verdict and the product becomes PFM. Ecosystems (Empower-class) merge both; the planner remains the projection artifact. |
| Robo-advisor | adjacent capability-overlap | Robo-advisor's object is the managed portfolio (construction, rebalancing, execution). Its retirement projections are a capability of this Type embedded inside it. Remove portfolio management/execution → this Type. |
| Wealth Management Platform / Financial Advisor Platform | container / channel | Advisor practice surfaces (portfolios, reporting, client comms) are broader; the plan-projection module inside is this Type. Advisor-facing planning platforms (client rosters, AUA) are this Type packaged for professionals. |
| Pension Administration Platform | different subject | Pension admin keeps institutional scheme/member records (employer/scheme side). The retirement planner models the household's own future. Remove the household-plan subject → pension admin. |
| Retirement calculator (one-shot) | degenerate form | A calculator is one pass of the projection without the persistent plan, scenario library, or maintenance loop. Kept as entry-form variant, not separate Type. |
| Budgeting Application | different horizon | Budget controls near-term cash flow; the planner projects decades. Distinct artifacts. |
| Tax Preparation Application | different time direction | Tax prep files past-year returns; the planner projects forward-looking lifetime tax surfaces. Overlap: projected tax estimation is L1/L2 machinery. |
| Estate Planning Application | different artifact | Estate planning produces legal instruments (wills/trusts); the planner may *estimate* legacy value as a projection output. |
| Financial Modeling Application (FP&A) | name collision only | FP&A models organizations; this Type models a household. No real-world confusion. |

## Uncertainties

1. Empower Retirement Planner's simulation method and assumption controls were not verifiable (product page evidence only) — no claims made about its mechanics.
2. Fidelity, Pralana, RightCapital unreachable — the brokerage-embedded tier beyond Empower and the advisor-platform tier beyond ProjectionLab's Pro remain evidenced only indirectly.
3. Whether "estate planning" modeling depth in some products constitutes drift toward Estate Planning Application — treated as optional output (legacy value estimation), not a separate workflow; not fully verified.
4. Exact deterministic-vs-probabilistic mixing in Boldin's engine ("thousands of market scenarios" — Monte Carlo per vendor description; internal mechanics not published).
5. Non-US-dedicated products (e.g., UK/AU-specific planners) were not directly sampled; regional breadth rests on ProjectionLab's preset list + abstraction reasoning.

## Final Synthesis

The Retirement Planning Application is the household's **long-horizon financial projection system**: a persistent plan (profile + resources + needs + assumptions) anchored at a retirement point, projected year-by-year across accumulation into decumulation, evaluated for sufficiency, explored through scenarios, and maintained as life changes. Market realizations differ by data posture (link vs manual), simulation philosophy (Monte Carlo / historical / deterministic), tax depth, regional benefit systems, and packaging (standalone consumer tool vs ecosystem module vs advisor platform) — all of which are variant dimensions, not defining structure. The Type sits between present-state tracking (PFM) and portfolio management (robo-advisor), and its one-shot degenerate form is the retirement calculator.
