# Research Notes — Virtual Classroom

Research date: **2026-09-09**

## Research Goal

Understand the Virtual Classroom as an Application Type: what its defining structure is, how a live lesson actually flows through it (before → during → after), which capabilities are standard versus optional or vendor packaging, and where its boundaries sit against the neighboring §23 Types (LMS, Tutoring Platform, Classroom Management, Online Proctoring, MOOC Platform) and against the neighboring media Types (Video Conferencing, Webinar Platform).

This pass also **discharges two ratified forward flags**:

1. `tutoring-platform` (§23, processed 2026-09-09): "strongest shared surface, different center — every sampled tutoring platform ships an in-platform classroom, but the room is separable (marketplace pole documents external-video fallback; operator-side tutoring-business software integrates a third-party classroom). Removal tests both ways recorded; seam should be ratified when this pass runs."
2. `classroom-management` (§23, processed): "joint-review flag — a virtual classroom delivers the lesson itself online … classroom management observes and controls an in-room or device-equipped class … recommend joint review when virtual-classroom is processed."

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a Virtual Classroom is the teacher-led live "room" for online teaching — video/audio plus a teaching surface (whiteboard/slides) plus class interaction mechanics (raise hand, chat, polls, breakouts) plus participation control in the teacher's hands.
- Most likely confusions: LMS (persistent course container — asynchronous), Tutoring Platform (service formation + roster + commerce), Video Conferencing (generic meetings), Webinar Platform (broadcast to audience), Classroom Management (control/monitoring of devices/behavior), Online Proctoring (same media, integrity purpose).
- Unknowns going in: is a persistent room definitional or common? Is the lesson surface definitional or just dominant? Where exactly does the Type end and video conferencing begin, given Zoom-class products now ship whiteboards/polls/breakouts too?

## Research Questions

1. What is the unit of work: a "room", a "class", a "session"? How do these objects relate?
2. What role/permission structure exists (teacher vs learner; moderator/speaker variants)?
3. What does the teacher actually do in the room, in order? (official teaching lifecycle)
4. Which interaction mechanics are education-native (vs meeting/broadcast mechanics)?
5. What persists after a session (recording, attendance, analytics, board state)?
6. How is the room reached (standalone console vs LMS embed vs link)?
7. What surrounds the room (content library, class management, registration, branding) and is any of it definitional?
8. What distinguishes the Type from video conferencing in the vendors' own words and structures?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Tier / Segment | Philosophy |
|---|---|---|
| BigBlueButton | open-source education-native reference; higher-ed + LMS infrastructure (default virtual classroom of major LMSs per its own site) | "Built for teachers", explicitly anti-"generic web conferencing" |
| Kaltura Virtual Classroom | commercial video-platform suite module; corporate training + education | persistent "continuous classroom" + training-event machinery (registration, branding, analytics) |
| ClassIn | K-12 / tutoring-native classroom (China-origin, global) | classroom-first ("a class is not a meeting"), blackboard-centric, discipline/reward mechanics, own admin backend |
| LearnCube | language-school / tutoring niche, white-label | browser-only minimal teaching room + lesson-material library; sells classroom as embeddable API |

Boundary anchors: generic video conferencing (Zoom-class) — positioned against by BigBlueButton and ClassIn verbatim; LMS conference tools — confirmed as a common LMS capability by `research/learning-management-system-lms.md` ("web conferencing in course … common").

## Sources

Tier-1 (official operational documentation):

- BigBlueButton — Educator Guide (Prepare / Teach / Reflect), https://support.bigbluebutton.org/docs/getting-started/educator-guide (fetched 2026-09-09)
- BigBlueButton — Support/KB welcome ("the complete virtual classroom platform"), https://support.bigbluebutton.org/hc/en-us (fetched)
- BigBlueButton — Documentation center ("mission is to build the most effective virtual classroom"; Greenlight "simple room manager"), https://docs.bigbluebutton.org/ (fetched)
- Kaltura — Virtual Classroom knowledge-center section (TOC: create classroom, user roles, logging in, Home/Team/Analytics/Integrations tabs), https://knowledge.kaltura.com/help/virtual-classroom (fetched)
- Kaltura — "Introduction to Kaltura Virtual Classroom" (continuous classroom, session management, analytics), https://knowledge.kaltura.com/help/introduction-to-kaltura-virtual-classroom (fetched)
- Kaltura — "Virtual classroom user roles" (Admin/Organizer/Speaker/Moderator with activity lists), https://knowledge.kaltura.com/help/virtual-classroom-user-roles (fetched)

Tier-2 (official product pages):

- BigBlueButton — Teachers/Features page (features list, LMS embedding claim, 2007 origin), https://bigbluebutton.org/teachers/ (fetched)
- ClassIn — Home + Virtual Classroom product page ("a class is not a meeting"; blackboard; 20+ tools; admin backend; IM/assignments/reports), https://www.classin.com/en/ , https://www.classin.com/virtual_classroom (fetched)
- LearnCube — Home / Virtual Classroom page (whiteboard, audio/video, browser-based, white-label, lesson materials, recording, API embedding), https://www.learncube.com/ (fetched)

Unreachable (source-access limitations):

- Adobe Connect — helpx.adobe.com returned 403; adobe.com product pages timed out (×2). Persistent "pods/layouts" room model **not verified first-hand**; excluded from evidence. The persistent-room concept is instead evidenced at Kaltura ("continuous classroom") and Greenlight ("room manager").
- docs.bigbluebutton.org teaching paths (404 — teaching docs relocated to support.bigbluebutton.org); Greenlight overview path (404; room-manager description captured from docs root instead); corp.kaltura.com/products/virtual-classroom/ (404); learncube.com/virtual-classroom.html (404 — content fetched from site root instead).
- ClassIn Help Center / User Guide not fetched (product pages only) → classroom-mechanics claims for ClassIn held at product-page strength.
- First-generation (2000s) virtual classrooms (Elluminate/Wimba/Centra class) not fetched — historical check reasoned canonically, not product-verified.

Sibling evidence reused from already-processed passes: `tutoring-platform` (in-platform classroom separable; external-video fallback), `classroom-management` (control/monitoring vs delivery), `learning-management-system-lms` (web conferencing in course = common capability), `online-proctoring-platform` ("same media, no instruction, output is an integrity record"), `mooc-platform` (live sessions optional enrichment vs asynchronous self-serve).

## Product Observations

### BigBlueButton (A = directly observed)

- Self-positioning: "created in a classroom, not a boardroom"; "a generic web conferencing system falls far short of the needs of teachers and students". Mission (docs center): "build the most effective virtual classroom". [A]
- Official teaching lifecycle (Educator Guide), three stages: **Prepare** (set up your room — create rooms, configure settings, invite participants; create engaging content — upload presentations, set up "Smart Slides" for polling) → **Teach** (manage your class — assign roles, manage students, keep time; teach — present slides, share screen, play external videos; engage with active learning — polls, quizzes, check understanding in real time; assess & give feedback — Learning Analytics Dashboard) → **Reflect** (recordings — record sessions, manage formats/access; review your class — analyze engagement data, improve next session). [A]
- Feature set (official features page): user list, chat (public + private), presentation area laid left-to-right, document upload (PowerPoint/Word/PDF/images), whiteboard + **multi-user whiteboard**, breakout rooms, polling, shared notes, screen share, hand raise, emojis, webcam video, video playback options, Learning Analytics Dashboard (who is attending / participating / learning). [A]
- Distribution: "deeply embedded into major learning management systems … adopted by Canvas, Moodle Cloud, Sakai, Jenzabar, D2L, and Schoology as their default virtual classroom" (vendor claim; market-representation signal, not a market-size fact). [A for vendor's own claim]
- Greenlight = "the simple room manager tailored for BigBlueButton" — rooms as a managed object outside the LMS context. [A]
- Origin: developed 2007 at Carleton University (vendor-stated). Open-source project + commercial hosting split. [A]

### Kaltura Virtual Classroom (A)

- Positioning: "an all-in-one platform built for effective training and learning experiences … create, brand, promote, and manage sessions with powerful interactive features and detailed analytics." Training-market flavor (onboarding/upskilling/customers-and-partners). [A]
- **Continuous classroom**: "maintains all settings, branding, and files from session to session, eliminating repetitive setup and ensuring you're always ready to pick up where you left off" — the strongest first-hand statement of room persistence in the sample. [A]
- Console structure (knowledge-center TOC): Home page → create a virtual classroom; Home / Team / Analytics / Integrations tabs; account setup; logging in. Sessions: prepare for session / manage a session / participate in a live session. [A]
- Roles: **Admin** (account-wide: create/view/edit/delete all classrooms, team management, account analytics, integrations), **Organizer** (owns assigned classrooms: manage details/title/description, branding logo/banner/theme, registration page/form, users and role assignment, emails/notifications, analytics + downloadable reports), **Speaker** (subject expert; sends polls/notifications during session), **Moderator** (Q&A chats, group chat moderation, interactivity tab — polls, message board). Role naming is event/training-flavored rather than teacher/student. [A]
- Related machinery in the same knowledge tree: "Kaltura Meetings / Virtual Classroom" guides (join a live room, set up your live room, moderating live sessions, upload and share files, meeting tools, breakout, quizzes, participant guide, mobile), LMS extensions for Canvas/Blackboard/Brightspace/Moodle/Sakai. [A]
- Product internals observed: separate "Meetings" and "Virtual Classroom" products sharing infrastructure (login URL pattern) — same vendor, two surface products. [A; naming withheld as L3]

### ClassIn (A, product-page strength)

- Positioning: "A class is not a meeting, and we know it"; "near-limitless blackboard. Save, share, and review blackboard writing any time after a class ends"; "Bring the spirit of offline classes online — reward participation … spotlight on individual students". [A Tier-2]
- Classroom feature set (product page): Interactive Blackboard, Break-out Rooms, Teaching Tools, Resource Center, Attendance. [A Tier-2]
- Surrounding ecosystem (product page): IM System (teacher↔student communication), Assignments & Grading, Learning Reports, **Class Management backend** ("one intuitive backend system to manage all classes and personnel and view analytics"), Virtual Lab simulations, admin portal (assign tutors, store materials, supervise ongoing sessions, auto-generated learning reports to parents). [A Tier-2]
- Surfaces: cloud-based "20+ tools" (group chat, media storage, multiway screen-sharing, native web browser, breakout rooms, drag-and-drop STEM experiments …). [A Tier-2]
- Segments: K-12, Higher Education, Tutoring (all-in-one platform), Independent Teachers. LTI + SDK integration surfaces; hybrid classroom hardware line (ClassIn X). [A Tier-2]
- Format artifacts: classroom "templates" gallery of ready-made EDB files (proprietary lesson-file format). [A Tier-2]

### LearnCube (A, product-page strength)

- Positioning: "The virtual classroom made for teaching & tutoring"; "purpose-built virtual classroom for teaching languages online"; "A generic web-conferencing software leaves you with few options for branding" — explicit anti-generic-conferencing positioning on the branding axis. [A Tier-2]
- Classroom feature set: interactive online whiteboard (draw, type, annotate, load content, switch between multiple whiteboards), reliable audio & video (WebRTC), download-free browser delivery, white-label (logo, colours, domain), upload lesson materials (multi-media content saved and accessible in class), class recording. [A Tier-2]
- Business shape: sells the classroom standalone (sign-up, free trial) AND as API/white-label embedding ("integrate our highly scalable APIs into your existing language teaching platform"); separate **Online School Platform** product for scheduling/payments/reporting "if you have more than 10 teachers" — the school-operations machinery is a *different product* from the classroom. [A Tier-2]

## Cross-product Comparison

| Structure | BigBlueButton | Kaltura VC | ClassIn | LearnCube | Layer |
|---|---|---|---|---|---|
| Live real-time teaching session as unit of work | ✅ rooms/classes, prepare-teach-reflect | ✅ sessions on a classroom | ✅ classes/sessions | ✅ live classes | definitional |
| Instructor-side authority over participation & tools | ✅ assign roles, manage students, keep time | ✅ organizer/moderator manage session, users, interactions | ✅ teacher spotlight/reward/spotlight controls | ✅ teacher-run room | definitional |
| Shared lesson surface (whiteboard/slides/documents, annotation) | ✅ presentation + whiteboard + multi-user whiteboard | ✅ upload/share files, meeting tools | ✅ interactive blackboard (center of product) | ✅ whiteboard as center | definitional |
| Class-shaped learner participation (chat, hand-raise, polls, breakouts, turn-taking) | ✅ hand raise, chat, polls, breakouts, shared notes | ✅ chat/Q&A, polls, breakout, quizzes | ✅ chat, breakout, reward mechanics | ✅ chat/Audio-video class interaction | definitional |
| Persistent room/classroom object | ✅ Greenlight room manager; LMS-created rooms | ✅ "continuous classroom" keeps settings/files | ✅ classes in admin backend | ✅ reusable classroom (implied by materials/branding) | common (not definitional — see Rejected) |
| Content/courseware library bound to room or teacher | ✅ presentation upload | ✅ files persist in classroom | ✅ Resource Center | ✅ lesson materials | common |
| Session recording | ✅ + formats/access management | ✅ (via platform video stack) | ✅ (review blackboard writing after class; recording implied) | ✅ | common |
| Attendance / participation analytics | ✅ Learning Analytics Dashboard | ✅ Analytics tab, downloadable reports | ✅ Attendance, Learning Reports | ⚠️ not on fetched page | common |
| Breakout rooms | ✅ | ✅ | ✅ | ⚠️ not on fetched page | common |
| Polls / quizzes in-session | ✅ | ✅ quizzes, polls | ✅ (teaching tools) | ⚠️ not on fetched page | common |
| LMS integration (LTI/link/API) | ✅ (core distribution) | ✅ LMS extensions | ✅ LTI + SDK | ✅ API embedding | common (dominant channel, not definitional) |
| Surrounding school/training ops (class management, assignments, reports, registration) | ❌ (delegated to LMS) | ✅ registration, notifications, reports (training-market) | ✅ own admin backend | ❌ (separate product) | variant packaging |
| Client form | browser (HTML5), self-hosted server | web app | desktop/mobile apps + cloud | browser-only (WebRTC) | variant |
| Subject-specialized content | — | — | EDB templates, STEM labs | ESL library (CEFR-aligned) | variant |

Vendor's-own-words boundary evidence: BigBlueButton "generic web conferencing system falls far short of the needs of teachers and students"; ClassIn "A class is not a meeting"; LearnCube "a generic web-conferencing software leaves you with few options for branding" — three independent vendors define their product *against* video conferencing. [A]

## Canonical Model

### L0 — Defining Invariant (minimal)

Four jointly-held structures. Remove any one and the product stops being a virtual classroom:

1. **The live instructional session as the unit of work** — a bounded real-time occasion in which teaching happens, launched on demand or joined at a scheduled time. Remove → a meeting tool being used for teaching, or an async content platform.
2. **Instructor authority over the room** — one side (teacher / instructor / moderator) holds elevated control: admitting and managing participants, granting and revoking speaking/interaction rights, assigning roles, keeping the session on track. Remove → peer meeting; nobody is teaching.
3. **The shared lesson surface** — a shared instructional display (whiteboard, slides, documents, courseware) that is the organized center of lesson delivery, visible to all and markable by those granted access. Remove → video conferencing/webinar with talking heads.
4. **Class-shaped participation** — many learners with instruction-oriented interaction channels: request-to-speak (hand raise), chat, polls/quizzes, breakout small groups, per-learner spotlight. Remove → broadcast/webinar (audience, not class).

Load-bearing decomposition:

- 1 alone = video meeting
- 2 alone = roster/scheduling tool
- 3 alone = whiteboard application
- 4 alone = chat/broadcast surface
- 1+2 without 3+4 = a class run over generic video conferencing (usage overlap, not the Type)
- 1+3 without 2+4 = collaborative whiteboard session
- 1+4 without 2+3 = group video chat / live stream with chat
- 1+2+3 without 4 = presentation/webcast tool
- 1+2+4 without 3 = meeting tool with classroom choreography but no lesson surface (Zoom-class edge)
- 2+3+4 without 1 = content authoring/preview without a live occasion

### L1 — Common Mature Structure (standard capabilities of mature products)

- persistent room/classroom object that keeps settings, content, branding between sessions
- content/courseware library or upload attached to room or teacher
- in-session chat (public, commonly private)
- hand-raise / request-to-speak mechanics
- polls and quizzes during class
- breakout rooms for small-group work
- screen/content sharing by the instructor (commonly multi-way)
- session recording, managed afterwards
- attendance and participation analytics; downloadable reports
- LMS integration surface (LTI / link / API) — the dominant distribution channel in education

### L2 — Variant / Optional Structure

- sector packaging: higher-ed (LMS-embedded), K-12 (school-backed), tutoring/language schools (standalone + white-label), corporate training (registration, promotion, reporting)
- room persistence philosophy: per-occasion rooms created ad hoc vs continuous classrooms vs LMS-course-scoped meetings
- client form: browser-only vs installable app vs self-hosted open-source server + hosted offering
- surrounding ops layer: own class-management backend / assignments / grading / learning reports / IM (some vendors) vs none (delegated to LMS or separate product)
- subject-specialized machinery: language-teaching content libraries, STEM virtual labs, proprietary lesson-file formats and template galleries
- extra delivery surfaces: hybrid classroom hardware, mobile apps, native web browser inside the room
- white-label/branding and embed-as-API (classroom sold as a component)
- monetization/registration pages and email/notification machinery (training-market flavor)
- era-current: AI teaching/lesson-generation assistants (beta-stage at one sampled vendor)

### L3 — Vendor-specific (research notes only)

- Kaltura: Admin/Organizer/Speaker/Moderator role naming; registration-page machinery; product built on an acquired conferencing stack (distinct login host); "Meetings" vs "Virtual Classroom" product split; marketing scale claims omitted.
- BigBlueButton: Greenlight room manager; open-source governance + commercial hosting split; Carleton University 2007 origin; "75% of LMS market" / "65 languages" / daily-schedule marketing figures omitted (not independently verified).
- ClassIn: EDB proprietary lesson-file format + template gallery; reward/badging economy; ClassIn X hybrid hardware; IM/assignments/learning-report module names; "60,000+ organizations / 30M+ sessions monthly" marketing figures omitted.
- LearnCube: AI Teacher Assistant (beta); CEFR-aligned ESL content library; white-label domain branding; 10-teacher threshold for its separate school platform.

## Rejected Findings (anti-overfit)

- **"20+ tools" / feature-count framing** (ClassIn marketing) — not a structure; rejected.
- **Persistent room as definitional** — rejected. BBB documents ad-hoc room creation and LMS-scoped meetings; LearnCube sells the classroom as a stateless-ish embeddable API; the tutoring marketplace pole documents teaching over external video tools with *no* virtual classroom product at all. Persistence is common (Kaltura's "continuous classroom" is its headline) but not invariant.
- **LMS embedding as definitional** — rejected. It is the dominant *channel* (BBB's LMS-default claim; Kaltura LMS extensions; ClassIn LTI), but standalone classrooms with their own admin backends are fully in-type (ClassIn, Kaltura standalone, LearnCube standalone).
- **Attendance/assignments/grading/learning reports as definitional** — rejected. Present where the vendor sells school ops (ClassIn), absent when an LMS or a separate product owns them (BBB, LearnCube's split). School-operations machinery belongs to neighboring Types.
- **Registration/promotion machinery as definitional** — rejected; training-market packaging (Kaltura only in-sample).
- **Blackboard-first UI layout as definitional** — rejected; layout differs (BBB left-to-right with user list and chat; ClassIn blackboard-centric; Kaltura stage-oriented). The *existence* of a lesson surface is definitional; its layout is not.
- **Whiteboard + polls + breakouts alone as the distinguishing edge vs video conferencing** — rejected as *sufficient* test: Zoom-class tools now ship all three. The distinguishing edge is the joint L0 structure (instructor authority + lesson surface + class participation organized for instruction), not any single feature.
- **AI features** — era-current, optional. Rejected from core.

## Boundary Findings

**1. vs Tutoring Platform — FLAG DISCHARGED, keep-both ratified.**
The classroom is the *room* (delivery medium + teaching machinery); the tutoring platform is the *service* (tutor roster, engagement formation, session commerce, quality loop). Removal tests both ways, now confirmed from this side: (a) remove roster/formation/commerce from a tutoring platform → what remains is a virtual classroom *plus* an empty marketplace — the room itself is exactly this Type's object; (b) remove the room from a tutoring platform → the platform still exists (documented external-video fallback and offline-ancestry sessions in that pass). Independently: every sampled virtual classroom here runs *without* any tutor roster or service commerce (BBB rooms, LearnCube rooms, Kaltura classrooms), while LearnCube and ClassIn demonstrate the reverse packaging (classroom first, school/tutoring ops adjacent or in a separate product). The tutoring pass's claim "in-platform virtual classroom NOT definitional [for tutoring]" is mirrored by "tutor roster/service commerce NOT definitional [for virtual classroom]". Seam = room vs service. **Ratified.**

**2. vs Classroom Management — FLAG DISCHARGED, keep-both ratified.**
A virtual classroom *delivers the lesson itself online* (live session, lesson surface, class participation). Classroom management *observes and controls* an in-room or device-equipped class (device monitoring, screen control, behavior/attention tracking). Overlap case: remote learners joining a managed physical classroom — the management product's surface remains control/monitoring even then. Purpose-and-record test: the virtual classroom's output is a delivered lesson (recording, attendance, analytics for instruction); classroom management's output is control/observation state (device screens, behavior records). No sampled virtual classroom controls learner devices; no classroom-management product (per that pass's own evidence) delivers the lesson. **Ratified.**

**3. vs Learning Management System.**
The LMS is the persistent course container: curriculum, assignments, grades, asynchronous content across a term. The virtual classroom is the live delivery surface *inside* an occasion. LMS research records "web conferencing in course" as a common LMS capability, and this sample confirms the embedding channel (BBB adopted as LMS default; Kaltura LMS extensions; ClassIn LTI). Remove the persistent course container (curriculum/assignments/grades) → virtual classroom; remove the live session → LMS. Distribution-channel overlap is real but the centers of gravity do not collide.

**4. vs Video Conferencing Application.**
Same media, different organizing structure. Generic conferencing organizes *peer meetings*; the virtual classroom organizes *instruction*: a designated instructor holds authority over participation and tools, a lesson surface is the delivery center, and participation mechanics are class-shaped (hand-raise turn-taking, polls as comprehension checks, breakouts as pedagogy). Three vendors define their products *against* generic conferencing in their own words (BBB, ClassIn, LearnCube). Zoom-class products used to teach a class are usage overlap, not the Type — the same way a phone call can deliver a lesson without being a virtual classroom. The market even sells the boundary: one vendor's separate "Meetings" and "Virtual Classroom" products share infrastructure but ship as two surfaces.

**5. vs Webinar Platform.**
Webinar = broadcast to an audience (registration, promotion, one-to-many delivery, moderated Q&A). Virtual classroom = multi-way class participation where learners interact with the lesson surface and each other under instructor authority. The sample shows a genuine market gradient: Kaltura's role vocabulary (Speaker/Moderator/registration pages) is training-event-flavored, and corporate-training deployments drift webinar-ward. Seam test: if learners cannot be granted the surface or small-group collaboration and the structure is presenter→audience, it is webinar territory. The virtual classroom is recognizable when class participation (L0-4) exists.

**6. vs Online Proctoring Platform.** Same media (webcam, chat, observation), different purpose and record: proctoring has no instruction; its output is an integrity record bound to an assessment delivered elsewhere. Ratified in that pass; no conflict observed here.

**7. vs MOOC Platform.** Live human-led instruction in a closed room vs open-enrollment asynchronous course catalog. Live sessions appear in MOOCs only as optional enrichment (that pass's finding); the virtual classroom has no catalog and no open self-service enrollment.

**8. vs Digital Whiteboard.** The whiteboard is the lesson surface (L0-3) — a component inside the room. A whiteboard application has no instructor authority over a class of participants and no live-instruction occasion as its unit.

## Historical / Market-Sample Check

Would older, regional, differently positioned products still fit the L0? First-generation online-teaching rooms of the 2000s (the Elluminate/Wimba/Centra generation — audio + shared slides/whiteboard + text chat + instructor moderation, before webcams, breakouts, or analytics were standard) satisfy all four L0 legs with none of the modern machinery: live session, instructor authority, shared lesson surface, class-shaped participation (chat-based). Regional products (China-origin ClassIn in-sample; regional classroom products elsewhere) fit. The L0 names no medium detail (webcam-optional), no client form, no sector, no persistence model, no feature set — historical fit holds. Correspondingly the L1 list is explicitly modern-era (breakouts, analytics, LMS/LTI embedding).

## Uncertainties

1. Adobe Connect could not be fetched (403/timeout). The longest-lived commercial persistent-room implementation is therefore **not directly evidenced**; persistent-room claims rest on Kaltura + Greenlight instead. Precision about pods/layouts intentionally omitted everywhere.
2. ClassIn claims held at product-page strength (help center not fetched) — classroom mechanics (reward economy, spotlight) not verified at help-article depth.
3. Kaltura's role model is training-event-flavored; the clean teacher/learner role split is best evidenced at BigBlueButton ("assign roles, manage students"). The canonical claim is "instructor side vs learner side with elevated rights on the instructor side" — role naming varies by product and market.
4. First-generation (2000s) products were not fetched; the historical check is canonical reasoning, not product-verified evidence.
5. Attendance/analytics depth varies (LearnCube's fetched page does not mention it) — held common, not universal.

## Final Synthesis

The Virtual Classroom is the live delivery surface of online teaching. Its defining core is exactly four jointly-held structures: the live instructional session as the unit of work, instructor authority over participation and tools, the shared lesson surface as the delivery center, and class-shaped multi-way learner participation. Everything else — persistent rooms, content libraries, recordings, analytics, breakouts, LMS embedding, school-operations backends, white-labeling, AI assists — is standard mature capability or market packaging, not definition. The two forward flags are discharged with keep-both ratifications: the room is separable from the tutoring service, and lesson delivery is separable from classroom control/monitoring. The Type's sharpest edges are against generic video conferencing (usage overlap, structural difference, confirmed by vendors' own positioning) and against the LMS (occasion vs container).
