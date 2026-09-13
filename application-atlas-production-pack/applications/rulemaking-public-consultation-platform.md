# Rulemaking & Public Consultation Platform

## Overview

A **Rulemaking & Public Consultation Platform** is the institution-side system of record for running formal public consultations and rulemaking procedures. A government body — an agency, department, local authority, or planning organization — uses it to publish a proposal or draft instrument, operate a bounded public input window against that proposal, hold the input it receives on the procedure's record, and record and publish how the input was handled and what was decided.

The defining structure is small:

```text
Consultation / rulemaking procedure (the institution's container of record)
└── Published proposal + supporting materials
    └── Bounded public input window (structured channel, attributed input)
        └── Disposition recorded back on the record (response, decision, outcome)
```

Everything else commonly associated with these products — online question forms, AI-assisted comment analysis, publishing individual responses, participant accounts, maps, moderation — is widespread in current products but is not what makes the product a consultation platform. A consultation run through a gazette notice with written submissions and a published response report satisfies the same structure without any of that machinery.

When the system's only object is a public-input campaign — a petition or a standalone comment period with no procedure around it — the product belongs to a neighboring type (Petition / Public Comment Platform). When the system is a composed space for ongoing community engagement (ideas, debates, participatory budgeting), it is a Civic Engagement Platform.

## Users & Context

**Primary users are institution staff** who are responsible for running the procedure:

- **policy / consultation officers** — design and publish the consultation, draft the questions or open the comment channel, and write the response
- **rulewriters / program staff** — prepare the draft instrument (proposed rule, policy, plan) and the supporting materials
- **analysts** — tag, categorize, and interpret the input; produce summary reports
- **program / portfolio managers** — oversee the set of consultations across the organization, check that procedures are closing the loop

**Secondary users:**

- **legal / compliance roles** in statutory contexts, where notice, comment windows, publication of responses, and record-keeping are legal obligations
- **communications teams** who promote the consultation and manage respondent communications

**The consulted public** is the other side of every procedure: people and organizations who find the consultation, read the proposal, and submit input during the window. They typically need no account; where accounts exist, they serve attribution, consent, and follow-up.

The work context is formal and deadline-driven: consultations are announced, run for a stated period, close on a date, and must produce a recorded outcome. In statutory settings the procedure itself is defined by law, and the platform's record may be subject to public-inspection and records obligations.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a consultation/rulemaking platform:

**1. The procedure as the institution's unit of record.**
A consultation platform's world is organized around persistent, individually identified containers — a consultation, an engagement project, a draft-document review, a rulemaking filing or docket. Each container is bound to one specific proposal or draft instrument, holds the procedural materials (the draft text, supporting documents, notices), carries an owner and a lifecycle, and persists after closure as the institution's record of what was consulted on and what happened. Without the container, input is just a pile of form submissions; with only the container and no public window, it is an internal records system.

**2. The institution-operated public input window.**
The institution publishes the proposal — an overview with introductory text, supporting documents, and a clear call to participate — and operates a structured input channel against it during a bounded, date-driven window. The channel takes different shapes: a question form or survey, an open comment submission, in-context comments attached to the draft document itself, or input captured at meetings and imported from letters and email. Input is attributed (named or anonymous, by design), retained on the procedure's record, and accepted only while the window is open. Without the window there is no public consultation; without the bound to a published proposal there is only an open feedback wall.

**3. The disposition recorded back on the record.**
After the window closes, the institution's handling of the input is recorded on the procedure: the input is reviewed and analyzed, a response or decision is produced, and the outcome is published back on the procedure's record — a results report, a "we asked / you said / we did" summary, a response to comments, or, in rulemaking, the final instrument and its effective date. This closes the procedure. Without it, the system is a submission collector; the consultation loop never closes and the "consultation" in the name is hollow.

### What Mature Products Add

Modern products commonly carry most of the following. They make the platform practical, but a product lacking them can still be a consultation platform:

- **structured question forms** — question types, required questions, skip logic, embedded media and maps
- **in-document commenting** — comments attached to specific passages of the draft, not just to the procedure as a whole
- **analysis tooling** — tagging and categorization of responses, filtering and grouping, quantitative and qualitative views, exports and generated summary reports; increasingly AI-assisted (for example first-pass theme analysis, sentiment and text classification, or transcription and import of offline input)
- **response publishing** — publishing individual submissions on the public record, moderated and redacted, with respondent consent captured before publication
- **moderation** — human and/or automated vetting of public discussions
- **participant registration and profiles** — optional identity layer for attribution, consent, and follow-up
- **communications** — confirmations, notifications, and updates to respondents
- **archives and portfolio views** — libraries of past consultations and organization-wide dashboards showing which procedures have published outcomes
- **timelines and phases** — visible milestones for multi-stage procedures
- **accessibility and translation** — WCAG-class conformance and multi-language operation

### One Structure, Many Implementations

The core is written in conceptual terms; products realize each concept differently:

```text
Concept:   procedure container
Realized as:  consultation activity (with type templates and phases)
              engagement project inside an engagement hub
              draft-document review (the document is the container)
              rulemaking filing / docket entry (the legal record)

Concept:   input channel
Realized as:  question form / survey
              open comment submission
              in-context annotation on the draft
              meeting testimony and imported letters/email

Concept:   disposition
Realized as:  published results report
              "we asked / you said / we did" summary
              response to comments
              final rule + effective date + codification
```

A reader who has only seen one shape — say, a government department running an online policy consultation — should still be able to recognize a state agency's rulemaking docket or a planning department's annotated draft review as the same type.

## How It Works

### The institution-side loop

```text
Prepare
→ draft the proposal / instrument, assemble supporting materials
→ configure the input channel (questions, comment form, document annotation)
→ set the window (open and close dates)

Publish / give notice
→ publish the procedure's public page
→ (statutory contexts) issue formal notice through official publication channels

Collect
→ the window opens automatically on the start date
→ input arrives through the configured channel, attributed, retained on the record
→ staff monitor volume and respond to questions

Close
→ the window closes automatically on the end date
→ the public page switches from "participate" to "what happens next"

Analyze
→ tag and categorize responses; quantify and read qualitatively
→ (commonly) AI-assisted first-pass analysis; offline input imported and merged

Dispose
→ record the response / decision on the procedure
→ publish the outcome on the record (results report, response summary,
   final instrument and its effective date)
→ optionally publish individual responses, moderated and consent-checked

Archive
→ the procedure's record persists as the institution's archive
→ portfolio views show which consultations closed the loop
```

### The public side

```text
Find the consultation (listing, search, notification)
→ read the proposal: overview, supporting documents, timeline
→ submit input while the window is open (form, comment, in-document annotation)
→ (optionally) give consent and see published responses
→ return after closure to see the outcome
```

### The statutory realization

In jurisdictions where rulemaking is legally defined, the same loop is carried by legally typed records. A typical statutory flow: the agency files a typed instrument (for example a proposed rule, a change to a proposed rule, or an emergency rule); the filing passes procedural review; it is published in the official bulletin or register with its comment dates; a minimum comment period runs; the agency then reviews the comments received; and the procedure closes with an effective-date notice and codification of the final rule. The platform (often government-operated) holds the filing record and its history, the public register or docket of filings, and the public portal over both. The exact filing types, review chains, and day counts are jurisdiction-specific and vary widely.

## Interfaces

### Institution side

**Portfolio dashboard**
The staff entry surface: the organization's consultations and filings with their status (forthcoming / open / closed), response counts, and outcome-publication state. Primary actions: create a procedure, open one for editing, check closure across the portfolio, export lists.

**Procedure builder**
Where a consultation is assembled: the overview page (introductory text, related documents and links, embedded content), the input channel (question pages with types and skip logic, comment settings, document upload for annotation), the window dates, visibility (public or private to a stakeholder group), and ownership. Primary actions: add and arrange content, set dates, preview, publish.

**Response analysis workspace**
The analyst's surface over the collected input: responses listed individually and by question, tagging and categorization, filtering and grouping, quantitative charts and qualitative reading, analyst-only fields (in some products), exports and generated summary reports. Primary actions: tag, filter, exclude or remove responses, export, generate a report.

**Outcome publishing**
Where the disposition is recorded and published: upload or write the results report, fill a structured response summary (what was asked / what was said / what was done), and optionally publish individual responses after moderation and redaction. Primary actions: publish results, publish response summary, moderate and redact individual responses.

**Filing workspace (statutory variants)**
In government-operated rulemaking systems: a work queue of filings, typed filing forms, and the filing's history; on the public side, the register/docket of filings and the code or rules portal.

### Public side

**Consultation finder**
The listing of open, forthcoming, and closed consultations, searchable and filterable. Primary actions: find, view.

**Procedure page**
The consultation's public face: introductory text, supporting documents, timeline or phases where used, and the call to participate — an invitation to give views while open, the opening date while forthcoming, and outcome information once closed. Primary actions: read materials, participate.

**Input surface**
The question form or survey, the comment submission, or the annotated document with in-context commenting. Primary actions: answer, comment, attach, submit.

**Outcomes pages**
Published results, response summaries, and (where enabled) individual published responses — often aggregated in a site-wide "outcomes" section across consultations.

## Important Rules / Behaviors

**The window is a date-driven state machine.** A procedure moves forthcoming → open → closed on its published dates — in online products automatically, without staff intervention. Input is accepted only while open, and the public page changes its call to participate at each transition.

**Editing a live procedure is restricted.** Published and open procedures carry warnings and limits on editing, because the published proposal is the thing the public is responding to; changing it mid-window undermines the record.

**The comment process is not a vote.** Input is weighed by substance, not counted. A single well-supported comment can matter more than a thousand identical form letters — guidance that rulemaking authorities publish almost verbatim. Count-based semantics (thresholds, most-supported-wins) belong to petition mechanics, not consultation analysis.

**Attribution and consent govern publication of input.** Input may be anonymous or identified by design. Publishing individual responses requires respondent consent (captured in-product), moderation, and redaction of personal or inappropriate content. Some consultation types — planning consultations are the common case — carry a statutory duty to publish the submissions received.

**The record is retained and commonly public.** The procedure's record — proposal, materials, input, disposition — persists after closure and, in statutory contexts, is explicitly available for public inspection; it is also the substrate for records-request obligations.

**Statutory machinery binds where it applies.** Mandated notice channels, minimum comment periods, hearing triggers (including hearings required on request), review chains, and codification are legal requirements in rulemaking jurisdictions. They shape the platform's states and deadlines but are jurisdiction-specific; advisory consultations run without any of them.

**Multi-channel input is normal.** Formal comment is not form-bound: comments arrive at meetings, by email, and as long documents with attachments. Mature platforms import and consolidate such offline input so the analysis covers the whole record, not just the web form.

## Variants

- **Statutory rulemaking systems** — government-operated, filing/docket-centric, carrying legally typed instruments, official publication, mandated comment windows, and codification. The binding-instrument pole of the type.
- **Policy and legislative consultations** — departments consulting on policy development, legislation research, and calls for evidence; advisory posture, outcome is a response report or policy decision.
- **Planning, permitting, and infrastructure consultations** — statutory publication duties (e.g., planning consultations required to publish submissions), often place-based with maps and phased timelines.
- **Plan / policy document reviews** — document-centric: comments attached in context to draft plans and designs, continuing through adoption into implementation tracking and plan libraries.
- **Stakeholder and internal consultations** — private procedures run with restricted visibility for work groups, committees, or staff.
- **Deployment variants** — multi-tenant SaaS used across many institutions vs single-government operated systems built around that jurisdiction's statutory process.

A variant stays a variant while the defining core applies. When the object stops being a procedure bound to a published proposal — a signature campaign, an always-open ideas wall, a measurement survey — a different type has begun.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Petition / Public Comment Platform | closest sibling | the public-input **campaign** is the only object and the platform is the participation venue; here the **procedure** is the container — the system of record holds the draft instrument, the analysis machinery, and the lifecycle from drafting through disposition to archival |
| Civic Engagement Platform | adjacent | composed spaces for ongoing engagement (ideas, debates, participatory budgeting, assemblies) with consultation as one mechanism; here the formal procedure is the whole system |
| Survey Platform | adjacent | a private measurement instrument over a respondent sample; here a public procedure of record with an institutional decision context and a published disposition |
| Legislative Tracking Platform | opposite stance | the external watcher's mirror of lawmaking, which neither authors nor advances; here the institution operates the record itself |
| Government Meeting / Agenda Management | adjacent | hearing and meeting comment capture is meeting-centric (the meeting is the record); here the procedure is the record and meetings are one input venue |
| FOI / Public Records Request Platform | opposite flow | the public requests records the institution holds; here the institution collects input from the public — both produce public records, with different objects |
| Regulatory Change Management | different side | organizations tracking regulatory obligations written elsewhere; here the institution writing those obligations |
| Government Transparency Portal | adjacent | publishes institutional records for inspection; here the system operates the procedure whose record transparency portals may later expose |

The boundary with the Petition / Public Comment Platform is the most important one, because an institution-initiated comment period can look like both. The structural test: is the campaign the whole system, or one phase of a managed procedure the system also holds before and after?

## Representative Products

- **Delib Citizen Space** — consultation and engagement SaaS used by central departments, local authorities, and agencies (UK-origin, international); the end-to-end consultation-management pole
- **Granicus EngagementHQ** (marketed as Sentiment & Feedback) — engagement-hub platform for local and state government (AU-origin, global); the omnichannel engagement pole
- **Konveio** — document-centric engagement platform for plans and policies, used by local governments, state agencies, and planning consultants (US); the in-document-annotation pole
- **Utah eRules / Administrative Rules Register** — a government-operated statutory rulemaking system (US state); the filing-and-docket pole
- **Regulations.gov** (US federal eRulemaking) — the canonical federal notice-and-comment portal; treated as a market anchor only (see Sources)

## Sources

Research date: **2026-09-09**

- Delib — Citizen Space product page: https://www.delib.net/citizen_space
- Delib Knowledge Base: https://help.delib.net/ — including "Activity types", "The status of your activity — Open, Closed and Forthcoming", "Publishing results and outcomes", "Response publishing — what is it?", and the "Creating and managing activities", "Analysis and reporting back", and "Response publishing" sections
- Granicus — Sentiment & Feedback (EngagementHQ): https://granicus.com/product/sentiment-feedback-engagementhq/ ; product directory: https://granicus.com/products/
- Konveio: https://konveio.com/
- Utah Office of Administrative Rules — "eRules Help", "Rulemaking Process – The Basics", "Participate in Rulemaking": https://rules.utah.gov/help/

> Sourcing limitation: Regulations.gov (the US federal eRulemaking portal) returned HTTP 403 on every attempt across two research passes and was not reachable; PublicInput returned 403 twice; the EU "Have Your Say" portal renders only via client-side scripting and yielded no content. These are held as market anchors only. No operational detail for them is stated in this document, and claims about the statutory pole are calibrated to the state-level system that was directly observed. Precise numeric limits, day counts, and vendor-specific feature names are recorded in the paired Research Notes rather than asserted here.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis (including the joint review with the petition/public-comment leaf) are recorded in the paired Research Notes.
