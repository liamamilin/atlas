# AI Gateway / Model Routing Platform

## Overview

An **AI Gateway / Model Routing Platform** is an intermediary layer that sits between client applications and AI model provider APIs. Applications send their model requests to the gateway instead of directly to model providers; the gateway understands model API traffic, executes each request against an upstream model provider chosen by the gateway's own configuration, and returns the response — recording what happened along the way.

The defining core is small:

```text
Client application
  → model request directed to the gateway
    → gateway resolves its configuration (which provider/model, which credentials, which policy)
      → request executed against an upstream model provider API
        → response returned to the client
```

Three properties make the Type what it is:

- **Intermediary position** — the gateway is on the request path. Applications point at it (a base-URL swap, a gateway URL, a routing header); providers are reached only by the gateway.
- **Model-aware traffic handling** — the gateway understands model API semantics: model identifiers, prompt/message bodies, token usage, provider-specific schemas. This is what separates it from a generic HTTP reverse proxy.
- **Gateway-side execution decision** — which upstream serves each request is decided by the gateway's configuration and policy, applied uniformly across all applications, not hard-coded in each client. In the simplest case that decision is a single fixed upstream; in the mature case it is a routing rule with fallbacks, load balancing, and conditions.

Everything else the market associates with the category — the OpenAI-compatible unified API, provider credential custody, virtual API keys, fallback chains, cost dashboards, budgets, caching, guardrails — is standard capability layered on that core, not the definition. A gateway that fronts a single provider, passes provider keys through untouched, and keeps no logs is still recognizably this Type; a product that serves model inference itself, or routes generic HTTP without model semantics, is not.

## Users & Context

Primary users are technical:

- **Application / AI engineers** integrating model calls into products. They point an existing model client at the gateway (often a one-line base-URL change) and keep writing the same request code.
- **Platform / infrastructure teams** operating model access for an organization. They register providers and credentials once, issue per-team access, set budgets and rate limits, and rotate provider keys without touching application code.
- **Engineering leadership and finance-adjacent roles** consuming the visibility side: usage, spend, and error dashboards aggregated across teams and providers.

Typical context: an organization with more than one application calling more than one model provider, where teams otherwise each hold their own provider keys, hard-code provider endpoints, and duplicate retry logic. The gateway is the response to that fragmentation: one place where provider access, routing behavior, spending limits, and usage records live.

A secondary, newer context is agent and coding-agent traffic: teams route the model calls of agents and AI developer tools through the same gateway to get the same credential, budget, and logging control.

## Core Model

The gateway's world consists of a small set of objects arranged along the request path:

```text
Caller (application / team, authenticated by a gateway-issued key)
  → Model route (gateway-facing model name)
      → resolves through Routing configuration
          → one or more Provider targets
              (upstream provider API + credential + deployment)
  → Policy controls applied on the way (cache, guardrails, rate & budget limits)
  → Request record (outcome, tokens, cost, latency)
```

- **Provider connection** — a configured upstream: a model provider API plus the credential used to call it (stored at the gateway, referenced from an external secret manager, supplied per request by the caller, or replaced by the platform's own billing). This is the object that lets an organization rotate provider keys centrally instead of in every application.
- **Model route / catalog entry** — a gateway-facing model name that applications request. It may map to one physical provider model, to several deployments of the same model (a pool for load balancing), or to an ordered set of different models (a fallback chain). The name the client sends is the gateway's name, not the provider's.
- **Routing configuration** — the executable decision logic attached to a route: which target first, what to do on failure (retry, then fall back to which targets), how to distribute traffic (weights across deployments or keys), and under which conditions to deviate (user segment, request metadata, cost or latency rules). In some products this is a declarative config file; in others a visual, versioned flow; in others a set of entities in a control plane. Conceptually it is the same thing: the per-request upstream decision, owned by the gateway.
- **Caller identity** — the gateway authenticates applications with its own credentials (issued keys, tokens, or identity-provider integration), and those identities carry entitlements: which models may be called, how much may be spent, how fast. This is the layer that turns the gateway from a proxy into a governance point.
- **Policy controls** — checks applied on the path: response caching, content guardrails, rate limits, and budget limits that can reject a request or divert it to a fallback target when exceeded.
- **Request record** — the per-request log of what happened: which route and target served it, token usage, computed cost, latency, error or fallback outcome. Aggregated, these records become the usage, spend, and health analytics that justify the gateway's existence.

Two relationships organize everything: **routes resolve to provider targets through routing configuration**, and **callers are entitled through their identity, not through the providers**. An application never holds a provider relationship; it holds a gateway relationship.

### Concept vs implementation

The core model is conceptual; products implement each piece differently:

```text
Concept:            Access surface
Implementations:    OpenAI-compatible endpoint (drop-in base-URL swap),
                    provider-schema passthrough endpoints,
                    multi-format universal API (OpenAI and Anthropic request
                    formats translated to any provider)

Concept:            Provider credential handling
Implementations:    credentials stored at the gateway,
                    references to external secret managers,
                    bring-your-own-key stored with the platform,
                    per-request pass-through of the caller's own key,
                    platform-billed usage (caller holds no provider key)

Concept:            Routing configuration
Implementations:    declarative config files, JSON config objects,
                    versioned visual route flows, control-plane entities

Concept:            Request record
Implementations:    spend logs in a database, request logs with traces,
                    dashboard analytics, OpenTelemetry / metrics export
```

A reader who has only seen one form — say, a self-hosted proxy with a config file — should still be able to recognize a managed edge gateway or an API-gateway product extended with AI entities as the same Type.

## How It Works

### Set up the gateway

```text
Register provider connections (provider API + credentials)
→ define model routes (gateway-facing names → targets)
→ attach routing behavior (fallbacks, load balancing, conditions)
→ issue caller keys / connect identity provider
→ set budgets, rate limits, caching, guardrail policies
```

This is operator work, done once per provider and maintained as providers change. The payoff claim of the whole Type is concentrated here: change providers, rotate keys, or reroute traffic by editing gateway configuration — not application code.

### Serve a model request

```text
Application sends a model request to the gateway
(name it a gateway model route; authenticate with a gateway key)
→ gateway authenticates the caller and checks entitlements
→ gateway resolves the route's configuration to a target
→ policy checks on the way in (cache lookup, guardrails, rate/budget limits)
→ gateway transforms the request into the target provider's schema
→ upstream call; on failure: retry, then next target in the fallback chain
→ response returned to the client (normalized or as the provider sent it)
→ request recorded (route, target, tokens, cost, latency, outcome)
```

The loop is per-request and stateless from the client's perspective: the client asked for a model and got a response; whether it was served from cache, by the first-choice provider, or by the third fallback is visible in the gateway's records, not in the client's code.

### Operate and govern

```text
Inspect logs and analytics (requests, tokens, spend, errors, cache hits)
→ adjust routing (add a fallback, shift traffic, canary a new model)
→ manage access (issue/revoke keys, change model entitlements)
→ enforce spend (budgets, rate limits, per-team caps)
→ rotate provider credentials without touching applications
```

Operation is continuous: providers change pricing and availability, models are replaced, teams grow. The gateway's management surface — admin UI, control plane, configuration-as-code, management APIs — is where that work happens.

### Capability tiers

**Defining core** — without these, not an AI gateway:

- intermediary position on the model request path
- model-aware request handling (schemas, model names, token usage)
- gateway-side execution decision (configured upstream selection)

**Standard capabilities** — present in essentially all mature products:

- unified / OpenAI-compatible access surface
- provider/model catalog with gateway-facing model names and aliases
- provider credential custody or explicit BYOK handling
- retries and fallback across providers/models (some products distinguish failure classes — such as context-window overflow, content-policy rejection, or rate limiting — and route each to a different fallback)
- load balancing across deployments, keys, or providers
- per-request logging and usage analytics (requests, tokens, cost, errors, latency)
- spend tracking and attribution per key/team/application
- budgets and rate limits enforced at request time
- response caching (exact and semantic)
- guardrail hooks (content filtering, sensitive-data handling)
- admin/management surface plus management APIs or configuration-as-code
- team- or segment-scoped access organization
- observability export (OpenTelemetry, metrics, log export)

**Optional / variant** — depends on product and segment:

- delivery form: self-hosted open-source proxy, managed SaaS, platform-bundled edge gateway, API-gateway product extended with AI entities, control-plane-plus-data-plane architecture
- schema posture: strict OpenAI compatibility, multi-format universal API, provider-schema passthrough
- credential and billing posture: custody vs BYOK vs pass-through vs platform-billed usage
- extended traffic: MCP tool traffic, agent-to-agent traffic, AI developer-tool proxying, non-chat provider APIs (embeddings, image, speech, rerank, batch, fine-tuning)
- advanced routing: semantic or complexity-based model selection, percentage splits and canary rollouts, traffic mirroring, request prioritization
- enterprise governance: organization/workspace hierarchies, SSO/SCIM, audit logs, key-management and secret-manager integration, locked-down "admin-curated only" modes, regional/data-residency deployments

## Interfaces

### Inference endpoints

The surface applications call.

- Purpose: accept model requests in a schema the client already speaks.
- Typical forms: an OpenAI-compatible chat-completions endpoint (the dominant integration — existing model clients work by changing the base URL), provider-specific passthrough endpoints that preserve each provider's own API shape while adding gateway features, and in some products a multi-format universal endpoint that accepts several vendors' request formats and translates.
- Primary actions: send a model request (chat, embeddings, and in some products image/audio/batch), stream the response, attach request metadata.

### Management / admin surface

The operator's console (web UI, control plane, or both).

- Purpose: configure and govern everything the request path consumes.
- Typical information: provider connections and credential status, model routes and their targets, caller keys and their entitlements, budgets and rate-limit state, request logs, usage and spend analytics.
- Primary actions: register providers, define routes and routing rules, issue and revoke keys, set budgets/limits, inspect and export logs, rotate credentials.

### Configuration-as-code

- Purpose: manage gateway configuration declaratively alongside other infrastructure.
- Typical forms: config files (model lists, router settings), JSON routing configs, declarative entity definitions applied via CLI or API.
- Primary actions: define models/targets/fallbacks, version and apply changes, roll back.

### Logs & analytics

- Purpose: turn the request path into visibility.
- Typical information: per-request records (route, target, tokens, cost, latency, fallback outcome), aggregate dashboards (usage, spend, errors, cache hit share), export pipelines (OpenTelemetry, metrics, log export, query APIs).
- Primary actions: filter and inspect requests, build spend/usage views, export to external observability tooling.

## Important Rules / Behaviors

- **Provider credentials are a gateway concern.** Applications authenticate to the gateway with gateway-issued identities; provider keys live at the gateway (or are explicitly delegated via BYOK or per-request pass-through). This separation is what makes central rotation and offboarding possible.
- **Model names are gateway-defined.** A requested model name resolves through the gateway's catalog and routing configuration; it may be an alias, a pool of deployments, or a fallback chain. Clients cannot bypass this by naming a provider model directly unless the gateway is deliberately configured in pass-through mode.
- **Failure is handled inside the gateway.** The standard sequence is retry within the chosen target, then move down the configured fallback chain; persistently failing targets are taken out of rotation (cooldown or circuit-breaking) until they recover. Fallbacks can be error-class-aware — a context-window overflow or a content-policy rejection can route differently from a rate-limit error.
- **Fallbacks respect governance.** In mature products, a caller's model entitlements can be enforced on fallback targets too — a key that may not call a model directly will not reach it via failover either (this can be configurable).
- **Budgets and rate limits bind at request time.** When a budget or quota is exhausted, the gateway rejects the request or diverts it to a cheaper fallback target; enforcement happens on the path, not in a nightly report.
- **Cache can answer without the provider.** Cached responses (exact or semantic) are served from the gateway, which is both a latency and a cost behavior, and shows up in analytics as a distinct outcome.
- **Logging scope is a policy decision.** What the gateway stores about each request (bodies, metadata, nothing) is configurable in serious products, because prompt traffic is sensitive. The routing and enforcement functions do not depend on full body logging.
- **Streaming is preserved.** Responses stream through the gateway; the gateway meters and records without buffering the client experience.
- **The gateway is not the model.** It serves no inference of its own (beyond cache). Its upstreams are provider APIs — public model providers, cloud-managed model services, or self-hosted inference endpoints, all of which are just targets.

## Variants

- **Self-hosted open-source proxy** — deployed next to the applications it serves; configuration as files; governance features (SSO, audit, rotation) often gated behind a paid tier.
- **Managed SaaS gateway** — a hosted endpoint plus a web control plane; the operator configures, the vendor runs. May bill usage (at pass-through prices) or leave provider billing with the customer's own keys.
- **Platform-bundled edge gateway** — a gateway as a feature of a broader infrastructure platform; value concentrated in observability, caching, rate limiting, and simple fallbacks at the platform's edge.
- **API-gateway lineage** — a generic API-gateway product extended with AI entities and policies; strongest where model traffic must share one governance plane with the rest of the organization's API traffic.
- **Control-plane + data-plane product** — central management with enforcement nodes deployed in the customer's environment (self-hosted, Kubernetes, or provider-hosted); the enterprise form.
- **Scope expansions** — the same intermediary pattern extended to MCP tool traffic, agent-to-agent traffic, and AI developer tools; increasingly common, treated here as scope variants rather than a separate Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Model API Platform | the thing routed to | serves model inference and owns the models; the gateway owns no models and only intermediates. Managed unified-API gateways drift toward aggregation but remain intermediaries (BYOK, pass-through pricing, provider failover) |
| API Gateway Management Console (generic API gateway) | adjacent, different semantics | routes generic HTTP to services; lacks model awareness (token metering, prompt inspection, model-level fallback). An AI gateway is defined by model-aware handling — vendors extend generic gateways into this Type by adding exactly that |
| LLM Observability Platform | feeds and overlaps | observability platforms center on trace inspection and quality analysis and ingest from anywhere; the gateway's logging is a byproduct of being on the path. Products bundle both; the center of gravity differs |
| AI Cost / FinOps Platform | feeds and overlaps | FinOps platforms aggregate and attribute AI spend across tools; the gateway enforces spend at the request path and produces the raw usage records. Budget enforcement at the gateway is the shared zone |
| AI Safety / Guardrail Platform | capability overlap | guardrails appear as bundled capabilities inside gateways and as standalone platforms; the standalone Type centers policy checks, not routing |
| AI Model Hosting Platform | different layer | hosting serves model inference (often customer-deployed models); the gateway routes to hosted endpoints as one more upstream |
| LLM Application Development Platform | different layer | dev platforms center on building LLM applications (SDKs, orchestration, prompts); the gateway is the runtime access and routing layer beneath them. Some products span both (SDK + proxy) |
| Agent Orchestration Platform | different coordinated unit | orchestrates tasks and messages between agents; the gateway routes individual model calls. Agent-era products increasingly touch both |

The two most important boundaries: against the **model API platform** (who owns the models — nobody confuses a provider's own API with the layer in front of it) and against the **generic API gateway** (model-awareness — the ability to understand prompts, meter tokens, and fail over by model is what makes this a distinct Type rather than a configuration of an existing one).

## Representative Products

- **LiteLLM (AI Gateway / Proxy)** — open-source unified interface and self-hosted OpenAI-compatible gateway; virtual keys, budgets, spend tracking, routing and fallbacks; enterprise tier for SSO/audit.
- **Portkey (PRISMA AIRS AI Gateway)** — gateway product company: universal API, config-driven routing (fallbacks, load balancing, conditional), caching, guardrails, logs/traces/analytics, organization/workspace governance; open-source gateway plus managed control plane.
- **Cloudflare AI Gateway** — platform-bundled edge gateway: provider passthrough plus OpenAI-compatible and unified endpoints, BYOK or pass-through credentials, analytics, caching, rate limiting, versioned dynamic routes.
- **Kong AI Gateway** — API-gateway lineage: AI Model/Provider entities, consumer groups with token budgets, AI policies (semantic cache, prompt guards, cost management), control plane plus self-hosted data plane.
- **Vercel AI Gateway** — managed unified API: one key across providers, automatic provider failover, budgets and spend monitoring, pass-through token pricing.

The sample deliberately spans delivery forms (self-hosted OSS, gateway vendor, platform-bundled, API-gateway incumbent, managed dev-platform) and customer levels (individual developer to enterprise platform team); the defining core was checked against the degenerate forms (single-provider passthrough, credential pass-through, no-control-plane operation) so the definition does not over-fit today's dominant bundle.

## Sources

Research date: **2026-09-06**

- LiteLLM — Getting Started: https://docs.litellm.ai/docs/
- LiteLLM — Routing & Load Balancing: https://docs.litellm.ai/docs/routing-load-balancing
- LiteLLM — Virtual Keys: https://docs.litellm.ai/docs/proxy/virtual_keys
- LiteLLM — Fallbacks (Provider Failover): https://docs.litellm.ai/docs/proxy/reliability
- Portkey — What is Portkey: https://docs.portkey.ai/
- Portkey — AI Gateway: https://docs.portkey.ai/docs/product/ai-gateway
- Portkey — Configs: https://docs.portkey.ai/docs/product/ai-gateway/configs
- Cloudflare AI Gateway — Overview / Get started / Dynamic routing / Analytics: https://developers.cloudflare.com/ai-gateway/
- Kong AI Gateway — Overview: https://docs.konghq.com/gateway/latest/ai-gateway/
- Vercel AI Gateway — Overview: https://vercel.com/docs/ai-gateway

> Sourcing limitations: Kong's documentation subpages (load balancing, AI Model entity reference) were unreachable on the research date (repeated 404s), so Kong-level mechanics are asserted only at its overview-page level. Vercel evidence is root-documentation level. Vendor performance figures (latency, uptime, request volumes) observed in vendor docs were deliberately excluded from this document. Precise product limits, defaults, and pricing details are intentionally not stated; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
