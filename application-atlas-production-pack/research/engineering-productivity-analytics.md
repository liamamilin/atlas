# Research Notes — Engineering Productivity Analytics

Research date: 2026-09-08
Slug: engineering-productivity-analytics
Directory leaf: Engineering Productivity Analytics (§12 Software Development & Product Engineering)

## Research Goal

Understand what an Engineering Productivity Analytics application actually is as a Type: what it ingests, what it computes, who it serves, how the measurement-to-improvement loop works, and where its boundaries sit against neighboring Types (code quality, BI, project management, delivery governance, time tracking, people analytics, observability).

## Initial Boundary Hypothesis

- Core use: continuously measure the engineering organization's development process (not the code, not the production system) from the tools where work happens, and give engineering leaders insight to act on.
- Primary users: engineering leaders (VPs, directors, managers, team leads); developers as data subjects and, in some products, as participants (surveys, team views).
- Nearest neighbors: Code Quality Platform (code health vs work flow), BI Platform (generic vs engineering-domain), Engineering Project Management Platform (manages work vs observes work), Software Delivery Governance Platform (policy vs insight), Time Tracking Application, People Analytics Platform, APM/Observability, Employee Survey Platform.
- Unknowns at start: whether developer surveys are definitional or common; whether allocation (FTE-based investment measurement) is core or variant; how individual-level metrics are governed; whether the category is stable enough to be one Type given naming drift.

## Research Questions

1. What data sources does the system ingest, and how does ingested data become a persistent record?
2. What are the core objects (teams, contributors, metrics, dashboards, goals, surveys)?
3. Which metric families are computed, and who owns the metric semantics (cycle-time boundaries, attribution)?
4. What surfaces do leaders vs developers see?
5. How is individual-level visibility governed (roles, opt-in, de-identification)?
6. How does the improvement loop work (goals, working agreements, triage, playbooks)?
7. Where are the boundaries against neighboring Types?

## Representative Products

Selected for market representation + documentation quality + different philosophies + different customer tiers:

| Product | Positioning (own words) | Philosophy / tier |
|---|---|---|
| LinearB | "engineering delivery optimization platform" / "engineering productivity platform" | delivery-flow-first + automation; mid-market to enterprise |
| Jellyfish | "Software Engineering Intelligence Platform" (earlier: "Engineering Management Platform") | enterprise engineering-resource management; allocation & finance alignment |
| Swarmia | "software engineering intelligence platform … with data they can trust and the tools to act on it" | developer-trust-first, team-owned improvement; startup to enterprise |
| DX | "Developer Intelligence Platform … designed by researchers" | developer-experience-first (survey-led) + platform; large enterprise |
| Pluralsight Flow (legacy sample) | (GitPrime lineage; individual/team activity analytics generation) | historical check only — acquired by Appfire 2025-02, EOL announced 2027-12-31, maintenance mode |

## Sources

Evidence layers: A = directly observed on an official source for a specific product; B = cross-product commonality; C = canonical inference.

Fetched 2026-09-08 (all Layer A unless noted):

- LinearB product page — https://linearb.io/
- LinearB Help Center — https://linearb.helpdocs.io/ (root + category index)
- LinearB, "Cycle Time Metric" — https://linearb.helpdocs.io/article/v9pckvmkbj-cycle-time
- LinearB, "LinearB: Core Concepts" — https://linearb.helpdocs.io/article/8tcpearzrv-core-concepts
- Jellyfish product page — https://jellyfish.co/
- Jellyfish, "What is Allocation?" (vendor blog, Tier 2/3) — https://jellyfish.co/blog/what-is-allocation/
- Swarmia product page — https://www.swarmia.com/
- Swarmia docs index (llms.txt) — https://help.swarmia.com/llms.txt
- Swarmia, "Get started in 15 minutes" — https://help.swarmia.com/getting-started/get-started-in-15-minutes.md
- Swarmia, "Working agreements" — https://help.swarmia.com/features/working-agreements.md
- Swarmia, "Roles and permissions" — https://help.swarmia.com/settings/organization/managing-users-and-roles.md
- DX product page — https://getdx.com/
- DX docs index (llms.txt) — https://docs.getdx.com/llms.txt
- DX, "Concepts" — https://docs.getdx.com/concepts.md
- DX, "Onboarding" — https://docs.getdx.com/onboarding.md
- DX, "Individual contributor metrics" — https://docs.getdx.com/ic-metrics.md
- DX, "How should DX be used for performance assessment?" — https://docs.getdx.com/knowledgebase/using-dx-for-performance-assessment.md
- Appfire, "Flow will be discontinued" (EOL notice) — https://www.pluralsight.com/product/flow

Source-access limitations:

- **Jellyfish Help Center (help.jellyfish.co) requires login** — operational documentation inaccessible. Jellyfish claims below rest on the public product pages and one vendor blog post (Tier 2/3). Assertion strength for Jellyfish operational detail is reduced accordingly; no precise Jellyfish workflow/rule claims are made.
- Pluralsight Flow product page is now only an end-of-life notice; no operational docs reachable. Used solely as a historical/legacy sample and for the EOL fact itself.
- Gartner Magic Quadrant for "Developer Productivity Insight Platforms" (2026) is cited only as reported by LinearB and Swarmia on their own pages (market-category naming evidence, not an independent source).

## Product Observations

### LinearB (Layer A)

- Self-description: connects Git provider + project management tool + (optional) incident system into "a unified view of how work moves from code → review → release → production", linking activity back to issues, epics, and services.
- Delivery pipeline model: Open → Merge → Release (a pull-request funnel); stages show where work gets stuck.
- Cycle Time = coding time + pickup time + review time + deployment time. Coding start = first commit or Jira "In Progress" transition (configurable). Only PRs deployed to production are included in full cycle time. Data sources: git commit metadata, PR creation/merge timestamps, review events, deployment logs, Jira workflow transitions.
- Tunable metric configurations: Jira-based coding start, production deployment detection, branch inclusion/exclusion rules, working-day exclusion. Normalization: AVG/P50/P75/P90 aggregation over completed PRs per time bucket.
- Documented metric limitations: requires successful production deployment; backfilled deployment data can adjust historical values; long-lived branches inflate coding time; inaccurate Jira transitions degrade coding start; small samples volatile. "Cycle Time measures delivery duration, not code quality."
- DORA metrics auto-calculated from Git/deployment/incident data: deployment frequency, lead time (cycle time), change failure rate, MTTR.
- Philosophy: "Action Over Insight" — Team Goals (turn DORA signals into trackable targets), bottleneck detection, AI code review, gitStream PR automations, AI adoption/impact tracking (claims detection of 50+ AI tools).
- Platform areas (product page): AI & Developer Productivity Insights; AI Code Reviews; DevOps Workflow Automation (policy-based PR routing/approvals/test enforcement); Developer Experience Optimization (delivery metrics + qualitative feedback + surveys + MCP); Executive Reporting & ROI (resource allocation, cost capitalization — "connect engineering costs—AI, people, projects and processes—to business results"); Developer Surveys.
- Help center structure: Getting Started; Platform Capabilities; Metrics Hub (94 articles); Integrations; gitStream; Administration; WorkerB (Slack/Teams notifications); AI & Automation; Role-Based Playbooks; Troubleshooting.
- Integrations: GitHub, GitLab, Bitbucket, Azure DevOps, Jira, Slack, Microsoft Teams, AI coding tools (Copilot, Cursor, Gemini, Claude, Amazon Q, Windsurf).
- Market category evidence: "Leader in the 2026 Gartner Magic Quadrant for Developer Productivity Insight Platforms" (self-reported).

### Jellyfish (Layer A for positioning/modules; operational detail limited — help center login-gated)

- Self-description: "turns your developer tool data into productivity insights that help R&D drive measurable impact"; "Engineering Intelligence Across Your SDLC".
- Product modules: AI Impact (adoption, token cost, impact insights, workflow optimization, vendor comparison, report builder); Operational Effectiveness (Metrics, Life Cycle Explorer, Workflow Analysis, People Management, Team Benchmarks); Business Alignment (Resource Allocations); DevEx (developer surveys); DevFinOps (software capitalization, R&D tax credits).
- Allocation concept (vendor blog): "the measurement of the distribution of a software engineering team's work across a number of axes" — features vs infrastructure vs bugs vs customer support, or custom frameworks (priority projects, product themes, business objectives). Measured in FTEs. Manual pre-platform practice: spreadsheets, time cards, dedicated analysts. Platform practice: "analyzes data from the tools your team already uses, without manual inputs… pulls together, cleans, normalizes, and links data from disparate sources… algorithms associate activity performed in your SCM with heuristic workflow data in Jira and other contextual data to accurately reconstruct the work effort of each team member."
- "Patented data model" and "Data Hub" named as platform components.
- Audiences: engineering executives, engineering managers, platform engineering, product leaders, finance teams, software developers.
- Integrations (product page): Git, GitHub, GitLab, Bitbucket, Azure DevOps/Boards/Repos, Jira, Linear, SonarQube, PagerDuty, Opsgenie, Jenkins, CircleCI, Google Calendar, Slack, Productboard/Aha!/ProductPlan, AI tools (Copilot, Gemini, Amazon Q, Cursor, Sourcegraph, Windsurf, Claude), Google Sheets.

### Swarmia (Layer A, rich docs)

- Self-description: "helps engineering leaders and their teams understand whether they're working on the right things, find what's holding them back, and keep getting better — with data they can trust and the tools to act on it."
- Onboarding ("Get started in 15 minutes"): sign up (Google/Microsoft/GitHub auth; Okta optional) → connect code hosting (GitHub Cloud/Enterprise, GitLab Cloud/Server) → connect issue tracker (Jira, Linear; also Azure Boards, Shortcut, GitHub Issues per settings docs) → connect messaging (Slack, Teams) → create teams (manual, GitHub import, or team API). Default sync: 1 year of code and issue tracker data. Contributor identities auto-merged across tools; reviewable in contributor settings.
- Data posture: "Swarmia collects the file names and sizes of commits from the source code. We do not store your source code." All org users can read metadata of all integrated repositories (documented caution).
- Feature areas (docs index): Focus (focus summary in FTEs; investment balance with activity-based and effort-based models; categorization with automatic categorization; initiatives; work log; sprints with scope increase/carryover); Metrics (code metrics: PR cycle time incl. time to first review/review time; change lead time vs PR cycle time distinction; DORA metrics with automatic change failure detection from rollbacks/reverts/hotfix filters; issue metrics; CI visibility; Explore; Key metrics pinned to the front page as a shared view); AI tools (adoption per tool, activity patterns, AI impact on code metrics, AI ROI, AI cost, cloud agents, review agents, automatic AI-tool detection); Signals (PR inbox; working agreements); Surveys (create/preview/duplicate/close/delete; responses reported by team; name display in comments optional); Software capitalization (auto-generated timesheets, approval, export); Swarmia AI; Developer overview; Notes; Forecast (Monte Carlo simulation of past effort).
- Working agreements: team-owned improvement commitments ("help you spring from idea to action, execute consistently, and form new habits"); after setup, insights + list of exceptions from the past two weeks; daily digest via Slack/Teams.
- Definitions documented: throughput (PRs per period), normalized throughput (per active FTE), batch size (changes per PR), issue cycle time, flow efficiency (active days / lifetime), scope creep; DORA set (change lead time, time to deploy, deployment frequency, MTTR, change failure rate).
- Attribution rule: historical team memberships tracked over time; "contributions made for one team will stay correctly attributed, even if their author later switches teams or leaves."
- Deployment detection options: from merged PRs (proxy), GitHub deployments, GitHub checks (CI), or deployment API (incl. monorepos).
- PR↔issue linking: multiple detection methods documented; test-file rules classify code vs test changes; org- and team-level PR exclusion filters.
- HR integrations: BambooHR, Merge.dev (Workday), CSV time-off upload — used to normalize effort (FTE) calculations.
- Roles: organization admin / editor / viewer (org-wide) + team admin (per team); permission table covering integrations, filters, investment breakdowns, contributor merge, initiatives, API tokens, survey creation, capitalization, team management, working agreements. SSO: GitHub, Google, Microsoft Entra, Okta.
- Export: CSV, Data Cloud, Export API; MCP server; APIs for reports/team management/time-off.
- Market category evidence: "Leader in the 2026 Gartner Magic Quadrant for Developer Productivity Insight Platforms" (self-reported).

### DX (Layer A, rich docs)

- Self-description: "Developer Intelligence Platform"; "engineering intelligence platform designed by researchers"; "Measure and improve software health, R&D productivity, and AI-human collaboration for a truly AI-Native SDLC."
- Core concepts (docs "Concepts" page):
  - Data connectors: "Integrations that pull data from your engineering tools—like GitHub, GitLab, Jira, PagerDuty, and CI/CD systems. Connecting tools lets DX correlate what developers say (in snapshots) with what systems show (in metrics)."
  - Team hierarchy: mirrors the org chart; teams roll up to parent teams; "managers see their team's results, directors see aggregated data across their org."
  - User linking: identity mapping across systems (email auto-link; manual usernames for some tools).
  - Attributes: DX-managed (tenure bands, AI usage levels), self-reported (during snapshots), admin-set (CSV/API/HR).
  - Core 4: Speed, Quality, Impact, Effectiveness (DXI).
  - Snapshots: short recurring surveys via Slack/Teams; most orgs run quarterly.
  - Drivers: topics impacting developer productivity (code maintainability, local iteration speed, CI/CD, documentation); developers rate drivers and vote on what slows them down; feed the DXI.
  - DXI: single 0–100 developer experience index from driver responses; baseline for quarter-over-quarter tracking; industry benchmarks.
  - System metrics: "quantitative data pulled from your connected tools—like PR cycle time, deployment frequency, and incident response time."
  - Workflows: measured time spent on tasks (waiting for review, debugging CI, local env setup) vs recommended targets/benchmarks.
  - Comments (qualitative, attachable to drivers/CSAT), Playbooks (research-backed improvement guides), Triage (manager sets per-driver status: keep monitoring / make improvements / needs support).
- Onboarding module: time to first PR, time to 10th PR (from SCM data), 90-day sentiment survey, experience index; benchmarks at P50/P75/P90; individual-level columns visible only to admin/privileged users.
- IC metrics governance (docs "Individual contributor metrics"): visibility settings per surface (reports, group dashboard, DX AI chat, AI transcripts) with a spectrum from "Everyone" through team-scoped and role-scoped options to "Nobody" (re-enabling requires DX support). De-identification: protected users redacted to "Hidden" across reports/dashboards/exports while aggregate metrics stay accurate; motivated by regional/policy requirements "such as a Works Council agreement"; drilldown text search also blocked; Data Studio (custom SQL) exempt from application-layer redaction and separately access-controlled with a compliance warning.
- Performance-assessment guidance (KB): individual metric-based evaluation is "sensitive and often problematic"; recommends composite "Performance Index" reports be built in spreadsheets outside the platform, combining DX exports with peer feedback/HR data; "metrics never tell the full story"; compare like-for-like peer groups; keep confidential.
- Reports (docs index): DORA metrics; allocation (Jira/Azure DevOps/Linear with categorization rules); PR throughput; sprint/iteration analytics (completion, predictability, spillover, volatility); AI adoption/cost/impact/code-percentage; cohort analysis; scenario planner; custom SLAs.
- Administration: roles, permissions, access control, team hierarchies, directory sync (Okta, Workday RaaS), SSO (SAML/OIDC/Atlassian), SCIM, benchmarks, PHI-usage guidance.
- Connectors (docs index, ~80): VCS (GitHub, GitHub Enterprise, GitLab, Bitbucket Cloud/Data Center, Azure DevOps, Gerrit), issue trackers (Jira Cloud/DC, Linear, Asana, ClickUp, Shortcut, GitHub Projects, Azure Boards), CI/CD (GitHub Actions, CircleCI, Buildkite, Harness, Bitbucket/GitLab Pipelines, Vercel), incident (PagerDuty, Opsgenie, Rootly, Firehydrant, incident.io, Datadog Incident Management, ServiceNow), calendars (Google, Outlook), AI tools (Copilot, Cursor, Claude Code, Gemini CLI, Codex, Devin, Tabnine, Sourcegraph Amp/Cody, Amazon Q/Kiro, Augment), quality/security (SonarQube/Cloud, Snyk, Wiz, Checkmarx, GitHub Security), observability (NewRelic, Datadog SLOs, Sentry, Rollbar, Sumo Logic, Coralogix), feature flags/analytics (LaunchDarkly, Statsig), HR (Workday), docs (Confluence).
- Data Cloud API: deployments.create, incidents.upsert, pipelineRuns.upsert, customMetrics.push, aiToolMetrics.push — programmatic ingestion for anything without a connector.
- Platform extensions: Software Catalog, Scorecards, Developer Self-service, PlatformX, DX AI chat, MCP, Terraform provider.

### Pluralsight Flow (legacy sample; Layer A for EOL facts only)

- Product page is an end-of-life notice: Appfire acquired Flow from Pluralsight in February 2025; Flow retires December 31, 2027; maintenance mode; no new feature requests; renewals ended June 30, 2026.
- Historical significance: Flow is a representative of the first generation of this Type. Its feature-level characterization (VCS + issue-tracker integrations, computed activity/flow metrics, team and individual dashboards with privacy controls) is **background context from model memory, not verified from fetched sources this pass** — the fetched page is only the EOL notice. It is used solely to argue the Type predates current-era machinery; no operational claim in the final document rests on it. The historically load-bearing evidence is instead the Jellyfish blog's own documentation of the pre-platform manual practice (spreadsheets, time cards) as the state the category replaced.

## Cross-product Comparison

| Dimension | LinearB | Jellyfish | Swarmia | DX | Verdict |
|---|---|---|---|---|---|
| Ingests dev-tool data continuously | Yes (Git/PM/incident) | Yes (SCM/Jira/CI/incident/calendar) | Yes (Git/issue tracker/messaging/HR) | Yes (~80 connectors + push API) | **Core (B)** |
| Persistent activity record + backfill | Yes (backfill documented) | Yes (implied by data model; docs gated) | Yes (1-year default sync) | Yes (backfill guides) | **Core (B)** |
| Defined process metrics over the record | Yes (Metrics Hub, cycle-time decomposition) | Yes (metrics, life cycle explorer) | Yes (definitions pages) | Yes (system metrics, Core 4) | **Core (B)** |
| Team/org modeling with roll-ups | Yes (teams) | Yes (teams) | Yes (teams, sub-teams, historical membership) | Yes (team hierarchy mirroring org chart) | Common mature (B) |
| Contributor identity resolution across tools | Yes (implied by integrations) | Yes (implied) | Yes (auto-merge, reviewable) | Yes (user linking, documented) | Common mature (B) |
| DORA metric set | Yes (auto-calculated) | Yes (metrics module) | Yes (with change-failure detection) | Yes (DORA reports) | Common mature (B) |
| Cycle-time decomposition into phases | Yes (coding/pickup/review/deploy) | Yes (life cycle explorer) | Yes (PR cycle time, time to review) | Yes (lifecycle by phase) | Common mature (B); exact phase boundaries vary per product |
| Investment/allocation breakdown | Yes (resource allocation, cost capitalization) | Yes (allocation in FTEs — flagship) | Yes (investment balance, activity vs effort models) | Yes (allocation reports + categorization rules) | Common mature (B); depth varies |
| Developer-experience surveys | Yes (developer surveys) | Yes (DevEx module) | Yes (surveys; team-reported results) | Yes (snapshots, DXI, drivers) | Common mature (B) — 4/4 current sample; absent in first generation (Flow) |
| Improvement loop (goals/agreements/triage) | Yes (Team Goals) | Partial evidence (workflow optimization) | Yes (working agreements + digests) | Yes (triage + playbooks) | Common mature (B); form varies |
| Benchmarks | Yes (benchmarks report) | Yes (team benchmarks) | Yes (benchmarks & comparisons) | Yes (industry benchmarks P50/P75/P90) | Common mature (B) |
| Chat-surface delivery (Slack/Teams) | Yes (WorkerB) | Yes (Slack integration) | Yes (digests, notifications) | Yes (surveys, bots) | Common mature (B) |
| Individual-level metrics | Governed (role playbooks; not emphasized) | Yes (people management; docs gated) | Yes (developer overview; team-level survey reporting) | Yes (IC metrics with 6-level visibility + de-identification) | Common mature (B); governance posture is a variant axis |
| AI-tool measurement | Yes (50+ tools claim) | Yes (AI Impact module) | Yes (adoption/activity/impact/cost) | Yes (AI measurement suite) | Era-current standard capability (B) — absent pre-2023 |
| Software capitalization / finance reporting | Yes (cost capitalization) | Yes (DevFinOps) | Yes (capitalization + timesheets) | Yes (R&D capitalization) | Era-current extension (B) — 4/4 current sample, absent in first generation |
| Dashboards/reports as primary surface | Yes | Yes | Yes | Yes | **Core (B)** |
| Roles/SSO | Yes (administration category) | Yes (enterprise security) | Yes (4 roles, table) | Yes (roles, SCIM, SSO) | Common mature (B) |
| Automation of the work itself | Yes (gitStream PR automations, AI code review) | No (insight-only posture) | No (signals only) | No (insight + enablement catalog) | Vendor-specific / edge drift (A) |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The engineering activity record of record.** A persistent, continuously updated record of the organization's software development activity, assembled from the systems where the work happens — version control, issue trackers, CI/CD, incident tools — without changing how engineers work. Remove → there is nothing to measure; the product degenerates into a survey tool or a manual reporting exercise.
2. **Derived process metrics with defined semantics.** Measures computed over that record — delivery flow (cycle time, throughput, deployment frequency), quality-of-process (change failure, rework), and investment distribution — each with explicit, inspectable definitions. Remove → raw event feed / data lake; the "analytics" is gone.
3. **The engineering-management insight surface.** Dashboards and reports through which the people responsible for how engineering works (team leads through VPs) review trends over time, compare teams and periods, and drive action. Remove → a metrics pipeline/API with no management surface; not recognizable as this Type.

Jointly-held is load-bearing:
- 1 alone = data pipeline / warehouse feed
- 2 without 1 = one-off calculator
- 3 without 1+2 = generic dashboarding (BI territory)
- 1+2 without 3 = metrics API, not an analytics application

### L1 — Common Mature Structure (very common, not definitional)

- Team/org modeling (teams, hierarchy, roll-ups) as the unit of measurement
- Contributor identity resolution across connected tools
- DORA metric set as a packaged, benchmarkable view
- Cycle-time decomposition into named phases (exact boundaries vary by product)
- Investment/allocation breakdown (features vs maintenance vs bugs vs other; FTE-based in mature implementations)
- Developer-experience surveys (recurring, team-reported) correlated with system metrics
- Industry benchmarks (percentile comparisons)
- Improvement-loop machinery (goals/targets, working agreements, triage, playbooks)
- Chat-surface delivery (Slack/Teams digests, notifications, survey delivery)
- Historical backfill from connected tools
- Roles/permissions, SSO, audit posture
- Data export/API (and, era-current, MCP)
- Era-current standard capabilities: AI-tool adoption/impact/cost measurement; software capitalization / R&D finance reporting (both 4/4 in the current sample, both absent in the first generation — era markers, not definitional)

### L2 — Variant / Optional Structure

- Posture: delivery-flow-first (LinearB) vs enterprise resource-management-first (Jellyfish) vs developer-experience-first (DX) vs team-trust-first (Swarmia) vs DORA/deployment-focused thin products
- Allocation modeling depth: activity-based vs effort-based (FTE) models; custom category taxonomies
- Individual-level visibility posture: open → team-scoped → role-scoped → nobody; de-identification for works-council/regional requirements
- Survey depth: one-off polls → recurring snapshots with indices and driver models
- Onboarding/ramp-up analytics (time-to-first-PR class metrics)
- Forecasting (e.g., Monte Carlo on past effort)
- HR-system integration (time-off normalization, attributes)
- Deployment-detection method (PR-merge proxy, CI checks, platform deployment events, API)
- Self-hosted/private deployment options; support for self-hosted VCS
- Adjacent platform extensions (software/service catalogs, scorecards, internal developer portal features) — drift zone toward Internal Developer Portal territory

### L3 — Vendor-specific (research notes only)

- LinearB: gitStream (PR workflow automation), WorkerB (chat notifications), "APEX framework", 50+ AI-tool detection claim, cost-capitalization reports framing
- Jellyfish: "patented data model", DevFinOps branding, AI Assistant, Scenario Planner, Life Cycle Explorer naming
- Swarmia: working agreements as branded feature, Focus summary, WBSO timesheet approval (Dutch R&D tax incentive), Monte Carlo forecast, "Build" book, "we do not store source code" posture
- DX: DXI (0–100), Core 4 framework, TrueThroughput™, DevSat, PlatformX, Experience Sampling, Playbooks/Triage statuses, Software Catalog/Scorecards, "designed by researchers" positioning, CAFE(S) framework

## Vendor-specific Findings

- Only LinearB among the sample automates the delivery work itself (PR routing/approval policy automation, AI code review). This drifts toward Software Delivery Governance / automation territory and is not part of the Type's core.
- Only DX documents a formal de-identification mechanism tied to works-council agreements and a "build performance reports outside the platform" guidance — the strongest documented individual-privacy posture in the sample.
- Only Swarmia documents the "metadata not source code" data-access posture explicitly.
- Jellyfish is the only sampled product whose flagship framing is financial (allocation in FTEs, DevFinOps, R&D tax credits) — consistent with its enterprise/finance-audience positioning.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| Code Quality Platform | adjacent, data exchanged | Quality platform owns the health of the **code** (issues, coverage, ratings, verdicts on changes); EPA owns the flow of the **work** (people/process/time). EPA ingests quality signals (SonarQube connectors observed) but does not own code-health state. Remove EPA's people/flow subject → it becomes a code-quality platform. |
| Business Intelligence Platform | adjacent, converging at the edges | BI models arbitrary organizational data with generic query/visualization; EPA ships an engineering-domain data model, dev-tool connector fabric, and predefined metric semantics. DX's Data Studio (custom SQL) shows the convergence seam; the built-in engineering model + connectors is what keeps EPA distinct. Remove the engineering-domain model → generic BI. |
| Engineering Project Management Platform | upstream, data source | PM platforms **plan and manage** the work (backlogs, sprints, assignments); EPA **observes** the work from tool data. EPA ingests from PM tools; EPA initiatives/forecast features drift toward PM but don't manage work. Remove observation-from-tools → project management. |
| Software Delivery Governance Platform | adjacent, policy vs insight | Governance enforces policy/compliance over delivery; EPA measures and explains. LinearB's policy-based PR automation is an edge drift; its core remains measurement + improvement guidance. Remove measurement subject → governance/automation. |
| Time Tracking Application | adjacent, signal source | Time tracking records self-declared/active time; EPA derives process signals from the work's own systems without manual input. Swarmia's auto-generated timesheets (for capitalization) blur the edge but are derived, not self-tracked. Remove tool-derived derivation → time tracking. |
| People Analytics Platform | sibling under HR | People analytics spans the whole workforce (HRIS data, engagement, attrition); EPA is scoped to the engineering development process. EPA connects HR systems for attributes/time-off but its subject is engineering work. Remove the engineering-process subject → people analytics. |
| APM / Observability | different subject entirely | Observability monitors production systems; EPA measures the development process. Incident tools feed EPA (MTTR, change failure) but EPA never monitors production health. |
| Employee Survey / Engagement Platform | adjacent, survey overlap | Engagement platforms run generic workforce surveys; EPA's surveys are engineering-specific (drivers like CI/CD, review latency) and are correlated with system metrics ("correlate what developers say with what systems show"). Remove the system-metric correlation → survey platform. |
| Internal Developer Portal / IDP | adjacent extension zone | Some EPA products add catalogs/scorecards/self-service (DX). The catalog/portal surface serves platform engineering; EPA's core remains measurement. |

"Remove what to become the other Type" summary: remove the work-flow subject → code quality; remove the engineering-domain model → BI; remove observation (add management) → project management; remove insight (add enforcement) → delivery governance; remove tool-derivation → time tracking; remove the engineering scope → people analytics; remove the process subject → observability.

## Historical / Market-Sample Check

- First-generation products (Pluralsight Flow lineage; feature characterization per the background-context note above, not freshly verified): VCS + issue-tracker integrations, computed flow metrics, team/individual dashboards — consistent with all three L0 legs and with **no** DORA packaging, surveys, AI measurement, or capitalization. Treated as a consistency check, not a load-bearing leg. ✓
- Pre-software practice (documented by Jellyfish's own blog as the pre-platform baseline): engineering leaders manually aggregating SCM/Jira data into spreadsheets, sometimes with time cards, to compute allocation — satisfies the measurement intent but not the continuous automated record (periodic manual compilation). Thin ancestor, correctly excluded from the Type while confirming the need the Type serves. ✓ (load-bearing historical evidence)
- Naming drift across a decade: "Engineering Management Platform" (Jellyfish ~2021) → "Software Engineering Intelligence" (Jellyfish current) → "engineering intelligence platform" (Swarmia) → "Developer Intelligence Platform" (DX) → "engineering productivity platform" (LinearB) → Gartner category "Developer Productivity Insight Platforms" (2026, as reported by two sampled vendors). The directory leaf name "Engineering Productivity Analytics" is one label among many for the same stable underlying Type. ✓
- The check confirms the L0 is not over-fitted to the current AI-era implementation: AI measurement, surveys, and capitalization are all era-current additions sitting above a stable three-leg core.

## Uncertainties

- Jellyfish operational workflows (team setup, metric configuration, permission model) unverified — help center login-gated. All Jellyfish-specific operational claims are withheld; only positioning/module/allocation-concept claims are made.
- Exact metric formulas differ per product and change over time (Swarmia documents an effort-model change in August 2026); no cross-product metric equivalence is claimed.
- Market-size / adoption figures (e.g., "50+ AI tools detected", customer counts) are vendor claims, not independently verified; not used in the final document beyond clearly attributed positioning.
- Whether thin DORA-only dashboards (not sampled this pass) would satisfy L0 leg 3 fully — reasoned yes (they present metrics for management review), but not directly evidenced; kept out of representative products.
- Open-source data-layer products (e.g., Apache DevLake-class) were not sampled; their fit as a variant is reasoned, not observed.

## Final Synthesis

An Engineering Productivity Analytics application is the engineering organization's measurement system for its own work process. Its defining core is three jointly-held structures: a continuously maintained record of development activity assembled from the organization's own tools (version control, issue trackers, CI/CD, incident systems); derived process metrics with explicit semantics computed over that record (delivery flow, quality-of-process, investment distribution); and an insight surface through which engineering management reviews trends, compares teams and periods, and drives improvement. Around this core, mature products add team/org modeling, contributor identity resolution, the DORA metric set, cycle-time decomposition, allocation in FTEs, developer-experience surveys correlated with system metrics, benchmarks, improvement-loop machinery (goals, working agreements, triage), chat delivery, backfill, governance (roles, SSO, individual-visibility controls), and — as era-current capabilities — AI-tool measurement and software-capitalization reporting. The Type is distinct from code quality (code health vs work flow), BI (generic vs engineering-domain), project management (manages vs observes), delivery governance (insight vs enforcement), time tracking (self-declared vs tool-derived), people analytics (HR-wide vs engineering-scoped), and observability (production vs process). The Type predates its current-era machinery: first-generation products satisfied the core without surveys, DORA packaging, AI measurement, or capitalization.
