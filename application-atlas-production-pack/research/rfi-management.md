# Research Notes — RFI Management

Research date: 2026-09-09

## Research Goal

Understand what a construction **RFI Management** application really is, from real products: what the RFI object is, who asks and who answers, how the question→answer lifecycle works, what rules and states matter, how RFIs relate to other project records, and where the Type's boundary sits against neighboring Types (Submittal Management, Change Order Management, Construction Project Management, Ticketing System).

## Initial Boundary

Working hypothesis before research:

- RFI = Request for Information: a formal question raised during a construction project (usually by a contractor) about the design/contract documents (drawings, specifications, scope), answered by the design team or owner.
- RFI Management software tracks these questions as records: creation, routing to a responsible party, response, due dates, closure, and a project-wide log.
- Nearest neighbors: Submittal Management (approval of proposed items, not questions), Change Order Management (contract changes, not clarifications), Construction Project Management (broader suite), Ticketing System (same request→respond→close shape but no project-document binding).
- Unknowns: exact lifecycle states per product; whether the RFI is always a first-class object or sometimes a typed communication; direction of asking (contractor→designer only?); how impact tracking connects to change management.

## Research Questions

1. What is an RFI as an object: fields, references, attachments, numbering?
2. Who creates RFIs and who answers them (roles, companies, directions)?
3. What is the lifecycle (statuses) of an RFI, and who controls each transition?
4. How is accountability assigned and moved (single responsible party vs multiple)?
5. How do due dates, reminders, and overdue states work?
6. How do RFIs link to other project records (drawings, specs, submittals, change orders)?
7. What interfaces exist (log/table, detail, mobile, drawing-anchored creation, reports)?
8. What rules matter (numbering uniqueness, visibility/privacy, closing authority, editability)?
9. What reporting exists (RFI log, aging, response time, exports)?
10. What variants exist (dedicated object vs typed mail vs form; GC-centric vs owner/document-control vs field-first)?

## Representative Products

| Product | Pole | Customer level | Why chosen |
|---|---|---|---|
| Procore | GC-centric construction management platform; RFI as a dedicated project tool with rich accountability machinery | Mid-market to enterprise GCs | Market leader; deepest documented RFI workflow |
| Oracle Aconex | Enterprise document-control / project-mail heritage; RFI realized as a typed project mail with response-required semantics | Enterprise owners, engineers, contractors | Different philosophy: RFI as communication record, not standalone object |
| Fieldwire by Hilti | Field-first jobsite tool; RFI as a dedicated module with company-based permissions and lead-company model | SMB to mid-market GCs and specialty contractors | Field/foreman perspective; multi-company mechanics |

Also attempted: Autodesk Construction Cloud (blocked — see Sources), Kahua (Tier-2 pages reachable, RFI-specific documentation not reachable), Buildertrend (403). These are recorded as market context only; no claims based on them.

## Sources

Tier 1 (official operational documentation, fetched 2026-09-09):

- Procore Support — RFIs tool landing: https://support.procore.com/products/online/user-guide/project-level/rfi
- Procore Support — What is an RFI?: https://support.procore.com/faq/what-is-an-rfi
- Procore Support — Create an RFI: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi
- Oracle Aconex Support Central — Mail guide: https://help.aconex.com/aconex/our-main-application/using-aconex/using-project-mail/
- Oracle Aconex Support Central — Create and send mail: https://help.aconex.com/mail/create-mail/
- Fieldwire Help Center — Introduction to RFIs in Fieldwire: https://help.fieldwire.com/hc/en-us/articles/4408422176539-Introduction-to-RFIs-in-Fieldwire
- Fieldwire Help Center — What are RFIs?: https://help.fieldwire.com/hc/en-us/articles/360005020631-What-are-RFIs

Tier 2 (official product pages):

- Fieldwire — RFI software page: https://www.fieldwire.com/rfis/
- Fieldwire — main site: https://www.fieldwire.com/
- Kahua — platform and design-management pages: https://www.kahua.com/ , https://kahua.com/solutions/design-management/

Source-access limitations:

- Autodesk Construction Cloud / Autodesk Build: help.autodesk.com returns a JS shell; product pages return 403 (bot protection). Tried help.autodesk.com/view/ACD/ENU/, /view/BIM360D/ENU/, and the product overview page. **No Autodesk-specific claims are made in this research.**
- Fieldwire's legacy support host (support.fieldwire.com) transport-errors; the live help center is help.fieldwire.com (used).
- Buildertrend help returns 403. Kahua knowledge base is JS-rendered (empty HTML without scripts).
- Per the evidence rules, no precise operational details were taken from model memory to fill these gaps.

## Product A — Procore

### Key observations (evidence layer A — directly observed)

Definition (official FAQ): "In construction, the term Request for Information (RFI) refers to a business process initiated by a contractor (for example a general contractor, subcontractor, or supplier) to request information or raise concerns that must be formally answered by that contractor's client or the project's architect." Purpose: "resolve information gaps, eliminate ambiguities, and capture specific project decisions." RFIs are asked "during a project's Bidding process and/or during the project's course of construction." The answer "can change the project's scope of work and may also require approval when it affects contract costs."

RFI as an object (Create an RFI tutorial). In Procore, RFIs are comprised of:

- **General Information** — background/context for the question
- **Question** — "a formal question related to the construction project that requires a response from another person"; can be asked on behalf of another person/vendor
- **Replies** — replies sent by assignees
- **Official Response** — one or more replies designated as the official answer; "the 'RFI Manager' typically chooses the official response"

Required fields to save an RFI in Open status: **Number, Subject, Assignees, Due Date, Question**. Duplicate RFI numbers are NOT permitted.

Field list (Admin creation form): Number (sequential, or prefix-by-stage option), Subject, Question, Attachments, Due Date (auto-populated from a configurable default number of days; respects project working days), Assignees (multiple; per-assignee "Make Response Required" flag), RFI Manager (project default designated), Distribution list, Received From, Responsible Contractor (auto-filled from Received From's company), Drawing Number (manual entry possible; recommended path is linking the RFI to a Drawing in the Drawings tool), Location (multi-tier), Spec Section (from the project's specification book), Cost Code (links RFI to budget for later change orders), Project Stage, Cost Impact (Yes + $ amount / Yes (Unknown) / No / TBD / N/A), Schedule Impact (Yes + days / Yes (Unknown) / No / TBD / N/A), Private flag, Reference, Custom Fields, Sub Job.

Accountability machinery:

- **Ball In Court** — the single person currently responsible for the RFI's next action. Creating as Open shifts Ball In Court to the Assignees; a Draft keeps it with the RFI Manager. Ball In Court can be shifted explicitly.
- **RFI Manager** — a per-RFI role (with a project-level default); acts as the manager of the RFI process; granular permission "Act as RFI Manager" lets Standard users perform manager actions on RFIs they created or manage.
- **Assignees** — one or more responders; a per-assignee "response required" flag; the current Ball In Court assignee can add assignees or forward for review.
- **Distribution list** — read-only-and-up users kept informed; Standard creators must be on the distribution list to be notified of the official response.

Statuses and transitions (from tutorials list and permissions matrix): Draft, Open, Closed; a newer "Closed-Draft" status exists (release note 03/2025); Reopen an RFI; Revise an RFI (RFI REVisions, GA 09/2025); RFI Recycle Bin (RFIs keep Open status when recycled). Standard-level users create Draft RFIs and send them to the RFI Manager for review; the RFI Manager places them in Open and assigns responders.

Downstream conversion: Create a Change Event from an RFI; Create a Potential Change Order from an RFI (requires approved prime contract, two/three-tier CO configuration); Create an Instruction from an RFI; Create a Correspondence Item from an RFI.

Document anchoring: Create or Link RFIs on a Drawing (from the Drawings tool, both web and mobile).

Email integration: "Answer RFIs by email"; Forward an RFI by Email; configurable notification behavior ("How do I control which emails are sent by Procore during the RFI process?").

Reporting: Create and View an RFI Report (custom reports), Export RFIs to CSV or PDF, Export an RFI, saved views, customizable columns, distribution history of reports.

Permissions: None / Read Only / Standard / Admin plus granular permissions (Act as RFI Manager; Mark Official Responses). Viewing of responses can be restricted ("Only Show Official Responses to Standard and Read-Only Users" setting).

Mobile: full RFI tool on iOS/Android (create, respond, change status, link to drawings, offline support noted for some actions).

AI: "Draft RFI Agent" in open beta (09/2025) — AI drafting of RFIs.

## Product B — Oracle Aconex

### Key observations (evidence layer A — directly observed)

RFI as a typed mail, not a standalone object. From "Create and send mail": "Writing a memo, an RFI, or some general correspondence? You need Aconex Mail." "Every mail must have a mail type, which does a few things: It identifies the different processes on the project, such as Request for Information. It sets up a form, helping you to enter the right details. It helps you find mail again later." The Project Admin decides which mail types are available for each organization.

Mail as the record: "Mail provides you with an unalterable record of all project and process related communications." Visibility: "In most cases, you have access to all mail sent to anyone in your organization" (organization-scoped visibility).

Response-required semantics (the RFI loop inside mail):

- When sending, the sender chooses a **Response Required** option and a **respond by date**. This sets the mail status per recipient:
  - **Outstanding** — for each To recipient until they (or someone in their organization) responds
  - **Overdue** — automatically set when the respond-by date passes without a response
  - **N/A** — for CC recipients and when no due date is set
- Mail needing response appears in the recipient's **Tasks** page as Outstanding or Overdue.
- Project admins can make Response Required mandatory for a mail type, set default response times, configure mail status labels, and create mail distribution rules (auto-adding recipients to certain mail types).

Composition: recipients (To/Cc from the project directory), attachments (documents, other mail, local files), attribute fields (configured per project/mail type), auto-text templates, signatures, subject, body. Drafts are visible to anyone in the sender's organization. Confidential mail restricts visibility. Distribution-rule preview shows who will be auto-included.

Lifecycle operations: reply/forward, mark sent mail as your response, mark mail as No Action Required, **close-out sent mail** (for accurate reporting), mail reports and saved searches, mail approval rules (org-level approval before sending).

External participation: guests can reply to email notifications without logging in; incoming external email can be registered into Mail.

Other modules (context): Documents (document control), Workflows (document review processes), Field (quality/issues), Cost, Packages, Tenders. RFIs are not a separate module — they live in Mail as a process type.

## Product C — Fieldwire by Hilti

### Key observations (evidence layer A — directly observed)

Definition (legacy form article): "RFIs are designed to formally communicate questions with the design team, client, or general contractor that will likely affect the contract scope, drawings, and/or specifications."

Dedicated RFI module (current): part of Fieldwire's Project Management; "helps extend the flow of data from the Field and bridges the gap between various stakeholders. RFIs provide neutral data ownership and empower teams to intuitively build an indisputable record of RFIs." Sold as an add-on (Business Plus tier / demo).

Statuses: **Draft → Open → Pending → Closed**, plus **Void** (with Unvoid). Definitions:

- Draft: first created; question is the only required field to assign; can attach crop plans, photos, files; related tasks/RFIs/plans; impact. Contributors can create drafts; only Managers move Draft→Open by assigning to another company.
- Open: assignee indicated and due date selected → **an RFI number is assigned**. Assignee answers, reassigns, voids, or creates a related RFI.
- Pending: after an answer is submitted, the RFI is reassigned to the creator; the creator can **accept and close** or **reject the answer** (reason required; goes back to the previous assignee for clarification).
- Closed: answer accepted; RFI becomes uneditable; all stakeholders notified.
- Void: no longer applicable; uneditable; can be unvoided (reverts to prior status); only Managers can permanently delete Void RFIs (and only ones created by their company).

Multi-company mechanics:

- Permissions per role (Manager/Contributor) **within each company**; the "Asker company" is the company that created and submitted the question.
- **Lead Company** (optional, e.g., the GC): only lead-company users may "Answer on behalf"; the lead company sees every non-Draft RFI on the project; lead-company managers can renumber RFIs to the lead company's numbering format (company code stays fixed); submitters in other companies can only add reviewers from the lead company when a lead company is set.
- **Reviewers** — multiple users can add responses, but only the assignee submits the final answer; the submitter cannot see assignee/reviewer responses unless made a reviewer.
- **Watchers** — receive email notifications on progress; cannot edit; assignee changes auto-add the previous assignee as a watcher.
- Visibility: users see RFIs created by their company, assigned to them, or where they are a reviewer; project admins can restrict visibility of Closed RFIs created by non-lead companies.

Fields (RFI table columns): # (company code + number, assigned when moving Draft→Open), Name, Status, Due date, Reviewers, Assignee, Reference # (for other parties' numbering), Impact (None / Cost / Schedule / Cost & Schedule), Date asked, Date answered, Response time (days between question and answer).

External participation: assign to a **project user or an email address** (non-user); the external assignee replies by email; the creator (or lead company manager) can "answer on behalf" and mark the emailed response as the answer; only the lead company can assign to email addresses. Optional assignee email reminder 48 hours before the due date (product-stated value).

Creation surfaces: from the RFI tab; **from a plan** (RFI hyperlink on the single-page plan view; link existing RFIs to plans); **from a Task** (convert a task with photos into a draft RFI); **bulk import** of draft RFIs (name, question, suggestion, reference number, impact, impact notes).

Linking: link or create related **Specifications, Tasks, RFIs, Change Orders** from an RFI.

Exports: CSV and PDF reports (summary + table; columns match the user's table view); bulk export individual RFI PDFs (noted as useful for project closeout); email an RFI PDF (logged in activity).

Mobile: create and fill draft RFIs (question, due date, attachments, impact, photo markup); status changes are web-only; view related items.

Legacy: RFIs were previously handled as a **form template** (with Sent/Due/To/From, Ref. Drawings, Ref. Specs, Cost/Schedule Impact yes-no-n/a checkboxes, Question, Suggestion, Response, Answered by/date); the vendor has replaced the default form with the dedicated module.

## Cross-product Comparison

| Dimension | Procore | Oracle Aconex | Fieldwire |
|---|---|---|---|
| RFI substrate | Dedicated first-class RFI object (project tool) | Typed project mail ("mail type" = Request for Information) with response-required semantics | Dedicated first-class RFI module (formerly a form template) |
| Unit of record | Numbered RFI (Number, Subject, Question required for Open) | Mail with correspondence ID; mail type + form fields | Numbered RFI (company code + number assigned at Open) |
| Asker → responder | Contractor (GC/sub/supplier) asks; client/architect answers; owner can also create (documented in training-video titles) | Any project participant; mail type availability set per organization | Any company on the project; "Asker company" concept; lead-company overlay |
| Accountability | Ball In Court (single current responsible person) + RFI Manager + Assignees (response-required flags) | Per-recipient Outstanding/Overdue status; response required by date | Assignee (single accountable) + Reviewers (input only) + Watchers (notify only) |
| Lifecycle | Draft → Open → Closed (+ Closed-Draft; Reopen; Revise) | Sent → Outstanding/Overdue per recipient → responded → closed out | Draft → Open → Pending → Closed (+ Void/Unvoid) |
| Answer authority | Assignees reply; RFI Manager designates the Official Response | Any recipient org responds; sender closes out | Assignee submits; asker accepts/rejects; lead company can answer on behalf |
| Due dates | Required for Open; default from configurable settings; respects working days | Respond-by date optional or mandatory per mail type; drives Overdue | Required to submit; optional reminder before due date |
| Overdue handling | Notifications; overdue visible in log | Automatic Overdue status per recipient | Overdue filter (Open past due date) |
| Document anchoring | Link to Drawings; Spec Section field; Drawing Number field | Attach documents/other mail; attribute fields | Link plans (pin from plan view); Ref. Drawings / Ref. Specs (legacy form); link Specifications |
| Downstream links | Change Event / Potential Change Order / Instruction / Correspondence from RFI; related items | Mail can be referenced; Cost module separate | Link/create Change Orders, Tasks, RFIs, Specifications |
| Impact tracking | Cost Impact (Yes/$, Yes-Unknown, No, TBD, N/A) + Schedule Impact (Yes/days, …) | Not observed as RFI-specific fields (attribute fields configurable) | Impact (None/Cost/Schedule/Cost & Schedule) + impact notes; impact changes logged |
| External parties | Answer by email; distribution list | Guest reply via email notification; register incoming mail | Assign to email address; reply by email; CC list |
| Visibility control | Private flag; permission levels; official-response-only setting | Organization-scoped visibility; confidential mail | Company-based visibility; lead-company overlay; closed-RFI visibility setting |
| Reporting | Custom RFI reports; CSV/PDF export; saved views | Mail reports; saved searches | CSV/PDF reports; bulk PDF export; status summary |
| Mobile | Full tool incl. offline actions | Mobile app (mail/field) | Create/fill drafts; no status changes on mobile |
| Record posture | "Record a history of all RFIs"; change history per RFI | "Unalterable record of all project and process related communications" | "Indisputable record"; activity feed with timestamps |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures. Removing any one stops the product from being RFI Management:

1. **The RFI as the unit of record** — a formal, individually identified (numbered) question bound to a construction project, asking for clarification or a decision about the project's design/contract documents (drawings, specifications, scope), carrying the question text, references to the documents it concerns, and attachments. Remove → a memo/notes tool or a bare form, not managed RFIs.
2. **The accountable question→answer loop** — the question is routed to a designated responsible party (person and/or organization) who must answer by a tracked date; the answer is recorded on the RFI; the asker judges the answer (accept/close or reject/return for more work); accountability can be reassigned while the question is live. Remove → a document archive or a discussion board; nothing is *answered*.
3. **The project RFI register** — RFIs accumulate in a project-wide, filterable log showing status and aging (open / awaiting response / answered / closed, overdue), giving the project a durable, exportable record of its formal questions and the decisions taken — the contractual memory that outlives the exchange. Remove → scattered correspondence with no management layer.

Jointly-held load-bearing:

- 1 alone = a question form / memo template
- 2 alone = generic task assignment or ticketing
- 3 alone = a spreadsheet log with no workflow
- 1+2 without 3 = correspondence with no register (management dies)
- 1+3 without 2 = a log nobody works
- 2+3 without 1 = a generic request tracker with no project-document semantics

Historical/market-sample check: the paper-era practice — a numbered RFI form referencing drawing/spec sheets, sent to the architect, answered, and entered into a project RFI log (the register) — satisfies all three structures with no software machinery. Older software generations (RFI as a form template in Fieldwire's legacy; RFI as a mail type in Aconex) also satisfy the core. The definition is therefore not over-fitted to the modern dedicated-module implementation.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature products but not definitional:

- Due dates with configurable default response windows and overdue tracking/reminders
- Distribution lists / CC / watchers keeping the wider team informed
- Multiple contributors (reviewers, assignees) around a single accountable party
- Designation of the authoritative answer when multiple replies exist (official response / accepted answer)
- Cost and schedule impact flags (yes/no/TBD/unknown, with amount or days)
- Links to project records: drawings, specifications, submittals, change orders, tasks
- Creation anchored in context: from a drawing/plan location, from a field task/observation
- Email integration: notifications, respond-by-email, guest participation for external parties
- Reports and exports of the RFI log (CSV/PDF), status summaries, response-time metrics
- Mobile access with photos/markups
- Numbering conventions (sequential numbers, prefixes, per-company codes, per-stage prefixes)
- Draft workflow (field person drafts; project engineer/manager reviews and opens)
- Reopening or revising closed RFIs; revision history / activity feed on the record
- Private/confidential flags and role/company-based visibility rules

### L2 — Variant / Optional Structure

- Implementation substrate: dedicated RFI object (Procore, Fieldwire) vs typed project mail (Aconex) vs form template (Fieldwire legacy) — the container varies; the loop is the invariant
- Direction of asking: contractor→designer is the dominant documented flow; owner-initiated and designer-initiated RFIs are supported in sampled products
- Authority models: RFI Manager (per-RFI manager role), Lead Company (GC as routing/visibility hub), organization-scoped visibility (document-control heritage)
- Multi-round depth: reply threads with a designated official response vs strict accept/reject loop
- BIM/3D model context attached to RFIs
- AI drafting assistance (beta at one sampled product)
- Segment shape: GC platform module vs owner-side capital-program suite vs field-first jobsite tool; residential/small-project scale
- Offline mobile support; per-project vs per-organization configuration of types/fields

### L3 — Vendor-specific Structure (research notes only)

- Procore: "Ball In Court", "RFI Manager" role, "Official Response", Change Events, Potential Change Orders, Instructions, Correspondence items, Closed-Draft status, Draft RFI Agent (AI, beta), RFI REVisions, sub jobs, cost codes, prefix-by-project-stage numbering, "Only Show Official Responses…" setting, Recycle Bin behavior
- Aconex: mail types per organization, correspondence IDs, auto-text templates, mail approval rules, organization-wide mail visibility, mail distribution rules, UTC date handling, guest email replies, close-out semantics
- Fieldwire: Lead Company (crown icon), company codes on RFI numbers, answer-on-behalf, unvoid, watchers auto-added on reassignment, 48-hour pre-due reminder, upload size limits, RFI importer, plan-hyperlink creation, task→RFI conversion

## Rejected Findings

- "RFI Management = a module of a construction management suite" — rejected as definitional: Aconex implements RFIs inside project mail; standalone RFI tools exist. The suite container is a market realization, not the Type.
- "RFIs always flow from contractor to architect" — rejected: sampled products support owner- and designer-initiated RFIs; the dominant flow is a market pattern, not the definition.
- "Cost/schedule impact fields are definitional" — rejected: impact tracking is strong in two of three sampled products and configurable/absent in the third; it is common mature structure, not the core.
- "RFI = ticket" — rejected: the project-document binding (drawings/specs/contract scope), the contractual record posture, and the construction role model distinguish the Types (see Boundary Findings).
- "Email integration is definitional" — rejected: it is the dominant transport for external parties but the loop works fully in-product; historical paper practice satisfies the core without email.

## Boundary Findings

- **vs Submittal Management**: a submittal is the contractor *proposing* an item (material, shop drawing, method) for *approval* with revision cycles; an RFI is a *question* about design intent seeking an *answer*. Different initiative direction, different object, different resolution (approval vs clarification). In sampled products they are always separate tools/modules (Procore: Submittals tool; Fieldwire: Submittals module; Aconex: separate document processes). Replace the question→answer loop with propose→approve and the Type becomes Submittal Management.
- **vs Change Order Management**: an RFI may reveal cost/schedule impact and *spawn* a change record (documented: Procore creates Change Events/PCOs from RFIs; Fieldwire links change orders), but the RFI itself is not a contract change — it carries no agreed price/scope. The relationship is one-directional (RFI → potential change).
- **vs Construction Project Management (broader suite)**: RFI Management is one process inside a project-management suite. The Type is defined by the question-record core, not by schedules, budgets, or documents at large.
- **vs Ticketing System (ITSM)**: the request→assign→respond→close shape is shared, but ticketing lacks the project container, the design-document references, the contractual record posture, and the multi-company construction roles. Strip the project/document semantics from an RFI tool and what remains is a ticketing system.
- **vs Construction Document Management**: RFIs *reference* documents but are not document control — no versioning/transmittal of the documents themselves. In Aconex the two live in different modules (Mail vs Documents).
- **vs general project correspondence / mail**: general mail is broader small-group communication; the RFI is the typed, response-required question process. Aconex demonstrates the RFI can live inside mail as a type — the defining core is the loop, not the container.
- **vs Punch List Management**: punch items are deficiencies to fix (work items); RFIs are questions to answer (information). Both are project logs with assignees and closure, but the object and resolution differ.

## Uncertainties

- Autodesk Construction Cloud's RFI implementation could not be verified (bot-blocked help site). Its exact statuses, fields, and workflow are unknown here; no claims made.
- Exact default response windows (e.g., Procore's configurable default number of days) were not stated as specific values in the fetched pages; no numeric defaults are asserted.
- The relative market frequency of owner-initiated vs contractor-initiated RFIs is not established by official documentation; only capability is documented.
- Kahua's RFI specifics unverified (knowledge base JS-rendered); Kahua is cited only as market context.
- Whether "Closed-Draft" (Procore) represents a broader industry pattern or a single-product status — single-product evidence, kept out of the canonical model.

## Final Synthesis

RFI Management is the construction project's **formal question system**: numbered question records about the project's design and contract documents, each routed to an accountable responder who must answer by a tracked date, with the asker accepting or rejecting the answer, and all questions accumulating in a project-wide register that serves as the durable record of what was asked, answered, and decided. Everything else — due-date defaults, distribution lists, impact flags, drawing anchors, email transports, mobile capture, AI drafting, lead-company authority models — is mature structure layered on that loop. The Type's identity is held jointly by the question record, the accountable answer loop, and the register; the container (dedicated tool, typed mail, or form) is implementation, not definition.
