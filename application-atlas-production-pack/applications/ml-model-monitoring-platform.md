# ML Model Monitoring Platform

## Overview

An **ML Model Monitoring Platform** watches the behavior of a deployed machine learning model in production over time. It observes the inputs and predictions the model produces, evaluates them — continuously or on a schedule — against a reference point (most commonly the data the model was trained on), and surfaces departures as alerts: shifts in input or prediction distributions, data-integrity problems, and performance degradation where ground truth is available. Results are retained as comparable history for investigation.

The reason this software exists is that model degradation is silent. A deployed model keeps returning predictions even when the world it was trained on has drifted away; unlike broken software, a degraded model raises no errors. Monitoring closes that gap by comparing production behavior against what the model was built to expect.

The defining core is deliberately small:

```text
Monitored Model (identified, version-bound)
└── Observed Prediction Traffic (inputs + predictions, optionally late ground truth)
    └── Reference / Baseline to evaluate against
        └── Recurring Evaluation over time
            └── Departures surfaced as Alerts, retained as Comparable History
```

Everything commonly associated with modern products — per-model dashboards, segmentation, custom metrics, embedding analysis, fairness monitoring, LLM monitoring — is standard capability that mature products add, not what makes this Type recognizable. The platform itself owns no training, deployment, or serving machinery: the model runs elsewhere, and integration is the touchpoint.

## Users & Context

Primary users are the people accountable for model quality after deployment:

- **Data scientists / ML engineers** — configure what to watch (monitors, baselines, thresholds), receive alerts, and investigate departures against their knowledge of the model.
- **MLOps / platform teams** — operate monitoring across a portfolio of models, wire up ingestion and notification channels, and keep telemetry flowing.
- **Model owners / business stakeholders** — read dashboards to confirm models remain healthy, often on a periodic review cadence.
- **Risk and compliance roles** (regulated industries) — consume bias/fairness monitoring and audit trails where offered.

The context is the post-deployment phase of the model lifecycle: the model is already served by infrastructure this platform does not operate. Teams run anywhere from a handful to hundreds of monitored models, which makes portfolio-level views and reusable monitor templates practical concerns.

## Core Model

### The defining core

```text
Monitored Model (identified, version-bound)
└── Observed Prediction Traffic (features/inputs + predictions, + actuals when they arrive)
    └── Reference / Baseline (training data, reference dataset, prior period, defined expectations)
        └── Recurring Evaluation (time-windowed, scheduled or continuous)
            └── Retained Comparable Results → Alerts → Investigation
```

- **Monitored model** — the organizing record. A named, version-bound model registered with the platform, to which its traffic, baseline, monitors, and alerts attach. The version binding matters: behavior evaluation is only meaningful against a known model version, and version changes reset expectations.
- **Observed prediction traffic** — the platform's raw material: records of what went into the model (features/inputs) and what came out (predictions/scores), with actual outcomes (ground truth) joined when they become available. The same record shape — features, predictions, actuals — recurs across the market.
- **Reference / baseline** — the anchor every evaluation compares against. Most commonly the training dataset; also a labeled reference dataset, a prior time window, explicitly defined expectations, or a learned anomaly baseline.
- **Recurring evaluation** — monitors that run continuously or on schedules over time windows, producing aggregate metrics for each window. The record is time-windowed statistics over many predictions, not per-request traces.
- **Alerts + retained history** — departures notify people through configured channels; every evaluation result is stored, so metric evolution is visible and comparable — that history is what turns a one-off check into monitoring.

### What monitoring measures

Across the researched market, evaluation concentrates on recurring dimensions:

- **Data drift** — input/feature distributions shifting away from the reference (new categories, changing ranges, evolving populations).
- **Prediction drift** — the model's outputs shifting as a distribution, a proxy for trouble when labels are unavailable.
- **Data integrity** — missing values, out-of-range values, type mismatches, unexpected new values.
- **Model performance** — accuracy-class metrics, computable only when ground truth exists or arrives.
- **Volume / activity** — traffic patterns and their anomalies, commonly watched alongside the above.

The first four appear in essentially every mature product under varying names; volume monitoring is widespread but not universal.

### What mature products add

Standard capabilities beyond the core:

- per-model dashboards and custom panels
- monitors as configurable objects (dimension + baseline + threshold + schedule)
- notification channels (email, chat, paging, webhooks) with alert history
- segmentation — the same metrics computed per data slice or cohort
- model version comparison
- custom metrics and formulas
- delayed-actuals joining
- drill-down investigation: feature-level drift breakdowns, raw-record inspection, root-cause analysis
- feature-attribution drift and embedding/vector monitoring in more recent products

### One structure, many implementations

```text
Concept:            Getting production behavior in
Implementations:    push from serving via SDK / query the warehouse where predictions land /
                    native capture by the serving platform / OpenTelemetry-style instrumentation

Concept:            The reference point
Implementations:    training data / curated reference dataset / rolling time window /
                    fixed thresholds / learned anomaly baseline

Concept:            Product form
Implementations:    dedicated platform / open-source evaluation library + platform /
                    monitoring module inside a cloud ML suite
```

A reader who has met only one implementation — say, a dedicated SaaS platform fed by an SDK — should still recognize the warehouse-query form and the minimal suite module as the same Type from this model.

## How It Works

### Onboard a model

```text
Register the model (identity, version, schema: inputs / features / predictions / actuals)
→ connect the data (send telemetry, point at storage, or enable capture)
→ establish the baseline (usually training data or a reference period)
→ configure monitors and alerts
```

Onboarding is per model (and typically re-done or versioned per model version), because the schema mapping — which fields are features, predictions, actuals — is what gives later evaluation its meaning.

### The watch loop

```text
Evaluation runs (continuously or on schedule, over time windows)
→ window metrics computed for drift / integrity / performance / volume
→ compared against the baseline
→ departures fire alerts → routed to configured channels
→ open the dashboard → drill into the affected dimension
→ compare segments, inspect raw records, review feature-level shifts
→ act outside the platform (retrain, roll back, fix upstream data)
```

The platform informs the action; retraining and deployment live in other systems. Mature products frame this explicitly: monitoring tells you when it is time to retrain or investigate — the corrective machinery belongs to the wider MLOps estate.

### When ground truth is late

Performance evaluation depends on outcomes that often arrive days or weeks after prediction (a loan default, a churn event, a confirmed fraud). The market handles this structurally:

- drift, integrity, and volume evaluation work without labels — this is precisely why drift monitoring exists;
- actuals may be absent (null) for a period and are joined when they arrive;
- performance metrics populate progressively as ground truth lands.

So a model can be fully monitored — and can alert — long before anyone can compute an accuracy number for recent traffic.

### Tiers of capability

- **Defining core** — monitored model subject; observed inputs + predictions; reference-based evaluation over time; recurring loop; alerts; retained history.
- **Standard in mature products** — dashboards, segmentation, version comparison, custom metrics, notification integration, drill-down investigation.
- **Optional / variant** — bias/fairness monitoring, feature-attribution drift, embedding monitoring, LLM/GenAI monitoring, retraining-trigger integrations.

## Interfaces

Surfaces described conceptually; names and layouts vary by product.

**Model list / portfolio view**
Purpose: survey the health of all monitored models at a glance.
Typical information: models and versions, alert status, key metrics, last-evaluated time.
Primary actions: open a model, triage alerts, configure.

**Model dashboard (per model)**
Purpose: the primary monitoring surface for one model.
Typical information: performance metrics over time, per-feature drift charts, integrity violations, prediction distribution, traffic volume.
Primary actions: change time window, compare versions or segments, drill into a metric.

**Monitor configuration**
Purpose: define what is watched and when it alerts.
Typical information: monitored dimension, baseline/reference choice, thresholds, schedule, scope (segment).
Primary actions: create, edit, enable/disable, preview.

**Alerts / notifications**
Purpose: deliver departures to the right people.
Typical information: fired monitor, model, severity, timestamp, link to evidence.
Primary actions: acknowledge, route (email / chat / paging / webhook), inspect alert history.

**Investigation / analytics**
Purpose: explain why an alert fired.
Typical information: recent events/records, feature-by-feature drift, integrity summaries, distributions, segment comparisons.
Primary actions: filter, compare periods or segments, export.

**Administration**
Data-source connections, teams and roles, integration settings. Necessary because ingestion and notification are the platform's only live touchpoints with the outside.

## Important Rules / Behaviors

- **The model runs elsewhere.** The platform never trains or serves. Every capability depends on the integration holding — if telemetry stops, monitoring silently goes blind, which is why ingestion health itself is a monitored concern in mature setups.
- **An alert means "departure from reference," not "malfunction."** The semantic heart of every evaluation is comparison against the chosen baseline; changing the baseline changes what alerts mean.
- **Ground truth latency is structural, not exceptional.** Products explicitly tolerate absent actuals; drift monitoring exists so that problems are detectable before labels arrive. The performance leg is conditional by design.
- **Alerts require tuning.** Alert fatigue from overly sensitive monitors is a documented concern in the market's own guidance; configurable thresholds, warning-vs-critical severities, and scoped segments are the standard countermeasures.
- **Aggregates, not traces.** The central record is time-windowed metrics over populations of predictions. This is what separates the Type from per-request tracing and software-APM tooling.
- **Modality scope varies.** Some implementations compute statistics on tabular inputs only; embedding/vector monitoring is a newer extension and not universal.

## Variants

- **Dedicated platform** — multi-AI observability spanning ML models, LLM applications, and agents; ML monitoring is the historic core.
- **Open-source library + platform** — evaluation/reporting library used in notebooks, with a platform layer for continuous monitoring, storage, and alerts (self-hosted or cloud).
- **Cloud-suite module** — monitoring embedded in the suite that also trains and serves; may expose the minimal loop only: capture → baseline → schedule → violations → notifications.
- **Ingestion philosophy** — push telemetry vs query-your-warehouse vs native serving-platform capture.
- **Deployment posture** — SaaS, self-hosted, air-gapped/VPC for regulated customers.
- **Modality scope** — tabular-first vs extended to embeddings, text, and LLM workloads.
- **Regulated-industry overlays** — bias/fairness drift monitoring and audit-facing reporting.

## Related Application Types

| Application Type | Distinction |
|---|---|
| MLOps Platform | automates the model lifecycle (build → deploy → retrain); monitoring is one bundled capability; this Type owns no lifecycle machinery |
| Machine Learning Platform | the organization's build-and-operate system (training runs, model artifacts, deployment bridge); monitoring attaches afterwards |
| Model Registry | record machinery for model versions, stages, approvals; monitoring consumes version identity but holds no registry of record |
| Data Observability Platform | same watch-loop shape, but the subject is data assets (freshness, volume, schema) with a stateful incident record — not model behavior against a reference |
| Data Quality Platform | defined rules and tests over data as the primary object; model-input integrity overlaps, but there are no prediction/model semantics |
| Observability Platform / APM | software telemetry (latency, errors, saturation); a degraded prediction is not a software failure |
| LLM Observability Platform | instrumented per-request execution traces of LLM applications vs time-windowed aggregate behavior vs a reference; the market bundles both, but the central records differ |
| AI Model Evaluation Platform | evaluates the market's models with standardized public instruments for selection; this Type watches the organization's own deployed models |
| LLM Evaluation Platform | offline scored runs against curated test datasets; this Type watches live production behavior |

The sharpest seam is with MLOps/ML platforms, because monitoring ships as a module inside them. The removal test: strip monitoring from a lifecycle platform and the platform remains a lifecycle platform; strip the lifecycle machinery from a dedicated monitor and what remains is still a model monitor. When a product's central record becomes the per-request trace rather than time-windowed behavior metrics, it has crossed into LLM/application observability.

## Representative Products

- Fiddler — dedicated AI-observability platform spanning ML models and LLM applications
- Evidently — open-source evaluation library with a self-hosted or cloud platform on top
- Aporia — dedicated platform that connects directly to the stores where predictions already live
- Amazon SageMaker Model Monitor — the cloud-suite module form (closed to new customers at research time)

Market note: the dedicated category is consolidating into broader "AI observability" platforms — WhyLabs discontinued operations and Arize repositioned its documentation around LLM/agent observability during the research window. The Type's defining structure persists across dedicated platforms, OSS stacks, and cloud-suite modules.

## Sources

Research date: **2026-09-08**

- Fiddler — ML Observability; Observability overview — https://docs.fiddler.ai/getting-started/ml-observability ; https://docs.fiddler.ai/observability/monitoring
- Evidently — ML monitoring quickstart; Platform overview — https://docs.evidentlyai.com/quickstart_ml ; https://docs.evidentlyai.com/docs/platform/overview
- Aporia — documentation overview; Data Sources; Monitors & Alerts; Why Monitor ML Models — https://docs.aporia.com/
- Amazon SageMaker AI — Model Monitor — https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html
- WhyLabs (market evidence: shutdown notice) — https://docs.whylabs.ai/
- Arize (market evidence: repositioning) — https://docs.arize.com/arize ; https://arize.com/

> Sourcing limitation: Google Vertex AI Model Monitoring documentation could not be reached (repeated timeouts), so the cloud-suite module form rests on one sampled module. Precise defaults (drift thresholds, schedules, metric formulas, retention windows) are intentionally not stated in this document; vendor-specific metric names, connector lists, and layouts are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
