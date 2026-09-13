# AI Safety / Guardrail Platform

## Overview

An **AI Safety / Guardrail Platform** is a control point on the path between users and LLM-based applications: it screens the content that flows to the model and/or comes from it, checks that content against a configurable policy of safety, security, and compliance rules, and turns each detection into a decision — block the content, alter it (for example mask sensitive data), flag it for downstream handling, or allow it through.

The defining core is small:

```text
Screening point on the LLM application path
└── configurable policy of checks (what to detect, how strictly)
    └── explicit detection finding per piece of content
        └── actionable decision: block / alter / flag / allow
```

Everything else commonly associated with the category — the specific detector catalog (toxicity, jailbreaks, PII, off-topic questions, ungrounded answers), sensitivity tuning, test consoles, dashboards, policy versioning — is the standard capability set that mature products carry, not what makes a product a guardrail platform. The same function ships in several delivery forms: as a feature built into a model platform, as a standalone screening API, or as a developer framework embedded in the application.

When the product stops screening content on the model path — for example it only maintains registries of AI systems and human review processes, only records traces, or only decides where to route a request — it has become a different Application Type (AI Governance, LLM Observability, or AI Gateway respectively).

## Users & Context

Primary users are the teams responsible for shipping and operating LLM applications safely:

- **AI/ML and platform engineers** — integrate screening into the application (SDK, API call, or platform configuration), define what is checked, and handle flagged traffic in code.
- **Security and trust-and-safety teams** — define the policy (which threats and content classes to screen for), set strictness, and monitor detection activity; this audience dominates security-pure-play products.
- **Compliance and risk owners** — care about sensitive-data handling, topic restrictions, and the audit trail of what was blocked.

Secondary users:

- **Application operators** — watch dashboards, tune thresholds to reduce false positives, respond to incidents.
- **Product owners** — review how often user experience is affected (blocks, confirmations).

Typical context: an organization is deploying chatbots, RAG assistants, or agents and must control what users can ask, what the model may say, and what data may pass through — for reasons of safety policy, regulation, brand, or defense against prompt attacks. The platform is used both during rollout (testing, tuning, monitor-only observation) and continuously in production.

## Core Model

### The Defining Core

```text
Policy (what to check, how strictly, for which application)
└── applied at a screening point on the model path
    ├── on content going to the model (user input, and often retrieved context)
    └── on content coming from the model (responses, and often tool interactions)
        └── detection finding (unsafe elements identified, with reason/category)
            └── decision: block / alter / flag / allow
                └── enforced inline, or surfaced for the application to act on
```

Four properties. Remove any one and the product is no longer this Type:

- **Screening of model-path content** — the unit of work is a piece of LLM application content (a user prompt, a model response, a retrieved chunk, a tool exchange) submitted for evaluation. There is always such a screening act; what varies is where it sits.
- **Configurable checks policy** — what is screened for, and how strictly, is defined by the customer, per application or use case. A fixed, non-configurable single check would be a feature, not this platform.
- **Detection findings** — each screening produces an explicit result: whether unsafe content was found and what it was (a harm category, an entity type, a matched rule, a confidence level).
- **Actionable decision** — the finding materializes as block, alter, flag, or allow — either enforced by the platform itself or returned to the application, which acts on it. A product that only *records* content without producing decisions is observability; one that only *moves* requests is a gateway.

### Standard Capabilities

Mature products commonly carry most of the following. They make the platform practical; they do not define it.

**Detector catalog.** The checks a policy can draw from, typically organized as:

- harmful-content moderation — predefined categories (violence, hate, sexual, self-harm and similar) with configurable strength or severity
- prompt-attack defense — jailbreaks, prompt injections, direct and indirect manipulation attempts
- sensitive-data detection — PII and other regulated data, with block-or-mask handling
- topic control — topics the application must not discuss (denied topics, topical rules)
- groundedness checks — whether a response is actually supported by the supplied source material
- organization-specific rules — custom word/phrase lists, custom-trained categories, rules written in natural language or as logical constraints

**Policy machinery.**

- a named policy or guardrail configuration, typically versionable, scoped per application, feature, or environment, with a safe default
- per-check or per-policy threshold/sensitivity settings balancing false positives against misses
- a monitor-only posture (detection without blocking) so teams can observe behavior before enforcing

**Rollout and operations.**

- test surfaces: try sample content against a draft policy before deployment
- some products additionally simulate how a proposed policy change would have behaved on recorded traffic
- dashboards of flag rates, category distributions, and latency; screening logs with per-request breakdowns

**Outcome handling.**

- configurable user-facing behavior on block — for example a defined fallback message, or handing the decision to the application
- in framework-form products, a remediation loop (for example, re-asking the model when output fails validation)

### One Function, Several Placements

The core model is written in conceptual terms. Delivery differs:

```text
Concept:            Screening point
Implementations:    model-platform feature (screening invoked with the model call, or callable standalone)
                    standalone screening API the application calls before/after the model
                    in-app framework wrapping the LLM call
                    guardrails server exposing an OpenAI-compatible endpoint

Concept:            Policy object
Implementations:    named, versioned guardrail/policy assigned to an application
                    per-request parameters plus product-managed detector resources
                    configuration files defining rails and checks in code

Concept:            Decision
Implementations:    platform-enforced block with fallback message
                    flag returned to the application (which blocks, confirms with the user, or logs)
                    rewritten output (masked/filtered) substituted for the raw model output
```

A reader who has only seen one placement (for example a cloud-platform feature) should still be able to recognize the framework-form and API-form products from the core model.

## How It Works

### Define the policy

```text
Choose the application/use case to protect
→ select the checks to apply (harm categories, prompt-attack defense, sensitive data, topics, grounding, custom rules)
→ set strictness per check
→ test against sample content
→ publish (as a versioned policy, or as request parameters the application sends)
```

### Screen a request

```text
User input arrives at the application
→ application (or platform) submits the input to the screening point
→ platform evaluates the configured checks
→ if unsafe: return the finding and decision
    → block with the defined fallback message, or
    → alter (e.g. mask sensitive data) and continue with the clean version
    → flag: the application decides (proceed, ask the user to confirm, or refuse)
→ if safe: content proceeds to the model
```

### Screen a response

```text
Model (or agent tool chain) produces output
→ output submitted to the screening point (same or separate checks)
→ checks applied: harm, sensitive data, off-policy topics, grounding against source material, custom rules
→ unsafe output blocked or rewritten; suspicious content (e.g. untrusted links) flagged or removed
→ clean response reaches the user
```

In framework-form products the loop is tighter: the framework wraps the model call itself, validates the output, and can automatically re-ask the model until the output passes validation.

### Roll out and tune

```text
Start in monitor-only mode (findings recorded, nothing blocked)
→ review dashboards: what is being caught, at what rate, how much is false positive
→ adjust check selection and sensitivity, validated against historical traffic
→ switch to enforcement
→ keep monitoring; adjust as threats and content drift
```

### Core vs common vs optional

- **Defining core** — screening of model-path content, configurable checks policy, detection findings, block/alter/flag/allow decisions.
- **Standard capabilities** — the detector catalog, thresholds, monitor-vs-enforce posture, versioned policy objects, test consoles, dashboards and logs, fallback messaging, re-ask loops.
- **Optional / variant** — delivery form; breadth of interception (input/output only vs also retrieval, conversation, tool calls); modality (text, image, multimodal); detector sourcing (vendor-managed, self-hosted models, third-party services, LLM self-checking); agent/tool behavior controls; bundled red-teaming and evaluation tooling.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Policy / guardrail configuration console

Where the safety policy is authored.

- lists of checks with per-check settings (category, strength/severity, entities, topic definitions, custom rules)
- policy scoping per application, feature, or environment; version management
- primary actions: create/edit policy, configure checks, test, publish/version

### Screening API

The programmatic entry point — the actual workhorse surface.

- input: the content to screen (prompt, response, retrieved chunk, tool exchange), plus the policy reference
- output: the finding — whether content was flagged, by which check, at what confidence/severity — and the decision where the platform enforces
- primary actions: screen input, screen output, retrieve a screening breakdown

### Test / simulator surface

Used before and during rollout.

- run sample or historical content through candidate policies
- compare outcomes (flag rates, misses, false positives) across strictness settings
- primary actions: run test, compare configurations, promote a configuration

### Monitoring dashboard

The operational view for security and operations teams.

- flag rates over time, category/severity distributions, latency, affected applications
- drill into individual screened requests with per-check breakdowns
- primary actions: filter, inspect a request, tune policy in response

### In-app integration surfaces (framework-form products)

For developer-embedded deployments, the primary surface is code:

- a guard object or rails configuration wrapping the model call
- validator/check definitions composed into input and output guards
- call history and validation results inspectable in the development environment

## Important Rules / Behaviors

### The decision can be enforced or delegated

Some products enforce directly (blocked content never reaches the model or the user, replaced by a defined message). Others return findings and let the application decide — including softer outcomes such as asking the user to confirm before proceeding. A common pattern is a posture control: the same integration runs in detection-only or enforcing mode, so blocking can be turned on and off without reworking the integration.

### Screening applies to both sides of the model

Input screening protects the model (from manipulation, abuse, and data that should not enter); output screening protects the user (from harmful, leaking, ungrounded, or off-policy content). Mature products treat the two as distinct check applications with different catalogs and thresholds; input checks alone are the narrower deployment.

### Thresholds trade false positives against misses

Every detection check has a strictness setting. Stricter settings catch more threats but flag more legitimate traffic; looser settings protect user experience but let borderline content through. Products expose this as per-category strength, severity levels, or confidence thresholds — the vocabulary differs, the trade-off is structural.

### Monitor-only mode is the standard rollout instrument

Because false positives directly damage user experience, teams commonly begin in a posture where findings are recorded but nothing is blocked, tune on observed (or simulated historical) traffic, then enable enforcement.

### Grounding checks need source material

Groundedness checking is only meaningful when the application supplies reference material (as in RAG); the check compares the response against that source, not against general truth.

### Screening sits on the critical path

Inline screening adds latency to every model interaction, so latency is a documented consideration of this Type, and products describe mitigation techniques (such as parallel evaluation and chunking) in their operational documentation.

### Findings are audit-relevant

Screening results — what was detected, what was done — are recorded for analysis and, in regulated settings, as compliance evidence; some platforms let operators control how much of the blocked content is retained in logs.

## Variants

- **Model-platform native** — the guardrail is a managed feature of a model hosting platform, activated per model invocation or through a standalone screening call; strongest for teams already on that platform.
- **Standalone screening API / service** — a dedicated content-safety or AI-security service the application calls before and after the model; often serves general content moderation alongside LLM protection; SaaS or self-hosted.
- **Security-pure-play platform** — screening API plus dashboard oriented to security operations, with managed and frequently updated threat detectors, policy-per-application scoping, and agent/tool behavior controls.
- **Developer framework / toolkit** — an in-app library where engineers compose checks in code, wrap model calls directly, and rely on the library for validation, remediation (re-asking the model), and call history; often pluggable with external detector services.
- **Agentic variant** — the same screening function extended to agent workflows: validation of tool calls and arguments, runtime allow/deny lists for tools, and detection of actions outside the agent's mandate.

A variant remains a variant unless it abandons the defining core — for example, a product that only red-teams models before release (no runtime screening) belongs to a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| AI Governance Platform | organization/process-level control: registries of AI systems, policy frameworks, human review lifecycles and recorded decisions; no runtime content screening or per-request decisions |
| LLM Observability Platform | records and inspects executions (traces, spans, costs) for analysis; does not decide whether content may proceed; guardrail findings often land in its dashboards |
| AI Gateway / Model Routing Platform | sits on the same request path but decides where/how a request is served (provider, failover, budgets); guardrails bundled into gateways are a capability, not the Type |
| LLM Evaluation Platform | pre-release testing of models/agents against datasets and scorers; guardrail platforms screen live traffic and may bundle evaluation as rollout tooling |
| Data Loss Prevention / DLP | protects sensitive data across enterprise channels generally; the same detection idea appears inside guardrails scoped to the LLM path as one check among many |
| AI Security Platform | broader AI estate security programs (red teaming, threat intelligence, posture); runtime input/output screening is the guardrail slice of it |
| Content moderation (neighboring market) | screens user-generated content at scale on arbitrary platforms; the guardrail Type is anchored to the LLM application path, though some services serve both |

The most important boundary is with **AI Governance Platform**: governance decides *whether and how* an AI system is allowed to operate (people, review, evidence); the guardrail platform decides *whether a specific piece of content* may proceed at runtime. Products increasingly bundle both, which makes the runtime screening-and-decision function the reliable tell of this Type.

## Representative Products

- Amazon Bedrock Guardrails
- Azure AI Content Safety
- Check Point AI Guardrails (formerly Lakera)
- Guardrails AI
- NVIDIA NeMo Guardrails

The core model was checked across all delivery forms above — model-platform native, standalone service, security pure-play, and open-source frameworks — to avoid defining the Type by any single placement or by the current threat fashion.

## Sources

Research date: **2026-09-06**

- Amazon Web Services — Amazon Bedrock Guardrails (User Guide): https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html , https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Microsoft — Azure AI Content Safety overview: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview
- Check Point — AI Guardrails documentation (Guardrails overview, Policies): https://docs.lakera.ai/ , https://docs.lakera.ai/docs/defenses , https://docs.lakera.ai/docs/policies
- Guardrails AI — documentation (Introduction, The Guard): https://www.guardrailsai.com/docs , https://www.guardrailsai.com/docs/concepts
- NVIDIA — NeMo Guardrails documentation (Overview, Guardrail Types): https://docs.nvidia.com/nemo/guardrails/latest/ , https://docs.nvidia.com/nemo/guardrails/latest/about-nemo-guardrails-library/rail-types

> Sourcing notes: all sources above were fetched live on 2026-09-06. Content-filtering features attached to model deployments inside the Azure AI Foundry platform were not directly researched and are not described here. Detector catalogs in this market change frequently; the capability descriptions reflect the documented state on the research date.
