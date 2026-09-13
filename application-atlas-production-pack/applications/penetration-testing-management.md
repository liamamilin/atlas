# Penetration Testing Management

## Overview

A **Penetration Testing Management** application is the system of record for offensive security testing organized as managed engagements. It exists to make a penetration test — an authorized, simulated attack against defined systems, carried out by identified testers within bounded rules — into a managed piece of work: scoped and scheduled before it runs, recorded while it runs, and tracked through remediation after it runs.

The problem it solves is specific. A penetration test involves parties who must coordinate but not fully trust each other: the asset owner who authorizes the test, the testers who execute it, and the stakeholders who must fix what is found. Without a shared system, the engagement lives in contracts, spreadsheets, chat threads, and word-processor reports; findings get lost between test and fix, retests are ad hoc, and nobody can show what was tested, what was found, and what was done about it. A PTM application gives the engagement a record, gives its findings a lifecycle, and gives both sides one place to meet.

The defining core is small:

```text
Engagement (scoped, authorized, staffed test undertaking)
└── Findings (evidenced vulnerability records produced by the test)
    └── Lifecycle through remediation verification
        (planned → executed → reported → fixed-and-retested or accepted-risk → closed)
```

Everything else commonly associated with the category — tester marketplaces, continuous testing programs, compliance attestation letters, scanner integrations, AI-assisted report writing — is widespread but not what makes the product a PTM system.

## Users & Context

The application sits between three parties whose work must stay separated but coordinated:

**Primary users on the testing side:**

- **Engagement manager / pentest lead** — scopes the test, schedules it, assigns testers, reviews findings before delivery, owns the report. In provider models this role is staffed by the vendor; in in-house models by the organization's own offensive team.
- **Penetration testers** — execute the test against the scoped targets, record findings with evidence as they work, answer client questions, and perform retests after fixes.

**Primary users on the client side:**

- **Security manager / asset owner** — requests and scopes engagements, authorizes targets and test windows, tracks findings to closure, and consumes the report as assurance evidence.
- **Remediation owners** (developers, IT operations) — receive findings as work items, fix them, and submit them for retest.

**Secondary users:**

- **Compliance and risk stakeholders** — consume attestation letters and framework-mapped reports as evidence that independent security testing happens.
- **Executives** — read summary-level posture and trend reporting across engagements.

The context is professional offensive security: web, mobile, API, network, cloud, and increasingly AI/LLM assets, tested by internal teams, security consultancies, or provider platforms with staff or vetted-community testers. The work is episodic by nature — an engagement has a beginning, a bounded window, and an end — even when organizations run engagements continuously.

## Core Model

### The Defining Core

**The engagement.** The unit of record is the engagement — one offensive-security test undertaking. It is persistent and individually identified, and it carries the structures that make an attack test legitimate:

- **Scope** — the targets to be tested (assets such as a web application, API, network range, or cloud environment) and, just as importantly, what is out of scope.
- **Test window** — the bounded period during which testing may occur.
- **Authorization context** — who may test what, under which rules: permitted techniques, knowledge level given to testers, exclusions, and emergency contacts.
- **Assigned testers** — the identified people executing the test, with a lead responsible for the team and the deliverable.

Remove the engagement record and the product becomes a findings tracker or a scheduling tool — there is no test undertaking to manage.

**Findings.** The engagement's security output is the finding: a structured record of one discovered vulnerability, bound to the engagement and to the affected target. A finding carries what was found, where, the evidence that proves it (screenshots, request fragments, proof-of-concept steps), a severity, and remediation guidance. Findings are reviewed before they reach the client — triage and quality review are part of the record, not an afterthought. Remove findings and the product is authorization paperwork with no security result.

**The lifecycle through remediation verification.** The engagement advances through recognizable states — planned, in execution, reported — and its findings are tracked to resolution. A finding is closed in one of two ways: it is fixed and a retest confirms the fix (the retest is recorded against the same finding), or the organization formally accepts the risk. The engagement closes when its findings reach one of those ends. This loop is what turns a one-shot report into management. Remove it and the product is a report generator.

### Standard Capabilities

Mature products build the following around the core. They make the Type practical; they do not define it.

- **Asset and target catalogs** — persistent records of the things that get tested (applications, APIs, hosts, cloud accounts), reusable across engagements, often with environment designations (production, staging, development).
- **Scoping machinery** — structured ways to size and bound a test: scoping parameters per asset type, test-period selection, and in provider models, pricing that scales with scope.
- **Methodology and coverage structures** — test plans or checklists mapped to industry frameworks (OWASP Top 10 family, OSSTMM, PTES, MITRE ATT&CK), attached to the engagement and worked as tasks, so coverage is visible and repeatable.
- **Findings-quality machinery** — triage states, deduplication, severity models (CVSS-family scoring or impact-times-likelihood rating), and reusable findings libraries so the team's standard write-ups and ratings survive personnel changes.
- **Report generation** — templated deliverables combining an executive summary with technical finding detail; attestation-style letters for compliance audiences; branded or co-branded variants.
- **Client-facing surfaces** — portals or channels where the client side sees findings (often as they are discovered), communicates with testers, and tracks remediation progress.
- **Remediation handoff** — pushing findings into ticketing systems (Jira, ServiceNow, GitHub/GitLab/Azure DevOps class) or tracking remediation in-product, with retest workflows closing the loop.
- **Tester staffing and scheduling** — assignment by skill and technology, capacity and workload management, and in provider models, matching testers to the engagement's stack.
- **Program analytics** — trends across engagements, per-asset or per-client history, and risk-reduction over time.
- **Integrations** — ingestion of scanner output alongside manual findings, APIs and webhooks, notification channels.

## How It Works

### Scope and authorize the engagement

```text
Select or create the asset(s) to test
→ define scope (targets, boundaries, exclusions)
→ set the test window
→ agree the rules (knowledge level, permitted techniques, credentials, contacts)
→ submit for review / authorization
→ engagement is planned and testers are assigned
```

In provider models the provider reviews the submission, confirms the schedule, and staffs the test from its tester pool; a communication channel for the engagement is opened. In in-house models the organization's own lead performs the same steps with its own testers. Either way, the engagement now exists as a record both sides can see.

### Execute the test and record findings

```text
Testers work the scoped targets within the window
→ findings are recorded as they are discovered
   (what, where, evidence, initial severity)
→ findings are triaged and validated
   (invalid ones declined; duplicates merged; out-of-scope ones flagged)
→ the client can start remediating confirmed findings during the test
```

Real-time delivery is a characteristic behavior: findings reach the client side while testing continues, not only in the final report. Communication about findings happens in the platform (threads on the finding, dedicated channels), keeping the exchange attached to the record.

### Report, remediate, retest, close

```text
Testing window ends
→ the lead compiles the report
   (executive summary, scope and methodology, findings with evidence and severity,
    recommendations, remediation status)
→ client remediates each finding
→ per finding: fix → submit for retest → retest confirms (fixed)
                or issue persists (back to remediation)
                or risk formally accepted
→ all findings resolved → engagement closes
→ report retained as the engagement's deliverable and assurance evidence
```

The retest is recorded against the same finding, so the engagement's history shows not just what was found but what was done about it. Open findings can carry into a follow-up engagement on the same asset, where they are tracked for verification rather than rediscovered.

### Run a program, not just a test

Organizations that test continuously repeat this loop across assets and time. The system accumulates the history: findings per asset, remediation speed, recurrence of issues across engagements, and trend reporting for management and clients. Scheduling machinery balances tester capacity against inbound demand.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Engagement list / scheduler

The program-level entry surface.

- lists engagements with their state (planned, live, in remediation, closed), assets, testers, and dates
- manages inbound scheduling requests and tester workload
- primary actions: create engagement, schedule, assign testers, open an engagement

### Engagement detail

The workspace for one test undertaking.

- scope and targets, test window, authorization context, assigned testers, activity timeline
- communication channel or thread set for the engagement
- primary actions: edit scope, message participants, advance state, pause or cancel

### Findings list and finding detail

The security output surface.

- findings filtered by state (triaging, pending fix, ready for retest, fixed, accepted risk) and severity
- finding detail: description, affected target/URLs, evidence (screenshots, request fragments, proof of concept), severity, remediation guidance, state history
- primary actions: triage, validate or decline, set severity, submit for retest, accept risk, push to ticketing

### Report builder / report view

The deliverable surface.

- report sections assembled from engagement data (summary, scope, methodology, findings, recommendations, remediation status)
- template selection and branding; export to document formats
- primary actions: generate, review, publish, download, share

### Client portal

The client-side window onto engagements (prominent in provider and service-provider models).

- real-time view of findings and their states, engagement progress, historical results per asset
- communication with testers on specific findings
- primary actions: review findings, ask questions, track remediation, download reports

### Administration

Organization-level configuration: users and roles, tester pools, integrations (ticketing, scanners), templates and findings libraries, security settings.

## Important Rules / Behaviors

### Authorization bounds the test

Testing happens only against scoped targets within the test window, under the agreed rules. Findings discovered outside scope are flagged as out of scope rather than silently absorbed. Some rules are explicit safety rules: certain destructive techniques (such as denial-of-service testing) are commonly excluded from standard engagements, and testing against third-party services is limited to the integration points, not the third party's own systems.

### Findings are reviewed before they count

A discovered vulnerability typically enters a triage state where it is validated and severity is assigned before it becomes a client-visible finding. Invalid reports are declined, duplicates merged. This review gate is part of the record, protecting both sides from noise and from premature escalation.

### The retest closes the loop

A fix is not "done" until a retest confirms it; a failed retest returns the finding to remediation. Accepting a risk is a formal, recorded alternative to fixing. The engagement stays open until every finding reaches one of these ends.

### Findings are sensitive by nature

A findings corpus is a map of an organization's weaknesses. Access is scoped per engagement and per organization; evidence and reports are handled as confidential data. This is why delivery models that keep data entirely on the buyer's infrastructure exist as a first-class variant, not an edge case.

### Severity is a model, not a measurement

Severity is assigned through a defined rating approach — CVSS-family scoring or impact-and-likelihood rating — applied consistently across testers. Shared findings libraries and review workflows exist precisely so that the same finding gets the same rating regardless of who found it.

### The report is a deliverable with standing

Reports serve audiences beyond the testing team: management, auditors, regulators, customers. Attestation-style deliverables exist because third parties need evidence that independent testing occurred, not just a list of bugs.

## Variants

- **Provider / PtaaS model** — the platform supplies vetted testers (employees, contractors, or a vetted researcher community) alongside the management system; the client scopes and consumes. Commercial models include per-scope credits and subscriptions.
- **In-house model** — the organization's own offensive team (or a contracted third party) runs engagements on the platform; the system provides the engagement, findings, and reporting machinery without supplying testers.
- **Service-provider model** — consultancies and MSSPs run engagements for many clients on one platform, with white-labeled client portals and per-client history.
- **Point-in-time vs continuous programs** — single bounded engagements vs rolling test cycles over an asset base; the same core model serves both, with continuous programs emphasizing scheduling, carried-over findings, and trend analytics.
- **Delivery poles** — multi-tenant SaaS vs fully self-hosted deployment (including air-gapped installations), the latter driven by the sensitivity of findings data.
- **Service-line breadth** — the same engagement machinery covers web, mobile, API, internal/external network, cloud, desktop, AI/LLM testing, and adjacent service lines such as secure code review or social engineering.
- **Automated execution modules** — some products add autonomous or scanner-driven testing beside the human engagement model. Where the automated layer becomes the primary structure (continuous technique execution with control-response grading, no engagement record), the product has crossed into Breach & Attack Simulation territory.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Breach & Attack Simulation | adjacent, most easily confused | BAS runs a maintained library of attack simulations continuously against the organization's own controls and records each control's response (prevented/detected/missed); PTM manages scoped, authorized engagements staffed by testers that produce findings about the tested targets. "Automated pentesting" products straddle the seam |
| Vulnerability Management | downstream complement | VM owns the organization-wide vulnerability record and remediation lifecycle across all sources; PTM produces findings through authorized engagements and hands them over. A PTM product does not manage the patch/vuln backlog |
| DAST / IAST | tooling inside the engagement | DAST/IAST are testing engines that exercise applications and emit findings; a pentest engagement uses such tools during execution. The engagement-management layer is the Type |
| Attack Surface Management | upstream complement | ASM discovers and inventories externally exposed assets; PTM tests a scoped, authorized target set. ASM output can feed PTM scope; some vendors sell both as separate products |
| Bug bounty / vulnerability disclosure platforms | adjacent crowd model | open, continuous, unscoped submission by arbitrary researchers vs scoped, authorized, staffed engagements; the authorization boundary is the seam |
| Security Program Management / GRC | program layer above | governs security activities and control frameworks at program level; PTM is the engagement-level execution system whose outputs (attestation letters, framework-mapped reports) serve it |
| Professional Services Automation | generic sibling | PSA manages billable client work generically (resourcing, time, billing); PTM carries the offensive-security-specific object model — scope, authorization, methodology coverage, findings, retest |
| Cyber Incident Response | different object | findings are pre-incident vulnerabilities recorded under authorization; incidents are detected events with their own lifecycle |

The boundary with Breach & Attack Simulation is the most important one, because both attack the organization from the attacker's side. The structural difference is whether the system's record is an engagement — scoped, authorized, staffed, producing findings that individuals must remediate — or a continuous validation loop grading control responses against a technique library.

## Representative Products

- **Cobalt** — Pentest as a Service platform with a marketplace tester pool, and a pentest-management mode that lets organizations run their own testers on the same engagement machinery.
- **Synack** — managed continuous pentesting combining a vetted researcher community with an autonomous AI testing agent.
- **PlexTrac** — pentest reporting and management platform for internal offensive teams and service providers, extending toward exposure management.
- **Dradis** — self-hosted pentest reporting and management platform with an open-source Community Edition dating to 2007; the data-sovereignty pole and the sample's historical anchor.

## Sources

Research date: **2026-09-09**

- Cobalt Product Documentation — Pentest Process, Pentest States, Finding States, Engagements Overview, In House Pentests, Create a Pentest, Scope & Test Period, Contents of a Pentest Report, User Roles and Permissions, Methodologies Overview: https://docs.cobalt.io/
- Synack — official site (platform structure, products, solutions): https://www.synack.com/
- PlexTrac — Platform Overview and homepage: https://plextrac.com/platform/overview/
- Dradis — product site (Pro) and Community Edition site: https://dradis.com/ , https://dradisframework.com/ce/

> Sourcing limitations: PlexTrac's help center was not reachable (authentication-gated), so its behavior is described from official product pages only, without precise state names or operational defaults. Synack's product documentation is login-gated; its description stays at platform level. AttackForge and Reconmap could not be verified (site unreachable / domain repurposed) and are excluded. Precise vendor figures (test-period lengths, tester counts, template counts, marketing percentages) are intentionally not stated in this document; they remain in the Research Notes.
