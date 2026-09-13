# Research Notes — HR Case Management

Research date: 2026-09-07
Slug: hr-case-management
Directory leaf: HR Case Management (§09 HR, Workforce & Talent)

Cross-references (this pass is the designated joint pass for three prior flags):
- research/employee-relations-case-management.md §Boundary Findings — "HR Case Management (§09 sibling) needs a joint pass; market blurs the naming (HR Acuity brands its ER product 'HR Case Management')".
- research/employee-service-management.md §Boundary Findings #4 — "HR case handling = department-specific extension of ESM machinery (JSM case work category); test: strip general request machinery → HR case management remains; strip HR case semantics → generic ESM remains. Joint review when HR Case Management is processed."
- research/enterprise-request-management.md §Boundary Findings #8 — "HR cases are sensitive case types with structured findings/outcomes; ERM requests are general service fulfillment."
- research/employee-service-portal.md §Boundary Findings #5 — "sensitive people matters handled agent-side with restricted visibility; the portal is at most their intake surface."
- research/employee-record-system.md — "cases/requests are the working objects there; the employee record is context."
- research/employee-offboarding-platform.md — "case management is service-request-shaped; offboarding is lifecycle-shaped."

## Research Goal

Establish what HR Case Management is as an Application Type: its defining core, standard mature structure, variants, and — because this is the joint pass — the resolved boundaries against Employee Relations Case Management (§09 sibling), Employee Service Management (§10), Employee Service Portal (§09), Enterprise Request Management (§10), Employee Record System/HRIS (§09), and the customer-support Types (§07).

## Initial Boundary (working hypothesis before research)

- The market uses "HR case management" for at least two overlapping things: (a) the HR service-delivery case desk (employee questions/requests worked as cases by HR agents — the PeopleDoc/Dovetail/ServiceNow-HRSD lineage), and (b) sensitive people-matter case handling (the ER lineage, marketed under the same name by HR Acuity).
- The directory keeps both leaves (Employee Relations Case Management and HR Case Management), so this pass must draw the seam rather than merge them.
- Nearest neighbors: ER Case Management (sensitive matters), Employee Service Management (general machinery), Employee Service Portal (front door), Enterprise Request Management (request orchestration), HRIS/Employee Record System (records), Help Desk/Ticketing (same mechanics, different population), Customer Service Platform (external customers).
- Unknowns: does the Type's core include sensitive-matter handling or only transactional requests? Is the employee-facing portal definitional? Is SLA/knowledge discipline definitional or mature-common? How do HCM integrations bind cases to employee records?

## Research Questions

1. What is the central object, and what defines it (type, parties, employee binding, context)?
2. How does work enter the system (portal, email, chat, phone, agent-created, HR-initiated)?
3. What does the handling lifecycle look like, and what closes a case?
4. How is confidentiality/access control structured, given that case content is personal employee data?
5. What role do knowledge, SLAs, templates, documents, and approvals play — definitional or mature-common?
6. How do cases bind to employee/HCM data, and what does that binding enable?
7. How is sensitive people-matter work (ER) handled relative to transactional requests — same object family or separate machinery?
8. How is the capability packaged (dedicated pure-play vs HR-suite module vs ESM-platform module vs ER-specialist)?
9. Historical check: would a 2000s-era HR shared-services case system (email-to-case, agent-side only, no portal/AI) still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / pole | Evidence tier reached |
|---|---|---|---|
| HR Help Desk | Oracle | HR-suite-native: case desk unified with HCM ("service request and case management solution") | Tier 2 (official product page, rich) |
| Dovetail | Dovetail Software | Dedicated HR case management pure-play ("Built for HR, not IT"); portal + knowledge + reporting around the case desk | Tier 2 (official home + product page, feature-level) |
| Jira Service Management | Atlassian | ESM-embedded: HR service delivery template inside a service-management platform; requests vs cases as two work categories | Tier 1 (official support docs) |
| Freshservice | Freshworks | ESM-embedded, mid-market: "Freshservice for HR Teams" with case management + SOP controls | Tier 2 (official product page) |
| HR Acuity | HR Acuity | ER-specialist pole / naming-blur boundary anchor (markets ER case management as "HR Case Management") | Tier 2 (fetched in the ER pass, cross-referenced) |

Rejected / unreachable samples (source-access limitation recorded):

- **ServiceNow HR Service Delivery** — the enterprise flagship. servicenow.com product page timed out ×2 in this run (and ×2 in each of two prior passes); docs.servicenow.com is a client-rendered JS shell. Abandoned per source-access rules; no claims depend on it. The enterprise-suite pole is evidenced indirectly (Dovetail's positioning against "incident management systems that IT would use"; the Sapient Insights HR Service Delivery survey category cited on Dovetail's page).
- **Zoho People** — HR-suite SMB pole. Two URL guesses 404'd (zoho.com/people/hr-help-desk.html, hr-helpdesk.html). Abandoned.
- **Neocase** — dedicated HRSD pure-play. neocase.com timed out ×2 (root + /products/). Abandoned.
- **UKG (PeopleDoc heritage)** — ukg.com/solutions/hr-service-delivery 404. Abandoned after one failure.

Consequence: the dedicated-pure-play pole is represented by one product (Dovetail) and the SMB HR-suite pole is unsampled; assertions are calibrated accordingly.

## Sources

Fetched 2026-09-07:

- Oracle — "Oracle HR Help Desk" product page — https://www.oracle.com/human-capital-management/hr-help-desk/ (Tier 2)
- Dovetail Software — home page ("HR Case Management and Employee Portal Software") — https://www.dovetailsoftware.com/ (Tier 2)
- Dovetail Software — "HR Case Management" product page — https://www.dovetailsoftware.com/hr-case-management (Tier 2, feature-level)
- Atlassian Support — "What is case management in Jira Service Management?" — https://support.atlassian.com/jira-service-management-cloud/docs/what-is-case-management-in-jira-service-management/ (Tier 1; full doc-tree nav captured in same fetch)
- Freshworks — "Freshservice for HR Teams" — https://www.freshworks.com/freshservice/business-teams/hr-service-delivery/ (Tier 2)

Cross-referenced from prior passes (not re-fetched):

- HR Acuity product pages + FAQs (ER pass, 2026-09-06) — https://www.hracuity.com/platform/hr-case-management/ et al. (Tier 2)
- Freshservice "Business Teams" page + support KB structure (ESM pass, 2026-09-06) (Tier 2 / Tier 1 structure)

Unreachable / degraded (this run):

- servicenow.com (timeout ×2), docs.servicenow.com (JS-only shell, prior passes)
- zoho.com/people/* (404 ×2)
- neocase.com (timeout ×2)
- ukg.com (404 ×1)

## Product Observations

### Oracle HR Help Desk — Layer A (official product page)

- Definition on the page: "a scalable and unified **service request and case management** solution that makes it easy for employees to find answers without the risk of sensitive data getting into the wrong hands." — the dual framing (requests + cases) in one product sentence.
- Multichannel inquiries: "Submit inquiries via multiple channels—digital assistant, SMS, email, and social platforms."
- Assignment/routing: "Route complex questions to the right HR person"; "Tailored workflows for automatic routing — configure your service request management system to handle complex HR rules required to manage contractual terms and conditions."
- **Service request linking**: "Connect multiple service requests to a single case to expedite the resolution of a systemic issue and apply consistent actions across all associated requests." — requests and cases are distinct object levels; cases can aggregate requests.
- **Comprehensive case management**: "Manage complex employee relations cases with multiple process steps, long-term tracking, correspondence, documentation, and best practice action plans." — ER cases are explicitly inside the HR help desk's case-management pillar.
- Contextual collaboration: "Enable collaboration within each case via conversations and document sharing among stakeholders."
- Employee surface: "a single place to find immediate answers, submit service requests for additional support, and track the progress of requests"; knowledgebase "to resolve routine inquiries"; personalized guidance "for sensitive employee relations issues using Oracle Journeys."
- Analytics: "360-degree view of each employee's profile and history"; "Trend analysis — which types of service requests, cases, and inquiries are trending"; embedded BI (Oracle Transactional Business Intelligence).
- Privacy: "keeps highly sensitive employee data private and protected"; "a help desk that's fully managed by HR and uses the same single security model used across all Oracle Cloud products."
- Native HCM integration: "unified with HCM, removing the need for third-party integrations"; "real-time data... unified across all HCM processes."

### Dovetail — Layer A (official home + product pages)

- Positioning: "HR Case Management Software for Enterprise HR Teams"; "Easy to use. Fast to launch. **Built for HR, not IT.**" — the anti-ITSM pole.
- Definition on the product page: "Often referred to as an HR Helpdesk, HR Case Management helps HR teams and HR Service Centers efficiently manage employee inquiries and requests. It improves HR Service Delivery through workflow automation, enhanced case tracking and reporting, and personalized dashboards."
- Suite structure: Employee Portal (employee-facing) + HR Case Management (HR-facing) + Knowledge Management + Reporting & Analytics + System Setup + Workday Integration. Knowledge Management "underpins both HR Case Management and the Employee Portal... the same problem never needs to be solved twice."
- HR Home Console: "full visibility on their workload. Case data is segregated based on the HR profile and/or Case lifecycle stage, ensuring employee data security is fully maintained. HR team members and team leaders can monitor Service Level Agreements, Priorities and Urgency of employee questions and take immediate action."
- Case Creation: "When an employee contacts HR with a question, the HR team member will either update an existing case or create a new case. The case creation screen will show the HR team member if an existing case exists automatically. The HR team member will also have instant knowledge results, and full visibility of the employee's HCM core data."
- Knowledge Search: "Automatic knowledge searches are performed whenever an HR team member works a case... fast access to existing cases, knowledge articles, attachments, and XpertHR content."
- Case Tracking & Escalation: "monitor, track, and resolve cases efficiently throughout the case lifecycle. Cases can be escalated manually or through automated workflows, while employees and HR teams stay informed through automatically generated emails and notifications."
- Emails & Notes: "fully integrated email client... Emails and attachments are automatically added to cases, while phone call interactions are logged directly against the case, eliminating lost notes and disconnected conversations."
- Templates: "preconfigured emails and notes... faster, more consistent responses to employees across the organization."
- Audit Timeline: "Every case interaction is logged, including who made the change, when it occurred, and the previous and updated values. This gives HR teams a clear chronological record to support investigations, dispute resolution, and process improvement."
- SLA: "workflow-driven SLAs automatically prioritize cases on the HR Home Console based on your KPIs and service metrics."
- Workflow Automation: "From automated case notifications to complex parallel workflows."
- HCM Integration: "Access key employee HR data on a single screen while working cases... Data visibility is controlled based on the HR team member's profile and the employee being viewed." (vendor stat: customers used an average of five HCM screens before — marketing figure, notes only)
- More features: GDPR & Privacy ("employee purge, data redaction, legal hold and data retention policies"); Broadcasts ("mass communicate... Track employee acknowledgments"); Assets ("record tangible and intangible assets against employees"); Attachments (auto virus scanning); 30+ languages; 50+ out-of-box reports.
- Employee Relations module (sibling): "Digitally document and manage employee relations issues, including workplace conflicts, grievances, disciplinary actions, discrimination and harassment cases and affirmative action cases." — ER handling exists as a distinct module/console beside the case desk.
- Email Automation: "Email-to-Case", automated replies, email parsing.
- HR Copilot GenAI (Teams/Slack), pre-built intents.
- Customer quotes (why the Type exists — Layer A, attributable):
  - Boston University HR Director: "we needed a Service Center with Ulrich model approach and this drove the requirement for an HR case management system, as it was recognized that our current spreadsheet/shared inbox solution would not be fit for purpose."
  - FOS HR Project Manager: "my fear was that we were going to be buying something that would have been seen as just a ticketing system... The others were building on incident management systems that IT would use. Dovetail was definitely more aligned with what HR wanted."
  - Morgan Stanley HR Shared Services head: "With a Shared Inbox we ran into issues when people were out... an HR case management system was 'a natural evolution' from a shared inbox solution."
  - Tower Health VP Total Rewards: reasons for buying — "control over HR data, metrics on our activity, a tool that we could use to track cases, and a knowledge base to achieve consistent service as people would start getting the same answers to questions and not getting a different answer every time they contacted a different HR representative."
  - Swire Coca-Cola Leave & Accommodation Partner: "customizable to allow for the famous HR 'it depends' situations... helped us achieve our Employee Relations objectives."

### Jira Service Management — Layer A (official support docs, Tier 1)

- HR template positioning (doc-tree nav): "Run HR service delivery in Jira Service Management, from everyday people requests to sensitive, long-running cases."
- "Case management gives HR teams a structured way to handle complex, sensitive, long-running work — like an investigation or a performance concern — separately from standard service requests. Cases live in your service space alongside the requests your team already handles, so HR agents can record allegations, findings, and outcomes in one place."
- "Record allegations and findings: Capture what was raised and what your investigation concluded in a structured way."
- Ready-made HR request types: "Report workplace concern or incident", "Performance management support", "Request health or wellbeing support" — "each providing the forms shaped for that kind of HR work."
- Roles: "HR agents open cases, log allegations and findings, and record outcomes"; HR operations leads oversee usage; space admins enable the category and map request types.
- Mechanism: "Case management adds a new work category to your service space... The work category gives cases their own behaviour for findings and outcomes, while still using the rest of Jira Service Management — queues, automation, and the portal — in the same way as service requests."
- Requests (from the requests doc): "Requests are how work items are represented on help centers to help seekers... automatically triaged into queues."
- Security rule: "Case Management uses your existing Jira Service Management security model... Cases are only visible to people in your service space who have access to the work item... Your employees (help seekers) don't see the case component at all. To restrict who can see and work on specific cases, use your service space's issue security scheme."
- Surrounding machinery (doc-tree): request types/forms, portal groups, queues, workflows with statuses, approvals (approvers, approval by email/chat), SLAs (goals, calendars, conditions), CSAT surveys, knowledge base with article suggestions, virtual service agent, automation rules, reports/dashboards, email channels (multiple addresses, DMARC), chat in Slack/Teams, embeddable widget, customer permission settings, SSO, organizations (email-domain grouping), journeys (onboarding), language support, canned responses, workforce management (schedules/capacity/routing), data classification levels for work items.

### Freshservice (Freshworks) — Layer A/B (official product page)

- "Manage employee requests with structured case management, clear SLAs, and built-in guidance like agent checklists to ensure consistent, compliant resolution."
- "Move beyond shared inboxes and manual tracking." — the same "before" state as Dovetail's customers.
- Feature set: Case Management with SOP controls (SLAs + checklists); Service Catalog ("structured HR services through an intuitive self-service portal"); Journeys ("automate onboarding, offboarding, and transitions with cross-team workflows"); Document & E-signature Management ("generate, e-sign, and store documents within HR workflows"); Integrations (HRIS, payroll, collaboration tools); HR Analytics ("track volumes, SLAs, and service trends with purpose-built HR dashboards").
- AI HR Agents: "answer questions and complete routine requests across systems, reducing ticket volume."

### HR Acuity — Layer A (ER pass, cross-referenced; boundary anchor)

- Brands its ER platform "Employee Relations & HR Case Management Software": "the industry-leading platform for HR case management and investigations from intake through aftercare."
- Explicit contrast with ticketing (FAQ): "Ticketing tools were built to route requests and close them out. They were not built for the nuance and complexity of workplace investigations. A help desk queue has no privilege flag, no guided investigation workflow, no defensible audit trail and no way to separate access by role when a matter is sensitive."
- Methodology: Plan → Investigate → Determine; privilege marking; role-based permissions; retaliation check-ins; ThroughCare aftercare; anonymous intake converting to structured cases; benchmarking analytics.
- Interpretation for this pass: HR Acuity occupies the sensitive-matter pole of the "HR case management" name — the naming blur the ER pass flagged. Its own FAQ draws the same seam this pass must draw: help-desk-style case handling vs investigation-grade matter handling.

## Cross-product Comparison

| Structure | Oracle HR Help Desk | Dovetail | Jira Service Management | Freshservice | HR Acuity (anchor) | Evidence |
|---|---|---|---|---|---|---|
| Workforce member as identified requester/party | yes (HCM-unified 360 view) | yes (HCM data view in case) | yes (customers = employees, SSO) | yes (HRIS sync) | yes (HRIS sync) | A×5 → B |
| Case as tracked, typed unit of HR work | service requests + cases (SRs linkable to a case) | cases (email-to-case, phone logged, templates) | requests + cases as two work categories | cases/tickets with SOP controls | cases (reports auto-convert) | A×5 → B |
| Case typing from an HR vocabulary | request/case types; trending by type | case types/templates | ready-made HR request types (workplace concern, performance, wellbeing) | catalog services | allegation categories | A×5 → B |
| Assignment to HR handler/queue | "route to the right HR person" | HR console, assignment, escalation | queues, agents | routing, checklists | assign to investigators | A×5 → B |
| Managed lifecycle to recorded resolution | "multiple process steps, long-term tracking" | case lifecycle, escalation, audit timeline | workflow statuses; findings/outcomes on the record | SLAs, checklists, resolution | plan→investigate→determine, outcomes | A×5 → B |
| Confidentiality / restricted visibility | "sensitive data... wrong hands"; single security model | data segregation by HR profile; GDPR/privacy; legal hold | help seekers don't see the case component; issue security | access controls | role-based permissions, privilege | A×5 → B |
| Retained, attributable history | correspondence + documentation on case | audit timeline (who/when/prev-updated values) | comments + history | (implied by SOP/SLA machinery) | complete audit trail | A×4 + B |
| Knowledge base (deflection + agent-side search) | knowledgebase for routine inquiries | knowledge mgmt underpins cases + portal; auto-search while working | KB with article suggestions | service catalog + portal | (not the focus) | A×4 + B |
| Employee self-service portal | "single place to find answers, submit, track" | employee portal (case tracking, ask HR, feedback) | help center/portal | self-service portal | (intake via reporting instead) | A×4 + B |
| SLA machinery | (not explicit on page) | SLA prioritization on console | SLAs (goals, calendars, conditions) | "clear SLAs" | (not the focus) | A×3 + B |
| Correspondence capture on the case | contextual collaboration (conversations + docs) | emails/attachments auto-added; calls logged | comments | (implied) | documentation | A×3 + B |
| Templates / consistent answers | (not explicit) | templates for emails/notes | canned responses | agent checklists | guided workflows | A×3 + B |
| Documents / e-signature | documentation on cases | attachments | (not explicit) | document & e-signature mgmt | documentation | A×2 + B (depth varies) |
| Case linking / systemic issues | multiple SRs → one case | (not explicit) | (not explicit) | (not explicit) | case linking across incidents | A×2 (product-specific mechanics) |
| Reporting / analytics | trend analysis, embedded BI | 50+ OOB reports, dashboards | reports/dashboards | HR analytics dashboards | trends + benchmarking | A×5 → B |
| AI assistance | digital assistant, multichannel | HR Copilot GenAI | virtual service agent | AI HR agents | olivER companion | A×5 → B |
| Lifecycle journeys (onboarding/offboarding) | Oracle Journeys | (not explicit) | journeys | journeys | (not the focus) | A×3 + B |
| HCM/HRIS integration | native HCM unification | Workday/Dayforce connectors, HCM data view | (marketplace) | HRIS/payroll integrations | Workday partnership | A×5 → B |
| Sensitive people-matter handling | ER cases inside case mgmt ("multiple process steps, long-term tracking") | ER module (conflicts, grievances, discipline, discrimination/harassment) | case work category (investigations, performance concerns) with findings/outcomes | (not explicit) | the core (investigation-grade) | A×4 + B |
| Employee feedback / CSAT | (not explicit) | portal feedback & ratings | CSAT surveys | (implied by dashboards) | (not the focus) | A×2 + B (weaker) |
| Anti-ticketing / anti-ITSM positioning | "fully managed by HR" | "Built for HR, not IT"; customer: "not just a ticketing system" | (neutral — it IS a service-mgmt platform) | "beyond shared inboxes" | "help desk queue has no privilege flag" | A×3 + B |

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

```text
Workforce member raises HR work (question / request / report) — or HR initiates it
  └── Case as the tracked, typed unit of HR work
      (bound to the employee and their organizational context)
      └── Assigned to an HR handler / queue (HR as the providing function)
          └── Managed lifecycle to a recorded resolution
              under confidentiality discipline
              (restricted visibility + retained, attributable history)
```

Three compact properties; remove any one and the Type stops being recognizable:

1. **HR as the providing function for workforce-raised work.** The requester population is the organization's own employees/managers; the handler population is HR. Remove this → generic employee service management (any department) or customer support (external customers).
2. **Case as the tracked, typed record bound to the employee.** Each piece of HR work becomes a durable record with a type from the HR case vocabulary, bound to the requesting/subject employee and their organizational context. Remove this → a shared inbox or spreadsheet tracker (the documented "before" state at multiple customers).
3. **Managed lifecycle to a recorded resolution under confidentiality discipline.** The case moves through assignment → work → resolution with statuses, and ends in a recorded outcome; access is restricted because the content is personal employment data, and the handling history is retained and attributable. Remove the lifecycle → a correspondence log; remove the confidentiality discipline → a generic ticket board, which no HR organization can actually run on personal data.

Historical check (§24 reasoning): a 2000s-era HR shared-services case system (employee emails HR; HR logs a typed case, works it, closes it with a recorded resolution; access restricted to HR staff) satisfies all three properties with no portal, no SLA module, no knowledge base, no AI, no journeys. A union-grievance tracker fits too (a case-type variant). A generic IT ticketing tool with an "HR" queue also satisfies the invariants — honestly: the Type is the case-management pattern applied to HR work, and the market's dedicated products are distinguished by HR-specific structure (HCM data binding, HR knowledge, ER handling, document machinery), which belongs to L1/L2, not the definition. The L0 therefore does not require portals, SLAs, knowledge bases, catalogs, journeys, or AI.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B); expected in mature products but not definitional:

- **Employee self-service portal / help center** — browse knowledge, submit requests, track own case status (absent in agent-side-only older deployments).
- **Knowledge base with deflection + agent-side knowledge search** — articles surfaced to employees before contact and to agents while working a case ("the same problem never needs to be solved twice").
- **Multi-channel intake** — portal forms, email-to-case, chat/collaboration apps, phone calls logged as cases, digital assistants; agent-created cases for walk-ups.
- **SLA machinery** — goals, calendars, workflow-driven prioritization, escalations.
- **Routing/assignment rules** — by case type, workload, region, HR specialization.
- **Correspondence capture** — emails, notes, attachments, call logs automatically attached to the case record.
- **Templates / canned responses / agent checklists** — consistent answers across HR reps (an explicit buying reason in customer evidence).
- **Approvals as fulfillment gates** — manager/HR approval steps inside case workflows.
- **Document generation / e-signature / attachments** — HR documents produced and stored within case workflows (depth varies by product).
- **Case linking** — related requests/cases connected (systemic-issue aggregation at one product; repeat-incident linking at another).
- **Reporting & dashboards** — volumes, SLA attainment, trends by case type; HR service analytics.
- **CSAT / employee feedback** — per-case ratings and surveys (weaker evidence; two products direct).
- **AI assistance** — virtual agents for deflection, reply drafting, case summaries (era-common).
- **Lifecycle journeys** — onboarding/offboarding/transitions orchestrated as multi-step flows adjacent to the case desk.
- **HCM/HRIS integration** — employee data pulled into the case view; population data synced for routing/attribution; the case desk never owns the employment record.
- **Sensitive-case handling with restricted visibility** — long-running people-matters tracked as cases invisible to help seekers, with structured findings/outcomes (present in four of five products at varying depth; the investigation-grade regime belongs to ER case management).

### L2 — Variant / Optional Structure

- **Packaging posture**: dedicated HRSD pure-play vs HR-suite-native module (HCM-unified) vs ESM/ITSM-platform module vs ER-specialist platform marketed under the same name.
- **Case-type breadth**: transactional service requests only vs including sensitive people-matters (the seam with ER case management).
- **Operating model**: tiered HR shared services / service centers (Ulrich-model framing in customer evidence) vs generalist HR teams.
- **Channel breadth & language coverage** (one product: 30+ languages).
- **AI posture**: rule-based virtual agent vs GenAI copilot vs agentic execution.
- **Adjacent modules**: broadcasts with acknowledgment tracking, asset tracking against employees, union grievances, accommodations, PIPs.
- **Deployment & commercial shape**: cloud vs on-prem; per-agent licensing (not asserted).

### L3 — Vendor-specific Structure (research notes only)

- Oracle: service-request→case linking as an object-level mechanism; embedded OTBI; Oracle ME/Journeys coupling; native HCM unification ("no third-party integrations"); single security model across Oracle Cloud.
- Dovetail: HR Home Console with profile/lifecycle-stage segregation; XpertHR content integration; Mineral HR compliance integration; broadcasts with acknowledgment tracking; assets recorded against employees; 50+ OOB reports; "Built for HR, not IT" positioning; Sapient Insights #1 vendor-satisfaction claims (marketing).
- Atlassian: "work categories" (request vs case) as the mechanism; findings/outcomes fields on the case work category; help-seeker invisibility rule; reuse of issue security schemes; Confluence-as-KB; JQL-defined SLAs; workforce management module.
- Freshworks: "Business Teams" packaging; SOP checklists inside case management; document/e-signature inside HR workflows; AI HR Agents.
- HR Acuity: Plan/Investigate/Determine methodology; olivER; managER; ThroughCare™; benchmarking (from ER pass).
- ServiceNow: not researched (unreachable); no vendor-specific claims recorded.

## Vendor-specific Findings

- Oracle's service-request→case linking (multiple requests aggregated into one case for systemic resolution) is product-specific mechanics; the generalized need (connecting related work) appears elsewhere as case linking (Case IQ, ER pass) — keep product-specific.
- Dovetail's broadcasts-with-acknowledgments and assets-against-employees are product-specific adjacent modules; not part of the Type.
- Atlassian's help-seeker invisibility rule for cases is product-specific wording of the general confidentiality discipline; the general rule (sensitive HR work restricted from the requester-facing surface) is cross-product.
- Freshservice's SOP checklists and in-workflow e-signature are product-specific implementations of consistency and document needs.
- All vendor marketing statistics (5 HCM screens, 50% inquiry reduction, 50+ reports, #1 rankings) are unverified claims — recorded here only.

## Boundary Findings

1. **vs Employee Relations Case Management (§09 sibling, processed) — the joint-pass seam, now resolved.** ER case management's defining core is the *confidential case record of a reported sensitive people-matter* with investigation logic, party linkage, privilege, fairness constraints, and defensibility. HR case management's defining core is the *HR case desk per se* — the full range of workforce-raised HR work, predominantly transactional questions/requests, worked to recorded resolutions. The seam is a matter of defining core, not of product boundaries: sensitive-matter handling appears *inside* HR case products as a case type or sibling module (Oracle: "complex employee relations cases" inside case management; Dovetail: separate ER module; JSM: case work category with allegations/findings/outcomes), but the investigation-grade regime (privilege marking, guided investigation methodology, anonymous intake, aftercare/retaliation monitoring) is ER's defining core and only shallowly present in HR case desks. Tests both ways: strip the sensitive-matter machinery → the HR case desk remains (transactional service work); strip the transactional request machinery → ER case management remains. Naming blur recorded: HR Acuity markets its ER platform as "HR Case Management"; the directory split remains defensible because the two Types have different defining cores, different access regimes, and different stakes. The ER pass's framing ("service requests vs sensitive matters") is confirmed as the *market-dominant* division of labor, with the caveat that HR case desks commonly carry some sensitive-matter capability.
2. **vs Employee Service Management (§10, processed).** ESM is the general service-delivery machinery (catalog, SLA, knowledge, CSAT discipline) operated across departments, with HR as one department; HR case management is the HR department's case desk — either a module of an ESM platform (JSM, Freshservice) or an HR-native product (Oracle, Dovetail). The ESM pass's test is confirmed with direct evidence: JSM implements HR case handling as a work category *inside* its service space ("while still using the rest of Jira Service Management — queues, automation, and the portal — in the same way as service requests"). Strip general request machinery → HR case management remains; strip HR case semantics → generic ESM remains.
3. **vs Employee Service Portal (§09, processed).** The portal is the front-door surface (browse, submit, track); HR case management is the handling machinery behind it. Dovetail ships both as separate products (Employee Portal + HR Case Management); JSM's help center is a component of the service space. Strip fulfillment machinery → a portal remains; strip the portal → the case desk still works (email-to-case, phone, agent-created).
4. **vs Enterprise Request Management (§10, processed).** ERM centers request intake/approval/fulfillment orchestration; HR case management adds the HR case discipline (case vocabulary, employee binding, resolution ownership, confidentiality regime). Consistent with the ERM pass's finding.
5. **vs Employee Record System / HRIS (§09).** Cases are the working objects; the employee record is context. Every sampled product binds cases to employee data pulled from HCM/HRIS (Oracle natively; Dovetail via connectors with profile-scoped visibility; Freshservice/HR Acuity via integration). Remove the case process → the HRIS remains. No sampled product manages employment records itself.
6. **vs Help Desk / Ticketing System (§07/§14).** Same mechanics (queues, statuses, SLAs), different population (employees vs external customers), different provider (HR vs IT/support), different data regime (personal employment data). The market itself polices this boundary: Dovetail's customer rejected tools "built on incident management systems that IT would use"; HR Acuity's FAQ contrasts help-desk queues with matter handling. Swap the population to external customers → customer support.
7. **vs Whistleblowing / Speak-up Platform (§11).** Speak-up centers safe disclosure (anonymity, channels, compliance); HR case management centers the handled case. Different program ownership (ethics/legal vs HR). Intake channels may feed HR cases, but the anonymity machinery is not part of this Type's core.
8. **vs Ethics & Conduct Management (§11, processed).** E&C is the conduct-program record system (disclosures, attestations, registers) under the ethics program; HR case management is HR's case desk. Consistent with that pass's boundary.
9. **vs Employee Offboarding Platform (§09, processed).** Offboarding is lifecycle-shaped (organization-initiated event with templated fan-out); HR case management is case-shaped (employee-raised work worked to resolution). HR case products may *model* onboarding/offboarding as journeys (Freshservice, Oracle, JSM) — a packaging overlap, not a structure identity. Consistent with the offboarding pass.
10. **vs Business Case Management Platform (§10).** Generic case management provides record+routing+lifecycle without the HR domain semantics: employee binding, HR case vocabulary, employment-data confidentiality, HCM integration. HR case management is a domain instantiation of the case pattern.

## Taxonomy Observations

- The market category is real and named: "HR Case Management" appears as a product name (Dovetail), a module name (Oracle HR Help Desk's case-management pillar; JSM's HR case management), and an analyst survey category (Sapient Insights HR Service Delivery, cited on Dovetail's page). The directory leaf is well-founded.
- The naming blur with ER case management is confirmed and now documented from both sides (HR Acuity's own FAQ draws the ticketing-vs-matter seam; Dovetail and Oracle ship ER handling as a sibling module/case type inside HR case products). The two-leaf split is defensible; no directory change recommended.
- The dedicated-HRSD pure-play segment is consolidating and hard to reach (ServiceNow/Neocase/UKG/Zoho unreachable in this environment; Espressive absorbed into Resolve per the ESM pass). Recorded as a sampling limitation, not a taxonomy problem.

## Uncertainties

- **ServiceNow absent** — the enterprise flagship is evidenced only indirectly. All ServiceNow-specific framing is absent; the enterprise-suite pole rests on Dovetail's positioning and analyst-category evidence. Assertion strength calibrated accordingly.
- **Evidence tier**: Tier 1 only for JSM; Oracle/Dovetail/Freshservice rest on Tier 2 official product pages (Dovetail's is feature-level and quote-rich, but still marketing-tier). No exact state names, field lists, or numeric parameters are asserted in the final document.
- **Oracle's operational depth** (exact service-request vs case object model, exact routing rule types) is not verified in documentation — only the product page's conceptual claims.
- **CSAT/feedback** is directly evidenced at two products only; treated as common with moderate wording.
- **Case linking** mechanics evidenced at one product (Oracle) plus repeat-incident linking in the ER pass (Case IQ); kept product-specific/optional.
- **Sensitive-matter depth** inside HR case desks varies and could not be quantified; the boundary statement is calibrated ("commonly present at varying depth; investigation-grade regime is ER's core").
- **SMB HR-suite pole unsampled** (Zoho unreachable); the Type's shape at the smallest customer scale is inferred from Freshservice's mid-market positioning only.

## Final Synthesis

HR Case Management is best understood as **HR's case desk**: the system where work raised by the workforce — questions, requests, transactions, and reports — becomes a typed, tracked case bound to the employee and their organizational context, is assigned to an HR handler, and is worked through a managed lifecycle to a recorded resolution, under a confidentiality discipline appropriate to personal employment data.

The defining core is small: HR as the providing function + the case as tracked typed record bound to the employee + a managed lifecycle to recorded resolution under confidentiality discipline. Everything the market associates with modern HR service delivery — self-service portals, knowledge bases, SLAs, routing rules, correspondence capture, templates, document generation, approvals, analytics, AI assistants, lifecycle journeys, HCM integration — is mature-common structure, not definition. Older agent-side-only HR case systems (email-to-case, no portal) still satisfy the core.

The market expresses the Type through four packaging postures: dedicated HRSD pure-plays ("built for HR, not IT"), HR-suite-native modules (case desk unified with HCM), ESM-platform modules (HR as one department in a service-management platform), and ER-specialist platforms that market sensitive-matter handling under the same name. The sharpest boundaries: against ER case management (the sensitive-matter specialization with investigation-grade regime — the joint-pass seam, resolved as two Types with an overlapping implementation zone), against employee service management (the general machinery of which the HR case desk is the HR instantiation), against the HRIS (records vs case work), and against customer support (population). The Type's reason to exist, in the market's own words: replace shared inboxes and spreadsheets, give HR control over its data, make answers consistent across HR reps, and keep sensitive employee data in the right hands.
