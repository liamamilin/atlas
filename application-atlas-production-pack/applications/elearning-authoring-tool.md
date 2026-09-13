# eLearning Authoring Tool

## Overview

An **eLearning Authoring Tool** is an authoring application for creating interactive, self-paced learning content — courses, modules, lessons — and publishing it as a deliverable that a delivery system (typically a learning management system, a website, or a hosted link) presents to learners.

The defining core is small:

```text
Authored course project
└── content composed with learner-facing interactivity
    └── publishable learner-facing deliverable
        └── handed to a delivery system outside the authoring environment
```

Three properties. If any one is removed, the product is no longer recognizable as an eLearning Authoring Tool:

- **A persistent authored course project** — the author creates, names, edits, and revisits a self-contained unit of instruction over time. Without it, the software is a one-off content generator.
- **Learner-facing interactivity composed into the content** — the author assembles instructional content together with elements the *learner* will operate: questions with feedback and scoring, interactive objects, navigation and branching. Without it, the software is a presentation or document tool — content that a presenter drives, not content a learner works through.
- **A publishable learner-facing deliverable** — the finished project is exported or published as a package or hosted unit intended for delivery to learners outside the authoring environment. Without it, the software is a content platform or a delivery system, not a tool that produces content for one.

Everything else commonly associated with the category — SCORM packaging, cloud editing, AI assistance, template libraries, real-time collaboration, responsive design — is widespread in current products but is not what makes the product an authoring tool. Older desktop-era authoring tools from before learning-content standards existed, and open-source tools that publish embeddable content without SCORM at all, both satisfy the definition.

## Users & Context

The primary user is someone who produces learning content for an audience of learners:

- **Instructional designers and L&D specialists** — build structured courses with assessments, branching scenarios, and brand-consistent design; typically the power-user pole.
- **Subject-matter experts and internal trainers** — capture organizational knowledge directly as training content; a growing pole of products is deliberately designed so that non-specialists can author without design or technical skills.
- **Educators and academic staff** — build interactive learning activities and self-study materials, often inside the platforms their institution already runs.

Typical content: employee onboarding, compliance and policy training, product and systems training, sales enablement, higher-education and school learning activities, customer training. The work context is project-based: an author (or a small team) works on a course over days or weeks, collects stakeholder feedback, then publishes it to the organization's delivery platform.

## Core Model

### The course project

The center of the tool's world is the **course** (also called a module, lesson, or project). It is a persistent, self-contained authored object: it survives between editing sessions, can be duplicated to create variations, and represents the unit that will eventually be published. A course is typically organized into an internal structure — sections, chapters, topics, or a simple sequence of pages — that defines the learner's path through the material.

### Content and interactive elements

Inside the course, the author composes two kinds of material:

- **Instructional content** — text, images, video, audio, documents, and layout. This is what the learner reads and watches.
- **Interactive elements** — what the learner *does*. The characteristic elements are:
  - **Questions and assessments** — a library of question types (multiple choice, fill-in-the-blank, matching, drag-and-drop, sequencing, open response, and more, depending on the product) with correct answers, per-answer feedback, scoring, attempt limits, and often question pools with randomization so that repeated attempts draw different questions.
  - **Content interactions** — clickable hotspots, tabs, accordions, timelines, flip cards, labeled graphics, and similar objects that reveal or reorganize content in response to learner actions.
  - **Navigation and branching logic** — rules that decide what the learner sees next: conditional display of content, variables that record learner choices, and branching scenarios that route different learners down different paths (commonly used for decision-making and soft-skills practice).

The interactivity is what separates this Type from slide or document authoring: the author is programming a learner experience, not preparing a linear presentation.

### The publishable deliverable

The course, once finished, is **published** — turned into a deliverable that leaves the authoring environment:

- a **standards-based package** (SCORM, xAPI/Tin Can, AICC, and in some products cmi5) that is uploaded to a learning management system, which then delivers it to enrolled learners and reports progress and scores back;
- a **web publication** — a hosted page or link, an embed code for a portal or intranet, or a downloadable HTML bundle;
- occasionally other formats (PDF handouts, video exports) as secondary outputs.

The deliverable is the structural hinge of the Type: the authoring tool creates content; the delivery system (LMS or equivalent) handles learners, enrollment, and completion tracking. Some products also offer a lightweight delivery layer of their own — a hosted link service or a small built-in LMS — but this is an adjacent capability; the defining output remains the publishable course.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:            the course project
Implementations:    slide-based project, block-based course, screen-based course,
                    PowerPoint document, content-type instance inside a host platform

Concept:            learner-facing interactivity
Implementations:    trigger/state/variable engines, preset interaction templates,
                    content-type libraries, question engines, branching-scenario editors

Concept:            the publishable deliverable
Implementations:    SCORM/xAPI/AICC/cmi5 packages, hosted links, embed codes,
                    downloadable HTML, portable content files
```

A reader who has only seen one implementation — say, a slide-based desktop tool — should still be able to recognize a block-based web tool or an open-source embedded tool from the core model.

## How It Works

### The authoring loop

```text
Create a course (from scratch, from a template, or by importing existing material)
→ structure it (sections / pages / slides / screens)
→ compose each page: content + interactive elements
→ build assessments: questions, feedback, scoring, pools
→ add logic: conditions, variables, branching where needed
→ apply design: theme, layout, branding
→ preview as a learner (often per device type)
→ collect stakeholder review and revise
→ publish: package for the LMS, or host/embed for direct access
→ update and republish as content changes
```

Two entry accelerators are common: **templates** (pre-built course structures and page layouts, sometimes with draft content on common topics) and **import** (existing slide decks or documents converted into a first-draft course). Both are conveniences around the same loop, not the loop itself.

### The review loop

Course production is usually a team activity. Mature products provide a review mechanism in which stakeholders open the in-progress course — typically through a shared link, in a browser — and leave comments pinned to specific pages or screens; authors then resolve the feedback and republish. Some products add real-time co-authoring, task assignment from comments, and role-based access for reviewers versus editors.

### The delivery handoff

Publishing produces the deliverable and, where tracking is involved, connects it to the delivery system: the package carries the course plus the tracking instructions; the LMS (or the tool's own hosted delivery) presents it to learners and reports results back. Some products surface the results inside the authoring tool itself — a gradebook or results view per learner and per question — when tracking is enabled on their side.

### Capability tiers

**Defining core** — without these, not an eLearning Authoring Tool:

- persistent authored course project
- composition of content with learner-facing interactivity (questions/interactions/navigation)
- publishable learner-facing deliverable for a delivery system

**Standard capabilities** — present in most mature products:

- page/slide/block composition surfaces with drag-and-drop editing
- question/quiz machinery: multiple question types, scoring, feedback, attempts, pools/randomization
- conditional and branching logic
- templates, themes, and built-in asset libraries
- review and collaboration (comments, co-authoring, roles)
- standards-based export (SCORM/xAPI/AICC; cmi5 in some products) plus web publishing
- responsive multi-device output and learner-view preview
- accessibility support (alt text, captions/transcripts, keyboard navigation, contrast)
- localization/translation support for multi-language course versions

**Optional / advanced** — depends on product and segment:

- AI assistance (draft generation, quiz generation, image generation, text-to-speech, translation, automated review)
- simulation and screencast tooling (screen recording, software simulations, dialogue role-plays)
- enterprise governance (SSO, user roles, groups, course transfer between accounts)
- content protection (passwords, watermarks, domain restrictions, time-limited access)
- open sharing of content for reuse by other educators
- export beyond the LMS package (PDF, video)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Course editor

The primary workspace.

- shows the course structure (sections/pages/slides/screens) and the currently edited page
- primary actions: add/reorder/delete structural units, compose the page from content and interactive elements, apply layout and theme

### Question / assessment editor

Where knowledge checks and formal assessments are built.

- question type selection, answer options, correct-answer marking, per-answer feedback
- scoring rules, attempt limits, time limits, question pools and randomization
- primary actions: create/edit questions, assemble quizzes, configure scoring and feedback

### Asset and template libraries

Built-in stock of reusable material.

- images, characters, icons, audio, video; course and page templates; themes
- primary actions: search, preview, insert into the course, save custom items for reuse

### Preview

A learner-view rendering of the in-progress course.

- typically shows the course exactly as a learner will experience it, often with device-type switching (desktop/tablet/mobile) and sometimes a QR code to open it on a physical phone
- primary actions: navigate the course, verify interactions and scoring

### Review surface

Where stakeholder feedback is collected.

- the course rendered for commenting, with comments pinned to pages/screens, statuses, and notifications
- primary actions: leave/reply/resolve comments, assign tasks, switch between reviewer and author views

### Publish dialog

The handoff surface.

- output format selection (LMS package formats, web/hosted, embed), tracking settings, access options
- primary actions: choose format, configure tracking, generate the package or link, republish updates

### Results view (when tracking is enabled)

Learner performance surfaced back to the author.

- per-learner and per-question results, completion status, export
- primary actions: review results, export, identify content that needs revision

## Important Rules / Behaviors

### The deliverable crosses a system boundary

The published course leaves the author's control and enters a delivery system. Tracking data (progress, scores, completion) flows from the course to the LMS or learning-record store using the packaging standard chosen at publish time. The authoring tool defines *what* is reported; the delivery system decides *who* sees it and *when*.

### Editing a published course is state-sensitive

A published course may already have learners in progress. Products commonly warn that structural changes to a live course — adding, moving, or removing pages, or changing existing questions' answer options — can invalidate or misreport in-flight learner progress. The safe pattern is content-only updates, or republishing structural changes as a new version. (The exact behavior varies by product and delivery route; some delivery mechanisms decouple updates from the package entirely.)

### Assessment rules are author-configured, not fixed

Scoring, passing thresholds, attempt counts, time limits, negative marking, and question randomization are settings the author chooses per assessment. The tool enforces the configuration at runtime; it does not impose a pedagogy.

### Portability depends on the output format

Standards-based packages (SCORM/xAPI family) are portable across conforming LMS platforms. Hosted links and embeds tie the course to the vendor's hosting. Some products offer portable native content files that can be moved between installations of the same (often open-source) tool. The choice of publish target is therefore also a choice about where the content lives.

### Accessibility and localization are authoring responsibilities

Because the tool generates the learner-facing output, accessibility (alt text, captions, keyboard navigation, contrast) and multi-language support are handled at authoring time — either as author-supplied attributes or as tooling (translation export/import, machine translation, text-to-speech narration).

## Variants

Common forms of the Type:

- **Professional slide-based authoring** — deep interactivity engines (triggers, states, variables) on a slide canvas; favored by instructional design teams for custom, highly interactive courses.
- **Block-based web authoring** — courses assembled from pre-designed responsive blocks; fast, template-driven, lower learning curve.
- **PowerPoint-heritage authoring** — the authoring environment lives inside a familiar slide application; existing decks become courses; favored by teams without designers.
- **Cloud-native collaborative authoring** — browser-based, real-time co-authoring, centralized resource libraries, enterprise governance; favored by distributed teams.
- **Open-source embedded authoring** — the tool is a plugin/extension inside a host CMS or LMS; content is authored in the host's admin UI and delivered by the host; common in education.
- **SME-first authoring** — deliberately simplified tools plus AI guidance so subject-matter experts, not learning specialists, produce the content.

A variant remains a variant unless it changes the core model: a tool that stops producing a publishable learner-facing deliverable has become something else (a content platform or delivery system), and one that removes learner interactivity has become a presentation or document tool.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Learning Management System / LMS | downstream consumer | the LMS delivers courses to enrolled learners and tracks completion; the authoring tool produces the course the LMS delivers. Some LMS products include built-in course builders — lightweight builders are capability slices; a full authoring environment inside an LMS is the gradient case. Many authoring tools reciprocally offer lightweight delivery layers — adjacent capability, not the core. |
| Educational Content Platform | adjacent | the platform hosts and curates a library learners consume directly; the authoring tool produces content for delivery elsewhere. Production surfaces inside a content platform fill that platform's own library — they are not standalone authoring tools. |
| Presentation Application | adjacent | presentations are presenter-driven linear slides; e-learning is learner-driven self-paced content with interactivity, assessment, and tracking-oriented export. Authoring tools that build on a slide canvas are distinguished by what is added: questions, interactions, branching, LMS packaging. |
| Survey / Quiz builder | adjacent | quiz builders collect responses from respondents for later analysis; e-learning questions are part of the instructional experience with immediate feedback, scoring, and progression for the learner, embedded in course content. |
| Website builder | adjacent | general web pages vs instructional structure carrying assessment/scoring/tracking semantics and LMS-oriented packaging. |
| Video Editor / Screencast tool | ingredient supplier | video and screen recordings are materials inside courses; the course structure, interactivity, and packaging are the authoring tool's core. Some authoring tools bundle capture tools. |
| Virtual Classroom | different live/synchronous surface | live instructor-led sessions vs self-paced authored content; complementary rather than competing. |

The boundary with the LMS is the most important one, because the two Types interlock: the authoring tool's defining output exists precisely to be consumed by a delivery system. The structural test is the direction of the deliverable — creation produces a portable course; delivery manages learners against it.

## Representative Products

- Articulate 360 (Storyline / Rise)
- iSpring Suite
- Adobe Captivate
- H5P
- Gomo
- Easygenerator

The core model was checked against older desktop-era authoring tools (pre-learning-standard flowline/card/title-based tools) and against the open-source embedded pole to avoid over-fitting the definition to the current cloud/AI implementation.

## Sources

Research date: **2026-09-07**

- Articulate 360 platform — https://www.articulate.com/360/ ; Storyline — https://www.articulate.com/360/storyline/ ; Rise — https://www.articulate.com/360/rise/
- iSpring Suite — https://www.ispringsolutions.com/ispring-suite ; features — https://www.ispringsolutions.com/features
- H5P documentation — https://h5p.org/documentation ; author basics — https://h5p.org/documentation/for-authors/the-basics ; import/export — https://h5p.org/documentation/for-authors/import-and-export ; content types — https://h5p.org/content-types-and-applications
- Gomo — https://www.gomolearning.com/ ; feature list — https://www.gomolearning.com/elearning-authoring-tool/feature-list/
- Easygenerator — https://www.easygenerator.com/en/ ; help center — https://help.easygenerator.com/en/ ; How to Create a Course — https://help.easygenerator.com/en/articles/677415-how-to-create-a-course

> Sourcing limitation: Adobe Captivate's official documentation could not be reached from the research environment (repeated timeouts on two Adobe hosts). Captivate is listed as a market anchor only; no operational claims in this document rest on it. Vendor-quoted counts (question-type counts, asset-library sizes, language counts, LMS-compatibility counts) were observed in product marketing pages and are deliberately not restated as facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
