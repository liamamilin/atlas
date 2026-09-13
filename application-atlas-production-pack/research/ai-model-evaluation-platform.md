# Research Notes — AI Model Evaluation Platform

## Research Goal

Understand what an AI Model Evaluation Platform actually is by studying real products: what its central objects are (the model population, the evaluation instrument, the score, the leaderboard), how models get evaluated (fixed benchmark suites, blind pairwise human preference, consortium-defined workloads, self-serve harnesses), who runs the evaluations and who consumes the results, how comparability is maintained over time, and where the boundary lies against LLM Evaluation Platform, Agent Evaluation Platform, ML Model Monitoring Platform, Model Registry, Data Labeling Platform, A/B Testing Platform, and AI Safety/Guardrail Platform.

## Initial Boundary

Hypothesis before research: an AI Model Evaluation Platform systematically measures the capabilities/quality/performance/safety of AI models — the market's models, not the user's own application — against standardized evaluation instruments, and publishes persistent, comparable results (scores, rankings, leaderboards) that inform model selection and track model progress over time.

Nearest confusables:

- LLM Evaluation Platform — same word "evaluation", but the system under test is *your own* LLM application/prompt against *your own* test cases, to ship changes
- Agent Evaluation Platform — same, for *your own* agent; the sibling research pass (research/agent-evaluation-platform.md) already framed this leaf as "benchmarks foundation models against (often public, fixed) benchmark datasets to select a model"
- ML Model Monitoring Platform — observes *your deployed* model in production over time (drift, incidents)
- Model Registry — catalogs *your own* models/versions with lineage and stage
- Data Labeling Platform — produces ground-truth data; evaluation consumes instruments
- A/B Testing Platform — pairwise human preference mechanics overlap, but subject is product variants, decision is ship
- AI Safety / Guardrail Platform — guardrails enforce at runtime; safety benchmarks measure at rest

Prior note from the agent-evaluation-platform pass (STATUS.md Boundary Issues): "vs ai-model-evaluation-platform and test-automation-platform boundaries are clean (own-agent-vs-benchmark, graded-vs-pass/fail)". This pass researches the model-benchmarking Type itself.

## Research Questions

1. What is the central persistent object — the leaderboard? the per-model score record? the evaluation run?
2. What is the "evaluation instrument" — fixed benchmark suites? blind pairwise human votes? consortium-defined workloads? configurable harness runs?
3. Which subject is evaluated — the model, the hosted endpoint, or the hardware/software system?
4. How are models obtained (hosted APIs, open weights self-run, vendor submissions)?
5. What is scored and how is it aggregated (raw metrics, ratings like Elo, weighted indices)?
6. How is comparability maintained over time (fixed rules per round, versioned suites, reproducible runs)?
7. How are saturation, contamination, and gaming handled?
8. What does the user-facing comparison surface look like (leaderboard, model detail, side-by-side)?
9. What dimensions beyond quality are measured (speed, price, safety, bias, efficiency)?
10. Who operates and who pays (free public, commercial services, consortium membership, academic)?
11. Where is the line vs LLM/agent evaluation, vs monitoring, vs registries, vs labeling, vs A/B testing?

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| Chatbot Arena / LMArena (LMSYS origin) | defining human-preference arena; crowdsourced blind pairwise voting aggregated into ratings | crowd-human evaluation, free public web platform |
| Artificial Analysis | independent commercial analyst; intelligence + performance + price benchmarking of models and endpoints for buyers | independent third-party measurement, commercial |
| MLCommons (MLPerf, AILuminate) | industry consortium; working-group-defined benchmarks, audited vendor submissions; performance + safety | consortium/audited, member vendors |
| HELM (Stanford CRFM) | academic open framework + official leaderboards; holistic multi-metric evaluation | academic, open framework + public leaderboard |
| OpenCompass | open-source self-serve evaluation harness + public LLM/VLM leaderboards; non-Western ecosystem | open community, self-serve harness + leaderboard |

Selection covers: crowd-human vs automated-benchmark vs consortium vs academic vs open-self-serve philosophies; free-public vs commercial vs membership vs academic operating models; Western vs Chinese ecosystems; model vs endpoint vs system subjects.

## Sources

- LMSYS Org — "Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings" (original methodology post): https://lmsys.org/blog/2023-05-03-arena/ (fetched 2026-09-06)
- Artificial Analysis — Benchmarking Methodology: https://artificialanalysis.ai/methodology (fetched 2026-09-06)
- MLCommons — Benchmarks overview: https://mlcommons.org/benchmarks/ (fetched 2026-09-06)
- HELM — documentation (Read the Docs): https://crfm-helm.readthedocs.io/en/latest/ (fetched 2026-09-06)
- OpenCompass — documentation (Read the Docs): https://opencompass.readthedocs.io/en/latest/ (fetched 2026-09-06)

Source-access limitations:

- lmarena.ai (root, /methodology) and news.lmarena.ai timed out repeatedly; huggingface.co (Open LLM Leaderboard space and v2 announcement blog) timed out twice. Per the network-abandonment rule these sources were dropped. LMArena claims are therefore limited to what the original LMSYS methodology post documents (layer A for the original platform); current LMArena product specifics (category leaderboards, style controls, enterprise offerings) were NOT verified and are NOT asserted. The Hugging Face Open LLM Leaderboard was dropped from the sample entirely and is not described.
- Artificial Analysis sub-pages (intelligence-index internals, capability indices) were not fetched; AA claims are kept at the methodology-overview level.
- MLCommons sub-pages (per-suite rules, AILuminate safety methodology) were not fetched; MLCommons claims are kept at the benchmarks-overview level.
- No precise numeric limits (benchmark sizes, vote counts beyond the historical 4.7k example, index weights) are asserted in the final document.

## Product Observations

### Chatbot Arena / LMArena (LMSYS origin)

(Evidence layer A for the original platform via the LMSYS methodology post; current LMArena product specifics unverified.)

- Self-description: "a benchmark platform for large language models (LLMs) that features anonymous, randomized battles in a crowdsourced manner".
- Motivation: open-ended problems are hard to auto-evaluate → human evaluation based on pairwise comparison; desired properties: scalability (many models), incrementality (new model needs few trials), unique order (total ranking).
- Mechanism: user chats with two anonymous models side-by-side, votes for the better answer; model names revealed only after the vote; only votes cast while names are hidden are counted. Platform logs interactions.
- Aggregation: Elo rating system (chess-style) over pairwise battle outcomes → a single ranking; pairwise win rates used for calibration. (The 2024 paper moved to Bradley-Terry style aggregation — noted in citation, not asserted as current behavior.)
- Instrument: real user prompts ("in the wild") rather than fixed academic datasets; the comparison table in the post contrasts this with HELM/lm-evaluation-harness (academic datasets, program evaluator, basic metrics) and OpenAI evals (no ranking mechanism).
- Publication: leaderboard updated periodically via blog posts; hosted as a public HF space; community invited to contribute models (documented add-a-model guide) and votes.
- Planned (2023): fine-grained rankings on different task types; larger model counts; better sampling/tournament mechanisms.

### Artificial Analysis

(Evidence layer A, methodology overview page.)

- Self-description: "performs intelligence, quality, performance and price benchmarking on AI models, inference API endpoints and systems"; benchmarks "both proprietary and open weights models".
- Vocabulary it maintains: **Model** (LLM incl. proprietary/open), **Model Creator**, **Endpoint** (hosted instance via API; one model may have multiple endpoints across providers), **Provider**, **System** (dedicated compute environment benchmarked under load), **Open Weights**.
- Intelligence benchmarking: benchmark suites composed into weighted **capability/intelligence indices**; a **Cost per Task** metric derived from actual token consumption weighted by the same per-benchmark weights as the index.
- Performance benchmarking: measures "the end-to-end performance experienced by customers of AI inference services" — not maximum hardware performance; metrics include Time to First Token, Output Speed (tokens/sec, standardized to OpenAI tokens for cross-model comparability), total response time; reasoning-token averages computed over a fixed prompt set.
- Price benchmarking: per-token input/output prices as listed by providers; a **blended price** (fixed ratio assumption) for easier comparison.
- Scope beyond text: methodology sections for speech-to-text, text-to-speech, text-to-image, video generation, music generation; coding-agents benchmarking; system load testing; an "Openness Index".
- Surfaces: public leaderboards (LLM, image arena, video arena), an "Image Arena"/"Video Arena" (arena-style surfaces), model recommender, evaluations products, commercial services (data platform terms, services page).
- Positioning: independent third party; results intended to represent "real-world performance customers experience across providers".

### MLCommons (MLPerf, AILuminate)

(Evidence layer A, benchmarks overview page.)

- Self-description: "Delivering open, useful measures of quality, performance and safety to help guide responsible AI development."
- MLPerf goals (five, stated verbatim in structure): fair comparison while encouraging innovation; accelerate progress through fair and useful measurement; **enforce reproducibility**; serve commercial and research communities; keep benchmarking effort affordable so all can participate.
- Benchmark management: "Each benchmark suite is defined by a working group community of experts, who establish the fair benchmarks for AI systems. The working group defines the AI model to run, the data set against which it gets run, sets rules on what changes to the model are allowed, and measures how fast a given hardware runs the model."
- Suites: MLPerf Training (speed to train to a target quality metric; HPC variant), MLPerf Inference (Datacenter/Edge/Mobile/Tiny/Automotive/Client/Endpoints), MLPerf Storage, AlgoPerf (training algorithms), **AILuminate** ("assesses the safety of general chatbot gen AI systems to help guide development, inform purchasers and consumers, and support standards bodies and policymakers"; has safety methodology, a jailbreak benchmark, agentic and multimodal variants).
- Submission model: join the working group (membership required for most; some public groups allow non-members under a test agreement), sign CLA and trademark license, registration deadlines before submission rounds; results published per round.
- Subject: for MLPerf, the system (hardware + software stack) running a defined model on a defined dataset — "measure not only the speed of hardware, but also the quality of training data, and quality metrics of an AI model itself".

### HELM (Stanford CRFM)

(Evidence layer A, Read the Docs landing.)

- Self-description: "an open source Python framework … for holistic, reproducible and transparent evaluation of foundation models, including large language models (LLMs) and multimodal models."
- Framework features (listed): datasets and benchmarks in a standardized format (e.g. MMLU-Pro, GPQA, IFEval, WildBench); models from various providers accessible through a **unified interface**; metrics beyond accuracy (efficiency, bias, toxicity); **web UI for inspecting individual prompts and responses**; **web leaderboard for comparing results across models and benchmarks**.
- Workflow: `helm-run` (run benchmark entries: benchmark × model × suite) → `helm-summarize` (aggregate) → `helm-server` (local web UI). Suites are named result collections.
- Official leaderboards maintained by the team: HELM Capabilities, HELM Safety, VHELM (vision-language); plus domain leaderboards (medicine — MedHELM published in a medical journal, finance) and aspect leaderboards (multi-linguality, world knowledge, regulation compliance); HEIM for text-to-image models.
- Reproducibility: "The HELM framework can be used to reproduce the published model evaluation results from these papers"; dedicated reproducing-leaderboards documentation.
- Lifecycle note: "HELM entered maintenance mode on June 1, 2026" — leaderboards/benchmarks have finite lives.

### OpenCompass

(Evidence layer A, Read the Docs landing/index.)

- Open-source evaluation framework (Python, GitHub open-compass/opencompass) operated together with public leaderboards (opencompass.org.cn: LLM leaderboard, VLM/multimodal leaderboard).
- Self-serve workflow: installation → dataset preparation → quick start ("run a mini experiment") → config system → configure datasets → prepare models → efficient evaluation → task execution and monitoring → metric calculation.
- Model access: prepare models (API or local); acceleration via vLLM/LMDeploy; evaluation of reasoning models documented via tutorials.
- Scoring breadth: metric calculation; LLM-as-judge evaluation; code evaluation (incl. Docker-based service); **subjective evaluation guidance** (human/subjective judging as a supported mode); math-verify guidance.
- Extensibility: add a dataset, add a model; prompt engineering for evaluation (prompt templates, meta templates, chain of thought); prompt viewer tool; results persistence.
- Leaderboard reproducibility: "Guide to Reproducing CompassAcademic Leaderboard Results" — official leaderboard results are reproducible with the open harness.

## Cross-product Comparison

| Aspect | Chatbot Arena / LMArena | Artificial Analysis | MLCommons (MLPerf / AILuminate) | HELM | OpenCompass |
|---|---|---|---|---|---|
| Subject under test | LLM chat assistants (market models incl. closed APIs) | Models **and endpoints** (proprietary + open weights), multiple modalities; systems for load tests | For MLPerf: the **system** (hardware+software) running a defined model; for AILuminate: chatbot gen-AI systems | Foundation models (LLMs + multimodal) via unified provider interface | LLMs/VLMs the user configures (API or local) |
| Instrument | Blind pairwise battles on real user prompts | Fixed benchmark suites → weighted intelligence/capability indices; performance probes; listed prices | Working-group-defined model + dataset + allowed-change rules, per round | Standardized benchmark datasets + multi-metric evaluation | Configured benchmark datasets + metrics (program, LLM-as-judge, code, subjective) |
| Evaluator | Crowd humans (anonymous vote) | Automated (program) | Submitters under consortium rules/audit | Program metrics | Program + LLM-judge + human/subjective modes |
| Aggregation | Elo-style rating → single ranking | Weighted index scores; TTFT/output speed; blended price; cost per task | Per-suite metrics; per-round published results | Per-benchmark metrics; leaderboard tables | Per-benchmark metrics; leaderboard |
| Central artifact | Public leaderboard (rating-ordered) | Public leaderboards + indices across modalities | Published per-round results tables | Official public leaderboards (capabilities/safety/VHELM + domain/aspect) | Public LLM/VLM leaderboards |
| Who runs evaluations | Operator serves models; crowd votes | Operator calls endpoints | Member submitters run per rules | Operator for official leaderboards; anyone can self-run the framework | Anyone self-runs; operator maintains official leaderboard |
| Comparability over time | Continuous votes; periodic leaderboard updates | Continuous re-benchmarking as models/prices change | Fixed rules per round; reproducibility as explicit goal | Versioned suites; published results reproducible from the framework | Reproducible runs; official results reproducible |
| Beyond quality | — (quality/preference only, in documented form) | Speed, price, openness index | Performance (speed), power working group, safety (AILuminate) | Efficiency, bias, toxicity | Efficiency (acceleration guidance) |
| Delivery / business model | Free public web platform | Free public site + commercial services/data platform | Consortium membership (or non-member agreements) | Open-source framework + public leaderboards (academic) | Open-source + public leaderboards |
| Self-serve | Community can propose/add models (documented guide) | No (operator-run) | Members submit per round | Yes — framework is runnable by anyone | Yes — harness is the product |

**Cross-product commonalities (layer B):** every sampled product has (1) a population of market AI models (or model-bearing systems/endpoints) as the evaluated subject; (2) a standardized, publicly documented evaluation instrument applied uniformly; (3) per-model results computed under that uniform procedure; (4) a persistent, maintained published comparison (leaderboard / per-round results) that grows as models are added; (5) a published methodology explaining how scores are produced; (6) reproducibility or auditability as an explicit value (MLPerf goal, HELM/OpenCompass reproduction guides, AA's fixed methodology, Arena's shared voting data/notebook).

**Notable non-commonalities:** the evaluator role differs fundamentally (crowd humans vs program vs audited submitters); the subject differs (model vs endpoint vs system); beyond-quality dimensions (speed/price/safety) are present in some but not all; self-serve harnesses exist in some (HELM, OpenCompass) but not others (AA, Arena operator-run).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product is no longer an AI model evaluation platform:

```text
Model population (market AI models / endpoints / model-bearing systems
 as the evaluated subjects — not the user's own application)
└── Standardized evaluation instrument
    (a defined benchmark suite / procedure applied uniformly to every subject)
    └── Uniform scoring → per-subject comparable results
        └── Persisted, maintained comparison artifact
            (leaderboard / ranking / per-round results, updated as the
             model population changes)
```

Four invariants. Remove any one and the Type collapses:

- no model population as subject → it is application/agent evaluation (the user's own system), or generic software testing
- no standardized instrument → ad-hoc reviews, marketing claims, or a directory/catalog with no measurement
- no uniform scoring → a collection of unrelated test reports; no ranking or comparison possible
- no persisted maintained comparison → a one-off benchmark script or paper, not a platform

Historical/market-sample check: the structure predates LLMs and holds for older samples — ImageNet/ILSVRC-era classification leaderboards, GLUE/SuperGLUE NLP leaderboards, and MLPerf (2018, pre-LLM) all satisfy: models/systems as subjects, fixed benchmark, uniform metric, published ranking. Academic papers with comparison tables satisfy invariants 1–3 but not continuous maintenance — the platform packaging (operated, updated, growing comparison) is what distinguishes the Type from a paper. Therefore L0 must not include: LLM-specifics, chat surfaces, Elo/crowdsourcing, public-web delivery, quality-only scope, open-weights-only scope, or LLM-as-judge (a modern scoring implementation).

### L1 — Common Mature Structure

Present in most mature products (layer B), expected by the market, not definitional:

- leaderboard/ranking as the central user-facing artifact
- per-model detail with per-benchmark / per-dimension scores
- multiple capability dimensions or categories (reasoning, coding, math, safety, vision, domain leaderboards)
- published methodology pages explaining how scores are produced
- side-by-side comparison of models
- continuous operation: new models added, results updated over time
- reproducibility/auditability of published results (reproduction guides, audited submissions, shared voting data)
- quality measured alongside speed and price for API-served models (in the buyer-oriented sample)
- category filters (open vs proprietary, modality, size/domain)
- self-serve harness for running the instrument yourself (in the framework-based products)

### L2 — Variant / Optional Structure

Depends on philosophy, audience, scope, and business model:

- evaluation philosophy: fixed benchmark suites vs blind pairwise human preference vs consortium-defined workloads vs multi-metric academic suites vs hybrid (analyst indices + arenas)
- evaluator: crowd humans, program metrics, LLM-as-judge, audited vendor submitters, subjective/human judging modes
- subject granularity: model vs hosted endpoint vs hardware/software system
- modality scope: text-only vs multimodal (vision, audio, image/video generation)
- beyond-quality dimensions: speed, price, safety, bias/toxicity, efficiency, power, openness
- operating model: free public platform, commercial subscription/services, consortium membership, academic lab, open-source community
- self-serve posture: operator-run only vs runnable harness + official leaderboard
- rating aggregation: Elo/Bradley-Terry-style ratings vs raw metric tables vs weighted composite indices
- regional/ecosystem variants (e.g., a Chinese open ecosystem with its own leaderboards)
- instrument lifecycle practices: refreshed/private question sets, per-round rule freezes, leaderboard retirement/maintenance mode

### L3 — Vendor-specific Structure (Research Notes only)

- Chatbot Arena/LMSYS: Elo formula on the logistic curve; votes counted only when model names hidden; FastChat serving stack; leaderboard hosted as an HF space; documented add-a-model community guide; historical 4.7k-vote example
- Artificial Analysis: OpenAI-token standardization (o200k_base) as cross-model unit; blended price with a fixed 7:2:1 cache/input/output ratio assumption; 2k reasoning-token default assumption; named products (Optima, MicroEvals, Model Recommender, Data Playground, Image Lab); AA-SLT system load test; AA-AgentPerf; Openness Index; cost-per-task formula
- MLCommons: working-group governance; membership vs non-member test agreement; CLA + trademark license requirements; registration deadlines per round; named suites (MLPerf Client/Storage/Tiny/Endpoints/Automotive…); AILuminate jailbreak benchmark; power working group
- HELM: `helm-run`/`helm-summarize`/`helm-server` CLI; suite concept; named leaderboard families (Capabilities, Safety, VHELM, HEIM, MedHELM, ToRR); maintenance mode entered June 1, 2026
- OpenCompass: config-system authoring; vLLM/LMDeploy acceleration; Docker-based code-eval service; lark bot reporter; CompassAcademic leaderboard reproduction guide; ICP filing (Chinese operation)

## Vendor-specific / Rejected Findings

- "Evaluation requires Elo ratings" — rejected as definitional; Elo-style aggregation is specific to the arena philosophy. Raw metric tables (HELM, OpenCompass, MLPerf) and weighted indices (AA) are equally canonical implementations of "comparable scoring".
- "Evaluation requires crowdsourced human voting" — rejected; only the arena family uses crowd humans. Program metrics and audited submitters are at least as common.
- "The platform must measure speed and price" — rejected as definitional; buyer-oriented platforms do (AA), academic/consortium samples measure quality/safety/performance differently. Speed/price is L1/L2.
- "The subject is always the bare model" — rejected; AA explicitly benchmarks endpoints (same model, different providers can differ), and MLPerf benchmarks systems. The canonical subject is "a market AI offering" (model, endpoint, or system).
- "The platform must be a self-serve harness" — rejected; operator-run platforms (Arena, AA) don't expose harnesses. Self-serve is a variant posture.
- "The platform must be free and public" — rejected as definitional; free-public is dominant in the sample but consortium membership and commercial services exist. Public delivery is L2.
- Precise numbers (blended-price ratio, reasoning-token defaults, historical vote counts, benchmark names as exhaustive lists) — L3, kept out of the final document.

## Boundary Findings

1. **vs Agent Evaluation Platform** (sibling, §13; already framed in that pass): model evaluation benchmarks *market models* against *standardized instruments* to inform *selection/ranking*; agent evaluation measures *your own agent* against *your own test cases* across *your own versions* to *ship changes*. Different subject, dataset provenance, and decision. Clean distinction; no joint review needed beyond what is already flagged.
2. **vs LLM Evaluation Platform** (sibling, §13): same shape as (1) — the system under test is the user's own LLM application/prompt, the datasets are the user's own, the decision is a ship decision. Model evaluation's subject is the market's models, instruments are standardized/public, the decision is adoption/selection. In market practice the naming is loose: some LLM-eval vendors publish model leaderboards as content, and "model evaluation" is sometimes used for app eval — probable naming confusion, not structural identity. Flagged for joint review when LLM Evaluation Platform is processed.
3. **vs ML Model Monitoring Platform** (sibling, §13): monitoring observes *your deployed* model in production over time (drift, quality trends, incidents); model evaluation measures *market models* against fixed instruments at adoption time, in discrete rounds/updates. Different subject (yours vs the market's), different time orientation (continuous production vs point-in-time rounds). Clean.
4. **vs Model Registry** (sibling, §13): a registry catalogs *your own* models/versions with lineage, metadata, and stage; it answers "what do we have and what state is it in". Evaluation answers "how good is it against an instrument". Complementary; MLOps suites may bundle both. Clean.
5. **vs Data Labeling Platform** (sibling, §13): labeling produces ground-truth data; evaluation consumes instruments (which may embed labeled test sets). Some evaluation operators build private test sets — labeling-adjacent work, but the platform's defining act is measurement and comparison, not dataset production. Clean with a noted overlap.
6. **vs A/B Testing Platform** (§06 sibling): mechanics overlap (randomized pairwise human preference, aggregate ratings); subject and decision differ — A/B testing compares *your product's* variants with *your users* to make a ship decision; an arena compares *market models* with a crowd to produce a ranking. Clean.
7. **vs AI Safety / Guardrail Platform** (sibling, §13): guardrails enforce policy at runtime; safety benchmarks (AILuminate; HELM Safety) measure safety properties at rest and publish them. Safety evaluation is a scope/dimension of model evaluation, not a separate runtime control plane. Clean.
8. **vs the benchmark itself** (no dedicated leaf): a named benchmark (dataset + procedure) is an *instrument*; the platform operates instruments across a model population and maintains the comparison artifact. A benchmark without an operated comparison is not this Type. Recorded as an observation; no taxonomy change proposed.
9. **Taxonomy observation**: the leaf sits in §13 among enterprise AI-infrastructure leaves, but the dominant market form of this Type is a public web platform (often free) operated by an independent operator, consortium, or academic lab — not enterprise software purchased by an organization. This is a positioning observation, not a conflict; no taxonomy change proposed.

## Uncertainties

- Current LMArena product specifics (category leaderboards, style controls, enterprise/private arenas, post-2023 aggregation changes) unverified — lmarena.ai unreachable; final-document claims about the arena are limited to the documented original methodology, generalized.
- Hugging Face Open LLM Leaderboard not researched (huggingface.co unreachable); not described anywhere in the outputs.
- Private/expert evaluation services (paid private benchmarks, red-team reports) exist in the market per general awareness but were not sampled; not asserted.
- Artificial Analysis index internals (per-benchmark weights, suite composition) not fetched; kept coarse.
- MLCommons per-suite submission mechanics and AILuminate scoring internals not fetched; kept at overview level.
- Market share/adoption rankings not researched; product selection reflects documentation accessibility and philosophical diversity, not market size.
- Whether arena-style preference rankings will remain the dominant selection signal (vs static benchmarks) is a market question, not resolvable from this sample.

## Final Synthesis

An AI Model Evaluation Platform is a platform that measures and compares the market's AI models against standardized evaluation instruments, publishing persistent, comparable results that inform model selection and track model progress over time. Its world contains four defining structures: (1) a population of market AI models (models, hosted endpoints, or model-bearing systems) as the evaluated subjects; (2) a standardized, publicly documented evaluation instrument applied uniformly to every subject; (3) uniform scoring producing per-subject comparable results; (4) a persisted, maintained comparison artifact — a leaderboard, ranking, or per-round results table — that grows as models are added.

The instrument is the Type's philosophical fork: fixed benchmark suites scored by programs (academic/community leaderboards), blind pairwise battles voted on by humans and aggregated into ratings (arenas), consortium-defined workloads submitted under audit (performance/safety benchmarks), and independent analyst indices combining quality, speed, and price (buyer-oriented measurement). Everything else — Elo-style ratings, LLM-as-judge scoring, self-serve harnesses, multimodal scope, speed/price measurement, free-public vs membership delivery — is implementation or variant, not definition.

The Type is defined by the measurement-and-comparison loop over market models, not by the user's own application (that is LLM/agent evaluation), not by production observation of a deployed model (that is monitoring), not by cataloging one's own models (that is a registry), and not by runtime enforcement (that is guardrails). Its output is decision support for adoption and a public record of progress; it does not deploy models, host applications, or enforce anything.
