# Evidence Management System

## Overview

An **Evidence Management System** is the custody system of record that an investigative agency uses to track items — physical or digital — held because of their role in an investigation or legal matter. It records every item as a persistent, individually identified record; documents every change of possession, location, or access so that accountability for the item is unbroken and reconstructable at any time; and ensures that items leave custody only through recorded, authorized disposition.

The defining core is deliberately small:

```text
Evidence item of record
  (identified physical or digital item held for its role in a matter)
└── Chain of custody
    (every intake, transfer, movement, and access recorded as an
     attributed event — accountability never breaks)
    └── Controlled intake and authorized exit
        (items enter through recorded intake and leave only through
         recorded, authorized disposition)
```

Everything else commonly associated with these products — barcodes, storage-room shelf maps, automated disposition engines, prosecutor portals, camera ingestion, hashing — is widely supported by current products but is not what makes such a system what it is. A pre-digital property room operating on a paper property book, with numbered tags, signed sign-out lines, and disposition entries, satisfies the same core.

The system exists because an item's value as proof depends entirely on demonstrable integrity: if a court cannot be shown where an item has been and who has held it, the item's evidentiary value can be lost regardless of what the item is. That legal-accountability purpose separates this Type from inventory and asset tracking, which hold things for use.

## Users & Context

The center of gravity is the **evidence custodian / property-room staff**, for whom the system is a daily operations tool: receiving items, assigning identifiers, placing them in storage, processing check-outs and returns, running inventories, and moving items toward disposition.

Around the custodian:

- **Patrol officers** submit items collected in the field, often from the scene or a station intake point, with descriptions and required fields captured at the point of packaging.
- **Investigators and detectives** review the items in their cases, request items for further work, and organize them for presentation to prosecutors.
- **Supervisors and agency administration** oversee the health of the custody operation: audit results, backlog, storage pressure, and disposition approvals.
- **Prosecutors** (in deployments that expose external surfaces) consult evidence records and submit requests or authorizations electronically — for example, requesting laboratory analysis or approving return of an item to its owner.
- **Laboratory personnel** receive and return submitted items as part of the custody chain.
- **The public**, in some deployments, reports lost or found property through a public-facing intake surface that feeds the agency's custody process.
- **Administrators and IT** configure fields, workflows, storage structures, and the security model.

The operating context is the agency property room and its legal surroundings: secure storage, periodic inventories, accreditation audits, court calendars that pull items out on check-out, and jurisdiction-specific retention rules. Larger agencies may operate multiple offices or participate in multi-agency task forces, where items move between organizational units and accountability must follow them across the boundary. Security expectations are high — these systems are commonly operated under criminal-justice information security regimes, with role-based access, multi-factor authentication, and full audit logging.

## Core Model

### The Defining Core

**1. The evidence item of record.** Every item taken into custody is a persistent, individually identified record: what the item is, its category (such as narcotics, firearms, currency, electronics, documents, or digital media), who it is associated with, photographs or attached media, notes, and a unique identifier. The item — not the case, not the report — is the unit of custody. One item may be linked to more than one matter — some products let custodians designate which linkage is primary — and quantity-bearing items (such as currency or pills) may be split into child records when portions are consumed, sent to the lab, or separately disposed of.

**2. The chain of custody.** Every event that changes the item's possession, location, or accessibility is recorded as an attributed, time-stamped entry — who did it, when, why, and where the item went. The chain accumulates from intake onward and is effectively unalterable: corrections happen by adding recorded events (including recorded reversals), never by editing history away. For physical items the chain is a sequence of possession and location events; for digital items it generalizes to access events — every view, edit, download, or share of the authoritative copy is itself a custody event, and file integrity is verifiable through digital fingerprints (hashes) that prove content is unchanged.

**3. Controlled intake and authorized exit.** Custody is a bounded state, not indefinite storage. Items enter through a recorded intake bound to the matter that justifies holding them. Items leave only through recorded, authorized disposition: returned to an owner, released to another authority, destroyed, or otherwise resolved — with the authorization itself documented. Nothing silently enters or silently leaves.

Remove any one of the three and the Type collapses: without the item of record there is nothing to hold accountable; without the chain of custody the system is barcode inventory control; without controlled exit it is an indefinite archive.

### What Mature Products Add

These structures are standard in current products and make the custody core operable, but they are implementations rather than the definition:

- **Matter and person anchoring** — items attach to cases, with associated persons (owners, suspects, victims) and the officers who submitted them. Case linkage organizes work; the item record remains the custody anchor.
- **Identification and labeling machinery** — numbered identifiers rendered as printed barcode or QR labels, handheld and mobile scanners, and location labels. For digital items, identification is intrinsic (the fingerprinted file).
- **Storage machinery** — a structured hierarchy of storage locations (rooms, shelves, bins) with labels, containers such as boxes, and location-scoped visibility: users see only the storage areas they are permitted to access.
- **Circulation mechanics** — check-out with a configured reason and an expected return date, check-in with verification of condition, internal moves between locations, transfers between custodians or offices, and signature capture at the handover point. Overdue items generate follow-up notifications.
- **Verification machinery** — inventory reports, random or percentage audits, and discrepancy reports that surface items missing or in the wrong location for investigation.
- **Disposition machinery** — retention-driven review: items become eligible for review per agency rules, notifications go to the responsible officers and custodians, an authorized reviewer approves, and a configured disposal method is executed and recorded. Deployments can also configure hard blocks on prohibited exits — for example, destruction contingent on a documented court order, or stricter release gates for categories such as controlled substances.
- **Custody documentation** — chain-of-custody reports produced for trial preparation and audits.
- **Access governance** — role-based permissions commonly scoped by office and storage location, strong authentication (multi-factor authentication is common in this market), and comprehensive audit logging of the system's own activity.
- **Integration spine** — connections to records management systems (case data flows in), court and prosecution systems, laboratory systems, digital-evidence platforms, and sometimes towing/impound or purchasing systems.
- **Mobile surfaces** — field capture at the scene, mobile transactions, and mobile inventories, in some products with offline operation.

### One Structure, Two Realizations

The core model is written conceptually; current products realize it along two poles:

```text
Concept:            Custody event
Physical realization:   check-out / check-in / move / transfer, with scans and signatures
Digital realization:    view / edit / download / share of the authoritative copy, auto-logged

Concept:            Item integrity
Physical realization:   tamper-evident packaging, sealed containers, condition verification
Digital realization:    hash fingerprints validating content is unchanged

Concept:            Storage location
Physical realization:   labeled rooms/shelves/bins and containers with location barcodes
Digital realization:    the platform's own secure cloud store under access control
```

A reader who has only seen a physical property-room system should be able to recognize a digital-first evidence platform as the same Type, and vice versa.

## How It Works

### Intake: entering custody

```text
Item collected (scene / station / public submission)
→ packaged and documented at the point of collection
→ submitted to the property room
→ custodian receives it, records it as an item of record
→ identifier assigned and label printed
→ item linked to its case and associated persons
→ placed in a storage location (or into a container that is itself tracked)
→ first custody event recorded
```

The intake step is deliberately ceremonial: the moment an item becomes "evidence" is the moment the accountability chain begins, and the system is designed so no item exists in the building outside that chain.

### Circulation: the check-out / check-in loop

```text
Officer or investigator requests the item (with a reason)
→ custodian checks it out, expected return recorded, signatures captured
→ item is used (court, lab, investigation)
→ item returned and checked in; condition verified
→ item returned to its storage location
→ chain updated at every step
```

The loop is the heartbeat of the property room: a well-run room is one where items are constantly and legibly moving between custody states rather than accumulating untracked. Overdue check-outs generate notifications; some deployments configure rules that stop prohibited actions outright — for example, preventing the release of controlled substances to owners or the destruction of seized items without a documented court order.

### Verification: proving nothing is lost

```text
Scheduled or random audit / full inventory
→ items scanned and reconciled against records
→ discrepancies surfaced (missing, wrong location, unaccounted)
→ each discrepancy investigated and resolved as a recorded event
```

Verification is a standing discipline rather than an occasional cleanup: accreditation regimes commonly expect periodic inventories and random audits, and the system's reporting is built to make them routine.

### Disposition: leaving custody lawfully

```text
Agency retention rules make items eligible for review
→ notifications to responsible officers and custodians
→ reviewer authorizes (or items are held — case still active, appeal pending)
→ disposal method executed: return to owner, destruction, transfer to another authority, or another configured resolution
→ completion recorded as the item's final custody event
→ errors corrected by recorded reversal, not by deleting history
```

Disposition is where these systems earn their keep operationally: storage pressure is the chronic condition of property rooms, and the difference between a managed and an unmanaged room is measured in how far the disposition backlog is allowed to grow.

### The digital variant of the same loop

```text
Digital item ingested (camera fleet, file upload, public submission, third-party system)
→ fingerprint computed; integrity verifiable thereafter
→ organized into the case by tagging
→ access governed by role; every view/edit/download logged as a custody event
→ shared with authorized parties (prosecution, disclosure processes) as recorded transfers
→ redaction and transcription applied where disclosure requires it
```

The digital realization replaces physical possession with controlled access to the authoritative copy — but the accountability logic (identify, preserve integrity, record every transfer, exit lawfully) is identical.

## Interfaces

The surfaces below are described conceptually; layouts and names vary by product.

### Item profile

The custody anchor's home surface.

- typical information: identifier, description, category, associated persons, current location, current custodian status, chain of custody, media, notes, tasks, history
- primary actions: check out / check in, move, transfer, attach media and notes, print label, dispose, view full custody trail

### Case view with items

The investigator-facing organization of a matter's items.

- typical information: the case's item list, per-item status and location, associated persons and officers
- primary actions: open an item, submit a new item, organize items for prosecution, request actions

### Intake / booking surface

The point where items enter custody.

- typical information: item description, category, required fields, submitter, case linkage
- primary actions: record the item, assign identifier, print label, assign storage location

### Transaction surface (scan-first)

The property room's workbench, commonly driven by barcode scanning.

- typical information: scanned item or container, pending transactions
- primary actions: check in / check out, move, transfer, capture signatures

### Storage location browser

The map of where things are.

- typical information: location hierarchy, container contents, location-scoped item lists
- primary actions: locate an item, move items or containers between locations

### Inventory and audit tools

- typical information: audit scope, reconciled/unreconciled items, discrepancy lists
- primary actions: run inventory or random audit, record counts, open discrepancy investigations

### Disposition review queue

- typical information: items eligible for review, pending authorizations, pending destruction, disposal history
- primary actions: review eligibility, authorize or hold, execute and record disposal

### Dashboards

- typical information: items in intake, overdue check-outs, storage pressure, disposition backlog, category volumes
- primary actions: drill into lists, generate reports

### External and public surfaces (deployment-dependent)

- prosecutor/lab request and authorization surfaces; public lost-and-found property reporting; disclosure and redaction surfaces on the digital pole

### Mobile capture

- scene-side item creation, photo capture, transactions, and mobile inventories, in some products offline-capable

## Important Rules / Behaviors

- **The custody chain is append-only in effect.** History is not rewritten; corrections and reversals are themselves recorded events. This is the property that makes the record credible in court.
- **No unrecorded possession.** The system's operational discipline is that an item is always in exactly one recorded custody state — in storage, checked out to a named person, in transfer — and physical reality is expected to match.
- **Check-out has terms.** Reasons and expected returns are configured vocabulary; overdue items trigger follow-up. The circulation of items is governed, not informal.
- **Exit is legally gated.** Disposition requires documented authorization, and some products let agencies configure hard rules that block prohibited exits — for example, returning controlled substances to owners, or destroying seized items without a documented court order. Which gates exist and how they are configured is agency- and jurisdiction-specific.
- **Verification is standing policy.** Inventories, random audits, and discrepancy investigations are expected operating rhythm, commonly tied to accreditation requirements, rather than optional reporting.
- **One item, many matters.** An item may support multiple cases; some products let a custodian designate which linkage is primary. Splits of quantity-bearing items create related child records whose custody continues independently.
- **Integrity is verifiable.** Physical items move in sealed or documented packaging; digital items carry fingerprints that prove content has not changed since ingestion.
- **Access is scoped and audited.** Role-based permissions — commonly scoped by office and storage location — determine who can see and act on items, and the system's own usage is logged.
- **Retention drives review.** Items do not wait for someone to remember them; eligibility rules and notifications move the population toward lawful resolution.

## Variants

- **Physical property-room systems** — the classic realization: storage locations, containers, barcode circulation, inventory discipline, disposition programs; many now also manage digital items in the same chain.
- **Digital-first evidence platforms** — cloud systems centered on ingested files from cameras, uploads, and public submissions, with access-event custody, hashing, redaction, transcription, and disclosure workflows; some expand into physical evidence management as well.
- **Unified physical + digital systems** — one custody chain spanning shelves and files, with digital items hashed and physical items barcoded.
- **Suite-embedded modules** — evidence custody delivered as part of a broader public-safety records suite alongside reporting, dispatch, and booking, trading specialist depth for integration.
- **Public-intake extensions** — portals where residents report lost or found property, feeding agency custody intake.
- **Multi-office and multi-agency operation** — items moving between organizational units or task-force partners with accountability preserved across the boundary.
- **Deployment and hardware variation** — government cloud vs on-premises; scanner/printer/signature-pad ecosystems; RFID alongside barcodes in some deployments.
- **Adjacent specializations** — some vendors ship related custody domains as separate products (agency asset/quartermaster management, sexual-assault kit tracking), which share machinery but hold different kinds of things for different purposes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Law Enforcement Case Management | tightly interlocked | the case is the system of record for investigation narratives, persons, and outcomes; the evidence system of record is the item in custody — custody machinery (chain, check-out, storage, disposition) does not exist on the case side |
| eDiscovery Platform | adjacent (legal-technology pole) | preserves, searches, and produces electronically stored information for legal process; the discipline is preservation and production, not person-attributed possession of items |
| Legal Hold Management | adjacent | suspends routine destruction of records under a hold; it obliges retention, whereas evidence custody accounts for possession item by item |
| Enterprise Records Management | adjacent | retains documents per retention schedules for organizational/statutory memory; evidence items are held for their role in a matter, with custody attributed to individuals |
| Government Records Management | adjacent (public-sector sibling) | agency-wide records lifecycle; lacks item-level custody chains and legal-exit gates |
| Enterprise Asset Registry | adjacent | tracks items the organization owns and uses; evidence items are held as proof, preserved rather than consumed, with legally gated exits |
| Inventory Management System | contrast | exists to make stock available; a vendor in this Type draws the line explicitly — evidence tracking that is "no more than barcode-based inventory control" is missing the point |
| Archive Storage Management | contrast | storage-tier management for data; no custody semantics |
| Court Case Management | downstream consumer | exhibits handled at court; transfers to and from the agency appear here as custody transactions |
| Digital Evidence platforms (as a variant) | within this Type | the digital-first realization of the same custody model; whether standalone or integrated with physical evidence, it carries the same defining core |

The most important boundary is with **Law Enforcement Case Management**: the two are designed to interlock (case data flows in, items attach to cases), and suite vendors ship both. The test is the system of record — remove custody machinery and whatever remains is a case file system; remove case narratives and reporting and whatever remains is still an evidence custody system.

## Representative Products

- Tracker Products (SAFE) — property/evidence specialist, physical and digital evidence in one custody chain, cloud delivery
- FileOnQ (EvidenceOnQ) — property/evidence specialist, configurable platform, on-premises delivery, integrated digital-evidence sibling
- Axon Evidence — digital-first evidence platform in the camera ecosystem, cloud delivery
- Mark43 RMS — evidence custody as a module of a cloud public-safety records suite

The defining core was checked against pre-digital property-room practice (paper property books, numbered tags, signed custody and disposition entries) and against non-implementation-specific custody contexts, so the definition does not assume barcodes, cloud delivery, hashing, or automation.

## Sources

Research date: **2026-09-07**

- Tracker Products — homepage and FAQ: https://trackerproducts.com/ ; SAFE Support Guide (section structure): https://guide.trackerproducts.com/home
- FileOnQ — homepage: https://fileonq.com/ ; EvidenceOnQ product page and FAQ: https://fileonq.com/evidence-management-system/
- Axon — Axon Evidence product page: https://www.axon.com/products/axon-evidence
- Mark43 — corporate site and RMS product page: https://www.mark43.com/ , https://mark43.com/platform/mark43-rms/
- JusticeTrax (intended lab-side sample) — site unreachable during research; not used as evidence

> Sourcing limitation: vendor help-center article bodies and support portals for several sampled products were embedded behind document viewers or login gates during research, and one intended sample was unreachable. Operational detail is therefore evidenced at the structural level (documented entity and transaction structure, feature descriptions, vendor role models) rather than at the level of exact procedure. No numeric limits, retention periods, fee schedules, or state names are asserted; disposition gates and audit expectations are described at the strength their evidence supports.
