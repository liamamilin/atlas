# Research Notes — Model API Platform

Research date: 2026-09-08
Slug: `model-api-platform`
Directory leaf: "Model API Platform" (§13 Data, Analytics & AI Systems)

---

## Research Goal

Understand the Application Type whose product is **metered API access to AI models served by the models' own developer** — as distinct from (a) platforms that host models whose creation they do not own, (b) intermediaries that route model traffic, and (c) platforms that build applications on top of model APIs.

Answer, from real products: what is the defining structure, what does the developer-facing world consist of (objects, surfaces, flows), what rules govern usage, and where exactly are the boundaries with the four sibling Types that already carry joint-review flags into this pass (ai-model-hosting-platform, ai-gateway-model-routing-platform, api-management-platform, llm-application-development-platform)?

## Initial Boundary

Working hypothesis before research (to be tested, not asserted):

- The leaf names the "model developer's API" — OpenAI/Anthropic/Google-Gemini-style first-party inference APIs.
- Nearest neighbors: AI Model Hosting Platform (serves others' models), AI Gateway (intermediates), LLM Application Development Platform (builds on top), API Management Platform (governs endpoints as managed backends).
- Likely confusion: every one of these exposes "an API to models" — the discriminator cannot be "has an API"; it must be structural.

Pre-hung flags from sibling passes (STATUS.md Boundary Issues):

1. ai-model-hosting-platform vs model-api-platform: discriminator = model provenance relative to the platform operator (hosting = models whose creation it does not own; model API = the developer serving its own models); hyperscaler edge converges. → This pass owns the "own models" side and must discharge the flag.
2. ai-gateway-model-routing-platform vs model-api-platform: gateway owns none of the models; "OpenRouter-class aggregators (not fetched) likely sit on the model-API side — flagged for joint review." → This pass must adjudicate the aggregator question (and it fetched OpenRouter).
3. api-management-platform vs model-api-platform: gradient — management platforms treat AI model endpoints as ordinary managed backends; a model API platform's product is the inference API itself. → Confirm from this side.
4. llm-application-development-platform forward flag: model-api-platform is "the substrate layer — cloud suites sell model access AND app machinery, products straddle from the other side." → Confirm substrate position and packaging-vs-identity treatment.

## Research Questions

1. What is the unit of product here — the model? the API? the account? How do model families/versions relate to endpoints?
2. What does a developer actually do end-to-end: credential acquisition → first call → production operation → payment?
3. What rules bind usage: limits (on what axis?), tiers, spend controls, policy gating, data handling?
4. How is model versioning/lifecycle handled (snapshots, aliases, deprecation)?
5. Which surfaces exist beyond the API itself (console, playground, docs, status, changelog)?
6. Do first-party model APIs also distribute their models through third-party channels, and does that change the definition?
7. Where do aggregators (OpenRouter-class) belong?
8. Historical check: does the Type predate LLMs/chat (pre-LLM first-party model APIs), and does the definition survive without chat/token machinery?

## Representative Products

Selection principles applied: market representation + documentation completeness + different product philosophies + different customer levels + different geographies.

| Product | Role in sample | Evidence level |
|---|---|---|
| **OpenAI** | the archetype API-first lab; largest developer platform; enterprise tier | Tier-1 (Help Center, API collection + rate-limit article + nav) — docs site itself returned 403 |
| **Cohere** | enterprise-first specialist; endpoint-family organization; multi-cloud distribution + open-weight dual posture | Tier-1 (docs.cohere.com: going-live, rate-limits, models, tutorials) |
| **DeepSeek** | compatibility-posture challenger (OpenAI/Anthropic-compatible); non-US vendor; concurrency-based limits | Tier-1 (api-docs.deepseek.com: quickstart, rate limit & isolation) |
| **Anthropic** | API-first lab with separate consumer surface; partner-hosting channels | Nav-level only (claude.com platform/docs/console/pricing navigation; content region-blocked) |
| **Google Gemini API** | hyperscaler first-party model API (named for market representation) | Unreachable (2 transport failures) — no first-hand claims made |
| **OpenRouter** | boundary probe only — aggregator posture, not a sample member | Tier-1 (docs quickstart) |

## Sources

Fetched successfully on 2026-09-08:

- OpenAI Help Center root: https://help.openai.com/en/
- OpenAI Help Center API collection: https://help.openai.com/en/collections/3675931-api
- OpenAI — Troubleshooting API rate limits and 429 errors: https://help.openai.com/en/articles/5955604-troubleshooting-api-rate-limits-and-429-errors
- Cohere — Going Live: https://docs.cohere.com/docs/going-live.md
- Cohere — Different Types of API Keys and Rate Limits: https://docs.cohere.com/docs/rate-limits.md
- Cohere — An Overview of Cohere's Models: https://docs.cohere.com/docs/models.md
- Cohere — Build Things with Cohere (tutorial intro): https://docs.cohere.com/docs/build-things-with-cohere.md
- DeepSeek — Your First API Call: https://api-docs.deepseek.com/
- DeepSeek — Rate Limit & Isolation: https://api-docs.deepseek.com/quick_start/rate_limit
- OpenRouter — Quickstart: https://openrouter.ai/docs/quickstart
- claude.com (Anthropic) navigation surfaces — platform overview (/platform/api), developer docs link (platform.claude.com/docs), console login, API pricing anchor, partner hosting pages (AWS / Google Cloud / Microsoft Foundry), regional-compliance page: observed at navigation level only

Unreachable (abandoned per network rules; no details filled from memory):

- platform.openai.com/docs/** — 403 (bot wall); OpenAI covered via its Help Center instead
- claude.com / platform.claude.com docs pages — region-blocked content ("App unavailable in region") ×2
- ai.google.dev (Gemini API docs) — transport error/timeout ×3 attempts, 2 URLs
- docs.mistral.ai — transport error ×2
- docs.x.ai — transport error/timeout ×2

Evidence-layer convention used below: **A** = directly observed on an official source for that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning. Claims in the final document are calibrated to these layers.

---

## Product A — OpenAI (Help Center, API collection)

### Key observations

- **Naming and surface split (A).** The Help Center treats "OpenAI API" and the "API Platform" as the developer-facing product ("API Platform - Scale Tier…", "Admin and Audit Logs API for the API Platform", "the API Platform organization"), kept distinct from ChatGPT (the consumer product). The site footer pairs the two surfaces: "ChatGPT" (chatgpt.com) and "API" (platform.openai.com/docs), plus "Service Status" (status.openai.com). A developers.openai.com docs domain is referenced from help articles.
- **Account containers (A).** Organizations and projects are the operating containers: "How can I change my API platform's org name", default-organization setting, "If you belong to multiple organizations…", limits "apply at the organization and project levels. They are not individual user allowances." Enterprise adds SSO/SCIM and user management; an "API Organization Verification" article exists.
- **API keys (A).** "Find, create, manage, and delete your OpenAI API keys"; key permissions ("full access, restricted access, and read-only access"); sharing keys with teammates discouraged; keys are bound to organizations ("view the users or organizations associated with an API key"); a "safety identifier" can be attached to requests so abuse signals link to end users without sharing identifying information.
- **Limits and 429 semantics (A).** The rate-limit article: "API usage is subject to rate limits. These limits restrict requests, tokens, or other usage over a specified period." A 429 can mean a temporary rate limit, an exhausted prepaid balance, a usage limit, or a spend limit — with distinct error codes (credit_balance_exhausted, organization_usage_limit_exceeded, organization_spend_limit_exceeded, project_spend_limit_exceeded). Requests/minute and tokens/minute are separate limits; limits vary by model and "some model families share a limit"; enforcement can happen over sub-intervals (a 60/min limit may also be enforced per second); Retry-After honored, SDKs auto-retry eligible errors; failed requests count toward per-minute limits.
- **Usage tiers (A).** "As API spending increases, OpenAI can automatically graduate an organization to a higher usage tier. This usually increases rate limits across most models." A "Limits" page shows the current tier; the approved monthly usage limit is separate from rate limits. Enterprise "Scale Tier" manages token-capacity purchases.
- **Billing (A).** Prepaid credits model ("Add credits in your API billing settings", "Setting up and managing prepaid API billing"); spend limits at organization and project level with monthly reset; invoices/payment history articles; token counts visible in API responses and the Usage Dashboard ("Reviewing API usage and costs" — token counts, project filters, exports).
- **Endpoint families (A, from help-center article titles).** Text generation (Chat Completions; legacy Completions with a migration article), Embeddings, Image generation (incl. "Is DALL·E 3 available through an API?"), Whisper audio API, Moderation ("Is the Moderation endpoint free to use?"), Batch API ("endpoint for asynchronous batch processing"), Assistants API v1/v2 (with migration FAQ), Responses API, fine-tuning (incl. "Reinforcement Fine Tuning API" billing guide), function calling, logit bias, stop sequences, output-length control parameters.
- **Playground (A).** Chat Playground with function calling; "Prompt management in Playground"; parity articles ("Why am I getting different completions on Playground vs. the API?"; "Why are Playground outputs misclassified as unsafe?") — the playground runs the same models as the API.
- **Compliance/security surface (A).** BAA for HIPAA ("How can I get a Business Associate Agreement… for the API Services"), data residency ("opt to store and process data… within the United States or within Europe"), IP allowlisting, mutual TLS beta, admin/audit-logs API.
- **Data controls (A).** "Sharing feedback, evaluation and fine-tuning data, and API inputs and outputs with OpenAI — Manage how your organization shares…" — a data-use control surface.
- **Model lifecycle signals (A).** Knowledge-cutoff article ("Do the OpenAI API models have knowledge of current events?"); legacy-endpoint migration articles (Completions → Chat Completions; Assistants v1 → v2/Responses) — model/endpoint deprecation as a managed operation.
- **Open-weight dual posture (A).** Help-center collection "Open Models (gpt-oss) — Information regarding our open-weight models, gpt-oss."
- **Third-party serving channel (A).** "Responses API support on Amazon Bedrock — Learn how AWS operates an OpenAI-compatible Responses API implementation for supported OpenAI models on Amazon Bedrock." First-party models also served through another operator's hosting platform, with the first-party schema preserved.
- **Policy enforcement (A).** Account warnings and deactivation articles ("Why Did I Receive a Warning About My Account?", "Why Was My OpenAI Account Deactivated?") — usage-policy enforcement on the platform.

## Product B — Cohere (docs.cohere.com)

### Key observations

- **Positioning sentence (A).** "The Cohere platform lets developers access large language model (LLM) capabilities with a few lines of code." Access via "the playground and SDK"; SDKs "in four different languages: Python, Typescript, Java, and Go"; API key obtained from the dashboard (dashboard.cohere.com/api-keys).
- **Endpoint-organized API (A).** Endpoint families each powered by specific model families: Chat, Embed, Rerank, Parse (document parsing), Audio Transcriptions (ASR), Tokenize, EmbedJob (fine-tuning jobs for embeddings). The models reference maps every model to its endpoints.
- **Model catalog with explicit lifecycle statuses (A).** The models page is a table of named models, each with status: "Live", "Deprecated Sept 15, 2025", "Retired Apr 4, 2026"; aliases exist ("Alias for command-r-plus-04-2024"); per-model attributes: description, modality, context length, maximum output tokens, endpoints. Dated snapshot naming (command-a-03-2025). A changelog documents model refreshes.
- **Two key classes with a gated go-live (A).** "Cohere offers two kinds of API keys: evaluation keys (free but limited in usage), and production keys (paid and much less limited)". Going live requires acknowledging the SaaS agreement, terms, model limitations, model cards, and data statement; indicating a sensitive use case triggers a manual safety-team review before full limits ("Reviews on sensitive use cases will take no longer than 72 business hours").
- **Rate-limit tables per endpoint per model, split trial/production (A).** E.g., Chat models at 20 req/min trial, 500 req/min production for older variants, "Contact sales" for the newest; Embed at inputs/min; Rerank, Parse, Tokenize each with their own rows. Some prod keys "work like trial keys for newer model variants" until sales contact. Rate-limit-increase requests go through support/sales.
- **Multi-platform distribution (A).** "Cohere models are currently available on the following platforms: Cohere's proprietary platform, Amazon SageMaker, Amazon Bedrock, Microsoft Azure, Oracle GenAI Service" — with per-platform model-ID tables (Bedrock model IDs, SageMaker "unique per deployment", Azure AI Foundry IDs, Oracle OCI IDs). The first-party platform is listed first; third-party cloud channels are formalized distribution.
- **Open-weight dual posture (A).** Tiny Aya models: "available on the Cohere API via the Chat endpoint and as open-weight models on Hugging Face."
- **Fine-tuning (A).** "If you need more customization, you can train a model to tune it to your specific use case" (plus the EmbedJob endpoint family).
- **Operational surfaces (A).** Status page (status.cohere.ai) "featuring information including a summary status indicator, component statuses, unresolved incidents, status history, and any upcoming or in-progress scheduled maintenance", with email/phone subscriptions. Pricing docs exist ("how-does-cohere-pricing-work").
- **Tutorial corpus (A).** Seven-part hands-on intro building one assistant across Chat/Embed/Rerank endpoints — docs organized as developer onboarding.

## Product C — DeepSeek (api-docs.deepseek.com)

### Key observations

- **Compatibility posture (A).** "The DeepSeek API uses an API format compatible with OpenAI/Anthropic. By modifying the configuration, you can use the OpenAI/Anthropic SDK or softwares compatible with the OpenAI/Anthropic API to access the DeepSeek API." Two base URLs documented (OpenAI format and Anthropic format); API key applied for at platform.deepseek.com/api_keys.
- **Model naming with stable aliases (A).** Models `deepseek-v4-flash`, `deepseek-v4-pro`, `deepseek-v4-flash-vision-exp`; "The deepseek-v4-flash model has been updated to DeepSeek-V4-Flash-0731… The calling method remains unchanged — simply use deepseek-v4-flash… to access the latest version." — stable public name resolving to an updated dated snapshot.
- **Invocation shape (A).** Chat API with messages array, streaming toggle, thinking mode, reasoning-effort parameter; SDK examples in Python/Node via the OpenAI SDK pointed at the DeepSeek base URL.
- **Limits on a concurrency axis (A).** "Rate Limit & Isolation" page: per-model concurrency limits per account; "A request counts as one concurrent connection from the time it is sent until the model response is complete"; limits calculated at account level regardless of which API key; HTTP 429 when exceeded. Higher concurrency via a "capacity expansion request" form ("We will match the appropriate concurrency based on your actual business needs. There is no additional cost for capacity expansion.").
- **Caller-side user attribution (A).** A `user_id` request parameter for "Content Safety Isolation", "KVCache Isolation", and "Scheduling Isolation" of the caller's end users under one account — with per-user concurrency when quotas are expanded.
- **Long-request handling (A).** Keep-alive mechanism: empty lines (non-streaming) or SSE keep-alive comments (streaming) while inference runs; server closes the connection if inference has not started within a stated window (specific duration recorded here only).
- **Guide corpus (A).** Vision, Thinking Mode, Multi-round Conversation, Chat Prefix Completion (Beta), FIM Completion (Beta), JSON Output, Tool Calls, Files API, Context Caching, Responses API usage, Anthropic API usage; Error Codes page; Token & Token Usage page; Models & Pricing page; Change Log / News for model updates.
- **Agent-tool backend posture (A).** "The DeepSeek API is supported by many popular AI agent and coding assistant tools. If you use tools like Claude Code, GitHub Copilot, or OpenCode, you can use DeepSeek as the backend model directly — no code required."

## Product D — Anthropic (navigation-level only)

### Key observations (weak evidence — structure only)

- **Surface split (A, nav).** claude.com presents the consumer product (Claude app, Claude Code) and a distinct "Platform" area: "Build on Claude — Overview (/platform/api)", "Developer docs (platform.claude.com/docs)", "Console login (platform.claude.com)", "Pricing (/pricing#api)", "Anthropic Academy". The developer platform is a separate logged-in console surface with its own docs and pricing.
- **Model families presented by tier names (A, nav).** Models listed as Opus / Sonnet / Haiku plus research models — a small, tiered first-party model line.
- **Partner-hosting channels (A, nav).** Footer links: "Claude on AWS", "Google Cloud", "Microsoft Foundry", plus a "Regional compliance" page — first-party models also reachable through cloud partners.
- **Terms split (A, nav).** Separate "Terms of service: Commercial" and "Terms of service: Consumer" — the commercial (API) relationship is contractually distinct from the consumer one.
- **Not observed (limitation).** All operational mechanics (keys, limits, endpoints, playground, model lifecycle specifics) are behind the region-blocked docs/console and are NOT asserted anywhere in this pass.

## Product E — Google Gemini API (unreachable)

- Named in the sample for market representation; ai.google.dev unreachable after repeated attempts (transport errors/timeouts). **No first-hand claims about Gemini API/Vertex AI are made in this pass.** The hyperscaler first-party-model-API posture is covered structurally via the sibling ai-model-hosting-platform pass's already-ratified hyperscaler-convergence note.

## Boundary Probe — OpenRouter (aggregator question)

- **What it is (A).** "OpenRouter gives you access to hundreds of AI models through a single API endpoint. It handles fallbacks automatically and picks the most cost-effective option for each request." OpenAI-compatible endpoint (`/api/v1/chat/completions`); OpenAI SDK drop-in; its own API keys; credit-balance billing (its own); model catalog by slug across providers (`~openai/gpt-latest`, `~anthropic/claude-sonnet-latest`); "latest alias" routing that resolves to the newest upstream model; client SDKs and an Agent SDK.
- **Whose models (A).** The catalog is other providers' models (OpenAI, Anthropic, and others). OpenRouter authors none of them.
- **Verdict for this pass.** Developer-facing model access with unified API + own billing — the surface a developer sees resembles a model API platform. Structurally, however: model provenance is third-party (fails this Type's first-party leg) and the platform makes per-request upstream selection/fallback decisions on the path (the gateway pass's own defining property). OpenRouter-class aggregators therefore sit on the **aggregation pole of the AI Gateway / model-routing family**, not in Model API Platform — refining the gateway pass's hunch ("likely sit on the model-API side"): they face developers like model APIs but fail the provenance test that separates this Type from hosting/gateway. See Boundary Findings.

---

## Cross-product Comparison

| Aspect | OpenAI | Cohere | DeepSeek | Anthropic (nav only) |
|---|---|---|---|---|
| First-party models served | yes (A) | yes (A) | yes (A) | yes (nav) |
| API schema posture | own schema(s); multiple API generations (Chat Completions, Responses) (A) | own endpoint families (Chat/Embed/Rerank/Parse/ASR/Tokenize) (A) | OpenAI- and Anthropic-compatible formats (A) | own API (docs unreachable) |
| Developer identity container | organization + project; org verification (A) | dashboard account; trial vs production keys (A) | account (+ caller-side user_id layer) (A) | console (nav) |
| API keys | create/manage/delete; permission levels (A) | trial/production key classes (A) | key from platform console (A) | unverified |
| Limit axis | requests/tokens per period, per model, org+project scope; sub-interval enforcement (A) | per-endpoint per-model req/min or inputs/min, trial vs production (A) | per-model **concurrency** per account; capacity-expansion requests (A) | unverified |
| Tier/upgrade path | automatic usage-tier graduation with spending; enterprise Scale Tier (A) | trial → production key upgrade; sales contact for newest models (A) | capacity expansion form, no extra cost (A) | unverified |
| Billing | prepaid credits; spend limits org/project; invoices (A) | production keys paid; pricing docs (A) | Models & Pricing page; usage page (A) | API pricing page (nav) |
| Usage visibility | Usage Dashboard (tokens, project filters, exports); Service Health (A) | status page; dashboard implied by key management (A) | token-usage page; error codes (A) | unverified |
| Playground | Chat Playground; parity-with-API articles (A) | playground (dashboard URL) (A) | not observed | unverified |
| Model versioning | legacy-endpoint migration guides; knowledge cutoffs (A) | Live/Deprecated/Retired statuses with dates; aliases (A) | stable alias → dated snapshot updates (A) | unverified |
| Fine-tuning | fine-tuning + RFT billing guides (A) | "train a model to tune it" + EmbedJob (A) | not observed | unverified |
| Multi-channel distribution | Bedrock Responses-API implementation for OpenAI models (A) | SageMaker/Bedrock/Azure/Oracle + own platform (A) | not observed | AWS/GCP/Foundry partner pages (nav) |
| Open-weight dual posture | gpt-oss collection (A) | Tiny Aya on Hugging Face (A) | not observed in fetched docs | unverified |
| Consumer sibling surface | ChatGPT (footer pairing) (A) | none observed | none observed | Claude app (nav) |
| Compliance/security surface | BAA, data residency (US/EU), IP allowlisting, mTLS, SSO/SCIM, audit-logs API (A) | go-live acknowledgments (terms/model cards/data statement); sensitive-use-case review (A) | user_id content-safety isolation (A) | regional-compliance page (nav) |
| Status/incident comms | status.openai.com (footer) (A) | status.cohere.ai with subscriptions (A) | not observed (FAQ/error codes instead) | status.anthropic.com (nav) |

### Cross-product commonalities (Layer B)

1. First-party models are the product; the platform's identity is the model developer.
2. Programmatic API access under account-issued keys, with the account (org/dashboard/console) as the billing and limit container.
3. Documented request/response schema with SDKs; developer onboarding corpus (quickstarts/tutorials).
4. Usage limits bound at the account level, enforced at request time (429-class errors), with a defined path to more capacity (tiers, upgrades, expansion requests, sales contact).
5. Metered usage attributed to the account and billed (prepaid credits, paid production keys, pricing pages).
6. Model catalog documentation: per-model capabilities/context/modality, snapshot/version naming, deprecation signals.
7. An interactive try-it surface beside the API (playground) — observed in 2/3 deep samples, absent-observed in 1; held Common, not Core.
8. Model/endpoint lifecycle management as an explicit operation (deprecation, migration, changelog).
9. Operational surfaces: status page/incidents; usage dashboards; error-code references.
10. Policy/compliance layer: usage policy, terms acknowledgment, data-handling controls; enterprise security surfaces (residency, BAA, SSO) at the enterprise pole.

### Divergences (feed L2/L3)

- Limit axis differs structurally: throughput-per-period (OpenAI, Cohere) vs concurrency (DeepSeek) → axis is a variant, bounded account-level usage is the invariant.
- Schema posture differs: proprietary schemas vs compatibility-first (DeepSeek's OpenAI/Anthropic-compatible formats) → variant.
- Distribution posture differs: first-party-only vs formalized multi-cloud channels (Cohere explicit; OpenAI Bedrock article; Anthropic partner pages) → variant on top of the first-party platform.
- Commercial posture differs: free trial tier (Cohere evaluation keys), prepaid credits (OpenAI), contact-sales gates for newest models (Cohere) → variant.
- Consumer sibling presence differs → variant.

---

## Canonical Model (L0)

**The Type is: the model developer's own metered serving surface — a first-party model line, served terminally by its author, exposed to developers under bounded programmatic access.**

Three jointly-held, load-bearing structures (Layer C; removal tests applied):

1. **First-party models as the product of record.** The operator develops the models it serves; the model line — families, versions, roadmap — is the operator's own product, and the platform's value proposition is the models' capabilities. Remove → AI Model Hosting Platform (models from other origins), aggregator/gateway (others' models routed), or a bare model publisher (weights released, nothing served).

2. **Terminal, metered serving operated by the model developer.** The platform itself operates the inference serving behind its own API endpoints; the request path ends at the operator (no upstream model provider); usage is measured and attributed to developer accounts and bounded by account-level limits enforced at request time. Remove → gateway/aggregator/reseller (someone else serves); remove metering/bounding → a free demo, not a platform.

3. **Developer-facing programmatic access surface.** Access is programmatic and developer-identified (API keys, account containers) under a documented request/response schema (SDKs, reference docs); the caller integrates model calls into its own software. Remove → a consumer AI product (same models, chat surface) or an internal-only service.

Jointly-held logic (why each pair without the third fails):

- 1 without 2 = model publisher (open-weight release, research artifact) — no service.
- 1 without 3 = consumer AI product / internal service — no developer surface.
- 2 without 1 = hosting platform / aggregator — serves models it did not author.
- 3 without 1+2 = an empty developer portal — nothing to call.
- 1+3 without 2 = reselling/licensing own models through others' serving — a distribution channel, not the platform (and the observed multi-channel posture always sits ON TOP of a first-party platform, never replaces it).
- 2+3 without 1 = the hosting sibling (ratified boundary).

## L1 — Common Mature Structure (standard capabilities; not definitional)

- **Model catalog + model pages** — per-model capabilities, modalities, context/size characteristics, pricing basis, endpoint mapping.
- **Playground / interactive console** — try the models before writing code; same models as the API.
- **SDKs + code snippets + quickstarts** — several languages; onboarding tutorial corpus.
- **Rate limits + tier/upgrade machinery** — account-bounded throughput or concurrency; explicit upgrade paths (tier graduation, key-class upgrade, capacity-expansion requests, sales contact).
- **Usage & cost visibility** — usage dashboards (requests, tokens, cost, exports), service-health/status pages, error-code references.
- **Account containers & key management** — org/project/team scoping; key issuance, permissions, rotation; enterprise SSO/SCIM at the enterprise pole.
- **Model versioning & lifecycle** — dated snapshots, stable aliases, deprecation notices, migration guides, changelogs.
- **Endpoint families by capability** — text/chat, embeddings, image, audio/ASR, rerank, moderation, batch; streaming; tool/function calling; structured/JSON output; long-running and async modes.
- **Fine-tuning/customization** — training or tuning jobs producing deployable custom models (observed 2/3 deep samples; held Common).
- **Files/context services** — file storage, caching, retrieval-adjacent capabilities as API services.

## L2 — Variant / Optional Structure

- **Schema posture** — proprietary API schemas vs compatibility-first (implementing OpenAI/Anthropic-compatible formats so existing SDKs work by base-URL swap).
- **Limit axis** — throughput-per-period vs concurrent-connections vs other metered axes; sub-interval enforcement vs average-based.
- **Commercial model** — free trial key classes, prepaid credits, postpaid invoices, contact-sales production gates, enterprise capacity purchases.
- **Consumer sibling** — a consumer chat product on the same models (present at the largest labs; absent in specialist poles).
- **Open-weight dual posture** — publishing weights publicly while also serving them commercially.
- **Multi-channel distribution** — first-party models additionally served through cloud partner platforms (Bedrock/SageMaker/Azure/Oracle/Foundry-class), usually under partner-operated deployments.
- **Modality breadth** — text-first, multimodal (vision/audio), embeddings/rerank-specialist, document-parsing.
- **Enterprise posture** — data residency, BAA/HIPAA, mTLS, IP allowlisting, audit logs, regional compliance.
- **Regional/geographic posture** — region-blocked consumer surfaces with separate commercial terms; region-specialized model variants.

## L3 — Vendor-specific Structure (research notes only; NOT in final document)

- OpenAI: automatic usage-tier graduation tied to spend; Scale Tier token-capacity purchases for enterprise; the Chat Completions ↔ Responses API duality and Assistants v1→v2 migration history; Moderation endpoint free of charge; safety-identifier parameter; org/project spend limits with monthly reset; "gpt-oss" open-weight line; prepaid-credit error taxonomy (credit_balance_exhausted etc.).
- Cohere: evaluation-key vs production-key dichotomy; sensitive-use-case manual safety review with a stated review SLA; per-endpoint/per-model trial-vs-production limit tables; "Contact sales" rate limits for newest model variants; model statuses "Live/Deprecated/Retired" with dates; Tiny Aya open-weight availability on Hugging Face; formal multi-cloud distribution with per-platform model-ID tables.
- DeepSeek: OpenAI/Anthropic dual-format compatibility (two base URLs); concurrency-only limit axis; free capacity-expansion request flow; `user_id` triple isolation (content safety / KVCache / scheduling); keep-alive mechanism with a stated no-inference connection window; chat-prefix and FIM completion beta endpoints.
- OpenRouter (probe): credit-balance billing over third-party models; `~provider/model` slug space; latest-alias resolution; automatic cost-based provider selection.

## Rejected Findings (checked and NOT promoted to the core)

- **"Token-based pricing" as definitional.** Rejected: token metering is the current dominant basis for text models, but the same products meter embeddings per input, images per image, audio per minute (Cohere's tables; OpenAI image/audio articles); pre-LLM first-party model APIs priced per unit/request. Canonical: *metered usage*, axis varies.
- **"OpenAI-compatible schema" as definitional.** Rejected: it is one variant posture (DeepSeek adopts it; OpenAI/Cohere define their own). Also self-undermining — the compatibility target is a product of this Type, so compatibility cannot be the invariant.
- **"Chat/messages request shape" as definitional.** Rejected by the historical check: pre-LLM first-party model APIs (vision, speech, translation, language-understanding services) had no chat shape. The request shape follows the model's modality.
- **"LLM/generative models" as definitional.** Rejected by the same check — the first-party-model-API structure predates generative LLMs (cloud AI service APIs of the 2010s: first-party vision/speech/language models, metered developer access, keys, quotas). The Type is LLM-era-dominant, not LLM-defined.
- **"Self-serve trial keys" as definitional.** Rejected: observed in Cohere (evaluation keys) and consistent with enterprise contact-sales poles; commercial on-ramp is a variant.
- **"Playground" as definitional.** Held Common (observed in 2/3 deep samples only; it is a surface, not the product).
- **"Multi-cloud distribution" as definitional.** Rejected: it is an add-on channel; the first-party platform is the defining surface (removal test: strip partner channels → the Type is fully intact; strip the first-party platform → the product is a hosting-platform customer, not this Type).

## Historical / Market-Sample Check (§24 check applied)

- **Pre-LLM first-party model APIs** (2010s cloud "AI as a service" — vision/speech/translation/language APIs operated by their model developers, with keys, quotas, per-unit pricing, try-it consoles): satisfy all three L0 legs. The definition therefore must not name tokens, chat, generative models, or transformers. ✔
- **Open-weights developers** (publish weights AND serve a commercial API): satisfy the core; the open-weight release is a variant posture, and serving remains first-party. ✔
- **Platform-native/regional challengers** (compatibility-first APIs aimed at existing SDK ecosystems): satisfy the core; schema posture is a variant. ✔
- **Hyperscalers** (serve own models and third-party models side by side): the first-party surface satisfies the core; the third-party catalog side belongs to the hosting sibling — the documented convergence is a gradient at one operator, not a collapse of the two Types. ✔
- **Pre-cloud form** (a vendor serving its own models through a licensed/per-call API line): conceptually satisfies; named no specific vendor per source limits.

The definition survives all checks without era-specific machinery.

## Boundary Findings

### vs AI Model Hosting Platform (§13 sibling) — FLAG DISCHARGED

Ratified discriminator (from the hosting pass, confirmed from this side): **model provenance relative to the platform operator.** This Type serves models the operator authored (first-party model line as product of record); the hosting sibling operates serving for models whose creation it does not own (third-party open weights, community models, customer-uploaded/fine-tuned weights). Both expose metered model APIs; the load-bearing difference is who the models belong to and whose product roadmap the model catalog expresses. Convergence documented at the hyperscaler edge (one operator serving its own models next to third-party models — my sample's Google row is the same gradient the hosting pass recorded for Bedrock) — a gradient, not a wall. Additional corroboration from this side: first-party APIs also distribute through hosting channels (Cohere's SageMaker/Bedrock/Azure/Oracle tables; OpenAI's Bedrock Responses-API article; Anthropic's partner pages) — distribution does not move a product out of this Type, and hosting those models does not make the host the model's developer. Keep-both; joint-review flag satisfied.

### vs AI Gateway / Model Routing Platform (§13 sibling) — FLAG DISCHARGED (with refinement)

Structural test: **terminal vs intermediary.** This Type's endpoint is the end of the request path — the operator serves inference for its own models; there is no upstream model provider behind it. The gateway runs no inference and fronts provider APIs as configurable upstreams. The flagged open question — whether OpenRouter-class aggregators sit on "the model-API side" — is resolved from direct evidence: aggregators present a developer-facing, unified, usage-billed model-access surface (which is why the hunch existed), but they (a) author none of the models and (b) make per-request upstream selection/fallback/cost decisions — this Type's defining posture is the opposite on both counts. Verdict: aggregators = the **aggregation pole of the gateway family** (where the gateway pass already placed managed unified-API gateways), NOT a variant of this Type. Refinement recorded: "faces developers like a model API" is a surface property; "serves its own models terminally" is the structural property. Keep-both; no directory change.

### vs API Management Platform (§13 sibling) — FLAG DISCHARGED

Confirmed gradient: API-management platforms govern access to model endpoints as one more class of managed backend (routing, keys, quotas, analytics over any API); this Type's product **is** the model inference itself — the endpoint exists because the operator trains and serves models, not because it manages backends. A model API platform can sit behind API-management machinery and can consume gateway services; that is implementation topology, not identity. Keep-both.

### vs LLM Application Development Platform (§13 sibling) — FORWARD FLAG DISCHARGED

Substrate relationship confirmed from this side: the model API platform owns model access and inference; the LLM-app-dev Type builds applications on top of that substrate (developer-owned control flow, orchestration, prompts, RAG, agents). The straddle runs in both directions as packaging: model API platforms bundle developer machinery (playgrounds, fine-tuning, eval/feedback data controls, files, batch) — OpenAI's own platform articles show app-adjacent machinery inside the API platform; cloud suites sell model access and app machinery together. Packaging, not boundary collapse: remove the app machinery → the model API platform is fully intact; remove the first-party models → an app-dev platform with nothing native underneath. Layering stands as the llm-app-dev pass recorded.

### vs consumer AI assistant products (Enterprise AI Assistant / consumer chat)

Same models, different surface and different user: a consumer/assistant product converses with end users; this Type exposes programmatic access to developers integrating the models into their own software. Both surfaces can be operated by the same company on the same models (observed at OpenAI and Anthropic) — the split is so structural that these vendors run separate consoles, separate terms (commercial vs consumer), and separate pricing anchors. The API surface is this Type; the assistant surface is a different Application Type.

### vs Model Registry (§13 sibling)

A registry catalogs and governs model versions inside an ML lifecycle and does not operate serving or sell access. This Type's catalog documents the operator's own commercially served models. Distinct.

### "去掉什么就变成另一个 Type" summary

- Remove first-party authorship → AI Model Hosting Platform (or aggregator/gateway).
- Remove terminal serving (upstreams appear) → AI Gateway family.
- Remove the developer/programmatic surface → consumer AI product.
- Remove metering/bounding → a demo or research artifact, not a platform.
- Remove the models entirely (keep keys/quotas/analytics over any backend) → API Management Platform.

## Uncertainties

1. **Anthropic operational mechanics unverified** (region-blocked content ×2). Everything attributed to Anthropic in this pass is navigation-level (surface split, model tier naming, partner channels, commercial/consumer terms split). No Anthropic-specific rules, limits, or lifecycle claims are made anywhere.
2. **Google Gemini API not observed** (unreachable ×3). The hyperscaler first-party surface is covered structurally via the ratified hosting-pass convergence note; no Google-specific claims made.
3. **OpenAI docs site unreachable** (403) — OpenAI evidence is Help-Center-grade (articles + nav). Endpoint specifics beyond those named in help articles (e.g., exact current model names, pricing) are not asserted.
4. **Playground universality** — observed in 2/3 deep samples; treated as Common, not Core. DeepSeek's playground status unknown.
5. **Fine-tuning universality** — observed 2/3 deep samples (OpenAI, Cohere); treated as Common.
6. **Free/trial tier universality** — Cohere documents trial keys explicitly; OpenAI's help center documents prepaid credits without confirming a free tier; treated as Common-not-Core.
7. **Mistral, xAI** unreachable — the open-weights dual posture and additional lab poles rest on Cohere/OpenAI (gpt-oss) documentation plus general market structure; no claims from memory.
8. Whether the "aggregation pole" of the gateway family deserves its own directory leaf (OpenRouter-class) is a taxonomy-owner question — recorded, no change made.

## Final Synthesis

The Model API Platform is the **model developer's own serving surface**: the company that builds AI models operates metered, bounded, programmatic access to those models as its product. Its world is organized around a first-party model line (families, versions, lifecycle), terminal API endpoints operated by the author, developer identities (accounts, keys) that carry metering and limits, and a developer-supporting surface set (console, playground, docs, status, changelog). Usage is bounded at request time by account-level limits whose axis varies by product (throughput or concurrency); model versions are pinned and deprecated explicitly; commercial terms, data-handling controls, and policy gates wrap the whole.

Everything else commonly bundled — playgrounds, fine-tuning, batch, files, compatibility schemas, consumer sibling apps, open-weight releases, multi-cloud distribution channels, enterprise security postures — is standard capability or variant, not definition.

Boundaries: provenance separates it from hosting (own models vs others'); terminality separates it from gateways (including aggregators, which fail provenance and add upstream selection); product identity (the inference itself vs managed backends) separates it from API management; layer position separates it from LLM application development (substrate vs construction); surface separates it from consumer AI products.
