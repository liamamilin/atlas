# AI Model Hosting Platform

## Overview

An **AI Model Hosting Platform** operates model-serving infrastructure on behalf of others: it takes AI models — published by third parties or supplied by its users — runs them on compute the platform manages, and exposes them for invocation through APIs and interactive surfaces, with usage measured and billed to the invoker's account.

The defining structure is small:

```text
Hosted model (weights + serving runtime, versioned)
└── served on platform-operated compute
    ├── shared serving (pay per use, rate-limited)
    └── dedicated capacity (reserved, capacity-bound)
        └── invoked via API endpoint / playground
            └── metered usage attributed to the caller's account
```

Two properties make this a *hosting* platform rather than something else. First, the platform operates the serving: users choose hardware classes and scaling settings, but never manage servers. Second, the hosted models come from origins other than the platform operator itself — open models published by third parties, community contributions, or models the customer uploaded or fine-tuned. A platform that served only the models it created itself would be a model developer's API, not a hosting platform.

Everything commonly associated with the category — serverless and dedicated serving modes, model catalogs with pricing pages, OpenAI-compatible APIs, autoscaling and scale-to-zero, usage dashboards, fine-tuning — is widespread in current products but is not what makes the product a hosting platform. Older and differently positioned forms (pre-LLM model APIs, community model hubs, curated enterprise catalogs, serverless-only catalogs) all satisfy the same core.

## Users & Context

Primary users:

- **application developers** — integrate model calls into products and features; they want a model, an API key, and a code snippet, and they start on shared pay-per-use serving
- **ML engineers** — productionize models: pick hardware, configure scaling and environments, deploy fine-tuned or custom weights, and keep latency and cost under control
- **AI startups and product teams** — choose among many models as their product evolves, switching models without rewriting applications

Secondary users:

- **model creators** — publish or distribute models so others can run them (on community-style platforms) or sell access to them (on distribution-style platforms)
- **platform/ML platform teams and enterprises** — govern which models may be used, isolate workloads, satisfy data-residency and compliance requirements

The typical context is building and operating AI-powered software: prototype against shared serving, then promote to dedicated capacity as traffic grows; or bring a fine-tuned model from a training workflow and serve it without touching infrastructure.

## Core Model

### The Defining Core

```text
Hosted model (weights + serving runtime, versioned)
└── served on platform-operated compute
    ├── shared serving (pay per use, rate-limited)
    └── dedicated capacity (reserved, capacity-bound)
        └── invoked via API endpoint / playground
            └── metered usage attributed to the caller's account
```

Four properties. If any one is removed, the product is no longer recognizable as a model hosting platform:

- **Hosted model as the central object** — a model (its weights plus a serving runtime) is packaged and run by the platform as an addressable, typically versioned resource that users find in a catalog, deploy, and call. Without this, the product is generic cloud compute or GPU rental, where the unit of deployment is an instance or a container, not a model.
- **Platform-operated serving infrastructure** — inference executes on compute the platform provisions, monitors, and scales. Users configure (hardware class, replica bounds, regions) but do not operate servers. Without this, the product is self-hosting or tooling for running models on infrastructure the user already owns.
- **Invocation surface with metered usage** — an API endpoint (and, in practice, an interactive playground) accepts inputs and returns model outputs; usage is measured and attributed to the caller's account. Without this, the product is a weights repository or a model registry — a catalog of models that nobody can call.
- **Models from origins other than the operator** — the hosted population consists of third-party published models and/or customer-supplied models (uploaded or fine-tuned). The platform is a host and operator, not the model's author. Without this, the product is a model developer serving its own models — a different Application Type.

### Standard Capabilities

Mature products commonly carry most of the following. They are not what makes the product a hosting platform, but they make hosting practical:

- **Model catalog** — the browsable population of models, with per-model detail: capabilities and modalities, context or size characteristics, pricing basis, license and access requirements. Catalogs range from open community publishing (anyone can publish a model others can run) to operator-curated selections.
- **Two serving economics** — shared serving (many customers on pooled capacity, pay per use, subject to rate limits) and dedicated capacity (reserved hardware for one customer, billed by capacity and time, bounded only by the hardware). Mature products expose both through the same API shape, so an application can move from one to the other without code changes.
- **Playground** — an interactive surface (web form or console panel) generated from a model's inputs, for trying a model before writing code.
- **API keys, SDKs, and code snippets** — account-scoped keys; client libraries; ready-to-run examples. An OpenAI-compatible chat-completions surface is a common convergence point, though some products expose their own request schema or several API shapes side by side.
- **Autoscaling with a cold-start tradeoff** — dedicated deployments scale replica count between configured bounds; scaling to zero saves cost but makes the next request pay a start-up delay while weights load. Products document this tradeoff and mitigate it (warm minimum replicas, weight caching, deliberately slow scale-down).
- **Usage and cost visibility** — dashboards and logs of requests, consumed tokens or compute, errors, latency, and spend.
- **Rate limits and quotas** — enforced on shared serving; dedicated capacity removes hard rate limits.
- **Model versioning and lifecycle** — models have versions; updates are published without breaking callers of older versions; platforms document deprecation and migration paths.
- **Fine-tuning and training** — many platforms let users train or fine-tune models on the platform (or upload fine-tuned weights); the result becomes a hosted model deployable like any catalog model.
- **Async execution and webhooks** — long-running generations can be submitted asynchronously and delivered via callback.
- **Organization scoping** — models, keys, deployments, and billing are scoped to a team/organization/project container.

### One Structure, Many Implementations

The core model is written in conceptual terms. Specific products realize each concept differently:

```text
Concept:            Hosted model provenance
Implementations:    third-party open weights, community-published models,
                    customer-uploaded weights, platform-fine-tuned models,
                    (at the hyperscaler edge) the operator's own models alongside others

Concept:            Serving economics
Implementations:    shared per-token API, dedicated per-hour GPU endpoints,
                    provisioned-throughput tiers, batch queues

Concept:            Invocation schema
Implementations:    OpenAI-compatible chat completions, provider-native schemas,
                    platform-native request objects, multiple API shapes side by side

Concept:            Model packaging
Implementations:    platform-managed engine from configuration,
                    customer-packaged containers or model classes
```

A reader who has only seen one implementation (for example, a curated serverless catalog) should still be able to recognize a community model hub or a custom-model deployment platform from the core model.

## How It Works

### Find and try a model

```text
Browse/search the catalog
→ open a model's detail page (capabilities, pricing basis, license, limits)
→ try it in the playground (a form generated from the model's inputs)
→ accept any license or access terms the model requires
```

### Call it from an application

```text
Create an API key
→ point a client library at the platform's endpoint
→ send inputs, receive outputs (streaming where supported)
→ usage is recorded against the account and billed
```

On shared serving there is nothing to provision: the platform keeps popular models warm and starts others on demand. The caller may notice variable start-up latency on rarely used models.

### Move to production capacity

```text
Create a dedicated deployment of the model
→ choose hardware class and scaling bounds (min/max replicas, scale-to-zero window)
→ optionally stage it (development → staging → production environments)
→ the deployment gets a stable endpoint; the application passes it as the model/target
→ traffic can be split across deployments (weighted, A/B, shadow) while the endpoint stays constant
```

The API shape does not change between shared and dedicated serving — the same request that worked against the shared catalog works against the dedicated endpoint. What changes is the economics (per-use vs capacity billing) and the limits (rate-limited vs hardware-bound).

### Bring or make your own model

```text
Fine-tune a hosted base model on the platform, or upload/package custom weights
→ the result becomes a hosted model associated with the user's account
→ deploy and call it exactly like any catalog model
```

Packaging ranges from configuration-only (declare the model, hardware, and engine; the platform builds the serving runtime) to customer-supplied containers or model classes for custom pre/post-processing.

### Operate over time

```text
Monitor deployments (latency, throughput, errors, replica health, cost)
→ adjust scaling bounds or hardware
→ adopt new model versions as they are published
→ plan around deprecation notices for old versions
```

### Pay for what is consumed

Metering follows the workload: text models are commonly billed per token; dedicated capacity per unit of hardware-time; image/video/audio models per output unit or per unit of media. The account (personal, team, or organization) is the billing container.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Model catalog / explore

The discovery surface.

- lists available models, filterable by modality and task
- primary actions: search, open a model's detail page

### Model detail page

The per-model surface.

- capabilities, pricing basis, context/size characteristics, license and access state
- primary actions: open in playground, copy a code snippet, deploy, (on community platforms) view the author and version history

### Playground

An interactive try-it surface.

- input form generated from the model's input schema; output display; often parameter controls
- primary actions: run a request, inspect the raw response, copy code

### Deployment configuration

The production surface for dedicated capacity.

- hardware class, replica bounds, scale-to-zero behavior, region, environment assignment
- primary actions: create/update deployment, split traffic, promote between environments, roll back

### Usage & operations dashboard

The observability surface.

- request logs, token/compute consumption, cost, error and latency views, replica health
- primary actions: inspect a request, export data, set budgets or limits where offered

### API surface

The programmatic surface.

- endpoint URL, API keys, client libraries, code snippets, streaming and async variants

### CLI / management API

A command-line and programmatic management layer for deployments, models, and keys — the form preferred by ML engineers and automation.

### Admin & billing

Organization-level surface: members and roles, keys, spend, and (on enterprise postures) model-access governance and compliance settings.

## Important Rules / Behaviors

### Shared serving is rate-limited; dedicated is capacity-bound

Shared pay-per-use serving is pooled across customers and therefore subject to rate limits and quotas. Dedicated capacity has no hard rate limits — the bound is the hardware and the configured replica ceiling. Moving to dedicated is the standard answer when shared limits bind.

### Scale-to-zero trades cost for first-request latency

A dedicated deployment scaled to zero costs nothing while idle, but the next request waits while weights load and the runtime initializes. Keeping a minimum warm replica removes that delay at a standing cost. Products document this tradeoff explicitly and mitigate cold starts with weight caching and staged scale-down.

### Versions are pinned; deprecation is announced

Calling a model version yields reproducible behavior; new versions are published alongside old ones rather than silently replacing them. Platforms document deprecation and migration paths where models retire, and mature products let callers keep using older versions until they migrate.

### Access to a model can be gated

Some models require accepting a license, agreeing to terms on first use, submitting use-case information, or an explicit subscription step before they can be invoked. Enterprises can additionally restrict which models their identities may use. The gating lives at the model level, above ordinary API-key authentication.

### Metering basis follows the modality

Per-token for text-style models, per unit of hardware-time for dedicated capacity, per output unit or per unit of media for generative image/video/audio models. The same platform commonly mixes several bases.

### Output and request data may be short-lived

Some products delete request inputs/outputs on short retention windows; callers are expected to persist what they need. Retention terms differ between interactive and API-created work in some products.

### The platform operates; the user configures

Users select hardware classes, replica bounds, regions, and environments — but they do not patch servers, install drivers, or manage GPU fleets. Statements of the product's value across the researched sample consistently center on this division of labor.

## Variants

The Type is implemented in several recognizable shapes. A variant remains a variant of this Type as long as the core model above still describes it:

- **Community model hub** — anyone can publish packaged models; others discover and run them; private models and team organizations supported (e.g. Replicate)
- **Open-weights inference cloud** — a curated, fast-moving catalog of third-party open models with serverless and dedicated serving and fine-tuning (e.g. Together AI, Fireworks AI)
- **Custom-model deployment platform** — emphasis on bringing your own weights or code, packaging via CLI/containers, with environments and promotion pipelines (e.g. Baseten)
- **Hyperscaler enterprise catalog** — multi-provider foundation-model catalog inside a large cloud account, with model-access governance, regional controls, and compliance postures (e.g. Amazon Bedrock)
- **Training-integrated hosting** — training/fine-tuning jobs whose checkpoints deploy directly into the same hosting stack (present in several of the above)

When a variant's center of gravity moves away from hosting models — for example, to building applications on top of model APIs, or to routing traffic between providers — it is drifting toward a different Application Type (LLM Application Development Platform, AI Gateway).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Model API Platform | a model developer serving its own models as the product; a hosting platform hosts models whose creation it does not own (the two converge at the hyperscaler edge, where one product serves its own and third-party models side by side) |
| AI Gateway / Model Routing Platform | an intermediary on the model request path; it runs no inference and routes to hosting platforms and model APIs as upstreams |
| Model Registry | catalogs and governs model versions within an ML lifecycle; it does not operate serving |
| Machine Learning Platform / MLOps Platform | spans the full model lifecycle (data, training, pipelines, deployment, monitoring), often over user-owned infrastructure; hosting centers on operating serving for consumption |
| Serverless Management Platform / GPU cloud | the unit of deployment is a function, container, or instance — not a model with catalog semantics (weights, versions, licenses, per-token pricing) |
| LLM Application Development Platform | builds applications on top of hosted model APIs (orchestration, prompts, RAG, agents); hosting sits beneath it |
| AI Model Evaluation Platform | measures and compares models as its central record; hosting serves them (hosting platforms may bundle catalog guidance/benchmarks, but evaluation is not their operating core) |

The most important boundary is with the **Model API Platform**: both expose models through metered APIs, and the test is model provenance — who authored the hosted models relative to the platform operator. The cleanest structural split is with the **AI Gateway** (intermediary vs upstream) and the **weights repository/registry** (catalog without serving vs catalog with serving).

## Representative Products

- Replicate — community model hub + custom model packaging; prediction-centric API
- Together AI — open-weights cloud; serverless + dedicated model inference + fine-tuning
- Fireworks AI — speed/cost-focused open-model platform; serverless + on-demand deployments
- Baseten — production model-serving platform; hosted model APIs + dedicated deployments + training
- Amazon Bedrock — hyperscaler managed hosting of a multi-provider foundation-model catalog

The core model was checked against older and differently positioned forms (pre-LLM model APIs, community hubs, curated-only catalogs, serverless-only catalogs, weights repositories, GPU clouds) to avoid over-fitting to the current LLM-era bundle.

## Sources

Research date: **2026-09-06**

Primary vendor documentation:

- Replicate — How does Replicate work?: https://replicate.com/docs/reference/how-does-replicate-work
- Replicate — Deployments: https://replicate.com/docs/topics/deployments
- Together AI — Available models (serverless): https://docs.together.ai/docs/serverless-models
- Together AI — Dedicated model inference (overview + concepts): https://docs.together.ai/docs/dedicated-endpoints , https://docs.together.ai/docs/dedicated-endpoints/concepts
- Fireworks AI — docs root: https://docs.fireworks.ai/
- Fireworks AI — Deployments quickstart: https://docs.fireworks.ai/getting-started/ondemand-quickstart
- Baseten — overview: https://docs.baseten.co/
- Baseten — How Baseten works: https://docs.baseten.co/concepts/howbasetenworks
- Amazon Bedrock — What is Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- Amazon Bedrock — Model availability & compatibility: https://docs.aws.amazon.com/bedrock/latest/userguide/models.html
- Amazon Bedrock — Request access to models: https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html

> Sourcing limitation: Hugging Face documentation was unreachable from the research environment on 2026-09-06 (repeated timeouts) and was dropped from the sample; the community-hub shape of the Type is covered through Replicate's documentation instead. Fireworks evidence is limited to its documentation root and deployments quickstart; Bedrock custom-weight import was not verified. Numeric prices, limits, and default settings observed in vendor docs are intentionally not stated in this document; they are recorded, where relevant, in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
