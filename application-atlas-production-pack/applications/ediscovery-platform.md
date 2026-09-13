# eDiscovery Platform

## Overview

An **eDiscovery Platform** is the legal team's system of record for the document side of a disclosure obligation. For a specific legal matter — a litigation, an investigation, a regulatory or public-records request — the platform holds the matter's document corpus, organizes human review of it, and produces the disclosed document set to the party or authority entitled to receive it. The dominant subject matter is electronically stored information (ESI): email, chat, documents, and records collected from the organization's systems.

The defining structure is small — three things bound together by the matter:

```text
Matter / Case
└── Document corpus of record (ingested, processed, searchable records)
    └── Human-coded review (per-document determinations, managed as team work)
        └── Production (the numbered, redacted, logged deliverable)
```

Everything commonly associated with modern products — legal holds, data collection connectors, processing engines, analytics, technology-assisted review, generative-AI first passes — is standard machinery around this core, but none of it is what makes the software an eDiscovery platform. The workflow predates software: paper-era discovery already assembled a corpus from custodians' files, coded it on review sheets, and produced Bates-numbered copies with a privilege log. The platform digitizes and scales exactly that machine.

When the managed object becomes the dispute itself (pleadings, deadlines, spend) the product is drifting toward Legal Matter or Litigation Management; when it becomes the preservation duty rather than the corpus, it is Legal Hold Management; when disclosure is voluntary and owner-controlled, it is a Virtual Data Room.

## Users & Context

The platform is operated by legal professionals on the responding side of a disclosure obligation, in several distinct seats:

- **eDiscovery / litigation-support specialists** — assemble the corpus, run processing and searches, configure review and production machinery. In law-firm and service-provider settings this is a dedicated profession; inside corporations the same work is done by in-house legal operations or by the vendor's hosted services.
- **Review attorneys and reviewers** — the defining consumers: they examine documents and record determinations. Large reviews are staffed by teams working in coordinated passes.
- **Review managers / case leads** — distribute review work, monitor progress and quality, manage coding rules and privilege calls.
- **Matter leads / supervising attorneys** — own the strategy; consume reports; sign off on productions.
- **Administrators** — manage users, permissions, and the security posture that external auditors and courts expect.

The context is adversarial and deadline-driven: the corpus must be defensible in front of an opposing party, a regulator, or a court. Much of the product's machinery — audit trails, production logs, re-production and clawback features — exists because discovery conduct is itself judged. Typical customer tiers span corporate legal departments running matters themselves, law firms and litigation service providers running reviews for clients, and organizations using the machinery embedded in their existing suite for smaller matters.

## Core Model

### The Defining Core

**1. The matter-bound document corpus of record.** A case, matter, or workspace — every product names its container differently — holds the matter's document population as individually addressable records. Each record carries metadata (author, dates, source, custodian), extracted text, and a rendered form of the original. The corpus is *assembled*: documents arrive through ingestion — either the platform collects from custodian data sources itself, or it ingests externally collected and processed data (the load-file interchange is an established industry mechanism), or both. Once in, records are stable: the corpus is the fixed evidence base that review decisions and productions refer back to.

**2. Human-coded document review.** The work the whole platform exists to organize: a reviewer examines a document and records structured determinations on its record — responsive or not, privileged or not, confidential, relevant issue tags, production decisions. Determinations are data, not prose: they are searchable, reportable, auditable, and revisable with a recorded history. Because corpora are large and review is a team activity, the platform organizes review as *managed work*: document sets are distributed to reviewers through batches, assignments, or queues; progress and reviewer throughput are tracked; second-pass, privilege, and quality-control passes are staged on top of first-pass review.

**3. Production/disclosure as a managed, recorded output.** The selected document set leaves the platform as a structured deliverable: documents are numbered (Bates-style numbering is the dominant convention), redacted where required, endorsed with production markings, and packaged with the formats and metadata the receiving party expects — alongside a privilege log of withheld documents. The act is recorded: what was produced, when, to whom, in what form. Because mistakes have legal consequences, production is paired with correction machinery — re-productions, clawback of erroneously produced privileged documents, and pre-production quality checks.

The matter container is what binds the three: corpus, review work, and productions all hang off the same case object, and case membership governs who sees any of it.

### Standard Capabilities

Mature products almost always add:

- **Search and culling** — query languages spanning content, metadata, and coded fields; saved searches; sampling and statistics for scoping the matter before heavy review.
- **Processing machinery** on ingestion — text extraction, OCR for image-only files, metadata normalization, de-duplication, email threading, near-duplicate grouping, chat-conversation reconstruction.
- **Analytics and technology-assisted review** — clustering, theme detection, communication analysis, and predictive coding / AI relevance models that rank or group documents so reviewers see the most relevant material first; current-generation products add generative-AI summarization, question-answering over the corpus, and AI-drafted first-pass coding.
- **Legal hold and collection modules** — custodian identification, hold notices, and collection from enterprise systems, sold as the upstream stage of the same platform (see Related Application Types).
- **Early case assessment** — pre-review dashboards over the corpus to scope custodians, time ranges, and volumes.
- **Interchange** — import and export in the load-file formats the surrounding ecosystem uses, so matters can move between platforms and service providers.
- **Defensibility surface** — audit trails over consequential actions, chain-of-custody articulation, process reports for long-running jobs, reviewer activity reporting.
- **Access control** — role-based permissions scoped to the case: reviewers, review managers, administrators, and guest access for outside counsel or co-counsel.

### One Structure, Many Implementations

The core model is written conceptually; products realize it differently, and the differences are matters of packaging rather than kind:

```text
Concept:            Matter container
Implementations:    case, matter, workspace, database + project

Concept:            Corpus assembly
Implementations:    in-product collection from data sources, load-file
                    intake of externally processed data, forensic
                    collection as a professional service

Concept:            Review distribution
Implementations:    static batches checked out to reviewers, criteria-based
                    assignment groups, AI-ranked queues

Concept:            Production formality
Implementations:    full Bates-numbered image productions with placeholders
                    and endorsement stamps; structured export packages
                    with reports, for matters where that is the agreed form
```

A reader who has only seen one packaging (for example, a platform-native suite module that exports rather than formally stamps) should still recognize the full review-and-produce platforms from the core model above.

## How It Works

The canonical workflow, as the products themselves document it:

```text
Trigger (litigation filed, investigation opened, request received)
→ open the matter; preserve and scope (hold upstream; custodians and
   data sources identified)
→ assemble the corpus (collect and process, or ingest processed data)
→ search, sample, and cull
→ review in managed passes (first pass → privilege → QC)
→ produce the disclosed set (protocol → redact → number → log → deliver)
→ correct when required (re-productions, clawback)
```

### Assemble the corpus

The matter opens with identification of custodians (the people whose data matters) and data sources. Preservation duties are handled by the hold machinery — in most products a bundled module, in others a separate platform that feeds this one. The corpus itself is then built: either the platform reaches into source systems through connectors and copies the responsive-in-scope data, or an externally collected and processed set is ingested. Processing normalizes the material — extracting text, indexing metadata, de-duplicating copies, threading email chains, reconstructing chat conversations — so that the corpus becomes one searchable, reviewable record set.

### Search and cull

Operators scope the matter with searches before humans read anything: keyword and condition queries, metadata filters, statistical samples. The goal is to spend review effort where it matters. Search-term reports and volume statistics also serve the external negotiation — parties disclose and argue over search methodology.

### Review in managed passes

Review managers define the coding scheme (the determinations reviewers record) and distribute documents — as checked-out batches, criteria-based assignments, or AI-ranked queues. Reviewers work through their sets in a document viewer paired with a coding panel, advancing document by document; related documents (email threads, near-duplicates, conversation chains) are typically surfaced together. Subsequent passes re-touch the corpus: privilege review by senior attorneys, quality-control sampling, issue-focused second passes. Analytics models — trained on early coding decisions — prioritize, group, and in current products increasingly draft first-pass determinations, but the recorded determination that drives production remains review work subject to the same tracking and quality machinery.

### Produce

Productions are configured against the production protocol agreed for the matter — formats, metadata fields, numbering conventions. The platform assembles the selected documents, applies redactions, stamps numbering and endorsements, generates the privilege log, and packages the deliverable for the receiving party. Production records persist with the matter: what went out, in which production, under which numbers. When something was produced in error, clawback and re-production machinery exists precisely because discovery mistakes are legal events, not just filing errors.

### Core vs standard vs optional

**Defining core** — without these, not this Type:

- matter-bound document corpus of record, assembled through ingestion
- human-coded review with structured per-document determinations, organized as managed team work
- production/disclosure as a managed, recorded deliverable with correction machinery

**Standard capabilities** — present in most mature products:

- processing machinery (extraction, OCR, dedup, threading)
- advanced search, sampling, early case assessment
- analytics, predictive coding, AI-assisted review
- redaction and privilege-log machinery
- legal hold and collection modules bundled upstream
- audit trails, chain-of-custody articulation, role-based access with outside-party guest access

**Optional / variant** — depends on segment and posture:

- in-product collection connectors vs externalized collection
- managed review services and hosted operation
- jurisdiction-specific production conventions; public-records regime packaging
- adjacent case-prep surfaces (chronologies, deposition tools, case narratives)

## Interfaces

### Matter / case home

The operational entry point for the matter: custodians and data sources, corpus status, searches, review progress, and productions under one case object. Primary actions: add data sources, launch processing or searches, open review and production areas, manage case members.

### Search and results table

Purpose: scope the corpus and assemble review sets. Typical information: query builder (content, metadata, coding terms), result counts, volume statistics, document lists with preview. Primary actions: run and save searches, sample, bulk-tag, add results to review assignments, export.

### Document review window

The reviewers' primary surface: a viewer rendering the document (or its image/text) side by side with a coding panel carrying the determination fields; navigation across the assigned set; threading and near-duplicate context; redaction and annotation tools on the document itself. Primary actions: record coding, redact, flag for privilege or escalation, advance to next document. This surface is where the Type's defining work happens, and its design — speed, keyboard flow, related-document grouping — is a major axis of product differentiation.

### Review management console

Purpose: run review as a managed operation. Typical information: batches/assignments/queues with per-set progress, reviewer throughput, coding statistics, QC results. Primary actions: create and allocate batches or assignments, define coding rules, monitor dashboards, rebalance work, run quality-control passes.

### Production workspace

Purpose: configure, run, and record productions. Typical information: production protocols and their settings, document selections, pre-production validation results, produced-number ranges, delivery status. Primary actions: create/modify protocols, run pre-production checks, generate the production package, produce the privilege log, share the deliverable, clawback or re-produce.

### Administration and security

User and role management scoped to cases, audit and activity reporting, matter-level access restrictions — the surface that makes the platform acceptable to the organizations whose litigation exposure it carries.

## Important Rules / Behaviors

**The corpus is the fixed record.** Documents are individually addressable and effectively immutable once ingested; corrections and determinations attach to the record rather than rewriting it. Every downstream artifact — coding, production, log — refers back to the same corpus.

**Coding is recorded opinion, with history.** Determinations are structured data on the document record, attributed and auditable, revisable with the revision visible. This is what makes review defensible when challenged.

**Privilege gates production.** Privileged material is withheld (and logged) or produced with redactions; producing privileged material in error triggers clawback machinery that mature products provide for exactly this case. Mature products commonly run pre-production checks for the common errors — unredacted privileged material, numbering gaps — before the deliverable leaves.

**Case membership is the access boundary.** Visibility over corpus, review, and productions follows the case, with roles inside it; external parties (opposing counsel receiving a production, co-counsel, guest reviewers) participate through deliberately scoped access.

**Production formalities are negotiated per matter.** Formats, fields, and numbering are agreed matter-by-matter; products therefore treat the production protocol as a configured object rather than a fixed standard.

**Preservation runs ahead of review.** The hold stage can suspend deletion in source systems independently of the platform's corpus; the corpus assembled for review is downstream of, and traceable to, that preserved population. (The duty workflow itself belongs to Legal Hold Management — see Related Application Types.)

## Variants

- **Operating-model poles** — self-serve platforms run directly by corporate legal teams; platforms operated by law firms and litigation service providers with specialist administrators; products whose vendors supply managed review and collection services around the software.
- **Deployment posture** — multi-tenant cloud SaaS; single-tenant or private-cloud deployments for sensitive clients; government-cloud variants; an on-premises server lineage still maintained by the legacy enterprise pole.
- **Trigger regimes** — litigation discovery is the anchor, but the same machinery is packaged for internal and regulatory investigations, second requests, public-records/FOIA response (some vendors ship dedicated applications for this), data-subject-request reviews, and breach response.
- **Suite posture** — standalone review platforms; modules of broader legal-governance suites (hold → collection → review → production under one governance roof); platform-native eDiscovery shipped inside an existing productivity suite, where it can appear in staged tiers (basic search-and-export today, full review sets at a higher tier).
- **Regional practice** — the machinery is regime-neutral, but production conventions vary by jurisdiction; international disclosure practice and jurisdiction-specific production options are documented product variants, not different Types.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Legal Hold Management | the upstream first stage: manages the preservation *duty* (custodian notices, acknowledgment, release). Bundled into most eDiscovery platforms, but fully itself without them; a hold platform has no corpus, review, or production |
| Legal Matter Management | the legal function's system of record for its matters (status, deadlines, spend, work). Here the matter is a container scoping the document machinery, not the record of the dispute |
| Litigation Management Platform | runs the litigated dispute (pleadings, court events, counsel); the eDiscovery platform is invoked *for* one of its matters and owns the document side |
| Enterprise Records Management | standing, policy-driven retention and disposition over record classes; eDiscovery is trigger-scoped corpus assembly that *suspends* that standing regime for a matter — vendors themselves document the seam |
| Digital Forensics Platform | investigator-facing examination of digital evidence (imaging, artifacts); the two meet at collection, and suites sell them as separate product lines |
| Evidence Management System | agency custody of evidence *items* with chain-of-custody tracking; different object (items vs a review corpus) and different actors |
| Corporate Investigation Management | investigation case workflow; investigations *trigger* eDiscovery cases, and the corpus/review machinery is the instrument inside them |
| Virtual Data Room | the voluntary-disclosure counterpart: the owner stages a corpus and grants invited parties controlled access for a deal or audit; eDiscovery disclosure is compelled, shaped by privilege review and production obligations |
| FOI / Public Records Request Platform | request-side intake and tracking for statutory disclosure regimes; eDiscovery machinery appears packaged for the review/production side of the same regimes |
| Enterprise Search | organization-wide standing search; eDiscovery search is matter-scoped and exists to feed review and production |

The sharpest seam is with **Legal Hold Management**: the hold is the first pipeline stage, bundling is the market norm (every sampled platform ships a hold capability), and the boundary is center of gravity — strip collection, review, and production from an eDiscovery platform and a hold manager remains; strip the custodian duty workflow and what is left is a technical preservation capability, not the hold-management Type.

## Representative Products

- **Relativity (RelativityOne)** — the incumbent enterprise review platform; workspaces, a processing/collection stack, queue-based review management, deeply formalized production machinery, and a large developer ecosystem.
- **Everlaw** — cloud-native SaaS for firms and in-house teams; upload-based corpus assembly, assignment-driven review, protocol-driven production with pre-production QC, and bundled legal holds in matter containers.
- **Exterro** — legal-governance suite with hold-first heritage; eDiscovery sold as hold → collection/processing → review → production under a single defensibility and chain-of-custody framing for in-house teams.
- **Microsoft Purview eDiscovery** — platform-native eDiscovery inside a productivity suite; case-centric search, holds, review sets, and export against the suite's own data sources, staged across service tiers.
- **DISCO** — cloud-native litigation platform; ediscovery with check-out batches and review stages, alongside hold, request, and AI review products.

## Sources

Research date: **2026-09-08**

- Relativity — RelativityOne User Documentation (documentation index; "Production"; "Review Center") — https://help.relativity.com/RelativityOne/Content/index.htm , https://help.relativity.com/RelativityOne/Content/Relativity/Production/Production_overview.htm , https://help.relativity.com/RelativityOne/Content/Relativity/Review_Center/Review_Center.htm
- Everlaw — Knowledge Base (index; "Overview: Create a Production on Everlaw"; "Introduction to Assignments") — https://support.everlaw.com/hc/en-us , https://support.everlaw.com/hc/en-us/articles/218312623 , https://support.everlaw.com/hc/en-us/articles/210222443
- Microsoft Learn — "Learn about eDiscovery"; "Learn about the eDiscovery workflow" — https://learn.microsoft.com/en-us/purview/edisc , https://learn.microsoft.com/en-us/purview/edisc-workflow
- Exterro — eDiscovery suite product page — https://www.exterro.com/e-discovery-software
- DISCO — product site and Ediscovery Support Center — https://www.csdisco.com/ , https://support.csdisco.com/hc/en-us
- Paired boundary research: research/legal-hold-management.md (2026-09-07 pass) — hold-vs-pipeline seam and its bundling evidence.

> Sourcing limitations: Exterro's review and production internals were observed only at product-page level (suite structure and claims, not feature-level documentation); DISCO was observed at product-site plus support-center index level, without fetching individual help articles. Claims for these two are therefore stated at correspondingly lower strength. Vendor marketing performance figures observed during research were excluded. Numeric limits, defaults, and licensing details were intentionally not stated in this document; they remain in the Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
