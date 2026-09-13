# Research Notes — MOOC Platform

Research date: 2026-09-08
Slug: mooc-platform (DIRECTORY §23 Education — "MOOC Platform")

---

## Research Goal

Understand what a MOOC Platform is as an Application Type: what its defining structure is, how a course actually flows from publication to learner completion, which capabilities are standard versus optional, and where its boundaries sit against the neighboring Types in §23 (Learning Management System, Educational Content Platform, Virtual Classroom, Tutoring Platform, Test Preparation Platform, Digital Credential Platform) and against Corporate LMS (§09), LXP (§23), Customer Training / Academy Platform (§07), and Creator Course Commerce Platforms.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a platform hosting open online courses — learners self-enroll from a public catalog, progress through structured course material, get assessed, and (often) earn certificates.
- Likely confusion zones:
  - LMS — both have "courses, learners, progress, grades". Difference guess: institution-controlled rostering (LMS) vs open self-service enrollment (MOOC).
  - Educational Content Platform — both host learning content. Difference guess: enrollment act + tracked per-learner record (MOOC) vs standing library consumption.
  - Virtual Classroom / Tutoring — live human-led sessions vs asynchronous self-serve course programs.
  - Corporate LMS / Customer Academy — assigned organizational populations vs public self-selected learners.
- Open questions going in: Is "massive" structural? Is "open" (free) structural? Are cohort/scheduled runs required, or is self-paced enough? Are certificates definitional? Is video definitional?

## Research Questions

1. What is the core object (course)? What does it contain, and how is it structured?
2. What does enrollment bind, and what does it create?
3. How do self-paced and scheduled/cohort courses coexist?
4. How does progress/completion tracking work, and what role do assessments play?
5. How do audit/free vs paid/verified access regimes work?
6. Who authors and publishes courses (universities, companies, independent instructors), and what publishing machinery exists?
7. What does the platform operator contribute (curation, quality review, monetization, moderation)?
8. What learner-side and instructor-side interfaces exist?
9. How do multi-course programs (specializations, nanodegrees, degrees) relate to single courses?
10. Where are the exact seams vs LMS, Educational Content Platform, Corporate LMS, and adjacent Types?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer tiers.

| Product | Philosophy / tier | Evidence quality this pass |
|---|---|---|
| edX | University-partnership MOOC (founding generation), audit/verified dual track, Open edX open-source lineage | Tier-1: help center fetched (5+ articles) |
| Coursera | University+industry partnership platform at scale, credential ladder (Guided Projects → Degrees), consumer + enterprise | Tier-2: official product/how-it-works pages fetched; learner help center is a Salesforce SPA and was NOT reachable |
| Udemy | Open marketplace — anyone can author, set price, keep content copyright; consumer + Udemy Business | Tier-1: help center fetched (learner + instructor categories + lifetime-access article) |
| Udacity | Project/mentor-reviewed subscription programs (Nanodegrees), enterprise + scholarship programs | Tier-1: support center categories + Projects-and-Reviews section fetched |
| Khan Academy | **Boundary probe, expected NOT this Type**: free nonprofit standing library, no enrollment/certificates/instructor marketplace | Tier-1: help center fetched (structure confirms probe) |
| 中国大学MOOC (icourse163.org) | Regional probe (China, university-school model) | Weak: site returns JS-rendered JSON skeleton only (school count, enrollment statistics); content not readable — conceptual treatment only |

FutureLearn was planned as a cohort-run pole but its help center failed twice (transport errors) and was abandoned per the network-retry rule; no claims about it are made.

## Sources

Fetched 2026-09-08:

- edX Help Center — root: https://support.edx.org/hc/en-us
  - "When does my course start and end?" — https://support.edx.org/hc/en-us/articles/206211998
  - "Is there a walk-through of a sample course?" — https://support.edx.org/hc/en-us/articles/207205937
  - "What are the differences between audit (free) and verified (paid) courses?" — https://support.edx.org/hc/en-us/articles/360013426573
- Coursera — official product pages: https://www.coursera.org/ , https://www.coursera.org/about/how-coursera-works/
  - Learner help center (learner.coursera.help / coursera.support) NOT reachable this pass (Salesforce SPA "CSS Error", 2 attempts abandoned)
- Udemy Help Center — root: https://support.udemy.com/hc/en-us
  - Getting started category, Course building category (Quality Review Process, Course organization, Uploading content, Creating content sections)
  - "Lifetime access" — https://support.udemy.com/hc/en-us/articles/229603708
- Udacity Support — root: https://support.udacity.com/hc/en-us
  - "Projects and Reviews" category — https://support.udacity.com/hc/en-us/categories/201240726
- Khan Academy Help Center (boundary probe) — https://support.khanacademy.org/hc/en-us
- 中国大学MOOC — https://www.icourse163.org/ (JS-rendered; JSON skeleton only)

Source-access limitations:
1. Coursera operational documentation unreachable → Coursera claims limited to Tier-2 product-page positioning (partner model, product ladder, access programs). No precise Coursera workflow/rule claims.
2. FutureLearn unreachable → no cohort-run pole observed first-hand; scheduling claims calibrated against edX (which documents both modes) only.
3. icourse163.org not readable → regional check is conceptual, supported only by the JSON skeleton (894 schools; large enrollment counts).
4. Khan Academy main site blocked (JS challenge); help center reachable and sufficient for the probe.

Sibling-pass alignments read from STATUS.md before writing:
- learning-management-system-lms (§23): boundary recorded as "vs MOOC (open self-service at scale vs institution-rostered)"; LMS L0 requires rostering "never open discovery".
- educational-content-platform (§23): sampled Khan Academy; seam described as "enrollment act + cohort + scheduled graded instance vs standing library".
- corporate-lms (§09): org-defined learner population vs "public content site/MOOC".
- learning-experience-platform-lxp (§23): "the population is served, not anonymous — remove → public content site/MOOC".
- customer-training-academy-platform (§07): "vs education LMS/MOOC/educational-content-platform (population + relationship)".
- creator-course-commerce-platform: noted "vs MOOC marketplaces (distribution variant, not researched)".

---

## Product Observations

### edX (Evidence layer A unless noted)

- Catalog → **course enrollment page** ("search for a course in the course catalog then click the course thumbnail") with start/end dates shown above the **Enroll** button.
- After enrolling: **learner dashboard** (home.edx.org), **course homepage** with "Important Dates", and an in-course **Dates tab** listing due dates and the course end date.
- **Self-paced and dated courses coexist**: "If the course is self-paced and the course has already begun, the start date will show today's date." Other articles: "Does my course have due dates?", "How does the suggested schedule work?", "When will this course be offered again?" (re-runs), "What is the deadline to upgrade...?" — scheduling is a configuration, not a fixed pattern.
- **Audit (free) vs verified (paid) tracks** — comparison table directly observed:
  - Audit: free; readings, video lectures, ungraded practice assignments, discussion forums; **temporary access** (expires after the estimated course length posted on the course page); **no graded assessments or exams**; **no certificate**.
  - Verified: paid; **graded assignments and exams**; **verified certificate if passing score earned before course end**; access to materials after course end/archiving; certificate shareable to CV/LinkedIn; upgrade deadline applies.
- **Archived courses** exist; audit learners lose access ("no longer able to click View Course on your dashboard"), verified learners retain access.
- **Honor Code** is a named policy surface; **financial assistance** application flow exists.
- Help-center top categories: Account Basics, Courses, Payments & Refunds, **Certificates**, **Programs** (program certificates), **Credit**, Mobile, FAQ.
- A demo course (DemoX) teaches platform mechanics — evidence that the course-taking loop is standard enough to be demonstrated in-product.

### Coursera (Evidence layer A for positioning/product ladder from official pages; workflows unobserved)

- "Coursera partners with more than 325+ leading universities and companies" — provider-aggregation model; credentials "issued directly by trusted institutions" (university/company branding on the record).
- Product ladder on the official how-it-works page: **Guided Projects** (1–2 h), **Courses** (4–12 h, "starting at Free"), **Specializations** (1–3 months, subscription-priced), **Professional Certificates**, **MasterTrack® Certificates**, **Degrees** (2–4 years).
- Access programs: free previews ("preview for free, including access to the first module"), free trials, **Coursera Plus** subscription ("unlimited access to thousands of courses").
- B2B/C2C surfaces: **Coursera for Business** (Teams/Enterprise), **Coursera for Campus**, **Coursera for Government** — the same catalog distributed to organizational populations.
- Browse categories, trending searches, "Join for Free" account creation; mobile apps.
- Workflow details (enrollment steps, grading, certificates lifecycle) not observed — help center unreachable.

### Udemy (Evidence layer A unless noted)

- **Marketplace structure, directly stated**: "Our marketplace model means we do not own the copyright to the content of the courses; the respective instructors own these rights." Instructors may unpublish (closing new enrollments; enrolled students keep access); platform may remove courses for policy/legal reasons.
- **Quality gating before publication**: "Udemy's Quality Review Process", "Submit a Course for Review", test-video submission, course-length calculation — a course must pass review to go live.
- **Instructor-side machinery**: course management dashboard, **course curriculum page**, adding lectures/sections, uploading video content (bulk uploader, media library), practice tests, in-course labs, role plays, course landing page (description, intended learners), pricing/promotion tools, instructor payments (revenue share), teaching assistants, MFA for instructor accounts.
- **Learner-side machinery**: account signup, purchase → **lifetime access** ("access for life, provided that your account is in good standing and Udemy continues to have a license to that course"; free courses included), subscription content access tied to active subscription, refunds, **"Mark or Unmark Lectures as Complete"** (learner-controlled progress marking), "how to find your missing course" troubleshooting, mobile app.
- Free courses exist; paid courses exist; instructor coupons exist.
- Help-center structure: Student Topics / **Instructor Topics** / **Udemy Business Topics**; categories include Learning experience, Purchase/refunds, Mobile, Trust & Safety, Instructor payments, Selling & promotion, Course building, Course management, Affiliates.
- Note (market observation, not Type-defining): help articles titled "Coursera and Udemy combination" (learner and instructor versions) indicate the two companies are now combined; both product surfaces remain distinct. Recorded as market fact only.

### Udacity (Evidence layer A unless noted)

- **Program-centric**: "Udacity Subscription, Nanodegree Programs, & Courses" category; graduation and "Access to content post graduation (Static Access)" — completion produces standing access and (per program naming) a credential.
- **Subscription commercial model**: pausing subscription, auto-renew, refunds — learning entitlement tied to subscription state.
- **Project-and-review assessment loop** (category "Projects and Reviews"): "How to Submit your Project Successfully: Checklist", "Project review timeline", **"Who grades Udacity projects?"** (human reviewers), "Why Can't I Resubmit My Project?", "How to cancel project submission?", **"Project submission notes after Plagiarism"** — submission → review → pass/resubmit cycle with integrity enforcement.
- Audience programs: Enterprise, Government Programs, Scholarship Programs, Career Services, Alumni.
- No course-by-course purchase observed; enrollment is program/subscription-shaped.

### Khan Academy (boundary probe — Evidence layer A for what it lacks)

- Help-center structure: **Learners / Teachers & Coaches / Parents / School and District Administrators** — school-adjacent population, no self-enrolled individual-learner marketplace structure.
- Standing subject library (Math K-8, high school & college, Test prep, Science, Computing, Arts & humanities, Economics, Reading & language arts, Life skills) — courses as browsable subject areas, not enrollable offerings.
- No enrollment act, no certificates machinery, no instructor-side authoring marketplace, no commerce ("free... nonprofit organization. Donate").
- Conclusion: fails the hypothesized MOOC core on enrollment + per-learner course binding; consistent with the educational-content-platform pass, which sampled Khan Academy as one of its own products.

### 中国大学MOOC / icourse163.org (regional probe — weak evidence)

- JSON skeleton returned: `schoolNumber: 894`, large enrollment-statistics counters (`forumEnrollNumber` ~29M) — consistent with a university-school-partnership MOOC platform with very large learner enrollment, but page content not readable (JS-rendered).
- Treat as conceptual support for the regional variant only; no operational claims.

---

## Cross-product Comparison

| Dimension | edX | Coursera | Udemy | Udacity | Khan Academy (probe) |
|---|---|---|---|---|---|
| Public catalog + search/browse | A: yes | A: yes | A: yes (marketplace) | A: yes (program catalog) | A: yes (subject library) |
| Course as published learning program | A: yes | A: yes | A: yes (curriculum of lectures/sections) | A: yes (program curriculum) | A: yes (but not enrollable) |
| Instructor/provider authoring + publishing | A: partner model (implied); open-source Studio lineage | A: partner model (325+ institutions) | A: in-product studio + quality review + pricing/promotion | A: platform-produced programs | A: none (in-house production) |
| Open self-service enrollment by individuals | A: yes (Enroll button, anyone) | A: yes ("Join for Free") | A: yes (purchase = enrollment) | A: yes (subscription/program signup) | A: **no enrollment act** |
| Access regime variety | A: audit (free, temporary, no graded items) vs verified (paid, graded, certificate) | A: free previews/trials, subscription, per-program pricing | A: per-course purchase w/ lifetime access; free courses; subscription content | A: subscription-tied program access | A: free, no accounts required for consumption |
| Per-learner progress tracking | A: dashboard, Dates tab, progress of practice assignments | unobserved (help center down) | A: mark lectures complete; progress visible | A: project submission/review states; graduation | A: practice/mastery tracking (probe; different Type) |
| Graded assessment | A: graded assignments + exams on verified track | unobserved | A: quizzes/practice tests exist; grading depth varies | A: human-reviewed projects (pass/resubmit) | A: quizzes/mastery (probe) |
| Completion credential | A: verified certificates; program certificates | A: certificates/degrees named on product ladder | not observed this pass | A: Nanodegree graduation + post-graduation access | A: none |
| Scheduling model | A: both self-paced and dated; re-runs; optional due dates | unobserved | A: self-paced (no dates in any fetched doc) | A: subscription-paced (no cohort dates observed) | A: self-paced |
| Discussion/social layer | A: forums on both tracks | A: community site exists | A: Q&A/TAs implied by categories ("engage with students") | A: learner community site | A: community + teachers/coaches |
| B2B distribution of same catalog | unobserved this pass | A: Business/Campus/Government | A: Udemy Business topic section | A: Enterprise category | n/a (school/district admin = different population) |
| Academic integrity surface | A: Honor Code | unobserved | A: Trust & Safety; policy removals | A: plagiarism notes on projects | n/a |

## Canonical Model (world model)

```text
Catalog (public discovery surface: search / browse / recommend)
  └── Course (published learning program — the object of record)
        ├── Curriculum: sections/modules → instructional units (video, readings, etc.)
        ├── Assessments: practice and graded items (quizzes, assignments,
        │               peer- or human-reviewed projects)
        └── optional scheduled run (dates, deadlines) OR always-on self-pacing
  └── Enrollment (learner × course; often × access track)
        └── Progress record (per-learner, durable)
              └── Completion → recognition (certificate/credential — common, varies)
Provider side: author → (quality gate) → publish → price/promote (marketplace) → maintain
Platform side: aggregate catalog → curate/rank → monetize → moderate/integrity
Program layer (common): ordered courses → program completion → program credential
```

## Abstraction Hierarchy

### Level 0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a MOOC Platform:

1. **The published course as the platform's object of record** — a structured learning program (curriculum of instructional units + assessments) published by an instructor/provider into the platform's shared catalog; the anchor to which enrollment, progress, discussion, and completion all attach.
   - remove → a content library / open courseware site (materials without a managed learning offering)
2. **Open self-service enrollment of individual learners** — anyone can discover an offering in the public catalog and bind themself to it as a learner, without institutional admission or employer assignment controlling the population.
   - remove → an LMS / corporate-LMS-shaped system (rostered, assigned populations)
3. **Per-learner progress and completion tracking against the course** — the platform records each enrolled learner's advancement through the curriculum and holds durable completion state per learner per course.
   - remove → passive content publishing (nothing managed on the learner side)

Jointly-held is load-bearing:
- 1 alone = educational content platform / open courseware
- 2 alone = a signup page
- 3 alone = a generic progress tracker
- 1+2 without 3 = content library with accounts, still not course management
- 1+3 without 2 = institutional course site (LMS territory)
- 2+3 without 1 = account system with progress and nothing course-shaped

Deliberately NOT in L0 (tested against §24-style questions):
- "Massive" — a scale outcome, not a structure; a platform running small courses is structurally identical.
- "Open" as free-of-charge — monetization varies (free audit, paid verified, per-course purchase, subscription, B2B); only open *enrollment* is invariant.
- Video lectures — the dominant implementation of instructional material, not the concept.
- Certificates — heavily associated with the Type but absent on free-audit tracks and in some products; completion *tracking* is the invariant, the credential is not.
- Cohorts/scheduled runs — one configuration; self-pacing with today-as-start-date is equally native (edX documents both).
- Forums/community — pedagogically central historically, but structurally common-not-defining.

### Level 1 — Common Mature Structure

Present in most mature products (cross-product, layer B unless noted):

- Catalog machinery: category browse, search, recommendations/rankings, course landing pages with description/intended-learner/price/dates.
- Enrollment page as the conversion surface (edX A: dates above the Enroll button).
- Learner dashboard: my courses, progress state, dates/deadlines.
- In-course experience: curriculum navigation + content player + progress marking (Udemy A: mark/unmark lectures complete).
- Assessments beyond progress-marking: auto-graded quizzes; graded assignments/exams (edX A, track-gated); human- or peer-reviewed projects (Udacity A).
- Discussion / Q&A layer scoped to the course (edX A: forums on both tracks).
- Completion recognition: certificates of some form (edX A verified/program certificates; Udacity A graduation; Coursera A credential ladder); exact form varies by product and track.
- Instructor/provider publishing machinery: curriculum builder, content upload, landing page, publication gating (Udemy A quality review), post-publication maintenance.
- Multi-course program layer: specializations / program certificates / nanodegrees / degrees (edX A Programs category; Coursera A ladder; Udacity A).
- Academic integrity policy surface (edX A Honor Code; Udacity A plagiarism handling).
- Mobile apps (edX, Udemy, Coursera — A for categories/store listings).

### Level 2 — Variant / Optional Structure

- Commercial model: audit-free + paid-verified dual track (edX); per-course purchase with lifetime access (Udemy A); all-you-can-learn subscription (Coursera Plus A; Udemy subscription content A; Udacity A); free nonprofit operation (probe boundary).
- Scheduling configuration: dated runs/re-runs with deadlines ↔ self-paced always-on (edX documents both A); suggested schedules.
- Provider model: university/company partnership with co-produced credentials (edX, Coursera) ↔ open marketplace of independent instructors who retain copyright (Udemy A) ↔ platform-produced programs (Udacity).
- Regional/national deployments: university-school consortium platforms (icourse163 skeleton: 894 schools — weak evidence, conceptual); government skill programs (Udacity Government Programs A; Coursera for Government A).
- B2B distribution of the same catalog to organizational populations: Coursera for Business/Campus (A), Udemy Business (A), Udacity Enterprise (A) — seam toward Corporate LMS when assignment machinery becomes the center.
- Financial assistance / scholarships (edX A, Udacity A).
- Degree/credit layering (edX Credit category A; Coursera degrees A).
- AI-era add-ons (Udemy AI tools for instructors A; Coursera AI assistant mentions on marketing pages) — era-current, not structural.

### Level 3 — Vendor-specific Structure (kept out of the final document)

- edX: DemoX demo course; specific audit-expiry mechanics ("estimated course length"); specific upgrade-deadline article set; Open edX open-source lineage.
- Udemy: "Alex" virtual agent; Instructor Partner badges; specific revenue-share article set; bulk uploader; test-video submission; course-length calculation rules.
- Udacity: Static Access post-graduation policy; specific resubmission-limit rules.
- Coursera: MasterTrack® branding; specific price points on the product ladder page.
- icourse163: school-count/enrollment statistics endpoint fields.

## Rejected Findings (observed somewhere but NOT promoted)

- "MOOC = free" — falsified by the current market (paid verified tracks, per-course purchase, subscriptions dominate) while open *enrollment* persists. The word "open" in the Type's name survives structurally as open self-service enrollment, not free content.
- "MOOC = cohort courses with deadlines" — falsified by edX's own self-paced documentation (start date = today) and by marketplace products with no dates at all. Cohorts are a scheduling variant.
- "MOOC = video lectures" — video is the dominant medium but the concept is "structured instructional units"; nothing in the core requires video.
- "Certificate is the defining end state" — audit tracks (edX A) run the full course loop without any certificate; completion *tracking* is invariant, the credential is a common (and often monetized) add-on.
- "Marketplace authoring is definitional" — only the marketplace pole (Udemy) has independent-instructor authoring with pricing; partnership platforms concentrate authoring in institutions. The invariant is that a published course exists in the catalog, not who authored it or how it was priced.

## Boundary Findings

| Neighbor Type | Remove-what test | Result |
|---|---|---|
| Learning Management System (§23) | Remove open self-service enrollment; make the population institution-rostered and grades flow to an official student record → LMS | Distinct Type. Matches sibling LMS pass ("open self-service at scale vs institution-rostered"). The MOOC platform's own B2B/Campus offerings sit on this seam. |
| Corporate LMS (§09) | Remove the public catalog; make learners an employer-defined population with assignment/compliance records → Corporate LMS | Distinct Type. Consistent with corporate-lms pass. |
| Educational Content Platform (§23) | Remove the enrollment act and the per-learner course record; keep a standing library of learnable content → Educational Content Platform | Distinct Type. Khan Academy probe confirms empirically (fails enrollment + per-learner course binding). Consistent with the educational-content-platform pass, which sampled Khan Academy on its side. **Refinement:** that pass's shorthand described the seam as "enrollment act + cohort + scheduled graded instance"; this pass's evidence shows cohorts/scheduled runs are a variant, not the seam (edX documents self-paced enrollment + tracking). The durable seam = enrollment act + per-learner tracked/assessed course record. |
| Virtual Classroom (§23) | Remove the asynchronous course program; make live synchronous sessions the primary object → Virtual Classroom | Distinct Type; live sessions are optional enrichment here. |
| Tutoring Platform (§23) | Remove self-serve content at scale; make human-taught sessions the unit of service → Tutoring Platform | Distinct Type. |
| Test Preparation Platform (§23) | Narrow the goal to a specific exam; goal-specific prep becomes the whole Type | Distinct Type; test-prep courses can live inside a MOOC catalog as content variants. |
| Digital Credential Platform (§23) | Remove the course/learning operation; keep only issuing/verifying credentials → Digital Credential Platform | Distinct Type; MOOC certificates are an output, not a credential infrastructure. |
| Customer Training / Academy Platform (§07) | Make the learner population the operator's own customers/partners under a commercial relationship → Customer Academy | Distinct Type; consistent with that pass. |
| Creator Course Commerce Platform | Make the seller's own audience + checkout/offer machinery the center → creator commerce | Distinct Type (that pass's own note); Udemy is the straddling pole (marketplace distribution of creator courses). |
| eLearning Authoring Tool (§23) | Authoring deliverables exported elsewhere vs operating the learning venue | Distinct Type; authoring here is one capability among partnership/marketplace poles. |

## Historical / Market-Sample Check

- Correspondence-era distance education (open enrollment by mail, structured lesson programs, graded assignments, completion records): satisfies the three-leg core at analog level — open self-enrollment + course-of-record + per-learner tracking are not digital-era inventions. (Conceptual; no digital claim needed.)
- MIT OpenCourseWare generation (2001-): published course materials without enrollment/progress → fails legs 2–3; correctly classified as Educational Content Platform (matches that pass, which uses the OCW era as its own historical anchor).
- Connectivist cMOOCs (2008): distributed across the web, no central platform → not instances of the platform Type; the platform Type crystallized with the xMOOC platforms (2011–2012).
- Session-era xMOOC platforms (2012–2014, dated runs with deadlines) and today's self-paced-first platforms both satisfy the core — the definition names no scheduling model.
- Regional university-consortium platforms (icourse163 skeleton: 894 partner schools) satisfy the core with a school-partnership structure — definition names no provider model.
- The word "MOOC" (Massive Open Online Course) is historically loaded: "massive" and "free" both fail as invariants on current evidence; the definition therefore avoids both.

## Uncertainties

1. Coursera operational workflows (enrollment steps, grading, certificate lifecycle, audit-track details) unobserved — help center unreachable. All Coursera-specific behavior stays out of the final document; Coursera appears only in positioning/product-ladder claims.
2. FutureLearn (cohort-run pole) unobserved — the claim "cohort runs exist as a variant" is supported indirectly (edX dated courses + re-run documentation) and not by a cohort-native product.
3. Udemy certificates — not observed in fetched docs; no claim made either way in the final document.
4. Regional platforms (icourse163, XuetangX) — only JSON-skeleton evidence; regional variant treated conceptually.
5. Whether any sampled MOOC platform implements instructor-assignment or cohort-communication tools deep enough to blur toward LMS was not fully explored (Coursera Campus docs unreachable); seam described conceptually only.
6. "Discussion forums on both tracks" (edX A) is one product's evidence; forums-as-universal is a B-layer claim from the edX/Udemy/community-site pattern, not A-layer across all sampled products.

## Final Synthesis

A MOOC Platform is the open-enrollment online course platform: a public catalog of published courses (structured learning programs offered by instructors/providers), into which any individual learner can self-enroll, and against which the platform tracks each learner's progress and completion. Three structures jointly define it — course of record, open self-service enrollment, per-learner progress/completion tracking — and each is load-bearing: remove enrollment and it is an LMS territory; remove course+tracking and it is a content library; remove the public catalog and it is an institutional system.

Everything the market associates with MOOCs — massive scale, free access, video lectures, certificates, cohorts with deadlines, discussion forums, university branding, marketplace instructors, subscriptions, degrees — is either a scale outcome, a commercial variant, a medium choice, or a common-but-not-defining layer. The Type's name ("Massive Open Online Course") overstates two properties ("massive", "open-as-free") that current evidence falsifies; the surviving invariants are openness of *enrollment*, the course as managed object, and tracked learner progress toward completion.
