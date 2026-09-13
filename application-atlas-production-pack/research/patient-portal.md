# Research Notes — Patient Portal

## Research Goal

Understand what a Patient Portal actually is as an Application Type: what the patient's account is, what the patient can see and do inside it, how it relates to the record system the care organization runs, who initiates the interaction, and where its boundary lies against the Patient Engagement Platform, the EHR, the generic customer-portal family, and the personal-health-record concept.

## Initial Boundary

Working hypothesis before research:

- Core use: an authenticated web/mobile surface where a patient views the health information their care organization holds about them and performs self-service transactions (message the care team, request prescriptions, book/manage appointments, complete forms, pay bills).
- Primary users: the patient (and proxies/caregivers acting for another patient); staff on the organization side answer and process what comes in.
- Nearest neighbor Types: Patient Engagement Platform (processed sibling), EHR (record owner), Patient Scheduling, Telehealth Platform, Patient Registration & Intake, Remote Patient Monitoring, Customer Portal (generic analog, processed), Health Information Exchange (processed).
- Likely confusions: portal vs engagement (who initiates); portal vs EHR module (packaging); portal vs PHR (who holds the record); portal vs payer/member portals (naming blur flagged by the member-portal pass).

Known unknowns at start: whether the record-view leg or the transaction leg is definitional; whether payments/refills are definitional or market machinery; how the US EHR-embedded pole behaves versus national/regional poles.

## Research Questions

1. What does the patient's account consist of, and how is it established and verified?
2. What exactly can the patient see — whose record is being presented, and what governs visibility?
3. What can the patient initiate, and what happens to what they submit?
4. What does the organization side do (staff answering, configuration, credential issuance)?
5. How does proxy/carer access work?
6. How does the portal relate to the EHR/system of record — window, module, or record holder?
7. What varies by market/geography (payments, refills, self-booking, record scope)?
8. What would older, thinner, or non-US products still have to satisfy to be recognizably a patient portal?

## Representative Products

Chosen for market-representation spread across the main realizations (national/regional health-service portal, standalone multi-organization record platform, open-source EHR-embedded module) and documentation availability. US enterprise EHR-embedded poles (Epic MyChart, Oracle Health, athenahealth) were targeted but unreachable from this environment (see Sources / Uncertainties) — the EHR-embedded variant is evidenced indirectly (OpenEMR module pattern, MEDITECH family naming, cross-pass notes).

1. **NHS App** (NHS England) — national health-service patient portal; strong Tier-1 user documentation (nhs.uk).
2. **Patients Know Best (PKB)** — standalone patient-facing record platform aggregating feeds from multiple care organizations; self-labels "Personal Health Record"; official capabilities page and public manual; also delivered inside the NHS App for hospital-ordered results (NHS App docs name it).
3. **OpenEMR Patient Portal** (open-source project) — EHR-embedded portal module; official project wiki (features page + dedicated Patient Portal page) with operational detail unusual for the Type: credential issuance, gating flags, staff-side handling.
4. **MEDITECH** (boundary evidence only, not a portal sample) — Expanse Patient Connect is the engagement/communication layer; its own pages document driving "MyHealth portal enrollment" and pushing portal notifications by SMS — confirming the portal as a distinct product (MyHealth) inside the EHR family and corroborating the engagement↔portal seam from the vendor's own marketing.

## Sources

Research date: **2026-09-08**

- NHS App — https://www.nhs.uk/nhs-app/ ; help index https://www.nhs.uk/nhs-app/help/ ; setting up / getting full access https://www.nhs.uk/nhs-app/setting-up/get-full-access/ ; viewing test results https://www.nhs.uk/nhs-app/help/test-results/ ; family and carer access https://www.nhs.uk/nhs-app/help/profile/family-and-carer-access/ (all fetched 2026-09-08)
- Patients Know Best — https://www.patientsknowbest.com/ (platform overview); capabilities page https://patientsknowbest.com/capabilities/ (fetched 2026-09-08); public manual linked at manual.patientsknowbest.com (not deep-fetched)
- OpenEMR — Features page https://www.open-emr.org/wiki/index.php/OpenEMR_Features (Patient Portal section); dedicated page https://www.open-emr.org/wiki/index.php/Patient_Portal (both fetched 2026-09-08)
- MEDITECH — Expanse Patient Connect https://ehr.meditech.com/ehr-solutions/expanse-patient-connect (fetched 2026-09-08)
- Cross-pass evidence (prior passes in this repo): applications/patient-engagement-platform.md (who-initiates discriminator; portal-provisioning as campaign category; bundle/family split), STATUS.md EHR pass line (portal held as L2 of EHR), HIE pass flag (patient-facing aggregate → portal territory), customer-portal pass (generic self-service-account core), member-portal pass (<relationship>-portal family note), electronic-prescribing pass (patient refill ordering outside prescriber-side Type).

Failed fetches (not retried after failure per network rules): mychart.com (403), epic.com/software/patient-engagement/mychart/ (403), athenahealth.com patient-portal (403), oracle.com/health/patient-engagement/ and /patient-portal/ (404 ×2), veradigm.com/patient-engagement/ (403), followmyhealth.com (transport error; second attempt returned sign-in shell only — no content), nextgen.com patient-portal (404), 1177.se/en/ (403), meditech.com patient-and-consumer-health-portal path (404; superseded by Expanse Patient Connect page).

## Product Observations

### NHS App (national health-service portal, UK)

Evidence layer: A (direct, Tier-1).

- **Identity gate with levels.** Setup requires proving who you are (photo ID or GP online-registration details). Without proof ("part access") the app offers only general services (NHS 111 online, service finder); with full access: request repeat prescriptions, book/cancel GP appointments, see appointment dates/times, see test results, view health record content. A notice on the home screen prompts unverified users to prove identity.
- **Own-record presentation, scoped.** Health conditions and allergies, test results, vaccinations, documents (e.g., GP surgery letters), care plans, NHS number, contact details. Hospital-care information may not be available; hospital-ordered test results appear "through the Patients Know Best service" — i.e., a national portal can surface other systems' content. Recently changed GP surgery → information may not transfer.
- **Organization-side configuration is explicit.** "Your GP surgery can choose to switch off a service, such as booking an appointment, or hide sensitive information." Feature availability depends on the GP surgery and the system it uses.
- **Test-results release governance.** Results are reviewed by a healthcare professional and usually available within a few days (complex tests longer); "Your healthcare professional should wait to release a test result in the NHS App if they need to discuss it with you first"; patients may see results not yet discussed with them; a patient can ask for portal access or specific results hidden; historic results (pre-October 2023) may not appear automatically; releases may be withheld if releasing would cause serious harm or identify a non-consenting third party; results cannot be downloaded from the app; optional trend graph requires the same test done at least twice within 3 years with a reference range and is per-surgery.
- **Patient-initiated transactions.** Request repeat prescriptions; book or cancel GP appointments; request a fit note; messages inbox from the GP surgery; record symptoms; organ-donation and data-sharing preferences; contact-detail changes.
- **Proxy / carer access.** Family and carer access ("linked profile", "proxy access") set up by the GP surgery with ID and appropriateness checks, safeguarding and consent; level-of-access tiers (book appointments for the person, manage their repeat prescriptions, see their results/health information); "Acting for" banner with profile switching; GP can change or remove access; age-banded rules (before 11 parents usually control; 11–16 surgery-approved parental access; ends at 16; own access from 13 in England).
- **Support machinery.** Medical-abbreviation explainer for lay users; notification settings; login/security settings; prominent urgent-help routing (111 online / mental-health urgent help) alongside the non-urgent portal.

### Patients Know Best (standalone multi-organization record platform)

Evidence layer: A (direct, Tier-2 official pages).

- **Self-positioning straddle.** "World's largest Personal Health Record (PHR) platform"; also "Our portal solution provides digital tools to bridge the gap between patients and clinicians"; product surface named "Patient Engagement Portal (PEP)". Functionally: a patient-facing record platform fed by care organizations — useful boundary specimen for portal-vs-PHR naming blur.
- **Record aggregation as the center.** "Aggregate multiple data feeds from healthcare providers and patient-generated sources into a unified record for both patients and clinicians." Data feeds listed: diagnoses/problems, test results & imaging "(with optional delay filters)", medications, appointments, vaccinations, documents, care plans, allergies. Integration agnostic (FHIR/HL7) with any EPR, app, or device.
- **Patient-initiated actions.** Exchange secure messages with professionals (attachments supported); view, reschedule, or cancel appointments; complete SNOMED-coded questionnaires with branching logic and automated scoring (PROMs and clinical data), triggered by patient, professional, or API; add own information; connect wearable devices; track symptoms/trends.
- **Patient-controlled sharing.** "Enable patients to securely control access to and share their records with family, carers, or the VCFSE sector" — sharing with other professionals as well; patient consent gates research matching (no data leaves the platform until the patient engages; research banner in the record; explicit consent before the researching organization can see the record).
- **Care-plan co-production.** Co-created and co-edited care plans by anyone with access to the patient's record; RAG-status interactive plans with automated triggers for clinical intervention; education/resource library in the record.
- **National-infrastructure integration.** Integrations with NHS login, the NHS England App, the NHS Wales App, DigID, and MedMij as part of the Dutch national PGO programme — the portal as a login-anchored surface over national identity infrastructure.
- **Economics.** "Free and always will be... paid for by organisations such as your hospital, health board or local practice." Available on web, mobile, and inside the NHS App.

### OpenEMR Patient Portal (open-source EHR-embedded module)

Evidence layer: A (direct, Tier-1 project documentation).

- **Module of the EHR.** Two documented architectures: (a) Native Onsite Patient Portal served from the same site as OpenEMR; (b) CMS Portal — a WordPress patient interface talking to OpenEMR over its APIs, chosen for security isolation ("a compromise of the public portal is not a compromise of OpenEMR"; all connections initiated by the EMR; patient data on the CMS "transient and kept to a bare minimum").
- **Credential machinery is organization-side.** A per-patient demographic flag ("Allow Patient Portal") authorizes portal use; staff create/reset portal credentials from the patient summary screen; credentials are emailed (and printable); the patient is forced to set a new password on first login or after reset. A physician-side "Portal Dashboard" exists for staff to work with portal activity.
- **Patient-facing capability set** (features page, Patient Portal section): scheduling and appointments; secure messaging and chat; online payments; sending records via Direct messaging; customized forms; new-patient registration; CCDA support; reports; labs; medical problems; medications; allergies; appointments; "Secure API that Supports Third Party Patient Portals".
- **Flows back to the record, staff-reviewed.** CMS-portal documentation: patients submit demographics, history, insurance; upload images/documents stored in OpenEMR; fill clinical forms mapped to EHR layout-based forms; "Easy user interfaces in OpenEMR for reviewing, correcting and storing data from the portal"; "the doctor may choose to copy lab reports to the patient as they are e-signed" — a direct organization-side statement of the release-after-review rule.
- **Historical depth.** Portal documented since OpenEMR 4.1.x (CMS portal) and 5.0.1 (native portal) — an older-generation, self-hosted, no-app realization; language selection at login via the EHR's translation engine.

### MEDITECH (boundary evidence, not a portal sample)

Evidence layer: A (direct, Tier-2) — but the product observed is the engagement layer, not the portal.

- Expanse Patient Connect is "our real-time, automated communication solution": bi-directional SMS, appointment reminders, confirmations/cancellations flowing back into Expanse, outreach campaigns, surveys, pre/post-appointment instructions, AI assistants.
- Patient-side benefits listed include "MyHealth portal enrollment", "bill pay, and notifications"; organization benefits include "Automatically send patients all portal notifications — such as new results and post-visit instructions — as text messages" and "Drive portal adoption by providing a direct launch from text messages, including links that feed patient intake/appointment workflows."
- Reading: the vendor family separates the portal (MyHealth — the patient's window/transaction surface) from the engagement layer (Patient Connect — provider-initiated outreach that recruits patients into the portal). Corroborates both the Type separation and the bundle pattern.

## Cross-product Comparison

| Structure / capability | NHS App | PKB | OpenEMR portal | MEDITECH (boundary) |
|---|---|---|---|---|
| Authenticated patient identity with the care context | Yes — identity proofing gates full access | Yes — registration; national IdP integrations | Yes — staff-issued credentials + demographic flag, forced password change | (engagement layer has no patient login) |
| Presentation of the organization-held record about the patient | Yes — GP-record scoped; hospital content via PKB | Yes — aggregated multi-provider feeds | Yes — labs, problems, medications, allergies, CCDA, documents | Portal notifications reference "new results" (portal itself unsampled) |
| Patient-initiated transactions into org workflow | Yes — prescriptions, appointments, fit notes, messages, preferences | Yes — messages, reschedule/cancel, questionnaires, adding data, sharing decisions | Yes — messages, forms, registration, payments, uploads | — |
| Secure messaging with the care side | Yes — messages inbox (GP surgery) | Yes — with professionals, attachments | Yes — messaging & chat, attachments | SMS two-way is the engagement layer's own channel |
| Results visibility governance | Yes — review/release, withhold rules, per-surgery hiding | Yes — "optional delay filters" on results/imaging | Yes — lab reports copied to patient as e-signed | Portal notifications announce new results |
| Appointment self-service | Yes — book/cancel GP appointments (scope varies by surgery) | Yes — view/reschedule/cancel across providers | Yes — scheduling and appointments | Reminders/confirmations are the engagement layer |
| Prescription requests | Yes — repeat prescriptions | Not documented on reachable pages | Portal lists prescriptions/medications views; refill request not itemized | — |
| Payments | No (NHS care is free at point of use; no billing surface documented) | Not documented | Yes — online payments | Bill pay named in engagement layer's patient benefits |
| Proxy / carer access | Yes — surgery-managed, tiered, age-banded | Yes — patient-controlled sharing with family/carers/professionals | Not documented | — |
| Patient-generated data / devices | Symptom recording; data-sharing preferences | Yes — wearables, symptom tracking, diaries | Patient document/image upload | — |
| Organization-side configuration of what patients see/do | Yes — switch off services, hide sensitive information | Yes — feeds, filters, questionnaires configured | Yes — credential flags, forms mapping, global toggles | Campaigns configure outreach, not the portal |
| Packaging | National infrastructure (app + web) | Standalone platform, multi-provider, embeddable in NHS App | EHR module (native or CMS-fronted) | EHR family sibling product |
| Who initiates the interaction | Patient logs in and acts | Patient logs in and acts | Patient logs in and acts | Provider initiates (engagement) |

## Abstraction (research layers)

### L0 — Defining Invariant (minimal)

Three jointly-held structures; removing any one stops the product being recognizable as a Patient Portal:

1. **The patient's authenticated identity with the care context.** Access is identity-gated: a login/credential path that is verified against, or issued by, the care organization's patient records — never anonymous. The account maps to an identified patient (or to a proxy acting for one).
2. **The patient's own window onto the organization-held health record.** A scoped, read-mostly presentation of the clinical information that care organization(s) hold about that patient — at minimum results, medications, problems/allergies, appointments, documents — with visibility governed by release rules and organization configuration. The portal presents the record; it is not itself the record of record.
3. **Patient-initiated self-service transactions into the organization's care workflows.** The patient starts the work: secure messages to the care team, prescription/refill and appointment requests, forms/questionnaires, payments — submissions that enter staff/clinical queues or systems for action and closure.

Load-bearing combos:
- 1+2 without 3 = read-only results/statement delivery viewer
- 1+3 without 2 = generic self-service account app (the customer-portal shape, no health record)
- 2+3 without 1 = anonymous public services / general health website

### L1 — Common Mature Structure

- Secure messaging as the standing patient↔care-team channel (universal in the reachable sample)
- Results viewing with history/trend presentation (trend graphs common, not universal)
- Appointment visibility and self-service (view universal; booking/cancelling common, scope varies)
- Prescription/refill requests (directly evidenced in NHS; assumed common in US-market products but not directly documented in the reachable sample beyond NHS)
- Documents, immunizations, visit summaries, education content
- Forms/questionnaires completed by the patient (intake-style and clinical)
- Notifications (email/SMS/push) drawing the patient back in
- Proxy/carer access with governed levels (evidenced in NHS + PKB; not confirmed in OpenEMR docs)
- Enrollment machinery: self-signup with verification or organization-issued credentials/activation
- Multiple languages / accessibility support

### L2 — Variant / Optional Structure

- Packaging: EHR-embedded module (dominant US pattern), standalone multi-organization platform, national/regional health-service infrastructure, thin self-hosted module
- Scope of the presented record: one organization vs aggregated across providers vs one national GP record (hospital content optional)
- Transaction breadth: payments (US-market common; absent in NHS pole), refill requests, self-booking breadth, fit-note/admin requests
- Identity substrate: national identity infrastructure (NHS login, DigID, MedMij), organization-issued credentials, activation codes, social/app accounts — implementation, not invariant
- Patient-generated data: devices/wearables, symptom diaries, patient uploads (PKB deep; OpenEMR uploads; NHS light)
- Research/PROM programs, care-plan co-production, RAG self-monitoring plans (PKB depth)
- Inpatient/bedside portal variants; payer/member portals (adjacent family, different record content)
- AI-assisted responses, chatbots (engagement-layer overlap)

### L3 — Vendor-specific (research notes only)

- NHS App specifics: "Acting for" banner; pre-October-2023 historic-results caveat; serious-harm/third-party withholding rules; trend-graph conditions (same test ≥2× in 3 years with reference range, per-surgery); fit notes; organ-donation and national data-sharing preferences; abbreviation explainer; hospital results delivered via PKB.
- PKB specifics: SNOMED-coded questionnaire builder with scoring; 10GB-per-message attachment claim; RAG care plans; Population Health Management Engine research matching; "free to patients, paid by organizations"; self-label as PHR/PEP.
- OpenEMR specifics: CMS/WordPress portal architecture with EMR-initiated-only connections and transient CMS data; "Allow Patient Portal" demographic flag; Portal Dashboard staff GUI; translation-engine language selection.
- MEDITECH specifics: MyHealth portal name; Patient Connect SMS enrollment links; portal notifications as texts.

### Rejected findings (observed somewhere, rejected as definitional)

- **"The portal is an app"** — NHS App also runs as a web login; OpenEMR is web; app delivery is packaging.
- **"The portal includes payments"** — the NHS pole has no billing surface; payments are market machinery.
- **"The portal is an EHR module"** — PKB and NHS App stand outside any single EHR; EHR-embedded is the dominant packaging, not the Type.
- **"The portal serves one organization"** — PKB aggregates many; NHS App composes GP + hospital content; single-org is the common scope, not the invariant.
- **"The portal is where patients enter their own clinical data"** — patient-generated data is an extension (PKB); the record presented is organization-held in all sampled products.
- **"Proxy access is universal"** — evidenced in two products; not confirmed in OpenEMR docs; held common-mature, not defining.
- **"Refills are definitional"** — direct in NHS; not itemized in the other reachable samples; held common with qualification.

## Boundary Findings

- **Patient Engagement Platform** (processed sibling): the seam is who initiates. The portal waits for the patient (login, view, act); the engagement platform goes to the patient (outreach, campaigns, journeys) and manages the response loop in staff queues. The engagement pass already held "remove provider initiation → Patient Portal territory" and documented portal-provisioning as one of its campaign categories; this pass corroborates from the portal side (NHS/PKB/OpenEMR portals are all patient-initiated surfaces) and adds the vendor's own family split (MEDITECH MyHealth vs Patient Connect: the engagement product exists to drive portal enrollment and announce portal content). The two are frequently bundled in one vendor family; bundle ≠ same Type. No joint review needed — the seam is held identically from both sides.
- **EHR** (processed): the portal is a window, not the record of record — the EHR owns the clinical record and the portal presents it and shuttles transactions back. The EHR pass itself held the portal at capability level (L2) of the EHR; this pass holds the surface side as a Type. EHR-embedded portal is the dominant packaging variant; standalone (PKB) and national (NHS App) realizations prove the Type survives without an EHR of its own.
- **Customer Portal / the <relationship>-portal family** (customer-portal and member-portal passes): the same self-service grammar (authenticated external stakeholder, own-records visibility, self-service actions, organization-curated surface) recurs across customer/member/borrower/tenant/patient portals. The patient realization differs in what makes it work: the standing anchor is the patient record and care relationship, the record content is clinical, and the governing machinery is health-specific — identity proofing against patient records, release-governed result visibility, proxy/carer law-sensitive access, privacy regimes. Keep separate leaves; no consolidation proposed (consistent with the member-portal pass's family note).
- **Personal Health Record (PHR)** — no directory leaf; market concept: the person's own, person-controlled record (the classic PHR promise), vs the portal's organization-held record presented back. The seam is porous in market naming: PKB self-labels "PHR platform" while functionally aggregating organization feeds into a patient-accessible record, and national PGO programmes (NL) use personal-record vocabulary for organization-fed access surfaces. Held: the invariant for this Type is the organization-held record; person-held, person-authored records are a different (unlisted) concept. Recorded as a naming-blur note for any future PHR leaf.
- **Health Information Exchange** (processed): HIE moves records between organizations; the HIE pass flagged that patient-facing cross-organization access services drift toward portal territory "when the patient-facing aggregate becomes the product's center". Confirmed here: PKB/NHS-App-style multi-provider aggregation for the patient is this Type; the exchange substrate beneath it is HIE.
- **Patient Scheduling / Patient Registration & Intake / Telehealth / RPM**: scheduling owns slot inventory (portal links to it for self-booking); intake owns the episodic pre-visit registration workflow of record (portal forms are patient-initiated submissions, not the intake system's workflow); telehealth delivers the visit (a video action inside the portal); RPM owns device-telemetry monitoring loops (portals display patient-entered/device data without owning monitoring). All four are capability linkages from the portal side, not the same Type.
- **Payer/member portals**: market naming blur noted by the member-portal pass ("member portal" used for health-plan member surfaces). Health-plan member surfaces (claims/benefits records) are a different anchor from the clinical patient record; no §22 leaf exists for them — recorded here so a future pass scopes them deliberately.

## Uncertainties

- The US enterprise EHR-embedded pole (MyChart-class) — by far the largest market population — was unreachable (403 across vendors). Its shape is inferred indirectly (OpenEMR module pattern, MEDITECH family naming, engagement-pass and e-prescribing-pass notes). No precise claim about those products is made anywhere; where the US pattern differs (payments, refill workflows, open-notes release), statements are held at common/variant strength.
- Refill requests: directly evidenced only in the NHS pole; US-market prevalence asserted at common-mature strength only.
- Proxy access depth in OpenEMR-class portals: undocumented in reachable sources; the capability is held common (two A-evidenced products) not universal.
- Historical check: no 1990s–2000s portal product was directly sourced; the historical pole is argued from OpenEMR's documented older-generation CMS-era portal and the structural argument that a web page with login + results + requests satisfies the core. The paper-era analog does not exist (the Type is inherently digital); the pre-portal baseline is phone/counter requests.
- PKB's position as "PHR" vs portal: kept as documented naming blur; not resolved into a directory issue because no PHR leaf exists to conflict with.

## Final Synthesis

The Patient Portal is the care organization's authenticated patient-facing surface over the patient's own record and services. Its defining core is three jointly-held structures: the patient's verified identity with the care context; the patient's own read-mostly window onto the organization-held health record (release-governed, organization-configurable, never the record of record); and patient-initiated self-service transactions (messages, prescription/appointment requests, forms, payments) that enter the organization's workflows for staff/clinical action. Everything else commonly associated with portals — mobile apps, payments, refills, self-booking breadth, telehealth links, device data, national identity infrastructure, EHR embedding — is market machinery layered on that core. The who-initiates test separates it from the Patient Engagement Platform; the record-owner test separates it from the EHR; the organization-held-record test separates it from the PHR concept; the clinical-record anchor separates it from the generic customer-portal family.
