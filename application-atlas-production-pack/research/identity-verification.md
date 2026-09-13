# Research Notes — Identity Verification

Research date: 2026-09-08
Methodology: v1.1

## Research Goal

Understand what an Identity Verification application is as an Application Type: the core objects it manages, the end-to-end verification loop, the roles on both sides (the organization that needs trust and the person being verified), the rules that shape behavior, and — critically — where its boundary lies with KYC/KYB Platform, Government Digital Identity, Fraud Prevention Platform, CIAM/MFA, and Background Check Platform, since these neighbors are adjacent in the directory and in the market.

## Initial Boundary

Working hypothesis before research:

- An Identity Verification application is used by an organization to establish that a person is who they claim to be, usually before granting something (an account, a service, a benefit, a purchase). The person submits identity evidence (document, biometric, personal attributes); the product evaluates the evidence and returns a recorded decision.
- Likely adjacent: KYC/KYB Platform (the regulatory compliance program that usually consumes verification), Government Digital Identity (state-run identity ecosystems), Fraud Prevention Platform (broader risk across account lifecycle), CIAM/MFA (authentication of known users rather than first-time verification), Background Check Platform (records about a person's history, not their claimed identity).
- Potential taxonomy risk: this leaf may be an alias of KYC/KYB Platform, since many vendors market the same product to both names. This needs an explicit keep-both test.

## Research Questions

1. What is the subject of verification — how does the product represent the person being verified, and how does it persist across attempts?
2. What is the unit of work — what object represents one verification attempt, and what lifecycle/states does it move through?
3. What evidence types and check types exist across products (documents, biometrics, databases, watchlists, device signals)?
4. How is the verification flow configured (templates, workflow builders, workflow definitions) and by whom?
5. What does the end user experience (hosted flows, SDKs, embedded UIs), and what does the business side experience (dashboards, review queues, APIs, webhooks)?
6. What decisions/outcomes exist, and what happens on failure (retry, manual review, escalation to humans, in-person)?
7. Where is the boundary with KYC/KYB, Government Digital Identity, Fraud Prevention, CIAM/MFA, Background Check?
8. Historical check: would pre-document/pre-biometric era electronic identity verification (database matching, knowledge-based authentication) still fit the definition?

## Representative Products

| Product | Why sampled |
|---|---|
| Onfido (now Entrust Identity Verification) | document + biometric specialist; developer-first API/SDK; workflow orchestration layer |
| Persona | flexible multi-type verification platform; workflow/templates; strong dashboard/case tooling |
| Jumio | enterprise identity platform; workflow-execution API; authentication adjacency explicit in product split |
| ID.me | consumer-facing verification with government-grade assurance; reusable verified identity (wallet); human escalation paths |

Selection intent: document-centric vs multi-type-platform vs enterprise-workflow vs consumer-wallet philosophies; fintech/marketplace/enterprise/government customer tiers.

Attempted and abandoned (source-access limitation): Trulioo docs (docs.trulioo.com — transport error, 2 attempts), Socure docs (docs.socure.com — transport error), Veriff dev portal (dev.veriff.com — transport error). The pure data-orchestration eIDV pole is therefore under-sampled; see Uncertainties.

## Sources

Tier 1 (official developer documentation / help centers), fetched 2026-09-08:

- Entrust (Onfido) Identity Verification Documentation Portal — https://documentation.identity.entrust.com/ ; Getting started overview — https://documentation.identity.entrust.com/getting-started/general-introduction/
- Persona Developer Docs — https://docs.withpersona.com/docs ; Choosing an integration method — https://docs.withpersona.com/docs/choosing-an-integration-method ; Inquiries overview — https://docs.withpersona.com/docs/inquiries
- Persona Help Center — Verification Service Types index — https://help.withpersona.com/verifications/features/verification-service-types/ ; Verification checks — https://help.withpersona.com/articles/5Tc5tsWfBX03AHRkr2vqv2/
- Jumio Documentation Portal — https://docs.jumio.com/ ; Quickstart: ID + Selfie Verification — https://documentation.jumio.ai/docs/quickStart/ID_SelfieVerification
- ID.me Help Center — Identity Verification category — https://help.id.me/hc/en-us/categories/8984755179159-Identity-Verification ; Self-Service verification — https://help.id.me/hc/en-us/articles/9198013708439-Verify-your-identity-with-ID-me-Self-Service

Notes on access: all four primary products yielded official documentation. Jumio's retrieval example (statuses, decisions, capability results) was observed verbatim in the quickstart response sample. Persona's inquiry lifecycle statuses were observed via the docs' lifecycle description (`approved`, `declined`, `needs_review`). Numeric thresholds, SLA/turnaround times, and pricing were deliberately not collected.

## Product A — Onfido (Entrust Identity Verification)

Evidence layer: A (direct observation of official docs).

Key observations:

- Platform described as an "end-to-end identity verification solution … to smoothly and securely onboard customers and grant them access to your services." Suite spans document and biometric verifications, trusted data source verifications, and fraud detection signals.
- **Applicant**: "the representation of an end user, your customer … the individual who will be the subject of an identity verification flow. Creating an applicant is the first step towards initiating a check, and without an applicant a check cannot be completed. Applicants should map one-to-one with your customers." → subject-of-record concept, named.
- **Report**: "a single verification request" — typed checks: Document report (data integrity, visual authenticity, police record), Facial Similarity (Photo / Photo Fully Auto / Video / Motion), Known Faces (likeness against media of previous applicants in the account database — duplicate/repeat-fraud and account-recovery signals), NFC extraction from ePassports, Identity Enhanced (cross-reference against verified databases, "typically used for KYC purposes"), Watchlist (sanctions, PEP, monitored lists, adverse media), Proof of Address, Driver's License Data Verification (US state DMV database check), Device Intelligence, Repeat Attempts (same document reused with modifications).
- **Workflow Studio**: drag-and-drop orchestration for "building, managing and deploying identity verification flows"; workflows are "dynamic end-user verification journeys … made up of interactive and non-interactive tasks to manage the capture, upload and verification of user data."
- **Workflow run**: "individual instances of a workflow to be run against a given applicant" — creating a run begins the end-user verification journey for a designated applicant.
- **Capture SDKs** (iOS/Android/Web/React Native/Flutter): guided capture UI, image quality detection, direct upload; **Smart Capture Link**: fully hosted low/no-code frontend.
- API: create applicants, create/retrieve workflow runs, retrieve signed documents and timeline files (audit artifacts).

## Product B — Persona

Evidence layer: A (direct observation of official docs + help center).

Key observations:

- **Inquiry**: "a single instance of a Persona identity verification flow. Each time an end user goes through your verification flow, the details of that interaction are wrapped in an inquiry object." → unit-of-work concept, named.
- **Inquiry template**: configuration specifying "which screens to show, how to style the UI, which verification types to include, and which verification checks to require." Solutions ship pre-made templates "for common use cases, like KYC and age verification."
- **Account**: "group together all data from a single person or business" — inquiries for the same user linked via a reference ID; "if you require your users to verify during your onboarding (inquiry 1), and re-verify a year later (inquiry 2), you can link the two inquiries to the same account. Accounts help you spot patterns or inconsistencies across inquiries, and prevent users from completing extra, unneeded inquiries." → subject-of-record spanning multiple attempts; re-verification is a first-class concept.
- Integration methods: Hosted Flow (redirect to Persona-hosted page), Embedded Flow (iframe/modal via web SDK), Mobile SDKs (iOS/Android/React Native), and Transactions-based (API-based, for providing your own UI).
- **Verification checks**: "the individual tests run during a Verification. Each check scrutinizes a specific piece of information and returns a passed, failed, or not applicable result." Attributes: status, type (`Fraud` vs `User action required` — fraud signals vs quality problems), and `Required` (must pass for the Inquiry to complete). Configurable per-check in the dashboard.
- **Inquiry lifecycle**: statuses include `approved`, `declined`, `needs_review` (these "contain results for you to use"); sessions expire if not completed in a given time; expired inquiries can be resumed. Events emitted per transition; webhooks (`inquiry.approved`, `inquiry.declined`); results retrievable via dashboard or API.
- Verification service types (15 documented): Government ID Verification, Selfie Verification, AAMVA Verification, Database Verification, TIN Verification, VAT Verification (EU/UK), Document AI, Business Registry Verification, Business Footprint Verification, Business Website Verification, Phone Carrier Verification, Email (2FA) Verification, Phone Number Verification, Brand Asset Verification, Capital One Airkey Verification. → check taxonomy spans person verification, business (KYB-adjacent) verification, and risk signals.
- Platform sections beyond inquiries: Transactions (API-based), **Authentications** (returning-user surface, distinct entry point), Workflows, **Cases** (review tooling), Reports, Relay (claim types), Sentinel (fraud), Connect / Persona Wallet (reusable identity), Risk Scoring app. → verification vs authentication separation visible in product structure; manual review as a named surface.

## Product C — Jumio

Evidence layer: A (direct observation of official docs, including a full sample response).

Key observations:

- Flow (quickstart): obtain OAuth token → **create or update an Account** (`/accounts`, new or existing user) → launch the workflow → wait for callback → retrieve workflow results.
- **Workflow definition** selected by key (e.g. "ID + Selfie + Supporting Data"): "a workflow defines which Jumio services will process your user's credentials." → configuration layer, named.
- **Workflow execution** carries **credentials** with categories `ID | DATA | SELFIE | FACEMAP`, each with allowed capture channels `WEB | API | SDK`.
- Integration options: hosted interface (redirect / iframe / webview at hosted.jumio.com), native SDKs, or custom API upload (front, back, selfie parts + finalization endpoint).
- Callback contains "No PII data/non-sensitive data status info"; full results via retrieval API.
- Sample result structure: top-level workflow `status: PROCESSED`; **decision** with `type: WARNING` and a numeric **risk score**; per-**capability** results — `extraction` (document type, issuing country, name, DOB, expiry, document number), `similarity` (selfie ↔ ID, MATCH), `liveness`, `dataChecks`, `imageChecks` (with face-search findings — repeated-face detection across prior submissions), `usability`. Consent recorded (`obtained`, `obtainedAt`, `collectedBy`).
- Product split in quickstarts: **ID + Selfie Verification** (onboarding verification) vs **selfie.DONE / Authentication** (returning-user authentication) vs **Doc Proof** vs **Standalone Risk Signal** vs **Fastfill**. → the Type boundary (verification vs authentication) is drawn inside the vendor's own product structure.
- Capability pages observed: Advanced Watchlist Screening; government database checks (e.g. Australian DVS: "verify Australian government-issued identity documents against the Australian Document Verification Service (DVS) to confirm identity details"); age-related transaction handling (delete transactions for users below a certain age, via APIs or "Jumio Portal").

## Product D — ID.me

Evidence layer: A (direct observation of official help center).

Key observations:

- Positioning: "ID.me simplifies how individuals prove and share their identity online." Consumer-held **ID.me Wallet**; verified identity reused across organizations ("Sign in to your existing ID.me Wallet or create a new wallet" during verification at a government agency or business).
- Self-Service verification flow (end user): start at the relying organization's site → ID.me button → sign in / create wallet → MFA → consent to share → **take a photo of a government-issued photo ID** (live camera only — "Photos or files already saved on your device can't be used"), **video selfie** ("helps confirm your photo matches your ID"), **enter personal info** (phone, SSN, address; SSN card photo may be requested) → review and authorize sharing with the organization.
- **Escalation paths when self-service fails**: short video call, extended video call (with human agents, schedulable appointments), KBA-R (knowledge-based authentication variant), in-person verification "at a retail location near you", plus document-specific paths (non-US passport, ITIN).
- Relying-party base observed in help center: federal agencies (IRS, SSA, VA, Treasury, USPTO, FBI, HHS…), state benefits programs (per-state sections), employment/background-check integrations (Sterling, Indeed), healthcare (patient verification, e-prescribing), hospitality, financial.
- **Community Verification** is a separate category (military, nurse, teacher, student…) — verifying group affiliation, distinct from identity verification in the product's own taxonomy.

## Cross-product Comparison

| Structure | Entrust/Onfido | Persona | Jumio | ID.me | Reading |
|---|---|---|---|---|---|
| Subject of verification | Applicant (1:1 with customer) | Account (linked inquiries via reference ID) | Account (new or existing user) | ID.me Wallet (user-held, reused across orgs) | A persistent representation of the person being verified — B commonality |
| Unit of work | Workflow run (+ individual Reports) | Inquiry | Workflow execution | Verification performed into the wallet | One captured attempt with a recorded outcome — B commonality |
| Configuration layer | Workflow Studio workflows | Inquiry / Verification templates | Workflow definitions (keys) | Product-defined method paths | Verification logic is customer-configurable, not hard-coded — B commonality |
| Capture surface | Smart Capture SDKs; Smart Capture Link (hosted) | Hosted / Embedded / Mobile SDK / API | Hosted / SDK / API parts | Vendor-operated web+mobile flow | Embedded capture UI is standard; ownership varies — B commonality |
| Check types | Document, Facial Similarity, NFC, Known Faces, Identity Enhanced (database), Watchlist, PoA, DLDV, Device Intelligence, Repeat Attempts | Government ID, Selfie, AAMVA, Database, TIN/VAT, Document AI, Business registry/footprint/website, Phone/Email, Brand asset | Extraction, Similarity, Liveness, Data checks, Image checks (repeated face), Watchlist, Gov DB (AU DVS) | ID document + video selfie + SSN/personal data; KBA-R; video call; in-person | Checks cluster into: document authenticity, biometric match/liveness, authoritative-database corroboration, watchlists, fraud/duplicate signals — B commonality; exact menus differ (A per product) |
| Check granularity | Reports with sub-checks | Checks with passed/failed/not-applicable + required flag | Capabilities/steps each with decision | Step-wise human process | Results are check-level, aggregated into an overall decision — B commonality |
| Outcomes | Report results; run outcome | approved / declined / needs_review | decision PASSED/WARNING + risk score; capability decisions | verified / not verified (+ escalation) | Decision states incl. an intermediate human-review state — B commonality (names vary) |
| Result delivery | API retrieve; SDK; timeline files | Dashboard, API, webhooks, events | Callback (no PII) + retrieval API | Consent-based sharing to relying org | Programmatic delivery + human dashboard — B commonality |
| Manual review / escalation | Dashboard; timeline files | needs_review + Cases | Portal; WARNING state | Human video call, in-person | A human path exists in every product — B commonality |
| Reuse / repeat | Known Faces; biometric authentication (ATO); Repeat Attempts | Re-verification on same Account; Authentications; Connect/Wallet | Existing-user accounts; selfie.DONE authentication | Wallet re-verified identity shared with orgs | Re-verification / returning-user authentication built on the same substrate — B commonality |
| KYC adjacency | Identity Enhanced "typically used for KYC"; Watchlist | Pre-made "KYC Solution" templates | Watchlist screening; gov DB checks | IRS/SSA/federal use | KYC is a use case packaged on top of verification, not the object model itself — B commonality |

Product-specific structural details (do not generalize): workflow-run/report split (Entrust), inquiry-template versioning and claim-type relay (Persona), credential categories `ID|DATA|SELFIE|FACEMAP` and numeric risk score in the sample response (Jumio), wallet + retail in-person network + KBA-R (ID.me).

## Level 0 — Defining Invariant

The smallest structure without which the product stops being recognizable as an Identity Verification application:

1. **A claimed identity as the subject of record** — a specific person (held as a persistent, identified record — applicant / account / wallet) presents themselves to be verified on behalf of a relying organization. Remove → an ID-scanning or document-capture tool with no relying party and nothing at stake.
2. **Identity evidence capture** — the person submits evidence of their claimed identity (documents, biometrics, personal attributes) through a capture surface operated or embedded by the product. Remove → a form/survey tool.
3. **Evidence evaluation** — checks assess the evidence's authenticity, correspondence, and consistency (against the claim, against each other, and/or against authoritative data), producing check-level results. Remove → document storage / data collection.
4. **A recorded verification outcome** — an overall decision (verified / not verified / needs review) tied to the subject of record, retained and returned to the relying organization. Remove → an advisory scoring opinion with no recorded decision, or a raw data feed.

Jointly-held test: 1 alone = a customer record; 2 alone = a document upload form; 3 alone = a checking algorithm with no subject or capture; 4 alone = a decision log; 2+3 without 1+4 = a stateless checking function; 1+4 without 2+3 = an asserted status with no evidence trail. All four are load-bearing.

Deliberately NOT in the definition (checked against the historical sample):

- Document capture and biometrics specifically — pre-document-era electronic identity verification matched personal attributes (name/SSN/address) against databases and used knowledge-based questions; ID.me still offers KBA-R and human video calls today. The invariant is *evidence evaluation*, not any specific evidence class.
- Government-ID documents, liveness detection, watchlists, device signals, risk scores — L1/L2.
- APIs, SDKs, hosted flows, workflow builders — implementation of capture/integration, not the invariant.
- KYC/AML compliance framing — one context of use, not the definition (age gating, marketplace onboarding, benefits access, healthcare verification all satisfy the core without it).

## Level 1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- Capture experience layer: hosted flow, embedded widget, native mobile SDK, API-only — mature products typically offer more than one.
- Document authenticity analysis and biometric face match with liveness as the flagship check pair (3/4 sampled products; ID.me's self-service path also centers them).
- Authoritative-data corroboration: government/DMV database checks, bureau/database verification (Entrust DLDV + Identity Enhanced; Persona AAMVA + Database; Jumio gov-DB checks).
- Check-level configuration: enable/disable checks, mark required vs optional (Persona explicitly; Entrust/Jumio via workflow composition).
- Configuration surface: visual workflow/template builders (Entrust Workflow Studio, Persona Flow Editor, Jumio workflow definitions).
- Decision plumbing: overall decision + per-check/per-capability results; risk scores in some products (Jumio sample; Persona Risk Scoring app).
- Manual review path: intermediate review state (Persona `needs_review`, Jumio `WARNING`, ID.me human video call) and dashboard/case tooling.
- Programmatic integration: REST APIs, webhooks/events, callbacks (Persona, Jumio, Entrust).
- Audit artifacts: timeline files (Entrust), retrieval records (Jumio), inquiry/account history (Persona), consent records (Jumio, ID.me).
- Retry/expiry: capture failures retried; incomplete attempts expire and can be resumed (Persona documented; ID.me troubleshooting surfaces the same reality).
- Fraud cross-checks: duplicate-face / repeat-document detection against the vendor's or customer's prior corpus (Entrust Known Faces + Repeat Attempts; Jumio repeated-face findings; Persona fraud-type checks).

## Level 2 — Variant / Optional Structure

- Evidence philosophy: document-centric (document+biometric as the anchor) vs data-centric (attribute matching against authoritative databases) vs hybrid; geography determines data-source availability.
- Who operates the surface: customer-embedded (SDK/iframe), vendor-hosted, or vendor-owned consumer property (ID.me wallet; Entrust Smart Capture Link as hosted middle ground).
- Regulatory context: KYC/AML-shaped deployments (regulated onboarding) vs commercial trust contexts (age gating, marketplace seller onboarding, gig-driver onboarding, benefits eligibility, healthcare patient matching).
- Assurance escalation: automated-only vs human-in-the-loop (video call with an agent) vs physical presence (retail in-person network).
- Reusable verified identity: verification as a one-shot service vs issuance of a standing verified identity reused across relying parties (wallet models).
- Subject class: persons only vs extending to businesses (Persona business registry/footprint/website verification types — KYB-adjacent variant).
- Returning-user surface: re-verification and biometric authentication modules built on the same substrate (present in 4/4 sampled products as separate named surfaces).

## Level 3 — Vendor-specific Structure

(Research Notes only — not for the final document)

- Entrust/Onfido: Workflow Studio, Smart Capture Link, workflow-run/report object split, signed documents + timeline files retrieval, specific report names (Known Faces, Repeat Attempts, Identity Enhanced, DLDV).
- Persona: inquiry-template ID/version model, reference-ID account linking, Transactions-based integration tier, Relay claim types, Sentinel, Cases, Capital One Airkey Verification, pre-configured Solutions ("KYC", age verification).
- Jumio: workflow-definition keys, credential categories (ID/DATA/SELFIE/FACEMAP), facemap + numbered liveness classifiers, callback-then-retrieval two-step with no-PII callback, hosted.jumio.com, regional endpoint shards, numeric risk score in sample, product names (selfie.DONE, Doc Proof, Fastfill).
- ID.me: ID.me Wallet, MFA-protected wallet, short/extended video call appointments, KBA-R, retail in-person verification network, Community Verification (affiliation, adjacent), per-agency help sections.

## Vendor-specific Findings

- Entrust's Known Faces and Jumio's repeated-face findings both compare current capture against prior media — a shared idea (corpus-based duplicate detection) realized in product-specific ways; treated as L1, with naming/shape vendor-specific.
- Persona's check taxonomy explicitly includes business-entity verification types; no other sampled product centers this in its person-verification docs. Held as variant evidence, not Type structure.
- ID.me's wallet model makes the *relying organization* choose the surface ("select the ID.me button" at the org's site) — inverse of the API products, where the customer embeds the vendor. Same four-part core; different ownership of the capture surface.

## Rejected Findings

- "Identity Verification = KYC" — rejected. KYC is a packaged use case (Persona's pre-made KYC Solution; Entrust's Identity Enhanced "typically used for KYC"). The object model (subject, attempt, checks, decision) never references a compliance case file, screening program, or ongoing monitoring; those belong to the KYC/KYB Type.
- "Verification requires a government-ID document + selfie" — rejected. KBA-R and human video-call verification (ID.me), database verification (Persona Database/AAMVA, Entrust Identity Enhanced), and the historical database/KBA era satisfy the core without document capture.
- "Decision = binary pass/fail" — rejected. A distinct needs-review/escalation state and human path exist in every sampled product; risk scores introduce graded outcomes.
- "The end user is the customer" — rejected for the Type. In API-based products the customer is the organization; the verified person is the subject. ID.me inverts this (consumer-held wallet), showing the relationship varies while the core holds.
- Numeric specifics (risk-score scales, expiry durations, retry counts, turnaround times) — not asserted; either absent from reached docs or product-sample-specific.

## Boundary Findings

- **vs KYC/KYB Platform** — the most important seam. Verification centers the *act*: subject + evidence + checks + decision. KYC/KYB centers the *compliance program*: the entity's case file, risk classification of the relationship, sanctions/PEP screening programs, enhanced due diligence, ongoing monitoring, regulator-facing records. Evidence from this side: Persona packages KYC as a template solution over inquiries; Entrust frames Identity Enhanced as "typically used for KYC purposes" — a check *inside* verification serving a program *outside* it. Remove the program/case/monitoring structures and what remains is exactly this Type; remove the verification act and the KYC platform has no identity evidence layer. Keep both Types.
- **vs Government Digital Identity** — government-operated identity ecosystems (issuance, federation, national wallets). Identity Verification is operated by/for an organization that needs a decision about a person. ID.me sits between (private operator, government relying parties) and still satisfies this Type's core; a state-run identity provider is issuance/federation, not a per-attempt verification decision loop.
- **vs Fraud Prevention Platform** — fraud platforms span the account lifecycle (transaction fraud, account takeover, bot/abuse). Verification is the onboarding identity-trust act; device intelligence and duplicate detection are shared signals sold inside verification as context for the identity decision. Where decisioning becomes continuous, transaction-level risk → Fraud Detection Platform.
- **vs Account Abuse Protection / CIAM / MFA** — authentication asks "is this the same person who registered?"; verification asks "is this person who they claim to be?" Products mark the seam themselves: Jumio splits quickstarts (ID + Selfie Verification vs Authentication), Persona has separate Authentications and Inquiries entry points, Entrust separates Account Opening from Account Takeover Prevention. Re-verification and biometric authentication modules are adjacent capabilities built on the same substrate.
- **vs Background Check Platform** — background checks assemble records about a person's history (criminal, employment, education) for an HR decision; verification establishes that the claimed identity is genuine. The seam is visible in-market: ID.me's help center treats First Advantage (background checks) as a separate relying-party integration. Employment Verification Platform similarly verifies *attributes* (employment/income) via data sources, not claimed identity.
- **"Remove what?" tests** — remove the relying organization and recorded decision → personal ID-scanning/wallet utility; remove evidence evaluation → document collection; remove the persistent subject → stateless checking function; replace per-attempt decisions with continuous session/transaction risk → fraud detection; replace first-time verification with returning-user login → CIAM/MFA.

## Uncertainties

- **Data-orchestration-only pole under-sampled**: Trulioo, Socure, and Veriff docs were unreachable (transport errors, 2 attempts each within policy). The database-centric philosophy is evidenced indirectly (Entrust Identity Enhanced/DLDV, Persona Database/AAMVA types, Jumio gov-DB checks) but not by a pure-play vendor's own docs. The L0 deliberately does not depend on this pole.
- **Manual review console depth**: observed as named states/surfaces (needs_review, Cases, WARNING, human video calls) but review-queue internals (assignment, SLAs, sampling) were not researched and are not characterized.
- **Business (KYB) verification within this Type**: Persona documents business verification service types; the directory's separate KYB leaf owns the entity-compliance program. The overlap was held as a variant note rather than resolved into the definition.
- **Turnaround/latency characteristics, pricing, coverage claims**: deliberately not collected; no precise figures asserted anywhere.

## Final Synthesis

An Identity Verification application is an organization-side system of record for establishing that a specific person is who they claim to be. Its defining core is four jointly-held structures: a persistent subject of record carrying the claimed identity (applicant/account/wallet); a capture surface through which that person submits identity evidence; an evaluation layer of checks that test the evidence's authenticity, correspondence, and consistency and return check-level results; and a recorded overall decision (verified / not verified / in review) tied to the subject and returned to the relying organization. The evidence classes (documents, biometrics, database attributes, knowledge-based answers, human adjudication) are variant choices, not the invariant — pre-biometric electronic verification and today's human video-call paths satisfy the same core. Mature products wrap this core in configuration surfaces (templates/workflow builders), programmatic delivery (APIs/webhooks/dashboards), audit trails, retry/resume mechanics, fraud cross-checks against prior submissions, and a re-verification/authentication layer for returning users. KYC/AML is the largest context of use, packaged on top of the verification act, not the act itself — the KYC/KYB Platform remains a separate Type centered on the compliance program.
