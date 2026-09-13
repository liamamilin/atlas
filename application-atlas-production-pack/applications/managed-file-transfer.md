# Managed File Transfer

## Overview

A **Managed File Transfer (MFT) application** is an organization's system for moving files between defined endpoints — partner organizations, remote hosts, and internal or cloud storage — as **automated, tracked transfer events**. The platform holds the endpoint relationships and their credentials, carries out file movements on schedules, triggers, or requests, and records each movement's outcome for monitoring, alerting, and audit.

The defining core is small and jointly held:

```text
Defined endpoints of record
└── Platform-executed, rule-initiated transfer of files
    └── Transfer event record with outcome
```

Remove any leg and the product stops being an MFT:

- without held endpoints, file movement is supplied ad hoc by a person in a client tool or server session;
- without platform-executed transfers, the system is a passive receptacle and the flow is unautomated;
- without the retained per-transfer record, the movement is a blind pipe — transport, but nothing "managed".

Everything popularly associated with MFT — broad protocol support, encryption, PGP processing, portals for people, compliance reporting, SIEM streaming — is standard mature capability or optional packaging layered on this core, not the definition itself. The files move as opaque whole units: an MFT governs *the movement*, not the meaning inside the file.

## Users & Context

MFT is operational infrastructure operated by a small number of technical staff and consumed silently by many systems and partners.

Primary operators:

- **MFT administrators** — define endpoints and partner relationships, configure users and permissions, set up the transfers and automations, own security policy.
- **Integration/operations staff** — monitor transfer activity, respond to failures and missing deliveries, onboard and offboard partners.

Consumers (often without ever opening a console):

- **Application systems** — ERP, payroll, analytics, and other machines that drop or collect files through service accounts, protocol endpoints, or APIs on schedules.
- **External partner users** — vendor, customer, and agency staff who exchange files through isolated partner spaces or web portals.
- **Business end users** — send and receive ad-hoc sensitive files through web portals, desktop clients, or email-integrated flows, with every exchange tracked like any other transfer.
- **Auditors and security teams** — consume the retained transfer records, access reports, and event streams as compliance and incident evidence.

Typical context: mid-size and large organizations in file-heavy, compliance-sensitive industries — finance, healthcare, insurance, government, manufacturing, retail supply chains — running recurring machine-to-machine feeds (statements, invoices, EDI files, exports), partner exchanges, and regulated ad-hoc sharing. The Type emerged when organizations outgrew bare FTP servers and hand-written scripts: the problem it solves is not *whether* files can be moved, but whether movements between important endpoints are **reliable, governed, and provable** without a human babysitting each one.

## Core Model

### The Defining Core

**1. Defined endpoints of record.** The platform persistently holds named connection relationships: external partner organizations, remote hosts, internal filesystems, and cloud storage. Each endpoint carries its protocol bindings and credentials — host keys, SSH keys, passwords, certificates — so a transfer addresses a held relationship instead of asking an operator to re-enter "where and how" every time. External organizations are commonly modeled as partner containers: an isolated unit holding that organization's users, permissions, and exchange folders, manageable and removable as a whole. Local storage is often unified with remote storage, so clouds and on-premises servers appear as one addressable space.

**2. Platform-executed, rule-initiated transfer.** The platform itself performs file movements between those endpoints as its own managed operations. A transfer is defined by: *what* moves (files matching patterns), *where* (source and destination endpoints), *when* (a schedule, an event such as a file arriving or being modified, an inbound webhook, or a programmatic/API request), and optionally *what happens along the way* (encrypt, compress, rename, route). External parties also initiate movements as part of the managed surface — a partner system connecting through its held endpoint credentials, or a person sending through a portal — and the platform executes and records those movements like any other. Files travel as opaque units; the platform is content-agnostic about what they mean.

**3. The transfer event record with outcome.** Every transfer or attempt is captured as a discrete, retained record: which file(s), between which endpoints, in which direction, when, initiated by whom or what trigger, over which protocol, and with what outcome — success, failure, partial completion, skipped, retried. The record is surfaced to operators (searchable history, dashboards, reports), exposed programmatically (APIs, event streams to security systems), and commonly protected against tampering, because it doubles as compliance and dispute-resolution evidence. The "managed" in the Type's name is carried by this leg together with the held endpoints wrapped around the executed movement.

### One Structure, Many Implementations

The core is conceptual, and each part has several common realizations:

```text
Concept:  Defined endpoints of record
Realizations:  trading-partner records, remote-host connections,
               cloud-storage connections, on-premises links via
               an outbound-only agent, protocol service endpoints

Concept:  Rule-initiated transfer
Realizations:  scheduled jobs, file-arrival/modification triggers,
               webhooks, API/CLI calls, portal sends by people,
               protocol sessions from held partner endpoints

Concept:  Transfer event record
Realizations:  searchable activity history, per-run logs with
               retry outcomes, scheduled audit reports, event
               streams to security monitoring systems
```

### Standard Capabilities

Mature products commonly add these capabilities. They make MFT practical but do not define the Type:

- **Protocol breadth over one storage core** — SFTP, FTPS, FTP, HTTPS, WebDAV sessions and B2B transports such as AS2 all land in the same permissioned, audited file space, so partners can keep whatever protocol they already run.
- **Failure machinery** — automatic retries with bounded attempts, alerting on terminal and partial failures, and, in more mature products, *absence detection*: defining what a correct delivery looks like (which files, where, by when) and raising an incident when an expected delivery does not arrive at all.
- **Transfer-time content processing** — PGP encryption/decryption, compression, renaming, flattening, and routing rules by partner, file type, or time; some products also transform file contents (between formats such as CSV, XML, EDI, or HL7) at the point of transfer.
- **Security posture** — encryption in transit and at rest, folder/file permissions, user and role administration, single sign-on and multi-factor authentication, platform-held credentials and host keys, and partner-certificate lifecycle management in B2B-heavy products.
- **Storage and system integration** — cloud object stores and on-premises filesystems reachable directly or through a gateway/agent component; APIs, SDKs, CLIs, and webhooks to drive and observe transfers from other systems.
- **Administration surfaces** — scoped administrative roles; in some products, workspace-style organization, delegated administration of partner spaces, and bulk onboarding/offboarding.

## How It Works

The defining workflow has six steps, and a mature deployment runs it continuously across dozens or hundreds of configured flows.

### 1. Register an endpoint

```text
Create the relationship
→ record host/partner identity, protocol, credentials or certificates
→ define its accessible space (folders, isolation boundaries)
→ test connectivity
```

### 2. Define the transfer

```text
Choose what moves (file patterns)
→ choose endpoints (source and destination)
→ choose initiation (schedule / event trigger / API / portal)
→ optionally add processing steps (encrypt, compress, rename, route)
```

### 3. The platform executes

The platform performs the movement as a managed run — transferring files between endpoints, applying any defined processing, and completing the handoff without a human in the loop.

### 4. The outcome is recorded

Each run lands in the record: what moved, between where, when, over what protocol, with what result. Failures record what went wrong and what retry steps followed; some products distinguish partial or skipped states from clean success.

### 5. Monitor and respond

Operators watch dashboards and histories; failures are retried and escalated to alerts according to the product's failure machinery, and more mature products also raise an alert when an *expected* delivery never shows up. The typical operational loop is: alert → inspect the run record → fix the condition (endpoint down, partner late, wrong file) → let the flow resume.

### 6. Prove and report

Because records are retained and commonly tamper-resistant, the same machinery answers audits and disputes: who sent what, when, to whom, and whether it was received — plus scheduled reports on access, sharing, and activity for compliance reviews.

### The ad-hoc mode

Alongside scheduled flows, people send files on demand through portals, desktop clients, or email integrations. These exchanges enter the same record machinery — tracked, logged, expiring or governed per policy — which is precisely what distinguishes them from untracked email attachments or personal sharing links.

## Interfaces

### Administrative console

The operator's home surface: endpoint and partner management (create, test, isolate, onboard, offboard), user/group/role administration, and the definition of transfers and automations. Some products let partner organizations administer their own users within configured limits.

### Workflow/automation builder

The surface where transfers are composed — triggers, file patterns, destinations, processing steps. Ranges from simple scheduled copy definitions to multi-step, branching flows in more automation-heavy products.

### Monitoring and history views

Searchable transfer history and run outcomes (including retries and, in some products, partial states), dashboards of current activity, and — in more mature products — incident tracking for failed or missing deliveries.

### Audit and reporting surfaces

The retained record itself: searchable in the app, exportable, and — in many products — deliverable to external security-monitoring systems and packaged as scheduled compliance reports (access reviews, login history, sharing activity).

### User web portal

The person-facing surface for ad-hoc exchange: send and receive packages, share links, and intake inboxes — all governed by the same permissions and recording as machine flows.

### Protocol endpoints

Machine-facing surfaces — protocol endpoints such as SFTP, FTPS, FTP, HTTPS, or WebDAV, and B2B transport endpoints — that partner systems connect to using their held credentials. To the partner these look like ordinary servers; behind them everything lands in the same governed space.

### Programmatic surface

REST APIs, SDKs/CLIs, and webhooks/event streams, letting other software initiate transfers and consume run outcomes directly.

## Important Rules / Behaviors

### The record is the product of "managed"

What separates MFT from an automated copy script is not the movement — scripts move files too — but that the platform holds the endpoints, executes on rules, and **retains a complete, tamper-resistant account of every movement**. Some products protect the record so that even administrators cannot edit or delete it.

### Failure is a first-class state

Transfers do not silently vanish. Runs have explicit outcomes, failures are retried before escalating to alerts, and — in more mature products — the *absence* of an expected delivery is itself detected and raised. Late or missing partner files are treated as incidents, not surprises.

### Endpoints bound both access and visibility

The endpoint-of-record is also a security boundary: partner users are confined to their own assigned space — in strongly isolated implementations, an organization cannot even see that other partners exist — and external access happens only through held, credentialed relationships. The endpoint model doubles as an access-control surface.

### Files are opaque; meaning is not the platform's business

An MFT moves, stores, encrypts, routes, and (optionally) reshapes files, but it does not interpret business meaning inside them. When products do transform content, it is a processing step at the point of transfer — the transfer, not the transformation, remains the managed object.

### Ad-hoc and scheduled flows share one record

Person-initiated sends are not a side channel; they enter the same permissioned, audited space as machine flows. This is the structural answer to untracked "shadow" file sharing.

### Initiation is flexible; execution is always the platform's

Whether a movement starts from a schedule, an arriving file, an API call, a portal action, or a partner's protocol session, the platform performs and records the transfer. Movements executed entirely outside the platform by external tools are outside the record — which is exactly the gap MFT exists to close.

## Variants

- **On-premises enterprise MFT** — the classic form: server or appliance inside the organization's network, often behind DMZ/proxy architectures, common in mainframe-lineage environments running batch-initiated partner feeds. The recognized lineage of the Type since the early 2000s.
- **Cloud-native SaaS MFT** — the platform operated by the vendor; organizations configure endpoints, partners, and automations without running servers; on-premises systems reached through outbound-only agents; storage unified across clouds.
- **B2B-gateway-flavored MFT** — strong trading-partner orientation: certificate exchange, B2B transports with signed receipts, partner onboarding lifecycles, often embedded in wider supply-chain/EDI ecosystems.
- **Security-platform-embedded MFT** — transfer delivered as one "secure workflow" among email protection, forms, file sharing, and rights management inside a data-exchange governance platform; emphasis on unified visibility and compliance regimes.
- **Ad-hoc-exchange-heavy deployments** — portals and packages dominate (person-to-person and person-to-partner exchange), with automation in a supporting role; common in professional-services and government contexts.
- **Automation-heavy deployments** — hundreds of scheduled/triggered machine flows with little human transfer; common in finance, retail, and IT operations.

A variant stays a variant while the defining core holds. If a product's center shifts to interpreting document meaning between partners (EDI), to maintaining state equivalence between locations (sync), or to executing data pipelines with record-level transformation (integration), it has crossed into a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| File Transfer Application | user-operated client tool; each movement is human-initiated; endpoint lists are conveniences, not held relationships; no platform-executed automation or managed transfer-event record |
| File Sync Application | maintains continuous equivalence between locations (replication); MFT performs discrete, individually initiated and recorded transfer events |
| ETL / ELT Platform | data pipeline is the managed object with record-level transformation between data stores; MFT's managed object is the file-movement event, with files as opaque units |
| Data Integration Platform | persistent pipelines and transformation-centric execution; files may be a pipeline's medium, but the pipeline stays the unit — the overlap zone with MFT sits exactly on this seam |
| EDI Platform | standardized business-transaction document semantics (mapping, acknowledgment documents) between trading partners; MFT carries files content-agnostically and may *transport* EDI files without understanding them |
| Data Exchange Platform | dataset offerings with discovery and entitlements for consumers; MFT has no offering/entitlement semantics — it moves files between held endpoints |
| Personal Cloud Drive | person-facing storage and sharing; no endpoint automation, partner-of-record, or transfer-event management |
| Enterprise Content Management | document lifecycle, governance, and collaboration inside a repository; MFT centers movement between endpoints rather than repository life |
| Secure Email / Ad-hoc Sending Tools | person-to-person message exchange; ad-hoc sending exists *inside* MFT as a mode, but the Type centers held-endpoint automated flows |

The most important boundary is the one with Data Integration: when files are merely the medium of a persistent, transformation-centric pipeline, the product belongs to integration; when the *transfer event between held endpoints* is the managed, recorded unit, the product is MFT. Many organizations run both.

## Representative Products

- **Progress MOVEit** — classic category leader; on-premises server, cloud, and automation modules; compliance-heavy regulated-industry base.
- **Files.com** — cloud-native pole with deep automation and audit machinery; self-describes as a "file orchestration platform."
- **Cleo Harmony** — B2B/supply-chain-flavored MFT with transmission scheduling, event triggers, and non-event alerting inside a wider integration ecosystem.
- **Kiteworks** — security-first platform delivering MFT as one secure workflow among governed data-exchange surfaces.

The defining core was also checked against the legacy on-premises lineage (the long-standing enterprise products of the early-2000s MFT generation) to avoid over-fitting the definition to the current cloud-native implementation.

## Sources

Research date: **2026-09-08**

- Files.com — Documentation portal (Automation & Flow, Automations, Partners): https://www.files.com/docs , https://www.files.com/docs/automation-and-flow , https://www.files.com/docs/automation-and-flow/automations , https://www.files.com/docs/partners
- Files.com — Audit Log: https://www.files.com/features/audit-log
- Files.com — Managed File Transfer overview: https://www.files.com/managed-file-transfer
- Progress — MOVEit product page and FAQ: https://www.progress.com/moveit
- Cleo — Cleo Harmony product page: https://www.cleo.com/products/cleo-harmony
- Kiteworks — Managed File Transfer page: https://www.kiteworks.com/managed-file-transfer/

> Sourcing limitation: operational documentation for several long-standing enterprise MFT products (IBM Sterling, GoAnywhere, Axway SecureTransport, OpenText) was not reachable from the research environment on 2026-09-08 (access blocked or non-fetchable documentation portals). Findings about the legacy pole therefore rest on reachable product pages, cross-product commonality, and one competitor's market characterization, and are stated at conceptual strength only. Precise operational details (numeric limits, default settings, retention windows, exact protocol lists for unreachable products) are intentionally not asserted in this document; they remain in the paired Research Notes.
