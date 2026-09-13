# Research Notes — ePortfolio Platform

Research date: **2026-09-07**. Directory leaf: `ePortfolio Platform` (§23 Education, Research & Knowledge Institutions).

---

## Research Goal

Understand what an ePortfolio Platform actually is as an Application Type: what objects exist inside it (evidence/artifacts, portfolio pages/surfaces, reflections, templates), how the portfolio is built and shared over time, what the institutional/assessment layer looks like, who owns the content, and where the boundary lies against neighboring Types (LMS, website builder, blogging platform, digital credential platform, résumé builder, institutional repository, note-taking/PKM).

## Initial Boundary (working hypothesis before research)

- Hypothesized core: individuals (mainly learners) collect work evidence over time, reflect on it, assemble it into presentable portfolio surfaces, and control who sees each surface (advisor/assessor, peers, family, employer, public web). Institutions typically add templates/assignments and assessment/feedback machinery.
- Suspected confusions (checked against prior passes in this repository):
  - **Digital Credential Platform** — prior pass recorded: "holder-curated work and evidence collections vs issuer-attested achievements; some products enrich badges with portfolio attachments (the drift edge)". Held.
  - **Résumé Builder** — prior pass recorded: "persistent web surface assembling evidence of learning/work; résumé builder outputs a short portable document". Held.
  - **LMS** — LMS is course-container-centered; several LMS vendors ship ePortfolio modules, which makes packaging overlap real but the core model distinct.
  - **Website Builder / Blogging Platform** — general publishing without a personal evidence record or assessor audience.
  - **Institutional Repository** — organization-published scholarly record, not a personal learning record.

## Research Questions

1. What are the core objects — evidence items, portfolio surfaces, containers, reflection records?
2. What is the authoring workflow (capture → reflect → assemble → share → feedback → revise)?
3. Who owns the content, and what are the default privacy/sharing mechanics?
4. How do institutional templates/assignments/workbooks coexist with free authoring?
5. How does the assessment/feedback layer work (submission, locking, release, rubrics/outcomes)?
6. What audiences does sharing serve (instructor, peers, family, employer, public)?
7. What export/portability and continuity (alumni) mechanisms exist?
8. What variants exist (developmental vs showcase vs assessment portfolio; K-12 vs HE vs professional)?

## Representative Products

| Product | Segment | Philosophy | Why sampled |
|---|---|---|---|
| **Mahara** | open-source, HE/institution-hosted | portfolio-centric (pages/collections/artefacts), community-maintained | deep official manual reachable; open-source pole |
| **PebblePad** | commercial, UK-origin HE + professional programs | workbook + portfolio hybrid; personal space (Pebble+) + institutional space (ATLAS) | official Help Hub with role-based docs; structured-workbook pole |
| **Digication** | US higher education | assessment-integrated ePortfolio; outcome/accreditation orientation | official Help Desk student/faculty/admin guides; publish/permission model |
| **Seesaw** | K-12 schools/districts | class-managed student journal + family sharing | official Help Center; K-12 pole with teacher moderation |

Sample spans open-source vs commercial, higher-ed vs K-12, free-form vs template-driven, personal-showcase vs assessment-centric.

## Sources

All Tier 1 (official help/user documentation) and Tier 2 (official product pages), fetched 2026-09-07.

- Mahara: https://mahara.org/ (product home; purposes, sharing, LTI, groups) · https://manual.mahara.org/en/25.04/index.html (manual index) · https://manual.mahara.org/en/25.04/create.html (Create chapter: portfolios, blocks, journals, plans, résumé, SmartEvidence, feedback) · https://manual.mahara.org/en/25.04/portfolio/pages.html (pages, collections, sharing, submission, sign-off/verification)
- PebblePad: https://pebblepad.com/ (product home) · https://helphub.pebblepad.com/support/home (Help Hub, role folders) · https://helphub.pebblepad.com/support/solutions/articles/101000539578-pebblepad-for-learners (Pebble+ / PebblePocket / ATLAS)
- Digication: https://support.digication.com/hc/en-us (help desk) · https://www.digication.com/learning-platform/eportfolio (product page) · https://support.digication.com/hc/en-us/categories/9858828640667-Student-Guide (student guide index) · https://support.digication.com/hc/en-us/articles/11155625634971-Share-and-publish-your-Work (share/publish/permissions)
- Seesaw: https://help.seesaw.me/hc/en-us (help center) · https://help.seesaw.me/hc/en-us/categories/4525918493453-Teachers (teacher categories) · https://help.seesaw.me/hc/en-us/articles/203728745 (co-teachers, permissions) · https://help.seesaw.me/hc/en-us/articles/17964262819341-The-Learning-Journal-Navigating-The-Learning-Journal-as-a-teacher (journal model)

Access limitation noted: initial attempts at the Mahara manual root and wiki returned 404 / closed-GitLab pages; the correct versioned manual path (25.04) was found via the mahara.org footer link, after which Tier-1 manual pages were fully reachable. No claims below rely on model memory for product specifics.

---

## Product Observations

### Mahara — Key observations (Evidence layer A: official manual + product site)

- Positioning (mahara.org): "students and staff create their personal learning stories by uploading evidence of activities… write reflections on their experiences that frame this evidence, map it to competencies or registration requirements, and provide necessary context." Named portfolio purposes: study, professional development, work-integrated learning, assessment, showcase and presentation, employability.
- Core object chain (manual, Create chapter): **artefacts** ("learning evidence") are created/collected; **pages** arrange artefacts for presentation; **collections** are ordered series of pages with navigation; pages/collections are collectively called **portfolios** (renamed in 22.10).
- Structural sharing rule (manual): "You can only share artefacts with individuals or groups of people when you placed them on a page and give others the permission to view that portfolio." Artefacts are re-usable across any number of pages.
- Page composition via **blocks**: files/images/video, journal posts, general (text, navigation, comments), personal info, external content (RSS feed to an external blog). Drag-and-drop grid layout; keyboard/screen-reader accessible layout mode.
- Personal content store beyond files: **Files** (browser, quota), **Journals** (multiple journals, entries with images/attachments), **CPD** activities, **Notes**, **Plans** (with tasks), **Résumé** (education, employment, achievements, goals and skills, interests).
- Sharing (manual + site): with a specific person, a group, an institution, all registered users, or the public internet; **secret URL** sharing; access can be restricted to a **time frame** or "just within an assessment task".
- Copy/template machinery: pages can be copied from others who allow copying; a page can be marked **template** (copied pages preserve instructions; "prevent removing of blocks" option protects template structure); page **instructions** scaffold learners.
- Submission for assessment (manual): submitting a page/collection to a group or LMS activity **makes a copy that is locked from editing** until released; submitted/released states displayed; release converts back to editable; original vs submitted copy distinguished.
- Sign-off/verification: author signs off a page; a manager can verify (cannot revoke; author revokes sign-off); a **Portfolio completion** progress page aggregates sign-offs/verifications across a collection.
- **SmartEvidence**: institution-provided competency frameworks; evidence mapped to framework elements via annotations; annotations can receive feedback; matrix map view over a collection.
- Feedback: page-level and artefact-level comments, private comments, ratings, "Details" mode surfacing per-artefact commenting for assessment; watchlist notifications on changes.
- **Timeline**: save a page's state as a version snapshot and revisit/compare later.
- Other: profile page deliberately separated from portfolio pages ("use regular pages to create your portfolio and your profile page as a business card"); anonymise option; objectionable-material reporting; groups support collaborative portfolios and forums; multi-tenant institutions; LTI submission to LMS for marking (Moodle integration documented); mobile app.

### PebblePad — Key observations (Evidence layer A: official Help Hub + product site)

- Help Hub role model (six documented roles): **Learners** ("completing, collecting and curating work"), **Resource Builders** ("building custom templates and workbooks"), **Externals** (non-staff "coaching or assessing learners"), **Assessors** ("providing comments, feedback & grades"), **Workspace Managers** ("organising and overseeing learning and assessment in ATLAS"), **Platform Administrators**.
- Three core learner spaces ("PebblePad for learners"): **Pebble+** (the creative space: "create your own portfolios and blogs, complete templates and workbooks, and upload and save a range of files to use and reuse in your work"), **PebblePocket** (mobile app for in-the-moment capture — photo, video, blog post, reflection; works offline; custom course forms; digital signing by assessors), **ATLAS** ("Active Teaching & Learning Assessment Space" — institutional workspaces described as "digital classrooms"; work handed out as resources; submissions for feedback and grades).
- Ownership/privacy (Help Hub): "Every person's Pebble+ account is private to them. What you keep in your asset store cannot be seen by anyone else, until you expressly choose to share it."
- Sharing destinations: with other users (comment/collaboration), with the web (public), or with ATLAS (feedback and assessment) via submission.
- Product site positioning: "Flexible ePortfolio, workbook and assessment platform"; reflection and assessment embedded in learning design; staff/external supervisors give feedback and view progress in real time; LMS/VLE integration for enrolment and grade sync; alumni accounts let graduates "retain access to all their assets after leaving university and continue to track their development".
- Workbook pole (customer quote on site): workbook activities and assessment processes "align with program goals and any professionally mandated competencies" (nursing/social-work style professional programs implied).
- 2026-era additions on site: Progress Tracking & Insight Dashboards (institutional readiness insight) — new module, vendor-branded.

### Digication — Key observations (Evidence layer A: product page + Help Desk)

- Product page: "Create visually compelling ePortfolios… share your achievements, growth and reflections with peers, teachers and potential employers." Featured portfolio genres: First Year Experience, Capstone, Study Abroad, Advising, Internship, Service Learning, Global Learning.
- Platform positioning: "ePortfolios generate structured evidence of student learning, powering outcomes assessment, supporting accreditation, and surfacing retention insights."
- Authoring (product page + Student Guide): templates ("Schools can even share templates across a course or the whole campus"); drag-and-drop editor, no coding; capture image/video/audio "right on the page"; multimedia embeds (YouTube, Vimeo, SoundCloud, "hundreds more"); mobile-friendly responsive output.
- Kora object model (Student Guide sections): a portfolio is a **Work** composed of **Pages**, **Sections**, and **Modules** (text, image search, embeds, equations, tables, Google Docs/Sheets/Slides); files live in the **Library** (upload, image search, hide previously uploaded files); layout via moving/resizing modules, Organizer tool; style customization (backgrounds, opacity, whole-Work styles).
- Share/publish model (Share and publish article — precise): permission tiers **Private** (default; "only by you and your institution's Digication Administrators"), **Private within [your school]** (all logged-in faculty/students; optional listing in the school-wide **ePortfolio Directory** and user profile), **Public** (viewable outside the institution and indexable by search engines); per-individual/group/course grants with roles **Viewer / Editor / Publisher / Admin**; optional password protection; custom URL; thumbnail; social sharing; **published version vs unpublished changes** with per-page or all-page publishing.
- Course/assignment layer (Student Guide): courses, assignments ("Working on Your First Assignment: Using a Template"), "Submit Work", "View my works in progress and submissions", gradebook progress view; AI Reflection Assistant for assignments; LMS access via Canvas / Blackboard / Moodle / Sakai / Brightspace.
- Continuity: "Download your Work" (export); "Update or delete your Digication account or contents".

### Seesaw — Key observations (Evidence layer A: official Help Center)

- K-12 classroom container model: teacher creates a **class**, adds **students** (sign-in modes include QR codes and SSO/email), invites **family members**; co-teachers share full permissions ("approve, delete, or edit posts, invite and approve family members"); subscription tiers exist.
- **Learning Journal** ("where all learning lives in Seesaw"): per-student journals and a class journal; **posts** added by students and teachers (creative canvas: photos, video, drawings, text); drafts supported; calendar view; **folders** organize work.
- Review/mastery surface for teachers: filter journals by student, group, date range, folder, and **standards**; documented use cases include IEP-meeting evidence ("filter by student & standard"), parent-teacher/student-led conferences ("filter by student & date").
- Interaction on posts: like, comment (text and **voice comment**), "Seen by" viewer tracking; **Private (Teachers only) folder** and private notes; teacher approval/moderation of posts.
- Adjacent surfaces in the same product: **Blogs** (class blog publishing with privacy options, connected blogs), Activities/lessons library, gradebook + formative assessment + sitewide standards, Messages/announcements with translation, LTI integrations (Canvas, Schoology).

---

## Cross-product Comparison

| Dimension | Mahara | PebblePad | Digication | Seesaw | Reading |
|---|---|---|---|---|---|
| Unit of collected evidence | artefact (file, journal post, résumé entry, note, media…) | asset (file, template/workbook entry, blog post) | Library file + Work content | post in the student journal | **All four: a personal, accumulating evidence store owned by the holder** |
| Portfolio surface | page / collection ("portfolio") | portfolio; workbook pages | Work (pages/sections/modules) | student Learning Journal (chronological + folders) | All four render a selective/personal presentation; form varies from free canvas to chronological journal |
| Reflection/framing | reflections "frame this evidence"; journals, text blocks | reflection prompts in templates/workbooks; blogs | text modules; AI Reflection Assistant | captions, notes, voice recordings | Present in all four; pedagogically central in three |
| Ownership/privacy default | pages private until shared; explicit manage-access | asset store private "until you expressly choose to share" | new Work default Private | journal visible to class/family per settings; teacher-only folders | **All four: private by default, sharing is a deliberate act** |
| Sharing audiences | person / group / institution / registered / public / secret URL; time-boxed | users / web / ATLAS (assessment) | private / school / public + per-person/group/course; password; directory | class + invited families; teacher moderation; optional class blog | Audience spectrum private→institutional→public is universal |
| Institutional structure layer | copyable templates with instructions; groups | templates + workbooks via ATLAS; six roles incl. externals | templates; courses + assignments | teacher-assigned activities | Common where institution is present; absent in pure personal use |
| Assessment machinery | submission copies locked then released; sign-off/verify; SmartEvidence competency mapping | ATLAS submissions; assessor feedback/grades; digital signing; competency alignment | assignments, Submit Work, gradebook, outcomes/accreditation positioning | approval, standards tagging, gradebook, formative assessment | Common in education deployments; not needed for showcase use |
| LMS integration | LTI submission (Moodle documented) | LMS/VLE enrolment + grade sync | Canvas/Blackboard/Moodle/Sakai/Brightspace access | Canvas/Schoology LTI | Universal seam; confirms the boundary against LMS |
| Capture surfaces | web authoring; mobile app | PebblePocket offline mobile capture; custom forms | capture photo/video/audio "right on the page" | creative canvas; app-first | Common; form varies by segment |
| Continuity/export | timeline snapshots; copy machinery | alumni accounts retain assets | Download your Work; account/content control | class archive behavior documented only partially | Common intent, mechanisms vary; keep generic |
| Audience-facing "publish" state | share state, no draft/publish split | share to web | explicit draft vs published version | blog publishing | Product-specific machinery over a shared concept |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (minimal)

```text
Personal Evidence Record
└── Portfolio Surfaces assembled from it (selective, holder-arranged)
    └── Holder-authored framing of the work (reflection/captions/narrative)
        └── Controlled audience access (private → institutional → public;
            assessor/advisor as a first-class audience)
```

Four properties. Remove the **personal evidence record** → a generic website/asset publisher with no growing record of the person's work. Remove **holder-assembled surfaces** → a file store or activity feed. Remove **holder framing** → a file listing (no portfolio narrative; drifts to generic site builder or storage). Remove **controlled audience access** → a private journal/notes app. All four are present in every sampled product and in older/paper and self-assembled (personal-site) portfolio practices.

Deliberately NOT in L0 (historical/market-sample check): reflection is *framing*, not a mandated reflective-writing apparatus (paper binders and showcase portfolios satisfy the Type with captions alone); institutional context, templates, assessment machinery, competency mapping, family portals, cloud hosting, mobile capture — none required (paper portfolios, WordPress/Google-Sites self-assembled ePortfolios, and career showcase sites satisfy the core without them).

### L1 — Common Mature Structure

- Institutional structure layer: templates, workbooks, or assigned activities that learners complete and that scaffold what evidence to collect.
- Feedback/assessment loop: comment/feedback on portfolio or artefacts; submission-for-assessment with copy/lock/release or publish states; grades/rubrics/outcomes where the deployment is academic.
- Personal content store beyond files: journals/blogs, plans/tasks, résumé/profile sections as first-class evidence inputs.
- Re-use: one evidence item can appear on multiple portfolio surfaces.
- Draft vs shared/published state distinctions (concept universal; machinery varies).
- Mobile capture; media embedding; drag-and-drop/block-style authoring.
- LMS/VLE integration (LTI-class) for identity, assignment hand-out, and grade sync.
- Institutional reporting/analytics over portfolio activity.
- Export/download of one's own work; continued access beyond enrollment (alumni accounts).

### L2 — Variant / Optional Structure

- Family/caregiver access and teacher post-moderation (K-12 variant).
- Competency/standards mapping (framework matrices, standards filters, professional-registration requirements).
- Public publishing with custom URL, directory/profile listing, social sharing, search-engine indexing.
- Digital signing of structured placement/practice forms (professional-practice variant).
- Anonymous presentation, version timelines, watchlists, collaborative group portfolios.
- Adjacent surfaces that may co-exist without defining the Type: class blogs, badge/credential attachment, messaging.

### L3 — Vendor-specific (kept out of the final document)

- Mahara: SmartEvidence, secret URLs, sign-off/verification/portfolio-completion pages, skins, "Create via tags", Gridstack layout engine, objectionable-material reporting, isolated institutions, anonymise switch.
- PebblePad: Pebble+ / ATLAS / PebblePocket naming and split; Resource Builders/Externals roles; digital signing; Progress Tracking & Insight Dashboards; myday engagement-platform pairing.
- Digication: Kora platform naming; Work/Library/Organizer terminology; Viewer/Editor/Publisher/Admin role names; ePortfolio Directory; AI Reflection Assistant; TORI reflective-inquiry taxonomy; OAIR.
- Seesaw: Creative Canvas, Highlights, Seesaw Library/lessons, AI credits, connected blogs, sitewide standards, class QR/Home Learning codes, Seen-by tracking.

## Vendor-specific Findings

- The draft/published-version machinery is Digication-explicit (publish per page); Mahara achieves a similar audience effect via share states and submission copies; treat precise publish semantics as product-specific.
- PebblePad's three-space architecture (personal Pebble+ / institutional ATLAS / mobile PebblePocket) is a named, branded realization of the common personal-space + institutional-space pattern; do not promote the names.
- Seesaw's journal is chronological-first rather than page-curation-first — the K-12 pole of the same Type; folders/standards provide selection.
- Mahara's timeline and sign-off/verification chain are distinctive governance features.

## Boundary Findings

| Neighboring Type | Test ("remove what → becomes the other Type") | Verdict |
|---|---|---|
| Learning Management System (LMS) | Remove the learner-owned, cross-course, years-spanning evidence record and portfolio authoring → course-container-centered delivery system remains (LMS). Conversely an ePortfolio without any course layer still works. | Distinct Type; LTI/submission is the interlock; LMS-bundled ePortfolio modules are packaging variants |
| Website Builder | Remove the personal evidence record + reflection/assessment audience semantics → general-purpose site publishing. Drift edge: a purely public showcase portfolio with no record/feedback loop is functionally a personal site. | Distinct Type with a real drift edge |
| Blogging Platform | Remove curated portfolio surfaces (keep reverse-chronological posts as the primary object) → blogging platform. ePortfolio products *include* blogs as evidence inputs, showing the seam from both sides. | Distinct Type |
| Digital Credential Platform | Holder-curated work/evidence vs issuer-attested achievement artifacts (consistent with prior pass). | Distinct Type; badge-attachment is the drift edge |
| Résumé Builder | Living web surface assembling evidence vs a short portable document (consistent with prior pass). | Distinct Type |
| Institutional Repository | Organization-published scholarly record vs personal learning/evidence record. | Distinct Type |
| Note-taking / Personal Knowledge Management | Private capture without portfolio surfaces or audience control. | Distinct Type |
| Assessment Platform / Digital Gradebook | Assessment machinery is a *layer* inside education ePortfolios, not the center; the center remains the holder's evidence record and portfolio authoring. | Adjacent; machinery may be embedded |

## Historical / Market-Sample Check (§24 applied)

- **Paper/binder portfolios** (pre-platform): work samples + captions/reflection statements + shown to an advisor/panel — satisfies the four L0 properties → the definition is not over-fitted to cloud platforms.
- **Self-assembled web ePortfolios** (generic site builders/blogs used as ePortfolios): satisfy L0 without dedicated templates, assessment machinery, competency mapping, or family portals → those features stay out of the defining core.
- **K-12 journals, professional placement portfolios, career showcases**: all four poles sampled directly; each satisfies the core while differing on nearly every L1/L2 feature → confirms the abstraction level.

## Uncertainties

- Export formats (e.g., standards-based portfolio interchange) were not directly verified in fetched pages; kept generic ("mature products provide export/download of one's work" — directly observed only for Digication's "Download your Work"; PebblePad alumni retention observed at positioning level).
- Seesaw's archive/continuity behavior across years was not directly documented in fetched articles; not claimed.
- PebblePad's full asset-type taxonomy was not enumerated; observations rely on the learner overview and role docs (sufficient for structure, not for exhaustive lists).
- Portfolium, Pathbrite, Foliotek, Watermark/Tk20, and WordPress-as-ePortfolio were not directly researched; used only as market-context notes, no claims drawn from them.

## Final Synthesis

An ePortfolio Platform is a personal-evidence system: the portfolio holder accumulates work samples and reflective framing in an owned record, assembles selective portfolio surfaces from that record over time, and decides who sees each surface — from fully private, through named individuals/groups/courses, to the open web — with advisors/assessors as a first-class audience. Institutions add a structure-and-judgment layer (templates/workbooks/assignments; comments, grades, outcomes) on top of, but not instead of, the holder's ownership. The Type's identity lives in the four-property core; everything else — templates, assessment, competency mapping, family access, public publishing, mobile capture — is common structure or variant, shaped strongly by segment (K-12 vs higher-ed vs professional).
