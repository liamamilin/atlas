# Research Notes — Customer Training / Academy Platform

## Research Goal

Understand what a Customer Training / Academy Platform really is as an Application Type: its defining structure, standard capabilities, lifecycle and rules, and its boundaries against neighboring Types. This pass also carries a **joint-review obligation** recorded by the corporate-lms pass (2026-09-07): that pass drew the seam as "audience variant — identical machinery; learner population is customers/partners rather than employees; remove the employee population → customer training remains" and left ratification to this pass. This pass therefore (a) researches the customer-education market independently with a pure-play-weighted product sample, and (b) resolves the keep-both-vs-variant question from this side.

## Initial Boundary

- Leaf: **Customer Training / Academy Platform** (DIRECTORY §07 Sales, Customer & Revenue, line 596).
- Working hypothesis: software a company operates to train its own customers (and partners) — a branded "academy" where external learners take courses about the company's products, with tracked progress and certification.
- Nearest neighbors suspected up front: **Corporate LMS** (§09, processed — pre-held seam), **LMS** (§23, education), **MOOC Platform** (§23), **Educational Content Platform** (§23, processed), **Customer Onboarding Platform** (§07, unprocessed), **Customer Success Platform** (§07, processed), **Partner Relationship Management** (§07, unprocessed), **Product Usage / Adoption Platform** (§07, unprocessed), **eLearning Authoring Tool** (§23, processed), **Digital Credential Platform** (§23, unprocessed), **Customer Community / Community Platform** (§01.06/§25).

## Research Questions

1. Who operates the platform, and who are the learners? What is the relationship between them?
2. What are the core objects (academy/site/domain, course, path, lesson, enrollment/registration, progress, certificate)?
3. How do external learners get in — self-registration, SSO, invitation, access codes, purchase, entitlement?
4. How is the academy surface shaped (branding, domains, catalogs, per-audience portals)?
5. What role does monetization play (paid courses, subscriptions, credits, licenses)?
6. How does the platform connect to the operator's business systems (CRM, customer success, support, product)?
7. What records are kept and what are they used for (certification, adoption evidence, renewal support)?
8. Is this Type structurally distinct from Corporate LMS, or one Type with an audience switch? (joint review)
9. Where is the seam vs customer onboarding, customer success, and partner management?

## Representative Products

| Product | Segment / philosophy | Evidence level reached |
|---|---|---|
| **Skilljar** (Gainsight) | pure-play customer-education LMS ("External LMS"), mid-market→enterprise SaaS; now CS-suite-adjacent | Tier-1 help center (Gainsight support), 6 pages incl. framework article, Create/Manage guide maps, domain-access article + Tier-2 product site |
| **Thought Industries** | pure-play "Customer Learning & Intelligence Platform" with learning-business architecture (client academies, monetization) | Tier-1 help center (Zendesk), 4 category pages + Tier-2 product site |
| **Docebo** | extended-enterprise LMS — one platform for employees + customers + partners (unified-platform pole) | Tier-2 product pages (customer education, extended enterprise) + Tier-1 help center root; operational detail corroborated by the corporate-lms pass's Docebo fetches |
| **Intellum** | enterprise customer/partner education platform (Fortune-500 pole) | Tier-2 product pages only (help center unreachable ×2) |

Rejected/abandoned: Intellum help.intellum.com + knowledge.intellum.com (transport error ×2 each), Northpass help.northpass.com (404 ×1 — SMB pure-play pole under-sampled), LearnUpon (unreachable in the sibling pass; not retried).

## Sources

- Skilljar product site — https://www.skilljar.com/ — fetched 2026-09-08
- Gainsight Support — Skilljar guide root — https://support.gainsight.com/Skilljar — fetched 2026-09-08
- Skilljar — Understanding the Skilljar Framework — https://support.gainsight.com/Skilljar/Get_Started!/Getting_Started/Understanding_the_Skilljar_Framework — fetched 2026-09-08
- Skilljar — Create guide (Courses/Lessons/Quizzes/Live Training/Catalog Pages/Plans/Learning Paths/SCORM) — https://support.gainsight.com/Skilljar/Create — fetched 2026-09-08
- Skilljar — Manage guide (Students/Registration & Enrollment/Access/Domains/Groups/Completion/Certificates/Purchasing & Monetization/Dashboard Users) — https://support.gainsight.com/Skilljar/Manage — fetched 2026-09-08
- Skilljar — Domain Access: Public, Logins, and Access Codes — https://support.gainsight.com/Skilljar/Manage/Access/Domain_Access%3A_Public%2C_Logins%2C_and_Access_Codes — fetched 2026-09-08
- Thought Industries product site — https://www.thoughtindustries.com/ — fetched 2026-09-08
- Thought Industries Help Center root — https://support.thoughtindustries.com/ — fetched 2026-09-08
- Thought Industries — Content category — https://support.thoughtindustries.com/hc/en-us/categories/360003519553-Content — fetched 2026-09-08
- Thought Industries — User Management category — https://support.thoughtindustries.com/hc/en-us/categories/360003519593-User-Management — fetched 2026-09-08
- Thought Industries — Panorama category — https://support.thoughtindustries.com/hc/en-us/categories/360003495554-Panorama — fetched 2026-09-08
- Docebo — Customer Training LMS solution page — https://www.docebo.com/solutions/customer-education/ — fetched 2026-09-08
- Docebo — Extended Enterprise product page — https://www.docebo.com/products/extended-enterprise/ — fetched 2026-09-08
- Docebo Help & Support root — https://help.docebo.com/ — fetched 2026-09-08
- Intellum product site — https://www.intellum.com/ — fetched 2026-09-08
- Intellum — Customer Education Platform page — https://www.intellum.com/solutions/customer-education — fetched 2026-09-08
- Sibling-pass sources (Docebo help articles, Absorb, 360Learning, TalentLMS, LearnUpon) — fetched 2026-09-06/07, recorded in research/corporate-lms.md

Failed/abandoned: help.intellum.com (transport error ×2), knowledge.intellum.com (transport error ×2), help.northpass.com (404 ×1), knowledge.thoughtindustries.com (timeout ×1 — Zendesk mirror reachable instead).

## Product A — Skilljar (Tier-1, directly observed)

### Key observations

**Object structure (framework article, directly observed):**
- **Organization** = the top-level parent company providing the training; manages everything via the Skilljar **dashboard** (admin side) and is responsible for its content.
- **Training Domain** = "the main web page that hosts the organization's training experience"; Skilljar supports **single or multiple domains** "so you can cater your training to different audiences, such as customers, partners, and internal employees." Custom domain + SSL supported; domains are SEO-relevant web properties.
- **Catalog Pages** = "libraries of training courses, learning paths, and even other catalog pages" within a domain — "a file/folder system that allows you to organize your content and tailor it to specific audiences"; builder pages supported; per-page home pages.
- **Courses** = the delivery unit, made of **sections and lessons**; course lifecycle: draft → publish → unpublish → archive; clone; prerequisites; start/end dates; due dates; course families; content syndication; public preview links; slugs/URL redirects; duration and credit/units display.
- **Lessons & content** = building blocks: text, video, audio, PDF, embedded pages, PowerPoint/Google Docs embeds, **quizzes**, **live training events**, virtual labs, **SCORM** packages, **LTI** lessons; sequential navigation or free-form; optional lessons; lesson completion rules per type (video watched, audio done, SCORM completion, quiz passed); lesson score as course score; student assignments (submissions graded by admins).

**Live training (directly observed):** events with locations or virtual meeting links, multi-session events, waitlists, registration close, bulk add students, calendar display, reminder emails, event tags, universal join links (VILT), and post-event updates of scores/success status/attendance for past events.

**Learning paths & plans (directly observed):** ordered learning paths (courses in sequence, layouts, charging for paths, xAPI/cmi5 support); **Plans** = entitlement bundles — a course or path can be made "available as part of a plan only"; groups can be created based on plans; students can be deactivated from a plan.

**Access model (Domain Access article, directly observed):**
- Three domain access levels: **Public** (catalog visible to everyone, discoverable by search engines — "great if you're selling training"), **Login required** (catalog visible after sign-up; sign-up fields capture attributes like job title or software version used to route learners), **Access code required** (sign-up + code provided by the organization or purchased via subscription; codes apply at domain level only; direct invitations bypass codes).
- **SSO** per domain; "login required with SSO is the most private option and is often used for customer-only and internal product training."
- Registration is the norm: "Users will still need to sign up and register to access your courses, no matter which level."
- **Multiple domains**: related audiences (public lead-gen domain → customer SSO domain, with cross-domain access preserving training progress when a prospect becomes a customer) vs unrelated audiences (internal vs external with different SSO, treated as fully separate).
- Per-object visibility: courses, catalog pages, plans, and published paths can be made visible to select groups.

**Students & groups (directly observed):** student profile pages; merging student records; editing a student's lesson/course progress; self-service re-enrollment; disabling enrollments; PII removal; sign-in-as-student; password resets; **Student Managers** ("External Management" — customer-side people who manage their own learners); groups with membership rules that enroll members into courses/paths/plans, auto-grouping by email domain or sign-up fields, group categories, per-group default home pages.

**Certificates (directly observed):** create/issue certificates; **recurring certification programs**; certificates for catalog pages; customization; branded certificate verification URLs; manual issuing; LinkedIn sharing; integrations with Credly, Accredible, Caveon (proctored exams).

**Monetization (directly observed):** course/path/plan pricing; promo codes; group-based discounts; **subscriptions to a domain or training portal**; **training credits** (admin and learner sides, credit reports); **license packages**; bulk purchasing; order reports; custom receipts; external payment processors; multi-currency offers; purchase quantity limits; Stripe/PayPal/Salesforce payment integrations.

**Dashboard & operations (directly observed):** dashboard users with roles and permissions (custom roles, SCIM provisioning); audit logs; branded emails and announcements with customization variables; registration/completion email notifications; course announcements; task notification emails.

**Data & integrations (directly observed):** Data Connector (raw data export); reporting on enrollments and engagement with custom/exportable reports; native integrations with **Salesforce** (account-level insights, training data in Salesforce), **Gainsight** (CS), Google Analytics, Zoom, Webex, GoTo, Zendesk; public APIs.

**Positioning (Tier-2):** "The External LMS" for customer education; three pillars — design learner experiences, monetize training content, deliver business impact ("link training with NPS, adoption, and customer retention"); MCP server in beta; academy showcase.

**Vendor-specific (L3):** Training Domain/Catalog Pages/Plans/Training Credits/License Packages/Student Managers terminology; domain-level access codes; cross-domain progress preservation; course families; content syndication; hCaptcha on sign-up.

## Product B — Thought Industries (Tier-1 help center + Tier-2 site)

### Key observations

**Content model (directly observed):** content types — **Courses, MicroCourses, Videos, Articles, Learning Paths**; courses composed of **page types** (text, slideshow, presentation, video, discussion assignment, list roll, and more — 27 documented page types); content folders; templates folder; course annotations; **Events Manager** for live events; course settings including **manager assignment**, admin resource library, **copying a course from sandbox to production**, uploading third-party certificates, waitlisting, manual grading of surveys/quizzes/tests.

**E-commerce settings (directly observed):** managing free registration, pricing & availability per content; content-specific coupons; free preview lessons.

**Learner experience (directly observed):** external activity recording; recommendation assessment & engine; **assigned programs**; sharing certificates on LinkedIn; learners archiving content from their dashboard; admins taking assessments on behalf of learners.

**User management (directly observed):** **registration codes** (control site access) and **redemption codes** (manage learners); invitations; bulk import/update of learners; admin users; **manager-learner dual role**; auto assignment; impersonating a learner; refunds; deleting a learner's credit card on file.

**Panorama (directly observed — the learning-business architecture):** a **Panorama** is a client account: its own branding, **license separation**, **sublicenses**, **seat allocation**, its own reporting, content authoring scoped to the panorama, purchasable content added to a panorama, **B2B group subscriptions**, custom email settings, and **moving learners between panoramas** (individual and bulk, with FAQs). This is the machinery for an organization that runs many separately-branded, separately-licensed customer academies on one platform.

**Positioning (Tier-2):** "Customer Learning & Intelligence Platform"; AI-first (conversational AI learning with cited answers, answer-engine optimization surfacing content in ChatGPT/Claude/Google/Perplexity, AI content creation incl. authoring from inside Claude); personalization across products/audiences/regions/languages; monetization (subscriptions, bundles, native eCommerce, licensing for individuals/groups/organizations); measurement (learning connected to adoption, retention, revenue; BI connector); audiences: customer training, partner enablement, member education, professional learning, education as marketing, employee L&D.

**Vendor-specific (L3):** Panorama/sublicense/seat-allocation machinery, MicroCourses, registration-vs-redemption code split, sandbox→production course promotion, AEO, BI Connector.

## Product C — Docebo (Tier-2 product pages + help root; operational detail corroborated by sibling pass)

### Key observations

**Extended Enterprise definition (product page, directly observed):** "Extended Enterprise learning is any training, knowledge, certification, or performance support provided to audiences outside your organization, such as customers, channel distribution partners, resellers, dealers, franchises, and members."

**Multi-audience architecture (directly observed):** "You can set up multiple extended enterprise experiences with different administrative rights and distinct branding elements to each audience" — e.g., one for franchisees, one for channel partners, one for resellers, one for customer training — all off a single instance; per-audience catalogs; configuration "even at the individual learner level" (new customer sees onboarding content, established user sees a different experience); white-labeling; **Docebo Pages** for audience-specific look/feel; sub-administration with scoped permissions.

**Customer-education posture (solution page, directly observed):** accelerate onboarding/adoption/growth; turn support into self-sufficiency ("cutting support costs"); scale without complexity (automate workflows, localize content, reach every customer segment); prove impact ("connect learning data to real business outcomes... product usage, satisfaction, and renewal"); connect the ecosystem (CRM, support, community tools).

**Commerce (directly observed):** e-commerce app to sell courses ("creating your own marketplace"), pricing models (subscription, pay-per-course); payment gateways incl. PayPal, Authorize.net, Adyen, Stripe SCA, CyberSource; Shopify integration.

**Help center structure (directly observed):** categories for Users, Courses and learning plans, Training material, Content marketplace, Analytics, E-commerce, SSO, Integrations, Mobile learning, Compliance, Communities and social learning, AI — the same LMS engine serving all audiences.

**Vendor-specific (L3):** Extended Enterprise app, branches, Docebo Pages, Harmony AI/AgentHub, Content Marketplace, Headless Learning, Companion, Mobile App Publisher. Operational detail (enrollment rules, branches) recorded in the corporate-lms pass's research.

## Product D — Intellum (Tier-2 only)

### Key observations

**Positioning (directly observed):** "AI-powered enterprise learning platform"; solutions: Customer Education, Partner Education, Employee & Field Performance, Product Adoption & Onboarding, Certifications at Scale. Customer-education FAQ self-definition: "A customer education platform is software for training the people who use your product, including onboarding, courses, certifications, and resources."

**Customer-education capabilities (directly observed, product-page level):** customer certification programs ("build and update certification programs in minutes"); ongoing skills development (AI-recommended content based on usage patterns, support cases, or feedback); **adaptive onboarding** (tailored by role, product plan, or use case; dynamic learning paths adjusting as customers progress); **feature launch campaigns** (identify customers needing training on new releases; trigger targeted content); impact analytics (learning activity connected to retention, expansion, advocacy; warehouse export; conversational reporting).

**Organizations (directly observed):** "Intellum's Organizations give each audience its own branded subdomain, logo, colors, and navigation, so customers move into your academy without feeling like they left your brand."

**Commerce & scale (directly observed):** paid courses via Stripe; certifications and credentials; Meta case study "2M+ external learners enabled"; products: Intellum LMS, Evolve authoring, Analytics & Insights, Integrations & API, Services.

**Vendor-specific (L3):** Organizations, Evolve, Creator/Manager/Learner AI agents, Education-Led Growth framing.

## Cross-product Comparison

| # | Finding | Skilljar | Thought Industries | Docebo | Intellum | Strength |
|---|---|---|---|---|---|---|
| 1 | Operator = an organization training people outside its workforce; learners are customers/partners/members | ✓ (domains for "customers, partners, and internal employees") | ✓ (customer/partner/member/professional audiences) | ✓ ("audiences outside your organization") | ✓ ("the people who use your product"; "2M+ external learners") | A×2 + B×2 |
| 2 | Branded customer-facing academy surface (custom domain, theming, public catalog) | ✓ (training domains, custom domain+SSL, SEO) | ✓ (site design category; per-panorama branding) | ✓ (white-label, Docebo Pages) | ✓ (Organizations: subdomain/logo/colors/navigation) | A×2 + B×2 |
| 3 | Managed learning offerings: courses composed of lessons/pages; paths; live events | ✓ (courses→sections→lessons; paths; live training) | ✓ (courses/page types; paths; events manager) | ✓ (courses, learning plans; ILT) | ✓ (courses, certifications, paths) | A×2 + B×2 |
| 4 | Self-service external learner access under organization-set admission rules | ✓ (public/login/access-code domain levels; SSO; invitations) | ✓ (registration/redemption codes; invitations; free vs priced registration) | ✓ (per-audience experiences; SSO category) | ✓ (branded academies; adaptive onboarding entry) | A×2 + B×2 |
| 5 | Tracked per-learner progress/completion records | ✓ (course/lesson completion; progress editing; reports) | ✓ (reporting & notifications; Panorama reporting) | ✓ (analytics category; completion tracking) | ✓ ("tracks completion for every customer") | A×2 + B×2 |
| 6 | Certification/credential outputs | ✓ (certificates, recurring certification programs, verification URLs, Credly/Accredible/LinkedIn/Caveon) | ✓ (certificates on LinkedIn; third-party certificate uploads) | ✓ (certification in extended-enterprise definition) | ✓ (customer certification programs; credentials) | A×2 + B×2 |
| 7 | Multi-audience / multi-portal architecture (separate branded experiences per audience or per client) | ✓ (multiple domains; related vs unrelated audience patterns) | ✓ (Panorama client accounts, sublicenses) | ✓ (multiple extended-enterprise experiences off one instance) | ✓ (Organizations per audience) | A×2 + B×2 |
| 8 | Monetization of training (prices, subscriptions, credits/licenses, bulk B2B purchase) | ✓ (full purchasing & monetization guide) | ✓ (ecommerce settings; B2B group subscriptions; Panorama purchasable content) | ✓ (e-commerce app; gateways) | ✓ (Stripe; paid courses) | A×2 + B×2 |
| 9 | Business-system integration: CRM / customer success / support / webinar tools | ✓ (Salesforce, Gainsight, Zendesk, Zoom/Webex/GoTo, Google Analytics) | ✓ (integrations category; BI connector) | ✓ (CRM/support/community; Salesforce/Okta) | ✓ (usage patterns/support cases feeding recommendations; warehouse) | A×2 + B×2 |
| 10 | Adoption/retention framing of success (education measured against business outcomes) | ✓ ("link training with NPS, adoption, and customer retention") | ✓ ("adoption, retention, and growth") | ✓ ("product usage, satisfaction, and renewal") | ✓ ("retention, expansion, and advocacy") | A×2 + B×2 |
| 11 | Content sourcing: native authoring + standards import (SCORM/xAPI/LTI) | ✓ (native lessons; SCORM; LTI; xAPI/cmi5) | ✓ (native page types; AI authoring) | ✓ (authoring; SCORM marketplace) | ✓ (Evolve authoring) | A×2 + B×2 |
| 12 | Learner-side management (customer-side managers oversee their own people) | ✓ (Student Managers) | ✓ (manager-learner dual role; manager assignment) | n/o (sampled pages) | n/o | A×2 — common, not universal |
| 13 | Live training events with registration/waitlists/attendance | ✓ (rich live-training guide) | ✓ (events manager; waitlisting) | ✓ (ILT; Booking.com story) | n/o (positioning) | A×2 + B — common |
| 14 | Groups/segments targeting content and enrollment | ✓ (groups with membership rules) | ✓ (auto assignment; B2B group subscriptions) | ✓ (groups/branches per sibling pass) | n/o (positioning) | A×2 + B(sib) — common |
| 15 | Community/social learning | n/o (sampled pages) | ✓ (discussion assignment pages) | ✓ (communities product; social category) | n/o | A×1 + B — optional |
| 16 | In-app/embedded learning surfaces | ✓ (in-app positioning; MCP beta) | ✓ (conversational AI in flow of work) | ✓ (Companion; headless; embedded launcher) | n/o | A×2 + B — modern layer, optional |
| 17 | AI assistance (authoring, tutoring, recommendations, conversational answers) | ✓ (AI features page; MCP) | ✓ (AI-first positioning) | ✓ (Harmony/AgentHub/Content Creator) | ✓ (Creator/Manager/Learner agents) | A×2 + B×2 — era-current, not definitional |
| 18 | Education-as-marketing / lead-gen academies (public ungated content for prospects) | ✓ (public domain pattern; pre-customer domains) | ✓ (education as marketing audience) | n/o (sampled pages) | n/o | A×2 — variant |
| 19 | Learning-business posture (training sold as a product line with client licensing) | partial (subscriptions, licenses) | ✓ (Panorama sublicenses, seat allocation) | partial (marketplace) | partial (Stripe) | A×1 strong — variant pole |
| 20 | Compliance/audit depth (corporate-style mandatory training machinery) | light (audit logs present) | light | ✓ (compliance category — shared engine) | n/o | B — variant, weaker than corporate LMS |

n/o = not observed in sampled pages (absence not asserted beyond sampled evidence).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

A **Customer Training / Academy Platform** is an organization-operated learning platform whose defining core is four structures held jointly:

1. **The external-audience learner population** — the learners are people outside the operating organization's workforce: its customers, users, partners, resellers, franchisees, or members. The learner relationship is a commercial or membership relationship, not employment and not academic enrollment. (Remove → Corporate LMS or education LMS.)
2. **The managed learning catalog on a branded academy surface** — the organization authors, imports, or curates learning offerings (courses, paths, live events) and organizes them as a browsable catalog on a customer-facing, organization-branded learning site. (Remove the managed offerings → a marketing site or community; remove the branded surface → a bare content store.)
3. **Organization-governed learner access and enrollment** — external people enter the academy through admission rules the organization sets: open self-registration, gated sign-up, SSO into the organization's identity system, access/registration/redemption codes, invitations, purchase, or entitlement — with admin-side enrollment also possible. The organization controls who can see and take what. (Remove → an open content library with no gate; remove self-service → assigned-only corporate training.)
4. **Per-learner training records** — each learner's enrollment, progress, and completion are tracked as durable records, feeding certificates/credentials where configured. (Remove → a video/content site with no training record.)

Remove any one and the Type collapses: without (1) it is a corporate or academic LMS; without (2) it is a website or community; without (3) it is either an open content platform or an internal assignment engine; without (4) it is content publishing, not training.

**Historical/market-sample check (§24):** pre-cloud vendor customer-training portals and "customer universities" (course catalog + external registration + completion certificates) satisfy all four invariants with none of the modern layers — no SSO, no commerce, no AI, no communities, no in-app surfaces. Vendor-run classroom programs with registration forms and paper certificates satisfy the core with the catalog as a printed schedule and the record as a paper file. Association/member continuing-education programs fit the same core with members as the audience. The L0 does not overfit the modern SaaS-academy implementation.

### L1 — Common Mature Structure

- **Branded academy surface**: custom domain + SSL, theming, public catalog pages with search-engine discoverability, per-audience or per-client portals (separate branding, catalogs, and administration).
- **Content machinery**: native authoring (lesson/page types), SCORM/xAPI/LTI import, video/audio/PDF/embeds, microlearning, learning paths with ordering and prerequisites, quizzes/assessments with question banks and manual grading, live training events (ILT/VILT) with registration, waitlists, calendars, reminders, and attendance/success recording.
- **Access & identity**: SSO (frequently to the operator's own product identity), access/registration/redemption codes, invitations, bulk learner import, sign-up fields capturing learner attributes, groups/segments with membership rules, per-object visibility.
- **Entitlement & monetization**: priced courses/paths, subscriptions, training credits, license packages, bulk/B2B purchasing, group subscriptions, promo codes/coupons, order and refund handling.
- **Certification & credentials**: completion certificates, recurring/renewable certification programs, verification URLs, badge/credential integrations (Credly/Accredible/LinkedIn class), third-party certificate uploads.
- **Learner management**: learner profiles, record merging, progress editing, impersonation for support, learner-side managers overseeing their own people.
- **Analytics & business integration**: enrollment/engagement/completion reporting, dashboards, data connectors/BI export, CRM sync, customer-success integration, support-tool integration, webinar-tool integration.
- **Operations**: admin roles/permissions (SCIM in mature products), audit logs, branded email templates, registration/completion/reminder notifications, announcements.
- **AI layer (era-current)**: AI authoring, recommendations, conversational answers, learner tutors/agents.

### L2 — Variant / Optional Structure

- **Packaging poles**: pure-play customer-education platform (Skilljar, Thought Industries, Intellum, Northpass class) vs extended-enterprise LMS where customer training is one audience of a unified platform (Docebo, Absorb, LearnUpon portals class).
- **Learning-business posture**: training operated as a revenue line with client licensing, sublicenses, seat allocation, B2B group subscriptions (Thought Industries Panorama pole; Skilljar subscriptions/licenses; Docebo marketplace).
- **Education-as-marketing**: public ungated academies for prospects/lead generation; pre-customer domains that hand off to customer SSO domains.
- **Member/professional education**: associations running CE/CME credit programs for members.
- **Partner certification programs**: tiered partner/reseller certification as the academy's main job.
- **In-app/embedded learning**: learning surfaces inside the operator's product; headless delivery; MCP/agent surfaces.
- **Community/social learning**: discussions, cohorts, peer content.
- **Gamification, localization/multi-language, mobile apps, white-label mobile apps.**
- **Compliance depth**: audit trails and mandatory-training machinery — present where the same engine serves employees, weaker in pure-play customer deployments.

### L3 — Vendor-specific (kept out of the final document)

Skilljar: Training Domains, Catalog Pages, Plans, Training Credits, License Packages, Student Managers, domain-level access codes, cross-domain progress preservation, course families, content syndication, hCaptcha. Thought Industries: Panorama/sublicenses/seat allocation, MicroCourses, registration-vs-redemption codes, sandbox→production promotion, AEO, BI Connector. Docebo: Extended Enterprise app, branches, Docebo Pages, Harmony/AgentHub, Content Marketplace, Headless Learning, Companion. Intellum: Organizations, Evolve, Creator/Manager/Learner agents, Education-Led Growth.

## Vendor-specific Findings

- Skilljar's **domain access levels** (public / login required / access code) are the most explicit statement of the customer-academy admission model in the sample; the *concept* (tiered self-service admission under organization-set rules) is common (Thought Industries registration/redemption codes, free-vs-priced registration; Docebo per-audience experiences), the implementation is product-specific.
- Skilljar's **cross-domain progress preservation** (prospect domain → customer SSO domain) documents the lead-gen-to-customer journey as a first-class pattern; treat the concept (audience-state transitions) as common, the mechanism as product-specific.
- Thought Industries' **Panorama** is the strongest learning-business architecture in the sample (client accounts with own licenses, sublicenses, seats, branding, reporting); no other sampled product documents an equivalent at that depth — held as a variant pole, not core.
- Skilljar's **Student Managers** and Thought Industries' **manager-learner dual role** both document customer-side management (the customer's own admins managing their people) — promoted to L1 concept (learner-side management), not L0.
- Intellum's **feature launch campaigns** (training triggers tied to product releases) and usage/support-signal-driven recommendations document the product-adoption coupling distinctive to this Type; single-product evidence — kept as an L2/variant illustration.
- Docebo's own FAQ defines extended enterprise as covering customers, partners, resellers, dealers, franchises, and members — vendor self-evidence that the audience set of this Type is broader than "customers" alone.

## Boundary Findings

1. **vs Corporate LMS (§09, processed 2026-09-07) — joint review RESOLVED from this side: keep-both RATIFIED, seam refined.** The corporate-lms pass framed this leaf as an "audience variant — identical machinery; remove the employee population → customer training remains." This pass confirms the shared engine (offerings, enrollment, completion records) but finds the seam stronger than audience labeling: (a) the **centered relationship** differs — employment (org-structure assignment, compliance records) vs commercial customer/partner relationship (self-service admission, entitlement, commerce); (b) the **primary surface** differs — internal admin-driven delivery vs a public-facing branded academy web property with SEO, gated catalogs, and product-SSO entry; (c) the **purpose and downstream consumers** differ — workforce capability/compliance vs adoption/retention/revenue, with CRM/CS/support as the integration spine instead of HRIS; (d) the **market** differs — a distinct pure-play customer-education product category (Skilljar/Intellum/Thought Industries/Northpass) sold to customer-education teams, alongside extended-enterprise LMS products that straddle both (Docebo explicitly: "multiple extended enterprise experiences... one for customer training" beside employee training). Removal tests recorded both directions: strip the external audience + branded academy surface → corporate LMS remains; strip the employment relationship + HRIS spine → this Type remains. The extended-enterprise unified platform is the straddler and is documented as a packaging variant of both Types.
2. **vs LMS (§23, education)** — academic population (students, terms, grades, credit) vs external commercial audience; the record's consumer is an academic transcript vs the operator's customer/commercial systems.
3. **vs MOOC Platform (§23)** — MOOC serves public learners at scale with the operator as an educational institution/platform; the academy serves the operator's own customers/partners with a commercial relationship. A public lead-gen academy approaches MOOC-like openness but keeps the commercial anchoring.
4. **vs Educational Content Platform (§23, processed)** — that Type is a library consumed learner-directed with no enrollment relationship; the academy holds enrollment, admission rules, and per-learner records.
5. **vs Customer Onboarding Platform (§07, unprocessed)** — onboarding platforms center the transition workflow to first value (tasks, checklists, stages); the academy centers learning offerings and records. Onboarding is a use case here (adaptive onboarding directly observed at Intellum; onboarding paths common), not the centered object. Flag for that pass.
6. **vs Customer Success Platform (§07, processed)** — CS centers the managed account relationship and health workflow; the academy supplies learning records and adoption signals that CS consumes (Skilljar→Gainsight integration directly observed; Gainsight now owns Skilljar — the deepest coupling in the sample, still two products). Consistent with the CS pass's integration-spine finding.
7. **vs Partner Relationship Management (§07, unprocessed)** — PRM centers the partner lifecycle (recruitment, deals, MDF, performance); partner training/certification is a capability inside PRM and a primary audience of academies. Partner-only academies are a variant of this Type, not PRM. Flag for that pass.
8. **vs Product Usage / Adoption Platform (§07, unprocessed)** — adoption platforms measure/instrument product usage; the academy delivers learning and can consume usage signals (Intellum recommendation inputs). Different objects. Flag for that pass.
9. **vs eLearning Authoring Tool (§23, processed)** — authoring is a capability here (native builders; Evolve bundled with Intellum); dedicated authoring tools carry deeper authoring workflows as their primary job. Consistent with that pass's boundary.
10. **vs Digital Credential Platform (§23, unprocessed) / Certification Management (§25, unprocessed)** — certificates/badges are outputs of the training record here; dedicated credential platforms issue and verify standalone credentials at scale. Flag for those passes.
11. **vs Community Platform (§01.06/§25)** — communities center member discussion; academies center structured learning with records; community sections appear as optional additions (Docebo Communities product; discussion pages in Thought Industries).

## Uncertainties

- **Intellum operational structure** is evidenced only at product-page level (help center unreachable ×2); no workflow claims are made for it beyond its own published descriptions.
- **Docebo** operational detail (branches, enrollment rules) is corroborated from the corporate-lms pass's Tier-1 fetches; this pass directly observed only product pages and the help-center root.
- **Northpass** unreachable (404) — the SMB pure-play pole is under-sampled directly; its expected shape (simpler Skilljar-class) is asserted only as an expectation.
- Precise numeric limits, default validity windows, and pricing mechanics observed in single products are recorded as product-specific and not generalized.
- The keep-both resolution vs corporate-lms is recorded as a recommendation; the directory decision belongs to maintainers.

## Final Synthesis

The Customer Training / Academy Platform is the organization-operated system of record for training people outside its workforce. Its defining core is four structures held jointly: an external-audience learner population (customers, users, partners, members), a managed learning catalog on a branded customer-facing academy surface, organization-governed learner access and enrollment (self-service admission under rules the organization sets — open, gated, SSO, codes, purchase, entitlement), and per-learner training records feeding certification. Everything the market associates with the category — multi-audience portals, live events, monetization, credential integrations, CRM/CS/support integration, adoption analytics, communities, in-app surfaces, AI — is standard mature structure or variant structure on that core. The Type is distinct from the Corporate LMS not merely by audience label but by centered relationship (commercial vs employment), primary surface (public branded academy vs internal delivery), purpose (adoption/retention/revenue vs workforce capability/compliance), and market (a distinct pure-play product category beside the extended-enterprise straddler). The joint review with the corporate-lms pass is resolved from this side: keep both Types, with the extended-enterprise LMS documented as the packaging variant that realizes both in one platform.
