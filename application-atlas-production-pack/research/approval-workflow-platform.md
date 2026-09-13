# Research Notes — Approval Workflow Platform

## Research Goal

Understand what an Approval Workflow Platform is as an Application Type: what core objects it manages, how a request moves from submission to recorded authorization decision, what rules govern routing and decisions, and where its boundary lies against adjacent Types (Workflow Management Platform, BPM Platform, Enterprise Request Management, Form Builder, domain-specific approval gates such as Deal Desk or IT Change Management).

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis):** an application whose center of gravity is a submitted request (leave, expense, purchase, access, document, discount…) routed to one or more designated approvers who record approve/reject/return decisions, with state and attributable history kept on the request.
- **Nearest neighbors:** Workflow Management Platform (broader automation of task sequences), Business Process Management Platform (modeling + orchestration), Enterprise Request Management (intake + fulfillment), Form Builder (data collection without routing), Deal Desk / Purchase Order Management / IT Change Management (domain objects with embedded approval gates).
- **Unknowns going in:** how products define approval chains; the decision verb set; how approvers are assigned; delegation/escalation behavior; whether lightweight (no-license) approver participation is a pattern; exact state vocabularies.

## Research Questions

1. What is the central managed object (request / ticket / card / process instance / approval task)?
2. How is the approval path defined (chain, stages, parallel branches, conditions)?
3. How are approvers designated (named person, role, group, "manager of requester", external email/guest)?
4. What decisions exist (approve / reject / return-for-revision / delegate / escalate)? Are comments attached?
5. What is the request's state lifecycle (draft → submitted → under review → approved/rejected; withdrawn; revised)?
6. How are reminders, SLAs, and escalations handled when approvers don't act?
7. What happens after the final decision (downstream handoff to ERP/HR/identity/document systems)?
8. What admin surfaces exist (form builder, workflow designer, roles, policies)? What end-user surfaces (requester portal, approver inbox, mobile, email/chat response)?
9. What audit/history is retained and surfaced?
10. Where is the boundary against generic workflow/BPM products and against domain-specific approval gates?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, and different customer tier:

| Product | Philosophy / Tier | Sample rationale |
|---|---|---|
| **Kissflow** | horizontal no-code/low-code workflow platform; approval workflows as a first-class use case; mid-market→enterprise | sells "approval workflow software" explicitly; publishes a canonical end-to-end approval flow |
| **Cflow** | SMB/mid-market approval-centric workflow automation (Cavintek) | brands a dedicated "Approval Software" product line; lightweight approver participation (secure-link approval without login) |
| **Nutrient Workflow** (Integrify lineage; acquired by Nutrient) | enterprise approval/document workflow; regulated industries; cloud + on-premises | long-standing enterprise approval-workflow vendor; strongest structural feature documentation (Process Builder, parallel/conditional paths, SLAs, mobile approvals) |
| **onPhase Forms (frevvo lineage; acquired by onPhase 2022)** | forms-first approval workflows; SMB/education/finance teams | forms+approval heritage; route submissions through multi-step workflows with conditional rules |

Contrast sample (platform-native, for the historical/market-sample check and Type boundary):

- **Microsoft Power Automate — Approvals**: approvals as an action inside a general automation platform, with an Approvals center, email/mobile response, sequential/parallel patterns, cancel, guest approvers.

## Sources

Research date: **2026-09-06**. All fetches by WebFetch from official vendor surfaces.

| # | Source | Layer | Notes |
|---|---|---|---|
| 1 | Kissflow — Workflow Management and Automation Platform (`kissflow.com/workflow/`) | A (product page, Tier 2) | positioning, feature pillars (dynamic routing, governance/access permissions), app templates (Budget Approval, Expense, Leave, Travel Reimbursement, IT Service Requests) |
| 2 | Kissflow — Approval Workflow Software (`kissflow.com/workflow/approval-workflow-software/`) | A (product page + educational content, Tier 2) | definition of the category; 7-step end-to-end flow (submission, validation, coding, routing, review/decision, exception handling); FAQ distinguishing approval **workflow** software (steps/routing/decision logic) from approval **management** software (policy layer: who can approve what, segregation of duties, audit policy); FAQ: conditional logic, parallel and sequential approvals, role-based routing, SLA escalation configured without code |
| 3 | Cflow — homepage + Approval Software page (`cflowapps.com`, `cflowapps.com/platform/approval-software/`) | A (product pages, Tier 2) | approval stages and reviewers chosen in visual form builder; auto-approvals from predefined conditions; approval via secure link without login; "approve without a full user license" claim; AI decisioning (2026-era) |
| 4 | Cflow — Help Center / Knowledge Base (`cflowapps.com/help/`) | A (support docs, Tier 1-ish) | KB categories: Workflow Creation, Workflow Stages, Workflow Properties, Admin Users/Roles/Permissions, Security, Reports, Analytics, Mobile Application; "user = person with credentials, can play multiple roles"; reminders/weekend/holiday-calendar configuration; per-attachment 20 MB limit, 30 GB storage; on-premises option; REST API |
| 5 | Nutrient Workflow (Integrify lineage) — homepage + overview (`nutrient.io`, `nutrient.io/workflow-automation/overview/`) | A (product pages, Tier 2) | Process Builder (approvals, escalations, SLAs; parallel and conditional paths; group and role-based assignments; deadline enforcement and alerts); Form Designer (validation, conditional logic, prefilled fields); document viewing embedded; Reporting (SLA compliance, overdue tasks, exportable audit logs); mobile app (in-app approvals, push notifications); agentic approvals (AI recommendations); deployment cloud/private-cloud/on-prem/hybrid; SSO/SCIM |
| 6 | onPhase Forms (frevvo) — homepage + Forms & Workflow solution page (`onphase.com`, `onphase.com/forms-workflow-automation`) | A (product pages, Tier 2) | multi-step workflows with conditional rules to auto-route approvals and escalations; built-in audit trail ("every change, comment, and sign-off… captured automatically"); reporting (form status, approval timelines, bottlenecks); invoice routing by amount/department/vendor; integrations SharePoint/Google Drive/SQL/API |
| 7 | onPhase/frevvo documentation portal (`docs.frevvo.com` → `frevvo-docs.atlassian.net`) | A (docs home only) | docs moved to Atlassian wiki (frevvo v11.0 on-prem space; DocuPhase Forms v11.3 cloud space); legacy deep links broken — deeper operational pages not fetched (source-access limitation) |
| 8 | Microsoft Learn — "Create and test an approval workflow with Power Automate" (`learn.microsoft.com/en-us/power-automate/modern-approvals`) | A (official docs, Tier 1) | approvals as flow action ("Start and wait for an approval"); approval types; assigned-to by email; approver responds from email inbox, approvals center, or mobile app; response = Approve/Reject + comments; sequential and parallel approval patterns; sender can cancel a sent approval; History tab; long-running approvals (30 days+) via Dataverse; guest (external) approvers via Entra B2B |

Evidence-layer usage: claims below are tagged **[A]** (directly observed on one product's official source) or **[B]** (cross-product commonality across the sample).

## Product Observations

### Kissflow [A]

- Positions approval workflow software as a category: "handles the start-to-finish process of getting something authorised" — purchase requisition, leave request, sales discount above threshold, vendor master-data change, network access request, marketing budget.
- Canonical end-to-end shape (their framing): **request submission** (structured form, fields/validation configured per workflow type) → **validation** (data quality, attachments, pre-approval rules: budget remaining, vendor in master data, contract on file, duplicate detection) → **coding** (GL account/cost centre/project) → **routing** (based on rules — amount, department, request type, risk) → **review and decision** (approvers see full context, can ask for clarification, and **approve, reject, or send back for revision**; all actions **logged with timestamps**) → **exception handling** (SLA breach → automatic escalation, dedicated resolution queue) → (implicitly) downstream action in the system of record (e.g., purchase order in ERP, permission provisioning in identity system) + retained findable audit trail.
- Failure modes it claims to replace: requests in inboxes, no system of record, no "where is my request" answer, quarter-end audit-trail reconstruction from email/chat, per-team inconsistent approval practice, approval in one tool / action in another.
- FAQ distinction: approval **workflow** software = steps, routing, decision logic; approval **management** software = policy layer (who can approve what, segregation of duties, audit policy); "most modern platforms handle both."
- Configuration claims: visual designer, drag-and-drop forms, conditional logic, **parallel and sequential approvals**, role-based routing, SLA escalation, all no-code; IT retains governance over publishing/integrations. Native integrations to ERP/identity systems (SAP, Oracle, NetSuite, Workday, Salesforce, ServiceNow, M365, Okta, Azure AD) + REST API/webhooks.
- Templates: employee expense claim, advance payment, travel reimbursement, performance appraisal, leave management, IT service request, change management, access request.
- Admin/governance: role-based access restricting sensitive information; dashboards for approval progress and bottlenecks.

### Cflow [A]

- Dedicated "Approval Software" page: "simplifies review and approval at every stage of your workflows."
- Visual form builder lets users choose **the number of approval stages and reviewers**.
- **Auto-approvals** execute routine decisions automatically using predefined conditions.
- **Approval without login**: reviewers approve requests through a secure link, no login required (works "without Public Forms"); homepage comparison table claims "Approve without a full user license."
- Automated alerts/notifications to stakeholders on pending requests; AI-powered routing to right reviewers + reminders "to keep approvals on schedule" (2026 AI positioning; traditional core described as rule-based routing: "moves requests between people based on fixed rules").
- FAQ feature list for the category: automated routing, **multi-level approvals**, role-based access, real-time tracking, notifications, **audit logs**, integration.
- Help Center structure [A]: Workflow Creation, **Workflow Stages**, Workflow Properties, Users/Roles/Permissions, Security Settings, Reports, Analytics, Document Designer, Mobile Application. Concepts: a **Request** is the workflow instance (carries attachments; admins set max file size; account-wide storage); **user** = credentialed person who can play multiple roles across workflows; admins configure **reminders**, weekends, holiday calendars (i.e., business-time aware notifications); mobile apps for Android/iOS; REST API; Slack/MS Teams notification channels; cloud (AWS) **or on-premises** hosting.
- Use-case pages: CapEx approval, procure-to-pay, invoice approval, vendor approval, expense approval.

### Nutrient Workflow (Integrify lineage) [A]

- Self-description: "automates approvals, document generation, forms, and compliance across every department"; low-code, document-driven processes.
- **Process Builder**: drag-and-drop workflow design "including approvals, escalations, and SLAs"; **parallel and conditional paths**; **group and role-based assignments**; **deadline enforcement and alerts**; real-time testing before deployment.
- **Form Designer**: drag-and-drop fields, validation, conditional logic, prefilled fields.
- Embedded **document viewing** inside workflows (access controls, version-aware) — review documents as part of the approval; premium add-ons: document generation, editing, markup/collaboration, e-signature, intelligent document processing.
- **Reporting**: real-time metrics and workload views, role-based dashboards, **exportable audit logs and history**, SLA compliance and overdue items.
- **Mobile application**: complete tasks, submit forms, **approve requests**; in-app approvals and comments; push notifications.
- **Agentic approvals** (AI): autonomous recommendations based on predefined rules and policies; every autonomous action logged with rationale.
- Deployment: cloud, private cloud, self-managed/on-premises, hybrid; SSO/SCIM/roles.
- Template library: expense/reimbursement, capital expenditure request, invoice approval, vendor invoice approval, purchase requisition, new vendor request, PTO/leave, timesheet approval, employee onboarding/offboarding, user access request, software change request, contract review, policy signoff… (HR/finance/IT/legal/ops/civic).
- Audience evidence: regulated industries (BP/SOX compliance story, government administration reviews), audit trails repeatedly emphasized.

### onPhase Forms (frevvo lineage) [A]

- Heritage: frevvo (forms + approval workflows) → DocuPhase → onPhase Forms (acquired 2022); "all frevvo functionality now lives within onPhase."
- **Visual workflow designer**: "design multi-step workflows and create conditional rules to auto-route approvals and escalations."
- **Drag-and-drop builder**: launch or create forms without IT; conditional rules & validation ("eliminate missing GL codes, cost, or approvals").
- **Built-in audit trail**: "every change, comment, and sign-off … captured automatically for instant audit readiness."
- **Reporting**: form status, approval timelines, bottlenecks in real time.
- Use cases: expense management; **invoice approvals routed automatically based on amount, department, or vendor, approvers notified instantly**; travel requests; purchase requests ("request, approve, order — without email ping-pong"); employee onboarding; sales orders.
- Integration: SharePoint, Google Drive, SQL databases, open API to ERP/CRM.
- Docs home [A]: documentation moved to Atlassian wiki (frevvo v11.0 on-prem; DocuPhase Forms v11.3 cloud); legacy `docs.frevvo.com` links no longer resolve. Deep operational pages not fetched — evidence for this product is product-page level.

### Microsoft Power Automate Approvals (contrast sample, platform-native) [A]

- Approval is an **action inside a flow** ("Start and wait for an approval") rather than a standalone product: trigger (e.g., new SharePoint list item) → create approval request (title, details, assigned to) → wait → branch on response (Approve/Reject + comments) → downstream actions (notify requester, update source system).
- Approval **types** selectable (and custom values allowed); documented patterns for **sequential** and **parallel** approvals.
- Approver response surfaces: **email inbox, the Approvals center in Power Automate, or the Power Automate mobile app**. Modern email clients show the request auto-updated as completed.
- Requester (sender) can **cancel** a sent approval; **History** tab lists canceled requests; long-running approvals (>30 days) require storing approvals in Dataverse.
- **External approvers**: Entra B2B guest users can be assigned approver role.
- Interpretation: proves the conceptual approval loop is implementable on any orchestration engine; a dedicated Approval Workflow Platform is the productized, admin-governed form of this loop (forms, routing rules, SLAs, dashboards, licensing for occasional approvers).

## Cross-product Comparison

| Dimension | Kissflow | Cflow | Nutrient Workflow (Integrify) | onPhase (frevvo) | Power Automate (contrast) |
|---|---|---|---|---|---|
| Central object | workflow/process instance carrying the approval | **Request** | process instance + tasks | form submission routed through workflow | approval request inside a flow |
| Path definition | visual designer; conditional logic; parallel + sequential approvals | approval stages + reviewers in visual builder; rules engine | Process Builder: parallel/conditional paths; group & role assignments | multi-step visual workflow with conditional rules | approval action; sequential/parallel patterns |
| Request capture | drag-and-drop forms, per-type fields/validation | visual form builder | Form Designer (validation, conditional, prefilled) | form builder (heritage core) | trigger-source record (e.g., SharePoint item) |
| Approver designation | role-based routing; rules on amount/department/type/risk | chosen reviewers per stage | named/group/role-based assignment | conditional routing rules | assigned to (email address); guest users |
| Decision verbs | approve / reject / **send back for revision** (+ clarification) | approve; auto-approve conditions | approve (+ escalation paths) | sign-off / approve (with comments) | **Approve / Reject** + comments |
| Inactivity handling | SLA escalation + exception queue | reminders (business-calendar aware) | SLA tracking, deadline enforcement, alerts | escalation rules | none built-in in fetched doc (manual handling; 30-day timeout) |
| Notifications | configurable notifications | alerts/reminders; Slack/Teams channel | push notifications; email | approvers notified instantly | email + approvals center + mobile |
| History/audit | all actions logged with timestamps | audit logs; role-based access | exportable audit logs and history; SLA compliance | built-in audit trail of every change/comment/sign-off | History tab; Dataverse for long-running |
| Downstream handoff | ERP (PO), identity provisioning | integration hub, REST API | document generation/signing; SAP/SharePoint | SharePoint/Drive/SQL; ERP/CRM API | flow actions update source systems |
| Occasional-approver access | SaaS sign-in (standard) | **secure link, no login** | mobile + email; roles | email notification | email response; guest accounts |
| AI posture (2026) | gen-AI suggestions; dynamic routing | AI agents auto-approve/escalate with rationale | agentic approvals (recommendations) | — (not evidenced) | — (not in fetched doc) |
| Deployment | SaaS (multi-region) | cloud **or on-premises** | cloud/private cloud/on-prem/hybrid | cloud (DocuPhase Forms) + on-prem (frevvo v11) | cloud service |

**Stable across the whole sample [B]:** request as the managed record; defined multi-step approver path; conditional routing on request data; approve/reject decisions with comments; state visible to requester and approvers; reminders/escalation for stalled requests (weakest in the platform-native contrast); retained, attributable decision history; downstream handoff after the decision; admin surface to configure forms/steps/rules; parallel or sequential approval structures.

**Present in dedicated products, not in the platform-native contrast [B/A]:** form builder as first-class object; SLA/escalation machinery; no-code workflow designer; dashboards/bottleneck reporting; lightweight no-license approver participation (Cflow secure-link; Power Automate email response partially covers this need).

**Only in single products [A — keep product-specific]:** Kissflow's "coding" step (GL/cost-centre assignment) as an explicit stage; Cflow's no-login approval; Nutrient's embedded document viewing/generation/signing suite; Power Automate's Dataverse 30-day rule.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Smallest structure without which the product stops being an Approval Workflow Platform:

```text
Submitted request (structured record of what is being asked)
  → routed to designated approver(s) in a defined path
    → each records a decision (approve / reject[/return])
      → request state advances accordingly
        → outcome + attributable decision history retained
```

Four properties:

1. **Request record** — a submitted, structured item awaiting an authorization decision (what, who, supporting data/attachments).
2. **Designated-approver routing** — the system, not the requester's inbox, determines who must decide, in what order (sequence and/or parallel), per configurable rules.
3. **Recorded decisions** — approvers explicitly record approve/reject(/return) outcomes, normally with comments; decisions are attributable (who, when, what).
4. **Tracked state + retained history** — the request visibly moves through states until an outcome; the decision history persists as the record of authorization.

Remove routing → it's a form builder / task tracker. Remove recorded decisions → it's collaboration/commenting. Remove tracked state + retained history → it's ad-hoc email approval, the very thing this Type replaces. Remove the request record → nothing to approve.

### L1 — Common Mature Structure

Present in essentially all mature dedicated products (not required for the definition):

- form builder with validation and conditional fields
- conditional routing rules on request data (amount, department, type, risk…)
- sequential and parallel approval structures
- return-for-revision loop back to the requester
- reminders, SLA timers, escalation to a higher queue/person
- notification channels (email, chat, mobile push)
- requester-visible status ("where is my request")
- dashboards: pending load, cycle times, bottlenecks, SLA compliance
- exportable audit log / audit-ready history
- admin console: workflows, forms, roles/permissions; role-based access to sensitive data
- templates for common approval types (expense, leave, CapEx, access, vendor…)
- downstream handoff to systems of record (ERP, HR, identity, document stores)
- mobile approval surface

### L2 — Variant / Optional Structure

Depends on segment, deployment, regulatory posture:

- **light-touch approver participation** — secure-link approval without a full login/license (Cflow), email-only response (Power Automate; onPhase "email approvals" in AP context), external/guest approvers (Power Automate Entra B2B)
- **policy/governance layer** — who-can-approve-what administration, segregation of duties (Kissflow frames this as "approval management" alongside the workflow layer)
- **AI decisioning** — auto-approve routine in-policy requests, escalate exceptions with rationale (Cflow, Nutrient; 2026-era)
- **document-centric depth** — embedded viewing, generation, markup, e-signature inside the approval loop (Nutrient/Integrify; onPhase)
- **accounting enrichment** — GL/cost-centre coding as an explicit step (Kissflow)
- deployment model — SaaS vs on-premises/hybrid; data residency (Kissflow regions; Cflow on-prem)
- domain template packs verticalized per department (finance/HR/IT/procurement/civic)

### L3 — Vendor-specific (stays out of the final document)

- Kissflow: "7 steps" pedagogy; named integration catalog; data-residency countries; "approval workflow vs approval management software" FAQ framing
- Cflow: Seyarc AI branding; 20 MB per-attachment / 30 GB storage figures; "approve without a full user license" pricing claim; 14-day trial specifics
- Nutrient: agentic approvals branding; PSPDFKit-derived document stack; BP/SOX customer framing
- onPhase/frevvo: brand transition history (frevvo → DocuPhase → onPhase); AP Automation/Payments siblings
- Power Automate: Dataverse 30-day rule; Approvals center naming; approval "types" catalog; auto-updating email badges

## Rejected Findings (considered, not canonical)

- **"No-code visual builder" as defining** — rejected: Power Automate implements approvals in a developer-oriented flow designer; approval chains long predate no-code. Builder style is implementation.
- **"Form-based request capture" as strictly defining** — rejected: approvals can attach to records created elsewhere (SharePoint item trigger in Power Automate). The request *record* is defining; the *form builder* is common.
- **"SLA escalation" as defining** — rejected: absent from the platform-native sample's basic loop; it is mature-product machinery (L1).
- **"AI decisioning" as defining** — rejected: 2026-era differentiator on 2 of 5 samples.
- **"Cloud SaaS" as defining** — rejected: on-premises options evidenced (Cflow, Nutrient, frevvo v11).
- **Marketing performance numbers** (e.g., "cut cycle time by up to 70%", "average approval takes 9–14 days") — rejected as unverifiable vendor claims; not carried into any document.

## Boundary Findings

- **vs Workflow Management Platform**: the approval platform is the approval-decision-centered specialization of the workflow engine. Both share designer + forms + routing. Test: **if you remove the authorization decision as the organizing purpose** (arbitrary task sequences, notifications, data sync take over), it becomes a Workflow Management Platform. Conversely, a workflow platform used for approvals is *doing* this Type's job. Market reality: most vendors sell approvals as a use case of a horizontal workflow platform; a distinct "approval workflow" category exists mainly in marketing and in approval-first products (Cflow, Integrify lineage). Gradient boundary — flagged for joint review.
- **vs Business Process Management Platform**: BPM adds explicit process modeling (notation-level), cross-system orchestration, process mining/discovery; approval platform centers on human decision chains over submitted requests. Remove decision-centricity and add model-driven orchestration → BPM.
- **vs Enterprise Request Management**: ERM's object is the service request fulfilled by a team (intake → assignment → fulfillment), where approval is one possible gate; approval platform's object is the decision itself. Remove the fulfillment/ownership machinery and keep only the gate → approval platform.
- **vs Form Builder**: form builders end at collected data; approval platforms continue into routing/decision/state. Remove routing+decision → form builder.
- **vs domain approval gates (Deal Desk, Purchase Order Management, IT Change Management, ITSM approval tasks)**: those Types own a domain object (deal, PO, change record, ticket) whose lifecycle *includes* an approval gate; the approval workflow platform owns a **generic request** whose only purpose is the authorization. The same engine pattern (chain + decision + history) recurs inside all of them.
- **vs ad-hoc email/chat approvals**: approvals may be *responded to* via email/chat/mobile, but if the system of record does not hold state + attributable history, it is not this Type — it is the manual baseline this Type exists to replace.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Platform-native approvals** (Power Automate Approvals; SharePoint-list approval flows; ERP purchase-approval steps; ITSM change approval tasks): fit — request + designated approvers + recorded decisions + tracked state/history all present, even without no-code designers or SLA machinery.
- **Pre-SaaS / on-premises approval software** (Integrify and frevvo lineages both ship on-premises versions): fit — deployment is L2.
- **Email- or paper-memo approval chains**: these are the manual baseline the Type replaces; they lack tracked state in a shared system, so they sit *outside* — confirming the boundary criterion rather than breaking it.
- **AI-era positioning** (auto-approval of routine requests): layered on top; the human decision chain remains the defining structure (even auto-approvals are recorded decisions made by rule, logged with rationale).

Conclusion: L0 abstracts cleanly across era, deployment, and platform-nativeness; no over-fitting to the current no-code SaaS pattern.

## Uncertainties

- **Delegation / out-of-office coverage** (reassigning pending approvals to a deputy): widely expected in this category but **not directly evidenced** on any fetched page in this sample; kept out of the final document's capability list or hedged. Treat as unverified.
- **Rejection-requires-comment rules**: comments on decisions are evidenced; whether any product *enforces* comments on rejection was not observed.
- **Exact state vocabularies** (e.g., "Pending", "In Review", "Returned"): products surely differ; no canonical state list is asserted.
- **Self-approval restrictions / segregation-of-duties enforcement**: Kissflow describes SoD as part of the policy layer conceptually; no per-product enforcement detail observed — hedged in final document.
- **frevvo/onPhase operational detail**: legacy docs unreachable (moved); evidence for this product is product-page level only — assertion strength reduced accordingly.
- Whether the market sustains **dedicated** approval-only products long-term vs absorbing them into horizontal workflow suites (acquisition pattern: Integrify→Nutrient, frevvo→onPhase). Recorded as a taxonomy observation.

## Final Synthesis

An Approval Workflow Platform is the application type whose defining core is the **authorization loop**: a submitted request record is routed by the system — per configured rules, in sequential and/or parallel structure — to designated approvers who record approve/reject(/return) decisions with comments; the request's state advances accordingly to an outcome, and the attributable decision history is retained as the authorization record, with the approved outcome typically handed off to the system of record where the real work happens. Everything else — form builders, SLAs, dashboards, mobile response, no-login approver links, AI decisioning, document suites, policy governance — is mature-market machinery layered on that loop, and disappears or varies without changing what the Type is.
