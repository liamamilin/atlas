# Government Records Management

## Overview

A **Government Records Management** application governs a public agency's records: the content that documents the agency's decisions, transactions, and obligations. Records are held as evidence of public business, protected from change and loss, retained under a legally anchored retention and disposal schedule, and ultimately disposed of through an authorized, evidenced process that ends either in destruction or in transfer to the government's archives authority.

The defining structure is small:

```text
Agency record (content as evidence of public business)
└── Retention & disposal schedule
    │   (record classes → retention periods → disposition actions)
    │   anchored in public-records law, with disposition authority
    │   issued or approved by an external statutory archives/records authority
    └── Governed disposition (review → certificated destruction
        or transfer to the archives authority → recorded proof)
```

Three properties, jointly. If any one is removed, the product is no longer recognizable as this Type:

- **Records as evidence of public business** — while content is under record governance, editing and deleting it are controlled by the governing rules rather than by ordinary user discretion.
- **A schedule operating under external statutory authority** — the distinctive property of the government regime. The retention and disposal schedule is anchored in public-records law, and the authority to dispose — to destroy — is issued by, or formally approved by, an archives or records oversight authority outside the operating agency. An agency cannot lawfully destroy records on its own say-so; destruction is lawful only under an approved schedule item.
- **Governed, evidenced disposition with two endings** — end-of-retention leads to an authorized, reviewable act with recorded proof. Temporary records are destroyed (with that authority); records of enduring value are transferred to the archives authority rather than destroyed. Silent deletion is precisely what the system exists to prevent.

Everything else commonly associated with these products — classification automation, legal holds, audit trails, physical box tracking, digitization programs, freedom-of-information modules, compliance dashboards — is standard market capability, not what makes the product this Type. The paper-era practice (a file room, a schedule issued by the state archives, typed destruction authorities, boxed transfers to a records center) realizes the same three-part skeleton without any software at all.

## Users & Context

Primary operators:

- **Agency records officer / records manager** — owns the agency's records program: maintains the schedule and its record classes, ensures content is classified under it, monitors compliance, and oversees disposition. In government this role is often named or mandated by statute and answers to the oversight authority, not only to the agency's own management.
- **Departmental record coordinators** — staff in each business unit who file and classify records in their unit's terms, manage local access, and prepare material for cutoff and disposition.
- **Disposition reviewers / authorizing officers** — the people who examine records at end of retention and approve destruction, extension, or transfer; in the government regime, disposal action ultimately traces to an externally approved schedule item, and the authorization is itself recorded.

Secondary participants:

- **Business staff** — create and receive the records (correspondence, case files, contracts, permits, meeting files) and meet the governance layer mostly indirectly: their content is captured, classified, and protected while they keep working.
- **Archivists of the oversight authority** — external participants on the other side of the boundary: they issue or approve the schedule's disposition authorities, determine which records have enduring value, and receive transfers of permanent records.
- **Legal counsel and FOI/public-records officers** — place holds, answer requests for records, and consume the evidence the system produces.
- **Auditors and oversight bodies** — inspect the program itself; compliance with the records regime is externally monitored, not self-assessed.

Typical context: national, state/provincial, and local government agencies operating under a public-records or archives statute. The work is rule-driven and cyclical rather than transactional: maintain the schedule, keep the record population classified under it, respond to triggers and holds, run disposition cycles, and demonstrate compliance to outside scrutineers. Both electronic and physical records are routinely governed by the same machinery — paper case files, permits, and boxed inactive records remain a substantial part of many agencies' holdings.

## Core Model

### The Defining Core

```text
Retention & disposal schedule
│   (record classes / series → retention periods → disposition actions)
│   authority: issued or approved by the external archives/records authority
│
├── governs ──→ Agency record
│               (content under record governance:
│                change & deletion controlled by the rules)
│                   ├── electronic and physical items, one schedule
│                   └── linked to a trigger event (where event-based)
│
└── ends in ──→ Disposition
                (review/authorization → destruction  or  transfer to archive
                 → recorded proof)
```

**Agency record.** The central managed object: content that documents public business and must be kept as evidence. What makes the record state real is enforcement — while an item is governed, deleting it is blocked or restricted regardless of the user's ordinary permissions, and editing is controlled by the rule's strictness. The record population includes both electronic objects (documents, email, case records) and physical items (files, volumes, boxes), commonly managed in one schedule so that a single record class can cover both forms.

**Retention & disposal schedule.** The governance instrument: a structured set of record classes, each carrying a retention period, the event that starts the clock, and the disposition action at the end. What makes the government form of this instrument distinctive is where its authority comes from. In private-sector records management the organization defines its own schedule from its legal analysis. In the government regime, the schedule's disposition authority is external: national, state, or provincial archives and records authorities issue general schedules and approve agency-specific ones, and destruction is lawful only under an approved item. The agency operates the schedule; it does not own the authority behind it. Schedule entries commonly record their legal basis and the class of business they cover, because the point of the instrument is to demonstrate that retention and destruction trace to law rather than to housekeeping preference.

**Disposition.** The governed end of the lifecycle, with two canonical endings. For temporary records — the majority by volume — retention ends in destruction, executed only after review/authorization and recorded as proof (what was destroyed, when, under which schedule item, by whom). For records judged to have enduring value — the "permanent" or archival portion — the ending is not destruction but transfer: the records are accessioned into the custody of the archives authority, where a different Type (archives management) takes over. An agency that cannot show, for any disposed record, the authority it acted under has failed at the system's core purpose.

### Standard Capabilities of Mature Products

These are widespread in current products and expected by buyers; they make the defining core workable. They are not what makes the product this Type.

- **Classification and declaration machinery** — record status and schedule classes applied by users, by rules (content type, keywords, sensitive information), or by machine-learning classification; filing into the schedule at capture time or later.
- **Legal holds / freezes** — suspension of disposition for litigation, investigation, or audit; held records cannot be destroyed and typically cannot be altered. Holds outrank the schedule until lifted.
- **Audit trail** — who did what to which record and when: declaration, access, change attempts, and disposition decisions, logged as evidence by default.
- **Event-based retention** — the clock starts at a named event (case closed, employee separated, contract ended, license expired); records whose trigger has not fired stay in place, because their retention clock has not started.
- **Physical records machinery** — containers and boxes, storage locations and facilities, circulation with charge-out, and transfer tracking, so the paper holdings live under the same schedule as the electronic ones.
- **Capture and integration** — collecting content from the places work happens: collaboration platforms, email, line-of-business systems (case management, permitting, finance), scanning and capture of paper — into the system of record or under governance where it lives.
- **Role separation** — records officers, departmental coordinators, reviewers, and ordinary staff hold distinct authorities; disposition rights are deliberately narrow.
- **Search and retrieval** across the governed population, including by class, event, or hold status — retrieval is a duty, not a convenience: records must be findable when the law or a request demands them.
- **Compliance reporting and exports** — disposition certificates/reports, audit exports, program-level reporting to the oversight authority.
- **Public-access support** — surfacing and delivering records to citizens and to freedom-of-information / public-records request handling; some products bundle a request-processing module, others integrate with one.

### One Structure, Many Implementations

The core model is written in conceptual terms. Products realize the concepts differently:

```text
Concept:   Record population
Implementations:  records filed into the system of record at capture;
                  content governed in place across connected platforms;
                  physical items tracked alongside electronic ones

Concept:   Schedule under external authority
Implementations:  agency schedules approved item-by-item by the archives
                  authority; general government-wide schedules adopted
                  wholesale; state-issued schedules for local governments

Concept:   Disposition endings
Implementations:  certificated destruction workflows; transfer/accession
                  packages handed to the archives authority; frozen
                  disposal queues while a hold is active
```

A reader who has only seen one implementation — say, a cloud service classifying email and documents — should still be able to recognize a clerk's office tracking boxed permit files under a state-issued schedule as the same Type.

## How It Works

### Establish the schedule

```text
Identify the agency's record classes and the law that bears on each
→ adopt applicable general schedules and/or draft agency-specific items
→ submit for approval/issuance by the archives or records authority
→ publish the approved schedule; keep it current as law and programs change
```

The schedule is a living instrument: new programs create new record classes, statutes change, items are superseded. Disposed-under authority is always the currently approved item.

### Capture and classify

```text
Content is created or received (correspondence, case files, forms, email,
scanned paper) → captured into the system of record or governed where it lives
→ classified under a schedule class (by the filer, by rule, or by model)
→ record state applied: protection, retention clock basis, disposition path fixed
```

In records-centric deployments everything filed is a record from the start. In governance-layer deployments the system reaches into the platforms where staff work and applies record status where the rules demand it, ideally without disrupting the work itself.

### Retain and protect

```text
Record state enforced: edit/delete restricted per the class's strictness
→ for event-based classes: the trigger event fires, the clock starts
→ legal hold placed (litigation, audit, investigation) → disposal suspended,
   content frozen
→ physical items: stored, circulated, tracked; inactive material moves
   to storage facilities under the same schedule
→ actions logged as they occur
```

### Dispose

```text
Retention period ends (and no hold is active)
→ records flagged as due for disposition
→ reviewers inspect content, metadata, and history
→ authorized decision: destroy (per the approved item) or extend
   or relabel under another class
→ permanent/archival records: prepared and transferred to the
   archives authority instead of destroyed
→ proof recorded: what was disposed or transferred, when, under which
   schedule item, by whom
→ evidence available to auditors and the oversight authority on demand
```

The disposition cycle runs continuously across the agency's holdings — it is a program, not a one-time cleanup, and its outputs are exactly the artifacts an auditor or oversight body will ask to see.

### Core vs standard vs optional

**Defining core** — without these, not this Type:

- agency records under record governance (evidence of public business)
- a legally anchored retention & disposal schedule operating under external statutory authority
- governed, evidenced disposition ending in destruction or transfer to the archives authority

**Standard capabilities** — present in most mature products:

- classification/declaration automation, holds, audit trails, event-based retention
- physical-records machinery, capture/integration, role separation, search
- compliance reporting to oversight bodies, public-access support

**Optional / variant** — depends on jurisdiction, segment, and packaging:

- certification regimes for records functionality; digitization programs
- essential/vital-records and disaster-recovery programs
- bundled FOI/request-processing and government process automation (correspondence, briefings)
- privacy/minimization and AI-governance extensions

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Schedule / file-plan manager

The records officer's primary work surface.

- lists record classes with retention periods, trigger bases, disposition actions, and their legal/authority basis
- primary actions: adopt or draft classes, submit for approval, publish approved items, revise as law changes

### Capture and filing surfaces

Where content enters governance.

- capture of electronic items and scanned paper; classification under schedule classes; record-status indicators
- primary actions: capture, classify, declare as record, correct a classification

### File / search surfaces

The day-to-day retrieval layer for coordinators and business staff.

- organized views of the record population by class, unit, or container; search across records and metadata
- primary actions: locate records, view status (active, event pending, on hold, due for disposition), retrieve physical items

### Physical-records tracking

The paper half of the world.

- boxes/containers, storage locations and facilities, circulation and charge-out, transfer manifests
- primary actions: register containers, move/store, charge out and return, prepare transfers

### Disposition queue and authorization

The reviewer's work surface at end of retention.

- items due for disposition grouped by class, with hold status visible
- primary actions: review content and history, approve destruction, extend retention, relabel, prepare archival transfer, record the authorization

### Audit, reporting, and compliance

The evidence layer for oversight.

- action histories per record; program-level views (compliance status, disposition statistics, overdue actions)
- primary actions: generate disposition proofs and audit exports, report to the oversight authority

### Public-access surfaces

Where the regime meets the citizen.

- delivery of records to requesters (secure links, tracked access) and support for freedom-of-information / public-records request handling, native or through an integrated module

## Important Rules / Behaviors

### Destruction requires external authority

The load-bearing rule of the regime: no agency user — including senior administrators — can lawfully destroy records on their own authority. Destruction happens only under an approved schedule item, and the approval lives with an outside archives/records authority. Items that are unapproved, withdrawn, or superseded cannot be used for disposition.

### Disposition is never silent

End of retention leads to review and recorded authorization, not to automatic deletion. The system records what was destroyed or transferred, when, under which item, and by whom. This proof is a first-class output, routinely demanded by auditors and oversight bodies.

### Holds outrank the schedule

A legal hold or freeze suspends disposition for the affected records regardless of what the schedule says; frozen content cannot be destroyed and typically cannot be altered. Holds come from litigation, audits, investigations, and request activity, and are lifted explicitly.

### Unlawful destruction is a violation the regime takes seriously

Destroying records without authority is not a housekeeping mistake but a compliance breach. In the most directly researched regime this is explicit in law: the agency has a statutory duty to report threatened or actual unlawful destruction to the oversight archives, and equivalent regimes treat unauthorized destruction as an offense subject to oversight. The system's controls (blocked deletion, audit trail, disposition authorization) exist to make such violations both prevented and provable.

### Unfired events mean unstarted clocks

For event-based classes, retention does not begin until the named event occurs; records whose trigger has not fired are retained. Once the event fires, it cannot generally be undone.

### Two audiences see different systems

Business staff largely see capture, filing, and search. The records officer and reviewers see the schedule, the queues, and the authorization machinery — and outside the agency, the archives authority and auditors see the program's outputs. Mature products make the first experience unobtrusive and make the last two demonstrable.

## Variants

Common forms of the Type in the market:

- **Records-centric system of record (EDRMS)** — the records system is the agency's repository: everything filed is a record from the start, organized by the schedule, often with government process automation (correspondence, briefings) attached. Especially common in national and state/provincial agencies.
- **ECM suite with a records module** — a broader content platform where the records machinery is a certified component; common where agencies run wide document/process workloads.
- **Cloud manage-in-place governance** — a SaaS service that connects to collaboration platforms, file shares, and legacy archives and governs records where they live, with automated classification and continuous policy application; increasingly common for digital-heavy agencies.
- **Physical-records-first deployments** — programs centered on boxed holdings, storage facilities, and transfer logistics, with the same schedule/authorization machinery; common in local government and long-established agencies, often combined with digitization programs.
- **Jurisdiction shapes** — the same structure takes local form in each legal system: national-archives-approved agency schedules and government-wide general schedules in some federal systems; state-issued retention and disposal authorities for public offices in others; state-issued schedules for local governments elsewhere. The instruments differ by name; the external-authority structure does not.

A variant remains a variant unless it changes the core model. If disposition authority moves fully inside the operating organization and the archival transfer ending loses its counterpart, the product has become general enterprise records management rather than a variant of this Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Enterprise Records Management | regime-specialized sibling | same governance spine (record state + schedule + evidenced disposition), but the schedule is organization-defined and disposition authority is internal. In the government form, the schedule is legally anchored and destruction authority is external, and transfer to the archives authority is a canonical ending. Strip the external-authority property → ERM |
| Enterprise Content Management | adjacent sibling; packaging overlap | ECM centers the working content lifecycle (capture, collaborate, version, publish) in a governed repository; this Type centers the retention/disposition governance machinery. Records capability usually ships inside content platforms |
| Archives Management System | downstream handoff | archives take permanent custody of transferred records — preservation, description, and public access to material of enduring value. This Type governs the active lifecycle and *ends* in the transfer to archives |
| FOI / Public Records Request Platform | interlocking neighbor | request processing centers on an external requester's formal request and its statutory clock; this Type centers the record population and its schedule. Request outcomes depend on records the system governs; products bundle both without merging |
| Government Open Data / Transparency Portal | different object and lifecycle | proactive publication of datasets and meeting materials, not governance of the record population |
| Document Management | weaker cousin | filing and versioning convenience without schedule-bound governance, external disposition authority, or lawful-disposition proof |
| Legal Hold Management | consumer of the hold primitive | LHM centers the preservation-duty process (notices, custodians, releases) across systems; this Type implements the hold that freezes its own records |
| Public Sector Case Management | upstream producer | case systems generate the records (case files, decisions, permits) that this Type then captures, classifies, and disposes of |

The boundary with Enterprise Records Management is the most consequential one, because the two Types share their machinery. The structural difference is who owns the authority to destroy: the operating organization, or an external statutory archives/records authority. The boundary with Archives Management is the cleanest: one Type's disposition ending is the other's beginning.

## Representative Products

- Laserfiche — document and records platform with a strong US state & local government base (clerks, recorders, records departments)
- Objective Nexus — records-centric information-governance suite designed for government agencies (Australia/New Zealand federal and state)
- RecordPoint — cloud manage-in-place records and data governance with public-sector deployments (US and Australia)
- OpenText Content Manager (formerly HPE Records Manager / TRIM lineage) — classic records-centric government EDRMS; widely cited as a market reference but its documentation was not directly verifiable during research, so no structural claims rest on it

The core model was checked across these postures (ECM platform, records-centric suite, manage-in-place SaaS, plus the classic records-centric lineage as unverified reference) and grounded in the statutory machinery of two researched jurisdictions (a national archives authority and a state records authority) to avoid over-fitting the definition to any one country, level of government, or packaging.

## Sources

Research date: **2026-09-08**

Regime (domain-authority) sources:

- U.S. National Archives and Records Administration — FAQs About Records Management in General — https://www.archives.gov/records-mgmt/faqs/general.html
- U.S. National Archives and Records Administration — Records Control Schedule (RCS) FAQs — https://www.archives.gov/records-mgmt/faqs/rcs.html
- U.S. National Archives and Records Administration — Federal Records Management FAQ index — https://www.archives.gov/records-mgmt/faqs
- State Records NSW (Australia) — Recordkeeping resources, including Retention and Disposal Authorities and compliance monitoring — https://staterecords.nsw.gov.au/recordkeeping

Product sources (official product pages):

- RecordPoint — Records Management — https://www.recordpoint.com/platform/records-management
- Laserfiche — Document and Records Management — https://www.laserfiche.com/products/records-management/
- Objective — Objective Nexus — https://www.objective.com/products/objective-nexus

> Sourcing limitations: live operational help documentation for the sampled products was not reachable from the research environment on 2026-09-08 (vendor documentation portals rendered by script, or access blocked). Product-level statements in this document therefore rest on official product-page wording rather than operational manuals, and precise operational specifics (authorization workflows, review-chain structure, container schemas, numeric limits) are intentionally not stated. The government-specific structure — externally approved disposition authority, destruction-versus-transfer endings, oversight reporting — is grounded in the two domain-authority sources above rather than in vendor claims. One additional market reference (OpenText Content Manager) could not be verified at all and is identified as such.

Detailed evidence, product-by-product observations, cross-product comparison, the historical/market-sample check, and the sibling-Type boundary analysis are recorded in the paired Research Notes.
