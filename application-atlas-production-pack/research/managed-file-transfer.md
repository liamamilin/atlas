# Research Notes — Managed File Transfer

Research date: 2026-09-08

## Research Goal

Understand what a Managed File Transfer (MFT) platform actually is as an Application Type: its defining core, its standard mature capabilities, its variants, and its boundaries against the neighboring file-movement Types in the directory (File Transfer Application and File Sync in §03.15; ETL/ELT, Data Integration, EDI Platform, Data Exchange Platform in §13).

Prior passes left two binding notes for this pass (recorded in STATUS.md Boundary Issues):

1. **data-exchange-platform pass** — three-way inter-org data movement split: "MFT = transfer-event file movement, EDI = standardized business-transaction documents, exchange = dataset offerings with entitlements"; joint review recommended.
2. **data-integration-platform pass** — "files may be a pipeline's medium, but the MFT managed object is the transfer event"; overlap zone flagged.

This pass must discharge/confirm both.

## Initial Boundary (hypothesis before research)

- Core purpose: move files between defined endpoints (partners, hosts, internal storages) as automated, tracked transfer events; the platform holds connectivity, initiates movements by rule, and records outcomes.
- Users: IT/integration/operations staff; external partners as endpoints; business users for ad-hoc exchange.
- Nearest neighbors: File Transfer Application (client tool), File Sync, ETL/ELT & Data Integration, EDI Platform, Data Exchange Platform, Personal Cloud Drive, Enterprise Content Management.
- Unknowns: how products structure the transfer object (job vs event); how ad-hoc person-to-person exchange fits; how strong the automation leg is at the cloud-native pole; how transfer records are surfaced.

## Research Questions

1. What are the core objects — transfer, endpoint/partner, workflow/automation, event record?
2. How is a transfer defined and initiated (schedule, trigger, API, portal, protocol session)?
3. What is recorded per transfer, and how is it surfaced (dashboards, logs, audit, SIEM)?
4. What failure handling exists (retry, alerting, absence detection)?
5. What protocol/storage endpoint surface exists (implementation, not definition)?
6. What security posture (encryption, access control, credentials, certificates)?
7. What roles operate and consume the system?
8. Where are the boundaries with sync / ETL / EDI / exchange / client tools / servers?

## Representative Products

Selected for market position + philosophical diversity + customer-tier diversity + reachable documentation:

| Product | Pole | Why sampled |
|---|---|---|
| **Files.com** | cloud-native MFT / self-labeled "File Orchestration Platform" | deepest reachable operational documentation (Tier 1); modern SaaS pole |
| **Progress MOVEit** | classic category leader (one of the "legacy four") | on-prem server + cloud + automation module split; compliance-heavy; regulated industries |
| **Cleo Harmony** | B2B/supply-chain integration-flavored MFT | trading-partner orientation; transmissions/event triggers/non-event alerts |
| **Kiteworks** | security/compliance-first platform with MFT as one secure workflow | governance/visibility emphasis; platform-embedded variant |

Also referenced but **not reachable** (see Sources / limitations): IBM Sterling (Connect:Direct / File Gateway / Managed File Transfer), Fortra GoAnywhere MFT, Axway SecureTransport, OpenText MFT, JSCAPE. The legacy "big four" (IBM Sterling, MOVEit, GoAnywhere, Axway) are named as a set by Files.com's own market framing.

## Sources

### Reachable (used)

- Files.com — Documentation portal: https://www.files.com/docs (2026-09-08)
- Files.com — Automation & Flow docs: https://www.files.com/docs/automation-and-flow (2026-09-08)
- Files.com — Automations doc: https://www.files.com/docs/automation-and-flow/automations (2026-09-08)
- Files.com — Partners doc: https://www.files.com/docs/partners (2026-09-08)
- Files.com — Audit Log page: https://www.files.com/features/audit-log (2026-09-08)
- Files.com — Managed File Transfer page: https://www.files.com/managed-file-transfer (2026-09-08)
- Files.com — Switch From Legacy MFT page: https://www.files.com/switch (2026-09-08)
- Progress — MOVEit product page + FAQ: https://www.progress.com/moveit (2026-09-08)
- Cleo — Cleo Harmony product page: https://www.cleo.com/products/cleo-harmony (2026-09-08)
- Kiteworks — Managed File Transfer page: https://www.kiteworks.com/managed-file-transfer/ (2026-09-08)

### Not reachable (limitations recorded; assertions held at lower strength)

- docs.goanywhere.com / goanywhere.com — HTTP 403 (two attempts, abandoned)
- ibm.com/docs/en/connect-direct — HTTP 403; ibm.com/products/managed-file-transfer — redirects to generic catalog (two attempts, abandoned)
- moveit.docs.progress.com / docs.moveit.progress.com — transport errors (abandoned; product page used instead)
- docs.axway.com — SPA portal returns chrome only, article content not fetchable (abandoned)
- opentext.com/products/managed-file-transfer — HTTP 444 (abandoned)
- jscape.com — 404 (abandoned)

**Evidence impact:** the legacy/mainframe pole and GoAnywhere/Axway operational detail rest on Tier-2 product pages, one competitor's characterization (Tier 3, vendor-claim), and cross-product commonality reasoning — not on their own operational docs. No precise operational claims (numeric limits, defaults, exact retention windows, exact protocol lists for unreachable products) are asserted from model memory.

---

## Product A — Files.com (cloud-native pole)

### Key observations (evidence layer A unless noted)

- Self-definition (Tier 2): "software for moving files between people, systems, and trading partners"; "MFT adds the protocols (SFTP, FTP, AS2), encryption, access control, audit logging, and automation that a plain FTP server can't give you"; "MFT started in the early 2000s, when companies outgrew bare FTP servers". Names three modes: "system to system, partner to partner, and person to person."
- Automation definition (Tier 1, Automations doc): Automations "handle file actions such as Copy Files, Move Files, Delete Files, Create Folders, Import Files, and Run Sync. Each Automation runs based on a trigger like file uploads, file modifications, deletions, inbound webhooks, or scheduled time intervals." Automations "can automatically retry on failure."
- Run outcomes enumerated (Tier 1): Event Channels deliver per-event notifications covering "success, failure, partial failure, skipped, and retryable failure outcomes"; admin email covers terminal/partial failures "after all retries are exhausted."
- Monitoring of absence (Tier 1): "Expectations let you define what a correct file delivery looks like… which files must arrive, where, and by when. Each evaluation window is logged, and missed or invalid deliveries open Incidents." "Expectations also detect when nothing happens at all." (This is SLA/absence monitoring of transfer flows.)
- Shared schedules (Tier 1): Schedules object holds days/times shared by Automations, Syncs, AI Tasks, Expectations, Scheduled Exports; Holiday Calendars skip non-operating days.
- Transfer event record (Tier 1, Audit Log page): "every login, every file moved, every permission change, every protocol session, and every setting change" recorded; per-user, per-folder, per-protocol-session, per-setting-change, per-Automation/Sync-run histories "with the trigger, the outcome, and any retries recorded." "Every download, upload, delete and login is a discrete event with user, protocol, timestamp and IP address." Log is non-editable (WORM), retained for years (plan-scaled — product detail), reachable via app search, API/CLI, SIEM streaming, or log-file delivery (JSON/CSV to own server via Agent). Scheduled compliance reports (Permission Audit, Login History, Share Link Activity, Group Membership, Site Usage by Folder) email-able on a cadence.
- Endpoints of record (Tier 1, Partners + Remote Servers): "A Partner represents an external organization… Each Partner is an isolated, secure container for that organization's users and automated accounts… confined to the Partner's assigned root folder." Partner Channels = "structured two-way exchange paths under the root folder." Partner Admins = delegated external user management; offboarding deletes all partner accounts. Remote Servers integrations: S3, Azure Blob/Files, GCS, SFTP/FTP/FTPS/WebDAV, EFSS, "MFT systems," on-prem via outbound-only Agent (no inbound firewall rule).
- Roles (Tier 1): Site Administrators manage all Automations; Workspace Administrators within their Workspace; Folder Administrators within their folders. Partners carry delegated admins for external users.
- Storage unification (Tier 1/Tier 2): "Every protocol lands in the same folders, under the same permissions and the same audit log." Clouds + on-prem storage "work as one set of folders."
- Transformation at the transfer point (Tier 1): TransformScript "transforms and reshapes the contents of a file as it moves through your workflows… convert between formats such as JSON, CSV, XML, and the EDI and HL7 standards" — optional content-processing leg, explicitly separate from moving/routing ("Where Automations move and route files, TransformScript changes what's inside them").
- Automations vs Syncs seam (Tier 1): "Automations provide logic-driven, event-based workflows… Syncs, on the other hand, focus on reliable file replication between remote systems." — internal confirmation of discrete-event vs continuous-replication seam.
- Ad-hoc human exchange (Tier 2): share links, inboxes, branded portals; "every share-link creation, every recipient who opens one, and every inbox submission is captured as its own event" (same record machinery).
- Migration/market framing (Tier 3, competitor claims — use with caution): legacy MFT = on-prem appliance, per-module licensing, manual key-exchange partner onboarding; "the MFT products IT teams have been running since the 2000s"; the "legacy four" named. Customer stories describe workloads: z/OS batch software distribution, EDI with 150+ dealer/partner population, payroll-vendor exchange hub, carrier shipping feeds.

## Product B — Progress MOVEit (classic category leader)

### Key observations (evidence layer A)

- Self-definition (Tier 2): "automated and secure Managed File Transfer software for sensitive data and advanced workflow automation capabilities without the need for scripting." FAQ: "A Managed File Transfer (MFT) solution provides the security, visibility, and control required for high-volume, secure file transfers. MFT can assure the reliability of core business processes through the secure and compliant transfer of sensitive data among employees, partners, and customers."
- Module split (Tier 2): MOVEit Transfer (on-prem MFT server), MOVEit Cloud ("Managed File Transfer-as-a-Service"), MOVEit Automation ("file transfer automation… Connects to MOVEit Cloud, MOVEit Transfer, hybrid cloud endpoints (AWS S3, Azure Blob, Microsoft OneDrive, SharePoint, Google Cloud Storage), SFTP and FTP/S servers").
- Stated challenges the product answers (Tier 2, near-verbatim): "Transfer files more securely between people and/or systems"; "Provide an interface for external vendors without FTP resources to transfer files"; "Know who is sending, receiving and modifying files through reports, logs and tamper-evident audit trails"; "Enforce data governance and retention policies"; and for automation: "Automate routine or repetitive file transfer and file processing tasks"; "Schedule file transfers with a no/low code builder"; "Orchestrate smart file transfer automation with steps and branch logic"; "Get notified if a key workflow fails to reduce expensive delays or errors."
- Protocol surface (Tier 2 FAQ): FTP, FTPS, SFTP, HTTP/S, SMTP/POP3, CIFS/SMB (network storage), EDIINT AS1/AS2/AS3. "MOVEit supports the transfer of any file type" — content-agnostic.
- Ad-hoc person exchange (Tier 2): desktop client "with the full security, tracking and logging of a MOVEit file transfer"; Outlook add-in (send secure files, read statuses, recall); email-notification → browser sign-on → "View Packages" flow for recipients; scheduled desktop client (MOVEit EZ) "moves files on a scheduled, automated… basis… with minimal user involvement."
- Security posture (Tier 2): encryption at rest and in motion, MFA, tamper-evident audit logging, compliance framing (HIPAA, GDPR, PCI-DSS, SOC 2, ISO 27001).
- Industries (Tier 2): banking/finance, government, healthcare, insurance, manufacturing, education — regulated-sector orientation.

## Product C — Cleo Harmony (B2B/supply-chain flavored)

### Key observations (evidence layer A)

- Positioning (Tier 2): "File Integration Solution" under Cleo's "Managed File Transfer — Secure and automate file exchange workflows" solution line; Move / Control / Act framing.
- Transmission control (Tier 2, near-verbatim): "Schedule transmissions to occur automatically, at any time or interval"; "Set event triggers to speed up processing in high-volume environments."
- Monitoring/logging (Tier 2): "Monitor the activity of all data moving through your systems in real-time, with granular reporting, alert notifications, and dashboards"; "Robust file transfer and comprehensive logging"; "Set and monitor non-event alerts and resend files" — absence ("non-event") detection and resend machinery.
- Partner certificate lifecycle (Tier 2): "View and manage all your organization's certificates; Exchange certificates and notify partners of expirations certificates… activation scheduling and overlapping."
- Context (Tier 2): Cleo's surrounding platform is trading-partner onboarding/EDI/supply-chain; MFT sits as the file-exchange transport layer inside a B2B integration suite.

## Product D — Kiteworks (security-platform variant)

### Key observations (evidence layer A)

- Positioning (Tier 2): "Enabling Zero Trust Data Exchange in one platform"; MFT is one of several "Secure Workflows" (file share, email protection, forms, DRM, VDR); "exchange private data between people, machines, and systems."
- Emphasis (Tier 2): unified visibility for security teams over "all data entering and leaving the organization"; governance/compliance packaging (long list of regional compliance regimes); CISO dashboard; deployment-choice discussion (cloud vs on-premise).
- Documentation depth is lower this pass (marketing/blog pages only); used as a variant witness for the security-platform packaging, not for operational claims.

---

## Cross-product Comparison

| Dimension | Files.com | MOVEit | Cleo Harmony | Kiteworks | Strength |
|---|---|---|---|---|---|
| Defined endpoints/partners of record | Partners (isolated containers) + Remote Servers + Agent | Hosts/partners; external vendors; cloud endpoints; SFTP/FTP-S servers | Trading partners with certificate exchange | "people, machines, and systems" exchange relationships | **All 4** (B) |
| Rule-initiated automated transfers | Automations (upload/modify/delete/webhook/schedule triggers) | Scheduled tasks, no/low-code builder, steps + branch logic | Scheduled transmissions + event triggers | automated exchange (lower doc depth) | **All 4** (B) |
| Per-transfer/run outcome record | Discrete events (user/protocol/timestamp/IP) incl. automation runs w/ trigger+outcome+retries | Tamper-evident audit trails, reports, logs — "know who is sending, receiving and modifying" | "Comprehensive logging", real-time monitoring, granular reporting | unified visibility/tracking claims | **All 4** (B) |
| Failure handling | Auto-retry; failure outcomes (failure/partial/skipped/retryable) alerting; absence detection (Expectations→Incidents) | "Get notified if a key workflow fails" | Non-event alerts + resend | not confirmed this pass | **3/4** (B) |
| Protocol breadth incl. B2B transports | SFTP/FTPS/FTP/WebDAV/HTTPS/AS2 | FTP/FTPS/SFTP/HTTPS/AS1–3/CIFS | partner-protocol library implied (not itemized on page) | SFTP claimed | **2 itemized + 1 implied** (B) |
| Encryption/access control posture | AES/TLS claims, SSO/SCIM/MFA, folder permissions | at rest + in motion, MFA | certificate management | central pillar ("Zero Trust", compliance list) | **All 4** (B) |
| Ad-hoc person-to-person exchange | share links, inboxes, portals | packages, desktop/mobile/Outlook clients | "ad hoc transfer" mentioned | file-share workflow sibling | **All 4** (B) — common, not definitional |
| Content processing at transfer | TransformScript (JSON/CSV/XML/EDI/HL7), PGP feature pages | "file processing tasks" in automation | not detailed on page | not detailed this pass | **2 explicit** (A/B) — optional |
| Storage unification / cloud endpoints | same folders for all protocols; S3/Azure/GCS | hybrid cloud endpoints listed for Automation | not detailed | not detailed | **2 explicit** (A) — common |
| Absence/SLA monitoring | Expectations → Incidents | — | non-event alerts | — | **2** (A) — optional/advanced |
| Compliance reporting packaging | scheduled audit reports | compliance framing central | — | compliance regimes central | **3** (B) — variant emphasis |

## Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **Defined endpoints of record.** The platform persistently holds named connection relationships — external partner organizations, remote hosts, internal/cloud storages — with their protocol bindings and credentials, so that file movement addresses a held endpoint rather than asking a human to supply "where and how" each time. Remove → endpoints exist only per-session inside a client tool or bare server; that is the File Transfer Application / bare-server territory, not MFT.

2. **Platform-executed, rule-initiated transfer of files.** The platform itself carries out file movements between those endpoints as its own managed operations — initiated by schedules, event/trigger conditions, or programmatic/API/portal requests (including partner sessions against held endpoints) — rather than existing only as a passive receptacle for whatever a person moves with an external tool. Files move as opaque whole units; the platform governs the movement, not the file's internal meaning. Remove → movement is entirely human-ad-hoc (client tool) or passive (server); automation of the flow is gone.

3. **The transfer event record with outcome.** Every transfer/attempt is captured as a discrete, retained record — what file(s), which endpoints, direction, when, by whom/what trigger, protocol, outcome (success/failure, retries) — surfaced to operators for monitoring, alerting, and audit. Remove → the movement is an unmonitored pipe; "managed" collapses into mere transport.

Jointly-held is load-bearing:

- 1 without 2+3 → configured-address client tool / bare server (endpoints + ad-hoc human transfers, weak record)
- 2 without 1+3 → ad-hoc copy scripts with no held connectivity or record
- 3 without 1+2 → a log file, not a transfer platform
- 1+2 without 3 → automated but blind pipe (not "managed")
- 1+3 without 2 → a server with logging (passive, per-transfer human initiation only)
- 2+3 without 1 → scheduled scripts with logs but no held endpoint relationships

### Historical / market-sample check

- Mainframe-era transfer systems and 2000s on-prem MFT (the recognized lineage of this Type) are organized exactly as: held partner/host records, scheduled/batch-initiated transfers, retained transfer statistics/logs with resend on failure. They satisfy the three legs with no cloud, no portals, no protocol breadth, no SaaS. (Canonical inference C, supported by Files.com's migration framing + MOVEit/Cleo structure; direct legacy-product operational docs were unreachable this pass — assertion held at conceptual strength.)
- A bare FTP/SFTP server (endpoints only at connect time, human-initiated session transfers, minimal per-transfer records) fails legs 2+3 → correctly outside the Type. A desktop FTP client fails 1+2+3. A folder-sync tool fails the discrete-event record leg (continuous reconciliation instead).
- Check passes: the definition is not over-fitted to the current cloud-native implementation.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Protocol breadth on one storage core: SFTP/FTPS/FTP/HTTPS/WebDAV sessions plus B2B transports (AS2-class) all landing in the same permissioned, audited file space.
- Failure machinery: automatic retry with bounded attempts; alerting on terminal/partial failure; in mature products, absence ("non-event") detection that raises an incident when an expected delivery does not arrive.
- Transfer-time content processing: PGP encrypt/decrypt, compression, rename/flatten, routing rules by partner/type/time; deeper format transformation (CSV/XML/EDI/HL7) in some products.
- Security posture: encryption in transit and at rest; folder/file permissions; user/group/role administration; SSO/MFA; credentials and host keys held and rotated by the platform; partner certificate lifecycle in B2B-heavy products.
- Storage integration: cloud object stores and on-prem filesystems reachable directly or through an outbound-only agent/gateway.
- Programmatic surface: REST APIs, SDKs/CLIs, webhooks/event streams (including SIEM delivery) to drive and observe transfers from other systems.
- Administrative console: users, groups, workspaces/tenancy, partner onboarding/offboarding as a unit, delegated partner administration.

### L2 — Variant / Optional Structure

- Deployment: on-prem server / DMZ+agent architecture / SaaS cloud / hybrid; mainframe-lineage integrations in the legacy pole.
- Exchange modes: system-to-system, partner-to-partner, person-to-person ad-hoc (packages, inboxes, share links) — the mix varies by product and market; some products center ad-hoc secure exchange, others are almost purely machine flows.
- B2B/EDI-gateway flavor: AS2/EDIINT transports, MDN receipts, partner certificate exchange, trading-partner onboarding lifecycles — heavy in supply-chain-flavored products.
- Content transformation depth: none → light (rename/route) → format transformation at the transfer point.
- Compliance packaging: scheduled audit reports, retention windows, regional compliance regimes — emphasis varies (security-platform pole most pronounced).
- HA/clustering, high-speed transfer technology, e-discovery/legal-hold packaging — optional/advanced.

### L3 — Vendor-specific (research notes only)

- Files.com: Partner/Workspace container model; Expectations→Incidents; TransformScript; Holiday Calendars; "File Orchestration Platform" self-label; WORM audit log with long retention; nine permission levels; log-file streaming; Agent; published pricing as a differentiator; competitor comparisons naming "legacy four".
- MOVEit: Transfer/Cloud/Automation module split; MOVEit EZ scheduled desktop client; Outlook add-in; packages/recall model; specific supported databases; AS1/AS3 protocols.
- Cleo: Harmony vs Integration Cloud split; non-event alerts; scorecarding/chargeback-prevention ecosystem features; trading-partner network services.
- Kiteworks: private data network/control plane framing; MFT as one secure workflow among email/forms/VDR/DRM; CISO dashboard.
- Legacy characterization via competitor claims (Tier 3): per-module licensing, appliance footprint, manual key-exchange onboarding, z/OS batch workflows — recorded as vendor-claim strength only.

## Boundary Findings

| Neighbor Type | Seam | "Remove what → becomes the other Type" |
|---|---|---|
| File Transfer Application (§03.15) | user-operated client tool; each movement human-initiated; endpoint lists are convenience entries, not held relationships; no platform-executed automation or managed transfer-event record | remove platform-executed rule-initiated transfers + endpoint-of-record management → a client tool |
| File Sync Application (§03.15) | continuous state reconciliation vs discrete transfer events with initiation and outcome; Files.com itself documents Automations-vs-Syncs as different features | make the unit continuous equivalence-maintenance instead of discrete tracked movements → sync |
| ETL/ELT & Data Integration Platform (§13) | pipeline is the managed object (connections + persistent pipelines + managed execution, transformation-centric); files may be the medium | make the persistent pipeline (not the transfer event) the managed object with record-level transformation → integration platform |
| EDI Platform (§13) | standardized business-transaction document semantics (mapping, acknowledgments-as-documents); MFT is content-agnostic about file meaning | add document-semantic mapping/acknowledgment machinery as the core → EDI platform |
| Data Exchange Platform (§13) | dataset offerings with entitlements/discovery; MFT has no offering/entitlement semantics | make entitlement-to-a-dataset-offering the core object → exchange platform |
| Personal Cloud Drive (§03.15) | person-facing storage/sharing; no endpoint automation or partner-of-record | remove endpoint automation + held partner records → personal cloud drive |
| Enterprise Content Management (§10) | document lifecycle/governance inside a repository vs movement between endpoints | center repository lifecycle rather than endpoint movement → ECM |
| Secure email / ad-hoc sending tools | ad-hoc person-to-person sending is a **mode** inside MFT, but the Type centers held-endpoint automation + records | center ad-hoc person messaging only → different Type |

The three-way inter-org movement split from the data-exchange pass is **confirmed from this side**: MFT = transfer-event file movement; EDI = standardized business-transaction documents; exchange = dataset offerings with entitlements. The data-integration pass's note ("the MFT managed object is the transfer event") is **confirmed and made load-bearing** in L0 leg 2–3.

## Uncertainties

- Legacy pole operational detail (IBM Sterling / GoAnywhere / Axway / OpenText) unverified this pass; legacy characterization rests on Tier-2 pages + one competitor's Tier-3 claims + cross-product inference. Held at conceptual strength; no precise claims asserted.
- Kiteworks documentation depth was low (marketing pages); its observations are held at positioning-strength only.
- Whether "absence/non-event monitoring" is universal in mature MFT (observed in 2/4 sampled) — held as optional/advanced, not standard.
- Whether person-to-person ad-hoc exchange is definitional: sampled products all include it as a mode, but pure machine-flow deployments exist; held as common mode, not definitional.
- Directory placement: MFT sits in §13 (Data, Analytics & AI Systems) while its client/server siblings sit in §03.15 (Files). This is a taxonomy placement question, not a Type-boundary problem; recorded, not acted on.

## Final Synthesis

Managed File Transfer is the organization's system for moving files between held endpoints as managed, observable events. Its defining core is three jointly-held structures: **(1) defined endpoints of record** (partners/hosts/storages with held protocol bindings and credentials), **(2) platform-executed, rule-initiated file transfers** (schedules, triggers, API/portal/protocol-session initiation, files moved as opaque units), and **(3) the transfer event record with outcome** (discrete, retained, surfaced for monitoring, alerting, and audit). The "managed" qualifier is carried by legs 1+3 around the executed movement of leg 2; remove any leg and the product collapses into a bare server, a client tool, ad-hoc scripts, a blind pipe, or a log file. Everything else popularly associated with MFT — protocol breadth, PGP/transformation, SIEM streaming, portals, compliance packaging, absence monitoring, cloud storage integration — is standard mature capability or variant packaging, not definition.
