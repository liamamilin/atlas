# Research Notes — AI Model Hosting Platform

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (update-v1)

## Research Goal

Understand what an "AI Model Hosting Platform" actually is as an Application Type: what the central object is (a hosted model? an endpoint? a deployment?), where hosted models come from, how serving is operated and consumed, what rules govern usage, and where the boundary lies against the neighboring §13 Types (Model API Platform, AI Gateway / Model Routing Platform, Model Registry, Machine Learning Platform, MLOps Platform, LLM Application Development Platform, AI Model Evaluation Platform) and against generic GPU/serverless cloud (§14).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a platform that runs AI models on its own managed infrastructure and exposes them for invocation (API and/or interactive playground), where the hosted models are typically not the platform operator's own creations — third-party open-weights models, community-published models, or customer-uploaded/fine-tuned models.
- Likely confusions: Model API Platform (first-party model APIs — OpenAI/Anthropic serving their own models), AI Gateway (routing intermediary — already processed, frames hosting as the "upstream"), Model Registry (MLOps version catalog), ML Platform / MLOps Platform (end-to-end lifecycle), Serverless/GPU cloud (compute-level, not model-level), LLM Application Development Platform (builds apps on top of model APIs).
- Known cross-references: research/ai-gateway-model-routing-platform.md §Boundary Findings states "Hosting serves model inference (customer-owned/deployed models); the gateway runs no inference — it routes to hosted endpoints like any other upstream." This pass tests and refines that framing from the hosting side.

## Research Questions

1. What is the central managed object, and what is its lifecycle (catalog → deploy → serve → scale → update → deprecate)?
2. Where do hosted models come from (provenance): operator-curated third-party weights, community publishing, customer-uploaded weights, platform fine-tuning?
3. What serving modes exist (shared/serverless pay-per-use vs dedicated/private endpoints), and how does a user move between them?
4. What does the invocation surface look like (API shape, SDKs, playground, OpenAI compatibility)?
5. What infrastructure abstraction does the user see (hardware classes, replicas, autoscaling, scale-to-zero, cold starts)?
6. What rules matter (rate limits, quotas, access gating/licensing, regions, metering/billing basis, retention)?
7. What management surfaces exist (catalog pages, deployment config, dashboards, CLI, admin)?
8. What adjacent capabilities are bundled (fine-tuning/training, batch, evaluation, gateways, distribution)?
9. Where are the boundaries vs the neighboring Types listed above?
10. Would older / degenerate / differently-positioned forms (pre-LLM model APIs, community hubs, serverless-only catalogs, curated-only catalogs, weights-repository-only hubs, GPU clouds) still satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy | Customer level | Evidence quality |
|---|---|---|---|
| Replicate | developer-simple: "run models with a cloud API"; community model hub + custom model packaging | individual devs → teams/orgs | Tier-1 docs, multiple pages fetched |
| Together AI | open-weights inference cloud: serverless + dedicated model inference + fine-tuning | devs → startups → enterprise | Tier-1 docs, multiple pages fetched |
| Fireworks AI | speed/cost-focused open-model platform: serverless + on-demand dedicated + training | devs → enterprise | Tier-1 docs (root + deployments quickstart) |
| Baseten | production model-serving platform: hosted Model APIs + dedicated deployments + training; engines, multi-cloud capacity | devs → enterprises; also model labs | Tier-1 docs, multiple pages fetched |
| Amazon Bedrock | hyperscaler managed hosting of multi-provider foundation models; enterprise governance | enterprise (AWS accounts) | Tier-1 docs, multiple pages fetched |

Considered and not sampled:
- Hugging Face (community model hub + inference providers/endpoints) — docs at huggingface.co timed out on 2026-09-06 (2 attempts: /docs/inference-providers/index, /docs/inference-providers); per the source-access rule the source was abandoned. The community-hub shape of the Type is still covered through Replicate's community-model documentation.
- DeepInfra, OpenRouter (aggregator — gateway-side per the AI Gateway pass), Modal/RunPod (GPU compute clouds), SageMaker/Vertex AI (full ML platforms) — not fetched; used only as boundary reasoning anchors, not as evidence.

## Sources

All fetched 2026-09-06.

- Replicate — How does Replicate work?: https://replicate.com/docs/reference/how-does-replicate-work
- Replicate — Deployments: https://replicate.com/docs/topics/deployments
- Replicate — docs index (sidebar structure: models/predictions/deployments/webhooks/organizations/billing): fetched pages
- Together AI — Serverless models (available models): https://docs.together.ai/docs/serverless-models
- Together AI — Dedicated model inference overview: https://docs.together.ai/docs/dedicated-endpoints
- Together AI — DMI Concepts (resource model): https://docs.together.ai/docs/dedicated-endpoints/concepts
- Fireworks AI — docs root: https://docs.fireworks.ai/
- Fireworks AI — Deployments quickstart (on-demand): https://docs.fireworks.ai/getting-started/ondemand-quickstart
- Baseten — overview: https://docs.baseten.co/
- Baseten — How Baseten works: https://docs.baseten.co/concepts/howbasetenworks
- Amazon Bedrock — What is Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- Amazon Bedrock — Model availability & compatibility: https://docs.aws.amazon.com/bedrock/latest/userguide/models.html
- Amazon Bedrock — Request access to models: https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html

Source-access limitations:
- huggingface.co docs timed out twice on 2026-09-06 (2 distinct URL patterns); Hugging Face was dropped from the sample. No HF-specific claims are made anywhere in this research.
- Replicate /docs/topics/models returned a timeout on first attempt; not retried. The official-vs-community model distinction is asserted from the fetched docs' navigation structure and the "How does Replicate work?" page, not from a deep read of the dedicated pages.
- Fireworks evidence is root-page + deployments-quickstart level; serverless rate-limit mechanics and fine-tuning internals not verified.
- Bedrock custom-weight import (bring-your-own-weights) not verified; only customization via fine-tuning / continued pre-training / distillation observed on the fetched pages.
- Exact prices observed in docs (per-token, per-GPU-minute, per-hour) are recorded as pricing *bases* only; numeric price levels excluded as volatile commercial data.

## Product Observations

### Replicate (evidence layer A unless noted)

Positioning: "run machine learning models with a cloud API, without having to understand the intricacies of machine learning or manage your own infrastructure." Run open-source models others published, fine-tune with your own data, or build and publish custom models.

- Model definition (vendor's own): "a trained, packaged, and published software program that accepts inputs and returns outputs."
- Versions: model changes are published as new versions; "versioning is essential to making machine learning reproducible."
- Prediction = the central unit of work: an object representing a single run — inputs, outputs, model version, creating user, status, timestamps. Statuses: starting / processing / succeeded / failed / canceled; predictions time out after 30 minutes (contact support for more).
- Invocation surfaces: web UI (auto-generated form from the model's inputs — a playground) and HTTP API + client libraries (Python, JS, others). `replicate.run("black-forest-labs/flux-schnell", input={...})`.
- Model provenance: run any public model (open-source models created by others, e.g. meta/meta-llama-3-70b-instruct, stability-ai/sdxl) or push your own (public or private). Docs navigation distinguishes Official models vs Community models, private/public models, model versions, model hardware. (Layer A for structure; official/community page content not deep-read.)
- Discovery: explore/search returns models that are public, have ≥1 published version, and have ≥1 example prediction.
- Cold boots: "we only run the models that are actually being used. When a model hasn't been used for a little while, we turn it off." Warm vs cold responses; autoscaling runs multiple copies; popular models stay warm.
- Deployments (production tier): "production-grade control over your model's infrastructure and private, dedicated API endpoints." Hardware choice (A100/H100/T4 and more, switchable without code changes); auto-scaling from zero to hundreds of instances; min instances to keep warm; scale-to-zero; rolling updates, canary deployments, instant rollbacks; monitoring (latency, throughput, error rates, instance health, GPU memory, cost, request logs); private endpoints; audit logging. Works with open-source and custom models.
- Organizations: share models, API tokens, billing, dashboards; private models visible to the team.
- Rules/behaviors: rate limits on API requests; safety checker enabled for web predictions on some image models (disable-able via API); per-model licenses vary (commercial-use restrictions possible); API-created prediction inputs/outputs auto-deleted after an hour (web-created kept until deleted); output files served from a delivery domain; webhooks; prepaid-credit billing.

### Together AI (evidence layer A unless noted)

Positioning: open-model cloud. Two serving modes with an explicit relationship:

- Serverless models: "the fastest way to run inference... You call any supported model through a shared per-token API, with no provisioning, no replicas to size, and no minimum cost. Pay only for the tokens you process." Catalog organized by modality (chat, image, vision, video, audio, embedding, rerank, moderation) with models from many organizations (Qwen, DeepSeek, Meta, OpenAI gpt-oss, Google, Black Forest Labs, ByteDance, Moonshot, MiniMax, Z.ai, Cartesia, NVIDIA...). Pricing bases: per-1M tokens (chat), per megapixel + steps (image), per video, per-1M chars / per audio minute (audio). Serverless and dedicated support different model sets.
- Dedicated model inference (DMI): "serve a model on reserved hardware" — better performance, no hard rate limits, fine-tuned models, per-GPU-minute billing (cheaper at high utilization than per-token serverless). Uses the same inference APIs as serverless: "prototype on serverless, then deploy on DMI without changing your application code" — the endpoint string is passed as the `model` parameter.
- DMI resource model (vendor-documented): Project (org boundary, API-key scoped) → Model (concrete weights `ml_...`; an architecture has several weights, one per quantization) → Config (how a weight runs: engine, parallelism, GPU type/count, optimization profile; certified configs `cr_...`, immutable revisions) → Endpoint (stable inference URL, logical grouping of deployments) → Deployment (binds one model + config to an endpoint with an autoscaling policy) → Replica (model instance on dedicated hardware). Deployment profile = published certified weight×config pairing in the catalog. Instance types (e.g. `1xnvidia-h100-80gb`) with per-hour price and per-region capacity ("headroom" API).
- Traffic routing: weights per deployment; A/B tests (control/variant splits); shadow experiments (mirror traffic without serving responses). The application always calls the same endpoint string.
- Autoscaling: min/max replica bounds; scaling metric vs target; fast scale-up, deliberately slow scale-down (ride through troughs, avoid cold starts).
- Cold starts: loading weights + initializing engine; scale with model size; hold minReplicas ≥ 1 to keep warm.
- Model provenance: deploy Together-hosted models, models fine-tuned on Together, or uploaded fine-tuned models (associated with your project). Fine-tuning is a first-class adjacent capability.
- Management surfaces: console, management API, Python/TS SDKs, CLI (`tg beta endpoints deploy/get/rm`, A/B, shadow). Monitoring dashboards (latency, throughput, utilization) + events feed. Provisioned throughput (SLA, contact sales) as a third commercial tier.

### Fireworks AI (evidence layer A; root + quickstart level)

Positioning: "Fast inference and training for open source models."

- Three entry paths (vendor's own framing): Serverless ("popular models instantly with pay-per-token pricing... prototyping"), on-demand Deployments ("dedicated GPUs... high performance... fast autoscaling and minimal cold starts"), Training ("supervised and reinforcement fine-tuning... deploy immediately").
- 100+ supported models across text, vision, audio, image, embeddings; model selection guide.
- OpenAI compatibility as migration framing: "Drop-in replacement for inference and training — same API, same SFT data format."
- On-demand deployment mechanics (quickstart): `firectl deployment create <model> --deployment-shape fast --min-replica-count 0 --max-replica-count 1 --scale-to-zero-window 5m ...`. Deployment shapes = pre-configured templates (fast / throughput / cost) setting hardware and defaults; custom configuration also possible. Autoscaling load targets: requests_per_second, concurrent_requests. Deployment object exposes state (CREATING...), desired/actual replica counts, autoscaling policy, base model.
- Querying a dedicated deployment uses the same API as serverless — model string with deployment suffix, or plain deployment name via OpenAI SDK (`base_url=api.fireworks.ai/inference/v1`).
- Upload a custom model ("bring your own model and deploy it"); batch inference; function calling; structured outputs; embeddings & reranking.
- Compliance surface: SOC 2, HIPAA, audit reports (trust portal).

### Baseten (evidence layer A unless noted)

Positioning: "a platform for model inference and training. You can call hosted models through an OpenAI-compatible API, deploy your own models on dedicated infrastructure, or train models and serve the resulting checkpoints."

- Three ways to start (vendor's own framing): call a hosted model (Model APIs), deploy your model (dedicated), train a model (Loops / Training Jobs).
- Model APIs: "hosted endpoints for a curated set of models... support the OpenAI Chat Completions API and the Anthropic Messages API in beta... Baseten manages the model, engine, hardware, and scaling."
- Dedicated deployments: open-source model, private checkpoint, or custom model; defined via `config.yaml` (supported architectures — model, hardware, inference engine, no custom serving code), a Python model class, or a custom Docker server; deployed with the Baseten CLI. Control over model, hardware, autoscaling settings, release lifecycle; dev/staging/production environments.
- Packaging & engines: Truss (open-source packaging tool); weights downloaded from source repos (Hugging Face, S3, GCS) and compiled with TensorRT-LLM (Engine-Builder-LLM); BIS-LLM for large MoE models; BEI for embedding/rerank/classification; or vLLM/SGLang in a custom container. Each push produces an immutable content-hashed container image.
- Training: Loops (dedicated trainers/samplers for SFT and RL) or Training Jobs (your own container); checkpoints sync to storage and deploy to the inference stack like any model.
- Multi-cloud Capacity Management (MCM): provisions GPUs across cloud providers and regions; active-active deployments across clusters/clouds; reroute/reprovision on capacity loss.
- Request routing: per-model subdomain (`model-{id}.api.baseten.co`); URL path selects environment/deployment (`/production/predict`, `/development/predict`); scale-to-zero holds the request while a replica starts. Engine deployments expose OpenAI-compatible `/v1/chat/completions`; custom models use an arbitrary-JSON predict API.
- Autoscaling: concurrency-target based; scale-down delay and capped scale-down rate (defaults documented); min_replica 0 = scale-to-zero vs ≥1 = warm.
- Baseten Delivery Network (BDN): caches/deduplicates model weights across storage/clusters/nodes; a fine-tune sharing files with its base model downloads only the difference.
- Environments & promotion: development deployment → promote to named environment (staging/production); stable URL per environment; rollback re-promotes a previous published deployment reusing its image.
- Async requests: request ID returned immediately, queued, result delivered via webhook; sync requests get priority when capacity is tight.
- Operations: logs, metrics, request traces, observability export (Datadog, Prometheus, Grafana, New Relic); workspace secrets; SOC 2 Type II, HIPAA; regional environments for data residency; private networking / workload isolation / infrastructure ownership hosting options.
- Model Labs (adjacent business): Frontier Gateway (one access/policy layer across Baseten-hosted, third-party, and custom model targets) and Distribution Platform (model creators sell their model through Baseten; Baseten manages contract and billing).

### Amazon Bedrock (evidence layer A unless noted)

Positioning: "a fully managed service that provides secure, enterprise-grade access to high-performing foundation models from leading AI companies, enabling you to build and scale generative AI applications."

- Catalog: 100+ foundation models from leading providers — Amazon (Nova), Anthropic (Claude), DeepSeek, Moonshot AI (Kimi), MiniMax, OpenAI, xAI (Grok). Model cards with capabilities/pricing; "Models at a glance".
- Invocation: `bedrock-runtime` endpoint (plus `bedrock-mantle`); multiple API shapes — InvokeModel (provider-native body), Converse (AWS-native), Chat Completions and Responses (OpenAI-compatible), Messages (Anthropic-compatible; the docs' quickstart shows the Anthropic SDK pointed at a Bedrock base URL). Cross-region inference profiles for higher throughput/lower cost.
- Model access governance (distinctive enterprise layer): access to foundation models managed per account — AWS Marketplace subscription permissions (`aws-marketplace:Subscribe/Unsubscribe/ViewSubscriptions`), automatic subscription on first invocation, EULA agreement by first use ("by invoking/using a third-party model, you are implicitly agreeing to the applicable EULA"), Anthropic first-time-use form (use-case details per account/organization), IAM/SCP deny policies scoped to model ARNs to block specific models, GovCloud enablement flow. Model lifecycle page: versioning, deprecation timelines, migration guidance.
- Customization: "Customize your models to improve performance and quality" — fine-tuning, continued pre-training, distillation (custom-models chapter). (Custom-weight import not verified in this pass.)
- Commercial tiers: on-demand (per-use) vs Provisioned Throughput (reserved capacity for higher sustained throughput).
- Console: model catalog + playground ("select a model from the model catalog... open it in the playground").

## Cross-product Comparison

| Dimension | Replicate | Together AI | Fireworks AI | Baseten | Amazon Bedrock |
|---|---|---|---|---|---|
| Self-description | run ML models with a cloud API, no infra management | open-model cloud; serverless + dedicated inference | fast inference and training for open source models | model inference and training platform | fully managed access to foundation models from leading AI companies |
| Hosted-model provenance | community-published + official (third-party weights) + your own pushed models | many third-party orgs + fine-tuned-on-platform + uploaded fine-tuned | open source models + uploaded custom models | curated hosted set + open-source/private/custom deployments + trained checkpoints | multi-provider catalog (Anthropic, Meta, OpenAI, xAI, DeepSeek...) + Amazon's own + customized models |
| Shared/serverless mode | yes (run any public model; cold boots; per-use billing) | yes (shared per-token API, no provisioning) | yes (pay-per-token, prototyping) | yes (Model APIs, curated, OpenAI/Anthropic-compatible) | yes (on-demand invocation, per-use) |
| Dedicated mode | yes (deployments: private endpoints, hardware choice, min instances, canary/rollback) | yes (DMI: endpoint→deployment→replica, per-GPU-minute) | yes (on-demand deployments, shapes, load targets) | yes (dedicated deployments, environments/promotion) | yes (Provisioned Throughput; custom models) |
| Same API across modes | yes (deployment endpoints private; model API for shared) | yes (endpoint string as `model` param) | yes (deployment-specific model string) | yes (same endpoint URL across environments; OpenAI-compat for engines) | yes (same runtime APIs across on-demand/provisioned) |
| Invocation unit | prediction (object with status lifecycle) | request against model/endpoint string | request (chat completions) | request (chat completions or arbitrary-JSON predict) | request (Invoke/Converse/Chat Completions/Responses/Messages) |
| Playground / interactive surface | web form generated from model inputs | console | dashboard | dashboard | console playground |
| OpenAI compatibility | own prediction schema (HTTP API + client libs) | OpenAI-compatible chat completions | drop-in OpenAI replacement | OpenAI Chat Completions + Anthropic Messages (beta) | Chat Completions/Responses/Messages + native Invoke/Converse |
| Autoscaling & cold starts | scale 0→hundreds; min instances; cold boots documented | min/max replicas; fast-up/slow-down; cold-start guidance | min/max replicas; scale-up/down/scale-to-zero windows; load targets | concurrency-target autoscaler; scale-down delay; scale-to-zero; BDN weight caching | cross-region inference; provisioned throughput (mechanics not fetched) |
| Versioning | model versions; reproducibility emphasized | model weights per quantization; config revisions; deployment profiles | deployment over base model; custom model uploads | immutable content-hashed images; environment promotion; rollback | model lifecycle: versioning, deprecation, migration |
| Fine-tuning/training | fine-tune with your data (training destinations) | fine-tune on platform; upload fine-tuned models | SFT + RL fine-tuning, deploy immediately | Loops + Training Jobs; checkpoints deploy | fine-tuning, continued pre-training, distillation |
| Access gating | per-model licenses; safety checker | credit balance for image models | not observed on fetched pages | workspace access; Labs distribution | Marketplace subscription, EULA-by-use, use-case forms, IAM/SCP model-level deny |
| Org/team structure | organizations (shared models/tokens/billing) | projects (API-key scoped) | accounts | workspaces | AWS accounts + IAM + Organizations (SCP) |
| Metering basis | per-use (per second of compute for predictions; prepaid credit) | per-token (serverless) / per-GPU-minute (dedicated) | per-token (serverless) / dedicated per-hour implied by shapes | per-compute (replica-hours) + usage | per-token on-demand / provisioned capacity |
| Adjacent bundles | webhooks, MCP server, agent skills | A/B + shadow experiments, provisioned throughput, agent skills | batch inference, function calling, structured outputs | training, Frontier Gateway, Distribution Platform, async+webhooks | customization, cross-region inference, web search tool, IAM governance |

### Stable commonalities (evidence layer B, cross-product)

1. Hosted model as the central object: every product packages model weights + serving runtime into an addressable, versioned resource it operates (model/version, model weight + config, deployment over base model, Truss-packaged model, foundation model with lifecycle).
2. Platform-operated serving: the platform provisions and runs the compute (GPUs); users select hardware classes and scaling parameters but never operate servers. All five state this as their core value ("without... manage your own infrastructure", "no provisioning", "fully managed", "Baseten manages the model, engine, hardware, and scaling").
3. Invocation surface with metered usage: API endpoint (+ playground in all five) returning model outputs; usage attributed to the caller's account and billed on a documented basis (per-token, per-compute-time, per-output, per-hour capacity).
4. Models from origins other than the operator: third-party published weights (all five), community publishing (Replicate), customer-uploaded/fine-tuned models (all five except serverless-only paths), operator-customized models (Bedrock, Baseten, Together, Fireworks).
5. Dual serving economics: shared pay-per-use serving AND dedicated/reserved capacity exist in all five, with an explicit "same API, different backing" relationship (prototype shared → promote dedicated).
6. Catalog as the discovery surface: every product maintains a browsable model catalog with per-model detail (capabilities, pricing basis, limits, license/access requirements).
7. Scale-to-zero vs warm-capacity tradeoff and cold starts as a named, documented concern (Replicate cold boots; Together cold starts; Fireworks scale-to-zero window; Baseten cold starts + weight caching; Bedrock cross-region/provisioned alternatives).
8. Versioning and lifecycle: models have versions; platforms document updates and deprecation/migration (explicit at Bedrock; structural in the others).
9. Organization/team scoping of models, keys, and billing (orgs, projects, accounts, workspaces, AWS accounts).
10. Fine-tuning/training as an adjacent capability producing deployable hosted models (all five in some form).

### Stable variation axes (→ L2)

- Catalog posture: open community publishing (Replicate) ↔ curated operator catalog (Together, Fireworks, Baseten Model APIs, Bedrock).
- Packaging posture: platform-managed engine from configuration (Together configs, Baseten config.yaml, Fireworks shapes) ↔ customer-packaged code/container (Replicate Cog lineage, Baseten model class/Docker, Fireworks custom model upload).
- Pricing basis: per-token ↔ per-compute-time ↔ per-output-unit ↔ per-hour reserved capacity.
- Access gating: none/credit-balance ↔ license-gated models ↔ EULA-by-use + use-case forms + marketplace subscription + policy-level model deny (Bedrock).
- Governance/compliance depth: dev-tier ↔ SOC 2/HIPAA/regional residency/private networking/VPC (Baseten, Bedrock).
- Adjacent bundling: training, batch, A/B & shadow experiments, gateways, model distribution/marketplace, agent/MCP integration.

## Canonical Abstraction

### L0 — Defining Invariant

An AI Model Hosting Platform is a platform that operates model-serving infrastructure on behalf of others, with four defining properties:

1. **Hosted model as the central managed object** — a model (weights + serving runtime) packaged and run by the platform as an addressable, typically versioned resource that users select, deploy, and call. Remove this → the product is generic cloud compute / GPU rental (unit of deployment is an instance or function, not a model).
2. **Platform-operated serving infrastructure** — inference executes on compute the platform provisions, operates, and scales; the user configures (hardware class, scaling bounds) but does not operate servers. Remove this → the product is self-hosting or MLOps tooling over user-owned infrastructure.
3. **Invocation surface with metered usage** — an API endpoint (and commonly an interactive playground) that accepts inputs and returns model outputs, with usage measured and attributed to the caller's account. Remove this → the product is a weights repository or model registry (catalog without serving).
4. **Models from origins other than the platform operator** — the hosted population consists of third-party published models and/or customer-supplied (uploaded or fine-tuned) models; the platform is a host and operator, not the model's author. Remove this → the product is a first-party Model API Platform (a model developer serving its own models).

Deliberately NOT in L0 (checked against §24 historical/degenerate forms):
- LLM/foundation-model scope (Replicate hosts classic ML and image models; "machine learning models" is the vendor's own framing)
- dual serving modes (serverless-only catalogs satisfy the core; dedicated-only deployments satisfy the core)
- community publishing (curated enterprise catalogs satisfy the core)
- customer weight upload (curated serverless catalogs satisfy the core)
- OpenAI-compatible API (Replicate's prediction schema and Bedrock's Converse/Invoke are counterexamples)
- fine-tuning/training (bundled capability, not definitional)
- playground (common, not definitional — the API alone satisfies the core)
- specific pricing basis (per-token vs per-hour is a variant axis)

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- model catalog with per-model detail pages (capabilities, pricing basis, limits, license/access)
- dual serving modes: shared/serverless pay-per-use + dedicated/private endpoints on reserved hardware, reachable through the same API shape
- interactive playground / try-it surface (web form or console)
- API keys, client libraries/SDKs, code snippets; OpenAI-compatible chat-completions surface as a convergence point
- autoscaling with scale-to-zero vs warm-capacity tradeoff; cold starts documented and mitigated (weight caching, warm min replicas, scale-down delays)
- usage/cost dashboards and request logs
- rate limits/quotas on shared serving; dedicated capacity removes hard rate limits
- model versioning with update/deprecation lifecycle
- fine-tuning/training producing deployable hosted models (checkpoint → endpoint)
- async execution + webhooks for long-running generations
- organization/project/workspace scoping of models, keys, and billing

### L2 — Variant / Optional Structure

- catalog posture: open community publishing ↔ curated operator catalog
- packaging posture: config-only platform-managed engine ↔ customer container/code packaging
- engine transparency: engine choice exposed (TensorRT-LLM/vLLM/SGLang) ↔ hidden
- pricing basis: per-token / per-compute-time / per-output-unit / per-hour reserved
- access gating: credit balance / license-gated models / EULA-by-use + use-case forms / marketplace subscription / policy-level model deny
- region & compliance: cross-region inference, regional environments, data residency, private networking/VPC, SOC 2/HIPAA posture
- batch inference; provisioned throughput/SLA tiers
- adjacent bundles: training jobs, evaluation, A/B & shadow experiments, gateways, model distribution/marketplace, agent/MCP/coding-agent integration

### L3 — Vendor-specific (research notes only)

- Replicate: prediction object with status lifecycle and 30-minute timeout; Cog-lineage model packaging; official vs community model split; replicate.delivery output files; safety checker on web predictions; API prediction data auto-deleted after an hour; prepaid credit billing.
- Together AI: DMI resource model (project/model/config/endpoint/deployment/replica; certified config revisions `cr_...`; deployment profiles); instance types with per-region headroom; `tg` CLI; A/B tests and shadow experiments; provisioned throughput tier.
- Fireworks AI: deployment shapes (fast/throughput/cost); scale-up/down/scale-to-zero windows; load targets (requests_per_second, concurrent_requests); deployment-suffixed model strings.
- Baseten: Truss packaging; engine lineup (Engine-Builder-LLM/BIS-LLM/BEI); Multi-cloud Capacity Management; Baseten Delivery Network weight caching/dedup; environment promotion with stable URLs; async request service with sync priority; Model Labs (Frontier Gateway, Distribution Platform).
- Amazon Bedrock: AWS Marketplace subscription model for third-party models; EULA-by-use; Anthropic first-time-use form; IAM/SCP model-ARN deny policies; GovCloud flow; Converse API; bedrock-runtime/bedrock-mantle endpoints; cross-region inference profiles; Guardrails/Knowledge-Bases-style adjacent services (not fetched — not asserted).

## Rejected Findings

- "Hosting = LLM serving" — rejected: Replicate's own framing is "machine learning models" including image/classic models; the definition must not name LLMs or foundation models.
- "Hosting = dedicated GPU endpoints" — rejected: serverless-only catalogs (and dedicated-only deployments) each satisfy the core; dual modes are common, not invariant.
- "Hosting = community model hub" — rejected: curated enterprise catalogs (Bedrock, Baseten Model APIs) satisfy the core without community publishing.
- "Hosting = bring-your-own-weights" — rejected: curated serverless catalogs host only operator-onboarded models; upload is common, not invariant.
- "Hosting = OpenAI-compatible API" — rejected: Replicate's prediction schema and Bedrock's Converse/Invoke are counterexamples; OpenAI compatibility is a convergence point, not the definition.
- "Hosting = fine-tuning platform" — rejected: fine-tuning is a bundled adjacent capability; a hosting platform without training still satisfies the core.
- "Hosting = GPU cloud" — rejected: the unit of deployment differs (model vs instance/function); GPU clouds lack the hosted-model object and catalog semantics.
- "Hosting = model registry" — rejected: a registry catalogs/governs versions without serving; hosting serves. (Some registries sit inside ML platforms that also host — gradient noted in Boundary Findings.)

## Boundary Findings

1. **vs Model API Platform (§13 sibling).** The model API platform is a model developer serving its own models as the product (OpenAI/Anthropic pattern). The hosting platform hosts models whose creation it does not own. Test: remove third-party/customer models → a Model API Platform remains; add third-party models to a model vendor's API → it starts hosting. Gradient is real: hyperscalers host their own models alongside third-party ones (Bedrock serves Amazon Nova AND Claude/GPT/Grok), and model vendors increasingly host each other's open weights. Flag for joint review when Model API Platform is processed.
2. **vs AI Gateway / Model Routing Platform (§13 sibling, processed).** Confirmed from both sides: the gateway is an intermediary that runs no inference and routes to upstream provider APIs; the hosting platform IS the upstream that runs inference. The AI Gateway research explicitly frames hosting as the upstream ("routes to hosted endpoints like any other upstream"). Clean structural split; no flag needed beyond cross-reference.
3. **vs Model Registry (§13 sibling).** A registry catalogs and governs model versions (metadata, stages, approvals) within an ML lifecycle; it does not operate serving. A hosting platform runs models but its catalog is a consumption catalog, not a governance registry. Registries can feed hosting platforms (train → register → deploy). Flag for joint review when Model Registry is processed.
4. **vs Machine Learning Platform / MLOps Platform (§13 siblings).** Those span the full lifecycle (data, training, pipelines, deployment, monitoring) and often include self-managed serving on user-owned infra; the hosting platform centers on operating serving for consumption, with training as an adjacent bundle. Gradient: Baseten/Together/Fireworks bundle training; SageMaker/Vertex-class platforms bundle hosting. Flag for joint review when those leaves are processed.
5. **vs Serverless Management Platform / GPU cloud (§14).** The unit of deployment differs: serverless platforms deploy functions/containers; GPU clouds rent instances; hosting platforms deploy models with catalog semantics (weights, versions, licenses, per-token pricing). Baseten's custom Docker server and Replicate's custom packaging blur toward containers — gradient, not a wall. Flag for joint review when Serverless Management Platform is processed.
6. **vs LLM Application Development Platform (§13 sibling).** Dev platforms build applications on top of model APIs (orchestration, prompts, RAG, agents); hosting platforms serve the models those apps call. The AI Gateway pass already drew the model-API/agent-SDK gradient; hosting sits below both. Capability relationship only.
7. **vs AI Model Evaluation Platform (§13 sibling, processed).** Evaluation's central record is the scored run against criteria over a model population; hosting's central object is the served model. Hosting platforms may bundle benchmarks/leaderboards as catalog aids (observed as catalog guidance pages), but evaluation is not the operating core. Consistent with the evaluation pass.
8. **Naming observation.** The market uses "model hosting", "inference platform", "model serving platform", "AI cloud", "model API provider" for overlapping populations. "Hosting" names the operator relationship (hosting models on behalf of creators/users) better than "inference" (which names the workload) — the leaf name is serviceable; no rename proposed.

## §24 Historical / Market-Sample Check

The category predates the LLM boom, so the check runs against older and degenerate forms:

- Pre-LLM model APIs / ML-model hosting (Algorithmia-era; Replicate's original image/classic-model catalog; HF Inference API): satisfy the core — hence "AI/ML model", not "LLM/foundation model", in L0. ✔ covered.
- Community-hub form (anyone publishes; others run): satisfies the core — hence community publishing stays out of L0. ✔ covered.
- Curated enterprise catalog (Bedrock): satisfies the core — hence community publishing and open-weights emphasis stay out of L0. ✔ covered.
- Serverless-only catalog (no custom deployment): satisfies the core — hence dedicated endpoints and weight upload stay out of L0. ✔ covered.
- Dedicated-only deployment platform (no shared catalog serving): satisfies the core — hence serverless mode stays out of L0. ✔ covered.
- Weights repository without serving (HF Hub without inference): fails property 3 — correctly excluded (that is a registry/repository, not hosting). ✔ boundary holds.
- GPU cloud (rent instances, run anything): fails property 1 (no model-level object) — correctly excluded. ✔ boundary holds.
- First-party model API (OpenAI serving only GPT): fails property 4 — correctly excluded as a different Type. ✔ boundary holds.

The definition must also not over-fit today's dominant bundle (serverless + dedicated + fine-tuning + OpenAI-compatible API + usage dashboard); all of those are L1/L2.

## Uncertainties

- Hugging Face — arguably the most-cited model hub — could not be fetched (timeouts); its shape is covered indirectly via Replicate's community-model structure. If HF is later documented, re-check the community-publishing and catalog claims.
- Fireworks evidence is root + quickstart level; serverless rate-limit mechanics, fine-tuning internals, and custom-model upload flow not verified.
- Bedrock custom-weight import not verified; only fine-tuning/CPT/distillation customization observed.
- Replicate official-vs-community model page content not deep-read (timeout); distinction asserted from doc structure.
- Whether "model distribution/marketplace" (Baseten Labs) grows into a distinct Type — currently an adjacent bundle observed in one product (product-specific).
- Exact numeric limits (timeouts, rate-limit tiers, replica bounds defaults) observed per product but excluded from canonical claims as volatile vendor specifics.

## Final Synthesis

The AI Model Hosting Platform is the operator of model-serving infrastructure on behalf of others. Its defining core is small: models (weights + runtime) exist on the platform as addressable, versioned hosted objects; the platform provisions and operates the compute that runs them; users invoke them through APIs and playgrounds with usage metered to their accounts; and the hosted population comes from origins other than the platform operator — third-party published weights, community contributions, customer-uploaded or fine-tuned models. Everything the market associates with the category — the serverless/dedicated dual economics, the catalog with detail pages and pricing, OpenAI-compatible APIs, autoscaling and scale-to-zero with cold-start mitigation, usage dashboards, rate limits, versioning and deprecation, fine-tuning, batch, compliance postures — is mature structure layered on that core, and the catalog posture (community vs curated), packaging posture (config vs container), pricing basis, and access gating are variant axes, not the definition. The Type sits below application-development platforms (which build on its APIs), beside the model API platforms it converges with at the hyperscaler edge, upstream of the AI gateways that route to it, and distinct from the registries that catalog models without serving them and the GPU clouds that rent compute without model semantics.
