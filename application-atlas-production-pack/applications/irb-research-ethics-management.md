# IRB / Research Ethics Management

## Overview

An **IRB / Research Ethics Management** application is a research institution's system of record for the ethical and regulatory review of research involving human subjects. It manages the full life of a research protocol: preparation and submission by the research team, pre-review by ethics-office staff, review and determination by the institutional review board (ethics committee), and continued oversight of the approved study — amendments, continuing reviews, reportable events, and closure.

Its purpose is to make the institution's participant-protection obligations operational: every study that needs ethics review is captured as a persistent record, every review action is structured and routed, every determination is recorded and communicated formally, and the institution retains a complete compliance memory of each study.

The defining core is deliberately small: a protocol record, a submission-driven review workflow ending in a recorded determination, the committee's review machinery, and the post-approval oversight lifecycle. Everything else commonly associated with these products — smart forms, training verification, dashboards, multi-board consolidation, regulatory-grade e-signatures — is widespread but not what makes the system this Type.

## Users & Context

Primary users:

- **Principal investigator and research team** — prepare and submit protocols, respond to reviewer comments, request amendments, submit continuing reviews and reportable events, and retrieve approval letters.
- **IRB / ethics office staff (analysts, coordinators, administrators)** — pre-review submissions for completeness, route them, manage meetings, generate correspondence, configure forms and workflows, and maintain the protocol records.
- **Committee members and reviewers** — access assigned submissions, review materials, record comments and recommendations, and participate in convened-board determinations.
- **IRB chair** — assigns reviewers, determines review routes (exempt / expedited / full board), and often issues or signs determinations.

Secondary users:

- **Organizational approvers** (department chairs, deans, signatory authorities) — approve submissions in a routing chain before they reach the ethics office.
- **Compliance leadership** — monitor pipeline, statuses, and reporting across the institution's research portfolio.

The context is institutional: universities, academic medical centers, hospitals, and other organizations that conduct or oversee human-subjects research and are accountable for its ethical review. The system is used continuously across the whole research portfolio, not once per study.

## Core Model

The system's world is organized around one central object and four structures held together:

```text
Protocol (unit of record)
├── Research team (PI + personnel, with roles and attestations)
├── Submissions (initial / amendment / continuing review / reportable event / closure)
│     └── routed through a configured review path
│           ├── staff pre-review
│           ├── designated reviewer (exempt / expedited routes)
│           └── convened committee (full board)
│                 └── recorded determination + formal correspondence
└── Post-approval oversight (amendments, continuing review, events, closure)
```

### The protocol as unit of record

A **protocol** (often called a study) is a persistent, identified record of one research study subject to ethics review. It carries the study title, the research team — principal investigator, co-investigators, and other key personnel with defined roles — and accumulates every submission, review, decision, comment, and letter over the study's life. The protocol record is the institution's compliance memory: years after approval, the complete review history remains retrievable. Without this persistent record, the system is just a form processor.

### Submissions as the unit of work

Review actions are structured **submissions** made against the protocol. Across the researched products the same submission types recur:

- **Initial review** — the first application for a new study.
- **Amendment / modification** — a proposed change to an approved study.
- **Continuing review / renewal** — the periodic re-review that keeps an approval alive.
- **Reportable events** — adverse events, unanticipated problems, protocol deviations, participant complaints.
- **Closure / final report** — ending the protocol's active life.

Each submission is a versioned package of forms and attachments. Institutions configure their own forms; mature products provide form builders with branching logic and mandatory fields so the institution's review requirements are enforced at preparation time.

### The review workflow to a recorded determination

A submission moves through a configured path. The typical shape:

```text
Research team completes submission
→ PI (and often all key personnel) certify / attest
→ organizational approver chain (department, signatory authority)
→ ethics office pre-review (completeness, classification)
→ review route:
     exempt determination (staff/designee)
     expedited review (designated member)
     full board review (convened committee)
→ determination recorded and issued as formal correspondence
```

Determinations are recorded outcomes, not informal emails. Common determination types across products: **approved**, **modifications required** (returned to the team to address comments, then resubmitted and re-certified), **returned/disapproved**, **not human-subjects research / no engagement**, and route changes (e.g., not eligible for expedited review). The determination is communicated as a formal letter generated by the system and archived on the protocol.

### The committee as reviewing actor

The ethics board is a first-class actor in the system, not just a final signature. The system carries the board's machinery: reviewer assignment (often matched by expertise or sensitivity), distribution of submissions to reviewers, reviewer comments bound to specific sections of the submission, convened-meeting handling — agendas, meeting dates, minutes — and decisions attributed to the board. Reviewer comments captured electronically typically form the basis of minutes and stipulations to the research team.

### Post-approval oversight lifecycle

Approval is not the end. The approved protocol remains under management: amendments must be reviewed before implementation, continuing reviews recur on a cycle with system reminders as approvals near expiry, reportable events must be submitted and dispositioned, and the study is eventually closed with a final report. This lifecycle is what makes the protocol record a compliance memory rather than a one-shot application.

### Concept vs implementation

The core model is conceptual; implementations vary:

```text
Concept:  protocol record        → implementations: study folder, package series, protocol with form types
Concept:  submission             → implementations: submission, package, form instance
Concept:  review route           → implementations: exempt/expedited/full-board queues, panels
Concept:  determination          → implementations: decision types, approval letters, status changes
Concept:  oversight lifecycle    → implementations: renewal reminders, event forms, closure reports
```

## How It Works

### Initial review

```text
Create protocol (title, team, personnel roles)
→ complete the institution's submission form (branching questions, attachments: protocol, consent documents, recruitment materials)
→ certify / attest (PI, often all key personnel)
→ route through organizational approvers
→ ethics office pre-review — returned for clarification if incomplete
→ assigned a review route (exempt / expedited / full board)
→ reviewer(s) or committee review; comments recorded
→ determination issued:
     approved → approval letter archived, study may proceed
     modifications required → team addresses comments, resubmits, re-certifies
     disapproved / returned → recorded with reasons
```

### Amendments and continuing review

Once approved, any material change goes in as an amendment submission; the same route-and-determine loop runs at smaller scale. Continuing reviews recur on the approval cycle — mature products generate automatic reminders as the approval nears expiry, and an expired approval stops the study. Reportable events (adverse events, deviations) are submitted as they occur and dispositioned by the office or board.

### Convened board review

For full-board submissions: the office prepares the agenda, reviewers are assigned and complete their reviews (often with worksheets) before the meeting, the board convenes and records its decision, and the determination is issued afterward as correspondence. Submission deadlines are commonly tied to meeting dates.

### Capability tiers

**Defining core** — protocol record; structured submissions (initial, amendment, continuing review, reportable events, closure); routed review to a recorded determination with formal correspondence; committee review machinery; post-approval oversight.

**Common mature structure** — configurable smart forms with branching logic; section-bound comment threads and version comparison on resubmission; role-based dashboards and task lists; email notifications at workflow transitions; determination-letter generation and document archiving; training/certification verification surfaced on the protocol; ancillary/parallel reviews (biosafety, radiation, scientific); reporting and audit trails; meeting management (agendas, minutes).

**Optional / variant** — multi-board consolidation (IRB + animal care + biosafety + conflict of interest in one system); multi-institution operation and external-IRB reliance agreements; regulatory-grade features (e-signatures, Part 11-style controls) for regulated contexts; pre-approval "protocol development" records; national-portal submission integration (regional); institution-built vs commercial deployment.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Researcher dashboard / protocol list

The researcher's entry surface: their protocols with statuses (in progress, pending action, approved, expiring, expired), pending tasks, and notifications. Primary actions: create a protocol, open a submission, complete an assigned task, respond to comments.

### Submission form

The structured questionnaire the research team completes — sections covering the study team, research description, participant population, consent, risks and benefits, and attachments. Branching logic shows only relevant questions; mandatory fields and required uploads gate completion. Primary actions: edit sections, attach documents, certify, submit.

### Reviewer workspace

What a committee member sees: assigned submissions with review materials (protocol, consent forms, attachments), review worksheets, and comment entry bound to specific sections. Primary actions: record comments and recommendations, submit a review, participate in a determination.

### Office / administrator workspace

The ethics office's control surface: submission queues for pre-review, routing and reviewer assignment, meeting and agenda management, letter generation, form and workflow configuration, and reporting. Primary actions: pre-review, return for clarification, assign reviewers, schedule for meeting, issue determinations, configure forms.

### Protocol detail / history

The protocol's complete record: all submissions with their statuses, review comments and responses, decisions, letters, and event history — the institutional memory surface. Primary actions: view history, download approved documents and letters, start a new submission.

## Important Rules / Behaviors

- **Certification gates submission.** The PI (and commonly all key personnel) must certify or attest before a submission is accepted; resubmissions after modifications typically require re-certification.
- **Submitted packages are locked.** Once a submission is under review it is locked; changes happen through a new submission (amendment or revision), preserving the record of what was reviewed.
- **Modifications-required is a loop, not a rejection.** The common outcome is a return to the team with section-bound comments; the submission is resubmitted after all comments are addressed, and review resumes.
- **Review route determines the path.** Exempt and expedited submissions are typically processed by staff or a designated reviewer without a meeting deadline; full-board submissions are tied to convened meetings and their deadlines. The board can change the route a submission initially received.
- **Approvals expire.** Continuing review keeps an approval alive; systems track expiry and generate reminders, and an expired approval halts the study.
- **One pending action at a time.** Several products allow only one open submission per protocol at a time, keeping the review record unambiguous.
- **Access follows role and study assignment.** Researchers see their own studies; reviewers see assigned submissions; office staff and administrators see the institution's portfolio. Access on a study is granted at the minimum level needed.
- **The record is the compliance evidence.** Statuses, comments, decisions, and letters are retained and attributable — the system's audit trail is a primary institutional artifact.

## Variants

- **Commercial suite module** — IRB review as one app inside a research-administration suite, with record linkage to sponsored projects and other compliance boards.
- **Standalone platform** — dedicated IRB/ethics review systems, sometimes spanning multiple board types and multiple institutions.
- **Institution-built systems** — universities operating their own research-compliance systems with the same core structure.
- **Regulated-context deployments** — configurations with e-signatures and regulatory-grade controls for clinical-trial contexts.
- **Multi-institution / reliance configurations** — one reviewing IRB serving multiple institutions, with reliance requests as a submission type.
- **Regional variants** — systems oriented to national ethics-review portals (e.g., UK-style IRAS integration); the core model is the same, the submission plumbing differs.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Animal Research Ethics / IACUC Platform | Same review machinery, different subject domain: animal-use protocols rather than human-subjects research. Sibling Type. |
| Research Compliance Management | Broader program-level compliance management (multiple boards, COI, training programs, audits); the protocol-review loop is one part. |
| Research Administration Platform | Governs the funding lifecycle (proposals, awards); ethics review is a different obligation. Linkage between the two (congruence checks) is integration, not identity. |
| Clinical Trial Management System / CTMS | Manages study operations (sites, participants, visits, data) after approval; this Type governs the review and oversight of the protocol itself. |
| Peer Review Platform | Reviews manuscripts for publication quality; no participant-protection mandate, no compliance lifecycle. |
| Ethics & Conduct Management (corporate) | Organizational ethics policies, hotlines, and conduct cases; not research-protocol review. |
| Approval Workflow Platform | Generic routed approvals; lacks the protocol record, committee machinery, ethics determinations, and oversight lifecycle. |

The closest sibling is the IACUC platform: the two share the same structural core and differ in the regulatory domain of the review. The most important boundary is against generic approval workflow tools — what distinguishes this Type is not routing, but the protocol record, the ethics committee as reviewing actor, and the participant-protection semantics of the determination.

## Representative Products

- Cayuse Human Ethics (Cayuse)
- IRBNet (Research Dataware / WCG)
- RASCAL (Columbia University, institution-built)
- eProtocol (Key Solutions)
- InfoEd Human Studies / IRB & Ethics

The core model was checked against institution-built and paper-era practices to avoid over-fitting to any single commercial implementation.

## Sources

Research date: **2026-09-10**

- Cayuse — Human Ethics product page: https://www.cayuse.com/compliance-management/human-ethics/
- Cayuse IRB User Guide (customer-hosted official guide): https://www.depts.ttu.edu/research/responsible-research/irb/assets/pdf/Cayuse-IRB-User-Guide.pdf
- UC Merced — Cayuse IRB Researcher and Reviewer manuals: https://cayuse.ucmerced.edu/ , https://rci.ucmerced.edu/
- IRBNet — product site and user manual: https://www.irbnet.org/ , https://www.marshall.edu/ori/files/IRBNet-user-manual-072020.pdf
- Columbia University — RASCAL FAQ, CUIT service page, HRPO protocol life-cycle document: https://www.rascal.columbia.edu/help/irbfaq.html , https://www.cuit.columbia.edu/research-compliance
- Key Solutions eProtocol — customer guides (Berkeley, Stanford, Wayne State, Allina Health, NEOMED)
- InfoEd — Research Compliance product page and customer job aids: https://www.infoedglobal.com/products/research-compliance
- Iowa State University — OneAegis submission and review: https://compliance.iastate.edu/research-ethics-compliance/irb/submission-and-review
- NIH NHLBI — CDS-IRB IRBManager review-process document: https://www.nhlbi.nih.gov/sites/default/files/media/docs/CDS_IRB_Review_Process.pdf
- Cornell University — RASS-IRB guide: https://guide.rass.cornell.edu/institutional-review-board-for-human-participant-research

> Sourcing limitation: UK/EU-oriented ethics-review vendor documentation (rascal.ac.uk) could not be reached from the research environment; regional systems are under-sampled and geography-specific claims are avoided. Vendor marketing metrics (review-time percentages) were observed but not treated as evidence. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
