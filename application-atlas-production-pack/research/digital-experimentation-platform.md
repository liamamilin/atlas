# Research Notes — Digital Experimentation Platform

## Research Goal

Understand what a Digital Experimentation Platform actually is as an Application Type: its defining structure, its standard workflow, its interfaces, its rules, and its boundaries against neighboring Types. This pass also carries a **joint-review obligation**: the a-b-testing-platform pass (2026-09-06) flagged this leaf with "one shared defining core (variants + randomization + measured comparison + decision) expressed in two philosophies — probable audience-gradient split rather than two structures; flagged for joint review when Digital Experimentation Platform is processed." This pass must discharge that flag from this side.

## Initial Boundary

Initial hypothesis (pre-research):

- The leaf names the engineering/product-team pole of the experimentation market: server-side/feature-flag-integrated experimentation for software products, as opposed to the marketing/CRO pole documented under A/B Testing Platform.
- Candidate core objects: experiment, variant, randomization unit, assignment/exposure, metric (organization-wide definitions), feature flag/parameter, result, decision.
- Nearest neighbors: A/B Testing Platform (sibling leaf, processed — the joint-review counterpart), Feature Flag Management Platform (processed 2026-09-08 — control-as-center vs measurement-as-center), Conversion Rate Optimization Platform (processed 2026-09-07), Marketing Personalization Platform (processed 2026-09-08 — assignment-logic seam), Product Analytics / product-usage-adoption-platform (processed 2026-09-06 — observation without intervention), Marketing Mix Modeling / Marketing Attribution (observational vs interventional), ML experimentation/model-evaluation leaves (§13 — different object of experimentation).
- Likely confusion (inherited): the directory carries both "A/B Testing Platform" and "Digital Experimentation Platform" under §06; the market may treat these as one structure with an audience gradient. Additional candidate confusions: "experimentation platform" as umbrella marketing label spanning both philosophies; feature-flag platforms marketing "experimentation" add-ons; warehouse-native measurement as a differentiator vs a structure.

## Research Questions

1. What are the core objects of products sold as "experimentation platforms" to engineering/product teams? (experiment, variant, parameter, flag, metric, exposure, layer, holdout)
2. Is there a structural discriminator vs the A/B Testing Platform leaf, or one shared structure with two audience philosophies? What exactly differs: delivery surface, metrics layer, program machinery, statistics, users?
3. What is the role of the organization-wide **metrics layer** (shared metric definitions computed from a unified event stream) vs per-test goals — is it definitional-shaped or maturity?
4. How does delivery work in this pole: server-side SDKs, feature flags, client-side, edge? Is client-side visual-editor testing part of this Type or the sibling's?
5. What statistical machinery is standard (sequential testing, variance reduction/CUPED, multiple-comparison correction, Bayesian vs frequentist)?
6. What program machinery exists for running experimentation as a continuous program (concurrent experiments, layers/mutual exclusion, holdouts, scorecards, guardrails)?
7. Where are the boundaries: vs Feature Flag Management (control-as-center), vs product analytics (observation without intervention), vs personalization (rule-based assignment), vs MMM/attribution (observational modeling), vs CRO (practice superset), vs ML/model evaluation (different object of experimentation)?
8. Historical check: do older/simpler realizations (self-hosted open-source A/B tools, analytics-platform-native experiment features, early server-side split testers) still satisfy the definition?
9. What does "digital" bind: web/app surfaces only, or any software product experience?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers — deliberately covering the three edges the a-b-testing pass left unsampled:

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Statsig | Engineering-native full-stack experimentation (flags + experiments + analytics); startup→enterprise | The clearest self-described experimentation platform of the engineering pole; Tier-1 docs known reachable |
| Eppo | Warehouse-native experimentation for product/data teams | Warehouse-native specialist pole; explicitly named as unsampled in the a-b-testing pass |
| GrowthBook | Open-source, self-hostable experimentation | Open-source/self-hosted pole; explicitly named as unsampled in the a-b-testing pass |
| LaunchDarkly (Experimentation) | Flag-first platform with experimentation add-on | Flag-first pole; explicitly named as unsampled in the a-b-testing pass; tests the flag↔experiment boundary from the vendor's own side |
| Optimizely (Feature Experimentation) | Enterprise suite's server-side line | Category-defining vendor's engineering line; the a-b pass kept it general — this pass fetches the developer docs directly |

Fallback candidates if fetches failed: Amplitude Experiment (analytics-native), Kameleoon, Convert. None needed — all five primary fetches succeeded.

## Sources

Research date: 2026-09-08. All sources below were fetched directly (Tier 1 — official vendor documentation) unless noted.

### Statsig (Tier 1 — official documentation site)

- Documentation index: https://docs.statsig.com/llms.txt
- Experiments Overview: https://docs.statsig.com/experiments-plus/
- When to Use Feature Gates vs. Experiments?: https://docs.statsig.com/api/content/guides/featureflags-or-experiments
- Bootstrapping Your Experimentation Program: https://docs.statsig.com/api/content/statsig-warehouse-native/guides/experimentation-program
- Layers: https://docs.statsig.com/experiments/layers-overview

### Eppo (Tier 1 — official documentation site)

- Docs home / About Eppo: https://docs.geteppo.com/
- Feature Flags (Flag and Experiment Configuration): https://docs.geteppo.com/feature-flagging/
- Mutual exclusion (Layers): https://docs.geteppo.com/feature-flagging/concepts/mutual_exclusion/
- Holdouts: https://docs.geteppo.com/feature-flagging/concepts/holdout-config/
- Experiment Analysis: https://docs.geteppo.com/experiment-analysis/
- Data Management: https://docs.geteppo.com/data-management/
- Statistics: https://docs.geteppo.com/statistics/

### GrowthBook (Tier 1 — official documentation site)

- Docs home: https://docs.growthbook.io/
- What is GrowthBook (overview): https://docs.growthbook.io/overview
- Running Experiments: https://docs.growthbook.io/experiments
- Documentation index: https://docs.growthbook.io/llms.txt

### LaunchDarkly (Tier 1 — official documentation guides)

- Experimentation guides category: https://launchdarkly.com/docs/guides/experimentation.md
- Designing experiments: https://launchdarkly.com/docs/guides/experimentation/designing-experiments.md
- Measuring Experimentation impact with holdouts: https://launchdarkly.com/docs/guides/experimentation/holdouts.md

### Optimizely (Tier 1 — official developer documentation)

- Feature Experimentation introduction: https://docs.developers.optimizely.com/feature-experimentation/docs
- Run A/B tests: https://docs.developers.optimizely.com/feature-experimentation/docs/run-a-b-tests

### Cross-references to prior passes (context, not new evidence)

- research/a-b-testing-platform.md (2026-09-06) — sibling leaf's evidence on Optimizely Web, VWO, AB Tasty, Statsig experiment-creation flows.
- research/feature-flag-management-platform.md (2026-09-08) — flag-side boundary framing (control-as-center vs measurement-as-center).
- STATUS.md entries for conversion-rate-optimization-platform, landing-page-optimization-platform, marketing-personalization-platform, marketing-mix-modeling-application (§06 cluster context).

## Product Observations

### Statsig

Evidence layer: A (directly observed from official docs).

- **Self-definition**: "Statsig experimentation runs randomized controlled trials (A/B or A/B/n tests) that measure how product changes affect your key metrics." Experiments validate hypotheses before shipping; historical metrics show correlation, experiments establish causality.
- **Core concepts**: control variable (manipulated variable; two values = A/B, more = multivariate), variants (control = current state, treatment = modified state), randomization unit (user ID, device/stable ID, session ID, custom ID — each with documented trade-offs; StableID auto-generated for anonymous users), statistical significance (p-value, confidence interval).
- **Experiment detail tabs**: Setup (scorecard, allocation, targeting, groups, parameters), Diagnostics (live log stream of checks and events to confirm integration), Results (exposures + scorecard metric lifts), Explore (custom queries breaking down results by user/event dimensions), Summary.
- **Vendor's own flag-vs-experiment boundary** ("When to Use Feature Gates vs. Experiments?"): gate = control who sees a feature, roll out gradually, boolean return, Pass % ramping (can exceed 50/50); experiment = compare variants and quantify lift, any number of variants, JSON config return, Allocation % (splits cap at 50/50). Neither reshuffles existing users after assignment. Gates act as targeting pre-filters for experiments; after a winner, "lift the targeting gate and let the winning variant reach everyone." Layers provide "isolated universes" for parallel experiments.
- **Layers**: mutually exclusive universes; each layer has a logical representation of all users; parameters exist at the layer level and are shared across experiments; "abstracts the concept of 'Experiment' away from the SDKs, so that users only need to work with parameters in code" — new tests run without code changes or app releases; layer exposures logged with dedup windows.
- **Program guide** ("Bootstrapping Your Experimentation Program"): five steps — generate ideas, run first A/B test, share results, accelerate velocity, build culture of learning. "Turn every upcoming feature into an experiment": features behind flags; flags "automatically convert a feature rollout into an A/B test, measuring the impact on key metrics as the rollout progresses." Hypothesis = Action + Predicted Outcome + Rationale. Validation via live exposure stream; platform flags missing identifiers and exposure/event mismatches. Power calculator → target end date. Key metrics to avoid cherry-picking. Weekly/bi-weekly experiment reviews; program success criteria (time to set up, % decisions made with trustworthy data, experiments per week, quality).
- **Platform breadth** (from docs index): feature gates, dynamic configs, experiments, product analytics, session replay, web analytics, infra analytics; deployment models Cloud vs Warehouse Native (analysis runs against the customer's warehouse; metric sources, assignment sources, cluster experiments for assignment-unit ≠ analysis-unit); statistical methods pages (one-sided tests, Bonferroni, Benjamini–Hochberg); Autotune bandits (multi-armed and contextual); persistent assignment (sticky across sessions/devices); target apps (scope gates/experiments/configs to specific applications in a project); Console API, CLI, Terraform provider; integrations for experimenting on OpenAI/Azure AI prompts, models, and parameters; AI Experimentation (Early Access).

### Eppo

Evidence layer: A (directly observed from official docs).

- **Self-definition**: "Eppo is a composable next-generation feature flagging and experimentation platform focused on tightly integrating with your existing tech stack." Two components: a lightweight SDK (feature rollouts, kill switches, experimentation) and an analytics platform (experiment analysis + program management).
- **SDK architecture**: flags/experiments configured in the UI → generalized configuration file distributed via global CDN → downloaded and cached locally on initialization → evaluation done locally with no further network requests; polling keeps config current. **The SDK does no tracking of its own** — no user-level data passes through Eppo; the customer passes in an interface to their existing event tracking system (mitigates security/ad-blocking/consent concerns).
- **Flag concepts**: variations, allocations, environments, targeting rules, audiences, mutual exclusion (layers), dependent flags, holdouts, SDK tags. Use cases: feature gates, experiment assignment, progressive rollouts, kill switches, dynamic configuration.
- **Layers (mutual exclusion)**: for concurrent experiments on the same surface; cites Microsoft research that interaction effects are "vanishingly rare" — recommend mutual exclusion only when overlapping treatments critically degrade UX. Layer = parameters + four allocation levels (opt-out rule → experiments → rollout → default serving rule). Concluding: decide in Analysis, then Archive or **Rollout & Archive** — winning variation replaces the default experience in the Rollout allocation.
- **Holdouts**: "validate the aggregate impact of Experimentation." A holdout audience is isolated from all active experiments; randomly split into Status Quo (always default experience) vs Winning Variants (see each rolled-out winner). Global holdouts (all experiments in window auto-included) and Selective holdouts. Assignment-window eligibility rules; holdout-specific assignment keys so holdout logging doesn't interfere with experiment analysis; analysis compares held-out subjects across all qualifying rollouts. Analysis-Only mode supported with external randomization.
- **Experiment analysis**: experiment list view (filter by name, timeframe, status, entity, team, creator, primary metric, starred); detail view = per-variation per-metric control value + relative lift estimate + confidence interval (default 95%; multiple CI methods — sequential, fixed-sample, Bayesian — settable at company or experiment level); frequentist statistics (standard error, p-value, Z-score); Bayesian statistics (probability beats control, probability > precision / ROPE, risk, loss); **impact accounting** (coverage = share of events in experiment; global lift = expected increase if rolled out to 100%); segments (pre-computed subgroups) and single-property filters; metric explores (slice by properties); outlier capping; reversed metrics (desired change direction); CUPED.
- **Data management (the metrics layer)**: annotate the warehouse — entities (randomization units; multiple entity types supported, e.g., restaurants/customers/drivers for a delivery marketplace), assignment tables (who participated and what they saw), fact tables (actions → metrics), property tables (slicing dimensions). Metrics built on annotated tables (simple/conversion/ratio/funnel); **metric collections** (groups added to experiments at once); certified metrics; experiment run log; source diagnostics. "Once a Data team has annotated tables in their warehouse, anyone in the company can use them to plan, monitor, and analyze experiments."
- **Statistics section**: four tenets (flexibility, power, interpretability, trustworthiness); classical frequentist tests, sequential analysis (always valid), Bayesian; CUPED++; sample size calculator; global lift; interaction detection; multiple testing correction; sample ratio mismatch detection with notification.
- **Advanced experiment families**: contextual bandits (personalize per user), switchback experiments (marketplace-style), clustered analysis; randomization logs can come from Eppo's SDK, email marketing systems, ML models, or "other surface area on which you experiment"; LaunchDarkly migration guide.

### GrowthBook

Evidence layer: A (directly observed from official docs).

- **Self-definition**: "GrowthBook is the most popular open-source platform for feature flagging and experimentation." "GrowthBook is a modular platform. You can use it for either Feature Flags, Experiment Analysis, or both."
- **Stated philosophy**: feature flagging is the best way to release code, experimentation the best way to measure its impact; experimentation should sit on top of existing data and metrics "wherever they live and however they are defined"; data transparency (SQL behind every query, Jupyter export, stats engines on GitHub); SDKs evaluate locally with no network requests; no user-level data collected; same code powers Cloud and self-hosted.
- **Feature flags**: 4 types (boolean, number, string, JSON with schema validation); environments; override rules: Forced Value, Percentage Rollout, **Safe Rollout** (ramp while monitoring guardrail metrics, auto-rollback), **Experiment** ("run a controlled hypothesis test between 2 or more feature values"), Multi-Arm Bandit. All features per environment packaged into one JSON file for SDKs.
- **Experiment analysis**: connects to the SQL data warehouse; no raw user-level events or PII sent to GrowthBook — only aggregates (sums, sums of squares). **Fact Tables** (SQL selecting raw data) + **Metrics** built on them (proportion, mean, ratio, quantile, retention, funnel); metric library reused across experiments. Stats engine: frequentist or Bayesian; sequential testing (always-valid p-values, peek safely); CUPED; **Sample Ratio Mismatch detection**; multiple-comparison corrections (Holm-Bonferroni, Benjamini-Hochberg); custom baselines; custom priors; power calculator; difference types (relative/absolute/scaled). Dimensions for drill-down; raw SQL visibility; Jupyter export.
- **Ways to run experiments**: server-side via feature-flag experiment rules or inline SDK experiments; client-side via flags, inline, or **Visual Editor (WYSIWYG)**; API/ML experiments ("SDKs work anywhere code can run… deterministic hashing… same variation across your platform without storing state"); **custom assignment / 3rd-party experiments** ("As long as the exposure/assignment information is available from within your data warehouse, you can use GrowthBook to analyse the results").
- **Assignment mechanics**: consistent hashing (same user → same variation while seed + hashing ID unchanged); sticky bucketing when settings change.
- **Best practices** (vendor-published): A/A tests to validate setup; expose users as close to treatment as possible (activation metric to filter un-exposed users); flickering avoidance; sample size rules of thumb; minimum test durations (1–2 weeks typical); interaction effects rare — namespaces for mutual exclusion (same hash attribute required); experimentation frequency as program success factor.
- **Three use cases** (vendor's own): Full Experimentation Platform / **Feature Flags Only** (companies without traffic to experiment) / **Experiment Analysis Only** (teams with home-built assignment or another experimentation system).

### LaunchDarkly (Experimentation)

Evidence layer: A (directly observed from official docs guides).

- **Framing**: Experimentation is a capability of the flag platform: "You can create an experiment by connecting any flag or AgentControl config to a metric or group of metrics… Because you can wrap any part of your technology stack or product in a feature flag, you can use experiments to test for much more than the efficacy of user interface (UI) changes." Experiment uses listed: validate ideas, gauge interest before building, gather performance data for a feature/service/API, drive revenue by rolling out successful variations.
- **Experiment types**: A/B experiments (on flags and AgentControl configs); funnel metric groups (reusable ordered metric lists standardizing tracked behavior across experiments); **Data Export only experiments** (assignment in LaunchDarkly, analysis in a third-party tool — no LD metric required, no in-UI results); warehouse-native metrics experiments (BigQuery/Databricks/Redshift/Snowflake); A/A tests.
- **Design guide workflow**: generate ideas → formulate hypothesis ("If [specific change], then [measurable metrics improve] because [effect]") → choose sample size (Bayesian for small samples, min ~1 week; frequentist fixed-horizon t-test with pre-computed sample size vs sequential — act anytime; sample-size calculator with effect/exposure rate/control mean/SD/significance/power) → determine audience (targeting rules; context kind must match randomization unit) → mutually exclusive experiments via layers → holdouts → choose variations on the flag → set metrics (custom conversion count/binary, custom numeric, page viewed, clicked/tapped; **one primary metric only**; funnel metric groups) → choose analysis method (Bayesian vs frequentist) → roadmap (external tools) → build/run → roll out winning variation immediately via flag machinery.
- **Experimentation keys**: metered unit — unique context keys per experiment across server/client/AI/edge SDKs.
- **Holdouts guide**: "measure the overall effectiveness of your Experimentation program" — exclude a percentage of the audience from running experiments; compare in-holdout vs not-in-holdout on a chosen metric after a period (e.g., a quarter); decide which experiments to include; end holdout and read results; negative program impact → "examine the experiments you're running."
- **AI-era scope**: "Proving ROI with data-driven AI agent experiments" guide; experiments run on AgentControl configs (AI agent configs) as first-class experiment subjects alongside flags.
- **Migration guide from Statsig** exists (competitive set confirmation).

### Optimizely (Feature Experimentation)

Evidence layer: A (directly observed from official developer docs).

- **Self-definition**: "Optimizely Feature Experimentation is a feature flagging and experimentation platform for websites, mobile apps, chatbots, APIs, smart devices, and anything else with a network connection." Deploy code behind feature flags, experiment with A/B tests, use targeted deliveries to roll out or roll back immediately; microsecond performance via open-source SDKs. Rollouts = free plan (free flags + one A/B test).
- **Experiments as flag rules**: an A/B test is a **rule in a flag's ruleset** (per environment), with type `a/b`, variations (e.g., on/off), `percentage_included` per variation, audience conditions, metrics (event-based: event_id, aggregator, scope, winning_direction), and a **layer_id** (every experiment lives in a layer). Restriction: "If you intend to have multiple experiments and flag deliveries in your flag, your experiment must always be the first rule in your ruleset."
- **Decide method**: "The goal of the `Decide` method is to separate the process of developing and releasing code from the decision to turn a flag on." Users evaluated against each flag rule in an ordered ruleset before bucketing. Same flag implementation reusable across rules (delivery → experiment → rollout).
- **Flag variables / remote configuration**: variations carry variables edited remotely in the app instead of hard-coding; "Update your app in real time without a code deployment… even make changes to your experiments while they are running."
- **Workflow**: create flag → handle user IDs → create A/B test rule → integrate Decide code → **test in a non-production environment (QA)** → discard QA user events → enable in production. REST API for full ruleset management (GET-then-PATCH pattern to avoid overwriting).
- **Vendor's own two-line split**: "To build a company-wide experimentation program, consider pairing Optimizely's server-side experimentation product, Feature Experimentation, with the client-side experimentation product, Web Experimentation." Stats Engine provides "immediate, trustable results"; cross-platform consistent bucketing across languages.

## Cross-product Comparison

| Dimension | Statsig | Eppo | GrowthBook | LaunchDarkly Experimentation | Optimizely Feature Experimentation |
|---|---|---|---|---|---|
| Experiment record | Experiment (Setup/Diagnostics/Results/Explore/Summary tabs; scorecard) | Experiment Analysis attached to a flag/layer allocation | Experiment (feature-flag experiment rule, inline, visual editor, or custom assignment) | Experiment = flag or AgentControl config + metrics | A/B test rule in a flag's ruleset |
| Variants | Groups + parameters (JSON config returned) | Variations on a flag/layer | Feature values (bool/number/string/JSON) | Flag variations | Flag variations with variables |
| Assignment | SDK randomization; user/device/session/custom/stableID units; persistent (sticky) assignment | SDK local evaluation from CDN config; assignment logging to warehouse | SDK deterministic hashing; sticky bucketing | SDK bucketing by context kind; context kind = randomization unit | SDK Decide; in-memory bucketing; consistent across languages |
| Metrics layer | Scorecard (primary/secondary/guardrail); metrics computed from events or warehouse sources | Warehouse annotation (entities/assignments/facts/properties) → metrics + collections + certified metrics | Fact tables → metric library (proportion/mean/ratio/quantile/retention/funnel) | Managed metrics (conversion count/binary, numeric, pageview, click) + funnel metric groups | Event-based metrics attached to rules (aggregator, winning direction) |
| Mutual exclusion | Layers (universes; shared parameters; parameter-level SDK API) | Layers (opt-out/experiments/rollout/default) | Namespaces | Layers | Layers (layer_id on every experiment) |
| Holdouts | Program guide references measuring impact (object not directly fetched) | Global + selective holdouts; status-quo vs all-shipped-variants; analysis mode | Not observed in fetched pages | Holdouts as first-class object (create, add experiments, end, read) | Not observed in fetched pages |
| Statistics | p-values/CIs; one-sided tests; Bonferroni; Benjamini–Hochberg; CUPED; sequential (per a-b pass + index) | Frequentist (fixed/sequential) + Bayesian (prob-beats-control, ROPE, risk, loss); CUPED++; SRM; multiple-testing correction; global lift | Frequentist or Bayesian; sequential always-valid; CUPED; SRM; Holm-Bonferroni/BH; power calculator | Bayesian vs frequentist (fixed-horizon t-test, sequential); sample-size calculator | Stats Engine (sequential, real-time results) |
| Data posture | Cloud (hosted events) or Warehouse Native | Warehouse-native analysis; SDK does no tracking (BYO event system) | Warehouse analysis; aggregates only; open-source self-hostable | LD-hosted metrics or warehouse-native | Hosted (Stats Engine); events via Track Event |
| Delivery surface | Client/server/on-device SDKs; parameters in code | Client/server SDKs; local eval | Client/server/edge SDKs; flags, inline, visual editor | Server/client/AI/edge SDKs; flags + AgentControl | Client/server SDKs; Decide + Track Event; remote config |
| Decision → rollout | Winner: lift targeting gate | Rollout & Archive (winner replaces default in layer) | Ship winning feature value / rollout rule | "Engineering team can immediately roll out the winning variation" | Winner reaches everyone via flag rules |
| Program machinery | Program guide (reviews, velocity, culture); diagnostics | Holdouts, impact accounting, experiment reports, run log | A/A tests, namespaces, open guide | Holdouts, sample-size calculator, experimentation-key metering, roadmap guidance | QA environment, change history, REST API |
| Experimentable object | Product features, prompts/models (OpenAI/Azure integrations) | Product features, ML models, email marketing, "other surface area" | "Anywhere code can run" incl. API/ML | "Any part of your technology stack" incl. AI agents (AgentControl) | "Websites, mobile apps, chatbots, APIs, smart devices, anything with a network connection" |

**Cross-product commonalities (B-level, observed in all five):**

1. The shared experiment core: experiment record + variants (control + treatment) + randomized assignment of real users + measured metrics compared across variants + decision. Present verbatim in every product's own vocabulary.
2. Assignment machinery integrated into the running software via SDK/API; variants consumed by application code as parameters/flags/configs. The experiment is frequently literally a rule/mode of a feature flag (Optimizely, GrowthBook, Eppo, LaunchDarkly) or a parameter-consuming object (Statsig).
3. Metrics held as managed, reusable objects beyond the single experiment (scorecards, metric libraries, fact-table-derived metrics, funnel metric groups, event catalogs).
4. Mutual-exclusion machinery for concurrent experiments (layers/universes/namespaces) — 5/5.
5. A statistical engine as a first-class, marketed component with validity machinery (sequential methods, variance reduction, multiple-comparison corrections, SRM detection, sample-size/power calculation) — 5/5 in some form.
6. Decision wired to delivery: the winning variant is rolled out through the same flag/parameter machinery that ran the experiment.
7. Data-posture options spanning vendor-hosted and customer-warehouse analysis; several products advertise that raw user data need not pass through the vendor.
8. Experimentable object = the organization's own software product and stack (features, parameters, APIs, infrastructure, AI agents/models), not only marketing pages.

**Pole-differentiating observations (vs the a-b-testing sample):**

- In the a-b-testing sample (Optimizely Web, VWO, AB Tasty), the default authoring surface is the visual editor on live pages and the packaging is campaign-style; goals are chosen per campaign from tracker libraries. In this sample, the default is code-integrated assignment with parameters; visual editors are optional add-ons (GrowthBook) or a separate product line (Optimizely Web).
- The metrics layer in this pole is anchored in the organization's data estate (warehouse annotation, event streams, certified metrics) rather than per-campaign tracker lists.
- Program machinery in this pole manages many concurrent experiments as an ongoing organizational operation (layers, holdouts, program guides, impact accounting) rather than a portfolio of campaigns.

## Abstraction

### L0 — Defining Invariant (minimal)

A Digital Experimentation Platform is the product organization's system for running controlled experiments on its own software product, holding exactly three structures jointly:

1. **The controlled-experiment record over the organization's own product** — a named, persistent experiment carrying a hypothesis, variants (control + treatment(s)), and run state; remove → generic analytics/reporting tooling.
2. **Randomized assignment integrated into the running software** — the platform's SDK/API decides variant membership inside the application at runtime, and application code consumes the assignment (parameters, flags, configs) to shape behavior; remove → platform-rendered page testing (the A/B Testing pole) or a passive config service.
3. **Measured comparison and decision** — per-variant metric lift with statistical backing, computed against managed metrics, terminalized in a ship/keep/discard decision whose winner is rolled out through the same delivery machinery; remove → a feature-flag rollout tool (control-as-center) or an analytics dashboard (observation-as-center).

Jointly-held is load-bearing: (1) alone = a stats/reporting tool; (2) without (1)+(3) = a feature-flag platform; (3) without (2) = the page-surface A/B testing pole or passive analytics; (1)+(3) without (2) = campaign-style page testing; (1)+(2) without (3) = flag rollout without measurement.

### L1 — Common Mature Structure (present across the sample, not definitional)

- Feature flags/gates as the assignment substrate (5/5 carry flag machinery; flags-only use is a documented deployment variant)
- Environments separating configuration per deployment context (5/5)
- Attribute-based targeting/audiences as eligibility pre-filters (5/5)
- Layers/mutual exclusion for concurrent experiments (5/5)
- Statistical-engine machinery: sequential testing, variance reduction (CUPED family), multiple-comparison corrections, SRM detection, Bayesian/frequentist choice, sample-size/power calculators (5/5 in some form)
- Results surfaces: per-variant lift with confidence statements, segment/dimension breakdowns, exports
- Diagnostics/QA: exposure streams, event/exposure mismatch detection, non-production QA, A/A tests
- Sticky/persistent assignment across sessions and devices
- Integration spine: event pipelines, warehouses, CDPs, collaboration tools; APIs/CLI/config-as-code

### L2 — Variant Structure (segment- or philosophy-specific)

- Data posture: vendor-hosted analytics vs warehouse-native analysis vs open-source self-hosted
- Modularity: unified full-stack platform vs composable two-component architecture vs modular flags-only/analysis-only use vs flag-first add-on
- Assignment surface emphasis: server-side-first vs client-side/edge vs both
- Randomization-unit breadth: user/device/session/custom; multi-entity (marketplace participants); switchback designs
- Bandits/autotune as an allocation mode (optimization replacing comparison)
- Holdouts as program-level impact measurement (documented at 2/5 in fetched pages; program-guide context in others)
- Experimentable-object breadth: product features only vs infrastructure/APIs vs AI agents/prompts/models
- Visual editor as an additional surface (present in the pole as optional, not default)
- Program-methodology posture: tool-only vs vendor-published program playbooks

### L3 — Vendor-Specific Detail (kept out of the final document)

See Vendor-specific Findings below.

## Vendor-specific Findings

- **Statsig**: splits cap at 50/50 for experiments while gate Pass % can exceed 50/50; gate exposures bucketed Pass/Fail/Fail–Not-in-Analysis with only the balanced subset used for comparison; layer exposures deduplicated (10-minute window client SDKs, ~1 minute server SDKs — billable-exposure mechanics); free tier cited at "up to 5M events per month" in the program guide; AI Experimentation in Early Access "not accepting new customers."
- **Eppo**: SDK performs no tracking (BYO event-logging interface); layer allocations fixed at four levels (opt-out/experiments/rollout/default); holdout assignment uses composite keys ending with the holdout key; confidence-level defaults settable company-wide or per experiment; cites Microsoft research on the rarity of interaction effects; layer experiments can use as little as 2% of a layer.
- **GrowthBook**: aggregates-only data exchange (sums, sums of squares — no raw events/PII to the vendor); stats engines published on GitHub; sample-size rule of thumb "at least 200 conversion events per variation"; typical test duration 1–2 weeks; namespaces require the same hash attribute across experiments.
- **LaunchDarkly**: Experimentation keys metered per unique context key per experiment; Data Export-only experiments run assignment without in-UI analysis; AgentControl configs are experiment-capable alongside flags; holdout guide recommends deciding inclusion per experiment and ending holdouts after a set period.
- **Optimizely**: experiments must be the first rule in a flag's ruleset when combined with deliveries; Rollouts free plan includes one A/B test; REST API requires GET-then-PATCH on rulesets; QA events discarded after non-production testing; Feature Experimentation succeeded legacy "Full Stack" (projects after February 2021).

## Rejected Findings

- **"A digital experimentation platform is a different structure from an A/B testing platform"** — rejected as a structural claim. The shared core (variants + randomization + measured comparison + decision) is identical across both labels; vendors ship both under one roof (Optimizely Web + Feature Experimentation explicitly paired "to build a company-wide experimentation program"; VWO Testing + Feature Experimentation per the a-b pass; Statsig self-describes its core as A/B RCTs). The two leaves are two audience poles of one structure. (This discharges the a-b-testing pass's flag.)
- **"The metrics layer is definitional"** — rejected at definitional strength. All five sampled products hold metrics as managed reusable objects, but the sibling pole also has reusable goal/tracker libraries; the difference is degree of data-estate anchoring, not kind. Kept in L1/L2 with the center-of-gravity framing.
- **"Warehouse-native analysis is definitional"** — rejected. Hosted-analytics realizations (Optimizely Stats Engine, Statsig Cloud, LaunchDarkly hosted metrics) satisfy the core; warehouse-native is a data-posture variant.
- **"Feature flags are definitional"** — rejected. The assignment substrate can be flags, inline SDK experiments, or external/custom assignment (GrowthBook's custom-assignment mode; Eppo's analysis-only mode; LaunchDarkly's Data Export experiments). Flags are the dominant substrate (L1), not the invariant.
- **"Experimentation on AI agents/models is a new separate Type"** — rejected at this depth. Live-traffic RCTs on AI features (LaunchDarkly AgentControl experiments, Statsig OpenAI/Azure integrations) satisfy the same core with a new experimentable object; recorded as an L2 scope variant. Pre-registered model evaluation (§13 leaves) remains a different object of work.
- **"Holdouts are definitional"** — rejected. Documented as first-class in 2/5 fetched samples; the core survives without them (program-level impact measurement is maturity).

## Boundary Findings

### vs A/B Testing Platform (sibling leaf, §06) — JOINT REVIEW DISCHARGED

The a-b-testing pass flagged: "one shared defining core… two philosophies — probable audience-gradient split rather than two structures." **Confirmed from this side; keep-both ratified as two audience poles of one structure, mirroring the ai-coding-assistant/ai-coding-agent resolution pattern.**

Evidence:

- The L0 core is identical across both labels (this pass's five products all satisfy the sibling's L0 verbatim).
- Vendors ship both poles under one roof and name the pairing themselves: Optimizely pairs "Web Experimentation" (client-side) with "Feature Experimentation" (server-side) "to build a company-wide experimentation program"; VWO ships Testing + Feature Experimentation (a-b pass); Statsig, an engineering-native platform, describes its core as "randomized controlled trials (A/B or A/B/n tests)."
- The poles differ in center of gravity, not in structure: audience (marketing/CRO vs product/engineering/data), default authoring surface (visual editor on pages vs parameters in code), packaging (campaigns vs continuous program), metrics anchoring (per-campaign tracker libraries vs data-estate-anchored metrics layer), program machinery (campaign portfolio vs concurrent-experiment management with layers/holdouts).

Structural tests (recorded both directions):

- Remove code-integrated assignment and product-object scope (keep visual-editor page testing) → the A/B Testing Platform remains.
- Remove visual-editor page testing and campaign packaging (keep server-side parameters, metrics layer, program machinery) → this leaf remains, fully functional.

No taxonomy change requested; the directory's two leaves are retained as adjacent points on an audience/surface gradient with a shared framing. Both final documents state the gradient relationship.

### vs Feature Flag Management Platform (§14, processed 2026-09-08)

Consistent with that pass's own framing (control-as-center vs measurement-as-center):

- The flag platform's deliverable is controlled behavior of running software (registry + evaluation + rollout); measurement is optional and can be delegated entirely (GrowthBook's "Feature Flags Only" use case is the vendor's own statement of this pole).
- This Type's deliverable is the measured causal comparison; flag machinery is the dominant assignment substrate but a means, not the end.
- Remove measurement/decision machinery → flag platform remains; make metric-driven assignment + analysis the center → this leaf. The interlock is documented by the vendors themselves (Statsig: "flags automatically convert a feature rollout into an A/B test"; Eppo/LaunchDarkly/Optimizely/GrowthBook all implement experiments as flag rules or flag-attached analyses).

### vs Product Analytics / product-usage-adoption-platform (§07, processed 2026-09-06)

- Analytics observes behavior without intervening; experimentation intervenes by randomizing assignment to establish causality. Statsig's own framing: "Historical metrics may show correlation, but experiments allow you to establish causal relationships." The analytics layer ships inside several sampled products (Statsig product analytics, Eppo/GrowthBook warehouse analysis) as a sibling capability, not the Type center.

### vs Marketing Personalization Platform (§06, processed 2026-09-08)

- Assignment-logic seam confirmed: personalization assigns deterministically by visitor condition; experimentation assigns randomly to compare. Bandits (Statsig Autotune, Eppo contextual bandits, GrowthBook MAB rules) are an optimization mode that replaces comparison with exploitation — an L2 allocation mode inside this Type, adjacent to the personalization seam.

### vs Marketing Mix Modeling / Marketing Attribution (§06, processed 2026-09-08)

- Interventional causal lift vs observational modeling/credit. The MMM pass recorded that media-incrementality testing (geo lift/conversion lift) has no dedicated leaf and that the nearest leaves (A/B Testing Platform, Digital Experimentation Platform) are "product-experimentation-flavored" — consistent from this side: Eppo explicitly accepts randomization logs from email marketing systems and ML models, i.e., the assignment machinery generalizes beyond product features, but the Type's center remains product/software experimentation.

### vs Conversion Rate Optimization Platform (§06, processed 2026-09-07)

- CRO is the practice-framed superset (diagnosis + observation + testing); testing-only products trading under CRO labels belong structurally to the A/B Testing Type per that pass. This leaf is the engineering pole of that testing structure; no conflict.

### vs ML/Model Evaluation leaves (§13, processed)

- Different object of work: model-evaluation platforms test models against standardized instruments pre-release; this Type runs live-traffic RCTs on the product (including its AI features). Overlap zone: experiments whose treatment is an AI model/prompt/agent config (LaunchDarkly AgentControl, Statsig AI integrations) — recorded as an L2 scope variant of this Type; no taxonomy change proposed.

### vs Remote-configuration services (per the feature-flag pass boundary)

- Value-delivery orientation (deliver config values to clients) vs measurement orientation (decide, expose, compare, ship). Dynamic-config capabilities inside sampled products (Statsig dynamic configs, Eppo dynamic configuration) are the same machinery serving the flag pole; recorded as capability-inside-Type.

### "Remove what → becomes what" summary

- Remove randomized assignment (keep rule-based delivery) → personalization/rollout machinery.
- Remove measurement + decision (keep registry + evaluation + rollout) → Feature Flag Management Platform.
- Remove code-integrated assignment (keep visual-editor page testing) → A/B Testing Platform (sibling pole).
- Remove the experiment record's variants/comparison (keep observation) → product analytics.
- Remove the product anchoring (experiment on anything) → generic statistical tooling, not an application Type in this directory's sense.

## Historical / Market-Sample Check

- **In-house/home-built experimentation systems**: assignment in application code + analysis in notebooks or the warehouse — the exact shape GrowthBook documents as first-class support ("custom assignment or 3rd-party experiments… use GrowthBook to analyse the results") and Eppo supports via analysis-only mode and external randomization logs. These satisfy the core: experiment record (even if lightweight), variants, randomized in-code assignment, measured comparison, decision. ✓
- **Early open-source/self-hosted A/B tools and analytics-platform-native experiment features** (snippet-based, e.g., the Google Website Optimizer/analytics-content-experiments lineage): satisfy the shared core with the sibling pole's delivery surface; the Type's core does not require SDK-native assignment any more than it requires SaaS. ✓
- **Boolean-only, single-experiment deployments** (a team running its first server-side A/B test behind one flag): satisfy the core without layers, holdouts, warehouse integration, or program machinery. ✓
- No L0 element is a post-2015-only implementation: randomized in-code assignment and measured comparison predate the current SaaS wave; the modern additions (warehouse-native analysis, bandits, AI-agent experiments) are all L1/L2. ✓
- The word "digital" in the leaf name binds the domain (digital products/experiences), not a structure; the market's dominant label is "experimentation platform." Recorded as a naming observation.

## Uncertainties

1. **Analytics-native pole under-evidenced**: Amplitude Experiment (and Kameleoon/Convert as CRO-side hybrids) were not fetched; the analytics-native realization is covered only structurally (Statsig bundles product analytics; Eppo/GrowthBook analyze from warehouses). Expected to satisfy the core, but this is inference, not observation.
2. **Statsig holdouts**: the program guide references measuring program impact, but the holdout object was not directly fetched for Statsig; holdout evidence rests on Eppo + LaunchDarkly Tier-1 pages.
3. **Optimizely analysis depth**: results analysis lives in the support help center (fetched at category level by the a-b pass); this pass fetched the developer docs. Optimizely's analysis-layer claims are kept general.
4. **VWO Feature Experimentation**: not fetched this pass; the "suite vendor ships both poles" claim for VWO rests on the a-b-testing pass's product-page-level evidence.
5. **Pricing/plan tiers**: out of scope; free-tier facts (Optimizely Rollouts, Statsig free tier) recorded as positioning only.
6. **Holdout prevalence**: first-class holdout objects documented at 2/5 in fetched pages; prevalence across the wider market (e.g., Amplitude, Kameleoon) unverified.

## Final Synthesis

A Digital Experimentation Platform is the product organization's system for running controlled experiments on its own software product. The defining core is the shared controlled-experiment structure — experiment record with variants, randomized assignment of real users, measured comparison against managed metrics, and a ship/keep/discard decision — delivered through assignment machinery integrated into the running software (SDK/API evaluation whose results application code consumes as parameters, flags, and configs). Around that core, the mature products in this pole converge on a recognizable working layer: feature flags as the assignment substrate, environments, attribute targeting, layers for mutually exclusive concurrent experiments, a statistical engine with validity machinery (sequential methods, variance reduction, multiple-comparison corrections, SRM detection, power calculation), diagnostics and QA, sticky assignment, and warehouse-or-hosted data postures. What characterizes the pole against its sibling is center of gravity, not structure: product/engineering/data teams rather than marketers; parameters in code rather than visual editors on pages; a data-estate-anchored metrics layer rather than per-campaign goals; a continuous program (concurrent experiments, holdouts, reviews, velocity culture) rather than a campaign portfolio; and an experimentable object that is the organization's own software stack — features, APIs, infrastructure, and now AI agents and models. The joint review with the A/B Testing Platform leaf resolves as keep-both: one structure, two audience poles, vendors shipping both under one roof, with the gradient — not a wall — between them.
