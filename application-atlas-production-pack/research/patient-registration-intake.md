# Research Notes — Patient Registration & Intake

Research date: **2026-09-08**

## Research Goal

Understand, from real products, what Patient Registration & Intake software actually is and how it works:

- what the core objects are (patient record, visit/appointment, intake packet, forms/questionnaires/consents, coverage, payment, check-in/arrival)
- who uses it and on which surfaces (front-desk/registration staff vs patient self-service vs administrators configuring packets)
- how the intake loop runs (packet assembly → delivery → patient completion → staff review → handoff into PM/EHR/chart)
- how it integrates with the provider's PM/EHR (identity source, write-back, bidirectional sync)
- what rules govern it (packet configuration by visit, required items, coverage exceptions, e-signature consents, privacy, identity matching)
- where the boundary lies against Patient Scheduling, Patient Portal, Patient Engagement Platform, EHR/Practice Management, Healthcare Revenue Cycle Management, Online Form Builder, Digital Waiver Management, and Patient Flow Management

**Special obligations from prior passes (STATUS.md):**

1. **patient-engagement-platform pass (2026-09-08)** — requested a JOINT REVIEW: its intake-first pole (Phreesia) self-labels "patient intake software"; the proposed discriminator was "episodic pre-visit workflow of record vs ongoing provider-initiated loop." This pass must ratify or refine that split from the intake side.
2. **hospital-management-system pass (2026-09-08)** — pre-hung seam: patient-registration-intake + patient-scheduling are "capability slices" of hospital systems in some deployments; this pass must hold the seam (why a standalone Type is justified) and keep assertions about the enterprise/hospital pole weak.
3. **online-form-builder pass (2026-09-08)** — recorded "Patient Intake" as a template family inside generic form builders; the boundary (patient-record anchoring, coverage, EHR write-back, visit-bound operational loop) must be held from this side.

## Initial Boundary (hypothesis before research)

Working hypothesis: the provider-side system that gets a patient administratively ready for a specific care encounter — establishing/refreshing who they are and how their care is covered, collecting the per-visit information packet (forms, histories, screenings, consents), and handing the completed packet into the chart/schedule/billing ahead of or at the start of care. Nearest confusing neighbors: Patient Scheduling (upstream), Patient Portal (patient-initiated window), Patient Engagement (ongoing outreach loop), Practice Management/EHR (where registration is a native module), Revenue Cycle Management (the financial back office this feeds), generic form builders.

Key risks identified up front:

- Risk of the leaf collapsing into "a capability slice of EHR/PM" — must verify the standalone market exists (products whose entire center is intake).
- Risk of over-fitting to the modern US pattern: kiosk + SMS link + eligibility API + copay collection. Historical and regional check needed (paper clipboard, single-payer regions, hospital ADT registration).
- Risk of boundary confusion with Patient Engagement (the Phreesia straddle) — the two directory leaves share one vendor pole.

## Research Questions

1. What objects exist in the system? (patient, visit/appointment, intake packet/instance, form/questionnaire/screener, consent, coverage/insurance record, payment request, check-in/arrival state)
2. What triggers intake? (new patient, booked appointment, appointment type/provider/location rules, walk-in arrival)
3. What is the canonical loop? (assemble packet → deliver → patient completes → completion tracked → staff review/exception handling → write-back → arrival/encounter start)
4. Who completes the packet, on what surfaces? (patient device via secure link, kiosk, tablet, portal; staff-assisted fallback)
5. How does write-back work? (discrete data fields vs rendered PDF packet; bidirectional sync; identity matching)
6. What rules matter? (packet configuration per visit, required-question gating, coverage/eligibility exceptions surfacing to staff, redundant-question suppression for returning patients, e-signature consents, privacy of self-service)
7. Where do payments sit — defining or attached? (copays, balances, card-on-file)
8. Boundaries: vs scheduling, portal, engagement, EHR/PM, RCM, form builders, waivers.

## Representative Products

Selected for market representativeness, philosophical diversity, and customer-tier diversity (all four are standalone products whose center of gravity is patient intake/registration):

1. **Phreesia** — the category's flagship and largest-scale vendor ("Patient Intake Software That Grows Revenue"; 4,700+ organizations, 1-in-6 US patient visits claim); revenue-cycle-first philosophy (benefits verification, copay collection as leading pillars); health systems + independent groups; also the pole that straddles into patient engagement (the joint-review counterparty).
2. **Clearwave** — the patient-led kiosk pole: purpose-built check-in kiosks, mobile/tablet/QR, "portal-free check-in"; specialty-practice concentration (ophthalmology, orthopedics, oncology) and health systems; now packaged inside an 8-agent "AI Patient Engagement Platform" whose Pre-Registration / Clinical Intake / Check-In / Payments agents are the intake machinery.
3. **Kyruus Health Check-In** (Epion Health lineage) — the health-system/mid-market digital-intake pole: text-alert link-based intake with "no app download or log-in," screener library (PHQ-2/9, GAD-7, STEADI, EPDS), real-time bidirectional athenahealth/Oracle Health integration. Epion Health was acquired into Kyruus Health and its product continues as the Check-In solution — documenting the market's consolidation without losing the philosophy.
4. **Yosi Health** — the pre-arrival-first pole: "first pre-arrival focused patient intake platform" (2015), explicitly anti-kiosk ("while other companies were selling hardware, kiosks, and tablets…"), deep form-mapping philosophy (patient answers mapped onto the practice's existing forms, delivered back as discrete data + signed PDF packet); independent practices → health systems/FQHCs; won Best in KLAS 2024 in the "Patient Intake Management" category — evidence the market has an institutional category for this Type.

Rejected candidates: IntakeQ (site timed out twice — abandoned per network rules; would have been the SMB forms-first pole), Experian Health patient access (403 — would have been the enterprise revenue-cycle-front-end pole), Epic/athena EHR-native registration (403 per prior passes; EHR-embedded pole covered only indirectly).

## Sources

| Product | Source | Tier | Date |
|---|---|---|---|
| Phreesia | phreesia.com homepage + /end-front-desk-chaos/ pillar page (intake, self-scheduling, eligibility, payments sections + FAQ) | Tier 2 | 2026-09-08 |
| Clearwave | clearwaveinc.com homepage + /patient-check-in-system/ product page (module tabs + long FAQ incl. "What is patient check-in software?") | Tier 2 | 2026-09-08 |
| Kyruus Health | kyruushealth.com /solutions/check-in/ ("Digital Patient Intake Solution" + category-definition FAQ) | Tier 2 | 2026-09-08 |
| Yosi Health | yosi.health homepage + /platform/patient-intake-and-check-in/ + KLAS award press release reference | Tier 2 | 2026-09-08 |
| (cross-pass evidence) | research/patient-engagement-platform.md (Phreesia intake-first pole), research/hospital-management-system.md, research/online-form-builder.md ("Patient Intake" template family), research/electronic-health-record-ehr.md (registration as EHR feature) | internal | 2026-09-08 |

**Source-access Limitation:** No vendor help-center / operational-manual pages were reachable this pass (Phreesia support subdomain: transport error; Experian Health: 403; product admin guides sit behind customer logins for all four vendors). All direct evidence is Tier-2 official product/marketing pages and vendor FAQs. Accordingly: vendor-claimed performance numbers (adoption %, collection rates, check-in durations) are recorded here with attribution and are **excluded from the final document**; workflow and structural claims in the final document are kept at cross-product commonality strength, not vendor-mechanism precision. The enterprise/hospital registration pole (Epic-class inpatient ADT registration) remains documented only indirectly (via the hospital-management-system pass's observations).

## Product A — Phreesia (revenue-cycle-first flagship; Tier-2)

### Key observations (Evidence layer A — directly observed on official pages)

- Positioning: "Patient Intake Software That Grows Revenue"; "We power everything around the visit — from scheduling and registration to payments and communication."
- Four value pillars: increase revenue (verify benefits up front, collect copays before the visit), see more patients (no-shows, referrals, scheduling), **end front-desk chaos (self-check-in, forms, balance collection)**, patient experience (24/7 access, scheduling, paying).
- Front-desk pillar page describes the intake loop explicitly:
  - "Patients can complete registration, paperwork, insurance verification, scheduling and payments **before they arrive**… They simply receive a **secure link on their preferred device, so there's no portal to log into** or password to remember."
  - "Stop re-typing what patients already wrote… Phreesia makes it so the **patient chart is complete before they walk in**."
  - Eligibility verified "in real time across every patient and every visit. Inactive plans, missing authorizations and coverage changes get surfaced upfront."
  - Payments: card on file, text-to-pay, self-service plans; "86% of patient balances are cleared without anyone picking up the phone" (vendor-claimed).
  - Client quote (Southern Colorado Clinic): "updating patient registration details, verifying eligibility, and collecting copays and outstanding balances… saves us on costs for paper as well as… scanning documents into patients' charts."
- Bidirectional PM/EHR integrations ("Patient data flows into your PM/EHR and back out, so nothing gets keyed twice"); 16+ native integrations incl. Epic, athenahealth, Oracle; dashboards "across registration, payments and scheduling"; HITRUST/SOC 2/PCI.
- Adjacent modules beyond intake: VoiceAI phone agent, self-scheduling, Patient Activation Measure (licensed instrument), life-sciences network, MediFind — the engagement/growth layer that makes Phreesia the boundary straddle.

**Reading:** intake as *the pre-visit completion of the chart and the collection of money*: packet completion, coverage verification, and payment are one integrated pre-visit loop feeding the PM/EHR.

## Product B — Clearwave (patient-led kiosk pole; Tier-2)

### Key observations

- The registration product page defines the category: "Patient check-in software is a digital solution that **automates patient registration, insurance verification, payments and intake processes**" via "patient-led tools like kiosks, tablets and mobile devices."
- Module structure (the intake workflow made concrete):
  - **Pre-Registration** — "automatically captures demographics, insurance, consents and ID images **before patients arrive**, reconciling everything directly into the PMS/EHR"; patients "upload insurance card/IDs images, fill out unique screeners, sign consents"; data flows back "via discrete data fields or PDF"; collects SOGI/RELD/SDOH fields.
  - **Clinical Intake** — patients "input their own clinical histories"; workflows "shown based on the appointment service, provider and/or location"; results flow into the EHR.
  - **Kiosk Check-In** — scheduled **and walk-in** patients; built-in OCR scanners capture IDs and insurance cards; 13 languages.
  - **Mobile & Tablet** — "without apps, passwords or portals"; QR-code walk-in flow.
  - **Staff Control Center dashboard** — "alerts and flags help staff stay on top of timely pre-appointment tasks"; staff "quickly view upcoming appointments at-a-glance to solve errors" in eligibility/prior auth.
- Configurable logic (their own FAQ list): differentiate new vs returning patients; accept walk-ins while maintaining structured intake; configurable paths by appointment type; "alerts staff to complete tasks based on patient responses"; "automatically asks for the correct co-pay by specialty"; collects past-due balances, self-pay and estimations; **"removes redundant questions for subsequent visits"**; **"prompts for required answers, ensuring patients cannot skip past certain registration screeners"**; custom questions.
- Exception loop quoted from a client (Utah Cancer Specialists): "If their insurance is expired, the system will prompt patients to update their information and **it will notify our staff**."
- Explicit anti-portal stance: "**Portal-Free Check-in**: patients can check in… not locked behind a portal wall."
- Payments integrated: tap-to-pay, card-on-file, Apple/Google Pay; copay + prior balance + estimates "prior to care," posted to the PM system.
- Now sold inside an 8-agent AI platform (Voice, Scheduling, Eligibility, Clinical Intake, Pre-Registration, Check-In, Payments, Outreach) with a Workflow Agent orchestrating handoffs — marketing 2026-era, but the underlying module split is the intake workflow.

**Reading:** the same intake loop realized as *patient-led self-service with a hardware anchor*: the kiosk is the at-arrival completion surface, pre-registration is the pre-visit surface, and the staff dashboard is the exception queue. The workflow-configuration rules (per visit type, required gating, redundant-question suppression, staff alerting) are documented in unusual depth.

## Product C — Kyruus Health Check-In / Epion lineage (health-system digital-intake pole; Tier-2)

### Key observations

- Page title: "Digital Patient Intake Solution"; description: "the remote **pre-visit patient check-in** solution that captures **demographics, clinicals, consent forms, insurance card images, payments** and more — **before your patients even set foot in your office**."
- Delivery: "Through a **text alert**, patients can provide insurance information, complete health risk assessments, message with the practice, and pay copays or outstanding balances — all **without requiring an app download or log-in**."
- Personalization: "a personalized experience **based on appointment type, provider, and existing patient record**, ensuring patients only complete the steps relevant to them" — per-visit packet configuration.
- Forms: "Send patients custom forms, payment requests, and workflows to complete check-in steps **on-the-fly**"; library of fully-integrated screeners (PHQ-2/9, STEADI, EPDS, GAD-7 "and more").
- Integration: "real-time **bidirectional** integrations with athenahealth and Oracle Health EHRs"; "every form is completed… information is never lost."
- Vendor FAQ defines the category: "Digital patient intake is the electronic process of collecting essential patient information… before an appointment. It replaces traditional paper forms…"; "scheduling tools [integrate] to **trigger pre-visit forms when an appointment is booked**"; "payment processors to enable upfront collections and automatic posting of payments to the patient record"; HL7/FHIR named as transfer standards.
- FQHC-adjacent quote: "facilitates adherence to **accreditation and UDS reporting** requirements" — compliance capture at intake.
- Claims (vendor-reported, kept out of final doc): 94% patient completion rate, 15+ minutes saved per visit.

**Reading:** the same loop realized as *lightweight link-based remote intake with a clinical-screener spine* — closest to the "digital front door" pole; per-visit personalization and the trigger-on-booking rule are explicit.

## Product D — Yosi Health (pre-arrival-first, anti-kiosk pole; Tier-2)

### Key observations

- Lineage claim: "Since 2015… the first pre-arrival focused patient intake and management platform"; "**We were the first to remove patient intake from the waiting room**… While other companies were selling hardware, kiosks, and tablets, we created a better experience by eliminating the traditional point of care administrative choke points." Best in KLAS 2024 "Patient Intake Management Solution."
- Pre-arrival mechanics: "patients can register remotely and in advance using their own mobile device, laptop or home tablet. Create custom, **'appointment type specific'** patient intake forms and let patients easily update their insurance and identification information with the snap of a photo."
- Form management (distinctive philosophy): "you won't have to change any of your existing forms… we **map the patients' answers to your existing forms**. …the discrete data transfers securely into your EMR, but we also provide a **completed, signed and dated PDF packet** of all your existing forms that automatically gets pushed into the correct document section of your EMR." — dual write-back (discrete + PDF) as a first-class design.
- Forms personalization: "personalized screening questionnaires with **autoscoring** for every appointment type, patient category, scheduling provider, and specialty practice."
- e-signatures: "patients can easily sign all consent forms, privacy notices, and disclosures."
- Arrival layer (complements pre-arrival): **Auto Check-In** — confirm arrival via iPad kiosk, QR code, or GPS-based detection; "The EMR is automatically updated in real time, alerting staff and providers the moment a patient arrives"; "configurable pre-check steps (registration forms, payment, card-on-file)."
- **Walk-In Patient Management** — "patients self-register, complete intake, verify insurance, and make payments through an in-office kiosk or their own device via a QR code… **Automatic check-in upon payment and eligibility completion**."
- Payment module: pre- and post-visit collection, card-on-file, PCI-compliant.
- Adjacent modules: self-scheduling, surveys/reviews, telehealth, two-way texting, eligibility verification — the same "around-the-visit" bundle pattern as the other poles.

**Reading:** the same loop realized from the *pre-arrival-first* direction with a distinctive integration posture (map onto existing forms; dual discrete+PDF write-back). Walk-in handling shows the arrival gate logic: intake completion (payment + eligibility) *is* the check-in.

## Cross-product Comparison

| Structure / capability | Phreesia | Clearwave | Kyruus Check-In | Yosi |
|---|---|---|---|---|
| Patient registration record established/refreshed (demographics, contact, coverage) | ● | ● | ● | ● |
| Packet assembled per visit (appointment type / provider / location / new-vs-returning rules) | ● | ● (explicit config list) | ● (explicit) | ● (explicit) |
| Pre-arrival completion via patient device (secure link, no login/app) | ● | ● (mobile/tablet) | ● (text alert) | ● (own device) |
| At-arrival completion surface (kiosk/tablet/QR) | ○ (self-check-in named; kiosk not claimed) | ● (kiosk core) | ○ (in-office completion noted in FAQ) | ● (iPad kiosk + QR + GPS) |
| Clinical questionnaires/screeners collected pre-visit | ● ("3x patient-reported data" claim) | ● (Clinical Intake module; unique screeners) | ● (screener library) | ● (autoscoring screeners, HPI templates) |
| Consents / privacy notices / disclosures via e-signature | ● | ● | ● (consent forms named) | ● (explicit trio) |
| Insurance/ID card image capture | ● | ● (OCR scanners) | ● (card images named) | ● (photo capture) |
| Coverage/eligibility verification with staff alerting | ● (every visit) | ● (expired-insurance alert quoted) | ○ (coverage capture; verification via suite) | ● (module; walk-in gate) |
| Completion tracking + staff task surface | ● (dashboards) | ● (Staff Control Center, alerts/flags) | ● (completion-rate framing) | ● (arrival alerts; pre-check steps) |
| Payment collection attached (copay/balance/card-on-file) | ● (leading pillar) | ● (module; posted to PM) | ● (copays/balances) | ● (pre/post-visit module) |
| Write-back into PM/EHR (discrete and/or PDF) | ● (bidirectional, nothing keyed twice) | ● (discrete fields or PDF) | ● (bidirectional, real-time) | ● (discrete + PDF packet) |
| Walk-in self-registration flow | ○ | ● | ○ | ● (explicit) |
| Redundant-question suppression for returning patients | ○ | ● (explicit) | ○ (personalized to existing record) | ○ (patient category rules) |
| Self-scheduling bundled | ● | ● | ● (Schedule sibling) | ● |
| Reminders/communication bundled | ● (VoiceAI/texting) | ● (Outreach agent) | ● (two-way SMS) | ● (texting) |
| Portal as intake surface | — (explicitly "no portal") | — (explicitly "portal-free") | — ("no app or log-in") | — |
| Surveys/reputation/reviews bundled | — | — | — | ● |
| Telehealth links bundled | ● | — | — | ● |

● = observed in this product's official materials; ○ = partial/indirect; — = not observed.

### What repeats across all four (candidate core)

1. **Every product establishes or refreshes the patient's administrative registration record** — identity/demographics, contact, and how care is covered (insurance plan details or self-pay) — as the visit's administrative foundation, reconciled into the provider's PM/EHR.
2. **Every product structures intake as a visit-bound packet**: a configured bundle of updates, forms/questionnaires/screeners, consents, and (commonly) payment requests, whose composition follows the visit's attributes (appointment type, provider, location, new vs returning) — not a fixed one-size questionnaire.
3. **Every product tracks packet completion as an operational workflow** with a staff-side surface: pending tasks, completion states, alerts/flags for exceptions (coverage problems, incomplete packets, flagged answers).
4. **Every product hands the completed packet into the provider's systems** ahead of or at the encounter — discrete data fields and/or rendered PDF into the chart/PM — so the visit starts with the packet complete. Intake is not an end in itself.
5. **Patient self-service is the dominant completion mode** in all four (secure device links, kiosks, tablets, QR), with staff-assisted completion as the fallback pattern (the front desk the products exist to relieve).
6. Payments (copays/balances/card-on-file) ride the same loop in all four products — universal in the sample, but attached to the packet rather than constituting it (paper-era registration collected copays without any of this machinery).

### What varies (candidate variant axes)

- **Completion surface philosophy:** kiosk-first hardware (Clearwave) vs device-link-only "no portal, no app" (Phreesia, Kyruus) vs pre-arrival-first with optional in-office kiosk (Yosi). Clearwave and Yosi explicitly define themselves against each other's pole.
- **Write-back posture:** discrete-field mapping (Clearwave, Kyruus, Phreesia) vs form-mapping + PDF packet (Yosi's signature) — most support both.
- **Clinical depth of the packet:** demographic/financial at one end; scored screeners and specialty HPI templates at the other (Kyruus screener library, Yosi problem-specific HPI templates, Clearwave service-based clinical intake).
- **Customer tier:** independent practices (Yosi origin) → specialty groups/multi-site (Clearwave, Phreesia) → health systems (Phreesia, Clearwave, Kyruus) → FQHCs (Clearwave, Kyruus, Yosi) with accreditation/UDS compliance capture.
- **Bundle posture:** standalone intake (all four) wrapped in progressively wider "digital front door" suites (scheduling, communication, payments, reviews, telehealth).

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The patient registration record.** For the encounter to proceed, the provider must hold an administrative answer to *who this patient is* (identity, demographics, contact) and *how their care is covered* (payer/insurance details or self-pay responsibility). The intake system establishes or refreshes this record as part of preparing each encounter and reconciles it into the provider's administrative systems (PM/EHR). *Remove → a generic forms/questionnaire tool with no patient-record consequence.*

2. **The visit-bound intake packet.** The information the provider needs from the patient ahead of or at the start of a specific encounter — demographics updates, histories/questionnaires/screenings, consents and disclosures — assembled as a configured per-visit bundle (composition follows the visit's type/provider/location and the patient's new-or-returning status), delivered for completion (patient self-service or staff-assisted), and tracked to completion as a workflow of record. *Remove the visit-bound packet → static form library or a demographics master file with no collection workflow; remove the workflow-of-record tracking → a pile of documents.*

3. **The staff-side review-and-handoff loop.** Staff see pending/intake-incomplete visits, work exceptions (missing items, coverage problems, flagged answers), and the completed packet flows into the provider's scheduling/chart/billing systems before or at the encounter — intake is operational work that feeds care delivery, not a standalone survey. *Remove → a data-collection instrument with no operational destination.*

**Jointly-held load-bearing analysis:**

- 1 alone = patient demographic master-file management (a PM/EHR registration module slice)
- 2 without 1+3 = forms/questionnaire tooling
- 3 without 1+2 = generic task/workflow board
- 1+2 without 3 = data collection with no operational destination (survey territory)
- 1+3 without 2 = front-desk registration data entry (ADT-style slice)
- 2+3 without 1 = generic survey/workflow platform

**Historical / market-sample check:** the paper-era front desk satisfies all three legs with none of the modern machinery: the patient fills the clipboard packet (demographics, history, insurance, consents), the front desk reviews it for completeness, photocopies the card, keys/corrects the record in the practice's system, and files the packet into the chart before the visit proceeds. Practice-management registration modules and hospital ADT-style registration satisfy the same legs as embedded realizations. The definition therefore names no kiosk, no SMS link, no eligibility API, no payment rail, no cloud, no era machinery. **Anti-overfit:** the kiosk is NOT definitional (Yosi defines itself against kiosks; Phreesia's flagship surface is the device link); the "no-portal link" is NOT definitional (portal-hosted intake forms are a known realization); copay collection is NOT definitional (universal in the sample, absent from the paper-clinic and prepayment/single-payer contexts that still register patients); eligibility verification is NOT definitional (a coverage-capture record is; the real-time payer API is US-market machinery).

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- pre-arrival completion via patient's own device (secure link / text message; no app or login)
- at-arrival self-service surfaces (kiosk, tablet, QR) with arrival confirmation / auto check-in
- insurance eligibility & benefits verification surfaced before/at the visit, with staff alerting on coverage problems
- payment collection attached to the packet: copays, outstanding balances, card-on-file, estimates; posting to the PM/billing system
- insurance card / ID image capture (photo or scanner OCR)
- clinical screeners/assessments libraries (scored instruments) and specialty-specific questionnaires
- e-signature capture of consents, privacy notices, financial policies
- configurable workflow rules: required-question gating, conditional/skip logic, redundant-question suppression for returning patients, custom questions
- walk-in self-registration flows (unscheduled patients)
- staff dashboards / task queues / flags over pending pre-visit work
- real-time bidirectional PM/EHR integration (discrete fields and/or rendered PDF packet)
- multi-language patient experience; accessibility posture
- analytics on completion, collections, cycle-time

### L2 — Variant / Optional Structure

- completion-surface philosophy as market segmentation: kiosk-led vs device-link-led vs portal-hosted intake
- patient-portal integration as an alternative delivery surface (portal-hosted forms vs the "no-portal" poles)
- new-patient onboarding packets vs returning-patient refresh packets as distinct configured experiences
- FQHC / community-health configuration: sliding-scale/self-pay programs, accreditation and reporting capture (e.g., UDS-flavored reporting named by one vendor)
- urgent-care / walk-in-centric configurations where the arrival gate (payment + eligibility completion = check-in) dominates
- hospital / inpatient registration as an embedded realization inside HMS/EHR (ADT-style) rather than a standalone product
- specialty-tuned packets (per-specialty questionnaires, service-based workflow paths)
- reminders/recall, two-way messaging, self-scheduling, surveys/reviews, telehealth links bundled around the intake core (the "digital front door" wrapper)
- AI agents layered over intake steps (2026-era; pre-fill from EHR, conversational completion)

### L3 — Vendor-specific (research notes only)

- Phreesia: VoiceAI phone agent; PhreesiaOnCall after-hours; Patient Activation Measure licensing; MediFind consumer discovery sibling; life-sciences network side; AccessOne; "1-in-6 US visits" and other network-scale claims; 16+ native integrations named.
- Clearwave: 8-agent "AI Patient Engagement Platform" packaging + Workflow Agent; purpose-built kiosk hardware with OCR scanners; 13 check-in languages with per-patient language memory; SOGI/RELD/SDOH field capture; premium-service upsell questions (named examples: BOTOX, ICL); 900+ payer connections, 2B+ eligibility checks, 50+ PMS/EHR integrations (vendor claims); client-quoted mechanics (copay presentation by specialty; expired-insurance prompt + staff notification; check-in gated by required answers).
- Kyruus Health (Check-In / Epion lineage): text-alert no-app intake; screener library naming PHQ-2/9, GAD-7, STEADI, EPDS; on-the-fly form/payment sending; bidirectional athenahealth + Oracle Health integrations; UDS/accreditation compliance framing; "94% completion / 15+ minutes saved" vendor claims; acquisition into Kyruus Health (care-access platform with Provider Data Management, Search, Schedule).
- Yosi Health: proprietary form-mapping onto existing practice forms + completed/signed/dated PDF packet into the chart's document section; autoscoring questionnaires; problem-specific HPI templates (client-quoted, "no other athena Marketplace partner has this"); Auto Check-In via iPad kiosk / QR / GPS; walk-in gate = payment + eligibility completion; 99.95% uptime claim; Best in KLAS 2024 Patient Intake Management; physician-founded origin story (2015).

## Rejected Findings

- **"Patient registration & intake = a check-in kiosk."** Rejected: the kiosk is one completion surface; Phreesia/Kyruus run the full loop without kiosks and Yosi explicitly positions against hardware. The packet + record + handoff structure defines the Type; the kiosk is a variant surface (strongest at the Clearwave pole).
- **"Patient registration & intake = digital forms for clinics."** Rejected: generic form tools can produce the instruments but lack the patient-record anchoring, the visit-bound packet logic, the coverage/eligibility dimension, and the EHR/PM handoff loop. (The online-form-builder pass independently recorded "Patient Intake" as merely a template family inside its Type.)
- **"Intake is part of Patient Engagement."** Rejected as identity; confirmed as overlap. The engagement pass's own analysis treats Phreesia's intake center as a distinct pole; this pass ratifies the split — see Boundary Findings.
- **"Copay/payment collection is definitional."** Rejected: universal in the sampled digital products but structurally attached; paper-era, prepaid, charity, and single-payer contexts register patients without the digital payment rail. It is the most important Common, not part of the core.
- **"Eligibility verification is definitional."** Rejected for the same reason: the core needs the coverage record, not the real-time payer API (US-market machinery).
- **"Registration happens only before the visit."** Rejected: all sampled products handle at-arrival completion and walk-in self-registration; the boundary is *ahead-of-or-at the encounter*, not strictly pre-visit.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (what to remove/keep) |
|---|---|---|
| Patient Engagement Platform | overlap at one vendor pole (Phreesia) — JOINT REVIEW DISCHARGED | Intake = the **episodic, visit-bound** administrative workflow of record (packet assembled per visit, completed, handed into the chart). Engagement = the **ongoing provider-initiated loop** across visits (outreach, reminders, campaigns, journeys, staffed response queues). Remove the visit-bound packet + handoff and keep continuous outreach → engagement; remove the ongoing loop and keep the packet → this Type. Phreesia genuinely straddles: its center of gravity (its own positioning: "Patient Intake Software") is this Type; its reminders/recalls/campaigns are engagement machinery. Both leaves stand. |
| Patient Scheduling | upstream sibling, linked | Scheduling owns slot inventory and booking; intake begins once a visit exists (or, for walk-ins, at arrival) and prepares that visit. Intake vendors bundle self-scheduling (all four sampled) — a bundle, not an identity. Remove the packet and keep slot management → scheduling. |
| Patient Portal | adjacent, different initiation & scope | Portal = patient-**initiated, longitudinal** window onto the record and services. Intake = provider-configured **episodic** packets feeding each encounter. Two of four sampled poles explicitly market being "no-portal / portal-free"; conversely, portal-hosted intake forms are a known realization — the function can ride a portal, but the Type is defined by the packet+loop, not the surface. |
| Electronic Health Record / EHR (and Practice Management) | contains a registration module; embedded pole | Registration is a native PM/EHR capability (demographic master file, insurance capture, per the EHR pass's own observations). The standalone Type exists where the *packet depth* (questionnaires, screeners, consents, payments) and the *operational loop* (completion tracking, exception queues, multi-EHR write-back) are the product's center. Remove packet depth → PM registration module; keep it as the center → this Type. Seam held per the HMS pass's request. |
| Hospital Management System | embedded realization context | In hospitals, registration appears as an ADT-style capability slice inside the HMS; standalone intake products historically concentrate in ambulatory/specialty settings. The HMS pass's pre-hung seam is held: no consolidation; the standalone market is evidenced by the dedicated vendor category (KLAS "Patient Intake Management"). |
| Healthcare Revenue Cycle Management | downstream consumer | Intake is the *front end* of the revenue cycle (coverage capture, eligibility, point-of-service collection feed clean claims); RCM owns coding, claims, denials, A/R back office. Clearwave markets "revenue cycle acceleration" — a downstream-effect framing, not ownership of the back office. |
| Online Form Builder | instrument supplier, not the Type | Form builders supply generic instruments (their pass records "Patient Intake" as a template family); they lack patient-record anchoring, coverage semantics, visit-bound packet logic, and PM/EHR handoff. A form builder gains no registration consequence when a form is filled; this Type's whole point is that consequence. |
| Digital Waiver Management (§26) | one instrument | Waivers/consents are a single instrument inside the intake packet; no patient record, no coverage, no encounter context. |
| Patient Flow Management | downstream, arrival-adjacent | Flow owns rooming/throughput/room-state after arrival; intake's arrival confirmation is a handoff event into that world, not flow management itself. |
| Survey Platform / Questionnaire Application | same mechanics, different substrate | Surveys field instruments to anonymous/consenting respondents for measurement; intake completes an identified patient's administrative preparation under provider rules, with record consequences. Screeners look like surveys; their disposition is the chart, not a dataset. |

**Taxonomy observation:** the market itself institutionalizes this Type — a dedicated KLAS award category ("Patient Intake Management", awarded 2024) and consistent self-labeling ("patient intake software", "digital patient intake", "patient check-in system", "patient registration"). Vendors disagree sharply about surfaces (kiosk vs no-portal links) but agree on the packet/record/loop structure — good evidence the Type is stable beneath the surface wars.

## Uncertainties

- **No Tier-1 help-center evidence.** All four vendors' operational manuals sit behind customer logins; support subdomains failed (Phreesia transport error, Experian 403). Workflow claims rest on Tier-2 official product pages and vendor FAQs; precise mechanics (exact field mappings, state names, timing defaults) are not asserted.
- **Vendor performance numbers** (adoption %, collection lift, check-in durations, uptime) are marketing claims recorded here with attribution only — excluded from the final document.
- **EHR-native intake modules** (Epic-class, athena-native) remain unsampled per prior passes' 403s; the embedded pole is held only via cross-pass observations. The final document treats the embedded-vs-standalone distinction at the capability-slice level, not with product-specific claims.
- **Regional (non-US) products unsampled.** Coverage semantics were deliberately abstracted ("how care is covered — insurance or self-pay responsibility") rather than naming US payer machinery; single-payer / prepaid regional realizations are inferred, not observed (kept out of the final document's factual claims).
- **Boundary judgment call:** walk-in self-registration edges toward Patient Flow Management (arrival state) — held as a handoff here; if a future flow pass disagrees, revisit.
- **Kyruus Check-In is a post-acquisition product** (Epion lineage); whether pre- and post-acquisition product behavior differs is unverifiable from public materials.

## Final Synthesis

Patient Registration & Intake software is the care provider's administrative preparation system for each encounter. Its defining structure is the jointly-held trio: (1) the **patient registration record** — who the patient is and how their care is covered, established or refreshed as the visit's administrative foundation and reconciled into the provider's PM/EHR; (2) the **visit-bound intake packet** — a per-visit configured bundle of demographics updates, histories/questionnaires/screeners, consents, and commonly payment requests, delivered for patient self-service (device link, kiosk, tablet, QR, portal) or staff-assisted completion and tracked to completion as a workflow of record; and (3) the **staff-side review-and-handoff loop** — exception queues over pending intake, coverage problems surfaced to staff, and the completed packet flowing into the chart/schedule/billing so the encounter starts complete. Around that core, mature products add eligibility verification with alerting, point-of-service payment collection, card/ID capture, scored screener libraries, e-signature consents, configurable workflow rules (required gating, redundant-question suppression, per-visit personalization), walk-in flows, multi-language delivery, and analytics. The market divides by completion-surface philosophy (kiosk-led vs no-portal device links vs portal-hosted) and bundles outward into wider "digital front door" suites (scheduling, communication, payments, reviews). Remove the visit-bound packet and the loop and it collapses into a demographic master file or a generic form tool; remove the patient-record anchoring and it collapses into a survey; remove the episodic visit boundary and it drifts into Patient Engagement.
