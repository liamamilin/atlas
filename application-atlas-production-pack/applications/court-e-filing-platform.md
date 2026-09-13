# Court E-filing Platform

## Overview

A **Court E-filing Platform** is the intake channel into a court's case record: the application through which an identified filer packages court documents together with case information, submits them electronically to a specific court, passes a court-controlled review gate, and receives the outcome — acceptance, with the documents entering the court's official case record, or rejection, with reasons and a path to correct and resubmit.

The defining structure is small:

```text
Identified filer
└── Packaged electronic filing (documents + case identification)
    └── Routed to a specific court
        └── Court-controlled review gate
            └── Accept → filing enters the court's case record
                or Reject → reasons returned, correction and resubmission
```

Everything commonly associated with modern e-filing — service-provider marketplaces, electronic service on other parties, fee-disbursement services, multi-court accounts, auto-accept modes, guided preparation for self-represented litigants — is widespread in current products but is not what makes the product a court e-filing platform. A minimal court-run upload portal with manual clerk review satisfies the same definition; so does a national system where filing is bundled into the court's case management software.

The platform is deliberately **not** the court's system of record. It moves documents across the filing gate; the record of the case — the docket, hearings, and outcomes — belongs to the Court Case Management System. The two are inseparable in practice (accepted filings must be docketed) but distinct in function.

## Users & Context

The application is two-sided by nature.

**Filer side:**

- **Attorneys and law-firm staff** — the dominant users in mandatory e-filing regimes; file pleadings, motions, and evidence into existing cases or initiate new cases, often across many courts from one account.
- **Self-represented litigants** — file the same documents with more guidance; some products offer step-by-step document preparation built into the filing flow.
- **Agencies and institutional filers** — law enforcement submitting charging documents, trustees, process-serving firms filing on behalf of clients.

**Court side:**

- **Clerks and filing reviewers** — work the incoming queue, inspect submissions against court rules, accept or return them, initiate fee refunds, and manage the handoff into the case record.
- **Court administrators** — configure case types, filing codes, fee schedules, and review workflows.

The working context is deadline-driven litigation: filings are frequently time-sensitive, so submission is available around the clock in most products, while the review gate follows the court's business hours and local rules. Many jurisdictions mandate e-filing for attorneys in most case types; self-represented filers are commonly encouraged rather than required, and specific document types may remain exempt.

## Core Model

### The Defining Core

**The filing (submission).** The central object is a packaged submission: one or more documents (typically a lead document plus supporting attachments), bound to a case identification, submitted by an identified filer to one specific court. A submission is either a **new-case initiation** (the filing creates a case) or a **subsequent filing** into an existing case (identified by case number). All documents in one submission pertain to one case.

**Case identification.** Every submission carries structured data that places it: the court, the case category and type, the filing or document type drawn from the court's vocabulary, party information, and — for subsequent filings — the existing case number. This data is validated at submission time, before the filing reaches the court.

**Filer identity.** Filing requires a registered, identified filer. How identity is issued varies: some courts issue filing credentials directly to attorneys and authorized filers; in service-provider models the filer registers with a provider whose identity the court system accepts. Who may file (attorneys only, parties, agents) is a court decision.

**The review gate.** The defining control point. Submissions do not become filed documents automatically; they enter a court-controlled review in which a clerk accepts or rejects the submission. Acceptance is the moment of filing. Rejection returns the submission with reasons, and the filer corrects and resubmits.

**Proof of filing.** On acceptance the filer receives evidence that the documents were filed: an electronically stamped or "conformed" copy of the documents, a filing notice, or both. This returned artifact is what the filer relies on as proof of the filing and its date.

**The record handoff.** An accepted filing must enter the court's case record. In bundled systems this is automatic — the filing creates the docket entry itself. In separated architectures the platform transmits the accepted filing's data and documents to the court's case management system for docketing, so the information is not re-keyed.

### Standard Capabilities of Mature Products

These capabilities are common across mature products but do not define the Type:

- **Fee machinery** — filing-fee calculation at submission, payment collection, convenience or processing fees, provider service fees, refunds when a submission is returned, and fee-waiver handling.
- **Status tracking and notifications** — the filer can see where a submission stands (received, under review, accepted, returned) and receives email notifications at key points, including the acceptance notice with the stamped documents.
- **Rejection handling** — rejection reasons, return-for-correction workflows, and resubmission that reuses the original data instead of requiring full re-entry.
- **Electronic service (eService)** — serving filed documents on other parties through the platform, with delivery and open tracking. Service is a distinct legal act from filing; some products allow service without any court filing.
- **Case context for filers** — case search, case summaries (parties, judge assignment, a register of filing activity), and filing history with receipts.
- **Document preparation aids** — conversion of word-processing documents to text-searchable PDFs, format and size validation, electronic signatures, bookmarking.
- **Multi-court access** — one filer account usable across many courts, with the platform tracking each court's case types, fees, and rules.
- **Court-side review tooling** — a review queue of incoming submissions, detail views per submission, accept/reject/return actions, refund initiation, and in some products an auto-accept mode for filing types that qualify.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently:

```text
Concept:            Filing credentials
Implementations:    court-issued logins, service-provider accounts, state portal accounts

Concept:            Review gate
Implementations:    clerk review queues, dedicated review applications, auto-accept modes,
                    review built into the case management system

Concept:            Proof of filing
Implementations:    file-stamped copies, conformed copies, notices of electronic filing

Concept:            Record handoff
Implementations:    automatic docket entry (bundled systems), integration transmission
                    to a separate case management system
```

## How It Works

### The filing lifecycle (filer side)

```text
Select the court and case context
→ choose new case or existing case (case number)
→ upload documents (lead document + attachments; converted to compliant PDF)
→ complete the structured data (case type, filing type, parties, service contacts)
→ system validates required data elements and calculates fees
→ pay (court fees; provider and processing fees where applicable)
→ submit
→ track status while the court reviews
→ accepted: receive stamped/conformed copies and the filing enters the record
   rejected: read the reasons → correct → resubmit (fees typically refunded on return)
```

Two flows matter equally. **Case initiation** creates a new case and usually carries the heaviest data entry (parties, jurisdictional details, summons requests). **Subsequent filings** attach to an existing case number and are the high-frequency flow in active litigation.

### The review loop (court side)

```text
Incoming submissions arrive in the review queue
→ reviewer opens a submission (envelope) and inspects each filing:
   documents, case data, proposed orders, charges where criminal
→ accept: filing is stamped and docketed; filer is notified
→ return for correction: reasons recorded; fees refunded; filer notified
→ resubmitted filings re-enter the queue for a fresh review
```

Some courts configure automatic acceptance for filing types that meet criteria, reserving human review for the rest. Review workload, refund handling, and fee reporting are part of the court-side application.

### Service on other parties

Filing and service are related but separate acts. Most products let the filer designate service contacts and serve filed documents electronically, with per-recipient delivery and open tracking; paper mail service is commonly available as a paid adjunct. In some products service can be ordered without any court filing.

### Core vs Common vs Optional

**Defining core** — without these, not a court e-filing platform:

- packaged electronic filing bound to a case (new or existing)
- identified filer submitting to a specific court
- court-controlled review gate with accept/reject
- outcome returned to the filer
- accepted filings enter the court's case record

**Standard capabilities** — present in most mature products:

- fee calculation, payment, refunds, waivers
- status tracking and notifications
- rejection reasons and resubmission workflows
- proof-of-filing artifacts (stamped/conformed copies, notices)
- eService with tracking
- case search and filing history for filers
- document preparation aids (PDF conversion, validation, e-signature)
- multi-court single-account access
- court-side review queue tooling
- CMS integration for docketing on acceptance

**Variants / optional** — depends on jurisdiction, court, and product:

- service-provider marketplaces vs single portals vs CMS-bundled filing
- mandatory vs voluntary e-filing; exemptions
- service of process, courtesy-copy delivery, physical filing of exempt documents, concierge (human-mediated) filing
- guided document preparation for self-represented litigants
- agency filing portals (e.g., law enforcement)
- certified-copy purchase, docket monitoring, auto-accept policies

## Interfaces

### Filing wizard (filer side)

The primary work surface: a guided sequence from court/case selection through document upload, data entry, fee review, and submission. Typical information: court, case category/type, filing type, party details, document list with roles (lead vs attachments), fee breakdown. Primary actions: upload and convert documents, complete required fields, attach service contacts, pay, submit.

### Case list / matters view (filer side)

An organized view of the filer's cases and filings. Typical information: cases with numbers and courts, filing history, receipts, current status of submissions. Primary actions: file into a case, view filing details, download stamped copies, start a new filing.

### Status and history (filer side)

Where the filer tracks submissions. Typical information: submission status (received / under review / accepted / returned), rejection reasons, timestamps, payment receipts. Primary actions: open a returned filing for correction, resubmit, download documents and receipts.

### Review queue (court side)

The clerk's work surface: incoming submissions listed for review, often auto-refreshing. Typical information: submission (envelope) summary, filer, court, case context, documents. Primary actions: open for inspection, accept, return for correction with reasons, initiate refunds.

### Submission detail (court side)

The inspection surface for one submission. Typical information: each filing within the submission, lead and auxiliary documents in order, case and party data, charge information where criminal. Primary actions: view documents, accept or return individual filings, record comments.

### Notifications

Email carries the loop together: submission confirmations, acceptance notices with stamped documents, rejection notices with reasons, and — in many products — delivery of subsequent filings by other parties on the case.

## Important Rules / Behaviors

### The review gate is court-controlled

Acceptance is always the court's act, never the platform's. The platform can validate data and enforce formats, but only the court's review turns a submission into a filed document. This is why a returned submission is a normal, frequent event rather than an error state — the loop (submit → review → return → correct → resubmit) is a designed part of the workflow.

### Rejection refunds the fees

When a submission is returned for correction, the fees collected with it are typically refunded; the filer pays again on resubmission. Fee handling is therefore tied to the review outcome, not just to the payment event.

### The filed date follows submission rules set by each jurisdiction

Jurisdictions define when an e-filed document is considered filed — commonly tied to the moment of submission relative to a daily cutoff, with the court's review following. The exact cutoff and its effect on the filed date are set by local rules and vary; products surface the relevant deadlines rather than inventing them.

### Document rules are enforced at the gate

Courts constrain what may be filed: format (PDF is the near-universal requirement, usually text-searchable), size limits per document and per submission, redaction of personal identifiers (the filer's responsibility), and signing requirements (electronic signatures or /s/ conventions depending on the court). Products validate what they can at submission; the court's review remains the final check.

### Mandatory vs voluntary, with exemptions

Where e-filing is mandatory (typically for attorneys in most case types), specific documents and situations remain exempt — sealed or confidential documents, certain case types, self-represented filers in some courts. Paper filing persists for exempt documents, and some providers handle physical filing of exempt documents as a service.

### Filing and service are distinct acts

Serving documents on other parties satisfies different rules than filing them with the court. Products track the two separately even when both are ordered together, and service can exist without filing.

### One submission, one case

A submission's documents must all pertain to a single case; filings into different cases are separate submissions. This keeps the case binding unambiguous for docketing.

## Variants

- **Service-provider marketplace** — a state or court operates the filing manager and review gate; multiple certified providers compete on the filer side (one usually free and basic, others paid with value-added services). Credentials are commonly shared, so a filer registered with one provider can use another without re-registering.
- **Single court-run portal** — the court (or court system) operates one filer-facing portal itself; simpler filer choice, same review gate.
- **Bundled into the case management system** — filing, docketing, and public access live in one program; filing creates docket entries automatically. Common in nationally operated systems.
- **Mandatory regime** — attorneys required to e-file in most case types; the platform becomes core litigation infrastructure rather than an option.
- **Pro se-oriented** — guided document preparation and simplified flows for self-represented litigants, sometimes as a distinct self-help surface.
- **Agency filing** — dedicated portals for law enforcement or other agencies submitting specific document types into criminal cases.
- **Full-service provider** — the filing service bundled with service of process, courtesy-copy delivery, physical filing, and human concierge handling; the platform becomes a litigation-support hub.

A variant remains a variant while the defining structure holds. When the submission surface loses the case binding and the review gate — for example, a generic government submission portal — it is a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Court Case Management System | downstream record of reference | the CMS holds the case, docket, hearings, and outcomes; e-filing is the intake channel that feeds it. The market ships them as separate integrated products and sometimes as one bundled program, but the functions are distinct: remove the case record from an e-filing platform and it still files; remove intake from a CMS and it still manages cases |
| Legal Docket Management | same word, different object | law-firm docketing tracks the firm's deadlines and filing obligations; it may trigger a filing but does not submit one |
| Legal Document Automation | upstream producer | drafting tools produce the documents; the e-filing platform submits them. Submission-time auto-population is assistance, not document production |
| eDiscovery Platform | adjacent litigation data | party-to-party exchange and review of litigation data vs submission into the official court record |
| Government Service Portal | generic container | citizen-to-government submissions lack the case binding, court-controlled review gate, fee schedules, and record handoff |
| Court payment portals (fines and fees) | adjacent financial surface | payments against existing obligations vs filing fees attached to a submission |
| Public records access systems | the other direction | retrieval of court records vs submission of filings; nationally these are often separate programs |

The boundary with the Court Case Management System is the defining one. The two Types meet at acceptance: the platform's job ends when the filing enters the record; the CMS's job begins there.

## Representative Products

- **eFileTexas.gov** — state-run official e-filing system (Texas Office of Court Administration) with a certified service-provider marketplace, a free state-provided provider, and a dedicated court-side reviewer portal
- **CM/ECF (US federal judiciary)** — government-built system in which electronic filing is bundled with case management; the canonical record-centric implementation
- **Odyssey File & Serve (Tyler Technologies)** — commercial filing service operating as a state-provided provider (Texas) and as the court-side review application used by Texas reviewers
- **Green Filing** — independent commercial filing service provider operating across multiple US states
- **One Legal (InfoTrack US)** — commercial filing service bundled with service of process and litigation-support services (California/Nevada)
- **TrueFiling (ImageSoft)** — court-developed filing system deployable as either or both of the two architecture sides (filer-side service and court-side filing manager)

## Sources

Research date: **2026-09-07**

- eFileTexas.gov (Texas OCA) — home, FAQs, Service Providers, Information for Reviewers, State Provided EFSP: https://efiletexas.gov/
- United States Courts — FAQs: Case Management/Electronic Case Files (CM/ECF): https://www.uscourts.gov/court-records/file-a-case-cm-ecf/faqs-case-management-electronic-case-files-cm-ecf
- Green Filing — home and FAQ: https://www.greenfiling.com/
- One Legal — home and Court Filing product page: https://www.onelegal.com/ ; Support Center, Court Filing category: https://support.onelegal.com/en_US/court-filing
- TrueFiling (ImageSoft) — home: https://www.truefiling.com/
- Tyler Technologies — eFile & Serve Review Queue version updates (official product documentation): https://content.tylerhost.net/docs/ReviewApp/Help/version-updates.html

> Sourcing limitations: the New York courts e-filing site (a court-run portal example) was not reachable (403), and Tyler's main product site was unreachable in the same-day companion research; Tyler evidence here rests on the official eFileTexas state-provider page and Tyler-hosted review-application documentation. Non-US e-filing systems were not directly researched. Jurisdiction-specific figures (fee percentages, size limits, cutoff times) are recorded in the paired Research Notes rather than asserted here, and review timelines are treated as local-rule matters.

Detailed evidence, product-by-product observations, the cross-product comparison, and the architecture analysis (service-provider marketplaces vs court-run portals vs bundled systems) are recorded in the paired Research Notes.
