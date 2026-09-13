# LLM Evaluation Platform

## Overview

An **LLM Evaluation Platform** is a managed system for measuring how well an LLM application behaves: it runs the application's prompts and workflows — or captures its outputs from a live deployment — against curated test cases, scores the results against defined quality criteria using automated checks or human judgment, and stores each evaluation as a comparable record attributed to a specific version of the application.

Its purpose is to replace subjective spot-checking of non-deterministic software with repeatable measurement. The same input can produce different outputs, there is rarely a single correct answer, and a change that improves one quality dimension can silently degrade another. An evaluation platform makes "is this version actually better?" answerable with data — before a change ships and after.

The defining core is small:

```text
LLM application under test (prompts, model calls, workflows — reached
by running them or capturing their outputs)
└── Test-case dataset (inputs + expected outputs or grading criteria)
    └── Scoring (automated or human, applied per case)
        └── Persisted, comparable evaluation runs
            (attributed to a prompt/model/application version)
```

Everything else commonly associated with these products — LLM-as-judge graders, production traffic scoring, CI/CD regression gates, playgrounds, annotation queues — is standard capability of mature products, not what makes the product an evaluation platform. Remove the own-application subject and the product becomes a model benchmark; remove scoring against criteria and it becomes observability; remove persisted comparable runs and it becomes a script.

## Users & Context

Primary users are the people who build and iterate on LLM applications:

- **AI / application engineers** — connect the application to the platform, define test cases and scorers, run experiments, wire evaluation into CI
- **Prompt engineers / developers** — compare prompt, model, and workflow variants on the same dataset before promoting a change

Secondary users review quality without owning the code:

- **Product managers and subject-matter experts** — review outputs against rubrics, judge which of two responses is better, flag failures
- **Team leads / reviewers** — inspect experiment results and decide whether a version is ready to ship

The context is the LLM application lifecycle: during development, evaluation validates prompt, model, and code changes against curated datasets; in production, evaluation scores live traffic to catch regressions and discover failure cases; the two feed each other continuously.

## Core Model

### The defining core

Four structures. Every product in the researched sample has all four, and each is load-bearing.

**1. The LLM application under test, reachable for measurement.** The subject is the team's own LLM-driven system — a prompt template, a model configuration, a retrieval pipeline, an application workflow — not the market's models. The platform reaches it in one of several ways: it executes the prompt or task itself against configured model providers; it invokes the application's code through an SDK or library; or it captures outputs from an instrumented application via trace ingestion. What matters is that the platform can produce or obtain the system's outputs so they become measurable.

**2. Test-case dataset.** A curated, reusable collection of cases. Each case holds an input (what is fed to the application) and, optionally, a reference output or grading criteria (what "good" looks like). Datasets are versioned so comparisons target a known state, and cases are commonly sourced three ways: hand-written examples defining expected behavior, real production traces converted into cases, and user feedback signaling where the application fails.

**3. Scoring mechanism.** Defined scorers — automated or human — are applied to each case's result and produce feedback: a numeric score, a categorical label, or free-text commentary. Three scorer families recur across products:

- *code scorers* — deterministic checks (exact match, output is valid structure, required content present)
- *LLM-as-judge scorers* — an LLM grades the output against criteria written into a grading prompt, either comparing to a reference answer or judging reference-free qualities such as helpfulness, tone, or factual grounding
- *human scoring* — reviewers rate outputs, usually organized in review queues with rubrics, often comparing two variants side-by-side when judging "which is better" is easier than assigning an absolute score

**4. Persisted, comparable evaluation runs.** A run (commonly called an *experiment*) is the durable record of evaluating one version of the application on one dataset: per-case inputs, outputs, and every scorer's feedback. Runs are recorded as first-class objects and are comparable — the platform's comparison surfaces line up multiple runs over the same dataset so quality differences between prompt versions, model choices, or code changes are directly visible.

### Standard capabilities of mature products

These are widespread in the researched sample and expected by the market; they make evaluation practical but do not define the Type.

- **Offline evaluation** — batch scoring of a dataset against a candidate version before deployment, where reference outputs enable correctness checks
- **Online evaluation** — automated scoring of live production traffic as it arrives, without ground truth, restricted to reference-free criteria; sampling and budget controls are common
- **Regression gates in CI/CD** — evaluation runs triggered per change, with the new version required to hold or beat a baseline before shipping
- **Playgrounds** — a mutable workspace for fast iteration (reruns overwrite results) before promoting a configuration into the durable record
- **Side-by-side comparison** — experiment tables and matrix views that align outputs across prompt variants, model configurations, and dataset cases
- **Dataset growth from production** — user feedback, error patterns, and automated flags turn interesting live traces into new test cases
- **Score analytics** — trends over time per metric, with drill-down to the contributing cases
- **Model and provider catalogs** — running the same dataset across multiple model configurations to support selection decisions
- **Cost and latency as evaluation dimensions** — tracked alongside quality scores

### One structure, many implementations

The Core Model is written in conceptual terms. Products realize each concept differently:

```text
Concept:    Reaching the system under test
Forms:      platform-executed prompts against model providers, SDK/library
            invocation of application code, remote execution on the team's
            own infrastructure, trace ingestion from instrumented apps

Concept:    Grading criteria
Forms:      reference outputs, rubric prompts, acceptance criteria,
            assertions in declarative config, built-in metric catalogs

Concept:    The comparable record
Forms:      experiment, evaluation run, stored scored results
```

A reader who has only seen one implementation (for example, a browser playground) should still recognize a config-file-driven CLI evaluator as the same Type from the Core Model.

## How It Works

Two coupled loops drive the platform.

### The offline loop (pre-deployment)

```text
Build or extend a test-case dataset
→ connect the application (or point the platform at the prompt/model config)
→ run an evaluation: the system executes each case
→ scorers produce feedback per case
→ inspect results: drill into failed cases with their outputs
→ compare against previous versions on the same dataset
→ wire the same evaluation into CI so future changes are gated automatically
```

The evaluation run is the unit of work here. Each run captures a specific configuration — prompt, model, workflow — evaluated against a specific dataset state. Reference-based checks (correctness against expected answers) only work in this loop, because they require ground truth.

### The online loop (production)

```text
application serves live traffic → outputs/streams reach the platform
→ automated scorers grade sampled live traffic (no reference outputs:
   criteria are reference-free — safety, format, quality heuristics,
   judge models)
→ scores trend over time; regressions and anomalies surface
→ interesting cases (bad user feedback, errors, judge flags)
  are promoted into new dataset cases
```

### The feedback cycle

The two loops connect: production finds what matters → becomes offline test cases → fixes are validated offline → deployed → production confirms improvement. Evaluation spans the whole lifecycle rather than ending at deployment.

### Choosing what to compare

The comparison is only meaningful when the dataset is held fixed while the configuration varies. Teams typically compare prompt versions first (cheapest change), then model configurations (selection decisions), then application code changes (workflow edits). Because outputs are non-deterministic, conclusions rest on aggregate scores across the dataset rather than single outcomes.

## Interfaces

The following surfaces recur across the researched products. Names and layouts vary.

### Experiments / runs list and comparison

The home view for results. Lists evaluation runs for a project with aggregate scores and metadata; supports selecting multiple runs over the same dataset and comparing them case-by-case. Primary actions: open a run, compare runs, promote or discard a configuration.

### Run / case detail

One run, one case at a time. Shows the case input, the application's output, each scorer's result, and — for judge or human scores — the reasoning behind the score. Primary actions: inspect output, read scorer explanation, flag or annotate the case.

### Datasets

Management surface for test cases. Typical information: case inputs, reference outputs, metadata, source (manual, production trace, user feedback), version. Primary actions: add or edit cases, create a dataset from selected traces or feedback, manage versions.

### Scorers / evaluators

Configuration surface for grading criteria. Typical information: scorer type (code, judge prompt, human rubric), what it receives (output, reference, context), where it applies (datasets, live projects). Primary actions: create a scorer, attach it, set sampling, tune judge prompts.

### Annotation queues (human review)

Work queues for human scoring. Show items to review with the prescribed rubric, support multiple reviewers, and feed completed reviews back as scores — often with a one-step export of reviewed items into a dataset. Pairwise variants show two outputs side-by-side for a "which is better" judgment.

### Playground

A mutable iteration workspace: pick data, edit the prompt or select the model, attach scorers, run, and compare configurations live. Results here are disposable; the durable record is the evaluation run.

### Matrix / comparison views

Grid surfaces that align outputs across many prompt variants and inputs at once — the fastest way to see how a wording change or model swap shifts behavior across the whole case set. Primary actions: scan, filter by score, mark winners.

### Dashboards

Trend views over online evaluation: score distributions and time series per metric, cost and latency alongside quality. Primary actions: filter, alert, drill into contributing traces.

### SDK / CLI / CI surface

Evaluation is frequently defined in code or declarative configuration (a dataset, a task, a list of scorers), so the SDK, CLI commands, and CI pipeline integration are first-class interfaces alongside the web console.

## Important Rules / Behaviors

### Evaluation measures; it does not assert

The platform's scores are graded and comparative — "better than the baseline", "score dropped on this metric" — not binary pass/fail verdicts on deterministic behavior. Teams often convert evaluation metrics into regression assertions (the new version must not underperform the baseline), which is the bridge toward classical testing, but the underlying records remain graded feedback.

### Reference availability determines what can be checked

Any check that needs an expected answer (correctness, factual accuracy, exact match) requires a dataset with reference outputs and therefore only works offline. Live-traffic scoring has no ground truth, so it is restricted to reference-free criteria. Products in the sample are explicit and consistent about this split.

### Runs are durable; playgrounds are not

Once an evaluation run is recorded it does not change — later comparisons depend on that. Iteration happens in mutable surfaces where reruns overwrite results. This separation keeps fast iteration from corrupting the historical record.

### Results are attributed to versions

Every run is bound to a specific configuration of the application (prompt, model, workflow) and often to a dataset version. Without this attribution comparison would be meaningless; dataset changes are therefore tracked so CI runs can target a known dataset state.

### Human judgment flows back into data

Reviewer judgments are stored as scores and commonly promoted into datasets, making human evaluation both a measurement mechanism and a dataset-building mechanism.

### Non-determinism shapes interpretation

Because identical inputs can produce different outputs, single-case results are weak evidence; platform behavior (aggregate scores, side-by-side comparison, baselines) is built around comparing distributions of behavior rather than individual outcomes.

## Variants

- **Evaluation-first standalone platforms** — evaluation is the product's center of gravity; everything else serves the eval loop
- **Framework-attached companion platforms** — evaluation shipped as the companion product of a development framework; strongest when the application is built with the same vendor's tooling
- **Open-source and self-hosted platforms** — the evaluation machinery as installable software with an optional managed cloud tier
- **Local CLI / library tools** — declarative, config-file-driven evaluation that runs entirely on the developer's machine and in CI
- **ML-platform and cloud-suite modules** — evaluation as a module inside a broader ML experimentation or AI cloud platform
- **Scope emphasis** — prompt-and-completion-centric evaluation vs full application workflows; agent workloads (multi-step, tool-using systems with trajectory scoring) are served by the same products and treated in depth by the sibling Agent Evaluation Platform Type
- **Adjacent product surfaces** — red-teaming/security testing, guardrails, prompt management, and tracing ship inside some products as bundled or neighboring offerings

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Agent Evaluation Platform | sibling, gradient | same evaluation loop; the sibling centers multi-step tool-using agents with execution/trajectory scoring, this Type centers LLM application behavior at the output/response level. Market products serve both workloads in one platform |
| AI Model Evaluation Platform | adjacent, distinct subject | benchmarks the market's models against standardized public instruments to inform selection; here the subject is one's own application against one's own test cases to make a ship decision |
| LLM Observability Platform | adjacent, substrate | the observability record is the execution trace ("what happened"); the evaluation record is the scored run ("how good"). Evaluation consumes traces; sampled products commonly bundle tracing |
| LLM Application Development Platform | lifecycle neighbor | the build layer over foundation models; evaluation appears inside it as a bundled capability or a companion product, but the scored run is not the build layer's central object |
| Prompt Management Platform | adjacent | versioned prompt storage and deployment is a capability often bundled here; prompt management does not score behavior against criteria |
| AI Safety / Guardrail Platform | adjacent | guardrails intervene at runtime (block/alter/flag/allow on the live path); evaluation measures at rest (offline runs, asynchronous production scoring); some vendors bundle both |
| Test Automation Platform | adjacent, different assertion model | software tests assert deterministic pass/fail; LLM evaluation produces graded, comparative, non-deterministic quality measurements. The two meet at CI regression gates |
| Data Labeling Platform | adjacent, overlap on review surfaces | annotation queues overlap, but the managed object differs: annotation production vs quality measurement of one's own application |

The most consequential boundaries are the two gradients: with Agent Evaluation Platform (same loop, different center of gravity) and with LLM Observability Platform (shared machinery, different central record). Real products ship build, trace, and evaluate under one ecosystem, so the Types are best told apart by their central records — the scored evaluation run here — rather than by feature lists.

## Representative Products

- LangSmith (LangChain)
- Braintrust
- Langfuse
- W&B Weave
- promptfoo

These were the researched sample: a framework-attached companion platform, an evaluation-first standalone platform, an open-source/cloud platform, an ML-platform evaluation module, and a local open-source CLI/library.

## Sources

Research date: **2026-09-08**

- Braintrust — Evaluate systematically: https://www.braintrust.dev/docs/guides/evals
- Langfuse — Evaluation overview: https://langfuse.com/docs/evaluation/overview
- W&B Weave — Scoring overview: https://weave-docs.wandb.ai/guides/evaluation/
- promptfoo — Intro: https://www.promptfoo.dev/docs/intro/
- LangSmith — Evaluation concepts: https://docs.smith.langchain.com/evaluation (fetched 2026-09-06 and recorded in the paired Research Notes via the sibling research pass)

> Sourcing limitation: a provider-native pole (a leading model vendor's own evaluation tooling) could not be verified — its documentation host rejected fetches — so no provider-specific claims appear in this document. Only documentation-index and guide-root pages were reachable for some sampled products, so their claims are stated at reachable-page granularity. Precise operational details (numeric limits, sampling defaults, judge-model configurations, plan-gated capabilities) were not researched and are intentionally not stated; product-by-product observations and the cross-product comparison matrix are recorded in the paired Research Notes.
