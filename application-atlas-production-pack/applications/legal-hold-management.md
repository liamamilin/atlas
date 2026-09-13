# Legal Hold Management

## Overview

A **Legal Hold Management** application is the legal team's system of record for preservation duties. When litigation, a government investigation, an audit, or a comparable legal event is reasonably anticipated, an organization is obligated to preserve information that may be relevant — and the people who hold that information must be told so, in a way that can later be proven. This application exists to run that process: it records that a preservation duty exists for a specific matter, identifies the people who hold the relevant information (called *custodians*), sends each of them a preservation notice, records their acknowledgment, keeps the duty alive through reminders and updated notices, and formally releases it when the matter ends — retaining the entire trail so the organization can demonstrate the duty was handled defensibly.

It solves a specific operational problem: a preservation duty is spread across many people who will move on to other jobs, forget, or leave the organization, while the consequences of losing information (evidence destroyed after the duty arose — spoliation — and the sanctions that follow) land years later. Memos and spreadsheets can start the process; only a managed system can show, custodian by custodian and notice by notice, that the duty was communicated, acknowledged, maintained, and released.

The boundary of the Type: it manages the **duty**, not the data. It freezes nothing by itself in most realizations — the actual preservation of data happens in connected systems (mail platforms, archives, collaboration suites), either through integrations this product drives or through separate technical hold mechanisms. It is also not a records-retention system: retention schedules are standing rules that apply all the time, while a legal hold is a matter-scoped duty that temporarily suspends them and ends with a recorded release.

## Users & Context

**Primary users:**

- **Legal hold administrator** (in-house counsel, litigation counsel, or legal operations staff) — the operator of the process: scopes the matter, selects custodians, drafts and issues notices, tracks compliance, adds custodians as scope evolves, modifies notices, and releases holds. In most products this role is access-restricted to legal team members.
- **Custodians** — employees (or other identified information holders) who receive the preservation notice. They are unprivileged, task-scoped participants: they read the instructions, answer a questionnaire if one is attached, and acknowledge. They normally never log into the platform itself; they act through email links or an acknowledgment page that does not require an account.

**Secondary users:**

- **Managers and supervisors** — receive escalation notices when their reports do not acknowledge; they are an enforcement path, not operators.
- **eDiscovery / IT staff** — consume the hold's output: the questionnaire responses and custodian lists define who and what to preserve or collect; in some products they also operate the technical preservation integrations.
- **Legal leadership** — oversees the hold program through dashboards, status reports, and exports.

The work context is time-pressured and high-stakes: a hold typically must go out quickly after a duty arises, run for months or years, and survive hostile scrutiny long after. The users' shared concern is defensibility — every action in the system is timestamped and attributable because the record may one day be an exhibit.

## Core Model

### The Defining Core

```text
Matter / case / investigation (the trigger)
└── Legal hold of record (issued → active → released)
    └── Custodian population (added and released over time)
        ├── Duty notice (addressed to each custodian individually)
        │   └── Compliance state per custodian (delivered → acknowledged)
        └── Release (a recorded act; the history remains reportable)
```

Four structures, held together:

- **The hold of record** — a persistent, identified record that a preservation duty exists: what matter it belongs to, what it covers, when it was issued. It is the unit everything else attaches to, and it carries a lifecycle (drafted, issued, active, released). Without it there are only scattered memos — no managed process.
- **The custodian population** — the identified people placed under the duty. Custodians are managed as a population: added as scope widens, released individually as it narrows, and tracked per person. Without custodians there is only a technical content freeze — a capability of storage and archiving systems, not this application.
- **Duty communication with compliance tracking** — the system communicates the duty to custodians (a notice addressed to each individual) and records each custodian's compliance state — delivered, acknowledged — *against the hold*. The tracking is what turns memo-sending into management: the application can answer "who has not yet acknowledged" at any moment.
- **Recorded release** — the hold, and each custodian's duty, ends through a distinct recorded release act, not by deleting the record. Release notices go out, statuses change, and the hold's history remains reportable afterward. Without release semantics the object is not a hold but a standing retention policy.

The trigger container varies by product — a matter, a case, or a project — but in all realizations the hold is anchored to something that represents the legal event, and that anchor organizes the holds, custodians, and later collected data.

### Standard Capabilities

Mature products commonly add the following. They make the process scalable and defensible; they are not what makes the software a legal hold manager.

- **Reminder and escalation machinery** — automated reminders to custodians who have not acknowledged; escalation notices to their managers when non-acknowledgment persists; and periodic reminders to *all* custodians on long-running holds, since duties can outlast any individual's attention (some products allow requiring a fresh acknowledgment with each periodic reminder).
- **Notice authoring support** — reusable notice templates, merge fields that personalize each copy, a designated reply-to address that routes custodian questions, cc recipients (such as outside counsel) who receive copies without becoming custodians, and test sends before the real one.
- **Questionnaires** — an optional questionnaire attached to the notice, used to scope the duty: what devices, systems, and mailboxes the custodian holds, and who else should be on the hold. Responses are logged with the hold and feed later collection.
- **Custodian directories** — employee data (names, emails, managers, departments, employment dates) drawn from the organization and used to select custodians; custodians are typically retained at the organization level so they can be reused across holds, and a custodian's record can show every hold they belong to.
- **Status model** — a hold-level status (active, released; paused in some products) and per-custodian compliance states, with counts surfaced on dashboards and in reports.
- **Defensibility reporting** — hold reports and custodian reports listing who was noticed, when, which version of the notice they received, their acknowledgment date, reminders sent, and release dates; event histories of administrative actions; notice versioning when a hold is edited.
- **Role-based access** — administrator and viewer roles, matter- or case-scoped membership, and restricted handling for sensitive matters; custodian-facing surfaces expose nothing about other custodians.
- **Technical preservation integration** — connections that let the hold trigger or track preservation-in-place in the systems where the data actually lives (mailboxes, archives, collaboration platforms). The depth varies widely: in some products it is a first-class module, in others a tracking record for holds made elsewhere, and in the most basic realizations it is absent entirely.
- **Handoff to collection** — a link between held custodians and the documents later collected from them, so the duty record connects to the evidence record.

### One Structure, Many Implementations

The core model is written in conceptual terms. Realizations differ across products:

```text
Concept:    Hold of record
Realized as: a hold notice card, a hold policy inside an eDiscovery case,
             a notice/preservation record inside a matter

Concept:    Custodian
Realized as: a person of interest added to a case, an email recipient on a hold,
             a directory record selected into a matter

Concept:    Duty notice
Realized as: an email, a chat message, a link to an acknowledgment portal

Concept:    Compliance state
Realized as: a confirmation-button click, a portal acknowledgment with a
             confirmation email, delivered/read/acknowledged tracking

Concept:    Release
Realized as: a release notice to custodians, a "released" status on the hold,
             per-custodian release as scope narrows
```

A reader who has only seen one implementation — say, a compliance suite where the hold is a policy object — should still be able to recognize a standalone hold product or a litigation platform's hold module as the same Type.

## How It Works

### Issue and run a hold (the administrator's loop)

```text
Duty arises (litigation, investigation, audit, subpoena)
→ open a hold in a matter/case (or create the matter)
→ select custodians (directories, prior holds, HR data)
→ draft the notice (template + matter details + attachments)
→ optionally attach a questionnaire to scope the duty
→ issue — each custodian receives their own copy of the notice
→ track: acknowledged vs outstanding, per custodian
→ remind non-acknowledgers automatically; escalate to managers if needed
→ re-remind everyone periodically on long-running holds
→ scope changes: add custodians; update the notice
   (a materially changed notice may require everyone to re-acknowledge)
→ matter resolves: release the hold — all at once, or custodian by custodian
→ release notices go out; the hold becomes "released"; reports remain available
```

Issuing is the point of no return: notices cannot be unsent, which is why products put a summary and a test-send in front of the administrator first.

### The custodian's side

```text
Receive the notice email → open it → read the preservation instructions
→ (if attached) complete the questionnaire
→ acknowledge — a button click, or an acknowledgment page
→ receive a confirmation (on screen, and by email with the timestamp)
→ later: periodic reminders arrive; some require re-acknowledgment
→ eventually: the release notice — the duty ends
   (unless other holds still cover them — release notices often say so)
```

The custodian experience is deliberately friction-light: acknowledge in one click, or through a page that requires no account on the platform. At the same time it is deliberately formal: the acknowledgment and its timestamp are the record that the person knew of the duty.

### Editing a live hold

Scope evolves, so holds are edited after issuance. The rules that products document are conservative: custodians can always be added; whether the custodian list can shrink differs by product (release substitutes where removal is forbidden, and some products distinguish deleting a custodian as an error correction from releasing them as a scope decision). Editing the notice text is treated as material: the administrator may be required to reset every acknowledgment and re-notice the population, and every version of the notice that each custodian received is captured in the reports.

### Core vs Common vs Optional

**Defining core** — without these, not a legal hold manager:

- hold of record anchored to a matter
- custodian population under the duty
- duty communication with per-custodian compliance tracking
- recorded release with retained history

**Common mature structure** — present in most modern products:

- reminders, manager escalation, periodic re-reminders
- notice templates, merge fields, reply-to, cc recipients, test sends
- questionnaires for scoping
- custodian directories and reuse across holds
- status model with counts
- defensibility reports, notice versioning, event history
- role-based access
- technical preservation integrations and collection handoff

**Variant / optional** — depends on product and deployment:

- delivery and acknowledgment through chat platforms
- silent custodians (tracked but unnotified)
- tracking records for preservations made in external systems
- employee change monitoring (departures automatically raise hold tasks)
- AI assistance (custodian identification, task automation)
- program-level dashboards and analytics
- free or entry tiers for small organizations

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Holds dashboard

The administrator's worklist. Typical information: every hold with its status, matter, custodian counts, and acknowledgment progress. Primary actions: open a hold, start a new hold, filter, export reports.

### Hold creation wizard

A guided multi-step sequence (container → custodians → notice text → questionnaire → reminder/escalation settings → summary and send). Each step validates before the next; the final step shows a complete summary of settings and offers test sends, because issuance is irreversible.

### Hold detail

The per-hold management surface. Typical information: the notice text and its version, the custodian list with per-person status (issued, acknowledged, released, errored), reminders and escalations sent. Primary actions: add custodians, edit and re-issue the notice, release custodians or the whole hold, download reports and questionnaire results.

### Custodian record / cross-hold view

The per-person surface: every hold the custodian belongs to, their acknowledgment standing on each, and directory attributes (manager, department, employment dates) used for escalation and reporting.

### Acknowledgment portal (custodian-facing)

What the custodian lands on from the notice: the instructions, attachments, the questionnaire if present, and the acknowledgment control. Accountless by design; afterwards it shows that the hold was already acknowledged.

### Questionnaire builder

An administrator surface for composing scope questions (choice, text, date, and similar types), arranging them into pages, marking them required or optional, adding conditional rules, and previewing the result.

### Reports and exports

The defensibility surface: hold-level reports (status, dates, counts) and custodian-level reports (per-custodian-per-hold rows with notice versions, acknowledgment dates, reminders, releases), typically exportable for counsel or auditors.

### Settings

Notice templates, sender addresses and reply-to routing, role and permission assignment, and directory connections.

## Important Rules / Behaviors

- **The duty is personal and must be proven.** A hold notice is addressed to each custodian individually, and the per-custodian acknowledgment is the record that the person knew. Custodians see only their own notice — not who else is on the hold.
- **Issuance is irreversible; edits are forward-only.** Once sent, notices cannot be unsent. Material edits to an issued notice can reset acknowledgments and require the population to re-acknowledge, and every version of the notice is retained in reporting.
- **Release is not deletion.** A released hold changes status and stays reportable; in the products that document it, a released hold cannot simply be switched back to active — if the duty revives, a new hold is issued. Custodian-level removal usually distinguishes a correction (delete, for mistakes) from a scope decision (release).
- **The hold tool manages the duty; connected systems freeze the data.** Preservation-in-place is performed by mail platforms, archives, or collaboration systems — either driven through this product's integrations or by separate technical hold mechanisms. The hold record and the technical freeze are separable, and products differ in which one they natively provide.
- **Holds block closure.** A matter (or case) with active holds typically cannot be closed or deactivated; everything under it must be released first. Removing a technical hold after release may itself be delayed by the connected system, as a safeguard against premature deletion.
- **Escalation presupposes acknowledgment.** Reminder and escalation machinery targets custodians who have *not yet* acknowledged; periodic reminders to everyone on long holds are a separate mechanism, and some products require a fresh acknowledgment with each one.
- **Defensibility shapes everything.** Every notice version, acknowledgment, reminder, escalation, and release is timestamped and attributable, because the record of the process may one day have to stand up in court.

## Variants

- **Standalone legal hold product** — a pure-play tool focused on the hold workflow alone; often the entry point for smaller legal teams, sometimes with free tiers.
- **Module of an eDiscovery platform** — the hold as stage one of a pipeline that continues into collection, processing, review, and production; the hold's custodians connect directly to later-collected documents. This is the market's dominant packaging.
- **Module of a compliance or productivity suite** — the technical content hold is native to the suite, with the custodian duty workflow (notifications, acknowledgment tracking) as a higher tier or separate capability.
- **Trigger variants** — litigation holds, investigation holds, audit holds, and regulatory/subpoena-driven holds run on the same machinery; products differ only in which triggers their templates and marketing emphasize.
- **Delivery variants** — email-first is standard; some products deliver and collect acknowledgments through chat platforms.
- **Scale variants** — from single-matter small-team deployments to organization-level programs managing thousands of custodians across hundreds of simultaneous holds, with employee directories and program dashboards.

A variant remains a variant as long as the defining core — hold of record, custodian population, tracked duty communication, recorded release — is intact.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| eDiscovery Platform | same pipeline, later stages | eDiscovery centers on collection, processing, analysis, review, and production of documents; legal hold management centers on the preservation duty that precedes collection. The market bundles both constantly, so the seam is the center of gravity, not feature lists |
| Enterprise Records Management | opposite pole of disposition | records management applies standing retention schedules to record classes all the time; a legal hold is a matter-scoped duty that suspends normal disposition until released. Vendor guidance for a major suite states the seam directly: long-term retention belongs to retention policies, investigation-related preservation to eDiscovery holds |
| Legal Matter Management | host and anchor | matter management is the system of record for the matter itself (status, spend, documents, deadlines); here the matter is an anchor the holds hang from. ELM suites may embed hold modules — that is packaging, not the same Type |
| Corporate Investigation Management | trigger source | investigation platforms run the case lifecycle of an internal investigation; when evidence preservation is needed, a hold is issued in a system like this one. The investigation record and the preservation duty are different objects |
| Evidence Management System | custody vs duty | evidence management tracks items the organization physically or digitally holds (chain of custody); legal hold management tracks the duty of people to preserve their own information |
| Archiving & compliance suites with "litigation hold" | capability vs Type | an archive's hold freezes stored content but has no custodian duty workflow — no notices, acknowledgments, or releases. A freeze without the duty loop is a capability, not this Type |
| Data Retention / Disposition tools | standing policy | retention tools automate scheduled deletion; they have no trigger event, no custodians, and no release act |
| Compliance Policy Management | program-level | policy management administers standing obligations and attestations; a legal hold is a specific duty arising from a specific event |

The sharpest boundary is with eDiscovery. Both share vendors, surfaces, and custodians, and most products ship both. The working test: strip the collection/review/production machinery and the product is still fully itself — that is this Type. Strip the duty workflow and keep only search and review of collected data — that is eDiscovery.

## Representative Products

- **Exterro** — legal-hold-first module within an eDiscovery and legal-governance suite; documented the scoping-to-release framing, custodian interviews, reminders/escalations, and in-place preservation
- **Logikcull (Reveal)** — self-serve eDiscovery platform whose hold module documented the deepest operational detail: creation wizard, editing and re-acknowledgment semantics, release rules, and reporting
- **Microsoft Purview eDiscovery** — platform-native compliance module; documented both the technical content hold and the custodian notification workflow, and the seam between holds and retention policies
- **Everlaw** — litigation eDiscovery platform with an organization-level Legal Holds tool; documented matters, custodian directories, the acknowledgment portal, and default reminder/escalation cadences

The market sample was checked against the pre-software practice (hold memoranda, signed receipts, tracking spreadsheets, closing memos), which satisfies the defining core without any of the automation — confirming that reminders, questionnaires, portals, and technical preservation are the mature implementation, not the definition.

## Sources

Research date: **2026-09-07**

- Exterro — "Legal Hold & Preservation" product page (https://www.exterro.com/e-discovery-software/legal-hold); corporate site and product taxonomy (https://www.exterro.com/)
- Logikcull (Reveal) — documentation portal: "Creating Legal Holds" and the Legal Hold and Preservation section index (https://docs.revealdata.com/logikcull/docs/creating-legal-holds.md, https://docs.revealdata.com/logikcull)
- Microsoft Learn — Purview eDiscovery documentation: "eDiscovery legacy solutions" overview, "Learn about eDiscovery", "Create holds in eDiscovery" (https://learn.microsoft.com/en-us/purview/ediscovery, https://learn.microsoft.com/en-us/purview/edisc, https://learn.microsoft.com/en-us/purview/edisc-hold-create)
- Everlaw — Knowledge Base: "Introduction to Legal Holds", "Legal Holds: Hold Notices" (https://support.everlaw.com/hc/en-us/articles/4408079521819-Introduction-to-Legal-Holds, https://support.everlaw.com/hc/en-us/articles/4408079526171-Legal-Holds-Hold-Notices)

> Sourcing limitations: the archiving-vendor pole (web/social archiving products with hold features) could not be observed — the sampled vendor page returned HTTP 403 — so archiving-side claims are carried only at the capability-vs-Type level; one litigation-support platform's hold module documentation was unreachable (404); one sampled vendor was evidenced at product-page level only (marketing tier), with its operational claims corroborated indirectly by the other three samples. Product-specific numeric defaults (reminder and escalation intervals, data limits, licensing tiers) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
