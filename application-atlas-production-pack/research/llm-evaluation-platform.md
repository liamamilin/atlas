# Research Notes — LLM Evaluation Platform

## Research Goal

Understand what an LLM Evaluation Platform actually is by studying real products: what its central objects are (test-case datasets, scorers, evaluation runs/experiments, scores), how the LLM application under test is reached (direct prompt execution, SDK/library invocation, trace ingestion), what gets scored (single completions, prompt variants, app responses, model configurations), how offline (pre-deployment) and online (production) evaluation relate, how comparison across prompt/model/application versions works, and where the boundary lies against Agent Evaluation Platform, AI Model Evaluation Platform, LLM Application Development Platform, LLM Observability Platform, Prompt Management Platform, AI Safety/Guardrail Platform, and classical Test Automation.

This pass also carries three pre-hung joint-review flags to discharge:

1. agent-evaluation-platform flagged `agent-eval vs llm-evaluation-platform` as "one product family with two workloads — probable gradient or alias".
2. ai-model-evaluation-platform flagged `ai-model-eval vs llm-evaluation-platform` as "naming confusion, not structural identity — flagged for joint review when LLM Evaluation Platform is processed".
3. llm-application-development-platform hung forward flags on `llm-evaluation-platform + llm-observability-platform` as "capability siblings; companion-product pattern = LangSmith-class".

## Initial Boundary

Hypothesis before research: an LLM Evaluation Platform systematically measures the quality of the user's own LLM application's behavior — prompts, model calls, and application workflows — against test cases with defined scoring criteria, producing persisted, comparable evaluation results attributed to versions, so teams can decide whether a change improved quality before shipping and after. Nearest confusables:

- Agent Evaluation Platform — same evaluation loop; sibling centered on multi-step tool-using agents and trajectory scoring
- AI Model Evaluation Platform — benchmarks the market's models on standardized instruments; here the subject is the user's own application
- LLM Application Development Platform — the build layer; evaluation appears inside it as a bundled capability or companion product
- LLM Observability Platform — execution traces ("what happened"); evaluation produces scored runs ("how good")
- Prompt Management Platform — prompt-asset lifecycle (versions, deployment); evaluation measures behavior
- AI Safety / Guardrail Platform — runtime content screening and enforcement; evaluation measures at rest
- Test Automation Platform — deterministic pass/fail assertions; evaluation produces graded, comparative quality scores

## Research Questions

1. What is the central persistent object — the experiment / evaluation run? What does it contain?
2. What is a test case? What is a dataset, and where do cases come from?
3. How does the platform reach the system under test (run the prompt itself, invoke a function, ingest traces)?
4. What scorer families exist (code/deterministic, LLM-as-judge, human)? What does a score look like?
5. What is compared, and on what basis (versions of prompts, models, application code against a fixed dataset)?
6. How does online/production evaluation work without reference outputs?
7. How do CI/CD regression gates work?
8. How do playgrounds and other iteration surfaces relate to the durable record?
9. What delivery postures exist (SaaS, OSS self-host, local CLI/library, cloud-suite module)?
10. Where is the line vs agent evaluation, model benchmarking, observability, prompt management, guardrails, and software testing?

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| LangSmith (LangChain) | the canonical companion evaluation platform of a development-framework ecosystem; richest evaluation-concepts documentation | framework-attached, developer-first, SaaS |
| Braintrust | evaluation-first standalone platform; explicit full-lifecycle documentation (playground → experiment → CI → online → feedback) | evaluation-first startup, SaaS |
| Langfuse | open-source + cloud delivery; scores/annotation as central objects | OSS / self-host tier |
| W&B Weave | evaluation as code inside an ML-experiment-tracking lineage; scorer/Evaluation programming model | ML-platform heritage, library-first, enterprise ML teams |
| promptfoo | open-source local CLI/library with declarative config; test-driven prompt development philosophy | local dev tool, individual-developer tier |

Selection covers: framework-attached vs eval-first vs OSS vs ML-platform-heritage vs local-CLI philosophies; SaaS vs OSS vs local delivery; startup vs enterprise vs individual tiers.

Note: a provider-native pole (OpenAI's platform evaluation features) was desired for the sample but platform.openai.com returned 403; per the network-abandonment rule the source was dropped and no provider-native claims are made. This mirrors the llm-application-development-platform pass, which recorded the same limitation.

## Sources

- Braintrust — Evaluate systematically: https://www.braintrust.dev/docs/guides/evals (fetched 2026-09-08)
- Langfuse — Evaluation overview: https://langfuse.com/docs/evaluation/overview (fetched 2026-09-08)
- W&B Weave — Scoring overview (Evaluation guide): https://weave-docs.wandb.ai/guides/evaluation/ (fetched 2026-09-08)
- promptfoo — Intro: https://www.promptfoo.dev/docs/intro/ (fetched 2026-09-08)
- LangSmith — Evaluation concepts: https://docs.smith.langchain.com/evaluation (fetched 2026-09-06, recorded with evidence-layer-A observations in research/agent-evaluation-platform.md; re-used as imported evidence in this pass)

Source-access limitations: OpenAI platform docs unreachable (403, 2026-09-08) — the provider-native posture is noted as a market shape but no product-specific claims are made. LangSmith evidence is imported from the sibling pass's recorded fetch rather than re-fetched; it is marked "imported" wherever used. Only documentation-index and guide-root pages were fetched for Weave and promptfoo; deeper feature pages were not fetched, so claims for those products are kept at the reachable-page granularity. No precise numeric limits (dataset sizes, sampling rates, judge defaults, pricing-tier capabilities) were researched; none are asserted.

## Product Observations

### LangSmith (imported evidence)

(Evidence layer A via the sibling pass's recorded fetch, 2026-09-06; see research/agent-evaluation-platform.md.)

- Offline vs online evaluation is a first-class split: offline targets datasets/examples pre-deployment; online targets runs/threads from tracing on live traffic with reference-free evaluators.
- **Dataset** = collection of examples; **example** = input + optional reference outputs + metadata. **Experiment** = "the results of evaluating a specific application version on a dataset", capturing outputs, evaluator scores, and execution traces per example; multiple experiments per dataset compared side-by-side.
- Evaluators attachable to datasets/tracing projects with per-attachment sampling; evaluator output = **feedback** (metric key + score or categorical value + optional comment).
- Evaluation techniques: Human (annotation queues, rubrics, pairwise queues), Code (deterministic checks), LLM-as-judge (reference-based and reference-free), Pairwise comparison.
- Reference-based evaluators require datasets (offline only); reference-free evaluators work offline and online.
- Dataset splits and versions; CI targeting of dataset versions; pytest/Vitest integration; explicit conceptual separation of evaluation (fuzzy, comparative metrics) from testing (pass/fail assertions).
- Agent-relevant examples name tool selection and trajectories as eval targets — the overlap surface with the agent-evaluation sibling.

### Braintrust

(Evidence layer A unless noted.)

- The full evaluation cycle is stated as five named stages: **Iterate in playgrounds** (prototype prompts, models, scorers, or custom agent code) → **Promote to an experiment** (immutable snapshot) → **Automate in CI/CD** (evals on every pull request) → **Score in production** (online scoring rules on live traffic) → **Feed back** (production traces into datasets to improve offline test coverage).
- Framing motivation (matches the Type's problem statement): "the same input can produce different outputs, there's rarely a single correct answer, and a change that improves one metric can silently degrade another."
- Anatomy of an evaluation — three parts: **Data** (dataset of test cases with inputs, optional expected outputs, metadata; built from production logs, user feedback, or manual curation), **Task** ("the function being evaluated. Typically an LLM call, but can be any logic: a multi-step agent, a retrieval pipeline, or a custom workflow"), **Scorers and classifiers** (numeric scores; categorical labels; built-in autoevals, LLM-as-a-judge, custom code).
- **Experiments** are "the immutable, comparable record of your eval runs"; run from code or UI; results reproducible and comparable over time.
- Online scoring evaluates production traces automatically as they are logged, asynchronously; no ground truth for live requests → relies on LLM-as-a-judge scorers.
- Playgrounds are mutable (re-running overwrites) vs experiments immutable — an explicit durability distinction.

### Langfuse

(Evidence layer A unless noted.)

- Self-description: "Evals give you a repeatable check of your LLM application's behavior. You replace guesswork with data, and catch regressions before you ship a change."
- Evaluation spans the "AI engineering loop": trace → monitor → build datasets → experiment → evaluate; happens both **online** (live production traces, quality trends over time) and **offline** (pre-defined dataset tests before shipping).
- Evaluation methods table (from the overview feature map): annotation queues and scores via UI (manual review), user feedback collection, text scores, **datasets** (reusable test-case sets), **experiments** via UI / SDK / OpenTelemetry comparing prompt, model, or code changes side by side, **CI/CD experiments** ("block deploys on regressions"), code evaluators (deterministic checks), LLM-as-a-judge on live production traces, score analytics and custom dashboards for trends.
- Multiple metric kinds combined in one place: model-based evaluations (LLM-as-a-Judge), human annotations, custom workflows via API/SDKs.

### W&B Weave

(Evidence layer A for the scoring/Evaluation guide page; deeper pages not fetched.)

- Central vocabulary: **Scorers** evaluate AI outputs and return evaluation metrics — they take the AI's output, analyze it, and return a dictionary of results; they can use input data as reference and can return explanations/reasoning.
- **Evaluation** as a programming object: `weave.Evaluation(dataset=[...], scorers=[...])` — a dataset of rows plus scorers applied per row; per-row scores are aggregated into a final result (auto-summarize with overridable summarization logic).
- Scorer authoring: function-based scorers (deterministic checks, e.g. text-is-uppercase) and class-based scorers; LLM-as-judge realized as a scorer that calls an LLM with a scoring prompt interpolating dataset/op variables; column mapping between scorer arguments and dataset columns.
- Built-in scorer catalog exists (hallucination detection, summarization quality, embedding similarity, toxicity, context relevance) — a pre-built-metrics pole.
- Scorers can also be applied to individual calls (production traffic / specific op invocations) via an apply-scorer mechanism; results stored in the product's database and viewable in the UI; monitors/guardrails guides referenced for production use.
- Score analysis surfaces: per-call scores, multi-call score columns in the traces table, per-scorer views across all scored calls — comparison oriented to versions of models/ops.

### promptfoo

(Evidence layer A unless noted.)

- Self-description: "an open-source CLI and library for evaluating and red-teaming LLM apps"; goals: "Build reliable prompts, models, and RAGs with benchmarks specific to your use-case"; "Score outputs automatically by defining metrics (assertions)".
- Philosophy: "test-driven LLM development, not trial-and-error"; "Simple, declarative test cases: Define evals without writing code"; runs "completely locally — the evals run on your machine and talk directly with the LLM"; provider catalog (OpenAI, Anthropic, Azure, Google, HuggingFace, open-source models, custom API providers).
- Workflow (documented five steps): define test cases (core use cases and failure modes) → configure evaluation (prompts, test cases, providers) → run evaluation (CLI/library records model outputs per prompt) → analyze results (automatic requirements or review in structured format / web UI; select best model and prompt) → feedback loop (expand test cases as examples and user feedback accumulate).
- Output surfaces: **matrix views** for side-by-side comparison of outputs across many prompts and inputs; CLI output; web viewer with share functionality for teammates.
- Delivery: CLI, library, or CI/CD (GitHub Action documented in the integration menu); caching, concurrency, live reloads as developer-quality features.
- Red teaming / guardrails / model security ship as adjacent product surfaces of the same vendor — bundling note for the guardrail boundary.

## Cross-product Comparison

| Aspect | LangSmith (imported) | Braintrust | Langfuse | W&B Weave | promptfoo |
|---|---|---|---|---|---|
| Subject under test | your application version evaluated on datasets; app runs invoked via SDK | your task function ("typically an LLM call, but can be any logic: multi-step agent, retrieval pipeline, custom workflow") | your LLM application (traces, prompts, datasets, experiments via UI/SDK/OTel) | your model/ops invoked with dataset rows; scorers on outputs | your prompts/models/RAG pipelines across configured providers |
| Test cases | dataset → examples (inputs + optional reference outputs + metadata), splits, versions | dataset of test cases (inputs, optional expected outputs, metadata) | datasets as reusable test-case sets | dataset rows (label/target columns map to scorer args) | declarative test cases + assertions/metrics in config |
| Central record | experiment (per app version × dataset, with traces) | experiment ("the immutable, comparable record of your eval runs") | experiments (side-by-side comparison of prompt/model/code changes) | Evaluation results stored in database; per-call feedback records | recorded outputs per run, reviewable in web viewer/share |
| Scorer families | code, LLM-as-judge, human (queues, rubrics, pairwise) | code, LLM-as-judge, autoevals, classifiers | code evaluators, LLM-as-judge, human annotation (queues, UI scores, user feedback, text scores) | code functions, class-based scorers, LLM-as-judge; built-in catalog | assertions/metrics incl. model-graded (assertions doc); human review not evidenced on fetched page |
| Offline vs online | explicit first-class split | explicit (offline datasets vs online scoring rules) | explicit (online live traces vs offline dataset tests) | offline Evaluation object + apply-scorer-to-call for production | local/CI eval runs; production scoring not evidenced on fetched page |
| Comparison surface | experiments compared side-by-side per dataset | playground side-by-side; experiment comparison | experiments compare prompt/model/code changes side by side; score analytics trends | traces table score columns; per-scorer views; version comparison | matrix views across prompts × inputs; CLI; web viewer |
| CI/CD | dataset versions targeted in CI; pytest/Vitest | evals on every pull request | CI/CD experiments "block deploys on regressions" | not evidenced on fetched page | GitHub Action integration documented |
| Mutable iteration surface | playground (sibling record) | playgrounds (mutable) vs experiments (immutable) | experiments via UI (iteration implied); no playground claim made from fetched page | not evidenced on fetched page | live reloads + caching dev loop |
| Production → dataset feedback | explicit (traces to examples) | explicit ("Feed back" stage) | explicit (datasets from traces; monitor → build datasets) | apply-scorer on calls; monitors guide (feedback loop not explicit on fetched page) | feedback loop step (user feedback → test cases) |
| Delivery posture | SaaS (self-host posture not verified) | SaaS | OSS self-host + cloud | library + hosted platform (part of W&B) | open-source CLI/library, local-first; vendor cloud/red-team products adjacent |

**Cross-product commonalities (layer B):** every sampled product has (1) the user's own LLM-driven system as the subject, reached either by the platform running the prompt/task or by capturing the application's outputs; (2) a dataset of test cases with inputs and optional expected outputs/criteria; (3) a scoring layer producing per-case graded feedback, with the code / LLM-as-judge / human scorer triad (human scoring not evidenced for two products on fetched pages — held as common across the sample, not universal); (4) a persisted record of evaluation results attributed to a configuration, comparable across versions; (5) comparison of prompt/model/code variants against a fixed dataset; (6) production traces/user feedback as a dataset source; (7) CI/CD automation (4 of 5 evidenced on reachable pages — common, not universal); (8) the offline (pre-deploy, reference-based) vs online (production, reference-free) split (4 of 5 explicit on fetched pages — common).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product is no longer an LLM evaluation platform:

```text
LLM-shaped system under test, reachable for measurement
  (the team's own prompts, model calls, and application workflows —
   run directly by the platform or captured from the instrumented
   application; the user's own system, not the market's models)
└── Test-case dataset
    (curated, reusable inputs + optional expected outputs or grading
     criteria, applicable across runs)
    └── Scoring mechanism
        (defined scorers — automated or human — applied per case,
         producing graded feedback)
        └── Persisted, comparable evaluation runs
            (results recorded as first-class objects, attributed to a
             version/configuration of the prompt/model/application,
             comparable over time)
```

Four invariants. Remove any one and the Type collapses:

- no own-system subject (the evaluated population is the market's models on standardized instruments) → AI Model Evaluation Platform
- no test-case dataset → a one-off script or a bare playground with no reusable basis of comparison
- no scoring criteria → trace collection/observability, not evaluation
- no persisted comparable runs → an ad-hoc notebook; no regression detection, no ship decision possible

Historical/market-sample check: the structure predates the current product generation — classical ML evaluation (held-out test set + metric computation + stored per-version results) satisfies legs 2–4, and NLG/machine-translation evaluation practice (generated text scored against references, results tabulated across system versions) satisfies output-level scoring of generated text; 2020–2022 prompt-development teams ran the same loop with spreadsheets and scripts. The platform packaging (managed datasets, defined scorers, run records, comparison surfaces, automation) is exactly what distinguishes the Type from "a script". Therefore L0 must not include LLM-as-judge (a modern scoring implementation), trace standards or tracing substrate (an ingestion implementation), CI/CD (automation posture), online scoring (a production extension), or cloud delivery.

### L1 — Common Mature Structure

Present in most mature products (layer B), expected by the market, not definitional:

- LLM-as-judge scorers (reference-based and reference-free), judge prompts with variable interpolation
- code/deterministic scorers and assertions (exact match, format validation, classification checks)
- human scoring workflows: annotation queues, rubrics, scores via UI, pairwise variant comparison
- online/production evaluation: automated reference-free scoring of live traces, with sampling/budget controls in some products
- CI/CD regression gates: evals per pull request/change, "block deploys on regressions"
- playgrounds: mutable iteration surfaces whose results are disposable, distinct from the immutable run record
- side-by-side comparison surfaces: experiment tables, matrix views across prompt variants × inputs
- dataset construction from production traces and user feedback
- score analytics: trends over time, per-metric dashboards
- cost/latency tracked alongside quality (recorded in the sibling pass's sample; held as common)
- model/provider catalogs enabling the same dataset to be run across model configurations
- versioning of datasets (and splits) so comparisons target a known dataset state

### L2 — Variant / Optional Structure

Depends on segment, delivery, ecosystem, or workflow:

- delivery posture: SaaS vs OSS self-host + managed cloud vs local CLI/library vs cloud-suite module
- authoring surface: SDK-as-code vs declarative config files vs UI playgrounds (products mix several)
- invocation mechanics: platform-runs-the-prompt, in-process function/library invocation, remote execution on customer infrastructure, sandboxed artifacts, trace ingestion only
- built-in scorer/metric catalogs vs user-defined-only scorers
- bundling: prompt management/versioning, guardrails, red-teaming/security testing, agent simulation, observability — all ship inside some products as adjacent surfaces
- judge-model strategy (which model judges, spend limits)
- enterprise governance (RBAC, data residency, self-hosted data planes)
- audience breadth: developers only vs PM/SME reviewers

### L3 — Vendor-specific Structure (Research Notes only)

- LangSmith: evaluator attachments with per-attachment sampling and spend limits; single-run vs pairwise annotation queue types; dataset splits with multi-split membership; pytest/Vitest runners; "Rules" automation (imported sibling record)
- Braintrust: autoevals library; remote evals (task code on the customer's own infrastructure); cloud sandboxes with product-specific invocation timeouts; saved parameters surfaced as playground UI controls
- Langfuse: score types (numeric/categorical/text); Score Analytics dashboards; experiments via OpenTelemetry; "AI engineering loop" academy framing; self-hosting + cloud tiers
- W&B Weave: `@weave.op` decoration model; `column_map`/`columnMapping` dataset-column mapping; auto-summarize with overridable `summarize`; `apply_scorer` on individual calls; named built-in scorers (hallucination-free, summarization, embedding similarity, local toxicity, context relevance); scorer versioning with "scored_by" queries
- promptfoo: declarative YAML-style config; matrix view output format; provider catalog incl. custom API providers; GitHub Action integration; live reload/caching; red-teaming product line (plugins/strategies/frameworks) adjacent to evaluation

## Vendor-specific / Rejected Findings

- "Evaluation requires an immutable experiment abstraction" — rejected as definitional *under that name*: the durable comparable run record is invariant; whether it is called experiment (LangSmith, Braintrust, Langfuse) or stored evaluation results (Weave, promptfoo) is naming. What matters is persisted, attributed, comparable results.
- "Evaluation requires trace visualization" — rejected; promptfoo and Weave document evaluation with no trace-visualization dependency on their fetched pages. Tracing is the common substrate of several products, not the defining act.
- "The platform must ship a built-in metric catalog" — rejected; Weave and Braintrust lead with built-in scorers, but LangSmith/Langfuse treat scorers as user-defined resources. Catalogs are L2/L3.
- "The subject is the bare prompt" — rejected; all sampled products evaluate prompts, model configurations, and application code/workflows. The canonical subject is "the team's LLM-shaped system", realized from prompt-only to multi-step workflows.
- "LLM-as-judge is the definition" — rejected; the scorer triad (code / judge / human) is the stable structure; LLM-as-judge is one implementation, dominant online because live traffic has no ground truth.
- "Evaluation platforms are SaaS" — rejected; promptfoo runs entirely locally, Langfuse self-hosts. Delivery is L2.
- Precise numbers (sandbox timeouts, sampling defaults, plan-gated capabilities) — L3, product-specific, kept out of the final document.

## Boundary Findings

1. **vs Agent Evaluation Platform (sibling, §13; FLAG DISCHARGED — joint review resolved).** The sibling pass flagged the two leaves as "one product family with two workloads — probable gradient or alias". This pass confirms the observations and resolves: **keep-both as a workload gradient, not an alias.** Evidence: (a) the four-leg evaluation core (own system under test + test-case dataset + scoring layer + persisted comparable runs) is shared, first-hand in this sample and recorded in the sibling's sample; (b) Braintrust's own task definition — "Typically an LLM call, but can be any logic: a multi-step agent, a retrieval pipeline, or a custom workflow" — states the workload spectrum in one sentence; (c) the load-bearing difference is center of gravity: this Type centers LLM-application behavior measured at the output/response level (prompts, model configurations, app responses, RAG answers); the agent sibling centers the multi-step tool-using agent with execution/trajectory scoring as a first-class surface. Market products serve both workloads in one platform, so the boundary is gradient at market level and definitional only as emphasis. This mirrors the ratified llm-application-development-platform vs agent-development-platform resolution. Both documents cross-reference the gradient; no directory change made from this side.
2. **vs AI Model Evaluation Platform (sibling, §13; FLAG DISCHARGED — structurally distinct, confirmed).** The sibling pass flagged loose market naming ("evaluation platform" used for both; some LLM-eval vendors publish model leaderboards as content) for joint review here. Confirmed from this side that the structures differ: subject = the user's own LLM application (run/captured by the platform) vs the market's models/endpoints; instruments = the user's own test-case datasets vs standardized publicly documented benchmarks; decision = ship/regression decision across one's own versions vs selection/ranking across a model population; central artifact = comparable evaluation runs vs a maintained public leaderboard. Vendor publishing of model leaderboards is content marketing, not structure. Clean keep-both.
3. **vs LLM Application Development Platform (processed sibling; FORWARD FLAG CONFIRMED).** That pass recorded evaluation as a bundled standard capability of dev platforms and hung a capability-sibling flag citing the LangSmith-class companion-product pattern. Confirmed: the build layer's defining objects (application construction machinery, developer-owned control flow) are absent from the evaluation platforms' defining core; conversely the scored-run record is not the dev platform's center. Two Types, one lifecycle; bundling and companionship, not identity.
4. **vs LLM Observability Platform (sibling; llm-observability-platform unprocessed — flag re-hung for that pass).** The scored run against criteria ("how good") vs the execution trace ("what happened"). Evaluation consumes traces (online scoring, span/call-level scoring, datasets built from traces), and every evaluation product in the combined sample bundles tracing. W&B Weave's apply-scorer-to-call and Phoenix's span evals (sibling record) show the shared machinery; the central record still differs. Gradient, not wall — re-flagged for the llm-observability-platform pass.
5. **vs Prompt Management Platform (unprocessed sibling).** Evaluation platforms bundle prompt versioning (Langfuse prompts; playground prompt editing), but the prompt-management Type would center the prompt asset's lifecycle (versions, environments, deployment) as the managed object, with testing as a feature. Reverse bundling exists (prompt tools adding eval). Flag for joint review when that leaf is processed.
6. **vs AI Safety / Guardrail Platform (processed sibling; CONFIRMED).** Guardrails screen live traffic and enforce per-content decisions (block/alter/flag/allow) on the LLM I/O path; evaluation measures at rest — offline runs and asynchronous online scoring produce feedback, not enforcement. promptfoo ships red-teaming/guardrails as adjacent product surfaces and Weave references a guardrails guide — bundling, consistent with the guardrail pass's own flag. Clean.
7. **vs Test Automation Platform / Software Test Management (§12, confirmed from the sibling's record + this sample's evidence).** Software tests assert deterministic pass/fail on deterministic systems; LLM evaluation produces graded, comparative, non-deterministic quality measurements. The bridge: evaluation metrics converted into regression assertions in CI (documented in this sample). Adjacent Types sharing the CI-gate surface; the distinction was articulated explicitly in the imported LangSmith record.
8. **vs Data Labeling Platform (§13 sibling, processed).** Human-scoring surfaces (annotation queues, rubric review) overlap labeling workflows, but the evaluation platform's managed object is the quality measurement of the user's own application; labeling's managed object is annotation production. Human review here is a scorer implementation, not the center. Clean with a noted overlap.
9. **Taxonomy observation.** The leaf name says "LLM", and the market's products indeed center LLM applications; multi-modal/multi-step workloads are absorbed as task functions without changing the core. The population also serves agents (workload gradient, finding 1). No taxonomy change proposed from this side.

## Uncertainties

- Provider-native evaluation features (model vendors' own eval tooling) exist in the market per general awareness, but OpenAI's docs were unreachable (403) and no cloud-provider eval docs were fetched this pass; the posture is noted, not characterized. The llm-application-development-platform pass recorded the same limitation for its provider pole.
- Weave's CI/CD integration and promptfoo's production-scoring depth were not evidenced on fetched pages; both held as unverified rather than denied.
- Langfuse's playground surface was not evidenced on the fetched overview; no claim made.
- LangSmith evidence is imported from the sibling pass (fetched 2026-09-06), not re-fetched; if that record were ever corrected, this pass's LangSmith-specific rows inherit the correction.
- Human-scoring depth for promptfoo and Weave unknown (not on fetched pages); the human-scorer leg rests on Langfuse (this pass) + LangSmith/Phoenix (sibling records).
- Market share/adoption not researched; product selection reflects documentation accessibility and philosophical diversity, not market size.
- Whether "LLM evaluation" remains a stable purchase category as agent evaluation absorbs mindshare is a market question; the workload-gradient resolution makes either evolution representable without re-drawing the Type.

## Final Synthesis

An LLM Evaluation Platform is a managed system for measuring the quality of the user's own LLM application's behavior. Its world contains four defining structures: (1) the LLM-shaped system under test, reachable for measurement — the platform runs the team's prompts, tasks, or workflows directly, or captures the application's outputs from an instrumented deployment; (2) test-case datasets — curated, reusable inputs with optional expected outputs or grading criteria, built from hand-written cases, production traces, and user feedback; (3) a scoring layer — code checks, LLM-as-judge prompts, and human review, applied per case to produce graded feedback; (4) persisted, comparable evaluation runs — each run recording one version/configuration of the system against one dataset, so that quality differences between prompt, model, or application changes are directly visible and regression decisions are data-backed.

Work flows in two coupled loops: an **offline loop** (build dataset → run the system against it → score → compare versions side-by-side → gate changes in CI) and an **online loop** (score live production traffic reference-free → trend scores → promote interesting traces into new test cases). The experiment/run is the immutable unit of record; playgrounds are the mutable iteration surface in front of it.

The Type is defined by the measurement-and-comparison loop over one's own LLM system — not by benchmarking the market's models (model evaluation), not by building the application (development platform), not by storing traces (observability), not by managing prompt assets (prompt management), and not by runtime enforcement (guardrails) — though real products bundle across every one of these lines, which is why the sibling boundaries are gradients with load-bearing centers rather than walls.
