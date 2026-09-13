# RFI Management

## Overview

An **RFI Management** application is the construction project's formal question system. It manages **Requests for Information (RFIs)** — numbered, tracked question records raised about a project's drawings, specifications, and contract documents — from the moment a question is written, through routing to the party responsible for answering, to the recorded answer, the asker's acceptance or rejection, and closure. All RFIs accumulate in a project-wide register that becomes the project's durable record of what was asked, what was answered, and what was decided.

The defining core is small:

```text
Project
└── RFI register (the project's log of formal questions)
    └── RFI record
        ├── formal question about the design / contract documents
        ├── references and attachments to the documents it concerns
        ├── accountable responder (person / organization) + response date
        ├── recorded answer
        └── asker's accept / reject decision → closed
```

Everything else commonly associated with RFI tools — due-date defaults, distribution lists, cost/schedule impact flags, drawing anchors, email transports, mobile capture, AI drafting — is widespread in current products but is not what makes the product an RFI Management application. The paper-era practice this software digitized — a numbered RFI form sent to the architect, answered, and entered into a project RFI log — satisfies the same core without any of the modern machinery.

When the object stops being a question seeking an answer — when it becomes a proposed item seeking approval, or an agreed change to the contract — the work has moved into a different Application Type (Submittal Management, Change Order Management).

## Users & Context

RFI Management is used by the parties to a construction project during bidding and, predominantly, during the course of construction. The defining situation: work is proceeding in the field, someone hits a gap, ambiguity, conflict, or error in the drawings or specifications, and the project needs a formal, answerable question — because the answer may change what gets built, what it costs, or who is liable.

Primary users:

- **Subcontractors, specialty contractors, and suppliers** — raise most RFIs from the field: an unclear dimension, a missing product specification, a conflict between drawings.
- **General contractor project engineers and project managers** — create, review, and manage RFIs; route them to the right responder; keep the log current; often act as the process's manager role.
- **Architects and engineers of record** — receive and answer RFIs, issuing the authoritative interpretation of the design documents.
- **Owners and owner representatives** — ask questions of their own, monitor open RFIs and their schedule/cost implications, and rely on the register for oversight.

Secondary concerns fall to project administrators, who configure numbering, response-time defaults, visibility, and per-organization access. The work environment is split between the office (web, where the log lives) and the field (mobile, where questions are discovered and photographed).

## Core Model

### The Defining Core

**The RFI record.** The unit of work is a single formal question, individually identified by a project-unique number. An RFI carries:

- the **question** itself — a formal request for clarification or a decision, written so that another party can answer it;
- **references to the documents it concerns** — drawing numbers, specification sections, or the contract documents the question arises from — plus attachments (drawing excerpts, photos, files);
- the **parties**: who asked (and on whose behalf), who is responsible for answering, and who is kept informed;
- **dates**: when the question was formally asked, when a response is due, when it was answered, when it was closed;
- the **answer**, recorded on the same record as the question.

**The accountable responder.** Every open RFI has a designated responsible party — a person, and in multi-company projects typically a person within a specific organization — who owes the answer. Accountability is singular and movable: the question can be reassigned or forwarded to the right responder without losing its identity. Some products formalize this as a single "current responsible person" whose action the RFI awaits; others express it as a per-recipient obligation that becomes overdue when the response date passes. The concept is the same: at any moment, the RFI is someone's to answer.

**The question→answer loop.** The RFI moves through a tracked lifecycle:

```text
Draft (being written)
  → Open (asked; routed to the accountable responder; response due by a date)
    → Answered (response recorded on the RFI)
      → Accepted → Closed   (the question is resolved; the record becomes fixed)
      or Rejected → back to Open (the answer was insufficient; more work needed)
```

The asker — not the responder — decides when the question is resolved. A rejected answer returns the RFI to the responder for clarification; an accepted answer closes it. Closed RFIs are uneditable; some products allow reopening or issuing a formal revision when a closed question turns out to be unresolved, and some allow a moot question to be withdrawn (voided) rather than answered.

**The RFI register.** RFIs accumulate in a project-wide log — the table a project engineer lives in — showing each RFI's number, subject, status, assignee, due date, and age. The register is filterable and exportable, and it is the project's contractual memory: months or years later, the record shows what was asked, what was answered, and when. This register posture is what distinguishes "management" from merely "writing an RFI."

### Standard Capabilities

Mature products commonly add:

- **Response dates and overdue tracking** — a due date on each open RFI (often defaulted from a configurable response window), with overdue RFIs surfaced in the log and reminders sent to the responsible party.
- **Distribution and observation** — distribution lists, CC recipients, and watchers who are kept informed of progress without being accountable for the answer.
- **Multiple contributors, one authority** — reviewers or additional assignees can contribute input, but a single party submits the authoritative answer; when several replies exist, one is designated the official response.
- **Cost and schedule impact flags** — a structured indication of whether the answer may affect cost (with an amount, if known) or schedule (with days, if known), including "yes but unknown" and "to be determined" states.
- **Links to project records** — associations with drawings, specification sections, submittals, change orders, and tasks, so the question sits in the project's document context.
- **Creation in context** — starting an RFI from a drawing or plan location, or converting a field task or observation into a formal question.
- **Email as a bridge to outsiders** — notifications by email, answering by email, and participation by external parties who never log in; the emailed reply is captured back onto the RFI record.
- **Reporting and export** — RFI log reports (CSV/PDF), status summaries, response-time metrics, and per-RFI PDFs for archiving and closeout.
- **Mobile capture** — creating and answering RFIs from the field with photos and markups.
- **Draft workflow** — field staff draft a question; a project engineer or manager reviews it, opens it, and routes it.
- **Visibility control** — private flags and role- or company-based rules governing who sees which RFIs and which responses.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:            the RFI record
Implementations:    a dedicated first-class object in a project-management suite;
                    a typed project-mail record ("RFI" as a mail type with a
                    response-required form);
                    a structured form template (older generation)

Concept:            the accountable responder
Implementations:    a single "current responsible person" the RFI awaits;
                    a per-recipient response obligation that goes overdue;
                    an assignee with reviewer/watcher satellites

Concept:            the register
Implementations:    a dedicated filterable log table;
                    mail search and reports over typed correspondence;
                    exportable CSV/PDF logs
```

A reader who has only seen the dedicated-module implementation should still be able to recognize the mail-typed and form-based generations from the core model.

## How It Works

### Raise a question

```text
A gap or ambiguity is found (in the field or in the office)
→ create an RFI: subject + formal question
→ reference the drawings / spec sections it concerns; attach excerpts or photos
→ identify who is asking (and on whose behalf)
→ save as a draft, or open it directly
```

In the common draft workflow, the field person writes the question and a project engineer reviews it before it is formally asked. Drafts are visible to the asking side only.

### Ask and route

```text
Open the RFI
→ a project-unique number is assigned
→ designate the accountable responder (a person, within a specific organization)
→ set the response due date
→ add reviewers, distribution, or watchers as needed
→ the RFI is now the responder's to answer; notifications go out
```

Routing is deliberate: the asker chooses who must answer, and the RFI can be reassigned or forwarded if it lands with the wrong party. In multi-company projects, a designated lead company (commonly the general contractor) may act as the routing hub — seeing all non-draft RFIs and imposing its numbering on the flow.

### Answer

```text
The responder opens the RFI
→ writes the answer, with attachments (revised details, photos, references)
→ submits it
→ the RFI moves to the asker for judgment
```

Contributors may add input along the way, but the designated responder submits the authoritative answer. External parties can often answer by simply replying to an email; the reply is recorded on the RFI.

### Judge and close

```text
The asker reviews the answer
→ accept → close the RFI (optionally notifying a distribution list)
→ or reject, with a reason → the RFI returns to the responder for clarification
```

Closing makes the record fixed. All parties are notified; the register reflects the closed status. If the answer revealed cost or schedule consequences, the RFI's impact flags carry that forward — and in products that connect the two, a change record can be created from the RFI so the consequence enters the contract-change process rather than staying an informal note.

### Work the register

```text
Open the RFI log
→ filter by status, assignee, company, overdue
→ chase what is aging; reassign what is stuck
→ export the log (or individual RFI PDFs) for meetings, reporting, closeout
```

The register is not a byproduct — managing it (aging, overdue, response times, open-by-company) is the daily work of the people who own the RFI process on a project.

## Interfaces

### RFI log / register

The primary surface: a filterable table of all RFIs on the project.

- typical columns: number, subject/name, status, assignee (and company), due date, date asked, date answered, response time, impact
- status summary (how many draft / open / answered / closed) at the top
- primary actions: create, open a record, filter, search, sort, export, bulk actions

### RFI detail

The record itself, usually read as a conversation of blocks.

- question block (with references and attachments), answer block(s), activity/history feed with timestamps
- status, assignee, due date, distribution/watchers
- primary actions: answer, reassign, forward for review, edit (while open), accept/reject, close, void, reopen/revise, download/email as PDF

### Create form

The structured entry surface for a new RFI.

- subject, question, references (drawing number, spec section), location, attachments
- assignee(s), due date, process owner/lead, distribution
- impact flags (cost / schedule)
- primary actions: save draft, open/submit

### Drawing-anchored creation

On a drawing or plan view, a pinned point can spawn an RFI (or link an existing one), keeping the question tied to the exact location it concerns.

### Mobile

Field-facing surface: view the log and records, create and fill drafts, photograph and mark up, answer. Status transitions are commonly web-side; some products support offline capture that syncs later.

### Reports and settings

- report builder/exports for the log; per-RFI PDFs for archiving
- project settings: numbering scheme, default response window, required fields, visibility rules, notification behavior, per-organization access

## Important Rules / Behaviors

### Numbers are unique and meaningful

Each RFI carries a project-unique number; duplicates are not permitted. Numbering schemes vary — sequential, prefixed, per-stage, or per-company codes — and some products let a lead party renumber incoming RFIs into its own scheme while preserving uniqueness. The number is how the rest of the project (meeting minutes, change records, claims) refers to the question.

### The asker owns resolution

The party who asked decides whether the answer resolves the question. A rejected answer returns the RFI to the responder with a required reason. This is the loop's control point: responders answer, askers close.

### Accountability is singular while the question is live

However many contributors surround an RFI, one party owes the next action. Reassignment moves that accountability explicitly and is recorded. Overdue state attaches to the party who owes the response.

### Closed means fixed

A closed RFI is uneditable; its value is as evidence. Corrections happen by reopening or by issuing a formal revision, which is itself recorded. Voided RFIs remain in the register (some products allow un-voiding); permanent deletion is restricted and typically limited to a record's own organization.

### Visibility is governed

RFIs can be private or restricted; multi-company products scope visibility by company and role, and may limit who sees which responses (for example, showing standard users only the designated official answer). The record posture — an unalterable, attributable history of the exchange — is a structural feature, not an afterthought: activity feeds log who changed what, when.

### The RFI is not the change

An RFI's answer may change the work, the cost, or the schedule, but the RFI itself carries no agreed money or scope. When consequences are real, they must be carried into the change-management process through an explicit conversion or link. Treating an answered RFI as a contract change is exactly the confusion this boundary exists to prevent.

## Variants

- **Dedicated-module variant** — the RFI as a first-class object inside a construction management suite, with the richest accountability machinery (the dominant modern shape among general-contractor platforms).
- **Typed-communication variant** — the RFI as a formal mail type within project correspondence, inheriting the mail system's record posture, distribution rules, and organization-scoped visibility (the document-control heritage; common on enterprise and owner-side projects).
- **Field-first variant** — RFI creation anchored in plan viewing and field tasks, optimized for foremen and specialty contractors, with multi-company routing and lead-company numbering.
- **Authority models** — a per-RFI manager role; a lead company acting as routing and visibility hub; organization-scoped visibility where each party sees its own correspondence.
- **Direction of asking** — contractor→designer is the dominant documented flow, but owner-initiated and designer-initiated RFIs are supported; the loop is direction-agnostic.
- **Scale and segment** — from small residential projects (fewer, simpler RFIs, often form-based) to enterprise capital programs (formal registers, document-control integration, portfolio-level reporting).
- **Era-current additions** — AI-assisted question drafting, BIM/model context attached to RFIs, offline mobile capture. Present in some current products; not part of the Type's definition.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Submittal Management | closest sibling process | A submittal *proposes* an item (material, shop drawing, method) for *approval* with revision cycles; an RFI *asks a question* seeking an *answer*. Different object, different resolution. Always separate tools in the sampled products. |
| Change Order Management | downstream | An RFI may reveal cost/schedule impact and spawn a change record, but the RFI carries no agreed price or scope; the change process owns contract modifications. |
| Construction Project Management | broader container | RFI Management is one process within a project-management suite; the suite adds schedules, budgets, documents, and many other records. |
| Construction Document Management | adjacent substrate | RFIs reference drawings and specs but do not control them; document management owns versions, transmittals, and the document register. |
| Ticketing System | structural cousin | The request→assign→respond→close shape is shared, but ticketing lacks the project container, design-document references, contractual record posture, and construction role model. |
| Punch List Management | sibling log | Punch items are deficiencies to *fix* (work items); RFIs are questions to *answer* (information). Both are project logs with assignees and closure. |
| Project correspondence / mail | general container | General project mail carries all communication; the RFI is the typed, response-required question process — which one sampled product implements literally as a mail type. |

The boundary with Submittal Management is the most important one, because both are formal project-communication processes with numbers, due dates, and closure. The structural difference: an RFI's resolution is an *answer* recorded by the design side; a submittal's resolution is an *approval* of something the contractor proposes. Remove the question→answer semantics and substitute propose→approve, and this Type becomes Submittal Management.

## Representative Products

- **Procore** — RFI tool within its construction management platform; dedicated RFI object with explicit accountability machinery (a single current responsible person, a per-RFI manager role, designated official responses) and conversion into change records.
- **Oracle Aconex** — enterprise project-mail and document-control heritage; the RFI realized as a typed project mail with response-required semantics, per-recipient outstanding/overdue status, and an unalterable record posture.
- **Fieldwire by Hilti** — field-first jobsite platform; dedicated RFI module with multi-company permissions, a lead-company routing model, plan-anchored creation, and a strict accept/reject loop.

The core model was checked against the form-template generation of RFI handling (preserved in one sampled product's legacy documentation) and against the paper-era practice it digitized, to avoid defining the Type by the current dedicated-module implementation alone.

## Sources

Research date: **2026-09-09**

Primary official documentation:

- Procore Support — RFIs (tool guide): https://support.procore.com/products/online/user-guide/project-level/rfi
- Procore Support — "What is an RFI?": https://support.procore.com/faq/what-is-an-rfi
- Procore Support — "Create an RFI": https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi
- Oracle Aconex Support Central — Mail (user guide): https://help.aconex.com/aconex/our-main-application/using-aconex/using-project-mail/
- Oracle Aconex Support Central — "Create and send mail": https://help.aconex.com/mail/create-mail/
- Fieldwire Help Center — "Introduction to RFIs in Fieldwire": https://help.fieldwire.com/hc/en-us/articles/4408422176539-Introduction-to-RFIs-in-Fieldwire
- Fieldwire Help Center — "What are RFIs?": https://help.fieldwire.com/hc/en-us/articles/360005020631-What-are-RFIs
- Fieldwire — RFI product page: https://www.fieldwire.com/rfis/

> Sourcing limitation: official operational documentation for Autodesk Construction Cloud / Autodesk Build could not be retrieved from the research environment (help site renders only via scripts; product pages blocked). No claims about those products are made in this document. Precise operational values observed in single products (specific reminder intervals, upload limits, status-label spellings) are intentionally not stated here; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
