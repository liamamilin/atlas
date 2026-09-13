# Research Notes — Classroom Management

Research date: 2026-09-07
Leaf: Classroom Management (DIRECTORY.md §23 Education, Research & Knowledge Institutions)
Slug: classroom-management

## Research Goal

Understand what "Classroom Management" software actually is as an Application Type — from real products, not from the term's marketing usage — and produce a vendor-neutral Application Document. The term is heavily overloaded in the education market (it is used for device-control suites, behavior-point apps, whole-school platforms, and even childcare room/ratio management), so a central goal is to find the smallest structure that makes the Type recognizable and to mark the boundaries against neighboring Types.

## Initial Boundary

Initial hypothesis (before research):

- Core use: teacher-facing software for running the **live classroom** — observing and directing students in the moment (device/screen monitoring and control, behavior points, in-the-moment attendance, seating, timers/randomizers).
- Nearest neighbors: Virtual Classroom, Student Behavior Management, Student Attendance System, Learning Management System, Assignment Management (already processed — its notes record "classroom management governs the live classroom (devices, behavior, attendance in the moment); assignment management governs work completed across time"), UEM/Endpoint Management, SIS.
- Known ambiguity: the same words "classroom management" appear in childcare software (rooms/ratios — see processed leaf childcare-management-system) with a completely different meaning.
- Unknowns: whether device monitoring or behavior tracking is definitional (or two separate poles); how sessions start; whether lab-era products fit the same definition.

## Research Questions

1. What is the core object world (class, roster, session, student, device/screen, behavior event, seat)?
2. How does a class session start — roster sources, connection models (agent / extension / join code / MIS sync)?
3. What can the teacher observe (thumbnails, live screens, tabs, register) and do (lock, push URL, restrict, message, award points)?
4. How does behavior tracking work (points, skills/reasons, negative events, reports, family visibility)?
5. How do attendance and seating work — in-the-moment or prepared-ahead?
6. What roles exist (teacher / student / IT admin / school leader) and what do permissions gate?
7. Where is the boundary with MDM/UEM, school-wide discipline systems, virtual classrooms, and LMSs?
8. Historical check: do lab-era (pre-cloud) products and behavior-only products fit one definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Pole / philosophy | Segment | Evidence quality |
|---|---|---|---|---|
| GoGuardian Teacher | GoGuardian | device-monitoring pole; cloud + browser extension; district-scale | US K-12 | Tier-1 (official docs site, fully fetched) |
| LanSchool (Air + Classic) | Lenovo (Stoneware) | classic lab-heritage device control; cloud (Air) + on-prem (Classic) | K-12, international | Tier-2 (official product pages; Air KB unreachable) |
| NetSupport School | NetSupport | classic full-featured desktop classroom management; on-prem heritage, multi-platform | K-12 + higher ed + corporate training, international | Tier-1/Tier-2 (official features pages, fully fetched) |
| ClassDojo | ClassDojo | behavior/community pole; freemium, teacher-first | global K-12 | Tier-1 (official help center, Zendesk, fully fetched) + Tier-2 product pages |
| Satchel One | Satchel (Team Satchel) | whole-school learning platform with classroom-management modules; UK framing (behaviour/detentions/MIS) | UK schools | Tier-1 (official help center, Intercom, fully fetched) + Tier-2 product page (JS-gated) |

## Sources

Fetched 2026-09-07:

- GoGuardian Help Center index: https://docs.goguardian.com/llms.txt (full Teacher section listed)
- GoGuardian Teacher Overview: https://docs.goguardian.com/products/teacher
- GoGuardian Teacher — Start a Classroom Session: https://docs.goguardian.com/products/teacher/start-a-classroom-session
- GoGuardian Teacher — Commands Overview: https://docs.goguardian.com/products/teacher/commands-overview
- LanSchool home: https://lanschool.com/
- LanSchool Air product page: https://lanschool.com/solutions/lanschool-air
- LanSchool Classic product page: https://lanschool.com/solutions/classic
- ClassDojo home: https://www.classdojo.com/
- ClassDojo Points page: https://www.classdojo.com/points/
- ClassDojo Help Center — For Schools and Districts: https://help.classdojo.com/hc/en-us/categories/200185275-For-Schools-and-Districts
- ClassDojo Help Center — Class Points and Reports section: https://help.classdojo.com/hc/en-us/sections/200472659-Class-Points-and-Reports
- ClassDojo Help Center — Class Setup and Access section: https://help.classdojo.com/hc/en-us/sections/200472579-Class-Setup-and-Access
- ClassDojo Help Center — What is Toolkit?: https://help.classdojo.com/hc/en-us/articles/115003740283-What-is-Toolkit
- NetSupport School home: https://netsupportschool.com/
- NetSupport School features page: https://www.netsupportschool.com/features/
- Satchel One Help Center home: https://help.satchelone.com/
- Satchel One Help Center — Staff collection: https://help.satchelone.com/en/collections/6936480-staff
- Satchel One — Behaviour events and badges: https://help.satchelone.com/en/articles/11095655-behaviour-events-and-badges
- Satchel One — Seating Plans: https://help.satchelone.com/en/articles/10657620-seating-plans

Source-access limitations:

- `help.lanschool.com` returned HTTP 301 (redirect, unreachable target); `helpdesk.lanschoolair.com` KB returned empty content twice → abandoned per network rules. LanSchool evidence is therefore Tier-2 (official product pages) only; no operational detail (exact commands, limits) claimed for LanSchool beyond what its product pages state.
- `satchelone.com` homepage returned empty (JS-gated); Satchel One evidence comes from its official help center (Tier-1) instead.
- `classdojo.com/teacher-toolkit/` returned 403; Toolkit contents taken from the official help-center article instead.
- GoGuardian Teacher docs are fully reachable (Tier-1) — the strongest single evidence source in this pass.

## Product Observations

### GoGuardian Teacher (evidence layer A)

Positioning: "Classroom management tool used by 2M+ teachers to review student activity, guide devices, and maximize instructional time in real time." Supported platforms: ChromeOS, Windows, macOS, iOS.

- **Class container**: "Classroom" with a student roster. Rosters sync from Google Classroom, Clever, ClassLink (OneRoster); classes can also be created manually with students added by enroll code, email, or CSV. Classes can be merged; co-teachers supported via Google Classroom sync.
- **Session model**: "A classroom session is the digital equivalent of a classroom period." Teacher picks a session length (new classes default to 45 minutes — product default, research-notes only) and starts the session; students with the GoGuardian extension installed and signed in to school accounts **join automatically** — no join link. Sessions can be scheduled (recurring, A/B block schedules) via a calendar. Multiple concurrent sessions allowed. Sessions end manually or at the scheduled end time; locks clear automatically at session end.
- **Observation**: Screens view shows each connected student as a tile with name, active tab, browsing activity; per-student screen view; Timelines view of browsing history; screenshots (saved to a Screenshots tab); Off-Task Alerts (automatic detection of off-task behavior).
- **Commands** (applied to one, selected, or all students): Lock/Unlock Screen (disables browser windows; lock clears at session end; lock carries over if the student joins another teacher's session), Open Tab, Close Tab, Screenshot, Annotate (colored circle on the student's screen, visible ~10 seconds), Close App (Windows), Exclude/Include Student (hides an absent student from views without removing from roster), Teacher Chat (1:1 messages + class-wide announcements).
- **Scenes**: saved web-filtering rule sets (allow mode / block mode, site rules, Quick Lists, auto-open tabs, tab limits, YouTube filtering) applied to the whole class or to Custom Groups during a session; teachers can temporarily override district filtering (Teacher Override configured by admins) — GoGuardian Admin enforces the district's base policy at all times.
- **Focus Tabs**: mark one tab as the priority tab; students cannot interact with other tabs until released.
- **Custom Groups / Student Groups**: divide the class and apply different Scenes/settings per group; groups persist across sessions.
- **Communication**: 1:1 Teacher Chat, class-wide announcements, audio/video calls with the class, Lecture/Presentation mode (screen share), Student Check-Ins (start a check-in, review responses).
- **Session history**: past sessions store browsing history, chat records, screenshots, check-ins, command log; session report emails; student browsing reports can be emailed as PDF.
- **Roster/identity**: district SSO (Google/Microsoft); teacher accounts provisioned from Google Directory or Clever/ClassLink; Org Management is the cross-product admin hub (roles, OU permissions, RBAC, audit log, chat-log access).
- **Not observed**: behavior points, seating charts, attendance marking, parent messaging. (GoGuardian's separate Parent app is admin-controlled sharing of browsing data — a different product line.)

### LanSchool (Air + Classic) (evidence layer A, Tier-2 pages)

Positioning: "a pioneer and innovator of classroom management software… 30 years as an edtech leader"; "helps teachers connect with students… both in the classroom and remotely." Two hosting solutions at one price: **LanSchool Air** (cloud) and **LanSchool Classic** (locally hosted on school servers).

- **LanSchool Air features** (product page): monitoring & protection (limit web, blank screen, lock devices), co-teaching (shared access for lead teachers, paraeducators, admins), screen monitoring (real-time thumbnails of all student screens, full-screen view of individual screens), messaging (teacher-to-student, student-to-teacher, teacher-to-classroom), raise hand (students discreetly request help), share screen (teacher broadcasts to all devices), push website (launch the same site on every device), snapshot (screenshots), battery status. Integrations: Google Classroom, ClassLink, Clever (roster sync on login).
- **LanSchool Classic features** (product page): everything above plus — remote control (log in to student devices to install apps/updates), web and app history (browsing, app, keystroke history), app limiting (allow/block apps per student), keyword alert (alerts on search terms sent to a central reporting server), limit print, broadcast student screen, launch app, mute audio, send/receive files (distribute and collect work), group chat, **testing** (digital tests up to 100 questions, auto-graded; voting on a single question with CSV export), device management (battery status, remote power on/off, tech console for IT, report server collecting browsing/keyword/app history, enterprise data collection on educator usage).
- **New**: AI-based "On-Task Monitoring" (announced as beta on the site banner).
- **Roster**: Google Classroom and Clever integrations sync class lists.
- **Not observed**: behavior points, attendance register, seating plans on the fetched pages.

### NetSupport School (evidence layer A)

Positioning: "market-leading classroom management software that helps teachers monitor student screens, manage classroom devices, deliver interactive lessons and keep students focused and engaged… across all major platforms and devices." Also marketed for corporate training and higher education.

- **Connection methods** (how a class is formed): Room Mode (by room), PC Mode (fixed list of machine names), User Mode (fixed list of logged-on users), Browse Mode (browse the network), SIS Mode (ClassLink OneRoster / Google Classroom).
- **Class Wizard**: select/create a lesson; enter name, lesson title, objectives, outcomes (shared with students).
- **Student register**: printable register taken by requesting standard and custom information from each student at the start of class.
- **Lesson plan**: pre-made task lists with timings and prompts. **Student resources**: links to websites/apps/documents shown in the Student Toolbar. **Password reset**: teacher can reset student system passwords without IT.
- **Student check-in**: visual options to gauge how students feel / their confidence at start or end of lesson (wellbeing).
- **Monitoring**: student screens (including dual monitors) via adjustable thumbnails; applications and websites (foreground and background); keyboard monitoring (target/inappropriate word lists highlighted); collaboration observation; full history of app/internet use per student.
- **Control**: blank/lock screens (locks mice and keyboards), remote control (to instruct or remedy), application and website controls (approved-only or restricted lists; profiles store ready-made lists), quick launch (launch/close apps or web pages on selected PCs), print control (authorization, per-student, page counts), external drive control (USB/CD/DVD), webcam disable.
- **Instruction**: screen share (teacher→all/selected; website access restricted to an approved list during sharing; recording left on student PCs), annotation tools, virtual whiteboard (students can interact), messages with clickable URLs, hand out/collect work (file transfer with readiness feedback).
- **Collaboration**: group leaders (student granted teacher rights for a task), chat (all/selected students; logged automatically).
- **Rewards**: student screen sharing (showcase work), student rewards (star/animated sticker shown on the toolbar, added to the Student Journal).
- **Assessment**: student testing (custom tests with text/picture/audio/video questions, auto-collated and marked), student survey (voting, results pie chart, group students by response), **Q&A module** (verbal questioning with modes: first-to-answer with bounce, enter-an-answer, pot luck/random selection, peer assessment, basketball questioning; rewards tracked for individuals/teams).
- **Student Journal**: records lesson content, notes, assessment results, rewards — revision aid and record.
- **Audio**: audio support (teacher voice during share/remote control), language lab (view all screens, see live audio activity, listen to a student's audio or microphone).
- **Student Toolbar** (what students see): lesson objectives/outcomes, time remaining, available websites/apps, status of print/audio/keyboard monitoring, chat and help request, USB access, Student Journal, received work items.
- **Teacher-side ergonomics**: three graded user modes (Easy/Intermediate/Advanced); classroom layout (rearrange student icons to reflect the physical room; save and reload); auto-reconnect; power on/off and log in/out of classroom computers; one-click "Request Assistance" to IT.
- **Technicians' Console**: IT-side console for remote control, screenshots, school-wide "always on" internet/application restrictions.
- **Optional sibling products**: classroom.cloud (cloud-based classroom management + safeguarding + IT management), NetSupport DNA (IT management + safeguarding), NetSupport Notify (mass alerting).

### ClassDojo (evidence layer A)

Positioning: "Where classrooms become communities… Free for teachers, forever." Community/behavior pole; no device monitoring at all.

- **Class setup**: teachers add/create classes; upload student rosters; school directory maintained by school leaders; shared classes with co-teachers; class ownership transfer; personal classes; archive/delete; end-of-year directory clean-up.
- **Points** (the core behavior mechanism): staff award **positive points** and (in display settings) points can be shown separately, combined, or hidden; custom skills (reasons) are creatable/editable per class; point values editable; zero-point skills exist; points can carry a note; points can be undone; points can be awarded to groups; point bubbles can be reset; reports with timestamps and notes (PDF export, spreadsheet view); points reports can be shown or hidden in parent reports. Points page frames this as positive feedback aligned with PBIS and SEL ("Set consistent expectations across all classrooms… then give specific, positive feedback").
- **Toolkit** (in-class tools displayed on projector/smartboard, castable from mobile): Group Maker (random groups, exclusion sets), Music, Noise Meter (synced to computer via DojoCast), Timer (add time in taps), Today (daily announcements/welcome/morning work), Random (random student selector), Directions (visual reminder of instructions, saveable), Think Pair-Share.
- **Communication/community**: Class Story (private class feed of photos/videos for families), Messages (teacher↔family, auto-translated into 190+ languages), Class Events calendar with reminders, Student Portfolios (students share work), Big Ideas video series (SEL topics).
- **School/district layer**: School Leaders and District features (schoolwide usage, directory, roles).
- **Student-facing**: student accounts, monster avatars, Dojo Islands (student social game space — separate product).
- **Not observed**: any device monitoring, screen control, web filtering, attendance register (Toolkit article lists no attendance tool; homepage marketing mentions "attendance sheets" among toolkit items but the help-center tool list does not include one — treated as unconfirmed).

### Satchel One (evidence layer A)

Positioning (help center): a learning platform whose staff audience is "Classroom staff, attendance officers, behaviour managers." UK whole-school platform (successor to Show My Homework), integrated with the school MIS.

- **My Classes**: per-class workspace with Gradebook, **Seating Plans**, Welfare Notes, Assessment, **Attendance - Class register**.
- **Attendance**: class register per lesson; Attendance Import; **Attendance Pro** (teacher-facing attendance taking); Daily tracker; attendance reports.
- **Behaviour**: staff award **positive points, negative points, and badges**; events stored centrally, visible on student profiles, group pages, and reports; loggable from multiple surfaces (Behaviour Overview, a group's Behaviour tab, a student's profile, the homework Assess page); reasons configurable per school; optional activity/location/comment fields; comments visibility to students/parents controlled per event and by school configuration (positive-only mode, staff-only mode); **Referred Incidents** (status workflow, visible to parents only when Resolved); **Sanctions**; **Detentions** (set detention directly from a negative event); **Thresholds** setup; behaviour insights reports/exports; points can sync with the MIS; totals reset per academic year; granular permissions gate each action (`My positive behaviour events`, `All negative behaviour events`, `Badges`, etc.).
- **Seating Plans**: desk-layout canvas per room (desk types, stamp/snap desks), room templates, drag-and-drop student placement with autofill, custom seats (reserved/labeled, students blocked from sitting), student cards showing up to eight data slots (inclusion groups, assessment data), whiteboard-safe full-screen mode (strips sensitive data before projecting), export image, staff-only visibility (students/parents cannot see seating plans), seating coverage reports.
- **Welfare Notes**: per-student welfare records accessible during lessons.
- **Other modules** (context, not classroom-management core): Homework (set/mark tasks — the Assignment Management side), Documents, Notice Board, Timetable, Reports.
- **Roles/permissions**: staff roles include classroom staff, attendance officers, behaviour managers; granular permission names gate actions; students and parents have separate views (web + mobile app).

## Cross-product Comparison

| Dimension | GoGuardian Teacher | LanSchool Air/Classic | NetSupport School | ClassDojo | Satchel One |
|---|---|---|---|---|---|
| Class container | Classroom; roster from Google Classroom/Clever/ClassLink or manual (code/email/CSV) | Class; roster from Google Classroom/Clever/ClassLink | Class formed via Class Wizard (Room/PC/User/Browse/SIS modes) | Class; manual roster upload, school directory | Class from MIS; My Classes |
| Live session model | Explicit session ("digital equivalent of a classroom period"); scheduled or manual; auto-join via extension | Connected students during lesson (implicit session) | Connection to students for the lesson (Class Wizard) | No explicit session; persistent class | No explicit session; per-lesson register |
| Screen/device observation | Thumbnails, active tab, timelines, screenshots, off-task alerts | Thumbnails/full-screen; web/app/keystroke history (Classic) | Thumbnails (dual monitors), app/website/keyboard monitoring, histories | None | None |
| Device control | Lock screen, open/close tab, focus tab, annotate, close app, exclude student | Blank screen, limit web, push website, launch app, mute audio, remote control, power on/off, app limiting, limit print | Blank/lock screens, quick launch, app/website controls, remote control, print/USB/webcam control | None | None |
| In-class web/app filtering | Scenes (allow/block, auto-open, tab limits), teacher override of district policy | Limit web, approved websites | Approved/restricted app/website lists, profiles | None | None |
| Communication | 1:1 chat, announcements, class audio/video, check-ins | Messaging (1:1/class), raise hand, group chat | Chat, messages, help request | Messages (teacher↔family), Class Story | Notice board |
| Behavior/conduct | None | None | Student rewards (stars/stickers) | Points (positive/negative, custom skills, notes, groups, reports) | Behaviour events (positive/negative points, badges, reasons, referred incidents, sanctions, detentions) |
| Attendance | None (exclude/include absent students) | Not observed | Student register (printable, custom prompts) | Not confirmed | Class register, Attendance Pro, daily tracker |
| Seating | Drag-drop tile reordering (not physical seating) | Not observed | Classroom layout (arrange icons to mirror physical room, save/reload) | None | Seating Plans (desk canvas, rooms, templates, data cards, whiteboard-safe mode) |
| In-class engagement tools | Check-ins, off-task alerts | Battery status | Surveys, Q&A module, testing, Student Journal, language lab, wellbeing check-in | Toolkit (timer, random, group maker, noise meter, directions, music, today, think-pair-share) | Welfare notes |
| History/reports | Session timelines, screenshots, command logs, chat logs, report emails | Report server (Classic), usage data | App/website histories, chat logs, Student Journal | Points reports (PDF/spreadsheet), parent reports | Behaviour insights, attendance/detention/seating reports |
| Roles | Teacher, student, IT admin (Org Management), super user | Teacher, student, IT (tech console) | Teacher, student, technician (Tech Console); graded user modes | Teacher, student, parent, school leader, district | Classroom staff, attendance officers, behaviour managers; granular permissions; student/parent views |
| Deployment | Cloud + browser extension/app | Cloud (Air) or on-prem (Classic) | On-prem heritage, multi-platform clients; classroom.cloud sibling | Cloud, freemium | Cloud, MIS-integrated |
| Family/parent layer | Separate Parent app (admin-controlled) | Not observed | Not observed | Core (Stories, Messages, portfolios) | Configurable event visibility, notifications |

### What is common (cross-product, layer B)

1. **A class roster of identified students** bound to a taught class — universal; roster sources vary (SIS/MIS sync, Google Classroom/Clever/ClassLink, manual entry).
2. **The teacher as operator** with a dedicated control surface; students are the managed subjects (they see the effects: locks, blocks, points, toolbar).
3. **In-the-moment operation during class time** — recording what is happening (register, behavior events, screen state) and directing it (commands, points, seating) — as distinct from authoring content or grading work over time.
4. **At least one in-class state domain filled in**: presence (register/attendance), conduct (points/rewards/sanctions), device/screen state (monitoring/control/filtering), physical arrangement (seating). No single domain is universal.
5. **Communication channel between teacher and students** (chat/messages/help requests) — present in 4 of 5 (all but Satchel One, which uses a notice board instead).
6. **Records of what happened** (session data, histories, reports) — universal in some form.
7. **Roster integration with school systems** — universal (Google Classroom/Clever/ClassLink/OneRoster/SIS/MIS).
8. **Role separation** between the classroom teacher and IT/administration — universal (Tech Console, Org Management, school leaders, MIS admins).

### What is NOT common (pole-dependent)

- Device/screen monitoring & control: GoGuardian, LanSchool, NetSupport — absent in ClassDojo, Satchel One.
- Behavior points: ClassDojo, Satchel One, (NetSupport rewards) — absent in GoGuardian, LanSchool.
- Attendance register: Satchel One, NetSupport — absent/unclear in GoGuardian, LanSchool, ClassDojo.
- Seating plans: Satchel One, NetSupport (layout) — absent in GoGuardian, ClassDojo.
- Family communication: core in ClassDojo, configurable in Satchel One — separate product in GoGuardian.

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as Classroom Management:

```text
Class roster (identified students bound to a taught class)
└── Teacher-facing control surface (teacher = operator; students = managed subjects)
    └── In-the-moment operation on the class as it meets:
        observe and record/direct students' in-class state
        (presence, conduct, device/screen state, physical arrangement)
```

Three properties:

1. **Class roster** — a defined set of identified students in a class the teacher teaches. Without it, there is no classroom to manage.
2. **Teacher-facing control surface** — the teacher operates; students are the managed subjects (not co-owners of a workspace, not an audience of a broadcast).
3. **In-the-moment operation on in-class state** — the unit of work is the class meeting/lesson; the teacher observes and acts on what is happening now (marking presence, recording conduct, watching/steering screens, arranging seats), not on work completed across time.

Deliberately NOT in L0 (tested against the sample): device monitoring (ClassDojo/Satchel lack it), behavior points (GoGuardian/LanSchool lack them), attendance (not universal), seating (not universal), cloud deployment (LanSchool Classic/NetSupport are on-prem), browser extensions, thumbnails, timers, parent apps, AI.

### L1 — Common Mature Structure

Present in most mature products, not required to define the Type:

- roster integration with school systems (SIS/MIS/Google Classroom/Clever/ClassLink/OneRoster)
- a session/connection model that binds the teacher's surface to the students' devices for the duration of the lesson (explicit sessions in GoGuardian; connection models in NetSupport/LanSchool)
- screen monitoring (thumbnails, live view, screenshots, activity timelines)
- device-control commands (lock/blank screen, open/push URL, close tab/app, restrict web/apps)
- in-class web/app filtering with teacher-level override
- teacher↔student messaging (chat, help requests, raise hand)
- behavior/conduct recording (points, rewards, custom reasons/skills, notes, reports)
- attendance/register
- seating charts (physical layout, drag-drop placement, student data cards)
- in-class engagement tools (timer, random selector, group maker, noise meter, check-ins, surveys)
- session/class history and reports (timelines, command logs, behavior reports)
- role separation: teacher vs IT/admin (Tech Console / Org Management / school leaders), co-teachers, granular permissions

### L2 — Variant / Optional Structure

- deployment posture: cloud SaaS vs on-prem server vs browser extension vs native agent
- device-platform scope: ChromeOS / Windows / macOS / iOS / mixed / BYOD
- conduct philosophy: positive-only framing vs positive+negative; PBIS/SEL alignment; gamification (avatars, badges)
- school-wide discipline extension: sanctions, detentions, referred incidents, thresholds (Satchel One) — the bridge toward Student Behavior Management
- family/parent layer: core community surface (ClassDojo) vs configurable visibility (Satchel One) vs separate admin-controlled app (GoGuardian Parent)
- embedded assessment: tests, surveys, Q&A games (NetSupport, LanSchool Classic)
- IT-management extensions: report servers, keyword alerts, enterprise usage data, print/USB/webcam controls
- wellbeing check-ins; language lab/audio; AI on-task monitoring (emerging)
- business model: freemium teacher-first vs district license vs hardware bundle (LanSchool/Lenovo)
- regional framing: US (PBIS, scenes, filtering) vs UK (behaviour/detentions/MIS register)
- audience extension: corporate training and higher-ed use (NetSupport)

### L3 — Vendor-specific (research notes only)

- GoGuardian: Scenes mechanics, Focus Tabs, default 45-minute session length, lock carry-over across teachers' sessions, Annotate ~10-second circle, session report emails, Org Management RBAC/OU model, Teacher Override configuration.
- LanSchool: Classic keystroke history, keyword alert to central server, 100-question auto-graded tests, voting CSV export, tech console, report server, enterprise data collection, Lenovo hardware bundle, On-Task Monitoring beta.
- NetSupport: Q&A module modes (first-to-answer with bounce, enter-an-answer, pot luck, peer assessment, basketball questioning), Student Journal, graded user modes (Easy/Intermediate/Advanced), language lab, room-layout save/reload, password reset by teacher, classroom.cloud/DNA/Notify sibling products.
- ClassDojo: monster avatars, point bubbles, zero-point skills, DojoCast, Dojo Islands, Big Ideas series, 190+ language translation, school directory clean-up, positive-only display configurations.
- Satchel One: On Call, Referred Incidents status workflow, Thresholds, Welfare Notes, whiteboard-safe seating mode, MIS sync of behavior points, academic-year point reset, permission names (`My positive behaviour events` etc.).

## Historical / Market-Sample Check

- **Lab-era products fit**: LanSchool (30 years) and NetSupport School predate cloud and 1:1 programs; their classic form is a teacher console controlling networked lab computers — roster (lab machines/users), live lesson connection, in-the-moment control. No cloud, no behavior points, no parent apps. The L0 holds.
- **Behavior-only products fit**: ClassDojo has no device control at all, yet is squarely marketed as classroom management. The L0 holds because the frame (teacher + roster + in-the-moment state operation) does not require any particular state domain.
- **Paper-era analog**: the frame is the digitization of the teacher's traditional in-class tools — the register, the seating chart, the conduct marks — plus a device-control layer that only exists once classrooms have screens. Nothing in the L0 depends on cloud, phones, extensions, or AI.
- **Conclusion**: the definition is era- and region-neutral. The three state domains (presence, conduct, devices) are capability families that fill the frame, not the frame itself.

## Vendor-specific Findings

See L3 above. Notable for boundary work: GoGuardian's split (Teacher = classroom; Admin = district filtering; Parent = admin-controlled sharing) demonstrates the teacher-vs-IT-vs-family role separation inside one vendor's suite. NetSupport's sibling products (classroom.cloud, DNA, Notify) show the same pattern. Satchel One shows a whole-school platform containing classroom-management modules alongside homework (assignment) modules — direct evidence for the Assignment Management boundary.

## Boundary Findings

1. **vs Assignment Management (processed leaf)** — sharpest recorded seam, confirmed from this side: assignment management governs work completed across time (set → submit → grade → return); classroom management governs the live class (presence, conduct, devices, seating in the moment). Satchel One contains both as separate modules (Homework vs Behaviour/Seating/Attendance), and its own help center treats them as different apps — direct evidence that the seam is real inside one product.
2. **vs Virtual Classroom (unprocessed sibling)** — a virtual classroom delivers the lesson itself online (video/whiteboard/lesson surface) for remote teaching; classroom management controls and observes an in-room or device-equipped class. Overlap risk: LanSchool/GoGuardian support remote learners, and NetSupport supports corporate training — but the surface is still control/monitoring, not lesson delivery. Flag for joint review when virtual-classroom is processed.
3. **vs Student Behavior Management (unprocessed sibling)** — in-class conduct recording (points/rewards) vs school-wide discipline machinery (referrals, sanctions, detentions, PBIS program management). Satchel One's Behaviour module contains the school-wide machinery (sanctions, detentions, referred incidents, thresholds) inside a platform that also has classroom-management modules — the boundary is a gradient, not a hard product split. Flag for joint review.
4. **vs Student Attendance System (unprocessed sibling)** — attendance appears here as an in-class register (Satchel class register/Attendance Pro, NetSupport student register); dedicated attendance systems are school-wide records systems. Flag for joint review.
5. **vs UEM/Endpoint Management** — classroom management is teacher-facing live control of students' devices during class; UEM is IT-admin policy management of device fleets. Vendors themselves split the two (GoGuardian Teacher vs Admin/Fleet; NetSupport Teacher vs Tech Console/DNA; LanSchool report server). The defining user of classroom management is the teacher.
6. **vs Learning Management System** — an LMS hosts courses/content/work over time; classroom management does not host content (GoGuardian merely links out to Google Classroom coursework; NetSupport transfers files). Roster overlap is high but the object worlds differ.
7. **vs Audience Response System (processed)** — an ARS is a live session where participants respond to items and see aggregates; classroom management's device pole shares "live session + student devices," but its defining action is teacher-side observation/control of student state, not item-based response collection. NetSupport's survey/Q&A module is an embedded ARS-like capability inside a classroom-management product — evidence that ARS is a capability, not this Type.
8. **Name collision with childcare software** — "classroom management" in childcare-management systems means rooms/capacity/ratios (see processed leaf childcare-management-system, which explicitly excludes classroom management from its in-home tier). Same words, different Type; no action needed beyond awareness.
9. **Taxonomy note** — the leaf name matches the market's own category label ("classroom management software" is how LanSchool, NetSupport, and GoGuardian describe themselves), so the leaf is a genuine market cluster, not an alias.

## Uncertainties

- LanSchool operational detail (exact command set, session model, attendance/seating presence) is unverified — Air KB unreachable; only product-page claims (Tier-2) available. No precise LanSchool claims made in the final document.
- ClassDojo Toolkit attendance: homepage marketing mentions "attendance sheets" among toolkit items, but the help-center tool list does not include one. Treated as unconfirmed; not asserted.
- Whether ClassDojo supports negative points by default or only via display settings: the help center shows display settings (separate/combine/hide totals) and a "Positive points guide," but the exact default posture was not verified. The final document says products commonly support positive and negative recording with configurable visibility, without claiming ClassDojo defaults.
- Market share/adoption numbers (GoGuardian "2M+ teachers", ClassDojo "45M+ students") are vendor marketing claims; recorded as claims, not facts.
- The exact relationship between Satchel One's Attendance Pro and the MIS register (which is authoritative) was not fully explored; no claims made.

## Final Synthesis

Classroom Management is best understood as **the teacher's live-classroom control surface**: a class roster of identified students, operated by the teacher through a dedicated surface, used to observe and act on students' in-class state — presence (register), conduct (points/rewards/sanctions), device and screen state (monitoring, control, filtering), and physical arrangement (seating) — during the lesson, with records kept of what happened. The market resolves into recognizable poles that fill the same frame differently: a device-monitoring pole (GoGuardian Teacher, LanSchool, NetSupport School), a behavior/community pole (ClassDojo), and whole-school platforms that carry classroom-management modules alongside homework and school-wide discipline (Satchel One). No single capability family is definitional; the frame is. The Type is bounded against assignment management (work over time), virtual classrooms (lesson delivery), student behavior management (school-wide discipline), attendance systems (records), UEM (IT policy), and LMSs (content/courses) — with joint-review flags recorded for the three unprocessed siblings.
