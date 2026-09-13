# Standards Development Platform

## Overview

A **Standards Development Platform** is a collaborative platform used by Standards Development Organizations (SDOs) to manage the full lifecycle of creating, reviewing, approving, and publishing technical standards.

The defining structure is:

```text
Standard/Project of record
└── Committee/Working Group (identified participants)
    └── Draft document (with version history)
        └── Comment/Feedback (with disposition tracking)
            └── Consensus mechanism (ballot/vote)
```

The platform supports the structured process by which technical experts develop consensus-based specifications — standards, codes, protocols, or guidelines — that guide design practices, manufacturing methods, construction quality, operational safety, or interoperability across industries.

When the dominant surface shifts to governance of people without technical content lifecycle, the product is drifting toward Committee Management. When it shifts to generic document storage without consensus machinery, it becomes Document Management. When it certifies people or products against existing standards rather than creating them, it becomes Certification Management.

## Users & Context

The primary users are participants in the standards development process:

- **Working group members / technical experts**: Draft the technical content, provide comments, and participate in consensus-building.
- **Committee officers / chairs**: Lead the working group, manage the drafting process, resolve comments, and advance the project through lifecycle stages.
- **Editors**: Ensure the document conforms to the SDO's editorial rules and formatting requirements.
- **Voters / ballot group members**: Participate in formal balloting to approve or reject the draft standard.
- **Staff / committee managers**: Administer the process, manage rosters, schedule meetings, and ensure procedural compliance.

Secondary users include:

- **National mirror committee members**: In international SDOs (ISO, IEC), national representatives who consolidate their country's position and submit national comments.
- **Public reviewers**: In some SDOs (IEEE, ISO), members of the public who can comment during a public review period.
- **Liaison representatives**: Representatives from related organizations who participate in an advisory capacity.

The work environment is typically remote and asynchronous, with participants distributed across organizations, geographies, and time zones. Standards development is a volunteer-driven process, and participants often balance standards work with their primary employment.

## Core Model

### The Defining Core

```text
Standard/Project of record
└── Committee/Working Group (identified participants)
    └── Draft document (with version history)
        └── Comment/Feedback (with disposition tracking)
            └── Consensus mechanism (ballot/vote)
```

Five properties. If any one is removed, the product is no longer recognizable as a Standards Development Platform:

- **Standard/Project of record** — A persistent identified record of a standards development effort, carrying scope, owner, and a lifecycle from proposal to publication. Without this, the product becomes generic document collaboration.
- **Committee/Working Group** — A group of identified participants (experts, members, organizations) authorized to develop the standard. Without this, the product becomes individual authoring.
- **Draft document with version history** — The evolving technical content, with tracked changes and versions. Without this, the product becomes meeting minutes or a task tracker.
- **Comment/Feedback mechanism** — A structured way for participants to provide feedback on the draft, with disposition tracking (accepted, revised, rejected). Without this, the product becomes document approval without feedback.
- **Consensus mechanism (ballot/vote)** — A formal or informal process to determine whether the draft has achieved consensus and can advance. Without this, the product becomes a document repository without consensus.

### Standard Capabilities

Mature platforms commonly add:

- **Lifecycle stage progression** — Defined stages (proposal, draft, review, ballot, approval, publication) with gates that must be passed before advancing.
- **Role-based permissions** — Different roles (officer, editor, member, voter) with different capabilities at different stages.
- **Comment resolution workflow** — Comments are reviewed by a comment resolution group, dispositioned, and incorporated into the draft.
- **Meeting management** — Scheduling, attendance tracking, agendas, minutes.
- **Document templates and formatting rules** — Ensuring drafts conform to the SDO's style guide and editorial directives.
- **Integration with publication systems** — Handoff to the publishing/distribution platform once the standard is approved.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Specific implementations vary:

```text
Concept:          Standard/Project
Implementations:  ISO Work Item, IEEE PAR, ASTM Project, IETF Internet-Draft

Concept:          Committee/Working Group
Implementations:  ISO TC/SC/WG, IEEE Standards Committee/WG, IETF WG, W3C Working Group

Concept:          Draft document
Implementations:  XML (NISO STS), Word document, PDF, plain text (I-D format)

Concept:          Comment/Feedback
Implementations:  In-document commenting, ballot comments, mailing list discussion

Concept:          Consensus mechanism
Implementations:  Formal ballot (75% approval), weighted balloting, rough consensus (IETF)
```

## How It Works

### Propose and authorize a new standard

```text
Identify a need for a new standard
→ Submit a project proposal (scope, justification, timeline)
→ Review and approve the proposal (by a governance body)
→ Authorize the project and assign it to a committee/working group
→ Form the working group (recruit participants, balance interests)
```

### Draft the standard

```text
Working group members collaborate on the draft
→ Editors and authors write and revise content
→ Track changes and maintain version history
→ Hold meetings (virtual or in-person) to discuss technical issues
→ Iterate until the working group reaches internal consensus
```

### Review and comment

```text
Circulate the draft for review (within the committee or to external stakeholders)
→ Participants submit comments (technical, editorial, general)
→ Comments are collected, organized, and made visible to the group
→ A comment resolution group reviews each comment
→ Each comment is dispositioned: accepted, revised, or rejected
→ Accepted changes are incorporated into the draft
```

### Ballot for consensus

```text
When the draft is ready, initiate a formal ballot (or informal consensus call)
→ Form a ballot group (balanced by interest category, if required)
→ Ballot group members vote: approve, disapprove (with comment), or abstain
→ Achieve required response rate and approval threshold
→ If substantive changes are made, conduct a recirculation ballot
→ Resolve remaining comments and iterate until consensus is reached
```

### Approve and publish

```text
Submit the approved draft to a review committee (procedural check)
→ Governance body approves the standard
→ Editors perform final editorial review and formatting
→ Publish the standard (PDF, HTML, XML, print)
→ Distribute to members, customers, and the public
```

### Maintain and revise

```text
Published standards are periodically reviewed (typically every 5 years)
→ Confirm (no changes needed), revise (update), or withdraw
→ If revision is needed, initiate a new project and repeat the cycle
```

### Core vs Common vs Optional

Capabilities fall into three tiers:

**Defining core** — without these, not a Standards Development Platform.

- Standard/project of record with lifecycle
- Committee/working group of identified participants
- Draft document with version history
- Comment/feedback mechanism with disposition tracking
- Consensus mechanism (ballot/vote)

**Common mature structure** — present in most modern platforms.

- Lifecycle stage progression with gates
- Role-based permissions (officer, editor, member, voter)
- Comment resolution workflow
- Meeting management (scheduling, attendance, minutes)
- Document templates and formatting rules
- Integration with publication systems

**Variant / optional** — depends on SDO governance, geography, or scale.

- Weighted balloting (by organization size or interest category)
- Public review period (non-members can comment)
- National mirror committees (international SDOs)
- Patent policy compliance (disclosures, licensing commitments)
- Open source development tools (GitHub, open source platforms)
- XML-based structured authoring (NISO STS)
- Content quality checks (automated validation against editorial rules)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Project / Standards Dashboard

The primary entry surface for staff and committee officers.

- Lists all active projects with status, stage, owner, and timeline
- Surfaces upcoming deadlines, open ballots, and pending actions
- Primary actions: create a new project, open a project, view ballot status

### Project Detail / Workspace

The working surface for a single standard.

- Project metadata (scope, committee, stage, timeline)
- Draft document(s) with version history
- Comments and comment resolution status
- Ballot history and results
- Meeting schedule and minutes
- Primary actions: edit the draft, add comments, initiate a ballot, advance the stage

### Draft Document / Editor

The surface where the technical content is authored and reviewed.

- The document text with track changes and version comparison
- Inline comments and proposed changes
- Content quality validation (if applicable)
- Primary actions: edit content, add comments, accept/reject changes, export

### Comment Management

The surface for reviewing and resolving comments.

- List of all comments with status (open, resolved, accepted, rejected)
- Comment detail (text, proposer, disposition, rationale)
- Link to the relevant document section
- Primary actions: review comments, disposition comments, incorporate accepted changes

### Ballot / Voting

The surface for conducting formal ballots.

- Ballot configuration (duration, quorum, approval threshold)
- Ballot group roster (balanced by interest category, if required)
- Voting interface (approve, disapprove, abstain, with comments)
- Ballot results (response rate, approval rate, comment summary)
- Primary actions: initiate ballot, cast vote, view results, close ballot

### Committee / Roster Management

The surface for managing participants.

- Committee roster with roles, affiliations, and interest categories
- Attendance and participation tracking
- Membership approvals, tenure limits, and reappointments
- Primary actions: add/remove members, assign roles, track attendance

### Meeting Management

The surface for scheduling and conducting meetings.

- Meeting calendar with agendas and materials
- Attendance tracking
- Minutes and action items
- Primary actions: schedule meeting, upload materials, record attendance, publish minutes

## Important Rules / Behaviors

### Lifecycle stages are gated

A project cannot advance to the next stage without meeting defined criteria (e.g., working group consensus, ballot approval, procedural review). The platform enforces these gates and prevents premature advancement.

### Ballot groups must be balanced

In many SDOs, no single interest category (e.g., producer, user, general interest) can comprise more than one-third of the ballot group. The platform tracks interest categories and alerts when balance is at risk.

### Comments must be dispositioned

Every comment submitted during a ballot or review period must be reviewed and dispositioned (accepted, revised, or rejected) with a rationale. Unresolved comments block advancement.

### Substantive changes require recirculation

If substantive changes are made to the draft after a ballot, a recirculation ballot is required to give voters an opportunity to review and respond to the changes.

### Roles and permissions change by stage

A participant's capabilities depend on their role and the project's current stage. For example, a working group member may be able to edit the draft during the preparatory stage but only comment during the enquiry stage.

### Procedural compliance is verified

Before publication, a review committee (e.g., IEEE RevCom, ISO CS) verifies that all procedural requirements have been met (proper balloting, comment resolution, balance, etc.).

## Variants

The Standards Development Platform type is implemented in many ways. Common variants:

- **International SDO platform** — Supports multiple national bodies, national mirror committees, and multi-language workflows (e.g., ISO/IEC OSD).
- **National SDO platform** — Supports a single country's standards development process, often with ANSI-accredited procedures (e.g., ASTM SpecBuilder, Stanza).
- **Technical society platform** — Supports a specific technical domain (e.g., IEEE SA for electrical/electronics engineering, ASME for mechanical engineering).
- **Informal consensus platform** — Uses "rough consensus and running code" rather than formal balloting (e.g., IETF Datatracker).
- **Open source standards platform** — Uses open source tools and processes for standards development (e.g., IEEE SA Open, IETF tools).
- **Code development platform** — Specialized for building codes and regulations, often with government adoption workflows (e.g., ICC using Stanza).

A variant should remain a **Variant**, not become a separate Type, unless the variant changes users, core objects, workflow or rules in a way that the Core Model no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Committee / Board Management | Focuses on governance of people (rosters, meetings, minutes) without the technical content lifecycle and consensus machinery |
| Document Management / CMS | Focuses on generic document storage, versioning, and access control without standards-specific lifecycle and consensus |
| Certification Management | Certifies people or products against existing standards rather than creating the standards themselves |
| Policy Management | Manages internal organizational policies rather than consensus-based external technical standards |
| Learning Management System / LMS | Delivers training and tracks learner progress; may be used for standards-related training but does not develop the standards |
| Project Management Application | Manages tasks, timelines, and resources; may be used within a standards project but does not provide the standards-specific lifecycle and consensus |

The boundary with Committee Management is the most important one, because the two Types often coexist in the same organization. The structural difference is whether the platform manages only the governance of people (committee management) or also manages the technical content lifecycle with consensus-building (standards development).

## Representative Products

- **ISO/IEC OSD (Online Standards Development)** — The platform used by ISO and IEC for collaborative standards development, built on FontoXML.
- **IEEE SA myProject / myBallot** — IEEE Standards Association's tools for standards development and balloting.
- **ASTM SpecBuilder** — ASTM's platform for collaborative document development and balloting, also offered as a white-label product.
- **IETF Datatracker** — The IETF's open-source tool for tracking Internet-Drafts and RFCs through the standards process.
- **Stanza (InfoBeans)** — A commercial platform for ANSI-accredited SDOs, used by organizations like ICC.

The Core Model was checked against multiple SDO governance models (formal balloting, rough consensus, weighted voting) and multiple technical domains (engineering, construction, IT, healthcare) to avoid over-fitting to a single process or industry.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces:

- ISO/IEC OSD — https://helpdesk-docs.iso.org/article/649-what-is-online-standards-development-osd, https://helpdesk-docs.iso.org/article/655-osd-permissions
- CEN OSD — https://boss.cen.eu/reference-material/guidancedoc/pages/drafting-in-osd/
- IEEE SA — https://standards.ieee.org/develop/etools/, https://standards.ieee.org/faqs/balloting-process/
- ASTM SpecBuilder — https://www.astm.org/standards-and-solutions/enterprise-solutions/specbuilder
- IETF Datatracker — https://datatracker.ietf.org/, https://datatracker.ietf.org/release/about
- Stanza (InfoBeans) — https://infobeans.ai/stanza/
- W3C Process — https://www.w3.org/policies/process/

> Sourcing limitation: Live fetch of vendor help-center articles was partially successful. Some vendor documentation (e.g., detailed IEEE SA Operations Manual sections, ASTM SpecBuilder user guides) was not fully accessible. Precise operational details (exact ballot durations, quorum thresholds, stage codes) are based on publicly available summaries and may vary by SDO. Such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison matrix, and historical / market-sample breadth check are recorded in the paired Research Notes.
