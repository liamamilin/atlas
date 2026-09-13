# Research Notes — Fitness Assessment Application

## Research Goal

Understand what software sits under the directory leaf "Fitness Assessment Application" (§28 Sports, Fitness & Recreation, between "Workout Tracking Application" and "Fitness Progress Tracker"): what its core objects are, who conducts assessments and on whom, how a structured fitness evaluation is defined, recorded, scored, and compared over time, and where the boundary lies against Fitness Progress Tracker, Personal Training Management, Workout Tracking Application, Athlete Management System, Sports Performance Analytics, and Corporate Wellness Platform.

## Initial Boundary (hypothesis before research)

- Hypothesis: the center is the **structured fitness assessment** — a defined battery of tests/measures (protocol) conducted on a person by an assessor, recorded as results, interpreted against standards/norms/baselines, and re-administered over time to show change.
- Likely neighbors: Fitness Progress Tracker (self-tracked body metrics), Personal Training Management (PT business software with assessment as a module), Workout Tracking Application (training session logs), Athlete Management System (organizational program management with testing as one input), Sports Performance Analytics (performance data analysis), Corporate Wellness Platform (health-risk questionnaires), Candidate/Psychometric Assessment Platform (§09, different domain).
- Key uncertainties going in: (1) is there a standalone product market for this Type, or is it mostly a module inside PT/gym platforms? (2) how do institutional (school/state) assessment systems differ from trainer-side ones? (3) does hardware-instrumented testing (force plates) belong here or in Sports Performance Analytics?

## Research Questions

1. What is an "assessment" in this domain — what defines the protocol/battery, and who authors it?
2. Who is the assessed person (client/student/athlete), and how are they represented?
3. What is the unit of assessment (event/session/occasion), and what states does it carry?
4. How are results recorded, scored, and interpreted (standards, norms, zones, algorithms)?
5. How does re-assessment / longitudinal comparison work?
6. What outputs exist (reports, client-facing results, exports)?
7. How do results feed downstream action (programming, instruction, reporting obligations)?
8. What roles exist (assessor, administrator, assessed person) and what can each do?
9. Where is the boundary against self-tracking, business management, and analytics products?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer levels:

1. **FitnessGram** (by GreenLight Fitness, Cooper Institute lineage) — institutional/school youth fitness assessment; protocol + criterion-referenced standards; state/district/school hierarchy. Strong Tier-1 help-center documentation.
2. **FMS / Functional Movement Systems** — professional movement screening (FMS/SFMA/YBT/FCS); certification-driven; clinician/trainer-side. Tier-1 help center + Tier-2 system pages.
3. **Exercise.com** — fitness business platform marketing "fitness assessment software"; assessments as a platform module tied to programming and lead conversion. Tier-2 product pages.
4. **Hawkin Dynamics** — hardware-instrumented sports performance testing (force plates, dynamometry) with capture app + cloud reporting. Tier-2 product pages.
5. **PT Distinction** — personal trainer software with built-in/custom assessments. Tier-2 product page only.

Rejected/considered: Trainerize (www + support both 403 — abandoned per network rules), TrueCoach (help center JS-blocked), Everfit (help center shows metrics tracking, not an assessment center of gravity).

## Sources

- FitnessGram: https://www.fitnessgram.net/ , https://www.fitnessgram.net/software-overview , https://help.fitnessgram.net/support-topics/ , https://help.fitnessgram.net/fitnessgram-test-events/create-a-fitnessgram-test-event/ , https://help.fitnessgram.net/fitnessgram-test-events/enter-fitnessgram-data/ , https://help.fitnessgram.net/reports/fitnessgram-reports-overview/ (fetched 2026-09-07)
- FMS: https://www.functionalmovement.com/ , /system , /system/fms , /membership/memberbenefits/app , https://help.functionalmovement.com/en/knowledge , /en/knowledge/fms-pro , /en/knowledge/who-can-use-the-fms-pro-app (fetched 2026-09-07)
- Exercise.com: https://www.exercise.com/ , https://www.exercise.com/platform/assessments/ (fetched 2026-09-07)
- Hawkin Dynamics: https://www.hawkindynamics.com/ , https://www.hawkindynamics.com/software (fetched 2026-09-07)
- PT Distinction: https://www.ptdistinction.com/ (fetched 2026-09-07)

Source-access limitations: Trainerize and TrueCoach official documentation could not be fetched (403 / JS-only). Consequently the PT-platform pole is evidenced by Exercise.com and PT Distinction at product-page (Tier-2) strength only; no operational help-center detail for that pole was directly observed. FMS Pro App and Hawkin cloud details are product-page level. Precise numeric limits, exact report parameters, and pricing are not asserted anywhere.

## Product Observations

### FitnessGram (evidence layer A — help center + official site)

- Positioning: "The Gold Standard in Student Fitness Assessment and Tracking", in market since 1982; roles: Teacher, School or District, State Program, Student or Parent.
- Evidence-based assessment: criterion-referenced standards; "Healthy Fitness Zone" (HFZ) per assessment area (aerobic capacity, muscular strength, flexibility, body composition); standards tailored by age group and gender; emphasis on personal health improvement "without shaming or ranking".
- Software structure (help center): Login; Licenses; Data Management (manage users/students, classes); Data Upload; OneRoster imports (SIS integration); **FitnessGram Test Events** (create / enter data / edit / delete); System Admin Settings (districts & schools, manage mandates, notifications, roles & privileges); Reports; SmartCoach; ActivityGram (activity behavior assessment); FitnessGram App; state program pages (Texas, Illinois, South Carolina, DoDEA).
- Test Event creation (help center): name (descriptive, incl. school/teacher/age group/semester); Test Event Type (Pre-test for fall, Post-test for spring, Other); start/end dates — end date calculates the student's age at assessment, which selects which standards the student is compared against, and appears on the student report; select Schools and Classes; choose Test Items (recommended battery options offered; guidance not to create one test event per test item); Save and Exit or Proceed to data entry.
- Data entry (help center): enter scores by Student or by Class; students can be exempted from test items within a test event; SmartCoach resources offered based on assessment selections.
- Reports (help center): FitnessGram Student Report, Completion Report, Overview Report (by class), Class Score (PYFA) Report, Data Export; reports can be generated and emailed.
- Compliance posture: FERPA compliant, TX-RAMP certified; "Private By Default".
- SmartCoach: library of step-by-step protocol videos for correct assessment technique, "ensuring accuracy and consistency from preparation to execution".

### FMS / Functional Movement Systems (evidence layer A for system/certification structure; B for app features)

- The System: FMS (Functional Movement Screen — baseline movement screen for fitness/performance professionals), SFMA (Selective Functional Movement Assessment — clinician-side, pain/diagnosis, "differential diagnosis"), FCS (Fundamental Capacity Screen — capacity testing after movement competency), YBT (Y Balance Test). Professions listed: physical therapist, chiropractor, athletic trainer, personal trainer, strength & conditioning coach, etc.
- FMS described as "standardized movement screening"; scoring criteria for "consistent and reliable screening results"; FMS Algorithm used to "interpret the scoring results and select the correct movement training priority"; screen informs programming ("objective filter and feedback tool"); correctives prescribed from screen results.
- Certification-driven: Level 1/Level 2 courses (live/virtual/online) with certification exam; CEU approvals; private courses for staff.
- FMS Pro App (product page): "Collect, calculate, report and program from the palm of your hand"; client management (profiles, search); access all FMS/FCS/YBT/SFMA data; auto-generate FMS correctives from the report screen; workout builder + exercise library; clients can log into the app to access their workouts and reports; cues built into each step to guide the screening process.
- Access gating (help center): app available to active FMS members; sections unlocked upon certification (e.g., only SFMA-certified individuals can access the SFMA section).
- Symmio: a separate digital platform product (linked, not researched in depth).

### Exercise.com (evidence layer A for module existence and stated capabilities; marketing-level for workflow)

- Platform module "Assessments" under Marketing; page titled "Fitness assessment software for personal trainers and fitness professionals".
- Stated capabilities: take clients through custom fitness assessments; assessment scores automatically create personalized, data-driven workouts; introductory fitness assessments for leads ("turn leads into clients"); recurring personalized assessments for engagement/retention; assessments support video, text, conditional logic, and routing logic; clients access assessments through custom-branded apps; automated reporting for client insights.
- Platform context: all-in-one fitness business software (business, workouts, marketing, online, payments); industries include gyms, personal trainers, sports performance, physical therapy, chiropractic, corporate wellness.

### Hawkin Dynamics (evidence layer A for product structure; marketing-level for workflow detail)

- Products: dual wireless force plates, Foundation force plate, TruStrength dynamometer; "Hawkin Software" cloud (cloud.hawkindynamics.com login).
- Stated workflow: "1. TEST — run the assessment on your force plate or TruStrength dynamometer, captured live on device. 2. IMMEDIATE FEEDBACK — see clear, validated metrics the moment testing ends. 3. DEEPER REPORTS IN THE CLOUD — trends, comparisons, and full reporting across athletes, teams, and time."
- Capture application ("Hawkin Capture") streamlines data collection across the device suite; real-time insights; cloud-based reporting; data ownership ("export, migrate, or delete"); "validated & repeatable — consistent methodology across devices and testers".
- Audience: "coaches, clinicians, and athletes"; scale claims (17k organizations, 120 countries, 19M all-time tests) — marketing figures, not asserted as facts in the final document.

### PT Distinction (evidence layer A for module existence; marketing-level otherwise)

- Feature list includes "Assessments — built-in, or custom assessments to help you better understand your client's needs" alongside training programs, nutrition, habits, client results, integrations ("track client metrics").
- Personal trainer software context: branded apps, automation, payments.

## Cross-product Comparison

| Structure | FitnessGram | FMS | Exercise.com | Hawkin Dynamics | PT Distinction |
|---|---|---|---|---|---|
| Assessment protocol/battery | Test items + recommended batteries; HFZ standards | Standardized screens (FMS/SFMA/YBT/FCS) with scoring criteria | Custom assessments built by the professional (conditional logic) | Standardized instrumented tests (validated metrics) | Built-in or custom assessments |
| Assessed person as record | Student (via classes; age/gender drive standards) | Client/patient profile | Client (CRM) | Athlete (profiles, teams) | Client |
| Assessment occasion | **Test Event** (named, typed pre/post, dated window) | Screen session per client in app | Assessment instance per client | Test session via Capture app | Assessment per client |
| Recording results | Enter scores by student or by class; exemptions per item | Collect scores in app; cues guide each step | Collect responses/results | Live capture from device | Record results |
| Evaluative interpretation | Criterion-referenced HFZ standards by age/gender | Scoring criteria + algorithm → training priority | Scores → areas of improvement → automated workouts | Validated metrics, immediate feedback, comparisons | Results inform programming |
| Longitudinal comparison | Trends across test events; student→state reports | Re-screening; movement data stored over time | Recurring assessments; progress tracking | Trends/comparisons across athletes/teams/time | Client results over time |
| Outputs | Student/Completion/Overview/Class Score reports + export | Advanced reports; client-accessible reports | Client-facing results in branded apps | Cloud reports, shareable | Reports to clients |
| Downstream action | Program improvement; state reporting | Correctives + workout prescription | Automated workout delivery; lead conversion | Training/recovery decisions | Programming |
| Institutional layer | District/school/state; mandates; roles; OneRoster | Certification body; certified members | Business (multi-location, staff) | Organization; teams | Trainer business |
| Protocol education | SmartCoach protocol videos | Certification courses + in-app cues | — | — | — |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (all four jointly held)

1. **The assessment protocol** — a defined battery of tests/measures with administration rules that structures what is evaluated and how. The protocol exists prior to and independent of any single assessment. Remove → generic client notes / progress log.
2. **The assessed person as a persistent record** — the subject (client, student, athlete, patient) whose results accumulate on an identified record. Remove → anonymous calculator or one-off paper form.
3. **The assessment record** — an identified person's results on the protocol at a point in time, held by the application (the protocol × person × occasion intersection). Remove → protocol reference material with nothing recorded.
4. **The evaluative reference** — results are interpreted against something beyond the raw number: criterion standards, norms, scoring rules, baselines, or goal-referenced ratings, producing zones/scores/flags that carry meaning for decisions. Remove → raw measurement log (Fitness Progress Tracker territory).

Jointly-held is load-bearing: protocol + record without evaluation = a data-capture form; evaluation without a protocol = generic quiz/survey; record without protocol = a notes app.

### L1 — Common Mature Structure (very common, not definitional)

- Longitudinal re-assessment: baseline → re-test → progress comparison (near-universal in the sample; a one-off scored screen still satisfies L0).
- Maintained protocol/standards content: vendor- or institution-maintained test batteries, standards, norms (FitnessGram HFZ; FMS screens; Hawkin validated test library).
- Reporting surfaces: individual reports, group/aggregate reports, exports (FitnessGram report family; Hawkin cloud reports; FMS reports).
- Downstream linkage: results feed programming/training decisions (FMS correctives; Exercise.com automated workout delivery; Hawkin training decisions).
- Subject-facing results: the assessed person can view their own reports (FitnessGram student/parent reports; FMS client app access; Exercise.com branded apps).
- Group administration: classes, teams, rosters as the unit of assessment delivery (FitnessGram classes; Hawkin teams).
- Roster/data import and SIS-style integration (FitnessGram OneRoster).
- Protocol education/guidance: protocol videos, in-app cues, certification (FitnessGram SmartCoach; FMS courses + cues).

### L2 — Variant / Optional Structure

- Institutional mandate/reporting layer: state mandates, compliance reporting (FitnessGram; US-school pattern).
- Organizational hierarchy: district → school → class → student; organization → team → athlete.
- Hardware-instrumented testing: force plates, dynamometers feeding the assessment record (Hawkin).
- Body-composition device integration (not directly researched; low-confidence variant).
- Certification-gated software access (FMS: sections unlock upon certification).
- Commercial use of assessments: lead conversion, paid assessment offerings (Exercise.com).
- Questionnaire-style screening inside the intake flow (health-history/PAR-Q-style forms; Exercise.com conditional logic).
- Exemptions/accommodations per subject per test item (FitnessGram).
- Privacy/compliance regimes for minors' data (FitnessGram FERPA posture).
- Activity-behavior companion assessments (FitnessGram ActivityGram).

### L3 — Vendor-specific (research notes only)

- FitnessGram: Healthy Fitness Zone, PACER test, SmartCoach, ActivityGram, PYFA report, My Healthy Zone portal, TX-RAMP certification, state program pages.
- FMS: FMS/SFMA/YBT/FCS product names, FMS Algorithm, FMS Academy, Symmio, FMS Pro App, certification levels.
- Hawkin: Hawkin Capture app, TruStrength, Scoreboard, cloud.hawkindynamics.com.
- Exercise.com: conditional-logic assessment builder, automations, custom-branded apps.
- PT Distinction: AI program generator, branded apps, "all features included" packaging.

## Historical / Market-Sample Check

- Would older or differently positioned products fit the L0? A spreadsheet-era school fitness-test recorder (protocol columns, student rows, standards lookup, fall/spring comparison) satisfies all four L0 properties. FitnessGram itself dates to 1982 as an assessment program with software following; the paper test-battery era (youth fitness test manuals with norms tables) satisfies protocol + evaluative reference even before software. The definition does not depend on mobile apps, cloud, hardware, or state mandates.
- The definition does not depend on the US school pattern: FMS (professional screening), Hawkin (sports organizations), Exercise.com/PTD (commercial training businesses) all fit without mandates, districts, or FERPA.
- Conclusion: L0 survives the historical/regional check. Modern specifics (protocol video libraries, client apps, automated workout delivery, hardware capture) stay in L1/L2.

## Vendor-specific Findings

- Certification-gated software (FMS) is unique in the sample: software sections unlock by certification level. Product-specific.
- State-mandate machinery (FitnessGram "Manage Mandates") is unique in the sample; institutional-reporting variant.
- Assessment→automated-workout-delivery closure (Exercise.com) is the strongest stated automation link in the sample; other products link results to human programming decisions.
- Hardware-captured objective metrics (Hawkin) vs assessor-scored observations (FMS, FitnessGram) vs questionnaire/logic forms (Exercise.com) — three different measurement philosophies across the same L0.

## Boundary Findings

1. **vs Fitness Progress Tracker** (directory sibling, unprocessed): the tracker centers the person's self-tracked body metrics over time (weight, measurements, photos) with no protocol, no assessor, and no evaluative reference. Discriminator: protocol + evaluator + reference. Remove the protocol/evaluator from this Type → progress tracker. Joint review recommended when that leaf is processed.
2. **vs Personal Training Management** (unprocessed sibling): PT business software centers the client business relationship (scheduling, packages, billing, programming); assessment is one module. The market realizes this Type largely as a module inside such platforms (Exercise.com, PT Distinction) — the module carries the L0; the platform does not become this Type.
3. **vs Workout Tracking Application**: workout tracking records executed training sessions; no evaluation protocol against standards, no assessed-person evaluation semantics.
4. **vs Athlete Management System** (processed): AMS centers the organizational roster + program management + longitudinal preparation record feeding a staff review loop; testing/benchmarking is documented there as a standard capability, not the center. When structured testing events become the center of gravity, the product is this Type.
5. **vs Sports Performance Analytics** (unprocessed): analytics centers on analyzing performance data (dashboards, models, trends); this Type centers the structured testing event that produces evaluative results. Hardware-testing clouds sit close to this seam.
6. **vs Corporate Wellness Platform** (processed): wellness assessments are personal health-risk/lifestyle questionnaires serving program engagement with aggregate employer reporting; this Type centers physical fitness testing protocols with person-identified evaluative records.
7. **vs clinical movement assessment (SFMA pole)**: FMS's SFMA is a clinician-side differential-diagnosis tool — drifts toward clinical/physical-therapy assessment. The fitness boundary: this Type serves fitness/performance evaluation, not medical diagnosis or treatment. Recorded as a variant edge, not a different leaf.
8. **vs Candidate/Psychometric Assessment Platform (§09)**: same abstract shape (protocol + subject + scoring + reports) but different subject matter (people's fitness vs hiring/psychology), different users, different standards. Family resemblance only; no merge.
9. **"去掉什么就变成另一个 Type" 判据**: remove the protocol → progress tracker / notes; remove the person-bound record → calculator/paper form; remove the evaluative reference → raw measurement log; move the center to the business relationship → Personal Training Management; move the center to program management → Athlete Management System; move the center to data analysis → Sports Performance Analytics.

## Taxonomy Observation

The market realizes this Type in three packaging poles: (a) dedicated protocol systems (FitnessGram, FMS), (b) modules inside fitness-business/PT platforms (Exercise.com, PT Distinction), (c) hardware-testing clouds (Hawkin Dynamics). No single pole dominates; the directory leaf is legitimate as a Type (dedicated products exist) but the embedded-module realization is at least as common. No directory change proposed.

## Uncertainties

- Trainerize/TrueCoach operational documentation inaccessible (403/JS) — the PT-platform pole's assessment-module mechanics (how assessments are built, taken, scored in those products) are unverified; assertions for that pole kept at product-page strength.
- FMS Pro App operational detail (exact in-app scoring workflow) observed only at product-page level.
- Hawkin cloud reporting detail (exact report types, norm sets) not directly observed.
- Consumer-facing self-assessment apps (person assesses themselves) were not researched; the sampled products are all professional-side. If such a market exists, it may warrant a boundary note against Fitness Progress Tracker.
- Body-composition device software (InBody-class) not directly researched; recorded as a low-confidence variant.
- Whether "Fitness Assessment" and "Fitness Testing" (sports performance testing) should be one leaf or two — this pass treats instrumented sports testing as a variant of this Type; Sports Performance Analytics remains the analytics neighbor.

## Final Synthesis

A Fitness Assessment Application is best understood as **the assessor-side system of record for structured fitness evaluation**: a defined assessment protocol (battery of tests with administration rules) is administered to identified people (clients/students/athletes), whose results are captured as point-in-time assessment records and interpreted against an evaluative reference (criterion standards, norms, scoring rules, baselines) to produce meaningful ratings; re-assessment over time turns single evaluations into progress narratives, and results feed programming, instruction, and institutional reporting. Everything else — protocol video libraries, client-facing reports, automated workout delivery, hardware capture, mandates, certification gating — is common mature structure, variant, or vendor detail. The Type's edge is defined by what centers the product: the evaluation event (here), the person's self-tracked metrics (Fitness Progress Tracker), the client business relationship (Personal Training Management), the organizational training program (Athlete Management System), or the analysis of performance data (Sports Performance Analytics).
