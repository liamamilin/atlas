# Research Notes — Employee Learning Platform

## Research Goal

Understand what an Employee Learning Platform (workplace/corporate learning software) really is as an Application Type: its defining structure, its standard capabilities, its lifecycle and rules, and its boundaries against neighboring Types (Corporate LMS, education LMS, LXP, Customer Training/Academy Platform, Employee Onboarding Platform, Skills Management Platform).

## Initial Boundary

- Leaf: **Employee Learning Platform** (DIRECTORY §09 HR, Workforce & Talent, line 761).
- Working hypothesis: organization-operated software to deliver, manage, and track employee learning.
- Nearest neighbors suspected up front: **Corporate LMS** (§09 sibling — possible alias), **LMS** (§23, education), **Learning Experience Platform / LXP** (§23), **Customer Training / Academy Platform** (§07), **Employee Onboarding Platform** (§09), **Skills Management Platform** (§09), **eLearning Authoring Tool** (§23), **GxP Training Management** (§22).
- Prior §09 passes already flagged an "experience cluster" (employee-communication / engagement / experience platforms bundle learning as one domain). This leaf is the single-domain learning specialist.

## Research Questions

1. What are the core objects (learner, course, enrollment, completion record, plan, certification)?
2. How does learning reach employees — mandatory assignment vs self-enrollment vs content recommendation?
3. What lifecycle/states do enrollments and completions have? What completion rules exist?
4. Which roles exist and how do permissions shape behavior (delegated admins, managers, instructors)?
5. How do compliance mechanics work (validity periods, re-certification, audit trail)?
6. Is this Type structurally distinct from Corporate LMS, or the same structure under another name?
7. Where does the content come from (authored, imported standards, third-party libraries)?
8. What is the lower bound of the Type (would a content-library product with licenses satisfy it)?

## Representative Products

| Product | Segment / philosophy | Evidence level reached |
|---|---|---|
| **Docebo** | standalone "learning platform", mid-market→enterprise, broad module set | Tier-1 help center, multiple articles (deep) |
| **Absorb LMS** | standalone LMS, SMB/mid-market | Tier-1 help center, multiple articles (deep) |
| **LinkedIn Learning** | content-library-first enterprise learning subscription | Tier-1 help center (Manage Users topic, root) |
| **Cornerstone Learning** | enterprise suite LMS (compliance-heavy; also ships legacy lines Saba, SumTotal) | Help-center root only (positioning level; deep docs 404/JS) |

Rejected/abandoned samples: SAP SuccessFactors Learning (SPA shell), Workday Learning (not attempted after repeated JS/login walls in sibling passes), Skillsoft Percipio (transport errors ×2), Litmos (login wall), TalentLMS (transport error), 360Learning (JS app), Cornerstone deep docs (404).

## Sources

- Docebo Help & Support — https://help.docebo.com (root; Courses and learning plans category; Enrollment statuses; Creating and managing learning plans and certifications; Setting time validity for courses; Compliance category; Users category) — fetched 2026-09-06
- Absorb Help Center — https://support.absorblms.com (root; Absorb LMS Knowledge Base; Course Enrollments section; Enrollment, Completion & Progress) — fetched 2026-09-06
- LinkedIn Learning Help — https://www.linkedin.com/help/learning (root; Manage Users topic a45) — fetched 2026-09-06
- Cornerstone Help Center — https://help.csod.com (root only) — fetched 2026-09-06

## Product A — Docebo (Tier-1, directly observed)

### Key observations

**Object structure (help-center category map):**
- Top-level admin domains: Platform setup, Users, Courses and learning plans, Training material, Content marketplace, Analytics, Compliance, SSO, Integrations, Mobile learning, E-commerce, Communities and social learning, Learning evaluation, AI.
- **Courses**: two delivery families — *e-learning courses* (self-paced) and *ILT courses* (instructor-led, incl. VILT) with **sessions**, locations/classrooms, attendance tracking, session cancel/restore, CSV import of sessions.
- **Course properties**: navigation policy, course player config, course rating, **time validity**, categories, **equivalencies**, additional fields.
- **Course enrollments**: dedicated section — enrollment statuses, enrolling users (manual, CSV), enrollment rules app, enrollment codes.
- **Learning plans and certifications**: "structured sequences of courses (e-learning and ILT)"; two types — *learning plan* (no certification) and *certification* (awards certification on completion); assigned to **users, branches, or groups**; courses marked *mandatory* or *optional* (≥1 mandatory course required to publish); prerequisites with optional unlock intervals; publication status *Published / Under maintenance*; **recalculation of completed enrollments** when the plan structure changes; certifications carry **validity status (valid / expiring / expired)**; certificate issued on completion date of last course.
- **Catalogs** (incl. public catalog) and **channels**; learning programs can be assigned to catalogs (self-enroll or purchase).
- **External training** app: record training taken outside the platform.
- **Users**: creation (incl. self-registration settings), account statuses, **levels/roles/statuses**, CSV import, **branches** (org hierarchy), groups, cohorts, profile merge; **Power Users** = delegated admins with resource-scoped permissions; **My team** = manager surface (courses/learning plans dashboards, skills); **Skills** (with HRIS/talent-platform integration); **Observation checklists** completed by managers.
- **Compliance**: E-signature app, **Audit trail** (event details), accessibility; cookie/privacy/terms dashboards.
- **E-commerce**: sell courses/learning programs (extended enterprise).

**Enrollment statuses (article, directly observed):**
- Course-level: *Enrolled, In progress, Completed, Waiting users / Enrollment to confirm, Suspended, Overbooking*.
- *Enrolled* = enrolled, not started; *In progress* = started material, not complete; *Completed* = e-learning: all **mandatory** training materials completed; ILT: required number of sessions completed.
- Waiting list mechanics: max enrollment quota + waiting list; paid course with pending payment; self-enrollment with *pending administrator approval*; enrollment by a Power User lacking *Can activate enrollments* permission.
- *Suspended*: user can access platform but not the course. *Overbooking*: enrolled but no access (e-learning only, manually set).
- ILT sessions carry their own enrollment statuses (Waiting users, Enrolled, In progress, Completed, Suspended).
- Learning-plan status derived from constituent courses (*Enrolled/Not started, In progress, Completed, Payment pending*); plan completed when all **mandatory** courses completed; completed status cannot revert to in-progress unless structure is updated and recalculated.
- Manual status editing by Power Users with *Enrollment / Edit* permission; **Power Users see only their assigned users**; waiting-list visibility needs a specific permission.

**Time validity (article, directly observed):**
- Course validity period (start date / end date / period, UTC-based), **enrollment validity period** (days from enrollment or first access), **soft deadline** (access continues after end date), learner-level validity overrides (e-learning: learner-level overrides course-level; ILT: course-level governs access, learner dates only drive card labels *Expiration / Overdue / Expired*).
- Stated purposes: "control access to paid courses, encourage timely completion, and meet compliance or legal requirements".

**Roles observed:** Superadmin, Power User (delegated, resource-scoped), Instructor, Manager (My team), Learner. Managers "track progress, provide support" for their teams. Notifications for learners and managers on learning-program events.

**Vendor-specific (L3):** Harmony AI tutor, AgentHub, Companion (in-workflow learning), channels, cohorts, branches terminology, 250-course recommendation for learning programs, legacy "Certification and retraining" app being migrated into "Learning plans and certifications" (BETA at research time).

## Product B — Absorb LMS (Tier-1, directly observed)

### Key observations

**Object structure (knowledge-base map):**
- **Courses** section: Course Administration, Question Banks, **Competencies**, Tags, Ratings, **Course Enrollments**, Lessons.
- **Users** section: Users, **Roles**, **Departments**, **Groups**, **Enrollment Keys**.
- **Reports** (per admin experience version), Dashboards, System Usage, Logins, Search Analytics.
- Surfaces: **Admin Experience**, **Learner Experience**, **Manager Experience** (own KB section incl. roles & permissions, import managers), Reviewer Experience; **Mentorship**; **E-Commerce** (transactions, coupons); Absorb Create (authoring), Absorb Engage, Absorb Analyze, Absorb Skills, Absorb Amplify & Content Hub (content), Aura (AI/UX layer), mobile app.

**Course Enrollments section (article list, directly observed):**
- Enrollment-Level Availability Dates; Scheduled Enrollments; **Creating Enrollment Rules**; **Enrollment Method Legend**; Course Enrollments; **Course Equivalencies**; Learner Un-Enrollment; **Automatic Enrollment Rules**; Enrollment, Completion & Progress; "Enroll Anyone" permission; "Why was a User Re-Enrolled in a Course?"; curriculum un-enrollment; **Re-Enrollment & Re-Certification**; **Enrollment Approval**.

**Enrollment, Completion & Progress (article, directly observed):**
- Progress values: *Not Started, In Progress, Complete, Failed, Not Completed*.
- *Complete* = all **mandatory** content completed (Online Course or Curriculum); for **ILC** (instructor-led class) = attendance marked for all classes.
- *Failed* = assessment lesson failed (if failure allowed at course level, can fail the whole course).
- *Not Completed* = "typically set manually by an Admin".
- ILC attendance values: *Absent* (0%) / *Completed* (100%); scores expected when assessments completed or attendance marked; assessment weighting formula documented.
- Admins manually update completion status via Admin Experience → Users Report → User Enrollments Report → Edit Enrollment.
- Edge case documented: course with no objects auto-completes with 0% progress.

**Vendor-specific (L3):** ILC terminology, Enrollment Keys, Aura, Create/Engage/Amplify/Skills product names, curriculum object, "Enroll Anyone" permission.

## Product C — LinkedIn Learning (Tier-1, directly observed)

### Key observations

- Enterprise model: organizations buy **licenses**; admins add/remove learners, assign/revoke licenses; learners activate via invitation email, **email-domain verification**, or SSO; **SCIM** and **CSV** user management; **custom attributes**; **Org Sync** to auto-update learner data; **Enterprise profile** (LinkedIn identity + company details + activity).
- **Groups** (with nested child groups) are used to "recommend content to a specific set of learners" — recommendation, not mandatory assignment (no org-defined mandatory-course machinery observed in the sampled pages).
- Learning content is the vendor's library (courses/videos); learner-side **video progress** and **completions**; **Certificates of Completion** (downloadable, addable to LinkedIn profile); **Continuing Education** (CE) support.
- Admin surface: **Admin Center** / Account Center; license management; learner reports (CSV download with attributes/groups/licenses).
- No org-authored courses observed; no ILT/session machinery observed; no waiting lists/approval flows observed in sampled pages.

**Interpretation:** content-library-first posture of the same underlying structure — identified employee learners, a managed offering (the library), a learner↔offering link (license), and tracked completion records. The organization-authored-course layer is thin/absent; assignment is recommendation-shaped.

**Vendor-specific (L3):** license model, Enterprise profile, Org Sync, CE credits, LinkedIn-profile integration.

## Product D — Cornerstone Learning (positioning level only)

### Key observations

- Help-center root (only reachable page): "Cornerstone Learn — Rapidly upskill your people and close compliance gaps through AI-powered learning using **Learning Management and Experience, Content, Extended Enterprise, and Reporting**."
- Same help center ships **Saba** and **SumTotal** as separate legacy product lines — evidence that the category has long-lived enterprise incumbents (useful for the historical check).
- Deep documentation unreachable (404 on product help page; JS-rendered sub-sites). No operational claims made for this product.

## Cross-product Comparison

| # | Finding | Docebo | Absorb | LinkedIn Learning | Cornerstone | Strength |
|---|---|---|---|---|---|---|
| 1 | Identified learner population tied to the organization (users/departments/branches/groups; licenses) | ✓ (users, branches, groups, cohorts) | ✓ (users, departments, groups) | ✓ (enterprise licenses, learners) | ✓ (positioning) | A×3 + B |
| 2 | Learning offerings as managed objects (courses) | ✓ (e-learning + ILT w/ sessions) | ✓ (online courses, curricula, ILC) | library courses (vendor-authored) | ✓ (positioning) | A×3 |
| 3 | Organization-controlled learner↔offering link (enrollment/assignment) | ✓ (enrollments, rules, codes, CSV) | ✓ (enrollment rules/methods/approval) | ✓ (license assignment; groups recommend) | ✓ (positioning) | A×3 |
| 4 | Tracked participation & completion as per-learner records | ✓ (statuses, completion rules) | ✓ (progress values, manual override) | ✓ (video progress, completions) | ✓ (positioning) | A×3 |
| 5 | Completion defined by mandatory-content rules | ✓ (mandatory materials/sessions) | ✓ (mandatory content; Failed state) | n/o | ✓ (positioning) | A×2 |
| 6 | Org-structure targeting (departments/branches/groups) | ✓ | ✓ | ✓ (groups) | n/o | A×3 |
| 7 | Role separation: platform admin / delegated admin / manager / learner (+ instructor) | ✓ (Superadmin/Power User/Manager/Instructor/Learner) | ✓ (Admin/Manager/Learner/Reviewer) | ✓ (admin/learner) | n/o | A×3 |
| 8 | Manager oversight surface (team dashboards, approvals) | ✓ (My team) | ✓ (Manager Experience; Enrollment Approval) | n/o | n/o | A×2 |
| 9 | Catalog / curated offering visible to learners | ✓ (catalogs, public catalog) | ✓ (catalog page) | ✓ (library) | n/o | A×3 |
| 10 | Certificates / completion evidence; certification validity & renewal | ✓ (certificates; certifications valid/expiring/expired) | ✓ (Re-Enrollment & Re-Certification) | ✓ (Certificates of Completion, CE) | n/o | A×3 |
| 11 | Reporting/analytics on learning activity | ✓ (Analytics) | ✓ (Reports/Dashboards) | ✓ (learner reports) | ✓ (positioning: Reporting) | A×3 |
| 12 | Content sourcing: authored + imported standards + third-party libraries | ✓ (training material incl. SCORM; content marketplace) | ✓ (Create; Amplify/Content Hub) | library only | ✓ (positioning: Content) | A×3 |
| 13 | Instructor-led delivery with sessions & attendance | ✓ (ILT/VILT sessions, attendance) | ✓ (ILC, attendance) | n/o | n/o | A×2 |
| 14 | Self-enrollment policies incl. approval / waiting lists | ✓ (pending admin approval, waiting users, quotas) | ✓ (Enrollment Approval, methods, keys) | n/o | n/o | A×2 |
| 15 | Time validity / expiration / re-training mechanics | ✓ (time options, soft deadline, validity statuses) | ✓ (availability dates, re-certification) | n/o | n/o ("close compliance gaps") | A×2 |
| 16 | HR/identity integration (SSO, SCIM, HRIS sync) | ✓ (SSO; skills↔HRIS) | ✓ (SSO, SCIM) | ✓ (SSO, SCIM, Org Sync) | n/o | A×3 |
| 17 | Notifications/reminders to learners & managers | ✓ | ✓ (message templates) | ✓ (invitation/resend emails) | n/o | A×3 |
| 18 | Skills/competency layer | ✓ (Skills, Skills Intelligence) | ✓ (Skills, Competencies) | n/o | ✓ (Transform, positioning) | A×2+B |
| 19 | External/offline training recording | ✓ (External training app) | n/o | n/o | n/o | A×1 — product-specific |
| 20 | E-commerce / extended enterprise (sell to customers/partners) | ✓ | ✓ | n/o | ✓ (positioning: Extended Enterprise) | A×2+B — variant |
| 21 | AI assistance (tutor, recommendations, content creation) | ✓ (Harmony, AI translation) | ✓ (Aura) | n/o | ✓ (positioning: AI-powered) | A×2+B — modern layer |
| 22 | Gamification / social learning / communities | ✓ | ✓ (Engage) | n/o | n/o | A×2 — optional |

n/o = not observed in sampled pages (absence not asserted as product absence beyond sampled evidence).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

An **Employee Learning Platform** is an organization-operated platform in which:

1. **Organization-defined learner population** — employees exist as identified learners, sourced from the organization (HR/identity data), organized by org structure.
2. **Managed learning offerings** — learning activities exist as managed objects (courses / learning activities) that the organization defines or curates.
3. **Organization-controlled learner↔offering link** — the organization determines which learners are linked to which offerings (assignment/enrollment), whether mandatorily or electively.
4. **Tracked participation and completion records** — each learner's progress and completion of each offering is recorded per learner, producing a durable training record.

Remove any one and the Type collapses: without the learner population it is a content site; without managed offerings it is an HR record system; without the controlled link it is a content library; without tracked records it is a content player.

**Historical/market-sample check:** early-2000s enterprise LMS lines (Saba, SumTotal — both now Cornerstone lines) satisfy all four invariants with none of the modern layers (no AI, no skills graphs, no LXP discovery); simple instructor-led training coordinators satisfy them with sessions as offerings; LinkedIn Learning satisfies them with licenses as the link and library content as offerings. The L0 therefore does not overfit the modern AI/skills-era implementation.

### L1 — Common Mature Structure

- **Delivery types**: self-paced e-learning (SCORM/xAPI/video/document material) and instructor-led training (sessions, locations, attendance).
- **Learning plans / curricula**: ordered bundles of courses with mandatory/optional marking and prerequisites; plan completion derived from constituent courses.
- **Catalogs & self-enrollment**: curated offering catalogs; self-enrollment policies incl. administrator approval, waiting lists, quotas, enrollment keys/codes.
- **Org-structure targeting**: departments/branches/groups as assignment and visibility units.
- **Role model**: platform admin, delegated/resource-scoped admins, managers, instructors, learners; permission-scoped visibility (delegated admins see only their assigned users).
- **Manager oversight**: team dashboards, enrollment approvals, progress tracking.
- **Certificates & certification validity**: completion certificates; certifications with validity windows and re-certification/re-training loops.
- **Reporting/analytics**: enrollment/completion/compliance reporting, dashboards, exports.
- **Content sourcing**: in-product authoring, standards-based import (SCORM/xAPI), third-party content libraries/marketplaces.
- **Notifications/reminders**; **SSO/SCIM/HRIS integration**; **mobile access**; **skills/competency layer** (modern).

### L2 — Variant / Optional Structure

- **Extended enterprise**: same machinery pointed at customers/partners, with e-commerce (both sampled standalone products ship it as a module).
- **External training recording** (offline/external events) — product-specific in sample.
- **Compliance depth**: audit trail, e-signature, regulatory reporting — depth varies by regulated-industry demand.
- **LXP posture**: self-directed discovery, content aggregation, AI recommendation — a posture of the same structure, not a separate one.
- **Gamification, social learning, communities, mentorship, observation checklists**.
- **AI assistance** (tutors, content generation, translation).
- **Deployment/packaging**: standalone vs HCM-suite-embedded; headless/embedded learning; SaaS vs on-prem.

### L3 — Vendor-specific (kept out of final document)

Docebo: Harmony AI, AgentHub, Companion, branches/cohorts terminology, 250-course plan limit, legacy retraining app migration. Absorb: ILC terminology, Enrollment Keys, Aura/Create/Engage/Amplify/Skills product names, "Enroll Anyone" permission. LinkedIn Learning: license model, Enterprise profile, Org Sync, CE credits. Cornerstone: Galaxy/Single Architecture lines, Saba/SumTotal legacy lines.

## Vendor-specific Findings

- Docebo's *Overbooking* status and *External training* app are product-specific structures (single-product evidence; not promoted).
- Absorb's auto-complete edge case (empty course → Complete with 0% progress) is product-specific behavior.
- LinkedIn Learning's groups "recommend content" (recommendation-shaped link) — sampled-pages observation; not generalized to all library-first products.
- Docebo's certifications are migrating to a new BETA "Learning plans and certifications" page (Sept 2026) — product roadmap detail, not canonical.

## Boundary Findings

1. **vs Corporate LMS (§09 sibling) — probable Alias.** The researched products are marketed as "learning platform" (Docebo), "Learning Management" (Cornerstone), "LMS" (Absorb); market usage treats *corporate LMS*, *employee learning platform*, *learning platform*, *workplace learning platform* as names for the same product category. No structural difference was found in the sample: the same objects (learners, courses, enrollments, completions, plans, certifications), the same roles, the same compliance mechanics. The two leaves likely denote one Type; flagged for joint review when Corporate LMS is processed. This document defines the structure once, under this leaf's name.
2. **vs LMS (§23, education) — same engine, different population and rules.** Education LMS centers students, academic terms, grades/credit, and institution-owned pedagogy; the workplace Type centers employees, jobs/roles, compliance/certification records, and employer-owned training. The record's downstream consumer differs (academic transcript vs HR/compliance file). Boundary test: remove the employment/compliance frame → education LMS remains.
3. **vs Learning Experience Platform / LXP (§23) — posture gradient.** LXP centers self-directed discovery and content aggregation; in the researched sample LXP capabilities are bundled inside the same products (Cornerstone Learn includes "Learning Experience"; Docebo ships channels/AI recommendations; Absorb ships Engage/Content Hub). LXP is treated as a posture/variant of this Type, not a separate structure.
4. **vs Customer Training / Academy Platform (§07) — audience variant.** Same platform machinery; learner population differs (customers/partners vs employees). Both sampled standalone products ship "extended enterprise" as a module of the same product. Remove the employee population → customer training remains.
5. **vs Employee Onboarding Platform (§09) — use-case overlap.** New-hire training is a learning-plan use case inside this Type; onboarding platforms center on workflow/tasks/checklists rather than learning records. Remove the learning-record core → onboarding platform remains.
6. **vs Skills Management Platform (§09) — capability relationship.** Skills profiles/assessments vs learning delivery/records; every modern sampled learning product bundles a skills layer (Docebo Skills Intelligence, Absorb Skills, Cornerstone Transform), while dedicated skills platforms exist. Capability, not duplicate.
7. **vs eLearning Authoring Tool (§23) — capability relationship.** Authoring exists inside learning platforms (course builders, Absorb Create) but dedicated authoring tools are separate products with deeper authoring workflows.
8. **vs Employee Experience Platform (§09, processed) — domain relationship.** The EX-platform pass recorded "learning aggregation" as one EX domain; this Type is the single-domain specialist whose records EX platforms aggregate. Consistent with prior cluster flags.
9. **vs GxP Training Management (§22) — regulated overlay.** Regulated-industry training (validation-linked curricula, signatures) is a compliance-depth variant of the same structure; depth differs, core does not.

## Uncertainties

- Cornerstone operational structures are asserted only at positioning level (deep docs unreachable); no workflow claims made for it.
- SAP SuccessFactors Learning and Workday Learning could not be fetched; the **HCM-embedded variant** is under-evidenced (expected: HR-suite-embedded learning with shared user/population model) — kept out of strong claims.
- LinkedIn Learning's assignment machinery: sampled pages show license assignment + group-based recommendation; absence of mandatory-assignment machinery is asserted only for the sampled pages.
- Exact numeric limits (e.g., Docebo's 250-course recommendation), default validity windows, and quota defaults are product-specific and intentionally not generalized.
- The alias question (this leaf vs Corporate LMS) cannot be settled unilaterally; recorded for joint review.

## Final Synthesis

The Employee Learning Platform is the organization-operated system of record for workforce learning. Its defining core is small: an organization-defined learner population, managed learning offerings, organization-controlled links between learners and offerings, and per-learner tracked participation/completion records. Everything the market associates with modern corporate learning — delivery formats, curricula, catalogs, self-enrollment with approvals, manager oversight, certificates with validity and re-training, reporting, content libraries, skills layers, AI — is standard mature structure or variant structure layered on that core, not part of the definition. The Type is structurally identical to what the market also calls a corporate LMS; the education LMS differs by population and rules, the LXP by posture, and customer-training platforms by audience.
