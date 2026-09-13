# Employment Verification Platform

## Overview

An **Employment Verification Platform** confirms a person's employment and income facts for a third party. It holds or can reach employment records that originate from employers and payroll systems, accepts verification requests from parties outside the employment relationship, resolves each request against those records, and returns the confirmed facts as a report the requester can use as decision evidence.

The defining structure is deliberately small:

```text
Employment records attributed to an identified person
(sourced from employers / payroll — not self-reported)
        ▲
        │ checked against
Third-party verification request
(subject identifiers + authorization for the disclosure)
        │ resolved into
        ▼
Verification report — the confirmed facts, as decision evidence
```

What the platform is *not* is equally defining. It is not the employer's HR system (it serves outside verifiers, not the employer's internal HR work), not a background check system (it confirms one fact domain — employment and income — rather than orchestrating criminal, motor-vehicle, and education checks), and not work-authorization screening (in the US, "employment verification" also names the I-9/E-Verify eligibility domain, which is a different thing entirely).

## Users & Context

Four parties meet inside this Type of application, and the platform is shaped around all of them:

**Verifiers** — the operating users. Mortgage processors and underwriters, consumer lenders, property managers and tenant screeners, background-check teams, and benefits agencies. They submit requests at decision moments: an underwriter confirming income before approving a loan, a property manager confirming employment on a rental application, a hiring team confirming past employment during a background check. Verifiers typically act under professional and legal duties (in the US, the Fair Credit Reporting Act shapes this market), and the platform treats them as accountable parties — many products vet the verifier, not just the request.

**Employees / data subjects** — the people whose records are confirmed. They are not passive: mature platforms notify them of inbound requests, ask them to authorize payroll connections, let them review what was shared, and let them revoke access or delete data.

**Employers** — the source of truth. They make records available directly (contracting the platform to handle verification on their behalf), through HRIS/payroll partnerships, or implicitly by maintaining the payroll accounts employees can connect.

**Platform operator** — the intermediary that holds pre-collected records, operates connection and outreach machinery, applies quality review, and prices per completed verification.

The work context is almost always an application or approval flow on the verifier's side: lending, housing, hiring, or benefits. Speed and completion rate matter because a stalled verification stalls the underlying decision.

## Core Model

### The employment record

The central object is an **employment record attributed to a specific person**: employer identity, employment status (active, inactive, on leave, unknown), employment type (full-time, part-time, contractor), job title, hire date, and termination date. When income is in scope, the record extends to base pay and pay frequency, gross earnings history, hours, and pay changes. Products standardize this model across heterogeneous sources — one product documents a structured identity-and-pay data model spanning profile/employment fields and line-by-line pay data; another documents a fixed report field list covering status, title, dates, earnings, and remarks. The conceptual object is the same: a normalized employment/income profile per person per employer.

### The verification request

A **verification request** is submitted by a third party and carries three things:

- **Subject identifiers** that match the request to the right person's records — name plus strong identifiers such as date of birth and, in the US sample, a government ID number.
- **Scope**: which employer(s) to confirm, and whether employment only, employment with income, or income only is requested.
- **Authorization**: the data subject's consent (captured as a signed authorization form, an in-product consent screen, or a consumer-permissioned connection) and the requester's stated permissible purpose under applicable law. Without this, the platform will not disclose.

### Fulfillment sources

A request is resolved by reaching records through one of several paths. Mature platforms support more than one and choose among them:

- **Pre-collected records** — employment data the platform already holds, deposited by employers or obtained through HRIS and payroll partnerships, so a request can be answered immediately.
- **Consumer-permissioned payroll connections** — the employee logs into their existing payroll account through the platform; the platform retrieves the data directly from the source at the employee's direction. The employee may also upload documents (paystubs, tax forms) when account data is missing.
- **Direct outreach** — the platform's own staff contact the employer's HR department by phone, email, or fax, or submit the request to another verification provider that covers that employer.

### The verification report

The **report** is the deliverable and the reason the Type exists: the confirmed facts, returned to the requester in a structured or PDF form that downstream decision processes accept. Common report shapes observed across the sample:

- employment confirmation (status, title, dates)
- employment with income (the above plus pay and earnings history)
- income-only confirmation (drawn from payroll or, in some products, bank data)
- re-verification — a refresh of an earlier report later in the same decision process (for example, re-confirming employment at loan closing)

### The subject's control layer

Because the underlying data belongs to the employee, mature products expose a control surface: notifications when requests touch their data, consent steps before disclosure, review of what was shared, a dashboard of active connections, and the ability to withdraw access or delete data. The platform acts as the employee's authorized agent for data the employee directs it to share, while also serving verifiers on authorized requests.

```text
Concept:                        Common implementations:
Employment record               HRIS/payroll deposit; payroll-account data; standardized API data sets
Subject authorization           signed authorization form; in-product consent screen; consumer-permissioned connection
Fulfillment                     instant record lookup; payroll connect; document upload; staff outreach to employer
Report                          structured API response; PDF report; re-verification refresh
Subject control                 request notification; connection dashboard; revoke / delete
```

## How It Works

### The verification loop

```text
Verifier submits request
→ subject identifiers + target employer(s) + scope + authorization + permissible purpose
→ platform matches the subject and routes the request to a fulfillment path
→ records are reached and facts are extracted
→ quality review
→ report delivered to the requester
→ (optionally) re-verification later in the same decision process
```

Requesters typically work in a self-service web application — filling out the subject and employer details, choosing scope, attaching the authorization, and paying per completed verification — or submit through an API embedded in their loan-origination, point-of-sale, or screening software. Requests are tracked: mature products expose a live status trail so the verifier can see exactly where a request stands and what happens next.

### Fulfillment paths and fallback

Fulfillment is where products differ most, and where the internal logic matters:

- **Instant path.** If the person's employer is covered by the platform's pre-collected records, the request resolves immediately.
- **Connection path.** Otherwise, the platform recruits the data subject: an email or in-product prompt leads the employee through an employer/payroll search, a login to their existing payroll account, and an explicit consent step before data flows. Connection flows are designed to be embeddable in the verifier's own application, or sendable by email/text invitation.
- **Outreach path.** If no electronic path exists, staff contact the employer directly — including looking up the right HR contact, calling, emailing, or faxing — or route the request to a third-party verification provider that covers that employer. This is the same service that pre-digital verification desks performed, preserved inside modern platforms.

Platforms route between paths automatically — some learn which method works for which employer, and some run methods in parallel. Requests that cannot be completed are eventually canceled; in at least one major product the requester is charged only for completed verifications.

### The employee in the loop

Depending on the fulfillment path, the employee either actively drives the verification (connecting their payroll account and consenting to share) or is informed and able to review (notified that a request was made and what is being shared with the verifier). Both postures exist across the sample; the constant is that the data subject has a visible role and controls, not a hidden one.

### Employer-side outsourcing

A common pattern, especially for large employers: the employer contracts the platform to handle *all* incoming verification requests on its behalf. The platform becomes the employer's official verification channel — verifiers are directed there, records are answered from the deposited data, and HR is relieved of the request traffic entirely.

## Interfaces

**Verifier request form** (web app). Purpose: submit a new verification. Typical content: subject name and identifiers, authorization, employer selection from a searchable directory (multiple employers per request), scope selection, stated purpose, pricing summary. Primary actions: submit, save, pay.

**Requests dashboard** (verifier). Purpose: track open and completed verifications. Typical content: per-request status trail, method in use, additional-information requests, completed reports. Primary actions: respond to information requests, download reports, cancel.

**API and system integrations.** Purpose: run the same loop inside the verifier's own software (loan origination, point-of-sale, screening platforms). Typical shape: submit request, receive webhooks/status events, retrieve structured report data.

**Employee connection flow.** Purpose: let the data subject authorize and supply records. Typical content: employer/payroll search, login to the existing payroll account, consent screen showing what will be shared, document upload as fallback. Primary actions: search, connect, consent, upload.

**Employee dashboard.** Purpose: ongoing control of shared data. Typical content: connected accounts, data shared with which providers, sharing duration. Primary actions: adjust or remove connections, request deletion.

**Employer console.** Purpose: employers that outsource verification manage their participation — records available to verifiers, request handling on their behalf. (Details of this surface vary most between products; several keep it behind employer login.)

## Important Rules / Behaviors

**Authorization precedes disclosure.** No request is fulfilled without the data subject's authorization and the requester's stated permissible purpose. This is the legal spine of the Type (FCRA-shaped in the US sample) and is enforced structurally — required form fields, consent screens, permissioned connections — not just contractually.

**Requests must match a real record.** The platform confirms against employer-sourced data; it does not adjudicate self-reported claims. Strong identifiers are required precisely because matching the wrong person's record is the cardinal failure. If the subject's data cannot be found through any path, the honest outcome is an unfulfilled request, not a best guess.

**The record reflects payroll reality.** Reports state facts as payroll holds them — including terminated status, leave, and wage as of termination. Employers may decline to provide some information (certain products note that additional data points can be refused by the employer); the platform reports what the source supports.

**Completion is the billing event.** Commercial models charge per completed verification; unsuccessful requests are canceled without charge in the sampled pay-per-completion product, and unfulfillable requests are auto-canceled after a bounded period rather than left open indefinitely.

**Quality review before release.** Retrieved data is reviewed for completeness and accuracy before the report is issued; submissions that fail review are retried through another path or canceled.

**Subject control is revocable.** Connections can be withdrawn and data deleted by the data subject; platforms that market consumer permissioning treat this as a first-class capability (including a consumer-facing dashboard and a delete-data request path), not a support-ticket process.

## Variants

- **Database-first platforms** — the incumbent pattern: employers deposit records; verifiers pull reports from a large pre-collected database. Instant for covered employers; coverage is the product's main asset.
- **Consumer-permissioned direct-source platforms** — newer pattern: records are pulled live from payroll accounts the employee connects. Fresher data, no deposit needed, but completion depends on the employee acting.
- **Service-heavy verification** — platforms whose differentiator is a staffed operation that reaches any employer by any means; often combined with the other two as a fallback tier.
- **Embedded/API products** — the same loop sold as infrastructure inside loan-origination, point-of-sale, or background-check systems rather than as a standalone web app.
- **Industry packaging** — mortgage (report shapes and re-verification aligned to underwriting and closing, validation programs for government-sponsored loans), consumer lending, tenant screening, hiring background checks, government benefits eligibility. The core loop is identical; packaging changes report formats, integrations, and compliance framing.
- **Scope extensions** — asset verification from bank connections, document processing of uploaded paystubs and tax forms, gig-economy work data (tasks, earnings, ratings). These extend the Type; they do not define it.
- **Ownership patterns** — standalone platforms, credit-bureau product lines, and subsidiaries of background-check groups all exist in the current market.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Background Check Platform | consumer / adjacent | Orchestrates many check types (criminal, MVR, education, employment) with adjudication workflow; employment verification is one input it consumes — often bought from a platform of this Type. Remove the multi-domain orchestration and only employment-fact confirmation remains. |
| HRIS / Payroll System | upstream | The employer's system of record; it holds the data and may generate self-service verification letters for its own employees, but it has no external-verifier request loop. Verification platforms source from it via deposit or connection. |
| Identity Verification / KYC Platform | adjacent | Establishes *who someone is*; this Type establishes *facts about someone's employment and income*. Verification requests carry identity attributes for record matching, not for identity establishment. |
| Income Verification (financial documents / open banking) | overlapping capability | Confirms income from bank statements or tax transcripts — a different record substrate. Frequently bundled alongside employment verification; the employment-anchored confirmation against employer-sourced records is what belongs to this Type. |
| Employment Eligibility Verification (I-9 / E-Verify) | name collision only | Despite the shared US label "employment verification," this confirms work authorization with a government system — different object, parties, and rules. Not this Type. |
| Credit Bureaus / Credit Reporting | adjacent industry | Similar report-per-request economics and regulatory posture, but the underlying record domain is credit behavior, not employment. Some incumbents operate in both domains. |
| Candidate Assessment / Screening Tools | different phase | Evaluate candidates (skills, interviews); employment verification confirms factual history, typically later in hiring. |

The most important boundary is with the Background Check Platform: the two Types are complementary, not competing — background-check groups acquire and embed employment-verification platforms, and verification platforms list background-check companies among their customers. One confirms a single fact domain; the other runs a multi-domain check program.

## Representative Products

- **The Work Number (Equifax)** — the dominant incumbent; database/deposit model at credit-bureau scale.
- **Truework (Checkr Group)** — verifier platform uniting instant records, consumer payroll credentials, and staff outreach behind one request loop; API and web app.
- **Argyle** — consumer-permissioned direct-source platform; standardized payroll data sets delivered via API, console, and PDF reports.

The defining model was checked against the pre-digital pattern it replaced (HR departments and outsourced bureaus answering phone/fax requests) to ensure the definition does not over-fit today's digital implementations.

## Sources

Research date: **2026-09-06**

- Truework Help Center (official operational documentation):
  - Report Types — VOI vs. VOIE vs. VOI(only) vs. Reverification — https://help.truework.com/hc/en-us/articles/14530538028183
  - How does Truework complete every verification? — https://help.truework.com/hc/en-us/articles/4403451853335
  - How to submit a new verification request — https://help.truework.com/hc/en-us/articles/10827198639383
  - Status updates on pending verifications (full lifecycle guide) — https://help.truework.com/hc/en-us/articles/360049393333
  - What is Truework? Intro for Employees — https://help.truework.com/hc/en-us/articles/4408803758615
  - Truework 101 (for verifiers) — https://help.truework.com/hc/en-us/articles/4403451702935
- Truework product site — https://www.truework.com/
- Argyle developer documentation:
  - How Argyle Works — https://docs.argyle.com/overview/how-argyle-works
  - Data Sets (data model) — https://docs.argyle.com/overview/data-structure/data-sets
- Argyle product and consumer pages — https://argyle.com/ , https://argyle.com/consumers

> Sourcing limitation: The Work Number (theworknumber.com, equifax.com), Experian Verify, and Vault Verify refused automated access (HTTP 403) during this research pass, and no operational details for those products are stated from memory. The Work Number's role in the market is attested indirectly through sampled products' official documentation. Statements about the database/deposit model are calibrated to that indirect evidence; precise figures, defaults, and product-specific mechanics were intentionally excluded from this document and remain, where observed, in the Research Notes.

Detailed product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
