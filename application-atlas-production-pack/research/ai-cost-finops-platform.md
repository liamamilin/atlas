# Research Notes — AI Cost / FinOps Platform

Research date: 2026-09-06
Methodology: v1.1 (update-v1/WORKFLOW_v1.1.md, WRITING_GUIDE_v1.1.md)

## Research Goal

Understand what an "AI Cost / FinOps Platform" actually is as an Application Type: what objects it manages, how AI spend data enters it, how spend is attributed and governed, and where its boundary lies against Cloud Cost Management / FinOps, LLM Observability Platforms, and AI Gateways.

## Initial Boundary

Working hypothesis before research:

- Core use: give an organization visibility into and control over what it spends on AI (model APIs, AI services, inference), attributed to teams/apps/users, with budgets and optimization.
- Likely users: FinOps practitioners, finance, platform/engineering leads, AI product teams.
- Nearest Types: Cloud Cost Management / FinOps (§14), LLM Observability Platform (§13), AI Gateway / Model Routing Platform (§13), Spend Management Platform (§08), Billing Platform (§08, vendor side).
- Open questions: is this a distinct Type or a scope variant of Cloud FinOps? What is the central object — usage event, cost record, or budget?

## Research Questions

1. What is the central managed object (usage record? cost line? budget?)
2. How does AI usage/cost data enter the system (provider billing APIs, gateways, per-request telemetry)?
3. What unit economics are modeled (tokens, requests, models, per-model pricing)?
4. How is cost attributed to organizational dimensions (teams, apps, users, keys, environments)?
5. What governance mechanisms exist (budgets, alerts, anomaly detection, limits, enforcement)?
6. Showback vs chargeback: who consumes the outputs and how?
7. What optimization capabilities exist (model routing, caching, right-sizing, recommendations)?
8. Where are the boundaries vs LLM Observability, AI Gateway, and Cloud FinOps?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels:

| Product | Philosophy | Customer level | Role in sample |
|---|---|---|---|
| Vantage | Cloud FinOps platform extended with AI-provider cost ingestion | Enterprise FinOps | billing-side aggregation pole |
| CloudZero | "Financial control plane" for cloud + AI + SaaS, unit economics | Enterprise FinOps | billing-side + real-time hybrid pole |
| Helicone | LLM observability/gateway with cost analytics | Dev teams → scale-ups | request-side observability pole |
| Portkey | AI gateway + governance with spend controls | Platform teams, enterprise | request-side enforcement pole |
| Cloudflare AI Gateway | Platform-native AI gateway with cost analytics | Individual devs → enterprise | platform-native minimal pole |

## Sources

All fetched 2026-09-06 (Layer A unless noted):

- Vantage docs root: https://docs.vantage.sh/ ; index: https://docs.vantage.sh/llms.txt
- Vantage — Anthropic integration: https://docs.vantage.sh/connecting_anthropic.md
- Vantage — Custom LLM Enrichment: https://docs.vantage.sh/custom_llm_enrichment.md
- Vantage — Cloudflare AI Gateway Enrichment: https://docs.vantage.sh/cloudflare_ai_gateway_enrichment.md (listed in index; page not separately fetched)
- Vantage — Segments (showback/chargeback), Budgets, Cost Alerts, Anomaly Detection, Forecasting, RBAC: listed with descriptions in https://docs.vantage.sh/llms.txt (index-level evidence)
- CloudZero docs root: https://docs.cloudzero.com/ ; index: https://docs.cloudzero.com/llms.txt
- CloudZero — AI Platforms: https://docs.cloudzero.com/docs/ai-platforms.md
- CloudZero — AI Signals: https://docs.cloudzero.com/docs/real-time-ai-spend-with-ai-signals.md
- CloudZero — Connecting to Anthropic: https://docs.cloudzero.com/docs/connections-anthropic.md
- CloudZero — Overview (cloudzero.md), Dimensions, Unit Economics, Budgets, Anomaly Detection, Optimize, Model Right Sizer: index-level evidence
- Helicone docs root: https://docs.helicone.ai/ ; index: https://docs.helicone.ai/llms.txt
- Helicone — Cost Tracking & Optimization: https://docs.helicone.ai/guides/cookbooks/cost-tracking.md
- Helicone — How We Calculate Cost: https://docs.helicone.ai/references/how-we-calculate-cost.md
- Helicone — Alerts, Custom Rate Limits, Reports, Sessions, User Metrics: index-level evidence
- Portkey docs root: https://portkey.ai/docs ; index: https://docs.portkey.ai/docs/_llms/latest/docs.md
- Portkey — Model Pricing and Cost Management: https://docs.portkey.ai/docs/product/observability/cost-management.md
- Portkey — Budget Limits / Integrations (workspace provisioning, budget & rate limits): https://docs.portkey.ai/docs/product/observability/budget-limits.md (page rendered as the Integrations/Model Catalog limits page)
- Cloudflare AI Gateway — Overview: https://developers.cloudflare.com/ai-gateway/
- Cloudflare AI Gateway — Analytics: https://developers.cloudflare.com/ai-gateway/observability/analytics/

Source-access limitations: none material; all primary pages fetched successfully. Some Vantage/CloudZero/Helicone features are evidenced at index level (page title + official description) rather than full-page level; assertions relying on those are kept moderate.

## Product Observations

### Vantage (Layer A)

Positioning: "cloud observability and optimization platform that aggregates cloud infrastructure costs across providers… advanced FinOps workflows and cost governance."

Key observations:

- **AI providers as cost integrations.** Dedicated integrations for OpenAI, Anthropic, AWS (Bedrock), Google Cloud (Vertex/Gemini), Azure, plus AI-native providers: Anyscale, Baseten, Cursor, ElevenLabs, Fireworks AI, Modal, xAI. Same integration machinery as cloud providers (AWS, Azure, GCP, Kubernetes, Snowflake, Datadog, etc.).
- **Provider billing APIs as data source.** Anthropic integration ingests from two sources: Claude API (Admin API key → Usage and Cost API; breakdown by workspace, API key, model, token type) and Claude.ai (Enterprise Analytics API key; breakdown by user, product, model, token type). Read-only posture stated explicitly ("Vantage cannot perform cost-informing actions and only ever reads cost and usage data"). Usage measured in tokens; provider tags auto-created (`anthropic:model`, `anthropic:billing_source`, `anthropic:user_email`, `anthropic:inference_geo`, etc.).
- **Per-request token telemetry enrichment.** "Custom LLM Enrichment": customer emits one JSON record per LLM request (Token Cost Allocation Specification: provider, model, token counts incl. cache read/write, allocation `tags`) to an S3 bucket; Vantage joins telemetry to provider cost rows and **splits each cost row proportionally by token share**, adding the customer's tags. Splits are additive — "the sum of the enriched rows always equals the original cost row to the cent"; uncovered usage becomes a "leftover" row so totals reconcile. Metadata-only: no prompt/completion content collected.
- **Gateway logs as telemetry source.** Cloudflare AI Gateway Logpush logs can be read from S3 for the same enrichment purpose.
- **Allocation machinery.** Virtual Tags, Segments ("hierarchical cost governance and showback/chargeback capabilities"), Workspaces, RBAC with per-action permission tables, SSO.
- **Governance objects.** Budgets, Cost Alerts, Anomaly Detection (ML-powered), Forecasting, Scenario Models, Report Notifications (email/Slack/Teams), Cost Recommendations, Issues (collaboration on optimization), Business Metrics (unit cost / margin vs cloud costs).
- **API/export.** REST API, VQL (SQL-like cost query language), Terraform provider, Snowflake data sharing.

### CloudZero (Layer A)

Positioning: "the financial control plane for your cloud and AI spend."

Key observations:

- **AI platforms as connections.** Anthropic (Platform: costs by project, model, operation via Usage and Cost API with Admin key; Anthropic Enterprise: per-user costs by product, model, context window via Analytics API key), Cursor (Admin API; per-user usage, billing groups, model costs), OpenAI (read-only Admin key; Costs API; by project, model, service tier, usage type). All connections read-only.
- **Real-time AI spend (AI Signals, preview).** Captures AI usage as it happens via: macOS Collector (network extension on devices), LiteLLM gateway streaming, Bifrost gateway streaming, OpenTelemetry ingestion. Two data paths: live usage "in seconds" + reconciled costs "within about 24 hours, matched against your actual provider billing."
- **Same allocation machinery as cloud.** AI costs flow into Explorer; allocated with Dimensions (team, product, feature, environment, customer — built visually or via CostFormation code), shared/unknown spend splitting, Views, Unit Economics, Dashboards, Budgets, Anomaly Detection, Optimize recommendations, AI Hub (natural-language questions over spend; Model Right Sizer for model choice).
- **Custom ingestion.** AnyCost: custom cost data via REST API or S3 bucket in a Common Bill Format (CBF) — the escape hatch for unsupported providers.
- **Telemetry APIs.** Allocation telemetry and unit-metric telemetry streams (sum/replace/delete) for customer-defined allocation and unit costs.
- **Users.** FinOps/finance (track, allocate, budget, ROI), platform/DevOps engineers (drivers, anomalies, optimization), engineering/business leaders (dashboards).

### Helicone (Layer A)

Positioning: LLM observability + AI gateway ("Get your first LLM request logged… using the AI Gateway"; OpenAI-compatible unified API across 100+ models).

Key observations:

- **Per-request capture in the request path.** Requests flow through the AI Gateway (or proxy/SDK integrations); each request logged with model, tokens, computed cost. Two cost-calculation regimes: gateway = "100% Accurate" via Model Registry; direct provider integrations = "best-effort" estimates from an open-source pricing repository (300+ models).
- **Cost computation from tokens × pricing.** Usage object (prompt/completion/total tokens) captured from provider responses; cost estimated from pricing tables; streaming requires enabling usage flags; open-source cost calculator published.
- **Attribution via request metadata.** Custom properties (e.g., `Helicone-Property-UserTier`, `-Feature`, `-Environment`) attached per request; Sessions group related requests into workflows ("a support chat costs $0.12 on average with 5 API calls"); User Metrics tie cost to end users.
- **Cost prevention.** Alerts with graduated thresholds on spend; Custom Rate Limits "by request count, cost, or custom properties"; caching to eliminate redundant calls (cache hit rate → savings); automated weekly Reports (spend summaries, top cost drivers) to email/Slack.
- **Cost optimization in the gateway.** Cost-based routing (cheapest available provider), BYOK priority (use owned credits first), smart fallbacks; Model Registry with real-time pricing sorted by cost.
- **Data access.** REST APIs, HQL (SQL with row-level security), ETL to warehouse, webhooks, MCP server.

### Portkey (Layer A)

Positioning: AI gateway + governance ("unified interface for 250+ AI models… control, visibility, and security"). Now distributed as Palo Alto Networks PRISMA AIRS AI Gateway (branding observed in docs banner).

Key observations:

- **Per-request cost at the gateway.** Real-time cost tracking per request; centralized pricing JSON (auto-updates; 24h cache in hybrid mode); input/output token costs; analytics (total spend, cost per model/provider/token, budget utilization).
- **Pricing coverage is a first-class concern.** Unsupported models show $0.00 cost and are excluded from budget limits; streaming requests need `stream_options: {include_usage: true}` to get token counts (documented troubleshooting).
- **Custom pricing.** UI-based price overrides for negotiated rates; custom/fine-tuned/self-hosted model entries with own pricing; pricing adjustments (discount/markup multipliers per integration); explicit use case: "internal chargebacks — set custom rates for internal cost allocation."
- **Budget limits as enforcement.** Cost-based (USD) or token-based limits; when reached, the key "automatically expire[s]… to prevent further usage"; alert thresholds before the limit; periodic resets (weekly/monthly at UTC boundaries); limits cannot be edited once set; minimums documented ($1 / 100 tokens). Rate limits (request- or token-based, per minute/hour/day) with rejection after exhaustion.
- **Organizational structure.** Organizations → Workspaces; Integrations (centralized provider credentials) provisioned to workspaces with per-workspace budgets/rate limits/model allowlists; API keys with enforced default configs; RBAC, SSO, SCIM, audit logs; admin can enforce budget/rate limits at org, workspace, integration, and API-key levels.
- **Metadata for attribution.** Request metadata (custom context) for observability/analytics; metadata enforcement available.

### Cloudflare AI Gateway (Layer A)

Positioning: "Observe and control your AI applications" — gateway in front of multiple providers (Workers AI, Anthropic, Google Gemini, OpenAI, Replicate, more).

Key observations:

- **Gateway-level analytics.** Dashboard metrics: requests, token usage, costs ("track spending, manage budgets, and optimize resources"), errors, cached-response percentage; filterable by time; GraphQL API for programmatic queries (dimensions: model, provider, gateway, timestamp).
- **Cost-adjacent controls.** Caching (serve from cache "for faster requests and cost savings"), rate limiting, request retry/model fallback.
- **Minimal cost surface.** No dedicated budget-limit object or chargeback machinery documented at this level; cost is an analytics metric of the gateway. This is the thinnest cost implementation in the sample — useful as the boundary marker toward "gateway with cost analytics" rather than a cost platform.

## Cross-product Comparison

| Dimension | Vantage | CloudZero | Helicone | Portkey | Cloudflare AI Gateway |
|---|---|---|---|---|---|
| Philosophy | Cloud FinOps platform extended to AI | Financial control plane (cloud+AI+SaaS) | LLM observability + gateway | AI gateway + governance | Platform-native gateway |
| AI data path | Provider billing APIs + customer token telemetry (S3) + gateway logs | Provider billing APIs + real-time collectors (device/gateway/OTel) + AnyCost | Request-path logging (gateway/proxy/SDK) | Request-path capture at gateway | Request-path capture at gateway |
| Central record | Provider cost row (enriched/split) | Cost record organized into Dimensions | Request log with computed cost | Request log with cost + budget-limit objects | Aggregated analytics |
| Unit economics | tokens (incl. cache read/write), model, token type | tokens, model, operation, project, user, product, context window | tokens/request, session cost, user cost | input/output tokens, per-request cost | tokens, requests, cost |
| Attribution | Virtual Tags, Segments, enrichment tags (team/purpose) | Dimensions (CostFormation), shared-cost split | custom properties, sessions, users | workspaces, API keys, metadata | gateway/provider/model |
| Pricing source | Provider-reported cost (bill truth) | Provider-reported cost (bill truth) | Computed: tokens × pricing tables (two accuracy regimes) | Computed: tokens × pricing JSON (+ custom pricing) | Computed at gateway |
| Budgets/alerts | Budgets, Cost Alerts, Anomaly Detection, Forecasting | Budgets, Anomaly Detection, notifications | Alerts (thresholds), rate limits by cost | Budget limits (cost/token, key expiry, resets), rate limits | Rate limiting only (no budget object documented) |
| Showback/chargeback | Segments (explicit) | Dimensions + unit economics | Unit economics per session/user | Custom pricing for "internal chargebacks" | — |
| Optimization | Recommendations, FinOps Agent | Optimize, Model Right Sizer | Cost-based routing, caching, BYOK | Caching, routing, model selection | Caching, rate limiting |
| Enforcement posture | Read-only (observe) | Read-only (observe; AI Signals observes) | Observe + rate limits | Observe + enforce (key expiry) | Observe + rate limit |
| Latency of truth | Daily refresh cadence | ~24h reconciliation (+ seconds-level live) | Real-time | Real-time | Real-time |
| Scope | Cloud + AI + SaaS + observability vendors | Cloud + AI + SaaS | AI/LLM only | AI/LLM only | AI/LLM only (within Cloudflare) |

### Cross-product commonalities (Layer B)

1. Every product turns **AI consumption into money** — either by ingesting provider-reported costs or by computing cost from token counts × model pricing.
2. Every product carries a **model/provider dimension** and token-based usage measures; token kinds (input/output/cache) appear wherever granularity allows.
3. Every product provides **attribution to organization-defined dimensions** beyond what the provider bill exposes (tags, dimensions, properties, workspaces).
4. Every product provides **analysis surfaces** (reports/explorer/dashboards/analytics) with filtering/grouping by those dimensions over time.
5. Mature implementations add **budgets/alerts/anomaly detection** (4 of 5) and **optimization levers** (caching, model selection/routing, recommendations).
6. Two data-path families recur: **billing-side aggregation** (read-only, reconciled to provider bills, lagged) and **request-side capture** (real-time, computed cost, optionally enforcing). CloudZero explicitly runs both and reconciles them.
7. **Pricing coverage/maintenance** is a shared operational problem: pricing catalogs, update mechanisms, custom/negotiated rates, and explicit handling of unsupported models.
8. **Enterprise governance** (roles, workspaces, SSO, audit) appears in the enterprise-tier products; dev-tier products emphasize self-serve setup.

### Divergences (candidate L2/L3)

- Where cost truth comes from (provider bill vs computed estimate) — posture, not invariant.
- Whether the platform can enforce (cut off spend) or only observe — Portkey enforces; Vantage/CloudZero observe.
- Scope: AI-only vs cloud+AI unified — both viable; not defining.
- Real-time vs reconciled lag — data-path property, not defining.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Minimal structure without which the product is not an AI Cost / FinOps Platform:

```text
AI consumption usage records
  (metered model/AI-service consumption: model identity + token/request measures)
  └── Cost assignment
      (usage mapped to money: ingested provider cost or computed from pricing)
      └── Organizational attribution
          (spend mapped to organization-defined dimensions: team/app/user/key/environment)
          └── Spend visibility surface
              (breakdown/analysis of attributed spend over time)
```

Four properties:

1. **AI consumption as the metered object** — usage records of model/AI-service consumption (model identity, tokens and/or requests). Remove → not about AI.
2. **Cost assignment** — usage mapped to money, ingested or computed. Remove → usage analytics, not cost.
3. **Organizational attribution** — spend mapped to owners/dimensions the organization defines. Remove → a provider billing dashboard; the FinOps job (who owns what, showback/chargeback, per-team budgets) collapses.
4. **Spend visibility surface** — the attributed spend is queryable/browsable for decisions. Remove → a data pipeline, not a platform.

§24 historical/market-sample check: the Type is young; the "older/simpler" forms are provider-native usage/cost consoles (single-provider, provider-native dimensions only) and pre-AI cloud FinOps platforms. The definition above excludes provider consoles via property 3+4 at organization level with organization-defined (not provider-native) attribution, and excludes generic cloud FinOps via property 1. It does not require: gateways (billing-side platforms lack them), real-time (billing-side is lagged), token-level granularity (provider APIs expose differing granularity), enforcement (observe-only platforms qualify), or multi-provider coverage as an absolute (though all sampled products are multi-source; single-source organization-level cost platforms would still satisfy the core — recorded as an uncertainty).

### L1 — Common Mature Structure

- Multi-provider/model coverage (provider integrations or gateway fronting many providers)
- Pricing data maintenance (model price catalog, update mechanism, custom/negotiated pricing, coverage-gap handling)
- Cost reports/dashboards with filter/group by dimensions and time
- Budgets, alerts, anomaly detection, forecasting
- Allocation machinery: tags/dimensions/segments; shared-cost splitting; showback/chargeback
- Unit economics (cost per user/session/customer/feature; business-metric linkage)
- Optimization levers: caching, model selection/right-sizing/routing, recommendations
- Roles/permissions, workspaces, SSO (enterprise tier)
- Export/API (REST/GraphQL/SQL, warehouse sharing), notification channels (email/Slack)

### L2 — Variant / Optional Structure

- Data path: billing-side aggregation vs request-side capture vs hybrid (live + reconciled)
- Enforcement posture: observe-only vs inline enforcement (budget cutoff, key expiry, rate limits)
- Scope: AI-only vs unified cloud+AI+SaaS
- Attribution substrate: provider-native dimensions vs customer-emitted telemetry vs gateway metadata
- Deployment: SaaS vs self-hosted/hybrid; air-gapped (legacy)
- Customer tier: enterprise FinOps program vs dev-team self-serve
- Provider-native usage/cost consoles: adjacent minimal form, not this Type (single-provider, provider-native attribution only)

### L3 — Vendor-specific (Research Notes only)

- Vantage: Token Cost Allocation Specification; `vntg:ai:*` tag namespace; leftover-row reconciliation; MSP invoicing; Autopilot (Savings Plans); VQL; Build Hours
- CloudZero: CostFormation (YAML allocation language); Dimension Studio; AnyCost + Common Bill Format; AI Signals macOS network-extension collector; Model Right Sizer; engineering-activity correlation events
- Helicone: Sessions; HQL; BYOK-priority routing; open-source cost repository; graduated alert thresholds guidance
- Portkey: Virtual Keys → Model Catalog migration; budget limits immutable once set; documented minimums ($1 / 100 tokens); weekly/monthly UTC resets; pricing adjustments (markup/discount multipliers); PRISMA AIRS rebranding
- Cloudflare: GraphQL analytics schema; Logpush as an export surface consumed by other cost platforms; Workers AI bundling

## Vendor-specific Findings

See L3. Notable: Vantage's enrichment is explicitly **metadata-only** (no prompt content) — a privacy posture likely shared but only directly documented there. Portkey documents that budget limits cannot be edited after creation and that unsupported models are excluded from budgets — precise operational rules that stay here.

## Boundary Findings

1. **vs Cloud Cost Management / FinOps (§14 sibling discipline).** Same allocation/budget/anomaly/showback machinery; the difference is the metered object: AI consumption (models, tokens, AI providers, gateway telemetry) vs infrastructure consumption (compute, storage, network). In the sample, cloud FinOps platforms absorb AI cost as additional data sources (Vantage, CloudZero), and AI-native tools grow cost features — a gradient, not a wall. Test: remove AI-specific consumption/pricing → generic cloud FinOps remains; remove infrastructure cost → AI cost platform remains. **Flagged for joint review; probable scope-variant relationship.**
2. **vs LLM Observability Platform (§13).** Observability centers on traces/quality/debugging with cost as one metric; this Type centers on money (attribution, budgets, chargeback). Helicone/Portkey implement both on one request log. Test: remove cost attribution/budgets → still observability; remove traces/quality → still a cost platform.
3. **vs AI Gateway / Model Routing Platform (§13).** The gateway is a runtime control plane (routing, fallback, credentials); cost visibility is a byproduct. A gateway without cost analytics is still a gateway (Cloudflare's cost surface is thin); a cost platform without a gateway exists (Vantage, CloudZero). The shared zone is spend governance at the gateway (Portkey).
4. **vs provider-native usage/cost consoles** (e.g., OpenAI/Anthropic consoles — their existence is documented inside the Vantage/CloudZero integration pages). Single-provider, provider-native attribution; no organization-level multi-source governance. Adjacent minimal form, not the Type.
5. **vs Spend Management Platform (§08).** Corporate spend/procurement/cards vs metered technical consumption. Different objects and users.
6. **vs Billing/usage-metering platforms** (vendor side; e.g., Metronome appears in Vantage's docs as an imported *business metric* source). Buyer-side spend management vs vendor-side revenue metering — opposite sides of the transaction.

## Uncertainties

- Whether the market consolidates this Type into cloud FinOps platforms as an "AI cost module" (consolidation signals: Vantage/CloudZero position as cloud+AI; Portkey absorbed into a security vendor's gateway). The leaf remains defensible because the data paths, unit economics, and pricing volatility are AI-specific.
- Whether single-provider organization-level cost platforms exist as a stable form (all sampled products are multi-source).
- FinOps Foundation's "FinOps for AI" practice framing was not fetched; the practice-level framing (inform→optimize→operate applied to AI) is inferred from product positioning only and was not needed for the product-structure conclusion.
- Exact refresh cadences, minimums, and reset schedules vary by product and change over time; deliberately excluded from the final document.

## Final Synthesis

An AI Cost / FinOps Platform is the buyer-side application that turns an organization's AI consumption into attributable, governable spend. Its defining core is small: metered AI usage records → cost assignment (ingested or computed) → organizational attribution → spend visibility. Everything else — multi-provider coverage, pricing catalogs, budgets/anomalies/forecasts, showback/chargeback, unit economics, optimization levers, enforcement — is mature structure layered on two data-path families (billing-side aggregation vs request-side capture) that converge on the same deliverable. The Type sits between Cloud FinOps (same discipline, different metered object), LLM Observability (same request log, different center of gravity), and AI Gateways (same runtime position, different primary job).
