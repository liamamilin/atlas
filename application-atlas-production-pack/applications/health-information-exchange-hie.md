# Health Information Exchange / HIE

## Overview

A **Health Information Exchange (HIE)** application is the cross-organizational layer through which independent healthcare organizations exchange clinical information about identified patients — securely, under an enforceable trust framework, and with some mechanism for knowing that records held by different participants refer to the same person.

It exists because patient care spans organizations: a person's history sits in the records of hospitals, clinics, labs, and community providers that do not share a system. An HIE application connects those organizations as a standing participant community and moves patient-anchored clinical data between them — typically as clinical documents and increasingly as structured records — so the information can inform care at the receiving organization.

The defining structure is deliberately small:

```text
Cross-organization participant community
└── Patient-anchored clinical exchange (documents / records about identified patients)
    └── Patient identity linkage across organizations
        └── Governed trust framework (participation, permitted purposes, auditability)
```

Two exchange modalities dominate real deployments — directed (push) exchange between known parties and query-based (pull) exchange across the community — but the modalities are realizations of the exchange core, not the core itself. Everything else commonly associated with HIE — centralized record repositories, notification services, public-health routing, patient portals, analytics — is common or optional structure layered on this foundation.

When the reach collapses to a single organization, the product is drifting toward Electronic Health Record territory; when the exchanged payload stops being patient-anchored clinical data, it is drifting toward generic data exchange.

## Users & Context

The HIE application serves several distinct user groups whose relationships to it differ:

**Primary operational users**

- **Clinicians and care-team staff at participating organizations** — look up whether a patient has records elsewhere (often for unplanned care: emergency visits, referrals, transitions), view exchanged records in a portal or inside their own EHR, and receive documents pushed from other providers.
- **IT / integration staff at participating organizations** — connect the organization's systems to the exchange (interfaces, credentials, registration feeds), keep feeds healthy, and resolve onboarding or delivery problems.
- **Exchange operators** (the organization running the HIE) — onboard participants, monitor exchange activity and data quality, administer consent choices, and operate help desks for participants.

**Secondary users**

- **Patients** — exercise choice over whether their information is available through the exchange (opt-out / opt-in, jurisdiction-dependent) and, in some deployments, access their own cross-organization record.
- **Public health agencies** — receive routed reporting (a common but optional flow).
- **Payers and other institutional participants** — participate under the same governance in some deployments.

The work context is institutional and regulated: every exchange act is attributable and auditable, participation is contractual, and the permitted reasons for requesting or sharing data are constrained by the governing framework.

## Core Model

### The Defining Core

Four structures held jointly. Removing any one stops the product from being a health information exchange:

**1. Cross-organization participant community.** A standing population of independent organizations — hospitals, clinics, labs, health systems, agencies, sometimes other exchanges — connected as participants of one exchange capability. Membership is explicit, credentialed, and maintained (onboarding, credentials, suspension). This is what separates an exchange from a single organization's own system: the community, not any one member, is the unit.

**2. Patient-anchored clinical exchange.** What moves between participants is clinical information *about identified patients* — encounter summaries, care documents, lab results, medication and problem information, discharge and transition documents — carried as standard clinical documents and, increasingly, as structured records. The exchange does not create clinical data and does not modify source records; it moves and makes available what participants hold.

**3. Patient identity linkage across organizations.** Every participant has its own patient identifiers. For exchange to be safe, the capability maintains — somewhere in the system — the association that records from different participants refer to the same person. Realizations vary widely: a platform-level master patient index maintained from registration feeds; matching performed independently by each responding organization against the demographics supplied in a query; or, in directed exchange, credentialed provider addressing plus the sending system's own patient record. What is invariant is the linkage itself, not where it lives.

**4. Governed trust framework.** Participation sits inside enforceable governance: participation agreements, identity and credential verification of participants and endpoints, defined purposes for which data may be requested or shared, and auditability of exchange activity. Governance is what makes "appropriately and securely share" enforceable rather than aspirational — it determines who may join, what they may ask for and why, what they must contribute in return, and what happens when they violate the rules.

### Capabilities Mature Products Commonly Add

These are widespread in real products but not what makes a product an HIE:

- **Directed (push) exchange** — secure, encrypted transmission of patient documents between known, credentialed parties (referrals, discharge summaries, lab results), supported by a **provider/participant directory** of verified addresses and endpoints.
- **Query-based (pull) exchange** — discover-and-retrieve across the community: a request for a patient's available records is routed to the participants likely to hold them, and documents or metadata come back from each responder.
- **Event notifications** — alerts that a patient had activity somewhere in the community (facility admission/discharge/transfer feeds, or notifications derived from observed exchange activity), delivered to organizations following that patient.
- **A data layer held central, federated, or both** — some deployments aggregate exchanged documents into a longitudinal record; others leave data at the source and route queries to it ("record location"); many products offer both postures.
- **Processing depth as a spectrum** — retrieved documents can be delivered raw (source-native clinical documents) or processed (parsed, normalized to structured form, deduplicated, and stored for reuse). Transport-oriented services may perform none of this processing.
- **Consent administration** — recording and honoring patient choices about whether their information is available through the exchange.
- **Audit and accountability** — exchange activity logged and reviewable; compliance monitoring with consequences up to suspension.
- **Onboarding and integration machinery** — the operational workflow of connecting a participant's systems, establishing feeds, and testing exchange.

### One Structure, Many Implementations

The core model is conceptual; implementations differ on where things live and how they are packaged:

```text
Concept:  Patient identity linkage
Realizations:  platform master patient index · distributed matching at each
               responding organization · credentialed addressing + directory

Concept:  The exchanged data layer
Realizations:  central aggregated record · federated/record-location routing ·
               transport-only (data never at rest in the exchange)

Concept:  Trust framework
Realizations:  regional/state exchange programs · national frameworks with
               designated networks · EHR-vendor-run exchange networks
```

## How It Works

### Joining the exchange (participant onboarding)

```text
Execute participation agreement
→ establish identity/credentials for the organization and its endpoints
→ connect systems (clinical interfaces, registration feeds, messaging endpoints)
→ test exchange against the framework's requirements
→ go live as a requestor and/or responder
```

Participation roles differ: some organizations both request and provide data; some respond to queries without initiating them; transport/connectivity participants serve the others.

### Keeping identity coherent (registration and matching)

```text
Participant systems send patient registration/updates (registration feeds or records)
→ demographics are standardized (names, dates, addresses, contact details)
→ records are matched and linked to the same person across participants
→ ambiguous cases are held as multiple candidates rather than forced together
```

Matching is inherently probabilistic and runs on multiple demographic factors; no single field is decisive, and completeness of demographics drives confidence. In distributed designs, the responding organization applies its own matching logic, so the same query may match differently at different participants.

### Directed exchange (push)

```text
Provider selects a patient document (e.g., a care summary)
→ selects the receiving provider from the verified directory
→ message travels encrypted between the two endpoints
→ delivery is logged; the receiver renders/imports the document
```

Typical content: referrals, discharge summaries, lab orders and results. The same channel commonly carries reporting to public health agencies in exchange-active deployments.

### Query-based exchange (pull)

```text
A care encounter creates a need (ER visit, referral, intake)
→ clinician or system queries for the patient across connected networks
→ the request is routed to participants likely to hold the patient's data
   (record-location discovery, known patient links, directory endpoints)
→ each responding organization checks the request against its own rules
   (identity match, purpose of use, consent)
→ available documents / metadata are returned
→ records are viewed, or processed (normalized, deduplicated) and stored for reuse
```

Results depend on who participates, what they hold, and how matching went; completeness is never guaranteed, and honest products say so.

### Notifications and follow-up

```text
Facility feed or exchange-derived detection indicates patient activity
→ notification delivered to the subscribed organization (integration or secure channel)
→ source document available on request where licensed/permitted
```

Notifications are situational awareness, not a complete encounter history — a limitation mature products document explicitly.

### Consent administration

```text
Patient records a choice (opt-out / opt-in, per the jurisdiction's regime)
→ choice recorded in the exchange
→ matching and exchange honor the choice
→ patient can change the choice at any time
```

## Interfaces

The surfaces vary by packaging pole, but recurring interfaces include:

**Clinician portal** — a secure web application over the exchanged record. Typical information: patient summary assembled from multiple sources, documents with source attribution, medications, allergies, results. Primary actions: search patient, view documents, download/print, push a document to another provider.

**EHR-embedded access** — the same exchanged data surfaced inside the clinician's own system (integrated views or standards-based app launches), so lookup happens without leaving the chart.

**API / developer surface** — programmatic access to the exchange for other software: query for documents, retrieve and process records, contribute data, subscribe to notifications. This is the primary surface of the API-first pole.

**Secure messaging interface** — an inbox-style surface for directed exchange (encrypted provider-to-provider messages with document attachments).

**Operations console** — the operator's surface: participant onboarding and status, exchange monitoring, transaction and usage reports, consent administration, issue investigation.

**Patient-facing surface** — the consent form/portal where patients record their choice, and in some deployments a portal for accessing their own cross-organization record.

## Important Rules / Behaviors

**Permitted purposes gate exchange.** Data may be requested or shared only for purposes the framework allows (commonly: treatment, payment, healthcare operations, public health, government benefits determination, and patient personal access, in the US national framework). The purpose is declared with the request; a query made for one purpose cannot quietly serve another. At least one product derives its activity alerts exclusively from requests carrying the treatment purpose.

**Retrieval generally carries contribution obligations.** National exchange frameworks are built on reciprocity: organizations that retrieve external records are generally expected to contribute clinically meaningful data in return, per their participation model. The platform enforces contribution requirements based on role and configuration.

**Responders keep control.** Every response is discretionary and rule-checked at the responding organization: its own matching decision, its own consent policy, its own access controls. A requestor never reaches into a participant's system directly; results are what responders choose to return.

**Identity matching is probabilistic by design.** No single demographic field is decisive; ambiguity produces multiple candidates rather than a forced match — trading convenience for safety. Some frameworks require stricter agreement (exact core demographics plus a shared contact or address detail) before automatic linkage.

**Patient choice overrides availability.** An opt-out removes the patient's information from exchange availability; the choice is honored during matching and queries and can be changed at any time. Regimes differ by jurisdiction (opt-out is common in US regional deployments; other deployments require affirmative opt-in).

**Personal access requires verified identity.** When a person retrieves their own records through the exchange, the transaction requires identity verification plus explicit authorization, beyond the usual participant credentials.

**Everything is logged.** Exchange activity is recorded and auditable; frameworks provide for compliance review, remediation, and suspension or termination of participation for serious violations.

**Retrieval is not completeness.** A query returns what participating, consent-compliant responders hold and choose to return. Mature products document that notifications and retrievals are not an authoritative encounter history.

## Variants

- **Regional / state exchange programs** — an operator runs the exchange for a jurisdiction's provider community; patient choice regimes and reporting flows are often shaped by state policy.
- **National framework networks** — designated national networks whose participants exchange under a shared trust agreement; regional exchanges and vendors participate as members.
- **Platform-vendor pole** — a vendor supplies the exchange platform for a program or a health system coalition, typically including the portal and record aggregation; common for shared-care-record programs.
- **API-first interoperability platform** — the exchange is consumed programmatically; a single connection abstracts many underlying networks.
- **Connectivity-service pole** — the thin edge: accredited transport, directory, and trust services carrying exchange traffic, with record aggregation and matching left to the edge systems.
- **EHR-embedded exchange networks** — exchange operated by an EHR vendor across its customer base; the machinery is the same while the packaging sits inside the EHR relationship.
- **Scope breadth** — clinical documents as the base; some deployments add labs, imaging, or claims-adjacent data; public-health reporting routing is a common extension.
- **Consent regime** — opt-out vs opt-in vs person-authorized access, varying by jurisdiction.
- **Architecture posture** — central repository vs federated/record-location vs hybrid; transport-only vs full processing depth.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Electronic Health Record / EHR | one organization's internal system of record; the HIE is the cross-organization exchange layer between such systems; exchanged data typically lands back inside an EHR |
| Care Coordination Platform | owns care workflow (plans, tasks, team communication); HIE owns the data-exchange substrate those workflows may consume |
| Referral Management | manages the referral as a workflow object with lifecycle and appointments; directed exchange may carry the referral document without managing the referral |
| Patient Portal | patient-facing access to one organization's records; cross-organization personal record access (individual access services) is an HIE service that drifts toward portal territory when it becomes the product's center |
| Clinical Communication Platform | staff-to-staff messaging about care; HIE directed exchange is patient-anchored document movement between organizations under governance |
| Data Exchange Platform (generic) | moves any data between parties; lacks patient identity linkage, clinical document semantics, permitted-purpose constraints, consent, and health-regulatory audit obligations |
| Integration / interface engines | transformation-and-routing tooling — a component inside realizations, not the exchange itself |
| Population Health Management | consumes aggregated patient data for analytics; the HIE moves and makes available the data |

## Representative Products

- **Orion Health** — pure-play HIE platform vendor (shared-care-record programs; direct secure messaging)
- **Health Gorilla** — API-first interoperability platform and designated national network (QHIN)
- **MedAllies** — accredited connectivity service provider (direct transport, directory, national network on-ramp)
- **KONZA Health** — regional/state HIE operator providing national network services

The core model was checked across these poles — record-centric platform, API platform, transport service, and operator — to avoid defining the Type by any single packaging.

## Sources

Research date: **2026-09-08**

- ONC (HealthIT.gov) — "What is HIE?" (definition, exchange forms, permitted exchange purposes) — https://www.healthit.gov/topic/health-it-and-health-information-exchange-basics/what-hie
- Health Gorilla developer documentation (network participation, patient matching, data contribution, governance, record retrieval, clinical alerts, individual access services) — https://developer.healthgorilla.com/docs/
- Orion Health — product and solution pages (shared care record, direct secure messaging) — https://orionhealth.com/
- MedAllies — product and service pages (HISP, national network, provider directory) — https://www.medallies.com/
- KONZA Health — HIE services and patient resources pages (longitudinal record access, query-based exchange, patient opt-out/opt-in) — https://www.konza.org/

> Sourcing limitation: three of the four sampled vendors are evidenced at product/service-page level only (their operational documentation is not public); detailed operational behavior — matching depth, consent machinery, audit detail — is asserted specifically only where vendor documentation is public. The platform-suite pole of the market could not be sampled directly (documentation behind a login/license wall). Precise operational parameters (limits, fees, defaults, exact thresholds) are intentionally not stated in this document.
