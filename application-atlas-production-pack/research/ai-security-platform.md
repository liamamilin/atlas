# Research Notes — AI Security Platform

Research date: **2026-09-06**

## Research Goal

Understand what an **AI Security Platform** (directory §15, Cybersecurity, Identity & Trust) actually is as an Application Type: what objects exist inside it, what its users do, how the security work flows, and where its boundary lies against neighboring Types — especially **AI Safety / Guardrail Platform** (§13), with which a joint review was flagged by the `ai-safety-guardrail-platform` research pass (Check Point/Lakera straddle).

## Initial Boundary (hypothesis before research)

An AI Security Platform is software that runs the **security program over an organization's own AI estate**: it identifies the AI assets an organization runs (models, AI applications, agents, AI services, ML pipeline artifacts), assesses them for AI-specific weaknesses and attacks, detects attacks against AI systems where it covers runtime, and drives the resulting security findings through a security-team response loop.

Expected confusion surfaces:

- **AI Safety / Guardrail Platform** — per-request content screening on the LLM I/O path vs estate-level security program. (Joint review pending.)
- **AI Governance Platform** — registry/review/policy process level vs security assessment and attack response.
- **Application Security Platform / SAST / SCA** — conventional app/code asset security vs AI-native assets and threat classes.
- **CSPM / CNAPP** — cloud posture over cloud resources; AI-SPM is emerging as a module of it.
- **Vulnerability Management / Attack Surface Management / SBOM Management** — generic findings/EASM/software-supply-chain machinery vs AI-specific instances.
- **Model Registry (§13)** — ML lifecycle registry as inventory *source*, not security assessment.
- Naming trap: "AI security" can mean *security for AI systems* (this Type) or *security products that use AI internally* (EDR with ML detection — not this Type).

## Research Questions

1. What are the core objects? (AI asset inventory entries; assessments; findings; targets/tests; policies; response items)
2. How is the AI estate discovered — cloud connectors, registries, code-to-cloud scanning, traffic observation, manual registration? What is "shadow AI" discovery?
3. What assessment families exist: posture checks (misconfigurations/exposure/identity), artifact & supply-chain scanning (model files, AI libraries), adversarial/red-team testing, runtime attack detection?
4. What does a finding look like: severity, framework mapping (MITRE ATLAS, OWASP), remediation guidance, false-positive handling?
5. How does the response loop work — triage, workflow automation, exports (SIEM/SOAR, ticketing, CI/CD)?
6. What operational surfaces exist (inventories, test consoles, framework advisers, reports, dashboards, CLIs/SDKs)?
7. What delivery forms exist (pure-play platform, cloud-suite module, testing service, traffic/gateway layer) — variants of one Type or separate Types?
8. Where exactly does this Type end and the Guardrail Type begin at runtime?

## Representative Products

Selected for market representation, different product philosophies, different customer tiers, and documentation accessibility:

| Product | Philosophy / tier | Form |
|---|---|---|
| Microsoft Defender for Cloud — AI security posture management (AI-SPM) | hyperscaler, posture-first, security-team console | module of a cloud security plan |
| HiddenLayer AISec Platform | pure-play "comprehensive AI security platform", enterprise | standalone platform (discovery + supply chain + attack simulation + runtime) |
| Mindgard | red-team / continuous AI security testing first | testing platform (CLI/SDK/web) with findings + remediation loop |
| Prompt Security (now part of SentinelOne) | GenAI traffic/app security layer, agentic tooling | platform within an endpoint-security vendor's suite |
| Check Point (Lakera) | straddle case: Guard (runtime screening) + Red (red teaming) | boundary evidence from prior pass |

## Sources

Fetched live 2026-09-06:

- Microsoft Learn: https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture — fetched OK (evidence layer A, operational documentation)
- Mindgard docs: https://docs.mindgard.ai/ (root + llms.txt index), /user-guide/test-results.md, /user-guide/plan-ai-risk-management.md — fetched OK (layer A)
- HiddenLayer: https://hiddenlayer.com/aisec-platform/ — fetched OK (official product page; module structure and positioning — Tier 2 strength; docs site docs.hiddenlayer.com unreachable)
- Prompt Security: https://www.prompt.security/ — fetched OK (official site; acquisition notice + open-source tools + glossary; **docs.prompt.security unreachable after transport error; sentinelone.com platform page returned 403** — assertions kept weak)
- Prior pass (ai-safety-guardrail-platform, 2026-09-06): Check Point AI Guardrails (Lakera) docs at docs.lakera.ai — reused for the boundary analysis only.

Abandoned per network-restriction rule (1–2 failures → stop): docs.hiddenlayer.com, docs.prompt.security, docs.protectai.com (401), paloaltonetworks.com/prisma/ai-access-security (404), sentinelone.com platform page (403), protectai.com (403). Protect AI / Prisma AIRS therefore **not** usable as a sampled product; nothing about it is asserted from memory.

## Product Observations

### Microsoft Defender for Cloud — AI security posture management (layer A)

- Positioning: Defender CSPM "secures generative AI applications and AI agents throughout their entire lifecycle" across multicloud (Azure, AWS, GCP incl. Vertex AI).
- **AI BOM discovery**: "Discovering the generative AI Bill of Materials (AI BOM), which includes application components, data, and AI artifacts from code to cloud."
- **Continuous discovery of deployed AI workloads** across: Azure OpenAI Service, Azure AI Foundry, Azure Machine Learning, Amazon Bedrock, Google Vertex AI.
- **Dependency vulnerabilities**: discovers vulnerabilities in GenAI library dependencies (TensorFlow, PyTorch, LangChain) by scanning source code; IaC misconfigurations; container image vulnerabilities.
- **AI agent discovery (Preview)**: agent inventory in the Microsoft Defender portal with per-agent security status; noted organizational change — effective 2026-07-01, agent discovery/posture for Foundry and third-party cloud agents moves to a separate Microsoft Agent 365 license (Defender CSPM continues discovering Foundry accounts/projects). [Vendor-specific organizational detail; shows the agentic scope is still fluid.]
- **Recommendations**: posture assessment issues recommendations on identity, data security, internet exposure; example IaC AI security checks: use private endpoints, restrict AI service endpoints, use managed identity, use identity-based authentication for AI service accounts.
- **Attack path analysis**: identifies weaknesses in AI workloads — exposure during grounding of models to data, fine-tuning datasets; externally reachable AI endpoints with weak/missing authentication; multicloud-spanning paths; follow-up with recommendations.
- Externally reachable AI endpoints highlighted "so teams can enforce strong authentication and least privilege identities".
- No runtime LLM I/O screening in this document — pure posture/assessment layer.

### HiddenLayer AISec Platform (layer A for positioning/module structure; product-page level)

- Positioning: "The Most Comprehensive AI Security Platform — Discover every model. Secure every workflow. Prevent AI attacks."
- **Four platform modules**:
  - **AI Discovery** — "Gain visibility into AI assets across environments to eliminate shadow AI."
  - **AI Supply Chain Security** — "Secure AI models before deployment by validating integrity and supply chain."
  - **AI Attack Simulation** — "Simulate real world AI attacks continuously to uncover weaknesses early."
  - **AI Runtime Security** — "Detect and respond to AI attacks without impacting performance in production."
- Use cases: model scanning ("malware, vulnerabilities, backdoors, and unknown components before they reach production"), red teaming ("continuously test AI systems against evolving attacks"), AI guardrails ("enforce policies that prevent prompt injection, data leakage, and unsafe AI behavior in real time" — note: guardrails appear here as a *use case inside* the security platform), agentic & MCP security ("prompt injection, unsafe tool use, and harmful autonomous actions"), agent harness security (coding agents).
- Governance & AI security posture: "organization wide visibility into every model, apply consistent governance rules, classify risk, and monitor posture".
- Claims: model-agnostic, agentless, zero training data, "without exposing intellectual property, weights, prompts, or customer data".
- Integrations: cloud, CI/CD, data platforms, SIEM/SOAR, API gateways, MLOps tools.
- Audiences: CISO, AI leaders, application developers; industries incl. financial services, US federal government, healthcare.
- Research arm: AI Threat Landscape reports, "Security Advisory" section for AI (SAI), NSPM-11 commentary.

### Mindgard (layer A)

- Positioning: continuous AI security testing ("Lets start securing your AI"); docs oriented to testing AI systems (models and chatbot applications) through an attack library.
- **Core objects**:
  - **Project** — container for testing work (list projects API; sharing projects).
  - **Test / test target** — a run of the attack library against a registered target (CLI, web, Burp integration, Python SDK); test history grouped per target; multi-turn tests.
  - **Finding** — first-class object with its own API (list findings for project, create finding, get finding by ID).
  - **Dataset** — attack datasets, AI safety datasets, custom prompts, CLI-generated custom datasets.
  - **Policy** — evaluation policy applied to tests; baseline policy by default; custom policies (regex refusal, policy violation) to tailor evaluation.
- **Reconnaissance** module: guardrails detection, system prompt extraction, tool discovery, input/output encoding, formatting, rendering — pre-test profiling of the target's protections and structure.
- **Observations** layer: input-in-output, empty output, LLM error, decode — signals feeding flagging.
- **Attack library**: LLM/ML attack techniques organized in families — jailbreaks (named techniques e.g. Crescendo, ActorAttack), prompt injection (encoding-based), violations (PromptAlignment, MaliciousGeneration).
- **Test results surfaces**:
  - **MITRE ATLAS Adviser** — all AI risks from all testing grouped by the MITRE ATLAS framework; exposure highlighted per technique.
  - Model test results page (history per target), test overview with model performance history (events vs flagged per test).
  - Test summary (attack surface covered); **flagged events by threat categories**; CSV export of attacks list.
  - Per-attack report: summary (success rate of attack attempts, techniques, potential impact), **framework mapping** (OWASP Top 25 and MITRE ATLAS), target details, **remediation recommendations**, event details (every interaction with inputs/outputs and layered observations; each event flagged or cleared based on Mindgard's internal evaluation and threat intelligence).
  - **False positive/negative tagging** by the user, which also feeds back to improve Mindgard's classification.
- **Remediation library**: per-technique guidance (output obfuscation, context windows, separate system instructions, model hardening, input restoration, differential privacy, filter outputs, implement guardrails, etc.).
- **Adoption model** (documented): PoC → initial visibility (most critical AI assets) → ongoing visibility (posture changes from app changes, model changes, or "new emerging AI vulnerabilities and exploit techniques") → triage & remediation workflow automation ("development teams are alerted and take action to triage and remediate new relevant AI security risks").
- Workflow integrations, reporting, enterprise setup documented.

### Prompt Security from SentinelOne (layer A for the thin facts above; weak overall)

- The site now presents as "Prompt Security | From SentinelOne" — the product is being folded into the SentinelOne platform ("Securing AI / Prompt"). [Consolidation fact, not operational detail.]
- Open-source tools: **ps-fuzz** ("Test and harden your system prompt against dynamic LLM-based attacks. Supports 16 providers and 16 attack types."), **ClawSec** ("Security skill suite for AI agents. Drift detection, live recommendations, automated audits, and skill integrity verification."), **OneClaw** ("Track and analyze OpenClaw deployments across your organization. Visibility into agent activity, usage patterns, and security insights.").
- Live usage widget (self-reported): prompts/day tracked in mid-size orgs; "Top Guardrails Triggered" (customer guardrails, topics detector, sensitive data, secrets); prompt injection flagging — indicates the product layer monitors AI traffic and triggers guardrails/policies.
- Glossary defines an AI gateway as "a centralized layer between an organization's users or applications and the AI models or services they call, letting security teams monitor, control, and secure that traffic from one place" — product philosophy: secure the AI traffic plane org-wide.
- **Limitation**: platform documentation not reachable; operational structure (consoles, findings model, deployment surfaces) NOT evidenced — no precise claims made.

### Check Point (Lakera) — straddle evidence (reused from prior pass, layer A)

- docs.lakera.ai documents **AI Guardrails** (real-time AI application firewall screening LLM inputs/outputs; policy per project; detect/enforce modes) — that function is the AI Safety / Guardrail Platform Type per the prior pass.
- The same vendor's offering set includes an **AI Red Teaming offering** adjacent to the guardrails product — i.e., the vendor spans both the runtime screening slice (other Type) and the estate-level security testing (this Type). This is the concrete straddle that motivated the joint review.

## Cross-product Comparison

| Dimension | Microsoft Defender AI-SPM | HiddenLayer AISec | Mindgard | Prompt Security (SentinelOne) | Check Point/Lakera (straddle) |
|---|---|---|---|---|---|
| Primary protected object | enterprise GenAI apps + agents + AI libraries across cloud services | "every model and every AI workflow" (models, pipelines, agentic systems) | registered test targets (models, chatbot apps, agents) | GenAI app traffic org-wide + agents | LLM applications (runtime) + AI systems (red team offering) |
| Estate discovery | continuous discovery across Azure OpenAI/Foundry/AzureML/Bedrock/Vertex; AI BOM from code to cloud | AI Discovery module; "living inventory… including shadow AI" | manual/target registration (projects); no estate discovery claimed in fetched docs | traffic observation (prompts/day tracked); OneClaw agent-deployment tracking | not the guardrails product's job; Red offering works on engagements |
| Posture/misconfig | recommendations (identity/data/exposure), IaC AI checks, attack path analysis | governance & posture ("classify risk, monitor posture") | — (testing-first) | — | — |
| Artifact/supply-chain | GenAI library dependency vulns via source/IaC/container scanning | AI Supply Chain Security; model scanning (malware, backdoors, unknown components) | — | — | — |
| Adversarial testing | — (not in fetched doc) | AI Attack Simulation module; red teaming use case | core: attack library (jailbreaks/injection/violations), recon, datasets, policies, multi-turn | ps-fuzz (system prompt hardening) | Lakera Red |
| Findings model | recommendations + attack paths | risk classification, monitoring | flagged events → findings (first-class API), success rate, framework mapping (MITRE ATLAS adviser; OWASP), false-positive feedback | injection/sensitive-data/secrets flags in traffic | flagged true/false per request (guardrails side) |
| Remediation guidance | remediation via recommendations | posture monitoring (guidance not evidenced) | remediation library per technique; remediation section in every report | — | — |
| Runtime attack detection | — (not in fetched doc) | AI Runtime Security module | — (testing-time) | traffic monitoring with guardrail triggering | core of the guardrails product |
| Response loop | fix recommendations; (presumably) Defender ecosystem | SIEM/SOAR integrations | triage & remediation workflow automation stage; CSV/exports; workflow integrations | SentinelOne platform handoff (not evidenced) | app decides per request (guardrails side) |
| Delivery form | plan/module of Defender for Cloud | standalone platform | SaaS testing platform + CLI/SDK/Burp/SDK | platform of an endpoint-security vendor | screening API + red team service |
| Buyer | cloud security teams (CSPM audience) | CISO/security teams; FS/federal/healthcare | AppSec/dev teams + security | security teams via SentinelOne | app/dev + security teams |
| AI-specific vocabulary | AI BOM, grounding, fine-tuning, agents | model backdoors, agentic/MCP, agent harness | jailbreaks, prompt injection, ATLAS/OWASP mapping | guardrails, prompt injection, agent skills | prompt attacks, guardrail policies |

## Canonical Abstraction

### L0 — Defining Invariant

```text
AI estate: the organization's AI systems held as identified, security-managed assets
└── AI-specific security assessment of those assets
    (posture of AI services / integrity of AI artifacts / adversarial testing / attack detection — any subset)
    └── Security findings (weaknesses, exposures, attacks — attributable to identified assets)
        └── Security-team response loop (triage → prioritize → remediate/mitigate)
```

Three properties; remove any one and the product stops being this Type:

1. **The AI estate as the managed object** — the system knows *which* AI systems it is responsible for (auto-discovered cloud AI workloads, a living model inventory, registered test targets, observed AI traffic/deployments). Findings must land on identified AI assets. Without this, the product is a point tool (a scanner, a fuzzer) or the per-request screening slice.
2. **AI-specific security assessment** — evaluation against the AI-native threat space (model/artifact integrity, AI service misconfiguration and exposure, adversarial jailbreak/injection techniques, agent tool abuse). Scanning a model file for embedded malware or red-teaming a chatbot with an attack library is assessment of a kind conventional vulnerability management does not perform. Without AI-specificity, the product is generic asset inventory / cloud posture / appsec.
3. **Findings feeding a security response loop** — results materialize as security findings (typically severity- or framework-mapped) that security and engineering teams triage and act on (fix configuration, patch/replace artifact, harden prompts, tighten policy, respond to attack). Without this, the product is research tooling or a governance registry.

Deliberately NOT in L0:

- **The assessment family mix** — posture-only (Microsoft's fetched core), testing-only (Mindgard), scanning+runtime (HiddenLayer), traffic-monitoring (Prompt) are all recognizably this Type; the families are the common structure, not the invariant.
- **Runtime attack detection / enforcement** — posture-only and testing-only products remain the Type without it.
- **Estate discovery mechanics** — discovery vs registration vs traffic observation both satisfy "identified assets".
- **GenAI/LLM specificity** — the estate is *AI systems* generally; LLM-centricity is a current market weighting, not the definition (pre-LLM model scanning/adversarial-ML testing products fit the same structure).

### L1 — Common Mature Structure

- **Estate discovery / inventory**: connectors to cloud AI services (Azure OpenAI, Azure AI Foundry, Azure ML, Amazon Bedrock, Google Vertex AI observed in Microsoft; similar cloud integrations claimed by pure-plays), MLOps integrations, code-to-cloud inventory of AI components/data/artifacts ("AI bill of materials" terminology observed in Microsoft; the inventory concept is common, the BOM term is vendor usage), shadow-AI discovery (HiddenLayer, Prompt/OneClaw), agent inventories (Microsoft Preview, Prompt/OneClaw).
- **Posture assessment of AI assets**: misconfiguration/exposure/identity recommendations for AI services (private endpoints, endpoint restriction, managed identity, identity-based auth observed), attack-path analysis linking AI apps → data → identity (grounding/fine-tuning data exposure).
- **Artifact & supply-chain security**: scanning model files/artifacts for malware, backdoors, unknown/unsafe components; integrity validation before deployment; vulnerability scanning of AI library dependencies (TensorFlow/PyTorch/LangChain observed); AI BoM.
- **Adversarial testing / red teaming**: attack-technique libraries (jailbreaks, prompt injection, policy violations — Mindgard, layer A); registered test targets/projects; test datasets (incl. custom/generated); evaluation policies; reconnaissance of targets (guardrail detection, system-prompt extraction, tool discovery — Mindgard only in fetched evidence; treat as a product pattern, not a market invariant); multi-turn attack testing; per-attack success-rate reporting (Mindgard).
- **Findings model**: flagged/failed events → findings with severity/risk classification and framework mapping (MITRE ATLAS and OWASP mappings observed directly in Mindgard; ATLAS/OWASP are industry-standard reference vocabularies widely used in the market's material, though only one sample evidences the mapping machinery in fetched docs); false-positive/negative handling with feedback into detection quality (Mindgard, layer A).
- **Remediation support**: per-technique remediation guidance libraries; recommendations/fix guidance attached to findings.
- **Runtime monitoring & detection (where the product covers runtime)**: observation of AI traffic (prompt volume, injection/sensitive-data/secrets flags), attack detection against production AI, agent-activity monitoring; enforcement postures (guardrail triggering) exist alongside monitor-only postures.
- **Response-loop machinery**: triage/remediation workflow automation, alerts to dev/security teams, exports (CSV/attack lists), integrations with SIEM/SOAR, CI/CD, ticketing, API gateways, MLOps tooling.
- **Operational surfaces**: asset inventory views, posture recommendation/attack-path views, test consoles and result reports, framework advisers (ATLAS), dashboards, reporting (executive/compliance-facing), CLIs/SDKs/APIs.
- **Threat research/intelligence feed**: vendor research on AI threats (threat reports, advisories) feeding detection and context.

### L2 — Variant / Optional Structure

- **Center of gravity**: posture-first (cloud-suite module), supply-chain/scanning-first, testing/red-team-first, runtime-first; breadth ("comprehensive platform") vs depth.
- **Packaging**: standalone pure-play platform vs module of a broad security platform (cloud security plan, endpoint-security vendor suite) vs service-like engagement (red team offerings).
- **Estate emphasis**: GenAI/LLM applications vs classical ML pipelines/models vs agentic AI (agent inventories, MCP/tool security, agent-harness security for coding agents).
- **Deployment**: SaaS vs self-hosted/on-prem components; agentless vs sensor-based; model-vendor-hosted; handling of "we never see your weights/prompts" privacy postures.
- **Buyer/industry overlay**: enterprise security teams vs AppSec/dev teams; regulated-industry and government packaging (financial services, US federal, healthcare observed in marketing).
- **Framework/regulatory overlay**: MITRE ATLAS and OWASP mappings as common vocabulary; national-policy positioning appears in vendor material.
- **Adjacent bundled functions**: guardrails (runtime screening) as a use case inside the platform; AI governance features (policy/risk classification); AI threat intelligence; fuzzing tools.

### L3 — Vendor-specific (research notes only)

- Microsoft: Defender CSPM plan mechanics; exact IaC check list; AWS connector reconfiguration steps; AI agent discovery Preview and the 2026-07-01 transition of agent security posture to Microsoft Agent 365 licensing; diagram of lifecycle coverage.
- HiddenLayer: module names (AI Discovery / AI Supply Chain Security / AI Attack Simulation / AI Runtime Security); "model-agnostic, agentless, zero training data" claims; CISO-quote marketing structure; NSPM-11 commentary; $100M Series B.
- Mindgard: project/test/finding/dataset/policy object vocabulary; observation taxonomy (input_in_output, empty_output, llm_error, decode); recon categories; attack-technique names (Crescendo, ActorAttack, DevModeV2, Ascii85…); MITRE ATLAS Adviser; 4-stage adoption model; Burp integration; CLI/SDK surface.
- Prompt Security/SentinelOne: ps-fuzz ("16 providers / 16 attack types"), ClawSec, OneClaw; live usage widget ("3,500 prompts/day in a 500–1,000 employee org"); top-guardrails list.
- Check Point/Lakera: Guard (screening API, policies per project, detect/enforce, sensitivity L1–L4) vs Red (red teaming); docs.lakera.ai branding transition.

## Rejected Findings

- "AI Security Platform = AI-SPM" — rejected: AI-SPM (posture) is one assessment family; testing-first (Mindgard) and runtime-first (Prompt/HiddenLayer runtime) products without posture engines are still the Type.
- "Model scanning is the core" — rejected: posture-only and testing-only samples never scan artifacts in the fetched evidence; scanning is L1.
- "Red teaming is the core" — rejected: posture-first sample has none in the fetched doc.
- "Runtime detection/enforcement is the core" — rejected: two of four sampled products lack it in fetched evidence; enforcement belongs to the guardrail slice when done per-request.
- "This Type includes guardrails because vendors list guardrails as a use case" — rejected as a definition: guardrails inside an AI security platform are the *runtime enforcement slice* — the same function the AI Safety / Guardrail Platform Type is defined by. Bundling pattern, not invariant.
- "AI Security Platform = security products that use AI" — rejected: direction of protection is the discriminator (see Boundary Findings).
- Precise claims (module behaviors, agent-365 licensing details, usage statistics) — kept vendor-specific in research notes; none promoted to canonical prose.

## Historical / Market-Sample Check

The market is young (roughly 2023+) and consolidating (Lakera→Check Point, Robust Intelligence→Cisco, Protect AI→Palo Alto, Prompt Security→SentinelOne — the last two known from public reporting/vendor sites; the first two from prior research passes). Applying the "older / platform-native / differently positioned products" check:

- **Pre-LLM ML security practice**: scanning serialized model files for unsafe constructs and adversarial-robustness testing of vision models predate the LLM wave. Productized versions fit L0 exactly (identified models + AI-specific assessment + findings loop). Pure research libraries (adversarial-robustness toolkits) have no estate and no response loop — they are tooling *below* the platform Type. L0 therefore must not be defined by LLM-specific threats (jailbreaks, prompt injection) — those are today's attack-library contents, not the invariant. This mirrors the guardrail pass's decision to hold the detector catalog out of its L0.
- **Organizational model-risk programs** (financial model validation) predate the market but are governance (use decisions, validation sign-off), not security findings/response — they belong to the governance neighbor, not here.
- **Cloud-native instantiation**: a hyperscaler embedding AI posture into its cloud security plan (Microsoft) still satisfies L0 — packaging is L2.

## Boundary Findings

- **vs AI Safety / Guardrail Platform (§13) — the flagged joint review, resolved here**: the guardrail Type is defined by the *per-request screening-and-decision function on the LLM I/O path* (content in → policy → finding → block/alter/flag/allow). This Type is defined by the *estate-level security program* (inventory → AI-specific assessment → findings → response). Litmus tests:
  - Keep per-request screening but remove the estate inventory/assessment program → AI Safety / Guardrail Platform.
  - Keep the estate program but remove runtime I/O screening entirely → still AI Security Platform (Microsoft AI-SPM posture-only; Mindgard testing-only).
  - Vendors straddle by bundling (Check Point Guard+Red; HiddenLayer lists guardrails as a use case; Prompt's layer triggers guardrails). Bundling is L2.
  - Disposition: **two distinct Types confirmed; runtime screening stays with the guardrail leaf; the estate-level security program is this leaf.** Joint review closed.
- **vs AI Governance Platform (§13)**: governance decides *whether/how AI may be used* (registries, policy frameworks, human review gates, evidence); this Type assesses and defends AI assets against *attacks and weaknesses*. Shared surface: both keep an AI inventory. Remove security findings/assessment → governance; add review-gate workflows → drifts to governance.
- **vs Application Security Platform (§15)**: AppSec secures conventional application code/builds (SAST/DAST/SCA); this Type secures AI-native assets against AI-native threats (weights, prompts, agent behavior, AI service configuration). Overlap gradient: AI-library dependency scanning is SCA-like (Microsoft extends DevOps scanning to GenAI libs); model-file scanning has no AppSec analog.
- **vs CSPM / CNAPP (§15)**: AI-SPM is emerging as a *module inside* CSPM (Microsoft Defender CSPM plan) — a gradient/capability relationship: the generic posture engine is shared; the AI-specific object scope (AI BOM, AI service checks, AI attack paths, agent inventory) is this Type's slice. When a CNAPP ships AI-SPM, it contains this Type as a module.
- **vs Vulnerability Management (§15)**: generic findings aggregation/remediation across all asset classes; this Type generates AI-specific findings and consumes/feeds VM ecosystems. Gradient relationship; the AI-specific assessment engine is the differentiator.
- **vs Attack Surface Management (§15)**: EASM discovers external-facing assets; AI estate discovery is organization-internal + cloud + shadow AI. Partial overlap only on externally reachable AI endpoints (observed in Microsoft's posture doc).
- **vs SBOM Management / Software Supply Chain Security (§15)**: the AI BoM and model supply-chain security are the AI-specific analogs; bundling pattern (HiddenLayer module; Microsoft AI BOM discovery).
- **vs Model Registry (§13)**: an MLOps lifecycle registry (lineage, versions, approvals) is an inventory *source* and governance surface, not security assessment; no findings/response loop.
- **vs Threat Intelligence Platform (§15)**: generic cyber threat intel vs AI-specific threat research/feeds (vendor threat reports, AI security advisories); TI is a supporting input (observed as a Mindgard flagging input and HiddenLayer research arm).
- **Naming discriminator**: products whose *detection engine* merely uses AI internally (AI-powered EDR, AI-assisted SIEM) are NOT this Type — the protected object must be the AI estate itself.
- **Agentic security fluidity**: agent inventories / agent-harness security / MCP security are currently sold inside this Type (all samples) but the agent-security object set (skills, tool grants, harnesses) is expanding fast; whether it remains a variant or becomes its own Type is left open and flagged for future review.

**Litmus tests**:
- Remove identified AI assets (attribute findings to nothing) → point tooling, not a platform.
- Remove AI-specific assessment (generic misconfig/SCA only) → CSPM/AppSec, not this Type.
- Remove findings/response loop → research tooling or a governance registry.

## Uncertainties

- **Prompt Security**: platform documentation unreachable (docs transport error ×2; SentinelOne platform page 403). Observations limited to the public site; the product's operational structure (consoles, findings model) is NOT evidenced. Assertions kept weak; product retained as a sample only for its philosophy positioning and open-source tooling facts.
- **Protect AI / Palo Alto Prisma AIRS**: intended sample; all official URLs unreachable (401/403/404). Dropped from the sample; nothing asserted from memory. Its expected profile (AI-SPM + model scanning + runtime API security) is noted only as market context known from prior directory work, not as evidence.
- **HiddenLayer**: evidence at product-page level (Tier 2). Module structure and positioning are official; operational mechanics (how scans, simulations, and runtime detection actually work day-to-day) are not evidenced in fetched docs.
- **Microsoft**: AI-SPM doc fetched covers posture only; Defender's runtime AI-protection components (e.g., any LLM-path protections in other Defender plans) were not fetched and are not claimed.
- **Market churn**: M&A and module re-branding are frequent; scope claims are time-boxed to 2026-09-06. The Microsoft Agent 365 transition shows agentic scope is still moving between products/licenses.
- **Whether "agent security" stays in this Type** is open (see Boundary Findings).

## Final Synthesis

An AI Security Platform is the security-program layer over an organization's own AI estate. Its world has three load-bearing structures: (1) the AI estate held as identified, security-managed assets — discovered across cloud AI services and code, registered as test targets, or observed as AI traffic, with shadow AI made visible and an AI bill of materials assembled; (2) AI-specific security assessment — posture checks on AI services and their exposure/identity, integrity scanning of model artifacts and AI library dependencies, and adversarial testing with attack-technique libraries against models, chatbots, and agents; (3) security findings that carry severity and framework mapping (MITRE ATLAS / OWASP vocabularies are the common lingua franca) and feed a triage-and-remediation loop with fix guidance, workflow automation, and handoffs into SIEM/SOAR, CI/CD, and ticketing. Runtime attack detection and per-request enforcement appear in many products — but the per-request screening function itself is the AI Safety / Guardrail Platform Type; AI security platforms bundle it. The Type is defined by the estate-level program, not by any one assessment family, delivery form, or current threat fashion; LLM-centricity is today's weighting, not the definition.
