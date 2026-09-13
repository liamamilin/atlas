# Research Notes — A/B Testing Platform

## Research Goal

Understand what an A/B Testing Platform actually is as an Application Type: its defining structure, its standard workflow, its interfaces, its rules, and its boundaries against neighboring Types (Digital Experimentation Platform, Feature Flag Management, CRO Platform, Personalization, Marketing Analytics, Survey).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: run controlled comparison experiments (A/B, A/B/n, multivariate) on live digital experiences — split real traffic between variants, measure a goal, decide a winner.
- Primary users: growth/CRO teams, product managers, marketers, analysts; engineers for instrumentation.
- Nearest neighbors: Digital Experimentation Platform (sibling leaf in the same directory section), Feature Flag Management Platform, Conversion Rate Optimization Platform, Landing Page Optimization Platform, Marketing Analytics Platform, Marketing Personalization Platform, Survey Platform.
- Likely confusion: the directory carries both "A/B Testing Platform" and "Digital Experimentation Platform" under §06 — the market may treat these as one structure with an audience gradient. This was flagged as a research question from the start.

## Research Questions

1. What are the core objects? (experiment, variant, control, audience, allocation, goal/metric, event, result, decision)
2. What is the experiment lifecycle? (draft → running → paused → stopped/concluded → archived)
3. How does assignment work? (randomization unit, stickiness, allocation percentages)
4. How are variants authored? (visual editor, code editor, server-side parameters)
5. How are goals defined and measured? (primary/secondary/guardrail, events, retroactivity)
6. How are results presented and what statistics back them? (lift, confidence intervals, p-values, Bayesian probability, sequential testing)
7. What rules govern validity? (peeking, allocation changes, primary-metric lock, QA, isolation between experiments)
8. What interfaces exist? (dashboard, editor, visual editor, results page, QA mode, libraries)
9. Where is the boundary vs Feature Flags, Personalization, Analytics, CRO, Digital Experimentation Platform?
10. Historical check: do older/simpler products (split-URL testers, early website optimizers) still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Optimizely | Enterprise full-stack; splits its own offering into "Web Experimentation" and "Feature Experimentation" | Category-defining vendor; both client-side and server-side lines |
| VWO | CRO/marketing-oriented suite; Bayesian stats engine; visual-editor-first | Mid-market-to-enterprise marketing philosophy |
| AB Tasty | Mid-market CRO + personalization; guided campaign flow | Different workflow packaging (step-based campaign flow) |
| Statsig | Engineering-native experimentation platform; server-side, feature-flag-integrated, warehouse option | Modern product/engineering philosophy; different customer tier (product teams) |

## Sources

Research date: 2026-09-06.

### Optimizely (Tier 1 — official support help center, Zendesk-hosted)

- Support Help Center root: https://support.optimizely.com/hc/en-us
- Web Experimentation category: https://support.optimizely.com/hc/en-us/categories/39024919539981
- Key components (Pages, events, tags, audiences): https://support.optimizely.com/hc/en-us/articles/4410284313101
- Steps to create an experiment: https://support.optimizely.com/hc/en-us/articles/4410289104013
- Note: docs.optimizely.com (Archbee portal) is behind a login wall; developer docs (docs.developers.optimizely.com) were identified but not deeply fetched. Feature Experimentation details kept general.

### VWO (Tier 2 — official product pages only; help center unreachable)

- Root product page: https://www.vwo.com/
- Testing product page: https://vwo.com/testing/
- Limitation: vwo.com/help returned 404 and help.vwo.com failed with a transport error (2 attempts). VWO operational details below come from product/marketing pages, not the operational help center. Assertions about VWO internals are therefore kept weaker (positioning-level, not workflow-level).

### AB Tasty (Tier 1 — official GitBook documentation)

- Docs root: https://docs.abtasty.com/
- How to create an A/B Test: https://docs.abtasty.com/web-experimentation-and-personalization/campaign-creation-and-dashboard/how-to-create-a-campaign/experimentations/how-to-create-an-ab-test.md
- Campaign flow: Goals step: https://docs.abtasty.com/web-experimentation-and-personalization/campaign-flow-goals-step.md
- Experimentation campaign types index: https://docs.abtasty.com/web-experimentation-and-personalization/campaign-creation-and-dashboard/how-to-create-a-campaign/experimentations.md

### Statsig (Tier 1 — official documentation site)

- Experiments overview: https://docs.statsig.com/experiments-plus/
- Create an Experiment: https://docs.statsig.com/experiments/create-new
- How to Read Experiment Results: https://docs.statsig.com/experiments/interpreting-results/read-results
- Ending an Experiment: https://docs.statsig.com/experiments/ending/ending-experiment

## Product Observations

### Optimizely (Web Experimentation)

Evidence layer: A (directly observed from official help center articles).

Key observations:

- **Reusable always-on components**: Pages (URL templates deciding where experiments run), Events (tracked visitor actions: clicks, pageviews, form submissions, purchases), Tags (describe page parts visitors engage with, e.g. product type, cost), Audiences (groups of visitors to target or compare in results). These are set up once, "reusable and always on", and passively collect baseline data before any test runs.
- **Experiment creation flow** (documented step-by-step): Create New Experiment → select A/B Test → name/description → set where it runs (Target By URL once, or Target By Saved Pages for recurring use; page triggers/conditions for SPAs) → set targeting (Audiences, combinable with AND/OR; default audience "Everyone") → design variations in the Visual Editor (layout, visibility/position, typography, images, backgrounds, inline CSS, jQuery selectors, change timing) → shared code across variations → Traffic Allocation (random split between variations including the original; per-variation and total traffic adjustable) → Metrics (first metric added = primary metric, "determines whether your experiment wins or loses"; secondary metrics and monitor goals for downstream effects; Sample Size Calculator tied to Stats Engine) → integrations (e.g. GA4) → schedule (start/end time, timezone) → preview and test → summary page → optional AI pre-launch review (Opal) → Start Experiment.
- **Lifecycle vocabulary**: publish vs start vs pause are distinct operations (dedicated article); events from paused experiments, stopped variations, and archived experiments are treated differently (dedicated article).
- **Results**: Experiment Results page; segmentation of results; CSV export; event export; Warehouse-Native Experimentation Analytics as an alternative analysis mode.
- **Advanced**: multivariate tests with section rollups; redirect experiments with enhanced redirect analytics; contextual bandit results page (adaptive allocation exists as a product mode); change history (governance); webhooks; API tokens; SEO guidance for testing.
- **Product split**: the vendor itself ships "Web Experimentation" (client-side) and "Feature Experimentation" (server-side) as separate product lines under one experimentation umbrella, plus a separate "Personalization" product using the same components (pages/tags/audiences) for behaviorally targeted audiences.
- **AI**: Opal — test idea generation from URL/screenshot, AI variation summary, pre-launch experiment review with categorized feedback.

### VWO

Evidence layer: A for positioning-level facts (product pages), degraded overall (help center unreachable).

Key observations (positioning level):

- **Suite framing**: "Comprehensive Experimentation Platform" organized as Experiment (Web Testing, Mobile App Testing, Feature Testing), Observe (behavior analytics: heatmaps, session recordings, funnels, form analysis), Personalize. Testing is one pillar of a wider optimization suite.
- **Test types offered**: A/B Testing, Split URL Testing, Multivariate Testing; across client-side web, mobile app, and server-side/feature experimentation (SDKs, feature flags with on/off toggles and variables).
- **Stated workflow model** (product page): Create (control + variations across front-end/back-end/middleware) → Target (built-in options, custom conditions, behavior-based attributes; AND/OR logic; qualification on first visit or every visit) → Track (primary and secondary metrics; winner declared on primary goal; guardrail metrics that can auto-pause tests or notify) → Decide (Bayesian "SmartStats"; reports show probability to be 'Better Than Control', 'Worse Than Control', 'Practical Equivalence'; outlier handling) → Analyze (heatmaps and session recordings inside test reports) → Rollout (push winning experiences to production without developer dependency).
- **Program management layer**: "VWO Plan" — hypothesis management, observations, Kanban-style workflow for the experimentation pipeline.
- **Statistics positioning**: Bayesian engine marketed as handling "peeking errors and multiple testing errors"; A/B test significance and duration calculators offered as free tools.
- Not verified (help center unreachable): exact goal/tracker taxonomy, report mechanics, dashboard behavior, QA tooling details.

### AB Tasty

Evidence layer: A (directly observed from official GitBook docs).

Key observations:

- **Campaign types**: A/B Test, Multipage Test, Split Test (test by redirection), A/A Test, Patch / Multipage Patch, Multivariate Test; plus Personalizations as a separate campaign family using the same flow. An AI assistant ("Ally") helps choose the campaign type.
- **Guided 7-step campaign flow** (documented): 1) Main information — with a recommended hypothesis template ("If I apply [this change] to [this audience], then [impact] and it enhances [goal]"); 2) Editor — Visual Editor (change colors, images, wording; widget library) or Code Editor (JavaScript/CSS); 3) Goals — choose primary goal (the metric that "determines which variation takes precedence over the others") + secondary goals (up to 50 documented); goals are chosen from a tracker library: Action Trackers (set up in visual editor), Page trackers (pageviews), Custom trackers (code/dataLayer), Browsing metrics (bounce rate, exit rate, pages per session, revisit rate), Transactions; metrics are retroactive (page tracking, browsing, transactions — populated after start) or non-retroactive (action/custom trackers — must exist before launch); **primary goal cannot be modified or removed once the campaign has started**; 4) Targeting — WHERE (pages), FOR WHOM (whole traffic, mobile users only, etc.), WHICH conditions (e.g. after a number of pages, weather), WHEN (recurrence/scheduling); 5) Traffic allocation — default even split (50/50 for A/B, 33/33/33 for A/B/C); uneven allocation discouraged for statistical reasons; 6) Advanced options — third-party integrations, loading method, sequential testing option (early detection that an experiment will not succeed, for conversion/transaction-rate goals); 7) QA — QA Assistant to verify targeting, tracking, and modifications in real conditions before production; plus a campaign scheduler for timed start/pause.
- **Reporting**: campaign reporting section with metrics, analysis copilot (Evi Analysis).

### Statsig

Evidence layer: A (directly observed from official docs).

Key observations:

- **Definition framing**: "Statsig experimentation runs randomized controlled trials (A/B or A/B/n tests) that measure how product changes affect your key metrics." Experiments validate hypotheses before shipping; historical metrics show correlation, experiments establish causality.
- **Core concepts**: control variable (the manipulated variable; two values = A/B, more = multivariate), variants (control = current state, treatment = modified state), randomization unit (user ID, device ID/stable ID, session ID, custom ID — each with documented trade-offs), statistical significance (p-value, confidence interval).
- **Experiment creation**: name + hypothesis (rich text with a fill-in template: "We believe [change] for [segment] will [outcome] because [reason]; we will measure success using [primary metric] and monitor [guardrail metrics]") → Target Application required → Layer (default: own layer; layers manage multiple experiments/flags together for isolation) → Scorecard configuration (required: hypothesis + at least one primary metric; secondary metrics monitored for side effects; metrics computed daily; eligible for CUPED and sequential testing) → Allocation (percentage of eligible users, 0–100%; recommended to start small and ramp up; **increasing allocation is allowed anytime, decreasing is discouraged without resetting because it biases group allocation and pollutes results**) → Targeting (inline criteria or reference to an existing Feature Gate) → Groups and Parameters (parameters are the variables controlling variant behavior; groups are the buckets; adding groups auto-rebalances allocation).
- **Experiment types**: Standard A/B/n (default), Switchback tests, A/A tests.
- **Results**: Results tab with cumulative exposures chart (verifies enrollment rate and ratio vs configured), Scorecard (per-metric relative delta %, confidence interval, significance color coding: green positive / red negative / grey non-significant), lift formula Delta% = (Test − Control) / Control, default 95% CI, winsorization of extreme values, optional CUPED (pre-experiment bias reduction), sequential testing, SPRT (supports unlimited peeking), Bonferroni / Benjamini-Hochberg corrections for multiple comparisons, configurable confidence level, target duration (days or exposures; power analysis calculator; results computed for first 90 days by default, extendable in 30-day increments), views (cumulative, table, daily, days-since-exposure), dimension breakdowns (user dimensions, event dimensions), Explore tab for custom queries.
- **Explicit anti-peeking rule**: first 24 hours of results are hourly and diagnostic only — "Do not make any experiment decisions based on real-time results data in this first 24-hour window"; decisions should wait for target duration / power.
- **Ending lifecycle**: Make a Decision (ships the selected variant's parameters to all users; updates layer defaults), Abandon (finished state; users fall back to defaults), Reset (back to unstarted; re-salts so users are re-randomized — used after bugs), Disable group (kill one buggy group, keep others running), Archive (read-only, preserves history), Unarchive (editable again, does not auto-restart).
- **Engineering-native extras**: deterministic hashing with per-experiment salts (copyable for related experiment series), ID mapping (warehouse-native), Diagnostics tab (live log stream of checks/events), templates, team assignment, tags, decision frameworks (ship-vs-iterate logic), Hypothesis Advisor (AI feedback on hypothesis quality).

## Cross-product Comparison

| Dimension | Optimizely | VWO | AB Tasty | Statsig | Verdict |
|---|---|---|---|---|---|
| Experiment as persistent named record | Yes ("experiment"/"campaign") | Yes (tests) | Yes ("campaign") | Yes (experiment with hypothesis) | **L0** |
| Variants incl. control | Yes (original + variations) | Yes (control + variations) | Yes (original + variations) | Yes (control + treatment groups) | **L0** |
| Randomized assignment of real users | Yes (random traffic allocation) | Yes | Yes (default even split) | Yes (randomized controlled trial; deterministic hashing) | **L0** |
| Measured goal compared across variants | Yes (metrics; primary decides win/lose) | Yes (primary goal declares winner) | Yes (primary goal decides precedence) | Yes (scorecard; primary metric) | **L0** |
| Decision output (ship/keep/discard) | Yes (start/publish; winner rollout) | Yes (rollout winners) | Yes (campaign conclusion) | Yes (Make a Decision / Abandon) | **L0** |
| Audience targeting / segmentation | Yes (Audiences, AND/OR) | Yes (segments, custom conditions) | Yes (where/whom/conditions/when) | Yes (targeting criteria, feature gates) | L1 |
| Traffic allocation control | Yes (per-variation + total) | Yes | Yes (default even) | Yes (0–100%, ramp-up guidance) | L1 |
| Primary + secondary metrics | Yes (+ monitor goals) | Yes (+ guardrail metrics) | Yes (up to 50 secondary documented) | Yes (+ monitoring metrics) | L1 |
| Statistical engine with confidence reporting | Yes (Stats Engine; sample size calculator) | Yes (Bayesian SmartStats) | Yes (sequential testing option) | Yes (frequentist + CUPED/SPRT/BH) | L1 |
| Results page with per-variant comparison | Yes | Yes | Yes | Yes (scorecard, multiple views) | L1 |
| Lifecycle states (draft/run/pause/stop/archive) | Yes (publish/start/pause; archived) | Yes (implied by rollout/auto-pause) | Yes (scheduler; QA before launch) | Yes (decision/abandon/reset/archive) | L1 |
| QA / preview before launch | Yes (preview, test cookie) | Yes (simulated environments) | Yes (QA Assistant) | Yes (diagnostics live stream) | L1 |
| Scheduling | Yes (start/end, timezone) | Yes (implied) | Yes (timed start/pause) | Yes (target duration) | L1 |
| Reusable component libraries | Yes (pages/events/tags/audiences) | Yes (metrics library, segments) | Yes (trackers page) | Yes (metrics, gates, templates) | L1 |
| Integrations with analytics tools | Yes (GA4 etc.) | Yes (GA4, Mixpanel per testimonial) | Yes (third-party tools step) | Yes (Slack/email; warehouse) | L1 |
| Visual editor (client-side authoring) | Yes (central) | Yes (central) | Yes (central) | No (server-side parameters instead) | L2 (surface-dependent) |
| Server-side / feature experimentation | Yes (separate product line) | Yes (feature experimentation) | Limited evidence | Yes (native mode) | L2 |
| Multivariate testing | Yes | Yes | Yes | Yes (A/B/n generalizes) | L2 |
| Split URL / redirect testing | Yes (redirect analytics) | Yes | Yes | Not observed | L2 |
| A/A testing | Not observed in fetched pages | Not observed | Yes | Yes | L2 |
| Bayesian vs frequentist stats | Frequentist-leaning (Stats Engine) | Bayesian | Both options (sequential) | Frequentist + sequential methods | L2 (methodology varies) |
| Randomization unit choice | Not deeply fetched | Not verified | Not observed | Yes (user/device/session/custom) | L2 |
| Experiment isolation (layers/mutual exclusion) | Not observed in fetched pages | Not verified | Not observed | Yes (layers) | L2 |
| Feature-flag integration | Yes (feature experimentation line) | Yes (flags with toggles) | Not observed | Yes (gates/flags) | L2 |
| Personalization mode (non-random) | Yes (separate product) | Yes (suite pillar) | Yes (campaign family) | Not core | L2 |
| Program management (ideas/pipelines) | Yes (idea builder) | Yes (Plan, Kanban) | Yes (Evi Ideas) | Yes (decision frameworks) | L2 |
| Behavioral analytics bundled | Not observed | Yes (heatmaps/recordings) | Not observed | No | L2 |
| AI assistance | Yes (Opal) | Yes (Wandz, GPT-4 ideas) | Yes (Evi, Ally) | Yes (Hypothesis Advisor) | L2 |
| Bandits / adaptive allocation | Yes (contextual bandits results page) | Not observed | Not observed | Not observed | L2 (product-specific so far) |
| Warehouse-native analysis mode | Yes (integration section) | Not verified | Not observed | Yes (WHN mode) | L2 |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an A/B Testing Platform:

```text
Experiment (persistent, hypothesis-bearing record)
└── Variants (control + at least one alternative)
    └── Randomized assignment of real users to variants
        └── Measured goal compared across variants
            └── Decision output (which variant should become the experience)
```

Five properties:

1. **Experiment as persistent record** — a named unit of testing that exists before, during, and after the test, carrying its configuration and results. Without it, the product is an ad-hoc script.
2. **Two or more variants, including a control** — the current experience plus at least one alternative. Without alternatives, there is no comparison.
3. **Randomized assignment of real users** — the platform, not a human rule, decides who sees which variant, by chance, per a randomization unit. Without randomization, it is targeting/personalization.
4. **Measured goal compared across variants** — a defined metric measured per variant and compared (lift/difference with statistical backing). Without measurement, it is a rollout tool.
5. **Decision output** — the platform exists to answer "which variant should we ship?" (winner, no difference, or discard). Without the decision framing, it is raw data collection.

Removal test:

- Remove variants → analytics/monitoring platform
- Remove randomization → personalization/targeting platform
- Remove measurement → feature flag / rollout manager
- Remove decision framing → event collection pipeline
- Remove persistence → one-off script, not a platform

### L1 — Common Mature Structure

Present in all or nearly all mature products; expected by the market but not definitional:

- hypothesis/metadata on the experiment record
- audience targeting/segmentation (who is eligible)
- traffic allocation control (share entering the experiment; split across variants)
- primary metric + secondary metrics (+ guardrail/monitor metrics)
- statistical engine reporting lift with confidence (frequentist or Bayesian)
- results page: per-variant comparison, significance/probability indicators
- lifecycle states: draft → running → paused → stopped/concluded → archived
- QA/preview mode before launch
- scheduling (start/end)
- reusable libraries: events/goals/metrics, audiences/segments, pages/URL conditions
- experiments dashboard/list
- integrations with analytics/collaboration tools
- winner rollout / decision mechanism

### L2 — Variant / Optional Structure

Depends on segment, philosophy, deployment, maturity:

- execution surface: client-side (visual editor + snippet) vs server-side (SDKs + parameters) vs hybrid
- test types: A/B, A/B/n, multivariate, split URL/redirect, multipage, A/A
- statistical methodology: frequentist (p-values, CIs, sequential testing, multiple-comparison corrections, variance reduction like CUPED) vs Bayesian (probability to be better, practical equivalence)
- randomization unit choice (user/device/session/custom)
- experiment isolation (layers, mutually exclusive experiments)
- feature-flag integration and rollout control
- warehouse-native vs vendor-hosted measurement
- personalization mode (same delivery machinery, deterministic assignment)
- program management layer (idea pipelines, hypothesis boards)
- AI assistance (idea generation, pre-launch review, analysis copilots)
- bundled behavioral analytics (heatmaps, session recordings)
- bandits / adaptive allocation

### L3 — Vendor-specific Structure

Stays in Research Notes only:

- Optimizely: Pages/Events/Tags/Audiences as "always-on" reusable components; one-line snippet; Stats Engine; Web vs Feature Experimentation product split; Performance Edge; Opal AI; contextual bandits results page
- VWO: SmartStats (Bayesian), SmartCode, guardrail auto-pause, VWO Plan Kanban, bundled heatmaps/session recordings, Wandz AI layer
- AB Tasty: 7-step campaign flow; tracker taxonomy (action/page/custom/browsing/transactions); retroactive vs non-retroactive metrics; up-to-50 secondary goals; Patch campaigns; Evi/Ally AI assistants
- Statsig: Scorecard; Layers; ID types + salt management; CUPED/SPRT/BH; 90-day compute window with 30-day extensions; Make a Decision/Abandon/Reset/Disable-group/Archive states; Warehouse Native mode; Hypothesis Advisor; switchback tests

### Anti-overfitting Check

- "Visual editor" is central in the marketing-CRO sample (Optimizely Web, VWO, AB Tasty) but absent in Statsig's native mode → not L0, not even L1; it is the client-side implementation of variant authoring (L2).
- "Bayesian stats" is VWO's identity but not the industry's → methodology is L2.
- "Feature flags" are bundled by 3 of 4 products → tempting to promote, but a pure A/B testing platform without flags still exists and flags without measurement are a different Type → L2.
- Even traffic split (50/50) is AB Tasty's documented default and common practice, but allocation control exists precisely because splits vary → the invariant is *randomized* assignment, not *even* assignment.

### Historical / Market-Sample Check

- Early-generation tools (split-URL redirect testers, early website optimizers of the 2000s–2010s) had: experiment records, control + variant, random split, conversion goals, significance reporting. They satisfy L0 without any of: server-side SDKs, layers, CUPED, feature flags, AI, program management. ✓
- Embedded A/B testing (email subject-line testing inside email marketing platforms, ad creative testing inside ad platforms) shares the L0 pattern but lives inside other Application Types — supporting the reading that A/B testing is a portable structure, and the standalone Type is the dedicated platform. ✓
- The definition does not depend on web-only surfaces: mobile app and server-side experimentation in the sample satisfy the same L0 with different delivery. ✓

## Vendor-specific Findings

See L3 above. Additionally:

- Optimizely treats Pages/Events/Tags/Audiences as infrastructure that runs "always on" and collects baseline data before any experiment — a program-maturity pattern not observed in the other sampled products' fetched docs.
- AB Tasty documents a hard rule: the primary goal cannot be modified or removed once the campaign has started. (Product-specific rule; not generalized.)
- Statsig documents precise operational rules: allocation decrease biases results (increase-only guidance), 24-hour real-time results are diagnostic-only, results computed for first 90 days by default, reset re-salts assignments. (Product-specific; used as examples of the *kind* of rules this Type carries, not generalized as universal values.)
- VWO markets guardrail metrics that can automatically pause tests — auto-pause behavior is product-specific in this sample.

## Boundary Findings

### vs Digital Experimentation Platform (sibling leaf, same directory section)

The researched market does not maintain a structural wall between "A/B testing" and "digital experimentation":

- Optimizely names its products "Web Experimentation" and "Feature Experimentation" and markets "experimentation" as the umbrella.
- VWO sells "Testing" and "Feature Experimentation" as capabilities of one platform.
- Statsig, an engineering-native platform, describes its core as "randomized controlled trials (A/B or A/B/n tests)".
- The L0 (variants + randomization + measured comparison + decision) is identical across both labels.

The directory split appears to encode an **audience/philosophy gradient**, not a structural one:

- A/B Testing Platform: marketing/CRO-centered, visual-editor-first, client-side web testing as the default surface, campaign-style packaging (Optimizely Web, VWO, AB Tasty).
- Digital Experimentation Platform: engineering/product-centered, server-side/feature-first, stats-engine-heavy, integrated with feature flags and data warehouses, continuous-experimentation framing (Statsig; Optimizely Feature Experimentation).

**Test**: remove the visual editor and web-page surface → the engineering platform remains an experimentation platform; remove the server-side/flag machinery → the CRO tool remains an A/B testing platform. Both keep the same L0. → Record as boundary issue; the two leaves likely need a shared framing or a joint review pass when Digital Experimentation Platform is processed.

### vs Feature Flag Management Platform

- Flags control delivery (who gets what; on/off; gradual rollout). Experiments measure effect (what works).
- A flag without measurement is not an experiment; an experiment without delivery control is still an experiment.
- Products bundle both (Statsig natively; Optimizely and VWO via feature-experimentation lines). The bundle is L2 for this Type.
- **Test**: remove goals/measurement → flag manager remains; remove flag/rollout control → A/B testing platform remains.

### vs Conversion Rate Optimization Platform

- CRO is the practice/goal; A/B testing is the instrument. VWO's own glossary frames CRO as the practice and A/B testing as the process within it.
- Vendors market the same product as both. A "CRO platform" in the market usually = testing + behavior analytics + personalization + program management (a superset).
- Likely the CRO leaf will resolve as a practice-framed superset or alias cluster. Flag for joint review when Conversion Rate Optimization Platform is processed.

### vs Landing Page Optimization Platform

- Same L0 restricted to a surface (landing pages) and often to acquisition campaigns. Likely Variant of A/B Testing Platform rather than independent Type. Flag for joint review.

### vs Marketing Analytics Platform

- Analytics observes and reports what happened; A/B testing intervenes (assigns users) and establishes causal comparison between assigned groups.
- Results pages borrow analytics forms (charts, segments, funnels) — hence the confusion — but the defining act is the controlled comparison.
- **Test**: remove assignment → analytics remains; remove passive observation-only mode → A/B testing remains.

### vs Marketing Personalization Platform

- Same delivery machinery (who sees which experience), different assignment logic: personalization assigns deterministically by segment rule; A/B testing assigns randomly to compare.
- Products bundle both (Optimizely Personalization; AB Tasty personalizations; VWO Personalization). Personalization mode inside an A/B testing platform is L2.
- **Test**: replace randomization with rule-based targeting → personalization; restore randomization → A/B testing.

### vs Survey Platform

- Surveys collect stated preference (users answer); A/B testing measures revealed preference (users act) under controlled comparison. Different data source, different validity claims.

## Uncertainties

1. **VWO operational detail**: help center unreachable (404 + transport error). VWO observations are positioning-level (product pages). VWO's exact goal taxonomy, report mechanics, and QA tooling are unverified. Assertions involving VWO internals are kept weaker throughout.
2. **Optimizely Feature Experimentation**: developer docs identified but not deeply fetched (docs portal behind login). Server-side specifics for Optimizely kept general.
3. **Statistical defaults**: precise defaults (confidence levels, compute windows, correction methods) were only documented in fetched Statsig pages; they vary by product and change over time. The final document states only directly observed facts and otherwise speaks in general terms.
4. **Market edges not sampled**: open-source tools (e.g. GrowthBook), warehouse-native specialists (e.g. Eppo), and flag-first platforms (e.g. LaunchDarkly) were not sampled; the L0 is expected to hold for them but this is inference, not observation.
5. **Pricing/packaging**: out of scope; plan-tier differences not researched.

## Final Synthesis

An A/B Testing Platform is best modeled as a **controlled-experiment machine for live digital experiences**:

```text
Hypothesis
→ Experiment record (variants: control + treatment(s))
→ Eligibility rules (audience) + share of traffic (allocation)
→ Randomized assignment per randomization unit
→ Goal measurement per variant (from behavioral events)
→ Statistical comparison (lift + confidence/probability)
→ Decision (ship winner / keep control / discard) + rollout
```

The defining core is deliberately small: variants, randomization, measured comparison, decision, persisted as an experiment record. Everything else the market associates with the category — visual editors, Bayesian engines, feature flags, heatmaps, idea pipelines, AI copilots — is common mature structure or variant structure, not definition.

The Type's center of gravity in the current market is split between two philosophies (marketing/CRO vs engineering/product) that share one structure. The directory's sibling leaf "Digital Experimentation Platform" most plausibly names the second philosophy rather than a second structure — recorded as a boundary issue for joint review.
