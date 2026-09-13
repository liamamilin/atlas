# FOI / Public Records Request Platform

## Overview

A **FOI / Public Records Request Platform** is a system of record for handling formal requests for access to records under freedom-of-information and public-records laws. It lets members of the public file a request that "reasonably describes" the records they seek, logs that request as a tracked record inside the receiving organization, coordinates the internal work of finding, reviewing, and redacting responsive records, and produces a formal disposition: the release of records (in whole or in part) or a recorded refusal.

The defining core is deliberately narrow:

```text
External requester
  ↓ files
Formal request record (description of records sought)
  ↓ tracked through
Managed processing lifecycle → acknowledged → worked → disposition
  ↓ ends in
Disposition centered on release of records (or recorded refusal)
```

Everything else commonly associated with these products — public intake portals, requester accounts, automated deadline calendars, fee and payment machinery, redaction tooling, proactive publication of released records, compliance dashboards — is standard market capability, not what makes the product this Type. The paper-era process (a written letter, a log book, a typed response) realizes the same four-part skeleton, and products that are modules of broader records or content-management suites carry the same skeleton inside a larger system.

When the deliverable is a completed service action rather than existing records, the product belongs to a service-request Type. When records are simply published with no per-request processing, it belongs to an open-data or transparency portal.

## Users & Context

**Requesters** are the external side: citizens, journalists, campaign groups, researchers, businesses, and other agencies. They are outside the organization's structure, may file occasionally or in high volume, and may decline to identify themselves at all. They care about how to file, what is required of them, what it will cost, how long it will take, and how to get the released records.

**Agency-side users** are the processing organization's staff:

- the public-records or FOI officer who owns the request queue, acknowledges requests, tracks statutory deadlines, and signs off dispositions;
- department coordinators and subject-matter staff who search their own systems for responsive records;
- legal counsel and reviewers who apply exemptions and decide what can be released, redacted, or refused;
- administrators who configure forms, fee schedules, departments, and reporting.

The work environment is a compliance function under a legal regime: requests arrive continuously, response deadlines are set by statute rather than by the agency's convenience, and volumes range from a handful of requests a month at a small municipality to continuous high-volume intake at large agencies — with body-camera video, email archives, and other bulky digital records now routine request subjects.

## Core Model

### The Defining Core

Four properties. Remove any one and the product is no longer this Type.

- **The formal request as a managed record.** Each request is an identified, persistent record: it carries the requester's description of the records sought, the date received, the applicable legal regime, and everything that happens to it. The request — not the underlying record, not a customer — is the object the platform manages. Without it there is only an inbox or a contact form.
- **An external requester distinct from the processing organization.** The requester is not an employee; they may hold an account, or be effectively anonymous. The platform binds responses to the requester-and-request pair, which is why anonymous requests can still be tracked and served through a retrieval key or link. Without this, the product is internal case management.
- **A managed lifecycle tracked to a formal disposition.** The request moves through acknowledged → in process → (clarification, extension, or fee events) → disposition, with status retained and visible to the staff — and, in most modern products, to the requester. Statutory deadlines and extensions are the characteristic implementation of this tracking. Without tracked progression, correspondence has no memory and compliance cannot be demonstrated.
- **A disposition centered on release of records.** The end state is delivery of records the organization already holds — in full, in part after exemption review, or a recorded refusal or no-records finding. The organization is generally not obliged to create new records, analyze data, or answer questions; the deliverable is existing documents, files, recordings, and correspondence. Without this, the product is a service-request or Q&A system.

### Standard Capabilities of Mature Products

These are common across the market and expected by buyers; they make the defining core practical.

- **Intake portal** — public web forms shaped to the agency's requirements, accepting submissions that would otherwise arrive by phone, email, or letter.
- **Requester self-service** — status views, personal request history for account holders, and download access to released files.
- **Anonymous intake with retrieval** — a way for unidentified requesters to submit and later reach their own request (typically a security key or unique link), because many laws do not require identity.
- **Correspondence threads** — acknowledgements, clarification requests, fee notices, and extension letters kept inside the request record rather than in personal inboxes.
- **Deadline and extension machinery** — the statutory clock, computed from the regime's rules, with escalation when due dates approach or lapse.
- **Routing and collaboration** — assignment to departments, delegation of subtasks, and consolidation when several departments hold parts of one response; some mature products also group sub-requests and partial installments under a single original request.
- **Responsive-records gathering** — tools to extract, de-duplicate, and search email archives, and to handle large video and audio files, so "any and all" requests can be worked across agency systems.
- **Review and redaction** — annotation of exempt material, redaction of personal information, and audit trails that make the decision defensible; AI-assisted redaction is increasingly common in the commercial market.
- **Fees** — estimation, itemized invoicing, and payment acceptance where the regime allows cost recovery.
- **Secure release** — delivery of responsive records as tracked downloads or expiring links that stop working rather than circulate freely.
- **Deflection and proactive publication** — libraries of already-released records matched against incoming searches, proactive posting of high-interest records so no request is needed, and detection of duplicate or similar requests so they can be answered together.
- **Reporting** — volumes, timeliness, and disposition statistics, aligned to the annual reporting that many access-to-information regimes require of agencies.

### One Structure, Many Implementations

```text
Concept:  Formal request record
Realized as:   portal form submission, emailed letter logged by staff,
               a public request page with a permanent address

Concept:  Requester identity
Realized as:   registered account, email address, anonymous request
               paired with a retrieval key

Concept:  Statutory clock
Realized as:   configurable deadline calendars per regime, escalation
               triggers, overdue status shown to requester and staff

Concept:  Disposition / release
Realized as:   tracked download links, published file pages, postal
               delivery of paper records, a refusal notice with reasons
```

A reader who has only seen one implementation should still recognize the others: the defining core is the request-lifecycle skeleton, not any portal, account, or link mechanics.

## How It Works

### The request lifecycle (the primary loop)

```text
Requester submits a request describing the records sought
→ platform logs it as an identified record (requester + scope + regime)
→ agency acknowledges receipt and starts the statutory clock
→ clarification requested if the description is insufficient
→ routed to departments that may hold responsive records
→ records gathered, de-duplicated, reviewed for exemptions
→ exempt material redacted; non-exempt material segregated for release
→ fee estimate issued and paid where applicable
→ disposition: full release / partial release / refusal / no records
→ records delivered; disposition and timing recorded for reporting
```

Two features of this loop distinguish it from generic work management. First, the timing is externally imposed: the platform's deadline machinery exists because the law, not the agency, sets the response window, and extensions must be justified and recorded. Second, the work is asymmetric: the requester need not justify why they want the records; the agency must justify why it withholds any of them.

### The requester's loop

```text
Check whether records are already published
→ file the request (account, email, or anonymously)
→ receive acknowledgement with a tracking reference
→ respond to clarification or fee requests
→ watch status change; receive the released records
→ (where dissatisfied) pursue review or appeal
```

Status visibility is a defining user experience in modern products: requesters no longer call to ask where their request stands. Anonymous requesters reach the same visibility through their retrieval key rather than an account.

### The publication loop

```text
Records released in response to requests (or flagged high-interest)
→ added to a reusable release library / posted proactively
→ future requesters find them by search or tags — no new request needed
→ duplicate incoming requests detected and answered from the library
```

Many access-to-information laws affirmatively require proactive posting of frequently requested records, so this loop is not a marketing extra; it is the pressure-relief valve that keeps request volume survivable. Its extent is a variant: some implementations publish only the released records, others publish the request thread and correspondence as well.

## Interfaces

### Requester portal

The public surface of the platform.

- Purpose: file requests, track their progress, receive records.
- Typical information: intake forms with guidance on required descriptions, legal notices the agency must display, status labels and dates, fee invoices, download pages for released records, searchable libraries of previously released material.
- Primary actions: submit a request, create or use an account, check status, pay a fee, download records, search published records, request internal review where offered.

### Agency processing console

The staff surface — the operational heart of the Type.

- Purpose: work the request queue to compliant dispositions.
- Typical information: request queue with age and due-date columns; request detail showing the description, requester, correspondence, deadline state, assigned departments, and attached evidence; review workspaces for marking and redacting exempt material; audit history of every action.
- Primary actions: acknowledge, request clarification, assign and reassign, delegate sub-requests, log searches performed, apply exemptions, redact, compute and send fee estimates, extend the deadline with a recorded reason, release, refuse, close.

### Public archive / release library

The transparency surface.

- Purpose: make already-released material reusable and reduce repeat requests.
- Typical information: released records organized by topic, tags, or request type; in the fully-public pole, the requests and correspondence themselves.
- Primary actions: search, browse, download, subscribe to updates on topics of interest.

### Reporting / compliance views

- Purpose: demonstrate and manage compliance.
- Typical information: open and overdue counts, timeliness against statutory windows, volume by department and request type, disposition breakdowns.
- Primary actions: filter, drill into requests, export for statutory reporting.

## Important Rules / Behaviors

- **The clock is statutory.** Response deadlines come from the applicable law, and they vary by jurisdiction and by request complexity. Platforms therefore treat deadlines as configuration, not hard-code — the same product serves regimes with different windows, extension rules, and business-day conventions. Overdue status, escalations, and requester-facing due dates are all derived from that configuration.
- **The requester owes no justification.** A request only needs to reasonably describe the records sought; motivation is irrelevant. Requests can be valid without any requester identity at all.
- **The agency owes no creation or analysis.** There is no obligation to generate new records, conduct research, or answer questions — only to find and release (or withhold with reasons) what exists.
- **Withholding requires recorded reasons.** Exemptions protect defined interests (personal privacy, law enforcement, security, and similar); the characteristic discipline is to segregate and release what can be released, redact the rest, and document why. This is why redaction tooling and audit trails sit inside the request record rather than in side documents.
- **Identity is handled carefully on both sides.** Requester identity may be protected (anonymous intake exists for a reason), and released records are screened for personal information about third parties. The fully-public publication pole adds a further rule set: hiding or demoting requests that contain private or improper material is a standing moderation duty.
- **Release is secured, not broadcast.** Links to responsive records are tracked and commonly expire, because released packets routinely contain sensitive material even after redaction.
- **Every action is attributable.** The audit trail is not bureaucracy for its own sake: agencies must be able to defend their handling in reviews, appeals, and oversight — what was searched, who decided what, and when the clock was moved and why.

## Variants

- **Operator pole.** Most products are bought by the agency and process requests from its side. The other pole is the requester-side public platform, operated by an intermediary or civil-society organization, which files requests on citizens' behalf with many authorities and archives the results publicly. The lifecycle skeleton is identical; the philosophy differs.
- **Publication posture.** Records-only publication (the released documents go online; request threads stay private) versus the full public archive (requests, correspondence, and responses all published by default, with moderation to hide private or improper material).
- **Legal regime and locale.** FOIA in the US federal context, state and local public-records acts, freedom-of-information and environmental-information regimes elsewhere; each brings its own deadlines, exemptions, fee rules, and appeal routes. Mature platforms configure to the regime; request states and deadline arithmetic are jurisdiction-shaped, and exact labels vary by product.
- **Segment and scale.** Municipal and county offices, state agencies, school districts, public-safety organizations (high-volume, video-heavy requests with heightened security postures), and special districts each tune the same machinery.
- **Records mix.** Email-archive extraction and large video/audio redaction dominate in some deployments; paper files and correspondence in others.
- **AI depth.** AI-assisted redaction and automated email processing are common in current commercial products and absent from older and open-source generations.
- **Packaging.** Standalone product, member of a government-operations suite, or a module of a records-management / content-management platform — the request-lifecycle core is the same in all three.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Government Records Management | adjacent, complementary | governs the lifecycle of the agency's own records (retention schedules, disposition); this Type manages *requests* for records — remove the external requester and the request machinery, and you are in records management |
| Government Open Data Portal | overlapping on publication | proactively publishes datasets with no per-request processing, no requester relationship, and no deadlines; remove the request lifecycle and this Type becomes an open-data portal |
| Government Transparency Portal | overlapping on publication | publishes performance, agenda, and financial information; no exemption review and no requester; a transparency portal hosting released records is sharing capability, not the same Type |
| 311 / Citizen Service Request Platform | adjacent | service requests seek an *action* (repair, inspection); records requests seek *existing records*; the disposition object differs structurally |
| Ticketing / Case Management (generic) | implementation fallback | shares queue/assign/status mechanics but lacks the statutory clock, the exemption discipline, the external-requester identity model, and the records-release disposition |
| Government Service Portal | container | the citizen's front door to many services; records intake may be embedded in it, but the processing console — not the front door — is this Type's center |
| eDiscovery / Legal Matter tooling | capability donor | shares search, review, and redaction techniques, but is matter-scoped litigation work rather than standing public access |

The load-bearing boundary is the pair of questions: *who is asking, and for what?* An external party asking for existing records under a statute — tracked to a recorded disposition — is this Type. An employee asking a colleague, or a citizen asking for a pothole repair, is not.

## Representative Products

- **Granicus Records Request Management (GovQA)** — commercial market leader on the agency side; US state/local government, public safety, schools; compliance automation, deflection, and secure release at scale.
- **JustFOIA (MCCi)** — commercial SaaS at the local-government pole; intake forms, correspondence, workflow automation, redaction, payments, and a self-service public portal.
- **Alaveteli / WhatDoTheyKnow (mySociety)** — open-source platform at the requester-side pole, deployed internationally; requests are filed by the public and archived openly with the full correspondence.

## Sources

Research date: **2026-09-07**

- Granicus — Records Request Management (GovQA) product page: https://granicus.com/product/records-request-management-govqa/ ; GovQA × Veritone Redact announcement: https://granicus.com/blog/govqa-and-veritone-forge-strategic-relationship/
- JustFOIA — product site and Public Portal feature page: https://www.justfoia.com/ ; https://www.justfoia.com/product-features/public-portal/
- Alaveteli (mySociety) — documentation: About https://alaveteli.org/about/ ; Request states https://alaveteli.org/docs/customising/states/ ; Managing requests https://alaveteli.org/docs/running/requests/
- FOIA.gov (U.S. Department of Justice; statutory context, not a product): What is FOIA https://www.foia.gov/about.html ; How to make a FOIA request https://www.foia.gov/how-to.html

> Sourcing limitation: the NextRequest product (planned fourth sample) was unreachable — its site, code repository, and deployment portals returned timeouts or access-denied responses — so it is not relied on anywhere in this document. Agency-side operator documentation for GovQA (help-center depth) was not reachable in this pass; its evidence is from official product pages, so agency-internal workflow details are described at capability level rather than screen level. Jurisdiction-specific statutory windows (deadline day counts, fee schedules, exemption lists) are intentionally not stated; they vary by regime and were not the object of this research.
