# Legal Intake & Client Onboarding

## Overview

A **Legal Intake & Client Onboarding** application is the law firm's system for turning an incoming legal inquiry into an accepted client with an executed engagement and an opened matter. It captures each prospective client and their matter inquiry as a managed record, runs the firm's pre-commitment screening — of which conflict screening against the firm's own records is the signature step — records an explicit accept-or-decline decision, and, on acceptance, formalizes the relationship (engagement agreement) and hands the new client and matter into the firm's client-matter system of record.

The defining structure is deliberately small:

```text
Prospective client (person/organization + matter inquiry) — explicitly not yet a client
  ↓ captured through defined intake surfaces
Screening gate — conflict screening, case evaluation, risk assessment (firm-defined)
  ↓ recorded outcome
Engagement decision — accept as client / decline (declined representation stays reportable)
  ↓ on acceptance
Onboarding closure — engagement agreement executed + client/matter opened in the firm's system of record
```

Everything else commonly associated with modern intake — web forms, automated texts, scheduling links, e-signature, marketing attribution, AI lead scoring — makes intake fast and measurable but is not what makes it intake. A paper intake form, a conflicts check, a partner's yes-or-no, and a typed engagement letter realize the same structure; mature products digitize each step.

The Type ends where representation begins: once a client is accepted and the matter is opened, ongoing work belongs to Law Practice Management and Legal Matter Management. Likewise, deep firmwide conflicts search machinery belongs to Legal Conflict Checking Platform; intake only requires that a screening step can be run and recorded.

## Users & Context

Primary users sit on the firm side, before any attorney-client relationship exists:

- **Intake specialists / new-business coordinators** — capture inquiries, run initial screening, schedule consultations, chase signatures and documents; in high-volume consumer-law firms this is a dedicated role with its own pipeline.
- **Evaluating attorneys** — assess merits, value, and fit during consultation; their accept/decline is the decision the system records.
- **Conflicts / risk staff (larger firms)** — review conflict hits, risk scores, and questionnaires; at the enterprise pole they act as gatekeepers who determine whether the firm can take the work on.
- **Firm management** — watch conversion rates, source ROI, and pipeline value.

The **prospective client** is an external actor: they complete intake forms, attend consultations, sign engagement agreements, and supply documents through client-facing surfaces.

Two very different contexts share the same structure. In **consumer-law firms** (personal injury, immigration, family law), intake is a high-volume funnel where speed of response determines who wins the client. In **large corporate firms**, "new business intake" is a risk-controlled acceptance process where questionnaires, conflict and risk review, and engagement-letter policies gate every new client and matter. Products may serve one pole or both.

## Core Model

### The defining core

Four properties. If any one is removed, the product is no longer recognizable as legal intake:

- **Prospective-client record** — an identified person or organization together with their matter inquiry, held as a managed record that is explicitly *not yet* a client. The record accumulates everything learned during intake: contact details, matter description, source, screening results, communications. Remove it, and there is nothing to screen or decide about — only a contact form.
- **Screening gate before commitment** — the firm evaluates the inquiry through defined checks before any obligation arises. Conflict screening against the firm's existing client and adverse-party records is the legal-profession-signature instance; case evaluation (merits, viability, value) and, at the enterprise pole, risk and compliance questionnaires sit in the same gate. Remove it, and the product is marketing lead capture.
- **Recorded engagement decision** — an explicit outcome that changes the record's class: accepted as a client, or declined. The decision is recorded, not conversational; a declined prospective client remains on record and reportable, which matters professionally because a firm must be able to show it did not accept a representation it screened and passed on. Remove it, and the product is a lead tracker.
- **Onboarding closure into representation** — on acceptance, the relationship is formalized: the engagement agreement (engagement letter, fee agreement, retainer) is executed, and the client and matter are created in the firm's client-matter system of record. Remove it, and the product is a screening register; the "client onboarding" half of the Type disappears.

These four hold jointly. A record plus a decision without screening is a CRM; screening plus a decision without onboarding is a compliance checkpoint, not intake.

### Standard capabilities of mature products

Modern products commonly carry most of these. They make intake practical; they do not define the Type.

- **Intake form building** — forms configured per practice area or matter type, embedded on the firm's website or sent by email/text, often brandable, with client-side save-and-resume.
- **Automated response and scheduling** — immediate acknowledgment of new inquiries by text or email, self-service consultation booking links, confirmations, reminders, and no-show handling.
- **Intake pipeline** — firm-defined stages representing milestones (inquiry received, screened, consulted, intent to hire, signed), with records advanced by staff or by automation triggered on events such as a booked consultation or a signed document.
- **E-signature on engagement documents** — generating and sending the engagement agreement for electronic signature, with reminders and deadline tracking.
- **File and document requests** — structured requests for the documents the matter will need, fulfilled by the prospective client.
- **Payment collection during intake** — collecting retainers or flat fees at signing (common in suite products, optional rather than universal).
- **Source and marketing attribution** — tracking where each inquiry came from (referral, campaign, website) and reporting conversion and return per source.
- **Conflict-check records** — each check recorded with its search terms, date, and outcome (cleared / flagged / denied), forming an auditable history.
- **Client-facing portal access** — a secure surface where the prospective or new client completes forms and shares documents.
- **Handoff to the firm's system of record** — either the same product (when intake is built into practice management) or a sync/integration that creates the client and matter in a separate practice-management system.
- **Roles and reporting** — separation between intake staff, attorneys, and risk reviewers; dashboards on funnel conversion and staff performance.

### One structure, many realizations

The core model is conceptual; implementations differ in how they realize each concept:

```text
Concept:   Prospective-client record
Implementations:  a matter flagged "prospective" (matter-primary);
                  a contact record carrying intake status (contact-primary);
                  an intake request record feeding a matter

Concept:   Screening gate
Implementations:  lightweight in-product conflict check against the firm's own records;
                  a dedicated conflicts platform invoked as a step;
                  risk/AML questionnaires with scoring and approval routing

Concept:   Engagement decision
Implementations:  client/matter outcome states (hired / declined);
                  approval workflows with named reviewers

Concept:   Engagement agreement
Implementations:  fee agreement, engagement letter, retainer agreement — e-signed

Concept:   Handoff to system of record
Implementations:  native (same system is the practice-management system);
                  integration/sync into a separate practice-management platform
```

Whether the prospect is modeled primarily as a matter or as a contact is a vendor modeling choice: the workflow — capture, screen, decide, formalize, open the matter — is the same either way.

## How It Works

The canonical intake loop runs as follows:

### 1. Capture the inquiry

```text
Prospect contacts the firm (website form, phone, referral, ad, walk-in)
→ the inquiry is recorded as a prospective-client record with its source
→ duplicates against existing contacts/matters are detected
→ an immediate automated acknowledgment may go out by text or email
```

Capture surfaces range from public web forms embedded on the firm's site to staff-entered records from a phone call — some products let staff fill the same intake form on the prospect's behalf while they are on the phone or in the office.

### 2. Screen and evaluate

```text
Run conflict screening against the firm's client and adverse-party records
→ record the check (terms, date, outcome)
→ evaluate the case: merits, practice-area fit, expected value
→ at the enterprise pole: firm-configured questionnaires, risk scoring,
  third-party data on the prospective client, reviewer approval routing
```

Screening precedes commitment. Work on the matter begins only after the gate clears; a flagged conflict or failed risk assessment stops or redirects the intake.

### 3. Decide

```text
Attorney or acceptance committee reviews the screened inquiry
→ recorded outcome: accept as client, or decline
→ declined: the non-engagement is recorded and reportable
→ undecided: the record stays in the funnel with follow-up (reminders,
  rescheduling sequences, nurture campaigns)
```

### 4. Onboard the accepted client

```text
Engagement agreement is generated from firm templates
→ sent for electronic signature (with reminders until signed)
→ optionally: retainer/fee payment collected
→ onboarding items executed: file/document requests, welcome communications,
  new-client tasks
```

### 5. Open the matter

```text
Client and matter are created in the firm's client-matter system of record
→ native (intake is part of the practice-management product)
   or synced/integrated into a separate practice-management platform
→ intake state reconciles with the practice-management state:
   the accepted matter exists exactly once
```

### 6. Keep the funnel visible

Throughout, the intake pipeline shows every prospective record by stage; management reporting aggregates conversion by stage, by source, and by staff. Some products attach monetary estimates and historical conversion rates to stages, turning the intake funnel into a revenue forecast.

### Tiering

**Defining core** — prospective-client record; screening gate with recorded conflict check; recorded accept/decline decision; onboarding closure (engagement agreement + matter opening).

**Standard capabilities** — form building and embedding; automated response, reminders, and consultation scheduling; intake pipeline; e-signature; file requests; source attribution and conversion reporting; client portal; system-of-record handoff; roles.

**Optional / variant** — payment collection during intake; marketing automation depth (drip campaigns, ROI analytics); AI lead scoring, AI chat and voice intake; AML/KYC compliance machinery; ongoing monitoring of accepted clients' risk posture.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Intake pipeline / board

The intake team's primary working surface.

- lists prospective-client records grouped by stage, with aging and owner
- typical information: prospect name, matter inquiry summary, source, stage, next action, value where tracked
- primary actions: advance stage, assign, open record, trigger follow-up

### Intake record page

The prospective client's file.

- inquiry details, contact information, source, conflict-check results, documents, communications, task list, event timeline
- primary actions: run a conflict check, schedule a consultation, send a form or document request, generate and send the engagement agreement, record the decision

### Form builder and public form pages

The capture surface.

- drag-to-configure forms with conditional questions, practice-area variants, branding; embed codes for the firm website
- primary actions: create/clone form variants, embed, send by email/text, review pending and submitted responses

### Conflict-check console

- search terms (names, emails, phone numbers) matched against firm records; results reviewed and classified (for example, cleared, flagged, or denied)
- history of past checks with terms, dates, and outcomes
- primary actions: run check, review hits, record clearance decision

### Risk / questionnaire review (enterprise pole)

- firm-configured questionnaires, risk scores, and approval routes; external data on the prospective client alongside internal answers
- primary actions: assign reviewers, request missing information from the client through secured external forms, approve or reject with recorded reasons

### E-signature surface

- the engagement agreement rendered for signature by the prospective client, with staff-side status tracking and reminders

### Reporting / dashboards

- funnel conversion by stage and source, response performance, staff productivity, revenue estimates where tracked

### Client-facing surfaces

- public intake forms, self-scheduling links, document upload, and a portal where the prospective/new client can complete and resume intake steps securely

## Important Rules / Behaviors

- **The prospect is not the client until the decision.** Records live in an explicitly "not yet client" state; the accept/decline is a recorded transition, and the record's class changes with it (prospective → client, or prospective → declined). This is the Type's central state rule.
- **Screening precedes commitment.** Engagement follows screening; a failed or unresolved screening gate (conflict hit, risk rejection) blocks progression. The gate order is structural, not a suggested best practice.
- **Declined representation is retained, not erased.** A declined inquiry stays on record and reportable — a firm must be able to demonstrate what it screened and declined.
- **Client submissions are typically frozen at submission.** Where products document this behavior, a form submitted by the prospective client is locked against their further edits; if information is missing, staff corrections are recorded as a new version alongside the original rather than overwriting it, with each version filed to the record and its timeline. Products vary in whether staff-side editing exists at all.
- **Duplicate protection at capture.** Because inquirers may already exist in the firm's records (as former clients, adverse parties, or referral sources), products detect likely duplicates at form submission or import and typically merge or link rather than create parallel records.
- **The handoff must reconcile.** When intake hands an accepted client to the practice-management system, the accepted matter must exist exactly once — a second, parallel client/matter record for the same acceptance would corrupt the firm's books and conflicts base. Products therefore either share one system of record with practice management or automate/tightly integrate the conversion step.
- **Speed of first response is a designed behavior, not a nicety.** In the high-volume consumer pole, immediate automated acknowledgment and booking are first-class automation because unresponsiveness loses clients to competing firms.

## Variants

Common variants of the Type:

- **Consumer-law intake funnel** — high inquiry volume from advertising; marketing-led capture, immediate response automation, consultation booking, rapid e-signature; conversion and source ROI are the headline metrics. Common in personal injury, immigration, family, and criminal defense practices.
- **Large-firm new business intake** — lower volume, higher stakes; firm-configured questionnaires, conflict and risk review by gatekeepers, AML/KYC and compliance steps where regulation requires, approval routing, engagement-letter policy enforcement, and in some products ongoing monitoring of client risk after acceptance.
- **Packaging variants** — standalone intake CRM, intake module embedded in a practice-management suite, intake as a native feature inside practice management, or intake as part of an enterprise risk/compliance suite.
- **Sector variants** — legal aid and nonprofit intake adds financial-eligibility screening to the same gate (recorded as a variant; not directly verified in the sampled documentation).
- **Cross-industry reuse** — the same new-business-acceptance structure (questionnaire, conflict check, risk assessment, engagement letter) is sold to accounting and consulting firms, indicating the structure is professional-services-generic while its vocabulary is legal.
- **AI-assisted intake (current market layer)** — AI lead scoring, AI website chat and voice agents answering and pre-qualifying inquiries, AI summaries of new requests for reviewers.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Law Practice Management System | the firm's system of record for accepted clients and active matters; intake covers the pre-acceptance record and feeds the matter into it. In integrated products intake appears as a section or stage inside practice management, but the intake surface (capture, screening, decision, engagement execution) remains the distinctive unit. |
| Legal Matter Management | the matter is the downstream container this Type creates and hands off; intake's object of record exists before the matter is accepted. |
| Legal Conflict Checking Platform | intake *runs* a conflict screening step and records outcomes; the dedicated platform provides deep firmwide conflicts search, clearance workflows, and ethical walls. That enterprise vendors ship these as separate products is direct evidence they are separable. |
| Lead Management Platform / CRM (generic) | captures and nurtures leads but lacks the professional gate: conflict screening, a recorded accept/decline with non-engagement significance, engagement-agreement execution, matter creation. A CRM re-labeled for lawyers without the gate is still lead management. |
| Customer Onboarding Platform | post-sale activation of a paying customer in a commercial relationship; legal client onboarding is the pre-representation acceptance step with professional-responsibility semantics and a different object (client + matter, not account + subscription). |
| Employee Onboarding Platform | HR object (employee joining an organization) vs legal object (client entering a representation). |
| Corporate legal matter intake (internal request triage) | audience is the organization's own employees requesting legal help; object is a service request routed to the legal team, not an external prospective client being screened for representation — likely a separate Type rather than a variant. |

The sharpest seam is with Law Practice Management: the two meet at the moment of acceptance, and integrated products blur the surface while keeping the structure — prospective record, gate, decision, formalization belong to intake; active-matter work belongs to practice management.

## Representative Products

- **Lawmatics** — standalone legal intake CRM for consumer-law firms; matter-primary prospect model with intake pipelines, automation, and marketing attribution.
- **Clio Grow** — intake and onboarding module attached to the Clio Manage practice-management suite; form-driven intake with native matter conversion.
- **PracticePanther** — all-in-one practice management with native intake forms, contact sync, workflows, and e-signature.
- **Intapp Intake** — enterprise new-business intake for large firms; questionnaires, risk/AML scoring, approval routing, engagement-letter generation; also sold to accounting and consulting firms.

The defining structure was checked against older and simpler realizations — paper intake forms with a conflicts check and a typed engagement letter, and the long-standing large-firm "new business acceptance" process — to avoid defining the Type by today's SaaS funnel features.

## Sources

Research date: **2026-09-07**

- Lawmatics — product page: https://www.lawmatics.com/ ; help center: https://help.lawmatics.com/ — articles "Intake Pipeline", "Contacts vs. Matters", "Conflict Checking", "How to Automate Sending Engagement Agreements"
- Clio — help center: https://help.clio.com/ — Clio Grow section, Grow AI section, Intake Forms section; article "Send, View, and Manage Intake Forms"
- PracticePanther — https://www.practicepanther.com/ ; intake feature page: https://www.practicepanther.com/legal-crm/client-intake-software/
- Intapp — New business intake (Intapp Intake): https://www.intapp.com/legal/new-business-intake/ ; product index: https://www.intapp.com/products/intapp-intake/ ; AML subpage referenced at https://www.intapp.com/legal/new-business-intake/aml-kyc-cdd/

> Sourcing limitations: Clio's marketing pages were unreachable (HTTP 403); Clio evidence derives from its help center only. Intapp evidence is limited to official solution/product pages — operational documentation was not fetched, so enterprise workflow details are stated only at the strength of vendor feature descriptions. The legal aid / nonprofit variant and payment-at-intake universality were not directly verified. Precise vendor-specific facts (form-link validity windows, named stages, scoring formulas) are intentionally omitted from this document and remain in the paired Research Notes.
