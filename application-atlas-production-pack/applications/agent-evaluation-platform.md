# Agent Evaluation Platform

## Overview

An **Agent Evaluation Platform** is a managed system for measuring how well an AI agent behaves: it runs or observes the agent against curated test cases, scores the results against defined quality criteria, and stores the outcomes as comparable records attributed to a specific version of the agent.

Its purpose is to replace subjective spot-checking of non-deterministic software with repeatable measurement. The same input can produce different outputs, there is rarely a single correct answer, and a change that improves one quality dimension can silently degrade another. An evaluation platform makes "is this version actually better?" answerable with data, both before a change ships and after.

The defining core is small:

```text
Agent under test (reached through an evaluation hook)
└── Test-case dataset (inputs + expected outcomes or grading criteria)
    └── Scoring (automated or human, applied per case)
        └── Persisted, comparable evaluation runs
            (attributed to a version/configuration of the agent)
```

Everything else commonly associated with these products — LLM-as-judge graders, production traffic scoring, CI/CD regression gates, playgrounds, annotation queues — is standard capability of mature products, not what makes the product an evaluation platform. Remove scoring against criteria and the product is observability; remove the agent hook and it is a checklist; remove persisted comparable runs and it is a script.

## Users & Context

Primary users are the people who build and iterate on agents:

- **AI / agent engineers** — connect the agent to the platform, define test cases and scorers, run experiments, wire evaluation into CI
- **Prompt engineers / app developers** — compare prompt, model, and workflow variants on the same dataset before promoting a change

Secondary users review quality without owning the code:

- **Product managers and subject-matter experts** — review agent outputs against rubrics, judge which of two responses is better, flag failures
- **Team leads / reviewers** — inspect experiment results, decide whether a version is safe to ship

The context is the agent development lifecycle: during development, evaluation validates changes against curated datasets; in production, evaluation scores live traffic to catch regressions and find new failure cases; the two feed each other continuously.

## Core Model

### The defining core

Four structures. Every mature product in the researched sample has all four, and each is load-bearing.

**1. Agent under test with an evaluation hook.** The platform does not build or host the agent — the agent is an external system the platform can *reach*. The hook takes one of several forms (an SDK call that invokes the agent's code, a remote execution server the platform triggers, a packaged artifact the platform invokes in a sandbox, or trace ingestion from an instrumented application). What matters is that the platform can produce or capture the agent's execution — including its intermediate steps and tool calls — so the behavior becomes measurable.

**2. Test-case dataset.** A curated, reusable collection of cases. Each case holds an input (what is fed to the agent) and, optionally, a reference output or grading criteria (what "good" looks like). Datasets are versioned and often split into named subsets (for example, by category or by deployment stage). Cases are commonly sourced three ways: hand-written examples defining expected behavior, real production traces converted into cases, and synthetic variations of existing cases.

**3. Scoring mechanism.** Defined scorers — automated or human — are applied to each case's result and produce feedback: a numeric score, a categorical label, or a free-text comment. Three scorer families recur across products:

- *code scorers* — deterministic checks (exact match, output is valid structure, generated code compiles)
- *LLM-as-judge scorers* — an LLM grades the output against criteria written into a grading prompt, either comparing to a reference answer or judging reference-free qualities such as helpfulness or safety
- *human scoring* — reviewers rate outputs and traces, usually organized in review queues with rubrics, and increasingly compare two versions side-by-side when judging "which is better" is easier than assigning an absolute score

**4. Persisted, comparable evaluation runs.** A run (commonly called an *experiment*) is the durable record of evaluating one version of the agent on one dataset: per-case inputs, the agent's outputs and execution traces, and every scorer's feedback. Runs are immutable and comparable — the platform's comparison surfaces line up multiple runs over the same dataset so quality differences between agent versions, prompts, or models are directly visible.

### Standard capabilities of mature products

These are widespread in the researched sample and expected by the market; they make evaluation practical but do not define the Type.

- **Execution-level scoring** — because an agent acts over multiple steps, scoring is not limited to the final answer: tool selection, argument formatting, intermediate steps, whole trajectories, and multi-turn conversations are all legitimate scoring surfaces
- **Online evaluation** — automated scoring of live production traffic as traces arrive, without ground truth; sampling and budget controls are common
- **Offline evaluation** — batch scoring of the dataset against a candidate version before deployment, where reference outputs enable correctness checks
- **Regression gates in CI/CD** — evaluation runs triggered per change, with assertions that a new version must beat a baseline before shipping
- **Playgrounds** — a mutable workspace for fast iteration (reruns overwrite results) before promoting a configuration into an immutable experiment
- **Dataset growth from production** — user feedback, heuristics, and automated flags turn interesting live traces into new test cases
- **Run comparison UI** — side-by-side views with per-case drill-down into execution traces and scorer explanations
- **Cost and latency as evaluation dimensions** — run cost and duration tracked alongside quality scores

### One structure, many implementations

```text
Concept:    Evaluation hook to the agent under test
Forms:      in-process SDK call, remote eval server on the team's own
            infrastructure, pushed sandbox artifact, trace ingestion
            from an instrumented application, prompt-only execution

Concept:    Grading criteria
Forms:      reference outputs, rubric prompts, free-form acceptance
            criteria, named quality metrics, pass/fail-style assertions

Concept:    The comparable record
Forms:      experiment, evaluation run, scored dataset snapshot
```

## How It Works

Two coupled loops drive the platform.

### The offline loop (pre-deployment)

```text
Build or extend a test-case dataset
→ connect the agent through the evaluation hook
→ run an experiment: the agent executes each case
→ scorers produce feedback per case
→ inspect results: drill into failed cases with their execution traces
→ compare the experiment against previous versions on the same dataset
→ wire the same evaluation into CI so future changes are gated automatically
```

The experiment is the unit of work here. Each run captures a specific configuration — prompts, model, workflow — evaluated on a specific dataset state. Reference-based checks (correctness against expected answers) only work in this loop, because they require ground truth.

### The online loop (production)

```text
agent serves live traffic → traces stream to the platform
→ automated scorers grade sampled live traces (no reference outputs:
   criteria are reference-free — safety, format, quality heuristics,
   judge models)
→ scores trend over time on dashboards; regressions and anomalies surface
→ interesting traces (bad user feedback, errors, judge flags)
  are promoted into new dataset cases
```

### The feedback cycle

The two loops connect: production finds what matters → becomes offline test cases → fixes are validated offline → deployed → production confirms improvement. Evaluation runs across the whole lifecycle rather than ending at deployment.

### Where agent-specific evaluation differs

Evaluating an agent, rather than a single model call, changes three things in practice:

- the *task* under evaluation can be an entire multi-step workflow, not one completion
- the execution itself — which tools were chosen, whether arguments were formatted correctly, what path the agent took — becomes gradeable, independent of whether the final answer looks right
- conversation-level properties (coherence across turns, whether the agent stayed on task) can be scored at the thread level rather than per message

## Interfaces

The following surfaces recur across the researched products. Names and layouts vary.

### Experiments / runs list and comparison

The platform's home view for results. Lists evaluation runs for a project with aggregate scores and metadata; supports selecting multiple runs over the same dataset and comparing them case-by-case. Primary actions: open a run, compare runs, promote or discard a configuration.

### Run detail / case drill-down

One run, one case at a time. Shows the case input, the agent's full output and execution trace (every step and tool call), each scorer's result, and — for judge or human scores — the reasoning behind the score. Primary actions: inspect trace, read scorer explanation, flag or annotate the case.

### Datasets

Management surface for test cases. Typical information: case inputs, reference outputs, metadata, source (manual, production trace, synthetic), version and split membership. Primary actions: add or edit cases, create a dataset from selected traces, upload cases, manage versions/splits.

### Scorers / evaluators

Configuration surface for grading criteria. Typical information: scorer type (code, judge prompt, human rubric), what it receives (outputs, reference, trace), where it applies (datasets, live projects). Primary actions: create a scorer, attach it to a dataset or project, set sampling, tune judge prompts.

### Annotation queues (human review)

Work queues for human scoring. Show items to review with the prescribed rubric, support multiple reviewers and claim/reservation, and feed completed reviews back as scores — often with a one-step export of reviewed items into a dataset. Pairwise variants show two outputs side-by-side for a "which is better" judgment.

### Playground

A mutable iteration workspace: pick data, pick or edit the task (prompt, model, or connected agent code), attach scorers, run, and compare configurations live. Results here are disposable; the durable record is the experiment.

### Dashboards

Trend views over online evaluation: score distributions and time series per metric, cost and latency alongside quality, regression alerts. Primary actions: filter, alert, drill into contributing traces.

### SDK / CLI / CI surface

Evaluation is usually defined in code (a dataset, a task, a list of scorers), so the SDK, CLI commands, and CI pipeline integration are first-class interfaces alongside the web console.

## Important Rules / Behaviors

### Evaluation measures; it does not assert

The platform's scores are graded and comparative — "better than the baseline", "score dropped 4 points" — not binary pass/fail assertions on deterministic behavior. Teams often convert evaluation metrics into regression assertions (new version must not underperform baseline), which is the bridge toward classical testing, but the underlying records remain graded feedback.

### Reference availability determines what can be checked

Any check that needs an expected answer (correctness, factual accuracy, exact match) requires a dataset with reference outputs and therefore only works offline. Live-traffic scoring has no ground truth, so it is restricted to reference-free criteria. Products in the sample are explicit and consistent about this split.

### Experiments are immutable; playgrounds are not

Once an evaluation run is recorded it does not change — later comparisons depend on that. Iteration happens in mutable playground surfaces where reruns overwrite results. This separation keeps fast iteration from corrupting the historical record.

### Results are attributed to versions

Every run is bound to a specific configuration of the agent (prompt, model, workflow) and often to a dataset version. Without this attribution, comparison would be meaningless; dataset changes are therefore tracked as versions so that CI runs can target a known dataset state.

### Human review flows back into data

Reviewer judgments are stored as scores and commonly promoted into datasets, making human evaluation both a measurement mechanism and a dataset-building mechanism.

### Non-determinism shapes interpretation

Because outputs vary between identical invocations, single-case results are weak evidence; platform behavior (aggregate scores, side-by-side comparison, baselines) is built around comparing distributions of behavior rather than individual outcomes.

## Variants

- **Evaluation-first standalone platforms** — evaluation is the product's center of gravity; everything else serves the eval loop
- **Observability suites with an evaluation module** — the platform's core is trace capture and inspection; evaluation is a scoring layer over traces (span-level evals, datasets built from logs)
- **Framework-attached evaluation services** — evaluation shipped as the companion platform of a development framework; strongest when the agent is built with the same vendor's tooling
- **Delivery posture variants** — SaaS-only vs open-source self-hosted with a managed cloud tier vs managed enterprise platform
- **Scope emphasis** — agent-trajectory-centric evaluation (multi-step, tool use, conversations) vs broader LLM-application evaluation (single completions, RAG answers); in current market practice these are workloads of the same products rather than different products

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Agent Development Platform | adjacent, heavy bundling | defines, hosts, and orchestrates the agent; evaluation is a bundled module. The evaluation platform's central record is the scored run, not the agent definition or runtime |
| Agent Observability Platform | adjacent, substrate | central record is the execution trace ("what happened"); evaluation's central record is the scored run ("how good"). Evaluation consumes traces; all sampled evaluation platforms bundle tracing |
| LLM Evaluation Platform | sibling, gradient | same evaluation loop over a different system under test — single model completions vs multi-step tool-using agents; market products serve both workloads in one platform |
| AI Model Evaluation Platform | adjacent, distinct subject | benchmarks foundation models against fixed public datasets to choose a model; agent evaluation measures one's own agent against one's own cases across one's own versions to ship changes |
| Test Automation Platform | adjacent, different assertion model | software tests assert deterministic pass/fail; agent evaluation produces graded, comparative, non-deterministic quality measurements. The two meet at CI regression gates |
| AI Safety / Guardrail Platform | adjacent | guardrails intervene at runtime (block/rewrite); evaluation measures at rest (offline runs, async production scoring); some vendors bundle both |
| Prompt Management Platform | adjacent | versioned prompt storage and deployment is a capability often bundled here, but prompt management does not score behavior against criteria |

The most consequential boundary is with Agent Development Platform and Agent Observability Platform: real products ship all three concerns under one roof (build the agent, trace it, evaluate it), so the Types are best understood by their central records — agent definition + runtime loop vs execution trace vs scored evaluation run — rather than by feature lists.

## Representative Products

- LangSmith (LangChain)
- Braintrust
- Langfuse
- Arize Phoenix
- Galileo

These were the researched sample: an evaluation module of a framework ecosystem, an evaluation-first standalone platform, an open-source/cloud platform, an observability-first platform with open-source and enterprise editions, and a metric-driven SaaS platform.

## Sources

Research date: **2026-09-06**

- LangSmith — Evaluation concepts: https://docs.smith.langchain.com/evaluation
- Braintrust — Evaluate systematically: https://www.braintrust.dev/docs/guides/evals
- Braintrust — Remote evals and sandboxes: https://www.braintrust.dev/docs/evaluate/remote-evals
- Langfuse — Evaluation overview: https://langfuse.com/docs/evaluation/overview
- Arize Phoenix — What is Phoenix: https://docs.arize.com/phoenix
- Galileo — What is Galileo: https://docs.galileo.ai/
- Galileo — Run an experiment: https://docs.galileo.ai/getting-started/experiments

> Sourcing limitation: for Galileo, only the documentation root and the experiments quickstart could be fetched (deeper evaluation pages were unreachable), so claims specific to that product are stated at reduced precision. Precise operational details (numeric limits, sampling defaults, judge-model configurations, pricing-tier capabilities) were not researched and are intentionally not stated in this document; product-by-product observations and the cross-product comparison matrix are recorded in the paired Research Notes.
