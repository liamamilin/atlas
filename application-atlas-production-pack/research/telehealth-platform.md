# Research Notes — Telehealth Platform

Research date: 2026-09-09
Leaf: Telehealth Platform (DIRECTORY §22 Healthcare & Life Sciences)
Slug: telehealth-platform

## Research Goal

Understand what a Telehealth Platform actually is as an Application Type: what its unit of work is, what structures are definitional vs merely common in the current market, how the patient-side and provider-side surfaces fit together, and where its boundaries sit against Video Conferencing Application, Patient Scheduling, Patient Portal, Remote Patient Monitoring, Practice Management System, EHR, Clinical Communication Platform, and the education analog Virtual Classroom.

## Initial Boundary

Working hypothesis before research:

- A telehealth platform is software whose unit of work is the **remote clinical encounter** (commonly video) between an identified patient and a clinician — not a generic meeting.
- Suspected core surroundings: patient entry into the visit (scheduling and/or on-demand request, check-in, waiting room), the delivery surface itself, and hooks into clinical operations (documentation, prescribing, billing) under a healthcare regulatory posture.
- Nearest neighbors: Video Conferencing Application (generic meeting container — the sharpest seam), Patient Scheduling (booking machinery without the encounter), Patient Portal (patient-side access surface), Remote Patient Monitoring (continuous device data vs episodic encounter), Practice Management System (business loop vs care delivery), EHR (record vs encounter), Clinical Communication Platform (staff-to-staff vs patient-facing).
- Open questions going in: (1) Is the waiting-room/check-in flow definitional or common? (2) Is documentation/prescribing definitional or optional? (3) Is the D2C on-demand model (vendor's own provider network) structurally the same Type as the provider-side tool model? (4) Does a generic conferencing product with a healthcare compliance posture cross the seam?

## Research Questions

1. What is the unit of work a telehealth platform advances? (visit? encounter? appointment? session?)
2. Who are the participants, and how is each represented (patient account vs patient-as-guest; clinician account)?
3. How does a patient enter a visit — scheduled appointment, on-demand request, walk-in room link? What does the entry flow look like (check-in, waiting room, queue)?
4. What happens during the encounter beyond video/audio? (chat, screen share, photo capture, peripherals, interpreter, group multi-party)
5. What happens after the encounter? (documentation, notes, consent records, prescriptions, billing/claims, session history)
6. How do the three operating models differ: provider-side tool (clinician's own patients), embedded module inside a practice-management/EHR suite, and D2C/enterprise service with the vendor's own provider network?
7. What regulatory/compliance machinery is carried, and is it definitional or variant?
8. Where exactly is the seam vs generic video conferencing (including a conferencing product marketed to healthcare)?
9. Would older/regional telehealth (telephone consults, 1990s telepsychiatry over ISDN, store-and-forward) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, and different customer tiers:

| Product | Tier / philosophy | Why sampled |
|---|---|---|
| Doxy.me | Provider-side standalone virtual-room tool; individual-clinician pole (free tier); minimal-philosophy "telemedicine platform" | Documents the encounter+waiting-room model in isolation from any suite; strong Tier-1 help center |
| SimplePractice (Telehealth) | Telehealth as an embedded capability inside a practice-management/EMR suite (wellness/behavioral-health private practices) | Documents the embedded pole and the scheduling/billing/clinical-operations integration; strong Tier-1 help center |
| Teladoc Health | D2C/consumer membership service + enterprise virtual-care programs; vendor operates its own provider network | Documents the on-demand care-delivery pole where the platform is a service, not a tool |
| Amwell | Enterprise health-system/payer platform; vendor provider network (Amwell Medical Group) + EHR-embedded scheduled visits + virtual-care hardware | Documents the enterprise orchestration pole; "virtual visit platform designed for healthcare, which integrates with the electronic health record" |

Attempted but excluded: **Zoom for Healthcare** — the support knowledge-base article is client-side rendered (no content served to fetch) and the healthcare product page returned HTTP 404 (two attempts across two URLs). Recorded as a source-access limitation; no Zoom-specific operational claims are made anywhere in this research. Zoom was retained as a *conceptual* boundary test (generic conferencing with a healthcare compliance posture) only in the boundary discussion, with its positioning stated at market-common-knowledge strength, not as a researched product finding.

## Sources

Tier 1 (official operational documentation):

- Doxy.me Help Center — https://helpcenter.doxy.me/en/
  - Basic doxy.me features — https://helpcenter.doxy.me/en/articles/8272767-basic-doxy-me-features
  - Waiting Room — https://helpcenter.doxy.me/en/articles/8272808-waiting-room
  - Features and Apps collection (49 articles: Waiting Room, History, Dashboard, Analytics, Chat, Invite via email/text, Interpreter, Teleconsent, Scribe, Notepad, Payment, Photo Capture, Record, Screen Share, Shared Rooms, Group Call, Transfer, Timer, Transcript, Whiteboard, Dialer, Fax, File Transfer, CBT Activities, EMDR, Assessments, Closed Captions, Document Builder, Shared Rooms, roles/permissions) — https://helpcenter.doxy.me/en/collections/5677156-features-and-apps
- SimplePractice Support (Telehealth & ePrescribe category) — https://support.simplepractice.com/hc/en-us
  - Getting started with telehealth — https://support.simplepractice.com/hc/en-us/articles/360001196372-Getting-started-with-telehealth
  - (category also documents: Telehealth waiting room, screen share, whiteboard, mobile device, troubleshooting)

Tier 2 (official product pages):

- Doxy.me — homepage/product overview: https://doxy.me/
- Teladoc Health — homepage + audience pages (individuals / employers / health plans / hospitals & health systems / clinicians): https://www.teladoc.com/ , https://www.teladoc.com/organizations/hospitals-health-systems/virtual-care-platform (navigation-linked)
- Amwell — corporate site + platform page: https://business.amwell.com/ , https://business.amwell.com/the-amwell-platform/
- SimplePractice — telehealth product surface: https://www.simplepractice.com/telehealth/

Tier 3: none needed for the sampled poles.

Source-access limitations:

- Zoom for Healthcare unreachable (JS-rendered KB + 404). Boundary statements involving generic conferencing are calibrated accordingly.
- Teladoc's "/start/how-it-works" URL served the homepage (client-side routing); Teladoc visit-flow internals are NOT directly documented here — Teladoc observations are limited to what its public pages state (care services, member registration/app, provider network, health-system programs).
- Amwell www.amwell.com timed out once; business.amwell.com succeeded — used as the Amwell source.

## Product A — Doxy.me

### Key observations (evidence layer A unless noted)

Positioning: "The simple, free, and secure telemedicine platform… the leading video platform solely for healthcare professionals." (A)

- **Provider room model**: every provider gets a personal room URL (doxy.me/drparker); patients join by clicking the link in a browser — "No downloads, no patient login, browser-friendly." (A)
- **Check-in + Waiting Room flow**: patients "check in" from the room link; the provider has a Waiting Room — "This is the page your patients will see after they check in for an appointment… Just like a waiting room in a physical office." The provider sees who has checked in and starts the call. Default waiting room on all plans; custom waiting rooms on paid plans. (A)
- **Dashboard**: appointment details, the Waiting Room link, and invitations "from one place." (A)
- **Invite via email/text**; **History** ("track past appointment details"); **Analytics** (session metrics, monthly usage); **Chat** during session. (A)
- **In-visit tools**: screen share, photo capture, file transfer, whiteboard, group call, pause session, timer, closed captions, interpreter, virtual background, record, background-noise reduction, adaptive video quality, picture-in-picture ("keep your patient visible while taking EHR notes"). (A)
- **Documentation aids**: session history, SOAP and DAP notes, transcript, teleconsent, notepad, scribe, document builder. (A)
- **Clinic structure**: "Even if you work independently today, your account is structured as a clinic, so you can add providers or staff later" — premium adds shared rooms ("manage patient flow as a team"), patient transfer between providers, roles/permissions, clinic branding. (A)
- **Domain-specific tools**: CBT activities, EMDR tool, assessments (behavioral-health emphasis). (A)
- **Money/compliance**: payment collection in-session; fax; dialer (call patients by phone from the platform); HIPAA-compliant video, free BAA, SOC 2, GDPR, CPRA, PHIPA/PIPEDA, HITECH. (A)
- Marketing figures (1M+ providers, 12B+ minutes, 1.3M weekly sessions) — recorded here only, excluded from the final document. (A, marketing)

### Reading

Doxy.me is the purest expression of the provider-side pole: the platform's world is provider → room → checked-in patients → session → history, plus documentation/billing aids. It has no scheduling engine of its own at base (appointments appear on the dashboard), no claims machinery at base — the encounter and its clinic-shaped entry flow carry the Type. Layer: the waiting room + check-in + session + history loop is directly observed (A); its necessity for the Type is a cross-product judgment (see Comparison).

## Product B — SimplePractice (Telehealth)

### Key observations

Positioning (official, Tier-1): "Unlike a stand-alone provider for video appointments, SimplePractice offers a fully integrated suite of practice management tools. Having your video appointments, calendar, client details, and more all in one platform." (A)

- **Telehealth as a scheduling location**: telehealth is realized as a "**Video Office**" location in the practice's settings; telehealth can be turned on/off (turning it off removes the Video Office location). Telehealth appointments are calendar appointments held at that location; each generates a telehealth link. (A)
- **Patient entry**: appointment reminders carry telehealth links; clients can request telehealth appointments through the online Client Portal against clinician availability blocks ("clients will see a virtual office option in the Client Portal"); a separate client-side help center documents the client experience. (A)
- **Delivery surface**: browser-based ("Clients aren't required to install any applications… it seamlessly operates in their web browsers" — with optional telehealth mobile app); telehealth waiting room; screen share; whiteboard; virtual backgrounds. (A)
- **Clinical-operations integration**: telehealth links into superbills and electronic claim filing; telehealth-specific **Place of Service codes** (02 — other than patient's home; 10 — patient's home) configurable on the Video Office location; guidance to confirm codes/payers because "coverage for telehealth changes frequently." (A)
- **Regulatory machinery**: platform-level HIPAA compliance and BAA covering all features including telehealth; "Clinicians must be licensed in each state in which they want to provide telehealth appointments"; minors/consent rules depend on the state where the client is physically located during the visit; signposts to ATA/CCHP/CMS resources. (A)
- The telehealth capability ships on all subscription plans at no additional cost — embedded packaging, not a separate product. (A)

### Reading

SimplePractice proves the embedded pole: identical encounter/waiting-room/link machinery, but the entry flow is the suite's calendar + client portal, and the encounter drains into the suite's documentation/billing. The Type survives packaging as a module — the definitional content cannot be the standalone-ness.

## Product C — Teladoc Health

### Key observations

Positioning (official, Tier-2): "Teladoc Health connects patients and care providers for medical care, mental health, chronic condition management and more." (A)

- **Consumer membership model**: individuals register as members (member.teladoc.com registration/sign-in) and use the member app ("Get care now"); care offered across 24/7 Care ("Talk to a medical provider anytime, day or night"), Primary Care ("checkups, preventative care and prescriptions"), Mental Health (therapists and psychiatrists), Condition Management ("personalized coaching and connected devices"), Specialty Care (dermatology, expert medical opinion), Everyday Healthy Habits. (A)
- **Care-delivery service pole**: the vendor operates/contracts its own clinician workforce (dedicated Clinicians section, provider careers); care is delivered as a service to members (including "Care Without Insurance" purchase path). (A)
- **Organizational side**: employers, health plans, and hospitals & health systems buy virtual-care programs; the health-system arm includes a "Virtual Care Platform" with programs such as telestroke, virtual nursing, virtual sitting, inpatient and outpatient services, and devices; "Integrated Care" packaging. (A)
- Flow internals (request → queue → visit → prescription) are publicly described in outline ("Talk to a medical provider anytime… get the care you need from anywhere") but the operational help documentation was not directly reachable in this pass — flow details are NOT asserted at precise strength. (A for positioning; limitation noted)

### Reading

Teladoc represents the pole where the platform is not a tool sold to a practice but a care-delivery service: the patient is a member of the service, the clinician belongs to the vendor's network, and the encounter is orchestrated by the vendor. Structurally, the same three poles of the model appear — an identified patient, an identified clinician, and the encounter organized through the service's entry flow (on-demand request rather than the practice's schedule).

## Product D — Amwell

### Key observations

Positioning (official, Tier-2): "Amwell provides payers and healthcare systems with a single technology-based care platform… More than telehealth." "It starts with our future-ready platform—a convergence of technologies, services and devices that enables care delivery at scale." (A)

- **Enterprise platform (Converge)**: customer quote (El Camino Hospital CIO): "The Amwell Platform has provided our clinics with a **virtual visit platform designed for healthcare, which integrates with the electronic health record**" — the EHR-embedded scheduled-visit deployment; case studies document embedding into Epic and Oracle Cerner EHRs. (A)
- **Intelligent consult routing**: "Intelligently route virtual consults across your clinical network, third-party network, and the Amwell Medical Group to augment virtual visit volumes and ease staffing demands" — the vendor's provider network (Amwell Medical Group, ~2.2K active providers — marketing figure, research notes only) as an overflow/24/7 national coverage source. (A)
- **Virtual care hardware**: "Extend virtual care capabilities in hospitals and facilities by integrating software-enabled Carepoint devices to connect with the appropriate patient, device, and location." (A)
- **Consumer-side framing**: "real-time eligibility, credentialed providers, short wait times, and transparent pricing"; member journey/virtual primary care programs for payers; group therapy configuration observed in a customer quote (clinician "leading group therapy… see all the patients on their screen… access to chat"); crisis-safety workflow quote (clinician keeps patient on screen while viewing the patient's address from the EMR and can send help). (A)
- **Clinical programs beyond the visit**: virtual primary care, digital behavioral health (SilverCloud), specialty programs (dermatology, second opinion, cardiology, MSK, lactation, nutrition, psychiatry, therapy). (A)

### Reading

Amwell is the enterprise orchestration pole: the encounter machinery is embedded in the health system's EHR and room hardware, and the platform adds network routing (own clinicians as capacity) and program packaging. The encounter remains the unit; everything else is orchestration around it.

## Cross-product Comparison

| Structure / capability | Doxy.me | SimplePractice | Teladoc | Amwell | Layer |
|---|---|---|---|---|---|
| Remote clinical encounter as the central object (visit/session) | ✓ (room + session + history) | ✓ (telehealth appointments at "Video Office") | ✓ (care visits; service-delivered) | ✓ (virtual visits embedded in EHR) | B→C |
| Identified patient bound to identified clinician per encounter | ✓ (patients of the provider's room) | ✓ (clients of the practice) | ✓ (members ↔ network clinicians) | ✓ (patients ↔ health-system clinicians/network) | B→C |
| Encounter organized through a care-entry flow (scheduled and/or on-demand queue), not ad-hoc meeting invites | ✓ (check-in → waiting room; dashboard appointments) | ✓ (calendar + client-portal requests → link → waiting room) | ✓ (on-demand 24/7 request; member app) | ✓ (scheduled visits; consult routing) | B |
| Patient joins without install/without patient account (or with a light member identity) | ✓ ("no downloads, no patient login") | ✓ (browser; optional app) | member account (service pole) | ✓ ("without needing to download anything" — customer quote) | B (shape varies by pole) |
| Waiting room / patient queue | ✓ (default on all plans) | ✓ (telehealth waiting room) | (not directly observed — limitation) | (scheduled-visit flow; not article-documented) | B (2 products direct; treated as common, not definitional) |
| In-visit delivery surface: video (dominant) + audio + chat; multi-party possible | ✓ (group call) | ✓ (group-capable; whiteboard/screen share) | ✓ (video visits; implied) | ✓ (group therapy quote) | B |
| Invitations/links into the encounter | ✓ (email/text invite) | ✓ (reminders with telehealth links) | (member app entry) | (EHR/portal entry) | B |
| In-visit clinical aids (screen share, photo capture, file transfer, captions, interpreter, whiteboard) | ✓ (extensive) | ✓ (screen share, whiteboard) | (not directly observed) | (not directly observed) | B (2 products) — common, not definitional |
| Documentation support (notes templates, transcript, session history, teleconsent) | ✓ (SOAP/DAP, transcript, teleconsent, scribe) | ✓ (suite documentation module adjacent) | (service-side; not observed) | (EHR is the record — integration) | B (packaging varies: in-platform ↔ in-EHR) |
| Encounter→billing hooks (payment, telehealth claim/POS codes) | ✓ (payment in session) | ✓ (POS 02/10, superbills, claims) | (service pricing; not observed) | (eligibility/pricing on consumer side) | B — common; machinery is region/payer-dependent |
| Healthcare privacy/compliance posture (BAA/HIPAA-class) | ✓ (HIPAA, BAA, SOC 2…) | ✓ (HIPAA, BAA platform-wide) | (regulated service posture; pages state compliance focus) | (enterprise healthcare posture) | B — universal in-sample; regime-specifics vary by geography |
| Vendor-operated provider network delivering the care | ✗ (tool) | ✗ (tool) | ✓ (network clinicians) | ✓ (Amwell Medical Group as overflow/24/7) | A/product-specific at this strength → pole variant |
| EHR embedding of the encounter | ✗ (companion: picture-in-picture beside EHR) | ✗ (suite is separate from telehealth core) | (health-system programs) | ✓ (embedded in Epic/Cerner) | A/pole variant |
| Virtual care hardware (carts/devices) | ✗ | ✗ | ✓ (devices for health systems) | ✓ (Carepoint) | A/optional pole capability |
| Behavioral-health-specific tooling (CBT activities, EMDR) | ✓ | (suite serves behavioral health; tools not article-documented) | ✓ (mental health programs) | ✓ (behavioral health programs) | A/domain emphasis — variant, not definitional |
| RPM/connected devices attached to encounters | ✗ | ✗ | ✓ (condition management with connected devices) | (monitoring programs referenced) | A/optional |

## Canonical Model (abstraction result)

### Level 0 — Defining Invariant (deliberately small)

The Telehealth Platform is recognizable by exactly three jointly-held properties:

1. **Remote clinical encounter as the unit of work.** The platform's central object is the visit/consultation through which clinical care is delivered at a distance. Remove it → generic video conferencing / meeting tool.
2. **Two-sided clinical participants.** Each encounter binds an identified patient (participating as a patient of a practice/service) to an identified clinician (participating as the care provider). Remove the patient side → generic meeting tool; remove the clinician side → peer calling.
3. **Care-delivery context.** The encounter is anchored in a care-delivery operation — scheduled, requested, or queued as clinical work within a practice/service — and handled under the posture of regulated clinical care (healthcare privacy/compliance for the encounter). Remove it → conferencing with healthcare branding; the encounter stops being clinical work.

Jointly held and load-bearing: 1 alone = video conferencing; 2 alone = generic calling; 3 alone = a compliance program; 1+2 without 3 = generic calls between patients and doctors (e.g., a consumer video app used ad hoc); 1+3 without 2 = anonymous broadcast care surfaces, which the market does not treat as telehealth visits.

### Level 1 — Common Mature Structure (present in most modern products, not definitional)

- waiting room / patient check-in queue (2/4 direct; market-wide expectation)
- scheduling integration or an on-demand request queue as the entry mechanism
- link/invitation-based patient access; browser join without install (patient-side identity shape varies by pole: guest link vs member account)
- in-visit delivery surface: video (dominant) + audio + chat; multi-party configurations
- in-visit clinical aids: screen share, photo/file exchange, captions, interpreter
- session history and documentation support (in-platform notes/templates or handoff to EHR)
- consent capture for telehealth (teleconsent)
- payment/claim hooks around the encounter
- healthcare privacy/compliance machinery (BAA-class agreements, compliance pages)

### Level 2 — Variant / Optional Structure

- operating model: provider-side tool (Doxy.me pole) ↔ embedded suite module (SimplePractice pole) ↔ enterprise EHR-embedded platform with routing/hardware (Amwell pole) ↔ service with vendor's own provider network (Teladoc/Amwell-Medical-Group pole)
- entry mechanism: scheduled appointment vs on-demand queue
- domain emphasis: primary/urgent care, behavioral health (longer sessions, CBT/EMDR-class tools), specialty programs (telestroke, dermatology)
- device/hardware layer: virtual care carts/devices, peripherals
- EHR integration depth: companion use beside the EHR ↔ embedded scheduled visits in the EHR
- billing machinery: US telehealth POS codes/claims ↔ direct-pay/payment-collection ↔ service-inclusive pricing
- multi-party configurations: interpreter, family member, supervising clinician, group therapy
- attached asynchronous components (photo submission for review) and RPM/condition-management extensions
- regional regulatory regimes (US state-by-state licensure vs other jurisdictions)

### Level 3 — Vendor-specific (research notes only)

- Doxy.me: room-URL model (doxy.me/name), Day Pass, Dialer, CBT Activities/EMDR games, clinic-structured accounts for solo users
- SimplePractice: "Video Office" location concept, POS 02/10 location-switching workaround, Therapy Finder
- Teladoc: Integrated Care/Teladoc One packaging, BetterHelp relationship, telestroke/virtual nursing/virtual sitting program names
- Amwell: Converge platform name, Carepoint devices, Amwell Medical Group as branded overflow network, SilverCloud behavioral health

### Anti-overfitting check (historical / market-sample)

- Would a **1990s telepsychiatry service** (scheduled patient, psychiatrist, dedicated video lines, clinic intake) fit? Yes — encounter + two-sided clinical participants + care-delivery context, with no browser, no cloud, no BAA-class wording. The core survives.
- Would a **telephone-consultation service** fit? Yes — video is not definitional; the remote clinical encounter is (audio-realized).
- **Store-and-forward teleradiology** (images sent for later interpretation, no live two-participant encounter) does NOT fit the L0 — it is a different mode of telehealth practice; the market's "Telehealth Platform" label today denotes the encounter-delivery Type. The dermatology photo-submit service sits at this seam (asynchronous component attached to an encounter-based service). Recorded as a boundary/uncertainty, not silently absorbed.
- The modern browser-no-install pattern (dominant in-sample) is held as a **common implementation of patient access**, not an invariant — older/regional implementations (phone lines, dedicated hardware, kiosk sites) satisfy the core.

## Vendor-specific Findings

See Level 3 above; additionally: Doxy.me markets usage figures (1M+ providers, 12B+ minutes, 1.3M weekly sessions) and Amwell markets coverage figures (~90M members, ~50 health plans, ~2.2K active providers, 98% visit success, 99.9% uptime) — all marketing figures, recorded here and excluded from the final document. SimplePractice's statement that telehealth ships on all plans at no additional cost is packaging evidence, not a market invariant.

## Boundary Findings

| Neighbor Type | Seam (what to remove/add to cross) |
|---|---|
| Video Conferencing Application | Conferencing's object is the meeting between meeting-participants; telehealth's object is the clinical encounter between patient and clinician inside a care-delivery context (entry flow as clinical work, regulated posture, clinical operations hooks). A conferencing product marketed to healthcare with a compliance posture does NOT automatically cross: the seam is the care-delivery context, not compliance alone (Zoom-for-Healthcare-class products sit on the conferencing side unless they add the care-delivery context). Boundary test sample (Zoom) was unreachable — seam statement calibrated to structural reasoning + market naming, flagged in Uncertainties. |
| Patient Scheduling | Scheduling owns the booking machinery; telehealth consumes bookings as the entry into the encounter. Remove the encounter delivery → Patient Scheduling. |
| Patient Portal | Portal is the patient-side access surface (records, messages, results); telehealth is the care-delivery surface. Portals commonly *link into* telehealth visits (SimplePractice client portal request flow) without being the encounter system. |
| Remote Patient Monitoring | RPM is continuous device-data collection between encounters; telehealth is the episodic encounter. Teladoc's condition-management pairing shows they attach (RPM data into encounters) but remain distinct Types. |
| Practice Management System | PM owns the practice's business loop (registration, scheduling, billing); telehealth owns encounter delivery. SimplePractice documents the embedded packaging (telehealth as a location/module of the PM suite) — packaging does not merge the Types. |
| Electronic Health Record / EHR | EHR owns the clinical record; telehealth delivers the encounter and drains documentation into the record (Amwell embedded-in-EHR case studies; Doxy.me picture-in-picture "while taking EHR notes"). |
| Clinical Communication Platform | Clinical communication is staff-to-staff (care teams); telehealth is patient-facing encounter delivery. |
| Virtual Classroom | Same genus (scheduled remote sessions with a lead and attendees, waiting-room-class entry), but education domain: learner-teacher, no clinical participants, no care-delivery context/regulatory posture. |
| ePro/eConsult & store-and-forward services | Asynchronous review without a live two-participant encounter lacks the L0 unit; when attached to an encounter-based service it is a component, not the Type. |

## Uncertainties

1. **Zoom-for-Healthcare seam placement**: the intended boundary-test sample was unreachable (JS-rendered KB; 404 product page). The claim "a generic conferencing product with a healthcare compliance posture remains on the conferencing side" rests on structural reasoning + market naming conventions, not on a researched product in-sample. Flagged for a future joint-review pass with the Video Conferencing Application leaf if one is processed.
2. **Teladoc visit-flow internals** were not directly documented (help center not fetched; how-it-works URL served the homepage). Teladoc is used as evidence of the service pole's *shape*, not of its operational details.
3. **Waiting room universality**: directly documented at 2/4 sampled products (Doxy.me, SimplePractice); treated as common-mature, not definitional. Some enterprise/EHR-embedded deployments may realize entry differently (EHR-launched visit) — not directly observed.
4. **Store-and-forward boundary**: whether the market would admit a purely asynchronous "telehealth platform" is unresolved; this research holds the synchronous (or at least live two-participant) encounter as the Type's unit and records the disagreement zone.
5. **Regional breadth**: all sampled products are US-market-rooted; non-US telehealth platforms (e.g., national-health-service virtual consultation platforms) were not sampled. The L0 was abstracted to be regime-neutral (no HIPAA/US-licensure terms in the invariant), but this rests on the historical check rather than on sampled non-US products.

## Final Synthesis

A Telehealth Platform is the software through which clinical care is delivered remotely. Its defining core is small: the remote clinical encounter as the unit of work, binding an identified patient to an identified clinician, anchored in a care-delivery context (entry into the encounter as clinical work — scheduled, requested, or queued — under the posture of regulated clinical care). Around that core, mature products add the market-expected machinery: waiting-room/check-in entry, link-based patient access without install, video+audio+chat delivery with clinical aids, documentation and consent capture, billing hooks, and compliance agreements. The Type is realized across three packaging poles — standalone provider tool, embedded suite/EHR module, and vendor-operated care service with its own network — and none of the packaging is definitional. The sharpest boundary is against generic video conferencing: the difference is not the video, the compliance certificate, or the healthcare marketing — it is whether the encounter is organized and carried as clinical work.
