# Research Notes — Continuing Education Management

## Research Goal

Understand what "Continuing Education Management" software actually is as an Application Type: what objects exist inside it, who uses it, how CE credits flow through it, how compliance is evaluated, and where its boundaries sit against Certification Management, LMS, Government Licensing Management, and related Types.

## Initial Boundary

- Leaf: "Continuing Education Management", DIRECTORY §25 (Nonprofit, Membership & Religious Organizations).
- Working hypothesis before research: software that manages the continuing-education (CE) obligation loop of a profession — requirements, approved providers/activities, credit capture, compliance evaluation, renewal linkage. Expected to be distinct from an LMS (delivery) and from Certification Management (credential lifecycle), with heavy interlocking.
- Prior-pass context that must be discharged:
  - `certification-management` (processed 2026-09-06) flagged a joint review: "CE tracking is the renewal input of certification management and the same vendor ships CE Management as its own solution (approved-provider networks, course catalogs); working split: CE management centers learning-activity approval/credit capture, certification management centers the credential lifecycle and consumes CE as maintenance evidence."
  - `association-event-management` (processed): "CE management is the credit/certification system of record; association events are one common source of credits."
  - `association-management-system-ams` (processed): CE/certification tracking is capability depth inside AMS products, owned by their own Types.

## Research Questions

1. What are the core objects (license/credential, CE cycle, requirement, activity/course, credit, provider, transcript, compliance status, audit)?
2. How do credits enter the system (provider report, self-report, auto-report, import)?
3. How is compliance evaluated (requirements, categories/subject areas, cycle dates, status)?
4. What is the approved-provider machinery (provider application, course approval, provider portal, attendance upload, course catalog)?
5. What happens at renewal — does the CE system renew, or gate the renewal?
6. What is the audit loop and who decides outcomes?
7. How do the governing-side and provider-side poles differ, and what do they share?
8. Where does learning delivery fit (is a CE manager also an LMS)?
9. Which rules are board/program-configured vs structural?
10. Where exactly are the boundaries vs Certification Management, LMS, Government Licensing Management, Accreditation Management, Association Event Management?

## Representative Products

| Product | Vendor | Pole | Why sampled |
|---|---|---|---|
| CE Broker | Propelus | compliance marketplace (boards + providers + licensees) | the flagship CE compliance-tracking system; official tracker for licensing boards; three-sided structure |
| LearningBuilder | Heuristic Solutions | governing side (boards / certifying bodies) | ships a solution literally named "CE Management"; approved-provider programs; same platform also ships Certification/License/Accreditation Management — ideal for the boundary test |
| EthosCE | Cadmium | provider side (accredited healthcare CE) | healthcare CE LMS; credit tracking + accreditation reporting (ACCME PARS, JA PARS, CPE Monitor, CE Broker integration) |
| Rievent | HealthStream | provider side (accredited CME/CE) | 20-year CME/CE management specialist; activity types, credit options, automated accreditor reporting, MOC transmission |

Certemy (license/certification compliance) was a fifth candidate but returned HTTP 403 twice across two passes (this pass and the certification-management pass) — abandoned per network rules; no claims made for it.

## Sources

Fetched 2026-09-07 unless noted:

- CE Broker (Propelus) — Help Center (Tier-1):
  - https://help.cebroker.com/ (home; three audience categories)
  - https://help.cebroker.com/hc/en-us/categories/15226509166612-Licensed-Professionals
  - https://help.cebroker.com/hc/en-us/categories/15226492874900-Education-Providers
  - https://help.cebroker.com/hc/en-us/categories/15818260022420-Board-Users
  - https://help.cebroker.com/hc/en-us/articles/15226535234964-CE-Broker-How-Everything-Works
  - https://help.cebroker.com/hc/en-us/articles/15226551056916-CE-Broker-for-Boards-Explained
  - https://help.cebroker.com/hc/en-us/articles/48099161102740-...-Understanding-Your-Compliance-Status
  - https://help.cebroker.com/hc/en-us/articles/15226550796948-Report-Continuing-Education
  - https://help.cebroker.com/hc/en-us/articles/24564257246228-Completing-Your-Audit
  - Note: https://www.cebroker.com/ root returns 403 in this environment (also in the certification pass); all CE Broker evidence comes from the reachable help center.
- LearningBuilder (Heuristic Solutions) — product site (Tier-1 product pages):
  - https://www.heuristics.net/ (root)
  - https://www.heuristics.net/education-management-software/ (the "Continuing Education (CE) Management Software" solution page)
  - Cross-pass (certification-management, 2026-09-06): certification-management, recertification, auditing pages on the same domain.
- EthosCE (Cadmium) — https://www.ethosce.com/ (Tier-2 product page incl. FAQ)
- Rievent (HealthStream) — https://rievent.com/ (root) and https://rievent.com/features/certification-management (Tier-2 product pages)

## Product Observations

### CE Broker (Propelus) — compliance pole, three-sided marketplace

Evidence layer: A (directly observed, official help center).

- Self-description: "the official continuing education tracking system for over 2 million licensed professionals, collaborating with 100+ boards and 6,000+ providers across 200+ professions" (vendor claim; scale figures are marketing, not independently verified).
- Three audiences with dedicated help-center categories:
  - **Licensed Professionals** — "Get access to your account, self-report credits, and manage your CE."
  - **Education Providers** — "Register to provide continuing education, apply to boards, and report completions."
  - **Board Users** — "Resources for regulating boards."
- Role split (from "How Everything Works"):
  - Licensees track compliance and report completed CE credits through individual license accounts.
  - Regulating entities have direct access to the completed-CE status and history in any licensee's account — "no need to wait for records to be transferred or submitted before proceeding with license renewal."
  - State Boards manage and communicate with educational providers on CE content applications, plus auditing tracking; "immediate access to compliance tracking verification."
  - Educational providers register through a Board application process, report completions, and their courses appear in the CE Broker course search library.
- Board-side business model: "fully-hosted system is offered at no cost to State Boards," tailored per board; implementation/customization/support included. (Monetization sits with professionals' subscriptions and provider services.)
- Practitioner-side compliance mechanics ("Understanding Your Compliance Status"):
  - Per-license compliance status: **Complete** / **Not Complete** (product labels; conceptual states).
  - **Requirements tab**: "a general outline of renewal requirements" — CE Cycle date range + hours required per subject area (example given: "2 hours of Medical Errors").
  - **Course History**: reported courses; each course carries its subject area so the licensee can match courses to requirements.
  - Basic (free) account: manual compliance calculation — "use the Requirements tab as a checklist"; paid subscription unlocks the "CE Compliance Transcript" which "calculates the specific credits you need."
  - When the regulating entity is linked, it "can see your course history and compliance status at any time"; when complete, "you can proceed to your state website to review the next steps for your license renewal."
  - Explicit limit: "CE Broker is not authorized to renew licenses. It serves solely as a platform for tracking CE compliance, while all license issuance and renewal is handled directly by your regulating entity."
- Credit capture ("Report Continuing Education"):
  - Provider-reported completions flow directly into licensee accounts (timing "up to 30 days, may vary by provider").
  - Self-reporting: a guided form (completion date, course type, number of hours, educational provider, course name); for many options the licensee must search the approved provider or course (provider tracking numbers typically "50-", course tracking numbers "20-"); attach the certificate of completion or use "Maintain Your Own Documentation" where allowed; attest accuracy; the record appears in course history immediately and the board gets instant access.
  - Multiple licenses: "Credits that are applicable to multiple licenses must be reported to each license individually."
  - Exemptions are a reportable record type ("Reporting and Deleting Exemptions").
  - Board-configured policy: "certain regulatory agencies... do not permit self-reporting" (examples given: Tennessee Real Estate Commission, Ohio State Cosmetology Board).
  - Hosted courses ("CE Broker Now" / "Take It Here"): completion auto-reports to the account.
  - Concierge tier: staff report on the member's behalf.
- Audit loop ("Completing Your Audit"):
  - The board initiates an audit of a previous renewal cycle; selected licensees see a red banner; transcript shows "the specific subject areas and number of credit hours that need to be reported"; licensee reports all required CE, then submits the audit; banner turns yellow ("routed to your Board for review").
  - "Do not submit course completion certificates directly to the Board... they will not be accepted" — all documentation flows through the system.
  - "CE Broker is the tracking system and doesn't make decisions about audit outcomes" — the board decides.
  - Audits work on a free Basic account.
- Practitioner account surface (from category structure): credential overview page, credential status, compliance status, CE cycle updates, multiple licenses, course history, certificates of completion, PDF CE report, subscription tiers (Basic / Professional / Pro+ / Concierge), employer-sponsored accounts, SSO.

### LearningBuilder (Heuristic Solutions) — governing pole, named "CE Management" solution

Evidence layer: A (directly observed, official product pages this pass; certification pages cross-pass).

- Platform framing: "Reliable, Robust, and Scalable Software for Certification, Licensure, and Accreditation Programs... handles the whole process: candidate applications, exams, continuing education, recertification, and renewals."
- Solutions menu: Certification Management, Recertification, License Management, **CE Management** (URL slug: education-management-software), Accreditation Management, Workforce Development — sibling solutions on one platform. This is direct evidence that CE Management and Certification Management are distinct offerings of the same vendor.
- CE Management page definition: "Continuing education (CE) management software runs approved-provider programs and tracks learner CE, from a simple CE log to category minimums, limits, and approved courses."
- FAQ definition: "Software that tracks learner CE and manages approved provider and course approval programs for certification and licensure bodies."
- CE credit tracking FAQ: "It records credits and candidate progress against category minimums and limits, validates requirements, and automatically flags shortfalls."
- Approved-provider machinery:
  - **Approved provider applications** — "Define an application and approval process for your approved provider program. Manage provider lists on a course-by-course basis."
  - **Provider portals** — "a user-friendly approach for your provider network to submit applications for course approval and upload attendance records."
  - **Attendance upload** — providers upload attendance directly "so that attendance records no longer need to be submitted by your learners... removes an auditing step for you."
  - **Searchable course catalogs** — "a directory of approved provider courses, sortable by domain, method, date, or region."
- Adjacent capabilities on the same platform: assessments (continuing competency), eLearning ("customized learning plans for required, recommended, and/or self-directed education"), reflective practice, certificate printing, auditing (cross-pass), automated communications, analytics.
- Licensure framing: "A single platform for applications, renewals, CE management, and complaints and investigations."

### EthosCE (Cadmium) — provider pole, healthcare CE LMS

Evidence layer: A (directly observed, official product page + FAQ).

- Self-description: "the LMS healthcare professionals trust to simplify continuing education. Manage all your CE activities in one place."
- Serves medical societies, universities, healthcare providers (named customers: Society of Hospital Medicine, Tulane, NCCN, etc.).
- Healthcare-LMS differentiation (FAQ): "CME tracking, Accreditation support, Compliance management, Tools to help content meet regulatory requirements."
- Credit mechanics (FAQ): "Automated CME credit tracking: When professionals need a certain number of continuing education credits to maintain certifications, you can set up a system to track that and send reminders about when certificate renewal dates are approaching."
- Accreditation/reporting automation: "integrates with major healthcare accreditation boards and systems, such as ACCME PARS, JA PARS, CPE Monitor, and CE Broker." — direct evidence of the provider→board/compliance-system transmission seam.
- Platform modules: Platform Overview, E-Commerce, Accreditation Management, Faculty Management, Course Management; activity types include Course Bundles, RSS (Regularly Scheduled Series), Virtual Learning.
- Learner-facing: certificates with self-service reprints, course library/search, Learning Groups (curated catalogs), reminders, follow-up assessments, attendance tracking.
- Compliance dashboards "to track progress toward healthcare compliance training goals."

### Rievent (HealthStream) — provider pole, CME/CE management specialist

Evidence layer: A (directly observed, official product pages).

- Self-description: "CME software that works better for everybody... a CME/CE management system"; "We've been building CME/CE software for 20 years."
- Activity types: "live events, enduring activities, journals, webinars, regularly scheduled series (RSS), and manuscript review."
- Activity management: "Create and manage all activities from one place. Production templates... add any content in common learning file formats."
- Accreditor reporting: "Generate and submit your ACCME PARS, ANCC NARS, or ACPE reports in under five minutes" (vendor claim on timing); "Automate annual reporting to accreditation bodies, like ACCME PARS."
- Certification Management Tool (CMT): "create and manage credit options, accredited providers, and certificates"; "supports all credit types and accredited providers"; custom certificates built once, accessed by learners "after earning the requisite credits."
- MOC: "Add MOC as a credit type that learners can claim for qualifying activities. Real-time web service integration with the ACCME automatically transmits and verifies MOC points with participating medical boards."
- Learner self-service: "viewing and downloading up-to-date certificates, transcripts, and test scores"; activity catalog + events calendar; pause/resume activities.
- Tests & surveys: pre/post-tests, evaluations, automated post-activity outcomes surveys.
- E-commerce: registration and payment for activities, discount codes, packages, tokens.

## Cross-product Comparison

| Aspect | CE Broker | LearningBuilder | EthosCE | Rievent |
|---|---|---|---|---|
| Market pole | compliance marketplace (board + provider + licensee) | governing side (boards / certifying bodies) | provider side (accredited healthcare CE) | provider side (accredited CME/CE) |
| Tracked individuals | licensees (per-license accounts) | candidates / certificants / licensees | learners | learners |
| Requirement machinery | Requirements tab per license × cycle; hours per subject area; CE cycle date range | category minimums and limits; requirement validation; shortfall flags | credit tracking toward certification renewal; compliance dashboards | credit options (types) incl. MOC; accreditor-defined credit values |
| Credit capture | provider report; self-report with documentation + attestation; auto from hosted courses; exemptions | provider attendance upload; learner CE log | attendance tracking; course completion | attendance/evaluation processing; credit claiming |
| Approval machinery | board application process for providers and courses; provider/course tracking numbers | approved-provider applications; course approvals; provider lists per course | accreditation management module (ACCME-class) | accredited-provider registry; credit options per provider/certificate |
| Reporting outward | board sees status/history directly; audit submissions | program reports/analytics | ACCME PARS, JA PARS, CPE Monitor, CE Broker | ACCME PARS, ANCC NARS, ACPE; MOC transmission to ACCME |
| Learning delivery | hosted courses (CEB Now) as marketplace add-on | optional eLearning module | full LMS (course engine, bundles, RSS, virtual) | activity delivery (online activities, journals, webinars) |
| Certificates / transcript | certificates of completion; transcript; PDF CE report | certificate printing; CE log → transcript | certificates, self-service reprints | custom certificates; learner transcripts |
| Renewal seam | status Complete → renew at the board; explicitly not authorized to renew | recertification/renewal machinery on same platform | reminders toward renewal dates | — (serves providers whose learners renew elsewhere) |
| Audit | board-initiated audits; documentation through system; board decides | auditing module (cross-pass) | n/a (provider is audited, not auditor) | n/a |
| Business model | boards free; professionals subscribe (free Basic → paid tiers → concierge); providers register | platform license to the body | platform license to the provider | platform license to the provider |

### Shared spine (evidence layer B — cross-product commonality)

All four products, despite opposite poles, share:

1. **Tracked individuals** — identified people (licensees / certificants / learners) whose CE record the system maintains.
2. **Credit-bearing learning activities** — discrete activities (courses, live events, journals, webinars, RSS, self-study) carrying defined credit values and (on the governing side) subject-area/category classification.
3. **Recorded credit awards** — a person × activity × credit binding accumulating into a per-person record (course history / CE log / transcript).
4. **A requirement framework** — credit amounts, categories, and cycle periods that define what credits count for (defined and evaluated in-system on the governing side; reflected as accreditor-defined credit types on the provider side).

### Poles (evidence layer B/C)

- **Governing-side products** (CE Broker board side, LearningBuilder) run the requirement → approval → capture → evaluation → audit loop over a population.
- **Provider-side products** (EthosCE, Rievent, CE Broker's provider side) run activity management → credit issuance → accreditor/board reporting. They do not evaluate individual compliance; they feed the systems that do (Rievent transmits MOC via ACCME to boards; EthosCE reports PARS and integrates with CE Broker).
- The two poles meet at the credit record: a credit earned at a provider becomes an entry in the individual's record at the governing system.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Tracked individuals** — identified people whose continuing-education record the system maintains (licensees, certificants, members).
2. **Credit-bearing learning activities** — the unit of record is a discrete learning activity carrying a defined credit value (and typically a category/subject-area classification).
3. **Recorded credit awards** — the binding of person × activity × credit value, accumulating into a persistent per-person CE record (course history / transcript).
4. **Requirement framework** — defined credit requirements over renewal cycles (amounts, categories, periods) that give credits their meaning; evaluation against it produces per-person standing.

Historical check: paper-era board CE tracking (requirement letters, activity records, transcripts, audits), association CE programs (approved providers, credit cards, transcripts), and provider-side attendance rosters with accreditor-defined credit values all satisfy these four properties without any modern implementation detail. The L0 survives the check.

### L1 — Common Mature Structure

- Approved-provider programs: provider application/approval, course approval, provider portals, direct attendance/completion reporting.
- Course/activity catalogs and search (find approved courses).
- Self-reporting with documentation attachment and accuracy attestation.
- Compliance status evaluation (Complete / Not Complete-class states) with progress vs requirements.
- Transcripts and certificates of completion; learner self-service.
- Audit machinery on the governing side (board-initiated review, documentation through the system, board decides).
- Exemptions/waivers as recorded objects.
- Multiple licenses/credentials per person, with per-license credit reporting.
- Reporting outward to accreditors/boards (PARS-class automated reports; direct board access to records).
- Renewal linkage: CE standing gates renewal (renewal itself usually happens in the licensing/credentialing system).
- Reminders/notifications toward deadlines.
- E-commerce for activities (provider side).

### L2 — Variant / Optional Structure

- Learning delivery in-platform (LMS depth): hosted course marketplaces, course engines, bundles, RSS, virtual learning — present in provider-pole products and as optional modules elsewhere; not definitional.
- MOC (maintenance of certification) as a credit type with board verification transmission.
- Who owns the requirement framework: regulator (statutory CE) vs certifying body vs association (voluntary/recertification programs) vs accreditor (credit-type definitions).
- Scope: single board vs multi-board/multi-profession/multi-jurisdiction; single profession vs many.
- Mandated vs voluntary CE.
- Concierge / data-entry services; employer-sponsored accounts; SSO.
- Assessments, reflective practice, competency models as CE-adjacent extensions.
- Business model: boards-free/professionals-pay; platform license; suite membership (AMS/LMS/event suites).

### L3 — Vendor-specific (research notes only)

- CE Broker: provider/course tracking-number scheme ("50-" / "20-"), CEB Now hosted-course marketplace with direct deposit, Concierge tier, Credential Tracker, red/yellow audit banners, Propelus ownership, "no cost to State Boards" model, IMLCC (interstate license compact) renewal articles.
- LearningBuilder: reflective practice module, employer voucher programs, LearningBuilder Academy, "education-management-software" URL slug for CE Management.
- Rievent: Certification Management Tool (CMT), Rievent Connect, sandbox-onboarding, "under five minutes" PARS claim, HealthStream ownership.
- EthosCE: Learning Groups, Cadmium suite (Elevate LMS, Eventscribe, Warpwire), support portal on gocadmium.com.

## Vendor-specific Findings

- CE Broker's three-sided free-to-boards model is distinctive; LearningBuilder/EthosCE/Rievent license to the operating organization.
- CE Broker's per-license compliance status with board-visible course history is the purest expression of the governing pole; LearningBuilder expresses the same loop as "category minimums and limits... automatically flags shortfalls."
- Rievent's MOC auto-transmission to ACCME and EthosCE's PARS/CPE Monitor/CE Broker integrations document the provider→governor transmission seam from the provider side.

## Boundary Findings

1. **vs Certification Management (§25 sibling) — DISCHARGES the joint-review flag.** Confirmed distinct Types that interlock at renewal. LearningBuilder ships CE Management and Certification Management as separate named solutions on one platform — direct vendor evidence that the market treats them as different jobs. Structural test: CE management's spine is the learning-activity/credit machinery (activities, credits, requirements, provider approval, compliance status, audits); certification management's spine is the credential lifecycle (application → eligibility → exam → grant → standing → renewal → revoke), which *consumes* CE as one maintenance input. Remove the credential lifecycle and the credit machinery still forms a complete product (CE Broker is exactly that); remove the credit machinery and the credential lifecycle still forms a complete product (certification programs that accept attestations or use external trackers). The seam is the renewal input: certification renewal reads CE standing; CE management produces it.
2. **vs LMS (§09 Corporate LMS / §23 LMS).** An LMS delivers learning and tracks completions; CE management governs credits against an external requirement framework. Provider-pole CE products are LMS-like (EthosCE self-describes as an LMS) but their defining layer is credit types, accredited-provider registries, accreditor reporting, and compliance tracking. Test: is the system of record the person's credit standing against requirements, or the learning content/completions? A CE manager can lack delivery entirely (CE Broker's core); an LMS lacks the requirement/credit/compliance machinery.
3. **vs Government Licensing Management (§24).** The license lifecycle (issuance, renewal, fees, discipline) vs the CE slice. CE Broker states it explicitly: "not authorized to renew licenses... all license issuance and renewal is handled directly by your regulating entity." CE management produces the compliance evidence that the licensing system consumes at renewal.
4. **vs Accreditation Management (§25).** Accreditation manages organizations against standards; CE management manages individuals against credit requirements. They meet at approved-provider programs (an accredited-provider program is CE machinery deciding which organizations may issue credit).
5. **vs Association Event Management (§26).** Events are one common credit source; event management centers the event (registration, attendance, logistics), CE management centers the credit (approval, award, requirement evaluation). Association Event Management's own pass recorded credit awarding as a common capability, not the defining one — consistent.
6. **vs AMS / Membership Management (§25).** Membership registry vs CE program machinery; AMS products bundle CE tracking as capability depth (per the AMS pass).
7. **vs Digital Credential Platform (§23).** Certificates of completion here are records of credit; a digital-credential Type would center portable verifiable credential artifacts.
8. **vs Employee Learning Platform / Corporate LMS (§09).** Employer-side training vs profession-wide CE obligation; different requirement owner (employer vs regulator/certifying body) and different population (employees vs licensees/certificants).
9. **vs Higher-education registration/SIS (§23).** Academic credit toward a degree vs CE credit toward continued authorization to practice; different populations, cycles, and semantics.

## Uncertainties

- Certemy unreachable (403 ×2 across passes) — no claims; the license-compliance pole is represented by CE Broker + LearningBuilder instead.
- CE Broker scale figures (2M professionals, 100+ boards, 6,000+ providers, 200+ professions) are vendor claims from a help-center article; recorded as claims, not verified facts.
- Exact credit-hour rules, cycle lengths, category names, audit timeframes: board-specific and deliberately not asserted anywhere.
- Whether every governing-side product supports board-initiated audits: directly observed at CE Broker; LearningBuilder has an auditing module (cross-pass product page); provider-pole products are audited rather than audit. Treated as a governing-pole standard capability, not universal.
- Association-side CE modules (inside AMS products) were documented in the AMS pass as bundled capability; not re-researched here.
- The provider-pole products' internal compliance dashboards (EthosCE) were observed only at product-page depth; no help-center-level operational detail was fetched for EthosCE/Rievent.

## Final Synthesis

Continuing Education Management is the credit-and-compliance machinery around a profession's continuing-education obligation. Its defining core is small: tracked individuals, credit-bearing learning activities, recorded credit awards accumulating into a per-person transcript, and a requirement framework over renewal cycles that gives credits meaning and drives a per-person compliance determination. Around that core, mature products add the approved-provider program (provider application, course approval, provider portals, attendance reporting, course catalogs), self-reporting with documentation, audits, exemptions, multi-license handling, accreditor reporting, and renewal linkage. The market realizes the Type in two interlocking poles — governing-side systems that run the requirement→approval→capture→evaluation→audit loop over a population, and provider-side systems that manage activities, issue credits, and report to the governing systems — meeting at the credit record. The Type is distinct from Certification Management (credential lifecycle consumes CE), from LMS (delivery vs credit governance), and from Government Licensing Management (license lifecycle consumes CE evidence at renewal).
