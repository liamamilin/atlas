# Research Notes — Athlete Management System

## Research Goal

Understand what software sits under the directory leaf "Athlete Management System" (§28 Sports, Fitness & Recreation): what its core objects are, who plans and who consumes, how the plan→deliver→collect→review→adjust loop works, and where the boundary lies against the sibling leaf Athlete Injury / Availability Management (joint review was flagged when that leaf was processed), Sports Performance Analytics, Team Management Application, S&C programming tools, and AI Fitness Coach.

## Initial Boundary (hypothesis before research)

- Hypothesis: AMS is the organizational "system of record" for a defined athlete population's preparation and welfare — roster + training programming + longitudinal per-athlete data (readiness, testing, load) + coordination across specialist staff roles; the medical/injury slice is usually embedded but is the sibling leaf's concern.
- Likely neighbors: Athlete Injury / Availability Management (medical slice, sibling), Sports Performance Analytics (insight layer), Team Management Application (team/event-centered), Sports Coaching Platform, S&C programming tools (no dedicated leaf), AI Fitness Coach (individual), School/College Athletics Management (administrative).
- Key uncertainties: (1) whether "programming" is a defining invariant or just the common center of gravity; (2) how vendors' inconsistent use of "AMS" (management vs monitoring; platform vs solution vs add-on) affects the definition; (3) whether the medical module is definitional for AMS or optional.

## Research Questions

1. What objects exist? (athlete, roster/team/group, program/session/workout, drill/exercise, wellness/RPE submission, testing result, load data, availability status, development plan)
2. Who plans, who executes, who reviews? What roles exist (S&C, performance staff, coaches, medical, nutrition, sport scientists)?
3. How does the daily loop work: plan → assign → execute/collect → review → adjust?
4. What accumulates per athlete over time, and what surfaces are used to review it?
5. What rules matter (role-based visibility, medical privacy wall, alerts, consent/compliance)?
6. Where is the boundary vs the sibling injury/availability leaf, analytics platforms, team management apps, and S&C programming tools?

## Representative Products

| Product | Segment | Philosophy | Why sampled |
|---|---|---|---|
| Teamworks — AMS (formerly Smartabase) | collegiate (D I/II/III, NAIA), pro, Olympic/NGB, military & tactical | configurable no-code platform; flagship use of the exact term "Athlete Management System" | the term's flagship; shows platform-first packaging with S&C/Nutrition/EMR as sibling products |
| Kitman Labs — iP: Performance Optimization ("Beyond an AMS") | elite pro clubs/leagues, collegiate | enterprise intelligence platform; AMS-like solution beside Performance Medicine and Coaching & Development solutions | richest documented programming/readiness machinery; shows AMS as one solution on a broader platform |
| TeamBuildr — Strength + AMS add-on | high schools/PE, colleges, pro, gyms, tactical | S&C programming-first; AMS sold as a paid "sport-science layer" add-on | programming-first pole at the school/college tier; shows the market packaging the readiness layer as an add-on |
| Catapult — Athlete Monitoring (Vector) | elite teams, wearable-first | load/wearable monitoring platform with injury tracking | boundary data point: monitoring-first products share roster + longitudinal data but lack the programming loop |

Rejected/adjusted samples:
- AthleteMonitoring.com — intended as availability-first standalone sample; root page returned empty again (2026-09-06; also unreachable during the sibling leaf's research). Dropped per source-access rule; recorded as sample limitation.
- Kinduct (kinduct.com) — long marketed under the "Athlete Management System" category; transport error on fetch (2026-09-06). Dropped after one attempt per network rule.
- Smartabase — brand redirects to Teamworks AMS after acquisition; treated as Teamworks AMS.

Reused sibling evidence (same research date, Layer A, recorded in research/athlete-injury-availability-management.md): Teamworks Sports EMR, Kitman Performance Medicine, Healthy Roster, Catapult Athlete Monitoring. Used here for boundary analysis and the medical-module question, not as primary AMS samples.

## Sources

All fetched 2026-09-06 (Layer A unless noted):

- Teamworks — AMS: https://www.teamworks.com/ams/ (fetched directly this session; sibling fetched via smartabase.com redirect)
- Kitman Labs — Performance Optimization: https://www.kitmanlabs.com/platform/performance-optimization/ (page title: "Athlete Monitoring System (AMS) - Performance Optimization"; nav label "Performance Optimization - Beyond an AMS")
- TeamBuildr — homepage + FAQ: https://teambuildr.com/
- Catapult — Athlete Monitoring solution: https://www.catapult.com/solutions/athlete-monitoring (via sibling research notes)
- Teamworks — Sports EMR: https://www.teamworks.com/sports-emr/ (via sibling research notes)
- Kitman Labs — Performance Medicine: https://www.kitmanlabs.com/platform/performance-medicine/ (via sibling research notes)
- Healthy Roster: https://www.healthyroster.com/ (via sibling research notes)

Limitations:
- No vendor help-center article describing exact program-builder mechanics, readiness-indicator vocabularies, or role models was reachable; these are described conceptually.
- AthleteMonitoring (availability-first standalone) and Kinduct unreachable → the standalone availability-first pole and one long-standing category vendor are under-represented; assertions about market packaging rely on the sampled products plus sibling evidence.
- TeamBuildr evidence is from its marketing homepage/FAQ (including its own FAQ definitions); no help-center article was fetched. Its structural claims (Strength vs AMS add-on split) are the vendor's own packaging statements.

## Product Observations

### Teamworks — AMS (formerly Smartabase)

Key observations (Layer A, this session + sibling):

- Positioning: "A 360° View of Your Athletes — An Athlete Management System for integrated performance teams"; "helps integrated and multidisciplinary sports performance teams deliver personalized and unified support to elite athletes. By centralizing data and providing a timely and holistic view of individual players and teams, performance leaders and specialists have the complete context needed to make decisions."
- Three value props: (1) Improve Athlete Availability & Readiness — "Centralize and analyze load, testing, nutrition, and survey data to create personalized programs"; (2) Mitigate & Manage Injuries — "Combine performance and medical data… identify athletes at risk of injury or in the return-to-play process"; (3) Develop Talent — "Create data-informed Individual Development Plans based on your athletes' strengths and weaknesses."
- Featured capabilities: Centralize Your Data (integrations with wearables/performance tech — vendor claims "100+", API + R analytics package, bulk upload, custom digital forms for manual capture); Visualize Your Metrics (dashboard builder, permissions-based views, third-party analytics integration); Flexibility (no-code platform; configurable forms, workflows, calculations, dashboards; automated notifications and alerts; "sophisticated org, group, and role structures"); security (robust permissions, ISO 27001, SOC 2 Type II, HIPAA compliant).
- Record vocabulary shown on the page: Incident, Treatment, RTP Protocol, Encounter Note, Injury Surveillance – EMR, Return to Play Tracker, Weight Tracking, Load Monitoring, Performance Testing, Game Report, Post-Session Report → the medical vocabulary ships inside the AMS product as record types.
- Ecosystem: roster sync with Teamworks OSS ("single, accurate source of truth"); "A Unified Performance Ecosystem — Break down silos by integrating High Performance with Nutrition, S&C, and EMR. Unify your data to align Medical, Performance, and Coaching staff around readiness, injury risk, and return-to-play"; unified mobile app across products; multi-language support.
- Segments: professional sports, collegiate (D I/II/III, 2-year, NAIA), Olympic & NGBs, military & tactical.

### Kitman Labs — iP: Performance Optimization ("Beyond an AMS")

Key observations (Layer A, this session):

- Page header literally reads "ATHLETE MONITORING SYSTEM (AMS). Performance optimization" while the nav labels it "Performance Optimization - Beyond an AMS — Plan and adapt training to improve outcomes" → naming hazard: the same vendor uses "AMS" for both "Athlete Management System" and "Athlete Monitoring System", and positions this solution as beyond an AMS.
- Framing: "Combine performance data – including game, training, gym, physical testing and more – with your medical data for a total assessment of where your athletes are now, where they've come from and where they need to be."
- Core capabilities (Layer A):
  - Centralized Performance & Wellness Dashboard — "Unify training, wellness, and recovery data in one view to monitor trends, track progress"
  - Advanced Metric Management & Monitoring — "Collect and configure key performance metrics to track gym outputs, physical data, and trends, supporting individualized plans"
  - Self-Service Reporting & Performance Analysis — "analyze training load, physical performance, wellness trends, and response to programming. Track progress over time, compare across units"
  - Session Planning & Workload Management — "Plan and adapt training sessions based on athlete readiness, workload data, and performance goals. Align with team availability, monitor completion"
  - Mobile Engagement — Player App (log wellness and RPE, view schedules, get feedback); Coach App (check player status, receive alerts, communicate)
  - Training & Participation Management — "Plan and manage training, recovery, and games. Track participation and workload to understand availability"
  - Drill Library & Readiness — "centralized drill library to design sessions that match athlete workload and readiness"
  - Daily Player Status — "Using key metrics like workload, recovery, and wellness, get a real-time snapshot of each athlete's readiness. Identify who needs attention"
  - Wellness & RPE Monitoring — "self-reported wellness and RPE data via mobile or kiosk"
  - Player Engagement & Feedback — athletes "view personal profiles, receive feedback, and log subjective data"
  - Assessments & Benchmarking — "quantitative and qualitative assessments from performance, coaching, and medical staff. Benchmark individual and group development using structured ratings, reviews, and test results"
  - Player Profiling & Availability Analysis — "Track athlete availability due to injury, illness, or time off. Analyze injury burden"
  - Centralized Calendar & Scheduling — "training, gym, recovery, and team activities in one shared calendar"
  - Group Reporting & Multi-Team Analytics — "insights across multiple teams, age groups, or cohorts"
  - Game Participation & Performance Logging — "player minutes by game and position, including contextual indicators such as age group adjustments and substitutions"
  - Forms & Data Collection — "mobile, kiosk, or web"
- Add-ons: API for extracting training/performance data; Growth & Maturation Aware Training (maturity-adjusted norms for youth academies); Risk Advisor (ML injury-risk, attached to Performance Medicine, "maximize the impact… by enabling Performance Optimization" to widen exposure data).
- Platform context: iP Core (operations & administration — shared schedules, communication & coordination), My iP (reporting), Integrations, plus sibling solutions Performance Medicine, Coaching & Development, League Operations, Concussion Management, Operations & Pathway Management.

### TeamBuildr — Strength + AMS add-on

Key observations (Layer A, this session):

- Product split (vendor's own FAQ): "four products: Strength (workout programming and athlete management), AMS (the athlete management system add-on for pain, soreness, and load monitoring), OS (gym management and member operations), and Practice (practice planning for sport coaches)."
- "What's the difference between TeamBuildr Strength, AMS and OS? Strength is the workout programming and athlete tracking platform — the daily tool for strength and conditioning coaches. AMS is a paid add-on to Strength that adds sport-science layer tools (pain mapping, wellness, readiness, load monitoring)."
- AMS add-on description: "adds athlete management system tools: track KPI's, map pain and soreness, view prescribed versus completed volume and more. Used by Johns Hopkins University, Elon University, and Lockeroom to correlate subjective athlete data with weight room training volume."
- Strength platform: "build custom periodized programs on a calendar or dateless view. Athletes can log data through the free mobile app or weight room tablet view. All data can be viewed or exported through TeamBuildr's 16 reports."
- Sport-science tools: "TeamBuildr Strength provides dashboards and reports that monitor performance progress, wellness, injuries, and habit tracking. TeamBuildr AMS offers deeper insights by identifying areas of pain, soreness, and overall wellness, and compares these metrics against objective data such as training volume and repetitions completed."
- Segments: professional (NBA/NFL/NWSL clubs named), college athletic departments, high schools & PE, private gyms, tactical (Air Force units, fire departments).
- Compliance badges: GDPR, COPPA, CSPC, HIPAA, FERPA, and others. Pricing tiers exist (Silver ~50 athletes to Platinum Pro ~1000 athletes) — pricing detail kept out of the final document.
- AI posture: "Built to Work With Coaches – Not Replace Them… use AI to expand the reach, impact, and opportunity of the coaching profession."

### Catapult — Athlete Monitoring (Vector) [boundary data point, sibling Layer A]

- Wearable-based athlete monitoring: load/GPS/heart-rate data as the center of gravity; "track injuries and recovery"; "centralize training and performance… in one central hub"; communication between coaches, athletes, support staff.
- No evidence of training-program planning/assignment as a managed object → monitoring-first products share the roster + longitudinal athlete data but lack the programming loop. Boundary, not a primary AMS sample.

## Cross-product Comparison

| Aspect | Teamworks AMS | Kitman Performance Optimization | TeamBuildr Strength + AMS | Catapult Athlete Monitoring |
|---|---|---|---|---|
| Organizational roster | org/group/role structures; OSS roster sync | squads/teams/age groups; multi-team analytics | teams/athletes/groups (5 segments) | athlete groups |
| Program planning & assignment | "personalized programs"; S&C sibling product | Session Planning & Workload Mgmt; Drill Library; calendar | periodized programs, calendar or dateless view; tablet/mobile delivery | not evidenced |
| Athlete execution & logging | custom digital forms; unified mobile app | Player App logs wellness/RPE; completion monitoring | athlete logging via free mobile app / weight-room tablet | device-generated data |
| Athlete-reported status | survey data | Wellness & RPE Monitoring (mobile/kiosk); Forms & Data Collection | pain/soreness mapping, wellness (AMS add-on) | — |
| Readiness/daily status | availability & readiness value prop; dashboards | Daily Player Status (workload/recovery/wellness) | readiness (AMS add-on) | load insights |
| Prescribed vs completed | implied by program value prop | "monitor completion"; "response to programming" | "prescribed versus completed volume" | — |
| Testing & benchmarking | Performance Testing record type | Assessments & Benchmarking; structured ratings | maxes tracking; reports | — |
| Load/monitoring data | Load Monitoring record type; integrations | workload data; Advanced Metric Management | load monitoring (AMS add-on) | core (GPS/LPS/HR) |
| Medical/injury module | Incident/Treatment/RTP/Encounter Note record types; EMR sibling product | availability analysis; medical data combined; Performance Medicine sibling solution | injuries mentioned in Strength dashboards; no medical module in AMS add-on | injury/recovery tracking |
| Development planning | Individual Development Plans ("Develop Talent") | benchmarking vs norms; Growth & Maturation add-on | progress reports | — |
| Reporting/analytics | dashboard builder; permissions-based views | self-service reporting; group/multi-team analytics | 16 reports; dashboards | analytics |
| Calendar/scheduling | — (in ecosystem) | Centralized Calendar & Scheduling | calendar view for programs | — |
| Alerts | automated notifications and alerts | Coach App alerts | — | — |
| Integrations/API | 100+ integrations (vendor claim); API + R package | Integrations; API add-on | — | device ecosystem |
| Compliance posture | ISO 27001, SOC 2, HIPAA | security/compliance page | GDPR/COPPA/HIPAA/FERPA badges | — |
| Configurability | no-code forms/workflows/calculations/dashboards | configurable metrics; Logic Builder (Medicine) | fixed product + add-ons | configurable groups |

## Canonical Model (Layer C synthesis)

L0 — Defining Invariant (smallest structure without which the Type is unrecognizable):

1. **Organizational athlete roster** — identified athletes managed as members of teams/programs within one organization. Without the organizational container there is no one to manage (the product becomes an individual training app).
2. **Training/development program as managed work** — the system plans, assigns, and tracks structured training or development work (programs, sessions, workouts) for athletes and groups over time. Without this the product is a monitoring platform, an analytics dashboard, or a medical record — not an AMS.
3. **Longitudinal per-athlete preparation record feeding a staff review/adjust loop** — data about each athlete's preparation and condition (completed work, athlete-reported status, testing/monitoring results — at least some of these) accumulates over time against the athlete, persists across sessions and seasons, and is surfaced to staff who review and adjust that athlete's preparation. Without the accumulating record and the review loop, the product is a scheduling/communication tool.

The defining workflow is the loop these three imply: plan → assign/deliver → execute/collect → review → adjust.

Historical check (§24): paper-era equivalents — a performance director's binder holding the squad roster, the season/periodization plan, and one file per athlete (session logs, test results, notes) — satisfy all three invariants; the review loop happened in weekly staff meetings. Older software-era equivalents (spreadsheets + email) also fit. Modern machinery (athlete apps, wearable pipelines, no-code configurability, ML risk) is not required for the definition. The L0 holds for older, regional, and platform-native implementations.

L1 — Common Mature Structure (cross-product commonality, Layer B):

- Athlete-facing mobile app: receive programs/schedule, log sessions, submit wellness/RPE, receive feedback (Teamworks unified app; Kitman Player App; TeamBuildr free athlete app)
- Athlete-reported status collection: wellness, soreness/pain, RPE questionnaires; configurable forms; sometimes kiosk capture
- Daily readiness/status view: per-athlete snapshot (workload, recovery, wellness; configurable indicators) used to decide who needs attention
- Prescribed-vs-completed comparison as a core review mechanic
- Performance testing & benchmarking: test batteries, structured ratings/reviews, norms, progress over time
- Load/session monitoring: training load data, metric management
- Dashboards & reporting: per-athlete and squad/group level; self-service builders; multi-team analytics
- Calendar/scheduling of training, gym, recovery, team activities
- Alerts/notifications: thresholds, status changes, missed submissions
- Role-based access and org structures: teams, groups, roles; permissions-based views
- Integrations with wearables/performance tech + API/export
- Development planning: Individual Development Plans, benchmarking against norms/expectations

L2 — Variant / Optional Structure:

- Medical/injury module (the sibling Type embedded): incident/treatment/RTP/encounter records, availability determination, injury surveillance — present in elite-tier platforms (Teamworks record vocabulary; Kitman medical-data combination; Teamworks sells Sports EMR as a sibling product) but absent from the S&C-first pole (TeamBuildr AMS add-on has no medical module)
- Nutrition management (Teamworks value prop lists nutrition data; sibling Nutrition product)
- Wearable/device data pipelines (GPS/load) as first-class ingestion
- ML injury-risk prediction (Kitman Risk Advisor add-on)
- Concussion-specific modules (Kitman C3Logix; Teamworks Concussion Assessment)
- Clinical/privacy compliance posture: HIPAA/FERPA/GDPR/COPPA certifications (US school and collegiate contexts)
- No-code configurability of forms/workflows/calculations/dashboards (Teamworks; Kitman Logic Builder)
- Multi-language support (Teamworks)
- League/federation-wide standardization (Kitman League Operations; MLS NEXT account portal)
- Growth & maturation adjustment for youth (Kitman add-on)
- Roster sync with wider club operations platforms (Teamworks OSS)
- Practice planning for sport coaches (TeamBuildr Practice)
- Gym/business management (TeamBuildr OS — arguably a different Type sold by the same vendor)

L3 — Vendor-specific (research notes only):

- Teamworks: "Operating System for Sports™", OSS roster sync, unified mobile app across products, R analytics package, product suite (Hub, Compliance, Academics, GM, Wallet, Recruiting, Scouting…), "military-grade security" phrasing
- Kitman Labs: iP: Intelligence Platform naming, iP Core / My iP, Logic Builder, Risk Advisor, C3Logix, Growth & Maturation Aware Training, MLS NEXT registration portal, "Beyond an AMS" positioning
- TeamBuildr: Strength/AMS/OS/Practice product split, 16 reports, pricing tiers ($90–$280/mo bands by athlete count), Locker Room education marketplace, "Built to Work With Coaches – Not Replace Them" AI posture
- Catapult: Vector device line, LPS indoor tracking

## Vendor-specific Findings

- **Naming hazard**: "AMS" expands to both "Athlete Management System" and "Athlete Monitoring System", and vendors apply the acronym to whole platforms (Teamworks), solutions within platforms (Kitman Performance Optimization), add-on layers (TeamBuildr AMS), and monitoring systems (Kitman's own page title; Catapult's category). The canonical Type must be defined by the recognizable whole (roster + programming + longitudinal record + review loop), not by the label.
- **Packaging variance is structural, not incidental**: the same concern ships as (a) a standalone platform (Teamworks AMS), (b) one solution on a multi-solution platform (Kitman), (c) a paid add-on to a programming tool (TeamBuildr), and (d) a monitoring platform adjacent to the Type (Catapult). Packaging is L2; the underlying loop is stable.
- Teamworks' medical record vocabulary (Incident, Treatment, RTP Protocol, Encounter Note) ships inside the AMS product — direct evidence that the sibling Type's core is usually embedded in AMS products rather than sold only separately.
- TeamBuildr's own FAQ distinguishes "workout programming and athlete management" (Strength) from the "sport-science layer" (AMS add-on) — evidence that the market treats programming and readiness-monitoring as separable layers, with the "AMS" label attaching to the readiness layer in that packaging.

## Boundary Findings

1. **vs Athlete Injury / Availability Management (sibling leaf — joint review resolution)**: The sibling's L0 is roster + injury/illness record lifecycle + per-athlete availability state surfaced for participation decisions. AMS's L0 is roster + training/development program as managed work + longitudinal preparation record feeding the review/adjust loop. The two Types share the roster and the athlete-reported input layer, and AMS products usually embed the medical slice as a module. Directional tests: remove programming from an AMS → the remainder is the sibling Type (or a monitoring platform); remove injury/availability machinery from an AMS → still an AMS (Teamworks lists injury mitigation as one of three value props; TeamBuildr's AMS add-on has none at all). Both leaves are definable; no taxonomy change. This resolves the joint review flagged in research/athlete-injury-availability-management.md §Boundary Findings.
2. **vs Sports Performance Analytics**: analytics platforms provide the insight layer over performance data but do not own the athlete roster's preparation loop or program delivery; AMS products embed reporting (and sell analytics separately — Kitman Custom Analytics, Teamworks Intelligence), evidence that analytics is a separable concern. Remove program delivery and the managed roster → analytics platform.
3. **vs Team Management Application**: team/event-centered (roster, schedule, communication for games/practices, often amateur) vs athlete-preparation-centered (longitudinal development data, programming, readiness). A team app may display availability but does not manage preparation as work.
4. **vs S&C programming tools (no dedicated directory leaf)**: programming-only tools (TeamBuildr Strength pole) are the programming slice of an AMS; the market packages the readiness layer as an add-on to them. The directory has no S&C leaf; these products are documented under this leaf. Taxonomy observation, no change proposed.
5. **vs monitoring-first platforms (Catapult pole)**: share roster + longitudinal athlete data but lack the programming loop; some vendors label them "AMS" too (naming hazard). They sit at the boundary of this Type and Sports Performance Analytics.
6. **vs AI Fitness Coach**: individual trainee + system-composed programming vs organizational roster + staff-composed programming. The AI coach's L0 (already documented) has no organizational container.
7. **vs School/College Athletics Management**: administrative department operations (eligibility, compliance, event operations) vs athlete preparation; Teamworks sells Compliance/Academics as separate products — evidence of separability.
8. **vs Sports Eligibility Management**: administrative right to compete vs preparation management; different record types and decision owners.
9. **Structural analog (not a confusion risk)**: Workforce Management / L&D in HR — organization + people + assigned development work + tracked completion + readiness for duty. Same abstract shape, different domain semantics.

## Uncertainties

- Exact program-builder mechanics (periodization models, exercise-library structure, progression rules) were not evidenced from help-center documentation; described conceptually.
- Whether "development planning" (IDPs) is L1 or L2: named by Teamworks as a value prop and approached by Kitman via benchmarking; treated as L1 with cautious wording since both flagship products show it, but it may be a packaging emphasis rather than universal structure.
- The standalone availability-first / monitoring-first pole (AthleteMonitoring, Kinduct) is under-represented due to unreachable sources; assertions about the monitoring boundary rely on Catapult plus vendor naming usage.
- Whether nutrition is L1 or L2: named in Teamworks' value prop and as a sibling product; not evidenced in TeamBuildr/Kitman core lists → L2.
- TeamBuildr's "injuries" mention in Strength dashboards is marketing-level; no medical-module evidence → medical module treated as absent in that pole.

## Final Synthesis

An Athlete Management System is organizational sports software whose defining core is: a roster of identified athletes managed as members of teams/programs; training and development programs planned, assigned, and tracked as work; and a longitudinal per-athlete preparation record — fed by completed work, athlete-reported status, and testing/monitoring data — that staff use to review and adjust each athlete's preparation. Around that core, mature products add athlete-facing mobile apps, wellness/RPE collection, daily readiness views, prescribed-vs-completed comparison, testing and benchmarking, dashboards and multi-team reporting, calendars, alerts, role-based access, and wearable/API integrations. The market implements the core as standalone platforms, as solutions inside broader performance platforms, and as readiness add-ons to S&C programming tools; the medical/injury slice (the sibling Athlete Injury / Availability Management Type) usually ships inside elite-tier AMS products as an embedded module, and nutrition, wearables, ML risk prediction, concussion protocols, compliance certifications, and league-wide standardization are variant capabilities, not definitions. The acronym "AMS" is applied inconsistently across management platforms, monitoring systems, and add-ons; the Type is defined by the recognizable loop (plan → deliver → collect → review → adjust), not by the label.
