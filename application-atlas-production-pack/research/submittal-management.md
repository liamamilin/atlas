# Research Notes — Submittal Management

Research date: 2026-09-10
Leaf: Submittal Management (§17 Construction, Real Estate & Facilities)
Slug: submittal-management

## Research Goal

Understand what a construction Submittal Management application really is: the object it manages (the submittal), the review/approval process it digitizes, the parties involved, the lifecycle and decision semantics, the register it maintains, and where its boundaries sit against RFI Management, Construction Document Management, Construction Project Management, Construction Closeout Management, and generic approval workflow software.

## Initial Boundary

Hypothesis before research:

- A submittal is a contractor-side proposal (shop drawings, product data, samples) sent to the design team for approval before fabrication/installation.
- The management application is the submittal log/register plus the routed review workflow.
- Closest neighbors: RFI Management (sibling formal process), Construction Document Management (the attachments are documents), Construction Project Management (submittals are one instrument family in the coordination record), Construction Closeout Management (open submittals block acceptance).
- Known term collision: "submittal" in staffing-agency management means a candidate submitted to a client — a different domain entirely (noted, not a taxonomy conflict since this leaf is scoped to §17).

Pre-hung seams from sibling passes (must be ratified from this side):

- construction-project-management (2026-09-07): submittals/approvals named as one instrument family of the cross-organization coordination record.
- rfi-management (2026-09-09): "A submittal *proposes* an item for *approval* with revision cycles; an RFI *asks a question* seeking an *answer*." Boundary declared from the RFI side.
- construction-document-management (2026-09-08): "a submittal register is a specialized controlled register, but the approval workflow — not the general document record — is its defining core."
- construction-closeout-management (2026-09-07): closeout consumes submittal closure state; the submittal workflow itself is a distinct upstream Type.

## Research Questions

1. What exactly is a submittal as an object (fields, attachments, references)?
2. What is the canonical lifecycle (statuses) and the decision vocabulary (responses)?
3. Who are the parties and roles (submitter, manager/coordinator, reviewers, official reviewer, distribution)?
4. What links the submittal to the rest of the project record (spec sections, drawings, RFIs, cost, schedule)?
5. What does the register look like and how is it worked (aging, due dates, response times, completion)?
6. How do revision cycles work (resubmit vs new revision)?
7. What happens after the decision (distribution, closeout, procurement)?
8. How do products without a dedicated submittal object realize the process (workflow-over-documents)?
9. Where are the boundaries vs RFI / document management / generic approval workflow?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

1. **Procore** — contractor-operated market-leading platform; dedicated Submittals tool with the richest workflow machinery (Ball in Court, Submittal Manager, sequential approval workflows). Tier: GC/mid-market to enterprise.
2. **Autodesk Build (Autodesk Construction Cloud)** — suite module; submittal items + packages + spec sections; configurable multi-step review workflows. Tier: mid-market to enterprise.
3. **Oracle Aconex** — enterprise/owner-side platform with a mail/document-control heritage; submittals realized as review workflows over registered documents (Workflows module recommended; dedicated Submittals module optional). Tier: enterprise capital projects.
4. **Kahua** — owner- and GC-side enterprise platform; Submittal Items + Submittal Packages sub-applications with a register-first, coordinator/official-reviewer gatekeeper model. Tier: owners, agencies, enterprise GCs.
5. **Fieldwire by Hilti** — field-first jobsite platform (Business Plus tier); company-based routing with a linear status ladder. Tier: SMB / field crews / specialty contractors.

## Sources

All fetched 2026-09-10 unless noted.

- Procore Support — Submittals (user guide root): https://support.procore.com/products/online/user-guide/project-level/submittals
- Procore Support — "What is a submittal?": https://support.procore.com/faq/what-is-a-submittal
- Procore Support — "What are the default submittal statuses in Procore?": https://support.procore.com/faq/what-are-the-default-submittal-statuses-in-procore
- Procore Support — "What are the default submittal responses in Procore?": https://support.procore.com/faq/what-are-the-default-submittal-responses-in-procore
- Procore Support — "Upload and Submit a Submittal": https://v2.support.procore.com/product-manuals/submittals-project/tutorials/upload-and-submit-a-submittal
- Procore Support — "Best Practices: Submittal Workflow Management": https://support.procore.com/products/online/user-guide/project-level/submittals/best-practices-submittals/best-practices-submittal-workflow-management
- Autodesk Help — "Work with Submittals": https://help.autodesk.com/cloudhelp/ENU/Build-Submittals/files/Work_Submittals.html
- Autodesk Help — "Process Submittal Items": https://help.autodesk.com/cloudhelp/ENU/Build-Submittals/files/work-submittals/Process_Submittal.html
- Autodesk Help — "About Autodesk Build": https://help.autodesk.com/view/BUILD/ENU?guid=What_is_Build
- Autodesk blog — "Customize RFI and Submittal Review Workflows with Autodesk Build": https://www.autodesk.com/blogs/construction/rfi-submittal-review-workflows-autodesk-build
- Oracle Aconex Support Central — "Submittals" (implementation guide): https://help.aconex.com/implementation/submittals
- Kahua Help — "Submittals": https://help.kahua.com/main/Content/4-DocumentationMngmt/Submittals/submittals.htm
- Kahua — GSA Quick Reference Guide "Packaged Submittals" (PDF): https://www.gsa.gov/system/files/Kahua_Packaged_Submittals_v001.pdf
- Kahua support release notes (Nov 2025 — QC Review workflow, official-response visibility): https://support.kahua.com/support/solutions/articles/24000100132-november-2025-release-notes
- Fieldwire Help Center — "Introduction to the Submittals Workflow in Fieldwire": https://help.fieldwire.com/hc/en-us/articles/7160473659419-Introduction-to-the-Submittals-Workflow-in-Fieldwire
- Fieldwire — Specifications product page (submittal extraction): https://www.fieldwire.com/specifications

Source-access notes: all five vendors' operational documentation was reachable. Kahua's help pages are configuration-oriented (role/workflow options) rather than end-to-end tutorials; Aconex's dedicated Submittals module is documented mainly at implementation-guide level (the vendor recommends the Workflows module instead), so module-internal field detail is thinner for those two. No claims are made beyond what the fetched pages support.

## Product Observations

### Procore (evidence layer A)

- **Definition (vendor's own FAQ)**: "A submittal refers to the written and/or physical information provided by a responsible contractor (i.e., contractors and subs) to the general contractor. This information is submitted to the design team for approval of equipment, materials, etc. **before they are fabricated and delivered to the project**." Formats: shop drawings, cut sheets on equipment, material samples. Purpose: "architect and engineer to verify that the correct products and quantities will be installed on the project in compliance with the design documents/contract documents."
- **Process (vendor's own FAQ)**: created by a PM/contractor to request information from the responsible subcontractor about items planned for fabrication/installation; subcontractor submits; project and design teams review for compliance with drawings and specs; once approved, returned to the subcontractor, "which signifies that the work (or fabrication) is approved for construction."
- **Approval workflow chains (documented examples)**: Subcontractor (submits) → GC (reviews) → Architect (reviews) → GC (distributes) → Subcontractor (receives and prepares work); longer chains add Engineer, CM, Owner's Rep as intermediate reviewers.
- **Roles**: Submittal Manager ("responsible for overseeing the submittal throughout its lifecycle"; default configurable per project), Submitter(s), Approver(s) in a sequential workflow; Reviewer (forward for review); Distribution list.
- **Ball in Court**: explicit field naming who currently holds the action; system "waits until all required users in each step of a submittal's workflow respond before shifting the Ball In Court to the next step." Reject workflows option: a Rejected / Revise-and-Resubmit response automatically sets Ball in Court to the Submittal Manager for intervention.
- **Statuses (defaults)**: Open (waiting for approver responses; default for new), Draft (created, not yet in workflow; due dates do not advance), Closed. Custom log statuses supported.
- **Responses (defaults)**: APPROVED ("work may proceed"; some orgs rename to 'REVIEWED'), APPROVED AS NOTED ("work may proceed provided that it complies with the notations... and contract documents"), FOR RECORD ONLY, PENDING, REJECTED ("work may NOT proceed"), REVISE AND RESUBMIT ("work may NOT proceed until a revision... is resubmitted"), SUBMITTED, VOID ("an official response... has been discharged", e.g. duplicate). Custom responses supported (the FAQ headline says "nine (9) default" but enumerates eight — count not asserted anywhere in my outputs). Procore explicitly advises organizations to define their own legal definitions for each response.
- **Register**: the Submittals tool "enables you to organize your submittal log by division"; log export (CSV/PDF), custom reports, approver response-time report, open submittals report (company level), search/filter, configurable columns, views.
- **Structure extras**: Submittal Packages (grouping items; bulk review/distribute), Submittal Builder (generate the submittal log from the Specifications tool), numbering (option to append spec section to submittal number), spec-section organization, cost codes, schedule calculations (optional; lead-time based), related items, privacy flag, revisions ("Create a Submittal Revision"; best-practice doc warns that reverting ball-in-court overwrites recorded dates/responses and recommends revisions instead for managing resubmissions), close/revise/distribute, redistribute, QR codes, mobile viewing, PDF markup stamps, AI-powered submittal generator (release note 03/2026), email notifications at each step.
- **Permissions**: Admin/Standard tiers on the tool; granular permission to apply workflow templates; only Admin can change status (per create-a-submittal notes); Standard users can update workflow on their own drafts.

### Autodesk Build / Autodesk Construction Cloud (evidence layer A)

- **Definition (vendor help)**: "Submittals are used to submit documents, materials, and equipment for approval within the project team." Positioning: "Create and track submittal items and manage all information in a single submittal log."
- **Structure**: Submittal **items**; **Submittal Packages** (group by tangible elements like floors/rooms); **Submittal Spec Sections** (categorize items); attachments with review/annotation workflow.
- **Workflow**: workflow bar (current stage; "Pending review from" vs "Responded: X"); workflow table (dates, attachments, comments, Response/Action column); custom review workflows with **multiple review steps and multiple reviewers per step**, each reviewer submitting a formal response (approved/rejected) with attachments; the **Submittal Manager serves as the gatekeeper** — "track statuses and close or revise submittal items at any step in the workflow" (vendor blog).
- **Roles/companies**: Submittal Manager, Responsible Contractor, Reviewers — assignable as individual users, roles, or whole companies; role/company assignment drives notifications and access automatically.
- **Planning dates**: Required Date, Required Approval Date, Required on Job Site Date, Lead Time.
- **Terminal actions**: **Close and distribute** ("formally conclude the review process... submittal information is distributed to all individuals involved"); **Create new revision** (assign responsible contractor, submitter due date, watchers); **Void** (invalidate; item no longer relevant). Managers/admins can close or revise regardless of status except Draft/Void.
- **References**: link items to Assets, Files, Forms, Issues, PCOs, Photos, RFIs, other Submittals, Schedule, Sheets.
- **Surfaces**: list view with Ball-in-court and "Pending action from" columns; detail page (general info, workflow bar/table, planning, activity log with @mentions, references); mobile review (iOS/Android); export as report; search/filter; AutoSpecs integration generating submittal items from specifications (vendor blog 2025).

### Oracle Aconex (evidence layer A, implementation-guide depth)

- **Definition (vendor implementation guide)**: "Submittals, also sometimes referred to as Supplier or Vendor Documents, are **groupings of documents that illustrate how the construction team plans to build elements of the project**. Submittals are made up of things like shop drawings, material and product data and samples. Submittals are usually issued for review and approval **per an agreed upon schedule**."
- **Realization**: Aconex "is routinely used for the management of both the Submittals themselves as well as the reviews associated with them." Vendor recommends the **Workflows** module (document review workflows) as the primary mechanism; a dedicated **Submittals** module is optional and "very effective... when you have advance knowledge of the schedule and details of the submittals" (register of packages and associated dates created in advance; percentage-of-completion reporting per submittal, visible to issuing/receiving organizations).
- **Cross-org participation**: Workflows and the Submittals module require all participants to be Aconex users; **Transmittals** allow both users and non-users to participate in the process.
- **Record posture**: both mechanisms "make use of a registered document so wet signatures can be included in the document itself." Real-time status/response tracking and reporting across all organizations involved (Workflows). Supporting tools: Templates (repeatable review processes) and Review Sets (standardized review terminology per step).

### Kahua (evidence layer A)

- **Definition (vendor help)**: "The submittal process in construction is where contractors on a project submit product data or samples of the materials and equipment they intend to use on the project for review by the architects and engineers. This ensures that the proper items are used and installed on the project."
- **Structure**: **Submittal Items** sub-application (individual items submitted for review); **Submittal Packages** sub-application (multiple items grouped); **submittal register** — "a list of anticipated submittal items, can be created ahead of time."
- **Process**: "Submittal packages or submittal items are routed to the appropriate parties for review and responses are returned to the contractors involved."
- **Roles (GSA quick-reference + help)**: Submittal Coordinator (manages the process; may differ from the creator), Submitting Vendor (EXT-Contractor), **Official Reviewer** (determination authority; configuration option "Only Official Reviewer can Mark Complete"), optional **Consultant Reviewers**; responses "are filtered back through the Official Reviewer who shares the comments with the Submittal Coordinator who then returns the reviewed submittals to the Submitting Vendor."
- **Gatekeeper pattern (release notes)**: "Submittal Consultant Responses are visible only to the Official/Primary Responder and the Owner's Representative. This ensures that the Official/Primary maintains their role as the 'gatekeeper,' determining the final content of the official response sent back to the Coordinator."
- **Workflow options (configuration)**: Owner Directed workflow; **register & material tracking** — the submittal vendor submits their list of items for submission "including fabrication time"; "Allow Submitter to Submit to Review"; resubmission-period recalculation on Revise action (vendor resubmission period default); QC Review workflow (optional QC Reviewer role with QC Notes/QC Response fields, pre-submission quality check).
- **Hierarchy**: configuration inherits down domain → partition → project.

### Fieldwire by Hilti (evidence layer A)

- **Positioning**: "Fieldwire Submittals streamline the approval process for material and equipment that will need to be installed on-site. Submittals are centralized and accessible to all individuals on the Project." Paid module (Business Plus).
- **Status ladder (linear, explicit)**: Draft → Requested → Pending review → Pending approval → Pending close → Closed; plus Void (and Unvoid). Status counts surfaced at the top of the log.
- **Numbering**: assigned when the submittal moves from Draft to Requested; by company (submitting company's code as prefix) or by specification (spec number as prefix).
- **Specification link**: one spec section per submittal (CSI MasterFormat number + name), many submittals per section; submittals can be **extracted directly from uploaded specifications** (spec book → submittal log) or CSV-imported; closed submittals can be imported for record.
- **Types**: Shop drawings, Sample, Product data, O&M manual, Warranty, Report, Certificate, Mockup, Other.
- **Dates**: Submission due / Submission received / Sent for approval / Response due / Response received / Response time (computed); On-site date; Lead time.
- **Parties**: Assignee (current owner of next action), Reviewers (additional responders; automatically become watchers), Watchers, CC'd external emails; **Lead company** model (lead company sees all non-draft submittals; non-lead companies can only send submittals to the lead company; only lead company can assign to external email addresses); "Respond on behalf" / "Submit on behalf" with mandatory received-date entry.
- **Decision**: Response dropdown at Pending approval (customizable response options via "Manage responses"); rejection reason + attachments displayed in the submittal body; independent of response, item moves to Pending close; Assignee closes (optional distribution-list email) → non-editable state; reopen possible; "Create revision" returns the item to Requested with new assignee/due date.
- **Email participation**: external email assignees receive the submittal by email and reply; replies and attachments auto-logged in the activity feed.
- **Downstream**: approved Plans/Shop-drawings submittals can be sent to the Plans module; CSV/PDF exports; per-submittal PDF with attachments.

## Cross-product Comparison

| Dimension | Procore | Autodesk Build | Oracle Aconex | Kahua | Fieldwire |
|---|---|---|---|---|---|
| Submittal as object | dedicated item in Submittals tool | submittal item | grouping of registered documents (Workflows) or Submittals module | Submittal Item record | submittal record |
| Register/log | submittal log (by division), export/reports | single submittal log | register of packages + dates (module); real-time status reporting (workflows) | submittal register created ahead of time | Submittals tab with status counts |
| Spec-section anchoring | spec sections tool; numbering can append spec section; builder generates log from specs | spec sections categorize items | (via document attributes) | references | one spec section per item; extraction from spec book |
| Review loop | sequential workflow steps; Submitter/Approver roles; Ball in Court | multi-step, multi-reviewer custom workflows; Submittal Manager gatekeeper | review workflow over registered documents; templates + review sets | routed to Official Reviewer + consultant reviewers; coordinator returns to vendor | assignee + optional reviewers; linear statuses |
| Decision vocabulary | APPROVED / APPROVED AS NOTED / REVISE AND RESUBMIT / REJECTED / FOR RECORD ONLY / PENDING / SUBMITTED / VOID (customizable) | formal responses per reviewer (approved/rejected) + manager close | review-step responses (review sets standardize terminology) | official determination via Official Reviewer; Mark Complete gated | customizable response dropdown (Approved, Approved as Noted, ...) |
| Revision cycle | submittal revisions (recommended over ball-in-court revert) | Create new revision | resubmit through workflow | Revise action; resubmission period | Create revision → back to Requested |
| Closure | Close; distribute; redistribute | Close and distribute | completion of review workflow | Mark Complete (Official Reviewer gated) | Close → non-editable; distribution email |
| Grouping | Submittal Packages | Submittal Packages | packages of documents | Submittal Packages | none observed |
| Planning dates | due dates per workflow step; schedule calculations (optional) | Required / Required Approval / Required on Job Site / Lead Time | agreed schedule for issuance | submission due; vendor fabrication time; resubmission period | submission/response due & received; response time; on-site date; lead time |
| Cross-org participation | collaborators by email; permissions per company | roles/companies as reviewers | transmittals reach non-users | vendor + reviewers across orgs | external email assignees; email reply capture |
| Downstream | cost codes; schedule tasks; related items | references (RFIs, PCOs, issues, schedule...) | registered documents feed archive | responses returned to contractors; owner visibility | approved shop drawings → Plans module |
| Operator posture | contractor-operated suite | suite module | neutral/owner-side enterprise | owner/GC enterprise | field-first SMB |

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The submittal item of record** — a numbered, attributable record on which a submitting party proposes the specific materials, products, equipment, or execution content (shop drawings, product data, samples) it intends to use, referenced to the design/specification requirement that calls for it.
   - Remove → a file attachment or a generic document record; the propose-for-approval transaction disappears.
2. **The cross-organization review decision loop** — the proposal is routed to a party holding review authority (typically the design team, reached through intermediaries) which returns a recorded decision on the same record — proceed (with or without notations), revise and resubmit, or reject — where a non-proceeding decision sends the item back for revision, cycling until final disposition; the recorded decision is the official answer that governs whether procurement/fabrication/installation may proceed.
   - Remove the decision → document distribution; remove the propose→approve semantics (substitute question→answer) → RFI Management.
3. **The submittal register** — the project's log of submittal items — required/anticipated entries planned ahead of need plus in-flight items — each carrying status, dates, and the party holding the next action, worked as a management surface (aging, overdue, response times, completion against the required set).
   - Remove → one-off approval exchanges with no managed population; "management" disappears.

Jointly-held load-bearing:
- 1 alone = an attachment record
- 2 alone = a generic approval workflow engine
- 3 alone = a spreadsheet of required items
- 1+2 without 3 = ad-hoc approvals, not a managed process
- 1+3 without 2 = a log nobody routes through
- 2+3 without 1 = workflow machinery over nothing

### L1 — Common Mature Structure

- Spec-section anchoring (the item tied to the specification section that demands it; spec-driven register generation)
- A process-manager role (Submittal Manager / Coordinator) owning the item's lifecycle
- Multi-step review chains with intermediate reviewers (GC → consultant → design side), one official decision path
- A decision vocabulary in the approve / approve-with-notations / revise-and-resubmit / reject family
- Revision cycles as first-class objects (new revision, not overwrite)
- Distribution of the decided submittal back to the submitting side (close-and-distribute)
- Due dates per step, response-time measurement, overdue/aging surfaces
- Grouping into packages
- Related-item links (RFIs, drawings, files, cost, schedule)
- Email participation for external parties; mobile viewing/review; PDF export of the record
- Custom statuses/responses per organization

### L2 — Variant / Optional

- Status vocabulary shape: two-state (Open/Closed + Draft) vs linear multi-step ladders (Draft→Requested→Pending review→Pending approval→Pending close→Closed)
- Realization substrate: dedicated first-class object vs review workflow over registered documents (Aconex pole)
- Operator posture: contractor-operated vs owner-directed (Kahua Owner Directed workflow) vs neutral correspondence platform
- Register-first planning (anticipated items created ahead of need; vendor-supplied registers with fabrication times — Kahua) vs create-as-needed
- QC review step before submission (Kahua)
- Material/vendor tracking attached to the submittal process (Kahua)
- Lead-time/schedule calculations feeding the schedule (Procore optional)
- Cost-code linkage (Procore)
- Numbering schemes (sequential, company-prefixed, spec-prefixed)
- AI submittal generation / spec extraction (era-current)
- QR codes, offline mobile (era-current)

### L3 — Vendor-specific (research notes only)

- "Ball in Court" (Procore's term for the single action owner; Autodesk uses "Ball in court" column too — term shared by the two, still vendor vocabulary)
- "Submittal Manager" (Procore/Autodesk role name), "Submittal Coordinator" / "Official Reviewer" (Kahua)
- Procore's nine-default-responses claim (FAQ enumerates eight; count not asserted)
- Procore "Enable Reject Workflows" auto-routing to Submittal Manager
- Kahua "Only Official Reviewer can Mark Complete", "Recalculate Submission Due from Vendor Date on Revise Action"
- Autodesk "Close and distribute" button; Bridge sharing of closed submittals; AutoSpecs
- Fieldwire Lead Company crown model; "Respond on behalf"/"Submit on behalf" with mandatory received dates; send-to-Plans for approved shop drawings
- Aconex percentage-of-completion reporting for the Submittals module; Review Sets terminology

## Historical / Market-Sample Check (§24)

The paper-era practice this software digitized: the specification divides the work into sections; each section's "submittals" paragraph requires the contractor to submit shop drawings, product data, and samples for review; the contractor (via the GC) transmits them; the design team reviews and returns them bearing a rubber-stamp action — the classic approve / approve-as-noted / revise-and-resubmit / reject action set — while the contractor's office keeps a submittal log (a ledger of item, spec section, dates sent/returned, status, and who holds the ball). Every leg of the L0 is satisfied with no software at all: the proposed item referenced to its spec section (1), the routed review returning a recorded decision with revision cycles (2), and the log worked by the contractor's office (3). The modern response vocabularies are direct descendants of the review stamp; the register is the digitized ledger. The definition therefore does not depend on any current implementation pattern (dedicated objects, cloud workflows, AI extraction).

Also checked against the non-suite realization: Aconex manages submittals as review workflows over registered documents rather than a dedicated submittal object — the L0 holds without a first-class "submittal" entity, so the definition must be written at the transaction level, not the object-schema level.

## Vendor-specific Findings

See L3 above. Additional observations kept out of the final document: Procore's specific permission tiers and granular permissions; Kahua's domain/partition configuration inheritance; Autodesk's Bridge cross-project sharing; Fieldwire's per-seat licensing notes and 20 MB email attachment limit; exact status-label spellings per product.

## Boundary Findings

1. **vs RFI Management (closest sibling; ratifies the RFI pass's pre-hung seam).** Both are numbered, stateful, cross-organization project processes with due dates and closure, and every sampled product ships them as separate tools. The structural difference: an RFI *asks a question* and resolves with an *answer* recorded by the design side; a submittal *proposes an item* and resolves with an *approval decision* that authorizes (or blocks) procurement/fabrication. Substituting propose→approve for question→answer turns one Type into the other. Remove test holds both ways.
2. **vs Construction Document Management (ratifies that pass's seam).** The submittal's attachments are documents, and the submittal register is a specialized controlled register — but the defining core is the approval transaction, not the document record. A submittal without revision-controlled document custody is still a submittal; a document register without the propose→approve loop is document management.
3. **vs Construction Project Management (ratifies).** Submittals are one instrument family inside the coordination record. This leaf is the dedicated process for that family: deeper decision vocabulary, revision cycles, spec anchoring, register planning. Strip the rest of the suite (schedule, money, field) and the submittal process stands alone; strip the submittal process from the suite and it remains Construction PM.
4. **vs Construction Closeout Management (ratifies).** Closeout consumes submittal closure state (open submittals are swept before acceptance) and submittal deliverables (O&M manuals, warranties) feed the closeout record — but the submittal workflow itself is upstream and runs throughout construction, not only at the end.
5. **vs Engineering Document Management.** The design-org sibling hosts transmittal/submittal *distribution packages* (issuing documents outward). The construction submittal is the *propose→approve transaction over contractor-proposed content*. Direction and resolution differ: EDM transmittals issue controlled documents; submittals seek decisions on proposed ones.
6. **vs generic Approval Workflow Platform (§10).** A generic approval engine routes items for sign-off, but lacks the submittal's domain semantics: spec-driven demand, design-team review authority, the approve/revise-and-resubmit/reject decision family tied to fabrication and procurement, revision cycles as project record. The submittal loop is construction-specific.
7. **vs Change Order Management.** A rejected or revise-and-resubmit submittal may reveal that the specified product is unavailable or the design must change — the consequence enters the change process through an explicit conversion. The submittal itself carries no agreed money or scope (same rule as the RFI pass).
8. **Term collision (not a taxonomy issue).** "Submittal" in staffing-agency management means a candidate submitted to a client for a job order — an entirely different domain (staffing-agency-management-system pass, 2026-09-08). This leaf is scoped to construction by its directory position; no conflict.

## Uncertainties

- Procore's FAQ states "nine (9) default submittal responses" but enumerates eight; the count is not asserted anywhere in my outputs.
- Aconex's dedicated Submittals module is documented at implementation-guide level only; its internal register fields and module mechanics are not deeply evidenced. Claims about Aconex are limited to what the implementation page states (workflows-over-registered-documents realization, register of packages with dates, percentage-of-completion reporting, transmittals for non-users).
- Kahua's end-to-end default workflow is configuration-dependent (domain administrators customize); observations are from help overview + GSA quick-reference + release notes, which show the role model and options but not one canonical status ladder.
- Whether "distribution after decision" is universal: observed in Procore, Autodesk, Fieldwire, Kahua (responses returned to contractors); Aconex implies it via the review workflow returning documents. Treated as common-mature, not definitional.
- Owner-side direct approval authority: evidenced (Procore chains include Owner's Rep; Kahua owner-directed workflows; Kahua release notes mention Owner's Representative visibility), but the frequency/depth of owner-as-final-approver configurations is not quantified — phrased as variant.

## Final Synthesis

Submittal Management is the construction project's formal proposal-approval system. Its world has three load-bearing structures: the submittal item of record (a numbered proposal of specific products/shop-drawing content, referenced to the specification that demands it), the cross-organization review decision loop (routed to review authority, returning an official decision — proceed / revise and resubmit / reject — that governs whether fabrication and procurement may proceed, cycling through revisions until disposition), and the submittal register (the project's planned-and-in-flight log of these items, worked for aging, accountability, and completion). Everything else — spec-section numbering schemes, the review-stamp response vocabulary, packages, planning dates, distribution lists, email participation, mobile, AI extraction — is common mature structure or variant machinery, not the definition. The paper-era submittal log + transmittal + review stamp satisfies the core with no software, and the workflow-over-registered-documents realization (Aconex) satisfies it without a dedicated submittal object.
