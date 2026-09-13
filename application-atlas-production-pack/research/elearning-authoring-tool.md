# Research Notes — eLearning Authoring Tool

## Research Goal

Understand what an "eLearning Authoring Tool" actually is as an Application Type: what the central authored object is, how authors compose interactive instruction, what the publishing/output model is, how collaboration and review work, who the users are, and where the boundary lies against neighboring Types (LMS, Educational Content Platform, Presentation Application, quiz/survey builders, website builders, video/screencast tools).

Directory context: leaf "eLearning Authoring Tool", section 23 (Education, Research & Knowledge Institutions). Research date: 2026-09-07.

Prior-pass context: the educational-content-platform pass recorded "vs eLearning Authoring Tool (production surfaces fill the platform's own library, not standalone authoring)" — this pass verifies that seam from the authoring side.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: software for creating interactive self-paced learning content (courses/lessons) that is published as a package or hosted unit for delivery to learners, typically via an LMS or the web.
- Suspected confusions:
  - LMS (delivery/tracking/enrollment vs content creation) — the classic seam.
  - Presentation Application (presenter-driven slides vs learner-driven interactivity).
  - Quiz/survey builders (respondent data collection vs in-content assessment with learner feedback).
  - Educational Content Platform (library of content vs tool that produces content).
  - Website builder (general pages vs instructional structure with scoring/tracking semantics).
- Unknowns: exact internal object structure per product (slides/scenes/blocks/screens), output standards (SCORM/xAPI/AICC/cmi5), review workflow mechanics, template/asset ecosystems, AI-era features.

## Research Questions

1. What is the central authoring object (course/project), and what is its internal structure (slides/scenes/pages/blocks/screens)?
2. What interactive elements can be composed (questions, interactions, branching, variables, simulations)?
3. What is the publishing/output model (SCORM/xAPI/AICC/cmi5, web/HTML5, embed, review links, built-in delivery)?
4. How do templates, themes, and asset libraries work?
5. How do collaboration/review workflows work (comments, co-authoring, roles, task tracking)?
6. Who uses the tool (instructional designers vs SMEs vs educators), and how does positioning differ?
7. Where are the boundaries vs LMS, presentation software, quiz builders, content platforms, website builders?

## Representative Products

| Product | Philosophy / pole | Customer tier | Evidence tier |
|---|---|---|---|
| Articulate 360 (Storyline + Rise) | market leader; slide-based deep interactivity (Storyline) + block-based web authoring (Rise) in one subscription | enterprise L&D | Tier-1 product pages (platform, Storyline, Rise) |
| iSpring Suite | PowerPoint-heritage authoring inside the familiar slide editor; SMB/mid-market | SMB/mid corporate | Tier-1 product + features pages |
| H5P | open-source; authoring embedded in host platforms (WordPress/Drupal/Moodle, LTI to Canvas/Brightspace/Blackboard); education/OER pole | education / public sector | Tier-1 documentation (basics, import/export, content types) |
| Gomo | cloud-native collaborative responsive authoring; enterprise | enterprise | Tier-1 product + full feature list |
| Easygenerator | SME-friendly cloud authoring; "Employee-generated Learning" philosophy | SMB/mid enterprise | Tier-1 product page + help center (How to Create a Course) |

Adobe Captivate was selected as a sixth anchor (legacy slide-based leader) but was unreachable: helpx.adobe.com timed out twice, www.adobe.com timed out once (see Sources). No claims rest on it; it is retained only as a market-structure anchor.

## Sources

- Articulate 360 platform — https://www.articulate.com/360/
- Articulate Storyline — https://www.articulate.com/360/storyline/
- Articulate Rise — https://www.articulate.com/360/rise/
- iSpring Suite — https://www.ispringsolutions.com/ispring-suite ; features — https://www.ispringsolutions.com/features
- H5P documentation — https://h5p.org/documentation ; the basics — https://h5p.org/documentation/for-authors/the-basics ; import/export — https://h5p.org/documentation/for-authors/import-and-export ; content types — https://h5p.org/content-types-and-applications
- Gomo — https://www.gomolearning.com/ ; feature list — https://www.gomolearning.com/elearning-authoring-tool/feature-list/
- Easygenerator — https://www.easygenerator.com/en/ ; help center — https://help.easygenerator.com/en/ ; How to Create a Course — https://help.easygenerator.com/en/articles/677415-how-to-create-a-course
- Adobe Captivate — https://helpx.adobe.com/captivate/get-started.html (timeout ×2), https://www.adobe.com/products/captivate.html (timeout ×1) — **unreachable; market anchor only, no claims**

Source-access limitation: Adobe's official documentation could not be fetched from the research environment (3 timeouts across two hosts). Per the evidence rules, no operational claims are made about Captivate; the historical/market role of slide-based authoring is instead supported by the four reachable products and by Easygenerator's own public comparison framing ("Specialist tools like Articulate 360 give you deep customization options…", Easygenerator FAQ).

## Product A — Articulate 360 (Storyline + Rise)

### Key observations (evidence layer A unless noted)

- **Two authoring engines, one subscription**: Storyline ("build custom interactive content") and Rise ("author beautiful content quickly"), plus Review (stakeholder feedback), Localization (translate/validate), Reach ("share & track with a frictionless LMS"), AI Assistant, Content Library (13+ million images/templates claim — vendor number, L3).
- **Storyline internal model (A)**: slides with **slide layers, triggers, states, and variables**; "learners can click, hover over, or drag any object to trigger any action"; interactive objects (buttons, dials, sliders, markers, hotspots) droppable on slides; variables enable "dynamic, personalized training content".
- **Storyline media/simulation (A)**: screencast recording; "build immersive simulations… record your screen once, then edit recordings whenever and however you want"; video import; background audio; AI text-to-speech.
- **Storyline assessment (A)**: "25 different question types" (vendor number), question import, AI quiz generation; "pool and randomize questions"; negative scoring; combine results from multiple quizzes for a final score; "realistic, branching scenarios".
- **Rise internal model (A)**: "intuitive, block-based authoring… stack and arrange modular media, text, and interactive blocks"; interactive blocks (sorting, labeled graphic, process, timeline, accordion, scenario); assessments/knowledge checks (multiple choice, multiple response, fill-in-the-blank, matching); 1,000+ course templates (vendor number); themes; real-time team co-authoring; shared block templates; team folders with permissions.
- **Collaboration/review (A)**: "gather in-context feedback on your courses from stakeholders. Comments, tasks, and notifications"; cloud project access for teams.
- **Distribution (A)**: "Publish Tin Can API 1.0-, SCORM-, and AICC-compliant content to your learning management system (LMS) or to Reach"; responsive player (video quality adaptation, playback speed, captions/transcripts, touch gestures).
- **Localization (A)**: 80+ languages (vendor number), AI translation, language validators "review and edit in context", RTL support.
- **Accessibility (A)**: "broadly support the Web Content Accessibility Guidelines 2.1 AA criteria"; Section 508; accessible feedback layers, closed captions, accessible navigation.

## Product B — iSpring Suite

### Key observations

- **Authoring substrate (A)**: "works inside PowerPoint"; "with one click, you can seamlessly convert PowerPoint presentations into mobile-ready online courses"; animations/SmartArt/transitions/hyperlinks preserved. Positioning: "Most tools force you into complicated timelines, layers, or coding-like logic. iSpring keeps everything familiar — right inside PowerPoint."
- **AI course generation (A)**: "iSpring Suite AI builds a ready-to-use course – either as a scrollable page or a complete PowerPoint presentation – with a quiz"; "Driven by Bloom's Taxonomy" (vendor framing).
- **Interactions (A)**: "14 interactions tailored to your learning goals… timelines, tabs, FAQs, glossaries" (vendor number).
- **Role-plays (A)**: "branching dialogue simulations bring characters, locations, emotions, voiceovers, and scoring together in a drag-and-drop editor."
- **Assessment (A)**: "14 question templates" (matching, multiple choice, true/false, short answer, numeric, hotspot, drag-and-drop, essay, fill in the blanks, select from lists, drag the words, likert scale, sequence, multiple response); per-question tracking: "time limits, attempt counts, passing scores, and negative marking; custom feedback for every answer"; pop-up explanations inside quizzes; branching logic (wrong answer → extra explanation); "results reported automatically to your LMS via SCORM or xAPI".
- **Media (A)**: screencasts with video narration and timeline editing; flipbooks from documents ("from static document to interactive, trackable flipbook"); AI text-to-speech in 50+ languages (features page says 53 languages for TTS; localization in 70+ languages — vendor numbers).
- **Collaboration (A)**: "real-time collaboration, from creation to review. Microcourses are built entirely in the browser"; comments; shareable link for instant learner access; "custom roles and secure permissions"; on-slide feedback.
- **Publishing (A)**: SCORM, HTML5, AICC, xAPI, cmi5, Moodle formats; "verified across 160+ LMS platforms" (vendor number); player customization (navigation flow, required time on screen, attempt limits); responsive playback with cross-device progress; HTML5 web/intranet publish; MP4 export; content protection (password, time-limited access, watermarks, domain restrictions).
- **Accessibility (A)**: WCAG 2.1 AA and Section 508; "accessible mode with one click — same course, adapted for accessibility"; screen readers, keyboard navigation, high contrast, alt text.
- **Asset library (A)**: large built-in asset library (homepage claims 310,000+ assets, features page claims 130,000+ — inconsistent vendor numbers; treat as "large built-in asset/character library", L3).

## Product C — H5P

### Key observations

- **Authoring substrate (A)**: open-source; "to create H5P content on your own site, you must have the H5P plugin installed and enabled on your site. Plugins that support content authoring currently exist for WordPress, Drupal and Moodle"; LTI integration for Canvas, Brightspace, Blackboard "and many other VLEs". Authoring happens **inside the host platform's admin UI** ("Add content > Interactive content" / "Add an activity or resource > Interactive Content").
- **Content-type model (A)**: authoring is organized around **content types** installed from a Hub — Interactive Video, Course Presentation, Branching Scenario, Question Set (Quiz), Drag and Drop, Fill in the Blanks, Flashcards, Interactive Book ("create courses, books or tests"), Timeline, Virtual Tour (360), and dozens more (50+ listed on the examples page).
- **Editor structure (A)**: "the standard editor lists all fields sequentially"; advanced content types ship dedicated WYSIWYG editors (Course Presentation editor, Interactive Video editor). Content is "completely self-contained"; some content types have parent/child structure (Course Presentation slides containing questions).
- **Portability (A)**: .h5p file download ("Reuse" → "Download") and upload to any H5P-supporting site; copy/paste of questions between content within a site; iframe embed of hosted content.
- **Tracking (A)**: "Interactive Video implements xAPI statements"; scoring requires hosting on a supported platform ("you will need to install one of the 3 supported plugins and host the contents there to be able to retrieve scores"); results analysis documentation; "save content state" (resume) option in plugin settings.
- **Community/sharing (A)**: OER Hub — "lets educators around the world discover, share, and reuse interactive H5P content"; clone-and-edit of example content.
- **Accessibility (A)**: accessibility upgrades tracked per content type; Section 508 questions handled in community; no VPAT maintained by core team (community answer).

## Product D — Gomo

### Key observations

- **Positioning (A)**: "a collaborative, cloud-based, and responsive eLearning authoring tool that makes it easy to create beautiful multi-device learning."
- **Course structure (A)**: courses organized in folders; three-step new-course wizard; screens with flexible 1–4 column layouts ("no fixed/rigid screen templates"); screen layout templates (editable); navigation styles (horizontal/vertical pagination or continuous scroll); course structure visualization.
- **Composition (A)**: drag-and-drop content editor with "a wide range of content interactions, sub-screen reveals, and display conditions"; hotspots/image markers; buttons triggering an action library (show sub-screen, link, branch, set variable); animation; background video; iFrame embed (YouTube, H5P content); flip cards.
- **Logic (A)**: variables + display conditions ("tailor the content shown on screen or even the screen itself, based on one or more conditions"); branching scenarios ("use a combination of display conditions and variables to track user decisions (e.g. role filter)").
- **Assessment (A)**: question banks ("build up your bank of questions on a topic and then choose how many questions you want to include"); two randomization types (answer order + bank selection); feedback and multiple attempts; "Gomo will automatically calculate the score… Whether you publish your course as SCORM 1.2, 2004, or xAPI, Gomo will send the assessment result back to your LMS or LRS."
- **Collaboration (A)**: reviewer access per course capturing "feedback per screen in your course as tasks assigned to your production team"; task management; real-time co-authoring; "topic locked indicators/overwrite protection"; user roles; SSO; team management.
- **Resources (A)**: centralized resource library reused across courses; "content in use indicators" preventing accidental deletion; "update once, apply everywhere" resource replacement.
- **Localization (A)**: single- or multi-language courses; learner language selectors; XLIFF export/import; AI translation; 250+ languages (vendor number).
- **Publishing/delivery (A)**: publish wizard; zip download for LMS upload; SCORM 1.2, SCORM 2004 (3rd/4th ed.), xAPI (defined/undefined LRS endpoints); Google Analytics option; **Gomo Delivery** — tiny "LMS wrapper" package uploaded to LMS(s) with instant updates from the authoring tool; direct-access links (anonymous or registration form); HTML embed code for portals/intranets; "last publish" archive.
- **Accessibility (A)**: keyboard-accessible navigation; screen-reader friendly HTML output (tested with JAWS); alt text; transcripts; VTT closed captions; public VPAT/conformance report.
- **AI (A)**: AI text generation (introductions, conclusions, learning objectives); "automated course review"; AI translation.

## Product E — Easygenerator

### Key observations

- **Positioning (A)**: "an authoring tool anyone can use"; Employee-generated Learning (EGL) — "an organization's own subject-matter experts create training content directly, instead of routing everything through a central L&D or instructional design team." FAQ defines the Type itself: "An e-learning authoring tool is software you use to create digital training content such as courses, quizzes, interactions, and assessments, which you then publish to a learning platform for delivery. An authoring tool is where the content gets built, while a Learning Management System (LMS) hosts and tracks it."
- **Course creation flow (A, help center)**: four steps — (1) course introduction page: sections + content pages + questions added via "Add Item"; content pages composed by dragging **content blocks**; sections optional (microlearning uses flat pages); (2) settings: design, results tracking, scoring, certificates, learner survey, number of attempts, timer, question pool, language; (3) publish: Easygenerator-hosted private link, website embed, LMS, own hosting, PDF export; "when the course is published you can update it anytime"; explicit warning that structural changes to a published course being completed by learners "may lose or incorrectly report progress"; (4) learner results: Gradebook per section/question, results export.
- **Starting points (A)**: from scratch (drag-and-drop), ready-to-use templates (microlearning modules), Course Builder (3-step guided structure, AI or manual), SCORM import (Articulate Rise packages; enterprise, on demand).
- **AI (A)**: EasyAI agent — "build, edit, and refine courses through conversation"; turns documents/decks into first drafts; included in all plans (vendor claim). EasyVideo (AI video from decks), EasyCoach (voice/text conversational practice), EasyTranslate (75 languages, vendor number).
- **Publishing (A)**: "export your courses as SCORM or xAPI files that work in virtually any LMS or LXP"; **dynamic SCORM** — "update a published course without re-exporting and re-uploading the SCORM file"; "one SCORM file can hold all language versions".
- **Collaboration (A)**: help-center Collaboration collection (10 articles); enterprise groups with course access management and Group Admins.
- **Adjacent owned LMS (A)**: "Easygenerator LMS" help collection — a lightweight delivery/tracking layer alongside the authoring tool.

## Cross-product Comparison

| Dimension | Articulate (Storyline/Rise) | iSpring Suite | H5P | Gomo | Easygenerator |
|---|---|---|---|---|---|
| Central authored object | course (Storyline project / Rise course) | course (PowerPoint presentation + quiz/interactions) | self-contained H5P content (content-type instance) | course (screens/topics) | course (sections + pages + questions) |
| Composition unit | slides+layers (Storyline) / blocks (Rise) | PowerPoint slides + interaction/quiz objects | content-type-specific fields or WYSIWYG slides | screens with columns/blocks | pages with content blocks |
| Learner interactivity | triggers/states/variables; interactive objects; branching scenarios | 14 interactions; role-plays; branching quizzes | 50+ content types (questions, interactive video, branching scenario) | interactions, hotspots, sub-screens, actions | content blocks + question pages |
| Assessment machinery | 25 question types (vendor n.), pools, randomization, negative scoring | 14 question templates, attempts/time limits/negative marking, pop-up feedback | question types + question sets; xAPI scoring | question banks, randomization, attempts, scoring to LMS/LRS | question pool, attempts, timer, scoring, certificates |
| Conditional logic | variables + triggers + states | branching in quizzes/role-plays | branching scenario content type | variables + display conditions + actions | (not directly observed in fetched pages) |
| Templates/themes | 1,000+ templates (Rise, vendor n.); themes; Content Library | Content Library templates; characters | clone examples; content-type Hub | theme library + custom themes; screen layout templates | course templates; look & feel settings |
| Collaboration/review | Review (in-context comments/tasks); real-time Rise co-authoring; team slides | real-time browser co-authoring; comments; roles | (single-author model observed; community reuse instead) | reviewer comments→tasks; real-time co-authoring; topic locking; roles; SSO | collaboration collection; enterprise groups |
| Publishing targets | SCORM/xAPI(Tin Can)/AICC to LMS; Reach (built-in LMS) | SCORM/HTML5/AICC/xAPI/cmi5/Moodle; web; MP4 | .h5p file; iframe embed; LTI to VLEs; xAPI when hosted | SCORM 1.2/2004/xAPI zip; Gomo Delivery (wrapper/direct link/embed) | SCORM/xAPI; hosted link; website embed; own hosting; PDF |
| Built-in delivery layer | Reach | iSpring LMS (sibling product) | host platform is the delivery layer | Gomo Delivery | Easygenerator LMS |
| Responsive/multi-device | responsive player; Rise auto-adapts | mobile-ready; cross-device progress | host-dependent; HTML5 | responsive/adaptive as standard | (web-based; device claims on marketing page) |
| Accessibility | WCAG 2.1 AA posture; Section 508 | WCAG 2.1 AA; Section 508; accessible mode | per-content-type upgrades; community-driven | keyboard nav; JAWS-tested; VPAT published | Accessibility & Compliance collection |
| Localization | 80+ languages (vendor n.); validators; RTL | 70+ languages; AI TTS 50+ | multilingual content docs | 250+ languages (vendor n.); XLIFF; AI translation | 75 languages (vendor n.); one-SCORM-all-languages |
| AI assistance | AI Assistant (drafts, quizzes, images, writing tools); Nova agent | AI course builder; AI TTS; AI images | not observed in fetched docs | AI text generation; AI review; AI translation | EasyAI agent; EasyVideo; EasyCoach |
| Authoring substrate | desktop (Storyline) + web (Rise) | PowerPoint add-in (desktop) + browser microcourses | embedded in host CMS/LMS (open source) | cloud web | cloud web |
| Business model | subscription suite | perpetual/subscription suite | open source + hosted SaaS (H5P.com) | enterprise subscription | subscription (freemium trial) |

## Canonical Abstraction

### L0 — Defining Invariant

Three structures. Remove any one and the product stops being an eLearning Authoring Tool:

1. **The authored course project** — a persistent, self-contained unit of instruction (course/module/lesson) that the author creates, names, edits, and revisits over time. Without it, the software is a one-off content generator, not an authoring tool.
2. **Learner-facing interactivity composed into the content** — the author assembles instructional content together with elements the *learner* will operate: questions with feedback/scoring, interactive objects, navigation/branching. Without it, the software is a presentation or document tool (presenter-driven, not learner-driven).
3. **A publishable learner-facing deliverable** — the project is exported/published as a self-contained package or hosted unit intended for delivery to learners outside the authoring environment (LMS package, web page, embed, hosted link). Without it, the software is a content platform or an LMS, not an authoring tool.

Note what is deliberately NOT in L0: SCORM (H5P publishes .h5p/embed/LTI without SCORM; pre-SCORM-era tools were still authoring tools), cloud delivery (desktop-era tools qualify), AI, templates, collaboration, question-type counts, responsive design.

### L1 — Common Mature Structure

Present across the sampled products (evidence layer B):

- page/slide/block/screen composition surfaces with drag-and-drop or structured editors
- question/quiz machinery: multiple question types, scoring, per-answer feedback, attempts, question pools/randomization
- conditional/branching logic (variables, display conditions, branching scenarios) — present in 4/5 sampled with direct evidence; Easygenerator's conditional depth not directly observed
- templates, themes, and built-in asset/character libraries
- review & collaboration: in-context comments, stakeholder review links, co-authoring, roles (H5P's open-source model is the outlier: community reuse instead of in-tool review)
- standards-based export (SCORM 1.2/2004, xAPI/Tin Can, AICC; cmi5 at two products) plus web/HTML5 publish
- responsive multi-device output and preview (device preview, QR preview)
- accessibility support (WCAG/Section 508 posture, alt text, captions/transcripts, keyboard navigation)
- localization/translation support (multi-language courses, AI or XLIFF translation)
- results visibility when tracking is enabled (gradebook/results export at two products; LRS/LMS at others)

### L2 — Variant / Optional Structure

- authoring substrate: desktop application vs PowerPoint add-in vs cloud web app vs open-source embedded in a host CMS/LMS
- packaging: standalone tool vs multi-product suite vs platform-embedded capability
- built-in delivery layer (vendor-operated lightweight LMS/delivery: Reach-class, wrapper-class, hosted-link-class) — an adjacent capability, not the Type
- AI assistance depth (draft generation, quiz generation, image generation, TTS, translation, AI review, conversational agents)
- simulation/screencast/video tooling (screen recording, role-play dialogue editors, video-from-deck)
- enterprise governance (SSO, user roles, groups, course transfer between accounts, content protection: passwords/watermarks/domain restrictions)
- OER/community sharing (public hub for discover/reuse)
- export breadth beyond the LMS package (PDF, MP4, Google Analytics)
- audience positioning (professional instructional designers vs SME/employee authors vs educators)

### L3 — Vendor-specific Structure

(kept out of the final document; listed for traceability)

- Storyline's slide layers / triggers / states / variables model; Rise's block library and shared block templates; Reach; Nova agent
- iSpring's PowerPoint-embedded authoring; role-play dialogue editor; flipbook conversion; player "required time on screen"; 160+ LMS verification claim; asset-count claims (130k vs 310k inconsistency)
- H5P's content-type Hub, .h5p package format, host-plugin model (WordPress/Drupal/Moodle), LTI integrations, OER Hub, clone-and-edit culture
- Gomo's LMS wrapper + instant updates, XLIFF round-trip, topic locking, "update once apply everywhere" resource library, course transfer
- Easygenerator's dynamic SCORM, one-SCORM-all-languages, Course Builder, EGL philosophy, EasyCoach
- All vendor numbers: 25/14 question types, 13M+/130k+/310k+ assets, 80+/70+/75/250+ languages, 1,000+ templates, 160+ LMS platforms

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- **Pre-SCORM era (1990s–early 2000s)**: flowline/icon-based authoring (Authorware-class), card/book-based authoring (ToolBook-class), title-based web authoring (Lectora-class), and screen-capture-based authoring (early Captivate/RoboDemo-class) all satisfy the L0: a persistent authored course project, learner-facing interactivity, and a publishable deliverable (CD-ROM/web/exe; LMS packaging arrived with SCORM). None of them require SCORM, cloud, AI, or template marketplaces.
- **PowerPoint-heritage tools** (Articulate Presenter era, iSpring): satisfy the L0 with the slide deck as the project substrate.
- **Open-source embedded tools** (H5P): satisfy the L0 with the content-type instance as the project and the host platform as the delivery surface — confirming that neither SCORM nor a standalone app is definitional.
- **LMS-native course builders**: a lightweight page builder inside an LMS is a capability slice; the L0's "publishable deliverable for delivery outside the authoring environment" is what separates the Types — but the boundary is a gradient where an LMS ships a full authoring environment (recorded in Boundary Findings).

Conclusion: the L0 survives the historical check; everything modern (SCORM specifics, cloud, AI, responsive, accessibility machinery, localization suites) is L1/L2.

## Vendor-specific Findings

See L3 above. Additionally:

- Easygenerator's own FAQ is the clearest vendor-articulated statement of the authoring-tool/LMS seam ("An authoring tool is where the content gets built, while an LMS hosts and tracks it") — used as a market-structure signal, not as a definition source.
- iSpring markets an "On-premise authoring tool" use case (air-gapped/regulated deployments) — deployment variant.
- Gomo and Easygenerator both sell a companion delivery/LMS layer; Articulate ships Reach; iSpring has a sibling LMS product. The authoring tool + lightweight delivery bundle is a market pattern, not a definitional structure.

## Boundary Findings

1. **vs Learning Management System (LMS)** — the load-bearing seam. The authoring tool's defining output is a **portable content deliverable consumed by a delivery system**; the LMS's defining objects are learners, enrollments, and tracked completion. Evidence: every sampled product publishes SCORM/xAPI packages "to your LMS"; Easygenerator's FAQ states the split explicitly; Articulate ships Reach and iSpring/Gomo/Easygenerator ship lightweight delivery layers as *adjacent* products/capabilities. Reverse direction: LMS-native course builders are capability slices, not this Type — unless the LMS bundles a full authoring environment (gradient; flag for the LMS pass). Removal test: remove the publishable deliverable → content platform/LMS; remove learner/enrollment management → authoring tool remains.
2. **vs Presentation Application** — the discriminator is **who drives**: presentations are presenter-driven linear slides; e-learning is learner-driven self-paced content with interactivity, assessment, and tracking-oriented export. iSpring literally authors inside PowerPoint — the seam is what the author adds (questions, interactions, branching, LMS packaging), not the slide canvas itself. Removal test: remove learner interactivity + publishable course deliverable → presentation tool.
3. **vs Survey/Quiz builder** — quiz builders collect responses from respondents for later analysis; e-learning questions are part of the instructional experience with immediate feedback, scoring, and progression for the learner, embedded in content. Overlap: standalone quiz-maker siblings exist (iSpring Quiz Maker as a separate product). Removal test: remove the instructional content around the questions → quiz builder.
4. **vs Educational Content Platform** — the platform hosts/curates a library learners consume directly; the authoring tool produces content for delivery elsewhere. Consistent with the educational-content-platform pass ("production surfaces fill the platform's own library, not standalone authoring"). Removal test: remove the authored-project + publishable-deliverable loop → content platform.
5. **vs Website builder** — general web pages vs instructional structure carrying assessment/scoring/tracking semantics and LMS-oriented packaging. Removal test: remove instructional semantics → website builder.
6. **vs Video editor / screencast tools** — video/screencasts are ingredients inside the course; the course structure + interactivity + packaging is the core. Some authoring tools bundle capture tools (iSpring Cam-class, Storyline screencasts) — adjacent capability.
7. **"去掉什么就变成另一个 Type" tests** — remove the persistent project → one-off generator; remove learner interactivity → presentation/document tool; remove the publishable deliverable → content platform/LMS; remove instructional purpose entirely → generic interactive-content builder (H5P's own tagline "rich HTML5 content" shows this edge — the market keeps it inside the e-learning family via its LMS/VLE integrations and education audience).

## Uncertainties

- **Easygenerator conditional-logic depth**: branching/variables not directly observed in fetched pages (help-center "Questions and pages"/"Course Settings" collections not fetched article-by-article). Treated as unverified; the L1 claim "conditional logic" rests on 4/5 products with direct evidence.
- **H5P collaboration**: no in-tool review/co-authoring observed; the open-source model centers on community reuse. Whether hosted H5P.com offers team review was not verified.
- **Adobe Captivate**: unreachable; its current feature set (e.g., VR/interactive-video emphasis) is intentionally not asserted.
- **Question-type counts** (25/14) are vendor numbers; the canonical claim is "a library of question types", not a count.
- **Asset-library sizes and language counts** are vendor marketing numbers; recorded as L3 only.
- **LMS-native authoring gradient**: how many LMS products ship full authoring environments vs lightweight builders was not researched (LMS leaf unprocessed at time of pass); flagged for the LMS pass.

## Final Synthesis

An eLearning Authoring Tool is an authoring application whose defining core is small: a persistent authored course project, learner-facing interactivity composed into that project (questions with feedback/scoring, interactive objects, branching), and a publishable learner-facing deliverable handed to a delivery system (LMS package, web page, embed, hosted link). Around that core, mature products add page/slide/block composition surfaces, question/quiz machinery with pools and randomization, conditional/branching logic, templates/themes/asset libraries, review and collaboration, standards-based export (SCORM/xAPI/AICC/cmi5) plus web publishing, responsive output, accessibility support, and localization. The market implements the Type along several poles — professional slide-based deep interactivity, PowerPoint-heritage simplicity, block-based web authoring, cloud-native collaborative enterprise, open-source embedded education — increasingly with AI assistance layered on top. The Type is bounded from the LMS (delivery/tracking vs creation), from presentation software (presenter-driven vs learner-driven), from quiz builders (response collection vs in-content assessment), from educational content platforms (library vs production), and from website builders (general pages vs instructional semantics).
