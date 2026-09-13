# Research Notes — Patient Engagement Platform

Research date: **2026-09-08**

## Research Goal

Understand, from real products, what a Patient Engagement Platform actually is and how it works:

- what the core objects are (patient, outreach/trigger, campaign, conversation, task, form, survey, journey)
- who uses it and on which surfaces (staff-side vs patient-side)
- how the engagement loop closes (outreach → response → staff work → outcome)
- how it relates to the EHR/PM system (identity, triggers, write-back)
- what rules govern it (consent/opt-out, messaging hours, PHI, escalation to clinical staff)
- where the boundary lies against Patient Portal, Patient Scheduling, Patient Registration & Intake, Care Coordination, Telehealth, Remote Patient Monitoring, Population Health, and business-to-consumer messaging

## Initial Boundary (hypothesis before research)

Working hypothesis: a provider-side system for actively engaging patients outside the exam room — reminders, recalls, two-way messaging, intake, education, surveys, care journeys — while managing the resulting staff work. Nearest confusing neighbors: Patient Portal (patient-initiated), Patient Registration & Intake, Care Coordination Platform, healthcare-flavored CRM/marketing, Customer-to-Business Messaging.

Key risks identified up front:

- "Patient engagement" is a marketing umbrella term; some vendors use it for portals, some for outreach, some for intake. Risk of Alias-of-Portal or Alias-of-Intake finding.
- Risk of over-fitting to the modern SMS/texting-hub pattern (same anti-overfit concern as phone-number identity in IM).

## Research Questions

1. What objects exist in the system? (patient record, communication line/channel, trigger, campaign, conversation, task, form, survey, journey/pathway, education item)
2. What initiates engagement? (appointments, referrals, recalls, care gaps, campaigns, manual staff action, inpatient admission/discharge)
3. How does the loop close? (outreach → patient response/action → staff handling → outcome recorded back where?)
4. What does the patient see? (SMS, voice call, email, web links, app, portal pages)
5. How does EHR/PM integration shape the product? (identity source, event source, write-back)
6. What rules matter? (opt-out/consent, messaging-hours regulation, secure vs unsecure content, patient contact/language preferences, staffing of response queues)
7. Where does this Type end and Patient Portal / Intake / Care Coordination / CRM begin?

## Representative Products

Selected for market representativeness, philosophical diversity, and customer-tier diversity:

1. **Artera** (formerly WELL Health) — enterprise patient-communications/messaging hub; #1-in-KLAS patient communications claim; health systems, FQHCs, federal agencies. Rich public Tier-1 knowledge base. The *two-way messaging hub* pole.
2. **GetWellNetwork ("Get Well")** — enterprise cross-continuum engagement with inpatient/bedside heritage (25+ years "interactive patient care"); SmartRoom, Hospital Journey Manager, GetWell Loop guided care plans, patient activation, population health. The *care-journey / patient-activation* pole.
3. **Solutionreach** — SMB → multi-location practice outreach suite (dental/eye care/medical; DSOs); claims to have "created the patient retention and engagement market in 2000". The *practice-growth outreach* pole.
4. **Phreesia** — intake-first engagement ("patient intake software"); around-the-visit operations (scheduling, registration, payments, communication); Patient Activation Measure; health systems + independent groups + life sciences. The *intake-first / visit-operations* pole.
5. **TeleVox (WestCX)** — 30+ years voice-heritage patient outreach ("HouseCalls" reminder lineage); now an omnichannel outreach platform. The *voice-heritage / historical lineage* pole. Its site title is literally "Patient Engagement Platform".
6. **Updox** — independent-practice unified communications platform with an explicit "Patient Engagement" product family (portal, reminders, forms, broadcast, secure text) built around a universal inbox. The *SMB unified-communications* pole.

Rejected candidates: Luma Health (site unreachable in the research environment — 404/403 on both domains, dropped per network-limit rules), Epic MyChart / athenahealth patient engagement (403 — see Source-access Limitation).

## Sources

| Product | Source | Tier | Date |
|---|---|---|---|
| GetWellNetwork | getwellnetwork.com homepage + product navigation (Get Well 360, Hospital Journey Manager, SmartRoom, GetWell Loop, Patient Activation, Point of Care Engagement, Transitions of Care) | Tier 2 | 2026-09-08 |
| Solutionreach | solutionreach.com homepage + full feature navigation (reminders, two-way texting, recall, digital intake, check-in, surveys, reputation, batch messaging, payment technology, integrations) | Tier 2 | 2026-09-08 |
| Phreesia | phreesia.com homepage + navigation (platform, VoiceAI, PhreesiaOnCall, Patient Activation Measure, pricing, patient FAQ) | Tier 2 | 2026-09-08 |
| Artera | artera.io homepage + knowledge.artera.io index + KB articles: "Campaigns Overview", "Triggers" category | **Tier 1** | 2026-09-08 |
| TeleVox | televox.com homepage (WestCX Orchestrate positioning, HouseCalls Pro customer quotes, KLAS quotes) | Tier 2 | 2026-09-08 |
| Updox | updox.com homepage + product navigation (Patient Engagement family, Universal Inbox) | Tier 2 | 2026-09-08 |

**Source-access Limitation:** Luma Health (lumahealth.io / lumahealth.com), Epic (epic.com, mychart.com) and athenahealth patient-engagement pages returned 403/404 and were abandoned after the allowed retries. The EHR-embedded pole (EHR vendor selling its own engagement module) is therefore covered only indirectly (Artera KB documents EHR-integration mechanics from the third-party side; TeleVox quote documents SMS-capture write-back into Epic). Claims that would depend on EHR-native products' internal workings are kept at reduced strength. GetWellNetwork's GetWell Loop patient FAQ is JS-rendered and yielded no article content — inpatient/bedside mechanics rely on Tier-2 descriptions only.

## Product A — Artera (two-way messaging hub; Tier-1 evidence)

### Key observations (Evidence layer A — directly observed in official KB)

**Platform object model visible in the KB structure itself:**

- **Patient Channel** — the patient-side communication surface (SMS-first); "Managing Appointments" sits under it.
- **Triggers** — event-driven automated outreach, with explicit trigger families: *Appointment Triggers*, *Inbound Message Triggers*, *Recall Triggers*, *Referral Triggers*. Plus trigger filters, TCPA-hours settings, patient contact-preference sync (synced-from-EHR vs not).
- **Campaigns** — large-volume targeted outreach. Documented mechanics:
  - audience sources: CSV upload of EMR patient IDs (MRNs), or "Patients with Appointments" filtered by appointment status / location / event (appointment type) / provider;
  - campaign categories: Appointment, Clinical, Financial, Health System Update, Marketing, Other, **Portal Invitation**, Scheduling, Referral, Survey — effectively the vendor's own taxonomy of engagement use cases;
  - delivery channels: text, call (incl. AI voice conversations), email; secure vs unsecure message modes; attachments; per-patient language-preference translations; opt-out language required;
  - scheduling controls: start date/time, allowed sending hours, TCPA hours (documented as 8:00 AM–9:00 PM in the practice's timezone), business-days-only tied to practice hours;
  - sending line choice (practice line vs high-volume toll-free number) as a deliverability instrument;
  - send-rate control (messages per hour) explicitly motivated by staff-response capacity ("enough staff to engage with patient responses without being overwhelmed");
  - lifecycle: pending → queued → running; editable only before start; deliverability reporting afterwards.
- **Inbox (Collaborative Inbox)** — the staff work surface where patient responses land, including *unverified patients* handling; **Patient Facesheet** — per-patient view (contact preferences, history); **Lines, Events, Resources** — communication lines mapped to locations/departments, "Events" = appointment types; **Quick Responses** — staff-side templates; **Conversation Flows** — automated conversation bots; **Self-Rescheduling**, **Recalls**, **Referrals** as first-class modules; **AI Agents**; **Users and Groups** (staff/manager roles, permissions); **Insights & Analytics**.

**Homepage (Tier 2):** two-way messaging heritage ("11+ years connecting providers & patients", 2B+ patient interactions/year), care-gap closure outbound campaigns, scheduling/intake/payments/referrals AI solutions, EHR integrations, warm handoff from AI to staff with "a complete log of all conversation history".

**Reading:** the platform's center of gravity is the *conversation loop at scale*: EHR events trigger outbound messages; replies land in a collaborative staff inbox organized by line/practice; automation (flows, AI agents) absorbs routine traffic; staff handle the rest. Identity and triggering data come from the EHR.

## Product B — GetWellNetwork (cross-continuum journeys / patient activation; Tier-2)

### Key observations

- Positions as "A Digital Whole Health Platform Built for the Patient Journey"; "digital patient engagement" explicitly; 25+ years "interactive patient care".
- **Hospital Journey Manager** — "end-to-end patient support from admission through discharge"; **SmartRoom** — inpatient room-based engagement (screens in the room); pediatric variants.
- **GetWell Loop** — guided care plans / transitions of care (patient-facing programs; Loop support portal exists for patients).
- **Patient Activation** as a named platform pillar (activation, growth, retention); **Population Health** programs (health equity, community); payer/member engagement; federal (VA, FedRAMP).
- 20+ EHR integrations, 500 partner integrations; HITRUST/SOC2/FedRAMP certifications.
- Solutions organized by journey stage and care setting rather than by channel: Point of Care Engagement, Transitions of Care, GetWell Anywhere, ambulatory programs (maternal health, COVID-19, retention).

**Reading:** the same Type realized as *structured patient journeys/programs* (education, screening, navigation, surveys across a care episode) rather than as a messaging hub; staff side includes live navigators and care-team support. The EHR relationship is integration-heavy but the journey content is owned by the engagement platform.

## Product C — Solutionreach (practice outreach/growth; Tier-2)

### Key observations

- Homepage H1: "PATIENT ENGAGEMENT SOFTWARE — Engage patients at every stage to keep schedules full and get paid faster… automated recalls, appointment reminders, two-way texting, and more — securely integrated with your PM/EHR."
- Feature family: Appointment Reminders, **Two-Way Texting**, Batch Messaging, **Recall**, Online Scheduling, Digital Intake, Patient Check-In, Payment Technology, Patient Surveys, Reputation Management, Refer-a-Friend, Patient Education/Marketing Campaigns, Secure Documents, Insurance Eligibility, Video Call/Telehealth, Phone System, AI Receptionist, Data Hub, Integrations ("400+ PM/EHR systems").
- Value framing: reduce no-shows, recall revenue, faster payments, front-office efficiency — the practice-growth orientation.
- "Solutionreach created the patient retention and engagement market in 2000" — historical anchor; SMB practices → DSOs/multi-location; G2 badge literally in a "PatientEngagement" category.

**Reading:** same Type at the SMB pole: reminder/recall-triggered outreach + two-way texting + intake + surveys + reputation, all hooked to the PM/EHR schedule and patient list; the staff surface is the front-office team.

## Product D — Phreesia (intake-first visit operations; Tier-2)

### Key observations

- Positions as "Patient Intake Software That Grows Revenue"; "We power everything around the visit — from scheduling and registration to payments and communication — all through AI-enabled workflows."
- Pillars: increase revenue (benefits verification, copay collection), see more patients (no-shows, referrals, scheduling), end front-desk chaos (self-check-in, forms, balance collection), patient experience (24/7 access, scheduling, paying).
- "3x more patient-reported data captured before the visit" — patient-reported data capture is a first-class outcome; licenses the **Patient Activation Measure** (PAM) — an activation-scoring instrument.
- VoiceAI (inbound/outbound phone agent for appointments, payments, refills, recall, collections); PhreesiaOnCall (after-hours); MediFind (consumer discovery sibling).
- 4,700+ organizations; 1-in-6 U.S. patient visits claim; 16+ native PM/EHR integrations; also a life-sciences network side (content/surveys to patients at scale).

**Reading:** the Type realized from the *around-the-visit operations* angle: the triggered touchpoint is the visit itself (pre-visit intake forms, screenings, payments), with communication, scheduling, and activation layered on. Overlap with the Patient Registration & Intake leaf is real and documented from the vendor's own positioning.

## Product E — TeleVox / WestCX (voice-heritage outreach; Tier-2)

### Key observations

- Site title: "Patient Engagement Platform - Digital Healthcare Solutions". "For more than 30 years, Televox has powered patient and member communication across healthcare and pharmaceutical experiences."
- WestCX Orchestrate — "real-time, inbound and outbound interactions across voice and digital channels… understanding intent, guiding next best actions"; multilingual; regulated-environment governance framing.
- Customer quote (Kettering Health): "Since adopting **HouseCalls Pro** to capture real-time, **self-reported patient information via SMS and record that in Epic**, we have continued to expand automated workflows." — direct evidence of outbound-SMS data capture written back into the EHR.
- Another KLAS quote references "self-scheduling options and AI technology" being added.
- Serves health systems, hospitals, physician practices, payers, pharma; 2,000+ customers; 1B+ patient communications/year.

**Reading:** the historical pole: automated reminder/outreach systems (voice-first, HouseCalls lineage) that modernized into omnichannel engagement. Confirms the Type's pre-portal, pre-app lineage and the EHR write-back loop.

## Product F — Updox (SMB unified communications; Tier-2)

### Key observations

- Practice-communication platform (eFax, Direct Secure Messaging, payments, documents) with an explicit **"Patient Engagement"** product family: Telehealth, **Patient Portal** ("view test results, make appointments, pay bills"), Appointment Reminders (text/email/phone), Forms, Broadcast Messaging ("message all the patients at once or in groups based on demographics or diagnosis"), Secure Text.
- "Engage Patients" philosophy page: access to practice + information → engaged patient base → outcomes, fewer missed appointments, reliable payments.
- Universal Inbox funnels all communications (emails, eFaxes, etc.) into one organized staff inbox; integrates with most EMRs; Best in KLAS Virtual Care Platforms 2022 badge.

**Reading:** the Type realized as an add-on family to a practice communications platform; notably the vendor sells Patient Portal and engagement as **separate product family members**, which is useful boundary evidence (portal = patient window; engagement = outreach/reminders/broadcast/forms).

## Cross-product Comparison

| Structure / capability | GetWell | Solutionreach | Phreesia | Artera | TeleVox | Updox |
|---|---|---|---|---|---|---|
| Patient population sourced from EHR/PM (identity + contact + events) | ● (20+ EHR) | ● (400+ PM/EHR) | ● (16+ native) | ● (MRN-based audiences, EHR specs) | ● (Epic write-back quoted) | ● (most EMRs) |
| Provider-initiated outbound engagement (reminders/outreach/campaigns) | ● (journeys/programs) | ● (reminders, recall, batch) | ● (communication, VoiceAI outbound) | ● (triggers, campaigns — Tier 1) | ● (30-yr outreach lineage) | ● (reminders, broadcast) |
| Patient-side response & action (reply, confirm, forms, self-schedule, pay) | ● (loops, education, surveys) | ● (two-way texting, check-in) | ● (intake, PAM, VoiceAI) | ● (channel replies, self-rescheduling — Tier 1) | ● (SMS self-report) | ● (secure text, forms, portal) |
| Staff-side managed work surface (inbox/queues/tasks/navigators) | ● (care-team support, navigators) | ● (front-office efficiency framing) | ● (dashboards, staff workflows) | ● (collaborative Inbox, facesheet — Tier 1) | ● (workflow automation framing) | ● (universal inbox) |
| Appointment/event triggers | ● | ● | ● | ● (Tier 1) | ● | ● |
| Recall / care-gap / retention outreach | ● | ● | ● (recall via VoiceAI) | ● (Tier 1: Recall Triggers, recalls) | ● | ○ (recall not named; broadcast covers) |
| Broadcast campaigns to segments | ● | ● (batch) | ○ | ● (Tier 1) | ● | ● |
| Digital intake forms / pre-visit registration | ○ | ● | ● (core) | ○ (add-on/AI) | ● (SMS self-report) | ● |
| Surveys / patient-reported capture | ● | ● | ● (PAM) | ○ (campaign category) | ○ | ○ |
| Education content delivery | ● (core) | ● | ○ (screenings) | ○ | ○ | ○ |
| Self-service scheduling/rescheduling | ○ | ● | ● | ● (Tier 1) | ● (quoted) | ● (portal) |
| Payments | — | ● | ● (core) | ○ (AI intake & payments) | — | ● |
| Reputation/reviews/referral marketing | — | ● | — | — | — | — |
| Bundled patient portal | — | — (mobile app) | — | ○ (secure messaging portal; portal-invitation category) | — | ● (separate family product) |
| Inpatient / bedside surfaces | ● (core) | — | — | — | — | — |
| AI agents/voice bots (2026-era) | ● | ● | ● | ● | ● | ○ |

● = observed in this product's official materials; ○ = partial/indirect; — = not observed.

### What repeats across all six (candidate core)

1. Every product maintains an **identified patient population anchored in the provider's EHR/PM** — engagement targets, triggers, personalization, and (where documented) write-back all reference it.
2. Every product **initiates contact outward** — scheduled or event-triggered reminders/outreach/journeys/campaigns across text, voice, email, app/web links.
3. Every product gives the patient a **way to respond and act** (two-way reply, confirm, complete forms/screenings/education, self-schedule, pay).
4. Every product gives the provider organization a **staff-side surface where responses are worked** (inbox, queues, tasks, navigators, dashboards) — engagement is managed operational work.
5. Appointment-related events are the universal trigger; recall/care-gap/retention outreach is nearly universal.

### What varies (candidate variant axes)

- Center of gravity: messaging hub (Artera) vs journey/program engine (GetWell) vs intake-first (Phreesia) vs growth/outreach suite (Solutionreach, TeleVox) vs communications add-on (Updox).
- Customer tier: SMB practices (Solutionreach, Updox) → medical groups/DSOs → health systems/FQHCs/federal (Artera, GetWell, TeleVox) → payers/pharma (GetWell, TeleVox, Phreesia).
- Care setting: ambulatory vs inpatient/bedside vs transitions/home vs payer member base.
- Channel era and mix: voice-first heritage (TeleVox) → SMS/email/web → app/portal → AI voice/text agents (2026-era layer across all poles).
- Commercial add-ons: payments, reputation, eligibility, telehealth links — common at the SMB pole, partial elsewhere.

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The provider's patient population as identified engagement subjects.** A persistent roster of identified patients in the care organization's context — demographics, contact channels, preferences, and the care events (appointments, referrals, episodes) that give outreach its meaning. Identity/event data anchored in the provider's clinical-administrative systems (EHR/PM), usually by integration. *Remove → generic B2C messaging or a lightweight healthcare CRM with no care context.*

2. **The two-way engagement loop initiated by the provider.** The organization proactively reaches patients outside the clinical encounter — on schedules, on care events, on campaigns, or through structured programs — and the patient responds and acts within the same loop: replies, confirms, completes forms/screenings/education, self-schedules, pays. The loop closes back into the organization (responses, completed data, confirmed/canceled appointments). *Remove provider-side initiation → patient-initiated self-service = Patient Portal territory; remove patient-side response/action → one-way notification blast.*

3. **The managed engagement work surface.** Patient responses and pending interactions land in organization-managed queues/conversations/tasks that staff work, escalate (including to clinical staff), and track; outreach volumes are paced and measured against the team's capacity. Engagement is operational work with an audit trail, not fire-and-forget messaging. *Remove → unmanaged broadcast/notification tooling.*

**Jointly-held load-bearing analysis:**

- 1 alone = patient contact roster / light healthcare CRM
- 2 without 3 = one-way reminder/notification service (the autodialer boundary case)
- 3 without 1+2 = generic team inbox / task board
- 1+2 without 3 = blast messaging with no managed follow-up
- 1+3 without 2 = patient-initiated portal
- 2+3 without 1 = generic business-to-consumer messaging platform

**Historical/market-sample check (§24):** TeleVox's 1992-heritage reminder systems and Solutionreach's 2000 "SMILE" reminder-and-reply lineage satisfy all three legs with no portal, no app, no SMS hub, no AI, no cloud — patient list from the PM system, outbound reminders, staff handling of replies. One-way autodialer notification services without reply capture or staff handling fail leg 3 and sit outside the Type (notification tooling). The definition therefore names no channel, no era machinery, no AI. **Anti-overfit:** the modern SMS-hub pattern (Artera's collaborative inbox, triggers, campaigns) is the best-documented realization (Tier 1), but it is NOT the definition — the journey-engine and intake-first poles satisfy the same three legs with different center-of-gravity objects.

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- appointment reminders/confirmations with confirm/cancel/reschedule actions (universal trigger family)
- recall / no-show backfill / care-gap and retention outreach
- broadcast campaigns to patient segments (batch outreach)
- digital intake forms and pre-visit questionnaires; patient check-in
- surveys and patient-reported data capture (experience and clinical screenings)
- patient education content delivery tied to episodes/conditions
- templated, EHR-personalized messages (smart phrases / merge fields) with per-patient language preference
- self-service scheduling/rescheduling links and flows
- multi-channel delivery (text, voice call/IVR, email, app/web links)
- consent/opt-out management, contact preferences, regulated messaging-hours handling
- engagement analytics (deliverability, response, no-show, activation)
- staff roles/permissions and location/department organization

### L2 — Variant / Optional Structure

- payments/balance collection, insurance eligibility (intake-first and SMB poles)
- reputation management, review requests, referral marketing (SMB growth pole)
- bundled patient portal as a family product (present in some vendors, explicitly separate in at least one)
- telehealth visit links/video as an engagement surface
- inpatient/bedside interactive engagement (SmartRoom-class) — one pole's core, absent elsewhere
- structured care journeys/programs across episodes (transitions, chronic-condition programs)
- patient activation scoring instruments (licensed measures)
- payer/member engagement and pharma/life-sciences network use
- AI agents for inbound/outbound voice and text (2026-era layer, present across poles)
- community/population outreach for health-equity programs
- high-volume deliverability machinery (toll-free sending, rate pacing, carrier compliance)

### L3 — Vendor-specific (research notes only)

- Artera: Campaigns (≤30,000 patients per campaign; CSV-of-MRN audience; 10 category taxonomy incl. "Portal Invitation"; pending→queued→running lifecycle; editable only pre-start; TCPA 8AM–9PM practice-timezone constraint; per-hour send-rate slider 1,248/2,496 msg/h ceilings; practice line vs high-volume toll-free; 160/153-char SMS segmentation; Smart Phrases incl. {eventDate}; secure-vs-unsecure messages; Secure Messaging Portal for large attachments), Triggers (Appointment/Inbound/Recall/Referral), Collaborative Inbox, Patient Facesheet, Lines/Events/Resources, Conversation Flows, Self-Rescheduling, Quick Responses, AHFE federal edition.
- GetWellNetwork: Get Well 360, SmartRoom, Hospital Journey Manager, GetWell Loop, O'Neil Center for Patient Engagement Research, FedRAMP/GovCloud federal variant.
- Solutionreach: "created the patient retention and engagement market in 2000", Stella AI Receptionist, DSO/vision-group packaging.
- Phreesia: VoiceAI, PhreesiaOnCall, Patient Activation Measure distribution, MediFind, life-sciences network side, AccessOne.
- TeleVox/WestCX: HouseCalls / HouseCalls Pro lineage, WestCX Orchestrate.
- Updox: Universal Inbox, eFax/Direct Secure Messaging family context, EverHealth parentage.

## Rejected Findings

- **"Patient engagement = patient portal."** Rejected: Updox sells portal and engagement as separate family products; Artera treats portal access as a campaign *category* ("Portal Invitation"), i.e., outreach *about* the portal; GetWell's engagement center is journeys/outreach, not the record window. The portal is a patient-initiated surface; this Type is defined by the provider-initiated loop. (Boundary, not identity.)
- **"Patient engagement = appointment reminders."** Rejected: reminders are the most universal trigger but only one trigger family (recalls, referrals, care gaps, campaigns, journeys, intake are all documented); a reminder service without response capture and staff handling is notification tooling, not this Type.
- **"Patient engagement = marketing/CRM for healthcare."** Rejected: reputation/referral-marketing features appear only at the SMB growth pole; the sampled center of gravity is operational care communication tied to care events, not demand generation. Straddle acknowledged for the SMB pole.
- **"SMS texting is the defining channel."** Rejected: TeleVox's 30-year voice-first lineage and GetWell's inpatient-screen surfaces satisfy the Type without SMS; channels are variant machinery.
- **"AI agents are part of the definition."** Rejected: 2026-era layer present across all six poles but absent from the historical lineage that still satisfies the Type.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (what to remove/keep) |
|---|---|---|
| Patient Portal | adjacent, frequently bundled | Portal = patient-initiated window onto the record and services. Remove this Type's provider-initiated outreach loop and staff-managed response handling → portal. Engagement platforms often *provision* portal access (campaign category "Portal Invitation") rather than *be* the portal. |
| Patient Registration & Intake | overlap (intake-first pole) | Intake = the pre-visit registration workflow of record feeding the chart. Intake is a common capability here (and Phreesia's center). Remove the ongoing outreach loop and keep episodic pre-visit capture → intake system. |
| Patient Scheduling | adjacent, linked | Scheduling owns slot inventory/booking. Engagement links out (self-schedule/reschedule links, reminders about bookings) but does not own the calendar. |
| Care Coordination Platform | adjacent, payer/clinician-side | Care coordination = clinician-managed longitudinal plans/tasks across settings. Engagement = patient-facing activation; GetWell's transitions programs straddle. If the unit of work is the care team's clinical coordination task list → coordination; if it is the patient-side journey/conversation loop → engagement. |
| Population Health Management | upstream sibling | Pop health decides (panel analytics, risk stratification, gap lists); engagement executes the individual-level outreach that closes gaps. GetWell sells both; the seam is decision vs execution. |
| Telehealth Platform | adjacent | Telehealth delivers the visit; engagement products carry telehealth *links* as one action among many. |
| Remote Patient Monitoring | adjacent | RPM owns device-data monitoring loops; engagement captures patient-*reported* data (forms/surveys) without device telemetry. |
| Customer-to-Business Messaging Application | same mechanics, different substrate | C2B messaging = business-customer conversations on public identity; here identity is the patient record, triggers are care events, and PHI/consent/messaging-hours regulation shapes behavior. Healthcare-specific rules and EHR anchoring are the differentiators. |
| Healthcare CRM / marketing platforms (marketplace context, not a single leaf here) | straddle at SMB pole | Reputation/review/referral features sit in this Type's SMB variants but the core loop is care-journey communication, not demand generation. |
| Employee Engagement Platform (§09) | name-parallel only | Same word "engagement", completely different domain (workforce surveys vs patient care loop). No structural confusion. |

**Taxonomy observation:** "Patient Engagement Platform" in the market is an umbrella used for at least four different product centers (messaging hub, journey engine, intake-first operations, growth outreach). The Type is real and stable at the L0 level (all four realize the same three jointly-held structures), but the Directory's neighboring leaves (Patient Portal, Patient Registration & Intake, Care Coordination) each capture one pole's overlap zone. Worth a joint-review note for the intake seam.

## Uncertainties

- EHR-embedded engagement modules (Epic, athenahealth) could not be fetched (403). Their internal structure is inferred only from third-party integration documentation; claims about how EHR-native engagement differs (e.g., MyChart-centric flows) are unverified and kept out of the final document.
- GetWellNetwork's operational mechanics (Loop enrollment, SmartRoom workflow) rest on Tier-2 material only; the patient FAQ was JS-rendered and unreadable.
- Pricing/packaging and precise limits were deliberately not carried into the final document (single-source precision facts stay here).
- Whether the market would consider a pure one-way reminder autodialer "patient engagement": vendors historically marketed some such tools under that banner; this analysis excludes them from the Type (fails the managed-response leg) — a judgment call worth flagging.
- Regional (non-US) products were not sampled; consent/messaging-hours rules cited are US-flavored (TCPA), so the final document treats regulation as "applicable consumer-communication law" rather than naming US statutes.

## Final Synthesis

A Patient Engagement Platform is the care organization's system for actively engaging its identified patients outside the clinical encounter and managing that engagement as operational work. Its defining structure is the jointly-held trio: (1) the provider's patient population anchored in the EHR/PM as the engagement subjects, (2) the two-way engagement loop the provider initiates — outreach triggered by care events, schedules, or programs, answered by patient response and action that closes back into the organization — and (3) the staff-managed work surface where responses are worked, escalated, and tracked. Around that core, mature products add the trigger families (appointments, recalls, referrals, care gaps), broadcast campaigns, intake forms, surveys, education, self-service scheduling, consent/preference machinery, and analytics; variants differ by center of gravity (messaging hub vs journey engine vs intake-first vs growth outreach), customer tier (SMB practice → health system → payer), and care setting (ambulatory, inpatient, transitions, member base). Remove the provider-initiated loop and the product collapses into a patient portal; remove the managed-response surface and it collapses into notification tooling; remove the patient-anchored care context and it collapses into generic business messaging.
