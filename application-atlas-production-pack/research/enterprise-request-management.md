# Research Notes — Enterprise Request Management

## Research Goal

Understand what an Enterprise Request Management (ERM) application actually is as a Type: what objects exist inside it, who uses it, how a request moves from submission to fulfilled service, which rules govern it, and where its boundary sits against ITSM, Enterprise Service Management, Approval Workflow Platforms, ticketing systems, and the public-sector 311 twin.

Context: this leaf was flagged by the employee-service-management pass (2026-09-06) as "request-orchestration subset without the full service discipline" and by the approval-workflow-platform pass ("ERM's object is the service request fulfilled by a team; approval platform's object is the decision itself"). This pass must confirm or correct those flags with direct product evidence.

## Initial Boundary (pre-research hypothesis)

- ERM = internal request orchestration: a defined catalog of requestable services → submitted request → routing through approvals and fulfillment → tracked completion with requester-visible status.
- Nearest neighbors: ITSM (§14), Enterprise Service Management (§10 sibling), Approval Workflow Platform (§10), Ticketing System / Help Desk (§07/§14), 311 Citizen Service Request Platform (§24, public-sector twin), Employee Service Portal (§09, front-door surface), Workflow Management Platform (§10).
- Unknowns: (1) is the catalog binding part of the defining core or just common? (2) is the requester population strictly internal? (3) does the market still use the literal "ERM" label? (4) how deep does fulfillment automation go in the defining core vs as an advanced variant?

## Research Questions

1. What is the central object — request, ticket, submission, work item — and how is it bound to a defined offering?
2. What does the catalog/offering definition contain (form, owner, approval path, SLA, visibility)?
3. Who fulfills requests — teams, individuals, automation — and how is fulfillment tracked?
4. What role do approvals play (gate vs organizing purpose)?
5. What does the requester see (portal, status, notifications)?
6. How do products differ in product form: standalone orchestration layer vs request slice of an ITSM/ESM suite?
7. Where is the boundary vs ITSM/ESM (service discipline), vs approval platforms (decision-centricity), vs ticketing (free-form intake), vs 311 (population/routing)?
8. Historical check: would Remedy-era service request management and platform-native request lists still fit the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier | Evidence tier reached |
|---|---|---|---|
| Kinetic Platform | Kinetic Data | ERM-native lineage (25+ years; formerly Kinetic Request on BMC Remedy); now positioned as "workflow orchestration platform"; standalone catalog+orchestration layer over existing systems of record; enterprise/government | Tier 1 (docs.kineticdata.com: Key Terms, llms.txt index) + Tier 2 (service-request-management and it-service-catalog use-case pages) |
| Freshservice | Freshworks | SaaS mid-market ITSM→ESM; "manage internal requests from your employees"; department workspaces (FSBT) | Tier 1 (support.freshservice.com KB: Service Catalog category + Configure the Service Catalog article + KB structure) |
| Jira Service Management | Atlassian | team-scale service desks; request/work-item duality; template-based departments | Tier 1 (support.atlassian.com: full doc tree + "About requests and work items" article) |
| SolarWinds Service Desk | SolarWinds | mid-market ITSM with ESM feature set; ITIL-framed service catalog education | Tier 2 (product page + IT Service Catalog use-case page) |

Rejected / unreachable samples (per network rules, abandoned after 1–2 failures):

- **ServiceNow** — docs.servicenow.com is a JavaScript application (no content without JS); product page timed out. The largest enterprise incumbent is therefore unverified this pass; no claims made about it.
- **TeamDynamix** — teamdynamix.com 403 on both root and product page. The other ERM-native vendor is unverified.
- **BMC Helix ITSM** — docs.bmc.com URL 404; bmc.com 403. The Remedy lineage is instead evidenced indirectly through Kinetic's own documentation (Remedy Edition lineage).

## Sources

Fetched 2026-09-06:

- Kinetic Data — https://kineticdata.com/ (home), https://kineticdata.com/use-cases/service-request-management, https://kineticdata.com/use-cases/it-service-catalog, https://docs.kineticdata.com/ (welcome), https://docs.kineticdata.com/llms.txt (index), https://docs.kineticdata.com/docs/key-terms.md
- Freshservice — https://support.freshservice.com/en/support/home (KB home), https://support.freshservice.com/support/solutions/159916 (IT & Employee Service Management category), https://support.freshservice.com/support/solutions/articles/199643-configure-the-service-catalog
- Atlassian — https://support.atlassian.com/jira-service-management-cloud/resources/ (doc tree), https://support.atlassian.com/jira-service-management-cloud/docs/what-are-issues-and-requests/
- SolarWinds — https://www.solarwinds.com/service-desk, https://www.solarwinds.com/service-desk/use-cases/it-service-catalog

Carried-over context from same-day sibling passes (not re-fetched): research/employee-service-management.md, research/approval-workflow-platform.md, research/311-citizen-service-request-platform.md, research/employee-portal.md, research/employee-service-portal.md.

## Product Observations

### Kinetic Data (Kinetic Platform)

Evidence tier: A (docs) + A (use-case pages, vendor-authored operational walkthroughs).

Key observations:

- **Positioning drift**: the homepage now leads with "workflow orchestration platform" — AI builds forms/workflows/integrations, a "governed, deterministic engine" executes across existing systems. The literal "Enterprise Request Management" label is no longer the headline. The request function survives as use-case pages: "Service Request Management" and "IT Service Catalog". (Market-label drift — see Taxonomy Observations.)
- **Catalog as unified front door over heterogeneous backends**: "a unified service catalog layer that sits on top of every backend system… presents a single, searchable catalog where every service — regardless of which systems fulfill it — appears in one consistent experience." Explicit contrast with native ITSM catalogs: "the catalog becomes a submission form, not a delivery mechanism… In Kinetic, submission triggers an automated workflow that orchestrates fulfillment across every system involved."
- **10-step request lifecycle** (vendor-documented walkthrough): submit via self-service portal (dynamic form adapting to role/department) → business rules evaluate (approval chain, fulfillment path, SLA target by request type/cost/security classification/department) → approval routing (manager, cost center owner, data owner, security team; approve from email/mobile/portal) → SLA clock + escalation → parallel fulfillment across backend systems → sequential dependency management → exception handling (failed step routed to the right team with context; unblocked branches continue) → status pushed to requester (real-time progress, expected completion) → fulfillment confirmed across all systems → audit trail.
- **Object vocabulary (Tier 1 docs, Key Terms)**: Space (tenant) → Kapp ("a collection of Forms… typically represents a single end user experience. Service portals and work order systems are both examples of Kapps") → Form → Submission ("an instance of a form that contains field values"). **Submission Activity** = "a way to attach additional information to a submission, typically with the purpose of exposing some process details to the original submitter. Examples include 'Assigned to User' and 'Awaiting Approval'." Teams group users; User Attributes (location, job title, hire date) drive workflow. Workflows are trees (nodes, wait states, loops, process gates, connector logic); Routines are reusable cross-Kapp processes; Handlers execute units of work; Bridges connect data sources.
- **Event example from docs**: "Submission Submitted" event → workflow that does "creating a record in the fulfillment system and assigning it to the appropriate team when a request is submitted."
- **Security**: Security Policy Definitions with KSL rules evaluated at runtime on resource access; SAML/LDAP/CAC authentication; on-premises and air-gapped deployment options; IL5 certification claimed on marketing pages.
- **Lineage**: docs state the platform is "built with a version of Request (CE) that is entirely our own creation, unlike our previous versions (RE, or Remedy Edition) that relied on Remedy to act as the platform" — direct evidence that this product family's request-management lineage runs through BMC Remedy, the classic enterprise request/ITSM platform generation.
- **Scale claims (marketing, Tier 2)**: FCPS 250K+ requests/year across 200+ locations; USDA provisioning 3 weeks → 30 minutes. Not asserted in the final document beyond "high-volume" framing.

### Freshservice

Evidence tier: A (KB article + KB structure).

Key observations:

- **Positioning**: "Streamline your IT service and manage internal requests from your employees" (support portal product blurb). ITSM core with ESM extension: KB has a dedicated "Enterprise Service Management" category ("Setup ESM with employee onboarding, access controls, and more") and "Freshservice for Business Teams" (FSBT) department workspaces (onboarding articles for HR teams and finance functions).
- **Service Catalog definition (Tier 1)**: "The Service Catalog is a centralized list of services offered by an organization. It gives users clear information about each service—including its purpose, availability, and how to request it."
- **Catalog structure**: multi-level categories (up to three levels); per-workspace catalogs; service items with: name, category, short/detailed description, cost, estimated delivery (hours), "Requested for" option, custom fields (incl. shared fields, lookup fields, content fields), additional items (related services requestable alongside the main one, optionally generating **child requests/tickets per item** handled by agents in respective departments under their own SLAs), fulfillment options (asset type/product binding for hardware/consumables/software), visibility restriction to requester groups, subject customization. Items have **Save & Publish vs Save as Draft** states.
- **Requester side**: multi-level catalog in the support portal; "Requesting a Service from the Service Catalog [End User Guide]" exists as an end-user article; multiple requester portals (workspaces) with per-portal configuration.
- **Approvals (Tier 1 KB structure)**: dedicated Approvals folder — "Service Request Approvals Access for Requesters", "Ticket and change approval via Email", "Introducing Groups and Chains in Approvals", "Delegating Approvals to Your Peers". So: approval chains/groups, email approval, delegation, requester visibility of approvals.
- **Fulfillment machinery**: Task management folder — tasks assigned to team members, task OLA policies; SLA policies per department/group; XLAs (experience level agreements) as a newer layer.
- **Adjacent ITIL modules present** (incident/problem/change/release) — confirming that in suite products the request function sits inside a wider service-management discipline.

### Jira Service Management

Evidence tier: A (docs).

Key observations:

- **Request/work-item duality (Tier 1)**: "Work items are how pieces of work are internally represented… to admins and agents… Requests are how work items are represented on help centers to help seekers, and are the items submitted by your customers or end-users. When customers submit requests… their requests automatically become work items that can be tracked in your service space. These work items are automatically triaged into queues." And: "A work item and a request are two different views of the same unit of work."
- **Request types**: "Request types let you define and organize incoming requests… Phrasing request types in a customer-friendly way allows your customers to identify what kind of service or request they need quickly. For example, *Purchase a new monitor*, *Get help with printers* or *Get wi-fi access*." Work types give fields + workflow statuses; request types give naming/portal presentation; one work type can back many request types. Request types can carry restrictions (who can see/use), portal groups, per-type workflow customization.
- **Channels**: help center/portal, email (multiple addresses, processing rules), embeddable widget, chat (Slack/Teams). Agents can raise requests on behalf of customers.
- **Approvals**: "Set up an approval stage" section — approval steps added to workflows, preset approver lists, customer-chosen approvers, approval by email and chat. Approvals are workflow stages, not the organizing purpose.
- **Queues**: agent-side triage views over incoming requests.
- **Population flexibility**: "customers" can be external or internal ("Allow internal accounts to request a service space"); templates for customer service, business, or IT teams. The same machinery serves customer support and internal service — the Type boundary is the deployment frame, not the machinery.
- **Service discipline present**: SLAs (goals, calendars, conditions), CSAT, knowledge base, reports — again the request function inside a wider discipline.

### SolarWinds Service Desk

Evidence tier: B (Tier 2 product + use-case pages, vendor-authored educational content).

Key observations:

- **Service catalog framing (ITIL)**: "An IT service catalog has two views: 1. A customer-facing view for users to browse and select the services they need. 2. A technical service view showing exactly what's needed to deliver the services contained in the catalog… clear guidance on how to route requests to the right support professionals and how to complete services." And: "The services within an IT service catalog are typically very repeatable, with controlled inputs, processes, and outputs."
- **Catalog item metadata** (educational list): owner/accountable person or group, identification label, description, categorization, supporting/underpinning services, SLA data, escalation points/approvals/key contacts, business criticality.
- **Example catalog services**: new hardware, software licenses, cloud application access, password reset, onboarding, periodic maintenance, change request, project management, new virtual server.
- **Dynamic request forms**: "Instead of displaying the same form to every user, you can create custom forms and establish dynamic form rules to control when each specific form appears."
- **Per-service workflows + approvals**: "Automate workflows and approval processes specific to each service… many of the services you provide to your employees involve multiple departments."
- **ESM posture**: "Service Desk's IT service catalog software is where the IT department, HR, facilities, or other departments can connect employees to the services they need"; ESM feature = "Empowering departments to publish offered services and structure service delivery… Segregated service desks ensure access control to sensitive data."
- **Employee self-service portal** as the front door; knowledge base for deflection; SLA monitoring.

## Cross-product Comparison

| Dimension | Kinetic | Freshservice | JSM | SolarWinds |
|---|---|---|---|---|
| Central object | Submission (form instance) exposed as a request with Submission Activities | Service request (ticket) bound to a service item | Request (external view) = work item (internal view) | Service request bound to a catalog service |
| Catalog binding | Forms within Kapps (service portal Kapp); unified catalog over external systems | Service items in multi-level categories; publish/draft states | Request types (customer-friendly) backed by work types | Catalog services with two views (user-facing + technical) |
| Requester surface | Self-service portal; real-time status; Submission Activities | Support portal; multiple portals; end-user guide | Help center/portal; requests list; email/widget/chat channels | Employee self-service portal |
| Approvals | Business-rule routing (cost/security/department); email/mobile/portal approval | Groups & chains; email approval; delegation; requester-visible | Approval stages in workflow; preset/chosen approvers; email/chat approval | Per-service approval processes; escalation points |
| Fulfillment | Cross-system orchestrated automation (parallel/sequential, exception routing) | Tasks to agents/teams; child requests per additional item; OLA policies | Queues → agent assignment; automation rules | Workflows per service; routing guidance in technical view |
| Time governance | SLA clock from submission, escalation before breach | SLA policies; task OLA policies; XLAs | SLA goals/calendars/conditions | SLA data per service; service level management |
| Population | Enterprise/government internal (employees; also citizens in gov deployments) | Employees ("internal requests"); department workspaces (HR/finance) | Customers or internal accounts; IT/business/customer-service templates | Employees across IT/HR/facilities |
| Product form | Standalone orchestration layer over existing systems of record | ITSM suite with ESM extension | Team-scale service desk product (Jira platform) | ITSM suite with ESM feature set |
| Service discipline around requests | Minimal by default (orchestration-first; SLA/audit present) | Full ITSM suite around it | Full (SLA/CSAT/KB/reports) | Full ITSM suite around it |

**Stable across all four (Layer B — cross-product commonality):**

1. A **defined, published set of requestable services** (catalog items / request types / forms / services) that requesters submit against — with per-offering request forms.
2. A **submitted request as a tracked record** binding requester × offering × submitted data, with a lifecycle.
3. **Routing into fulfillment**: assignment to a responsible team/agent, optionally through approval gates and decomposed into fulfillment tasks.
4. **Requester-visible lifecycle**: status/progress surfaced back to the requester (portal lists, Submission Activities, notifications).
5. **Dual view**: requester-facing presentation vs fulfiller-facing working view of the same record.
6. **Per-offering configuration**: form fields, visibility, approval path, fulfillment path, delivery expectations.
7. **Approval as a gate inside the flow**, not the organizing purpose (present in all four, but always one stage among fulfillment steps).
8. **Time governance** (SLA/OLA) and **audit/history** as standard layers.

**Not universal (variant/optional):** cross-system fulfillment automation (Kinetic's differentiator; suite products fulfill natively or via integration apps); multi-department workspaces (Freshservice FSBT, SolarWinds ESM; JSM per-space); external-customer use (JSM); AI classification/virtual agents (Freshservice Freddy, SolarWinds AI; Kinetic AI-assisted build); knowledge-base deflection (JSM, SolarWinds, Freshservice; not evidenced in Kinetic's fetched surfaces).

## Canonical Model (synthesis)

**L0 — Defining Invariant** (remove any one and the Type stops being recognizable):

1. **Published catalog of defined service offerings** — the organization pre-defines what can be requested, each offering carrying a request form and (implicitly) a fulfillment path. This is the discriminator vs free-form ticketing.
2. **Submitted request as tracked record** — an internal requester's submission bound to a specific offering, holding the submitted data and a tracked lifecycle state.
3. **Routing into fulfillment** — the request is directed to a responsible internal provider (team/individual/automation) along a defined path, which may include approval gates and fulfillment tasks.
4. **Tracked lifecycle to an outcome with requester-visible state** — the request advances through states (received → approved/assigned → fulfilled → closed; or rejected/cancelled) and the requester can see where it stands.

The requester population is **internal** (employees/teams of the operating organization) — this is part of the Type's frame ("enterprise"); external-customer deployment of the same machinery is the customer-support Type's frame.

**L1 — Common Mature Structure** (very common in mature products, not definitional):

- Requester portal / catalog front door (browse, search, submit, "my requests" tracker)
- Approval gates: multi-step chains, groups, email/chat/mobile approval, delegation
- Fulfillment task decomposition (tasks assigned to teams/individuals; OLA-style task targets)
- SLA targets per offering with escalation
- Dynamic/conditional request forms; pre-population from organizational data (manager, cost center, entitlements)
- Catalog item metadata: owner, description, category, cost, delivery expectation, visibility restrictions
- Notifications and status updates to requester and fulfillers
- Fulfillment automation/integration (provisioning across connected systems)
- Reporting/analytics (volumes, fulfillment times, bottlenecks, SLA compliance)
- Knowledge base deflection; CSAT
- Multi-department operation (department workspaces, segregated desks)
- Audit trail / compliance reporting

**L2 — Variant / Optional Structure**:

- Product form: standalone catalog+orchestration layer over existing systems of record vs request-management slice of an ITSM/ESM suite vs team-scale service desk
- Departmental scope: IT-only vs all departments (ESM posture)
- Fulfillment depth: native ticket-and-human vs orchestrated cross-system automation
- Requester population extensions: external customers (JSM), citizens (public-sector deployments)
- AI posture: assisted build, classification, virtual agents, auto-approval
- Deployment: SaaS vs on-premises/air-gapped; multi-tenant workspaces
- Catalog scale practices: incremental rollout, multi-location variance

**L3 — Vendor-specific** (kept out of the final document):

- Kinetic: Kapp/Space/Submission Activity/Bridge/Handler/Routine vocabulary; KSL security policies; IL5/CAC; USDA/MDA/FCPS case-study numbers
- Freshservice: FSBT workspaces, Freddy AI, loaner service items, child-request mechanics per additional item
- JSM: work-item/request terminology, team-managed vs company-managed spaces, Rovo AI knowledge base
- SolarWinds: Samanage lineage, benchmarks, ITSM maturity model, ITIL educational framing

## Historical / Market-Sample Check

- **Remedy-era request management**: Kinetic's own docs document the Remedy Edition lineage ("previous versions (RE, or Remedy Edition) that relied on Remedy to act as the platform"). The catalog → request → fulfillment structure predates the current SaaS generation; the L0 holds for that generation. SolarWinds frames the catalog in ITIL 4 terms — the ITIL service-catalog concept (customer-facing view + technical view) is the older discipline the software implements.
- **Platform-native request lists** (SharePoint/Forms-style request tracking, ERP approval steps): fit L0 when they bind a request to a defined offering and route it to a responsible provider with tracked state; degenerate to form+email when they don't.
- **Manual baseline** (email/verbal requests to a service desk): outside the Type — no catalog binding, no tracked shared state. Confirms the boundary criterion.
- **Regional/era fit**: the ITIL service-catalog discipline is global; no region-specific structure entered L0. No over-fitting to the current SaaS pattern detected.

## Boundary Findings

1. **vs IT Service Management (§14, unprocessed)** — the most common implementation of ERM is the *service request management slice* of ITSM products (all three suite samples evidence this). Boundary: ITSM centers the IT function's full service discipline (incident/problem/change/CMDB/ITIL practices); ERM centers the request-fulfillment flow for defined offerings, across departments. Test: strip incidents/problems/changes/CMDB → ERM remains; strip the catalog+fulfillment flow → ITSM remains. Structurally continuous; scope-based boundary. Flag for joint review when ITSM is processed.
2. **vs Enterprise Service Management (§10 sibling, unprocessed)** — consistent with the employee-service-management pass flag: ESM wraps the request flow in the full service-management discipline (departments as providers, SLA framework, knowledge, measurement); ERM is the request-orchestration subset. Test: strip the service discipline → ERM remains; strip request orchestration → ESM remains. Probable scope gradient; flag for joint review when ESM is processed.
3. **vs Approval Workflow Platform (§10, processed)** — confirmed the approval pass's boundary from the ERM side: the approval platform's object is the authorization decision; ERM's object is the requested service fulfilled by a team. Approval appears in all four sampled products, always as a gate inside fulfillment (workflow stage, task, or rule-evaluated routing), never as the organizing purpose. Test: remove fulfillment/ownership machinery, keep only the gate → approval platform.
4. **vs Ticketing System / Help Desk (§07/§14)** — free-form ticket intake vs catalog-bound requests with pre-defined fulfillment paths. Test: remove the catalog/offering definitions → generic ticketing remains. (JSM shows the two share machinery; the catalog binding is the structural discriminator.)
5. **vs 311 Citizen Service Request Platform (§24, processed)** — public-sector twin with the same skeleton (catalog → request → routing → tracked lifecycle → status feedback). Differences: requester population (resident vs employee), routing basis (jurisdiction/location vs organizational structure), accountability framing (public transparency vs internal governance). Test: swap the population to residents + civic catalog → 311 Type.
6. **vs Employee Service Portal (§09, processed)** — portal = front-door surface (browse/submit/track); ERM = the orchestration behind it. In the sample, portals ship as components of request/ESM products (JSM help center, Freshservice portal, SolarWinds self-service portal, Kinetic portal Kapp). Test: strip fulfillment machinery → a portal remains.
7. **vs Workflow Management Platform / BPM (§10, unprocessed)** — generic engines route tasks between people/systems but have no requester-facing catalog or request lifecycle as first-class objects. Test: remove the requester-facing request object + catalog → workflow engine remains. Kinetic's current "workflow orchestration" positioning shows a vendor drifting toward the engine framing while keeping the catalog+request layer — a gradient to watch, not a merge.
8. **vs HR Case Management (§09, processed)** — consistent with the ESM pass: HR cases are sensitive case types with structured findings/outcomes; ERM requests are general service fulfillment. HR service requests (equipment, onboarding tasks) route through ERM machinery; investigations/grievances belong to case management.
9. **vs Customer Service Platform (§07)** — audience identity: internal requesters vs external customers. JSM demonstrates the machinery is shared and deployable for both; the Type boundary is the deployment frame (internal service catalog semantics vs customer support semantics).
10. **vs Purchase Order Management / Procurement (§10)** — procurement requests may be catalog items inside ERM; the PO system remains the system of record for purchase orders. ERM routes and tracks the request; downstream systems execute. (Kinetic's own framing: orchestration over systems of record.)

## Taxonomy Observations

- **Market-label drift**: the literal leaf label "Enterprise Request Management" is rare in current market language. The ERM-native flagship (Kinetic Data) now headlines "workflow orchestration platform"; the function is overwhelmingly sold as "service request management", "request management", "service catalog", or "enterprise service management" inside ITSM/ESM suites. The Type remains structurally real (catalog + request + fulfillment orchestration is stable across all four samples), but the leaf name is a minority label. Recorded for the taxonomy owner; no directory change proposed.
- **Consolidation pressure**: like approval workflows (see approval pass observation), standalone request-management positioning is being absorbed into suites and orchestration platforms; the request function persists as a slice/capacity of larger products. This supports keeping the Type defined by structure, not by product-category labels.
- The employee-service-management pass's flag ("ERM = request-orchestration subset without the full service discipline") is **confirmed** by direct evidence; the approval pass's boundary is **confirmed** from the ERM side.

## Uncertainties

- ServiceNow, TeamDynamix, BMC Helix unreachable — the enterprise-incumbent tier is characterized only indirectly (Kinetic's Remedy lineage note; SolarWinds' competitor-comparison page names). No claims made about those products' current mechanics.
- Whether any current vendor still markets a dedicated "ERM" SKU could not be verified; the label-drift observation rests on the sampled surfaces.
- Kinetic's Submission Activity state vocabulary ("Awaiting Approval", "Assigned to User") is documented as examples, not an exhaustive state list; no canonical state names asserted.
- Freshservice child-request mechanics and approval groups/chains are evidenced at KB-structure + article level; exact configuration limits not asserted.
- Public-sector deployment of internal request machinery (e.g., Kinetic in government) is evidenced by marketing pages only; kept out of the final document.

## Final Synthesis

Enterprise Request Management is the **internal request-fulfillment orchestration Type**: the organization publishes a catalog of defined service offerings; internal requesters submit requests against those offerings; each request is routed through a defined fulfillment path — approval gates where required, fulfillment tasks and/or automated actions executed by the responsible internal provider — and advances through a tracked lifecycle to a completed outcome, with status visible to the requester throughout. The defining core is deliberately small (catalog + request + routing + tracked requester-visible lifecycle); portals, approvals machinery, SLA/OLA governance, dynamic forms, automation depth, multi-department workspaces, and analytics are the mature market's standard additions, not the definition. The Type is most commonly implemented as the request-management slice of ITSM/ESM suites, with a smaller standalone-orchestration segment; the literal "ERM" label has largely receded in market language while the structure persists.
