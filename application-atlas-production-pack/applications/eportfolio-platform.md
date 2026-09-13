# ePortfolio Platform

## Overview

An **ePortfolio Platform** is a web application where a person builds and manages a living record of their own work: they collect evidence of what they have done — documents, images, video and audio, files, notes, journal entries — frame that evidence with their own reflection or commentary, assemble selected evidence into presentable portfolio pages, and control exactly who can see each portfolio, from fully private, through named individuals, groups, or courses, to the open web.

The defining core is small:

```text
Personal evidence record — the work samples a person collects and owns
└── Portfolio surfaces   — selective presentations assembled from that record
    └── Holder framing   — reflection, captions, and narrative that present the
                          work as evidence of learning or development
        └── Controlled audience access — deliberate sharing decisions, with
            instructors/assessors as a first-class audience
```

Everything else commonly associated with these products — institutional templates, assignment submission, grades and outcomes mapping, competency frameworks, family portals, public showcase publishing, mobile capture — is standard or optional capability layered on this core, not what makes the product an ePortfolio platform. A paper binder of work samples with reflection statements and an audience satisfies the same structure; a self-assembled personal site used as a portfolio does too.

The platform is centered on the holder, not the course and not the institution. When the course container, its materials, and its gradebook become the center, the product is a Learning Management System. When publishing arbitrary sites becomes the center, it is a website builder.

## Users & Context

**Primary user — the portfolio holder.** A student, trainee, or professional who accumulates evidence over time. Their recurring work: capture or import work samples, write reflections about them, assemble them into portfolio pages for a specific audience, adjust who can see what, and respond to feedback. The portfolio holder's space is private by nature; sharing is always an explicit act.

**Instructor / advisor / assessor.** Views portfolios they have been given access to, leaves comments and feedback, and — in education deployments — receives submitted portfolios for assessment against rubrics, outcomes, or professional requirements. External supervisors (for example, a placement mentor outside the teaching institution) may be given assessor access without being staff.

**Institution administrators.** Distribute templates and structured workbook formats, manage accounts and competency frameworks, and read institutional reporting over portfolio activity.

**Audience members.** Peers and reviewers invited to comment; family members connected to a child's journal in school deployments; potential employers and the public where the holder publishes openly.

Typical contexts: coursework portfolios that accumulate across years rather than a single course; placement and professional-practice records; capstone and first-year-experience programs; career and employability showcases; continuing professional development.

## Core Model

### The defining core

Four structures. Removing any one of them collapses the product into a neighboring Type.

- **Personal evidence record.** The portfolio holder owns an accumulating store of work samples: uploaded files, captured photos/video/audio, embedded external media, written entries, and structured records such as résumé details or plan entries. Evidence lives in this store whether or not it is currently on display, and it persists across courses, years, and programs. Without it, the product is a generic site or file publisher with no memory of the person's work.

- **Portfolio surfaces.** Presentations the holder deliberately assembles from the evidence record — a page of selected artifacts, an ordered set of pages forming one portfolio, a completed workbook, or a chronological learning journal. A single evidence item can appear on multiple surfaces. The act of selection and arrangement is what makes a surface a portfolio rather than a feed or a folder; without it, the product is a file store or activity stream.

- **Holder framing.** The holder's own voice attached to the work — a reflection that explains what a sample demonstrates, a caption, a narrative that gives the collection meaning as evidence of learning, growth, or capability. Without any holder-authored framing, a portfolio degrades into a file listing.

- **Controlled audience access.** Each portfolio surface has an audience the holder chooses: nobody (private), specific people, a group, a class or course, an entire institution, or everyone. Instructors and assessors are a first-class audience with a distinct reason for access — viewing and judging the work. Without audience control, the product is a private notes app or a plain website.

### One core, several realizations

The products in this space name and shape the same concepts differently, and the definitions above deliberately do not depend on any one naming:

```text
Evidence record:    artifacts attached to an evidence store; assets in a private
                    personal space; files in a library; posts in a student journal
Portfolio surfaces: pages and ordered page collections; completed workbooks and
                    portfolios; works built from pages, sections and modules;
                    a per-student learning journal organized with folders
Framing:            reflections and journal entries; reflection prompts built into
                    templates; text and voice commentary on posts
Audience control:   share settings per person/group/institution/public; permission
                    tiers with named viewer roles; class and family visibility rules
```

### Standard capabilities mature products commonly add

- **Structure distributed to learners.** Institutions prepare templates, workbooks, or assigned activities that scaffold what evidence to collect and where reflection belongs; the learner completes rather than invents the structure. Templates commonly carry instructions that survive copying, and may protect their layout from accidental changes.
- **Feedback and assessment machinery.** Comments on a portfolio or on individual evidence items; submission of a portfolio for assessment; grades, rubrics, or outcome/competency mapping where the deployment is academic. Some products map evidence to a competency or standards framework and show coverage at a glance.
- **Personal content types.** Journals or blogs as first-class evidence inputs; plans and tasks; résumé and profile sections; structured forms for placement or practice records.
- **Draft vs shared state.** The working version of a portfolio and what the audience currently sees are kept distinct in mature products, whether through explicit publish steps, share states, or snapshot copies made at submission.
- **Media authoring in place.** Capture of photo, video, or audio directly into a portfolio page or journal post, plus embedding of content hosted elsewhere.
- **Integration with the learning ecosystem.** Single sign-on and rostering from the institution's systems; assignment hand-out and grade return through LMS integrations, so the portfolio work happens in the portfolio while the course shell stays the course's.
- **Institutional reporting** over portfolio activity and, where present, outcome coverage.
- **Continuity.** Export or download of one's own work, and continued access after leaving the institution in mature deployments.

## How It Works

### The personal authoring loop

The loop the portfolio holder repeats, often over months or years:

```text
Capture or import evidence (upload files, record media, write a journal entry)
→ add framing (reflection, caption, note explaining what the evidence shows)
→ assemble a portfolio surface (arrange evidence blocks on a page,
  complete a distributed template or workbook, or let a journal accumulate)
→ decide the audience (keep private, invite named reviewers,
  open to the class/institution, publish to the web)
→ receive comments and feedback from that audience
→ revise the surface and grow the evidence record
```

Nothing in this loop requires a course. A person can run it entirely for their own development, a job search, or professional registration evidence.

### The institutional loop (where the platform is deployed by an organization)

```text
Instructor or resource builder prepares structure (template, workbook, assignment)
→ structure is handed out to enrolled learners
→ learners complete the structure with their own evidence and reflection
→ learner submits the portfolio for review or assessment
→ assessor views, comments, and records feedback or a grade
→ submitted portfolio is released back; the holder keeps working on the original
```

A common pattern in assessment deployments: when a portfolio is submitted for assessment, the system works with a copy or a locked state so the judgment is made against a fixed version, while the holder continues editing their own original. The submitted state typically unlocks or is released back to the holder after review.

### Sharing is surface-level

Evidence items can be re-used freely across many portfolio surfaces, but the audience is granted at the surface — a page, a collection, a completed workbook — not file by file. The holder composes a surface for an audience rather than handing out raw items. Some products allow grants to be scoped further, for example time-boxed or limited to the duration of an assessment.

## Interfaces

The surfaces below are described conceptually; exact layout and naming vary by product.

### Portfolio overview / manage screen

The holder's home for their portfolios.

- lists the holder's portfolio surfaces with state (private or shared, submitted or released, draft or published)
- primary actions: create a new page/collection/portfolio, copy an existing one (own work, distributed templates, or others' work where copying is allowed), open for editing, manage sharing

### Editor

The authoring surface for a portfolio page or equivalent.

- drag-and-drop layout of content blocks or modules (text, images, embedded media, files, journal excerpts, résumé fields)
- media capture from camera/microphone in place; linking to externally hosted content
- template scaffolding where the institution distributed one: pre-placed blocks, instructions, and reflection prompts
- primary actions: add/arrange/configure content, save, preview as the audience will see it

### Sharing / permissions screen

The audience-control surface — the interface where the defining "who can see this" decision is made.

- audience choices from private through named individuals, groups, courses, institution-wide, to public web
- optional password protection, directory or profile listing, secret/unlisted links, and expiration or time-window constraints in some products
- primary actions: grant, change, or revoke access; set the published vs working state

### Evidence store

The holder's content library.

- uploaded files, media, journal/blog entries, notes, résumé entries, structured forms
- primary actions: upload, organize (folders, tags), re-use in any portfolio surface

### Review / assessment view

The assessor's surface.

- the portfolio presented the way the audience sees it, with per-evidence commenting and (where present) rubric or outcome entry
- submission queues listing learners' submitted work; gradebook linkage in academic deployments; filters by student, date, or standard in school deployments

### Audience view

What a viewer gets: a readable, self-navigating presentation of the holder's work with its framing, plus — where the holder allows it — the ability to comment.

## Important Rules / Behaviors

- **Private by default, shared on purpose.** Across the researched products, new work is visible only to its holder (and, in institutional deployments, designated administrators); any audience requires an explicit grant. This is the load-bearing privacy rule of the Type.
- **Ownership stays with the holder.** The holder can change or revoke access at any time, keep working on their portfolio after feedback, and in mature products export or delete their own work. The institution adds structure and judgment; it does not take over the record.
- **Audience attaches to surfaces, not raw evidence.** An evidence item may sit unused in the store indefinitely; only when the holder places it on a shared surface can that audience see it.
- **Assessment freezes a version, not the record.** Where portfolios are submitted for assessment, the review targets a fixed copy or locked state; the holder's original continues to evolve and is returned/released afterward.
- **Templates structure without dispossessing.** A distributed template or workbook shapes the learner's portfolio (instructions, protected layout, prompts), but the completed result lives in the learner's own space and carries their evidence.
- **Moderation exists in younger audiences.** In school deployments, a teacher typically approves, edits, or removes posts in student journals, and family members see only what the class settings allow. This is a segment behavior, not a universal rule.
- **What the audience sees can trail the working version.** Depending on the product, viewers see the last published/shared state rather than every keystroke; exact publish mechanics vary.

## Variants

- **Developmental / learning portfolio.** Evidence accumulates continuously; reflection is central; audience is usually advisor and peers; journals and workbooks dominate.
- **Assessment / accreditation portfolio.** Institution-templated, tied to outcomes or professional requirements, driven by submission-and-review cycles; institutional reporting matters.
- **Showcase / career portfolio.** Curated best work for employers or admission; public or link sharing; framing is presentational; the developmental machinery recedes.
- **School (K-12) portfolio.** Class-container and student journal model; teacher moderation; family access; standards-tagged work samples for conferences and reviews.
- **Professional practice / CPD portfolio.** Placement logs, structured forms with assessor sign-off, registration or competency evidence; mobile capture matters.
- **Packaging variants.** Standalone platforms; ePortfolio modules bundled inside LMS or student-success suites; the defining core is identical, the surroundings differ.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Learning Management System (LMS) | course-centered: content delivery, course-scoped assignments, gradebook. An ePortfolio centers the learner-owned evidence record that persists across courses and years; LMS integrations hand work in and grades back, and some LMS vendors bundle an ePortfolio module as packaging |
| Website Builder | publishes general-purpose sites; no owned evidence record, no reflection/assessment semantics, no structured audience tiers. A purely public showcase portfolio with no record or feedback loop drifts toward this Type |
| Blogging Platform | reverse-chronological posts are the primary object; an ePortfolio's primary object is the curated evidence record with selective surfaces (products here often include blogs as evidence inputs, which shows the seam from both sides) |
| Digital Credential Platform | issuer-attested achievement artifacts (badges/certificates) that third parties verify; an ePortfolio holds holder-curated work. Some credential products attach portfolio evidence — the drift edge |
| Résumé Builder | outputs a short portable application document; an ePortfolio is a living web surface with an evidence record |
| Institutional Repository | the organization publishes and preserves scholarly output; an ePortfolio is the individual's learning and work record |
| Note-taking / Personal Knowledge Management | private capture without portfolio surfaces or audience control |
| Assessment Platform / Digital Gradebook | institutional judgment machinery; may be embedded in education ePortfolio deployments but is not the center of this Type |

The closest boundary is with the LMS. The structural test: remove the learner's personal, cross-course, years-spanning evidence record and portfolio authoring, and what remains is an LMS; remove the course container from an ePortfolio platform and it still fully works.

## Representative Products

- **Mahara** — open-source, institution-hosted; page/collection portfolio model with artefact re-use, templates, submission-and-release, competency mapping
- **PebblePad** — commercial, higher education and professional programs; personal creative space plus institutional assessment workspaces; workbook-led structure
- **Digication** — US higher education; template-driven ePortfolios integrated with assignments, outcomes assessment, and accreditation reporting
- **Seesaw** — K-12; class-managed student learning journals with teacher moderation and family access

The core definition was checked against older and non-platform practices (paper/binder portfolios, self-assembled personal sites used as portfolios) to avoid defining the Type by the current institutional template-and-assessment implementation.

## Sources

Research date: **2026-09-07**. All sources are official product documentation or product pages.

- Mahara — product site: https://mahara.org/ ; user manual 25.04 (Create / Portfolios chapters): https://manual.mahara.org/en/25.04/index.html , https://manual.mahara.org/en/25.04/create.html , https://manual.mahara.org/en/25.04/portfolio/pages.html
- PebblePad — product site: https://pebblepad.com/ ; Help Hub (roles, learners overview): https://helphub.pebblepad.com/support/home , https://helphub.pebblepad.com/support/solutions/articles/101000539578-pebblepad-for-learners
- Digication — product page: https://www.digication.com/learning-platform/eportfolio ; Help Desk (Student Guide; share & publish): https://support.digication.com/hc/en-us , https://support.digication.com/hc/en-us/articles/11155625634971-Share-and-publish-your-Work
- Seesaw — Help Center (Teachers; Learning Journal): https://help.seesaw.me/hc/en-us , https://help.seesaw.me/hc/en-us/articles/17964262819341-The-Learning-Journal-Navigating-The-Learning-Journal-as-a-teacher , https://help.seesaw.me/hc/en-us/articles/203728745

> Sourcing note: findings are calibrated to what these official sources document. Precise product parameters (export formats, storage limits, exact permission matrices beyond those quoted) were not verified and are intentionally not stated. Detailed product-by-product observations and cross-product comparison are recorded in the paired Research Notes.
