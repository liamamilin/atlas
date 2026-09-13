# Research Notes — Employee Service Management

Cross-references: research/employee-portal.md §Boundary Findings (flags this leaf for joint review: "ESM is the management discipline (service design, fulfillment, measurement) behind those service streams"); research/employee-experience-platform.md §Boundary Findings #4 ("service portals center employee-initiated requests/cases"; service is one domain inside EX platforms).

## Research Goal

Establish what an Employee Service Management application is as an Application Type: its defining core, its standard mature structure, its variants, and its boundaries against ITSM, Enterprise Service Management, Employee Service Portal, HR Case Management, Enterprise Request Management, and customer-support Types.

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- ESM = the service-management discipline (service catalog, request/case lifecycle, fulfillment teams, SLAs, knowledge, measurement) applied to internal services consumed by employees — HR, IT, facilities, finance, legal.
- Nearest neighbors: ITSM (same discipline, IT-only provider), Enterprise Service Management (same discipline, enterprise-wide internal scope), Employee Service Portal (the front-door surface), HR Case Management (HR-specific sensitive cases), Enterprise Request Management (request-fulfillment orchestration), Customer Service Platform (external customers).
- Biggest risk: ESM collapsing into ITSM (the market's ESM products are mostly ITSM platforms expanding outward) or into Employee Service Portal (the visible surface).

## Research Questions

1. What objects exist in these systems? (service offering / request type, request, case, team, workflow, task, approval, knowledge article, SLA, feedback, journey)
2. How does an employee request flow end-to-end?
3. What does the "employee service" framing add or change relative to ITSM — multi-department span? employee identity? department-as-provider?
4. How is sensitive HR work handled relative to ordinary requests?
5. What role do self-service, knowledge, and virtual agents play — definitional or mature-common?
6. How do onboarding/offboarding "journeys" fit?
7. Historical check: would older single-department HR help desks and classic internal help desks fit the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier | Evidence tier reached |
|---|---|---|---|
| Jira Service Management | Atlassian | dev-collaboration ITSM lineage; per-team service projects; template-based departments | Tier 1 (support docs, 2 pages + full doc-tree nav) |
| Freshservice | Freshworks | SaaS mid-market ITSM→ESM; "Business Teams" department-first packaging | Tier 2 product pages + Tier 1 KB structure |
| ServiceDesk Plus | ManageEngine (Zoho) | value tier; on-prem + cloud; multi-instance ESM model | Tier 2 product page (rich, incl. editions + FAQ) |
| Service Desk | SolarWinds | mid-market ITSM with ESM feature set | Tier 2 product page |

Rejected / unreachable samples:

- **ServiceNow** — the market's most prominent ESM/HR-service-delivery vendor. servicenow.com product pages timed out twice; docs.servicenow.com is a client-rendered JS application (no extractable content). Dropped per source-access rules; no claims in this research depend on it.
- **Espressive** — dedicated "employee service management" pure-play; espressive.com now redirects to resolve.io (vendor absorbed into Resolve Systems' automation platform). Recorded as a market-structure observation, not a sample.
- **Applaud** (HR service delivery) — cookie-wall stub, no content. Abandoned after one failure.
- **Neocase / Dovetail / PeopleDoc** (dedicated HR service delivery suites) — not attempted after the Applaud failure; the dedicated-HRSD philosophy is therefore under-sampled and this is recorded as a limitation.

## Sources

Fetched 2026-09-06:

- Atlassian Support — "What is Jira Service Management?" — https://support.atlassian.com/jira-service-management-cloud/docs/what-is-jira-service-management/ (Tier 1)
- Atlassian Support — "What is case management in Jira Service Management?" — https://support.atlassian.com/jira-service-management-cloud/docs/what-is-case-management-in-jira-service-management/ (Tier 1)
- Freshworks — "Freshservice for Business Teams" — https://www.freshworks.com/freshservice/business-teams/ (Tier 2)
- Freshworks — "Freshservice for HR Teams" — https://www.freshworks.com/freshservice/business-teams/hr-service-delivery/ (Tier 2)
- Freshservice Support KB root (section structure) — https://support.freshservice.com/en/support/solutions (Tier 1 structure)
- ManageEngine — ServiceDesk Plus product page — https://www.manageengine.com/products/service-desk/ (Tier 2)
- SolarWinds — Service Desk product page — https://www.solarwinds.com/service-desk (Tier 2)

Unreachable / degraded:

- servicenow.com (timeout ×2), docs.servicenow.com (JS-only shell)
- espressive.com (redirects to resolve.io)
- applaud.com (cookie wall)
- freshworks.com/freshservice/ root (timeout ×1; sibling paths fetched fine)

## Product Observations

### Jira Service Management (Atlassian) — Layer A (official support docs)

From "What is Jira Service Management?":

- Purpose framing: "receive, track, manage, and resolve requests from your team's customers. Customers can send requests by email, via help centers, and an embeddable widget."
- Team-per-area structure: "Each team can work on a project that services requests from a certain area – like IT, HR, legal, or finance. Templates are different types of projects that are tailored to suit certain teams." Each team has its own portal, owns its service space, and can route work into other teams' projects.
- Work tracking: "requests are tracked as work items in a queue. Work item progress is set up by a workflow that can include steps like In progress or Needs approval."
- Deflection: Confluence-based knowledge base surfaced on the portal "so your customers can help themselves before reaching out."
- ITSM-specific practices (incident, problem, change, on-call/alerts, post-incident reviews) are out-of-the-box for ITSM projects "and can be enabled on other projects" — i.e., ITSM practices are a department-specific layer, not the generic structure.

From the doc-tree navigation (Tier 1 structure):

- Request types: forms per request type, portal groups, request type groups, restrictions on request types, workflow per request type, field layout per work type.
- Channels: portal, email (multiple addresses, DMARC handling), embeddable widget, Slack/Microsoft Teams chat, live chat, API.
- Customers & organizations: customer permission settings, SSO for customers, organizations grouping (email-domain based).
- Approvals: approval steps in workflows, defined approvers, approval by email/chat, customers choosing approvers.
- SLAs: SLA goals, calendars, conditions, JQL-based definitions, priority grouping.
- CSAT surveys; organization-wide surveys ("Collect feedback from your organization with surveys").
- Knowledge base: internal vs external KB, article suggestions in request forms, article performance, multiple knowledge sources (Confluence, Google Drive, SharePoint).
- Virtual service agent: intents, conversation flows, AI answers, deployment across portal/email/widget/Slack/Teams; usage limits.
- Journeys: "Build journeys in Jira Service Management" — journey types with triggers, work items, conditions, dependencies, in-progress tracking, active/inactive states. "Create employee onboarding journeys with Request Resolver."
- HR service management section: "Manage HR cases in Jira Service Management", "Log findings and outcomes on a case".

From "What is case management in Jira Service Management?" (Tier 1):

- "Case management gives HR teams a structured way to handle complex, sensitive, long-running work — like an investigation or a performance concern — separately from standard service requests."
- Cases are a distinct work category from service requests; they carry structured allegations, findings, and outcome decisions on the same record.
- Cases vs requests table: cases for "complex, sensitive, long-running HR work"; requests for "transactional HR work that follows a known path, like a leave request or a benefits question."
- Visibility rule: "Help seekers don't see the case component. Cases are only visible to people in your service space who have access to the work item" (issue security).
- Ready-made HR request types: "Report workplace concern or incident", "Performance management support", "Request health or wellbeing support".
- Roles: HR agents open cases and log findings/outcomes; HR operations leads oversee usage; space admins enable the category and map request types.

### Freshservice (Freshworks) — Layer A/B (product pages + KB structure)

From "Freshservice for Business Teams" (Tier 2):

- Positioning: "Enterprise service management for any business team… no ITSM implementation needed."
- Four stated pillars: Unified team platform ("centralize requests, approvals, and tasks with built-in SLAs, routing, and visibility"); Structured employee requests ("replace unstructured emails and shared inboxes with service catalogs"); Productive employee journeys ("automate cross-functional processes with reusable, prebuilt workflows"); Data-driven service excellence ("spot trends and bottlenecks by department").
- Department pages: HR service delivery, Finance, Facilities, Legal.
- Integrations: Workday, Microsoft Teams, Slack, marketplace apps.
- Customer quote (Databricks): "Expanding from ITSM to ESM… a unified hub for all employee needs" — evidence of the ITSM→ESM expansion motion in the market.

From "Freshservice for HR Teams" (Tier 2):

- "Manage employee requests with structured case management, clear SLAs, and built-in guidance like agent checklists."
- Feature set: Case Management with SOP controls (SLAs + checklists); Service Catalog ("structured HR services through an intuitive self-service portal"); Journeys ("automate onboarding, offboarding, and transitions with cross-team workflows"); Document & E-signature Management ("generate, e-sign, and store documents within HR workflows"); Integrations (HRIS, payroll, collaboration tools); HR Analytics ("track volumes, SLAs, and service trends with purpose-built HR dashboards").
- AI HR Agents: "answer questions and complete routine requests across systems, reducing ticket volume."

From the support KB root (Tier 1 structure):

- KB sections: "Support Guide: IT and Employee Service Management"; "Freshservice for Business Teams — enables non-IT departments such as HR, Facilities, Finance, Legal, and Marketing to deliver seamless employee experiences on a unified, AI-first platform"; "Enterprise Service Management — setup ESM with employee onboarding, access controls, and more."
- Freshservice self-description: "Streamline your IT service and manage internal requests from your employees."

### ServiceDesk Plus (ManageEngine) — Layer A/B (product page, incl. editions and FAQ)

- Positioning: "AI-driven unified service management platform for the digital enterprise… combines IT service management, IT asset management, and CMDB with enterprise service management capabilities for departments including HR, facilities, and finance."
- ESM model: "Multi-instance model for enterprise service management — service desk instances with clear data and process segregation for multiple departments."
- FAQ: "Can non-IT help desk teams use ServiceDesk Plus as well? Yes, non-IT teams like facilities, legal, and HR can leverage the enterprise service management capabilities… to handle user queries and requests."
- Editions ladder: Standard ("service desk for IT and non-IT teams": incident management, customizable ticket templates, visual ticket lifecycle builder, no-code ticket handling automation, self-service portal, knowledge base, SLA management and escalations, reporting and live dashboards); Professional (adds ITAM); Enterprise (adds service catalog, problem management, change enablement/release, IT project management, CMDB). → The formal service catalog module sits at the Enterprise tier; the Standard tier already carries portal, KB, SLAs, templates, automation.
- AI: predictive intelligence (triage/routing/assignment/sentiment), virtual support agent ("on-demand handling of end user requests through text and voice conversations"), GenAI reply assist.
- Analyst framing: "A Strong Performer in the Forrester Wave™ ESM Platforms, Q4 2025" — the market category "ESM Platforms" exists as an analyst construct.
- Deployment: on-premises and cloud.

### Service Desk (SolarWinds) — Layer A/B (product page)

- ESM feature block: "Enterprise Service Management — improve the management, efficiency, interactions and experience across every department. Taking service management beyond IT. Unified service provider: empowering departments to publish offered services and structure service delivery. Streamline processes: provide tools needed to be successful providers. Security & Privacy: segregated service desks ensure access control to sensitive data."
- Feature taxonomy: Core Service Management (incident/problem/change/release, automation, mobile, reporting); Asset & IT Operations (asset mgmt, CMDB, discovery); Self-Service & Experience (Employee Self-Service Portal, Service Catalog, Knowledge Base, Live Chat, Service Level Management, Enterprise Service Management, Sandbox).
- AI: generative sidekick for agents, virtual agent, smart suggestions, sentiment analysis, auto-categorization.
- Pricing model surfaced: per-technician pricing with unlimited users (marketing page; not asserted in final doc).

## Cross-product Comparison

| Structure | JSM | Freshservice | ServiceDesk Plus | SolarWinds | Evidence layer |
|---|---|---|---|---|---|
| Employee/requester as identified internal customer | yes (customers/organizations, SSO) | yes (internal requests from employees; HRIS sync) | yes (self-service portal users) | yes (employee self-service portal) | A×4 → B |
| Defined service offerings for employees | request types + portal groups | service catalog | service catalog (Enterprise tier); ticket templates at Standard | service catalog; "departments publish offered services" | A×4 → B (formal catalog module is tier-dependent in one product) |
| Employee-initiated request as tracked work item | work items in queues | tickets/cases | tickets | tickets | A×4 → B |
| Routing to responsible team | team-per-area projects, queues | routing, department transfer ("support agents are able to easily transfer tickets within departments" — customer quote) | assignment/routing, predictive intelligence | assignment; segregated service desks | A×3 + B |
| Managed lifecycle to resolution | workflows with statuses (In progress, Needs approval) | visual lifecycle, SLAs, checklists | visual ticket lifecycle builder, SLA escalations | SLM, workflows | A×4 → B |
| Approvals as fulfillment gate | approval steps, approvers, email/chat approval | approvals centralized | auto-approvals | approvals in change mgmt (IT-side) | A×3 + B |
| Knowledge-based self-service | Confluence KB, article suggestions | knowledge base | knowledge base (all editions) | knowledge base | A×4 → B |
| Virtual agent / AI assistance | virtual service agent, AI answers | AI HR agents, Zia-style agents | predictive intelligence, virtual support agent, GenAI | virtual agent, GenAI sidekick | A×4 → B |
| CSAT / feedback | CSAT surveys, org surveys | surveys (Freshsurvey lineage; HR dashboards) | happiness ratings (implied by CIO quote on surveys) — not directly confirmed | SLM (SLA-based; CSAT not directly confirmed) | A×2 + B (weaker for two products) |
| Multi-department span (HR/IT/facilities/finance/legal) | "IT, HR, legal, or finance" teams | HR/Finance/Facilities/Legal/Marketing | "HR, facilities, and finance" + FAQ (facilities, legal, HR) | "across every department" | A×4 → B |
| Department data segregation | issue security on cases; per-space access | access controls (ESM KB section) | multi-instance with data/process segregation | segregated service desks | A×4 → B (mechanism differs per product) |
| Lifecycle journeys (onboarding/offboarding) | journeys + Request Resolver onboarding journeys | journeys (onboarding/offboarding/transitions) | employee onboarding (ESM KB section title) | not directly observed | A×3 + B |
| Sensitive-case handling (allegations/findings/outcomes) | case management work category, structured | case management with SOP controls | not directly observed | "segregated service desks… sensitive data" (segregation only) | A×2 (product-specific depth varies) |
| Department-specific extensions | ITSM practices enabled per project | HR doc/e-sign, finance approvals, facilities maintenance | ITAM/CMDB/change (IT-side) | asset mgmt/CMDB (IT-side) | A×4 → B |
| Measurement/reporting | reports, dashboards | HR analytics dashboards, benchmark report | reporting and live dashboards | reporting, dashboards | A×4 → B |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable as employee service management:

```text
Employee as identified internal service customer
  └── Organization-defined internal service offerings (what can be asked for)
      └── Employee-initiated request/case as tracked unit of work
          └── Routing to the responsible internal service team (department as provider)
              └── Managed fulfillment lifecycle to resolution
                  under service-level and knowledge discipline
```

Five properties:

1. **Employee as identified internal service customer** — the population served is the organization's own workforce, authenticated through employment. Remove this → external customer support.
2. **Defined internal service offerings** — the organization declares what services employees can request and under what form. Remove this → an unstructured suggestion box / shared inbox.
3. **Request/case as tracked unit of work** — each demand is a durable record with state. Remove this → email.
4. **Routing to a responsible internal service team** — a department (or fulfillment group) owns fulfillment. Remove this → unowned ticket pile.
5. **Managed fulfillment lifecycle to resolution under service-level and knowledge discipline** — statuses, service-level commitments, knowledge-based self-service, and measurement govern the flow. Remove this → a bare ticket list, not "service management".

Historical check (§24 reasoning): a 2000s-era HR help desk module (employee cases handled by an HR team with statuses and knowledge) satisfies all five without any modern machinery (no portal polish, no AI, no formal catalog UI, no multi-department span). A classic internal IT help desk also satisfies all five — which is honest: the single-department internal service desk is the degenerate case of this Type, and the modern market's center of gravity (multi-department span) is a maturity/scope finding, not a definitional one. The L0 therefore does not require multi-department span, portals, virtual agents, or journeys.

### L1 — Common Mature Structure

Present across the researched sample; expected in the market but not definitional:

- **Multi-department span** — HR, IT, facilities, finance, legal (and more) operating as service providers in one system; the modern market's center of gravity and the practical differentiator from IT-only deployments.
- **Self-service portal / help center** — the employee-facing surface for browsing offerings, submitting requests, and tracking status.
- **Knowledge base with deflection** — articles surfaced before/during request submission.
- **Approvals as fulfillment gates** — manager/department approval steps inside request workflows.
- **SLA machinery** — goals, calendars, conditions, escalations.
- **CSAT / feedback collection** — per-request satisfaction plus broader surveys.
- **Virtual agent / AI assistance** — conversational deflection, triage/routing assistance, reply drafting.
- **Lifecycle journeys** — multi-step, cross-team orchestration for onboarding/offboarding/transitions.
- **Department data segregation** — access control so sensitive departmental work (esp. HR) is not broadly visible.
- **Reporting/dashboards per department** — volumes, SLA attainment, bottlenecks.

### L2 — Variant / Optional Structure

- **Packaging posture**: IT-anchored expansion (ITSM platform adds departments) vs department-first (start with HR, no ITSM implementation) vs multi-instance segregation (separate service desk instances per department).
- **Formal catalog module vs request-type/template machinery** as the implementation of "defined offerings" (tier-dependent in at least one product).
- **Sensitive-case machinery**: structured allegations/findings/outcomes as a distinct work category (observed in two products with different depth; single-product mechanics stay product-specific).
- **Department-specific extensions**: HR document generation/e-signature; finance approval workflows; facilities maintenance; IT asset/CMDB/change practices.
- **Deployment**: cloud vs on-premises; per-technician vs other commercial models (not asserted).
- **Channel breadth**: portal, email, chat/collaboration apps, embeddable widget, live chat, API.
- **AI posture**: rule-based virtual agent vs GenAI answers vs agentic execution.

### L3 — Vendor-specific (Research Notes only)

- Atlassian: "work categories" (request vs case), Request Resolver execution modes, Confluence-as-KB coupling, JQL-defined SLAs, Opsgenie-lineage operations (alerts/on-call) as an IT-side add-on, virtual-agent usage limits.
- Freshworks: "Business Teams" packaging name, SOP checklists inside case management, document/e-signature inside HR workflows, Freshsurvey lineage, benchmark report.
- ManageEngine: multi-instance ESM model as the segregation mechanism, edition ladder (catalog only at Enterprise), Zia virtual support agent with voice, on-prem + own-datacenter privacy posture.
- SolarWinds: "unified service provider" phrasing, per-technician pricing with unlimited users, Sandbox feature, THWACK community.
- ServiceNow: not researched (unreachable); no vendor-specific claims recorded.
- Resolve/Espressive: acquisition consolidation; RITA virtual agent deflecting IT+HR requests (customer-story tier only).

## Vendor-specific Findings

- ManageEngine's multi-instance model (one service desk instance per department with data/process segregation) is a product-specific segregation mechanism; the generalized finding (departmental data segregation) is cross-product.
- Atlassian's case-management work category (allegations/findings/outcomes structure, help-seeker invisibility) is product-specific in its mechanics; the generalized finding (sensitive HR work tracked separately from transactional requests with restricted visibility) is supported by two products.
- Freshservice's document/e-signature inside HR workflows is product-specific as a bundled feature; document handling as an HR-service extension is a plausible common need but only directly observed once.
- SolarWinds' "departments publish offered services" phrasing is a vendor articulation of the catalog concept; the concept is cross-product.
- All vendor marketing statistics (deflection %, savings, happiness %) are unverified claims, recorded here only.

## Boundary Findings

1. **vs IT Service Management (§14, unprocessed)** — same service-management discipline; the provider population differs. ITSM centers the IT function's services and ITIL practices (incident/problem/change/CMDB); ESM centers employee-facing services across departments, where IT is one department among several. Test: strip the non-IT departments → ITSM remains; strip IT-specific practices (CMDB, change windows) → generic employee service management remains. Evidence: all four sampled products are ITSM platforms that add ESM as "beyond IT" (SolarWinds), "business teams" (Freshservice), "departments including HR, facilities, and finance" (ManageEngine), "IT, HR, legal, or finance" teams (JSM). The two Types are structurally continuous — a scope gradient, not a wall. Flag for joint review when ITSM is processed.
2. **vs Enterprise Service Management (§10 sibling, unprocessed)** — the directory keeps both leaves. In the reachable market, "ESM" products serve employees as the requester population; department-to-department internal services are a further scope extension of the same machinery. Probable requester-population gradient (employee-facing vs enterprise-wide internal) or alias; flag for joint review when Enterprise Service Management is processed.
3. **vs Employee Service Portal (§09, unprocessed)** — the portal is the front-door surface (browse offerings, submit, track); ESM is the fulfillment machinery and management discipline behind it. In the sample, the portal is a component of ESM products (JSM help center, Freshservice portal, SolarWinds employee self-service portal). Test: strip fulfillment machinery → a portal remains; strip the portal → ESM still works (email/chat/agent-created requests). Consistent with the employee-portal pass's flag. Joint review when Employee Service Portal is processed.
4. **vs HR Case Management (§09, unprocessed)** — HR case management centers HR-specific sensitive case types (investigations, grievances, employee relations) with structured findings/outcomes and restricted visibility; ESM centers the general service-delivery machinery across departments. JSM's evidence shows HR case handling embedded as a work category inside the service space — a department-specific extension of ESM machinery. Test: strip HR case semantics → generic ESM remains; strip general request machinery → HR case management remains. Joint review when HR Case Management is processed.
5. **vs Enterprise Request Management (§10, unprocessed)** — ERM centers request intake/approval/fulfillment orchestration across the enterprise; ESM wraps that request flow in the full service-management discipline (offerings, SLAs, knowledge, measurement, department-as-provider). Probable overlap; flag for joint review.
6. **vs Customer Service Platform / Help Desk / Ticketing System (§07)** — audience identity is the boundary: employees (employment-based identity, internal services) vs external customers (customer accounts, commercial services). The machinery is analogous; the population, service catalogs, and compliance posture differ. Test: swap the population to external customers → customer support Type.
7. **vs Employee Experience Platform (§09, processed)** — service is one domain inside EX platforms (delivered via native agents or partner integrations per that research); ESM is the service domain operated standalone with full fulfillment depth. Test: remove service → EX remains; remove listening/comms/content → ESM remains. Consistent with that pass's flag.
8. **vs Employee Portal (§10, processed)** — the portal aggregates entry points (content, self-service, links); ESM operates the service streams those entry points surface. Requests raised in a portal are handed to ESM machinery (per the employee-portal pass: "requests handed off to ITSM/HRIS"). Complementary, not overlapping.
9. **vs Digital Employee Experience Management (§14)** — DEX monitors endpoint/application telemetry; ESM fulfills employee requests. Same word "experience", different objects and owners. No overlap beyond naming.
10. **vs Approval Workflow Platform (§10)** — approvals are one gate inside ESM fulfillment (L1); an approval platform centers the approval itself as the product. Test: remove request fulfillment → approval platform remains.

## Taxonomy Observations

- The market category "ESM Platforms" exists as an analyst construct (Forrester Wave ESM Platforms Q4 2025, cited by ManageEngine), and its products are overwhelmingly ITSM platforms expanded outward. The directory's §10 "Employee Service Management" and §14 "ITSM" therefore sit on a continuous gradient; both remain definable, but the boundary statement must be scope-based, not structure-based.
- The dedicated HR-service-delivery pure-play segment (Neocase/Dovetail/PeopleDoc/Espressive/Applaud lineage) was not reachable in this environment; Espressive's absorption into Resolve Systems suggests consolidation of that segment into automation platforms. Recorded as a market observation with low evidence strength.

## Uncertainties

- ServiceNow — the most prominent vendor in this category — was unreachable; all ServiceNow-specific framing is absent, and the enterprise-suite pole of the market is evidenced only indirectly (via competitor positioning and analyst mentions on fetched pages).
- Operational depth (exact SLA semantics, exact approval routing options, exact journey trigger types) is Tier-1 only for JSM; for the other three products it rests on Tier-2 product pages. No precise numbers, defaults, or time windows are asserted anywhere.
- CSAT/feedback could not be directly confirmed for ServiceDesk Plus and SolarWinds; treated as common (L1) with moderate wording.
- Whether "journeys" are universal could not be confirmed for SolarWinds; treated as common with moderate wording.
- Dedicated HRSD pure-plays under-sampled (see Taxonomy Observations).
- Pricing/packaging not researched; nothing asserted.

## Final Synthesis

Employee Service Management is best understood as **the organization's system for running internal services for its employees**: departments act as service providers that publish defined offerings; employees request help through self-service and assisted channels; each request becomes a tracked record routed to the responsible team; fulfillment proceeds through a managed lifecycle (tasks, approvals, checklists, status) to resolution; and service levels, knowledge-based self-service, and measurement govern the whole flow.

The defining core is small: employee-as-customer + defined offerings + tracked request + responsible team + managed lifecycle under service-level/knowledge discipline. The multi-department span (HR, IT, facilities, finance, legal) is the modern market's center of gravity and the practical differentiator from IT-only service desks, but it is a scope finding, not a definitional one — older single-department help desks still satisfy the core. The market expresses the Type through one dominant packaging (ITSM platforms expanding "beyond IT") plus a department-first packaging, with segregation of sensitive departmental work (especially HR cases) as a structural behavior. The strongest boundary signals: population = own employees (not external customers); provider = internal departments (not the IT function alone); structure = fulfillment machinery (not the portal front door, not HR records, not EX domain consolidation).
