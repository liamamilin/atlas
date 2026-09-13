# Research Notes — Legal Hold Management

Research date: 2026-09-07
Slug: legal-hold-management
DIRECTORY leaf: "Legal Hold Management" (§11 Legal, Risk, Compliance & Governance)

## Research Goal

Understand what "legal hold management" software actually is as an Application Type: its central objects, the custodian-facing and administrator-facing workflows, the lifecycle from hold creation to release, the role of technical preservation-in-place versus process management, and the boundaries against eDiscovery platforms, matter management, records management, and archiving/compliance products that expose a "hold" capability.

## Initial Boundary

Initial hypothesis (pre-research):

- A legal hold (litigation hold, preservation hold) is the practice of instructing identified people ("custodians") to preserve potentially relevant information when litigation or investigation is reasonably anticipated, and of tracking that instruction.
- The application Type is expected to center on: the hold record, the custodian population, notices, acknowledgment tracking, reminders/escalations, release, and audit/defensibility evidence.
- Nearest neighbors: eDiscovery Platform (legal hold is the first stage of the eDiscovery pipeline), Legal Matter Management (matter anchor), Enterprise Records Management (retention schedules — a hold suspends disposition), Corporate Investigation Management (investigations trigger holds), and archiving/compliance suites that ship a "litigation hold" content-freeze capability.
- Suspected confusion: "legal hold" in the market names both the human duty workflow (notice → acknowledge → track → release) and a technical in-place data freeze. Which of these carries the Type is a primary research question.

## Research Questions

1. What is the central object — the hold, the matter, the custodian?
2. What does the hold lifecycle look like (draft → issue → active → remind → release)? Is release reversible?
3. How do custodians interact (notice delivery, acknowledgment, questionnaires, re-acknowledgment)?
4. What reminder/escalation machinery exists and is it definitional or standard?
5. How does the product interact with actual data preservation — does it preserve data itself (in-place holds) or manage the human process while preservation happens in connected systems?
6. What does "defensibility" concretely mean in these products (reports, audit trails, versioning)?
7. Where is the boundary with eDiscovery platforms, matter management, records retention, and archiving-based hold capabilities?
8. Would older, non-software practice (memos + tracking spreadsheets) still satisfy the definition? (historical check)

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers/packaging.

1. **Exterro** — legal-hold-first pure play inside an eDiscovery/legal-governance suite; enterprise legal-ops pole. Product page (Tier 2) fetched; vendor is also the boundary-informing product recorded by the corporate-investigation-management pass.
2. **Logikcull (now Reveal)** — self-serve eDiscovery platform where legal hold is the entry stage; subscription tiering; Slack delivery of holds. Support documentation (Tier 1) fetched — deepest operational detail of the sample.
3. **Microsoft Purview eDiscovery** — platform-native compliance module inside a productivity suite; hold realized both as a technical content-location hold (base tier) and as custodian management + legal hold notifications (premium tier). Official Learn documentation (Tier 1) fetched — documents both the process leg and the technical leg in one vendor.
4. **Everlaw** — litigation eDiscovery platform with a dedicated Legal Holds tool managed at organization level, matter containers, custodian directories, and data-preservation objects for external systems. Knowledge Base (Tier 1) fetched.

Considered and abandoned: Pagefreezer (legal-hold page 403 — archiving-vendor pole not directly observed), Relativity (help URL 404; RelativityOne Legal Hold module not reached), Exterro free-tier page (404).

## Sources

- Exterro — "Legal Hold & Preservation" product page, https://www.exterro.com/e-discovery-software/legal-hold (fetched 2026-09-07, Tier 2). Marketing page; operational claims below the "feature" level treated cautiously. Root page also fetched for product taxonomy.
- Logikcull (Reveal) — docs portal index, https://docs.revealdata.com/logikcull (category "Legal Hold and Preservation"); "Creating Legal Holds", https://docs.revealdata.com/logikcull/docs/creating-legal-holds.md (fetched 2026-09-07, Tier 1). Additional hold articles listed in the index (release FAQ, templates, Slack hold, Vault/M365 preserve-in-place integrations) — titles observed, bodies not fetched.
- Microsoft Learn — "eDiscovery legacy solutions" overview, https://learn.microsoft.com/en-us/purview/ediscovery; "Learn about eDiscovery" (new experience), https://learn.microsoft.com/en-us/purview/edisc; "Create holds in eDiscovery", https://learn.microsoft.com/en-us/purview/edisc-hold-create (fetched 2026-09-07, Tier 1). Note: classic eDiscovery experiences retired 2025-08-31; the "custodian management + legal hold notifications" description is quoted from the legacy-overview page describing the Premium solution.
- Everlaw — Knowledge Base, "Introduction to Legal Holds", https://support.everlaw.com/hc/en-us/articles/4408079521819-Introduction-to-Legal-Holds; "Legal Holds: Hold Notices", https://support.everlaw.com/hc/en-us/articles/4408079526171-Legal-Holds-Hold-Notices (fetched 2026-09-07, Tier 1). Additional articles (Hold Notices tracking, custodian summary page, data preservations) observed via KB index titles.

Unreachable (recorded per source-access limitation rules): pagefreezer.com/legal-hold (403 ×1); exterro.com/free-legal-hold (404 ×1); help.relativity.com Legal Hold page (404 ×1); learn.microsoft.com/ediscovery-custodians and /ediscovery-premium-overview (404 — URLs moved). No product claims made for Pagefreezer or Relativity.

## Product Observations

### Exterro (Legal Hold & Preservation) — evidence tier A for marketing-page claims, no Tier-1 body

Key observations (product page):

- Product framed as managing "legal holds from scoping to release" — the lifecycle spans scoping → issue → preserve → release.
- "Legal hold saves time and increases defensibility by allowing you to easily manage data preservation activities through legal hold and in-place preservation technology" — two named legs: the hold process and in-place preservation.
- Scoping and "custodian interviews" named as activities; In-Place Preservation positions preservation of "custodial and non-custodial data" as a separate but linked capability ("preserve broadly and refine as your matter team gets additional data points").
- Automated reminders and escalation notices: "customize automatic hold reminders to be sent to custodians, allowing them to acknowledge their legal holds in one click... Send automatic escalation emails to their manager to encourage compliance." One-click acknowledgment + manager escalation directly documented.
- Defensibility = "maximum hold compliance and generate powerful reports with robust audit trails"; dashboards and reporting on the preservation process.
- Templates, "pre-set workflows" for drafting/sending holds.
- Comprehensive Interview: "configurable interview templates and questionnaires to send to your custodians immediately upon issuing a hold... logs all interview activity and responses for increased defensibility."
- Employee Change Monitor: detects employee status changes (departures, name/title changes) and "automatically performs actions including assigning tasks, sending notifications" — spoliation-risk framing around custodian population changes.
- AI layer (Exterro Assist) automating "custodian identification, legal holds, and acknowledgments" — vendor marketing numbers (400x, 95%, 6 seconds) recorded here only, excluded from the final document.
- 190+ connectors to enterprise data sources; compliance portal named in the FAQ list (module — vendor-specific).
- Positioning context: legal hold is one module of an eDiscovery suite (Subpoena Manager, Data Management, Review, etc. are siblings in the same product taxonomy).

### Logikcull (Reveal) — evidence tier A (Tier-1 support doc, deep)

Key observations from "Creating Legal Holds":

- Creation flow is a 4-step wizard: name the hold (a project is created automatically — "Projects are required for legal holds because legal holds are fully integrated with our Discovery product"; a hold can be attached to an existing project) → compose message → add custodians → review & send.
- The hold object carries: internal notes (not visible to custodians, exportable to a report field), hold message, reminder message ("precedes the original legal hold notice if you select to Resend"), release message (with variables incl. "List of Active Legal Holds for Custodian" — explicitly used to remind a released custodian of remaining holds).
- Message composition: templates ("start from a template"), subject, sender display name (emails sent from a fixed vendor address; verified custom sender addresses on a premium tier), reply-to (tip: a designated internal inbox to consolidate custodian replies), CC recipients (receive copies, not custodians), acknowledgment button text (customizable), attachments (virus-scanned, pending state until scan completes).
- Variable/merge fields in notice text (custodian names, created date, notice subject).
- Custodians: added by pasting email lists (with optional names), drawn from "Available custodians" (previously-used custodians stored at account level), or via Slack integration; **silent custodians** toggle — "tracked as part of your legal hold but will not receive any emails."
- Privacy of distribution: "Each custodian will only see that the hold notification was sent to them individually" — no visibility into other recipients.
- Preserve Data (premium): preserve-in-place integrations for Google Vault and Microsoft 365 — the hold can trigger technical preservation in external systems.
- Survey/questionnaire: optional; custodians are "automatically directed to (and required to complete)" the survey after clicking the confirmation button; builder with answer types (Yes/No, Date, Date/Time, Number, Multiple Choice, Paragraph, Short Answer), reorderable questions; results exportable as CSV; survey templates reusable.
- Sending: immediate or scheduled delivery; **reminders on non-acceptance** (to custodians who have not clicked the acknowledgment button); **resend email** (re-send the hold to all custodians at a set frequency, preceded by the reminder message); test message to self.
- Editing an issued hold: everything editable except custodians cannot be removed (only added) and surveys cannot be added/edited after send. Editing the subject/hold message/acknowledgment button offers "Update & Resend" which **resets every custodian's confirmation status and requires re-acknowledgment**; "Update" sends the new version only to newly added custodians. "The Custodian Report will capture every version of the hold that each custodian received."
- Reports: "Download Hold Report" (all active, paused, and released holds; hold name, created by/date, hold status, reminder frequency, **custodian count, confirmed count, pending count, failed count, released count**, notes) and "Download Custodians Report" (custodians, project info, active/inactive states, delivery dates, confirmation status).
- Hold status vocabulary observed: active / paused / released; counts pending / failed.
- Release: "Release Hold" for all custodians via the hold card menu; optional release email (default sent); after release: status "Released", all custodians "Released", **"A 'Released' hold cannot be changed to an 'Active' hold"**, notes remain editable, reports continue to be available "until they are deleted."
- Custodian-level removal: **delete** (for mistakes — removes from hold page, shows as "Deleted" in reporting) vs **release** (no longer required to be on hold — shows as "Released"); a removed custodian is notified of removal. No per-custodian release in this product (single-custodian release not offered; delete substitutes).
- Access control: only Account Owners and Account Admins can access/view/edit legal holds; "The Holds section of the app is not visible to non-account admins."
- Delivery channel extension: legal holds can be sent and confirmed **through Slack** (separate articles in the same section).

### Microsoft Purview eDiscovery — evidence tier A (Tier-1 official docs)

Key observations:

- The category split is explicit: base eDiscovery tier = "Place content locations on legal hold" (a technical hold); premium tier adds **"Custodian management"** and **"Legal hold notifications"** — "Manage the process of communicating with case custodians. A legal hold notification instructs custodians to preserve content that's relevant to the case. You can track the notices that were received, read, and acknowledged by custodians. The communications workflow... allows you to create and send initial notifications, reminders, and escalations if custodians fail to acknowledge a hold notification."
- Custodian definition: "the people that you've identified as people of interest in the case... plus other data sources that may not be associated with a custodian" (non-custodial data sources). Adding custodians enables: placing their data sources on hold, communicating via the notification process, and searching/collecting their data.
- The hold itself (new experience, "Create holds"): created **within an eDiscovery case** (case = "contains all searches, holds, and review sets related to a specific investigation"); hold policies carry name/description (unique per organization), scoped to data sources (users' Exchange mailboxes + OneDrive, group/team mailboxes and sites, organization-wide locations).
- Scoping: infinite hold (all content) vs **query-based hold** (only content matching a query) vs **date-range hold**; hold status tracked **per location** (on hold / not on hold / error).
- Technical mechanics documented (the "preservation leg" in its purest form): holds can take up to 24 hours to take effect; query-based holds initially hold all content and periodically clear non-matching content; deleted SharePoint documents are retained in a "Preservation Hold library"; removing a location from a hold triggers a **30-day delay hold** to prevent immediate purging; closing a case turns holds off and applies delay holds; group membership captured as a point-in-time snapshot at policy creation; per-user licensing requirements; separate **Litigation Hold** admin mechanism exists at the mailbox level (referenced as distinct).
- Explicit boundary guidance from the vendor: "For long term data retention not related to eDiscovery investigations, use retention policies and retention labels" — retention policy vs eDiscovery hold seam.
- Process transparency: Process manager/report for hold operations (status, created/completed, duration, created by).

### Everlaw — evidence tier A (Tier-1 KB, deep)

Key observations:

- Organization-level Legal Holds tool: "send hold notices to custodians in your organization and create data preservations on those custodians in Microsoft 365. When it comes time to collect documents from your custodians, you can connect your legal hold custodians to documents uploaded in your Everlaw database." — the hold stage is explicitly the pre-collection phase of an eDiscovery workflow.
- **Matter** defined: "A space to house custodians and legal holds in the early phases, before documents are ready to upload." Legal holds live in matters; matters can later promote to databases (evidence containers). Historically holds could live in databases; product has migrated to matter-first (database-managed holds deprecated and converted, January 2026).
- Three managed object types inside a matter: **hold notice** (communication), **data preservation** (preservation-in-place hold object created in external systems — Microsoft 365/Purview, Google Vault, Slack per release notes), **external data preservation** (a tracking record for a preservation made and managed outside the platform).
- Permissions: Organization Admin or **Legal Holds Organization Admin** (full access), **Legal Holds Viewer** (read-only); per-matter "Restrict matter permissions" for sensitive matters. The holds capability is carved out of the review product's permission model.
- **Custodian directories**: organization employee directories; custodian side panel aggregates "all of the legal holds that custodian belongs to in the entire organization, grouped by matter." Custodian records carry HR-style attributes (manager name/email, employee type, start/end dates, department, office, preferred language) surfaced in exports.
- Hold notice creation wizard: name (blank or copy existing) → select custodians from directories → draft email (subject defaults to hold name; reply-to; cc/bcc; merge fields incl. #CustodianName, #ManagerName, #HoldNoticeName, #IssueDate, #CustodianList; attachments with size limit; test emails incl. "view email as" a specific custodian) → questionnaire → **auto-renotification** → **auto-escalation** → **reminder** settings → summary → issue.
- **Acknowledgment required by default**; disabling acknowledgment also disables questionnaire, auto-renotification, and auto-escalation (they presuppose acknowledgment).
- **Auto-renotification**: reminder emails to custodians who have not yet acknowledged (default every 7 days until acknowledged). **Auto-escalation**: emails to the custodian's manager when unacknowledged (default starting 14 days after send, every 7 days until acknowledgment or release; custodian is always cc'd and cannot be removed as cc; warning if a selected custodian lacks a manager email). **Periodic reminders**: sent to **all custodians regardless of acknowledgment status** (default every 3 months; months/weeks/days configurable; optional **require acknowledgment with each reminder**) — rationale quoted: "Some legal holds last for months or even years, and legal hold administrators have a duty to ensure that all custodians on those holds are periodically reminded."
- **Custodian experience**: email → "View and acknowledge hold" → **legal hold acknowledgement portal** (accountless — custodians need no Everlaw account; the portal is not tied to any Everlaw account even if one exists) → questionnaire if present → confirm → confirmation page **plus a confirmation email including the date and time of acknowledgment**; re-visiting the portal shows "already acknowledged."
- Send is irreversible: "Once emails have been sent, they cannot be unsent." Admins may receive confirmation summary emails containing all settings and notice text ("the date and time that the hold was sent").
- Questionnaire builder: question types (multiple choice, checkboxes, dropdown, short text, long text, date, date range), pages, required/optional per question, **conditional visibility** and **logic rules**, preview, copy-existing, introduction text; purpose quoted: "collect additional information from the custodians, such as identifying additional devices that may contain relevant data and additional custodians who should also be included in the legal hold."
- Status vocabulary (from export column documentation): hold/custodian statuses include Draft, Issued, Creating, Creation error, Nonexistent, Active, Releasing, Releasing error, Released, Pending, Error; exports count custodians as not acknowledged / acknowledged / released / errored / pending / active.
- Reporting/exports: "filtered legal holds" CSV (hold name, status, custom field values, custodian counts, issuer, first/last issued date, release date, preservation start date, **hold custom ID, hold version ID**, keywords, hold URL, notes) and "custodian summary" CSV (per-custodian-per-hold rows with acknowledgment status/date, directory, manager, HR attributes). Same data available via API.
- Governance: custom fields on matters with bulk CSV import; matter status (deactivate/activate) — **a matter can only be deactivated after all holds within it are released**; all status changes logged as events on the User Access History page.
- Versioning: hold version IDs in exports (echoes Logikcull's "every version of the hold" reporting).

## Cross-product Comparison

| Aspect | Exterro | Logikcull (Reveal) | Microsoft Purview | Everlaw |
|---|---|---|---|---|
| Packaging | Standalone module of an eDiscovery/legal-governance suite | Legal hold as entry stage of a self-serve eDiscovery product | Compliance-suite module (base tier: hold-only; premium tier: custodian mgmt + notifications) | Dedicated org-level Legal Holds tool inside a litigation eDiscovery platform |
| Central container | Hold tied to matter context (product page level) | Hold creates/is attached to a project | Hold policy inside an eDiscovery case | Matter (defined as the early-phase container before upload) |
| Hold of record | "scoping to release" lifecycle; dashboards/reports | Hold card with status (active/paused/released), notes, versions | Hold policy (named, org-unique) with per-location hold status | Hold notice / data preservation / external data preservation records with version IDs |
| Custodian model | Custodians + interviews + employee-change monitoring | Email-paste, account-level custodian reuse, silent custodians | Custodians (people of interest) + non-custodial data sources | Org directories, HR attributes, custodian-level cross-hold view, silent custodians (implied by "non-silent" phrasing) |
| Duty communication | Hold notices with templates, one-click acknowledge | Email (or Slack) notice with customizable acknowledgment button | Legal hold notifications (premium): initial / reminders / escalations | Hold notice email + accountless acknowledgment portal |
| Acknowledgment tracking | One-click acknowledgment; automated reminders; manager escalation | Button-click confirmation; per-custodian status; reset & re-acknowledge on notice edit | Track received / read / acknowledged | Portal acknowledgment + confirmation email with timestamp; re-acknowledgment per reminder optional |
| Questionnaires | Comprehensive Interview module (configurable templates, logged responses) | Optional survey required to complete confirmation | Not observed at this tier (data source mapping instead) | Full builder: question types, pages, conditional visibility, logic, required/optional |
| Non-acknowledger machinery | Automated reminders + escalation to manager | Non-acceptance reminders; resend to all at frequency | Reminders + escalations (premium notifications) | Auto-renotify (7d default) + auto-escalate to manager (14d start, 7d cycle default) |
| Long-hold reminders | Present (automation framing) | Resend at set frequency | Present (notifications) | Periodic reminders to ALL custodians regardless of acknowledgment (3-month default) |
| Technical preservation | In-Place Preservation module + connectors; "preserve broadly, refine later" | Preserve-in-place integrations (Google Vault, M365) on premium tier | The hold IS the technical mechanism (in-place, query-based, date-bound; delay holds; Preservation Hold library) | Data preservation objects in M365/Vault/Slack; external data preservation tracking records |
| Release semantics | Lifecycle ends at release; in-place preservation released | Release hold (all custodians); release message optional; release irreversible; delete-vs-release custodian distinction | Remove locations from hold; 30-day delay hold; case closure turns holds off | Release custodians / release all holds; matter deactivation gated on all holds released |
| Defensibility evidence | Audit trails, reports, interview logging | Hold Report + Custodians Report capturing versions and per-custodian status | Per-location hold status; process reports | User Access History events; exports with hold version IDs; admin confirmation emails |
| Access model | Role-based (legal team; not detailed on page) | Account Owners/Admins only; section hidden from others | Case membership + RBAC role groups | Org Admin / Legal Holds Admin / Viewer; per-matter restrictions |

**Reading of the comparison:**

- All four products implement the same human-duty loop: identify custodians → send a preservation notice → track acknowledgment → remind/escalate → release. This loop is the market's center of gravity for "legal hold."
- Technical preservation-in-place appears in all four but is realized as an *adjacent or integrated capability* (module/integration), except in Microsoft where the base-tier hold *is* purely technical and the custodian workflow is the premium layer — Microsoft's own two-tier split is strong evidence that the technical freeze and the duty-management workflow are separable, and that the market category (and this directory leaf) corresponds to the duty-management workflow with preservation as its most common complement.
- The matter/case/project container exists everywhere but is realized differently (project, case, matter) — the container is an anchor, not the defining object.
- Reminder/escalation automation, questionnaires, templates, and reports are universal in mature products but demonstrably absent in simpler realizations (Microsoft base tier has holds without notifications; a spreadsheet-era hold had none of these).

## Abstraction

### L0 — Defining core (invariants; remove any one → different Type or no Type)

A legal hold management application maintains, for a specific matter/case/investigation:

1. **The hold of record** — a persistent, identified record that a preservation duty exists: what triggered it, what it covers, when it was issued. The unit everything else attaches to. *(Remove → scattered memos/emails; no managed process.)*
2. **The custodian population** — identified people placed under the duty, with membership explicitly managed over time (custodians added as scope evolves, released individually or in bulk). *(Remove → a content-location freeze: a preservation capability of storage/archiving/records systems, not this Type.)*
3. **Duty communication with compliance tracking** — the system communicates the preservation duty to custodians and records each custodian's compliance state (delivered / acknowledged) *against the hold*, per custodian. *(Remove → a duty list; one-off memos; spreadsheet tracking.)*
4. **Release as a recorded lifecycle act** — the hold — and each custodian's duty — ends through a distinct recorded release (not by deletion of the record); the hold's history remains reportable after release. *(Remove → a retention policy: standing, unconditional, with no matter-scoped on/off.)*

Jointly-held is load-bearing: a hold of record without custodians = technical content hold; custodians without communication/tracking = a list; communication without a hold of record = memos; without release semantics = retention.

### L1 — Standard capabilities (common mature structure; not definitional)

- Automated reminders to non-acknowledging custodians; escalation notices to custodians' managers; periodic reminders to all custodians for long-running holds (with optional re-acknowledgment)
- Notice templates and reuse; merge fields; reply-to routing; cc recipients who are not custodians; test sends
- Questionnaires/interviews attached to the hold (scope discovery: devices, systems, additional custodians)
- Custodian directories drawn from organization/HR data; custodian reuse across holds; custodian-level cross-hold views
- Hold status model and per-custodian status counts (issued/pending/acknowledged/released/errored)
- Defensibility reporting: hold reports and custodian reports, notice versioning, event/audit history of administrative actions
- Role-based access (administrator vs viewer; case/matter-scoped visibility; sensitive-matter restrictions)
- Technical preservation-in-place integration (mailboxes, archives, collaboration systems) — the "preservation leg," common but externalized or modularized in most products
- Handoff linkage to collection/review: connecting held custodians to later-collected documents

### L2 — Variant / optional

- Delivery channels beyond email (Slack/instant messaging; acknowledgement via chat)
- Silent custodians (tracked, unnotified)
- Data preservation objects for external systems (tracking records for holds made elsewhere)
- Matter deactivation/activation lifecycle above holds
- Custom fields on matters/holds; bulk import; API access
- AI assistance (custodian identification, automation of hold tasks)
- Employee change monitoring (departures trigger hold tasks — spoliation-risk framing)
- Dashboards and program-level analytics; free/entry tiers

### L3 — Vendor specifics (research notes only; excluded from the final document)

- Exterro: In-Place Preservation, Employee Change Monitor, Comprehensive Interview, Exterro Assist/ARMOUR AI, "190+ connectors," compliance portal, marketing metrics (400x/95%/6-sec), Fortune-500 customer logos, certification stack.
- Logikcull/Reveal: project-per-hold integration requirement; fixed vendor sender address with premium custom verified senders; attachment limits (5 files / 7 MB; virus-scan pending state); DMARC-domain custom sender setup; Slack app send-and-confirm; "Update & Resend" resetting acknowledgment; delete-vs-release custodian semantics; no per-custodian release; holds section hidden from non-admins; hold statuses active/paused/released with failed counts.
- Microsoft: hold-policy model with org-unique names; point-in-time group membership snapshots; ≤24h hold effectiveness; query-based holds clearing non-matching content periodically (7–14 day timer as documented) and the >5-holds-per-location caveat; Preservation Hold library; 30-day delay holds on release and case closure; per-user licensing tiers (E5-class for premium hold capabilities); mailbox-level Litigation Hold as a separate admin mechanism; distribution-list expansion limits.
- Everlaw: matter container with database promotion; acknowledgement portal accountless and disconnected from Everlaw accounts; default intervals (7-day renotify, 14-day escalation start, 3-month reminders); custodian always cc'd on escalations; consolidated-notification caveat; hold custom ID/version ID; matter deactivation gated on releases; Purview/Vault/Slack data preservations; custom sender address setup; attachment size limit (7 MB).

## Vendor-specific Findings

- **Compliance portal** (Exterro FAQ mention) — vendor module, no other product analog observed.
- **Slack delivery and acknowledgment of holds** — Logikcull; delivery-channel variant, not Type-defining.
- **Silent custodians** — documented in Logikcull; Everlaw's "non-silent custodians" phrasing implies the same concept; treat as common-but-not-universal, retained in final doc as optional with care.
- **Employee change monitoring** — Exterro only in this sample; marked product-specific.
- **External data preservation tracking records** — Everlaw; a low-tech but telling realization: the platform tracks holds made *outside* it. Treat as optional capability.
- **Microsoft two-tier split** (hold without custodian workflow vs custodian workflow + notifications) — direct vendor evidence for the process/technical separability used in the L0/L1 split.

## Rejected Findings

- "Legal hold = litigation hold = retention hold" conflation from archiving products: rejected as the Type's center — archiving hold lacks custodian duty communication/tracking (not directly re-observed this pass; consistent with the Microsoft retention-vs-hold guidance and with the process/technical split).
- Marketing efficacy claims (Exterro 400x/95%/6 seconds) — rejected as vendor marketing, no independent evidence.
- "Projects/cases are required for legal holds" (Logikcull) — product design choice; other products realize the anchor differently.
- AI-driven custodian identification as a defining capability — rejected; current-generation common at best.
- A universal status taxonomy — rejected; status labels vary by product (active/paused/released vs draft/issued/active/releasing/released vs on-hold/not-on-hold/error); only the conceptual states (drafted → issued/active → released) are canonical.

## Boundary Findings

- **vs eDiscovery Platform (§11 sibling, unprocessed)**: the legal hold is the first stage of the eDiscovery pipeline (identify/preserve). Removing the downstream stages (collection → processing → analysis → review → production) leaves legal hold management; making review/production the center leaves eDiscovery. Bundling is the market norm (Logikcull, Everlaw, Exterro, Microsoft) — the two Types share vendors and surfaces, so the boundary must be center-of-gravity, not feature presence. Microsoft's own tier split (hold-only vs custodian+notifications vs full eDiscovery) is vendor-internal evidence of the staged structure. **Flag for the ediscovery-platform pass: treat this document as boundary counterparty; likely keep-both with center-of-gravity seam and "hold as first pipeline stage" cross-reference.**
- **vs Enterprise Records Management (§10)**: retention schedules are standing, policy-driven disposition rules over record classes; a legal hold is a trigger-scoped duty that suspends normal disposition for identified custodians/data until released. Microsoft's guidance states the seam explicitly ("For long term data retention not related to eDiscovery investigations, use retention policies and retention labels"). A hold without release semantics collapses into retention.
- **vs archiving/compliance "litigation hold" capability (email archiving, DM products)**: capability vs Type — a content-location freeze without custodian notices/acknowledgment tracking is not this Type. (Archiving-vendor pole not directly observed this pass — Pagefreezer unreachable; assertion carried at capability-vs-Type level, consistent with the Microsoft split.)
- **vs Legal Matter Management (§11, unprocessed)**: the matter is an anchor/scoping container here; matter management's system of record is the matter itself (status, spend, documents, deadlines). Holds-in-matter (Everlaw) vs matters-with-hold-modules (ELM suites) are the two embeddings; flag recorded for the legal-matter-management pass.
- **vs Corporate Investigation Management (§11, processed 2026-09-07)**: that pass recorded "vs eDiscovery/Legal Hold (evidence machinery without case lifecycle)". Confirmed from this side: investigations *trigger* holds; the hold tool holds no investigation case lifecycle of its own. Keep-both holds.
- **vs Evidence Management System (§24, processed 2026-09-07)**: that pass recorded "custody chain vs preservation/production obligations". Confirmed from this side: custody of identified items vs the duty to preserve custodians' own information. Keep-both holds.
- **vs Compliance Policy Management (§11)**: standing policies vs matter-triggered duties; no overlap of defining objects.
- **vs Data Loss Prevention / Insider Risk (§15)**: hold tools manage a preservation *duty*, not detection/enforcement of data movement. No sampled hold product monitors custodian behavior.

## Uncertainties

- **Archiving-vendor pole unobserved**: Pagefreezer 403; Smarsh/ZL/Global Relay not attempted after the sample reached Stop Conditions. The claim that archiving-suite "legal holds" sit outside this Type rests on the Microsoft tier split and the absence of custodian-workflow language in that market segment — moderate confidence, worth revisiting.
- **Relativity Legal Hold module not reached** (help URL 404); RelativityOne presumably ships a documented hold application — its absence slightly under-represents the litigation-support-platform pole; no claims made.
- **Exterro operational detail**: only Tier-2 product page observed; Exterro's help center not located in this pass. Exterro claims (templates, interviews, reminders/escalations, in-place preservation) are marketing-page-level — directionally corroborated by the other three samples but not independently verified at feature level.
- **Non-US/regional practice** (e.g., data-protection regimes intersecting holds; non-litigation triggers like audits/investigations in civil-law jurisdictions) not researched; sample is US-litigation-shaped. All four sampled products document investigation/audit triggers alongside litigation, so trigger breadth is documented, but regional variation is not.
- **Numeric defaults** (7-day renotification, 14-day escalation start, 3-month reminders, 30-day delay hold, 24-hour effectiveness, attachment limits, licensing tiers) are product-specific implementation values — recorded here and excluded from the final document.

## Historical Check (§24 discipline)

Pre-software practice: litigation hold memoranda (paper or email) distributed to identified employees, receipt/acknowledgment tracked manually (signed memos, tracking spreadsheets), follow-up reminders sent ad hoc, holds lifted by closing memoranda, records retained for defensibility. Does this satisfy L0?

1. Hold of record — the memo file + tracking sheet kept by counsel ✓
2. Custodian population — the named distribution list, added to/released over time ✓
3. Duty communication + compliance tracking — the memo itself + recorded acknowledgments ✓
4. Recorded release — the closing memo, records retained ✓

None of the automation (reminders, escalations, questionnaires, portals, technical preservation) is required. **Historical check passed** — the modern custodian-portal model is an implementation of a duty-management practice that predates the software.

## Final Synthesis

A legal hold management application is the legal team's system of record for preservation duties owed by identified custodians for a specific matter. Its defining core is small: the hold of record, the managed custodian population, duty communication with per-custodian compliance tracking, and recorded release. Everything else — reminders, escalations, questionnaires, directories, templates, audit reports, technical preservation-in-place, dashboards, AI — makes the duty process scalable and defensible but is not what makes the software a legal hold manager. The Type sits at the start of the eDiscovery pipeline (most products bundle forward into collection/review), sits opposite records retention (which it suspends), and is triggered by litigation, investigation, audit, or regulatory events. The two-tier Microsoft split independently corroborates the process/technical separability that the L0/L1 division encodes.
