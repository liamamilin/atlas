# Research Notes — AI Safety / Guardrail Platform

Research date: **2026-09-06**

## Research Goal

Understand what an AI Safety / Guardrail Platform actually is as an Application Type: what objects exist inside it, where it sits on the LLM application path, what its users do with it, what decisions it produces, and where its boundary lies against neighboring Types (AI Governance, LLM Observability, AI Gateway, LLM Evaluation, content moderation, DLP).

## Initial Boundary (hypothesis before research)

An AI Safety / Guardrail Platform is software that screens the inputs sent to and/or outputs produced by LLM-based applications against configurable safety/security policies, and returns a per-request finding/decision (block, alter, flag, allow).

Expected confusion surfaces:

- **AI Governance Platform** — organization/process-level control of AI systems (registry, review, policy) vs runtime content-level control.
- **LLM Observability Platform** — records/inspects executions vs acts on them.
- **AI Gateway / Model Routing** — sits on the same path but decides *where/how* to route, not *whether content is acceptable*.
- **LLM Evaluation Platform** — pre-release testing of model/agent quality vs live request-path screening.
- **Content moderation services** — UGC moderation at scale vs LLM application I/O protection (products may serve both).
- **DLP** — protects sensitive data across enterprise channels; guardrail DLP is scoped to the LLM path.

## Research Questions

1. What are the core objects? (policy/guardrail configuration, detector, screening request, finding, decision)
2. Where does interception happen — input side, output side, retrieval, tool/agent actions? Inline vs advisory?
3. What is detected? What is the detector taxonomy across products?
4. What decisions/actions are enforced? (block / mask-redact / flag / allow; fallback messages; re-ask)
5. How are policies configured, scoped (per app/feature/environment), and tuned (thresholds/sensitivity)?
6. What is the enforce-vs-monitor posture, and how do teams roll out (shadow mode, simulators, test windows)?
7. What operational surfaces exist (dashboards, logs, testing consoles, versioning)?
8. What delivery forms exist (model-provider native, standalone API, in-app framework, proxy) — and are they variants of one Type?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Delivery form |
|---|---|---|
| Amazon Bedrock Guardrails | hyperscaler-native safeguard, enterprise | managed feature of a model platform |
| Azure AI Content Safety | hyperscaler standalone content-safety service, spans UGC + AI content | API service + Studio |
| Check Point AI Guardrails (Lakera) | AI-security pure-play (security-team audience) | screening API (SaaS / self-hosted) + dashboard |
| Guardrails AI | open-source developer framework | Python library wrapping LLM calls |
| NVIDIA NeMo Guardrails | open-source orchestration toolkit, model-vendor neutral | library + optional guardrails server/microservice |

## Sources

All fetched live 2026-09-06 (evidence layer A unless noted):

- AWS: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html and …/guardrails-components.html
- Azure: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview
- Check Point AI Guardrails (Lakera): https://docs.lakera.ai/ , /docs/defenses , /docs/policies
- Guardrails AI: https://www.guardrailsai.com/docs , /docs/concepts
- NeMo Guardrails: https://docs.nvidia.com/nemo/guardrails/latest/ , /about-nemo-guardrails-library/rail-types

Note: docs.lakera.ai now serves Check Point AI Guardrails documentation (Lakera was acquired by Check Point); product-specific observations below are labeled accordingly.

## Product Observations

### Amazon Bedrock Guardrails (layer A)

- Positioning: "configurable safeguards … detect and filter undesirable content and protect sensitive information that might be present in user inputs or model responses."
- Filters ("safeguards") on a guardrail object:
  - **Content filters** — predefined harmful categories: Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack; per-category configurable strength; text and image; Standard tier extends detection into code elements.
  - **Denied topics** — user-defined topics to avoid; blocked when detected in user queries or model responses (example: banking assistant avoiding illegal investment advice).
  - **Word filters** — custom words/phrases (exact match) to block; ready-to-use profanity list; competitor names.
  - **Sensitive information filters** — PII detection (probabilistic, entity types such as SSN, date of birth, address) plus custom regex; per-use-case **block or mask**.
  - **Contextual grounding checks** — detect ungrounded (not supported by source) or irrelevant model responses in RAG; **block or flag**.
  - **Automated Reasoning checks** — validate responses against logical rules defined in natural language.
  - **Prompt attacks** — jailbreaks, prompt injections, prompt leakages (as a category within content filters).
- Guardrail lifecycle: created as a **working draft**, iterated with a **built-in test window**, then **versioned** and used with models.
- Applied by specifying guardrail ID + version at model inference; also usable **standalone** via the `ApplyGuardrail` API without invoking a model.
- On violation: blocked content replaced by **configurable messaging** (default available); blocked content appears in Model Invocation Logs (can be disabled).
- Input **tagging** lets RAG apps selectively evaluate only the user-input portion of a prompt (SDK-only).
- Cross-account and cross-region deployment options.

### Azure AI Content Safety (layer A)

- Positioning: "an AI service that detects harmful user-generated and AI-generated content in applications and services." Serves both UGC moderation and AI-content protection scenarios.
- Feature groups:
  - **AI safety and prompt protection**: Prompt Shields (jailbreak / user-input attack on LLMs), Groundedness detection (preview; responses grounded in supplied source material), Protected material text detection (known text such as lyrics/articles), Task adherence API (agent tool use misaligned/unintended/premature).
  - **Content analysis**: Analyze text / Analyze image APIs over harm categories (sexual, violence, hate, self-harm) with **multi-severity levels**; multimodal analyze.
  - **Custom detection**: Custom categories standard (train your own category) and rapid (define emerging patterns); blocklists (built-in terms + customer-uploaded).
- **Content Safety Studio**: online tool to test text/image content, adjust sensitivity, export code; **Monitor Online Activity** page with usage trends, category/severity distribution, latency, block rate and other KPIs; moderation workflows.
- API-first: each check is a separate REST endpoint with stated input limits and rate limits; region availability varies per feature.
- Noted limitation documented by vendor: cannot be used to detect CSAM.

### Check Point AI Guardrails (formerly Lakera Guard) (layer A)

- Positioning: "real-time AI application firewall for any applications using LLMs … screens any user or referenced contents passed into an LLM and the output response from the LLM."
- Five defense categories:
  - **Prompt defense** — direct and indirect prompt attacks, jailbreaks, prompt injections.
  - **Content moderation** — harmful/unwanted content per organization policy.
  - **Data leakage prevention** — PII, system-prompt leakage, sensitive data.
  - **Malicious links detection** — phishing/malicious links in LLM output.
  - **Agent Behavior Defense** — "Dangerous Deviation" detector (actions outside the agent's mandate) + runtime Tool Allow/Deny lists.
- Managed guardrails: ML + language models + rule-based filters; updated daily; fine-tunable on customer data/feedback.
- **Custom guardrails**: describe what to detect in plain language; AI assistant compiles into a detection policy (pattern rules + semantic rules).
- **Policy** object: assigned per **project** (application / LLM feature / environment / customer); determines which guardrails run on each `guard` API request and the flagging sensitivity; dynamically updatable on the fly.
- **Flagging logic**: `guard` API returns `flagged: true/false`. **Detect mode** forces `flagged: false` (monitor without enforcing); **Enforce mode** returns the real flag. Optional **breakdown** lists each guardrail's detection and confidence.
- **Sensitivity levels L1–L4** aligned with OWASP WAF paranoia levels (L4 paranoid default); threshold tunes detector confidence, not severity.
- Application decides what to do with a flagged response: block input/output, trigger user confirmation, or just log; recommendation is to control this via Project Mode so blocking can be switched without touching the integration.
- **Policy Impact Simulator**: compares flagging rates across sensitivity levels using historical traffic. Results endpoint for detector performance analysis (not intended for runtime decisions).
- Default policy: all managed guardrails at strictest sensitivity for untagged requests.
- Latency considerations documented; smart parallelization and chunking to minimize latency.
- Dashboard (platform.lakera.ai); SaaS and self-hosted deployment; evaluation frameworks and datasets for proof-of-value; adjacent AI Red Teaming offering.

### Guardrails AI (layer A)

- Positioning: Python framework that "runs Input/Output Guards in your application that detect, quantify and mitigate the presence of specific types of risks."
- **Guardrails Hub**: collection of pre-built **validators** for specific risk types; multiple validators combined into Input and Output Guards that "intercept the inputs and outputs of LLMs."
- **Guard object**: wraps LLM calls, orchestrates validation, keeps call history; central runtime interface.
- Two flows: `guard(...)` (framework calls the LLM, then validates the output) and `guard.parse(...)` (validate an output the developer already obtained), with optional **re-asks** (`num_reasks`) — re-prompting the model until output validates.
- Response distinguishes **raw LLM output** vs **validated output** vs `validation_passed`; documented error-handling and retry behavior.
- Also supports structured-data generation (pydantic) as a second function.

### NVIDIA NeMo Guardrails (layer A)

- Positioning: open-source Python library to "block, alter, or validate unsafe, off-topic, malicious, or policy-violating user inputs and model responses."
- **Rails at stages** of the LLM interaction:
  - **Input rails** (before LLM): content safety, jailbreak detection, topic control, PII masking.
  - **Retrieval rails** (RAG pipeline): document/chunk filtering.
  - **Dialog rails** (conversation): flow control, guided conversations.
  - **Execution rails** (tool calls): validate tool inputs/outputs and arguments before/after invocation.
  - **Output rails** (after LLM): response filtering, fact checking, sensitive-data removal.
- Configuration: YAML (models, prompts, rails, tracing) + **Colang** flows (guardrail logic, event-driven behavior) + **custom actions** (Python functions/tools/external APIs).
- Detector sourcing is pluggable: LLM self-checking, NVIDIA NemoGuard safety models, community models (e.g., LlamaGuard), third-party APIs (ActiveFence, Cisco AI Defense, Prompt Security, Pangea, Private AI, Presidio, GLiNER…), custom Python.
- PII can be configured to **detect-and-block or mask** before processing.
- Runtime interfaces: Python SDK (`LLMRails.generate`) or a **guardrails server** exposing OpenAI-compatible `/v1/chat/completions`; framework integrations (LangChain/LangGraph).
- Library (PyPI, self-managed) vs **microservice** (container, Kubernetes/Helm); configurations portable between both.
- Agentic security guidance: isolate auth from the LLM, validate tool inputs, apply execution rails, monitor actions.

## Cross-product Comparison

| Dimension | Bedrock Guardrails | Azure AI Content Safety | Check Point AI Guardrails | Guardrails AI | NeMo Guardrails |
|---|---|---|---|---|---|
| Screening target | user inputs + model responses | user prompts + AI-generated content (+ UGC) | LLM inputs + outputs + referenced content + tool interactions | LLM inputs + outputs (in-app) | inputs, outputs, retrieval, dialog, tool calls |
| Config unit | named guardrail (draft → test → version) | API-per-check + blocklists/custom categories + Studio workflows | policy per project; default policy fallback | guard composed of Hub validators | rails config (YAML + Colang) |
| Interception locus | model-platform native (at inference) or standalone API | standalone content-safety API called by app | screening API called by app/proxy | in-app around the LLM call | in-app library or OpenAI-compatible server |
| Detector catalog | harm categories, prompt attacks, denied topics, words, PII+regex, grounding, automated reasoning | harm categories (multi-severity), prompt shields, groundedness, protected material, custom categories, blocklists, task adherence | prompt defense, content moderation, DLP, malicious links, agent behavior | validators per risk type (Hub) | content safety, jailbreak, topic, PII, agentic; pluggable detectors |
| Decisions | block / mask / flag + configured fallback message | detection result + severity returned; app decides | flagged true/false (mode-controlled) + breakdown; app decides (block/confirm/log) | validation passed/failed; validated output; re-asks | block / alter (mask, rewrite) / validate |
| Tuning | per-category filter strength | severity levels; sensitivity in Studio | confidence levels L1–L4 (OWASP-style); per policy | validator parameters | rail/detector configuration |
| Monitor-only posture | flag (vs block) per filter | detection without blocking is app's choice | explicit Detect vs Enforce project mode | post-processing posture by construction | rails can inspect without intervening |
| Testing / rollout | built-in test window on draft | Studio test + monitor KPIs | Policy Impact Simulator on historical traffic; datasets/eval framework | call history; dev-time validation | dev-time config; playground via server |
| Ops surfaces | console; model invocation logs (blocked content visible) | Studio monitor: usage, category/severity distribution, block rate, latency | dashboard; results endpoint; policy management | call history in Guard object | tracing config; server logs |
| App scoping | guardrail ID+version at invocation | API resource + per-request parameters | projects → policy assignment | guard instances in code | config IDs per application |

## Canonical Abstraction

### L0 — Defining Invariant

```text
Screening point on the LLM application path
└── configurable policy of checks evaluated against model-bound / model-produced content
    └── per-content detection finding (unsafe elements identified)
        └── surfaced decision the path acts on (block / alter / flag / allow)
```

Four properties; remove any one and the product stops being this Type:

1. **Screening of LLM application content** — it evaluates the content that flows to the model (user input, and in many products retrieved context/tool exchanges) and/or comes from the model (responses, tool outputs). Not organization registries, not routing, not telemetry.
2. **Configurable checks policy** — what is checked, and how strictly, is customer-configurable rather than fixed.
3. **Detection findings** — each screened piece of content yields an explicit unsafe/safe determination, usually with the reason (category/entity/rule).
4. **Actionable decision on the path** — the finding materializes as block, alter (mask/rewrite), flag (annotate for downstream action), or allow, in either enforcement or advisory form.

The detector catalog is deliberately NOT in L0: older and simpler products (content-moderation-era services) screened for a narrow slice (e.g., toxicity only) yet were recognizably this function; and the catalog keeps expanding (today: agent/tool behavior). What makes the Type is *screening LLM-path content against a configurable policy to produce enforceable findings* — not *which* harms are detected.

### L1 — Common Mature Structure

- **Detector catalog across recurring harm families**: harmful-content moderation (predefined categories with configurable strength/severity), prompt-attack/jailbreak/injection defense, sensitive-data (PII) detection with block-or-mask, topic control (denied topics / topical rails), groundedness/hallucination checks against source material, and custom/organization-specific rules (phrase lists, trained custom categories, natural-language custom policies, logical-rule validation).
- **Threshold / sensitivity tuning** per check or per policy (filter strength, severity levels, confidence levels).
- **Monitor vs enforce posture** (flag-only / detect mode for rollout and false-positive tuning, then enforcement).
- **Named, versionable policy/configuration object** scoped per application/use case, with a safe default.
- **Testing surfaces**: sample-content test consoles, simulators against historical traffic, evaluation datasets.
- **Operational visibility**: dashboards of flag rates / category distributions / latency, screening logs, per-request breakdowns.
- **Configurable user-facing outcome on block** (fallback message; user confirmation as an alternative action).
- **Re-ask / remediation loop** (regenerate output when validation fails) in framework-form products.

### L2 — Variant / Optional Structure

- **Delivery form**: model-provider-native feature, standalone API service, in-app library/framework, OpenAI-compatible guardrails server, SaaS vs self-hosted.
- **Interception breadth**: input+output only vs adding retrieval, dialog, and tool/execution rails; agent/tool behavior defense.
- **Modality**: text-only vs text+image (+ multimodal); code-domain detection.
- **Detector sourcing**: managed vendor detectors vs LLM self-check vs community/safety models vs third-party APIs — pluggable in toolkit-form products.
- **Regulatory/IP extensions**: protected-material detection; logical-rule (compliance) validation.
- **Adjacent functions bundled by some vendors**: red-teaming, evaluation frameworks/datasets, governance reporting, structured-data validation.

### L3 — Vendor-specific (research notes only)

- `ApplyGuardrail` standalone API, cross-account/cross-region enforcement, input tagging, Automated Reasoning checks (AWS).
- Task adherence API; multi-severity vocabulary; Studio KPI set; region-per-feature availability matrix (Azure).
- "Dangerous Deviation" detector naming; daily detector updates; Policy Impact Simulator; OWASP paranoia-level L1–L4 vocabulary; plain-language custom guardrail compiler; default policy at L4 (Check Point/Lakera).
- Colang language; rail stage names; NemoGuard NIMs; `num_reasks`; Guard object / RAIL / validated-output vocabulary; Guardrails Hub (Guardrails AI).
- Naming: docs.lakera.ai now fronts Check Point AI Guardrails.

## Rejected Findings

- "Guardrail platforms are content moderation services" — rejected as the definition: moderation (UGC at scale) is a neighboring market some products also serve; the defining orientation here is the LLM application I/O path.
- "PII masking is core" — rejected: not all samples center PII (Azure's fetched overview doesn't even list it as a headline feature); PII is one entry in the detector catalog (L1).
- "Prompt injection defense is core" — rejected: security-pure-play products center it, but the older moderation-era function and content-safety-only deployments are still the same Type; catalog entry (L1).
- "A versioned policy object is core" — rejected: Azure's API-first shape applies checks per request with product-managed detector resources; named policy objects are the common mature shape, not the invariant.
- "Latency numbers" — only one product publishes concrete latency-handling claims in the fetched docs; no cross-product numeric claims made.

## Historical / Market-Sample Check

The Type is young (2023+). Applying the "older / platform-native / differently positioned products" check: predecessor content-moderation services (and classic UGC moderation stacks) performed a narrow slice of this function — screening content against fixed categories — without the LLM-path orientation, configurable check composition, or the input/output pairing. They fit the *detector-catalog* layer but not the L0 screening-point-on-the-model-path framing. Conversely, defining L0 by today's headline threats (jailbreaks, prompt injection) would exclude those predecessors and freeze the definition to a 2024–2026 threat fashion. Therefore the invariant is stated at the screening/policy/decision level, with the detector catalog explicitly held at L1. Platform-native model-provider features (Bedrock), standalone services (Azure), and developer frameworks (Guardrails AI, NeMo) all satisfy the L0 — delivery form is L2.

## Boundary Findings

- **vs AI Governance Platform**: governance operates at the organization/process level — registry of AI systems, policy frameworks, human review lifecycle, recorded decisions, evidence. Guardrails operate at the content/request level at runtime. A guardrail platform without the screening/decision path (only registries/reviews) becomes an AI Governance Platform; a governance platform with an embedded runtime screening engine starts to *contain* this Type as a module. Remove the LLM-path content screening and the decision-on-path, and what remains is governance.
- **vs LLM Observability Platform**: observability records and inspects executions (traces, spans, costs) without deciding. Guardrails decide. Overlap: guardrail findings land in dashboards/logs, and some observability products bundle basic moderation checks — a capability/gradient relationship. Remove the enforceable per-request decision and the product is observability.
- **vs AI Gateway / Model Routing Platform**: both sit on the request path, but gateways decide *where/how* a request is served (provider selection, failover, budgets); guardrails decide *whether the content may proceed*. Guardrail hooks inside gateways are a bundling pattern (already flagged by the ai-gateway research pass). Remove content-level findings/decisions and the product is a gateway.
- **vs LLM Evaluation Platform**: evaluation tests models/agents before release (datasets, scorers, runs); guardrails screen live traffic. Guardrail vendors bundle eval datasets/red-teaming as rollout tooling. Remove the live-path enforcement and the product is evaluation.
- **vs Content Moderation (neighboring market, no dedicated directory leaf)**: Azure explicitly serves UGC-moderation scenarios too. The LLM-I/O orientation (paired input/output screening on the model path, prompt-attack family, grounding checks) is the distinguishing center of gravity; pure UGC moderation is a different (here unlisted) Type.
- **vs DLP**: classic DLP protects enterprise data across channels; guardrail DLP is the same detection idea applied to the LLM path as one entry in the catalog — a capability, not the Type.
- **vs AI Security Platform (§15 leaf, separate)**: Check Point/Lakera shows the straddle — AI-security platforms span red teaming, threat intelligence, posture; guardrails are the runtime enforcement slice. The runtime I/O screening function is this Type; the broader estate-level security program is the other leaf. Flagged for joint review.

**Litmus tests**:
- Remove per-content screening/decisions on the model I/O path → AI Governance (process level) or Observability (measurement level).
- Keep screening but drop the model context (arbitrary UGC channels) → content moderation, not this Type.
- Keep the path position but the decision is routing/cost → AI Gateway.

## Uncertainties

- **Azure AI Foundry content filtering** (filters attached to model deployments) was not fetched; Azure's role as model-provider-native guardrail (parallel to Bedrock Guardrails) is inferred from product family structure, not directly evidenced. Stated carefully in the final document.
- Detector catalogs evolve weekly in this market; the comparison table reflects the fetched documentation state (2026-09-06), not a stable catalog.
- Guardrails AI also serves structured-data generation; whether that is in-scope for this Type was treated as an adjacent function (its Input/Output Guard function is the in-scope part).
- Whether the market converges on "AI safety" vs "AI security" naming (governance-flavored vs security-flavored) is unsettled; the directory leaf covers the guardrail function under either name.
- PII handling in Azure Content Safety: not evidenced in the fetched page; no claim made either way.

## Final Synthesis

An AI Safety / Guardrail Platform is a control point on the path between users and LLM applications: it screens the content that goes to the model and/or comes from it against a configurable policy of checks (harm moderation, prompt-attack defense, sensitive-data, topic control, grounding, organization-specific rules), produces explicit per-content findings, and materializes them as decisions — block, mask/alter, flag, or allow — under either enforcement or monitor-only posture. The same function ships in several delivery forms (model-provider native, standalone API, in-app framework, guardrails server); the detector catalog, tuning machinery (thresholds, sensitivity, simulators), testing surfaces, and dashboards are the common mature structure around it. Its identity is held by the runtime screening-and-decision function, not by any specific detector or delivery form.
