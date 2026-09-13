# Research Notes — Software Delivery Governance Platform

## Research Goal

Understand what a "Software Delivery Governance Platform" is as an Application Type: what it governs, what objects it holds, how policies are expressed and enforced, what evidence it produces, and how it differs from adjacent Types (Continuous Delivery Platform, Release Management Platform, IT Change Management, Approval Workflow Platform, Engineering Productivity Analytics, Security Compliance Platform).

## Initial Boundary

Hypothesis: this is a cross-cutting control layer over the software delivery pipeline — policies, gates, approvals, audit evidence — distinct from the platforms that *execute* delivery (CD platforms) and from platforms that *measure* delivery (engineering analytics).

Risks identified up front:
- Many vendors embed governance inside broader delivery platforms (Harness, Opsera, Copado). Must separate the governance function from the host platform.
- "Governance" is a marketing word used loosely; must anchor on operational structures (policy objects, evaluation events, enforcement outcomes, audit records), not vendor slogans.
- Sleuth has pivoted its main site to AI-agent skill governance; its legacy change-management product (Sleuth DORA / change management) is the relevant evidence.

## Research Questions

1. What are the core objects? (policy, policy set, gate, evaluation, approval, change/deployment record, audit trail)
2. When are policies evaluated? (on save, on run, on step start, pre-deployment, pre-merge)
3. What outcomes can enforcement produce? (block/error, warn/continue, require approval)
4. How is scope organized? (account/org/project hierarchy; per-team, per-environment, per-repo)
5. Who uses it? (engineering leaders, platform/DevOps teams, security/compliance, auditors)
6. What evidence does it produce for auditors?
7. How does it differ from IT change management and from analytics platforms?

## Representative Products

Selected for different philosophies and customer tiers:

1. **Harness** — platform-embedded governance: OPA policy-as-code across a full SDLC platform. Strong official operational documentation (Tier 1).
2. **Opsera** — heterogeneous-toolchain orchestration pole: governance/policy-as-code across any CI/CD tool, unified insights, activity logs.
3. **Copado** — regulated-industry pole: Salesforce DevOps platform with Compliance Hub, release approvals, audit trail, FedRAMP/GovCloud positioning.
4. **LinearB** — code-level policy pole: gitStream policy-as-code workflow automation over pull requests plus delivery metrics dashboards.
5. **Sleuth (legacy change management)** — lightweight deployment/change governance pole: deployment tracking, approvals, audit trail. (Site has pivoted; evidence limited.)

## Sources

- Harness Policy As Code overview (official docs, developer.harness.io) — accessed 2026-09-10. Tier 1.
- Harness platform page (harness.io) — governance built in: OPA policy, RBAC, audit trail, secrets. Accessed 2026-09-10.
- Opsera platform / DevSecOps governance pages (opsera.ai, opsera.io) — accessed 2026-09-10.
- Copado product pages: Compliance Hub, GovCloud DevOps, Release stage (copado.com) — accessed 2026-09-10.
- LinearB platform pages incl. DORA metrics, gitStream policy-as-code references (linearb.io, PRNewswire releases) — accessed 2026-09-10.
- Sleuth homepage (sleuth.io) — accessed 2026-09-10; legacy docs (docs.sleuth.io) unreachable (transport error).

## Product Observations

### Harness (evidence layer A — official operational docs)

- Uses Open Policy Agent (OPA) as the central service to store and enforce policies across the platform.
- A **policy** is a single rule written in Rego; a **policy set** groups policies and binds them to an entity type and an event. Policies are not enforced until added to a policy set.
- Entities governed: pipelines, templates, feature flags, repositories, services, custom payloads (via Policy step).
- Events: **On Save**, **On Run**, **On Step Start** (step-start behind feature flag).
- Severity per policy in a set: **Error and Exit** (action blocked) vs **Warn and Continue** (action completes with message).
- Scope hierarchy: Account → Organization → Project; where a policy/set is saved determines scope; account-level policies apply downward.
- Input payload: JSON representation of the entity plus user metadata (roles, groups) enabling attribute-based rules.
- Policy editor with library of sample policies, testing terminal, evaluation history with retention.
- Separate **Audit Trail** feature: tracks changes to resources; audit streaming to external destinations.
- Platform page: "Policy checks, RBAC, audit trails, and secrets management are built into every module. Define once. Enforce everywhere." Agent and human actions governed by the same policy engine; evidence returned as scorecards and audit trails.

### Opsera (evidence layer A — official product pages; operational docs not fetched)

- Markets "Governance, Security, and Compliance" as a platform pillar; "Governance — Policy as code" in product nav.
- Unified DevOps across 100+ integrations (Jenkins, GitLab, GitHub, Octopus, etc.) — governance applied across heterogeneous toolchains, not one proprietary pipeline engine.
- Every pipeline generates an **activity log** of every step including console outputs; unified analytics across Pipelines, Planning, SecOps, Quality, Operations; DORA metrics.
- Positions governance as "guardrails": balance speed and quality, manage risk and compliance.

### Copado (evidence layer A — official product pages)

- **Compliance Hub**: monitor and enforce rules for metadata changes; identify non-compliant changes before deployment; automated compliance scans across the DevOps process; real-time compliance monitoring; industry standards (SOX, ISO, GDPR).
- Release governance: release approvals, audit trail, quality gates, real-time monitoring ("Governance + Compliance" datasheet).
- GovCloud: "Track every change, approval, commit, and deployment with a complete, immutable forensic audit trail"; FedRAMP Moderate ATO; CMMC 2.0 / NIST 800-171 support.
- Every change connected back to a user story with full auditability; governed promotions through centralized pipelines.

### LinearB (evidence layer A — official pages/press)

- gitStream: "policy-as-code through programmable workflow automation" — automating PR routing, approvals, tests per policy across GitHub/GitLab/Bitbucket.
- Platform: DORA metrics, benchmarks, resource allocation, project forecasting, "AI & workflow governance" nav item.
- Philosophy: metrics + automation to actively improve delivery; governance expressed at the code-change (PR) level.

### Sleuth legacy (evidence layer B — limited; docs unreachable)

- Historically: change management for software teams — deployment tracking, change governance, deploy approvals automation, audit trail, change impact visibility. Current site confirms approval workflows, audit trails, RBAC as governance features (now applied to AI-agent skills — pivot noted).

## Cross-product Comparison

| Structure | Harness | Opsera | Copado | LinearB | Sleuth |
|---|---|---|---|---|---|
| Organization-defined delivery policies as enforceable rules | Y (OPA/Rego) | Y (policy as code) | Y (compliance rules) | Y (gitStream YAML policies) | Y (approval/governance config) |
| Evaluation at defined delivery events/gates | Y (On Save/On Run/On Step Start) | Y (pipeline steps) | Y (pre-deploy scans, quality gates) | Y (PR lifecycle) | Y (deploy/approval events) |
| Outcomes: block / warn / require approval | Y (Error&Exit / Warn&Continue) | Y | Y (block non-compliant before deploy) | Y (auto-approve/block/label) | Y (approvals) |
| Attributed persistent audit record | Y (audit trail + streaming) | Y (activity logs) | Y (immutable forensic audit trail) | partial (metrics history) | Y (audit trail) |
| Cross-cutting scope (multi-team/project/tool) | Y (account/org/project) | Y (any CI/CD tool) | Y (multi-org Salesforce) | Y (multi-repo) | Y (multi-service) |
| Delivery metrics/analytics | Y (DORA) | Y (DORA) | Y (value stream maps) | Y (DORA core) | Y (DORA) |
| Host execution engine | proprietary pipelines | orchestration of external tools | proprietary Salesforce CI/CD | none (attaches to Git hosts) | none (attaches to deploy tools) |

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

Four jointly-held structures:

1. **The delivery policy of record** — the organization's rules for how software may move through delivery (what requires approval, what is forbidden, what standards apply), held in the system as explicit, machine-evaluable rules rather than tribal knowledge or prose documents. Remove → generic rules engine or a wiki.
2. **Evaluation of delivery events against those policies at defined gates** — concrete lifecycle events (saving a pipeline definition, starting a run, promoting a change, deploying to an environment, opening/merging a change) trigger evaluation; outcomes are enforced (block, warn-and-continue, or require a recorded approval). Remove → a policy document nobody enforces, or an approval workflow platform with no delivery semantics.
3. **Attributed, persistent audit record** — who did what, when, to which change/pipeline/deployment, and whether policy passed; retained as compliance evidence. Remove → enforcement with no memory; not governable.
4. **Cross-cutting scope over the delivery lifecycle** — applies across multiple teams/projects/services (and commonly multiple tools), not a feature of a single script or single tool's settings page. Remove → a per-tool configuration option.

Jointly load-bearing: 1 alone = rules engine; 2 without 1 = bare approval workflow; 3 without 1–2 = audit log; 4 without 1–3 = a tool setting. The binding is software delivery: policies speak delivery language (pipelines, deployments, environments, changes), not generic business approvals.

### L1 — Common Mature Structure

- Policy-as-code (OPA/Rego or DSL/YAML), versioned, often Git-stored
- Severity modes: error-and-exit vs warn-and-continue
- Scope hierarchy (account/org/project or team/repo/environment)
- Approval steps/gates inside delivery flows
- Delivery metrics (DORA four) and dashboards for leaders
- RBAC over who can define/change policies and who can approve/override
- Audit streaming/export to external systems
- Policy libraries/templates and testing of policies before enforcement

### L2 — Variant / Optional

- Standalone governance layer vs governance embedded in a delivery platform (Harness/Opsera/Copado) vs code-change-level governance (gitStream)
- Regulated-industry packaging (FedRAMP, CMMC, SOX/GDPR mappings — Copado)
- AI-agent governance extension (Sleuth Skills; Harness agent governance) — same policy/audit machinery applied to a new actor class
- Value-stream/portfolio-level governance (adjacent to VSM products)
- Change-ticket integration (ServiceNow/Jira) linking delivery changes to ITSM change records

### L3 — Vendor-specific

- Harness: OPA 0.62.0, Rego packages importable across scopes, evaluation retention, feature-flagged events (On Step Start, Git-backed onSave enforcement)
- Copado: metadata-specific compliance rules for Salesforce; Org Intelligence
- LinearB: gitStream automation vocabulary; free DORA dashboards tier
- Opsera: Hummingbird AI, GitCustodian

## Vendor-specific Findings

See L3 above; none promoted to the canonical document.

## Boundary Findings

- **vs Continuous Delivery Platform**: CD executes delivery; governance defines and enforces the rules delivery must satisfy. Harness ships both — the governance module is the Type-relevant slice; the platform is the host. Remove the execution engine and the governance layer still stands (gitStream, Sleuth attach to external tools).
- **vs IT Change Management (ITSM)**: ITSM change management governs changes to IT services via tickets/CABs, tool-agnostic and ops-centric; software delivery governance is native to the engineering pipeline (policy-as-code evaluated automatically at delivery events). They interconnect (change tickets linked to deployments) but the object worlds differ.
- **vs Approval Workflow Platform**: generic approvals over arbitrary business requests; no delivery semantics, no pipeline/deployment objects, no policy-as-code evaluation of delivery artifacts.
- **vs Engineering Productivity Analytics**: analytics observes and measures; governance enforces and gates. Products bundle both (LinearB, Jellyfish-class), but enforcement is the distinguishing structure.
- **vs Security Compliance Platform**: org-wide compliance posture (controls, frameworks, audits of the company); delivery governance is scoped to the software delivery pipeline specifically, though it feeds compliance evidence.
- **vs Release Management Platform**: release management orchestrates the release process; governance sets the rules the release process must pass. Overlap heavy in Copado-class products; keep-both with the seam "orchestrate vs define-and-enforce rules".
- Decisive removal test: remove policy evaluation/enforcement → analytics or release orchestration; remove delivery binding → generic policy engine / approval workflow; remove audit → enforcement tool, not governance.

## Historical / Market-Sample Check

Pre-policy-as-code era: delivery governance existed as configured approval rules, sign-off matrices, and compliance scans (Copado-style rule enforcement predates OPA ubiquity; enterprise change-approval configurations in CI/CD tools). These satisfy the L0 core without Rego/OPA — so policy-as-code is a common modern implementation, not the invariant. Manual era (paper sign-offs, CAB meetings) lacks the system-held machine-evaluable policy and automatic evaluation — that is IT change management territory, confirming the seam. Historical check passed.

## Uncertainties

- Sleuth legacy docs unreachable; its inclusion rests on the current homepage's governance feature claims plus prior positioning — assertions about Sleuth kept weak.
- Opsera operational docs not fetched; governance mechanics inferred from official product pages (policy-as-code claim, activity logs) — kept at moderate strength.
- Market naming is unstable: "software delivery management", "engineering management platform", "DevOps governance" overlap; the leaf is defined by the governance function, not by vendor category labels.
- Whether pure-play standalone governance products (no host platform) form a large market segment is unclear; the sampled market mostly embeds governance in delivery platforms. Recorded as a taxonomy observation, not resolved unilaterally.

## Final Synthesis

The Type is best understood as the **governance layer of software delivery**: it holds the organization's delivery rules as enforceable policy, evaluates real delivery events against them at defined gates with blocking/warning/approval outcomes, and keeps attributed audit evidence — across teams, projects, and commonly multiple tools. Everything else (policy-as-code languages, DORA dashboards, regulated-industry packaging, AI-agent governance) is mature structure or variant.
