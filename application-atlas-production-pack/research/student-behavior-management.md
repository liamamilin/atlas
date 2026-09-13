# Research Notes — Student Behavior Management

## Research Goal

Understand what "Student Behavior Management" software actually is as an Application Type — from real products, not from the term's marketing usage — and produce a vendor-neutral Application Document. The term is used loosely across the education market (behavior-point apps, discipline/referral systems, PBIS program platforms, SIS behavior modules), so a central goal is to find the smallest structure that makes the Type recognizable and to mark the boundaries against neighboring Types — especially Classroom Management (a joint-review flag is pending from that pass) and the SIS.

## Initial Boundary

- Core use hypothesis: the school's system for recording student conduct events (positive and negative), applying the school's behavior framework (points, consequences, sanctions), and using the accumulated data for decisions — school-wide, not per-classroom.
- Nearest neighbors: Classroom Management (joint-review flag pending), Student Information System / SIS (behavior/discipline modules), Student Case Management (unprocessed), School Counseling Management (unprocessed), Special Education Management (processed — its notes name "student-behavior-management (incident loop)" as a boundary), Student Attendance System (processed — no behavior overlap found there), Parent Portal (capability, not Type).
- Unknowns: whether points/rewards are definitional (SWIS suggests not); whether the administrative referral loop is definitional (PBIS Rewards sells it as an add-on — suggests not); where the classroom-management seam exactly runs; whether SIS behavior modules make this leaf a capability rather than a Type.

## Research Questions

1. What is the core object world (behavior event, student, reason/behavior taxonomy, points, referral, consequence/sanction, detention, report)?
2. What does the school configure before the system works (behaviors/reasons, point values, consequences, thresholds, sanction rules)?
3. How does an event flow: who records it, what happens next, who acts, how is the loop closed?
4. How do positive-behavior (recognition) and negative-behavior (discipline) poles differ structurally?
5. What reporting/decision machinery exists (per-student history, school-wide patterns, equity/demographic views, program fidelity)?
6. How do products relate to the SIS/MIS (roster sync, data handoff, module vs standalone)?
7. What roles exist (teacher, administrator, family, student) and what can each do?
8. Where is the boundary against Classroom Management's conduct recording?
9. Historical check: do paper-era discipline systems (referral forms, demerit ledgers, detention slips) and the 25-year-old SWIS fit one definition?

## Representative Products

| Product | Vendor | Pole | Market | Evidence |
|---|---|---|---|---|
| SWIS (School-Wide Information System) | PBISApps / University of Oregon (Educational and Community Supports) | academic/nonprofit incident-of-record pole; ODR data for school-wide decision making | US K-12, 10k+ schools | Tier-1 (official product pages + resource pages, fully fetched) |
| SchoolMint Hero | SchoolMint | commercial behavior+attendance suite; PBIS/MTSS/SEL/RTI framing | US K-12 schools & districts | Tier-2 (official product page, fully fetched); help center JS-gated |
| PBIS Rewards | Navigate360 (formerly Motivating Systems) | schoolwide PBIS points economy + referral add-on | US + international K-12 | Tier-1/Tier-2 (official product + feature pages, fully fetched) |
| LiveSchool | LiveSchool | teacher-first school-wide points platform; rewards store/houses | US K-12, large districts | Tier-2 (official product + feature pages, fully fetched) |
| Satchel One (Behaviour module) | Team Satchel | UK whole-school platform; behaviour points + referred incidents + detentions + sanction rules; MIS-integrated | UK schools | Tier-1 (official help center articles, fully fetched) |

Selection rationale: academic/nonprofit vs commercial suite vs points-program vs teacher-first vs UK/MIS-integrated; incident-of-record philosophy vs points-economy philosophy vs whole-school platform philosophy; single school to district scale; US and UK regimes. Satchel One's Behaviour module was already deeply fetched by the classroom-management pass (2026-09-07); this pass re-fetched the key articles fresh and adds the school-wide machinery articles (Referred Incidents, Detentions, Sanction rules, Thresholds) that the sibling pass did not need.

## Sources

- PBISApps — https://www.pbisapps.org/ (root)
- PBISApps — SWIS product page: https://www.pbisapps.org/products/swis
- PBISApps — "Entering and Managing Referrals for Referral Entry Only Users" (video resource page): https://www.pbisapps.org/resource/referral-form-for-referral-entry-only-user
- SchoolMint — Hero product page: https://schoolmint.com/hero (also served at /schoolminthero/)
- SchoolMint help center: https://help.schoolmint.com/ — **JS-gated, unfetchable** (limitation recorded)
- PBIS Rewards — root: https://www.pbisrewards.com/
- PBIS Rewards — How it Works: https://www.pbisrewards.com/how-it-works/
- PBIS Rewards — Behavior Referral System: https://www.pbisrewards.com/features/behavior-referral-system/
- LiveSchool — root: https://www.whyliveschool.com/
- LiveSchool — Behavior Tracking: https://www.whyliveschool.com/features/behavior-tracking
- Satchel One Help Centre — Behaviour events and badges: https://help.satchelone.com/en/articles/11095655-behaviour-events-and-badges
- Satchel One Help Centre — Referred Incidents: https://help.satchelone.com/en/articles/4934555-referred-incidents
- Satchel One Help Centre — Detentions: https://help.satchelone.com/en/articles/11504031-detentions
- Satchel One Help Centre — Thresholds setup: https://help.satchelone.com/en/articles/11524365-thresholds-setup
- Satchel One Help Centre — Sanction rule setup: https://help.satchelone.com/en/articles/11136811-sanction-rule-setup
- Sibling pass (context, not new fetches): research/classroom-management.md (2026-09-07) — Satchel One Behaviour observations, ClassDojo points observations, L0/boundary framing
- Sibling pass (context): research/special-education-management.md boundary note naming "student-behavior-management (incident loop)"

Research date: 2026-09-09.

## Product A — SWIS (PBISApps, University of Oregon) [Evidence layer A]

Positioning: "The School-Wide Information System… your comprehensive, online home for understanding the student behaviors happening in your building every day." "Use office discipline referral (ODR) data to know what's happening schoolwide." "Powerhouse reports for schools."

- **Explicit SIS contrast (high-value boundary evidence)**: "You Already Collect referrals in Your SIS—Why use SWIS to do the Same Thing? … Where traditional student information systems store referral data for end-of-year-reporting, SWIS transforms your data for real-time decision making in ways your SIS can't."
- **Meaningful referral data**: "Keep data accurate and organized with standardized, research-backed menu selections. Require only the information you need for decision making: Who, What, When, Where, and Why. Capture data unique to your school with searchable Custom fields."
- **Paperless referral entry**: "Teachers can enter referrals directly and send them to an administrator for review with workflows. Match your in-app workflow settings with your school's existing referral process. Administrators receive email alerts when there's a referral for them to review." Draft referrals supported; a "Referral Entry Only" user role exists (video resource).
- **"Every Behavior, Every Action Taken"**: "Document every behavior, every action taken with every referral."
- **Reports**: "16 school-wide reports come standard with every subscription. With one click: View referral patterns in real-time. Compare your school-wide trends with national averages of schools your same size. Identify students in need of additional support sooner."
- **Equity Report**: referral/suspension rates broken down by race, ethnicity, gender, language, IEP status; "Interpretive sentences included with each graph."
- **Other features**: Drill Down (drag-and-drop filters), Classroom-managed Behaviors ("Track classroom-managed behaviors before they become bigger headaches"), Role-Based Access, Custom Fields, Cross-App Data, Data Exports, Unlimited Users, Import Rosters (person import), SWIS Mobile app.
- **Suite structure**: SWIS (ODRs) + EC-SWIS (early childhood) + CICO-SWIS (Check-In Check-Out, Tier 2) + I-SWIS (individual student support plans, Tier 3) + TIPS Meetings + PBIS Assessment (TFI/school climate surveys) + PBIS Evaluation (district/region/state roll-ups).
- **Integration**: automatic SIS data integration included; named integrations PowerSchool, Synergy, Aeries, Infinite Campus, Skyward, Alma.
- Scale/age: 10k+ schools, 4.6m+ students, 25 years. Pricing $500/year, "All SWIS features are included out of the box; no hidden fees or subscription levels."
- Not observed: points/rewards economy, parent communication surfaces, hall passes, detention scheduling (action taken is recorded, but no scheduling machinery on the fetched pages).

## Product B — SchoolMint Hero [Evidence layer A for positioning/feature surface; no operational detail]

Positioning: "Behavior & Attendance Tracking Software… Transform Student Behavior Management and Attendance Tracking… the practical way to promote positive behavior, ensure consistency in discipline, and improve attendance."

- **Explicit classroom-app contrast (high-value boundary evidence)**: "Unlike other classroom management systems, SchoolMint Hero isn't an app for individual classes. It's one powerful platform for uniting your entire school community."
- Framework support: "SchoolMint Hero is configurable and supports your preferred framework: SEL, PBIS, MTSS, RTI, and more."
- Behavior tracking: "Assign discipline, and quickly create referrals. Track any behavior you want, including custom ones. Support a school house system. Create a virtual point system that translates to real rewards. Ensure fairness, equity, and consistency in discipline."
- Attendance/tardy machinery: "Automate tardy management and pass printing"; tardy processing for teachers and front office.
- Family layer: "Notify parents/guardians in real time via text or email"; parent app; "Standardize on one behavioral communication tool for the entire school."
- Data: "Monitor behavior interactions by subpopulation: grade, gender, race, etc. Measure progress through preloaded and custom reports."
- Roles: Administrators ("align everyone behind established behavior initiatives, ensure consistency in discipline"), Teachers, Families (parent app), Students (student app: "reward points, positive behaviors, schedules, historical data, detentions, and more").
- Testimonial evidence of detention assignment and late slips ("assign detentions and late slips in seconds").
- Not fetched: help center (JS-gated). No precise workflow/field/limit claims made for Hero anywhere.

## Product C — PBIS Rewards (Navigate360) [Evidence layer A]

Positioning: "PBIS Rewards is an affordable schoolwide PBIS management system… The multi-device platform makes it easy to continuously recognize students for meeting behavior expectations from anywhere in the school, not just the classroom." "A Digital SCHOOLWIDE PBIS MANAGEMENT Solution."

- **Recognize**: staff select the expectation and number of points, scan the student's ID badge or search by name, see results instantly; web portal supports groups and giving points to one/some/all students. "Any staff member can recognize any student, anywhere!"
- **Redeem**: integrated school store (cart/checkout, inventory auto-adjust, redeem now or later), teacher stores, event management (events deduct points or qualify students by points earned in a grading period/year), raffles. "No more fumbling around with torn up papers… Go paperless" — replaces the paper-ticket token economy.
- **Reporting**: "Point totals are automatically tracked in the secure web portal. Complete with admin reports, goal setting, and a student portal." Admin reports cover staff utilization and student progress; "admins will be able to dig deeper into program fidelity and student activity."
- **Students and Families**: student portal + family app; "Families enjoy seeing their student's progress, and are alerted when a referral is given." Push notifications for events and per-student messages.
- **Behavior Referral System (BRS, add-on fee)**: "An important measurement of progress involves tracking office discipline referrals." Customizable lists: Infractions (e.g., Bullying, Fighting), Redirections (teacher de-escalation attempts, e.g., Time Out), Motivations (what was behind the infraction), Administrative Actions (e.g., In-School Suspension, Letter of Apology). Proxy submission (another staff member starts the form); "When a referral is started, the office staff is immediately notified"; "Closed-Loop View – The staff responsible for the referral will see what action was taken by the Administrative Staff"; "360 Degree View" teacher-by-teacher referral analytics; Behavior Intervention Recommendations (Suite360 lessons as possible administrative actions). From the How-it-Works page: "Staff members will be able to see all minor referrals for a student so that when it is time to roll up to a major referral, that is easy too."
- **Other add-ons**: Check-In/Check-Out (Tier 2 progress tracking), House Groups, Hall Pass Plus, SEL/Status Check (per-student SEL tracking + student self-check), Teacher Rewards (staff recognition with its own store), District Portal.
- Fidelity/common-language framing: "Promote a common language among your staff and students, keeping everyone on the same page." ODR-reduction outcome claims tied to the BRS add-on.

## Product D — LiveSchool [Evidence layer A]

Positioning: "The behavior management platform for positive school culture… Behavior Tracking & Rewards for Schools… Reduce referrals. Save time."

- **Explicit classroom-app contrast (high-value boundary evidence)**: "LiveSchool picks up where classroom apps, paper systems, and spreadsheets leave off — with school-wide consistency, real data, and less manual work." "Switch from ClassDojo / Paper Bucks / Spreadsheets / PBIS Rewards."
- **Behavior rubric**: "A school-wide expectations rubric sets the foundation for staff collaboration. You set the behaviors, categories, point values, and more." Example matrix: Respect/Responsibility/Safety categories with named 1-point behaviors (Active Listening, Following Directions, On Task, Walking in Hallways…).
- **Recording**: "Award positive points, document negative behaviors, track referrals – all in one platform." Instant rosters, student search, QR badge scan. Comments on any behavior ("visible to students, families, in addition to staff").
- **Negatives**: "Choose if Negatives Subtract Points. It's up to your team whether students lose points for negative behaviors." "Customize real-time email alerts for major misbehavior and referrals." Demerits referenced in outcome stats ("83% of students with zero demerits").
- **Classroom-adjacent utilities**: project on board, enter points after class, bulk entry, mark absences, random student picker, timer — the teacher-facing surface coexists with the school-wide record.
- **Data views**: School Progress, Teacher Shoutouts, Student Log, Paycheck (weekly earned points), Event List.
- **Economy**: Rewards Store ("students learn financial literacy as they spend their points"), House Points, Family Engagement (real-time updates), Hall Passes ("Launch a pass in one tap, see who is out in real time… smart limits").
- **Setup**: Clever/ClassLink/spreadsheet roster sync; guided launch.
- Outcome framing: referral/suspension reductions in success stories; "Track your positive-to-negative ratio weekly and aim for 5:1 or higher" (practice guidance).

## Product E — Satchel One, Behaviour module (Team Satchel, UK) [Evidence layer A]

Positioning (help centre): "The Behaviour app allows staff to award positive points, negative points, and badges to recognise student behaviour and achievement. All events are stored centrally and can be viewed on student profiles, group pages, and reports. Built-in insights help staff and leaders spot trends and intervene early when needed."

- **Behavior events**: logged from multiple surfaces (Behaviour Overview, a group's Behaviour tab, a student's profile, the homework Assess page). Event fields: reason (school-configured list), date (defaults today, backdatable), optional activity/location, comment (visibility to students/parents per-event and per-school), points. Events editable; students addable/removable; per-student points and outcomes editable.
- **School configuration**: custom Reasons, custom Badges, Lookups (Status, Activity, Location, Time of day, Outcome). Restricted reasons require elevated permissions.
- **Permissions**: granular — `My positive behaviour events`, `My negative behaviour events`, `All positive behaviour events`, `All negative behaviour events`, `Badges`, `Shared behaviour comments`, detention permissions, `My referred incidents`/`All Referred Incidents`, `Sanction rule setup`, `Behaviour threshold setup`, `Detention attendance`.
- **Referred Incidents** (school-wide discipline machinery): "Report serious or repeated low-level incidents to your colleagues for further action." On creation, key staff notified per school policy; staff update, take follow-up actions; **status workflow (Unresolved/Resolved)**; "Once an incident is marked as Resolved, students and parents will also be notified" — parent visibility gated on Resolved. Form: date, reason, activity, location, time of day, reported-by (auto), **assign to** (escalate to a specific staff member), status. Students involved carry **role, points (auto-filled from reason default; 0 for witnesses/targets), and outcome**. Comments staff-only by default with share toggle.
- **Detentions**: "assign, manage, and track student detentions efficiently – from scheduling and attendance to rescheduling and reporting." Detention types (pre-populate per school policy), cover teacher (appears on their timetable and detention list), scheduled date, location, start/end time. Students added with behaviour reason; can be added directly while recording negative points. **Detention register**: attendance recorded per student — Attended / Authorised absence (reschedule) / Unauthorised absence. Reschedule to next available date (approve or set manually). Some fields locked once live; date changes via delete + recreate "to ensure students and parents are notified ahead of time." Reports: Detentions overview.
- **Sanction rules** (automation): "Sanction rules define the behaviour patterns that should trigger follow-up actions, such as detentions or referrals. Once a rule is met, a recommendation appears on the Sanctions dashboard for staff to review and act upon." Rule = reasons × occurrences × timeframe (last day / 7 days / 30 days / academic year) × severity (1–5) → sanction type (specific detention type or Referred Incident). Recommendations require staff action — not auto-executed.
- **Thresholds**: advisory weekly limits on positive/negative points and badges ("soft limits… to promote consistency across staff"); warnings dismissible; school-wide, reset weekly.
- **Visibility**: parent/student views via web and app with notifications; school-configurable (positive-only, staff-only, badges-only); referred incidents visible only when Resolved.
- **Year mechanics**: "Points remain available for previous years. Student totals reset to zero for a fresh start" at academic-year change. MIS sync "depending on your MIS system." Mobile awarding supported.

## Cross-product Comparison

| Dimension | SWIS | SchoolMint Hero | PBIS Rewards | LiveSchool | Satchel One Behaviour |
|---|---|---|---|---|---|
| Unit of record | office discipline referral (behavior event + action taken) | behavior events + discipline/referrals | points events; referrals via BRS add-on | points events (positive/negative) + referrals | behaviour events (points/badges) + referred incidents + detentions |
| School-defined framework | standardized research-backed menus + custom fields; school configures what to require | custom behaviors; framework support (SEL/PBIS/MTSS/RTI) | expectations + point values; customizable infraction/redirection/motivation/action lists (BRS) | school-wide expectations rubric (behaviors, categories, point values) | custom reasons, badges, lookups (status/activity/location/time/outcome); detention types; sanction rules |
| Points economy | none | virtual point system → real rewards | core (recognize/redeem, store, events, raffles) | core (points, rewards store, paycheck) | points + badges (no store observed) |
| Positive/negative duality | negative-focused (ODRs) | both | both (positive core; negatives via BRS) | both (configurable whether negatives subtract) | both (+ badges) |
| Referral/administrative loop | teacher entry → administrator review workflow + email alerts | quick referrals + discipline assignment | BRS: office notified → admin action → closed-loop view; minor→major roll-up | real-time alerts for major misbehavior/referrals | Referred Incidents: assign-to, status workflow, roles/outcomes, Resolved-gated parent visibility |
| Consequence machinery | action taken recorded per referral | discipline assignment; detentions (student app) | administrative actions list (BRS) | alerts; consequences not prominent | detentions (types, cover teacher, register, attendance codes, reschedule); sanction rules recommend |
| Parent/family layer | not observed | real-time text/email + parent app | family app + referral alerts + push | family engagement updates | parent/student views + notifications, school-configurable visibility |
| Student-facing | not observed | student app (points, history, detentions) | student portal | student/family visibility of points | student views (visibility-configurable) |
| Per-student history | student referral data; drill-downs | historical data in student app | point totals + progress | Student Log | student Behaviour tab (academic-year range, statistics, most common reasons) |
| School-wide analytics | 16 standard reports; equity report; national averages | subpopulation monitoring; preloaded + custom reports | admin reports; staff utilization; program fidelity | School Progress; Teacher Shoutouts | Behaviour insights reports/exports; detention overview |
| Roster substrate | SIS integration (named SIS vendors) | (not detailed on fetched page) | integrations page | Clever/ClassLink/spreadsheets | MIS sync |
| Roles/permissions | role-based access; referral-entry-only role | admin/teacher/family/student | staff vs admin; district portal | staff; family; student | granular named permissions per action |
| Mobile | SWIS Mobile | parent/student apps | staff/family/student apps | (web-first; apps implied) | mobile awarding + parent/student app |
| Adjacent machinery bundled | CICO/I-SWIS/EC-SWIS; PBIS Assessment; TIPS | attendance/tardies, passes, houses | CICO, houses, hall passes, SEL check, teacher rewards | houses, hall passes, attendance marking | (homework platform around it; attendance module sibling) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The student behavior event of record** — a persistent, individually recorded conduct event bound to identified student(s), attributed to a staff member, stamped with time and context (commonly location/activity), and classified against the school's behavior vocabulary; events accumulate into the student's behavior history. Remove → a notes log / nothing to manage.

2. **The school's conduct framework** — the school-defined structure that gives events consistent meaning and consequence across the whole school: the behavior taxonomy (categories/reasons, commonly with point values, commonly spanning positive and negative conduct) together with the consequence structure (actions/sanctions that events can call for). One framework, one record — not per-classroom. Remove → classroom-local conduct tracking (Classroom Management territory) or an unstructured log.

3. **The record→respond→review loop** — events drive recorded responses (recognition points, administrative actions/consequences, sanctions) that are attached to the event and accumulate on the student's record; the accumulated data is surfaced — per-student history and school-wide patterns — for staff review, follow-up, and early intervention. Remove → a log nobody acts on; the "management" dies.

Jointly-held load-bearing tests:

- 1 alone = behavior log/notes archive
- 2 without 1 = a conduct policy document (paper matrix), no system
- 3 without 1+2 = free-floating consequences with no record
- 1+2 without 3 = classified archive nobody acts on
- 1+3 without 2 = per-classroom/inconsistent tracking → Classroom Management's conduct pole
- 2+3 without 1 = framework with no events (nothing happening)

### L1 — Common Mature Structure (very common, not definitional)

- Positive/negative duality (recognition + discipline) — 4/5 (SWIS is ODR-focused)
- Points/merit economy with redemption (store, events, raffles) — 4/5 (SWIS lacks)
- Referral/administrative processing loop (staff submits → office notified → administrator records action → closed-loop visibility back to the referrer) — present in all 5 in some form, but sold as an add-on at PBIS Rewards → common, not definitional
- Parent/guardian notification and configurable visibility — 4/5 (SWIS lacks)
- Per-student behavior history/profile view — all 5
- School-wide analytics (patterns over time, demographic/equity breakdowns, staff-utilization/fidelity views) — all 5
- Roster substrate from the SIS/MIS (named SIS integrations, Clever/ClassLink, MIS sync) — all 5
- Role-based access with named per-action permissions — all 5
- Mobile awarding surfaces — 4/5 observed
- Hall passes / tardy machinery — 3/5 (Hero, PBIS Rewards Hall Pass Plus, LiveSchool)
- House/group systems — 3/5 (Hero, PBIS Rewards, LiveSchool)
- Minor/major (classroom-managed vs office-managed) classification and roll-up — SWIS + PBIS Rewards explicit
- Detention/sanction scheduling depth — 2/5 deep (Satchel One; Hero testimonial-level)
- Threshold/consistency guardrails — 1/5 explicit (Satchel advisory thresholds)

### L2 — Variant / Optional Structure

- Program framing: PBIS/MTSS/SEL/RTI (US) vs plain behaviour/discipline (UK) vs school-culture framing
- Points philosophy: positive-only emphasis vs positive+negative vs demerit-based; whether negatives subtract from spendable balances (product-configurable at LiveSchool)
- Tier-2/3 intervention support: CICO tracking, individual support plans (SWIS Suite CICO-SWIS/I-SWIS; PBIS Rewards CICO add-on)
- Behavior intervention content: recommended lessons as administrative actions (PBIS Rewards/Suite360)
- Regional machinery: UK MIS integration + detention culture + academic-year reset; US discipline data flowing to SIS year-end/state reporting (SWIS's own framing)
- Deployment/packaging: standalone specialist vs module inside a whole-school platform (Satchel One) vs suite member (SWIS Suite) vs SIS-suite behavior module (market context; not sampled directly)
- Early-childhood variant (EC-SWIS)
- District/multi-school roll-ups (PBIS Rewards District Portal, PBIS Evaluation, LiveSchool For Districts)

### L3 — Vendor-specific (Research Notes only)

- SWIS: 16 standard reports; Equity Report with interpretive sentences; national same-size-school averages; facilitator network/certification; $500/year flat pricing; draft referrals; Referral Entry Only user role; TIPS Meetings; PBIS Assessment (TFI)
- PBIS Rewards: ID-badge scanning ("debit card" framing); BRS customizable four-list structure; Suite360 intervention recommendations; Teacher Rewards; SEL/Status Check with student self-check; raffles; event qualification by grading-period points; add-on fee structure
- LiveSchool: Paycheck view; Teacher Shoutouts; rubric generator/house-name tools; "switch from" comparison pages; 5:1 ratio practice guidance; 2–3 school day Clever/ClassLink sync window
- Satchel One: Referred Incidents Resolved-gated parent visibility; detention register attendance codes (Attended/Authorised/Unauthorised); reschedule-to-next-available; delete-and-recreate rule for date changes (notification guarantee); sanction rules (reasons × occurrences × timeframe × severity → recommendation on a Sanctions dashboard); advisory weekly thresholds (dismissible, Monday reset); academic-year point reset with retained history; named permission strings; MIS-sync dependency
- Hero: tardy automation + pass printing; customer case-study statistics (85% tardy reduction etc. — marketing figures, not asserted as Type facts)

## Vendor-specific Findings

See L3. Additional notes:

- The three US points products (Hero, PBIS Rewards, LiveSchool) all bundle hall passes and house systems — a US-market bundle pattern, not definitional.
- PBIS Rewards' BRS being an add-on fee is strong evidence that the referral/administrative loop, while very common, is not the definitional minimum: a points-only deployment remains recognizably Student Behavior Management.
- SWIS's lack of points/parents/passes is equally strong evidence in the other direction: an incident-of-record system with reports remains recognizably Student Behavior Management.

## Boundary Findings

1. **vs Classroom Management (§23 sibling; JOINT REVIEW FLAG DISCHARGED from this side — keep-both RATIFIED).** The sibling pass recorded a gradient: "in-class conduct recording (points/rewards) is classroom management, while school-wide discipline machinery (referrals, sanctions, detention administration, PBIS program management) is the sibling Type," and noted the seam runs through products (Satchel One carries both). This pass confirms and sharpens the seam: the discriminator is **whether the conduct framework, the record, and the response loop are school-wide or classroom-local**. Classroom Management's conduct pole = the teacher's in-the-moment, per-class recording (ClassDojo per-class custom skills) inside a live-classroom tool; Student Behavior Management = one school-defined framework, one central record, an administrative response loop, and school-wide measurement. Vendor behavior supports the split: Hero's own copy — "Unlike other classroom management systems, SchoolMint Hero isn't an app for individual classes. It's one powerful platform for uniting your entire school community"; LiveSchool's "Switch from ClassDojo — Get real analytics and school-wide PBIS" and "picks up where classroom apps… leave off — with school-wide consistency." Removal tests: remove the school-wide framework + administrative loop from this Type → classroom-local conduct recording (Classroom Management); remove the live-classroom operation (device control, seating, timers, in-the-moment direction) from Classroom Management → nothing conduct-shaped remains there but per-class points. The seam runs through products (Satchel One Behaviour module vs its classroom modules; LiveSchool's classroom-adjacent utilities beside its school-wide record) — module-level, not product-level. Both leaves stand.

2. **vs Student Information System / SIS (§23 sibling, UNPROCESSED — flag for the SIS pass).** The SIS owns the student population and stores discipline data for official/year-end reporting; standalone behavior products own the conduct program loop (real-time decision support, program measurement, recognition economies). SWIS's own framing is the cleanest evidence: "Where traditional student information systems store referral data for end-of-year-reporting, SWIS transforms your data for real-time decision making in ways your SIS can't." SIS behavior modules are a packaging variant of this Type's loop; standalone products integrate with the SIS for rosters (SWIS named SIS integrations; LiveSchool Clever/ClassLink; Satchel MIS sync) and hand data back. Removal test: remove the conduct framework + response loop from an SIS behavior module → plain incident storage. Keep both; center-of-gravity seam. Not discharged here (SIS unprocessed) — recorded for the SIS pass.

3. **vs Student Case Management (§23 sibling, UNPROCESSED — flag).** This Type runs the incident/conduct loop over the general student population; events are closed by administrative resolution, not by assigned caseworkers. Case management (per the academic-advising pass's framing) is issue-driven casework with an ongoing responsible party. Repeated incidents may feed intervention processes (CICO, behavior intervention plans) that touch Special Education/MTSS machinery, but the incident loop itself has no eligibility gate, no mandated plan, no caseload. Consistent with the special-education pass's boundary note ("student-behavior-management (incident loop)").

4. **vs Special Education Management (§23, processed).** Consistent with that pass: special-ed owns the regulated process (evaluation → eligibility → plan → compliance); behavior management feeds conduct data toward it and stays outside the regulated machinery. No conflict.

5. **vs Student Attendance System (§23, processed).** Attendance records presence; behavior records conduct. Behavior products bundle tardy/attendance features (Hero, LiveSchool mark absences) as adjacent machinery; the attendance pass found no behavior overlap from its side. Clean.

6. **vs School Counseling Management (§23 sibling, UNPROCESSED — flag).** Counseling = caseload/appointments/notes/plans for student support; behavior = conduct events and consequences. A counselor may be a consumer of behavior data; the objects and loops differ. Flag for that pass.

7. **vs PBIS as a framework.** PBIS is a methodology, not an Application Type; products implement it with varying fidelity machinery. PBIS Assessment (TFI surveys, action plans) is program-fidelity measurement — a different job from conduct-event recording; treated here as suite-adjacent (SWIS Suite), not part of the Type's core.

## Historical / Market-Sample Check (§24)

- **SWIS itself is the historical anchor**: 25 years old (late-1990s generation), predates the modern points-app era, and satisfies the L0 with no points economy, no parent app, no mobile-first design: school-defined behavior definitions + referral entry + action taken + school-wide reports.
- **Paper-era practice fits**: office discipline referral forms routed to the office for administrative action, a per-student discipline file, a school-wide code of conduct with demerit/merit systems and detention slips, and end-of-term discipline summaries — all three L0 structures present with no software.
- **UK detention/behaviour culture** predates the software and fits via the Satchel One shape (points + referred incidents + detentions).
- **Regional/platform-native variants**: MIS-embedded behaviour modules (UK SIMS-class) and SIS behavior modules (US) fit the same core as packaging variants.
- Conclusion: the definition is not over-fit to the modern positive-points app pattern. Points, parents, passes, houses, and mobile awarding are era-current layers, not definitional.

## Uncertainties

1. **SchoolMint Hero operational detail unverified** — help center JS-gated; all Hero statements are positioning/feature-surface level (Tier-2). No Hero workflow, field, or numeric claims are made anywhere.
2. **State discipline reporting** — SWIS's framing evidences that SIS-side storage serves end-of-year reporting, but whether standalone behavior products ship direct state-reporting exports was not evidenced; kept out of the final document.
3. **SWIS positive-event recording** — not evidenced on fetched pages; SWIS is treated as ODR-focused (its own framing). Whether schools record positive referrals in SWIS is unknown.
4. **Minor/major machinery breadth** — explicit at SWIS (classroom-managed behaviors) and PBIS Rewards (minor→major roll-up); generalization to the whole market kept weak.
5. **Market breadth** — Kickboard (PowerSchool), Review360, and SIS-native behavior modules (PowerSchool/Infinite Campus/Skyward) were not sampled; the SIS-module pole is evidenced indirectly (SWIS's SIS contrast + integration lists). Recorded as an uncertainty for the SIS pass.
6. **Threshold automation depth** — Satchel's thresholds are advisory and its sanction rules recommend rather than auto-execute; whether other products auto-execute consequences without staff action was not evidenced; the final document says recommendations/automation "commonly require staff review" only where evidenced (Satchel), and otherwise stays generic.

## Final Synthesis

A Student Behavior Management application is the school's conduct system of record: it holds the school's behavior framework (a school-defined taxonomy of behaviors/reasons — commonly weighted with points and paired with a consequence structure — applied uniformly across classrooms and staff), records conduct events against identified students as staff observe them (positive recognition, negative incidents, referrals), drives recorded responses (points accumulating on the student's record, administrative actions/consequences, scheduled sanctions such as detentions), and surfaces the accumulated record — per-student behavior histories and school-wide patterns, commonly with demographic/equity breakdowns — so staff can follow up, intervene early, and measure the school's behavior program. The market realizes the Type as: incident-of-record systems (SWIS pole), points-economy platforms with rewards stores and houses (PBIS Rewards, LiveSchool, Hero poles), whole-school platform modules with deep sanction machinery (Satchel One pole), and SIS-suite behavior modules (packaging variant). The defining core is the event-of-record + school-wide framework + record→respond→review loop triad; points, parents, passes, houses, mobile apps, Tier-2/3 intervention support, and detention scheduling depth are common or variant structure. The Type's boundaries: classroom-local conduct recording is Classroom Management; population/academic record-keeping and official reporting storage is the SIS; regulated intervention processes are Special Education Management; issue-driven casework is Student Case Management; presence recording is Student Attendance.
