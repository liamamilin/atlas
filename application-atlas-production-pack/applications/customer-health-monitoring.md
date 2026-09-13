# Customer Health Monitoring

## Overview

A **Customer Health Monitoring** application is a vendor-side system that maintains a standing, account-level measure of how each of the vendor's own customers is doing — a **health score or rating** — by aggregating multiple customer signals (product usage, support activity, satisfaction, engagement, commercial standing) through a customer-defined health definition, recomputing it on an ongoing cadence, and watching it against thresholds so that deteriorating accounts are classified and surfaced for attention.

The defining core is small:

```text
Monitored customer accounts (the vendor's own customers)
└── Health measure per account
    ├── produced by a customer-defined health definition
    │   └── aggregating multiple customer signals
    ├── recomputed on an ongoing cadence, retained as history
└── Monitoring loop
    └── thresholds/bands classify health and surface accounts needing attention
```

Everything else commonly associated with the category — weighted scoring machinery, segment-scoped health profiles, trend charts, portfolio consoles, automated alerts, CRM write-back — is standard capability that makes health monitoring practical, not what makes it health monitoring. A spreadsheet of accounts with usage, ticket, and survey columns, an agreed formula producing a red/yellow/green status per account, and a weekly review that flags the reds satisfies the same core; the definition does not depend on any modern platform packaging.

The Type is realized predominantly **inside customer success platforms**, where the health measure is the signal core of the wider customer-success workflow. What distinguishes it from its neighbors: a product usage platform *produces* the usage signal at event and user granularity; renewal management *consumes* health for the renewal decision; the customer success platform *operates the relationship workflow* around the customer. Health monitoring's own center is the health measure and its monitoring loop.

## Users & Context

Primary users:

- **Customer success managers (account owners)** — monitor the health of the accounts in their book, inspect what is driving a score, and act when health turns adverse. Health is designed to be actionable: a poor rating conventionally means "this account needs intervention."
- **Customer success leadership** — watch portfolio-level health distribution, contract value at risk, and trends over time; allocate attention across the book.

Secondary users:

- **CS operations / administrators** — design and maintain the health definition itself: which signals count, how they combine, which segments get which standard, and how health flows to alerts and other systems.
- **Sales and renewal owners** — consume health as risk context for renewal and expansion decisions.
- **Executives** — read aggregate health as a standing indicator of the customer base.

Context: business-to-business vendors with recurring revenue, where losing or expanding an existing customer is a primary revenue lever and where no single signal (usage alone, tickets alone) reliably expresses the state of the relationship. Health monitoring is part of the operating rhythm: accounts are checked continuously, reviewed in team cadences, and health changes trigger work.

## Core Model

### The defining core

**1. The monitored customer account population.** The system watches a standing population of identified customer accounts — the vendor's own customers, held as records (companies, or company relationships in products that manage partner/reseller structures). Every health value in the system is attributed to one account. Without the population there is nothing to monitor; the system collapses into generic analytics.

**2. The account-level health measure.** Each account carries a persistent health state — commonly a numeric score on a defined scale and/or a banded rating (a small set of classes such as good / average / poor, or healthy / at risk / neutral). Three properties make it a health measure rather than a metric:

- **It is defined, not measured.** An administrator configures a *health definition* — which signals feed it, how each signal is judged (criteria, ranges, weights), and how signals combine into the account-level result. The definition is a managed, inspectable artifact of the business, not a fixed formula.
- **It aggregates multiple signals.** The recurring signal families are product usage (logins, license utilization, usage depth), support (open tickets, resolution times, ticket age), satisfaction and sentiment (survey scores, CSM-assessed sentiment and, in some products, AI-derived conversation sentiment), engagement (recency of contact, stakeholder involvement), and commercial standing (billing status, contract value, product footprint). The mix is customer-defined; a definition built on a single signal is a degenerate case, not the norm.
- **It is alive.** Health is recomputed on an ongoing cadence as signals change, and past values are retained — current state plus history, so trend is a first-class question ("is this account getting better or worse?"), not an afterthought.

**3. The monitoring loop.** The health measure is continuously evaluated against configured thresholds or bands. The evaluation classifies each account (e.g., into good / average / poor) and makes adverse health *surface*: accounts in poor bands appear in at-risk views and segments, raise alerts, trigger tasks or playbook actions, and are diagnosed down to the signals that pulled the score down. The loop is what turns scoring into monitoring — without it, the system is a batch report generator.

### Standard capabilities

Mature products commonly add:

- **Structured aggregation machinery** — signals organized into groups or dimensions (e.g., a support group holding ticket count, ticket age, resolution time), with configurable weights so the account score is a weighted synthesis rather than a flat average.
- **Segment-scoped health definitions** — different health standards for different situations: onboarding accounts judged by onboarding progress, established accounts by adoption and renewal posture; enterprise accounts by a different yardstick than mid-market. Multiple definitions coexist, scoped by segment criteria (journey stage, account type, product), applied by precedence rules.
- **Dual representation** — the numeric score and the banded rating shown together; bands are threshold evaluations of the score or of attribute criteria, with ranges the customer sets.
- **History and trend** — periodic snapshots (frozen weekly/monthly values in some products), per-account timelines, and trend views at account and portfolio level.
- **Portfolio monitoring surfaces** — book-level views: health distribution across accounts, contract value weighted by health, breakdowns showing which signal dimension is dragging health down, health of accounts approaching renewal.
- **Hierarchy rollups** — where customers have parent/child structures, parent health derived from children (weighted or averaged per the customer's choice).
- **Manual and subjective inputs** — the account owner's own judgment (e.g., a sentiment assessment after a difficult call) recorded as a signal alongside automated feeds, usually with an expectation that it is kept current.
- **Alerts and automated actions** — notifications or created tasks/plays when health drops below a threshold or crosses a band; health attributes usable as filters that drive segments and workflows.
- **Integration surfaces** — connectors feeding the signals (product telemetry, support desk, surveys, CRM, billing) and, in some products, health written back out (CRM account fields, APIs) so other systems can consume it.

### One structure, many implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:            Health measure
Implementations:    numeric score on a defined scale; banded rating; both together

Concept:            Signal aggregation
Implementations:    weighted averages across measures/groups; criteria-based
                    classification (all-good vs any-poor); additive point systems

Concept:            Health definition scoping
Implementations:    multiple profiles by segment with precedence; multiple
                    scorecards with one active per account; single profile

Concept:            Signal sourcing
Implementations:    product telemetry integrations, support-desk sync, survey
                    tools, CRM/billing data, manual entry, AI-derived sentiment
```

A reader who has only seen one implementation — say, a weighted 0–100 score with red/yellow/green bands — should still recognize a criteria-based good/average/poor classification or an additive point score as the same structure.

## How It Works

The operating loop has six recurring movements.

**1. Define health.** An administrator designs the health definition: choose the signals available from connected systems, group them into dimensions, set the judgment for each (what counts as good, what counts as poor — criteria or ranges), set weights if the model is weighted, set the band thresholds for the final result, and scope the definition to a segment of accounts. Some products ship starter definitions and encourage starting simple — a handful of signals centered on usage and relationship — then refining against reality.

**2. Feed the signals.** Integrations bring signal data in: product usage from the vendor's own product telemetry, tickets from the support desk, survey responses from feedback tools, contract and billing data from CRM/finance, and manual entries from account owners. Signal data is materialized at the account level — raw user-level events must be aggregated into account-attributed measures before they can feed health.

**3. Compute and keep history.** The system recomputes health per account on its cadence — documented patterns include daily recalculation and weekly/monthly frozen snapshot values, varying by product. Current and previous values are kept, and history accumulates so that any account's trajectory is inspectable. Some products can recalculate health retroactively when definitions change.

**4. Monitor.** Users watch health at two levels. At the **account level**, a health view shows the current state, the contributing signals (which dimension or input is pulling the score down), and the trend. At the **portfolio level**, consoles and dashboards show the distribution of health across the book, contract value sitting in poor health, which dimensions are dragging the portfolio down, and how all of it moves over time. Accounts are commonly worked through saved segments filtered by health band.

**5. Act.** When health is adverse, the loop converts it into work: alerts or notifications on score drops, automatically created tasks or plays, at-risk segments routed into workflows, and diagnosis — some products explicitly highlight the single most impactful input so the owner knows where intervention moves the needle. Health also flows outward: written back to CRM fields, exposed via API, consumed by renewal and expansion processes as risk context.

**6. Tune.** Health definitions are living artifacts. Teams review whether the definition still predicts what it should (do poor-health accounts actually churn?), adjust criteria and weights, and re-validate. Vendors consistently advise against frequent definition churn — teams build trust in the bands, and constant recalibration erodes it; changes are made periodically and communicated.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Account health view

The per-account surface, usually a widget or module on the account record.

- Typical information: overall health (score and/or band), the health definition in force, the contributing signals with their current standing, trend over time, and — where applicable — the most impactful negative input.
- Primary actions: inspect signal detail, trace history, record a manual input (e.g., sentiment), jump to related work.

### Portfolio / book monitoring views

The manager-and-team surface for watching many accounts at once.

- Typical information: health distribution (counts and contract value per band), trend charts, breakdowns by signal dimension, health of accounts in renewal windows, drill-down into the accounts behind any number.
- Primary actions: filter to a band or dimension, open account lists, hand accounts to owners.

### Health definition console

The administrator surface where health is designed.

- Typical information: the definitions (profiles/scorecards), their signal composition, weights/criteria/ranges, segment scoping and precedence, computation status.
- Primary actions: create/edit definitions, preview and validate changes where supported, enable/activate, recalculate where supported.

### Alert and action surfaces

Where monitoring becomes work.

- Typical information: accounts that crossed a threshold, created tasks/plays, at-risk segments.
- Primary actions: acknowledge, work the task, adjust the alerting rule.

### Reports and dashboards

Standard reporting over health data — score distributions, trends, cohort comparisons — plus health as a field available in general reporting, segments, and APIs.

## Important Rules / Behaviors

- **Health is a managed definition, not a raw fact.** Two vendors — or two segments of the same vendor — can legitimately compute different health for the same observable behavior, because the definition encodes the business's judgment of what "doing well" means. The definition, not the number, is the artifact of record.
- **Bands carry an action convention.** The poor/at-risk band is not just a label: across the sampled products it is explicitly the "requires action" state. The monitoring loop is built around making that state impossible to miss.
- **Unclassified accounts exist.** An account that matches no health definition — or that has been cancelled — can sit in an explicit "unknown"/unclassified state. Mature configurations ensure a default definition catches everything else, and treat unknown health as a configuration problem to fix.
- **Manual inputs need protocol.** Subjective signals (owner sentiment) are legitimate health inputs but decay without discipline; products that support them pair them with expectations that owners keep them current.
- **Signal granularity matters.** Survey scores are typically collected per user; aggregating them to the account can mask the difference between a champion and a casual user. Usage events must be aggregated into account-level measures before they can feed health. These are known design pitfalls the products themselves document.
- **Definitions should be stable.** Frequent changes to health definitions undermine the team's ability to reason across time; changes are periodic, previewed, and often recalculated retroactively so history stays comparable.
- **Hierarchy health is derived.** Parent/child rollups are computed from child health by a chosen method; the parent's health is a view over its children, not an independently observed fact.
- **Health is an input, not the workflow.** The system classifies and surfaces; the response — the call, the save plan, the renewal negotiation — lives in the neighboring systems (customer success platform, CRM, renewal management).

## Variants

- **CS-platform-embedded (dominant realization)** — health machinery as the signal core of a customer success platform, surrounded by the wider relationship workflow.
- **Suite-embedded** — health scoring as a feature of a CRM or service suite, lighter-weight, computed over CRM-resident signals.
- **Purpose-specific scores** — separate health measures for different questions (churn risk vs expansion/upsell opportunity), kept apart deliberately because mixing purposes muddies the scale.
- **Predictive/ML health** — model-derived churn likelihood as a health input or as a parallel measure, sometimes optimized against realized renewal outcomes.
- **AI-signal variants** — conversation sentiment mined from emails, chats, and call transcripts as a standing signal; AI-assisted definition tuning.
- **Scale/tier variants** — enterprise definitions with many weighted dimensions and governance; smaller-team variants with a few criteria and a simple three-band rating.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Customer Success Platform | host/adjacent — embeds health monitoring as its signal core | the CS platform's center is the managed customer relationship (success plans, plays, renewals, collaboration); health monitoring's center is the health measure and its monitoring loop. Remove the CS workflow and health monitoring still stands; remove the health measure and a CS platform still functions on other signals |
| Product Usage / Adoption Platform | upstream — produces the usage signal | usage platforms capture and analyze usage at event/user/feature granularity; health monitoring consumes account-level aggregates of multiple signal types into one standing measure |
| Renewal Management Platform | downstream — consumes health | renewal management owns the renewal decision (dates, amounts, outcomes, forecast); health is one of its risk inputs, not its object of record |
| CRM | adjacent substrate | the CRM stores the account and often receives health as a synced field; it does not define, compute, or watch the health measure |
| Business Intelligence / Dashboard Platform | confused neighbor | BI reports over data; health monitoring maintains a managed per-account health state — a definition, a cadence, history, and an action loop. A dashboard with a red/yellow/green column is not the Type |
| Customer Feedback Management / VoC | signal supplier | feedback systems own the feedback item and survey programs; their scores (NPS/CSAT) are one input family to health |
| Customer Onboarding Platform | adjacent workflow | onboarding platforms execute onboarding work; onboarding progress is a common health signal for onboarding-stage accounts |

The boundary with the Customer Success Platform is the most consequential: in the current market, health monitoring is almost always delivered inside a CS platform. The leaf stands on the strength of the distinct center of gravity — the health measure and its monitoring loop — but the module-convergence should be revisited jointly when the Customer Success Platform leaf is documented.

## Representative Products

- **Gainsight** — enterprise customer success suite; its Scorecard (measures, measure groups, grading schemes, weights, snapshots, rules-driven actions) is the most fully documented health machinery in the sample.
- **Totango** — customer success platform with two health models (attribute-based rank and weighted multidimensional score), segment-scoped health profiles, and dedicated portfolio health consoles.
- **Planhat** — customer success platform with an additive point-based health score and group-level rollups.
- **Catalyst** — customer success platform (now part of Totango) with input→group→account weighted scoring and explicit "most impactful input" diagnosis.

The defining core was checked against a spreadsheet-era practice model (account list + agreed formula + RAG status + weekly review) to avoid over-fitting the definition to the current CS-platform packaging.

## Sources

Research date: **2026-09-08**

- Gainsight — Scorecards Overview: https://support.gainsight.com/gainsight_nxt/05Scorecards/01About/Scorecards_Overview
- Gainsight — Calculation of Measure Group Scores and Overall Score: https://support.gainsight.com/gainsight_nxt/05Scorecards/02Admin_Guides/Calculation_of_Group_Scores_and_Overall_Scores
- Gainsight — Use Scorecard Data in Rules and Reports: https://support.gainsight.com/gainsight_nxt/05Scorecards/02Admin_Guides/Use_Scorecard_Data_in_Rules_and_Reports
- Totango — Analyze health at the account level: https://support.totango.com/hc/en-us/articles/360032136152-Analyze-health-at-the-account-level
- Totango — Configure profiles for multidimensional health: https://support.totango.com/hc/en-us/articles/4410017625748-Configure-profiles-for-multidimensional-health
- Totango — Best practices for designing health profiles: https://support.totango.com/hc/en-us/articles/202301749-Best-practices-for-designing-health-profiles
- Totango — Manage your book by risk + health: https://support.totango.com/hc/en-us/articles/37966349334804-Manage-your-book-by-risk-health
- Planhat — How Health is Calculated: https://help.planhat.com/en/articles/9590704-how-health-is-calculated
- Planhat — Health Scores: What You Can Include: https://help.planhat.com/en/articles/9587239-health-scores-what-you-can-include
- Catalyst — Monitor customer health: https://help.catalyst.io/hc/en-us/articles/28924640472980-Monitor-customer-health

> Sourcing limitation: several additional candidate products (ChurnZero, Vitally, HubSpot, ClientSuccess) could not be reached from the research environment and were dropped rather than filled from memory. The verified sample is four customer success platforms; no standalone pure-play health-monitoring vendor was verified. Claims about non-CS-platform realizations and about the universality of automated alerting are calibrated accordingly and kept at "commonly" strength.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
