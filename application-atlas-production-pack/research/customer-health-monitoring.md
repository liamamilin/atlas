# Research Notes — Customer Health Monitoring

## Research Goal

Understand **Customer Health Monitoring** as an Application Type: what its defining core is, how health is defined and computed, who operates it, what the monitoring loop looks like, and where its boundaries sit against the dense §07 neighbor cluster — especially **Customer Success Platform** (unprocessed sibling), **Product Usage / Adoption Platform** (processed), **Renewal Management Platform** (processed), **Customer Feedback Management** (processed), and CRM.

## Initial Boundary

Working hypothesis carried in: the Type is the vendor-side standing watch over its own customer accounts — multiple customer signals aggregated into a per-account health measure (score/rating), evaluated against thresholds, surfaced when adverse. The market term of art is "customer health score / health scoring"; "monitoring" captures the standing, ongoing character.

Known risks going in:

1. **Module-convergence risk**: health scoring is embedded in essentially every customer success platform. The leaf risks being judged a module of Customer Success Platform (same risk renewal-management-platform recorded).
2. **Confusion with usage analytics**: product usage is the most common health input; the usage-platform leaf already recorded this seam.
3. **Pure-play question**: whether standalone health-monitoring products exist apart from CS platforms.

## Research Questions

1. What is the unit of record — what exactly is "monitored"?
2. What is the health measure — score, rank, status? What scale?
3. How is health defined — who configures it, from what signals, with what aggregation machinery?
4. What signals feed health in practice (usage, support, sentiment, commercial, engagement)?
5. How does the monitoring loop work — cadence, thresholds, alerts, actions?
6. What surfaces do users work in (account level, portfolio level, configuration)?
7. How is history/trend handled?
8. How do hierarchies (parent/child accounts) roll up?
9. Where do manual/subjective inputs fit?
10. What are the boundaries vs Customer Success Platform, usage platform, renewal management, CRM, BI?

## Representative Products

| Product | Positioning | Segment | Evidence tier |
|---|---|---|---|
| **Gainsight (NXT Scorecards)** | enterprise CS suite; Scorecard is its health machinery | enterprise | Tier-1 help center (3 articles fetched) |
| **Totango** | mid-market CS platform; health profiles with two models; "Customer Health Console", "My Business \| Risk + Health" | mid-market | Tier-1 help center (4 articles fetched) |
| **Planhat** | modern CS platform; additive 0–10 health score | mid-market/enterprise | Tier-1 help center (2 articles fetched + collection listing) |
| **Catalyst** | modern mid-market CS platform (now Totango-owned); input→group→account scoring | mid-market | Tier-1 help center (1 article fetched + Health section listing) |

Rejected/abandoned samples (source-access limitation): **ChurnZero** (transport errors ×2), **Vitally** (empty responses ×2), **HubSpot** (KB search empty shell + 404 on guessed article), **ClientSuccess** (transport error). No standalone pure-play health-monitoring vendor was verified this pass; the reachable market is CS platforms with health machinery at their core.

## Sources

- Gainsight — Scorecards Overview: https://support.gainsight.com/gainsight_nxt/05Scorecards/01About/Scorecards_Overview
- Gainsight — Calculation of Measure Group Scores and Overall Score: https://support.gainsight.com/gainsight_nxt/05Scorecards/02Admin_Guides/Calculation_of_Group_Scores_and_Overall_Scores
- Gainsight — Use Scorecard Data in Rules and Reports: https://support.gainsight.com/gainsight_nxt/05Scorecards/02Admin_Guides/Use_Scorecard_Data_in_Rules_and_Reports
- Totango — Analyze health at the account level: https://support.totango.com/hc/en-us/articles/360032136152-Analyze-health-at-the-account-level
- Totango — Configure profiles for multidimensional health: https://support.totango.com/hc/en-us/articles/4410017625748-Configure-profiles-for-multidimensional-health
- Totango — Best practices for designing health profiles: https://support.totango.com/hc/en-us/articles/202301749-Best-practices-for-designing-health-profiles
- Totango — Manage your book by risk + health: https://support.totango.com/hc/en-us/articles/37966349334804-Manage-your-book-by-risk-health
- Planhat — How Health is Calculated: https://help.planhat.com/en/articles/9590704-how-health-is-calculated
- Planhat — Health Scores: What You Can Include: https://help.planhat.com/en/articles/9587239-health-scores-what-you-can-include
- Planhat — Health Scores collection listing: https://help.planhat.com/en/collections/9801519-miscellaneous
- Catalyst — Monitor customer health: https://help.catalyst.io/hc/en-us/articles/28924640472980-Monitor-customer-health
- Catalyst — Health section search listing: https://help.catalyst.io/hc/en-us/search?query=health+score

Research date: **2026-09-08**. All fetched pages are official vendor help centers (Tier 1).

## Product A — Gainsight (Scorecards)

### Key observations (Layer A unless noted)

- Framing: "proactively monitor your customer's vital signs, usage trends, and other important dimensions… track multiple dimensions of a customer's health."
- **Unit of record**: a **Scorecard** attached to a **Company** or **Relationship** entity. Multiple scorecards can exist; only one is **active** per company/relationship at a time.
- **Structure**: Scorecard = collection of **Measures** and **Measure Groups**. Measure = one dimension of customer health (examples given: Product usage, Customer Support, Renewal Chances, Product Bugs). Measure Group = similar measures grouped (e.g., "Support group" containing Age of tickets, Severity of tickets).
- **Scores**: set per measure **manually or automatically through Rules Engine**. Grading schemes: **number, letter, or color**; score ranges define bands (example: 0–50 Poor, 51–75 Average, >76 Very Good).
- **Aggregation**: Measure Group score = weighted average of measure scores (weights configurable); Overall Score = weighted by percentile contribution. Color/grade schemes display the range average on hover while the numeric value drives calculation.
- **Admin configuration** (Administration > Scorecard): measures, groups, grading scheme, **weights, exceptions, validity period**.
- **End-user consumption**: Scorecard section on the **C360** (customer 360) page; Relationship scores on **R360**. End users may modify scores for **subjective/manual measures** (e.g., sentiment) when configured as Manual.
- **Action loop** (Rules Engine): documented scenario — extract Current Score + Previous Score, compute a "Decreased Score" expression, and **create a CTA (Call to Action) whenever the health score drops**, to notify the CSM. Tutorial also exists: "Create CTA when Measure Label is Red."
- **History**: **Scorecard Fact object** holds Current Score and Previous Score per company; **Scorecard History object** holds historical scores — weekly snapshot frozen at end of week, monthly snapshot at end of month.
- **Reporting**: standard reports (view-only, on Scorecard Fact / History / Unified Fact objects) and **Mass Edit reports** (admin can bulk-edit scores); Scorecard Widgets for dashboards.
- **AI**: "AI Scorecards / Scorecard Optimizer" (beta) — optimize scorecards; setup depends on Renewal Center data (i.e., optimization against renewal outcomes).
- Example measures seen in calculation docs: Number of support tickets, Avg time to resolve ticket, Frequency of tickets logging, CSAT, Customer Loyalty Index, Average Resolution Time, First Contact Resolution Rate, Customer Health Score.

## Product B — Totango

### Key observations (Layer A)

- Framing: "Customer health allows you to view a snapshot of how your customer is doing, according to a pre-defined 'ideal' profile. You can also look back at health snapshots over time."
- **Health rank** color-coded throughout: **Good** (on track) / **Average** (off track or recovering) / **Poor** ("typically requires action").
- **Two health models** (one active at a time): **Account health** (attribute-based rank) and **Multidimensional health** (rank + numeric **0–100** score).
- **Multidimensional model**: **dimensions** (e.g., "Usage") contain **attributes/metrics**; dimension weights and metric weights each sum to 100%; weighted-average scoring (Good=100, Average=60, Poor=0 points); admin sets **score ranges** for good/average/poor; option to **exclude metrics with no values** (weights redistributed proportionally) or include them.
- **Health profiles**: multiple profiles, each scoped by **segment criteria** (e.g., customer journey stage = onboarding, account type, product), **account type/hierarchy level**, and product; **ordered precedence** — most restrictive first, default profile last; accounts not matching any profile show **"unknown health"** (also cancelled accounts).
- **Cadence**: health **calculated daily**; weekly period color computed from last day of period week; recalculation on profile updates; **retroactive historical recalculation** available.
- **Account-level surface**: health widget on account profile — overall health, profile name, expandable conditions/dimensions with weights, **timeline** with hover points (icons mark contract-value changes and profile changes).
- **Hierarchy**: "enterprise calculation" — parent-level health combined from child profiles (rollup options).
- **Portfolio surfaces**: aggregate health in **segment summary**; **Customer Health Console** across team portfolios; **My Business | Risk + Health** page — tiles (average health score + contract value; accounts in poor health % + contract value; average health of accounts in renewal), **health over time** charts (average score, contract value in poor health, threshold distribution), **health breakdown by dimension**, **contract value by poor-health dimension**.
- **Signal design guidance** (best-practices article): common health indicators grouped as **Product usage** (license utilization, # logins), **Engagement** (last touch in x days, success plan exists), **Service** (% of paid tier, # products), **Satisfaction** (risk status, CSM sentiment), **Support** (# open tickets, billing status). Good column = AND criteria; Poor column = OR criteria; neither = average.
- **CSM Sentiment** attribute: subjective manual input by the account owner (None/Low/High/Critical), with a protocol expectation for regular updates.
- **Survey data caution**: NPS/CSAT measured at user level; aggregation to account level "challenging" and can obscure champions vs general users — balance carefully.
- **Usage data caution**: usage must be materialized as account-level custom metrics; choose impactful/actionable, benchmarkable metrics; beware "change in" operators on small numbers.
- **Trend noise control**: currency threshold setting to ignore small contract-value changes (e.g., FX noise).
- **Purpose framing**: "the purpose of health scores is to *communicate the reason* behind the score so that your team has *a clear path for action*." Design principles: simple, predictive, actionable.
- **Governance**: avoid daily/weekly profile adjustments; tune periodically (30 days after rollout, after product changes, after business-model changes); communicate changes in advance.
- Health attributes usable as **segment filters/columns** (health rank, 0–100 score, per-dimension score/rank) — i.e., health drives segmentation and downstream workflows.

## Product C — Planhat

### Key observations (Layer A)

- **Scale**: health calculated on **0–10**, **5 = neutral starting point**; factors **add or subtract health points** per the Health Profile configuration; final score clamped to 0–10.
- **Factors**: examples — Average Daily Logins, NPS Score, "low usage", "last contacted", industry, contract size, tenure. Recommended **2–8 factors** ("plenty").
- **Purpose framing**: decide what the score is for — **churn-risk indicator** (most common) or **upsell-opportunity indicator**; "do not include 'upsell opportunity' in the same scale as your churn prediction… create another, separate, Health Score." Predictive factors (industry, contract size, tenure) vs **actionable** factors (low usage, low NPS, last contacted) — actionable factors are ones the CSM can affect.
- **AI factor**: **conversation sentiment** from emails/chats/call transcripts aggregated at Company/End User/User level, score **−100 to +100**, usable as a health factor (example: linear, −100→100 mapped to −1→+1 impact).
- **Group rollup**: **group-level Health Score = mean average** of the companies in the group (worked example: parent = mean of children, rounded).
- **Configuration surfaces**: "Set up your Health Score Profiles", "Setting Up Your Health Factors", "Configuring Health Scores and Success Units in upgraded Planhat"; **trending** health scores article exists.
- Collection placement: Health Scores live under "Miscellaneous" in the help center — health is a core data feature of the platform rather than a separately marketed module.

## Product D — Catalyst

### Key observations (Layer A)

- Framing: "Customer health gives you insight into how a customer is doing according to an 'ideal' profile."
- **Account object fields**: the ultimate account score maps to two core fields on the account object — `Health` (**Health / At Risk / Neutral** picklist) and `Numeric Health Score` (calculated from input scores and group scores within each profile).
- **Scoring hierarchy**: **inputs → groups → account**. Input scoring for numeric and non-numeric fields; group score = **highest input score** in the group; account score = weighted value of all group scores. Null-value exclusions at input level (release note).
- **Diagnostic emphasis**: Catalyst **scores the "most impactful field"** (highlighted in a distinct color) — "the input that is bringing the account score down the most. Focusing on improving this input would have the biggest impact."
- **Profiles**: "Configure health profiles" — segment-based; **Overrides tab** to define health score overrides; accounts carry the weighted health score at the time they left a segment.
- **Monitoring surfaces**: **Current health module** (detail + trend per account on object layouts), **field module** (hover for detail/trend), **segments** (filter + columns), **aggregates module** (health break-down chart Health/Neutral/At Risk; click into the chart to list accounts per status).
- **Integration**: "Sync Catalyst health to Salesforce" — health scores written back to CRM (with sync-interval caveat that values may differ transiently).
- **API**: `/health_scores` endpoint including group and input scores, with `score_updated_at` (release note).
- Related monitoring surfaces: "Monitor customer expansion signals", "Monitor customer journey progress" — health is one of several standing monitoring lenses.

## Cross-product Comparison

| Dimension | Gainsight | Totango | Planhat | Catalyst |
|---|---|---|---|---|
| Unit of record | Scorecard on Company/Relationship | Health profile applied per account | Health Score per Company | Health profile per account |
| Health measure | Overall score + per-measure/group scores; numeric/letter/color schemes with ranges | Rank (Good/Average/Poor) or 0–100 score (two models) | 0–10 score, 5 neutral | `Health` picklist (Health/At Risk/Neutral) + numeric score |
| Aggregation machinery | Measures → Measure Groups → Overall; weights; exceptions; manual or Rules Engine scores | Attributes with good/poor criteria (AND/OR) → dimensions → weighted overall; no-value handling | Factors add/subtract points; linear ranges | Inputs → groups (max input) → weighted account score; null exclusions |
| Profile segmentation | Multiple scorecards, one active per company | Multiple profiles by segment criteria + precedence order | Health Score Profiles | Profiles by segment + overrides |
| History/trend | Fact (current/previous) + History object; weekly/monthly frozen snapshots | Health timeline; weekly period color; retroactive recalc | Trending health scores | Detail + trend on modules; `score_updated_at` API |
| Portfolio views | Scorecard widgets, reports | Segment summary, Customer Health Console, My Business Risk+Health page | Group structures | Aggregates module (breakdown chart), segments |
| Hierarchy rollup | Company/Relationship scorecards | Enterprise calculation (parent from children) | Group mean | (not fetched) |
| Manual/subjective input | Manual measures (e.g., sentiment) editable by CSM | CSM Sentiment (None/Low/High/Critical) | (not observed) | (not observed) |
| Action loop | Rules Engine → CTA on score drop / red label | Health ranks trigger tasks/notifications; health as segment filter | Health factors feed workflows/automations | Most-impactful-field highlight; workflows; Salesforce sync |
| AI | Scorecard Optimizer (beta) | — | Conversation-sentiment factor | — |

### Cross-product commonalities (Layer B)

1. **Monitored population = the vendor's own customer accounts** (companies/relationships), held as standing records.
2. **Health is a defined, not measured, quantity**: an admin-configured definition (profile/scorecard) maps underlying signals to a per-account health state. All four products center a configuration surface (Scorecard admin / Health Designer / Health Score Profiles / health profiles).
3. **Multi-signal aggregation**: usage, support, satisfaction/sentiment, engagement, commercial/billing signals are the recurring input families; the mix is customer-defined.
4. **Dual representation**: a numeric score and/or a banded rank (red/yellow/green-class; Good/Average/Poor; Health/At Risk/Neutral). Bands are threshold evaluations of the score or of attribute criteria.
5. **Standing, recurring computation** with history: daily calculation (Totango), weekly/monthly frozen snapshots (Gainsight), trend views everywhere.
6. **Monitoring surfaces at two levels**: per-account health view (widget/module with detail + trend) and portfolio/book views (consoles, breakdown charts, contract-value-weighted views).
7. **Action orientation**: health exists to drive action — "Poor… typically requires action" (Totango), CTA creation on score drop (Gainsight), most-impactful-field diagnosis (Catalyst), actionable-factor design guidance (Planhat).
8. **Segment-scoped health definitions**: different health standards for onboarding vs adoption, enterprise vs mid-market, per product.
9. **Hierarchy rollups** where account hierarchies exist.
10. **Health as data**: health attributes usable as filters/columns/fields in segments, reports, CRM sync, APIs.

## Canonical Model (Layer C — canonical inference)

Three jointly-held structures:

1. **The monitored customer account population** — the vendor's own customers held as identified accounts under standing monitoring. Remove → generic analytics/BI with nothing institutional to watch.
2. **The account-level health measure** — a persistent health state per account (numeric score and/or banded rating), produced by a **customer-defined health definition** that aggregates multiple underlying customer signals (weights/criteria/ranges), recomputed on an ongoing cadence and retained as history. Remove → raw signal feeds/dashboards, or a single-metric tracker.
3. **The monitoring loop** — health evaluated against configured thresholds/bands so adverse health is classified and surfaced for attention (at-risk flags, alerts, triggered tasks/plays, review queues, diagnostic emphasis). Remove → periodic batch scoring/reporting; the "monitoring" is gone.

Jointly-held is load-bearing: (1) alone = account list; (2) without (1) = metric calculator; (2) without (3) = scoring/reporting, not monitoring; (3) without (2) = alerting over raw metrics with no standing health state.

## L0 / L1 / L2 / L3

### L0 — Defining Invariant

- monitored customer account population (vendor's own customers as standing identified accounts)
- account-level health measure (persistent, multi-signal, customer-defined aggregation, recurring computation, history)
- monitoring loop (threshold/band evaluation surfacing accounts needing attention)

### L1 — Common Mature Structure

- weighted/grouped aggregation machinery (measures→groups→overall; dimensions; inputs→groups)
- segment-scoped health profiles with precedence (journey stage, account type, product)
- dual numeric-score + banded-rank representation with configurable ranges
- health history/trend (snapshots, timelines, frozen periods)
- portfolio/book monitoring views (breakdowns by dimension, contract-value weighting, distribution charts)
- hierarchy rollups (parent/child, group means)
- manual/subjective inputs (CSM sentiment) alongside automated signals
- alerts/automated actions (CTAs, tasks, notifications, workflow triggers)
- CRM write-back of health fields; APIs
- data-source integrations feeding signals

### L2 — Variant / Optional

- AI-derived signals (conversation sentiment) and AI score optimization
- predictive/ML churn-likelihood as a health input or parallel measure
- purpose-specific scores (churn risk vs upsell opportunity as separate scores)
- expansion-signal monitoring as a sibling lens
- retroactive recalculation; trend-noise thresholds (currency)
- health embedded in broader suites (CRM/service suites) vs CS-platform-native

### L3 — Vendor-specific (research notes only)

- Gainsight: Scorecard Fact/History objects, Rules Engine CTA 2.0, Mass Edit reports, validity period, Scorecard Optimizer (beta), Zoom-app scorecard, measure exceptions
- Totango: two health models (account health vs multidimensional), Health Designer, Good=100/Average=60/Poor=0 point scheme, unknown-health segment workaround, My Business Risk+Health page, enterprise-calculation options
- Planhat: 0–10 scale with 5 neutral, additive points, group-mean rollup, Success Units linkage
- Catalyst: raspberry most-impactful-field, Health/At Risk/Neutral picklist, group score = highest input, aggregates module, `/health_scores` API

## Vendor-specific Findings

See L3. Additional: Totango's survey-data caution (user-level NPS/CSAT aggregation is problematic) and usage-metric benchmarking guidance are design-methodology positions, not Type structure. Gainsight's AI Scorecard Optimizer depends on Renewal Center data — evidence of health↔renewal coupling from the vendor side.

## Boundary Findings

1. **vs Customer Success Platform (sharpest seam; joint-review flag)** — all four sampled products are CS platforms with health machinery at their core; no standalone pure-play health product was verified. Test: remove the CS workflow (success plans, plays/playbooks, QBRs, renewals, customer collaboration) → the health measure + monitoring loop still stands as a coherent system; remove the health measure → a CS platform still functions on other signals (usage, support, CRM data). The leaf is defensible as a distinct center of gravity (the health measure and its monitoring loop), but module-convergence is strong and must be recorded for joint review when customer-success-platform is processed.
2. **vs Product Usage / Adoption Platform** — usage platform produces the usage signal at event/user/feature granularity; health monitoring consumes account-level aggregates of multiple signal types into one standing measure. Adoption dashboards per account are the overlap zone (recorded from the usage side in research/product-usage-adoption-platform.md).
3. **vs Renewal Management Platform** — health produces risk signals; renewal management consumes them for prioritization and forecast (Gainsight's renewals-due-by-health view; AI Scorecard Optimizer keyed to renewal outcomes). Direction of consumption is the seam.
4. **vs CRM** — health is often synced into CRM account fields (Catalyst→Salesforce), but the CRM stores the account and does not define/operate the health measure or its monitoring loop.
5. **vs BI / analytics platforms** — BI reports on data; health monitoring maintains a managed, per-account health state with a definition, cadence, and action loop. A BI dashboard with an RAG column is not the Type: no managed health definition, no standing per-account state driving workflow.
6. **vs Customer Feedback Management / VoC** — survey scores (NPS/CSAT) are one input signal family; feedback management's unit of record is the feedback item, not the account health state.
7. **vs Churn-prediction / revenue-intelligence tools** — predictive churn models are one implementation/variant of the health measure (or a parallel measure); revenue intelligence works on sales-conversation signals, a different center.

**"去掉什么就变成另一个 Type" 判据**：去掉多信号聚合（只看单一指标）→ 单指标仪表盘；去掉账户归集（只看事件/用户粒度）→ Product Usage Platform；去掉监控回路（只算分不设阈值不浮出）→ 报表/评分工具；去掉健康测量的"管理定义"（无配置、无状态、无历史）→ BI。

## Historical / Market-Sample Check

Spreadsheet-era customer success: an account list with columns for usage, open tickets, NPS, last contact; an agreed formula producing a red/yellow/green status per account; a weekly review meeting flagging red rows for action. This satisfies all three L0 legs — health definition (the agreed formula), standing per-account state (the RAG column), monitoring loop (the review that surfaces reds). No cloud, weights UI, AI, or snapshots in the core. Pre-CS account management red/yellow/green reviews fit the same shape. The definition does not depend on the modern CS-platform packaging. ✓

## Uncertainties

1. **Pure-play existence**: whether standalone customer-health-monitoring products (apart from CS platforms) form a real market segment — not verified this pass; ChurnZero/Vitally/HubSpot/ClientSuccess unreachable. Assertion strength reduced accordingly.
2. **Alert machinery universality**: direct evidence of automated alerting/CTA creation at Gainsight (Rules Engine) and workflow linkage at Catalyst; Totango documents health-triggered tasks/notifications via hierarchy; Planhat's alert/automation linkage was not directly fetched (implied by automations collection). Held as common-mature, not definitional.
3. **Non-CS-platform realizations** (CRM suites, service suites): HubSpot's customer health score exists in the market but was unreachable; suite-side packaging remains unverified in detail.
4. **Exact cadences**: daily calculation (Totango) and weekly/monthly snapshots (Gainsight) are product-specific; cadence in general is held abstract in the canonical model.

## Final Synthesis

Customer Health Monitoring is the vendor-side standing watch over its own customer accounts. Its defining core is small: a monitored population of identified customer accounts; a per-account health measure — a persistent score/rating produced by a customer-defined aggregation of multiple customer signals, recomputed on an ongoing cadence and kept as history; and a monitoring loop that evaluates health against thresholds so adverse health is classified and surfaced for attention. Around that core, mature products add weighted aggregation machinery, segment-scoped health profiles, dual score/rank representation, trend views, portfolio monitoring surfaces, hierarchy rollups, manual sentiment inputs, alert/action automation, and CRM/API integration. The Type is realized predominantly inside customer success platforms — the strongest taxonomy risk is module-convergence with Customer Success Platform, recorded as a boundary issue for joint review. Boundaries: usage platforms produce the usage signal; renewal management consumes health for the renewal decision; CRM stores accounts; BI reports; health monitoring maintains and watches the account's standing health state.
