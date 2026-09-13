# Research Notes — Student Attendance System

## Research Goal

Understand what a **Student Attendance System** is as an Application Type: what objects exist inside it (attendance records, codes, sessions, absence records), who operates it, how attendance is captured and reconciled, what the absence-resolution loop looks like, what reporting/compliance machinery exists, and where its boundary sits against the dense sibling cluster (School Management System / SIS, Classroom Management, Time & Attendance, Parent Portal, attendance-intervention products).

## Initial Boundary

- Core hypothesis: the school's attendance operation as a system of record — capture who is present for the school day and its sessions, hold per-student presence states as a persistent record, resolve absences with guardians, report outward (statutory/funding/internal), and surface patterns for follow-up.
- Nearest neighbors: School Management System / SIS (attendance as a module leg of the whole-school loop), Classroom Management (in-class register as a live-classroom capability), Time & Attendance System (employees, not students), Parent Portal (surfaces the record), attendance-intervention products (consume the record downstream).
- Two prior flags to discharge:
  1. classroom-management pass: "the in-class register (Satchel class register/Attendance Pro, NetSupport printable student register) is a classroom-management capability, while school-wide attendance records, statutory reporting, and absence management belong to the sibling Type; recommend joint review when student-attendance-system is processed."
  2. school-management-system pass: daily attendance is one leg of its operational loop; the pass explicitly anticipated that "slice Types center their own loop … the school management system centers the school. Boundary holds; the slices' passes should confirm."
- Unknowns going in: whether the intervention layer (predictive analytics, automated letters) is inside the Type or adjacent; whether capture is definitional or whether record-consumption products count; how daily vs per-period granularity distributes; how the SIS-embedded module pole relates to standalone products.

## Research Questions

1. What is the unit of record — per student per day? per session/period? What states does it hold?
2. How is attendance captured (teacher roll call, office/kiosk check-in, parent-submitted absence, automated check-in)?
3. What happens after capture — missing marks, unexplained absences, approval workflows, guardian notification?
4. What codes/marks governance exists (excused/unexcused, subcodes, reason codes)?
5. What reporting exists — statutory/funding (ADA, census, clock-hour/Title IV), internal dashboards, per-student history?
6. How does the system relate to the SIS (roster in, attendance write-back)?
7. Which roles operate it (teacher, attendance officer/clerk, admin, guardian, student)?
8. What rules matter (permissions, edit/overwrite semantics, roster dependency, timetable binding)?

## Representative Products

| Product | Pole | Segment / geography | Why selected |
|---|---|---|---|
| SchoolPass | campus-operations attendance (parents + office + teachers) | US K-12 private/independent + some public | dedicated attendance product bundled with dismissal/visitor ops; SIS write-back posture |
| Orah | real-time student-location attendance (roll checks, kiosk, boarding) | Independent day + boarding schools, NZ-origin/US | attendance as live source of truth; deepest help-center documentation of the standalone pole |
| Portico Attendance & Skills (formerly CourseKey) | compliance attendance (clock-hour/Title IV) | US postsecondary career schools (nursing, allied health, beauty/wellness, trade) | student self-check-in compliance pole; different customer tier entirely |
| SchoolStatus Attend | attendance-intervention pole (boundary sample) | US public districts | consumes SIS attendance data; intervention loop (letters, texts, conferences, early warning) — tests whether capture is definitional |
| Bromcom Attendance module | SIS/MIS-embedded module pole | UK state schools | the record-of-record realized inside a whole-school MIS; richest Tier-1 docs |

Sample spans: 4 standalone + 1 module pole; private K-12, independent/boarding, postsecondary career, public district, UK state; operations, real-time, compliance, intervention, and record-of-record philosophies.

## Sources

- SchoolPass — https://schoolpass.com/ (homepage; attendance-automation solution page returned 503 twice — abandoned per network rule; support portal is a Salesforce site, not fetched)
- Orah — https://www.orah.com/ (homepage), https://success.orah.com/en/articles/8855627-taking-class-attendance-with-orah (help guide), https://success.orah.com/en/articles/8855597-class-attendance-roll-type (help guide)
- Portico (CourseKey) — https://porticoedu.com/ (homepage), https://porticoedu.com/attendance-skills/ (product page)
- SchoolStatus — https://schoolstatus.com/ (homepage), https://www.schoolstatus.com/products/attend (product page + FAQ)
- Bromcom — https://docs.bromcom.com/knowledge-base/attendance-module-guidance/ (module index), https://docs.bromcom.com/knowledge-base/how-to-take-a-register/, https://docs.bromcom.com/knowledge-base/how-to-manage-absence-notifications-from-mcas/, https://docs.bromcom.com/knowledge-base/how-to-use-manage-attendance/
- Arbor (UK MIS, alternate module pole) — help.arbor-education.com unreachable (transport error ×2) — abandoned; Bromcom substitutes.

Research date: 2026-09-09.

## Product Observations

### SchoolPass (evidence: Tier 2 — homepage only; attendance page unreachable)

- Positioning: "complete K-12 campus operations & safety solution. Consolidate student safety, physical attendance, dismissal, and parent engagement into one connected & patented platform."
- Attendance Automation: "Connect parents, teachers, and the front office with automated day-level or per-period attendance."
- Parent Schedule Management: parents "update attendance, arrival, and dismissal changes from the SchoolPass App"; "85% less admin hours" claim (marketing figure — not carried into final doc).
- Emergency Attendance: "take real-time attendance during an emergency."
- After-school activity check-in/out with signature capture and attendance notifications to parents.
- SIS integration (Blackbaud, PowerSchool, Veracross, Senior Systems, FACTS): "We get parent, student, & attendance data when it changes in your SIS"; "We can send attendance data to your SIS when it's reported in SchoolPass by parents and the front office"; SSO from the SIS; ID-based syncing.
- **Not observed** (source limitation): attendance workflow detail, code configuration, reconciliation surfaces. No precise SchoolPass workflow claims made anywhere.

### Orah (evidence: Tier 1 help guides + Tier 2 homepage)

- Positioning: "School Safety Platform"; "Know where your students are"; "Orah uses routine school processes to keep a student's location updated. Attendance, dismissals, hall passes, check ins and emergency response turn Orah into your source of truth for where students are."
- Attendance product surface: "Period by Period Attendance — Update student location via manual or automated roll calls"; "Real-time attendance that writes back to your SIS"; "Two-way, period-by-period sync with Blackbaud, Veracross, FACTS"; "Live headcount feeds emergency mustering."
- Capture surfaces (help guide): web app (Homeboard > My Schedule > Start Roll Check), Roll Checks browser extension (side panel, "teachers don't have to switch apps"), iOS app; homepage also names RFID readers and QR codes as automation.
- Roll mechanics (help guides):
  - Class Attendance roll types "designed for taking attendance based on the school timetable" (classes, athletic groups, advisory meetings); "can only be used from the My Schedule page"; My Schedule "displays the staff member's timetable based on an integration with the SIS."
  - "Any new class created on SIS will take 24 hrs to reflect on Orah" — roster/timetable substrate is the SIS.
  - Roll codes can be locked "so only staff with access to roll settings can use them."
  - "An active pass must be ended before marking a student as present"; a student with a pass during class is recorded as 'On Pass - Excused'; schools configure whether staff may end passes during a roll check.
  - Changing a roll code requires the **edit roll record** permission (error otherwise).
  - Scheduled passes visible to the teacher during roll call ("returning at 12:00" context).
- Absences (homepage): "Parents submit absences via portal… Absence requests come in through the family app, route to the right approver, and apply to both the daily roll and the specific class periods the timeframe overlaps. If a parent logs a 10:30 to 12:00 dentist appointment, the student is excused from those periods only."
- Records: past attendance records viewable/editable/deletable from My Schedule; if a new student was added to the SIS after a roll call completed, they "won't show up on the roll call" until the roll is deleted and retaken.
- Downstream: Attendance Insights ("works out of the box with Blackbaud, Veracross & FACTS"); Attendance Alerts ("Flag repeated absences or tardies so you can step in early when patterns occur"); late arrivals/early dismissals logged by front office, "teachers see the change on their roster instantly. Parents get the confirmation."
- Adjacent modules sharing the same record: dismissals, passes, boarding check-in (curfew counts), emergency mustering, visitor management.

### Portico Attendance & Skills / CourseKey (evidence: Tier 2 product pages)

- Positioning: "Operational software for career education"; Portico = suite combining Campus Ivy, CourseKey, Verity IQ, Trajecsys. Attendance & Skills "(formerly CourseKey)".
- "Attendance & Skills gives learners a convenient place to manage attendance, chart progress, and stay on track… real-time access to attendance, assignments, schedules, and skills progress."
- Capture: "Ditch the rosters and manual data entry. Learners check in and out using secure methods like biometrics, QR codes, sound, or our patented GPS technology." — student self-check-in is the primary capture act.
- Compliance context: "From managing multiple campuses to accommodating clock and credit-hour programs…"; case study: "See how Unitek College fixed attendance issues and protected Title IV funding"; student quote: "Students valued the real-time visibility into their attendance records and began running to class to receive full credit for attendance."
- Nudges: "Set automated triggers for personalized reminders about attendance, overdue forms, or upcoming deadlines."
- Skills tracking alongside attendance (NCLEX domains, welding certifications, state board cosmetology hours) — separate capability bundled in the same product.
- Formats: "in-person, asynchronous, or hybrid instruction."
- Integrations: SIS (Verity, Orbund, Campus Cafe, Anthology, FAME, Banner), LMS (Canvas, D2L, Moodle, Blackboard), plus Portico SIS/CRM/financial aid.
- **Not observed**: exact clock-hour threshold logic, make-up work flows, state-reporting formats.

### SchoolStatus Attend (evidence: Tier 2 product page + FAQ) — boundary pole

- Positioning: "Attend — Attendance Interventions"; "Curb Chronic Absenteeism Before It Begins"; company tagline "Mission: Attendance".
- **Does not capture attendance**: "We integrate with multiple SIS providers to bring in student records and determine when students are eligible for an intervention." Attendance is "marked" upstream (SIS); Attend consumes it.
- Record views: "Track Attendance by Time, Period, or the Day"; "See How Attendance Codes Are Used Across the District"; block schedules supported; time-based attendance for state mandates ("districts in states like Ohio and Oregon can meet state mandates"; configurable thresholds, e.g. interventions at 10 and 30 missed hours — vendor-stated example).
- Intervention loop: automated interventions when absences accumulate ("first intervention… sent via physical mail and digitally. Subsequent… digitally"); Daily Attendance Notifications ("automated text when their child is marked absent and invites them to share the reason. Those responses are collected in a centralized dashboard"); Attendance Conferences ("identifies the right families and simplifies scheduling and documentation"); celebratory/positive messages; two-way messaging in 130+ languages.
- Analytics: Early Warning Insights ("predictive analytics to show who's likely to become chronically absent after just 60 days"); MTSS framework data; district/school heatmaps; intervention effectiveness ("54% of students return after one letter" — vendor claim, not carried).
- Funding framing: "In ADA states, higher attendance also means more state funding" + attendance impact calculator.
- Structural reading: the intervention layer operates **downstream of the attendance record**; the record of record remains in the SIS. This pole tests the capture leg of the definition.

### Bromcom Attendance module (evidence: Tier 1 documentation) — module pole

- Bromcom is a UK school MIS; Attendance is one module among ~25 (Students, Staff, Behaviour, Census, Curriculum, Finance, Timetable…). The module index itself maps the attendance operation:
  - **Setup**: create/manage Attendance Codes/Marks; subcodes; Registration Options; Register Update Parameters.
  - **Routines — Registers**: Take a Register; Secondary Register; Register Views; Today's Missing Registers.
  - **Routines — Manage Attendance**: overwrite/enter marks; Absence Notifications from MCAS (parent portal); Virtual Textback (parents text, school marks attendance from received messages); Bulk Attendance Update; Missing Marks; Amend Reason for Change; Merge Attendance; Student Attendance Status.
  - **Communication**: Watchlist; Absence Alert.
  - **Reporting**: Attendance Reports (Absentee List, Attendance Certificate); Analysis Exports; Fire Drill Report; School Summary; RAG-status reports.
  - **Analysis**: Attendance Dashboard; benchmark data; analysis tools.
  - **Student Record**: Attendance Highlights; Student Details Attendance Page.
- Taking a register (teacher): assigned to a Teaching Class/Tutor Group with the Teacher Role → Lesson Dashboard → select group + period → Take Register → fill attendance marks → Save. Can take a register for another staff member (cover). Primary schools: AM/PM sessions only; the AM register's present mark auto-populates the student's meal type from their meal pattern, and a cancelled-meaning code (e.g. COVID codes) flips the meal to Absent — attendance drives downstream operations.
- Manage Attendance (attendance officer): filter by year group/whole school/tutor/report group; date range (specific date, week, exam register); overwrite marks per cell, per period column (AM, Period 1, 2…), per day, or per student row; bulk flood-fill codes; missing marks display as the precreation '?' mark; entering marks via Manage Attendance does not clear Today's Missing Registers until Update Headers pulls them across; attendance comments attach to marks (red-triangle indicator; overwriting a mark loses its comment); exam registers (populated when exam basedata + entries + seating exist); visual indicators for Nature of Activity (blue), Comment (red), Sub-code (green); "Add minutes late" supported; everything permission-gated (Attendance Module in Roles & Permissions).
- Absence Notifications from MCAS (parent portal):
  - School-side config enables parents to report future absence (off by default); optional confirmation email.
  - Parent submits: student(s), Date From/To (today or future), optional partial-day Time From/To, reason message, attachments (up to 20MB each).
  - School sees a queue: Received Date, Student, Tutor/Year Group, Contact, dates/times, Reason, **Status (Awaiting Review → Approved/Rejected)**, Attendance Mark Comment, student's YTD attendance %, attachments.
  - Approve → assign an authorised Attendance Absent Code/Subcode (+ optional comment) → code lands in Manage Attendance; parent notified in MCAS Inbox. Reject → parent notified; Resubmit creates a copy in Awaiting Review.
  - Duplicate guard: alert if a notification is already in progress/approved for that student/period.
  - Notification bell for staff with the Absence Notifications permission.

## Cross-product Comparison

| Structure | SchoolPass | Orah | Portico/CourseKey | SchoolStatus Attend | Bromcom module | Strength |
|---|---|---|---|---|---|---|
| Persistent per-student attendance record (day + session/period) | Y (day-level or per-period) | Y (daily + period roll checks; records page) | Y (real-time attendance record) | Y (consumed: time/period/day views) | Y (AM/PM + period marks grid) | **A/B — universal** |
| Capture against the school's schedule | Y (parents + front office + teachers) | Y (roll checks on SIS timetable; kiosk/RFID/QR) | Y (student self-check-in/out) | **N — consumes SIS capture** | Y (teacher registers; officer backfill) | **A/B — universal in capture-bearing poles** |
| Configurable code/marks set (present/absent/tardy/late; excused/unexcused; reasons) | implied | Y (roll codes, lockable) | implied (attendance credit) | Y ("how attendance codes are used") | Y (codes/marks/subcodes setup) | B — common |
| Absence resolution with guardians (submit/approve/notify) | Y (parent-submitted attendance changes; notifications) | Y (absence requests routed/approved; period-scoped) | partial (nudges; real-time visibility) | Y (daily notifications invite reason; conferences) | Y (MCAS absence notifications w/ approval workflow; textback) | B — common |
| Reconciliation surface (missing marks, bulk edit, comments) | not observed | Y (edit/delete records; permission-gated) | not observed | n/a | Y (Manage Attendance, '?', Update Headers) | B — common where evidenced |
| Reporting outward (statutory/funding or internal) | Y (SIS write-back) | Y (SIS write-back; insights) | Y (Title IV/clock-hour compliance) | Y (state mandates; ADA funding) | Y (reports, census module, certificates) | B — universal |
| Pattern alerts / follow-up | not observed | Y (attendance alerts on repeated absences/tardies) | Y (nudges) | Y (early warning, interventions, MTSS) | Y (watchlist, absence alert) | B — common |
| Roster substrate = enrollment/SIS | Y (SIS sync) | Y (SIS timetable; 24h class sync) | Y (SIS integrations) | Y (SIS integration) | Y (native MIS population) | **A/B — universal** |
| Real-time headcount / live roster | Y (emergency attendance) | Y (live headcount → mustering) | partial | n/a | Y (fire drill report) | B — common |
| Intervention machinery (predictive, letters, conferences) | not observed | partial (alerts) | partial (nudges) | **Y (the whole product)** | partial (watchlist) | B — pole-dependent |

Reading: every capture-bearing product realizes the same three-part operation — capture presence against the school's schedule, hold it as a persistent coded record per student per day/session, and work the record (resolve absences, report outward, flag patterns). The intervention pole (SchoolStatus) realizes only the third part over an upstream record — it is the boundary that proves capture+record is the Type's center of gravity.

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The student attendance record of record** — persistent identified records of each enrolled student's presence state (present / absent / late-tardy, with excused-unexcused / reason-code depth where the segment requires it), organized against the school's day and commonly its session/period structure, held for the school's enrolled population. *(Remove → a notification tool or a live headcount display with no memory.)*
2. **Attendance capture against the school's schedule** — the operational act that produces the record: teacher roll call on a class/tutor group, office/kiosk check-in, parent-submitted absence, or automated student check-in — bound to the school's timetable/day structure and to the enrolled roster. *(Remove → a reporting/analytics layer over data captured elsewhere = the intervention pole; or an in-class register with no school-wide record = classroom-management capability.)*
3. **The absence accountability loop** — the record is worked: unexplained absences are reconciled with guardians (notification, reason/excuse, approval), attendance is reported outward (statutory/funding reports or internal dashboards), and patterns are surfaced for follow-up. *(Remove → a bare register nobody reconciles or reports from.)*

Jointly-held load-bearing: 1 alone = a mark grid/spreadsheet; 2 without 1 = ephemeral roll call; 3 without 1+2 = intervention analytics over someone else's data; 1+2 without 3 = a register archive with no accountability loop.

### L1 — Common Mature Structure

- Configurable attendance code/marks set (present/absent/tardy/late; excused/unexcused; subcodes/reasons; lockable codes)
- Daily AND per-period/session granularity (AM/PM vs period-by-period; block schedules)
- Guardian-facing absence submission + confirmation/notification (parent app/portal)
- Late-arrival / early-departure logging visible to teachers and office
- Attendance-officer reconciliation surface (missing marks, bulk update, comments, exam registers)
- SIS integration: roster/timetable in; attendance write-back (in standalone poles the SIS remains the record of record)
- Attendance dashboards/reports (per-student %, school summary, absentee lists, certificates)
- Pattern alerts/watchlists (repeated absences/tardies)
- Real-time headcount/live roster (safety and emergency use)

### L2 — Variant / Optional Structure

- Capture substrate: teacher roll call (web/mobile/extension), office/kiosk check-in, parent app, QR/RFID/biometric/sound-prompt/GPS-geofence student self-check-in, SMS textback
- Segment machinery: statutory/funding reporting (US ADA states, state time mandates; UK DfE census returns), clock-hour/Title IV compliance (career colleges), accreditation clinical-hours tracking
- Intervention layer: predictive early-warning, automated letters/postcards, attendance conferences, MTSS framing (the SchoolStatus pole — adjacent when capture is absent)
- Boarding/curfew rolls, event/activity attendance, emergency mustering
- Hall passes / student-location as an extension of the attendance record
- Register-driven downstream operations (meal selection from the AM register — UK primary)
- Biometric/RFID hardware estates

### L3 — Vendor-specific (research notes only)

- Orah: Roll Checks Chrome extension; 'On Pass - Excused' state; 24h SIS class-sync lag; edit-roll-record permission; "83 routine processes" marketing frame.
- Bromcom: '?' precreation mark; Update Headers semantics; meal-pattern auto-population; Nature of Activity indicators; MCAS absence-notification workflow specifics; exam registers from Basedata/entries/seating; dinner module coupling.
- SchoolPass: carline/dismissal/license-plate/RFID vehicle screening bundle; "85% less admin hours" claim.
- SchoolStatus: 60-day early-warning window; ADA impact calculator; Smore newsletter integration; mail-then-digital intervention cadence.
- Portico: patented GPS check-in; sound-based check-in; skills tracker (NCLEX domains, cosmetology hours).

## Rejected Findings (anti-overfit)

- **"Attendance = twice-daily AM/PM statutory registers"** — REJECTED as definitional: UK MIS pole uses AM/PM sessions, US poles use day-level or period-by-period; the invariant is record-against-the-school's-day-structure, with granularity a variant axis.
- **"Parent app absence submission is definitional"** — REJECTED: Bromcom ships it switched off by default; CourseKey's capture is student self-check-in; teacher roll call remains the dominant substrate. Guardian channel is common, not defining.
- **"SIS write-back is definitional"** — REJECTED as invariant: in the module pole the record is native to the MIS; write-back is the standalone pole's integration posture. The invariant is that the attendance record joins the school's student-record system, wherever that lives.
- **"Predictive intervention is definitional"** — REJECTED: only the SchoolStatus pole centers it; elsewhere it is alerts/nudges at most. Held as variant/adjacent.
- **"Biometric/RFID capture is definitional"** — REJECTED: regional/segment implementation detail (SchoolStatus-era US K-12, career schools); roll call and paper registers satisfy the core without them.
- **"Real-time student location is definitional"** — REJECTED: Orah's framing (location as source of truth) is a product philosophy; the record, not live location, is the Type's center. Emergency mustering is a consumer of the record.

## Historical / Market-Sample Check

- **Paper era**: teacher's roll book/class register marked at the start of the day (and again after lunch); office clerk compiles the daily absence list from the registers; guardian notes/phone calls excuse absences; attendance clerk maintains the cumulative register; statutory school-board returns; truant-officer follow-up. All three L0 structures satisfied with no digital machinery. **Passes.**
- **Regional**: UK statutory AM/PM session registers with DfE code sets and census returns; US ADA-funding states and time-mandate states; clock-hour career schools; boarding-house curfew rolls. All satisfy the core with different granularity/code machinery. **Passes.**
- **Platform-native**: SIS-embedded attendance module (Bromcom) satisfies — the Type does not require standalone packaging. **Passes.**
- The definition is not fitted to the modern mobile/kiosk implementation.

## Boundary Findings

1. **vs School Management System / SIS (processed sibling)** — attendance is one leg of the school's operational loop there; here the attendance operation is the center. The module pole (Bromcom) realizes the identical loop inside the MIS; standalone products realize it beside the SIS with roster-in/record-back integration. Keep both; seam = center of gravity (whole school vs attendance operation). Confirms the school-management pass's anticipation from this side.
2. **vs Classroom Management (processed sibling — JOINT REVIEW FLAG DISCHARGED)** — the in-class register (Satchel class register/Attendance Pro, NetSupport printable register) is the teacher's in-the-moment lesson register: a classroom capability without school-wide record semantics. Once marks become a school-wide, code-governed, reconciled record with absence resolution and outward reporting, the operation is this Type. Keep both; the seam is record-of-record + accountability loop vs in-the-moment register. Satchel's Attendance Pro sits on the seam (teacher-facing taking tool; the school-wide record lives in the MIS).
3. **vs attendance-intervention products (SchoolStatus pole)** — products that consume an upstream attendance record and center the intervention loop (predictive early warning, automated letters, conferences) operate downstream of the record of record. Recorded as an adjacent specialization of the attendance operation, not the Type's center: without capture+record the product depends entirely on the SIS/module that holds the record. Boundary pole in-sample; final document describes the intervention layer as adjacent machinery.
4. **vs Time & Attendance System (processed sibling)** — different subject population (students vs employees), different accountability (safety/funding/truancy/academic presence vs pay/compliance), different schedule substrate (school day/timetable vs shifts). Structural overlap in shape (capture → coded record → reconciliation → reporting) but non-overlapping worlds.
5. **vs Parent Portal** — the portal surfaces the record to families; the attendance system produces and works the record. Guardian absence submission is a channel into this Type, not the portal's center.
6. **vs School Transportation Management / dismissal tools** — dismissal/carline is departure logistics (SchoolPass bundles both); attendance is presence at school/sessions. Bundling in one vendor does not merge the Types.
7. **vs Emergency Management** — emergency mustering consumes the live headcount the attendance record provides (Orah, SchoolPass emergency attendance); the emergency response loop is a different Type.
8. **"去掉什么就变成另一个 Type" 判据**: remove the school context (enrolled students, school day/timetable) → generic time & attendance; remove the persistent record → in-class register (classroom-management capability); remove capture → attendance analytics/intervention layer; remove the accountability loop → a bare register archive; add whole-school population/structure/fees/admissions → school management system.

## Uncertainties

- SchoolPass attendance-automation page unreachable (503 ×2): attendance detail rests on homepage Tier-2 claims (day-level or per-period; parents/teachers/front office; SIS write-back). No precise SchoolPass workflow claims made.
- Arbor unreachable (transport error ×2): UK module pole covered by Bromcom alone; other UK MIS (SIMS) and US SIS modules (PowerSchool, Infinite Campus) not directly fetched — module-pole claims generalized from one deep sample.
- Exact statutory code sets (DfE national codes, state ADA/time-mandate rules) not enumerated from primary sources; held generic in the final document.
- Portico clock-hour threshold logic and state-reporting formats not observed.
- SchoolStatus's "54% return after one letter" and Orah's "83 routine processes" are vendor claims — not carried into the final document.

## Final Synthesis

A Student Attendance System is the school's attendance operation as a system of record. Its defining core is three jointly-held structures: the student attendance record of record (persistent coded presence states per student per day and commonly per session/period, held for the enrolled population); attendance capture against the school's schedule (teacher roll call, office/kiosk check-in, parent-submitted absence, or automated student check-in, bound to the timetable/day structure and the roster); and the absence accountability loop (unexplained absences reconciled with guardians, attendance reported outward for statutory/funding/internal purposes, patterns surfaced for follow-up). Around that core, mature products add configurable code sets, guardian channels, reconciliation surfaces for attendance officers, SIS integration (roster in, record back), dashboards and reports, pattern alerts, and live headcount. The market realizes the core across recognizable poles — campus-operations attendance (SchoolPass), real-time location attendance (Orah), compliance attendance for career schools (Portico/CourseKey), the SIS-embedded module (Bromcom) — with the intervention layer (SchoolStatus) operating downstream of the record as an adjacent specialization. The Type is bounded against the school management system (whole school vs attendance operation), classroom management (in-class register vs school-wide record), time & attendance (students vs employees), and parent portals (surface vs source).
