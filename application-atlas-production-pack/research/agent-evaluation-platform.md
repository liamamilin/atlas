# Research Notes — Agent Evaluation Platform

## Research Goal

Understand what an Agent Evaluation Platform actually is by studying real products: what its core objects are (datasets, test cases, scorers, evaluation runs), how agents get evaluated (invocation, replay, trace capture), what gets scored (final outputs vs execution trajectories), how offline (pre-deployment) and online (production) evaluation relate, and where the boundary lies against Agent Development Platform, Agent/LLM Observability Platform, LLM Evaluation Platform, AI Model Evaluation Platform, and classical Test Automation.

## Initial Boundary

Hypothesis before research: an Agent Evaluation Platform systematically measures the behavior quality of AI agents against test cases with defined scoring criteria, producing persisted, comparable evaluation results. Nearest confusables:

- Agent Development Platform — builds/hosts the agent; may bundle evaluation as a module
- Agent Observability Platform — traces production executions; answers "what happened", not "how good"
- LLM Evaluation Platform — same evaluation loop, but system-under-test is a single model completion rather than a multi-step agent
- AI Model Evaluation Platform — benchmarks foundation models on public benchmarks
- Test Automation Platform — deterministic pass/fail testing of deterministic software

Prior note from the agent-development-platform research pass (recorded in STATUS.md Boundary Issues): in agent development products, evaluation appears as a bundled standard capability; standalone evaluation platforms exist. This pass researches the standalone Type.

## Research Questions

1. What is the central persistent object — the evaluation run / experiment?
2. What is a test case for an agent? What is a dataset?
3. How does the platform execute or observe the agent under test (SDK call, remote server, sandbox, trace ingestion)?
4. What scorer types exist (code, LLM-as-judge, human, pairwise)? What does feedback look like?
5. Is agent execution (tool calls, intermediate steps, trajectory) a scoring surface?
6. How does online/production evaluation work without reference outputs?
7. How do CI/CD regression gates work?
8. How do human review workflows (annotation queues) feed back into datasets?
9. What delivery postures exist (SaaS, OSS self-host, managed enterprise)?
10. Where is the line vs observability, vs LLM evaluation, vs model benchmarking, vs software testing?

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| LangSmith (LangChain) | evaluation as a module of a framework-attached platform; richest evaluation-concepts docs | framework ecosystem, developer-first |
| Braintrust | evaluation-first standalone platform; strong agent-under-test mechanics (remote evals, sandboxes) | evaluation-first startup, developer-first |
| Langfuse | open-source + cloud delivery posture; scores as central objects | OSS / self-host tier |
| Arize Phoenix | observability-first platform adding evaluation; OTel/OpenInference substrate; OSS + managed enterprise (Arize AX) | observability-first, OSS + enterprise |
| Galileo | observability + evaluation + guardrails positioning; metric-driven evaluation | SaaS, quality-metric-driven |

Selection covers: framework-attached vs standalone vs observability-first vs metric-first philosophies; SaaS vs OSS; startup vs enterprise.

## Sources

- LangSmith — Evaluation concepts: https://docs.smith.langchain.com/evaluation (fetched 2026-09-06)
- Braintrust — Evaluate systematically: https://www.braintrust.dev/docs/guides/evals (fetched 2026-09-06)
- Braintrust — Remote evals and sandboxes: https://www.braintrust.dev/docs/evaluate/remote-evals (fetched 2026-09-06)
- Langfuse — Evaluation overview: https://langfuse.com/docs/evaluation/overview (fetched 2026-09-06)
- Arize Phoenix — What is Phoenix: https://docs.arize.com/phoenix (fetched 2026-09-06)
- Galileo — What is Galileo: https://docs.galileo.ai/ (fetched 2026-09-06)
- Galileo — Run an experiment: https://docs.galileo.ai/getting-started/experiments (fetched 2026-09-06)

Source-access limitations: Galileo was only reached at its docs root and experiments quickstart pages (deeper evaluation-pages URLs 404'd); Galileo claims are kept coarse. LangSmith's self-hosting posture was not verified in fetched pages and is not asserted. Arize's dedicated "online evaluation" page URL failed; Phoenix observations come from the product overview page. No precise numeric limits (dataset sizes, sampling rates, judge defaults) were researched; none are asserted.

## Product Observations

### LangSmith

(Evidence layer A unless noted.)

- Offline vs online evaluation split is a first-class concept: offline targets datasets/examples pre-deployment (benchmarking, regression testing, unit testing, backtesting); online targets runs/threads from tracing on live traffic (monitoring, anomaly detection, production feedback).
- **Dataset** = collection of examples; **example** = input (variables) + optional reference outputs + optional metadata. Reference outputs are used only by evaluators.
- **Experiment** = "the results of evaluating a specific application version on a dataset" — captures outputs, evaluator scores, and execution traces for every example. Multiple experiments per dataset are compared side-by-side.
- Online evaluation runs on **runs** (single execution traces: inputs, outputs, intermediate steps, metadata) and **threads** (multi-turn conversations); no reference outputs, so evaluators are reference-free (safety checks, quality heuristics).
- **Evaluators** are workspace-level resources attachable to multiple tracing projects/datasets; per-attachment configuration includes sampling rate and spend limits. Runs via Evaluators page, Playground, SDK, or Rules (automation).
- Evaluator output = **feedback**: metric key + numeric score or categorical value + optional comment.
- Evaluation techniques: **Human** (review outputs/traces; annotation queues with single-run and pairwise queue types, rubrics, multiple reviewers, reservations, progress tracking; assertions = free-form acceptance criteria gradable by offline evaluators; annotated runs export to datasets), **Code** (deterministic rule functions: non-empty output, generated code compiles, exact classification match), **LLM-as-judge** (criteria encoded in prompt; reference-based or reference-free; few-shot graders), **Pairwise** (compare two versions; heuristic, LLM, or human; used when absolute scoring is hard but comparison is easy).
- Reference-based evaluators (correctness, factual accuracy, exact match) require datasets → offline only; reference-free (safety, format validation, quality heuristics, reference-free LLM-judge) work offline and online.
- Dataset organization: **splits** (named subsets: train/val/test, category-based, staged rollout), **versions** (auto-created on example change; taggable; CI pipelines can target versions).
- CI/testing integration: evaluations can be written with pytest / Vitest-Jest; regression tests can assert new versions outperform baselines.
- Explicit conceptual distinction: "Evaluation measures performance according to metrics... fuzzy or subjective... compare systems against each other. Testing asserts correctness... system can only be deployed if it passes."
- Agent-relevant: examples of what to evaluate for an **agent**: "correct tool selection and proper argument formatting or trajectory that the agent took."

### Braintrust

(Evidence layer A.)

- Full evaluation cycle: iterate in playgrounds (mutable, real-time, side-by-side comparison) → promote to experiments (immutable snapshot) → automate in CI/CD (evals on every pull request) → score in production (online scoring rules on live traces) → feed back (production traces into datasets).
- Anatomy of an evaluation: **Data** (dataset of test cases: inputs, optional expected outputs, metadata), **Task** ("the function being evaluated. Typically an LLM call, but can be any logic: a multi-step agent, a retrieval pipeline, or a custom workflow"), **Scorers and classifiers** (numeric scores / categorical labels; built-in autoevals, LLM-as-judge, custom code).
- **Experiments** are "the immutable, comparable record of your eval runs."
- **Online scoring** evaluates production traces automatically as they are logged, asynchronously; no ground truth for live requests → relies on LLM-as-a-judge scorers.
- **Remote evals**: agent/task code runs on your own infrastructure (machine or server); Braintrust triggers execution, sends parameters, displays results. Motivations: internal APIs/VPN access, platform-locked tooling (e.g., Windows-only simulation, game engines), heavy dev setups, data security (only results sent to Braintrust).
- **Sandboxes**: push an execution artifact (code bundle or container snapshot); Braintrust invokes on demand; reproducible isolated runs; per-invocation timeouts (15 min Lambda invocation cap, 60 min Modal sandbox default — product-specific L3 detail).
- Parameters (model selectors, prompt editors, scalar params) surface as UI controls in playgrounds.

### Langfuse

(Evidence layer A for the overview page; the page itself indexes method sub-pages not all fetched.)

- "Evals give you a repeatable check of your LLM application's behavior... catch regressions before you ship."
- Evaluation spans the "AI engineering loop": trace → monitor → build datasets → experiment → evaluate. Happens **online** (live production traces) and **offline** (pre-defined dataset tests).
- Central object is the **score**; multiple metrics combined: model-based evaluations (LLM-as-a-Judge), human annotations, custom workflows via API/SDKs.
- Method menu (from feature table): annotation queues + scores via UI (manual review), user feedback collection, text scores, **datasets** (reusable test-case sets), **experiments** (via UI, SDK, or OpenTelemetry) comparing prompt/model/code changes side by side, **CI/CD experiments** ("block deploys on regressions"), code evaluators (deterministic checks), LLM-as-a-judge on live traces, score analytics + custom dashboards (trends over time).

### Arize Phoenix

(Evidence layer A for product overview page; deeper pages not fetched.)

- Positioning: "AI Observability and Evaluation"; built on OpenTelemetry + OpenInference instrumentation; OSS (self-host: Docker/Kubernetes) + managed enterprise platform (Arize AX) on the same open standards.
- **Tracing**: traces capture model calls, retrieval, tool use, custom logic; auto-instrumentation for frameworks (LlamaIndex, LangChain, DSPy, Mastra, Vercel AI SDK) and providers.
- **Evaluation**: "score traces & spans with LLM-based evaluators, code-based checks, or human labels"; LLM-based evaluations (pre-built or custom evaluators); **dataset evaluators** (attach evaluators to datasets so they run automatically during experiments); bring-your-own evaluators (Ragas, DeepEval, Cleanlab); human annotations attach ground-truth labels in the UI.
- **Datasets & Experiments**: group traces into datasets, rerun through different versions of the application, compare evaluation results to confirm whether a change improved performance; datasets created from traces or uploaded from code/CSV.
- Prompt engineering side: prompt versioning, playground, span replay (replay LLM calls with different inputs).
- Span-level scoring (evals attach to individual spans) is direct evidence that intermediate-step scoring is a supported surface, not only final-output scoring.

### Galileo

(Evidence layer A for root + experiments pages; depth limited by URL failures.)

- Positioning: "observability, evaluation, and guardrail platform for GenAI and agentic applications"; for engineers, PMs, and SMEs; works via agentic-framework integrations, Python/TypeScript SDKs, or API.
- Learning path: log your first trace → evaluate traces (metrics) → **run an experiment** ("use Experiments to move from spot testing to systematic evaluation").
- Experiments = evaluate "prompts, models, and your application code, using well-defined inputs, against metrics of your choice" — created via UI or code (`run_experiment` with prompt template + dataset + metrics).
- Named quality metrics exist (e.g., "context adherence") with per-trace score + explanation in the UI; LLM provider integrations configured in console.
- Experiment comparison is a first-class console concept.

## Cross-product Comparison

| Aspect | LangSmith | Braintrust | Langfuse | Arize Phoenix | Galileo |
|---|---|---|---|---|---|
| Central result record | Experiment (per app version × dataset) | Experiment (immutable, comparable) | Experiment | Experiment | Experiment |
| Test cases | Dataset → examples (inputs + optional reference outputs + metadata) | Dataset of test cases (inputs, optional expected, metadata) | Dataset | Dataset (from traces or uploads) | Dataset |
| Agent under test mechanics | SDK evaluation; app on dataset; agent tool-selection/trajectory called out as eval target | Task function (LLM call → multi-step agent); remote evals (own infra) + cloud sandboxes | App runs against dataset (SDK/UI/OTel) | App versions rerun on datasets; trace/span ingestion | Prompt + dataset or application code; agentic framework integrations |
| Scoring methods | Human (annotation queues, single-run + pairwise), code, LLM-as-judge, pairwise | Code, LLM-as-judge, autoevals, classifiers | LLM-as-judge, code evaluators, human annotation, scores via API/SDK/UI | LLM-based, code-based, human labels, BYO evaluators (Ragas/DeepEval/Cleanlab) | Pre-built named metrics (LLM-based) |
| Execution-level scoring surface | trajectory / tool selection named as eval target | task = multi-step agent (whole execution is the task) | session/thread-level evaluation available | traces & **spans** scoreable (step-level) | trace-level metrics; agentic positioning |
| Reference-based vs reference-free distinction | explicit and central | explicit (offline vs online ground truth) | present (offline datasets vs live traces) | present (datasets vs traces) | metric-centric, less explicit on fetched pages |
| Online/production evaluation | rules on runs/threads; sampling per attachment | online scoring rules, async on logged traces | online evaluators on live traces | evals on traces/spans + human annotation | monitoring part of positioning (guardrails) |
| CI/CD gates | dataset versions targeted in CI; pytest/Vitest | evals on every pull request | CI/CD experiments "block deploys on regressions" | not emphasized on fetched page | experiment comparison (CI depth unverified) |
| Trace substrate | runs/threads from tracing | logs → datasets | traces/sessions core | OTel/OpenInference traces/spans core | traces via SDK/integrations |
| Human review | annotation queues with rubrics, reviewers, reservations, export-to-dataset | playground sharing; human review present | annotation queues; scores via UI | human annotations attach labels in UI | SME/PM audience claimed (depth unverified) |
| Delivery posture | SaaS platform (self-host posture not verified in fetched pages) | SaaS; self-hosted deployments referenced | OSS self-host + cloud | OSS self-host (Docker/K8s) + managed Arize AX | SaaS console |
| Feedback loop (production → dataset) | explicit (convert traces to examples; user feedback, heuristics, LLM feedback) | explicit ("feed back" step of the cycle) | explicit (datasets from traces; block deploys) | explicit (group traces into datasets) | implied (trace-based) |

**Cross-product commonalities (layer B):** every product has (1) datasets of test cases with optional expected outputs; (2) an experiment/evaluation-run record as the durable, comparable result; (3) three scorer families — code, LLM-as-judge, human; (4) the offline (pre-deploy, reference-based) vs online (production, reference-free) split; (5) comparison of runs across agent/prompt/model versions; (6) production traces as a dataset source; (7) CI/CD as an automation target (4 of 5 explicitly evidenced on fetched pages; Phoenix CI depth not verified — treat CI as common, not universal).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product is no longer an agent evaluation platform:

```text
Agent under test with an evaluation hook
  (the platform can invoke the agent, or ingest its execution, so behavior is measurable)
└── Test-case dataset
    (curated inputs + expected outcomes / grading criteria, reusable across runs)
    └── Scoring mechanism
        (defined scorers — automated or human — applied per case, producing feedback)
        └── Persisted, comparable evaluation runs
            (results recorded as first-class objects, attributed to a version/
             configuration of the agent, comparable over time)
```

Four invariants. Remove any one and the Type collapses:

- no agent hook → a static checklist/spreadsheet, not a platform
- no test-case datasets → ad-hoc tracing/observability or a one-off script
- no scoring criteria → test execution without evaluation
- no persisted comparable runs → a script, not a managed platform; no regression detection possible

Historical/market-sample check (per §24 reasoning): pre-agent-era analogues satisfy the skeleton — classical ML evaluation (held-out test set + metric computation + stored results across model versions) fits invariants 2–4; the agent-specific addition is the system-under-test being a multi-step tool-using application and the scoring surface covering execution behavior, not only final text. Older teams also ran evaluation as ad-hoc notebooks/scripts; the platform packaging (managed datasets, scorers, run records, UI, automation) is exactly what distinguishes the Type from "a script". Therefore L0 must not include LLM-as-judge (a modern implementation), trace standards (OTel), or CI/CD (automation posture).

### L1 — Common Mature Structure

Present in most mature products (layer B), expected by the market, but not definitional:

- LLM-as-judge scorers (reference-based and reference-free), few-shot graders
- code/deterministic scorers (exact match, format validation, compilability checks)
- human review workflows: annotation queues with rubrics, multiple reviewers, progress tracking
- pairwise comparison of two versions when absolute scoring is hard
- online/production evaluation: automated scoring of live traces, sampling, no ground truth
- CI/CD integration: run evals per PR / block deploys on regression vs baseline
- experiment comparison UI (side-by-side, per-case drill-down with execution traces)
- playgrounds for mutable iteration before committing to immutable experiments
- dataset construction from production traces (user feedback, heuristics, LLM-flagged)
- evaluation of intermediate execution: tool calls, steps, spans, trajectories, threads
- cost/latency metrics alongside quality scores
- dataset versions/splits; baseline/regression assertions

### L2 — Variant / Optional Structure

Depends on segment, delivery, ecosystem, or workflow:

- delivery posture: SaaS-only vs open-source self-host + managed cloud vs managed enterprise
- invocation mechanics: in-process SDK, remote eval server on customer infra, pushed sandbox artifact, OTel trace ingestion only, prompt-only (no custom code)
- scope emphasis: agent-trajectory-centric vs broader LLM-app-centric
- guardrail bundling (runtime enforcement vs at-rest evaluation)
- simulation environments for agents (not verified in this sample — unverified, do not assert)
- judge-model strategy (which model judges, spend limits, managed judge models)
- framework-specific instrumentation integrations
- enterprise governance (RBAC, data planes, self-hosted data residency)

### L3 — Vendor-specific Structure (Research Notes only)

- LangSmith: evaluator spend limits per attachment; single-run vs pairwise annotation queue types; dataset splits allowing multi-split membership; pytest/Vitest runners; "Rules" automation
- Braintrust: autoevals library; remote evals (devserver, `bt eval --dev`); Lambda/Modal sandboxes with specific timeouts; saved parameters as UI controls
- Langfuse: score types (numeric/categorical/text); Score Analytics dashboards; OTel-based experiments; "AI engineering loop" framing
- Phoenix: OpenInference; span replay; PXI built-in agent; BYO evaluators (Ragas/DeepEval/Cleanlab); self-host via `uvx arize-phoenix serve`
- Galileo: named metric catalog (context adherence); prompt+dataset experiments via console; integration setup flow

## Vendor-specific / Rejected Findings

- "Evaluation requires a built-in metric catalog" — rejected as definitional; Galileo leads with named metrics, but LangSmith/Braintrust treat metrics as user-defined scorers. Metric catalogs are L2/L3.
- "Evaluation requires trace-visualization" — rejected; traces are the common substrate but the defining act is scoring against criteria, not visualization.
- "Agent simulation is the core" — rejected for this Type; none of the sampled products defines itself primarily as simulation; simulation environments (where they exist) are a mechanism for generating executions to score.
- "Evaluation = software testing" — rejected; LangSmith explicitly separates the two (metrics are fuzzy/relative vs tests assert pass/fail). Retained as a *boundary* insight, with the note that evaluation metrics can be converted into regression tests (threshold assertions).
- Precise numbers (Lambda 15-min invocation cap, Modal 60-min sandbox) — L3, product-specific, kept out of the final document.

## Boundary Findings

1. **vs Agent Development Platform** (sibling, §13): every sampled evaluation platform treats the agent as an *external* system under test (SDK hook, remote server, trace feed); it does not define, host, or orchestrate the agent. Conversely, the earlier agent-development-platform pass found evaluation bundled as a standard capability inside development platforms. Capability/overlap relationship; the two leaves likely need a shared framing — flagged for joint review.
2. **vs Agent Observability Platform / LLM Observability Platform** (siblings, §13): observability's central record is the execution trace ("what happened"); evaluation's central record is the scored run against criteria ("how good"). Evaluation *consumes* traces (online scoring, span-level evals, datasets built from traces), and all sampled products bundle tracing. Boundary test: remove scoring-against-criteria → remains observability; remove persistent trace inspection → remains an eval runner. A gradient, not a wall — flagged for joint review.
3. **vs LLM Evaluation Platform** (sibling, §13): same evaluation loop; differentiator is the system under test (multi-step, tool-calling agent producing trajectories vs single model completion) and the scoring surface (execution behavior / spans / trajectories vs single output). In market practice these are one product family with two workloads — probable gradient or alias; flagged for joint review when LLM Evaluation Platform is processed.
4. **vs AI Model Evaluation Platform** (sibling, §13): model evaluation benchmarks foundation models against (often public, fixed) benchmark datasets to select a model; agent evaluation measures *your own agent* against *your own test cases* across *your own versions* to ship changes. Different subject, dataset provenance, and decision. Clean distinction.
5. **vs Test Automation Platform / Software Test Management** (§12): software tests assert deterministic pass/fail on deterministic systems; agent evaluation produces graded, fuzzy, non-deterministic quality scores used comparatively. LangSmith's own docs articulate the distinction while also converting evals into regression assertions — adjacent Types sharing the CI-gate surface.
6. **vs AI Safety / Guardrail Platform** (sibling, §13): guardrails act at runtime (block/rewrite); evaluation measures at rest (offline runs, async online scoring). Galileo explicitly bundles observability + evaluation + guardrails — bundling, not identity.
7. **Taxonomy observation**: the leaf name says "Agent", but all sampled products serve both single-turn LLM apps and agents. The agent-specific part of the definition is the agentic system under test + execution-level scoring surface; the rest of the machinery is shared with LLM evaluation. Recorded in case a future joint review merges/reframes the sibling leaves.

## Uncertainties

- Galileo's online-evaluation and human-review depth unverified (URL failures); kept coarse.
- Phoenix CI/CD depth not verified on fetched pages; CI claimed as common on 4-of-5 evidence.
- LangSmith self-hosting posture not verified in fetched pages; omitted.
- Agent simulation environments exist in the broader market but were not directly researched in this sample; listed as unverified L2.
- Market share / adoption rankings not researched; product selection reflects documentation accessibility and philosophical diversity, not market size.

## Final Synthesis

An Agent Evaluation Platform is a managed, persistent platform for measuring the behavior of an AI agent against defined quality criteria. Its world contains four defining structures: (1) an agent under test reachable through an evaluation hook (SDK invocation, remote execution, or trace ingestion); (2) test-case datasets — curated inputs with expected outcomes or grading criteria, reusable and versionable; (3) scoring mechanisms — code, LLM-as-judge, human review, pairwise — that produce per-case feedback; (4) evaluation runs (experiments) persisted as immutable, comparable records attributed to a version of the agent, enabling regression detection and release decisions.

Work flows in two coupled loops: an **offline loop** (build dataset → connect agent → run experiment → score → compare versions → gate in CI/CD) and an **online loop** (score live production traces without ground truth → surface problems → convert interesting traces into new test cases). Agent-specific evaluation extends scoring from final outputs to the execution itself — tool selection, argument formatting, intermediate steps, trajectories, multi-turn threads.

The Type is defined by the evaluation loop, not by the agent runtime (that is the development platform), not by trace storage (that is observability), not by public benchmarks (that is model evaluation), and not by deterministic pass/fail assertion (that is software testing) — though real products bundle across these lines, which is the main joint-review risk for the sibling leaves.
