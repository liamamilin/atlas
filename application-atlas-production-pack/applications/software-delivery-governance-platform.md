# Software Delivery Governance Platform

## Overview

A **Software Delivery Governance Platform** is the control layer over an organization's software delivery pipeline: it holds the organization's rules for how software may move from code to production as enforceable policies, evaluates real delivery events against those policies at defined gates, and keeps an attributed, persistent audit record of what happened and whether the rules were satisfied.

It exists because engineering organizations need delivery to be fast *and* governed: production deployments must follow approval rules, security and quality standards must be checked before changes ship, and auditors must be able to see who changed what and under whose authority. The governance platform is where those rules live, where they are enforced, and where the evidence accumulates.

Its boundary: it governs delivery; it does not itself build, test, or deploy the software (that is the delivery platform's job), and it does not merely measure delivery (that is analytics). Many delivery platforms embed this governance layer as a module; the governance function is the Type.

## Users & Context

Primary users:

- **Engineering leaders / delivery owners** — define delivery standards (what requires approval, what may never ship unreviewed), monitor compliance across teams.
- **Platform / DevOps engineers** — author and maintain policies, wire them to pipelines and environments, keep enforcement working as the toolchain evolves.
- **Security & compliance stakeholders** — specify regulatory and security requirements as delivery rules; consume the audit evidence the platform produces.

Secondary users:

- **Developers** — encounter governance as gates: a pipeline that won't run until policy passes, a change that needs an approval, a warning on save.
- **Auditors** — read the audit trail and policy-evaluation history as evidence for SOC 2, ISO, SOX-class obligations.

The context is an organization running a real delivery pipeline (CI/CD, deployments to staged environments, releases) at a scale where rules must apply uniformly across many teams, projects, and commonly several tools — not a single team configuring its own repo settings.

## Core Model

The defining core is four structures held together:

```text
Delivery Policy of Record
└── Evaluation at Delivery Gates
    └── Enforced Outcome (block / warn / require approval)
        └── Attributed Audit Record
── held across teams, projects, and tools (cross-cutting scope)
```

- **Delivery policy of record** — the organization's rules for delivery, held in the system as explicit, machine-evaluable rules: which changes require approval before production, which environments demand extra checks, which pipeline configurations are forbidden, which standards a deployment must meet. The load-bearing property is that the rules are *operational* — the system can evaluate them — not prose in a wiki.
- **Evaluation at delivery gates** — concrete lifecycle events trigger policy evaluation: saving or changing a pipeline definition, starting a pipeline run, starting a step, promoting a change between environments, deploying to production, opening or merging a code change. The policy is evaluated against the actual artifact of the event (the pipeline definition, the deployment manifest, the change).
- **Enforced outcome** — evaluation produces a decision the system acts on: **block** the action (error and exit), **warn and continue**, or **require a recorded approval** before proceeding. Without enforcement the policies are advice; the enforcement outcome is what makes this governance.
- **Attributed audit record** — every governed action is recorded with who did it, when, what changed, and whether policy passed. Records persist and are commonly exportable/streamable, because their purpose is evidence: compliance reviews, incident forensics, and "who approved this deployment" questions.
- **Cross-cutting scope** — policies apply across many teams, projects, and services, typically organized in a scope hierarchy (organization → business unit → project, or team → repository → environment) with inheritance from broader to narrower scopes.

A useful way to hold the model: the policy says what must be true; the gate is where reality is checked against it; the audit record is the memory that it was checked.

### Capabilities Shared by Mature Products

These are widespread in current products but do not define the Type:

- **Policy-as-code** — policies written in a formal language (commonly OPA/Rego or a YAML DSL), versioned, often stored in Git, testable before enforcement.
- **Severity modes** — per-rule choice between hard block and warn-and-continue.
- **Scope hierarchy with inheritance** — organization-level rules that projects inherit; project-level rules that stay local.
- **Approval steps inside delivery flows** — named approvers or approver groups whose recorded sign-off is a gate condition.
- **Delivery metrics** — DORA metrics (deployment frequency, lead time, change failure rate, time to restore) and dashboards giving leaders visibility into the governed pipeline.
- **RBAC over governance itself** — who may author policies, who may approve, who may override.
- **Audit streaming/export** — forwarding audit logs to external SIEM or compliance systems.
- **Policy libraries and testing** — starter policies, sample payloads, evaluation history for debugging a rule.

## How It Works

### Define the policy

A governance or platform engineer writes the organization's delivery rules in the platform's policy language — for example, "every pipeline deploying to production must contain an approval step before the deploy stage", or "deployment manifests must declare resource limits". Policies are stored centrally, often versioned in Git, and tested against sample artifacts before they are enforced.

### Bind policies to entities and events

Policies are grouped into policy sets and bound to what they govern (pipelines, templates, feature flags, deployments, code changes) and when they evaluate (on save, on run, on step start, pre-deployment, on merge). Binding is where scope is decided: an organization-level policy set reaches every project beneath it; a project-level set stays local.

### Evaluate at the gate

When the governed event occurs, the platform serializes the artifact (the pipeline YAML, the deployment payload, the change metadata — commonly including who initiated it and their roles) and evaluates the bound policies against it. The outcome is enforced immediately:

```text
Delivery event occurs
→ platform assembles the artifact + actor context
→ bound policy set evaluates
→ pass → action proceeds (recorded)
→ warn → action proceeds with a visible violation (recorded)
→ fail → action is blocked, or an approval is demanded (recorded)
```

A typical loop: a developer saves a pipeline that deploys to production without an approval step → the save is blocked with the violating rule named → the developer adds the approval step → the save passes. At runtime, a deployment whose manifest violates policy fails at the gate before reaching the environment.

### Produce the evidence

Every evaluation, approval, override, and governed action lands in the audit trail: actor, action, object, time, policy result. Compliance teams and auditors query or export this record; some organizations stream it to a central audit store. Over time the audit trail becomes the organization's factual history of how its software was delivered and under which rules.

## Interfaces

- **Policy editor** — author rules in the policy language, with a library of starter policies and a testing surface that evaluates a rule against sample or historical payloads before enforcement.
- **Policy set / binding configuration** — group policies, choose the entity type and triggering event, set severity, and place the set in the scope hierarchy.
- **Gate surfaces in delivery flows** — developers see governance as inline messages: a blocked save with the violated rule, a warning banner, an approval prompt during a pipeline run.
- **Audit trail view** — searchable record of governed actions and evaluations, filterable by actor, object, time, and outcome; export/streaming configuration.
- **Compliance and metrics dashboards** — leadership views of policy compliance across teams, commonly alongside DORA delivery metrics.

## Important Rules / Behaviors

- **Policies are inert until bound.** A rule that exists but is not attached to an entity and event is not enforced; enforcement comes from the policy-set binding.
- **Enforcement outcomes are graded.** The same policy set can hard-block on one rule and merely warn on another; organizations choose per rule whether violation stops the action.
- **Scope inheritance flows downward.** Rules saved at a broader scope (organization) apply to narrower scopes (projects) beneath them; local scopes can typically add rules but the broader rule still applies.
- **Approvals are recorded, not informal.** A gate that requires approval produces a named, timestamped sign-off in the audit record — the approval itself is governed evidence.
- **The audit trail is append-oriented.** Governed actions are recorded as they happen; mature products treat this record as immutable or externally streamable precisely because its value is evidentiary.
- **Governance applies to automated actors too.** In current products, agent- and automation-initiated delivery actions pass through the same policy evaluation, RBAC, and audit trail as human actions.

## Variants

- **Embedded vs standalone.** Most market products embed governance inside a broader delivery platform (a CD/orchestration platform whose governance module is this Type); standalone layers attach to external tools via APIs and enforce policy without owning execution.
- **Code-change-level governance.** Policy enforcement at the pull-request stage (routing, auto-approval, required checks per policy) rather than at pipeline/deployment gates.
- **Regulated-industry packaging.** Prebuilt compliance mappings (SOX, GDPR, ISO, FedRAMP/CMMC-style frameworks), immutable forensic audit trails, and government-cloud deployments for customers whose auditors demand them.
- **AI-agent governance.** The same policy/audit machinery extended to govern what AI coding agents and automation may do in the delivery pipeline — an emerging variant reusing the core structures.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Continuous Delivery Platform | host / adjacent | executes builds and deployments; governance defines and enforces the rules that execution must satisfy. One product can host both. |
| Release Management Platform | adjacent | orchestrates the release process; governance sets the rules the release must pass (orchestrate vs define-and-enforce) |
| IT Change Management (ITSM) | adjacent | governs IT service changes via tickets and change boards, tool-agnostic; delivery governance is native to the engineering pipeline and evaluated automatically at delivery events |
| Approval Workflow Platform | adjacent | generic approvals over arbitrary requests; no delivery objects, no machine evaluation of delivery artifacts |
| Engineering Productivity Analytics | adjacent | measures and reports delivery; governance enforces and gates. Products often bundle both |
| Security Compliance Platform | adjacent | org-wide compliance posture and control frameworks; delivery governance is scoped to the delivery pipeline and feeds compliance evidence to it |
| Code Quality Platform | adjacent | produces quality signals; governance can consume those signals as gate conditions but owns the rule-enforcement layer |

## Representative Products

- **Harness** — governance built into a full SDLC platform: OPA-based policy-as-code with policy sets bound to entities and events, RBAC, and audit trail across every module.
- **Opsera** — governance and policy-as-code across a heterogeneous toolchain (100+ integrations), with per-step activity logs and unified delivery analytics.
- **Copado** — Salesforce DevOps platform with a Compliance Hub: automated compliance scans, release approvals, quality gates, and immutable audit trails for regulated industries.
- **LinearB** — delivery metrics plus gitStream policy-as-code workflow automation governing code changes across Git hosts.
- **Sleuth** — lightweight change/deployment governance: deploy tracking, approval workflows, and audit trails (its current focus has extended to governing AI-agent tooling).

## Sources

- Harness, "Harness Policy As Code overview" — https://developer.harness.io/harness-ai/use-harness-platform/governance/policy-as-code/harness-governance-overview.md (accessed 2026-09-10)
- Harness, Platform / Governance page — https://www.harness.io/ (accessed 2026-09-10)
- Opsera, Platform and DevSecOps Governance pages — https://opsera.ai/platform, https://www.opsera.io/platform/devsecops-devops-governance (accessed 2026-09-10)
- Copado, Compliance Hub / GovCloud DevOps / Release stage pages — https://www.copado.com/product-detail/compliance, https://www.copado.com/product-overview/govcloud-devops, https://www.copado.com/devops-stages/release (accessed 2026-09-10)
- LinearB, platform and DORA metrics pages — https://linearb.io/platform/dora-metrics, https://linearb.io/lp/dora-metrics (accessed 2026-09-10)
- Sleuth, homepage — https://www.sleuth.io/ (accessed 2026-09-10)

Research limitations: Harness documentation was available at operational depth; Opsera, Copado, LinearB, and Sleuth evidence comes from official product pages rather than operational manuals, so mechanics specific to those products are described at correspondingly moderate strength. Sleuth's legacy product documentation was unreachable during research.
