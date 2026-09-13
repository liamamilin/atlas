# Research Notes — AI Gateway / Model Routing Platform

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (update-v1)

## Research Goal

Understand what an "AI Gateway / Model Routing Platform" actually is as an Application Type: what sits where in the request path, what objects it manages, what "model routing" concretely means, how it is governed and observed, and where its boundary lies against the neighboring §13 Types (Model API Platform, LLM Observability, AI Cost/FinOps, Guardrail Platform, AI Model Hosting, LLM Application Development Platform) and against the generic API Gateway (§12).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: an intermediary layer between applications and AI model provider APIs. Applications send model requests to the gateway; the gateway executes each request against a configured upstream provider (with retries/fallbacks/load balancing), applies policy (auth, budgets, rate limits, caching, guardrails), and records usage.
- Likely confusions: Model API Platform (the provider's own serving API), generic API Gateway (§12), LLM Observability Platform, AI Cost / FinOps Platform, AI Model Hosting Platform.
- Known cross-reference: research/ai-cost-finops-platform.md already frames the gateway as "a runtime control plane (routing, fallback, credentials); cost visibility is a byproduct" and research/agent-orchestration-platform.md frames it as "routes model calls, not agent tasks". This pass tests those framings from the gateway side.

## Research Questions

1. What is the central request path, and who points at whom (client → gateway → provider)?
2. What objects does the gateway manage (providers, models, credentials, keys, configs/routes, budgets, logs)?
3. What does "routing" mean concretely — fallbacks, load balancing, conditional rules, semantic/complexity routing?
4. What access surface does it expose (OpenAI-compatible universal API, provider-schema passthrough, multi-format)?
5. How are provider credentials handled (custody vs BYOK vs pass-through)?
6. How is usage governed (virtual keys, budgets, rate limits, teams/workspaces) and observed (logs, analytics, cost)?
7. What is bundled vs standalone (caching, guardrails, MCP/agent traffic)?
8. What delivery forms exist (self-hosted OSS proxy, managed SaaS, edge-bundled, API-gateway plugin, control plane + data plane)?
9. Where are the boundaries vs the neighboring Types listed above?
10. Would a degenerate/older form (single-provider passthrough proxy; AI plugins inside a generic API gateway) still satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy | Customer level | Evidence quality |
|---|---|---|---|
| LiteLLM (AI Gateway / Proxy) | open-source developer-first proxy + SDK; self-host | individual devs → platform teams → enterprise tier | Tier-1 docs, multiple pages fetched |
| Portkey (now branded PRISMA AIRS AI Gateway) | gateway product company: routing + observability + guardrails + governance control plane | devs → enterprise (orgs/workspaces/SSO/SCIM) | Tier-1 docs, multiple pages fetched |
| Cloudflare AI Gateway | platform-native edge gateway bundled into a hyperscaler account; passthrough-first | individual devs → enterprise (free feature) | Tier-1 docs, multiple pages fetched |
| Kong AI Gateway | API-management incumbent extending a generic gateway with AI entities/policies | enterprise platform/infra teams | Tier-1 landing page only (subpages 404) |
| Vercel AI Gateway | managed unified API from a dev-platform vendor; usage-billed pass-through pricing | devs on a dev platform | Tier-1 docs root page |

Also considered and not sampled: OpenRouter (aggregator; likely on the Model API Platform side of the boundary — not fetched, see Uncertainties), TrueFoundry, Helicone (already sampled in the ai-cost-finops pass as observability+gateway), AWS Bedrock/Azure AI Foundry (model platforms, not gateways).

## Sources

All fetched 2026-09-06 unless noted.

- LiteLLM — Getting Started: https://docs.litellm.ai/docs/
- LiteLLM — Routing & Load Balancing index: https://docs.litellm.ai/docs/routing-load-balancing
- LiteLLM — Virtual Keys: https://docs.litellm.ai/docs/proxy/virtual_keys
- LiteLLM — Fallbacks (Provider Failover): https://docs.litellm.ai/docs/proxy/reliability
- Portkey — What is Portkey: https://docs.portkey.ai/
- Portkey — AI Gateway: https://docs.portkey.ai/docs/product/ai-gateway.md
- Portkey — Configs: https://docs.portkey.ai/docs/product/ai-gateway/configs.md
- Portkey — docs index (llms.txt): https://docs.portkey.ai/docs/llms.txt and https://docs.portkey.ai/docs/_llms/latest/docs.md
- Cloudflare AI Gateway — Overview: https://developers.cloudflare.com/ai-gateway/
- Cloudflare AI Gateway — Get started: https://developers.cloudflare.com/ai-gateway/get-started/
- Cloudflare AI Gateway — Dynamic routing: https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/
- Cloudflare AI Gateway — Analytics: https://developers.cloudflare.com/ai-gateway/observability/analytics/
- Kong AI Gateway — Overview: https://docs.konghq.com/gateway/latest/ai-gateway/
- Vercel AI Gateway — Overview: https://vercel.com/docs/ai-gateway

Source-access limitations:
- Kong subpages (/ai-gateway/load-balancing/, /ai-gateway/entities/ai-model/, /ai-gateway/llms.txt) returned 404 on 2026-09-06 (3 distinct URL patterns tried). Kong evidence is landing-page level; entity-level mechanics (AI Model entity fields, load-balancing algorithms) are NOT asserted.
- OpenRouter docs not fetched (time budget); aggregator-side boundary claims kept at positioning level only.
- LiteLLM /docs/proxy/getting_started 404'd; equivalent content obtained from /docs/ root page.
- Vendor performance claims (Portkey latency ms, request volumes, uptime) observed in docs but excluded as marketing numbers.

## Product Observations

### LiteLLM (evidence layer A unless noted)

Positioning: "open-source library that gives you a single, unified interface to call 100+ LLMs (OpenAI, Anthropic, Vertex AI, Bedrock, and more) using the OpenAI format." Two forms: Python SDK (in-process) and "LiteLLM AI Gateway (Proxy)" — a self-hosted OpenAI-compatible gateway; "Any client that works with OpenAI works with the proxy, with no code changes" (base_url swap; `api_key="anything"`).

- Unified schema: every response follows the OpenAI Chat Completions format regardless of provider; provider errors mapped to OpenAI exception types.
- Model configuration: `model_list` in config.yaml — each entry = model_name (gateway-facing alias) + litellm_params (provider-specific model, api_base, api_key, rpm...). Multiple deployments can share one model_name (a model group). Wildcard routing (`azure/*`) proxies all models of a provider.
- Routing (Router): load balancing across deployments; retries (`num_retries`); timeouts; cooldowns (`allowed_fails`, `cooldown_time`); fallbacks in order between model groups; three fallback classes — general, `context_window_fallbacks`, `content_policy_fallbacks`; pre-call checks (context-window enforcement, EU-region filtering by deployment region); health-check-driven routing (background checks remove unhealthy deployments proactively); budget routing; tag-based routing; auto routing (beta: complexity/semantic classification → pinned model / random pool / Thompson-sampled pool); request prioritization (beta).
- Fallback governance: `enforce_fallback_model_access` — a key not allowed to call the fallback model skips it; per-request/per-key `disable_fallbacks`; fallback attempts recorded in spend logs (`attempted_fallbacks`, `original_model_group`).
- Access & governance: virtual keys (`sk-...`) minted via `/key/generate` against a Postgres DB; master key = admin; keys carry model allow-lists, `max_budget`, `tpm_limit`, `rpm_limit`, expiry, aliases (map a requested model name to another group — upgrade/downgrade); users, teams, roles (proxy_admin, org_admin, internal_user, team, customer); OIDC/JWT auth; key block/unblock; key rotation (enterprise, with grace period); IP filtering; audit logs (enterprise).
- Spend tracking: per key/user/team, computed via `completion_cost()` from a model price table; spend logs table; budget resets.
- Bundled capabilities: caching, guardrails (content filtering, PII masking), logging/alerting/metrics, observability callbacks (Langfuse, MLflow, Helicone, OTel), secret managers, admin UI.
- Expansion: "Agent & MCP Gateway" — one endpoint for LLMs, A2A agents, and MCP tools; enterprise quickstart covers LLM+MCP+Agent gateway.
- Enterprise: SSO/SAML, audit logs, spend tracking, multi-team management.

### Portkey (evidence layer A unless noted)

Positioning: "unified interface for interacting with over 250 AI models, offering advanced tools for control, visibility, and security." Integration: point the OpenAI SDK at `PORTKEY_GATEWAY_URL` with Portkey headers (provider slug + Portkey API key), or use the Portkey SDK, or raw REST to `api.portkey.ai/v1/chat/completions`. Gateway is open source (`npx @portkey-ai/gateway`) and can be self-hosted/hybrid; managed control plane adds logs, governance, workspaces.

- Universal API: "One API for 200+ LLMs across every major provider. Use OpenAI's Chat Completions, Responses API, or Anthropic's Messages format — Portkey translates between them all."
- Routing via Configs: "a configuration is a JSON object that can be used to define routing rules for all the requests coming to your gateway." Strategies: `fallback`, `loadbalance`, conditional routing; targets reference virtual keys (`@openai-prod` slugs) and can carry `default_params` / `override_params` / `drop_params` (request-body shaping before forwarding, with wildcard paths). Passthrough targets defer provider resolution to the request (header or `@slug/model` in the model field). Configs attachable per request (header/SDK param) or as a default config on an API key (governance without code changes).
- Reliability features: automatic retries (exponential backoff), circuit breaker (stop routing to unhealthy targets until recovery), request timeouts, canary testing, load balancing across API keys "to counter rate-limits".
- Cache: simple & semantic.
- Model Catalog (replacing deprecated Virtual Keys): "a single pane to view and manage every AI provider and model in your organization... centralized governance, discovery, and usage controls"; Integrations = "securely store and manage AI provider credentials"; budget limits & rate limits per integration; custom models; pricing adjustments/discount multipliers; secret references to external secret managers (AWS Secrets Manager, Azure Key Vault, Vault); KMS encryption.
- Observability: logs ("chronological list of all the requests processed through Portkey"), traces, analytics, cost management, budget limits; OTel export (GenAI semantic conventions); log export; configurable request logging (what is stored).
- Guardrails: checks on requests & responses, PII redaction, bring-your-own guardrails via webhooks; org/workspace-level enforced guardrails.
- Administration/governance: organizations → workspaces → roles; API keys with default configs; "Enforcing Saved-Only Resources" — lock the gateway to admin-curated providers/configs/integrations, rejecting inline provider configuration at request time; enforce budget/rate limits at key and workspace level; SSO, SCIM, audit logs.
- Expansion: MCP Gateway (registry, access control, guardrails for tool calls), Agent Gateway (A2A), Coding Agents page ("governance layer for Claude Code, Codex... centralized credentials, cost controls, observability, and provider failover for platform teams"), gateway-to-other-APIs (rerank, video, listen), realtime API, batch inference, fine-tuning passthrough, custom hosts (privately hosted or local models).
- Branding: docs banner "Portkey is now PRISMA AIRS AI Gateway" (Palo Alto Networks) — observed, not researched further.

### Cloudflare AI Gateway (evidence layer A unless noted)

Positioning: "Observe and control your AI applications... gain visibility and control over your AI apps... analytics and logging... caching, rate limiting, as well as request retries, model fallback, and more. Better yet - it only takes one line of code to get started." A gateway is a named account-scoped object; auto-created on first authenticated request (`cf-aig-gateway-id: default`).

- Access surfaces (three): (1) provider-specific endpoints `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/{provider}` that "maintain the original provider's API schema while adding AI Gateway features" (passthrough); (2) an OpenAI-compatible endpoint (`/compat/chat/completions`; deprecated for standard single-model calls but required for dynamic routes); (3) a unified REST API on api.cloudflare.com ("Call any model... through the same Cloudflare API. No provider SDKs or API keys needed — authentication and billing are handled through your Cloudflare account").
- Provider authentication (three modes): Unified Billing (prepaid AI Gateway credits for Workers AI and supported third-party providers), BYOK ("Store your own provider API Keys with Cloudflare, and AI Gateway will include them at runtime"), or request headers (client passes the provider key through; gateway holds nothing).
- Dynamic routing: named, versioned routes used in place of the model name (`dynamic/support`); node graph — Start, Conditional (if/else on request body/headers/metadata, e.g. `user_plan == "paid"`), Percentage (probabilistic split for A/B and gradual rollouts), Model (call a provider/model), Rate Limit, Budget Limit (switch to fallback when exceeded), End; metadata = arbitrary key-value context attached by the app; versions with instant rollback; visual editor or JSON.
- Observability: analytics (requests, token usage, costs, errors, cached-response percentage) filterable by time, in dashboard or via GraphQL; logging of requests and errors.
- Features: caching ("Serve requests directly from Cloudflare's cache instead of the original model provider"), rate limiting, request retry + model fallback, custom metadata.
- Providers: Workers AI (Cloudflare's own inference), Anthropic, Google Gemini, OpenAI, Replicate, AWS Bedrock, Azure OpenAI, and more.
- Billing posture: free platform feature; Workers AI billing modes (standard vs unified prepaid credits).

### Kong AI Gateway (evidence layer A; landing-page level only)

Positioning: "Connectivity and governance layer for modern AI-native applications... a high-performance control plane that secures, governs, and observes AI-native systems end to end. Whether serving LLM traffic, exposing structured context via MCP, or coordinating agents through A2A."

- Architecture: Konnect-hosted control plane + data plane nodes (self-hosted, cloud, or Kubernetes); on-prem mode on self-hosted Kong Gateway; managed via Konnect UI, AI Gateway API, or `kongctl` CLI (decK for on-prem).
- Three traffic types with "unified control": LLM, MCP, A2A — "Define a single endpoint for any traffic type... Configure these entities once, then govern them from a unified control plane with built-in auth, policy enforcement, and observability."
- Entity model (v2; migrated from v1 AI Proxy/AI Proxy Advanced plugins): AI Model ("defines the upstream provider, model name, and routing behavior"), AI Model Provider ("Centralize LLM provider credentials in one place and rotate them without touching every team's configuration"), AI Consumer Group ("Scope model access and token budgets by team or department"), AI Prompt Template, AI Auth Strategies, AI MCP Server, AI Consumers.
- Policies: AI Semantic Cache, AI Prompt Compressor, Model cost management + AI Rate Limiting Advanced ("Calculate the true cost of each request... and enforce spend limits against it"), AI Prompt Guard / AI Semantic Prompt Guard / AI Sanitizer (PII redaction) / AI Semantic Response Guard, delegation to cloud trust services (AI AWS Guardrails, AI Azure Content Safety, AI GCP Model Armor).
- Routing: "Routing and load balancing across AI providers"; "Automatically fail over to a different provider or model when one is slow or unavailable" (mechanics not verified — subpages 404).
- Boundary evidence (vendor's own FAQ): "Why should I use AI Gateway instead of adding the LLM's API behind Kong Gateway? If you just add an LLM's API behind Kong Gateway, you can only interact at the API level... With AI Gateway AI Policies and runtime components, Kong Gateway can understand the prompts that are being sent through the gateway. AI Policies can inspect the body and provide more specific AI capabilities."
- Observability: audit logs, metrics exporters, OpenTelemetry (GenAI OTLP span attributes and metrics), Konnect dashboards (requests, tokens, errors, latency).
- Monetization surface: metering and billing ("Track token usage and automate invoicing based on prompt and response volume"), tiered AI budgets via identity claims.
- Also proxies AI CLI tools (Claude Code, Codex CLI, Qwen Code) for centralized control.

### Vercel AI Gateway (evidence layer A; root page only)

Positioning: "Build agents and AI applications through one API. AI Gateway routes requests, manages fallbacks and budgets, monitors usage, and connects supported coding agents."

- Access: one API key, hundreds of models; endpoints for OpenAI Chat Completions, OpenAI Responses, Anthropic Messages; AI SDK and framework integrations; `https://ai-gateway.vercel.sh/v1/chat/completions`.
- Reliability: "Automatically retries requests to other providers if one fails"; provider options for "routing, fallbacks, and provider preferences"; routing rules (changelog).
- Economics: "No markup on tokens. Tokens cost the same as they would from the provider directly, with zero markup, including with Bring Your Own Key (BYOK)"; usage and billing pages; auto-recharge; spend monitoring.
- Observability: "Monitor usage, latency, and spend across providers"; app attribution ("Track which apps are making requests through AI Gateway").
- Extras: web search augmentation, disallow-prompt-training control, coding-agent connection (`vercel ai-gateway coding-agents setup`), OIDC/API-key auth.

## Cross-product Comparison

| Dimension | LiteLLM | Portkey | Cloudflare AI Gateway | Kong AI Gateway | Vercel AI Gateway |
|---|---|---|---|---|---|
| Self-description | open-source unified interface + self-hosted "AI Gateway (Proxy)" | unified interface for 250+ models; control, visibility, security | "observe and control your AI applications" | "connectivity and governance layer for AI-native applications" | one API for hundreds of models; routing, fallbacks, budgets |
| Delivery form | self-hosted OSS proxy (+ enterprise license); SDK variant | OSS gateway + managed control plane; hybrid/private cloud | bundled platform feature (edge + dashboard) | control plane (Konnect) + data plane (self-hosted/K8s); on-prem | fully managed SaaS endpoint |
| Client integration | base_url swap, OpenAI-compatible | base_url + headers, SDK, REST | provider-schema passthrough URL, OpenAI-compatible endpoint, unified REST API | gateway endpoints per AI Model entity | OpenAI/Anthropic-compatible endpoints, AI SDK |
| Schema posture | OpenAI format universal | multi-format universal (OpenAI Chat/Responses + Anthropic Messages, translated) | provider schema preserved (passthrough) + OpenAI-compatible + unified | consistent API across providers (mechanics unverified) | OpenAI + Anthropic formats |
| Provider credentials | config/env/secret managers; keys in model_list | Model Catalog integrations (custody; secret references; KMS) | BYOK stored / unified billing credits / pass-through headers | AI Model Provider entity (centralized, rotatable) | platform key; BYOK optional; no markup |
| Routing object | model_list + Router settings (config.yaml) | Configs (JSON; fallback/loadbalance/conditional; params shaping) | Dynamic routes (versioned node graphs) | AI Model entities + policies | provider options + routing rules |
| Failure handling | retries, ordered fallbacks (3 error classes), cooldowns, health-check routing, pre-call checks | retries, circuit breaker, timeouts, fallbacks | retries + model fallback; rate/budget-limit nodes switch to fallback | failover across providers/models (mechanics unverified) | automatic retries to other providers |
| Access governance | virtual keys, teams, RBAC, budgets, TPM/RPM, OIDC/JWT, rotation | API keys w/ default configs, orgs/workspaces/roles, saved-only lockdown, SCIM/SSO | gateway auth, rate limiting, budget nodes | AI Consumer Groups, tiered budgets via identity, metering/billing | API keys/OIDC, budgets, spend monitoring |
| Usage visibility | spend per key/user/team; logs; OTel callbacks | logs/traces/analytics/cost; OTel export | analytics (requests/tokens/cost/errors/cache), GraphQL | usage analytics, OTel GenAI, audit logs | usage/latency/spend monitoring |
| Caching | yes | simple + semantic | yes | semantic cache | not observed on root page |
| Guardrails | guardrails module | guardrails suite + BYO webhooks | not observed on fetched pages | prompt/response guards, sanitizer, cloud trust-service delegation | prompt-training opt-out only |
| Extended traffic | MCP + A2A gateway | MCP gateway, agent gateway, coding agents, other APIs (rerank/video) | — (LLM-focused on fetched pages) | MCP servers, A2A, AI CLIs | coding agents, web search |
| Billing posture | OSS free; enterprise license | OSS free; managed free tier + paid; provider costs via customer keys | free feature; Workers AI billing modes | platform licensing; metering/billing for AI products | usage-billed at provider prices, no markup |

### Stable commonalities (evidence layer B, cross-product)

1. Intermediary position: every product is something the client points at instead of the provider (base URL swap, gateway URL, header-routed gateway, entity-defined endpoint).
2. Model-aware handling: every product parses/transforms/meters model traffic (token usage, prompts, model names) — Kong states this as its explicit differentiator vs a generic gateway.
3. Gateway-side routing decision: model names resolve through gateway-defined configuration (model_list / configs / dynamic routes / AI Model entities / provider options), not hard-coded client logic.
4. Provider credential handling centralized at the gateway or delegated explicitly (BYOK/pass-through) — never required in every client.
5. Resilience machinery: retries + fallback across providers/models in all five.
6. Per-request usage capture and spend/usage visibility in all five (form varies: spend logs, logs+analytics, dashboard analytics, OTel, spend monitoring).
7. Budgets/rate limits as request-time enforcement in all five.
8. Management surface separate from the inference surface (admin UI / control plane / config-as-code) in all five.
9. Team/segment-scoped access (teams, workspaces, consumer groups, app attribution) in all five.

### Stable variation axes (→ L2)

- Delivery: self-hosted OSS ↔ managed SaaS ↔ platform-bundled ↔ API-gateway lineage ↔ control/data plane split.
- Schema: strict OpenAI-compatible ↔ multi-format universal ↔ provider-schema passthrough.
- Credential posture: custody ↔ BYOK ↔ pass-through ↔ billing absorption.
- Scope: LLM-only ↔ LLM+MCP+A2A (agent-era expansion).
- Governance depth: per-key budgets ↔ org/workspace hierarchy + lockdown + SCIM.
- Monetization: free passthrough ↔ usage-billed reseller ↔ platform licensing.

## Canonical Abstraction

### L0 — Defining Invariant

An AI Gateway / Model Routing Platform is an intermediary layer between client applications and model provider APIs, with three defining properties:

1. **Intermediary position on the model request path** — applications direct model requests to the gateway rather than directly to model provider APIs; the gateway forwards each request to an upstream model provider API and returns the response to the client.
2. **Model-aware traffic handling** — the gateway understands model API semantics (model identifiers, prompt/message bodies, token usage, provider schemas) well enough to route, transform, meter, and apply model-specific policy to the traffic. A plain HTTP reverse proxy without this is not an AI gateway.
3. **Gateway-side execution decision** — which upstream provider/model/deployment serves each request is determined by the gateway's own configuration and policy (degenerate case: one fixed upstream; mature case: fallback chains, load balancing, conditional rules), applied uniformly across applications, instead of being hard-coded in each client.

Remove the intermediary → the product becomes a model API or an SDK. Remove model-awareness → it becomes a generic API gateway/reverse proxy. Remove the gateway-side execution decision → it becomes a client library. All three removals destroy the Type.

Deliberately NOT in L0 (checked against §24 historical/degenerate forms):
- multi-provider support (single-provider passthrough gateways exist — Cloudflare fronts one provider fine)
- OpenAI-compatible universal schema (Cloudflare preserves provider schemas; Kong routes per provider)
- provider credential custody (pass-through header mode exists)
- usage logging/analytics (OSS gateways run without the control plane; a logging-free routing proxy is still a gateway)
- budgets/virtual keys/caching/guardrails (all common, none defining)
- MCP/A2A/agent traffic (2025–26 expansion)

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- unified/OpenAI-compatible access surface (drop-in base-URL swap)
- provider/model catalog as configuration (model list, model entities, model catalog, routes) with gateway-facing model names/aliases
- provider credential custody or explicit BYOK management
- retry + fallback (provider failover), often error-class-specific (rate limit, context window, content policy)
- load balancing across deployments/keys/providers
- per-request logging; usage analytics (requests, tokens, cost, errors, latency)
- cost tracking / spend attribution per key/team/user
- budgets and rate limits enforced at request time
- caching (exact and semantic)
- guardrail hooks (content filtering, PII handling) — bundled capability
- admin/management surface (UI or control plane) + management APIs / config-as-code
- team/segment-scoped access organization
- observability export (OTel, Prometheus, log export, GraphQL)

### L2 — Variant / Optional Structure

- delivery posture: self-hosted OSS proxy / managed SaaS / edge-bundled / API-gateway plugin lineage / control-plane+data-plane
- schema posture: strict OpenAI-compatible / multi-format universal / provider-schema passthrough
- credential & billing posture: custody / BYOK / pass-through / usage-billed reselling (no-markup pass-through billing)
- extended traffic types: MCP gateway, A2A/agent gateway, AI CLI proxying, other provider APIs (rerank, video, speech)
- advanced routing: semantic/complexity auto-routing, canary/percentage splits, A/B, traffic mirroring, request prioritization
- guardrail depth: native checks vs delegation to cloud trust & safety services
- enterprise governance: SSO/SCIM, audit logs, KMS/secret references, org/workspace hierarchy, saved-only lockdown, data-residency/FIPS deployments
- batch/fine-tuning/realtime passthrough endpoints; multimodal endpoint coverage

### L3 — Vendor-specific (research notes only)

- LiteLLM: config.yaml `model_list` schema; `sk-` virtual keys; `LiteLLM_SpendLogs` table; `x-litellm-*` response headers; Router class; enterprise license gating (SSO, audit, rotation).
- Portkey: `x-portkey-*` headers; config IDs (`pc-...`); `@provider-slug` virtual-key references; Nitro mode (no-transformation forwarding); PRISMA AIRS (Palo Alto Networks) branding; Model Catalog replacing deprecated Virtual Keys.
- Cloudflare: `cf-aig-gateway-id` header; `gateway.ai.cloudflare.com/v1/{account}/{gateway}/{provider}` URL shape; Workers AI standard-vs-unified billing; GraphQL analytics dataset; auto-created default gateway.
- Kong: Konnect control plane; `kongctl`/decK; v1 AI Proxy plugins → v2 AI Model/AI Model Provider entities; AI Consumer Group; named policies (AI Sanitizer, AI Prompt Compressor, AI Semantic Prompt Guard).
- Vercel: `ai-gateway.vercel.sh` endpoint; AI SDK integration; app attribution; auto-recharge; no-markup token pricing.

## Rejected Findings

- "AI gateway = OpenAI-compatible universal API" — rejected: Cloudflare's primary form preserves provider schemas; Kong routes per provider entity. Universal schema is common (LiteLLM, Portkey, Vercel), not invariant.
- "AI gateway = cost/usage dashboard" — rejected: cost visibility is a byproduct; OSS gateways run without control planes; consistent with the ai-cost-finops pass.
- "AI gateway = guardrails" — rejected: bundled capability; standalone guardrail products exist; Cloudflare's fetched pages show none.
- "AI gateway = virtual keys" — rejected: Cloudflare has none; Portkey deprecated virtual keys in favor of Model Catalog; the invariant is gateway-side access governance, not the key artifact.
- "AI gateway = self-hosted proxy" — rejected: managed SaaS (Vercel), platform-bundled (Cloudflare), and control-plane products (Kong) are equally canonical forms.
- "AI gateway must be multi-provider" — rejected: single-upstream passthrough gateways satisfy the core; multi-provider unification is the standard mature motivation, not the definition.
- "Model routing is a separate Type from AI gateway" — rejected: in all sampled products routing is the gateway's internal function (configs/routes/router settings), not a separately marketed structure; the leaf's dual name names one Type.

## Boundary Findings

1. **vs Model API Platform (§13 sibling).** The model API platform is the provider-side serving API — the thing gateways route *to*. The gateway owns no models and serves no inference; it intermediates. Managed unified-API gateways (Vercel: usage-billed, no markup, BYOK) drift toward aggregation but remain intermediaries whose defining value is routing/governance over provider APIs, not model ownership. Aggregators that sell model access as the product (OpenRouter-class; not fetched) sit on the model-API side. Test: remove the intermediary → a model API platform remains; remove model ownership/serving → a gateway remains. Flag for joint review when Model API Platform is processed.
2. **vs API Gateway Management Console / generic API gateway (§12).** Generic gateways route HTTP to services without model semantics. Kong's own FAQ draws the line: behind a generic gateway you "can only interact at the API level", while AI Gateway "can understand the prompts" and applies body-level AI policies. Test: model-awareness (token metering, prompt inspection, model-level fallback, provider-schema handling). Remove model-awareness → generic API gateway remains. Note the gradient is real inside one vendor: Kong AI Gateway is a generic gateway plus AI entities/policies.
3. **vs LLM Observability Platform (§13 sibling).** Gateways record per-request logs/usage as a byproduct of being on the path; observability platforms center on trace inspection and quality analysis and ingest from anywhere. Portkey bundles a full observability suite; LiteLLM exports to observability tools; Cloudflare offers dashboard analytics only. Gradient, consistent with the agent-observability pass (Datadog LLM-Observability→Agent-Observability rename). Flag for joint review.
4. **vs AI Cost / FinOps Platform (§13 sibling).** Confirms the earlier pass from the gateway side: gateway = runtime control plane (routing, fallback, credentials) with cost visibility as byproduct and budget enforcement at the request path; FinOps platform = buyer-side spend aggregation/attribution across tools. Shared zone: spend governance at the gateway (budgets, tiered caps).
5. **vs AI Safety / Guardrail Platform (§13 sibling).** Guardrails appear as bundled L1/L2 capabilities (Portkey guardrails suite, Kong prompt/response guards + cloud trust-service delegation, LiteLLM guardrails module); standalone guardrail platforms exist. Capability relationship; flag for joint review when AI Safety / Guardrail Platform is processed.
6. **vs AI Model Hosting Platform (§13 sibling).** Hosting serves model inference (customer-owned/deployed models); the gateway runs no inference — it routes to hosted endpoints like any other upstream (Portkey custom hosts; LiteLLM custom api_base). Routing-to-hosted ≠ hosting.
7. **vs LLM Application Development Platform (§13 sibling).** Dev platforms center on building LLM apps (SDKs, orchestration, prompts); the gateway is the runtime access/routing layer beneath them. LiteLLM spans both (SDK + proxy) — a gradient, not a wall.
8. **Naming observation.** The market uses "AI gateway", "LLM gateway", "LLM proxy", "AI gateway/router" interchangeably; "model routing" names the mature core function rather than a separate structure. Recent vendor positioning drifts toward "governance layer" (Kong) and toward MCP/agent-gateway expansion — expansion trend, not a new Type.

## §24 Historical / Market-Sample Check

The category is young (≈2023+), so the "older/degenerate forms" check runs against the pre-AI gateway lineage and minimal forms:

- Generic API gateway with AI plugins (Kong lineage): satisfies L0 once AI entities/policies add model-awareness — the definition must not require purpose-built-for-LLM architecture. ✔ covered.
- Plain passthrough proxy in front of one provider (Cloudflare's original mode): satisfies L0 with degenerate routing (single fixed upstream). ✔ covered — hence multi-provider and unified schema stay out of L0.
- Credential-less pass-through mode (client keeps provider keys): satisfies L0. ✔ covered — hence credential custody stays out of L0.
- OSS gateway without control plane (no logs/UI): satisfies L0. ✔ covered — hence logging stays out of L0.
- The definition must also not over-fit today's dominant bundle (unified API + virtual keys + cost dashboard + guardrails); all of those are L1/L2.

## Uncertainties

- Kong entity-level mechanics (AI Model entity fields, load-balancing algorithms, failover configuration) unverified — subpages 404; all Kong claims above are landing-page level.
- OpenRouter-class aggregators not fetched; their placement on the Model-API side of the boundary is positioning-level reasoning, not documented evidence.
- Portkey↔PRISMA AIRS (Palo Alto Networks) branding status observed as a docs banner only; ownership/roadmap not researched.
- Whether guardrails/MCP/agent traffic will become defining for the Type over time (current evidence says no — they are absent from some canonical products — but the category is young and consolidating).
- Vercel evidence is root-page level; routing-rules mechanics not verified.
- Vendor performance numbers (latency, uptime, request volume) observed in docs but excluded from all claims as marketing figures.

## Final Synthesis

The AI Gateway / Model Routing Platform is the runtime intermediary that an organization points its model traffic through. Its defining core is small: applications send model requests to the gateway; the gateway understands model API traffic and executes each request against an upstream model provider chosen by the gateway's own configuration and policy; responses flow back through the gateway. Everything the market associates with the category — the OpenAI-compatible universal API, provider credential custody, virtual keys, fallback chains and load balancing, per-request logs and cost dashboards, budgets and rate limits, caching, guardrails, MCP/agent traffic — is mature structure layered on that core, and the delivery form (self-hosted proxy, managed SaaS, edge-bundled, API-gateway lineage) is a variant axis, not the definition. The Type sits between the model API platforms it routes to, the generic API gateways it differs from by model-awareness, and the observability/FinOps/guardrail products it feeds and partially bundles.
