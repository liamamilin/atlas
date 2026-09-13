# Research Notes — Educational Content Platform

## Research Goal

Understand what an Educational Content Platform actually is as a class of software: what objects exist inside it (content, organization structures, learners, producers), what the learner experience loop looks like, who supplies the content and how, and where the Type's boundaries lie against neighboring education Types (LMS, MOOC Platform, Language Learning Application, Test Preparation Platform, eLearning Authoring Tool, AI Tutoring Application) and against general media/content Types (Video Streaming Platform, Online Encyclopedia, Digital Library Platform).

## Initial Boundary

Working hypothesis: an Educational Content Platform is a platform whose product **is the content library** — organized instructional material (video lessons, interactive courses, articles) that learners find and consume directly, at their own pace, without enrollment in a scheduled course instance, without instructor-managed coursework, and without a grading relationship.

Adjacent Types that must be separated:

- **LMS** — instructor/institution-operated delivery system of record (assignments, gradebook); learners are assigned.
- **MOOC Platform** — institution-authored courses with enrollment acts (cohorts, schedules, graded work, certificates).
- **AI Tutoring Application** — software that itself executes a teaching loop conditioned on learner performance (processed sibling leaf; boundary already recorded there: "videos, articles, and reference material for consumption; no instructional loop").
- **Video Streaming Platform** — entertainment-first organization (titles, feeds), not learning-structured.
- **eLearning Authoring Tool** — produces courseware for others to deliver; not a learner-facing library.
- **Language Learning Application / Test Preparation Platform** — narrower-purpose instruction Types in the same directory section.

## Research Questions

1. What is the core object structure (lesson/lecture/course/series/subject)? How do content items nest?
2. What does the learner loop look like: find → consume → track → continue?
3. Is progress tracking / completion state definitional or common? Do accounts have to exist?
4. Who supplies content: platform-produced, independent instructors, or curation of external material? What production-side machinery exists?
5. What commerce models occur (free/donation, subscription, per-item purchase)?
6. Is there an educator/institution layer, and is it definitional or a bolt-on?
7. Where does practice/exercise/assessment machinery sit relative to the Type's center?
8. Where are the AI-tutor layers relative to this Type (drift check against processed sibling)?

## Representative Products

Selected for market spread, philosophy contrast, customer-tier contrast, and accessible official documentation:

1. **Khan Academy** — free nonprofit; school-age academic subjects; platform-produced video lessons + practice; learner/teacher/parent/administrator role structure. (Help center fetched.)
2. **Brilliant** — consumer subscription; interactive problem-first STEM courses; mastery tracking; 2026 homepage leads with an AI tutor (Koji) layered on the course library. (Homepage fetched.)
3. **Udemy** — open marketplace of instructor-authored self-paced courses; per-course purchase + subscription plans; business tier; completion certificates; instructor-side production/payments machinery. (Support center + Learning-experience category fetched.)
4. **TED-Ed** — free nonprofit platform-native pole; curated + produced short video "lessons" organized by subject and theme; no-account browsing; educator lesson customization. (Homepage fetched.)

Rejected as samples: Coursera/edX (MOOC Platform — different leaf, used only as boundary contrast); MasterClass (help center transport error ×2, main site 403 — inaccessible this pass); Skillshare (help center timeout ×2 — inaccessible this pass).

## Sources

- Khan Academy Help Center — https://support.khanacademy.org/hc/en-us (fetched 2026-09-07)
- Brilliant homepage — https://brilliant.org/ (fetched 2026-09-07)
- Udemy Support Center — https://support.udemy.com/hc/en-us (fetched 2026-09-07)
- Udemy "Learning experience" category — https://support.udemy.com/hc/en-us/categories/204119608-Learning-experience (fetched 2026-09-07)
- TED-Ed homepage — https://ed.ted.com/ (fetched 2026-09-07)
- MasterClass — https://help.masterclass.com/hc/en-us (transport error ×2), https://www.masterclass.com/ (403) — **not used**
- Skillshare — https://www.skillshare.com/en/help (timeout), https://help.skillshare.com/hc/en-us (timeout) — **not used**
- Prior processed sibling: research/ai-tutoring-application.md (boundary context)

## Product Observations

### Khan Academy (Evidence Layer A — help center)

- Help center organized by role: **Learners; Teachers & Coaches; Parents; School and District Administrators** — a four-audience structure on top of the learner base.
- Courses organized by subject area: Math (Pre-K–8, get-ready, high school & college), Test prep, Science, Computing, Arts & humanities, Economics, Reading & language arts, Life skills — subject taxonomy over course catalogs.
- Nonprofit, donation-funded ("provide a free, world-class education to anyone, anywhere"); "Our content specialists" — content produced by the platform, not open contributors.
- Accounts with passwords, per-role quick-start guides; iOS/Android apps.
- Administrator machinery exists (CSV data dictionary for administrator reports; district onboarding) — institution layer on top.
- Khanmigo (AI) exists as a named layer with its own help articles — an AI assistant/tutor on top of the library.
- "Khan Academy Reimagined" — current platform redesign with per-role change articles (student, teacher, administrator).

### Brilliant (Evidence Layer A — homepage)

- 2026 self-positioning: "Your personal tutor for math and coding"; "A world-class tutor for every home."
- Content model: **courses organized into subjects** (Math with 26+ additional courses, Computer Science, CS, Science, Data Analysis), each course a sequence of visual, interactive problems ("Every session is visual and interactive… you work through problems step-by-step").
- Mastery state: "Koji tracks what you've mastered and where you're stuck, then builds practice around the gaps. He speeds up when you're ready, and slows down when you need it." (AI tutor layer, explicitly conditioned on mastery state.)
- Habit machinery: streaks, levels, daily goals.
- Audience: "From grade 5 to college and beyond"; parents/teachers angle; Educators and Homeschools solutions; K–5 Math Practice (beta); kidSAFE/COPPA certification.
- Subscription commerce (pricing/subscribe page, gift purchase); iOS/Android apps.
- Curriculum "crafted by award-winning teachers, subject-matter experts, and learning designers" — platform-produced.

### Udemy (Evidence Layer A — support center + learning-experience category)

- Two-sided help structure: **Learner topics / Instructor topics / Udemy Business topics**.
- Learner side: getting started; account/profile; learning experience; purchase/refunds; mobile; subscriptions (Starter Plan etc.); course player (mark/unmark **lectures** complete, notes, video speed/quality, Q&A); practice tests; in-course labs & workspaces (subscription features); offline downloads; wishlist; learning reminders; subtitles; **certificates of completion** (incl. NASBA CPE for some courses); lifetime access; reviews/ratings.
- Instructor side: course building (curriculum page, lectures, landing page), uploading content (video standards, bulk uploader), course organization, **Quality Review Process** (submit course for review; course length calculation), pricing & coupons, promotional tools, **instructor payments/revenue share**, tax forms, instructor identity verification, communication tools (Q&A rules, educational announcements, direct messages), student-engagement analytics (content quality, practice-test insights, lab insights), instructor AI tools (Role Play creation; generative-AI policy).
- Business channel: Udemy Business content opportunities; subscriptions program revenue for instructors.
- Commerce: per-course purchase (guest checkout possible) and subscription plans; refunds; gifts; credits.

### TED-Ed (Evidence Layer A — homepage)

- Self-description: "We create and curate the best educational content on the web."
- Content model: **video-based lessons** ("Watch video-based lessons organized by subject and age"); **Collections** ("organized by theme"); **Explorations** (interactive experiences with partner organizations); "best of web" items — short videos curated from external platforms (YouTube-hosted thumbnails visible).
- Subject taxonomy: The Arts; Business & Economics; Design, Engineering & Technology; Health; Literature & Language; Mathematics; Philosophy & Religion; Psychology; Science & Technology; Social Studies; Teaching & Education; Thinking & Learning.
- Lesson cards show duration and view counts; favorites/collections require sign-in — **browsing itself requires no account**.
- Create side: "Build your own video-based lesson" around any TED-Ed Animation, TED talk, or YouTube video; "organize video-based lessons in your own collection"; roles addressed: Educator / Student / Parent.
- Free nonprofit (donation-supported); no commerce, no certificates, no progress machinery on the surface.

## Cross-product Comparison

| Dimension | Khan Academy | Brilliant | Udemy | TED-Ed |
|---|---|---|---|---|
| Content unit | course / lesson + practice | interactive course / problems | course / curriculum / lecture | lesson / collection |
| Organizing structure | subject taxonomy → courses | subjects → courses | topics/categories → courses → lectures | subjects → lessons; themes → collections |
| Content supply | platform-produced (content specialists) | platform-produced (experts/learning designers) | open instructor marketplace (independent authors) | platform-produced + curation of external videos |
| Access model | free / donation | subscription | per-course purchase + subscription | free / donation |
| Accounts | required for progress | required for learning | required for learning (guest checkout for purchase) | optional (browsing without) |
| Progress tracking | yes (learner + reporting to teachers/parents) | yes (mastery state) | yes (lecture completion, lifetime access) | minimal (favorites/collections only) |
| Practice/assessment | practice exercises (reported) | interactive problems + AI-conditioned practice | practice tests, labs (tier-dependent) | none observed on surface |
| Certificates | none observed | none observed | certificates of completion | none |
| Educator layer | teacher/coach/parent/admin roles | educators/homeschools solutions | instructor role (production side) | educator lesson customization |
| AI layer | Khanmigo assistant/tutor | Koji personal tutor | AI assistant; instructor AI tools | none observed |
| Commerce | none (donations) | subscription | transactions + revenue share | none (donations) |

### Evidence-strength summary

- **Layer A (directly observed, single product):** Khan's four-role administration structure; Brilliant's Koji/mastery framing and habit mechanics; Udemy's marketplace machinery (revenue share, quality review, verification); TED-Ed's no-account browsing and educator lesson building; Udemy's certificates.
- **Layer B (cross-product commonality, all four sampled):** a persistent organized catalog of learning-purpose content (subject → course/series → lesson unit); learner-directed self-paced consumption without cohort/schedule; accounts + personal progress state in the commercial/academic poles; web + mobile apps; search/browse discovery; video-centric delivery; learning-support extras (notes, reminders, subtitles — Udemy, Brilliant/Khan side evidence).
- **Layer C (canonical inference):** the defining core is *the instructional content library + learner-directed consumption*; everything else is mature structure or variant posture.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Two properties; remove either and the product stops being this Type:

1. **Instructional content library** — a persistent, organized catalog of content whose purpose is teaching: content items (lessons/lectures/interactive problem sets/articles) nested in learning-oriented structures (subject/topic → series/course → unit/lesson), supplied by the operator (produced, commissioned, licensed, or curated). Without instructional organization + purpose, the product is a general media/content platform.
2. **Learner-directed self-paced consumption** — the learner personally finds and consumes content directly from the library, on their own schedule. No enrollment act in a scheduled course instance, no cohort, no instructor-managed assignment or grading relationship. Without this, the product is an LMS (assigned), a MOOC (enrolled), or linear broadcast.

Deliberately NOT in L0 (checked against historical/market samples — MIT OpenCourseWare, iTunes U, early Khan YouTube videos, public-media education archives satisfy the core without them): accounts, progress tracking, practice exercises, certificates, apps, subscriptions/commerce, educator roles, AI layers.

### L1 — Common Mature Structure

- Accounts/profiles carrying personal progress state (resume position, completed marks, mastery levels)
- Practice machinery attached to content (quizzes, problem sets, practice tests) — universal in the academic/professional poles, absent in the curation pole
- Search/browse discovery over a subject taxonomy; recommendations
- Web + mobile apps; offline access
- Player-side learning aids: speed/quality controls, notes, subtitles/transcripts
- Completion markers (lecture/course complete), completion certificates in professional-skills poles
- Ratings/reviews (marketplace pole); Q&A with content authors
- Habit/engagement mechanics: reminders, streaks, goals
- Progress visibility to supervising adults/educators (K-12 pole)

### L2 — Variant / Optional Structure

- Content production model: platform-produced / curated-external / open instructor marketplace
- Access model: free-donation / subscription / per-item purchase / freemium
- Audience segment: school-age academic / adult professional / general curiosity
- Educator/institution layer depth: parent-teacher-admin reporting vs production-side marketplace roles vs light educator customization vs none
- Assessment depth: none → attached quizzes → interactive mastery-tracked problems → adaptive AI-conditioned practice
- Credentialing: none → completion certificates → CPE-eligible certificates
- B2B channel: consumer-only vs business/team plans
- Language localization breadth
- AI tutor/assistant layering (drift frontier)

### L3 — Vendor-specific (research notes only)

- Khanmigo (Khan), Koji (Brilliant), "Alex" virtual agent, Tipalti payouts, NASBA CPE process, Udemy's Quality Review Process internals, course cloner tool, Role Play feature, "Khan Academy Reimagined" migration, TED-Ed Student Talks/Educator Talks programs, kidSAFE certification (Brilliant), Udemy Business content-opportunity program, instructor Partner badges.

## Vendor-specific Findings

- Khan Academy: district administrator reporting (CSV data dictionary) — institution pole evidence, not generic.
- Brilliant: AI tutor as the *homepage* identity in 2026 — the strongest observed instance of the AI-layer drift; the course library remains the substrate ("Courses" page, subject lists).
- Udemy: full marketplace economy — instructor verification, revenue share, tax forms, promotional agreements, review-manipulation rules; per-course purchase with guest checkout and lifetime access.
- TED-Ed: curation of external YouTube-hosted videos into lesson form — evidence that platform-production is not required for the Type (curation suffices), and that account/progress machinery is not required either.

## Boundary Findings

1. **vs LMS** — LMS is institution-operated and instructor-mediated: assignments, due dates, gradebook, learner population managed by the org. Educational Content Platform has no manager of the learner relationship; the learner directs consumption. Khan's teacher tools are a supervisory/progress-view layer on top of a self-directed library, not an LMS core. *Remove learner-directedness → it becomes an LMS.*
2. **vs MOOC Platform** — MOOC = institution-authored course *instances* with enrollment (cohorts, schedules, graded assignments, verified certificates). Content platform = access to a standing library. Udemy's per-course purchase is a commerce transaction, not an enrollment act; there is no cohort or grading relationship. *Remove self-paced standing-library access → it becomes a MOOC.*
3. **vs AI Tutoring Application** — processed sibling leaf: the AI tutoring Type is defined by software executing a pedagogy loop conditioned on learner performance. Content platforms deliver material; their AI layers (Khanmigo, Koji) sit on top of the library. Consistent with the sibling's recorded boundary. Drift flag: two of four sampled products now lead with AI tutors — the library remains the substrate.
4. **vs Video Streaming Platform** — organization principle: learning structures (subjects, courses, lessons, progress) vs titles/feeds/watchlist; purpose: skill acquisition vs entertainment. A video streaming service hosting documentaries is not organized for instruction. *Remove instructional organization → it becomes streaming.*
5. **vs eLearning Authoring Tool** — authoring tools produce courseware for delivery elsewhere (typically via LMS); here Udemy's course-building surface exists to onboard content into the platform's own library — production-side machinery, not a standalone authoring product.
6. **vs Online Encyclopedia / Reference Database** — reference serves lookup of specific questions; content platforms teach through structured sequences.
7. **vs Language Learning Application / Test Preparation Platform** — narrower-purpose instruction Types; test-prep content can live *inside* a content platform (Khan/Udemy both have test-prep content) without the platform becoming that Type.
8. **vs Digital Library Platform** — general collections of works; no instructional structuring or learning support machinery.

## Uncertainties

- Skillshare and MasterClass official documentation unreachable this pass. The "creator-generated class catalog" and "premium studio-produced course" variants are therefore **not asserted from direct evidence**; the marketplace variant is covered by Udemy instead. No precise claims about either product appear in the final document.
- Khan Academy's exact mastery/progress mechanics (levels, points) not verified from fetched pages — final doc keeps progress description generic.
- TED-Ed lesson-page internals (embedded quizzes etc.) not verified — not claimed.
- Historical samples (MIT OCW, iTunes U) used from general knowledge for the historical check only — they anchor the *absence* claims (no accounts/progress required), which is safe because the claim is about non-requirement, not about their detailed operation.

## Final Synthesis

The Educational Content Platform is the **library-shaped** Type of the education domain: its product is a standing, organized catalog of instructional content — supplied by the operator (produced, curated, or authored by independent instructors) and structured for learning (subjects → courses/series → lessons) — which learners browse and consume directly, at their own pace, on their own initiative. There is no enrollment act, no cohort, no instructor-managed assignment or grading; where educators or institutions appear (K-12 reporting, marketplace production roles, educator customization), they are layers on the library, not the core relationship. Mature products add accounts with progress state, practice machinery, apps, discovery, certificates, reviews, and habit mechanics; variants span production model, access model, audience segment, and AI-tutor layering. The Type sits between course-managing Types (LMS, MOOC) that structure the learner relationship, and general content/media Types that lack instructional organization.
