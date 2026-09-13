# Engineering Productivity Analytics

## Overview

An **Engineering Productivity Analytics** application is an engineering organization's measurement system for its own work process. It continuously assembles a record of the organization's software development activity from the tools where the work happens — version control, issue trackers, CI/CD, incident systems — computes defined process metrics over that record, and presents the results as dashboards and reports through which engineering leaders review delivery flow, investment balance, and developer experience, and drive improvement.

The defining structure is small:

```text
Engineering activity record (from the org's own dev tools)
└── Derived process metrics with defined semantics
    └── Insight surface for engineering management
        └── Improvement loop (goals, agreements, triage)
```

Everything else commonly associated with the category — team hierarchies, DORA metrics, developer surveys, benchmarks, AI-tool measurement, capitalization reporting — is widespread in current products but is not what makes the product this Type. The measurement intent predates all of it: before platforms automated the work, engineering leaders assembled the same picture by hand, aggregating version-control and issue-tracker data into spreadsheets — a practice the vendors in this category themselves document as the state their products replaced.

The subject of measurement is the **work process** — how code, review, and release flow, where engineering effort goes, how developers experience their environment. It is not the health of the code (that is the code-quality platform's subject) and not the behavior of production systems (that is observability's subject).

## Users & Context

The primary user is an **engineering leader** — someone responsible for how engineering works rather than for doing the work: VPs and directors of engineering, engineering managers, team leads, and (in larger organizations) engineering operations or platform-engineering leaders.

Typical reasons to open the application:

- review how delivery flow is trending (cycle time, throughput, deployment cadence) for the org or a team
- see where engineering effort is going (feature work vs maintenance vs bugs vs support) and whether that matches intent
- find bottlenecks — slow reviews, large changes, stuck work, flaky pipelines
- check how developers say they are doing, and correlate that with what the systems show
- prepare reporting upward: board updates, investment reviews, AI-adoption impact
- run an improvement loop: set a goal, agree on a change of practice, check whether it held

Developers are the **data subject** of the system: their commits, reviews, tickets, and deployments are the raw material. In most products developers also see team-level views and receive notifications in chat tools; in some they answer recurring experience surveys. How much individual-level detail anyone may see is a governed setting, not an accident (see Rules).

The work environment is the engineering organization's own tool stack. The application sits **on top of** the tools engineers already use and does not change how they work — that non-intrusion is a design commitment across the category, because the data's credibility with developers depends on it.

## Core Model

### The Defining Core

```text
Engineering activity record
└── Derived process metrics
    └── Insight surface for engineering management
```

Three structures. If any one is removed, the product is no longer recognizable as this Type:

- **Engineering activity record** — a persistent, continuously updated record of the organization's development activity, assembled from connected systems: code changes and reviews from version control, work items from issue trackers, pipeline and deployment events from CI/CD, incidents from incident tools. The record is built by observation, not by asking engineers to report or tag differently. Without it there is nothing to measure.
- **Derived process metrics** — measures computed over the record with explicit, inspectable definitions: how long work takes (cycle time and its phases), how much flows through (throughput, deployment frequency), how reliable the process is (change failure, rework), and where effort goes (investment distribution). Without defined metrics the product is just a data feed.
- **Insight surface for engineering management** — dashboards and reports through which leaders review trends over time, compare teams and periods, and act. Without it the product is a metrics pipeline, not an analytics application.

### The Organizational Layer

Metrics only become actionable when they attach to the org structure. Mature products therefore maintain:

- **Teams and hierarchy** — the unit of measurement. Metrics roll up from teams to departments to the organization; managers see their teams, directors see aggregates. Team membership is tracked over time, so past contributions stay attributed to the team that did them even after people move.
- **Contributors** — individual engineers as identities resolved across tools (the Git username, the Jira user, and the HR record are linked into one person). Identity resolution is what makes per-person and per-team computation possible, and it is also the system's main privacy surface.

### The Metric Layer

Metric families recur across products, though exact definitions are product-owned and configurable:

- **Delivery flow** — cycle time (commonly decomposed into coding, pickup/review-wait, review, and deploy phases), pull-request throughput, batch size, deployment frequency.
- **Quality of process** — change failure rate, mean time to recovery, rework, CI pipeline health.
- **Investment distribution** — how engineering effort splits across categories such as new features, maintenance, bugs, and support; mature implementations express it in full-time-equivalent engineers, derived from tool activity rather than timesheets.
- **Developer experience** — recurring survey signals (satisfaction, friction drivers, time lost to specific waits) reported alongside the system metrics, so leaders can correlate what developers say with what the tools show.

### The Improvement Layer

Measurement alone is explicitly not the point — leading products frame themselves around the loop from insight to changed behavior:

- **Goals / targets** — a metric turned into a tracked commitment for a team or the org.
- **Team-level improvement agreements** — a team decides a practice change (for example, smaller pull requests, faster first review); the system tracks exceptions and sends reminders until the new habit holds.
- **Triage and playbooks** — managers mark each finding (keep monitoring / improve / needs support) and follow research-backed guidance for the areas they choose to work on.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ on every layer:

```text
Concept:   Activity record
Implementations:  connector fabric over many tools; deep-but-narrow Git+tracker focus;
                  programmatic push APIs for anything unconnected

Concept:   Process metrics
Implementations:  DORA metric sets; proprietary phase decompositions; FTE effort models;
                  survey-derived experience indices

Concept:   Insight surface
Implementations:  executive dashboards; team pages; scheduled reports; chat digests;
                  AI assistants that answer questions over the data
```

## How It Works

### Connect the tools and build the record

```text
Connect version control (GitHub / GitLab / Bitbucket / Azure DevOps …)
→ connect the issue tracker (Jira / Linear / Azure Boards …)
→ optionally connect CI/CD, incident tools, calendars, HR systems
→ the platform backfills history (depth varies by product)
→ contributor identities are merged across tools into one person per engineer
```

Setup is an administrator task and the org's on-ramp to everything else. The platform reads metadata and activity — commits, pull requests, review events, ticket transitions, deployments, incidents — not the source code itself; at least one product states explicitly that it stores file names and sizes but never the code.

### Model the organization

```text
Create teams (manually, imported from the code host, or synced from HR)
→ assign contributors to teams
→ map repositories and work items to teams
→ configure what counts as a deployment and how pull requests link to issues
```

This mapping layer is where metric accuracy is won or lost: attribution rules (who owns a change, which ticket it belongs to, which team gets credit) are configurable because every organization's conventions differ.

### Review the metrics

```text
Open the org or team dashboard
→ read the trend (cycle time, throughput, deployment frequency, failure rate)
→ drill into a metric's phases to find the bottleneck
→ compare teams, periods, or against industry benchmarks
→ segment by project, category, or — where permitted — individual
```

The recurring question the surface answers is "where is the work slowing down, and is it getting better?"

### Close the loop

```text
Pick one finding (e.g., review wait is the dominant phase)
→ set a goal or a team working agreement
→ the system tracks exceptions and sends digests in Slack/Teams
→ the next retro checks whether the metric moved
→ repeat
```

In survey-led products the loop also runs on the qualitative side: a recurring snapshot survey goes out in chat, results are reported at team level, managers triage each friction driver, and improvement playbooks suggest what to do.

### Report upward

Scheduled or on-demand reports translate engineering activity into management language — investment distribution, delivery predictability, AI-tool adoption and its measured effect on delivery — for executive audiences and, in some products, finance-adjacent outputs such as software capitalization reports.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Org / team dashboard

The primary entry surface.

- trend charts for the headline metrics, team roll-ups, period comparison
- primary actions: switch scope (org → team → sub-team), change period, drill into a metric

### Metric drill-down

One metric, decomposed.

- phase breakdown (e.g., coding vs review-wait vs review vs deploy), distribution views, the underlying work items contributing to the number
- primary actions: filter, segment, open the contributing pull requests or tickets

### Investment / allocation view

Where effort goes.

- category breakdown (features, maintenance, bugs, support, custom categories) in FTEs or activity share, over time and per team
- primary actions: adjust category rules, compare against target allocation

### Contributor view (governed)

Individual-level activity and metrics.

- per-person contribution, review, and (in some products) AI-usage detail
- primary actions: filter, export — visibility controlled by role settings, in some products down to full redaction

### Survey console and survey surface

Two sides of the qualitative layer.

- console: create and schedule surveys, view results by team, read comments, triage drivers
- developer side: a short questionnaire delivered in Slack/Teams; results reported at team level; whether individual comments carry names varies by product

### Goals / working agreements

The improvement-loop surface.

- current targets, progress, exception lists, digest history
- primary actions: create or edit an agreement, review exceptions, mark done

### Reports

Management- and executive-facing outputs.

- scheduled or ad-hoc summaries combining delivery, investment, and experience data; export and sharing

### Administration

The setup and governance surface.

- integrations, team and contributor management, metric and deployment configuration, roles and permissions, individual-visibility settings, data export and API keys

## Important Rules / Behaviors

### Metric semantics are product-defined and configurable

There is no industry-standard cycle time. Where the clock starts (first commit vs ticket moved to in-progress), what counts as a deployment, and which branches are excluded are all configuration choices, and products document that these choices materially change the numbers. Backfilled data can also retroactively adjust historical values. Two organizations comparing raw numbers are often not comparing the same thing.

### Attribution is a modeled choice, not a fact

Which team gets credit for a change, which ticket a pull request belongs to, and whether a file is code or test are all inferred by rules the organization configures. Products track team membership historically so attribution survives reorganizations, but the attribution itself remains a model of the org, not the org itself.

### Individual-level visibility is governed, and the category polices itself

Products in this category commonly treat individual-level metrics as a governed surface: role-based visibility settings (from open to leaders-only to fully hidden), team-scoped views, and in the strongest documented case de-identification that redacts a person across all reports while keeping aggregates accurate — a posture documented for works-council and regional-law contexts. Product guidance in this category explicitly cautions against using the metrics for individual performance evaluation, and at least one product recommends assembling any such composite report outside the platform. The measurement system is designed for process improvement, and using it as surveillance is both a trust risk and — per the vendors' own guidance — a measurement-quality risk, because developers who know they are individually measured change their behavior.

### The metrics measure the process, not the output's value

A fast cycle time is not a good product; a large throughput is not a productive team. Products document their own metric limitations (deployment-dependent calculations, inflated coding time on long-lived branches, volatile small samples) and position the numbers as signals for conversation, not verdicts. The improvement loop — team-owned agreements, triage, retros — exists precisely because the numbers alone do not decide anything.

### Non-intrusion is a structural commitment

The record is assembled from tools engineers already use; engineers do not tag, timer, or report differently for the system's sake. This is what distinguishes the Type from time tracking and from manual reporting practices, and it is also why the data can go stale in exactly the places the org's own hygiene is weak (for example, unmapped tickets or misconfigured deployment detection).

## Variants

- **Delivery-flow-first** — organized around the pull-request pipeline and DORA-style delivery metrics, increasingly bundled with workflow automation and AI-code-review features; typical of mid-market-oriented products.
- **Enterprise engineering-management-first** — organized around resource allocation, investment distribution, and finance alignment (capitalization, R&D reporting); typical of large-org products with executive and finance audiences.
- **Developer-experience-first** — organized around recurring surveys, experience indices, and friction drivers, correlated with system metrics; often positioned by research pedigree and adopted by large platform-engineering organizations.
- **Team-trust-first** — organized around team-owned improvement (working agreements, team-level survey reporting, conservative individual visibility); typical of products whose adoption depends on developer goodwill.
- **Deployment/DORA-focused thin products** — narrow dashboards over deployment and change data; the same core at smaller scope.
- **Legacy individual-activity generation** — first-generation products centered on per-developer activity metrics; largely consolidated or sunset, but historically definitional for the Type.
- **Era-current extensions** (present across most current products, not definitional): AI-tool adoption/impact/cost measurement; software capitalization and R&D finance reporting; AI assistants over the data; adjacent platform features such as service catalogs and scorecards.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Code Quality Platform | owns the health of the **code** (issues, coverage, quality verdicts on changes); this Type owns the flow of the **work**. Quality signals may be ingested here, but code-health state lives there. |
| Business Intelligence Platform | generic data modeling and visualization over arbitrary organizational data; this Type ships an engineering-domain data model, dev-tool connectors, and predefined metric semantics. Custom-query surfaces inside some products mark the convergence seam, not a merger. |
| Engineering Project Management Platform | **plans and manages** the work (backlogs, sprints, assignments); this Type **observes** the work from tool data. Project-management tools are a data source here, not a competitor surface. |
| Software Delivery Governance Platform | enforces policy and compliance over delivery; this Type measures and explains. Policy automation features in some products are an edge drift, not the core. |
| Time Tracking Application | records self-declared or actively-tracked time; this Type derives process signals from the work's own systems without manual input. Auto-generated timesheets inside some products are derived output, not self-tracking. |
| People Analytics Platform | spans the whole workforce on HR data (engagement, attrition, performance); this Type is scoped to the engineering development process. HR systems appear here only as attribute and calendar sources. |
| Application Performance Monitoring / Observability | monitors production systems; this Type measures the development process. Incident tools feed it (recovery time, failure rate) but it never monitors production health. |
| Employee Survey / Engagement Platform | runs generic workforce surveys; this Type's surveys are engineering-specific (review latency, CI friction, tooling pain) and are read against system metrics. |
| Internal Developer Portal | serves platform engineering (service catalogs, scorecards, self-service); some products extend into this territory, but the measurement core is what defines this Type. |

The most important boundary is with the **Code Quality Platform**: both are "engineering analytics," but one answers "is the code healthy?" while the other answers "is the way we work healthy?" Confusing them produces documents about linting and coverage where delivery flow and investment were the subject.

## Representative Products

- **LinearB** — delivery-flow-first platform with automation and AI-impact measurement
- **Jellyfish** — enterprise engineering-management platform centered on allocation and finance alignment
- **Swarmia** — team-trust-first engineering intelligence with working agreements and surveys
- **DX** — developer-experience-first platform combining survey research with broad system analytics

The defining core was checked against the legacy generation (Pluralsight Flow, now discontinued) to avoid over-fitting the definition to current-era machinery such as surveys, AI measurement, and capitalization reporting.

## Sources

Research date: **2026-09-08**

- LinearB — product page https://linearb.io/ ; Help Center https://linearb.helpdocs.io/ (incl. "Cycle Time Metric", "LinearB: Core Concepts")
- Jellyfish — product page https://jellyfish.co/ ; "What is Allocation?" https://jellyfish.co/blog/what-is-allocation/
- Swarmia — product page https://www.swarmia.com/ ; documentation https://help.swarmia.com/ (incl. "Get started in 15 minutes", "Working agreements", "Roles and permissions")
- DX — product page https://getdx.com/ ; documentation https://docs.getdx.com/ (incl. "Concepts", "Onboarding", "Individual contributor metrics", "How should DX be used for performance assessment?")
- Appfire — Pluralsight Flow end-of-life notice https://www.pluralsight.com/product/flow

> Sourcing limitation: the Jellyfish help center requires login and its operational documentation could not be accessed on 2026-09-08. Claims about Jellyfish rest on its public product pages and one vendor blog post; no precise Jellyfish workflow or rule details are stated in this document. Metric formulas, numeric limits, and plan-specific capabilities are intentionally not stated here; they vary by product and change over time. Detailed product-by-product observations are recorded in the paired Research Notes.
