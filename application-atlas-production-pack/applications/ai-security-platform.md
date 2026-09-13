# AI Security Platform

## Overview

An **AI Security Platform** is security software whose protected estate is the organization's own AI systems: the models, AI applications, agents, AI services, and AI artifacts (datasets, prompts, training and fine-tuning components) that the organization builds, buys, or lets its people use. The platform establishes which AI assets exist — including unsanctioned "shadow AI" — assesses them for weaknesses and exposures that conventional security tooling does not cover, detects attacks against them where it covers runtime, and drives every result into a security findings-and-response loop owned by security and engineering teams.

The defining structure is small:

```text
AI estate (AI systems held as identified, security-managed assets)
└── AI-specific security assessment of those assets
    └── Security findings (weaknesses / exposures / attacks, attributable to assets)
        └── Response loop (triage → prioritize → remediate / mitigate)
```

Two boundaries matter immediately:

- This is security **for** AI systems, not security products that merely use AI internally. An endpoint product with machine-learning detection is not an AI Security Platform; the object of protection must be the AI estate itself.
- The per-request screening of content flowing into and out of an LLM — blocking unsafe prompts and responses as they happen — is a distinct function with its own Application Type (AI Safety / Guardrail Platform). AI security platforms frequently bundle that runtime enforcement as one capability, but the platform's identity is the estate-level security program, not the per-request gate.

Everything else commonly seen — cloud-connector discovery, AI bills of materials, model-file scanning, red-team attack libraries, agent inventories, SIEM handoffs — is the mature market shape around that core, not the definition of it.

## Users & Context

Primary users:

- **Security operations and AppSec teams** — run the assessment cycles, triage findings, and drive remediation; the platform's findings compete for attention with vulnerability and incident queues, so workflow handoffs matter.
- **Security leadership (CISO office)** — owns the question "what AI exists in this organization, how risky is it, and are we defended?", answered through inventories, posture views, and reports.
- **AI/ML engineering and application developers** — register models and applications as assessment targets, receive findings and remediation guidance, and re-test after changes.

Secondary users:

- **Compliance and risk functions** — consume risk classification and reporting; AI assets increasingly carry regulatory expectations.
- **AI governance bodies** — overlap on the asset inventory, though their decisions (approvals, use policies) are a different function.

Typical context: an enterprise adopting AI through cloud AI services (managed model platforms, AI application frameworks, agents), through libraries and models pulled from public registries, and through employees using AI tools with or without approval. The estate changes continuously — new models, new versions, new attack techniques — which makes assessment an ongoing program rather than a one-time audit. Regulated industries (financial services, healthcare, government) are prominent adopters because AI assets carry compliance and IP exposure.

## Core Model

### The Defining Core

```text
AI estate (identified AI assets under management)
└── AI-specific security assessment of those assets
    └── Security findings (weaknesses / exposures / attacks)
        └── Security-team response loop
```

Four properties. If any one is removed, the product is no longer recognizable as an AI Security Platform:

- **AI estate as managed assets** — the system knows *which* AI systems it is responsible for, whether by discovering them automatically, by registration, or by observing AI traffic. Findings must land on identified assets. Without this, the product is a point tool — a scanner or fuzzer with no program around it.
- **AI-specific security assessment** — evaluation against the AI-native threat space: integrity of model artifacts, misconfiguration and exposure of AI services, adversarial techniques against models and agents, abuse of agent tools. Running a conventional vulnerability scan on a server that happens to host a model is not this; testing whether a chatbot can be jailbroken into revealing its system prompt is.
- **Security findings** — assessment results materialize as discrete findings: a flagged jailbreak, a backdoored model file, an internet-exposed AI endpoint, an agent invoking a tool outside its mandate. Findings typically carry severity and a mapping to shared AI threat vocabularies.
- **Response loop** — findings feed a triage-and-action cycle owned by security and engineering: prioritize, remediate (fix configuration, replace an artifact, harden a prompt, tighten a policy), and re-verify. Without this loop, the product is research tooling or a registry, not a security platform.

### Capabilities Shared by Mature Products

These capabilities appear across the researched market. They are not what makes a product an AI security platform, but they make the platform operational.

- **Estate discovery and inventory** — connectors into cloud AI services and MLOps platforms; scanning of code and infrastructure definitions to inventory AI components, data, and artifacts (an "AI bill of materials" in common vendor usage); detection of shadow AI; agent inventories listing autonomous AI agents with their security status.
- **Posture assessment of AI assets** — recommendations about identity, data security, and internet exposure of AI services (private endpoints, restricted endpoints, managed identity, identity-based authentication); **attack-path analysis** connecting AI applications to the data used for grounding and fine-tuning and to the identities that can reach them.
- **Artifact and supply-chain security** — scanning model files and artifacts for malware, backdoors, and unknown or unsafe components before deployment; validating integrity and provenance; vulnerability scanning of AI library dependencies; maintaining the AI bill of materials.
- **Adversarial testing / red teaming** — registered test targets (models, chatbot applications, agents); an **attack-technique library** (jailbreaks, prompt injection, policy-violation techniques, multi-turn attack chains); test datasets including custom-generated ones; evaluation policies; some products profile the target first — which guardrails it runs, whether its system prompt can be extracted, which tools it exposes; reporting of attack success rates and flagged events by threat category.
- **Framework mapping** — findings mapped to shared AI threat vocabularies, most prominently MITRE ATLAS and OWASP's AI/LLM risk lists, so security teams can reason about AI findings in familiar terms.
- **Remediation support** — per-technique remediation guidance (e.g., separating system instructions, filtering outputs, constraining context, model hardening); recommendations attached to findings.
- **Runtime monitoring and detection** — where a product covers runtime: observation of AI application traffic (prompt volume, injection attempts, sensitive-data and secret leakage flags), detection of attacks against production AI systems, monitoring of agent activity.
- **Agentic security** — inventory and defense for autonomous agents: tool-use oversight, protection against unsafe or excessive autonomous actions; some products add agent-skill integrity and drift checks.
- **Response-loop machinery** — triage and remediation workflow automation, alerts to development and security teams, exports of findings, and integrations with SIEM/SOAR, CI/CD pipelines, ticketing, API gateways, and MLOps tooling.
- **Operational surfaces** — asset inventories, posture dashboards, test consoles, framework advisers, and reporting for executive and compliance audiences; programmatic access via CLI, SDK, and API.

### One Structure, Many Implementations

The core model is written conceptually. Specific products realize each concept differently, and a reader who knows only one implementation should still recognize the others:

```text
Concept:     AI estate as managed assets
Realized as: auto-discovery through cloud AI services; user-registered test targets;
             observed AI application traffic and agent deployments

Concept:     AI-specific assessment
Realized as: posture recommendation engines over AI services; artifact scanners for
             model files and dependencies; red-team test harnesses with attack libraries;
             runtime monitors watching live AI traffic

Concept:     Security findings
Realized as: configuration recommendations; flagged attack events; risk classifications;
             injected-data / secret / injection flags on traffic
```

## How It Works

### 1. Establish the estate picture

The platform first answers "what AI do we have?". Three mechanisms are common, often combined:

```text
Connect to cloud platforms and MLOps tools → deployed AI workloads and services appear
Scan code and infrastructure definitions → AI bill of materials (components, data, artifacts)
Observe AI traffic / agent activity → usage of AI tools, including unsanctioned ones
```

The output is a living inventory of AI assets. Shadow AI — deployments nobody sanctioned — is a headline outcome of this stage.

### 2. Assess the assets

Assessment runs in families; mature platforms usually offer several, focused products usually one:

```text
Posture assessment:    AI service configurations → misconfigurations and exposures
                       → recommendations, attack paths (asset ↔ data ↔ identity)
Artifact scanning:     model files, libraries, containers → integrity and dependency findings
                       → block or remediate before deployment
Adversarial testing:   register target → profile it (recon) → select policy and attacks
                       → run attack library (single- and multi-turn) → collect flagged events
Runtime monitoring:    watch live AI traffic and agent actions → detect attacks and misuse
```

The adversarial-testing loop in detail, since it is the most distinctive: a team registers a model or chatbot as a target, the platform profiles the target's protections, an evaluation policy determines how outputs are judged, and the attack library fires techniques such as jailbreaks, encoded prompt injections, and multi-step manipulations at the target. Every interaction is recorded; events are flagged or cleared; flagged events consolidate into findings.

### 3. Triage and respond

```text
Findings accumulate across assessments
→ severity / risk classification, framework mapping (ATLAS / OWASP vocabularies)
→ review with per-finding context (attack success rate, affected asset, evidence)
→ remediation guidance attached
→ assign, track, export to ticketing / SIEM / SOAR / CI-CD
→ re-assess after the fix
```

Users can typically contest machine judgments — tagging a flagged event as a false positive or negative — which both corrects the record and improves the detection over time.

### 4. Monitor in operation (where covered)

Platforms with a runtime component watch production AI systems: traffic volumes and content flags, attack attempts against models and agents, policy violations. When they act — blocking a request, alerting, triggering a guardrail — the enforcement decision is layered on top of the monitoring posture; many teams run detection-only first and enable enforcement later.

### Capability tiers

- **Defining core** — identified AI assets; AI-specific assessment; findings; response loop.
- **Standard capabilities** — estate discovery and AI bills of materials; posture checks and attack paths; artifact and supply-chain scanning; attack-technique libraries and test policies; framework mapping; remediation guidance; integrations with the security and development toolchain; reporting.
- **Common variants / optional** — runtime attack detection and enforcement; agent inventories and agentic defenses; shadow-AI analytics; red-team services; AI threat-intelligence feeds; embedded guardrail enforcement.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### AI asset inventory / explorer

The estate map.

- lists identified AI assets — models, applications, agents, services — with owner, source, and security status
- surfaces unknown or unsanctioned assets (shadow AI)
- primary actions: inspect an asset's findings, register a target, connect a source

### Posture views

Configuration risk of AI services.

- recommendations on identity, data security, and internet exposure; attack-path visualizations linking AI apps to data and identities
- primary actions: review a recommendation, remediate, mark resolved

### Scan results

Output of artifact and dependency scanning.

- per-artifact findings: integrity issues, embedded malware, vulnerable dependencies
- primary actions: inspect details, block or quarantine, remediate before deployment

### Testing console

The adversarial-testing workspace.

- test targets, test runs, attack-technique catalogs, datasets, evaluation policies
- test reports: attack success rates, flagged events by threat category, per-attack evidence, framework mappings, remediation sections
- primary actions: create a test, choose attacks/policy, review results, export findings

### Findings and framework views

The security-operations entry point.

- consolidated findings across all assessment families, grouped by framework (e.g., an ATLAS-style adviser over all tested risks)
- primary actions: triage, tag false positives, assign, export, track remediation

### Runtime monitoring dashboards

Where the product covers production.

- AI traffic volumes, triggered policies, injection / sensitive-data / secret flags, agent activity
- primary actions: investigate an event, adjust policy, enable enforcement

### Programmatic surfaces

CLI, SDK, and API so testing and findings flow inside development workflows; workflow integrations into CI/CD, ticketing, and SIEM/SOAR.

### Reports

Executive and compliance-facing summaries: estate composition, risk posture, assessment coverage, trend over time.

## Important Rules / Behaviors

### Findings anchor to identified assets

Every finding belongs to a known model, application, agent, or service. The inventory is therefore not just a visibility feature — it is the backbone that makes findings attributable and actionable.

### Assessment is active and probabilistic

Adversarial testing fires real attack traffic at real targets; targets must be authorized for testing. Classification of results (was this jailbreak successful?) is inherently imperfect — mature products expose flagging decisions, evidence for every interaction, and an explicit false-positive/negative correction mechanism.

### Assessment is continuous, not one-shot

The estate changes (new models, app updates, new agent deployments) and the threat space changes (new attack techniques). Mature products treat re-assessment — on change, on schedule, and on new-technique release — as the normal operating mode, and posture shifts are themselves findings.

### Shared threat vocabularies are mappings, not universals

MITRE ATLAS and OWASP AI risk lists provide common reference points, but exact technique names, categories, and severity scales vary by product. The mapping is the interoperability layer, not a guarantee of identical taxonomies.

### Monitor-first postures are normal

Detection without enforcement is a deliberate rollout stage: teams observe flag rates and false positives before letting the platform block or alter behavior. Enforcement, where present, is a decision layer distinct from detection.

### Assessor privacy postures vary

Some products are built to assess without ever accessing the customer's model weights, prompts, or data; others operate inline on traffic. This affects what can be tested and is a deployment consideration, not a defining trait.

## Variants

Common shapes of the Type:

- **Posture-first (cloud-suite module)** — AI posture management embedded in a cloud security platform: AI bill of materials, AI service recommendations, attack paths; strongest for organizations already running that cloud security stack.
- **Comprehensive pure-play platform** — discovery, supply-chain security, attack simulation, and runtime defense sold as one estate-wide platform, typically aimed at enterprise security leadership.
- **Testing-first** — red-teaming and continuous AI security testing as the core, with findings and remediation workflow around it; often adopted by AppSec and development teams.
- **Runtime/traffic-first** — securing AI application traffic organization-wide (monitoring, policy enforcement at the AI boundary) plus agent visibility; frequently packaged within a broader endpoint or infrastructure security vendor's suite.
- **By estate emphasis** — GenAI/LLM application security vs classical ML pipeline and model security vs agentic-AI security; the current market leans GenAI but the underlying program shape is the same.
- **By deployment** — SaaS platforms, self-hosted/on-prem components (common for artifact scanning where models cannot leave the building), and privacy-postured designs that never ingest customer weights or prompts.

A variant remains a variant while the defining core holds; a product that drops the estate-and-findings program entirely (only screening requests, or only scanning files ad hoc) has left the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| AI Safety / Guardrail Platform | per-request screening of LLM inputs/outputs with enforceable decisions (block/alter/flag/allow) — the runtime content gate; an AI Security Platform runs the estate-level program (inventory, assessment, findings, response) and may *bundle* guardrail enforcement as a capability |
| AI Governance Platform | organization-level control of AI *use*: registries, policy frameworks, review gates, compliance evidence; an AI security platform assesses and defends assets against attacks and weaknesses — both keep inventories, but only one produces security findings |
| Application Security Platform | secures conventional application code and builds (SAST/DAST/SCA); the AI-native assets (model files, prompts, agent behavior, AI service configuration) and AI-native threat classes have no AppSec analog, though AI-library dependency scanning overlaps |
| Cloud Security Posture Management / CNAPP | generic posture over cloud resources; AI posture management is emerging as a module inside these platforms — the AI-specific object scope (AI BOM, AI service checks, AI attack paths, agent inventories) is this Type's slice |
| Vulnerability Management | aggregates and drives remediation of findings across all asset classes; the AI security platform is a *producer* of AI-specific findings feeding that ecosystem |
| Attack Surface Management | discovers external-facing assets; AI estate discovery is organization-internal and cloud-based (shadow AI, AI services), overlapping only on externally reachable AI endpoints |
| SBOM Management / Software Supply Chain Security | software bills of materials and dependency security for conventional software; the AI bill of materials and model supply-chain security are the AI-specific analogs, often bundled |
| Model Registry | MLOps lifecycle registry of models (versions, lineage, approvals); an inventory *source* and governance surface, without security assessment or findings |
| Threat Intelligence Platform | general cyber threat intelligence; AI-specific threat research and feeds are a supporting input to this Type, not the platform itself |

The boundary with the AI Safety / Guardrail Platform is the most important one, because vendors sell both functions and bundle them freely. The structural test: per-request content screening with an enforcement decision is the guardrail function; the standing program that knows the AI estate, assesses it AI-specifically, and drives findings to response is the AI security platform. A product with only the first is a guardrail platform; a product with only the second is still fully an AI security platform.

## Representative Products

- Microsoft Defender for Cloud — AI security posture management (hyperscaler, posture-first)
- HiddenLayer — comprehensive AI security platform (discovery, supply chain, attack simulation, runtime)
- Mindgard — continuous AI security testing / red teaming platform
- Prompt Security (now part of SentinelOne) — AI application traffic security and agentic tooling

The defining core was checked against pre-LLM and differently positioned analogs (productized model scanning and adversarial-robustness testing; research libraries; organizational model-risk programs) to avoid freezing the definition to the current GenAI moment.

## Sources

Research date: **2026-09-06**

- Microsoft Learn — AI security posture management in Microsoft Defender for Cloud: https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture
- Mindgard documentation (introduction, test results, plan AI risk management): https://docs.mindgard.ai/
- HiddenLayer — AISec Platform product page: https://hiddenlayer.com/aisec-platform/
- Prompt Security (SentinelOne) — public site and open-source tooling pages: https://www.prompt.security/
- Check Point (Lakera) documentation consulted via the adjacent AI Safety / Guardrail Platform research pass (boundary analysis): https://docs.lakera.ai/

> Sourcing limitations: official product documentation for HiddenLayer (docs site) and Prompt Security (docs site; vendor platform page) could not be retrieved from the research environment; their findings rest on official product/site pages, and operational details for those products are stated at correspondingly lower strength. Two additional intended samples (Protect AI / Palo Alto Prisma AIRS) were dropped because no official source was reachable. Precise operational facts (module behaviors, limits, licensing mechanics) are deliberately not asserted in this document; where a claim depends on a single product's documentation it is kept product-anchored or marked as varying by product.
