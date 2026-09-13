# Research Notes — IT Service Management / ITSM

## Research Goal

Understand what the software answering to "IT Service Management / ITSM" actually is as an Application Type: what its world consists of (objects, practices, records), how an IT organization uses it day to day, how it differs from the single-practice tools that share its vocabulary (incident/problem/change management), from the machinery beneath it (ticketing, help desk), from its operations sibling (ITOM), and from its cross-department sibling (Enterprise Service Management).

## Initial Boundary (pre-research hypothesis)

- ITSM is likely the **umbrella suite Type** of the IT service desk world: not one practice but a bundle of governed practices (request/incident/problem/change/configuration/asset/knowledge/service levels) operating on one shared record base, organized around "IT as a service".
- Sibling passes (incident-management, it-change-management, it-problem-management) each documented their practice as "one governed practice/module inside the ITSM suite" and hung a joint-review flag here: expected seam = **suite vs single practice sold standalone**, same pattern the enterprise-service-management pass faced.
- Nearest confusions: Ticketing System (generic machinery), Help Desk (requester-serving single-practice application), ITOM (estate operations layer), ESM (scope gradient beyond IT), CMDB / IT Asset Management (record types bundled inside ITSM suites and also sold standalone).

## Research Questions

1. What is the defining structure of an ITSM product — what must it contain so it is not just a help desk with a bigger name?
2. What is the role of the "service" concept — service catalog, service levels, customer contracts — in the record base? Is it formal (objects) or conceptual (classification), and does that variation break the definition?
3. How do the practices interlock on the record level (incident → problem → change; tickets ↔ configuration items ↔ services)?
4. Who uses it (roles) and what are the main surfaces (agent console, portal, admin config)?
5. Where exactly are the seams vs Ticketing System / Help Desk / ITOM / CMDB / ITAM / ESM / the standalone practice leaves?
6. Historical check: would pre-ITIL-era and older/regional products still fit a candidate definition that avoids ITIL-version naming?

## Representative Products

Selected for market representation, documentation completeness, different philosophies, different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Atlassian Jira Service Management | mid-market, collaboration-platform heritage, practice-template-oriented | richest Tier-1 operational docs; dev-collab philosophy ("ITSM without bureaucracy") |
| Freshworks Freshservice | SaaS, AI-era, mid-market→enterprise | ITSM+ITAM+ITOM+ESM "Unified ServiceOps" positioning; ITIL/PinkVERIFY-certified |
| ManageEngine ServiceDesk Plus | on-prem+cloud, ITIL-certified, SMB→enterprise | edition ladder (Standard→Professional→Enterprise) makes the suite-vs-desk seam visible inside one product line |
| iTop (Combodo, open source) | open-source self-hosted | Tier-1 data-model documentation exposes the full object graph (CMDB + service catalog + ticket classes) |

ServiceNow (the enterprise suite pole) was attempted once and timed out — unreachable in this pass and in four prior sibling passes; recorded as a sourcing limitation, not compensated from memory.

## Sources

Fetched 2026-09-08:

- Atlassian JSM docs (Tier 1): "What is Jira Service Management?" — support.atlassian.com/jira-service-management-cloud/docs/what-is-jira-service-management/; doc tree incl. ITSM template, SLAs, queues, request types, portals, approvals
- Atlassian ITSM concept guide (Tier 2): atlassian.com/itsm ("What is IT Service Management (ITSM)?")
- Freshservice product page (Tier 2): freshservice.com
- ManageEngine ServiceDesk Plus product page + FAQ (Tier 2): manageengine.com/products/service-desk/
- iTop wiki (Tier 1): Service Management module (itophub.io/wiki/page?id=3_2_0:datamodel:itop-service-mgmt) and Incident Management ITIL module (…itop-incident-mgmt-itil)

Unreachable this pass: servicenow.com/products/itsm.html (timeout ×1; unreachable in 4 prior sibling passes). Wikipedia ITSM not attempted (unreachable in the ITOM pass). Vendor marketing metrics (e.g. "77% faster resolution") recorded as marketing, not evidence.

## Product Observations

### Atlassian Jira Service Management (Tier 1 docs)

Evidence layer A (direct):

- Product definition (docs): "With Jira Service Management, you can easily receive, track, manage, and resolve requests from your team's customers. Customers can send requests by email, via help centers, and an embeddable widget. Jira Service Management makes it easier to categorize service requests, incidents, problems, and changes by organizing and prioritizing these requests in a single place, and keeps your team on track with goals (or service level agreements)."
- "Discover IT service management (ITSM)" docs section: "the strategic approach to designing, delivering, managing, and improving the way businesses use IT."
- The ITSM template is a specific space template with ITSM work categories (requests, incidents, problems, changes) — the practices arrive as a packaged template on a shared work-item platform.
- Structure: service project/space per team ("Each team can work on a project that services requests from a certain area – like IT, HR, legal, or finance"); request types with forms; queues for agents; agent/customer roles; portal + help center; email channel; KB (Confluence-linked) with article suggestions; SLA goals with calendars and conditions; approvals in workflows; automation rules; CSAT; reports.
- Assets (CMDB-class records) and Opsgenie on-call/alerts are addable surfaces ("Add Services, Alerts, and On-call to your sidebar") — practices beyond the desk present in-product.

Evidence layer B reading: single place holding request+incident+problem+change categories = the multi-practice shared record base, on a platform whose philosophy is anti-bureaucratic flexibility ("Atlassian flips that paradigm" — teams decide which SLAs/processes to adopt).

### Freshworks Freshservice (Tier 2 product page)

Evidence layer A (direct):

- Positioning: "Deliver enterprise IT service with Freshservice, an AI-powered ITSM platform"; "Service, operations, and assets unified… built on ITIL best practices".
- Blocks name the suite's spans: "Frictionless employee experience / Proactive incident management / Enterprise service delivery / 360° visibility / Intelligent automation"; "ITSM, ITAM, ITOM, ESM" named as connected domains on "one platform and CMDB".
- Modules named: Freddy AI Copilot/Agent Studio/Insights, incident management, on-call management, dependency mapping, workspaces, smart catalog, low-code orchestration, intelligent routing, asset lifecycle with continuous discovery.
- Certification framing: "PinkVERIFY®-certified across six ITSM processes"; "Gold Accredited Tool Vendor with certification across 14 ITIL practices" — ITIL practice certification is a market dimension of the category.
- Analyst framing: "Leader in the 2026 Gartner® Magic Quadrant™ for IT Service Management Platforms" — confirms "ITSM platform" as an analyst platform category (the suite, not a single practice).
- Customer quote: "Freshservice gave us one front door for the entire University. Students and staff don't need to know which team handles their request." — the desk as front door.
- Customer quote: "Change management in Freshservice is critical…" — change as an in-suite practice.

### ManageEngine ServiceDesk Plus (Tier 2 product page + FAQ)

Evidence layer A (direct):

- Positioning: "a service management solution that combines IT service management, IT asset management, and CMDB with enterprise service management capabilities for departments including HR, facilities, and finance."
- "ITIL®-certified for 14 practices"; PinkVERIFY practices named: "AI Capability, IT asset, change, configuration, incident, problem, request, and release and deployment management" — the canonical ITSM practice set enumerated by the vendor's own certification.
- Edition ladder: **Standard** = incident management, ticket templates, lifecycle builder, no-code automation, self-service portal, KB, SLA management, reporting; **Professional** = + ITAM (discovery, asset lifecycle, software asset management, purchase/contracts); **Enterprise** = + service catalog, problem management, change enablement & release management, IT project management, CMDB.
- FAQ: "Can ServiceDesk Plus be used solely as a ticketing system? Yes, the standard edition… can support your ticketing requirements." — the ticketing pole exists inside the same product family as a reduced edition.
- FAQ: "Can non-IT help desk teams use ServiceDesk Plus as well? Yes… enterprise service management capabilities."
- Deployment: on-premises and cloud, with migration between them.
- Customer quote: "the main competitor we looked at would've been ServiceNow" — ServiceNow as the enterprise suite pole.

### iTop, open source (Tier 1 data model wiki)

Evidence layer A (direct):

- Own definition: "IT Service Management (ITSM) is a process-based practice intended to align the delivery of IT services with needs of the enterprise. Part of this, is the management of the service catalog that defines services, SLA and contracts with the end users (or customers)."
- Top-level data model: **CMDB** (configuration core, end-user devices, virtualization, storage, data center) + **Service Management** (services, SLAs, contracts) + **Ticketing** (User Request Management, Incident Management ITIL, Simple/ITIL Change Management, Problem Management, Known Errors Management).
- Service Management module: Service Family → Service → Service Subcategory (subcategory binds to a request type: incident vs service request — "done to automate the qualification of a user request"); SLA = group of SLTs (metrics TTO "time to own" / TTR "time to resolve" per request type per priority); customer contracts bind customers to purchased services + applicable SLAs; provider contracts cover CIs; delivery model determines which teams may receive a customer's tickets ("If no delivery model is defined for a given customer, then you will not be able to create tickets for that customer").
- "The service management is integrated with the ticket management system: When creating a ticket for a given customer, the agent can select the service amongst the list of services defined for this customer. Ticket deadlines are computed depending on the SLA signed with the customer."
- Incident ticket fields: caller, origin (mail/monitoring/phone/portal), service + subcategory, impact × urgency → computed priority, team/agent, TTO/TTR deadlines, **parent incident / parent problem / parent change links**, impacted CIs tab, work orders, public/private logs, resolution code + solution, user satisfaction.
- Parent/child incident propagation: resolving the parent resolves children automatically.
- Single-company vs service-provider variants of the same catalog module (MSP pole exists in the open-source suite itself).

### Cross-product Comparison

| Structure | Atlassian JSM | Freshservice | ServiceDesk Plus | iTop |
|---|---|---|---|---|
| Service desk intake (portal, email, + channels) | A: portal/help center/email/widget/chat | A: self-service, employee experience block | A: self-service portal, email-to-ticket | A: portal; origins mail/monitoring/phone/portal |
| Demand records classified as requests vs incidents (+ problem/change classes) | A: "service requests, incidents, problems, and changes… in a single place" | A: incident mgmt block + change mgmt quote | A: incident/problem/change/release named practices | A: separate ticket classes per practice |
| Service orientation (service catalog / service-shaped classification) | A (conceptual): services surface; request types as the catalog | A: "smart catalog", service catalog | A: service catalog module (Enterprise) | A (formal): Service/SLA/contract objects; subcategory→request type |
| Service levels (SLA machinery on records) | A: SLA goals, calendars, conditions | A: SLA adherence quote | A: SLA management + escalations (Standard) | A: SLA/SLT objects computing ticket deadlines (TTO/TTR) |
| Configuration/asset records shared with tickets | A: Assets addable | A: "one platform and CMDB", asset lifecycle | A: CMDB (Enterprise), ITAM (Professional) | A: CMDB top-level module; impacted-CIs tab |
| Cross-practice record links (incident→problem→change) | A: linked work items in automation recipes | B (module structure implies; not directly quoted) | A: practices named together, ITIL-certified | A: parent problem/parent change FKs on the incident |
| Knowledge base / known errors | A: KB (Confluence) + article suggestions | A: KB/Freddy | A: KB (Standard) | A: Known Errors Management module |
| Approvals / governed workflows | A: approval stages in workflows | A: auto-approvals named | A: change workflow builders | A: ITIL Change Management module lifecycle |
| Satisfaction measurement | A: CSAT surveys | B | A: user satisfaction field (iTop = this row's product; SDP quotes "happiness… level of service") | A: user satisfaction field on incident |
| Automation / routing / AI | A: automation rules; virtual agent | A: Freddy AI, intelligent routing | A: predictive intelligence, virtual agent, GenAI | (open-source core thinner; extensions exist — not asserted) |
| Reporting / operation-level measurement | A: reports/dashboards | A: insights | A: reporting + live dashboards | A: dashboards (referenced in docs tree) |
| Deployment poles | cloud | SaaS | on-prem + cloud | self-hosted open source |

Everything in the table is A-evidenced per product as marked; B rows are cross-product readings where only the pattern (not the sentence) was observed.

## Canonical Abstraction

### L0 — Defining Invariant (the smallest structure without which it is not ITSM)

Three jointly-held structures:

1. **The IT organization held as a service provider.** The record base is organized around services the IT organization provides to the organization: demand records are classified against defined service offerings (a service catalog or equivalent service-shaped classification), and the operation's commitments to its users are held as service levels. Remove it → a ticketing system / help desk with categories, nothing service-shaped; the "SM" in ITSM disappears.
2. **The service desk as the governed front door.** The organization's people submit requests and reports through managed channels (portal, email, and commonly chat/phone); each becomes a ticket/work record classified by service and type, worked by a support organization (agents/teams, queues, priority, lifecycle) under measured service-level targets. Remove it → practice tooling with no intake (change-management/configuration territory), not a service operation.
3. **The multi-practice operating system of record.** Beyond the desk, a set of interlinked governed practices operates on one shared record base: resolution practices (request/incident) plus control practices (problem, change, configuration/asset, knowledge/known-error) whose records reference each other and shared configuration/service records (incident → problem → change chains; tickets ↔ configuration items ↔ services). Remove it → any single-practice tool (the standalone incident/problem/change-management leaves), or a bare IT help desk.

Jointly-held is load-bearing:

- 1 alone = a service catalog/SLA documentation exercise, nothing processing demand
- 2 alone = an IT help desk / IT ticketing system (the market's own reduced pole — see ServiceDesk Plus Standard edition FAQ)
- 3 alone = standalone practice tooling (the §14 sibling leaves)
- 1+2 without 3 = IT service desk / help desk (a real product shape; the family's Standard-edition pole)
- 2+3 without 1 = ticketing machinery with modules but no service orientation (thin edge; no sampled product presents this way)
- 1+3 without 2 = no intake, no real product shape

### L1 — Common Mature Structure

- Self-service portal with a request catalog (request types/forms per offering)
- SLA machinery: targets per priority/type, business-hour calendars, breach/escalation states
- Knowledge base with article suggestions and deflection; known-error publication (problem practice output)
- Change workflows with approvals/authorization gates; release/deployment practice in fuller editions
- Problem management with known-error records and incident linkage
- Configuration/asset records (CMDB and/or ITAM) bound to tickets (impacted CIs, affected user's device)
- Multi-channel intake consolidation (email backbone; portal, chat, phone, widget)
- Automation rules (routing, assignment, notifications), virtual agents / AI assistance (era-current)
- CSAT at resolution; operation-level reporting/dashboards
- Queues/teams/agent role model; audit trail on records

### L2 — Variant / Optional Structure

- Practice-set depth: desk-only posture (ticketing + KB + SLA) through full practice stack (the edition ladders within one product line)
- Domain extension to non-IT departments (ESM posture — becomes the ESM Type when central), multi-instance/department segregation, MSP/service-provider catalog variants
- Estate-operations integration (on-call, alerting, event monitoring — the ITOM boundary)
- IT project management modules, purchase/contract management modules
- Deployment: cloud SaaS vs on-premises vs self-hosted open source
- Framework posture: explicit ITIL alignment/certification vs flexible "no-bureaucracy" positioning
- Provider vs single-company catalog models (contracts per customer)

### L3 — Vendor-specific (research notes only; excluded from the canonical document)

- Atlassian: Jira platform inheritance (work types, JQL, Confluence KB linkage, Opsgenie alerts/on-call, "Rovo"), space/project templates
- Freshworks: Freddy AI Copilot/Agent Studio/Insights naming, "Unified ServiceOps" branding, PeopleCert 14-practice accreditation
- ManageEngine: Zia, edition names, proprietary AI stack claims, on-prem data-center privacy posture
- iTop: delivery-model semantics, TTO/TTR naming, single-company vs provider module split, Combodo commercial wrap
- Analyst-category artifacts: Gartner MQ for ITSM Platforms placements (marketing context)

## Rejected Findings

- "ITSM = ITIL" — rejected as a definition. ITIL practice naming varies (v3 "processes" vs ITIL 4 "practices", 34 practices per Atlassian's guide); iTop ships "Simple" and "ITIL" change modules side by side; JSM markets anti-rigid-process philosophy. Framework alignment is positioning (L2), not structure.
- "ITSM = the service desk" — rejected. The desk is one leg; the market itself separates "service desk vs help desk vs ITSM" (Atlassian's own topic page) and vendors ladder editions where the desk-only pole is explicitly a reduced posture.
- "ITSM requires a formal customer-contract/SLA object model" — rejected as invariant. iTop formalizes it (SLA/SLT/contract objects); JSM realizes the same concept as SLA goals on request types; Freshservice/SDP as SLA policies. The invariant is service-level commitments on the record base, not any object schema.
- "ITSM includes ITOM (monitoring/alerting/automation of the estate)" — rejected as definitional; integration with ITOM is common but the estate-operations loop is the ITOM Type's core (per it-operations-management-itom pass), with ITSM as the ticket system it opens tickets into.
- Single-vendor features (AI copilots, project management modules, purchase modules) — not promoted.

## Boundary Findings

- **vs Ticketing System (§07)**: ticketing = context-free demand-record machinery (ticket + queue + lifecycle, no requester/service semantics required). ITSM = service-bound system of record: records classify against defined IT services, carry service levels, and interlock across practices. Confirmed from this side by ServiceDesk Plus's own FAQ (usable "solely as a ticketing system" in its Standard edition — the machinery pole sold inside the same family) and by the ticketing-system pass's advance flag (disciplined/process-framework machinery). Removal test both directions holds.
- **vs Help Desk (§07)**: help desk = the requester-serving single-practice application (correspondence loop, open→resolved→closed). ITSM contains a desk but adds the service-oriented record base and the multi-practice operation. The help-desk pass itself recorded that its internal-IT pole "shades toward ITSM service-shaped request types" — the seam is practice-stack depth + service orientation, not the correspondence loop.
- **vs standalone Incident/Problem/Change Management (§14)** — DISCHARGES three sibling joint-review flags. The expected suite-vs-practice seam is CONFIRMED: each practice pass documented its practice as "one governed practice/module inside the ITSM suite" (3/3 sampled products each); from this side, the suite is defined by the jointly-held three legs, and a standalone practice tool fails leg 1 or leg 3. Keep-both: the practice leaves have real standalone product shapes (practice-first tools) and the suite leaf has its own shape (the bundle). The practice documents' module-packaging observations are consistent with this pass's evidence (SDP PinkVERIFY practice list; iTop separate ticket modules; JSM packaged template categories).
- **vs ITOM (§14)**: ITOM = operations layer over the estate (discovery → consolidated operational picture → response loop), machine-originated signals. ITSM = human-originated demand and the governed practices that consume/produce records around services. The ITOM pass itself documented "open/update ITSM tickets" as the hand-off — the two Types interlock but neither contains the other's core.
- **vs CMDB (§14) / IT Asset Management (§14)**: record types inside the ITSM suite (L1 common) and standalone Types in their own right (both passes document "ITSM-suite module" as one product-shape pole). An ITSM product may bundle them; a CMDB/ITAM product is not an ITSM system.
- **vs Enterprise Service Management (§10)**: scope gradient, vendor-stated ("ITSM focuses on IT operations, ESM applies the same proven processes across other business departments" — ManageEngine FAQ, quoted in the ESM pass). ITSM = the IT-bound system of record (its practices are IT practices: incidents, changes, configuration, services); ESM = the same machinery generalized across internal departments. Keep-both on domain binding; the same products populate both (vendor expansion motion, confirmed on both sides). Flag carried for the joint review the ESM pass requested.
- **vs Employee Service Management / Employee Service Portal (§10)**: requester-population orientation (employee as service customer) vs provider-side practice stack; consistent with the §10 passes' recorded orientation gradient.
- **vs On-call Management / Status Page (§14)**: coverage machinery and stakeholder publication are adjacent surfaces (JSM bundles alerts/on-call; all four sampled suites integrate or bundle them) — not part of the defining core.
- **Historical / market-sample check**: passed. A 1990s/2000s IT department operating on paper or early software — service catalog listing offered services + response commitments, a help-desk call log with priority/assignment, incident/problem/change registers, an asset/configuration inventory, a known-error/KB binder — satisfies all three legs at analog level without ITIL v4 vocabulary, cloud, portals, or AI. The candidate definition names no framework version, no practice count, no channel set, no deployment model. Early LAN help-desk suites (call tracking + asset inventory + KB) satisfy a thin form; a bare call logger satisfies only leg 2 and is correctly excluded as the help-desk pole.

## Uncertainties

- ServiceNow (the archetypal enterprise pole) remains unreachable (timeout this pass; four prior sibling passes) — the enterprise-suite pole is characterized only indirectly (SDP customer quote naming it as the considered competitor; Gartner MQ category framing; sibling passes' practice-doc evidence). Enterprise-scale structural claims (e.g., universal CMDB federation, flow-based orchestration) are deliberately not asserted.
- The exact formalization depth of "service orientation" varies (formal SLA/contract objects vs request-type catalogs); the L0 phrases the concept, and the implementation spread is documented, but the lower bound (the thinnest service classification any ITSM-branded product enforces) was not exhaustively established.
- Whether any product sells the "1+3 without 2" shape (service catalog + practices, no desk) — none found; treated as no-real-product-shape.
- Wikipedia/ITIL-primary-source verification of the "34 practices" figure rests on Atlassian's concept guide (secondary); the figure is not used in the canonical document.

## Final Synthesis

IT Service Management software is the IT organization's service-management system of record: the system where IT is run as a service provider. Its defining core is three jointly-held structures — services as the organizing unit of the record base (offerings + service levels), a governed service desk turning the organization's demand into classified, SLA-measured work records, and a multi-practice operation (request/incident resolution plus problem/change/configuration/asset/knowledge control practices) whose records interlink on one shared base. Mature products add the portal/catalog self-service layer, knowledge deflection, governed change workflows, configuration/asset records bound to tickets, automation and AI. The type shades into neighbors on every flank — ticketing/help desk beneath it (machinery and the desk-only pole), standalone practice tools inside it (sold separately as their own Types), ITOM beside it (estate operations feeding it tickets), ESM beyond it (the same discipline generalized past IT) — and the removal tests above fix each seam.
