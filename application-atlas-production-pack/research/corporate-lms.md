# Research Notes — Corporate LMS

## Research Goal

Understand what a Corporate LMS really is as an Application Type: its defining structure, standard capabilities, lifecycle and rules, and its boundaries against neighboring Types. This pass also carries a **joint-review obligation** recorded by the employee-learning-platform pass (2026-09-06): that pass flagged `corporate-lms` as a probable Alias of `employee-learning-platform` and deferred resolution to this pass. This pass therefore (a) researches the category independently with a different product sample, and (b) resolves the alias question.

## Initial Boundary

- Leaf: **Corporate LMS** (DIRECTORY §09 HR, Workforce & Talent, line 760).
- Working hypothesis: employer-operated software to deliver, manage, and track workforce training.
- Nearest neighbors suspected up front: **Employee Learning Platform** (§09 sibling — flagged probable alias), **LMS** (§23, education), **Learning Experience Platform / LXP** (§23), **Customer Training / Academy Platform** (§07), **HR Compliance Management** (§09, processed — its "training pole" straddles the seam per that pass), **Skills/Competency Management Platform** (§09, processed — remedy seam recorded by that pass), **Employee Onboarding Platform** (§09), **eLearning Authoring Tool** (§23), **GxP Training Management** (§22).

## Research Questions

1. What are the core objects (learner, course, path/curriculum, session, enrollment, completion, certificate)?
2. How does the learner↔offering link work — mandatory assignment vs governed self-enrollment vs manager assignment?
3. What lifecycle/states do enrollments, completions, and certificates carry?
4. Which roles exist and how do permissions scope behavior?
5. How do compliance mechanics work (validity, re-certification, audit)?
6. Is Corporate LMS structurally distinct from Employee Learning Platform, or one Type under two names? (joint review)
7. Where does content come from (authored, standards import, third-party libraries)?
8. Where is the seam vs HR Compliance Management's mandate-driven training pole?

## Representative Products

| Product | Segment / philosophy | Evidence level reached |
|---|---|---|
| **360Learning** | collaborative-learning LMS, mid-market→enterprise | Tier-1 help center, 5 pages (KB root, glossary, permissions & roles, enroll learners, Task Center) + Tier-2 product page (deep) |
| **TalentLMS** (Epignosis) | SMB/lightweight cloud LMS | Tier-2 product root + features page (positioning + published feature claims); help center unreachable ×2 |
| **LearnUpon** | multi-audience portal LMS, mid-market→enterprise | Tier-2 product root (positioning + FAQ); support portal unreachable ×2 |
| Litmos | corporate training LMS | **Rejected** — support site is a login wall (×2) |
| SAP SuccessFactors Learning | HCM-embedded enterprise LMS | **Rejected** — help portal returns JS shell (×1); consistent with the sibling pass's failure |

Corroborating sample (not re-fetched; from the sibling pass's Tier-1 research, used for the joint review): Docebo, Absorb LMS, LinkedIn Learning, Cornerstone Learning.

## Sources

- 360Learning Support (Zendesk KB) — https://support.360learning.com/hc/en-us (root) — fetched 2026-09-07
- 360Learning — Platform glossary — https://support.360learning.com/hc/en-us/articles/9194138706324-Platform-glossary — fetched 2026-09-07
- 360Learning — Permissions & roles — https://support.360learning.com/hc/en-us/articles/360051774011-Permissions-roles — fetched 2026-09-07
- 360Learning — Enroll learners in a path session — https://support.360learning.com/hc/en-us/articles/16740167802388-Enroll-learners-in-a-path-session — fetched 2026-09-07
- 360Learning — Process registration requests with the Task Center — https://support.360learning.com/hc/en-us/articles/23917113633940-Process-registration-requests-with-the-Task-Center — fetched 2026-09-07
- 360Learning — Share paths section map — https://support.360learning.com/hc/en-us/sections/360013274812-Share-paths — fetched 2026-09-07
- 360Learning product site — https://www.360learning.com/ — fetched 2026-09-07
- TalentLMS product site — https://www.talentlms.com/ and https://www.talentlms.com/features — fetched 2026-09-07
- LearnUpon product site — https://www.learnupon.com/ — fetched 2026-09-07
- Sibling-pass sources (Docebo help.docebo.com, Absorb support.absorblms.com, LinkedIn Learning help, Cornerstone help.csod.com) — fetched 2026-09-06, recorded in research/employee-learning-platform.md

Failed/abandoned: help.talentlms.com (timeout ×2), help.learnupon.com (403), support.learnupon.com (transport error ×2), support.litmos.com (login wall ×2), help.sap.com SAP_SUCCESSFACTORS_LEARNING (JS shell ×1), help.360learning.com (JS shell ×1 — Zendesk mirror reachable instead).

## Product A — 360Learning (Tier-1, directly observed)

### Key observations

**Object structure (glossary + KB category map, directly observed):**
- **Course** = e-learning content object built from **activities** (frames containing documents, cheat sheets, questions, recordings).
- **Path** = training object made of steps (courses, classrooms, other paths, assessments); paths can contain subpaths (auto-enrollment into subpaths documented).
- **Path session** = a specific instance of a path with a defined start date and optional end date, used to enroll learners and track progress. Multiple sessions per path; learners can be enrolled in multiple sessions of the same path.
- **Classroom** = live training event within a path (virtual or onsite) with scheduled **classroom slots** (date, time, location or virtual meeting link); **trainers** fill slot attendance.
- **Catalog** = a group's collection of content (courses, paths) learners can access freely; distinct from the **Library** (a group's shared repository used by editors/coaches to build paths or share to catalogs).
- **Audience Builder** = tool for defining learner enrollment groups based on criteria such as role, group, or custom field.
- **Open Registration** = a learner enrolling in a path on their own rather than being enrolled by a trainer.
- **Participant** = learner who clicked Start; **Participation Rate / Completion Rate / Pass Rate** = standard metrics (12-month windows).
- **Mandatory Replay** = setting forcing learners to replay a course/path when re-enrolled.
- **Learning Need** = users request learning content from their group.
- **Skills** = define, map, track employee competencies; **jobs** and **qualifiers** as skill structures; skill assessment.
- **Curated Programs** = third-party content integration (Udemy, LinkedIn Learning, Skillsoft named).
- **Extended Academies** = groups with distinct branded experience (custom colors, domain, self-registration).
- **Data Connect** = Snowflake-powered warehouse with SQL access to raw learning analytics.
- Group hierarchy: platform group → subgroups; **Member** = user assigned to a group with a role; newsfeeds per group; widgets on home/group pages.

**Role model (Permissions & roles article, directly observed):**
- Main roles: **Learner** (play courses/paths, forums, bookmarks/playlists), **Coach** (oversees group: create path sessions, share courses/paths, track group/user/course statistics, send reminders), **Contributor** (create content, update own; sees only own results), **Editor** (create content, update own + group's), **User admin** (add/remove users, reset passwords; no statistics), **Group admin** (user admin + coach + editor + create groups, edit settings, change roles, manage skills; **group-admin role cascades to subgroups**, other roles do not), **Platform admin** (everything except billing), **Owner** (billing; exactly one per platform).
- Specific roles: main author/co-author (course/path), **Manager** (extended permissions over specific users regardless of groups: track managees' statistics, send reminders, manage skills), main/co-instructor of a path session (edit session, fill attendance, see session statistics even after session ends), Translator, Reviewer (projects), Trainer (classroom slots).
- Statistics visibility is explicitly role- and scope-dependent (dedicated "Understand statistics visibility" article).

**Enrollment mechanics (Enroll learners article, directly observed):**
- Enrollment rights are role-scoped: platform admins enroll anyone; group admins/coaches enroll members of their groups in their group's sessions; instructors enroll in their own sessions; managers enroll their managees (feature-gated).
- Methods: specific learners (limit 20,000/session), by email list (can create new platform users), by groups (limit 5,000/session), everyone (platform admins only).
- **Audiences**: static (fixed cohort at save time) vs **dynamic** (auto enroll/unenroll as learners meet or stop meeting criteria; auto-enroll new joiners; updates can take up to 20 minutes; daily refresh option for date filters).
- Audience filters: path result (Completed / Not completed / Successful / Not successful — success = all mandatory steps + minimum scores + time limits), **certificate status (Not obtained / Valid / Expired / Expiring in 30 days)**, user creation date, user activation date, user custom fields.
- Stated use cases in the article: "Organization-wide training: Assign mandatory training, such as compliance or security awareness, to all employees at once"; "assigning an onboarding path to all new hires as they join" via dynamic audiences.
- Unenrollment: learners lose access but **keep their statistics** and resume progression if re-enrolled; saving an audience recalculates and can unenroll even learners who already started/completed.
- Email notifications on enrollment (at session start or next hour if already started).

**Self-enrollment approval (Task Center article, directly observed):**
- Path sessions shared in a catalog can **require validation** of open-access registrations; learners' self-enrollment then creates a registration request.
- Administrators, managers, or instructors (per session settings) validate/reject requests in a **Task Center**: pending/completed states, bulk actions, filters (groups/learners/sessions), actor identity attached to each decision, platform admins can act on behalf of their instructors/managers ("My team" view).
- Un-enrollment from self-assigned sessions can also require validation.

**Positioning (product page, Tier 2):** "AI-driven LMS"; use cases: compliance training ("Automate mandatory training and re-certification"), employee onboarding, sales enablement, frontline staff; deep HCM/HRIS integrations ("Leverage HR data to auto-enroll users in relevant courses"; Workday, SAP, BambooHR, Slack, Salesforce, Oracle, "80+ more"); product family: LMS, LXP, Academies, Skills; "One platform. One contract. Every learning audience." G2 badges include "Corporate Learning Management Systems Leader" (enterprise + mid-market).

**Vendor-specific (L3):** Audience Builder/Task Center naming, coach/contributor/editor role ladder, 20,000/5,000/64,000 numeric limits, "Expiring in 30 days" filter value, Mandatory Replay, Learning Need, newsfeeds, reactions/reaction score, Extended Academies, Curated Programs, Data Connect, legacy enrollment mechanism dates (Jan 24 2024 / Mar 27 2024), AI Companion, Video Pitch/Screencast Demo coaching activities.

## Product B — TalentLMS (Tier-2, published feature claims)

### Key observations

- Positioning: "The #1 Cloud LMS", "All-in-one LMS for growing businesses"; sibling products eFront (enterprise LMS), TalentCards (mobile microlearning), TalentHR (HRIS). G2 badge "Corporate Learning Management Systems" leader visible on site.
- **Course creation & delivery**: content options (video, audio, presentations, embedded), **Learning Paths** (connected courses, unlock in set order), assessments & certifications (quizzes, surveys, assignments; "custom certificates that reflect achievement and stay current over time"), **TalentLibrary** (1,000+ ready-made courses), **Course Store** (third-party providers incl. compliance/safety courses "that meet specific state training requirements"), **SCORM/xAPI/cmi5** import, **LTI 1.3**, **blended learning** (self-paced + live instructor-led, schedule in-person or virtual sessions), gamification (badges, points, levels, leaderboards), mobile apps (offline).
- **Admin & user management**: **Automations** ("trigger actions based on user behavior, like completions, expirations, or inactivity"), **custom roles & permissions**, **Groups** ("assign training to entire teams with just one click"), **Branches** ("separate training environments for different teams and departments... branded portals with unique content and users"), discussions, notifications, REST API, HRIS/CRM integrations + Zapier.
- **Reporting**: real-time reports, scheduled reports (emailed weekly/monthly), custom reports, analytics widgets, **Timeline** ("track platform activity... option to export results for a detailed audit trail").
- **Branding**: white-labeling, custom domain & homepage, custom mobile app.
- **Security/compliance posture**: SSO, GDPR tooling, ISO certifications, WCAG 2.1 accessibility.
- Use-case pages: employee training, onboarding, partner training, compliance training, customer training — the same product marketed across employee and extended-enterprise audiences.

**Interpretation:** the same four-part structure (employee users organized in groups/branches; courses/paths as offerings; assignment + self-service; tracked progress/completion/certificates) at the SMB tier, with lighter compliance depth and heavier ease-of-setup/branding emphasis. Branches = multi-audience portal variant.

**Vendor-specific (L3):** TalentLibrary/TalentCraft/Course Store product names, branches terminology, automations trigger set, 70,000+ teams marketing figure.

## Product C — LearnUpon (Tier-2, positioning + FAQ)

### Key observations

- Positioning: "Agentic Learning Platform" — self-described in FAQ as "an AI-driven learning management system (LMS) designed to automate administrative tasks and personalize the learning experience."
- FAQ (directly observed): "primarily used for employee onboarding and skilling, customer education, compliance training, association learning and certification, and scaling extended enterprise learning programs"; **Portals** ("multi-tenancy... unique, fully branded environments for employees, external customers, and associations, each with separate user permissions, catalogs, and reporting metrics"); integrations via "native, pre-built connectors and a developer-friendly REST API... automate user provisioning, sync data across platforms"; Create+ AI authoring.
- Platform modules: Learning Journeys (dynamic personalized learning), Skills ("surface and close skill gaps... insights from your tech stack"), Reporting & Analytics, LearnUpon Anywhere (embedded customer education), MCP Server.
- Products: LearnUpon for Employees / for Customer Education / for Associations — one platform, multiple audiences.
- G2 badge "Corporate Learning Management Systems" leader visible on site.

**Interpretation:** same core structure; the distinguishing posture is multi-audience portals (extended enterprise as a first-class architecture) and journey/skills layers. Employee use case is one portal population among several.

**Vendor-specific (L3):** Portals/IQ/Hubs naming, Learning Journeys, Create+, MCP Server, marketing figures (1,700+ organizations, 31M+ users, 290M+ courses).

## Product D — Litmos / SAP SuccessFactors (rejected samples)

- Litmos: support.litmos.com redirects to a Salesforce login wall. No operational evidence. Abandoned per network rules.
- SAP SuccessFactors Learning: help.sap.com returns a JS application shell. No operational evidence. The **HCM-embedded variant** remains under-evidenced in both this and the sibling pass; no operational claims are made for it.

## Cross-product Comparison

| # | Finding | 360Learning | TalentLMS | LearnUpon | Sibling sample (Docebo/Absorb/LinkedIn/Cornerstone) | Strength |
|---|---|---|---|---|---|---|
| 1 | Identified learner population tied to the organization, organized by org structure | ✓ (groups/subgroups, custom fields) | ✓ (groups, branches) | ✓ (portals with separate user sets) | ✓ (users/departments/branches; licenses) | A×3 + A(sib)×3 + B |
| 2 | Learning offerings as managed objects (courses; bundles) | ✓ (courses→paths→sessions) | ✓ (courses, learning paths) | ✓ (courses, learning journeys) | ✓ (courses, curricula, plans) | A×3 + B |
| 3 | Organization-controlled learner↔offering link | ✓ (admin/group/manager enrollment; audiences; catalog self-enrollment with validation) | ✓ (group assignment "one click", automations) | ✓ (portal catalogs, journeys) | ✓ (enrollment rules/approvals; license grants) | A×3 + B |
| 4 | Tracked participation & completion per learner | ✓ (participant/completion/pass rates; statistics visibility rules) | ✓ (real-time reports, progress) | ✓ (reporting & analytics) | ✓ (statuses, progress values) | A×3 + B |
| 5 | Completion governed by rules (mandatory content, scores, attendance) | ✓ (Successful = mandatory steps + min scores + time limits) | ✓ (assessments; certificates) | n/o (positioning) | ✓ (mandatory materials/sessions; Failed state) | A×2 + B |
| 6 | Instructor-led delivery with sessions & attendance | ✓ (classrooms, slots, trainers, attendance) | ✓ (blended learning, live sessions) | n/o | ✓ (ILT/VILT sessions, ILC attendance) | A×2 + B |
| 7 | Self-enrollment with governance (approval/waiting/validation) | ✓ (Open Registration + Task Center validation) | n/o (positioning) | n/o | ✓ (approval, waiting lists, keys) | A×2 + B |
| 8 | Role model: admin / delegated admin / manager / instructor / learner | ✓ (7 main roles + specific roles) | ✓ (custom roles & permissions) | n/o (positioning) | ✓ (Superadmin/Power User/Manager/Instructor/Learner) | A×2 + B |
| 9 | Manager oversight (team statistics, reminders, enrolling managees) | ✓ (Manager role, Manager Dashboard, enroll managees) | n/o (positioning) | n/o | ✓ (My team; Manager Experience) | A×2 + B |
| 10 | Certificates with validity & re-training loops | ✓ (certificate status Valid/Expired/Expiring; Mandatory Replay; re-certification use case) | ✓ ("stay current over time"; automations on expirations) | n/o (positioning) | ✓ (valid/expiring/expired; re-enrollment & re-certification) | A×2 + B |
| 11 | Compliance/mandatory training as headline use case | ✓ ("mandatory training... to all employees at once") | ✓ (compliance training solution page; state-requirement courses) | ✓ (FAQ: compliance training) | ✓ (Cornerstone "close compliance gaps") | A×3 + B |
| 12 | Content sourcing: authored + standards import + third-party libraries | ✓ (authoring; SCORM via integrations; Curated Programs) | ✓ (authoring; SCORM/xAPI/cmi5; TalentLibrary/Course Store) | ✓ (Create+; integrations) | ✓ (authoring; SCORM; marketplaces; library-only pole) | A×3 + B |
| 13 | Reporting/analytics incl. exports | ✓ (user/group/course analytics; Data Connect) | ✓ (real-time/scheduled/custom; Timeline audit) | ✓ (reporting suite) | ✓ (analytics; reports) | A×3 + B |
| 14 | Notifications/reminders | ✓ (enrollment emails; reminders; Task Center notifications) | ✓ (notifications; scheduled reports) | n/o | ✓ (notifications; message templates) | A×2 + B |
| 15 | SSO / HRIS / identity integration | ✓ (SSO; HCM integrations "auto-enroll users from HR data") | ✓ (SSO; HRIS integrations) | ✓ (SSO implied; provisioning via connectors) | ✓ (SSO, SCIM, HRIS sync) | A×3 + B |
| 16 | Skills/competency layer | ✓ (Skills: skills/jobs/qualifiers/assessment) | ✓ (Skills — AI skills-based training) | ✓ (Skills module) | ✓ (Docebo Skills, Absorb Skills, Cornerstone Transform) | A×3 + B |
| 17 | Multi-audience / extended enterprise (customers, partners, associations) | ✓ (Extended Academies; "every learning audience") | ✓ (branches; partner/customer solution pages) | ✓ (Portals; three audience products) | ✓ (Docebo/Absorb e-commerce; Cornerstone Extended Enterprise) | A×3 + B — variant |
| 18 | Gamification / social / collaborative learning | ✓ (forums, newsfeeds, reactions) | ✓ (gamification; discussions) | n/o | ✓ (Docebo communities; Absorb Engage) | A×2 + B — optional |
| 19 | AI assistance (authoring, recommendations, tutoring) | ✓ (AI Companion, AI content builder) | ✓ (TalentCraft, AI Coach, translator) | ✓ (agentic platform, Create+) | ✓ (Harmony, Aura; positioning) | A×3 + B — modern layer |
| 20 | White-labeling / custom domains / branded apps | n/o (sampled pages) | ✓ | ✓ (branded portals) | n/o | A×2 — optional |
| 21 | External/offline training recording | n/o | n/o | n/o | ✓ (Docebo External training app) | A×1 — product-specific |
| 22 | E-commerce for course sales | n/o (plans & billing only) | n/o (Course Store is vendor-side) | n/o | ✓ (Docebo/Absorb e-commerce) | A(sib)×2 — variant |

n/o = not observed in sampled pages (absence not asserted beyond sampled evidence).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

A **Corporate LMS** is an organization-operated platform in which:

1. **Organization-defined learner population** — employees exist as identified learners inside the platform, sourced from the organization (maintained directly or synchronized from HR/identity systems) and organized by organizational structure (departments, groups, branches, portals).
2. **Managed learning offerings** — learning exists as managed objects (courses, learning activities, paths/curricula) that the organization defines, authors, imports, or curates.
3. **Organization-controlled learner↔offering link** — the organization determines which learners are linked to which offerings: mandatory assignment (by admin action, rule, or dynamic audience), manager assignment, or governed self-enrollment (approval/validation, capacity, codes).
4. **Tracked participation and completion records** — each learner's progress and completion of each offering is recorded per learner and persists as a durable training record, with certificates and validity where configured.

Remove any one and the Type collapses: without (1) it is a public content site/MOOC; without (2) it is an HR record system; without (3) it is a content library; without (4) it is a content player.

**Historical/market-sample check:** early-2000s enterprise LMS lines (Saba, SumTotal — now Cornerstone product lines) satisfy all four invariants with none of the modern layers (no AI, no skills graphs, no portals); instructor-led training coordinators satisfy them with sessions as offerings; license-based content libraries (LinkedIn Learning) satisfy them with licenses as the link and vendor content as offerings. The L0 does not overfit the modern AI/skills/portal-era implementation.

### L1 — Common Mature Structure

- Delivery formats: self-paced e-learning (native authoring; SCORM/xAPI/cmi5 import) and instructor-led training (scheduled sessions, locations/virtual rooms, attendance marking).
- Learning paths / programs / curricula: ordered bundles with mandatory/optional marking, prerequisites; completion derived from constituents.
- Catalogs and governed self-enrollment: curated catalogs; approval/validation steps, waiting lists, capacity, enrollment codes.
- Org-structure targeting: groups/departments/branches as assignment and visibility units.
- Role model: platform admin, delegated/scoped admins, managers, instructors, learners; scope-limited visibility and separately controllable permissions.
- Manager oversight: team dashboards, reminders, enrollment approvals, enrolling managees.
- Certificates and validity: completion certificates; validity windows, expiration states, re-training/re-certification loops.
- Reporting/analytics: enrollment/completion/compliance reporting, dashboards, scheduled and custom reports, exports.
- Content sourcing: in-product authoring, standards-based import, third-party libraries/marketplaces.
- Notifications/reminders; SSO and HRIS/identity integration; mobile access; skills layer (modern).

### L2 — Variant / Optional Structure

- Extended enterprise: same machinery pointed at customers/partners/associations; multi-portal/multi-tenant architectures with separate branding, catalogs, permissions, reporting; e-commerce in some products.
- Collaborative/social learning: forums, newsfeeds, peer content creation, reactions.
- Gamification; AI assistance (authoring, recommendations, tutoring, translation); white-labeling/custom domains/branded mobile apps.
- Compliance depth: audit trails, e-signatures, regulatory reporting — depth varies with regulated-industry demand.
- External/offline training recording (product-specific in the combined sample).
- Deployment/packaging: standalone vs HCM-suite-embedded vs suite module; SaaS vs on-prem; frontline/deskless tuning.

### L3 — Vendor-specific (kept out of the final document)

360Learning: coach/contributor/editor role ladder, Task Center, Audience Builder, Mandatory Replay, Learning Need, newsfeeds/reactions, Extended Academies, Curated Programs, Data Connect, numeric limits (20,000 learners / 5,000 groups per session; 64,000 suggestion; 20-minute dynamic updates; "Expiring in 30 days" filter), legacy enrollment dates. TalentLMS: TalentLibrary/TalentCraft/Course Store, branches, automations trigger set, Timeline. LearnUpon: Portals/IQ/Hubs, Learning Journeys, Create+, MCP Server, marketing figures. Sibling sample: Docebo Harmony/AgentHub/branches/cohorts/250-course plan limit, Absorb ILC/Enrollment Keys/Aura, LinkedIn Learning license model/Org Sync/CE credits, Cornerstone Saba/SumTotal lines.

## Vendor-specific Findings

- 360Learning's audience model (static vs dynamic audiences with filter-based auto enroll/unenroll) is the most explicit rule-based assignment machinery in the sample; treat the *concept* (rule-driven assignment) as common, the *implementation* as product-specific.
- 360Learning's Task Center (validation of self-enrollment and even self-unenrollment, with actor attribution) is a product-specific realization of governed self-enrollment; the concept is common (Docebo/Absorb approvals, waiting lists).
- TalentLMS's branches and LearnUpon's portals are two implementations of the same multi-audience variant; neither is definitional.
- TalentLMS's Timeline (exportable activity audit trail) evidences that audit capability exists outside regulated-industry suites, but depth remains a variant.
- Certificate-status-as-enrollment-filter (360Learning) shows validity states are first-class queryable records, not just displayed PDFs — promoted to L1 concept (certificates with validity), not to L0.

## Boundary Findings

1. **vs Employee Learning Platform (§09 sibling) — ALIAS CONFIRMED (joint review resolved).** Two independent passes with disjoint product samples converged on the same four-part defining core: this pass (360Learning, TalentLMS, LearnUpon — none reachable in the sibling pass) and the sibling pass (Docebo, Absorb, LinkedIn Learning, Cornerstone). Market usage treats the names as one category: the sampled products are marketed as "LMS" (TalentLMS, LearnUpon FAQ, Absorb), "learning platform" (Docebo, LearnUpon), "Learning Management" (Cornerstone), and all carry the G2 "Corporate Learning Management Systems" category badge; no structural difference was found (same objects, roles, enrollment mechanics, compliance machinery). Resolution recorded: one Type, two directory names; both application documents define the same structure and cross-reference; consolidation decision (merge vs keep-both) left to directory maintainers — this pass does not modify DIRECTORY.md.
2. **vs LMS (§23, education) — same engine, different population and rules.** Education LMS centers students, academic terms, grades/credit, institution-owned pedagogy; Corporate LMS centers employees, jobs/roles, compliance/certification records, employer-owned training. The record's downstream consumer differs (academic transcript vs HR/compliance file). Boundary test: remove the employment/compliance frame → education LMS remains.
3. **vs Learning Experience Platform / LXP (§23) — posture gradient.** Self-directed discovery and content aggregation as center of gravity; in the sample, LXP capabilities are bundled inside the same products (360Learning ships an LXP product line; TalentLMS/LearnUpon ship discovery/recommendation features). Posture of this Type, not a separate structure.
4. **vs Customer Training / Academy Platform (§07) — audience variant.** Identical machinery; learner population is customers/partners/members rather than employees. All three sampled products ship the extended-enterprise form as portals/branches/products of the same platform. Remove the employee population → customer training remains.
5. **vs HR Compliance Management (§09, processed) — obligation-centered vs learning-centered.** That Type's loop is applicability-matched obligation knowledge → fulfillment → retained evidence; its training pole (mandate-driven compliance training) is delivered through exactly this Type's machinery (mandatory assignment, validity, re-training, completion reporting). Seam: the LMS's core object is the learning offering and its enrollment/completion record; the compliance system's core object is the obligation and its evidence. LMS completion records are the evidence the compliance side consumes. Boundary test: remove obligation-matching machinery → LMS remains; remove offerings/enrollments → compliance management remains. The hr-compliance-management pass's joint-review flag is answered from this side: keep both Types; the training pole is a use case of the LMS, not a separate structure.
6. **vs Skills Management / Competency Management Platform (§09, processed) — capability relationship.** That pass recorded the remedy seam: skill gaps flow to the LMS as assignment drivers; LMS completions do not confer assessed standing. Modern LMS products bundle skills layers (all three sampled products), while dedicated skills platforms exist. Capability, not duplicate.
7. **vs eLearning Authoring Tool (§23) — capability relationship.** Authoring exists inside LMS products (native course builders, AI authoring) but dedicated authoring tools carry deeper authoring workflows as their primary job.
8. **vs Employee Onboarding Platform (§09) — use-case overlap.** New-hire training is a learning-path use case (360Learning documents dynamic onboarding audiences explicitly); onboarding platforms center on workflow/tasks/checklists rather than learning records.
9. **vs GxP Training Management (§22) — regulated overlay.** Validation-linked curricula and signatures are a compliance-depth variant of the same structure.
10. **vs Employee Experience Platform (§09, processed) — domain relationship.** EX platforms aggregate several workforce domains including learning; this Type is the single-domain system of record whose outputs they aggregate.

## Uncertainties

- The **HCM-embedded variant** (SAP SuccessFactors Learning, Workday Learning) remains under-evidenced — unreachable in both this and the sibling pass. Expected shape (shared user/population model with HR processes) is asserted only as an expectation, not a finding.
- TalentLMS and LearnUpon operational structures are evidenced at published-feature-claim level (help centers unreachable); no workflow claims are made for them beyond their own published descriptions.
- Litmos unreachable; no claims made.
- Precise numeric limits, default validity windows, and status-name sets observed in single products are recorded as product-specific and not generalized.
- The alias resolution is recorded as a recommendation; the directory decision (merge vs keep-both) belongs to maintainers.

## Final Synthesis

The Corporate LMS is the employer-operated system of record for workforce training. Its defining core is four structures held jointly: an organization-defined learner population, managed learning offerings, an organization-controlled link between learners and offerings, and per-learner tracked participation/completion records. Everything the market associates with the category — delivery formats, paths/curricula, catalogs with governed self-enrollment, manager oversight, certificates with validity and re-training, reporting, content libraries, skills layers, multi-audience portals, AI — is standard mature structure or variant structure on that core. The joint review with the employee-learning-platform pass confirms the two directory names denote one Type: two independent product samples converge on the same defining core and the market uses the names interchangeably. The education LMS differs by population and rules, the LXP by posture, customer-training platforms by audience, and HR compliance management by center of gravity (obligations vs learning).
