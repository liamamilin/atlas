# Research Notes — Referral Management (Healthcare)

Research date: 2026-09-09
Leaf: Referral Management (§22 Healthcare & Life Sciences)
Slug: referral-management

---

## Research Goal

Understand what healthcare Referral Management software actually is, from real products: what a referral is inside these systems, who works it, how it moves between the referring side and the receiving side, what "closing the loop" means operationally, and where the Type's boundary sits against patient scheduling, care coordination, HIE, prior authorization, EHR-embedded referral orders, and the post-acute referral-growth CRM family.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: Referral Management = the workflow machinery that manages a patient's referral from one provider to another: create/send, receive/triage/accept, schedule, and report back — the "referral loop".
- Likely confusions: Patient Scheduling (booking vs the referral that creates the need), Care Coordination Platform (ongoing program vs discrete handoff), HIE (transport substrate vs workflow object), Prior Authorization (payer approval vs provider handoff), EHR (chart + orders vs cross-org workflow), Referral Marketing Platform (§06 — same word, different domain entirely).
- Pre-hung flags from earlier passes:
  - patient-scheduling pass: "referral = the clinical instruction/order establishing the need for care, scheduling converts an existing need into a booked encounter — expect 'order of record vs slot booking' seam and referral-native routing that bundles booking".
  - HIE pass: drift zone "(b) care-coordination-platform / referral-management / clinical-communication-platform — workflow objects vs the data-exchange substrate".
  - organ-transplant-management pass: "generic referral routing exists inside this Type as intake, but without candidacy/evaluation/listing semantics it is the referral Type, not transplant management".
  - home-health-ehr-management pass: "Referral-growth CRM (post-acute) — adjacent, market-side; manages referral-source relationships and the referral funnel on the marketing side; terminates at handoff, holds no clinical or operational record".
  - prior-authorization pass: "adjacent bundling (referral status, medical-necessity checking, appeals…)".

## Research Questions

1. What is a referral as a system object — order, letter, request, or booking? What does its record carry?
2. Who are the users on each side (referring vs receiving), and what does each do?
3. What is the referral lifecycle and its states? Where do referrals stall and what does the software do about it?
4. What does "closing the loop" mean concretely (acceptance notification, appointment booked, consult result, report returned, reconciliation)?
5. How do the poles differ: EHR-embedded referral feature vs network eReferral platform vs national/regional eReferral service vs network-optimization platform vs post-acute intake management?
6. What role do directories, provider data, wait times, and availability play?
7. Where does the patient appear (booking, reminders, alerts) — and is that definitional or common?
8. What regulatory machinery shapes the Type (US MIPS "electronic referral loops", NHS patient choice + 18-week RTT, provincial eReferral programs)?
9. Do older/regional/paper-era referrals still fit the definition?
10. Where is the seam to eConsult (advice without care transfer)?

## Representative Products

Selected for market representativeness, documentation accessibility, and pole diversity:

| Product | Pole | Customer tier / geography | Evidence level reached |
|---|---|---|---|
| RXNT (EHR referral feature) | EHR-embedded referral as document/order | US SMB ambulatory practices | Tier-1 (public help-center articles) |
| OceanMD (Ocean Provider Network) | Regional network eReferral platform | Canada (provincial programs; Ontario) | Tier-2 product pages + Tier-1 vendor case study |
| NHS e-Referral Service (eRS) | National eReferral service with patient booking | England (public health system) | Tier-1 (patient-facing NHS pages; clinician docs unreachable) |
| Lightbeam Health (CarePort lineage) | Network referral management / optimization | US health systems, ACOs, post-acute networks | Tier-2 (solution pages + case study summary) |
| AristaMD | Referral triage + eConsult routing | US provider orgs, plans, ACOs | Tier-2 (solution pages) |
| Trella Health (Community / Discharge) | Post-acute receiving-side referral management (+ growth CRM sibling) | US post-acute providers & hospitals | Tier-2 (solution pages + FAQ) |
| Kyruus Health | Boundary anchor: care access platform (provider data/search/scheduling) | US health systems & plans | Tier-2 (homepage/solution nav) |

Rejected/unreachable samples (recorded per source-access rules): Luma Health (lumahealth.io 403), ReferralMD (getreferralmd.com 403), athenahealth (403), Epic/Oracle Health (not publicly documented at operational level), Ensocare (transport error), digital.nhs.uk clinician-side eRS documentation (403, domain-wide), Ocean support portal (transport error ×2), AdvancedMD (403), Practice Fusion (403), Ontario Health (403), eClinicalWorks (reachable but no dedicated referral module documentation — population-health wheel mentions "Referral Network, Care Coordination Connector" only).

## Sources

- RXNT Help Center — "Manage Referrals": https://help.rxnt.com/hc/en-us/articles/360063828013-Manage-Referrals (fetched 2026-09-09)
- RXNT Help Center — "Quality & Compliance Reports" (MIPS Promoting Interoperability, electronic referral loops measures): https://help.rxnt.com/hc/en-us/articles/21402681219351-Quality-Compliance-Reports (fetched 2026-09-09)
- OceanMD — Ocean Provider Network (eReferrals): https://www.oceanmd.com/ocean-provider-network/ (fetched 2026-09-09)
- OceanMD — Solutions for Healthcare Systems: https://www.oceanmd.com/healthcare-systems/ (fetched 2026-09-09)
- OceanMD — homepage/platform overview: https://www.oceanmd.com/ (fetched 2026-09-09)
- OceanMD Stories — SCIBD case study ("How SCIBD Reduced Referral Friction and Appointment Confirmation Work with Ocean"): https://stories.oceanmd.com/stories/how-scibd-reduced-referral-friction-and-appointment-confirmation-work-with-ocean (fetched 2026-09-09)
- NHS — "Book an appointment using the NHS e-Referral Service": https://www.nhs.uk/using-the-nhs/nhs-services/hospitals/nhs-e-referral-service/ (fetched 2026-09-09)
- NHS — "Referrals for specialist care": https://www.nhs.uk/nhs-services/hospitals/referrals-for-specialist-care/ (fetched 2026-09-09)
- NHS — Manage Your Referral service (refer.nhs.uk): https://refer.nhs.uk/ (fetched 2026-09-09)
- Lightbeam Health — Referral Management: https://lightbeamhealth.com/referral-management/ (fetched 2026-09-09)
- Lightbeam Health — homepage: https://www.lightbeamhealth.com/ (fetched 2026-09-09)
- AristaMD — homepage: https://www.aristamd.com/ (fetched 2026-09-09)
- AristaMD — eConsults: https://www.aristamd.com/specialty-care/care-delivery/econsults/ (fetched 2026-09-09)
- AristaMD — Care Delivery: https://www.aristamd.com/specialty-care/care-delivery/ (fetched 2026-09-09)
- Trella Health — Referral Management (Trella Community): https://www.trellahealth.com/solutions/referral-management (fetched 2026-09-09)
- Trella Health — homepage: https://www.trellahealth.com/ (fetched 2026-09-09)
- Kyruus Health — homepage/solution nav: https://kyruushealth.com/ (fetched 2026-09-09)

## Product Observations

### RXNT (EHR-embedded referral feature) — evidence layer A (Tier-1 help center)

From "Manage Referrals":
- A referral is created **from the patient dashboard**: navigation menu → *Referrals* → **+Add**. The referral is patient-anchored from the start.
- **Referral destination** is chosen as either an **Institution or a Provider**, picked from an address book of saved referral providers/institutions or entered new at creation time. Search fields; "blue plus sign" to add a new destination with contact fields.
- **Referral details** are completed on a form, then **Preview**; then **Save & Send** ("to have the form faxed to the number entered above") or **Save & Print** (PDF). "For both options, the referral will be saved on the patient dashboard."
- **Regional form variants**: "If you are located in Maryland or Michigan, your referral forms will look slightly different." — jurisdiction-specific referral forms exist inside one product.
- **View referrals**: existing referrals display in a list on the patient dashboard; click the page icon to view the existing referral.
- **Favorite referral providers/institutions**: a per-user address book of referral favorites (Providers tab / Institutions tab), managed under utility menu → Medication Management → Manage Favorites.
- From "CCD Export": referral records are filterable by "Referred To or Referred By details" — the record carries both directions.
- From "Electronic Health Information Export Guide": exports include "patient documents, legacy encounters, smart forms, referrals, labs, and faxes" — referrals are a first-class patient-record object class.

From "Quality & Compliance Reports" (MIPS Promoting Interoperability):
- **"Support electronic referral loops by sending health information"** — denominator: "unique patients that had a transition of care or referral sent by the provider"; numerator: patients "who have also had a CCD chart summary successfully sent from the provider via direct email."
- **"Support electronic referral loops by receiving and reconciling health information"** — denominator: "unique patients that had a transition of care or referral received by the provider… based on the number of patients with the Referred by section completed in their demographics"; numerator: patients "who have also had a CCD chart summary received by the provider via direct email and reconciled to their patient chart. Reconciliation… is based on allergies, medications, and problems having each been reviewed with the external source data tool and updated as needed."
- Interpretation: the US regulatory frame defines the referral loop as **send + receive-and-reconcile** — the referral is complete when the clinical summary has crossed and been reconciled into the receiving chart. Also: denial code CO-237 "Authorization or referral issue" appears in the billing workflow — referrals touch the revenue cycle.

### OceanMD / Ocean Provider Network (regional network eReferral) — evidence layer A (Tier-2 pages + Tier-1 case study)

From the Provider Network page:
- Ocean is "Canada's digital gateway for healthcare"; the Provider Network lets clinicians "send or receive any type of eRequest, including eReferrals, eConsults, eOrders and eSubmissions" — the referral is one class of a broader eRequest family.
- **Healthmap**: "a comprehensive, map-based directory" of health services — "Easily find specialists and health services; Sort by up-to-date wait times or distance". The directory is the discovery layer feeding referral destination choice.
- "The Ocean Provider Network makes it easy to find healthcare services, **send and receive eRequests, and track the status of Requests, without leaving your HIS**" (EMR-integrated). "With eReferrals, you can eliminate paper and faxes, while reducing errors and rejected requests."
- For health systems: "improves **load balancing** to reduce wait times, while increasing adherence to evidence based standards. With system-wide analytics and data transparency…"
- For patients: "automated alerts that **track and manage their referrals, appointment times and details**."
- Scale claims: 170K+ monthly eReferrals; 2M+ eReferrals sent per year; "50+ day reduction in avg. wait times" (vendor claims — recorded as vendor claims).
- Quote from a family doctor: "I booked an urgent abdominal ultrasound for my patient and sent it via Ocean – MyHealth Centre called her while she and I were still talking in the appointment!" — referral → booking speed as the value story.

From the SCIBD case study (receiving side, specialist clinic):
- **Before state (fax era)**: "Staff had to keep checking for new faxed referrals; New patient records and files required manual handling; **Referral acceptance updates had to be sent manually**; Appointment confirmations required repeated calls and emails; Manual entry of appointment details created the possibility of mistakes."
- **After state**: "New referrals trigger staff notifications, referral information moves into the patient file, **referring physicians receive acceptance updates**, and appointment confirmations are sent automatically."
- The receiving clinic gets notified of new referrals; referral info auto-files into the patient record; the referrer is notified on acceptance; patients get automated confirmations. This is the loop, concretely.

From Solutions for Healthcare Systems:
- Standards-based interoperability (HL7 FHIR named), deep EMR integrations, "Proven to reduce patient wait times", "Export detailed usage reports and publish wait times", "Automatically collect patient experience data".

### NHS e-Referral Service (national eReferral, England) — evidence layer A (Tier-1 patient-facing)

From "Referrals for specialist care":
- The referral is a **letter**: "A specialist will only see you with a letter of referral from your GP. The letter will give the specialist essential background information, such as your medical history, and it'll also contain details that the specialist needs to pay particular attention to."
- Referral is clinician-gated: "whether you'll get the referral depends on what your GP feels is clinically necessary"; "Generally, you cannot self-refer to a specialist at a hospital within the NHS" (exceptions: sexual health clinics, A&E).
- **Patient choice**: "you may have the right to choose which hospital in England to go to for your first outpatient appointment… You can also choose which consultant-led team will be in charge of your treatment."
- **Booking through eRS**: "Once you have decided on a hospital, you could book your first outpatient appointment through the NHS e-Referral Service. This can happen in the following ways: your GP can book it while you're at the surgery; you can book it online using the appointment request letter your GP gives you; you can phone the NHS e-Referral Service line…"
- **Regulatory clock**: "if your GP refers you for a condition that's not urgent, you have the right to start treatment led by a consultant within 18 weeks from when you're referred" (NHS Constitution).
- Loop closure in correspondence practice: "When doctors write to each other about your care, they should aim to give you a copy of their letters or emails." Also: "your GP is not obliged to accept the specialist's recommendations" — the referrer retains clinical authority over the returned advice.

From "Book an appointment using the NHS e-Referral Service" + refer.nhs.uk:
- Patient-facing portal **"Manage Your Referral"**: patient needs "booking reference number" + "password or access code"; can "check your appointment details, change your appointment, cancel your appointment, cancel your referral."
- NHS App can also be used to book/manage the appointment.
- Choice criteria presented to patients: wait time for first appointment, how quickly treatment can start, distance.

### Lightbeam Health — Referral Management (network optimization pole) — evidence layer A (Tier-2)

- Positioning: "transforms how organizations **route, track, and optimize referrals**, using real-world cost, quality, and performance data to improve outcomes, **reduce leakage**, and strengthen network performance."
- Problem framing: "a **referral blind spot**… Manual workflows and limited performance insight lead to delays, **out-of-network referrals**, and missed value-based opportunities." Named failure modes: "Inefficient Referral Workflows — Manual coordination leads to delays, **lost referrals, and missed follow-ups**"; "Poor Referral Visibility — Organizations lack insight into **referral completion, leakage, and outcomes**"; "Limited Interoperability"; "Administrative Burden & Compliance Risk — Manual documentation increases staff workload and **audit exposure**."
- Features: "**Intelligent Provider Selection** — Stack-rank specialists based on cost, quality, and patient satisfaction—not just familiarity"; "**Enhanced Patient Engagement** — Automate referral follow-ups with appointment reminders and satisfaction surveys"; "**Seamless EMR Integration** — Embed referral intelligence directly into your existing EHR workflows"; "Market Expansion Planning".
- "The Lightbeam Difference": "Where traditional referral tools **stop at task management**, Lightbeam delivers true optimization"; "**Automate bi-directional referral coordination** across networks"; "Gain real-time visibility into referral leakage and cost drivers."
- Case study (Vanguard Medical Group): "no process to **close the loop** or measure the clinical and financial impacts" before; after: "75% Reduction in Referral Leakage… 100% Increase in Outbound Referral Visibility… 64% Increase in Patient Engagement" (vendor claims).

### AristaMD (referral triage + eConsult pole) — evidence layer A (Tier-2)

- The referral enters through the EHR: "**Send a Referral in Your EHR** — A patient is presenting with a complex issue that you'd like to refer out… AristaMD's specialist panel will have a recommendation within 24 hours" (vendor claim).
- **Human triage layer**: "AristaMD Nurse Creates eConsult — Our team of Registered Nurses curates and submits a thorough eConsult Request on your behalf by including test results, visit notes, labs, and other relevant details from your EHR."
- **Routing decision**: "the nurse manager determines where to route the patient for specialty care—**eConsult, video consultation, or in-person visit**" using "an evidence-based care plan specific to the condition."
- **Outcome returns to the referrer**: "Specialist Submits Response — One of our board-certified specialists provides a detailed recommendation for treatment"; then "PCP Treats Patient… many times eliminating the need for a face-to-face visit or helping better prepare for appropriate pre-visit workups when a referral is necessary."
- eConsult as referral *avoidance*: "Reduce routine clinical referrals by >70%" (vendor claim); eConsults "eliminate unnecessary face-to-face visits."
- Care Support: "care coordinators to perform patient intake, routing, and scheduling… nurse managers to select the appropriate care setting."

### Trella Health — Community (post-acute receiving-side referral management) — evidence layer A (Tier-2)

- Positioning: "Real-time visibility. Faster referral conversions." — "Trella gives teams the visibility to prioritize opportunities, coordinate next steps, and reduce delays across the **intake process**."
- **Referral visibility & prioritization**: "See incoming referrals, pending placements, and patient needs in one workflow"; "Receive and manage incoming referrals in a centralized workflow. Help intake teams review key patient details, understand **referral source context**, and move each opportunity toward the next step."
- **Patient review**: "Evaluate patient fit based on care needs, service capabilities, **payer context, and admission readiness**."
- **Referral prioritization**: "Identify which referrals need immediate attention, which require follow-up, and which are ready for admission."
- **Availability confirmation**: "Confirm through the portal when your agency is available for new patients" — receiving-side capacity signaling toward the referring hospitals.
- **Alerts**: "Mobile alerts — Notify the right team members when new referrals arrive or when referral status changes"; email notifications including "was selected by a patient at Taylor Mercy Hospital… requesting a response to the referral as soon as possible."
- **Provider profiles** ("Community Page"): agencies showcase "services, locations, care capabilities… quality, outcome, and performance information" to "hospital partners and patients."
- **Two-sided pairing**: "Trella Discharge helps hospitals send better-fit referrals faster. Trella Community helps post-acute providers **receive, review, respond**, and communicate availability in real time. Together, they connect **both sides of the referral flow**."
- FAQ: "see incoming referrals, **track referral status**, prioritize next steps"; "understand **which sources are sending referrals, which referrals convert, and where delays or leakage may be happening**."
- Sibling product **Trella CRM** = referral-source relationship management (sales reps/liaisons, territory planning) — the growth-CRM pole, distinct from intake management.

### Kyruus Health (boundary anchor: care access platform) — evidence layer A (Tier-2)

- Current solution set: Provider Data Management, Reach (listings), Search (directory/care search), Schedule (patient self-scheduling with EHR integration), Check-In (digital intake/payment), APIs, Analytics. **No referral-management module in the current lineup.**
- Confirms the seam: provider data + search + scheduling = the *access* layer that referral management sits beside and consumes; the referral workflow object (request → acceptance → outcome) is not Kyruus's center of gravity.

## Cross-product Comparison

| Dimension | RXNT (EHR feature) | Ocean (network) | NHS eRS (national) | Lightbeam (network optimization) | AristaMD (triage+eConsult) | Trella Community (post-acute intake) |
|---|---|---|---|---|---|---|
| Referral object | Patient-anchored referral record + generated form (fax/print) | eRequest (eReferral class) with status | Referral letter + booking reference | Tracked referral with cost/quality context | Referral request curated into eConsult/visit request | Incoming referral record with source context, payer context, status |
| Destination selection | Address book (provider/institution favorites) | Healthmap directory (wait times, distance) | Patient choice of hospital/consultant; GP books | Stack-ranked by cost/quality/satisfaction | Nurse routes to eConsult/video/in-person panel | Hospitals send; agency profiles + availability signal capacity |
| Sending mechanism | Fax or print (PDF); saved to dashboard | Electronic, EMR-integrated, no fax | GP books at surgery / patient books online / phone | EMR-embedded, bi-directional | EHR referral → AristaMD platform | Electronic referral from hospital discharge systems |
| Receiving-side work | (Receiving side out of scope for the feature; "Referred by" demographics + CCD reconciliation per MIPS) | Notification of new referral; acceptance updates; auto-file to patient record | Provider accepts booking; appointment managed | Completion/leakage visibility | Nurse triage; specialist responds with recommendation | Intake worklist: review, prioritize, accept/respond, admission |
| Loop closure | MIPS loop measures: send CCD / receive-and-reconcile CCD | Acceptance notification to referrer; patient alerts | Specialist letters back to GP (correspondence norm); GP may reject recommendations | "Bi-directional referral coordination"; close the loop | Specialist recommendation returned to PCP | Response to referral requested; conversion tracked |
| Patient-facing surface | None in the referral feature | Automated referral/appointment alerts | Manage Your Referral portal + NHS App (book/change/cancel) | Appointment reminders, satisfaction surveys | None surfaced (nurse-managed) | Patient selection of agency (via hospital-side flow) |
| Analytics | MIPS loop performance rates | System-wide analytics, wait-time publishing, load balancing | 18-week RTT clock (regulatory) | Leakage, completion, cost drivers, network expansion | Referral reduction (>70% claim), quality metrics | Conversion by source, delays, leakage |
| Regulatory frame | US MIPS Promoting Interoperability | Provincial eReferral programs (Canada) | NHS Constitution (18 weeks), patient choice | US VBC/ACO context | NCQA-guided specialist panel | US post-acute market (claims-based intelligence) |

**Cross-product commonalities (evidence layer B):**
1. Every sampled product holds a **referral record bound to a specific patient**, a **referring party**, and a **destination** (provider/institution/service), carrying reason/context.
2. Every sampled product treats the referral as **having a status that advances** and being **workable from both sides** (send side and receive side appear as distinct roles or modules — Trella even sells the two sides as separate products).
3. Every sampled product or its regulatory frame expresses **loop closure**: acceptance updates (Ocean), recommendation returned (AristaMD), letters back (NHS), send+receive-and-reconcile (US MIPS via RXNT), bi-directional coordination (Lightbeam), response requested (Trella).
4. **Stalled-referral management** is a named concern everywhere: "lost referrals, missed follow-ups" (Lightbeam), "keep checking for new faxed referrals" (SCIBD before-state), "which require follow-up" (Trella), "track the status" (Ocean).
5. **Directories/provider data** feed destination choice in the network poles (Ocean Healthmap, Lightbeam stack-ranking, Trella profiles, NHS choice) — but the thin pole (RXNT) runs on a plain address book, so the directory is common, not definitional.
6. **Patient-facing surfaces** appear in 3 of 6 (Ocean alerts, NHS portal, Lightbeam reminders) and are absent in 3 (RXNT, AristaMD, Trella) — common-mature, not definitional.
7. **Analytics** split into two families: operational (status, conversion, delays) and network/financial (leakage, cost, quality) — the second is VBC-context variant.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The healthcare Referral Management Type is held up by **three jointly-held structures**:

1. **The referral as the unit of record.** A persistent, individually identified request for care that binds a specific **patient**, a **referring party**, and a **receiving provider/service/destination**, and carries the **reason/clinical context** for the request. It holds a status that advances. Remove it → a referral letter template, correspondence, or a demographics field.
2. **The two-sided managed handoff.** The referral is created and sent on the **referring side** and received and worked on the **receiving side** — triaged, accepted or declined, scheduled or answered — with both sides present as parties the system distinguishes (roles, modules, or separately sold products). Remove it → one-way document transmission (fax a letter) or generic secure messaging.
3. **The tracked progression to a recorded outcome.** The referral's state advances through defined stages; stalled referrals surface for follow-up; the journey ends in a **recorded outcome** — appointment made, consult answered, admission completed, or a recorded decline/cancellation — communicated back toward the referrer (**closing the loop**). Remove it → the "referral blind spot": untracked correspondence with no completion visibility.

Jointly-held load-bearing:
- 1 alone = referral letter generator / document store
- 2 without 1 = secure messaging or fax transport
- 3 without 1+2 = generic task tracker
- 1+2 without 3 = untracked correspondence (the fax era's failure mode, as named by the vendors themselves)
- 1+3 without 2 = a tracker with no counterparty workflow
- 2+3 without 1 = messaging with read receipts and no care semantics

### L1 — Common Mature Structure (standard capabilities, not definitional)

- **Provider directory / destination discovery** — searchable directory of providers/services with relevance data (wait times, distance, quality, capabilities); per-user favorites/address books at the thin pole.
- **Referral worklists with prioritization** — inbound/outbound queues, "needs attention / needs follow-up / ready for next step" triage views.
- **Status notifications between parties** — acceptance/decline updates to the referrer; new-referral and status-change alerts to the receiver (push/email/mobile).
- **Appointment linkage** — booking or confirmation attached to the referral; automated appointment confirmations/reminders to patients.
- **Clinical context assembly** — reason for referral, history, test results, notes assembled into the referral (structured forms at the thin pole; curated packets at the triage pole).
- **Document/report return** — consult notes, clinic letters, CCD summaries returned and (in the regulatory form) reconciled into the receiving/referring chart.
- **Operational analytics** — referral volume, conversion, time-to-appointment, completion rates, source mix.

### L2 — Variant / Optional Structure

- **Patient-facing booking and choice** — patient self-service booking against the referral (NHS eRS "Manage Your Referral", NHS App), patient choice of provider; automated patient referral/appointment alerts (Ocean). Distinctive of national/regional and engagement-oriented poles; absent at the thin and triage poles.
- **Network optimization layer** — stack-ranked provider selection by cost/quality/satisfaction, leakage measurement and reduction, network expansion planning (Lightbeam; VBC/ACO context).
- **eConsult routing** — triage that resolves the referral into a virtual specialist consultation instead of a face-to-face visit (AristaMD; Ocean eConsults as a sibling eRequest class). eConsult is an *outcome* of referral triage, not the Type's identity.
- **Post-acute intake shape** — receiving-side referral management with availability confirmation, agency profiles, patient-fit review against service capabilities and payer context (Trella Community; the CarePort lineage).
- **Human triage services** — nurse managers/curators who assemble and route referrals (AristaMD) — service-wrapped variant.
- **Transport substrate** — fax/print (legacy), Direct secure messaging with CCD (US regulatory path), FHIR-based network exchange (Ocean), national service infrastructure (NHS). The transport is pluggable; the workflow object is the invariant.
- **Regulatory machinery** — US MIPS "electronic referral loops" send/receive-and-reconcile measures; NHS 18-week RTT clock and patient choice rights; provincial eReferral program rules (Canada); jurisdiction-specific referral forms (RXNT: Maryland/Michigan variants).
- **Load balancing / wait-time publishing** — system-operator capabilities (Ocean for provincial systems).
- **Referral-source growth machinery** — CRM for referral-source relationships (Trella CRM sibling; PlayMaker-class) — adjacent Type, sometimes sold beside.

### L3 — Vendor-specific (research notes only)

- RXNT: referral favorites live under "Medication Management → Manage Favorites" (quirky menu placement); "Save & Send" faxes the form; Maryland/Michigan form variants; CO-237 denial code ("Authorization or referral issue") in the billing workflow.
- Ocean: "eRequest" umbrella (eReferrals/eConsults/eOrders/eSubmissions); "Healthmap" brand for the directory; vendor scale claims (170K+ monthly eReferrals, 2M+/year, "50+ day reduction in avg. wait times") — vendor claims, not independently verified.
- NHS: "Manage Your Referral" portal (refer.nhs.uk) with booking reference + password/access code; phone booking line with published hours; NHS App integration; appointment request letter as the patient's booking token.
- Lightbeam: "IdealMATCH" scoring brand; Vanguard case-study figures (75% leakage reduction, 100% outbound visibility increase, 64% engagement increase) — vendor claims.
- AristaMD: "SpecialtyCare360" suite framing (Care Delivery / Care Support / Care Design / Performance Oversight); ">50% of eConsult cases returned within 4 hours" and ">70% reduction in routine clinical referrals" — vendor claims; NCQA-guided panel curation.
- Trella: "Community" (intake) vs "Discharge" (hospital side) vs "CRM" (growth) product split; "46.9% average increase in monthly referral volume", "2x patient selections for premium profiles" — vendor claims.

## Vendor-specific Findings

See L3 above. The most structurally interesting vendor facts:
- Trella sells the two sides of the referral flow as **separate products** (Discharge for hospitals, Community for post-acute) — market evidence that the two-sided handoff is one Type with two party-roles, not two Types.
- RXNT's referral feature is **document-centric** (form → fax/print) yet still satisfies the core via the patient-anchored record, destination selection, saved list, and the regulatory loop measures — evidence that the delivery transport is a variant, not the invariant.
- The US regulatory frame (via RXNT's MIPS documentation) defines the referral loop **in two halves** (send; receive-and-reconcile) — the same two-sided structure the network products implement as notifications and returned reports.

## Boundary Findings

| Neighboring Type | Seam | Test |
|---|---|---|
| **Patient Scheduling** | Referral = the clinical request establishing the need for care (order of record); scheduling = converting an existing need into a booked encounter (slot inventory). Referral-native products bundle booking (NHS eRS books; Ocean confirms; Trella tracks "ready for admission") — the appointment is the referral's *outcome*, not its center. | Remove the referral record and keep slot booking → Patient Scheduling. Add a managed request-for-care record ahead of booking → this Type. (Discharges the patient-scheduling pass's forward flag from this side.) |
| **Care Coordination Platform** | Care coordination runs an ongoing program/plan around a patient across encounters; referral management moves one discrete handoff to a recorded outcome. Referrals appear *inside* care coordination as task types (chronic-care-management doc lists "referrals" among coordinated tasks). | Ongoing program with plan + recurring documented service → Care Coordination; discrete provider-to-provider handoff → this Type. |
| **Health Information Exchange / HIE** | HIE = the data-exchange substrate (identity linkage, document semantics, permitted purposes); referral management = the workflow object riding on any transport (fax, Direct, FHIR, national service). The MIPS loop measures show the seam: the *exchange* (CCD via Direct) is the transport half; the *referral record and its states* are the workflow half. | Remove the workflow object, keep exchange → HIE. Remove the exchange, keep the workflow (fax/print pole) → still this Type. |
| **Prior Authorization Platform** | PA = payer-facing coverage approval (request → determination → authorization of record); referral = provider-to-provider care handoff. Some regimes couple them (referral requiring plan approval); the prior-auth pass recorded "referral status" as adjacent bundling. | Decision party is the payer about coverage → PA; the counterparty is another provider about care → this Type. |
| **EHR (Electronic Health Record)** | The EHR holds the chart and can create referral orders/letters; Referral Management is the cross-organization workflow machinery around the referral. An EHR-embedded referral feature satisfies this Type when it carries the referral record + destination + tracking (RXNT does); a bare letter template does not. | Chart-centered documentation → EHR; the referral's journey across parties as the managed object → this Type (embedded or standalone). |
| **Referral-growth CRM (post-acute)** | Growth CRM manages referral *sources* as accounts (liaison visits, territory planning, funnel) and terminates at handoff; referral management works the referral itself to a recorded outcome. Trella sells both as separate products (CRM vs Community) — the vendor's own split is the seam. (Consistent with the home-health pass's recorded seam.) | Relationship/funnel object = CRM; patient-anchored handoff object = this Type. |
| **Referral Marketing Platform (§06)** | Same word, different universe: customer referral programs (advocate → share → attributed conversion → reward) vs healthcare care handoffs. No shared objects, users, or workflows. Naming collision only; no taxonomy action. | Participants are consumers/advocates → §06; participants are providers/patients → this Type. |
| **Organ Transplant Management** | Transplant intake *contains* referral routing but binds it to candidacy/evaluation/listing semantics (the transplant pass recorded this seam from its side). | Generic referral routing without candidacy machinery → this Type; candidacy/evaluation/listing → transplant. |
| **eConsult services** | eConsult = specialist advice without transferring the encounter (PCP keeps the patient); referral = arranging the encounter/care transfer. In sampled products eConsult is a *routing outcome* of referral triage (AristaMD nurse routes to eConsult to avoid the visit; Ocean lists eConsults beside eReferrals). | Advice returned, care stays with referrer → eConsult capability; encounter arranged at the destination → this Type. |

## Uncertainties

- **Standalone US referral-management SaaS pole not directly sampled**: Luma Health and ReferralMD (the frequently cited pure-plays) were unreachable (403). That pole is evidenced indirectly through Lightbeam (network referral management) and Trella (intake management). Worklist/status vocabularies specific to that pole are not asserted.
- **NHS eRS clinician-side operational detail not sampled**: digital.nhs.uk (403, domain-wide) hosts the clinician-facing manuals; evidence is patient-facing Tier-1 plus structural reasoning. Clinician-side state names and triage mechanics not asserted.
- **Ocean support portal unreachable** (transport error ×2): step-level eReferral workflow not sampled; Ocean evidence is product-page + case-study level.
- **Enterprise EHR referral modules** (Epic, Oracle Health, athenahealth): login-gated or unreachable; the enterprise pole is held at realization-level assertions only, consistent with prior §22 passes.
- **Exact status vocabularies vary by product and regime**; no universal state-name set is asserted anywhere in the final document.
- **Vendor performance figures** (leakage reduction %, wait-time reduction, eConsult turnaround) are recorded as vendor claims in research notes only; none are reproduced as facts in the final document.
- **Payer-gated referral authorization** (US plans requiring referral approval) was not directly documented in the sampled sources; held as structural reasoning from the prior-authorization pass's adjacency note, not asserted as standard behavior.

## Final Synthesis

Referral Management software is the **provider-to-provider care-handoff system**: it holds the referral as a persistent, patient-anchored request for care (patient + referrer + destination + reason + status), moves it through a managed two-sided handoff (created/sent on the referring side; received, triaged, accepted or declined, scheduled or answered on the receiving side), and tracks it through defined states to a recorded outcome that closes the loop back toward the referrer.

Everything else commonly associated with the category — provider directories with wait times and quality scores, patient-facing booking portals, leakage analytics, eConsult routing, availability confirmation, automated reminders, regulatory loop reporting — makes the handoff work better in specific markets and regimes but is not what makes the software a referral management system. The paper-era referral (GP's letter + specialist's waiting list + the consult letter back, with pending-referral lists kept by both offices) satisfies the same three-part core with no software at all, and the fax era — which the sampled vendors themselves describe as the failure mode ("lost referrals, missed follow-ups", "keep checking for new faxed referrals") — shows what the Type looks like when the third leg (tracked progression to a recorded outcome) is missing: that is the "referral blind spot" the category exists to close.

The Type is realized across four product shapes that share one core: the EHR-embedded referral feature (document/order-centric, thin), the regional/national network eReferral service (directory + booking + system analytics), the network optimization platform (leakage/cost/quality intelligence over the same workflow), and the post-acute intake management product (receiving-side worklists + availability + conversion). The two-sided handoff is sometimes sold as two products (Trella Discharge + Community) — market evidence that the two party-roles are one Type, not two.
