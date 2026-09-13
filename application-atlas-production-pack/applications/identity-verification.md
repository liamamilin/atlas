# Identity Verification

## Overview

An **Identity Verification** application is an organization-operated system for establishing that a specific person is who they claim to be. The person submits identity evidence — typically a government-issued document, a biometric selfie, or personal attributes — through a capture flow operated or embedded by the product. The product evaluates that evidence through automated checks (and, where automation is not enough, human review), reaches an overall decision, and records it as a durable, auditable outcome that the relying organization acts on.

The defining core is deliberately small:

```text
Subject of record (the claimed identity)
└── Identity evidence captured from the person
    └── Evaluation of the evidence (checks)
        └── Recorded verification outcome returned to the organization
```

Everything else commonly associated with the category — document-authentication engines, liveness detection, workflow builders, risk scores, webhooks, watchlists — makes verification practical at scale but is not what makes a product an identity verification application. Older database-matching and knowledge-based verification products satisfy the same core without document capture or biometrics.

This Type ends where the surrounding programs begin: the compliance case file and monitoring regime of regulated onboarding belong to the KYC/KYB Platform; login and re-authentication of a known user belong to CIAM and Multi-factor Authentication; transaction- and account-level risk belongs to Fraud Prevention.

## Users & Context

Verification applications are unusual in serving two audiences with opposite relationships to the product.

**Organization side — the customer of the product:**

- **Integration engineers** connect the verification flow into their product's onboarding: they create verification attempts through APIs, embed capture SDKs, and consume results via callbacks or webhooks.
- **Compliance and risk operations staff** work the exceptions: they inspect verification records, review cases the automation flagged, and approve, reject, or escalate them.
- **Program administrators** configure how verification runs for their organization: which checks run, which are mandatory, what the end-user flow looks like, and what happens on failure.

**Person side — the subject of verification:**

- The person being verified is a customer, applicant, patient, beneficiary, or contractor of the organization — not a customer of the verification product. They encounter the product only as a capture flow: photograph a document, take a video selfie, enter personal details, wait for a result. In one market variant they hold a standing verified identity and reuse it across organizations.

**Typical contexts:** opening financial accounts, onboarding marketplace sellers and gig workers, accessing government benefits and tax services, age-restricted purchases, healthcare patient matching, workforce entrance, and re-checking identities at high-risk moments.

## Core Model

### The Defining Core

Four structures, jointly held. Removing any one leaves a product that is no longer identity verification:

- **Subject of record.** The person being verified is held as a persistent, individually identified record — called an *applicant* in some products, an *account* in others, a *wallet* in consumer-facing ones. The subject outlives any single attempt: a person who verifies today and re-verifies a year later maps onto the same record, which lets the organization spot inconsistencies across attempts and prevents duplicate submissions. Without a persistent subject there is no record to protect, only anonymous one-shot checks.
- **Evidence capture.** The subject submits evidence of the claimed identity through a capture surface the product operates or embeds: photographs of identity documents, live selfies or short videos, entered personal attributes, answers to knowledge questions. Mature products enforce *live* capture (for example, refusing photos already saved on the device) because the evidentiary value depends on the evidence being produced at verification time.
- **Evidence evaluation.** The captured evidence is tested by checks — automated in the normal path, human where automation is insufficient. Checks assess the evidence along three axes: authenticity (is the document genuine, is the person live), correspondence (does the selfie match the document photo, do the attributes match the document), and corroboration (do the attributes match authoritative data sources). Each check produces its own result.
- **Recorded outcome.** The check results aggregate into an overall decision — verified, not verified, or referred for review — tied to the subject of record and retained as an auditable artifact. The organization consumes this decision to grant or deny the thing being gated.

### Standard Capabilities in Mature Products

These are expected in current products but are layers over the core, not the core:

- **Configurable verification logic.** Which checks run, which are mandatory, and how results combine is customer configuration — visual workflow builders or check-level templates — not hard-coded behavior.
- **A check taxonomy spanning evidence classes.** Document authenticity analysis; biometric face match with liveness; database corroboration against government registries, licensing authorities, or credit-style data sources; watchlist screening; device and network signals; duplicate detection that compares the current capture against prior submissions.
- **Check-level granularity.** Results are reported per check (passed / failed / not applicable), with a distinction between failures that indicate fraud and failures that indicate a quality problem with the submission; some checks are marked required, others advisory.
- **Graduated outcomes and human review.** An intermediate state (needs review) with a review console; risk scores in some products; human escalation paths ranging from a review queue to a live video call with an agent or in-person verification.
- **Programmatic integration.** APIs to create attempts and retrieve results; webhooks or callbacks to push outcomes; dashboards for the business side.
- **Audit artifacts.** Timestamped records of what was captured, which checks ran, what they found, who decided what, and what consent was collected.
- **Attempt mechanics.** Capture-quality validation with retries; incomplete attempts that expire and can be resumed.
- **Re-verification and returning users.** The same substrate powers later identity checks on an existing subject — biometric re-authentication at high-risk moments, periodic re-verification — usually exposed as a separate module from onboarding verification.

### One Structure, Many Implementations

The core is written conceptually; products realize each piece differently:

```text
Concept:  Subject of record
Realized as:  applicant record · linked account · consumer-held wallet

Concept:  Evidence capture
Realized as:  embedded SDK · hosted web flow · API upload · vendor-operated consumer site
            · in-person capture

Concept:  Evidence evaluation
Realized as:  document forensics · biometric matching/liveness · database lookups
            · watchlist screening · knowledge-based questions · human adjudication

Concept:  Recorded outcome
Realized as:  overall decision + per-check results · decision + risk score ·
            verified-identity status in a reusable wallet
```

A reader who has only seen one shape (say, an SDK-based selfie-and-passport flow) should still be able to recognize a database-matching verification API or a human video-call service as the same Type.

## How It Works

### Configure once

Before any verification happens, the organization defines its verification logic: which evidence the subject must provide, which checks run against that evidence, which checks are mandatory, how the capture screens look, and what happens when checks fail. Products expose this as visual workflow builders or check/template configuration.

### The verification loop

```text
Initiate
→ the organization creates an attempt against a subject of record
  (a new subject, or an existing one being re-verified)
→ Capture
→ the person is guided through evidence submission:
  photograph the document (front/back), take a live selfie or video,
  enter personal attributes
→ Evaluate
→ automated checks run: document authenticity, biometric match,
  liveness, database corroboration, watchlists, duplicate detection
→ Decide
→ results aggregate into an outcome:
  · verified → the organization proceeds (opens the account, grants access)
  · not verified → the person is declined, often with a retry path
  · in review → a human inspects the record and decides
→ Return & record
→ the outcome and the per-check detail are delivered
  (API response, webhook, dashboard) and retained for audit
```

The loop is typically asynchronous: capture completes on the person's device, evaluation runs on the vendor's side, and the organization receives the outcome through a callback, webhook, or dashboard rather than a blocking response — completion time varies by product and by workflow.

### The human path

Every sampled product keeps humans in the loop somewhere. Lower-assurance automation flags a submission for review; a reviewer sees the captured evidence, the check findings, and the subject's history, then approves, rejects, or escalates. Consumer-facing verification extends this to scheduled video calls with trained agents, and in some variants to physical presence — because no automated check covers every population, document type, or edge case.

### Re-verification

A subject of record makes later checks cheaper and sharper. The organization can re-run verification on the same subject when risk policy demands it, and products commonly offer a biometric re-authentication mode that compares a fresh capture against the verified identity rather than re-running the full evidence chain. This is the hinge between verification (first proof of a claimed identity) and authentication (subsequent proof that the same person is present) — related surfaces, usually separate modules.

## Interfaces

### Capture flow (the person being verified)

The only surface most subjects ever see. Purpose: collect valid identity evidence from a non-expert user. Typical content: step-by-step instructions, live camera capture for documents and selfies, form fields for personal attributes, quality feedback ("move closer", "glare detected"), and a consent step before data is shared. Primary actions: allow camera access, capture/retake, enter details, submit, authorize sharing.

### Verification dashboard (the organization)

Purpose: visibility into who is being verified and with what result. Typical information: attempts listed by status — in progress, verified, declined, in review (exact labels vary by product) — timestamps, submitted evidence, check results, and risk signals. Primary actions: inspect a record, open a review case, approve or reject, download evidence or audit artifacts.

### Review console / cases

Purpose: let trained staff decide the subset automation cannot. Typical information: the flagged attempt with evidence and check findings side by side, the subject's prior attempts, and review notes. Primary actions: approve, reject, request resubmission, escalate.

### Configuration surface

Purpose: define the organization's verification logic. Typical content: workflow or template editors listing available checks, mandatory vs optional flags, capture screen composition, and failure routing. Primary actions: compose steps, toggle checks, publish configuration versions.

### Integration surface (API, webhooks, SDKs)

Purpose: make verification a component of the organization's own product. Typical shape: an API to create attempts and retrieve results, webhooks for outcome events, capture SDKs or hosted links for the front end. Primary actions: create attempt, attach evidence, fetch results, subscribe to events.

## Important Rules / Behaviors

- **Check results aggregate under configuration.** An overall outcome is computed from individual check results according to which checks the organization marked required. Advisory failures surface information without necessarily blocking; required failures do.
- **Not every failure means fraud.** Products distinguish fraud-indicating failures (document tampering, duplicate face, watchlist hit) from quality failures (blurry photo, unreadable document). The latter normally loop back to capture rather than to a decline.
- **Live evidence is enforced.** Capture flows reject pre-existing images and files because evidence produced at verification time is the entire point; this is why capture is guided, camera-based, and quality-checked before submission.
- **Incomplete attempts expire and can be resumed.** An abandoned capture does not stay open indefinitely; expired attempts can be re-opened rather than forcing the person to start from zero.
- **Human review is a designed state, not an error path.** The "needs review" outcome is a first-class result that the organization's staff must be resourced to work.
- **Consent and data discipline are structural.** Evidence is sensitive personal data: products record what consent was collected, when, and for what sharing. Some products also split delivery: a first callback carries only status-level information, with identity detail pulled separately by the entitled organization.
- **Decisions are auditable.** The retained record — evidence, check findings, decisions, reviewer actions — exists so the organization can demonstrate why a person was verified, which is what regulators, auditors, and appeals require.
- **Prior submissions inform current ones.** Comparing a capture against earlier media from the same organization's corpus (same face seen before, same document re-used with edits) is a standard anti-abuse behavior built on the subject-of-record and corpus of evidence.
- **Verification is not authentication.** The product proves a claimed identity once, at a decision moment; it does not vouch for every subsequent session. Products that offer returning-user biometric checks expose them as a separate capability precisely to keep these two trust questions apart.

## Variants

- **Document-centric** — the government-issued document plus a biometric selfie is the anchor evidence; strongest where document forensics are mature. The default mental image of the category.
- **Data-centric** — personal attributes matched against authoritative databases (licensing authorities, bureaus, government registries), with knowledge-based questions as a fallback; the older electronic form of the Type, still standard in markets with strong data infrastructure, and still offered today as a low-friction path.
- **Hybrid orchestration** — the dominant modern shape: compose document, biometric, and data checks into one configurable flow, often with risk scores grading the outcome.
- **Consumer-held verified identity** — the person verifies once into a standing identity (wallet) and consents to share it with many relying organizations; flips who operates the capture surface from the organization to the verification vendor.
- **High-assurance escalation** — human video-call adjudication and in-person verification networks for populations and documents that automation cannot clear; used by government-benefit and tax contexts.
- **Regulated-onboarding packaging** — verification sold as part of compliance onboarding, bundled with watchlist screening; the verification core is unchanged, but the buyer's language and the check mix are compliance-shaped.
- **Business-entity variant** — the same attempt/evaluate/decide shape applied to companies (registry and footprint checks); overlapping with, but simpler than, the dedicated KYB platform.
- **Geographic coverage as a feature** — since evidence classes and authoritative sources differ by country, coverage breadth is a major competitive axis and shapes which variants an organization can run.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| KYC / KYB Platform | consumes this Type | centers the compliance program: entity case files, relationship risk, screening regimes, enhanced due diligence, ongoing monitoring; identity verification is one evidence step inside it |
| Government Digital Identity | adjacent ecosystem | state-operated identity issuance and federation; not an organization's per-attempt verification decision loop |
| Fraud Prevention Platform | adjacent, shared signals | spans transaction fraud, account takeover, and abuse across the account lifecycle; verification is the onboarding identity-trust moment, with device/fraud signals as context |
| Account Abuse Protection | adjacent | defends existing accounts against abuse; assumes an established identity rather than proving a claimed one |
| Customer Identity / CIAM | adjacent infrastructure | manages the customer identity lifecycle (registration, login, consent) for an organization's own services; verification may be embedded as one step |
| Multi-factor Authentication | different trust question | proves a *known* user is present again; verification proves a *claimed* identity is genuine the first time |
| Background Check Platform | different evidence, same buyer | assembles records about a person's history (criminal, employment) for an HR decision; verification establishes the claimed identity itself |
| Employment Verification Platform | attribute verification | confirms attributes like employment or income through data sources; not a proof of claimed identity |
| Digital Credential Platform | downstream consumer | issues and manages portable credentials; may be fed by a verification outcome but centers credential lifecycle, not evidence adjudication |

The boundary that matters most in practice is with **KYC / KYB Platform**: the same vendor often sells both names. The working distinction is object-model-shaped — if the center of gravity is the verification attempt (subject, evidence, checks, decision), it is this Type; if it is the compliance case and its program machinery, it is KYC/KYB.

## Representative Products

- **Entrust Identity Verification (Onfido)** — document and biometric verification specialist with a workflow orchestration layer; developer-first API/SDK integration.
- **Persona** — flexible multi-type verification platform; template- and workflow-driven, with strong review and re-verification tooling.
- **Jumio** — enterprise identity platform; workflow-execution API with hosted, SDK, and API-only capture options; verification and authentication exposed as distinct products.
- **ID.me** — consumer-facing verification with a reusable verified-identity wallet; government-grade assurance with human video-call and in-person escalation paths.

These four span the main product philosophies: document-centric specialist, configurable platform, enterprise workflow engine, and consumer wallet. A further pole — pure data-orchestration verification APIs matching attributes against global data sources — is part of the market; its documentation was not reachable during research, so it is noted here rather than characterized in detail.

## Sources

Research date: **2026-09-08**

- Entrust (Onfido) Identity Verification documentation portal and getting-started guide — https://documentation.identity.entrust.com/ , https://documentation.identity.entrust.com/getting-started/general-introduction/
- Persona developer documentation (introduction, choosing an integration method, inquiries overview) — https://docs.withpersona.com/docs , https://docs.withpersona.com/docs/choosing-an-integration-method , https://docs.withpersona.com/docs/inquiries
- Persona help center (verification service types index; verification checks) — https://help.withpersona.com/verifications/features/verification-service-types/ , https://help.withpersona.com/articles/5Tc5tsWfBX03AHRkr2vqv2/
- Jumio documentation portal and quickstart (ID + Selfie Verification) — https://docs.jumio.com/ , https://documentation.jumio.ai/docs/quickStart/ID_SelfieVerification
- ID.me help center (identity verification category; self-service verification walkthrough) — https://help.id.me/hc/en-us/categories/8984755179159-Identity-Verification , https://help.id.me/hc/en-us/articles/9198013708439-Verify-your-identity-with-ID-me-Self-Service

> Sourcing limitation: attempts to reach documentation for several additional vendors in the data-orchestration segment failed during the research window (repeated transport errors). Claims in this document are calibrated to the four products whose official documentation was directly examined; precise operational figures (check thresholds, risk-score scales, expiry durations, turnaround times, pricing) are intentionally not stated, and no numeric detail was filled in from other sources.
