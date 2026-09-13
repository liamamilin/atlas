# Research Notes — Enterprise Service Management

Cross-references: research/employee-service-management.md (sibling, processed — flags this leaf: "probable requester-population gradient or alias"); research/enterprise-request-management.md (processed — flags this leaf: "ESM wraps the request flow in the full service-management discipline; ERM is the request-orchestration subset"); research/employee-portal.md (processed — "ESM is the management discipline behind the portal's service streams").

## Research Goal

Establish what an Enterprise Service Management (ESM) application is as an Application Type: its defining core, its standard mature structure, its variants, and — critically, given two prior flags — its boundary against Employee Service Management (sibling leaf), IT Service Management (§14), Enterprise Request Management (§10), and the surrounding portal/approval/case/ticketing Types.

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- ESM = the service-management discipline (defined service offerings, tracked requests, fulfillment teams, SLAs, knowledge, measurement) extended beyond the IT function to all of an organization's internal service departments — HR, facilities, finance, legal, and others.
- Nearest neighbors: ITSM (same discipline, IT-only provider), Employee Service Management (same discipline, employee-facing orientation), Enterprise Request Management (request-orchestration subset), Employee Service Portal (front-door surface), Help Desk / Ticketing (free-form intake), Customer Service Platform (external population), Approval Workflow Platform (approval-centered), Workflow Management / BPM (generic engines), Business Case Management Platform (investigative cases).
- Biggest risks: (1) ESM collapsing into ITSM — the market's ESM products are overwhelmingly ITSM platforms expanding outward; (2) ESM collapsing into Employee Service Management — both leaf names sit over one continuous market category.

## Research Questions

1. How do vendors themselves define ESM and its difference from ITSM?
2. What is the provider population — which departments, and how is a department realized as a service provider (space/project/instance/queue)?
3. What is the requester population — employees only, or any internal actor requesting from another department?
4. What objects exist in these systems (service desk instance, offering/catalog item, request/ticket/case, team, workflow, approval, SLA, knowledge article, journey)?
5. How do departments run their own service operation — autonomy vs enterprise governance, and how is sensitive departmental work segregated?
6. How do cross-department flows work (e.g., onboarding spanning HR, IT, facilities)?
7. Historical check: would older departmental help desks (HR help desk, facilities work-order desk) and classic ITSM fit the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier | Evidence tier reached |
|---|---|---|---|
| Jira Service Management | Atlassian | collaboration-platform lineage; per-team service spaces with department templates | Tier 1 (support docs: core doc + template library + full doc-tree navigation) |
| Freshservice | Freshworks | SaaS mid-market; ITSM→ESM expansion packaging ("Business Teams") | Tier 2 (dedicated ESM/business-teams page; KB structure via sibling corpus) |
| ServiceDesk Plus | ManageEngine (Zoho) | value tier; on-prem + cloud; dedicated ESM page with per-department instances | Tier 2 (dedicated ESM platform page incl. ESM-vs-ITSM FAQ) |
| Service Desk | SolarWinds | mid-market ITSM with ESM feature set | Tier 2 (product page; via sibling research corpus, fetched 2026-09-06) |

Rejected / unreachable samples:

- **ServiceNow** — the market's most prominent ESM vendor (enterprise incumbent). servicenow.com product page timed out (1 attempt this pass; prior sibling pass recorded timeouts ×2 and docs.servicenow.com as a client-rendered JS application). Abandoned per network rules; carried as a market anchor only, with no product-specific claims.
- **TOPdesk** (European ITSM/ESM vendor, attempted for regional diversity) — 404 ×2 on guessed documentation paths; abandoned.
- **InvGate** — HTTP 490 on product page; abandoned.
- **TeamDynamix** — recorded as 403 in the enterprise-request-management pass; not retried.

## Sources

Fetched 2026-09-06 (this pass):

- Atlassian Support — "What is Jira Service Management?" — https://support.atlassian.com/jira-service-management-cloud/docs/what-is-jira-service-management/ (Tier 1)
- Atlassian Support — "About Jira Service Management space templates" — https://support.atlassian.com/jira-service-management-cloud/docs/what-are-the-project-templates/ (Tier 1)
- Atlassian Support — JSM doc-tree navigation (request types, queues, approvals, SLAs, KB, portals, chat, virtual agent, surveys) (Tier 1 structure)
- Freshworks — "Freshservice for Business Teams" (ESM solution page; URL /solutions/enterprise-service-management/ redirects here) — https://www.freshworks.com/freshservice/solutions/enterprise-service-management/ (Tier 2)
- ManageEngine — "AI-powered enterprise service management (ESM) platform" (ServiceDesk Plus ESM page) — https://www.manageengine.com/products/service-desk/enterprise-service-management.html (Tier 2)

Via sibling research corpus (fetched 2026-09-06, recorded in research/employee-service-management.md):

- Freshservice Support KB root (section structure incl. "Enterprise Service Management" section) — https://support.freshservice.com/en/support/solutions (Tier 1 structure)
- Freshworks — "Freshservice for HR Teams" — https://www.freshworks.com/freshservice/business-teams/hr-service-delivery/ (Tier 2)
- ManageEngine — ServiceDesk Plus product page — https://www.manageengine.com/products/service-desk/ (Tier 2)
- SolarWinds — Service Desk product page — https://www.solarwinds.com/service-desk (Tier 2)

Unreachable / degraded:

- servicenow.com (timeout; prior pass: timeouts ×2, docs JS-only shell)
- topdesk.com (404 ×2 on attempted paths)
- invgate.com (HTTP 490)

## Product Observations

### Jira Service Management (Atlassian) — Layer A (official support docs)

From "What is Jira Service Management?" and the doc-tree (Tier 1):

- Team-per-area structure: "Each team can work on a project that services requests from a certain area – like IT, HR, legal, or finance." Each team owns a service space with its own portal, request types, queues, and workflows; work can route into other teams' projects.
- Purpose framing: "receive, track, manage, and resolve requests from your team's customers. Customers can send requests by email, via help centers, and an embeddable widget." (Note: JSM's generic vocabulary is "customers" — internal employees are a deployment of that vocabulary, not a separate structure.)
- Work tracking: "requests are tracked as work items in a queue. Work item progress is set up by a workflow that can include steps like In progress or Needs approval."
- Machinery per space: request types with forms and portal groups; queues; approvals (steps, defined approvers, approval by email/chat, requester-chosen approvers); SLAs (goals, calendars, conditions, JQL-based); knowledge base (internal vs external, article suggestions in request forms, multiple knowledge sources); CSAT surveys plus organization-wide surveys; virtual service agent across portal/email/widget/Slack/Teams; automation flows; reports/dashboards; workforce-management-assisted routing.
- ITSM practices (incident, problem, change, on-call/alerts) ship out of the box for ITSM spaces "and can be enabled on other projects" — ITSM practices are a department-specific layer, not the generic structure.

From "About Jira Service Management space templates" (Tier 1) — the multi-department span, directly evidenced:

- Template library: IT service management; General service management; Customer service management; HR service management ("manage staff and their requests... payroll, onboarding, change requests, general inquiries"); Facilities service management ("maintenance, moving, and event planning"); Legal service management ("contracts through the review cycle to resolution"); Finance service management ("field queries, and manage budget, spend..."); Marketing service management; Analytics service management; Sales service management; Design service management; Blank space.
- Each template "include[s] pre-configured request types, workflows and other features relevant to their type."
- Employee-as-requester phrasing: general template "makes it easy for employees to submit requests"; several templates say "help employees find answers"/"manage employee requests".

From the HR case-management doc (sibling corpus, Tier 1): cases as a distinct work category for "complex, sensitive, long-running" HR work (allegations, findings, outcomes), invisible to help seekers.

### Freshservice (Freshworks) — Layer A/B (product page this pass; KB structure via corpus)

From the ESM / Business Teams page (Tier 2):

- Positioning: "Enterprise service management for any business team… no ITSM implementation needed."
- Four stated pillars: Unified team platform ("Centralize requests, approvals, and tasks with built-in SLAs, routing, and visibility"); Structured employee requests ("Replace unstructured emails and shared inboxes with service catalogs"); Productive employee journeys ("Automate cross-functional processes with reusable, prebuilt workflows"); Data-driven service excellence ("Spot trends and bottlenecks by department").
- Department surfaces: HR (employee requests, onboarding, approvals), Finance (expense approvals, procurement requests), Facilities (centralized requests, maintenance workflows), Legal (contract reviews, document requests, compliance approvals).
- Integrations: Workday, Microsoft Teams, Slack, marketplace.
- Customer quote (Databricks): "Expanding from ITSM to ESM with Freshservice was a strategic move that transformed support, offering a unified hub for all employee needs." — direct evidence of the ITSM→ESM expansion motion.
- From HR page (corpus): case management with SOP controls (SLAs + agent checklists), service catalog, journeys (onboarding/offboarding/transitions), document & e-signature inside HR workflows, HRIS/payroll integrations, HR analytics, AI HR agents.
- From KB structure (corpus): "Enterprise Service Management — setup ESM with employee onboarding, access controls, and more"; product self-description "manage internal requests from your employees".

### ServiceDesk Plus (ManageEngine) — Layer A/B (dedicated ESM page, incl. FAQ)

- Positioning: "Make ITSM work beyond IT with enterprise service management. Break down silos to deliver efficient, collaborative services across HR, facilities, legal, and other departments."
- Vendor's own definition (FAQ): "ESM extends ITSM principles, like process standardization, automation, and self-service, across departments beyond IT. It helps HR, facilities, finance, legal, and other teams deliver structured, trackable, and scalable services through a centralized portal."
- Vendor's own ITSM boundary (FAQ): "While ITSM focuses on IT operations, ESM applies the same proven processes and practices across other business departments."
- Unified ESM portal: "instantly provides quick employee access to HR, facilities, finance, legal, and other department service desks relevant to their role. Submit requests, access information, and track ticket progress."
- Department-as-provider implementation: "Launch ready-to-use service desk instances for any department"; prebuilt templates and built-in catalogs "from default instances such as IT, HR, and facilities"; per-department autonomy — "Departments can run their own service desks while staying connected to organization-wide ITSM controls, automation, and reporting"; "Delegate admin privileges and enforce role-based access, ensuring enterprise-grade security."
- Department-specific extension modules: IT (integrated CMDB/asset management), HR (tailored onboarding and offboarding workflows), facilities (dedicated space management module, room bookings).
- Cross-department orchestration: native iPaaS builds "context-aware enterprise workflows, from adding new joiners in [HR systems] to creating accounts in [identity systems] and securing signatures" — evidence of multi-department fulfillment chains.
- AI: per-instance AI (conversational support, predictive insights, workflow/resolution assistance).
- Licensing model: per service desk instance, based on technicians and assets; existing IT licenses reusable.
- Prior-corpus product-page evidence: multi-instance model with data/process segregation; edition ladder with formal service catalog at Enterprise tier; Forrester Wave "ESM Platforms, Q4 2025" citation (market category exists as analyst construct).

### Service Desk (SolarWinds) — Layer A/B (product page, via sibling corpus)

- ESM feature block: "Enterprise Service Management — improve the management, efficiency, interactions and experience across every department. Taking service management beyond IT. Unified service provider: empowering departments to publish offered services and structure service delivery. Streamline processes: provide tools needed to be successful providers. Security & Privacy: segregated service desks ensure access control to sensitive data."
- Feature taxonomy: Core Service Management; Asset & IT Operations (asset mgmt, CMDB); Self-Service & Experience (Employee Self-Service Portal, Service Catalog, Knowledge Base, Live Chat, Service Level Management, Enterprise Service Management, Sandbox).
- AI: virtual agent, GenAI agent assist, auto-categorization, sentiment.

### ServiceNow — not researched (unreachable)

No product-specific claims. Market-structure role: enterprise incumbent whose ESM presence spans department-specific service-delivery offerings; its absence means the enterprise-suite pole is evidenced only indirectly (competitor positioning, analyst-category citations).

## Cross-product Comparison

| Structure | JSM | Freshservice | ServiceDesk Plus | SolarWinds | Evidence layer |
|---|---|---|---|---|---|
| Vendor framing of ESM | team-per-area service spaces ("IT, HR, legal, or finance") | "ESM for any business team… no ITSM implementation needed" | "extends ITSM principles… across departments beyond IT" (FAQ) | "Taking service management beyond IT… across every department" | A×4 → B |
| Provider population | teams per area via templates (IT/HR/legal/finance/facilities/marketing/analytics/sales/design) | HR, finance, facilities, legal (+ marketing per KB) | HR, facilities, finance, legal + "any department" | "every department" | A×4 → B |
| Requester population | employees (template phrasing; "customers" is the generic term) | "all employee needs"; "internal requests from your employees" | "employee access to… department service desks relevant to their role" | Employee Self-Service Portal | A×4 → B |
| Department-as-provider implementation | one service space per team; queues per space | department workspaces on one platform | separate service desk instances per department, data/process autonomous | segregated service desks | A×4 → B (mechanism differs) |
| Unified request front door | help center/portals; email; widget; chat | portal replacing shared inboxes | unified ESM portal | employee self-service portal | A×4 → B |
| Defined offerings per department | request types + templates per space | service catalogs | built-in catalogs per default instance; formal catalog module (Enterprise tier) | service catalog; "departments publish offered services" | A×4 → B |
| Tracked request lifecycle | work items in queues, workflows with statuses | tickets with visual lifecycle | tickets, visual lifecycle builder | workflows, SLM | A×4 → B |
| Approvals as fulfillment gates | approval steps, email/chat approval | centralized approvals | auto-approvals; delegation | approvals (IT-side observed) | A×3 + B |
| Service-level machinery | SLA goals/calendars/conditions/JQL | built-in SLAs | SLA management + escalations (corpus) | Service Level Management | A×4 → B |
| Knowledge / deflection | KB w/ article suggestions in forms | knowledge base | knowledge base | knowledge base | A×4 → B |
| Cross-department orchestration | journeys; route work into other teams' projects | cross-functional employee journeys | iPaaS workflows spanning HR→identity→signature chains | not directly observed | A×3 + B |
| Department-specific extensions | ITSM practices per space; HR case category | HR docs/e-sign, finance approvals, facilities maintenance | IT CMDB/assets, HR onboarding/offboarding, facilities space mgmt | IT assets/CMDB | A×4 → B |
| Autonomy + governance | per-space roles/permissions; site-level admin | access controls (ESM KB section) | delegated admins, role-based access, org-wide ITSM controls | segregated desks + access control | A×4 → B |
| Sensitive-work segregation | issue security on cases; help-seeker invisibility | case management with SOP controls | data/process segregation per instance | segregated desks for sensitive data | A×4 → B (mechanism differs) |
| Measurement per department | reports/dashboards per space | trends/bottlenecks by department; HR analytics | reporting + live dashboards | reporting, dashboards | A×4 → B |
| AI assistance | virtual service agent, AI answers | AI HR agents | per-instance AI (conversational, predictive, GenAI) | virtual agent, GenAI assist | A×4 → B |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable as enterprise service management:

```text
Internal service departments operating as managed service providers
  └── Department-owned defined service offerings
      └── Requests from the organization's people as tracked work records
          └── Fulfillment by a responsible department team through a managed lifecycle
              └── Shared service-management discipline across departments
```

Five properties:

1. **Internal service departments as managed service providers** — the provider is a department operated as a service unit (own offerings, queue, workflow, service levels), not the IT function specifically. The discipline is department-agnostic; IT is historically the first and most fully-featured provider. Remove this (provider = IT only) → IT service management; remove the managed-provider framing → scattered departmental point tools.
2. **Department-owned defined service offerings** — each provider department declares what can be requested and captures the details fulfillment needs. Remove this → unstructured email/shared inboxes, which is exactly the "before ESM" state vendors describe.
3. **Requests from the organization's people as tracked work records** — durable, stateful, attributable records. Remove this → email.
4. **Fulfillment by a responsible department team through a managed lifecycle** — routing to an owning team, statuses, tasks, approvals, resolution. Remove this → an unowned ticket pile.
5. **Shared service-management discipline across departments** — one common machinery (service levels, knowledge, measurement, governance) applied to every provider, rather than each department improvising its own tooling. Remove this → disconnected departmental help desks without a common operating model.

Historical check (per §24 reasoning): a 2000s-era HR help desk module satisfies properties 2–4 but usually not 5 (no shared cross-department discipline) and only partially 1 (a desk, not a managed provider in a common model) — it sits at the boundary, closer to the degenerate single-department case. Classic ITSM satisfies 2–5 for one provider (IT). The modern market's defining orientation — the enterprise-wide span of the discipline across all internal departments — is the practical differentiator and belongs at the center of the L1, while the L0 keeps the provider-side abstraction (departments as managed service units under one discipline). No region-specific or era-specific structure entered L0.

### L1 — Common Mature Structure

Present across the researched sample; expected in the market but not definitional:

- **Multi-department span as center of gravity** — HR, IT, facilities, finance, legal, and more operating as providers in one system (or one governed estate); the market's defining orientation and the practical differentiator from IT-only deployments. Single-department deployments are the degenerate case.
- **Unified employee-facing portal** — one front door across department service desks, with role-relevant access to the desks relevant to the employee.
- **Per-department queues/workspaces** — each provider team works its own queue; implementation ranges from spaces/projects on one platform to fully separate instances.
- **Service-level machinery** — response/resolution commitments per offering with calendars, conditions, escalations.
- **Approvals as fulfillment gates** — manager/department/budget-owner consent embedded in request workflows.
- **Knowledge base with deflection** — articles surfaced before/during request submission.
- **Satisfaction measurement** — per-request CSAT and broader surveys.
- **Cross-department orchestration** — journeys/workflows spanning providers for recurring processes (onboarding a new hire across HR, IT, facilities; contract review across legal and finance).
- **Virtual agent / AI assistance** — conversational deflection, triage/routing assistance, reply drafting, per-desk AI.
- **Per-department reporting/dashboards** — volumes, SLA attainment, bottlenecks by department.
- **Department data segregation** — access control so sensitive departmental work (especially HR) is not broadly visible; the requesting employee never sees sensitive case machinery.
- **Department-specific extension modules** — IT assets/CMDB/change; HR document generation/e-signature and onboarding/offboarding; facilities space management; legal contract review cycles.

### L2 — Variant / Optional Structure

- **Packaging posture**: ITSM-anchored expansion (ITSM platform adds departments — the dominant motion), department-first ("no ITSM implementation needed"), multi-instance segregation (one service desk instance per department).
- **Department realization**: shared platform with department routing/workspaces vs separate spaces vs fully separate instances with data/process segregation.
- **Offering machinery**: formal service catalog module vs request types/templates (tier-dependent in at least one product).
- **Channel breadth**: portal, email, chat/collaboration apps, embeddable widget, live chat, API.
- **AI posture**: rule-based virtual agent vs GenAI answers vs per-instance AI engines.
- **Deployment & licensing**: cloud vs on-premises; per-technician/per-instance licensing (not asserted in final doc).
- **ITSM practice enablement**: incident/problem/change/on-call enabled on non-IT spaces or confined to IT.

### L3 — Vendor-specific (Research Notes only)

- Atlassian: space-template library list; "work categories" (request vs case); Confluence-as-KB coupling; JQL-defined SLAs; virtual-agent usage limits; workforce-management routing.
- Freshworks: "Business Teams"/FSBT packaging; four-pillar framing; SOP checklists inside HR case management; document/e-signature inside HR workflows.
- ManageEngine: multi-instance ESM model; "60 seconds" instance-launch claim (marketing precision — excluded from final doc); choice of AI engines (Zia LLM/ChatGPT/Azure OpenAI); per-instance licensing by technicians + assets; Zoho-stack iPaaS examples; space management module name; edition ladder (formal catalog only at Enterprise tier).
- SolarWinds: "unified service provider" phrasing; Sandbox; per-technician pricing (corpus).
- ServiceNow: no claims recorded (unreachable).
- Analyst construct: "ESM Platforms" category (Forrester Wave Q4 2025, cited on ManageEngine page) — market-structure evidence, not a product feature.

## Vendor-specific Findings

- ManageEngine's per-department **service desk instances** (data/process-autonomous desks under org-wide governance) is a product-specific realization of department-as-provider; the generalized finding (departments run their own service operation under enterprise governance) is cross-product.
- Atlassian's **space-template library** (IT through design) is a product-specific expression of department templates; the generalized finding (pre-configured department starting points) is common but the specific library is vendor content.
- Freshservice's **"no ITSM implementation needed"** department-first packaging is a product-specific positioning; JSM/ManageEngine/SolarWinds all anchor ESM in ITSM expansion.
- All vendor marketing statistics (instance-launch time, deflection %, consolidation counts) are unverified claims, recorded here only.

## Boundary Findings

1. **vs IT Service Management (§14, unprocessed)** — vendor-stated boundary (ManageEngine FAQ: "ITSM focuses on IT operations, ESM applies the same proven processes and practices across other business departments"). Scope gradient, not a structure wall: all four sampled ESM products are ITSM platforms expanded "beyond IT". ITSM centers the IT function's services and ITIL practices (incident/problem/change/CMDB); ESM centers the enterprise-wide span with IT as one provider among several, and IT-specific practices as an enablement layer. Test: strip the non-IT departments → ITSM remains; strip IT-specific practices → ESM remains. Flag for joint review when ITSM is processed.
2. **vs Employee Service Management (§10 sibling, processed)** — the two leaf names sit over **one continuous market category**: the same products (JSM, Freshservice, ServiceDesk Plus, SolarWinds) populate both, and the analyst category "ESM Platforms" is employee-facing in its requester population. Orientation gradient: Employee Service Management defines by the **requester population** (employee as internal service customer); Enterprise Service Management defines by the **provider span** (all internal departments as managed service units under one discipline, historically generalized out of ITSM). Probable near-alias; the boundary statement must be scope/orientation-based, not structure-based. **Flag for joint review** — resolution options: keep both with orientation-based boundary statements (current), or merge with one as the canonical name. This pass keeps both leaves documented without contradicting the sibling.
3. **vs Enterprise Request Management (§10, processed)** — confirmed from this pass's evidence: ERM centers the request-fulfillment orchestration flow (catalog → request → routing → tracked lifecycle); ESM wraps that flow in the full service-management discipline — the department as an **ongoing managed service provider** with SLA framework, knowledge operation, measurement, and governance, not just per-request orchestration. Test: strip the service discipline → ERM remains; strip request orchestration → ESM remains. Scope gradient.
4. **vs Employee Service Portal (§09, processed)** — the portal is the front-door surface; ESM is the fulfillment machinery and management discipline behind it. In the sample, portals ship as components of ESM products. Consistent with the employee-portal and employee-service-management passes.
5. **vs HR Case Management (§09, processed)** — HR case management centers HR's sensitive case types with structured findings/outcomes; ESM provides the general machinery into which such case handling fits as one department's extension (JSM evidence: case work category inside the service space).
6. **vs Help Desk / Ticketing System (§07/§14, unprocessed)** — free-form ticket intake vs catalog-bound departmental service fulfillment under a managed provider model; internal population vs (often) external or mixed. JSM shows the machinery is shared (general service management template ≈ internal help desk); the ESM discriminator is the multi-department managed-provider structure.
7. **vs Customer Service Platform (§07, unprocessed)** — audience identity boundary: employees under employment-based identity vs external customers under commercial identity. JSM ships both an HR/internal template family and a customer-service template on the same machinery — the Type boundary is the deployment frame, not the feature set.
8. **vs Approval Workflow Platform (§10, processed)** — approvals are one gate inside ESM fulfillment (L1), never the organizing purpose. Confirms the approval pass's boundary.
9. **vs Workflow Management Platform / BPM (§10, unprocessed)** — generic engines route tasks between people/systems but lack the department-as-provider service model and the requester-facing defined offerings. ManageEngine's iPaaS cross-department workflows show the gradient to watch: orchestration features thickening inside ESM products.
10. **vs Business Case Management Platform (§10, unprocessed)** — investigative/adjudicative case work (a case that gets decided) vs service fulfillment (a request that gets delivered). Different object semantics despite shared ticket/case vocabulary.
11. **vs Employee Experience Platform (§09, processed)** — service is one domain inside EX bundles; ESM operates the service domain standalone with full fulfillment depth. Consistent with the EX pass's flag.

## Taxonomy Observations

- The **"ESM Platforms" analyst category exists** (Forrester Wave, Q4 2025) and is populated by ITSM platforms expanded outward — the market's own category does not separate "employee service management" from "enterprise service management". The directory's two §10 sibling leaves therefore need an orientation-based boundary or a merge decision; recorded for joint review.
- The ESM label is **umbrella marketing** in the current market: it names a packaging motion ("take ITSM beyond IT") more than a distinct structure. The structure (offerings, requests, fulfillment teams, SLAs, knowledge, measurement) is continuous with ITSM and ERM; the differentiator is provider span.
- The dedicated HR-service-delivery pure-play segment remains under-sampled (Espressive absorbed into Resolve Systems per prior pass; Applaud cookie-walled; Neocase/PeopleDoc/Dovetail unreachable in prior passes) — recorded as a market observation with low evidence strength.

## Uncertainties

- **ServiceNow absent** — the category's most prominent enterprise vendor was unreachable (timeout this pass; timeouts ×2 + JS-only docs in the prior pass). The enterprise-suite pole is characterized only indirectly. All ServiceNow-specific framing is absent from both documents.
- Operational precision is Tier-1 only for JSM; Freshservice and ServiceDesk Plus details rest on Tier-2 pages (plus Freshservice Tier-1 KB structure via corpus). No precise numbers, defaults, time windows, or state lists are asserted in the final document.
- CSAT/feedback for ServiceDesk Plus and SolarWinds not directly confirmed on fetched pages this pass; carried at moderate wording from corpus structure.
- Whether "journeys" (cross-department orchestration) exist in SolarWinds was not confirmed; carried at moderate wording.
- Requester-population nuance (employee-only vs any internal actor requesting across departments) could not be resolved definitively: template phrasing and portal language are employee-centric; cross-team routing exists structurally. Treated as an orientation finding, not a population claim.
- Pricing/licensing not asserted (per-instance licensing observed for one product only; kept in Research Notes).

## Final Synthesis

Enterprise Service Management is best understood as **the organization's system for running all of its internal services as managed operations**: internal departments — HR, facilities, finance, legal, IT, and beyond — operate as service providers that own defined offerings; the organization's people request those services through a common front door; each request becomes a tracked record routed to the responsible department team; fulfillment proceeds through managed lifecycles (tasks, approvals, service-level commitments) to resolution; and a shared service-management discipline — knowledge, measurement, governance — applies uniformly across providers, with sensitive departmental work segregated from general view.

The defining core is small and provider-side: departments as managed service providers + department-owned offerings + tracked requests + responsible-team fulfillment + shared discipline. The enterprise-wide span (IT as one provider among several) is the market's defining orientation and the practical differentiator from ITSM — but single-department deployments remain the degenerate case of the same machinery. The market expresses the Type through one dominant packaging (ITSM platforms expanding "beyond IT") plus a department-first packaging, with per-department autonomy under enterprise governance as the structural behavior. The strongest boundary signals: provider span across departments (vs ITSM's IT-only provider); full service-management discipline (vs ERM's orchestration subset); fulfillment machinery (vs the portal's front door); internal population (vs customer support); and — recorded for joint review — the sibling leaf Employee Service Management, which sits over the same market category with an employee-facing orientation rather than a provider-span orientation.
