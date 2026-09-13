# Submittal Management

## Overview

A **Submittal Management** application is the construction project's formal proposal-approval system. It manages **submittals** — numbered records on which a contracting party proposes the specific materials, products, equipment, or shop-drawing content it intends to use on the project, so that the party holding design review authority can return an official decision — approve, approve with notations, revise and resubmit, or reject — before fabrication, procurement, or installation proceeds. All submittals accumulate in a project-wide register that is planned from the specifications at the start of the work and worked throughout construction: who owes the next action, what is aging, what has been decided, and what remains outstanding.

The defining core is small:

```text
Project
└── Submittal register (the project's log of required and in-flight submittals)
    └── Submittal record
        ├── a proposal of specific products / shop-drawing content
        ├── reference to the specification or design requirement that demands it
        ├── attachments (shop drawings, product data, samples, certificates)
        ├── routing through reviewers holding review authority
        ├── the recorded decision — proceed / revise and resubmit / reject
        └── revision cycles until final disposition → closed and distributed
```

Everything else commonly associated with submittal tools — spec-section numbering schemes, the review-stamp response vocabulary, submittal packages, lead-time planning, distribution lists, email participation, mobile review, AI-assisted generation from specifications — is widespread in current products but is not what makes the product a Submittal Management application. The paper-era practice this software digitized — a submittal log kept by the contractor's office, transmittals carrying shop drawings to the architect, and a review stamp returning the decision — satisfies the same core without any of the modern machinery.

When the object stops being a proposal seeking an approval decision — when it becomes a question seeking an answer, or a controlled document being issued for its own sake — the work has moved into a different Application Type (RFI Management, Construction Document Management).

## Users & Context

Submittal Management is used by the parties to a construction contract, predominantly between award and the installation of the affected work. The defining situation: the specifications require the contractor to obtain design-team approval of specific products and fabrication details before they are ordered or built, and the project needs a formal, answerable approval record — because the decision governs what gets purchased, what gets fabricated, and who is liable when something does not comply.

Primary users:

- **Subcontractors, specialty contractors, and suppliers** — prepare and submit the actual content: shop drawings, product data, samples, warranties, certificates for their portion of the work.
- **General contractor project engineers and submittal managers** — plan the register from the specifications, create and route submittals, chase aging items, keep the log current; commonly act as the process's manager role and the hub through which items pass between the field and the design team.
- **Architects and engineers of record** — review what is proposed against the design documents and return the authoritative decision.
- **Owners and owner representatives** — on many projects a reviewer or final approver in the chain; on owner-run programs, the party that requires the register as oversight evidence.

Secondary concerns fall to project administrators, who configure numbering, review chains, response vocabularies, due-date defaults, and per-organization visibility. The work environment is mostly office-side (web, where the register and review happen), with mobile surfaces for viewing and responding; email remains a transport layer for parties who never log in.

## Core Model

### The Defining Core

**The submittal record.** The unit of work is a single formal proposal, individually identified by a project-unique number. A submittal carries:

- the **proposed item** — what the submitting party intends to use or build from: a shop drawing, product data, a sample, a mockup, a warranty, a certificate;
- the **reference to the requirement** — the specification section or design document that calls for the item, anchoring the proposal to the work it serves;
- **attachments** — the actual content to be reviewed;
- the **parties**: who submits (and on whose behalf), who reviews and decides, who is kept informed;
- **dates**: when submitted, when a response is due, when the decision was returned;
- the **decision**, recorded on the same record as the proposal.

**The review decision loop.** The submittal moves through a tracked lifecycle whose resolution is an approval decision, not an answer:

```text
Draft (being prepared)
  → Submitted (routed into review; response due by a date)
    → Under review (one or more review steps; intermediate reviewers possible)
      → Decision recorded:
         proceed (with or without notations) → close and distribute
         revise and resubmit → back to the submitter, new revision
         reject → work may not proceed; redesign or substitute
```

The reviewer — not the submitter — holds the decision authority. A "revise and resubmit" decision returns the item to the submitting side for a new revision, and the cycle repeats until a proceeding decision or a final rejection. The recorded decision is the official answer that governs whether procurement, fabrication, and installation may proceed; an approval with notations proceeds subject to the notations.

**The submittal register.** Submittals accumulate in a project-wide log — the table a project engineer lives in — showing each item's number, specification section, title, status, the party holding the action, and its dates. Mature practice plans the register ahead of need: the required submittals are extracted from the specifications at project start, so the log is both a workflow queue and a completion checklist against what the contract demands. The register is filterable and exportable, and it is the project's memory of what was proposed, what was decided, and when — a record that outlives the project into closeout and operations.

### Standard Capabilities

Mature products commonly add:

- **Spec-section anchoring** — the item linked to the specification section that demands it; register generation directly from the spec book; numbering schemes that carry the spec section.
- **A process-manager role** — a submittal manager or coordinator who owns each item's lifecycle, assembles review chains, and intervenes when a review stalls.
- **Multi-step review chains** — the proposal passing through intermediate reviewers (contractor review, consultants, engineers) before reaching the design-side decision maker, with one official decision path.
- **A decision vocabulary** — the approve / approve-as-noted / revise-and-resubmit / reject family, customizable per organization, with "for record only" and "void" dispositions for items that need no action or none anymore.
- **Revision cycles as records** — a resubmission creates a new revision of the same item rather than overwriting history, preserving the trail of what was seen and decided at each round.
- **Close and distribute** — the decided submittal formally returned to the submitting side (and any distribution list), signifying the work may proceed.
- **Due dates and aging** — per-step response dates, overdue surfacing, response-time measurement per reviewer, and register-wide aging views.
- **Grouping into packages** — related items (one trade, one system, one room) reviewed and returned together.
- **Related-item links** — associations with drawings, RFIs, change records, files, and schedule items, so the proposal sits in the project's context.
- **Email participation** — external reviewers and submitters receiving and answering by email, with replies captured back onto the record.
- **Reporting and export** — register exports (CSV/PDF), per-submittal PDFs with attachments, response-time and open-items reports.
- **Mobile surfaces** — viewing, reviewing, and responding from the field.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:            the submittal record
Implementations:    a dedicated first-class object in a project-management suite;
                    a review workflow over registered documents (the
                    document-control heritage);
                    a linear status ladder on a lightweight field platform

Concept:            the decision authority
Implementations:    named approvers in a sequential workflow;
                    a designated official reviewer whose determination is final;
                    a manager role acting as gatekeeper over reviewer input

Concept:            the register
Implementations:    a dedicated filterable log planned from the specifications;
                    a register of anticipated packages with dates;
                    status reporting over review workflows
```

A reader who has only seen the dedicated-module implementation should still be able to recognize the workflow-over-documents and field-ladder generations from the core model.

## How It Works

### Plan the register

```text
Award / mobilization
→ extract the required submittals from the specifications
   (or import a prepared list)
→ the register now shows what the contract demands:
   item, spec section, responsible party, needed-by dates
→ fill in items as the work approaches
```

The register is planned, not merely reactive: knowing what must be approved — and how long fabrication takes — is what keeps procurement from stalling the schedule.

### Create and route a submittal

```text
A required item approaches (or a question reveals the need)
→ create the submittal: title, type, spec section, description
→ attach the proposed content (shop drawing / product data / sample)
→ route it: designate the submitter and the review chain
→ set the response due date
→ notifications go out; the item is now someone's to act on
```

In the common pattern the general contractor's project engineer creates the item and routes it to the responsible subcontractor for content, or the subcontractor prepares the content and the engineer forwards it into review. One party holds the next action at every moment.

### Review and decide

```text
Each reviewer in the chain opens the item
→ reviews the attachments (often annotating them)
→ records a response with comments
→ the item advances to the next step, or back
→ the designated decision maker records the official decision:
   proceed (with or without notations)
   revise and resubmit
   reject
```

Contributors may comment along the way, but one recorded decision is official. A "revise and resubmit" decision sends the item back to the submitter; the resubmission becomes a new revision of the same record, and the cycle repeats.

### Close and distribute

```text
A proceeding decision is recorded
→ the submittal is closed (the record becomes fixed)
→ the decided content is distributed to the submitting side
   and the distribution list
→ the submitting party proceeds with procurement / fabrication / installation
```

Closed submittals are uneditable; their value is as evidence — of what was approved, on what date, and with what conditions. Approved shop drawings commonly flow onward to the drawing set the field builds from.

### Work the register

```text
Open the submittal log
→ filter by status, spec section, responsible party, overdue
→ chase what is aging; reassign what is stuck
→ watch completion against the required set
→ export the log (or individual PDFs) for meetings, reporting, closeout
```

Managing the register — aging, overdue, response times, completion — is the daily work of the people who own the submittal process on a project. Open submittals are swept before acceptance: nothing silently survives into closeout.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Submittal log / register

The primary surface: a filterable table of all submittals on the project.

- typical columns: number, title, specification section, type, status, submitter, current action holder, dates submitted/due/returned, response
- status summary (how many in each state) at the top
- primary actions: create, open a record, filter, search, sort, export, bulk actions

### Submittal detail

The record itself, read as a workflow.

- proposal block (references, attachments), review blocks with responses and annotated attachments, activity/history feed with timestamps
- status, current action holder, due dates, distribution, planning dates (needed-on-site, lead time) where supported
- primary actions: submit content, respond, forward for review, revise, close and distribute, void, download/email as PDF

### Create form

The structured entry surface for a new submittal.

- title, type, specification section, description, attachments
- submitter, review chain, due dates
- primary actions: save draft, submit into review

### Specification-anchored views

Register generation and navigation from the spec book: the required submittals extracted from uploaded specifications, organized by section, with the register built from the extraction.

### Mobile

Field- and reviewer-facing surface: view the log and records, review attachments, respond. Status transitions are commonly web-side.

### Reports and settings

- register exports, response-time reports, open-items reports
- project settings: numbering scheme, review-chain templates, response vocabulary, due-date defaults, visibility rules, per-organization access

## Important Rules / Behaviors

### The decision authorizes the work

An approval means procurement, fabrication, or installation may proceed; "revise and resubmit" and "reject" mean it may not. The decision's semantics are the point of the process — this is what separates a submittal from a document being shared for information.

### One official decision path

However many reviewers contribute, one recorded decision is official. Mature products formalize this: a designated decision maker whose determination is final, or a manager role acting as gatekeeper over reviewer input before the official response is returned.

### Revisions preserve history

A resubmission is a new revision of the same record, not an overwrite. The trail of what was submitted, seen, and decided at each round remains intact — which is why revising by rewinding the workflow (rather than creating a revision) is discouraged in products that allow it: it overwrites recorded dates and responses.

### Closed means fixed

A closed submittal is uneditable; its value is as evidence. Voiding (for duplicates and no-longer-needed items) and reopening are recorded actions; deletion is restricted and typically limited to drafts.

### Numbers are unique and meaningful

Each submittal carries a project-unique number — sequential, company-prefixed, or specification-prefixed — and is how the rest of the project (meeting minutes, RFIs, change records) refers to the proposal.

### The submittal is not the change

A rejected or repeatedly revised submittal may reveal that the specified product is unavailable or the design must change — but the submittal itself carries no agreed money or scope. When consequences are real, they enter the change-management process through an explicit conversion or link.

### Visibility is governed

Submittals can be private or restricted; multi-company products scope visibility by organization and role. In lead-party arrangements, the lead organization sees the flow across parties while others see their own segment. The record posture — an attributable history of proposals and decisions — is structural, not cosmetic.

## Variants

- **Dedicated-module variant** — the submittal as a first-class object inside a construction management suite, with the richest workflow machinery (the dominant modern shape among general-contractor platforms).
- **Workflow-over-documents variant** — the submittal realized as a review workflow over registered documents, inheriting the document-control heritage's record posture and cross-organization reach (common on enterprise and owner-side projects).
- **Field-first variant** — a linear status ladder on a lightweight jobsite platform, optimized for smaller teams and specialty contractors, with company-based routing and email participation.
- **Operator posture** — contractor-operated (the builder runs the process), owner-directed (the owner's program prescribes the workflow and consumes the register as oversight), or neutral platforms where each organization keeps its own workspace.
- **Register-first planning** — the anticipated submittal list created ahead of need, in some workflows supplied by the submitting vendor with fabrication times attached.
- **Quality-gated submission** — an internal quality-control review step before the item enters formal review.
- **Scale and segment** — from small residential projects (few, simple submittals) to enterprise capital programs (formal registers, portfolio-level reporting, document-control integration).
- **Era-current additions** — AI-assisted generation of the register from specifications, offline mobile capture, QR-coded records. Present in some current products; not part of the Type's definition.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| RFI Management | closest sibling process | A submittal *proposes* an item for *approval* with revision cycles; an RFI *asks a question* seeking an *answer*. Different object, different resolution. Always separate tools in the sampled products. |
| Construction Document Management | adjacent substrate | The submittal's attachments are documents and its register is a specialized controlled register, but the approval transaction — not the document record — is the defining core. |
| Construction Project Management | broader container | Submittals are one instrument family in the project's coordination record; this Type is the dedicated process for that family, with deeper decision and revision machinery. |
| Construction Closeout Management | downstream consumer | Closeout sweeps open submittals before acceptance and collects submittal deliverables (O&M manuals, warranties); the submittal workflow itself runs throughout construction. |
| Change Order Management | downstream | A rejected or revised submittal may spawn a change, but the submittal carries no agreed price or scope; the change process owns contract modifications. |
| Engineering Document Management | design-side cousin | That Type issues controlled documents outward (transmittals); here the contractor proposes content inward and seeks a decision on it. Direction and resolution differ. |
| Approval Workflow Platform | structural cousin | Generic sign-off routing lacks the submittal's domain semantics: spec-driven demand, design-team review authority, the approve/revise/reject decision family tied to fabrication and procurement. |

The boundary with RFI Management is the most important one, because both are formal project-communication processes with numbers, due dates, and closure. The structural difference: an RFI's resolution is an *answer* recorded by the design side; a submittal's resolution is an *approval* of something the contractor proposes. Remove the propose→approve semantics and substitute question→answer, and this Type becomes RFI Management.

## Representative Products

- **Procore** — Submittals tool within its construction management platform; the market's reference implementation of the dedicated-object pattern (submittal manager, sequential approval workflows, ball-in-court accountability, spec-section anchoring, submittal packages).
- **Autodesk Build (Autodesk Construction Cloud)** — suite module; submittal items and packages organized by spec sections, with configurable multi-step, multi-reviewer review workflows and a manager acting as gatekeeper.
- **Oracle Aconex** — enterprise project-mail and document-control heritage; submittals realized as review workflows over registered documents, with transmittals extending participation to non-users.
- **Kahua** — owner- and GC-side enterprise platform; submittal items and packages with a register-first posture, a coordinator role, and an official-reviewer gatekeeper model.
- **Fieldwire by Hilti** — field-first jobsite platform; a linear status ladder with company-based routing, specification extraction, and email participation for external parties.

The core model was checked against the workflow-over-documents realization (which has no dedicated submittal object) and against the paper-era practice it digitized — the submittal log, the transmittal, and the review stamp — to avoid defining the Type by the current dedicated-module implementation alone.

## Sources

Research date: **2026-09-10**

Primary official documentation:

- Procore Support — Submittals (user guide): https://support.procore.com/products/online/user-guide/project-level/submittals
- Procore Support — "What is a submittal?": https://support.procore.com/faq/what-is-a-submittal
- Procore Support — "What are the default submittal statuses in Procore?": https://support.procore.com/faq/what-are-the-default-submittal-statuses-in-procore
- Procore Support — "What are the default submittal responses in Procore?": https://support.procore.com/faq/what-are-the-default-submittal-responses-in-procore
- Procore Support — "Best Practices: Submittal Workflow Management": https://support.procore.com/products/online/user-guide/project-level/submittals/best-practices-submittals/best-practices-submittal-workflow-management
- Autodesk Help — "Work with Submittals": https://help.autodesk.com/cloudhelp/ENU/Build-Submittals/files/Work_Submittals.html
- Autodesk Help — "Process Submittal Items": https://help.autodesk.com/cloudhelp/ENU/Build-Submittals/files/work-submittals/Process_Submittal.html
- Oracle Aconex Support Central — "Submittals" (implementation guide): https://help.aconex.com/implementation/submittals
- Kahua Help — "Submittals": https://help.kahua.com/main/Content/4-DocumentationMngmt/Submittals/submittals.htm
- Kahua — Packaged Submittals quick-reference (GSA): https://www.gsa.gov/system/files/Kahua_Packaged_Submittals_v001.pdf
- Fieldwire Help Center — "Introduction to the Submittals Workflow in Fieldwire": https://help.fieldwire.com/hc/en-us/articles/7160473659419-Introduction-to-the-Submittals-Workflow-in-Fieldwire

> Sourcing limitations: Kahua's help is configuration-oriented (role and workflow options) rather than end-to-end tutorials, and Oracle Aconex documents its dedicated Submittals module mainly at implementation-guide level (the vendor recommends its Workflows module as the primary mechanism); claims about those two products are limited accordingly. Precise operational values observed in single products (specific response-wording counts, reminder intervals, permission tiers, file-size limits) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
