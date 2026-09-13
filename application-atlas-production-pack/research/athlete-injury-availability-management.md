# Research Notes — Athlete Injury / Availability Management

## Research Goal

Understand what software sits under the directory leaf "Athlete Injury / Availability Management" (§28 Sports, Fitness & Recreation): what its core objects are, who records and who consumes, how an injury moves through the system, how availability is determined and surfaced, and where the boundary lies against Athlete Management System, sports-medicine EMR products, Sports Eligibility Management, and Team Management Application.

## Initial Boundary (hypothesis before research)

- Hypothesis: this is the medical/injury slice of athlete-health software — organizations record injuries/illnesses per athlete and maintain a per-athlete availability state that coaches use for participation decisions.
- Likely neighbors: Athlete Management System (broader: training programming, load, nutrition), Sports EMR / clinical documentation (documentation-first), Sports Eligibility Management (administrative right to compete), Team Management Application (roster/schedule/comms).
- Key uncertainty: whether "availability" is a first-class object in real products or just a byproduct of injury records; whether standalone availability-first products exist.

## Research Questions

1. What objects exist? (athlete, injury/illness record, treatment, rehab, return-to-play, availability status, questionnaires, screenings)
2. How does an injury enter the system and move through its lifecycle?
3. How is availability determined, updated, and surfaced to non-medical staff?
4. Who records vs who consumes? What roles and privacy rules govern visibility?
5. What interfaces exist (medical profile, status board, athlete app, reports)?
6. Where is the boundary vs AMS / sports EMR / eligibility management / team management?

## Representative Products

| Product | Segment | Philosophy | Why sampled |
|---|---|---|---|
| Kitman Labs — iP: Intelligence Platform, Performance Medicine solution | elite pro clubs/leagues, collegiate | enterprise medical + performance platform; "more than an EMR" | richest documented injury-lifecycle + availability machinery |
| Teamworks — AMS (formerly Smartabase) + Sports EMR | collegiate/pro/Olympic/military | configurable no-code AMS + separate sports EMR product | shows both the AMS packaging and the EMR packaging of the same concern |
| Healthy Roster | US high schools, colleges, clinics, industrial AT | mobile-first sports-medicine EMR for athletic trainers | clinical-documentation-first pole; school/parent communication context |
| Catapult — Athlete Monitoring (Vector) | elite teams, wearable-first | load/wearable monitoring platform with injury tracking | boundary data point: load-first products still carry injury/recovery tracking |

Rejected/adjusted samples:
- AthleteMonitoring.com (athlete-monitoring.com) — intended as the availability-first standalone sample; root and /features/ pages returned empty twice (2026-09-06). Dropped per source-access rule. Consequence: the sample skews toward platform/EMR packaging; standalone availability-first products are under-represented (recorded in Uncertainties).
- Smartabase — brand now redirects to Teamworks AMS after acquisition; treated as Teamworks AMS.

## Sources

All fetched 2026-09-06 (Layer A unless noted):

- Kitman Labs — homepage: https://www.kitmanlabs.com/
- Kitman Labs — Performance Medicine: https://www.kitmanlabs.com/platform/performance-medicine/
- Kitman Labs — blog "Optimize Injury Management and Recovery with Performance Medicine": https://www.kitmanlabs.com/blog/optimize-injury-management-and-recovery-with-performance-medicine/
- Teamworks — AMS: https://www.teamworks.com/ams/ (fetched via smartabase.com redirect)
- Teamworks — Sports EMR: https://www.teamworks.com/sports-emr/
- Healthy Roster — homepage: https://www.healthyroster.com/
- Healthy Roster — EMR platform: https://www.healthyroster.com/our-platform
- Healthy Roster — Knowledge Base root + EMR Platform category: https://healthyroster.helpjuice.com/ , https://healthyroster.helpjuice.com/en_US/emr-platform
- Catapult — Athlete Monitoring solution: https://www.catapult.com/solutions/athlete-monitoring

Limitations:
- No vendor help-center article describing the exact availability-status vocabulary (e.g., named states like "Available / Modified / Unavailable") was reachable for any product. Status vocabularies are therefore described conceptually, without asserting specific state names.
- AthleteMonitoring unreachable (see above).
- Healthy Roster help-center article bodies beyond category pages were not fetched; its RTP capability is inferred from product positioning only and is marked accordingly.

## Product Observations

### Kitman Labs — iP: Intelligence Platform / Performance Medicine

Key observations (Layer A):

- Positioning: "Performance Medicine — More than an EMR: Manage athlete health, medical workflows, & return to play." Rugby page: "Manage player welfare, workload, & availability in one system."
- Centralized Medical Hub: "Centralize all current and historical medical data—including injuries, illnesses, treatments, diagnostics, and notes—in a secure, compliant, and easily accessible hub."
- Injury Lifecycle & Recovery Management: "Track injuries from onset through rehabilitation with detailed documentation, diagnostics, and progression monitoring to ensure safe and efficient return-to-play decisions."
- Treatment & Rehabilitation Planning: individualized care programs and preventative maintenance plans.
- Exposure & Availability Monitoring: "Monitor player availability due to injury, illness, or time off, and analyze injury burden to understand the true impact on game and training participation."
- Daily Player Status: "Using configurable indicators like recovery, wellness, or availability, staff can see each athlete's readiness at a glance… timely decisions on training modifications, treatment plans, or player clearance."
- Daily Status Report Export: "generate and share a secure daily status report with non-medical staff, summarizing athlete readiness and restrictions, while protecting sensitive health information." → structural privacy rule: medical detail restricted, status summary shared.
- Player Profile & Status Monitoring: "comprehensive, longitudinal view of each player's current medical status, injury history, assessments, alerts, diagnostics, and care plans."
- Configurable Meta Data & Injury Context: "Customize and standardize the data captured around each injury—including type, mechanism, contributing factors, and situational details."
- Self-Service Reporting & Injury Surveillance: "injury incidence, re-injury rates, time-loss trends, and treatment outcomes… patterns across teams or seasons."
- Logic Builder: "conditional, contextual data collection and built-in consent management across medical workflows from injury surveillance to ACL tracking."
- Mobile Engagement: Player App (athletes submit wellness, symptoms, treatment feedback); Coach App (staff access player status and alerts).
- Centralized Calendar & Scheduling: treatments, screenings, diagnostics, follow-ups.
- Screening & Testing Management: concussion baselines, clinical evaluations, test protocols with alerts and historical tracking.
- Player Wellness Tracking: sleep, stress, nutrition; forms for daily wellness, pain scores, symptom tracking.
- Medication & Stock Management; TUE tracking; e-prescribe; healthcare-systems integration; e-file/e-fax (add-ons).
- Risk Advisor (add-on): ML injury-risk from injury history + exposure data (minutes, RPE).
- C3Logix (add-on): SCAT6/SCOAT6 concussion assessment, baseline → return to play.
- Blog (injury lifecycle): lifecycle = prevention → early identification → treatment → rehabilitation → recovery → return to play; "medical teams can quickly gauge availability or modifications needed and then share these findings… to streamline training and game decisions"; milestone-based insights; readiness monitoring (fatigue, soreness, joint health).

### Teamworks — AMS (formerly Smartabase) and Sports EMR

Key observations (Layer A):

- AMS positioning: "An Athlete Management System for integrated performance teams."
- "Improve Athlete Availability & Readiness: Centralize and analyze load, testing, nutrition, and survey data to create personalized programs that help each athlete be available and ready to perform."
- "Mitigate & Manage Injuries: Combine performance and medical data to easily identify athletes at risk of injury or in the return-to-play process. Foster collaboration to speed recovery."
- Dashboard/record vocabulary shown on the AMS page: Incident, Treatment, RTP Protocol, Encounter Note, Injury Surveillance – EMR, Return to Play Tracker, Weight Tracking, Load Monitoring, Performance Testing, Game Report, Post-Session Report.
- Platform traits: no-code configurable forms/workflows/calculations/dashboards; "sophisticated org, group, and role structures"; automated notifications and alerts; 100+ wearable/perf-tech integrations; API + R package.
- Security: ISO 27001, SOC 2 Type II, HIPAA compliant; "robust permissions."
- Sports EMR (separate product page): "modernize medical documentation, improve injury visibility… protect athlete health and maximize availability."
  - "Improve Athlete Availability: Identify injury trends early and implement targeted prevention programs with centralized documentation, dynamic dashboards, and real-time reporting."
  - "Gain Complete Visibility: Access a unified 360° athlete view with injury notes, encounters, forms, documents, and availability status all in one place."
  - Key features: Concussion Assessment, Document Upload, Injury / Illness Record & Reporting, Medical Screening, Insurance Claim Form, Insurance Questionnaire, Return to Play Tracker.
  - "Unify your data to align Medical, Performance, and Coaching staff around readiness, injury risk, and return-to-play."
- Roster: "Sync athlete profiles directly with Teamworks OSS to maintain a single, accurate source of truth."

### Healthy Roster

Key observations (Layer A):

- Positioning: "the leading sports medicine EMR for Athletic Trainers"; "Where Athletic Trainers go to Document. Protect. Educate."; "documenting injuries, concussion testing… super easy."
- Documentation: "Faster injury and treatment logging"; injury timeline visualization; customizable note templates (boilerplates, SOAP notes, rehab exercises); mobile-first ("document on the field or in the training room").
- Communication: secure chat with athletes, parents, coaches, physicians "without sacrificing your privacy and PHI security"; high-school setting: "Document anywhere and easily update coaches and parents."
- Forms: digital custom forms/templates; track missing paperwork.
- Scheduling: athletes self-book appointments; ATs manage availability calendars (of the AT, for care appointments — care scheduling, not game availability).
- Reporting: "detailed injury breakdowns for schools or employers… graphical representations of what injuries occurred and to which location (or team)… identify trends in a particular sport"; encounter/referral metrics.
- Compliance: HIPAA + FERPA compliant; SOC 2 Type II; role-based access controls.
- Settings/segments: High School, College, Outreach (clinic ATs serving schools), Industrial AT.
- Integrations: Sway (concussion testing), Epic CareEverywhere, ImPACT, XLNTbrain, FinalForms, Datalys (injury surveillance data exchange).
- Knowledge-base structure: Documentation Overview, Communication & Telehealth, Invitations (patient/primary-user accounts), Reporting & Analytics, Custom Forms & Documents, Self Scheduling; patient/parent/representative walkthroughs; kiosk mode for encounters/treatments.
- Note: RTP not explicitly evidenced on fetched pages; referrals are. Treat Healthy Roster RTP as unverified.

### Catapult — Athlete Monitoring (Vector)

Key observations (Layer A):

- Positioning: wearable-based athlete monitoring ("optimize performance, reduce risk of injury & improve recovery").
- Athlete Monitoring Platform: "INJURY MITIGATION: Utilize our sophisticated tools to track injuries and recovery, minimizing downtime and enhancing athlete welfare."
- "MANAGE WITH EASE: Customize and control athlete data… from individual athletes to entire teams"; "CENTRALIZE TRAINING AND PERFORMANCE… in one central hub"; "ENHANCE COMMUNICATION between coaches, athletes, and support staff."
- Primary center of gravity is load/GPS/heart-rate data; injury tracking is a supporting capability. → boundary data point: load-first monitoring platforms include injury/recovery tracking but are not defined by it.

## Cross-product Comparison

| Aspect | Kitman Labs Performance Medicine | Teamworks AMS / Sports EMR | Healthy Roster | Catapult Athlete Monitoring |
|---|---|---|---|---|
| Organizational athlete roster | Player profiles, longitudinal | org/group/role structures; roster sync with OSS | patient/athlete records per org | athlete groups |
| Injury/illness record | injuries, illnesses, treatments, diagnostics, notes; configurable injury context (type/mechanism/factors) | Incident; Injury/Illness Record & Reporting | injury documentation + injury timeline + injury logs | "track injuries and recovery" |
| Treatment/rehab documentation | Treatment & Rehabilitation Planning; medication & stock | Treatment; Encounter Note | treatment logging; SOAP notes; rehab exercises | recovery tracking |
| Return-to-play | RTP decisions; milestone-based progression | RTP Protocol; Return to Play Tracker | not evidenced on fetched pages (referrals only) | "minimizing downtime" (implicit) |
| Availability as object | Exposure & Availability Monitoring; Daily Player Status (configurable indicators) | availability status in 360° view; "Improve Athlete Availability & Readiness" | coach/parent updates (not an explicit availability board) | not explicit |
| Athlete-reported input | Player App: wellness, symptoms, treatment feedback | custom digital forms; surveys | patient/primary-user accounts; forms; surveys | device data (wearable) |
| Surveillance/reporting | incidence, re-injury, time-loss trends; self-service dashboards | Injury Surveillance – EMR; dashboard builder | injury breakdowns by team/sport; trends | injury-mitigation analytics |
| Screening/testing | concussion baselines, screenings, alerts | Concussion Assessment; Medical Screening | concussion testing (Sway integration) | — |
| Privacy posture | secure daily status report protecting sensitive health info; consent management | robust permissions; HIPAA; SOC 2; ISO 27001 | HIPAA + FERPA; role-based access; secure chat | — |
| Scheduling | medical calendar (treatments, screenings, follow-ups) | — | care appointment scheduling; self-scheduling | — |
| Load/wearable integration | via integrations (WHOOP etc.) | 100+ integrations; API | — | core (GPS/LPS/HR wearables) |
| ML risk prediction | Risk Advisor add-on | — (configurable calculations) | — | AI algorithms (load insights) |

## Canonical Model (Layer C synthesis)

L0 — Defining Invariant (smallest structure without which the Type is unrecognizable):

1. **Organizational athlete roster** — identified athletes as members of a team/organization managed in the system. Availability only means something relative to a squad; without the roster there is nothing to be available *for*.
2. **Injury/illness record attached to an athlete** — a dated, documented health event (injury or illness) that belongs to one athlete and carries its own lifecycle (onset → assessment → treatment → progression → closure/return).
3. **Per-athlete availability state, changing over time, surfaced for participation decisions** — the system maintains, for each athlete, whether they can train/compete fully, in a modified way, or not at all, and makes that state visible to the people deciding participation.

If you remove the injury/medical record and the availability determination, keeping only training programming and load, you have a training/workload tool (part of AMS) — not this Type. If you remove the roster/organizational context, you have a personal health record or a clinical chart — not this Type.

Historical check (§24): paper-era equivalents — an athletic trainer's injury log card per athlete plus a daily availability list handed to the coach — satisfy all three invariants. Modern machinery (questionnaires, wearables, dashboards, consent workflows) is not required for the definition. The L0 holds for older, regional, and platform-native implementations.

L1 — Common Mature Structure (cross-product commonality, Layer B):

- Treatment/rehabilitation documentation (encounter notes, SOAP-style notes, interventions, rehab plans)
- Return-to-play progression: staged protocols, milestones, clearance decisions (explicit in Kitman, Teamworks; not evidenced in Healthy Roster)
- Athlete-reported input: wellness/symptom questionnaires, custom forms, surveys via athlete-facing app/account
- Injury surveillance reporting: incidence, time-loss, burden, trends by team/sport/injury type/season
- Role-based access separating restricted medical detail from coach-facing status summaries (Kitman daily status report; Teamworks permissions; Healthy Roster role-based access + secure chat)
- Medical calendar/scheduling of treatments, screenings, follow-ups
- Screening/testing records (pre-participation screening, concussion baseline tests)
- Alerts/flags on athlete status
- Mobile surfaces: athlete app for reporting; staff app for field documentation

L2 — Variant / Optional Structure:

- Clinical-compliance pole: HIPAA/FERPA compliance, insurance claim forms, e-prescribe, medication stock, TUE tracking (US AT-EMR pole: Healthy Roster, Teamworks Sports EMR, Kitman add-ons)
- Load/wearable integration feeding availability context (Catapult core; Teamworks/Kitman integrations)
- ML injury-risk prediction (Kitman Risk Advisor; Catapult AI algorithms)
- Concussion-specific protocol modules (baseline + SCAT/SCOAT-style assessment; Kitman C3Logix, Teamworks Concussion Assessment, Healthy Roster/Sway)
- League/federation-wide standardization (Kitman league operations; MLS NEXT)
- Secure messaging/telehealth with parents, physicians, external providers (Healthy Roster; Kitman e-fax/healthcare integration)
- No-code configurability of forms/workflows (Teamworks; Kitman Logic Builder)
- Care-appointment self-scheduling (Healthy Roster)

L3 — Vendor-specific (research notes only):

- Kitman Labs: Logic Builder, Risk Advisor, C3Logix, TUE tracking, Growth & Maturation Informed Care, E-File/E-Fax, Healthcare Systems Integration, Daily Status Report Export as a named feature, My iP dashboards
- Teamworks: Operating System for Sports™, OSS roster sync, unified mobile app across products, PFF/Scouting siblings
- Healthy Roster: Sway integration, CEU continuing-education platform, USCAH training, kiosk mode, Datalys/FinalForms integrations
- Catapult: Vector Pro/Core/One device line, LPS indoor tracking

## Vendor-specific Findings

- Kitman's "Daily Status Report Export… protecting sensitive health information" is the clearest articulation of the medical↔coach information boundary; treat the *pattern* as L1 (all sampled products implement some version) but the named feature as vendor-specific.
- Teamworks sells the same concern twice (AMS module + separate Sports EMR product) — evidence that the market packages this Type both as an AMS module and as a standalone EMR; packaging is L2, not definitional.
- Healthy Roster's continuing-education (CEU) platform is a business-model appendage, unrelated to the Type's core.

## Boundary Findings

1. **vs Athlete Management System (sibling leaf)**: AMS = roster + training programming + load + nutrition + testing + (often) medical. Injury/availability is the medical-availability slice. Evidence: Teamworks AMS lists "Mitigate & Manage Injuries" as one of three value props alongside availability/readiness and talent development; Kitman positions Performance Medicine ("more than an EMR") as a distinct solution from Performance Optimization ("beyond an AMS"). Test: remove training programming/load/nutrition → still this Type; remove injury records + availability → still an AMS. So the two Types overlap on a shared slice; this leaf is definable on its own (roster + injury record + availability state) and is implemented in the market both standalone-ish and as an AMS module. No taxonomy change proposed; flag for joint review when Athlete Management System is processed.
2. **vs Sports EMR / sports-medicine documentation (no dedicated directory leaf; nearest is EHR §22)**: documentation-first products (Healthy Roster, Teamworks Sports EMR) implement the same L0 (roster + injury record + availability/communication) with a documentation-heavy center of gravity; operations-first products (Kitman daily status, Teamworks AMS) implement it with an availability-operations center of gravity. The leaf spans both poles; the directory has no separate sports-EMR leaf, so those products are documented here. Distinction vs generic EHR: EHR serves care delivery/billing for a general patient population; this Type serves participation decisions in an organizational sports context. Remove the team/availability context → generic clinical EMR.
3. **vs Sports Eligibility Management (sibling leaf)**: eligibility = administrative right to compete (registration, academic standing, licensing, insurance paperwork); availability = medical readiness to participate. Different record types, different decision owners (registrar/compliance vs medical staff). Both can gate participation, which makes them easy to confuse; the record semantics differ.
4. **vs Team Management Application**: roster/schedule/communication for teams; no medical records, no health-driven availability states. A team app may *display* availability but does not *derive and manage* it from medical documentation.
5. **vs Sports Performance Analytics**: analytics over performance data; injury surveillance reporting overlaps as a capability, but analytics platforms do not own the medical record or the clearance decision.
6. **Structural analog (not a confusion risk): Leave & Absence Management (§09 HR)** — person + absence record + expected return + restricted medical detail + return-to-work clearance. Same abstract shape, different domain semantics (employment vs sport participation, HR vs medical ownership). Recorded as an observation.

Taxonomy observation: in the current market this functionality is usually *sold* as part of an AMS or a sports EMR; standalone injury/availability-only products exist (e.g., the unreachable AthleteMonitoring) but are a minority. The leaf remains a legitimate, definable Type — analogous to how Leave & Absence Management is definable despite usually shipping inside HRIS suites.

## Uncertainties

- Exact availability-status vocabularies (state names, who may set them, whether coaches can ever set status) were not directly evidenced; described conceptually only.
- Healthy Roster's return-to-play capability: not evidenced on fetched pages; marked unverified.
- AthleteMonitoring (availability-first standalone) unreachable → the "standalone availability-first product" pole is under-represented; assertions about market packaging rely on the sampled four.
- Whether concussion management is L1 or L2: it appeared in 3 of 4 products, but as distinct modules/add-ons rather than core structure → placed in L2.
- Relative weight of "exposure" (participation minutes/sessions) as a first-class object: only Kitman names it explicitly ("Exposure & Availability Monitoring", exposure data in Risk Advisor); treated as L1-leaning-L2, described cautiously.

## Final Synthesis

An Athlete Injury / Availability Management application is organizational sports software whose defining core is: a roster of identified athletes; dated injury/illness records attached to athletes, each with its own lifecycle; and a per-athlete availability state that changes over time and is surfaced to the staff making participation decisions. Around that core, mature products add treatment/rehab documentation, staged return-to-play progression, athlete-reported wellness/symptom input, injury-surveillance reporting, and a role-based privacy wall between restricted medical detail and coach-facing status summaries. The market implements this core both as documentation-first sports-medicine EMRs and as availability-operations modules of broader athlete management platforms; load/wearable integration, concussion protocols, clinical compliance (HIPAA/FERPA, e-prescribe, insurance), and ML risk prediction are variant capabilities, not definitions.
