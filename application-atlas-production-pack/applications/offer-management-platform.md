# Offer Management Platform

## Overview

An **Offer Management Platform** is the system of record for employment offers at the end of the hiring funnel. It manages the offer as an object in its own right: a specific candidate is bound to a specific position under proposed terms, the offer is authorized internally, extended to the candidate as a formal offer document, and the candidate's response — acceptance, decline, or non-response — is recorded as the offer's outcome.

Its purpose is to make the transition from "selected candidate" to "hired" controlled and traceable. The problems it exists to solve are concrete: offers carrying inconsistent or unauthorized terms, lost track of which offers are out and with whom, approval steps handled over email with no record, and signed offer letters buried in inboxes instead of attached to the candidate's file.

The defining core is deliberately small — two structures held together:

```text
The offer of record
  (candidate × position × proposed terms × lifecycle state)
        +
The extend-and-respond loop
  (offer document extended to the candidate
   → response recorded back as the offer's outcome)
```

Everything else commonly associated with offers — approval workflows, e-signature, templates, expiration windows, requisition and budget linkage — is standard capability that mature products add, not what makes the application what it is. Where the surrounding surface becomes the candidate pipeline as a whole, the product is an Applicant Tracking System; where the surface is what happens *after* acceptance, it is Employee Onboarding.

## Users & Context

Primary users (inside the hiring organization):

- **Recruiter / talent acquisition** — the operator. Creates the offer from the candidate's profile at the offer stage, fills in the offer details, generates the offer document, sends it, and tracks its status through approval and response. Owns the day-to-day queue of open offers.
- **Hiring manager** — reviews and approves the offer's terms (compensation, start date, benefits); in smaller setups may also create and send the offer directly.
- **Approvers** — managers, HR/compensation staff, or finance, depending on the organization. Receive the offer for review with its details visible, then approve or reject it, with a reason when rejecting.

Secondary users:

- **HR / recruiting operations** — configures offer templates, offer fields, and approval flows; manages permissions around who may see salary data and who may send or cancel offers.
- **Candidate** — the one external participant. Receives the offer document, reads it, signs or otherwise accepts it, declines it, or lets it lapse.

The work context is the offer stage of a hiring process: the candidate has been selected, terms are being settled, and the organization needs one governed channel between "we want to hire this person" and "this person has said yes." Offers are sensitive — they contain compensation — so visibility control is part of the context, not an afterthought.

## Core Model

### The Offer of Record

The center of the system is the **offer**: a persistent, individually identified record that binds together:

- **the candidate** — one specific person, usually arriving from the recruiting pipeline;
- **the position** — the job or requisition the offer is for, anchoring role, location, and often the requisition's approval history and budget;
- **the proposed terms** — the employment terms being offered, held as structured data: compensation, start date, work location, reporting line, benefits, and organization-specific fields. Some fields are internal-only (visible to staff, never shown to the candidate);
- **the lifecycle state** — where the offer stands: being prepared, awaiting approval, sent and awaiting response, accepted, declined, withdrawn, or expired;
- **the accumulating record** — the offer's documents (generated letter, signed copy), its approval trail (who approved and when; rejections and their reasons, where the product captures them), and its revision history.

An offer is not just a document; the document is one output of the record. The same offer record can produce a letter, route it for approval, receive a signature, and feed the result back into the hiring pipeline.

### The Extend-and-Respond Loop

The second defining structure is the loop that takes the offer to the candidate and brings an answer back:

```text
Offer record created (candidate × position × terms)
   → [internal authorization, when configured]
   → offer document extended to the candidate
   → candidate response
        ├── accepted / signed  → offer resolved as accepted; candidate moves toward hire
        ├── declined           → offer closed, reason recorded
        ├── no response        → offer lapses or expires
        └── withdrawn          → offer canceled by the organization
```

The loop is what distinguishes this application from both an internal approval tool and a document generator: the offer leaves the organization, and its external response becomes the record's outcome.

### Structure Without Fixed Implementation

The core is conceptual, and mature products implement it differently:

```text
Concept:   offer document production
Examples:  uploaded letter template with fill-in tokens; wizard-driven
           document generation; in-system template editor

Concept:   extending the offer
Examples:  email with the document attached; link to a signing surface;
           manual send outside the system with the signed copy uploaded back

Concept:   response capture
Examples:  integrated e-signature; candidate email reply marked by staff;
           status updated by hand
```

A reader who has only seen one implementation — say, a wizard that generates a PDF and routes it through an e-signature provider — should still be able to recognize the older pattern (typed letter, emailed PDF, manually marked "accepted") as the same application.

### Capabilities Around the Core

**Standard capabilities** — found across the researched products and expected in any mature implementation:

- offer document templates with fill-in variables, producing candidate-facing letters (typically as PDF) from the offer's structured details
- internal approval machinery for offers that require it: designated approvers or approver groups, sequential or parallel review, notifications with the offer's details visible to approvers, approve/reject with a reason, and the approval trail kept on the offer record
- offer status tracking on the candidate's profile, with the offer's details and documents attached
- permission separation: who can view offer details (especially salary), create offers, send them, approve them, and cancel them
- revision handling: a corrected or renegotiated offer supersedes the previous version, and a changed offer typically has to pass approval again
- reporting over offers: status, creation and sent dates, resolution dates, approvers

**Optional capabilities** — present in some products or configurations:

- e-signature collection built in or through integrated signing providers
- offer expiration windows, after which the candidate can no longer accept
- withdrawal (cancel) of an offer, in some products even after the candidate accepted
- linkage to requisitions and headcount: selecting a requisition when creating the offer, offers feeding budget or hiring-plan reporting, a withdrawn offer reopening the requisition
- bulk offer creation for high-volume hiring
- a company signatory who must sign the offer before the candidate sees it

## How It Works

### Settle terms and create the offer

The candidate has been chosen and moved to the offer stage. The recruiter (or hiring manager) opens the offer from the candidate's profile and enters the offer details — compensation, start date, location, and whatever else the organization tracks. The details are saved as the offer record; at this point the offer exists as data, before any document does.

### Route for internal approval (when required)

If the organization requires offer approvals, the offer is submitted and its approval status becomes pending. Designated approvers are notified and can see the offer's details — including compensation — and either approve or reject. A rejection — where the product supports one — asks for a reason, which is shown to the offer's creator, who revises and resubmits; a materially changed offer goes through approval again. Once the required approvals are in, the approval date is recorded on the offer. Where no approval is required, the flow skips straight to extension. Some products also short-circuit self-approval: a person who set up the offer is not asked to approve their own numbers.

### Produce and extend the offer document

The approved offer details are merged into an offer template — the organization's standard offer letter with fill-in spots for the candidate's name, position, salary, start date, and the rest. The system generates the candidate-facing document (typically a PDF), the recruiter reviews it, and it is sent to the candidate by email, often with a link to sign electronically. Some organizations instead send documents produced outside the system and upload the signed copy back, which the application supports by attaching it to the offer record.

### Record the response

The candidate's action lands on the offer record:

- **Signed / accepted** — the status updates to accepted, the signed document is archived on the candidate's profile, and the recruiting record moves forward (the candidate is marked hired or moved to the next stage, handing off to onboarding).
- **Declined** — the status updates to declined; products that capture it record the candidate's stated reason on the candidate's timeline.
- **Expired** — if the offer carried an expiration and the candidate did not respond in time, the offer can no longer be accepted; a fresh offer must be issued.
- **Withdrawn** — the organization cancels the offer; the candidate is informed if it is still pending with them, and downstream effects follow (for example, reopening the requisition the offer consumed).

### The recurring loop

Across many openings, the same cycle repeats: details → approval → document → response → disposition. The offer stage becomes a managed queue — which offers are drafted, which are stuck in approval, which are out with candidates, which were declined and why — visible per candidate and in aggregate through offer reports.

## Interfaces

### Candidate profile — offer panel

The operator's main surface, reached from the candidate's record at the offer stage.

- Purpose: create and manage this candidate's offer.
- Typical information: offer details (compensation, start date, location), approval status and approver trail, offer status, generated and signed documents.
- Primary actions: create offer, request approval, generate/send offer document, upload signed document, cancel or revise, mark hired.

### Approval queue / inbox

The approver's surface.

- Purpose: review offers awaiting authorization.
- Typical information: the candidate, position, and full offer details (salary included), plus who has already approved.
- Primary actions: approve or reject (with a reason, where the product captures one), view the approval trail.

### Template and workflow configuration

The administrator's surface.

- Purpose: govern how offers are produced and gated.
- Typical information: offer letter templates with their variables, offer fields, approval flows (approvers, order, scope), permissions.
- Primary actions: create/edit templates, configure approval flows, set who may view salary data or perform offer actions.

### Candidate-facing offer surface

What the candidate sees: an email carrying the offer document (or a link to it), and — where e-signature is used — a signing view showing the document with signature fields, accept and decline controls, and the resulting downloadable signed copy.

### Offers reporting

The manager's surface.

- Purpose: see the offer funnel in aggregate.
- Typical information: offers by status, sent and resolution dates, approvers, declines.
- Primary actions: filter, export, drill into an offer.

## Important Rules / Behaviors

- **The offer is gated before it leaves.** Where approvals are configured, the offer document cannot go to the candidate until the required approvals are complete. A rejection is recorded back to the offer's creator — with a reason, where the product captures one — and a revised offer re-enters the gate. Where approvals are not configured, sending is immediate — the gate is governance, not a technical precondition.
- **One active offer per candidate and position.** Issuing a corrected or renegotiated offer supersedes the previous version; the older document becomes inactive and only the current version shows on the record. Approvals attach to the version they cleared.
- **The response is a recorded state, not an anecdote.** Accepted, declined, withdrawn, and expired are statuses on the offer, with timestamps and — for declines — reasons where captured. The signed document is archived against the offer.
- **Compensation visibility is permissioned.** Offer details, especially salary, are visible only to roles granted that visibility; approvers see them by necessity, general pipeline users may not.
- **Withdrawal has consequences.** Canceling an offer is recorded on the offer itself; a candidate whose offer is still pending may be notified, depending on the product. In requisition-driven organizations, the cancellation may release the requisition the offer held. Withdrawal is possible at several points in the lifecycle; some products allow it even after acceptance.
- **Acceptance is a handoff, not an end.** An accepted offer moves the candidate forward (marked hired or moved to the next stage) — the point where Employee Onboarding takes over.

## Variants

- **Packaging** — the dominant market shape is offers as a first-class stage or section inside an Applicant Tracking System, and as a named module in enterprise talent suites; the same structure appears in lightweight form at the small-business end, where offer documents share machinery with general document sending but remain a distinct offer type.
- **Governance depth** — from no formal approval (owner sends directly) through single approver to sequential multi-group approval chains scoped by department or office; approval requirements may differ per job or per offer template.
- **Document production** — uploaded letter templates with tokens, in-system template editors, or documents produced outside the system and uploaded back after signature.
- **Signing substrate** — integrated e-signature, external signing providers, or no e-signature at all (emailed PDF, wet signature, manual upload and status update).
- **Hiring volume** — high-volume hiring adds bulk offer creation and stronger emphasis on throughput; executive hiring adds heavier approval chains and company signatories.
- **Requisition-driven organizations** — offers may tie to approved headcount: a requisition is selected when the offer is created, the offer may feed budget or hiring-plan reporting, and a withdrawn offer may release the requisition.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Applicant Tracking System / ATS | owns the whole candidate pipeline — sourcing, screening, interviews, stages; offer management owns only the offer artifact's lifecycle at the offer stage. In practice offer management usually ships inside an ATS, but the pipeline itself is a different object |
| Employee Onboarding Platform | begins at acceptance — preparing and starting the new hire; offer management ends at acceptance. The accepted offer is the seam between them |
| Compensation Management Platform | governs organization-wide compensation structure — bands, cycles, budgets, benchmarks; offer management consumes compensation-relevant fields for one hire's offer. A salary field in an offer form is not compensation management |
| HRIS / Employee Record System | the post-hire system of record for employed people; the offer is a pre-hire artifact whose record lives in the hiring funnel |
| Interview Scheduling / Assessment / Background Check | upstream pipeline neighbors that happen before the offer; they produce inputs to the hiring decision, not the offer itself |
| Proposal Management (sales) | structural analog in another domain — internal approval, external document, acceptance — but built on opportunities and commercial terms rather than candidates and employment terms |
| Contract Lifecycle Management | generic contract machinery for legal agreements; the offer letter is an employment-specific pre-hire artifact. Employment contracts that follow acceptance belong to HR document and onboarding flows |
| Approval Workflow Platform | generic engines routing arbitrary requests; offer approval is a hiring-specific instantiation whose subject is the offer's terms and whose outcome gates an external communication |
| E-signature products | delivery and signing substrate. Mature products themselves separate the offer — a record with terms, approvals, and outcomes — from a plain signature request |

## Representative Products

- Greenhouse (offers and offer approvals within Greenhouse Recruiting)
- Workable (offer documents and offer approval workflows)
- Breezy HR (offers and offer approvals)
- SmartRecruiters (offer management module within its enterprise hiring platform)

The researched sample spans the small-business to enterprise range; the market predominantly realizes this Application Type as a stage or module inside recruiting suites rather than as standalone products.

## Sources

Research date: **2026-09-08**

- Greenhouse Support — "Create an offer", "Request approval for a new offer", "Offer approval overview", "Generate and send offer document" — https://support.greenhouse.io/
- Workable Help — "Sending offer and e-signature documents", "E-signature offer approval workflows" — https://help.workable.com/
- Breezy HR Help Center — "Offers and Offer Approvals", "Electronic Documents" — https://help.breezy.hr/
- SmartRecruiters — official site (platform module listing naming Offer Management) — https://www.smartrecruiters.com/

> Sourcing limitation: several enterprise vendors' operational documentation was not reachable from the research environment (login-gated help portals; one vendor's guide rendered as JavaScript with an unreadable PDF; two vendors' help centers unreachable after repeated attempts). Claims about enterprise-suite implementations are therefore kept general, and no precise numeric limits, default timings, or vendor-specific mechanics are asserted in this document; such details as were observed remain in the paired Research Notes.
