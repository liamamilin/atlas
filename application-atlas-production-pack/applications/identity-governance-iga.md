# Identity Governance / IGA

## Overview

An **Identity Governance and Administration (IGA)** application is an organization's system for governing who has access to what — deciding whether access should exist, recording those decisions against accountable people, driving the actual access state to match, and proving all of it to auditors.

The defining core is a closed loop with three parts:

```text
Access model of record
  ("who has what access", built from connected systems)
        ↕ reconciled
Structured human decisions
  (requests + approvals, periodic certifications, policy violations)
        ↓
Remediation toward the desired state
  (grant / revoke / change access; execution native or delegated)
```

IGA does not authenticate anyone and does not enforce access at sign-in time — that is the job of the neighboring identity-and-access (IAM) infrastructure. IGA sits above that operating plane and governs it over time: what *should* each person have, what they *actually* have, whether the two match, and whether someone has reviewed and signed off on the difference.

## Users & Context

IGA serves an organization managing access for its workforce — employees, contractors, partners, and sponsored guests — across many connected applications and systems. The population is administered by the organization, not self-enrolled by end customers.

Primary users:

- **IGA / IAM administrators** — connect target systems, configure aggregation, define roles and policies, set up and monitor certification campaigns and provisioning.
- **Line managers** — approve their reports' access requests; periodically certify that their reports' access is still appropriate.
- **Application / resource owners** — approve access to the resources they own; certify who holds entitlements on their systems; take ownership of orphaned accounts.
- **Employees (end users)** — request the access they need, view what they have, and lose access automatically when their role changes or they leave.

Secondary users:

- **Compliance and security teams** — define separation-of-duties policies, monitor violations, run campaigns.
- **Internal and external auditors** — consume the decision trail: who approved what access, when, and what was reviewed and signed off.

The recurring problem this software exists to solve: people accumulate access as they change roles, joiners wait too long for access, leavers keep access they should not have, and no one can demonstrate to an auditor who has what and why.

## Core Model

### The defining structure

Three structures jointly define the Type. Remove any one and the product stops being IGA.

**1. Access model of record.** The system maintains a unified, identity-resolved picture of who has what access. It connects to target systems (directories, business applications, cloud platforms), aggregates their accounts and entitlements, and correlates each person's scattered accounts into a single identity record. Around that identity it organizes access into a hierarchy: individual **entitlements** discovered from the connected systems, grouped into bundles (called access profiles, access packages, or similar), grouped again into **roles** that can be assigned by attribute or request. The applications and entitlements themselves carry business meaning — ownership, descriptions, risk classifications — so that humans can decide about them.

**2. Structured human decision processes.** Access decisions are routed to specific accountable people through defined mechanisms:

- **Access requests** — a self-service catalog where users (or their managers) request bundles or entitlements; requests flow through approval chains that typically involve the requester's manager, the resource owner, and, for sensitive access, security reviewers. Every approval or denial is recorded.
- **Certifications / attestations / access reviews** — recurring campaigns in which reviewers (managers, resource owners, role owners) are presented with the access held by identities or the contents of entitlements and must confirm or revoke each item. Campaigns are scoped (which population, which systems, which reviewers), tracked for progress, and closed with a sign-off.
- **Policy-violation handling** — when a rule such as a separation-of-duties constraint is breached (or would be breached by a pending grant), the system flags it and routes it for resolution.

**3. Desired-state direction with reconciliation.** Recorded decisions are not just filed — they change things. Approvals and certification outcomes trigger grants or revocations in the target systems (executed directly by the product's provisioning machinery or handed off to IT processes for execution). Conversely, changes made directly inside target systems are detected and reconciled back into the model, so the record does not silently drift from reality. The maintained invariant is that the *actual* access state, the *recorded* state, and the *approved* desired state converge — assignments can sit in states such as approved, pending removal, orphaned, or in violation until they are resolved.

### Standard capabilities that mature products add

These are common across mature products and expected by the market, but a product missing some of them is still IGA:

- **Identity lifecycle automation** — access and account changes triggered by lifecycle events driven by the HR system as the source of truth: a joiner receives birthright access for their role, a mover's access is adjusted, a leaver's accounts and access are removed. Without this automation the governance loop still stands; with it, the loop runs itself at the edges.
- **Provisioning integration** — connector libraries and standard provisioning protocols for writing account and access changes into large numbers of connected systems, with tracking of executed changes.
- **Entitlement catalog** — discovered entitlements enriched with descriptions, owners, and risk levels so reviewers and requesters can understand what they are deciding on.
- **Role machinery** — role definitions, attribute-based or rule-based assignment, role versioning, and temporary/time-bound access (start and end dates).
- **Separation-of-duties (SoD) policy engine** — rules that define toxic access combinations; evaluated before grants are approved and continuously against the held access, with violation reports and remediation paths.
- **Orphan account management** — accounts whose owner has disappeared are surfaced for reassignment or deletion.
- **Access history and decision trail** — for any identity: how they acquired each entitlement, who approved it, when it changed, when it was revoked. This is the substance auditors consume.
- **Dashboards, compliance reporting, and search** — current compliance status, violation summaries, campaign progress, and ad-hoc queries over identities, entitlements, and events.
- **Delegated administration** — governance groups, scoping, and segmentation so large deployments can distribute administrative work safely.
- **AI assistance (era-current)** — recommendations on approve/revoke decisions during reviews, outlier detection (identities whose access diverges from peers), role discovery and role mining from observed access patterns, and generated entitlement descriptions.

The signature capability of the Type — the one a reader will meet in every product researched for this document — is the certification campaign. But even that sits on top of the core: a product with unified access visibility, requests with approvals, and reconciliation, but no campaign machinery, is still recognizable IGA (this was the historical shape of the category before audit regimes made attestations universal).

## How It Works

### Connect the systems and build the model of record

```text
Register a target system (directory, application, cloud platform)
→ connect it via a connector or standard protocol
→ aggregate its accounts and entitlements
→ correlate accounts to unified identities (by rule, by HR data, by manager chain)
→ enrich entitlements with owners, descriptions, risk
→ repeat for each system under governance
```

From this point on, "who has what access" is a query the organization can answer in one place, and aggregation runs on a schedule to keep the picture current. Direct changes inside target systems are detected and folded back in.

### Request access

```text
Employee (or their manager) opens the access catalog
→ selects a bundle or entitlement
→ request routes through the approval chain
  (manager → resource owner → security, as configured)
→ each approver approves or denies, with the decision recorded
→ on final approval, provisioning delivers the access to the target system
→ the grant lands in the access model and the access history
```

Separation-of-duties checks can reject the request outright if it would create a toxic combination, before any human approves it.

### Certify the access that exists

```text
Administrator designs a campaign
  (scope: population / applications / roles; reviewers; cadence; escalation)
→ campaign opens; reviewers receive their work items
→ reviewer confirms or revokes each item (with recommendations and
  outlier flags where AI assistance is enabled)
→ revocations trigger remediation in the target systems
→ campaign closes with a sign-off; results become audit evidence
```

Certification is how the loop catches the slow drift that requests cannot see: access that was correct when granted but is no longer needed.

### Run the lifecycle

```text
HR event (hire / transfer / leave)
→ identity created / updated / disabled in the model
→ birthright access granted or adjusted or revoked automatically
→ accounts and entitlements provisioned or deprovisioned in targets
→ every change recorded in the access history
```

### Prove it

Reports and dashboards answer the auditor's questions directly: who has access to a given application and how they got it; what was reviewed, by whom, and when; which SoD violations exist and how they were resolved; where accounts are orphaned. The decision trail — who approved what, when, and who signed off — is the product's evidentiary output.

## Interfaces

Exact layouts and names vary by product; these are the recurring surfaces.

**Administrative console.** Where administrators configure sources and connectors, aggregation schedules, correlation rules, roles and bundles, policies, campaign templates, and provisioning. Typically the largest and most technical surface.

**Access catalog (end-user).** A searchable storefront of requestable bundles and entitlements, with request status and the user's current access. Purpose: let users help themselves without an IT ticket.

**Approval queue / inbox.** The approver's work surface: pending requests with requester, item, and justification; approve / deny with comments; escalation when approvers are absent.

**Certification campaign workspace.** The reviewer's work surface: items to decide (an identity's access, an entitlement's holders, a role's composition), with context (usage, recommendations, peer comparison where available), one-decision-at-a-time flow, reassignment, progress tracking, and final sign-off.

**Identity and access detail.** The 360° view of one identity: linked accounts, held entitlements and roles, membership, access history, and lifecycle state. The pivot surface for help desk, managers, and auditors alike.

**Dashboards and reports.** Compliance status, violation summaries, campaign progress, orphan accounts, provisioning outcomes; exportable audit reports.

**Policy and SoD console.** Rule definitions, violation lists, simulation of rules against current access, remediation routing.

## Important Rules / Behaviors

- **Decisions have consequences.** A certification "revoke" or a denied request is not advisory — it initiates deprovisioning (or a documented handoff to those who execute it). Recording without action is what distinguishes an audit report from IGA.
- **The model must not drift.** Changes made directly in target systems (bypassing governance) are detected and reconciled; unmanaged drift defeats the model of record.
- **Least privilege is the direction of travel.** Reviews, expiry, and lifecycle automation all pull toward "no more access than the current role requires"; time-bound access and expiring packages enforce it mechanically.
- **Separation of duties binds at the gate.** SoD rules are checked when access is requested, and continuously against held access; violations are workflow items with owners, not just log entries.
- **Accountability is personal.** Approvals and certification sign-offs attach to named individuals (with reassignment and delegation handled explicitly, e.g., when a reviewer is absent or leaves); some products support re-authentication for sensitive approvals and electronic signatures for sign-off.
- **Orphans are surfaced, not ignored.** An account or assignment without an accountable owner is a flagged state awaiting reassignment or deletion.
- **Sensitive access gets more eyes.** Approval chains and review frequency typically deepen with the sensitivity or privilege level of the access; privileged roles commonly receive just-in-time activation with review — while privileged *credential vaulting and session control* remain the separate PAM territory.

## Variants

- **Deployment**: multi-tenant SaaS; on-premises appliances for enterprises that must keep governance data in-house; dedicated single-tenant cloud for regulated industries and government.
- **Packaging**: standalone pure-play IGA platform (the largest product families); governance as a separately licensed product layered on an existing cloud directory/IAM suite; IGA capability modules sold beside privileged, cloud-entitlement, and data-governance products from the same vendor.
- **Process formality**: some vendors ship a published best-practice process framework and structured implementation methodology; others leave the loop free-form for the customer to configure.
- **Population scope**: workforce only; plus sponsored guests, partners, and non-employees with their own lifecycle; plus machine identities and service accounts; plus AI agents (era-current — every researched vendor family now extends governance to agents).
- **Adjacency depth**: light data classification tags on resources vs full unstructured-data governance (the latter is its own Type); JIT privileged activation inside governance vs full PAM as a separate product.
- **Compliance emphasis**: audit/attestation-driven deployments (SOX heritage) and data-protection-driven deployments (GDPR heritage) use the same machinery with different vocabulary and campaign emphasis.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Identity & Access Management / IAM | closest sibling — same subject, different plane | IAM *operates* access: authenticates the person and enforces grants at runtime. IGA *governs* access: decides what grants should exist over time, reconciles actual vs desired, and produces audit evidence. IGA does not authenticate; IAM does not run review campaigns. Market confirmation: vendors ship them as separate products. |
| Single Sign-on / MFA | capability within IAM | Federation and factor enforcement are runtime capabilities; they appear in IGA products only as governed objects, never as the governance loop itself. |
| Privileged Access Management / PAM | adjacent | PAM's objects are privileged accounts, credential vaulting, and session brokering. IGA governs who *holds* privileged grants; PAM controls how privileged *sessions and credentials* are used. |
| Customer Identity / CIAM | adjacent — population boundary | CIAM's population self-enrolls and self-manages; IGA's population is org-administered workers and sponsored guests. |
| Data Access Governance | adjacent — object boundary | DAG governs the access state of data stores (file shares, unstructured data); IGA governs identity-to-application entitlements. Same vendors ship them as separate products; classification tags are the thin overlap. |
| GRC / Compliance Management Platform | downstream consumer | GRC manages the organization's controls and obligations across domains; IGA manages access specifically and *supplies* evidence (sign-offs, decision trails) that GRC consumes. |
| Approval Workflow / ITSM Platform | mechanism overlap | Generic workflow tools move tasks but hold no entitlement model, no SoD semantics, no provisioning execution. IGA may hand remediation work to ITSM, but the governance loop stays in IGA. |
| HRIS | upstream source | HR holds employment truth and feeds lifecycle events to IGA; IGA holds access truth and feeds nothing back to HR. |

## Representative Products

Researched for this document:

- **SailPoint** — Identity Security Cloud (SaaS) and IdentityIQ (on-premises); the pure-play reference family for the Type.
- **Microsoft Entra ID Governance** — governance product layered on a cloud directory/IAM suite.
- **Omada Identity** — enterprise IGA delivered as SaaS, dedicated private tenant, or on-premises, with a published best-practice process framework.

Additional market anchors (structure not verified from their documentation in this pass): Saviynt, One Identity (Identity Manager).

## Sources

Research date: **2026-09-08**

- SailPoint — Product Documentation portal, Identity Security Cloud admin help, IdentityIQ 8.5 overview: https://documentation.sailpoint.com/ , https://documentation.sailpoint.com/saas/help/index.html , https://documentation.sailpoint.com/identityiq/help/
- Microsoft — Entra ID Governance overview (Microsoft Learn): https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
- Omada — Omada Identity Cloud product page and Identity Governance functionality page: https://omadaidentity.com/products/omada-identity-cloud/ , https://omadaidentity.com/products/functionality/identity-governance/

> Sourcing limitation: official documentation for Saviynt (JavaScript-gated docs site; product URL returned 404) and One Identity (unreachable) could not be fetched after repeated attempts. They are listed as market anchors only and no operational claims in this document draw on them. SailPoint and Microsoft claims rest on full operational documentation; Omada claims rest on product and capability pages. No numeric limits, default cadences, or licensing gates are asserted.
