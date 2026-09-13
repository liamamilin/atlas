# Digital Experimentation Platform

## Overview

A **Digital Experimentation Platform** is the product organization's system for running controlled experiments on its own software product: it defines two or more versions of a feature or experience, randomly assigns real users to each version through machinery integrated into the running application, measures how each version affects managed product metrics, and turns the result into a ship-or-discard decision whose winner is rolled out through the same machinery.

The defining core is small:

```text
Experiment (a persistent, hypothesis-bearing record on the org's own product)
└── Variants (control + treatment(s)), expressed as parameters/flags the code consumes
    └── Randomized assignment decided inside the running software (SDK/API)
        └── Managed metrics compared across variants (lift + statistical confidence)
            └── Decision: ship a variant / keep control / discard — winner rolled out
```

Everything else commonly associated with the category — feature-flag registries, warehouse-native analysis, layers, holdouts, bandits, program playbooks, AI-agent experiments — is widespread in current products but is not what makes the product an experimentation platform. Simpler and older realizations (an in-house server-side split test with assignment in code and analysis in a notebook, a single boolean test behind one flag) satisfy the same core without any of those additions.

The platform answers the question no analytics tool can answer by observation alone: *did this change cause the improvement, or would it have happened anyway?* Vendors in this space state the same idea in their own words: historical metrics show correlation, experiments establish causality.

This Type is the engineering/product-team pole of the experimentation market. Its closest sibling, the A/B Testing Platform, shares the identical core and serves the marketing/CRO pole; the two are described together in Related Application Types below.

## Users & Context

Primary users:

- **Product managers** — turn feature ideas and roadmap bets into experiments, define success metrics, and make ship/no-ship decisions.
- **Software engineers** — integrate the SDK, expose parameters and flags the experiments control, and keep assignment and event instrumentation correct.
- **Data analysts / data scientists** — build and curate the metrics layer, scrutinize results, adjudicate statistical trustworthiness, and investigate anomalies.

Supporting roles:

- **Experimentation platform / growth teams** — operate the program: review results, manage concurrent-experiment allocation, measure program-level impact.
- **Executives / stakeholders** — read results and program-level reports to see what the experimentation effort is returning.
- **Administrators** — manage permissions, environments, and governance.

Typical contexts: software products of every shape — web applications, mobile apps, server backends, APIs, and increasingly AI features (prompts, models, agent configurations). The work is continuous rather than campaign-based: many experiments run concurrently, features ship behind flags that double as experiment scaffolding, and the program's health (velocity, win rate, trustworthy-decision rate) is itself measured. Mature organizations treat the platform as decision infrastructure for the product, not a marketing tool.

## Core Model

### The Defining Core

```text
Experiment
├── Hypothesis (what change, for whom, expected effect on which metric)
├── Variants (control + treatment(s)) — parameter/flag values the application consumes
├── Randomized assignment (SDK/API decides inside the running software; sticky per unit)
├── Metrics (managed, reusable definitions; primary decides, others watch)
├── Result (per-variant lift with statistical backing)
└── Decision (ship / keep / discard) → winner rolled out through the same machinery
```

- **Experiment** — the central object: a named, persistent record carrying the hypothesis, its configuration, its run state, and its results. In most products the experiment is literally attached to feature-flag machinery — a rule on a flag, an allocation in a layer, or a parameter-consuming object — so the same flag that rolls a feature out can measure it.
- **Variant** — one version of what is being tested. The control is the current behavior; treatments are the alternatives. Variants are typically expressed as parameter values, flag variations, or JSON configurations that application code reads and acts on — not as page mark-up the platform renders.
- **Randomized assignment integrated into the running software** — the platform's SDK or API decides, at runtime and inside the application, which variant each eligible user receives, keyed on a **randomization unit** (commonly the user; also device, session, workspace, or custom units). Assignment is sticky: the same unit keeps its variant for the life of the experiment. This is the property that separates experimentation from rule-based targeting, and code-integrated delivery is what separates this pole from page-surface testing tools.
- **Managed metrics** — the measured outcomes. Metrics are held as reusable, organization-level objects (computed from event streams or from the customer's data warehouse), not ad-hoc per-test goals. A **primary metric** decides the experiment; secondary metrics watch for side effects; guardrail metrics protect business-critical numbers.
- **Result** — the per-variant comparison: observed lift with a statistical statement of trustworthiness (confidence intervals and significance in frequentist products; probability-to-be-better and related quantities in Bayesian products).
- **Decision** — the terminal output: ship the winner (rolled out through the flag/parameter machinery that ran the experiment), keep control, or discard. The decision is the reason the platform exists.

### Standard Capabilities of Mature Products

These appear across the researched sample and are expected in practice, though they do not define the Type:

- **Feature flags as the assignment substrate** — gates, variations, and rollout rules that double as experiment scaffolding; the same flag moves a feature from dark launch to test to full rollout.
- **Environments** — separate configuration per deployment context (development, staging, production), with QA in non-production before exposing real users.
- **Targeting / audiences** — attribute-based eligibility conditions acting as pre-filters on who enters an experiment.
- **Layers / mutual exclusion** — containers that keep concurrent experiments on the same surface from overlapping, often with shared parameters so new experiments run without code changes.
- **Statistical engine** — sequential testing methods that permit safe interim looks, variance-reduction techniques that use pre-experiment data, multiple-comparison corrections across many metrics, sample-ratio-mismatch detection, sample-size and power calculators, and a choice of frequentist or Bayesian methodology.
- **Results surfaces** — per-variant metric lifts with confidence statements, segment and dimension breakdowns, exports, and in some products program-level views (aggregate impact of all shipped experiments).
- **Diagnostics / QA** — live exposure streams, checks that exposures and events match, A/A tests to validate the pipeline, and discardable QA traffic.
- **Sticky assignment** — persistent bucketing across sessions, devices, and releases so users do not switch variants mid-experiment.
- **Integration spine** — event pipelines, data warehouses, analytics and collaboration tools; APIs, CLIs, and configuration-as-code for managing experiments programmatically.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Assignment machinery
Implementations:    server-side SDK parameters, client-side SDK flags,
                    edge evaluation, custom/external assignment logs

Concept:            Metrics source
Implementations:    vendor-hosted event stream, customer data warehouse
                    (annotated tables → metrics), hybrid ingestion

Concept:            Data posture
Implementations:    vendor-hosted analytics, warehouse-native analysis
                    (raw data stays in the customer's warehouse),
                    open-source self-hosting

Concept:            Decision output
Implementations:    winner rollout via flag rules, parameter default change,
                    archive with recorded learning
```

## How It Works

The canonical loop:

```text
1. Formulate a hypothesis (action → predicted outcome → rationale)
2. Build the experiment on flag/parameter machinery (variants, metrics)
3. Target the audience and set allocation
4. Instrument assignment and events (SDK integration)
5. QA in non-production; validate exposures and events
6. Start — randomized assignment begins
7. Monitor (diagnostics, guardrails, sample-ratio checks)
8. Conclude — decide on the primary metric
9. Roll out the winner (or discard); archive the learning
```

**1. Formulate a hypothesis.** The experimenter states what change will affect which audience and which metric. Mature products provide a hypothesis field with a fill-in template, because the hypothesis determines the primary metric and keeps the decision honest.

**2. Build the experiment.** Variants are configured as parameter values or flag variations in the platform's UI or API; application code already reads those parameters. Because assignment rides on flag machinery, a feature can move from gradual rollout to measured experiment and back without new code — the pattern one vendor's program guide describes as turning every upcoming feature into an experiment.

**3. Target and allocate.** Targeting conditions (attributes, existing gates) decide who is eligible; allocation decides what share of that audience participates and how it splits across variants. Practitioners start small and ramp up.

**4. Instrument.** The SDK assigns users and logs exposures; events that feed metrics come from the application's own tracking, an event pipeline, or the data warehouse. Several products are deliberately hands-off: the SDK evaluates assignments locally and the customer's own event system supplies behavioral data, so raw user data need not pass through the vendor.

**5. QA and validate.** Before launch, the team verifies in a non-production environment that assignment fires, exposures log, and events match. Mature products surface live exposure streams and flag mismatches automatically, and QA traffic is kept out of the results.

**6. Start.** Randomized assignment begins. From this point assignment is sticky.

**7. Monitor.** Results accumulate per variant. Early data is diagnostic; sequential-testing methods make interim checks statistically safe where offered. Sample-ratio checks catch broken traffic splits; guardrail metrics catch harmful side effects, and some products can pause or roll back automatically.

**8. Conclude.** When the primary metric reaches a trustworthy state, the experimenter declares an outcome: treatment wins, control holds, or no meaningful difference.

**9. Roll out and archive.** The winner is pushed to everyone through the same flag/parameter machinery — often a single action that converts the experiment's treatment into the default experience. The record is archived as organizational learning.

### Running It as a Program

Beyond single experiments, mature deployments operate a continuous program: experiments run concurrently in layers that prevent interference; holdouts exclude a small share of users from all experiments to measure the program's aggregate effect; teams hold regular experiment reviews; and the platform's own health — experiment velocity, share of decisions made on trustworthy data — is tracked. Vendor documentation in this space treats program operation (idea generation, metric hygiene, review cadence, culture) as part of the product's job.

## Interfaces

### Experiments dashboard

The entry surface: lists experiments with status and key attributes.

- typical information: name, hypothesis excerpt, status, variants, allocation, owner, dates
- primary actions: create, open, filter/search, archive

### Experiment editor

The configuration surface for one experiment, usually organized as steps or tabs.

- typical information: hypothesis, variants/parameters, targeting conditions, allocation percentages, metric selection (primary/secondary/guardrail), schedule, layer membership
- primary actions: configure variants, set targeting/allocation, attach metrics, schedule, launch

### Results / report page

The analysis surface.

- typical information: exposures per variant, per-metric lift, confidence intervals or win probabilities, significance indicators, segment breakdowns; in some products program-level impact views (coverage and expected global effect of shipping)
- primary actions: switch metric views, filter by segment/dimension, adjust statistical settings, export, make the ship decision

### Diagnostics / QA mode

The verification surface used before and during a run.

- typical information: live exposure and event streams, assignment checks, error signals
- primary actions: force a variant, verify tracking, discard QA events, approve for launch

### Metrics and data management

Management surfaces for the reusable measurement layer.

- typical information: metric definitions, fact/event sources, metric collections, certification status
- primary actions: create/edit metrics, organize into collections, verify data quality

### Flags, layers, and holdouts

Management surfaces for the delivery and program machinery.

- typical information: flags and their rules/environments, layers and their experiments, holdout groups and their windows
- primary actions: create/configure flags, allocate layer traffic, start/end holdouts

## Important Rules / Behaviors

### Randomization is sticky

Once a unit is assigned a variant, it keeps that variant for the life of the experiment — across sessions, devices, and releases. Deterministic assignment keyed on the randomization unit is what keeps the comparison valid; products add explicit persistence mechanisms when experiment settings change mid-run.

### Assignment should coincide with exposure

Users who are assigned but never actually encounter the treatment add noise. Best practice, documented across the sample: expose as close to the treatment moment as possible, and filter un-exposed users out of the analysis where assignment and exposure cannot coincide.

### Allocation changes are asymmetric

Increasing an experiment's share of traffic is generally safe; decreasing it mid-run can bias group composition and pollute results — products warn against it or require a reset that re-randomizes users.

### Early results are diagnostic, not decision-grade

Stopping at the first significant reading inflates false positives. Products either warn explicitly, compute results on a fixed schedule, or offer sequential-testing methods that correct for interim looks.

### The primary metric governs the outcome

One primary metric decides the experiment; everything else is secondary or guardrail. Products restrict the primary metric to a single choice and, in some cases, lock it once the experiment starts, preventing post-hoc goal switching.

### Concurrent experiments can interfere — and usually do not

Experiments touching the same users can contaminate each other. Products provide layers (mutually exclusive universes) for the cases where overlap would genuinely break the experience, and vendor guidance notes that meaningful interactions are rare enough that blanket serialization costs more velocity than it saves.

### Broken randomization invalidates results

When traffic splits deviate from their configured ratios — through bugs, bots, or redirect loss — the comparison is untrustworthy. Mature products detect sample-ratio mismatch automatically and surface it before decisions are made on the data.

### Guardrails and safe rollouts bound the downside

A "winning" variant can still be unacceptable if it regresses something critical. Guardrail metrics watch for side effects; some products pause tests or roll back rollouts automatically when guardrails trip.

### The decision ships through the same machinery

The winning variant is rolled out with the flag/parameter machinery that ran the experiment — the distance from "decision" to "shipped" is deliberately short, and the experiment record is archived as organizational memory.

### Holdouts measure the program, not the experiment

Where offered, a holdout excludes a share of users from all (or selected) experiments for a period; comparing held-out users to everyone else estimates the aggregate effect of the whole experimentation effort — a negative result is a signal to examine the program, not one test.

## Variants

Common forms of the Type:

- **Unified full-stack platform** — flags, experiments, analytics, and session tooling in one product; the engineering organization's single decision infrastructure.
- **Composable two-component architecture** — a lightweight assignment SDK paired with a warehouse-native analysis platform; the SDK may do no tracking at all, with the customer's event system supplying behavioral data.
- **Open-source / self-hosted** — the same core run entirely on the customer's infrastructure, often with a hosted cloud offering of the same code.
- **Flag-first add-on** — experimentation as a capability of a feature-flag platform, where flags are the primary product and experiments attach to them.
- **Warehouse-native analysis** — results computed inside the customer's data warehouse; raw user-level data never leaves the customer's control.
- **Server-side-first vs client-side/edge delivery** — parameters consumed by backend code vs SDK evaluation in the browser/app or at the CDN edge; visual editors exist in some products as an optional surface, not the default.
- **Multi-entity and marketplace designs** — randomization units beyond the user (drivers, restaurants, workspaces), switchback designs that alternate treatments over time, and cluster analysis when assignment and analysis units differ.
- **Bandit allocation mode** — multi-armed and contextual bandits that shift traffic toward the best-performing variant during the run; optimization rather than comparison, shipped as a mode of the same machinery.
- **AI-feature experimentation** — experiments whose treatments are prompts, model choices, or agent configurations, using the same assignment and measurement core.
- **Analysis-only / assignment-only postures** — products (or product modes) that supply only the measurement layer for externally assigned experiments, or only the assignment layer with analysis exported elsewhere.

A variant remains a **Variant** unless it changes the defining core; all forms above keep the experiment record, randomized assignment integrated into running software, measured comparison, and decision intact.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| A/B Testing Platform | closest sibling — one structure, two poles | shares the identical core (variants + randomization + measured comparison + decision); this Type is the engineering/product pole (code-integrated assignment, product-object experiments, metrics layer, program machinery), the sibling the marketing/CRO pole (visual editor, page surface, campaign packaging). Vendors themselves ship both under one roof |
| Feature Flag Management Platform | adjacent, interlocked | flags control delivery (who gets what, on/off, gradual rollout); experiments measure effect. A flag platform can run with zero metrics; this Type cannot. Experiments commonly ride on flag machinery |
| Product Usage / Adoption Platform | sibling capability, opposite act | analytics observes behavior without intervening; experimentation intervenes by randomizing assignment to establish causality. Several products bundle both |
| Marketing Personalization Platform | assignment-logic seam | personalization assigns deterministically by visitor rule; experimentation assigns randomly to compare. Bandit modes sit between the two |
| Conversion Rate Optimization Platform | practice-framed superset | CRO is the goal (conversion diagnosis and improvement); experimentation is one instrument inside it |
| Marketing Attribution Platform | causal vs observational | attribution assigns observational credit for conversions; experimentation establishes causal lift through controlled intervention |
| Marketing Mix Modeling Application | causal vs observational, different grain | MMM models the whole marketing mix over history; experimentation tests discrete product changes on live traffic. Media lift tests are an adjacent experiment family |
| AI Model Evaluation Platform | different object of testing | model evaluation tests models against standardized instruments pre-release; this Type runs live-traffic experiments on the product, including its AI features |

The most important boundary is with the **A/B Testing Platform**: research across both samples found one shared structure expressed in two philosophies, with vendors themselves shipping both under one roof and naming the pairing. The distinction is a gradient of audience, delivery surface, and packaging — not a structural wall. The boundary with the **Feature Flag Management Platform** is the sharpest functional one: control-as-center versus measurement-as-center; remove the measurement and decision machinery from this Type and a flag platform remains.

## Representative Products

- **Statsig** — engineering-native, unified experimentation platform: feature gates, experiments, product analytics, and warehouse-native deployment; publishes its own program playbook
- **Eppo** — warehouse-native experimentation: a tracking-free assignment SDK paired with analysis that runs inside the customer's data warehouse
- **GrowthBook** — open-source, self-hostable experimentation and feature flagging; explicitly modular (flags only, analysis only, or both)
- **LaunchDarkly** — flag-first platform whose experimentation capability attaches experiments to flags and agent configurations, including program-level holdouts
- **Optimizely (Feature Experimentation)** — enterprise suite's server-side line: experiments as rules on feature flags, paired by the vendor with its client-side Web Experimentation product

The core model was checked against simpler and older patterns (in-house server-side split testing with external analysis, snippet-based website experiment features, single-flag boolean tests) to avoid over-fitting the definition to the current platform pattern.

## Sources

Research date: **2026-09-08**

- Statsig documentation — experiments overview, feature gates vs. experiments, experimentation program guide, layers: https://docs.statsig.com/experiments-plus/ , https://docs.statsig.com/api/content/guides/featureflags-or-experiments , https://docs.statsig.com/api/content/statsig-warehouse-native/guides/experimentation-program , https://docs.statsig.com/experiments/layers-overview
- Eppo documentation — platform overview, feature flags, layers (mutual exclusion), holdouts, experiment analysis, data management, statistics: https://docs.geteppo.com/ , https://docs.geteppo.com/feature-flagging/ , https://docs.geteppo.com/feature-flagging/concepts/mutual_exclusion/ , https://docs.geteppo.com/feature-flagging/concepts/holdout-config/ , https://docs.geteppo.com/experiment-analysis/ , https://docs.geteppo.com/data-management/ , https://docs.geteppo.com/statistics/
- GrowthBook documentation — overview, running experiments: https://docs.growthbook.io/overview , https://docs.growthbook.io/experiments
- LaunchDarkly documentation — experimentation guides, designing experiments, holdouts: https://launchdarkly.com/docs/guides/experimentation.md , https://launchdarkly.com/docs/guides/experimentation/designing-experiments.md , https://launchdarkly.com/docs/guides/experimentation/holdouts.md
- Optimizely developer documentation — Feature Experimentation introduction, run A/B tests: https://docs.developers.optimizely.com/feature-experimentation/docs , https://docs.developers.optimizely.com/feature-experimentation/docs/run-a-b-tests

> Sourcing limitation: all sampled products were evidenced directly from official vendor documentation (Tier 1). The analytics-native realization of the Type (experimentation embedded in a product-analytics platform) was not directly sampled and is described structurally only; holdout machinery is documented at Tier 1 for two of the five sampled products; one sampled vendor's results-analysis layer is documented in its support help center rather than its developer docs, so its analysis-depth claims are kept general. Precise statistical defaults, numeric limits, and plan-tier details are stated only where directly documented, and vendor-specific mechanics are excluded from the general description.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
