# Research Notes — Student Services Portal

## Research Goal

Understand what a "Student Services Portal" is as an Application Type: who uses it (student vs staff), what the surface aggregates (services, records, knowledge, requests), what the student actually does in it, how submitted requests flow to institutional offices and back, what roles/rules/privacy machinery matter, and where the Type's boundary sits — especially against the processed siblings **Student Case Management** (§23 — that pass's flag: "service-request/transaction resolution vs sustained casework"), **Student Billing System** (§23 — that pass's note: "money loop vs service/retention loop, no overlap observed"), and the unprocessed neighbors **Student Success Platform**, **Parent Portal**, **Academic Advising Platform**, **Student Information System** (processed), plus the cross-domain portal family (Customer Portal, Employee Portal, Government Service Portal, Self-service Support Portal, Information Portal).

## Initial Boundary

Initial hypothesis: the education institution's student-facing self-service front door — one authenticated surface where the student sees and acts on their own institutional business across multiple offices: view records/balances/holds, complete tasks, submit service requests and forms, book appointments, find answers, and track the state of each request to resolution. The institution's offices configure and fulfill on the staff side.

Adjacent Types to separate:
- Student Information System (§23, processed) — the record system of record; the portal is an access/interaction surface over it, not the record itself.
- Student Case Management (§23, processed) — sustained staffed casework over a concern; the portal resolves student-initiated service transactions.
- Student Success Platform (§23, unprocessed) — staff-side retention machinery; may ship its student surface as a portal (center-of-gravity seam expected).
- Parent Portal (§23, unprocessed) — guardian-facing sibling (record-view-centric in K-12).
- Customer Portal (§07), Employee Portal (§10), Government Service Portal (§24) — same constituent-portal family, different population/context.
- Self-service Support Portal (§07), Help Desk (§07) — single-provider support/knowledge surfaces; the student services portal spans the whole institution.
- Information Portal (§02.11) — aggregation without authenticated, personalized self-service.
- LMS / Virtual Classroom (§23) — learning delivery, not administrative services.
- Academic Advising Platform (§23, processed) — the advising relationship system; appointment booking commonly surfaces inside portals.

## Research Questions

1. Who signs in, and how is identity established (institution-granted? SIS-fed?)?
2. What does the surface aggregate — how many offices/domains, and via what structure (service catalog, dashboards, links, applications menu)?
3. What can the student initiate (requests, forms, appointments, registrations, payments) and what can they only view (records, balances, holds)?
4. What happens after a student submits something — routing, tracking, status visibility, notifications?
5. What knowledge/self-help machinery exists (KB articles, FAQ, AI answers) and how does it relate to requests?
6. What does the staff/admin side do (configure catalog/forms, triage, fulfill, publish knowledge, report)?
7. What varies by segment (higher ed vs K-12 vs continuing ed; service-catalog-centric vs records-centric vs retention-centric)?
8. What is common-but-not-definitional (mobile apps, AI assistants, SMS, events, personalization)?
9. Where are the boundaries (removal tests both directions) with the siblings above?

## Representative Products

| Product | Vendor | Pole | Tier |
|---|---|---|---|
| TeamDynamix client portal + public product KB | TeamDynamix | Service-management pole — portal as sign-in-gated front door with search, knowledge base, and applications (service catalog + ticketing across departments); vendor's own support portal runs on the product | Tier 1 (live product-run portal + official KB articles) |
| Ellucian Central Workspace (formerly Ellucian Experience) | Ellucian | Unified-campus-hub pole — role-based authenticated hub aggregating tasks, records access, and services across the institution's systems (student, finance, HCM) | Tier 2 (official product pages) |
| EAB Navigate360 — Student Engagement Hub | EAB | Retention/CRM pole — student self-service app/desktop (appointments, to-dos, holds, resources, self-reporting, journeys) as the student surface of a staff-side coordinated-care CRM | Tier 2 (official product page + FAQ) |
| PowerSchool Student Portal (K-12 SIS-attached view pole) | PowerSchool | K-12 records-view portal — authenticated student/parent view of grades, attendance, schedules, bulletins, fee transactions over the SIS | Tier 2 (official FAQ/resource pages) |

Selection rationale: four different vendors; four different product philosophies (service-catalog/service-management vs unified hub vs retention CRM vs SIS-attached records view); two segments (higher ed ×3, K-12 ×1); customer tiers from single schools to state systems and 850+ institution CRM deployments.

Considered and dropped (recorded limitations):
- **ServiceNow (CSM for higher education / student service portal)** — docs.servicenow.com is a JavaScript-only application (no content retrievable) and the product page timed out twice; abandoned per the network-restricted rule. No claims made about ServiceNow.
- **Anthology Student (self-service)** — docs.anthology.com now redirects to Blackboard developer docs; help.anthology.com returned no content. Abandoned.
- **TeamDynamix marketing site** — www.teamdynamix.com and all marketing URLs return 403; Wayback Machine timed out twice. Marketing positioning could not be directly verified; evidence limited to the vendor's live support portal and public product KB.

## Sources

Fetched 2026-09-09:

- TeamDynamix Solutions Portal (live client portal, product-run) — https://solutions.teamdynamix.com/TDClient/1965/Portal/Home/ and /KB/
- TeamDynamix KB article "Understanding Ticket Classifications: The differences between Incident, Major Incident, Problem, Change, Release, and Service Request" — https://solutions.teamdynamix.com/TDClient/1965/Portal/KB/ArticleDet?ID=2568
- Ellucian — https://www.ellucian.com/products ; https://www.ellucian.com/products/platform/central-workspace
- EAB — https://eab.com/technology/navigate (Navigate360 product page + FAQ)
- PowerSchool — https://www.powerschool.com/community-support/parent-student-resource-center/ (official student/parent portal FAQ)
- Bing search (source discovery only): powerschool student portal help documentation

Not reachable / degraded (recorded limitations): www.teamdynamix.com and all marketing paths (403, ×3 incl. two URL variants), web.archive.org (timeout ×2), docs.servicenow.com (JS app), www.servicenow.com product page (timeout ×2), docs.anthology.com → docs.blackboard.com (developer docs only), help.anthology.com (empty). One deployed-school portal observation (caisps.powerschool.com/public/ — leave application, report cards, attendance, car-service sign-up) was available only as a search-result snippet, not a fetched page — treated as corroborating, low-strength evidence.

## Product A — TeamDynamix (client portal + product KB)

### Key observations (Layer A unless noted)

- Live portal surface anatomy (observed on the vendor's own product-run support portal, solutions.teamdynamix.com): a **Sign In** gate (unique per-institution address pattern — "visit the unique web address assigned to your institution, e.g. myorganization.teamdynamix.com"), **Search** across portal areas ("Search all areas" / "Knowledge Base" filter), a **Knowledge Base** application with categories/articles/popular/recent lists/tags, an **Applications Menu** ("More Applications"), and a "Powered by TeamDynamix" footer. The portal's role as the client's front door to services and knowledge is directly observable.
- Product framing (Layer A, from KB chrome): the platform is described as an "ITSM/ESM or PPM platform" ("TDX Work Management"); admin KB categories cover "Work Management Admin — set up your ITSM/ESM platform" and "Using Service Management — day-to-day ITSM/ESM tasks".
- **Service request** as a first-class ticket classification (Layer A, official KB): "Service Request – A request from a user for information, advice, a standard change or access to an IT service… usually handled by a service desk" — one of six configurable ITIL-style classifications ("Incident, Major Incident, Problem, Change, Release, and Service Request").
- **Service catalog** as the organizing structure (Layer A, official KB, ITIL definition carried by the article): "provides a brief overview, in business terms, of all the business and infrastructure services offered by the IT provider and may include service charges."
- **Service desk** definition (Layer A, official KB): "The single point of contact between the service provider and users. A typical service desk manages incidents and service requests and handles communication with users."
- Configurability (Layer A, official KB): "Since these definitions may not perfectly suit the processes of a specific organization, these various classifications can be renamed and turned on or off as necessary. Service requests have a separate classification that can be created and used independently of a workflow." Parent/child ticket hierarchies; tickets can carry tasks, knowledge articles, assets/CI associations.
- Knowledge management practice present (Layer B — inferred from the KB's "kcs" [Knowledge-Centered Service] tag and knowledge-article association with tickets).
- Requester context (Layer A): tickets display the "Requestor's Data Card" — the request is bound to an identified person.
- SSO tags in the KB ("sso", "single-sign-on") indicate institution-identity integration (Layer B — tag-level evidence only).
- Limitation: marketing/positioning pages unreachable (403 ×3; Wayback ×2) — the vendor's "Student Services Portal" marketing claims could not be verified directly; all observations above come from the live portal and official KB articles.

## Product B — Ellucian Central Workspace (formerly Ellucian Experience)

### Key observations (Layer A, official product pages)

- Positioning: "A Productivity Hub for Every User — Deliver a unified, personalized digital experience for students, faculty, and staff. The central workspace connects people, tasks, and insights across your entire ecosystem — reducing friction in a single, centralized location."
- Hub character: "Through a centralized, secure, and customized hub, everyone — from the president to current students — gains one access point to essential information without switching screens or logging into multiple apps."
- Task/action orientation: "Drive Timely Actions Campuswide — Surface relevant information and next steps exactly when users need them, helping students complete tasks faster and staff manage priorities efficiently."
- Role-based personalization: "Tailor dashboards for each role, students, advisors, faculty, or executives, so everyone sees what matters most to them in one central experience." "Role-Based Digital Experiences — From course registration to payroll and advising, users get a personalized view of tasks and alerts."
- Aggregation across systems: "Insights at Your Fingertips — Integrate data from your student, finance, and HCM systems into one intuitive hub." Platform context: "Ellucian Platform — Transform faculty and student engagement with the leading SaaS platform."
- Student view: "One Hub for Student Life — Access classes, grades, schedules, and campus updates in one secure hub… without switching screens or logging into multiple apps."
- Multi-domain services named on one page: course registration, payroll, advising, rosters/grading (faculty), dashboards/reports (executives) — the one-hub-across-domains structure.
- Customer quotes corroborate the front-door role: "We've made a conscious effort to guide our students and staff through the central workspace as the entryway into our entire digital ecosystem" (PennWest); "With the implementation of [the Ellucian Platform's] central workspace, we left behind the era of siloed systems" (Universidad de los Andes).
- L3 detail: adoption stats (8.6M+ unique users, 500% increase in integration calls, 2.23M automated workflow runs) — marketing figures, not used in the final document.

## Product C — EAB Navigate360 (Student Engagement Hub)

### Key observations (Layer A, official product page + FAQ)

- Positioning: higher-education CRM ("Recruit, Retain, and Engage Students and Alumni"); staff side = "Coordinated Care Network" with "Complete Student Profile, Cases & Referrals, Automated Alerts & Messaging, To-Dos, Appointments & Surveys, Events, Notes & Attachments, Faculty Progress Reports".
- **Student surface as a named module**: "Navigate360's Student Engagement Hub serves as a comprehensive student engagement and voice platform… The student app — available for iPhone, Android, and desktop — gives students structure for the college journey, proactive guidance at pivotal moments, and creates opportunities for meaningful conversations between students and schools."
- **Student self-service** (FAQ, Layer A): "All Navigate360 partners receive a self-service student mobile application and desktop experience. Student self-service features for student success include appointment scheduling, access to campus resources and documents shared by their advisors, To-Dos, Student Journeys, and more… students will have Navigate360 with them as an invaluable tool to manage their own journey."
- Student engagement module inventory (Layer A): "AI Student & Prospect Knowledge Agent, Two-way Conversations & SMS Messaging, Student Surveys & Quick Polls, Program Advising, Career Match & Journeys, Sentiment Analysis, **Holds Center**, Study Buddies, Financial Planner, Program Explorer, Prospect Portal, **Student Hand Raise (Self-Reporting Concern Feature)**."
- Population substrate: "The main source of data used to populate Navigate360 comes from the institution's student information system (SIS)… Partners may also choose to integrate learning management system (LMS) data… as well as Common App data… custom data sets, such as financial aid data, housing data." Pre-built integrations named: Ellucian, Jenzabar, Oracle PeopleSoft, Workday Student, Canvas, Blackboard, Brightspace, Moodle.
- Who uses it: "Current students, prospective students, faculty, staff, and administrators all use Navigate360 as part of a Coordinated Care Network" — staff across "advising, enrollment, career services, and tutoring".
- Privacy/compliance stance (Layer A): "EAB is in compliance with FERPA and GDPR practices and requirements."
- Delivery: "cloud-based SaaS solution hosted on AWS… accessible via web browsers and includes a dedicated mobile app for students."
- L3 detail: retention/graduation improvement percentages, 10M students served, 850+ institutions, predictive-model counts, "Prospect Portal", "Study Buddies", Forage job-simulation integration — vendor statistics and branded modules, not used in the final document beyond variant illustration.

## Product D — PowerSchool Student Portal (K-12 pole)

### Key observations (Layer A, official FAQ/resource pages)

- **Student portal definition** (Layer A, official FAQ): "The student portal is an online portal accessible anywhere on the web that students can log in to and see their grades, assignments, scores, attendance, schedules, school bulletin, and more."
- **Parent portal sibling** (Layer A): "The parent portal is an online portal… parents can log in to and see all of their children in one place, their grades, assignments, scores, attendance, schedules, and school bulletins for each school your children attend."
- **Institution-granted identity** (Layer A): "PowerSchool logins are granted by schools and districts. Each school will verify your identity before giving you an account to help protect student data and privacy." Parents link children via school-issued Access IDs.
- **Per-institution configurability** (Layer A): "Features such as GPA, assignment grades, and schedule are configured on a school-by-school basis by your school district's PowerSchool administrators." Portal URLs are unique per school/district.
- **Mobile app** (Layer A): "Receive real-time push notifications with updates about grades, scores, attendance, assignments, teacher comments, daily bulletins, schedules, and **fee transactions**"; "Access all of your children in one portal."
- Deployed-portal service actions (Layer B, low strength — search-result snippet of a PowerSchool-hosted school portal): "submit Leave Application (new), view Report Cards, view Attendance Record, sign up for Private Car Services" — indicates that deployed K-12 portals on this platform can carry student-initiated service actions (forms/sign-ups) alongside the records view.
- Boundary-relevant: the K-12 pole is records-view-centric; its aggregation spans domains of one system (the SIS) plus whatever service forms the school enables. MyPowerHub branding (parent.powerschool.com) is L3.

## Cross-product Comparison

| Dimension | TeamDynamix (service-management pole) | Ellucian Central Workspace (hub pole) | EAB Navigate360 (retention/CRM pole) | PowerSchool portal (K-12 records-view pole) |
|---|---|---|---|---|
| Authenticated personal front door | Sign-in gate; per-institution address; SSO tags | "centralized, secure, and customized hub… one access point" | student app/desktop on institution's SIS-fed population | "logins are granted by schools and districts"; identity verified by school |
| Aggregation scope | services across departments via service catalog + applications menu + KB | "student, finance, and HCM systems" in one hub; registration/payroll/advising named together | multi-office care network; SIS+LMS+CRM+custom data (financial aid, housing) | multiple domains of one SIS: grades, attendance, schedules, bulletins, fees |
| Student-initiated actions | service requests (ticketed) | task completion; navigation to services ("course registration") | appointment scheduling, hand-raise self-reporting, surveys | account preferences; deployed portals add forms/sign-ups (snippet-level); fee transactions in app |
| Institution-initiated content | none observed on portal surface | tasks/alerts surfaced "exactly when users need them" | to-dos, documents shared by advisors, journeys | grades/announcements push; teacher comments |
| Tracked state visible to student | ticket lifecycle + notifications | task status, alerts | to-dos, holds, appointments | push notifications about changes |
| Knowledge/self-help | KB with categories/search/tags (KCS practice) | guidance surfaced in hub | "AI Student Knowledge Agent — governed, institution-approved guidance" | — (vendor FAQ is external to product) |
| Staff side | service desk + ticketing applications + workflows | staff manage priorities in same hub | Coordinated Care Network, cases & referrals, campaigns | school admins configure features per school |
| Mobile app | TeamDynamix Mobile (KB evidence) | — (device-consistent UI claimed) | dedicated student app (iPhone/Android/desktop) | PowerSchool Mobile with push notifications |
| Records visibility | — (not the center) | classes, grades, schedules | student profile incl. documents | grades/attendance/schedule = the center |

### What survives across all four (Layer B)

1. An **authenticated front door bound to the institution's student population** — the person signs in as themselves and the surface operates on their own business. (4/4)
2. **Aggregation of multiple service domains behind one surface** — spanning offices and/or systems, not one office's tool. (4/4)
3. **Self-service actions** the student performs on their own business — requests, forms, tasks, appointments, sign-ups, account changes. (4/4; weakest at the K-12 records-view pole)
4. **Visibility of the student's own state** — records, tasks, holds, request status, notifications. (4/4)
5. **A staff/administrative side** that configures the surface and handles what students initiate. (4/4)

Common-but-not-universal (Layer B): knowledge/self-help layer (3/4 — TDx, EAB, Ellucian loosely); notifications/push (3/4); mobile app (3/4); role-based personalization (2/4 explicit — Ellucian, EAB); institution-initiated task/hold content (3/4 — Ellucian, EAB, PowerSchool announcements); appointment booking (1/4 explicit — EAB; advising appointments are named by Ellucian as a domain).

## Canonical Model

### L0 — Defining Invariant (minimal, jointly-held)

Three structures. If any one is removed, the product stops being recognizable as a student services portal.

1. **The student's authenticated front door to the institution.** The person signs in under an institution-granted identity bound to the institution's student population, and the surface operates on that student's own institutional business (their records, tasks, requests — not anyone else's). Remove → a public website; remove the institution-student binding → a generic constituent portal (customer/employee/government portal family).
2. **One-stop aggregation of the institution's student services.** Services spanning more than one office or domain — registrar/records, financial, housing, IT, health, advising, and so on — are reachable through this single surface; the portal is a front door to the institution, not a single office's tool. Remove → a departmental service desk or one office's form.
3. **The two-way self-service loop.** The student initiates service actions on the surface (submit a request or form, complete a task, book an appointment, register, pay) and the institution handles them on its side; the state of the student's own business — request status, tasks, holds, records — is visible and tracked on the surface. Remove → a read-only records display (the SIS-view pole / information-portal territory) or a personal checklist with no institutional counterpart.

Jointly-held load-bearing:
- 1 alone = a login page.
- 2 without 1+3 = an information portal.
- 3 without 2 = a single department's service desk.
- 1+2 without 3 = an authenticated records view — the K-12 SIS-view pole; boundary documented below, not part of the strict core.
- 1+3 without 2 = departmental self-service (help-desk-shaped), not a student services portal.
- 2+3 without 1 = a public service catalog with anonymous requests — Government-Service-Portal-shaped machinery without the student binding.

### L1 — Common Mature Structure

- Knowledge/self-help layer — searchable knowledge base, FAQ/guided answers, increasingly governed AI assistants answering student questions before a request is needed.
- Records/balance/hold visibility — grades, schedules, balances, holds surfaced in the portal (commonly SIS-fed).
- Task/checklist layer — to-dos and required actions assigned by offices, completed by students.
- Appointment booking with offices/advisors.
- Notifications — in-app, push, email, SMS updates about state changes.
- Role-based personalization — dashboards tailored per role (student, advisor, faculty, staff).
- Search across the portal's services and knowledge.
- Mobile app as a companion surface.
- Integration substrate — SIS (population/records), LMS, finance/ERP, identity/SSO.

### L2 — Variant / Optional Structure

- Which domains are in scope — whole-campus service catalog vs SIS-records-centric view vs retention/success surface vs financial-aid-only or IT-only deployments.
- Segment grammar — higher-ed service-catalog portal vs K-12 records+forms portal vs continuing-ed/non-credit self-service.
- Prospective-student (pre-enrollment) portal variants.
- Two-way messaging/SMS and live chat.
- Events, engagement content, community features.
- Multi-institution/system deployments.
- Payment as one service action among many (the receivables loop itself is Student Billing territory).
- Deployment substrate — standalone portal products, ITSM/ESM-platform portals, SIS/ERP-attached self-service, CRM-attached engagement hubs.

### L3 — Vendor-specific Structure (research notes only)

- TeamDynamix: "TDClient" client portal, "TDX Work Management" framing, ITIL classification vocabulary (renamable), KCS practice, per-institution portal addresses (myorganization.teamdynamix.com pattern).
- Ellucian: "Central Workspace"/"Experience" naming, "Ellucian Platform" packaging, marketing stats (8.6M+ users, 2.23M workflow runs).
- EAB: "Student Engagement Hub", "Student Journeys", "Holds Center", "Student Hand Raise", "Study Buddies", "Program Explorer", Forage integration, retention/ROI percentages, 850+ institutions, AWS hosting statement.
- PowerSchool: MyPowerHub branding, Access ID mechanism, District Code, mobile-app specifics, per-school feature-disable behavior.
- ServiceNow: not researched (inaccessible) — no vendor-specific claims recorded.

## Vendor-specific Findings

- The term "Student Services Portal" could not be verified as a named vendor product on TeamDynamix's site (blocked); the directory leaf name is treated as the market's common phrase for the Type, evidenced by the service-catalog portal pole's structure rather than a vendor's marketing label.
- EAB's "Holds Center" is the only direct in-sample evidence of holds machinery; hold-gating mechanics (what holds block, how they clear) were not verified — carried as an uncertainty; holds are documented as variant-level, not definitional.
- The K-12 form/sign-up evidence (leave application, car-service sign-up) is snippet-level — used only as corroboration that the records-view pole can carry service actions, not as a structural claim.

## Boundary Findings

Removal tests (both directions):

- **vs Student Information System (processed)**: the SIS is the record system of record (enrollment, grades, attendance as authoritative data + school operations). The portal is an interaction surface: it presents SIS-fed state and carries service actions; it does not own the record. Remove the record authority → still a portal; remove the portal surface → still an SIS. Bundling (portals shipped inside SIS suites) is packaging.
- **vs Student Case Management (processed; sibling flag discharged)**: the portal resolves student-initiated service transactions (a request submitted, fulfilled, closed; a task completed; an appointment held). Case management is issue-driven sustained casework — an assigned staff owner working a documented case over time. The portal's staff side triages/fulfills; it does not work cases. Confirms the case-management pass's recorded seam ("service-request/transaction resolution vs sustained casework"). Keep both.
- **vs Student Success Platform (unprocessed)**: the retention platform's center is staff-side population management (campaigns, alerts, intervention measurement). Its student-facing surface (appointments, to-dos, resources) is portal-shaped — center-of-gravity seam expected. FLAG left for that pass: confirm the seam and whether its student surface is documented as a portal capability or the platform's own Type.
- **vs Parent Portal (unprocessed)**: same portal family, guardian-facing; the K-12 parent portal is the record-view sibling of the student-facing SIS view. Keep both; the student services portal is service/action-centric, the parent portal record/communication-centric per current evidence.
- **vs Customer Portal / Employee Portal / Government Service Portal**: identical constituent-portal machinery; the population and service context differ (consumers of a business, employees, citizens vs enrolled students of an education institution). Population swap, not separate structures.
- **vs Help Desk / Self-service Support Portal (§07)**: single-provider support/knowledge machinery. The student services portal spans the whole institution's offices under the student identity; where a portal is one department's (IT) it remains help-desk territory. ESM platforms can realize either — the aggregation scope is the discriminator.
- **vs Information Portal (§02.11)**: aggregation without authentication/personalization/self-service. Remove leg 1+3 and the Type collapses into it.
- **vs Academic Advising Platform (processed)**: the advising relationship system may expose its booking surface through the portal; the portal aggregates, advising manages the relationship and its casework-adjacent objects.
- **vs LMS / Virtual Classroom**: learning delivery (content, assignments, live teaching) vs administrative services. Course-related records may appear in portals; the LMS remains a different Type.
- **vs Student Billing System (processed)**: the portal commonly carries a view/pay touchpoint as one service action; the receivables loop (invoicing, payment plans, collections) is the billing system's. Confirms the billing pass's "no overlap — money loop vs service surface" note.
- **K-12 SIS-view pole (taxonomy observation)**: the directory has a Parent Portal leaf but no separate "student-facing SIS view" leaf. A read-only K-12 student records portal sits between this Type (lacks the action leg) and Parent-Portal-family territory (same SIS-view machinery, student-facing). If the directory ever wants that pole as its own leaf, it should be created as the Parent Portal's student-facing sibling — not folded silently into this Type. Recorded as a boundary issue; no directory change made.
- **Higher-ed "one-stop student services" programs**: institutional initiatives (one-stop shops for registrar+aid+records) are the business practice this Type digitizes; not a separate Type.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit? Yes — the three-leg core requires only an authenticated personal front door, multi-domain aggregation, and the self-service loop with visible state. A 2000s-generation SIS web self-service portal (registration + records + account balance + forms, no mobile app, no knowledge base, no AI) satisfies all three legs. Regional one-stop service-portal deployments (e.g., European or Asian university portals) satisfy the legs without any US-specific machinery. The paper-era analog — the multi-office service counter plus mail-in forms plus posted records — is conceptual lineage only (no software), but it shows the definition is not tied to the current mobile/AI implementation. Conversely, features common in today's market (AI assistants, SMS two-way, journeys, push apps) are deliberately kept out of the core.

## Uncertainties

- ServiceNow — entirely unreachable; the enterprise-ESM pole rests on TeamDynamix alone. The service-catalog/request-loop structure is additionally supported by the pole's public KB (Tier 1) but is single-vendor at the product level; cross-product support for that pole is therefore Layer B at best.
- TeamDynamix marketing positioning (exact "student services" packaging) unverified — all TeamDynamix evidence is from its live portal and product KB.
- Exact request-lifecycle states (names, timing, escalation rules) not researched — the final document describes the lifecycle conceptually.
- Hold mechanics (what holds gate, how they clear) verified only as a named module at one product — held variant-level.
- K-12 deployed-portal service actions — snippet-level corroboration only.
- The unprocessed siblings (Student Success Platform, Parent Portal, Academic Advising Platform — advising is processed but its portal interplay was not re-verified) may refine the seams recorded here; flags left accordingly.

## Final Synthesis

The Student Services Portal is the education institution's student-facing self-service front door. Its defining core is three jointly-held structures: (1) the student's authenticated front door — institution-granted identity binding the signed-in person to their own business with the institution; (2) one-stop aggregation — services spanning multiple offices/domains reachable through one surface, the front door rather than a single office's tool; (3) the two-way self-service loop — the student initiates service actions (requests, forms, tasks, appointments, registrations, payments) that route into institutional handling, with the state of the student's own business (request status, tasks, holds, records) visible and tracked on the surface. Around this core, mature products add the knowledge/self-help layer, records/balance/hold visibility, task checklists, appointments, notifications, role personalization, search, and mobile apps. The market realizes the Type through several product shapes — service-catalog/service-management portals, SIS/ERP-attached unified hubs, CRM-attached engagement hubs, and K-12 SIS-attached records views — which differ in emphasis but share the core. Boundaries: the SIS owns the record (the portal presents and acts), case management works sustained concerns (the portal resolves transactions), the success platform manages populations on the staff side (the portal is its student surface), the portal family swaps populations (customer/employee/government), and single-department portals are help-desk territory.
