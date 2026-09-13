# Prior Authorization Platform

## Overview

A **Prior Authorization Platform** is the multi-party system through which advance payer approval for planned health care services is requested, decided, recorded, and tracked. When a health plan requires that certain services — an imaging study, a surgery, a specialty medication, an admission — be approved before they are delivered, this is the machinery that carries the request from the provider side to the payer side, supports the payer's clinical and coverage review, returns a recorded determination, and holds the resulting authorization as a durable record that both parties keep referring to while care is arranged and billed.

The defining structure is deliberately small:

```text
Authorization Request
  (patient/member + provider + coded planned service + clinical justification)
      ↓ submitted in advance of care delivery
Review & Determination
  (payer side evaluates against coverage / medical-necessity rules
   → approve / deny / partial / pend for more information)
      ↓
Authorization of Record
  (durable, trackable approval — status-checkable by the requester,
   consumable as an input by later claims adjudication)
```

Three boundary statements position the Type. First, an approved authorization is **not a payment**: the claim machinery that eventually pays for care is a separate system that merely consumes authorization status as one of its decision inputs. Second, the platform does **not decide** coverage: decision support inside these products recommends and organizes; the determination belongs to the payer party — the plan's own review unit or the delegated review organization acting on its behalf. Third, the Type is the **request machinery**, not the payer's whole clinical review program: prospective, concurrent, and retrospective utilization review form a wider program (documented under Utilization Management) of which the prior-authorization loop is the prospective, transactional face.

## Users & Context

The platform sits between two organizations that must cooperate on every request: the organization delivering care and the organization covering it.

**Provider-side users** work in patient-access, financial-clearance, and prior-authorization roles:

- prior-authorization specialists and financial-clearance staff who determine what requires approval, assemble requests, and shepherd them to outcome
- clinical staff in service lines with heavy approval volume — imaging, orthopedics and spine, oncology and infusion, cardiology, laboratory, durable medical equipment — where the request must carry clinical justification
- referring physicians, who in some arrangements trigger or supply requests for the services they order
- billing and denial-management teams downstream, who depend on authorizations having been obtained correctly

**Payer-side users** work in the health plan's utilization-management operation:

- UM nurses and clinician reviewers who evaluate requests against the plan's coverage policies and medical-necessity criteria
- UM leadership and administrators who manage the review program, staffing, and delegated arrangements
- policy administrators who maintain the criteria and rules that both gate the review and, increasingly, drive automated decision support

A third actor class operates inside the loop without owning either side: **delegated review organizations** that many health plans charge with making determinations in specific service areas. Provider-side platforms must treat these entities as distinct routing destinations alongside the plans themselves.

The work context is a regulated exchange environment: requests carry protected health information and coded clinical data, determinations are consequential clinical-administrative acts, and both sides keep auditable records of what was requested, decided, and why.

## Core Model

### The Authorization Request

The unit of record is the request: a persistent, individually identified record that binds together a specific patient (identified to the payer as its member), the requesting and servicing providers, the planned service(s) expressed in the payer's vocabulary — coded procedures and diagnoses — and the clinical justification for why the service is appropriate. Requests are created from orders and scheduling contexts on the provider side (the order for the MRI, the planned procedure, the prescribed specialty drug), which is why mature platforms integrate with the provider's clinical and practice-management systems rather than standing alone. A request exists before the service does; that timing is part of the definition.

### Review and Determination

On the payer side, each request is worked to a recorded determination. The evaluation is against the payer's own operative rules — what the plan covers, under what clinical criteria, with what documentation — and the outcomes fall into a small closed set: approved (possibly with modifications), denied with reasons, partially approved, or pended pending additional information. The review may be performed by a clinician, by automated logic grounded in the plan's codified criteria, or — the common modern pattern — by automated recommendation with clinician review of the remainder. Across the researched sample, every payer-side product keeps the deciding authority with the plan (or its delegate): automated engines produce recommendations that are traceable to the criteria they applied and overridable by human reviewers, and complex cases are surfaced to clinicians with the relevant evidence organized for review.

### The Authorization of Record

The determination's outcome is held as the authorization: a durable record with its own identifier, defining which services are approved — commonly their scope and count — and, typically, a period of validity. This record is the Type's memory and its connective tissue:

- the provider consults it (status inquiry) while scheduling and delivering care
- the payer reconciles against it when the eventual claim for those services arrives
- extensions, re-authorizations, and additional-unit requests advance through the same loop against it

### What Mature Products Add

Beyond the defining core, mature products commonly carry a standard set of capabilities:

- **Requirement detection** — analyzing scheduled services and orders against payer rules to answer "is authorization required?" before anyone prepares a request, and to flag which clinical documentation the payer will demand
- **Multi-channel intake** — submission through portals, directly from EHR/practice-management workflows, through standardized electronic transactions and APIs, with phone and fax as the legacy baseline these products exist to replace
- **Clinical documentation assembly and attachments** — gathering the required clinical evidence, attaching it to the request, and confirming the payer received it
- **Status inquiry and tracking** — automated retrieval and display of where every outstanding request stands, on both sides
- **Policy-grounded decision support** — payer-side engines that apply codified criteria to incoming requests and organize evidence for human review of the exceptions
- **Delegation routing** — directing requests to whichever entity is charged with the determination, plan or delegate
- **Policy and criteria management** — payer-side maintenance of the review criteria themselves, with outcomes feeding back into policy refinement
- **Denial-avoidance analytics** — provider-side visibility into how authorization failures become claim denials, motivating the whole workflow

### Concept and Implementation

The core model is deliberately conceptual; implementations differ by vantage point:

```text
Concept:   "is authorization required?" check
Realized:  rules engines over provider orders · payer requirement-discovery APIs · manual payer lookup

Concept:   request submission
Realized:  payer or multi-payer portals · EHR-embedded submission · electronic transactions · APIs

Concept:   review
Realized:  clinician worklists · automated recommendations from codified criteria · hybrid

Concept:   status
Realized:  provider tracking boards · payer status inquiry services · public status-lookup pages
```

A reader who has only seen one realization — say, a provider team clicking through payer portals — should still be able to recognize the others from this model.

## How It Works

### 1. Detect the requirement

```text
Service scheduled or ordered
→ check patient's coverage and the planned service against payer rules
→ outcome: no authorization needed (proceed)
          or authorization needed (identify what the payer requires)
```

This step runs before or during registration, at the earliest point the planned service is known. Where requirement rules are machine-readable, the check is automatic; where they are not, it is staff work against payer lookup tools.

### 2. Submit the request

```text
Assemble request: patient/member · providers · coded service(s) · clinical justification
→ attach required clinical documentation
→ submit through the working channel (workflow-integrated, portal, electronic transaction, API)
→ request is lodged with the payer or its delegate; receipt acknowledged
```

Request completeness is the operational hinge: requests submitted with the documentation the payer requires can be approved in near real time; incomplete requests pend and accumulate delay. Mature products therefore push requirement knowledge forward into step 1 and confirm attachment delivery in this step.

### 3. Review and determine

```text
Payer-side worklist receives the request
→ automated logic applies codified criteria (routine cases)
→ remaining cases routed to clinician reviewers with evidence organized
→ determination recorded: approve / deny / partial / pend for information
→ reasons and criteria references recorded with the determination
```

Pended requests loop back: the requester supplies the missing information, review resumes. Denied requests carry reasons that feed both the provider's next step (revised request or appeal path) and the payer's own policy feedback.

### 4. Handle the outcome

```text
Authorization of record created (services approved, typically with validity period)
→ requester notified through their working surface
→ provider schedules / proceeds with care
→ status inquiries answered while care is arranged
→ extension or additional-service requests advance through the same loop
```

### 5. Reconcile downstream (payer side)

When a claim for the authorized services is later adjudicated, its authorization status is checked against the authorization of record. This is where the Type hands off to the claims machinery: some payer-side products also offer explicit reconciliation of claims against authorizations, but the paying itself belongs to the claims-processing Type.

### Capability tiers

**Defining core** — without these, the product is not operating prior authorization:

- authorization requests as persistent records binding patient, provider, coded planned service, and clinical justification
- routing of requests to the party charged with deciding, and a recorded determination with reasons returned to the requester
- the authorization of record: durable, trackable, referable by both parties

**Standard capabilities** — present in most mature products:

- requirement detection, documentation assembly and attachments, status inquiry, decision support with human exception review, delegation routing, EHR and payer connectivity, portal and electronic-channel intake

**Optional / variant** — depends on segment, operating model, and regulatory context:

- real-time automated approval for routine cases; payer-side policy-criteria tooling; claims-vs-authorization reconciliation; appeals handling; referral-status workflows; service-line specializations; regulatory API conformance programs

## Interfaces

### Provider authorization worklist

The provider team's operating surface.

- Typical information: outstanding and recently decided requests by patient, service line, payer, submission date, current status, next action
- Primary actions: initiate a request, complete or correct one, respond to information requests, check status, record outcomes

### Submission surfaces

Where a request is actually created and lodged.

- Either embedded in the provider's order/scheduling workflow (the request pre-populated from the order) or a portal form organized around the payer's requirements
- Typical information: member and coverage identifiers, procedure and diagnosis codes, servicing location and dates, clinical narrative and attachments
- Primary actions: submit, attach documentation, save draft, withdraw

### Payer review workspace

The reviewer's working surface on the determination side.

- Typical information: queued requests with clinical evidence, the applicable criteria side by side, automated recommendations with their rationale where present
- Primary actions: approve, deny with reasons, pend for information, route to another reviewer, record criteria applied

### Status and tracking surfaces

- Provider side: tracking board over all in-flight authorizations; status retrievals pulled from payers automatically where connectivity allows
- Payer/provider shared: status inquiry services, and in some implementations public status-lookup pages keyed to an authorization reference

### Connectivity and configuration surfaces

- Integration surfaces toward EHR/practice-management systems and payer/clearinghouse networks (electronic transactions, APIs, attachments)
- Payer-side policy/criteria configuration, where review logic and documentation requirements are maintained

## Important Rules / Behaviors

### Authorization is not payment

An approved authorization commits the plan to *consider* the service as covered; it is not a payment guarantee. The claim that eventually bills the service is adjudicated independently, and authorization status enters that adjudication as one input among others. This is why a provider can hold an authorization and still face a denied claim, and why payer-side reconciliation of claims against authorizations exists at all.

### The payer party decides

Platforms assist; they do not determine coverage. Automated decision support in these products is implemented as recommendation machinery — traceable to the criteria applied, auditable, and overridable — with the plan (or its delegate) remaining the deciding authority, and complex cases explicitly reserved for clinician review. Provider-side products, for their part, operate the request side end to end and have no determination authority at all.

### Completeness drives speed

The dominant operational rule of the workflow: a request carrying exactly the clinical information the payer requires can be turned around near-instantly, while an incomplete request pends. Much of the products' automation effort — requirement detection, documentation templates, delivery confirmation — exists to move work from the second case into the first.

### The authorization has scope

An authorization is for defined services, commonly in defined quantity within a defined period. Services outside the authorization, or delivered after it lapses, are not covered by it; extension and re-authorization requests therefore run through the same loop as original requests. Exact scope conventions vary by payer and service.

### Requirement rules are payer-defined and change

What requires authorization, and what evidence it needs, is set by each payer's policies and evolves with them. Both sides consequently maintain machinery for keeping requirement knowledge current, and automated feedback of outcomes into payer policy is a common feature of modern payer-side products.

### Denial has a governed aftermath

Denied determinations carry reasons, and the health care context provides structured paths beyond the platform's core loop — revised requests with new information, and formal appeal processes operated under the plan's and regulators' rules. The core loop ends at the recorded determination; appeals are adjacent machinery.

## Variants

Common shapes the Type takes in the market:

- **Provider-side suite component** — authorization handled as part of the provider's financial-clearance workflow alongside eligibility and coverage detection, with heavy workflow integration into EHR/ordering systems
- **Provider-side managed service** — technology plus specialist teams operating the provider's authorization function, human-in-the-loop by design, common in specialty practices, laboratories, and imaging groups
- **Payer-side UM suite** — the plan operates intake, review, and determination through the platform, with policy tooling and clinician workbenches; sold for in-house teams, for delegated operation in specific service lines, or as embeddable APIs
- **Shared network venue** — a connectivity platform operating between many plans and many providers, so one provider workflow reaches many payers and one plan reaches its whole network
- **Service-line specialization** — implementations tuned to the request patterns of specific service families: advanced imaging, musculoskeletal surgery, oncology and specialty pharmacy, cardiology, laboratory, DME
- **Regulatory machinery** — in the United States, standardized electronic transactions of the X12 278 family (request for review and response, inquiry and response, notification and acknowledgment) and payer API mandates for prior-authorization support; other jurisdictions maintain their own prior-approval regimes with the same underlying structure

A variant remains a variant so long as the core loop — request, review-determination, authorization of record — is intact. Where a product's center shifts to the payer's whole review program (concurrent and retrospective review, program governance), it is operating as utilization management; where it shifts to paying the claim, it is claims processing.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Utilization Management | closest sibling | the payer's clinical review *program* — criteria, review types including concurrent/retrospective, reviewer staffing and delegation governance; prior authorization is its prospective, request-level machinery, and market packaging overlaps heavily |
| Payer Claims Processing | downstream consumer | adjudicates claims and pays; consumes authorization status as one decision input; the request→determination loop and the claim→payment loop are distinct machines (the standards bodies themselves define separate transactions for each) |
| Health Plan Administration System | upstream rule holder | holds the benefit plan configuration, including *which services require authorization*; operates none of the request machinery |
| Provider Claims Management / RCM platforms | broader container | provider-side suites bundle authorization as one pre-service step within the whole revenue cycle; this Type is that step's machinery in depth |
| Electronic Prescribing | companion at point of prescribing | e-prescribing products surface electronic prior-auth assistance when prescribing; the authorization record and payer decisioning remain this Type |
| Referral Management | adjacent, different object | referrals authorize a care relationship provider-to-provider; no payer coverage determination is the center |
| Approval Workflow Platform (generic) | structural analogy | same abstract request→review→decision→record loop, but without member binding, coded clinical services, medical-necessity rules, or claims linkage |

The utilization-management boundary is the one most likely to require future refinement: payer-side products market prior authorization inside utilization-management suites, and the two Types share the determination act. The working seam is program versus request machinery, to be confirmed in a joint review of that leaf.

## Representative Products

- **Availity** — dual-sided health information network; payer-side "Intelligent Utilization Management" with policy-grounded AI recommendation and provider-side pre-service authorization tooling, both over a large multi-payer network
- **Waystar** — provider-side revenue-cycle platform whose Authorization Manager automates requirement detection, submission, attachments, and status tracking within financial clearance
- **Cohere Health** — payer-side utilization-management suite centered on prior-authorization automation, sold for in-house, delegated, and API-embedded operating models
- **Infinx** — provider-side technology-plus-services operation of the prior-authorization function for specialty-heavy providers, with AI agents and human-in-the-loop exception handling

## Sources

Research date: **2026-09-09**

- Waystar — Authorization Manager product page: https://www.waystar.com/our-platform/financial-clearance/authorizations/
- Availity — Intelligent Utilization Management (AuthAI): https://www.availity.com/intelligentum/
- Availity — Revenue Cycle Management (pre-service authorizations): https://www.availity.com/revenue-cycle-management/
- Cohere Health — platform and utilization-management overview: https://coherehealth.com/
- Infinx — platform, Patient Access Plus, and payer connections: https://infinx.com/
- X12 — Health Care Services Review Information Transaction Set (278) and example families: https://x12.org/products/transaction-sets

> Sourcing limitation: Experian Health, AMA, and a payer portal page were unreachable during research (HTTP 403/404); the payer-side pole rests on two current-generation vendors, and large legacy payer suites were not directly documented. Operational figures appearing in vendor pages (approval rates, turnaround times, network sizes) are vendor-reported and were not treated as canonical; precise turnaround rules, expiry windows, and regulatory dates are deliberately not stated in this document. Non-US prior-approval regimes were not directly researched; regional realizations are described only at the structural level.
