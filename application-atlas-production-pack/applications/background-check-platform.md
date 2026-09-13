# Background Check Platform

## Overview

A **Background Check Platform** is an application through which an organization orders, tracks, and receives background investigations on identified individuals — criminal-record searches, identity anchoring, employment and education verification, driving records, registry and watchlist checks, and related screens — and then makes an eligibility decision on the returned findings.

Its defining structure is small:

```text
Requesting organization
└── Screening order on an identified individual
    └── Subject's consent/authorization gate
        └── Composed screens executed against records and data sources
            └── Findings report (filtered per jurisdiction)
                └── Eligibility decision made by the organization, supported by
                    adverse-action and dispute machinery
```

Two properties distinguish the Type from anything that merely "looks up records":

1. **The subject's authorization gates execution.** The individual is informed, discloses, and consents before any investigation runs; the platform operates as a regulated reporting service, not a data broker.
2. **The platform reports; the organization decides.** Findings return as a report; the decision to proceed, decline, or take further action remains with the requesting organization, with structured machinery (notices, dispute handling, retained evidence) governing what happens when findings influence a negative decision.

In the dominant market this is employment screening: recruiters order checks on candidates inside a hiring workflow. The same mechanics are re-aimed at other verticals (tenant screening, platform-user screening, consumer self-checks), which appear as related Application Types.

## Users & Context

**Primary users (customer side):**

- **Recruiter / talent-acquisition specialist** — initiates check orders for candidates at the right point in the hiring flow, tracks their progress, and chases incomplete candidate steps.
- **Hiring manager** — consumes the outcome (cleared vs needs review) to inform the hiring decision.
- **Compliance / program administrator** — configures screening packages, jurisdictional rules, disclosure and authorization content, user roles, and adverse-action settings; owns the audit posture of the program.
- **Adjudicator / HR operations** (common in higher-volume organizations) — reviews reports with findings, applies the organization's decision criteria, and executes the adverse-action workflow when needed.

**Secondary users (subject side):**

- **Candidate** — receives the invitation, reads disclosures, signs the authorization, enters personal information and verification details, uploads documents, tracks status, and (commonly) accesses their own report or a copy.

**Typical context:** the platform operates inside a hiring workflow — usually integrated with an applicant tracking or HR system — processing a steady stream of orders whose progress depends on third parties (courts, verifiers, bureaus), which makes status visibility and exception handling central to daily use. High-volume operations (staffing, retail, gig platforms, healthcare systems) are a core market; single-hire small businesses are served by self-serve forms of the same structure.

## Core Model

### The Defining Core

**Requesting organization and identified subject.** Every investigation is initiated by an organization about one specific, identified person. The subject is the central record; orders, screens, consent artifacts, and results all attach to that person. The organization side carries its own legal identity (established during account onboarding, because a permissible purpose for ordering reports is a prerequisite of the service itself).

**Screening order.** The order is the unit of work. It binds the subject to a requested set of screens (a package) and moves through a tracked lifecycle from initiation to completion. Orders can be created through the platform's own interface or triggered programmatically by an integrated hiring system.

**Consent and disclosure artifacts.** Before screens run, the subject is presented with the legally required disclosures and signs an authorization; a summary of consumer rights is acknowledged. These artifacts are captured as discrete, auditable records (commonly with electronic signature), not folded into general terms of service. Who presents them varies — the platform's hosted candidate flow, or the customer's own flow — but the artifacts themselves are structural.

**Composed screens.** A screen is a single investigation type: a criminal search at a specific jurisdiction level, an employment or education verification, a registry or watchlist check, a driving-record check, and so on. The order composes screens into a package; the package also determines which personal information the subject must supply (for example, identity documents for identity validation, or past employers for employment verification).

**Records and data sources.** Screens execute against external sources of record: courts and judicial databases, government registries and watchlists, licensing authorities, motor-vehicle departments, credit bureaus, employers and schools, and aggregated record databases. The platform orchestrates these lookups and reconciles what comes back — turnaround is often governed by the slowest human-dependent source, not by the software.

**Findings report.** The report is the deliverable: per-screen results assembled into one document, filtered so that only records reportable under the subject's applicable jurisdictional rules are shown. Conceptually, a completed report resolves to a simple customer-facing outcome — nothing requiring attention, or items present that require review — while the underlying detail remains inspectable.

**Customer-side decision and its machinery.** The organization reviews the report and decides whether the subject is eligible. When findings may drive a negative decision, a structured adverse-action process applies: a preliminary notice with the report and the subject's rights, a window for the subject to respond or dispute, and a final notice if the decision stands. Disputed findings can trigger reinvestigation and a corrected report. All steps are recorded as compliance evidence.

### Standard Capabilities

Mature products commonly add:

- **Identity anchoring** — an initial identity trace or document validation that confirms the subject's identifying data is coherent and derives the name and address history used to scope subsequent searches (which courts and registries to search, which past employers to contact).
- **Candidate flow** — an invitation link, a guided form for personal information and consent, document upload, status notifications, and access to the report or a copy.
- **Package libraries** — pre-built packages by role, industry, or jurisdiction, plus custom composition for customers with program-specific needs.
- **Jurisdictional rule handling** — the platform applies location-dependent disclosure content, reporting filters, and process variations automatically from the subject's work location.
- **Order status tracking and estimates** — per-order and per-screen progress visible to both customer and candidate, with expected turnaround where available.
- **Adjudication support** — review queues, decision criteria, and recorded outcomes for reports that need human evaluation.
- **ATS/HRIS integration and API** — order creation, status callbacks, and report retrieval embedded in the hiring system of record; this is a first-class capability, not an afterthought.
- **Program dashboards and analytics** — order volumes, turnaround distributions, outstanding actions, and program-level compliance views.
- **Multi-entity operation** — hierarchies of locations, departments, or client organizations sharing one program (staffing firms and franchises in particular).
- **Post-hire monitoring** — recurring re-checks of criminal records, driving records, licenses, or drug-testing status for people already in the workforce.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Specific products realize each concept differently:

```text
Consent/authorization gate →   platform-hosted candidate flow with e-signature,
                               customer-hosted flow uploading signed artifacts,
                               in-person/legacy capture

Identity anchoring →           national identity-number trace, government ID document
                               validation, identity data evaluation against bureau files

Findings outcome →             two-valued result labels (clear / needs review), graded
                               scores, per-screen statuses assembled into a summary

Eligibility decision →         manual review with recorded outcome, criteria-based
                               adjudication queues, decision matrices configured per
                               customer policy
```

## How It Works

### The order lifecycle

```text
Initiate order
→ candidate invited (or PII entered directly by the customer)
→ candidate reads disclosures, signs authorization, supplies personal information
→ identity anchoring: identity confirmed, name/address history derived
→ screens run against courts / registries / bureaus / verifiers,
  scope expanded per address history
→ compliance filters applied; report finalized
→ customer reviews: nothing requiring attention, or items to evaluate
→ decision recorded: proceed, or structured adverse-action process
→ (if disputed) reinvestigation → corrected report
```

**Initiation.** A recruiter or integrated system creates the order. In the common candidate-invited flow, the platform emails the subject a link; alternatively, the customer enters the subject's information directly and certifies that consent was already collected offline. The package choice at initiation determines everything downstream — which screens run and what the candidate must provide.

**Candidate participation.** The subject completes the steps only they can do: signing disclosures and authorization, entering personal identifiers and history (addresses, past employers, schools, license numbers), and uploading documents. Order progress typically stalls here, which is why candidate-facing status visibility and reminders are standard.

**Processing.** The platform first anchors identity, then fans out the screens. Some screens return in seconds from databases; others require human court research or verifier responses. As individual screens complete, the report assembles. Address history discovered during identity anchoring can expand the scope of criminal searches to additional jurisdictions.

**Completion and decision.** The finalized report reaches the customer through the dashboard, the integrated hiring system, or notifications. A report with findings moves into human review: the organization evaluates the findings against its own criteria, records its decision, and — if declining based on the report — runs the adverse-action process, giving the subject the legally required opportunity to see the report, correct errors, and respond before a final decision.

**Exception handling.** Everyday exceptions are structural, not rare: candidates who never complete consent, identity data that doesn't match bureau records (triggering outreach to the candidate), courts or verifiers that are slow or unreachable, and disputed findings requiring reinvestigation. Platforms surface these as per-screen states rather than failing the whole order.

### Post-hire monitoring (common extension)

For subjects already employed or engaged, the platform re-runs selected screens on a recurring basis or monitors relevant record sources continuously, raising an alert and a new report when something reportable appears.

## Interfaces

### Customer dashboard (order list)

The operational center.

- typical information: orders with subject, package, age, per-order status, result outcome, actionable items
- primary actions: create order, invite candidate, open a report, take adjudication action, start adverse action, escalate a stalled order

### Report detail

The findings surface.

- typical information: subject summary, per-screen sections with searched jurisdictions and findings, documents, the reportable outcome label, timestamps and turnaround
- primary actions: review findings, mark decision outcome, initiate adverse action, order an upgrade or additional screen, download or share the report

### Candidate flow / portal

The subject's surface, usually mobile-friendly.

- typical information: pending steps, disclosure and authorization documents, forms for personal data and history, upload slots, current status
- primary actions: consent and sign, enter or correct information, upload documents, view status, access the report or a copy

### Configuration and administration

- typical information: screening packages, disclosure/authorization templates, jurisdictional rules and filters, user roles, entity hierarchy
- primary actions: compose or edit packages, manage users and permissions, configure decision criteria and adverse-action settings, connect integrations

### API and webhooks

For integrated customers, order creation, candidate data submission, status-change notifications, and report retrieval are available programmatically; this is how the platform typically sits inside an ATS-mediated hiring flow.

### Reporting / analytics

Program-level views of volumes, turnaround times, outstanding actions, and outcomes — used by program administrators to manage throughput and compliance posture.

## Important Rules / Behaviors

### Consent precedes execution

No screens run before the subject's authorization is captured. The disclosure is treated as a formal artifact presented on its own terms — not bundled into general terms of service — and the signed authorization is retained as evidence. Products differ in *who* captures it (platform-hosted flow vs customer-hosted flow), but the gate itself is not bypassable in the platform's primary markets; customers using their own flow must certify that consent was properly obtained.

### The platform reports; the organization decides

The platform does not decide whether a subject "passes". Reports with findings require the customer's evaluation; automated result labels only separate "nothing requiring attention" from "human review needed". This separation is a structural compliance property of the Type, not a product limitation.

### Reporting is jurisdiction-filtered

What appears on a report is not "everything on record" but everything *reportable* under the rules that apply to the subject's location and the purpose of the check. The same person can therefore produce different report content depending on work location and customer configuration.

### The package determines required information

Only the information needed for the ordered screens is required of the candidate — identity documents for identity screens, license details for driving-record screens, prior employers for employment verification. Ordering a narrower package reduces the candidate's burden; upgrading mid-order is a supported operation in mature products.

### Findings trigger a protected process, not an instant decision

When a customer intends a negative decision based on findings, the adverse-action sequence (preliminary notice, response window, final notice) must run, and disputed findings may force reinvestigation and report correction. This gives the candidate a real opportunity to contest inaccurate records before the decision takes effect.

### Turnaround is source-bound

Order completion time is dominated by external sources (courts, verifiers, bureaus), so platforms manage expectations with per-order estimates and per-screen statuses rather than fixed guarantees; stalled screens are escalated rather than silently pending.

## Variants

- **Product form:** API-first developer platforms (embedded programmatically in high-volume hiring flows); full-service enterprise providers (service desk, global programs, managed compliance); self-serve SMB products (pre-bundled packages, immediate signup, no integration required). All implement the same core lifecycle.
- **Volume verticals:** staffing and high-volume hourly hiring (multi-entity operations, fast packages); healthcare (license and sanctions checks); transportation and driving roles (regulated driving-record and drug-testing programs); gig and marketplace platforms (screening at activation).
- **Post-hire orientation:** continuous criminal/driving/license monitoring and periodic rescreening as a program on top of pre-hire screening.
- **Adjacent orchestrations:** employment drug testing (labs and medical review), work-eligibility forms (I-9 / E-Verify in US products), fingerprinting coordination, executive due-diligence investigations.
- **Geographic regimes:** country-specific criminal-record schemes and disclosure regimes; global programs handle per-country variations of the same consent → search → report → decision spine.
- **Vertical re-aims of the same engine:** tenant screening (landlord-initiated), platform-user trust screening, consumer-initiated self-checks — related Application Types rather than employment variants (see below).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Applicant Tracking System / ATS | container vs step | The ATS owns the requisition→candidate→offer hiring pipeline. The background check is one regulated step inside that flow, with its own order/consent/report/adverse-action objects; the two are typically integrated. An ATS without consent and reporting machinery is still an ATS. |
| Identity Verification | component vs whole | Identity verification asserts that a person is who they claim (documents, biometrics, data checks). A background check platform *includes* an identity-anchoring step, but its deliverable is a findings report about the person's history used for an eligibility decision. |
| Employment Verification Platform | one screen vs composition | Verifying employment history (or continuous employment/income data) is a single screen type. The background check platform composes many screen types into one governed order. |
| Tenant Screening Platform | vertical re-aim | The same engine and lifecycle initiated by a landlord rather than an employer, with different data emphasis and regulatory framing; a separate Application Type in this directory. |
| Candidate Assessment Platform | records vs competence | Assessment measures skills and fit; a background check investigates records and history. They share candidate-facing forms and hiring-flow integration but not core objects. |
| HR Compliance Management | policy vs investigation | HR compliance manages policies, training, and cases across the workforce; it does not order per-individual record investigations from reporting sources. |

Outside the directory, **people-search / data-broker services** are the closest damaging confusion: they return records without subject authorization, organizational purpose, or adverse-action machinery — precisely the three properties that make this a Background Check Platform.

## Representative Products

- Checkr — API-first platform; developer documentation explicitly models candidates, packages, invitations, reports, adverse actions, and continuous checks
- Sterling (now part of First Advantage) — full-service global enterprise screening; service catalog organized by identity-first / pre-hire / post-hire lifecycle
- HireRight — global enterprise screening with high-volume workflows and extensive ATS/HCM integration catalog
- GoodHire — self-serve SMB-oriented product; pre-bundled packages with candidate-visible results

The defining structure was checked across these products' different customer tiers and product forms (developer platform, enterprise full-service, self-serve) so that the core model does not overfit to any one packaging or one region's regulatory detail.

## Sources

Research date: **2026-09-06**

- Checkr — product homepage: https://checkr.com ; API documentation (screening process, resources, packages, invitations, adverse actions): https://docs.checkr.com
- Sterling / First Advantage — product homepage and service catalog: https://www.sterlingcheck.com
- HireRight — product homepage and services: https://www.hireright.com
- GoodHire — product homepage and screening services: https://www.goodhire.com

> Sourcing limitation: research relied on vendor homepages and, for one product, full API documentation. Dedicated help-center articles, candidate-status portals, and two vendors' developer documentation were not fetched in this pass. Accordingly, this document describes lifecycle and rule *shapes* observed across the sample and avoids precise operational specifics (numeric deadlines, exact status vocabularies, default settings), which vary by product and jurisdiction. Detailed per-product observations are recorded in the paired Research Notes.
