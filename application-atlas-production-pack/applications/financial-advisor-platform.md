# Financial Advisor Platform

## Overview

A **Financial Advisor Platform** is the advisor-side practice system for running a financial-advisory business: it holds the advisor's book of client households as named relationship records, maintains each household's structured financial position (accounts, assets, liabilities), and produces the advisory work products — financial plans, proposals, and client reports — that express what the advisor advises, kept current as the client's situation and the relationship evolve.

It answers a practical problem: an advisor serves dozens to thousands of client households, each with scattered accounts at multiple institutions, long-horizon goals, periodic reviews, and documentation obligations. No single record-keeping surface elsewhere — not the custodian's system, not the client's own apps, not a generic CRM — holds the household-level financial picture together with the advisory work done on it.

The defining core is deliberately small:

```text
Client household (advisor-held relationship record)
└── Structured financial position (accounts / assets / liabilities bound to the household)
    └── Advisory work products (plan · proposal · reports), maintained over time
```

Everything else the market associates with this category — account aggregation feeds, client portals, performance reporting, fee billing, trading and rebalancing, compliance modules, AI assistance — is widespread standard capability, not part of the definition. Older and simpler advisor tools (a client database plus a planning calculator) still fit the definition without any of them.

When the system stops being operated by an advisor for a book of client households, it becomes a different Application Type: a consumer money app (no advisor), a portfolio reporting engine (no relationship layer), or an advisor CRM (no financial position or plan engine).

## Users & Context

Primary users:

- **Financial advisor / planner** — owns client relationships; builds and presents plans and proposals; runs reviews. The system is organized around their book of households.
- **Paraplanner / planning associate** — prepares plans, enters and maintains client data, drafts scenarios and reports under the advisor's direction.
- **Operations / client service** — processes account paperwork, service requests, and day-to-day administrative tasks; keeps household and account data accurate.

Secondary users:

- **Firm leadership** — book-of-business-wide visibility: pipeline, activity, production, and client health across advisors.
- **Compliance officer** — audit trails, supervised workflows, and records of client interactions and recommendations (depth varies by product).
- **The client** — a secondary, advisor-controlled surface: a branded portal for viewing their plan, portfolio, goals, and documents, and sometimes for entering their own data or completing advisor-assigned tasks.

Typical context: an ongoing advisory relationship with a rhythm of onboarding → planning → implementation → periodic reviews. Work happens in the advisor's office (desktop/web workspace), in client meetings (presentation views), and increasingly on the client's phone (portal/mobile app). Firms range from solo independent advisors to enterprises — broker-dealers, banks, and aggregator firms running thousands of advisors — which changes the administration and compliance surface but not the core model.

## Core Model

### The Defining Core

**Client household.** The central managed record. An advisor's book is organized by household — the client, optionally a co-client (spouse/partner), and dependents — rather than by individual contact or by account. The household carries the relationship context: members with roles, connections to related entities (companies, trusts), notes, and interaction history. Every other object in the system hangs off a household. This is the grain at which the advisor thinks and works: plans, reviews, and fee relationships are household-scoped even when the underlying accounts are individual.

**Client financial position.** A structured representation of the household's financial reality, bound to the household record: bank and investment accounts with balances and holdings, credit cards and loans, properties, insurance policies, business interests, and often income sources, savings rates, and expenses. The position is the substance the advisor advises against. How it gets into the system varies (see How It Works); that it exists as structured, maintained data attached to the household is definitional.

**Advisory work products.** Outputs the advisor produces from the position for the client, and maintains over time:

- **Financial plan** — the household's goals (retirement age and lifestyle, education, major purchases), current situation, and long-term projections (cash flows; goals-based products add a success-probability measure), plus scenario analysis (what-if comparisons, stress tests) and recommended strategies (tax, insurance, estate, debt).
- **Proposal / recommendation** — an investment or strategy recommendation prepared for a specific household: risk profile, proposed allocation or strategy, often flowing into account opening paperwork.
- **Client reports** — plan summaries and performance/position reports produced on demand or on a review cycle, in client-ready form.

Work products are living objects: they are revised as the position changes and re-presented at each review. A system that holds client records but no financial position, or a position but no advisory work products, is a different kind of application (see Related Application Types).

### Standard Capabilities of Mature Products

These are common across the researched market and expected by buyers, but they implement or extend the core rather than define it:

- **Account data feeds and aggregation** — account balances and holdings-level data pulled from custodians and from aggregators that reach accounts held away from the advisor's custodian, refreshed on a regular cycle; portfolio-led products add reconciliation against custodian records — in the researched sample, run overnight so reporting starts each day from clean data.
- **Client portal and document vault** — a branded (often white-labeled), mobile-friendly client surface showing plan, portfolio, goals, and statements, with a document vault for exchanging files; some products separate client-shared from advisor-private storage. The advisor controls what each client sees.
- **Performance reporting** — portfolio performance measurement and client statements (the specialty of portfolio-led products); planning-led products offer investment analytics (allocation, holdings, concentration) inside the plan instead.
- **Risk assessment** — questionnaires and scoring that locate each client's risk tolerance and connect it to proposed portfolios.
- **Proposal-to-implementation workflow** — in integrated stacks, a proposal flows into new-account opening: client data pre-filled from the household record, custodian and account type selection, investment selection, and e-signature paperwork delivered to the custodian.
- **Practice workflow** — tasks, recurring workflows (onboarding, review prep), meeting notes, and service requests, with assignment across team members and an activity history per household.
- **Model portfolios** — firm or third-party model allocations applied to client portfolios (managed natively in portfolio-led products; imported in planning-led ones).
- **Integration fabric** — the platform exchanges household- and account-level data with custodians, aggregators, CRMs, planning tools, and portfolio analytics; single sign-on across the stack is common.
- **Roles and record-level permissions** — advisor, planner, operations, and compliance roles; visibility of a household controlled at record level; audit trails.
- **AI assistance** — increasingly common: data-entry extraction from documents and meeting transcripts, meeting preparation and notes, planning agents, and firm-level intelligence.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Client household
Implementations:  plan-container household (planning-led) · CRM household with
                  relationship web (CRM-led) · household as billing/reporting
                  roll-up over accounts (portfolio-led)

Concept:   Financial position
Implementations:  custodian daily feeds · third-party aggregation (held-away
                  accounts) · manual entry · client self-entry via portal ·
                  document/report import (including imports from other
                  planning tools)

Concept:   Plan
Implementations:  goals-based interface over cash-flow engine · pure cash-flow
                  modeling · modular plan workspaces (retirement, tax, insurance,
                  education, estate modules)
```

A reader who has only seen one implementation — say, a planning tool where the advisor types everything by hand — should still be able to recognize a portfolio-led platform or an enterprise advisor desktop as the same Type.

## How It Works

### 1. Onboard a client household

```text
Create the household record (client + co-client names → household)
→ gather the financial picture:
     advisor enters it · client enters it via invited portal access ·
     accounts link in from custodians/aggregators · documents/reports are imported
→ capture goals (retirement, education, purchases) and assumptions
     (income, savings, expenses, tax situation)
→ run a risk assessment
```

The household now exists as the container for everything that follows. Data gathering is deliberately multi-channel: the same position can be built by hand, by feed, by the client, or by importing an existing plan document from another tool.

### 2. Build and maintain the plan

```text
Position + goals + assumptions → long-term projections
→ review how likely the goals are to be met (goals-based products
   express this as a success probability); run what-if scenarios and stress tests
→ craft proposed strategies (savings, tax, insurance, estate, withdrawal order)
→ compare current plan vs proposed plan side by side
→ present to the client (meeting view, one-page summary, portal)
```

The plan is a living document. Scenario exploration happens in a sandbox: a proposed change is compared against the current plan and only becomes the client's plan when the advisor applies it. As account values, income, or goals change — often via the daily data feeds — the plan's projections update, which is what keeps the plan relevant between formal reviews.

### 3. Implement the advice

```text
Agree the recommendation
→ prepare the proposal (risk profile, allocation/strategy, projections)
→ open accounts: household data pre-filled → custodian & account type selection
   → investment selection → e-signature paperwork routed to the custodian
→ (portfolio-led products) rebalance holdings toward the target allocation,
   often household-level and tax-aware
```

In planning-led products, implementation may be handed off to the custodian or a portfolio tool; in portfolio-led and all-in-one products, trading and rebalancing are native. The direction of travel is the same: advice becomes accounts, positions, and paperwork without re-keying the household's data.

### 4. Report and review

```text
Generate client-ready reports (plan progress, performance, statements)
→ deliver via the client portal / vault / presentation
→ hold the periodic review meeting
→ record notes, decisions, and follow-up tasks on the household
→ update the plan; the cycle repeats
```

The review cycle is the economic heartbeat of the practice, and the platform is built around it: fresh position data, current plan projections, prepared meeting views, and recorded outcomes.

### 5. Run the practice

Across all of the above, the firm layer operates continuously: tasks and recurring workflows keep client service from falling through cracks; service requests track administrative changes in flight across the book; dashboards aggregate pipeline, activity, and production; compliance surfaces capture the audit trail. In enterprise deployments, firm-level administration (advisors, roles, supervision) sits above the advisor-level workspace.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Advisor dashboard / client views

The advisor's entry surface for the book.

- lists households (and prospects) with status signals — upcoming reviews, open tasks, at-risk relationships
- primary actions: open a household, start onboarding, work tasks

### Client record (household view)

The relationship surface for one household.

- members and roles, linked accounts and balances, interaction history (notes, emails, meetings), documents, open tasks
- primary actions: update household data, log interactions, launch plan/proposal/report, assign tasks

### Plan workspace

The advisor's working surface for a household's plan — typically modular.

- modules for the balance sheet/net worth, retirement projections, scenarios and stress tests, tax, insurance, education, estate, and cash-flow detail
- primary actions: adjust inputs, run scenarios, build proposals, generate client-ready summaries

### Proposal builder

A guided workflow from recommendation to presentation to paperwork.

- client data (pre-filled), goals and risk profile, custodian/account selection, investment selection, e-signature routing
- primary actions: build proposal, present, initiate account opening

### Report builder

Assembles client-facing documents from plan and portfolio data.

- selectable sections and branding; on-demand or scheduled generation
- primary actions: compose, generate, deliver to portal/vault

### Client portal

The client-facing surface, presented under the firm's brand.

- plan and goal progress, portfolio and statements, documents, tasks; sometimes client-side data entry and scenario viewing
- advisor-controlled: what each client sees is configured by the firm

### Administration / settings

Firm-level configuration: users and roles, permissions, integrations (custodians, aggregators, CRM), branding, workflow templates, compliance settings.

## Important Rules / Behaviors

- **The household is the unit of organization.** Accounts, plans, fees, and reviews are household-scoped; individuals are members of households. Tools that organize only by individual contact or only by account do not behave like this Type.
- **The position is kept current by data, not by re-entry.** Mature products refresh account data on a regular cycle from custodians/aggregators; portfolio-led products reconcile against custodian records so reporting starts from clean data. Manual entry remains a first-class fallback for accounts that cannot be linked.
- **Plans separate "current" from "proposed."** Scenario work is sandboxed; a proposal is compared against the current plan and becomes the plan only when applied. This current-vs-proposed discipline is a defining interaction pattern.
- **The advisor controls client visibility.** The client portal is advisor-configured per client; document vaults commonly separate client-shared from advisor-private storage. The client sees a curated view, not the advisor's workspace.
- **Record-level permissions and audit trails.** Who in the firm can see or edit a household is controlled at record level; interactions and recommendations are logged — a structural requirement of a regulated advisory practice, implemented with varying depth.
- **Data flows across the stack at household/account grain.** Whether the platform is one integrated suite or a stitched stack, the interchange vocabulary between planning, portfolio, and CRM tools is household- and account-level data. Integration depth is a major practical differentiator, not an afterthought.
- **Work products are versioned by revision, not replaced.** Plans and proposals are updated in place and re-presented; the historical thread of advice lives on the household record.

## Variants

The Type is one core with several stable postures:

- **Planning-led** — the plan is the product; portfolio data flows in for context; investment analytics live inside the plan. Typical of boutique and mid-market advisory firms.
- **Portfolio-led** — portfolio accounting, performance reporting, billing, and trading are the engine; planning is a companion module. Typical of investment-management-centered firms.
- **CRM-led** — the relationship and workflow layer leads; financial position and planning arrive through integrations. Common as the collaboration hub in larger teams.
- **All-in-one platform** — planning, portfolio, CRM, portal, billing, trading, and compliance bundled with a shared data layer. Typical of larger RIAs and enterprise channels.
- **Enterprise / institution deployment** — broker-dealer home offices, banks, and aggregator firms run the same core at scale, adding supervision, centralized administration, and multi-advisor management.
- **Regional and regulatory depth** — the researched sample is US-shaped (retirement accounts, tax-filing status, specific government-benefit modules). Products in other regimes substitute their own regulatory modules; the core model is unchanged, but module depth should be expected to vary by market.
- **Client self-service depth** — from read-only portals to clients entering their own data and completing advisor-assigned workflows.
- **AI depth** — from document extraction and meeting notes to planning agents and firm intelligence.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Advisor CRM (e.g., generic CRM shaped for advisory) | adjacent, commonly integrated | holds the relationship and workflow but not the financial position or plan engine; remove position + work products from this Type and a CRM remains |
| Portfolio Management System | adjacent, commonly integrated | account/portfolio is the unit and performance measurement the purpose; here the household relationship is the unit and the advisory work is the purpose |
| Wealth Management Platform | overlapping vocabulary, different operator | typically names the institution-side platform (broker-dealer/bank home office, product shelf, supervision); this Type is the advisor's practice tool — the seam deserves joint review |
| Robo-advisor | different operator | consumer self-service automated advice; remove the advisor as operator and this Type collapses into it |
| Retirement Planning Application | slice | single-purpose retirement projection tool; this Type carries the whole practice scope |
| Personal Finance Management Application | mirror image | the consumer manages their own finances; here the advisor manages many households on the client's behalf |
| Financial Planning & Analysis Platform | false friend | corporate budgeting/forecasting; shares only the word "planning" |
| Investment Research Platform | upstream content | market/strategy research feeds the advice; holds no client records |

The two most important boundaries: **vs Advisor CRM** (relationship without financial substance) and **vs Portfolio Management System** (financial substance without the relationship layer). A Financial Advisor Platform is defined by holding both, bound to the same household record, with advisory work products as the output.

## Representative Products

- **Orion Advisor Technology** — all-in-one platform pole: portfolio accounting, planning, CRM, trading, compliance, portals on a shared data layer; serves solo RIAs through enterprise broker-dealers.
- **RightCapital** — planning-led pole: household-centered plan workspace with modular planning, aggregation, and client portal; strong in boutique and mid-market firms.
- **Wealthbox** — CRM-first pole (boundary anchor): advisor CRM with households, workflows, and pipeline; financial position and planning arrive via integrations.
- **eMoney Advisor** — planning-led market leader (cash-flow modeling); not directly researched for this document — included as market context evidenced through integration documentation of the products above.
- **MoneyGuidePro (MoneyGuide)** — goals-based planning leader common in broker-dealer channels; same sourcing caveat.

## Sources

Research date: **2026-09-06**

Official documentation directly consulted:

- RightCapital Help Center — https://help.rightcapital.com/ (Getting Started: Creating Plans & Data Entry; Introducing the Planning Modules; Integrations; Client Experience Overview)
- Orion Advisor Technology — https://orion.com/ (Advisor Tech overview; Planning; Portfolio Accounting; Advisor Portal; Client Portal)
- Wealthbox — https://www.wealthbox.com/ (product overview; Contact Management feature page)

Market context (not directly fetched; evidenced via the sources above):

- eMoney Advisor — referenced in Orion Planning FAQ and integration page, RightCapital data-import documentation, Wealthbox integrations
- MoneyGuidePro — referenced in the same sources

> Sourcing limitation: emoneyadvisor.com and moneyguidepro.com were unreachable from the research environment (repeated 403/timeout), and Wealthbox's help center timed out; those products are calibrated to official product/feature pages and third-party official integration descriptions only. No precise operational details (numeric limits, pricing, default settings, exact refresh schedules) are asserted in this document; vendor-published performance statistics were treated as marketing claims and excluded.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
