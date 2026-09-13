# Research Notes — ML Model Monitoring Platform

Research date: 2026-09-08
Slug: ml-model-monitoring-platform
Directory leaf: ML Model Monitoring Platform (§13 Data, Analytics & AI Systems)

---

## Research Goal

Understand what an ML Model Monitoring Platform is as an Application Type: what it watches, what objects exist inside it, how a deployed model's behavior is evaluated over time, what surfaces operators use, and where its boundaries sit against neighboring Types (MLOps Platform, Machine Learning Platform, Model Registry, Data Observability Platform, LLM Observability Platform, Observability/APM, AI Model Evaluation Platform).

## Initial Boundary Hypothesis

- Core use: watch predictive ML models after deployment — detect input/prediction drift, data-integrity problems, and performance degradation once ground truth becomes available, and surface departures as alerts.
- Primary users: data scientists, ML engineers, MLOps/platform teams; secondary: model owners, risk/compliance roles in regulated industries.
- Nearest neighbors: MLOps/ML platforms (which bundle monitoring as a module), data observability (same watch-loop shape but subject = data assets), LLM observability (same industry, different central record: traces), APM (software telemetry), model registry (version records).
- Key unknowns at start:
  1. Is "monitoring" metric-evaluation-over-time or per-request tracing? (Affects boundary with LLM Observability / APM.)
  2. What is the baseline/reference object and where does it come from?
  3. How is performance measured when ground truth arrives late or never?
  4. Is the dedicated-product market still alive given the LLM-observability pivot? (WhyLabs status was unknown at start.)

## Research Questions

1. What is the monitored subject — model, endpoint, model version, deployment?
2. What does the platform observe (inputs, features, predictions, actuals, traffic)?
3. What is evaluated and against what reference (drift, integrity, performance, volume)?
4. What detection machinery exists (monitors, rules, anomaly detection, thresholds)?
5. What happens after detection (alerts, channels, history, investigation surfaces)?
6. How does production data get in (push SDK, warehouse query, native capture)?
7. What role does the training pipeline play (baseline from training data, retraining trigger)?
8. Where does delayed ground truth fit?
9. What are the variants (library vs platform, dedicated vs cloud module, SaaS vs self-host)?
10. Boundary: what must be removed before this becomes another Type?

## Representative Products

Selected for market representation, documentation completeness, differing product philosophy, and differing customer tier:

| Product | Philosophy / tier | Evidence reached |
|---|---|---|
| Fiddler | Dedicated enterprise AI-observability platform; ML + LLM + agents | Tier-1 docs: ML Observability + monitoring overview |
| Evidently | OSS evaluation library first, platform second (self-hosted or cloud) | Tier-1 docs: ML monitoring quickstart + platform overview |
| Aporia | Dedicated platform, query-time ingestion (connects to stores where predictions already live) | Tier-1 docs: overview, data sources, monitors & alerts, why-monitor concepts |
| SageMaker Model Monitor (AWS) | Cloud-suite module pole; minimal scheduled-monitoring loop | Tier-1 docs: model-monitor main page |

Market-structure products observed but NOT used as canonical samples:

- WhyLabs — **discontinued operations** (shutdown notice on docs.whylabs.ai, directly observed 2026-09-08); platform open-sourced; whylogs/langkit continue as OSS. Excluded as sample; recorded as market evidence.
- Arize — docs and site fully repositioned around "Arize AX" (agents/LLM tracing, evals, experiments); classic ML-monitoring surface no longer the documented center. Recorded as market evidence (pivot), not sampled.
- Vertex AI Model Monitoring — WebFetch timed out twice; abandoned. Cloud-module pole covered by SageMaker only.

## Sources

Fetched 2026-09-08:

1. Fiddler — ML Observability (docs.fiddler.ai/getting-started/ml-observability); Observability overview (docs.fiddler.ai/observability/monitoring)
2. Evidently — docs root; ML monitoring quickstart (docs.evidentlyai.com/quickstart_ml); Platform overview (docs.evidentlyai.com/docs/platform/overview)
3. Aporia — docs root; Data Sources overview; Monitors & Alerts overview (monitor-overview.md); Why Monitor ML Models (core-concepts/why-monitor-ml-models.md)
4. Amazon SageMaker AI — Model Monitor main page (docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
5. WhyLabs docs root (shutdown notice) — market evidence only
6. Arize docs root + arize.com — market evidence only

Evidence layers used below: **A** = directly observed on one product's official docs; **B** = cross-product commonality; **C** = canonical inference from comparison and boundary reasoning.

---

## Product Observations

### Fiddler (dedicated enterprise platform) — Evidence Layer A

From ML Observability and Observability overview docs:

- Positioning: "Monitor traditional ML models in production… Track performance, detect data drift, run root cause analysis, and ensure model fairness at scale." Platform spans traditional ML, LLM applications, and multi-agent systems.
- Three-step onboarding loop (documented as steps): (1) **Onboard your ML model** — define inputs, outputs, and related metadata; (2) **Publish your model data** — "send the 'digital exhaust' from your model serving platform to Fiddler" (push ingestion via SDK); (3) **Monitor performance** — "use dashboards and alerts."
- ML model observability capabilities: drift detection (documented naming: JSD and PSI metrics for distribution shifts); performance tracking (accuracy, precision, recall, F1 across deployments); data integrity (missing values, type mismatches, range violations); traffic monitoring (volume patterns, anomaly detection); vector/embedding monitoring (UMAP visualization).
- Advanced: model segmentation / cohort analysis; model version comparison; custom formula-based metrics; statistical analysis.
- Investigation surface: "four-part analysis experience" — events browse, feature-by-feature drift breakdown with prediction impact, data-integrity violation summaries, interactive analyze charts (confusion matrices, prediction scatterplots, feature distributions); root cause analysis.
- Alerting: drift alerts, data-integrity alerts, performance alerts, custom-metric alerts, traffic alerts; warning and critical threshold configuration; notification channels (email, Slack, PagerDuty, webhooks); alert history and audit logs; template-based alert creation.
- Dashboards: auto-generated per-model dashboard; custom dashboards; model comparison; collaboration/sharing.
- Fairness: segment analysis and bias detection named as a capability.

### Evidently (OSS library + platform) — Evidence Layer A

From docs root, ML monitoring quickstart, platform overview:

- Positioning: open-source framework (Apache 2.0) for "evaluate, test, and monitor data and AI systems… from predictive ML models to complex LLM-powered systems." Library + platform (self-hosted or cloud).
- ML monitoring quickstart structure: prepare **reference dataset** vs **production/current dataset**; run a Report with a DataDriftPreset; results render as an interactive report with summary scores and test results; JSON/HTML export.
- Explicit scope statement: evaluating "prediction quality (e.g. classification or regression accuracy), input data quality (e.g. missing values, out-of-range features), data and prediction drift." Drift evaluation "helps you detect shifts in the model quality and environment **even without ground truth labels**."
- Library model: 100+ metrics, declarative testing API, Reports/Tests with pass/fail; conditional Test Suites; presets.
- Platform model: monitoring = "run evaluations for live systems in batch or real-time. Track results on a dashboard and connect back to raw data as needed. Set alerts for violations." Projects store evaluation runs and datasets; dashboards with panels; regression testing via test suites; tracing (Tracely, OpenTelemetry-based) to collect production input-outputs.
- The library used manually (notebook reports) is explicitly distinguished from continuous monitoring on the platform ("Local Reports are great for one-off evaluations. To run continuous monitoring… upload the results to Evidently Platform").

### Aporia (dedicated platform, query-time ingestion) — Evidence Layer A

From docs root, data sources, monitors & alerts, why-monitor concepts:

- Positioning: "ML observability platform… visualize models in production, detect and resolve data drift, model performance degradation, and data integrity issues." Customization named as core philosophy (custom dashboards, monitors, metrics, segments).
- Ingestion philosophy: "monitors your models by connecting **directly** to your data" — supported sources include S3, Athena, BigQuery, Databricks, Glue, GCS, PostgreSQL, Redshift, Snowflake, Azure Blob, MSSQL. If predictions are not stored, a companion guide covers storing them.
- Model setup: create a **model version**; link a dataset by defining a query; **map the model schema** — raw inputs, features, predictions, **actuals**. Direct quote on delayed ground truth: "The ground truth can be `NULL` until it actually has value, that's okay."
- Monitor types (documented taxonomy): **Integrity** (new values, missing values, out-of-range); **Performance** (use-case KPIs; "decide when it's best to retrain"); **Drift** (features or predictions); **Activity** (volume changes "that need further investigation").
- Comparison methods (documented taxonomy): absolute values; change in percentage vs baseline; anomaly detection vs baseline; compared to (another) segment; **compared to training** (baseline = reported training data filtered to the segment).
- Practice guidance: per-model custom dashboard reviewed periodically + alerts for drift, performance degradation, integrity, custom-metric anomalies; customize alerts "to avoid false positives and alert fatigue."

### SageMaker Model Monitor (cloud-suite module pole) — Evidence Layer A

From AWS docs main page:

- Positioning: "monitors the quality of… machine learning models in production… set alerts that notify you when there are deviations in the model quality."
- Monitored subjects: real-time endpoints or batch transform jobs. Enable **data capture** of incoming requests + resulting predictions (or batch inputs/outputs).
- **Baseline from the dataset used to train the model**: baseline computes metrics and suggests **constraints**; live predictions are compared to the constraints; departures are reported as **violations**.
- **Monitoring schedule**: specify what data to collect, how often, how to analyze it, which reports to produce; recurring executions.
- Outputs: reports comparing latest data to baseline; violations; metrics; notifications via Amazon CloudWatch; visualization in SageMaker Studio.
- Monitoring types: data quality, model quality (drift in metrics such as accuracy), bias drift in predictions, feature-attribution drift.
- Constraints/notes: computes metrics on **tabular data** (non-tabular inputs: output statistics only); single-model endpoints; pipeline-level capture.
- Availability note (directly observed): "no longer open to new customers… we do not plan to introduce new features."

### Market-structure observations (Evidence Layer A on each statement)

- WhyLabs shutdown notice (docs.whylabs.ai, observed 2026-09-08): "WhyLabs, Inc. is discontinuing operations… privilege to define the AI Observability category." Platform open-sourced; whylogs/langkit continue as OSS.
- Arize (docs.arize.com + arize.com, observed 2026-09-08): product and docs repositioned as "Arize AX," an AI-engineering platform centered on traces, Signal, evaluators, experiments for agents/LLM apps; customer stories still mention "traditional ML" alongside agentic GenAI, but ML monitoring is no longer the documented center.
- SageMaker Model Monitor closed to new customers (AWS docs, directly observed).
- Of the four canonical samples, Fiddler and Evidently document LLM/GenAI monitoring alongside ML; Aporia's fetched pages remain ML-centric; SageMaker's module is ML-only and discontinued.

---

## Cross-product Comparison

| Dimension | Fiddler | Evidently | Aporia | SageMaker Model Monitor |
|---|---|---|---|---|
| Monitored subject | model (versioned); ML/LLM/agents | AI/data systems; predictive ML one target | model **version** linked to data | endpoint / batch transform job |
| Ingestion | push (SDK, "digital exhaust") | library computes on dataframes; OTel tracing capture | query customer stores where predictions live | native endpoint data capture |
| Reference/baseline | comparisons vs training baseline | reference dataset vs current | training data / segment baseline / anomaly baselines | baseline from training dataset → constraints |
| Evaluated dimensions | drift, integrity, performance, traffic, embeddings | data drift, data quality, prediction drift, performance (labels) | drift, integrity, performance, activity | data quality, model quality, bias drift, feature-attribution drift |
| Ground truth | performance metrics across deployments | drift works without labels; performance with labels | actuals nullable until available (direct quote) | model-quality monitors require ground truth for that type |
| Detection surface | monitors + warning/critical alerts | Reports/Tests pass-fail; platform alerts | monitors (4 types) × comparison methods | scheduled jobs → violations |
| Notification | email/Slack/PagerDuty/webhook | alerts on violations | alerts (channels in product docs) | CloudWatch notifications |
| History/investigation | dashboards, RCA, segmentation, UMAP | dashboards over stored runs; drill to raw data | dashboards, segments, drill-down | reports; Studio visualization |
| Form | dedicated SaaS (+ air-gapped per docs) | OSS library / self-hosted platform / cloud | dedicated SaaS | cloud-suite module |

### Cross-product commonalities (Evidence Layer B)

1. **Identified monitored model** — every product organizes around a named model (version/endpoint) distinct from generic data.
2. **Observed production behavior = inputs + predictions (+ optional actuals)** — the same record shape (features, predictions, actuals) appears in all four.
3. **Evaluation against a reference point** — training data as baseline (Aporia "compared to training"; SageMaker baseline from training dataset), reference dataset (Evidently), chosen segments/periods, or anomaly baselines (Aporia, Fiddler traffic).
4. **Four recurring monitored dimensions** — drift (features/predictions), data integrity, performance vs actuals, volume/activity; each appears in at least three of four samples under different names.
5. **Scheduled/recurring or continuous evaluation** — SageMaker schedules; Evidently "batch or real-time"; Fiddler/Aporia continuous monitors.
6. **Alerts as the surfacing mechanism, with tuning guidance** — every sample documents alert machinery; Aporia and Fiddler discuss alert fatigue and thresholds.
7. **Retained comparable results + visualization** — dashboards/panels/reports over stored results with drill-down to raw records.
8. **Segmentation** — metrics per data slice (Fiddler cohorts, Aporia segments, SageMaker bias drift on segments).
9. **No training/deployment machinery of its own** — every product depends on the model running elsewhere; integration is the touchpoint.

### Vendor-specific (L3 — kept out of canonical core)

- Fiddler: JSD/PSI naming; UMAP embedding visualization; "Centor models"; four-part RCA layout; market-statistic claims (marketing).
- Evidently: presets (DataDrift/DataSummary), 100+ metric catalog, Test Suites, Tracely, synthetic-data generation.
- Aporia: five named comparison methods; named data-source connector list; "storing your predictions" companion guide.
- SageMaker: constraints/violations machinery; CloudWatch coupling; Studio visualization; tabular-only scope.
- Arize (market evidence): Signal/Alyx/experiments; agent pivot.

---

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

Recognizable as this Type only when all three hold:

1. **The deployed model under watch** — an identified, version-bound model serving production traffic whose prediction behavior (inputs/features and outputs/predictions, optionally late-arriving ground truth) the platform observes. Remove → data-quality/data-observability tooling or a prediction-log store.
2. **Ongoing evaluation of observed behavior against a defined reference** — time-windowed production distributions/metrics compared against a baseline (training data, reference dataset, prior period, expected values, or anomaly baselines) across at least drift and integrity, and model quality where ground truth exists. Remove → a prediction log/telemetry store; "monitoring" becomes logging.
3. **The recurring watch loop with surfaced departures and retained history** — evaluation runs on a schedule or continuously; departures fire alerts/notifications; results retained as comparable history with an investigation surface. Remove → one-off offline analysis (notebook / evaluation-library run); nothing "monitors."

Jointly-held load-bearing tests:

- 1 without 2 → prediction logging / data capture
- 2 without 1 → data-drift/data-quality evaluation over datasets (Data Quality / evaluation library)
- 3 without 1+2 → generic metric alerting
- 1+2 without 3 → a drift report generator / notebook analysis
- 1+3 without 2 → logging with threshold alarms but no reference semantics
- 2+3 without 1 → Data Observability Platform (subject = data assets)

### L1 — Common Mature Structure

- Per-model dashboards; custom panels
- Monitors as configurable evaluation objects (dimension + baseline/threshold + schedule)
- Notification channels (email/chat/paging/webhooks); alert history/audit
- Segmentation / cohort analysis; model version comparison
- Custom metrics/formulas
- Traffic/volume monitoring
- Delayed-actuals ingestion and joining (A-observed on Aporia; performance documented on Fiddler/Evidently/SageMaker)
- Investigation surfaces: drill-down to raw records, feature-level drift breakdowns, root-cause analysis
- Statistical distribution measures for drift (naming varies per product — L3)
- Feature-attribution drift — common in mature enterprise products, not definitional

### L2 — Variant / Optional Structure

- Ingestion philosophy: push SDK vs query-your-warehouse vs native serving-platform capture vs OTel-style instrumentation
- Form: dedicated platform vs OSS library + platform vs cloud-suite module
- Deployment: SaaS, self-hosted, air-gapped/VPC
- Data modality scope: tabular-first vs extended to embeddings/vectors/unstructured
- Regulated-industry overlays: bias/fairness drift monitoring (documented at SageMaker + Fiddler) — segment variant
- Retraining linkage ("decide when to retrain"; corrective-action framing) — workflow overlay, not machinery in all products
- LLM/GenAI monitoring bundling (current market trend)

### L3 — Vendor-specific

See vendor-specific list; pricing tiers, connector catalogs, named AI helpers.

---

## Historical / Market-Sample Check

- The minimal form is documented, not imagined: the cloud-module pole realizes the Type with nothing but capture → training-data baseline → schedule → violations → notifications. Dashboards, segmentation, embeddings, custom metrics are not required.
- The pre-platform practice (scheduled scripts comparing production distributions against training data and emailing deviations) satisfies all three L0 legs conceptually. The Type's core predates its dedicated vendors; the definition names no SaaS, dashboard, SDK, or metric brand.
- No era-specific technology (PSI/KS names, CloudWatch, notebooks, OTel) is load-bearing in the definition.
- Check passes: an older, regional, or self-built implementation still fits; today's LLM-heavy "AI observability" platforms also fit when they monitor a model version's behavior over time vs a reference — but when the central record becomes per-request traces, the product drifts toward LLM Observability.

---

## Boundary Findings

1. **vs Machine Learning Platform / MLOps Platform (§13, processed)** — monitoring ships there as an embedded standard capability (the ML-platform pass names "production monitoring" standard-NOT-definitional; sampled suites bundle monitoring with registry/serving). The dedicated Type centers watching/evaluating deployed-model behavior and owns no training/deployment/registry machinery. Keep-both; removal tests hold both directions. Forward flag: mlops-platform and model-registry leaves are unprocessed; expect monitoring named as a bundled capability there too.
2. **vs Model Registry (§13, unprocessed)** — object-of-record split: registry holds version records/stages/approvals; monitoring attaches evaluation behavior to deployed instances and consumes version identity (Aporia's model version + data linking documents the interlock). Keep-both expected; joint review recommended at the registry's pass.
3. **vs Data Observability Platform (§13, processed)** — same watch-loop shape, different subject: data observability evaluates data assets/pipelines (freshness/volume/schema) estate-wide with a stateful incident record; model monitoring evaluates model behavior (features→predictions→quality vs reference) per model version. Model-input integrity monitoring overlaps data-quality semantics (gradient); without the prediction/model-reference leg the product is data observability. Consistent with that pass's seams.
4. **vs LLM Observability Platform (§13, processed)** — central record differs: LLM observability = instrumented per-request execution traces; model monitoring = time-windowed aggregate behavior vs reference. The market is converging (WhyLabs shutdown, Arize pivot, SageMaker sunset; Fiddler/Evidently bundle both) — bundling gradient, keep-both, consistent with that pass's core. Flag for any future consolidation review.
5. **vs Observability Platform / APM (§14, unprocessed)** — software telemetry (service latency/errors) vs model behavioral quality. Traffic/volume monitoring is the overlap gradient: model-serving latency belongs to APM; prediction quality belongs here.
6. **vs AI Model Evaluation Platform (§13, processed)** — market's models + standardized public instruments + selection decision vs the org's own deployed models + production traffic + reference comparison. Distinct.
7. **vs LLM Evaluation Platform (§13, processed)** — offline scored runs against test datasets vs live production watch. Distinct; complementary records.
8. **vs Data Quality Platform (§13, processed)** — rules-as-primary-object over data vs model-behavior evaluation; input-integrity monitoring is the capability gradient. Consistent with that pass's seams.
9. **Removal litmus for the Type as a whole** — take away the model/prediction subject → Data Quality/Data Observability; take away the reference comparison → prediction logging; take away the recurring watch loop → offline evaluation; replace aggregate time-window metrics with per-request traces → LLM Observability / APM.

---

## Uncertainties

1. Default drift methods/thresholds per product were not verified page-by-page (Evidently mentions default tests; specifics unfetched). No precise numbers asserted anywhere.
2. Fiddler's "real-time" performance tracking depends on actuals delivery; the join mechanics were not inspected. Performance-vs-actuals is documented as a capability; its timing nuance is not asserted.
3. Aporia's fetched docs are ML-centric; its current site positioning (possibly LLM-forward) was not verified. Aporia claims here are confined to fetched pages.
4. Vertex AI Model Monitoring unreachable (timeout ×2) — the cloud-module pole rests on SageMaker only; SageMaker is also discontinued for new customers, so the module-pole *live* market was not directly verified.
5. The LLM-bundling degree per vendor varies and evolves weekly; the market-structure statements are dated 2026-09-08 snapshots.
6. Notification-channel breadth for Aporia was not verified from a dedicated alerts page (alerts referenced on overview/monitor pages only).
7. Ground-truth-never-arrives cases: drift/integrity/activity monitoring still functions (Evidently states drift without labels; Aporia nullable actuals; Fiddler integrity/traffic alerts) — performance leg conditionally present, consistent with L0's "where ground truth exists" phrasing.

## Final Synthesis

**L0 (one sentence):** An ML Model Monitoring Platform continuously or recurrently evaluates the production behavior of an identified, version-bound deployed model — its input features, predictions, and (where available) outcomes — against a defined reference baseline, and surfaces departures as alerts over retained, comparable metric history.

**Canonical structure:** monitored model (version-bound subject) → observed prediction traffic (inputs/predictions/actuals) → baseline/reference (training data, reference dataset, prior period, anomaly model) → recurring evaluation (drift, integrity, quality-where-labels, volume) → retained comparable results → alerts + investigation surfaces.

**What it is NOT:** not the trainer/serving layer (ML/MLOps platform), not the version record (model registry), not data-asset health watching (data observability), not per-request tracing (LLM observability/APM), not market-model benchmarking (AI model evaluation), not offline scored test runs (LLM/ML evaluation).

**Market note:** the dedicated category is consolidating into broader "AI observability" platforms (direct evidence: WhyLabs shutdown, SageMaker module sunset, Arize pivot); the Type's defining structure persists inside dedicated platforms, OSS stacks, and cloud-suite modules.

---

## Application Document Input Map

- Overview ← L0 + boundary summary
- Users & Context ← ML/DS/MLOps roles documented across samples
- Core Model ← L0 legs + L1 capabilities (concept vs implementation separated)
- How It Works ← onboarding loop (Fiddler 3 steps; Aporia link+map; SageMaker capture→baseline→schedule) + watch loop
- Interfaces ← dashboards, monitor builders, alert configs, investigation surfaces
- Rules/Behaviors ← delayed actuals, label-less drift, alert fatigue, tabular scope (module pole), model running elsewhere
- Variants ← L2 list
- Related Types ← Boundary Findings 1–9
- Representative Products ← the four samples
- Sources ← Sources section above

<!-- END -->
