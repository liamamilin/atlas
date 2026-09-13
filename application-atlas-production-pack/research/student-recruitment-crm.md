# Research Notes — Student Recruitment CRM

Research date: 2026-09-09

## Research Goal

Understand what a Student Recruitment CRM actually is as an Application Type: what objects exist inside it, who uses it, how the recruitment work flows through it, what states and rules matter, and where its boundaries sit against Admissions Management, Enrollment Management, generic CRM, Marketing Automation, and the SIS family.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: software used by colleges/universities (and schools) to manage prospective students from first contact (inquiry/prospect) through application and enrollment decision — the "funnel" system.
- Likely users: admissions counselors/recruiters, enrollment marketing staff, events staff, admissions directors.
- Likely confusion points:
  - Admissions Management (application processing/review) — adjacent sibling leaf, already processed 2026-09-06.
  - Enrollment Management (commitment/readiness for the period) — sibling leaf, processed 2026-09-07; that pass explicitly held "recruitment marketing (Student Recruitment CRM)" as NOT definitional to its Type and flagged an interlock for this pass.
  - Generic CRM (§07) — same object family (person records + pipeline), different domain semantics.
  - Marketing Automation Platform — campaign machinery overlap.
  - Student Information System — the enrolled-student system of record; handoff seam.
- Unknowns going in: whether the Type requires application-processing machinery or only the pre-application relationship; how strong the "purchased name lists" (search lists) pattern is; regional variation (US search-list culture vs UK/EU UCAS/fair culture).

## Research Questions

1. What is the unit of record — how do products model the prospective student?
2. What lifecycle/stages do products define on that record (prospect → inquiry → applicant → admitted → deposited/enrolled)?
3. How do prospects enter the system (inquiry forms, purchased search lists, test-score files, imports, events)?
4. What outreach machinery exists (campaigns, drip sequences, one-off communications, two-way inbox, telemarketing)?
5. What event machinery exists (campus visits, open days, fairs, interviews, appointments, check-in)?
6. What counselor/recruiter work surfaces exist (territories, travel, tasks, notes, scoring)?
7. What segmentation and analytics exist (queries/populations/segments, funnel/yield reports)?
8. How far into application processing do these products go (hosted applications, review, decisions) — and where is the seam with Admissions Management?
9. What integrations anchor the Type (SIS, test-score providers, centralized application services, payment gateways)?
10. What varies by region/segment (US vs UK/EU, undergraduate vs graduate, K-12, community colleges)?

## Representative Products

Selected for market representation, documentation depth, different product philosophy, and different customer tiers/geographies:

1. **Technolutions Slate** — dominant US higher-ed admissions/recruitment CRM; exceptionally deep public knowledge base (Tier 1).
2. **TargetX (Liaison)** — Salesforce-platform-based higher-ed CRM; public help center (Tier 1) + product pages (Tier 2).
3. **Element451** — modern AI-native enrollment CRM; product/feature pages (Tier 2).
4. **Full Fabric** — UK/European higher-ed platform (CRM + Admissions + SIS modules); product pages (Tier 2) + Intercom help center (Tier 1).

## Sources

- Slate Knowledge Base (knowledge.technolutions.net / knowledge.technolutions.com): Roadmap Step 2: Outreach; Deliver Overview; Populations; College Board Search; Create a Trip; Constituent Record (Advancement); Person Record Overview; Behavior-Based Application Outreach (behavioral nudges); llms.txt documentation index. Fetched 2026-09-09.
- Technolutions root site (technolutions.com): product positioning (Admissions / Student Success / Advancement). Fetched 2026-09-09.
- TargetX Help Center (help.liaisonedu.com): TargetX Help Center index; TargetX Recruitment Manager; Recruitment Manager Overview. Fetched 2026-09-09.
- Liaison product pages (liaisonedu.com): TargetX root; TargetX Recruitment and Admissions. Fetched 2026-09-09.
- Element451 product pages (element451.com): root; /product/people (Contact Database); /product/campaigns; /product/events; /product/applications-decisions. Fetched 2026-09-09.
- Full Fabric (fullfabric.com): root; /products/higher-education-crm. Help Center (help.fullfabric.com): Data Management collection; Quick start — Profiles. Fetched 2026-09-09.
- Cross-reference: STATUS.md entries for admissions-management (2026-09-06), enrollment-management (2026-09-07), recruitment-marketing-platform (2026-09-07), financial-aid-management (2026-09-07), student-billing-system (2026-09-09).

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

---

## Product A — Technolutions Slate (Tier 1: knowledge base)

### Key observations

- **Positioning (A, Tier 2 root):** "Slate for Admissions defines higher education CRM systems, explicitly designed to optimize communications, streamline application processing, and simplify decision release." Sells Admissions + Student Success + Advancement from one platform; 2,000+ institutions claimed (marketing number, not asserted in final doc).
- **Person record as hub (A):** Knowledge base: "Records — Applicants, students, and alumni." The record ties together forms, events, imports; tabs include Dashboard, Timeline (chronological actions/interactions/communications), Profile (biographical data, contact info, relationships), Materials. (Constituent Record doc is advancement-facing but describes the same person-scoped record architecture; person record docs for admissions are video-led.)
- **Inquiry form as the entry point (A):** Implementation roadmap: "it's hard to manage records in two systems at once… this usually hinges on your inquiry form… before publishing your inquiry form or redirecting ongoing feeds like search lists to create new records in Slate." Inquiry form + ongoing feeds (search lists) are the two named population inflows.
- **Purchased name lists / search services (A):** "College Board Search" doc: source formats (Student Search Service fixed-width), a person-scoped "unique for merging" College Board ID field, remapping, retroactive refresh, "Living Record" licensed updates. Confirms the search-list import machinery with identity matching/merging.
- **Deliver — outbound communications engine (A):** "email, SMS, print, and voice communications… drip marketing campaigns, manage communications, and track the overall success." One-off, automated for a time span, or indefinite ("send an email from the Alaska representative at your institution" — rep-personalized ongoing sends). Merge fields, content blocks, Liquid markup, Deliver templates. Slate Print (partner print operation), Slate Voice (integrated telephony), Slate Video. Slate Credits cover third-party communication fees.
- **Drip campaigns ride on populations (A):** Populations doc: "a group of records with like attributes… assigned a common label… through population rules"; records enter/leave dynamically as rules evaluate; used "as the foundation for drip marketing campaigns," as query filters, and for record access. Timestamp Days filter ("day zero") supports time-based sequences.
- **Two-way inbox (A):** "Inbox is a tool that lets you directly manage email accounts hosted by external clients, incoming text messages, and phone communications… automate your two-way communications with AI chatbots."
- **Events (A):** Event templates with location (incl. online events), description, registration limits, waitlist/capacity, rescheduling; pre-configured event-template communications (confirmation, 24h confirmation, 48h reminder, 1h SMS reminder, no-show email, thank-you-for-attending) that must be customized and activated.
- **Interviews/appointments (A):** Scheduler + Availability: staff link external calendars bidirectionally; students register for slots in a portal; busy times close availability.
- **Recruitment travel (A):** "Create a Trip": trips organize "events, slots, stops, and notes under an overarching trip… used by users that travel off-campus to meet with constituents and host events"; trips are administrative, not public.
- **Behavioral nudges (A):** Official walkthrough of behavior-triggered outreach: nudge = "a message sent in response to a student's activity (or inactivity)"; canonical inflection points tabulated: application started not submitted; submitted with no checklist activity; event attended with no next step; no email engagement in 3+ weeks; accepted offer with no deposit. Recurring scheduled mailings + populations to suppress repeats.
- **Application processing depth (A):** Full application machinery: periods/rounds, Slate-hosted application pages, submission requirements (hard/soft fails), materials, checklists, status page, Reader and Workflows, decisions, decision reply forms, payments (application fees, deposits). This is the Admissions Management layer living inside the same product.
- **Implementation order (A):** Roadmap: essentials (users/permissions/branding) → outreach (communications/events/interviews) → historical data migration → application processing → integrations (SIS) → reporting.

## Product B — TargetX (Liaison) (Tier 1 help center + Tier 2 product pages)

### Key observations

- **Positioning (A, help center):** "The TargetX Recruitment Suite empowers admissions teams to build stronger relationships with prospects by leveraging best-of-breed communication tools that automatically track student engagement throughout the recruitment cycle, all in one comprehensive CRM."
- **Object model (A):** Salesforce-based. "Contact — The Student record. Includes basic contact, biographic, and demographic information." Accounts (schools), plus Inquiry Object, Application Object, Test Object, Enrollment History. **Profile Builder (Source to Master)**: "roll-up fields to mirror data stored on the Enrollment History object, Test Object, Inquiry Object and Application Object into roll-up fields on the Contact/Student Object" (e.g., most recent application decision shown on the Contact).
- **Stage field (A):** Settings doc "Populating the stage of 'Applicant'" — the Contact carries a recruitment stage; 'Applicant' is a named stage populated by triggers.
- **Module map (A):** Recruitment Manager (inquiry forms, reporting/dashboards, settings, triggers); Communication Planner (email campaigns, segmentation, automation, **SMS Inbox** — "centralized way to manage, send, and track SMS communications"); TX Forms (web forms for inquiries and events recording "submission data on the student record in real time"); Events (mobile-first registration, QR check-in, offline check-in, waitlists, event communication plans, event reporting); **Travel Planner** ("build and manage their counselors' travel itineraries as they attend off-campus admissions events"); Appointment Scheduler + Interviews; **Telemarketing** ("personalized call campaigns from birthdays to application follow-ups with queues and analytics"); **Territory/Group Assignment** ("assign all contacts, inquiries, and applicants to staff based on… territory assignment rules… geographic location or academic program… round-robin"); Online Application (mobile-first, "native CRM configuration reduces the number of stealth applications… the minute a student begins an application, you can begin marketing to them since all completed information is automatically captured on that student's record"); Application Review Tool (paperless review, rubrics, scores); Application Requirements Manager (checklists); Student Portal (personalized, application status, checklist widgets); TX Print (letters, envelopes, decision letters); Retention (student success side); Surveys; Engage (walk-in meeting queues).
- **Prospect Scorecard (A, product page):** "assigns dynamic scores to each prospect based on criteria important to the recruitment strategy, such as GPA ranges, standardized test scores, campus visit participation, and extracurricular involvement. Scores are recalculated automatically or manually… viewed on the Contact record."
- **Data inflows (A):** "Data Imports seamlessly import large volumes of related records into the CRM from sources like search lists, test scores, or application data." FAQ: pre-built imports/releases for SAT, ACT, TOEFL, GMAT, GRE, AP; "imports for various search/marketing data providers such as NRCCUA, SSS, and Cappex"; loads from Common App (SDS), CAS applications, statewide services (ApplyTexas).
- **Integrations (A):** bi-directional SIS integrations (Banner, Colleague, PeopleSoft, PowerCampus, Jenzabar, homegrown); payment gateways (PayPal, TouchNet, Nelnet, CyberSource…) with "payments… automatically recorded on the student record."
- **Roles (A):** "Constituency Roles deliver a field, Role, on the Contact object that allows Sharing rules to be enforced to control record-level access and identify groups for communications."
- **Analytics (A):** Delivered dashboards/reports; Yield History Chart; Feeder School dashboards/reports.

## Product C — Element451 (Tier 2 product pages)

### Key observations

- **Positioning (A, root):** "AI-native CRM built for higher ed… Marketing · Admissions · Enrollment · Student Success · CE & Workforce." Two deployment modes: Bolt (AI agents on existing stack) and Element (the CRM itself).
- **Contact database (A):** "The People database captures every student interaction and data point, from first click to cap toss." Custom labels "to categorize and segment students based on their status, such as prospects, applicants, or enrolled"; communication preferences/opt-outs; activity log; relationships (parents↔students, coaches↔athletes); customizable profiles.
- **Campaigns (A):** AI campaign creation ("nurture sequences for prospective students… yield campaigns for admitted students… post-event follow-ups"); dynamic content per segment; "behavior-based messaging… based on what students have opened, what events they attended, and where they are in the funnel"; omnichannel email + SMS from one builder; magic links into application/portal; trigger-based automated workflows; real-time analytics (opens, clicks, conversions, unsubscribes).
- **Events (A):** "Events are one of the highest-converting touchpoints in the enrollment funnel. A well-run campus visit moves a prospect to applicant. A targeted yield event moves an admitted student to enrolled." Event creation/templates, in-person + virtual, registration updating records in real time, paid events with promo codes, QR self-check-in with attendance flowing back, pre-scheduled messaging (confirmation/reminders/follow-ups by registration and attendance status), Bolt agents answering event questions and registering students from chat.
- **Appointments (A):** online scheduling via portal/website; staff availability; appointment-prep agent briefing advisors on the student's record.
- **Applications + Decisions (A):** no-code application builder, conditional logic, multiple application types (general, dual enrollment, transfer, program-specific), applicant portal (status, document upload, messaging), fraud detection (ID verification, risk scoring), AI reader (essay analysis, transcript evaluation, summaries/scoring), document management, collaborative review workflow (assign readers, notes, committee evaluations), automated scoring/prioritization, acceptance and aid packages.
- **Other surfaces (A):** Journeys, Surveys, Landing Page Builder, Task Management, StudentHub student portal, Bolt Insights, Automations, Integrations.

## Product D — Full Fabric (Tier 2 product pages + Tier 1 help center)

### Key observations

- **Positioning (A, root):** European higher-ed platform: four products — **CRM (Relationship Management)**, **Admissions**, **Student Information System**, **Commerce**. "Connect CRM, Admissions and SIS in One Platform." Recognized as a Representative Vendor in the 2025 Gartner Market Guide for Higher Education Recruitment and Admissions Platforms (vendor-quoted; market-category evidence only).
- **CRM product (A):** "Nurture leads, personalise communication, engage alumni and automate workflows." Features: **Lifecycle Tracking** ("Follow every prospect from first contact through to alumnus"; "Customise lifecycle states (e.g., Prospect Cold → Engaged → Qualified → Admitted → Student → Alumnus)"); **Smart, Flexible Forms** (lead capture: brochure requests, contact forms, surveys, events; third-party form connectors — Unibuddy, Studyportals); **Event Management** (custom event pages, maps/agendas/time zones, attendance via QR check-in, "automate lead scoring and funnel transitions based on attendance"); **Email Marketing & SMS** (drag-drop builder, dynamic content, opens/clicks/bounces/unsubscribes, SMS via MessageBird through automations); **Smarter Segments** (static and dynamic segments by "nationality, lifecycle stage, engagement score, programme, form response"; A/B messaging per country/programme); **Alumni Engagement**; automation (triggers on "form submissions, status changes, events, inactivity"; email sequences, tagging, status updates, internal alerts); tasks; activity logs; role-based permissions.
- **Profiles (A, Tier 1 help center):** "With Full Fabric's profiles, you can develop a comprehensive picture of a person and get a clear understanding of their needs and the next step that is needed to help them progress." Profile sidebar shows applications started/submitted and "the progress of their journey through your programmes and classes" (example: interested in Full-time MBA; started application for September 2019 intake; previously an "engaged prospect" for the January 2018 class but withdrew). **Latest activity** records the communication history (e.g., phone call with the MBA programme manager). **Source method vs category** doc: "Track where your prospects, applicants or students come from." **Class journeys**: "record the particulars of a candidate's affiliation with a class" (class = programme × intake). Duplicate profiles + merging; delete/anonymize/scrub (GDPR); imports (CSV) of candidates/event attendees.
- **Admissions as a separate product (A):** Admissions module = "Evaluations, Offers, and Enrolments" (evaluations & assessments, interview feedback, committees & decisioning, offer management, deposits/tuition payments, pre-arrival hub, e-signatures). The vendor itself splits recruitment-CRM from admissions processing into separately named products — vendor-side corroboration of the seam.
- **Regional machinery (A):** UCAS connector, HESA reporting (UK), Flywire/Stripe/PayPal, GDPR compliance surfaces, SSO/SAML.

---

## Cross-product Comparison

| Structure | Slate | TargetX | Element451 | Full Fabric | Layer |
|---|---|---|---|---|---|
| Person record for the prospective student ("person record" / Contact / contact / profile) | ✓ | ✓ (Contact = Student record) | ✓ (People) | ✓ (Profiles) | B → L0 |
| Recruitment lifecycle stage on the record | ✓ (populations/queries + application status; stage semantics present) | ✓ (stage field, 'Applicant' named) | ✓ (custom labels: prospects/applicants/enrolled) | ✓ (customizable lifecycle states incl. Admitted/Student) | B → L0 |
| Interaction/communication history on the record | ✓ (Timeline) | ✓ (Activities: calls/emails/tasks; Activity Timeline) | ✓ (activity log) | ✓ (latest activity, notes/interactions) | B → L0 |
| Outreach machinery bound to records (campaigns/sequences) | ✓ (Deliver drip campaigns on populations) | ✓ (Communication Planner) | ✓ (Campaigns) | ✓ (email/SMS + automation) | B → L0 |
| Inquiry/lead capture forms | ✓ (inquiry form) | ✓ (TX Forms / Recruitment Manager inquiry forms) | ✓ (landing pages/forms) | ✓ (smart forms) | B → L1 |
| Purchased name lists / search-service imports | ✓ (College Board Search source formats) | ✓ (Standard Imports; NRCCUA/SSS/Cappex) | not observed | generic CSV imports only | B (2/4 explicit) → L1 |
| Test-score file imports | ✓ (importing applications and test scores) | ✓ (SAT/ACT/TOEFL/GMAT/GRE releases) | not observed on fetched pages | not observed | B (2/4 explicit) → L1 |
| Segmentation (queries/populations/segments) | ✓ (Queries, Populations) | ✓ (segmentation in email) | ✓ (labels + segments) | ✓ (static/dynamic segments) | B → L1 |
| Multi-channel outbound (email/SMS/print/voice) | ✓ (email/SMS/print/voice/video) | ✓ (email/SMS/print; telemarketing call campaigns) | ✓ (email/SMS) | ✓ (email/SMS) | B → L1 |
| Two-way inbox | ✓ (Inbox: email/SMS/phone + chatbots) | ✓ (SMS Inbox) | ✓ (Shared Conversations Inbox) | ✓ (Inbox: applications/emails/tasks/registrations) | B → L1 |
| Recruitment events (registration, reminders, check-in, follow-up) | ✓ (templates, waitlists, event comms) | ✓ (QR + offline check-in, event comms, reporting) | ✓ (QR self-check-in, pre-scheduled messaging) | ✓ (QR check-in, attendance-based scoring) | B → L1 |
| Interviews / appointments scheduling | ✓ (Scheduler + Availability) | ✓ (Appointment Scheduler, Interviews) | ✓ (appointment booking) | ✓ (interview feedback in Admissions module) | B → L1 |
| Counselor territories / assignment | partial (rep-personalized sends observed; assignment machinery not directly observed) | ✓ (Territory/Group Assignment, round-robin) | not observed | not observed | B (US-centric) → L1/L2 |
| Recruitment travel (trips/itineraries) | ✓ (Trips) | ✓ (Travel Planner) | not observed | not observed | B (2/4, US-centric) → L2 |
| Prospect scoring / engagement scoring | not directly observed (behavioral nudges imply engagement tracking) | ✓ (Prospect Scorecard) | partial (fraud scoring; engagement-based messaging) | ✓ (lead scoring, engagement score segment field) | B → L1 |
| Applicant portal / status page | ✓ (status page) | ✓ (Student Portal) | ✓ (applicant portal, StudentHub) | ✓ (portal management) | B → L1 |
| Application intake (hosted application and/or imports from centralized services) | ✓ (Slate-hosted applications; Common App etc. via import) | ✓ (Online Application; Common App/CAS/ApplyTexas loads) | ✓ (Applications + Decisions) | ✓ (application portal; UCAS connector) | B → L1 |
| Application review/decision machinery | ✓ (Reader/Workflows, decisions, decision release) | ✓ (Application Review Tool, rubrics) | ✓ (AI reader, collaborative review, decisioning) | ✓ (separate Admissions product) | B → L1 (seam with Admissions Management) |
| Funnel/yield analytics | ✓ (queries/reports) | ✓ (Yield History, feeder-school reports) | ✓ (Bolt Insights, funnel drop-off) | ✓ (analytics/reporting; pipeline dashboards) | B → L1 |
| SIS integration | ✓ (roadmap step 5) | ✓ (named SIS list) | ✓ (integrations) | ✓ (SIS module itself) | B → L1 |
| Payments (application fees, deposits) | ✓ (Slate Payments) | ✓ (payment connectors recorded on record) | ✓ (paid events; acceptance/aid packages) | ✓ (deposits/tuition in Admissions) | B → L1 |
| AI agents/chatbots | ✓ (Slate AI, AI chatbots, AI interviews) | ✓ (AI writing assistance) | ✓ (Bolt agents everywhere) | ✓ (Mentor AI chatbot, Fin support) | era-current → L2 |
| Alumni/advancement extension | ✓ (Advancement product) | ✓ (Retention sibling) | ✓ (Element Advancement "coming soon") | ✓ (alumni engagement in CRM) | optional → L2 |
| GDPR delete/anonymize machinery | not observed on fetched pages | not observed | not observed | ✓ (delete/anonymize/scrub) | regional → L2 |
| UCAS/HESA (UK) machinery | not observed | not observed | not observed | ✓ | regional → L2 |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures (evidence: B across all four products; C for the abstraction):

1. **The prospective-student record.** A persistent, individually identified person record for someone the institution is recruiting — carrying identity/contact/biographic (commonly academic) attributes and accumulating the relationship history: interactions, communications, event attendance, notes. Every sampled product centers this object (Slate person record; TargetX Contact; Element451 contact; Full Fabric profile). Remove it → a campaign tool with no memory, or a generic contact list.
2. **The recruitment funnel state.** The record carries the institution's recruitment lifecycle stage — progress toward enrollment (prospect/inquiry → applicant → admitted → deposited/enrolled; exact labels vary by product and are commonly customizable). The funnel is the organizing spine of the population: segmentation, campaigns, reporting, and staff work are all keyed to it. Remove it → a generic CRM contact database (or an admissions tracker keyed to applications rather than people).
3. **The recruitment work loop.** Staff (and automated machinery) act on records to move them through the funnel — targeted communications (campaigns/sequences/one-off outreach), recruitment events, and personal outreach (counselor contact, tasks, notes) — and the outcomes are recorded back onto the record, feeding segmentation and reporting. Remove it → a static prospect registry (an SIS-style archive of names nobody works).

Jointly-held load-bearing tests:
- 1 alone = contact list / spreadsheet of names.
- 2 without 1 = a funnel report with nobody in it.
- 3 without 1+2 = generic marketing automation.
- 1+2 without 3 = a static pipeline nobody works.
- 1+3 without 2 = a generic CRM (relationship records + outreach, no enrollment funnel).
- 2+3 without 1 = anonymous campaign machinery.

### L1 — Common Mature Structure

Present in most mature products, not required to recognize the Type:

- inquiry/lead capture forms and landing pages (the primary population inflow)
- purchased name-list / search-service imports and test-score file imports (with identity matching/merging)
- segmentation (rule-based queries/populations/segments, static and dynamic)
- multi-channel outbound: email, SMS, print, voice/phone campaigns
- two-way inbox (email/SMS) with automation/chatbots
- recruitment events: campus visits, open days, fairs — registration, capacity/waitlists, reminders, check-in (QR common), attendance recorded back to the record, post-event follow-up
- interviews and appointment scheduling against staff availability
- counselor territory/assignment machinery and recruitment travel planning (US-centric)
- prospect/engagement scoring
- applicant portal / status page
- application intake — hosted application builder and/or imports from centralized application services
- funnel/yield analytics, dashboards, feeder-school/source reporting
- SIS integration and the enrollment handoff
- payments (application fees, event fees, deposits)
- tasks, notes, activity timeline; duplicate detection/merging
- roles and record-level permissions

### L2 — Variant / Optional Structure

- Depth of application review/decision machinery (reader workflows, committees, rubrics, decision release) — the Admissions Management seam; products range from hand-off-only to full processing.
- Deposits/financial-aid surfaces (aid checklists, award letters, net-price machinery).
- Alumni/advancement and student-success/retention extensions (same platform, adjacent Types).
- Regional machinery: UCAS/HESA (UK), GDPR anonymization (EU), Common App/CAS/statewide loads (US).
- Segment shape: undergraduate vs graduate vs international recruitment; community/technical colleges; K-12/private schools; business schools (EU pole).
- AI agents/chatbots (era-current).
- Travel/territory machinery depth (US search-and-travel culture vs EU fair/UCAS culture).

### L3 — Vendor-specific (research notes only)

- Slate: populations, Liquid markup, Slate Credits, periods/rounds, Source Format Library, Slate Print/Voice/Video, Time Warp/Clean Slate environments, turnkey model databases (4-year/2-year/K-12).
- TargetX: Salesforce objects (Contact/Account/EDA-compatible), Profile Builder "Source to Master", Prospect Scorecard, Engage walk-in queues, Telemarketing queues, Premier Services tiers.
- Element451: Bolt agent families, StudentHub, magic links, Bolt Discovery, ROI calculator.
- Full Fabric: class journeys, schema fields, Mentor AI/Fin, UCAS connector, separately-licensed CRM/Admissions/SIS/Commerce products.

## Anti-overfitting Notes

- **Purchased search lists are NOT definitional.** Explicit in 2/4 sampled products (Slate College Board Search; TargetX Standard Imports). Full Fabric shows generic CSV imports; EU/UK recruitment runs on fairs, inquiry forms, and UCAS without US-style search lists. The invariant is "prospects enter as records from multiple sources," not any specific source.
- **US travel/territory machinery is NOT definitional.** Trips/Travel Planner/Territory Assignment appear in the US pair only; the EU pole satisfies the core without them.
- **Application processing is NOT definitional for this Type.** All four sampled products carry application machinery, but Full Fabric licenses it as a separate product (vendor-side split), and the already-processed admissions-management leaf owns the application-pipeline core. Recruitment CRM requires only that applications (wherever processed) register as a funnel milestone on the person record.
- **AI is NOT definitional** (era-current; present in all four but in different shapes).
- **Stage label vocabularies vary** (Full Fabric's example states are explicitly customizable; TargetX populates 'Applicant' by trigger; Slate realizes stages via populations/queries/application status). The invariant is a funnel state on the record, not any label set.

## Historical / Market-Sample Check

- Paper-era admissions/recruitment office: inquiry cards and purchased name lists (College Board has supplied student names to colleges since long before software), campus-visit logs, counselor travel notes, letter series, funnel counts on a chalkboard — satisfies records + funnel + work loop with zero software. The Type predates its current digital machinery.
- Regional: UK universities recruit through UCAS-centered flows and open days; European business schools recruit masters candidates via fairs, inquiry forms, and brochures (Full Fabric pole) — fit the core without US search-list/travel machinery.
- K-12/private schools and community colleges: Slate ships dedicated model databases for both; same core.
- Conclusion: the L0 holds across eras, regions, and segments; search lists, travel/territories, and AI stay out of the core.

## Boundary Findings

- **vs Admissions Management (processed 2026-09-06):** That Type's core = the application pipeline (application to program × entry term as the tracked record, completeness/materials, structured review, recorded decision — lifecycle ON THE APPLICATION). This Type's core = the pre-application/enrollment relationship (funnel state ON THE PERSON, outreach machinery, events, counselor work). The market bundles both (Slate, TargetX, Element451 all carry application machinery), and Full Fabric sells them as separately named products — vendor-side corroboration that the centers differ. Removal tests: strip review/decision machinery from a recruitment CRM → still this Type (applications can be imported from centralized services and remain a funnel milestone); strip nurture/events/counselor machinery from an admissions processor → still Admissions Management. Keep both; document the bundle as common packaging.
- **vs Enrollment Management (processed 2026-09-07):** That pass explicitly held "recruitment marketing (Student Recruitment CRM)" as NOT definitional to its Type and flagged this interlock. Seam confirmed from this side: enrollment management = commitment-and-readiness for the period (who actually attends, contracts/deposits/readiness/holds); recruitment CRM = the relationship funnel before commitment (inquiry → application → admission → deposit as funnel milestones). The deposit moment is the shared boundary: recruitment CRM tracks it as a funnel outcome; enrollment management takes over the committed population. Keep both.
- **vs CRM (§07 generic):** Same genus (person records + relationship history + outreach), different domain semantics: the person is a prospective student, the pipeline is the enrollment funnel, the events are recruitment events, the intake includes test scores/search lists/SIS handoff. A generic CRM lacks the enrollment-funnel and education-intake semantics; this Type is the education-specific realization. Keep both (consistent with recruitment-marketing-platform pass's "same shape, different domain" note from the HR side).
- **vs Marketing Automation Platform:** Campaign machinery overlaps, but marketing automation centers campaign execution over lead pools; this Type centers the identified person record and the enrollment funnel, with campaigns as one leg of the work loop. Embedded-campaigns pattern here mirrors other domain CRMs.
- **vs Event Management Platform / Event Registration Platform:** Events are one leg of the recruitment loop (bound to person records, feeding funnel transitions), not the center. Full Fabric's own copy ("automate lead scoring and funnel transitions based on attendance") shows events as funnel machinery.
- **vs Student Information System / SIS:** SIS = the enrolled-student system of record; recruitment CRM = the pre-enrollment relationship system. The enrollment handoff is the seam (SIS integration is L1 here). Full Fabric ships both as separate products.
- **vs Lead Management Platform / Lead Capture Platform (§06):** Generic B2B lead capture/nurture lacks the enrollment funnel, education intake, and institutional context. The recruitment CRM embeds lead-capture as its inquiry-form leg.
- **vs recruitment-marketing-platform (§09, employer-side):** That pass recorded "same shape, different domain" — confirmed: employer-side recruitment marketing attracts candidates to jobs; this Type attracts students to enrollment. Different population, different conversion event, different downstream system (ATS vs SIS).

## Uncertainties

- Slate's admissions-side person-record documentation is video-led (Person Record Overview page carries no text); record structure inferred from the advancement-facing Constituent Record doc + implementation roadmap + applications docs. Confidence: high for the record-as-hub, moderate for tab-level detail.
- Element451 evidence is product-page level (no public help center fetched); operational depth (e.g., exact stage mechanics) not asserted.
- Slate counselor/territory assignment machinery not directly observed (rep-personalized sends observed; assignment rules not confirmed) — held as L1-common via TargetX only, marked accordingly.
- Precise numeric limits (list sizes, campaign volumes, credit costs) deliberately not asserted; vendor marketing numbers (2,000+ institutions; 350+ institutions; 6M emails/year) recorded here as claims, not facts.
- Whether a standalone recruitment-only product exists that never touches applications (pure pre-application CRM) was not directly sampled; the bundle pattern dominates the market. The L0 is written so such a product would still qualify (application machinery not required).

## Final Synthesis

A Student Recruitment CRM is the institution's system of record for recruiting prospective students: it holds each prospect as a persistent identified person record accumulating the relationship history, carries the recruitment funnel state on that record, and surrounds both with the work loop — segmentation, multi-channel outreach, recruitment events, counselor work — that moves records toward enrollment. Application processing, deposits, aid, alumni, and retention are common extensions or adjacent Types; search lists, travel territories, and AI are common implementations of the intake/work legs, not the definition. The Type's sharpest seam is with Admissions Management (application as record vs person as record), and the market overwhelmingly sells the two as one bundle while structurally keeping the centers distinct.
