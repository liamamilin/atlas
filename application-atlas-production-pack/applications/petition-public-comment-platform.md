# Petition / Public Comment Platform

## Overview

A **Petition / Public Comment Platform** is the public-input channel of institutional decision-making. Its unit of record is a bounded, publicly visible **input campaign** — a petition demanding a specific action, or a comment period on a specific proposal — addressed to the institution or decision-maker responsible for that action. People contribute **attributed input** to the campaign: signatures on the petition face, structured responses or comments on the public-comment face. The input accumulates as a public measure of support or concern, and what the addressed institution does with it — a response, a debate, the start of a procedure, published results — is recorded back on the public campaign record.

The defining core is small:

```text
Public-input campaign of record
└── addressed to an institutional decision context
    └── attributed citizen input accumulating on the campaign
        └── institutional handling with a published disposition
```

The leaf name covers two faces of the same structure. In the **petition face**, citizens initiate: someone drafts a demand, gathers initial support, and the platform runs a signature campaign whose volume can trigger defined handling. In the **public-comment face**, the institution initiates: it opens a bounded period in which the public responds to a specific proposal, and the responses are analyzed and answered. Who initiates, and what triggers the handling, are the main variant axes — not different Types.

The Type ends where participation becomes a composed multi-mechanism space (civic engagement platforms), where input becomes an operational service case (311 systems), where handling becomes statutory docket machinery (rulemaking platforms), and where the instrument becomes a private measurement tool (survey platforms).

## Users & Context

Three user roles, with the institution's handling side as prominent as the public's contributing side:

**Campaign initiators**
- petition creators: a person (or, in some systems, a required organising group) who drafts the demand, recruits initial supporters, and promotes the campaign
- consultation operators: government officers and consultation professionals who publish the proposal documents, configure the response form, and manage the comment period

**Participants**
- signers: people who add their signature to a petition, usually after an eligibility or identity check
- respondents: people who read the published proposal and submit a structured response or comment, sometimes with consent for their response to be published

**Institutional handlers**
- petitions teams and committees: staff and elected bodies that check petitions against standards, consider them, arrange debates, and record responses
- verification authorities: bodies that validate collected support in systems with formal verification
- analysts: staff who interpret response data and draft the published outcome

The context is formal public decision-making: parliaments and legislatures, government departments and agencies, municipalities, and supranational institutions. Open petition-hosting services extend the same structure to campaigns addressed at any decision-maker — companies, institutions, organizations — where the platform's role is hosting and promotion rather than formal handling.

## Core Model

### The campaign of record

The central object is the **campaign**: a persistent, individually identified, publicly visible record bound to one specific demand or proposal. A petition carries its call for action and supporting detail; a consultation carries the proposal documents and the questions put to the public. The campaign has an identity (title, text, owner/organiser), a state (see How It Works), and a public page where everything about it accumulates.

Two properties make it a campaign of record rather than a post or a form:

- it is **addressed** — it asks for, or comments on, an action by an identified institution or decision-maker responsible for it. Open petition hosts extend addressing to any target, but the addressing is still what the campaign exists for.
- it is **bounded** — it runs within a defined window (open and close dates, or a fixed collection period), after which it closes and its record is completed.

### Attributed input

Participants contribute input that is attributed to them and accumulates on the campaign:

- **signatures** (petition face) — a person's recorded support, commonly gated by an eligibility rule (citizenship, residency, age) or an identity confirmation
- **responses / comments** (comment face) — structured answers to the questions posed, or free-text comments on the proposal, commonly gated by consent rules when they are to be published

The accumulated input is publicly visible as a **count** — the signature total or response total on the campaign page. The count is the campaign's public measure of support or concern, and in threshold-based systems it is also the trigger for formal handling.

### The handling loop and the published disposition

The campaign exists to enter an institutional decision process. What happens there is recorded back on the campaign record:

- a **formal response** published on the campaign page (by the responsible department, the commission, or the operating institution)
- a **consideration outcome** — debate arranged or declined, procedure started, initiative accepted or rejected
- a **published analysis and outcome** — results reports, and structured summaries of what was asked, what respondents said, and what was done
- in systems with response publishing, the **individual responses themselves**, moderated and redacted, published for public inspection

In institution-operated products this loop runs inside the platform. In open petition-hosting products the loop is external — the platform hosts and promotes the campaign, and the "disposition" is whatever persuasive effect the campaign achieves — but the campaign is still built around the addressed decision.

### Concept and implementation

The core model is conceptual; products realize it differently:

```text
Concept:   input campaign of record
Realized as: e-petition, citizens' initiative, consultation activity

Concept:   attributed input
Realized as: signature, statement of support, structured survey response, comment

Concept:   admission gate
Realized as: standards check, registration decision, technical validation, operator publishing

Concept:   published disposition
Realized as: government response, formal communication, procedure start, results page, published responses
```

## How It Works

### The petition flow (citizen-initiated)

```text
Draft the demand
→ recruit initial supporters
→ pass the admission gate (standards check / registration / validation)
→ campaign published and opened for signatures
→ signatures accumulate publicly within the bounded window
→ threshold reached (where the system defines one)
→ formal handling (response / debate consideration / procedure start)
→ disposition published on the campaign page
→ campaign closes with its complete public record
```

Initiation is deliberately gated. Before a petition can collect signatures at scale, it typically must pass an admission step: a minimum of initial supporters, a check against published standards (with rejection and stated reasons when it fails), or a registration decision by the addressed institution. Duplicate control is common here — creators are asked to check for similar existing campaigns, and some systems suggest them automatically.

### The comment flow (institution-initiated)

```text
Institution prepares the proposal and the response questions
→ comment period published with open/close dates
→ public reads the documents and submits responses
→ responses accumulate (optionally published individually, moderated and redacted)
→ period closes
→ responses analyzed
→ outcome published (results report / structured summary / published responses)
```

The operator controls the window: the campaign is published ahead of its opening date, collects responses while open, and closes on its set date. A closed campaign's page typically turns to the outcome — either a results report or a structured summary of what was asked, what respondents said, and what was done.

### What both flows share

- the campaign page is the single public anchor: text, input count, and disposition all live there
- the window is bounded and its transitions are automatic
- the input is attributed and eligibility- or consent-gated
- the disposition is published, not silently filed

## Interfaces

### Campaign discovery / browse

The public entry surface: lists of open, closed, and (where applicable) rejected or archived campaigns, with search and filtering. Typical information: title, topic, input count, state, closing date. Primary actions: open a campaign, start a petition (petition face), find consultations (comment face).

### Campaign page

The campaign's public record and the Type's most important surface.

- the full campaign text (demand or proposal documents)
- the input count and, where defined, the threshold state
- the disposition once it exists: response text, debate outcome, procedure status, results report, structured outcome summary
- primary actions: sign / respond, share, follow for updates

### Input surface

What a participant actually completes: a signature confirmation (identity/eligibility details plus confirmation) or a response form (the questions posed, with validation). Where individual responses are published, the input surface carries the consent question that permits publication.

### Admission / moderation console (operator side)

Where campaigns are checked and managed before and during collection: standards review with approve/reject/amend decisions, duplicate checks, moderation and redaction of responses queued for publishing, moderator assignment.

### Analysis and outcome surfaces (operator side)

Response analysis and exports, results-report creation, and the outcome-publishing forms (results files, structured summaries of what was asked, said, and done). This is where the handling loop's analytical half happens.

## Important Rules / Behaviors

### Admission gates the campaign before it can collect

A campaign cannot collect input at scale until it passes its admission step — standards check, registration decision, or technical validation. Rejection is a first-class outcome: rejected campaigns are recorded (and in some systems publicly viewable, though not signable) with reasons.

### Eligibility and consent gate the input

Who may sign or respond is rule-governed: citizenship or residency requirements, age requirements, registration. Where individual responses are published, a consent question governs permission, and published responses pass through moderation and redaction first. Publishing may happen while the campaign is open or after it closes.

### The window is bounded and automatic

Campaigns open and close on set dates without manual intervention. After closing, the campaign's record is completed — the page turns from collection to disposition.

### Thresholds trigger defined handling — where the system defines them

In many government-run systems, reaching defined signature counts obliges or triggers specific handling: a formal response, consideration for debate, or the start of an administrative procedure. The counts, their consequences, and even their existence vary by jurisdiction and product; some systems gate handling by analysis rather than volume, and open-hosting systems define no formal handling at all.

### The disposition is public

Whatever the addressed institution decides — response, debate, procedure, results — is published on the campaign record. This closure of the loop is the Type's defining behavior: the platform is not only a collection channel but the public record of what the input achieved.

### Verification depth varies structurally

Support may be unverified (open hosting), identity-confirmed at signing, or formally verified by authorities with certificates. The deeper the verification, the more the platform functions as an instrument of formal procedure rather than persuasion.

## Variants

- **Parliament-run petition service** — the institution operates the platform as its official petition channel; admission standards, thresholds, committee consideration, and published responses are structural (e.g. a national parliament's e-petition site).
- **Supranational initiative instrument** — a treaty-based instrument with organising-group requirements, registration decisions, authority verification of support, and a fixed examination timeline ending in a formal institutional communication.
- **Municipal open-source initiative space** — a self-hosted framework in which the petition structure is one configured space type, with local rules determining initiative types and signature requirements.
- **Commercial consultation platform** — subscription software operated by institutions to run statutory and informal consultations: proposal publication, structured response collection, analysis, response publishing, and outcome reporting.
- **Open petition hosting** — a private service where anyone hosts a petition addressed at any target; no formal handling machinery, persuasive standing only, commonly freemium with promoted placements.
- **Statutory vs advisory posture** — some comment campaigns carry legal obligations (for example, planning consultations with a statutory duty to publish submitted responses); others are advisory engagement.
- **Paper + online hybrid** — systems that integrate paper-collected support (statement forms, physical collection points, offline response import) alongside online collection.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Civic Engagement Platform | composes many participation mechanisms (forums, ideas, budgets, polls) inside engagement spaces; here the input campaign is the primary and only object. A petition-shaped component inside a composed platform belongs to the engagement platform, not this Type |
| Rulemaking & Public Consultation Platform | the agency-side statutory machinery — docket management, comment aggregation and analysis obligations inside a rulemaking procedure; this Type is the citizen-facing input campaign. The public-facing comment portal of a rulemaking program sits on this leaf's side of the seam |
| 311 / Citizen Service Request Platform | individual service requests with an operational case lifecycle (report → assign → resolve); here the unit is collective input on a decision with formal handling |
| Advocacy Platform | multi-channel campaign orchestration (email/call campaigns, supporter journeys) for organizations; here the single input campaign of record with institutional addressing is the center. Open petition hosts sit closest to this seam |
| Survey Platform | the response instrument is often survey-shaped, but the container here is the public campaign of record with an addressed decision and a published disposition; a survey is a private measurement instrument |
| Online Donation Platform / Crowdfunding | petitions may carry donation asks, but the input of record is signatures/comments, not money |
| Government Meeting / Agenda Management | "public comment" in the meeting sense (speaking at hearings, commenting on agenda items) is meeting-centric; this Type is campaign-centric with a bounded collection window |
| Government Transparency Portal | one-way publication of information; here the public contributes input and the institution responds through a participatory loop |

## Representative Products

- **UK Parliament Petitions** (petition.parliament.uk) — parliament-run e-petition service with admission standards, signature thresholds, committee consideration, and published government responses
- **European Citizens' Initiative** (citizens-initiative.europa.eu) — supranational initiative instrument with registration, authority verification, and a formal Commission response procedure
- **Decidim** (Initiatives space) — open-source participatory framework whose initiative space realizes the petition structure under municipal rules
- **Citizen Space (Delib)** — commercial consultation platform for statutory and informal public comment, with response publishing and outcome reporting
- **GoPetition** — open petition hosting with persuasive rather than formal standing
- **Change.org** — the largest consumer petition platform (market anchor; its documentation was not reachable during research, so no operational details are asserted here)

## Sources

Research date: **2026-09-09**

- UK Parliament Petitions — "How petitions work" — https://petition.parliament.uk/help
- European Citizens' Initiative — "How it works" — https://citizens-initiative.europa.eu/how-it-works_en
- Decidim Documentation — "Participatory spaces", "Components" — https://docs.decidim.org/en/develop/features/participatory-spaces , https://docs.decidim.org/en/develop/features/components
- Delib Knowledge Base (Citizen Space) — "Activity types", "Response publishing — what is it?", "The status of your activity", "Publishing results and outcomes" — https://help.delib.net/
- Delib — product pages — https://www.delib.net/
- GoPetition — "How to write a petition" — https://www.gopetition.com/how-to-write-a-petition

> Sourcing limitation: Change.org (help center and about pages) and Regulations.gov (about and help pages) could not be fetched from the research environment on 2026-09-09. Both are held as market anchors only; no operational details for them are asserted in this document. Threshold values, window lengths, and verification regimes named in the researched products are recorded in the paired Research Notes; this document states the mechanisms conceptually because their specific values are jurisdiction- and product-configured.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the joint review with the civic-engagement pass) are recorded in the paired Research Notes.
