# Research Notes — AI Tutoring Application

Research date: 2026-09-06
Leaf: AI Tutoring Application (DIRECTORY §23 Education, Research & Knowledge Institutions)
Slug: ai-tutoring-application

---

## Research Goal

Understand what an AI Tutoring Application actually is as a class of software: what the software itself does (vs. what humans do), what objects exist inside it, how the tutoring interaction works, how learner progress is represented and used, and where the Type's boundaries lie against neighboring education Types (Tutoring Platform, LMS, MOOC Platform, Educational Content Platform, Test Preparation Platform, Language Learning Application) and against homework-helper / general-AI-assistant products.

## Initial Boundary (hypothesis before research)

- Working hypothesis: an AI Tutoring Application is software that **itself performs the tutoring role** — it teaches a subject to a learner through interactive instruction — rather than brokering human tutors (Tutoring Platform) or merely delivering content (content platforms / LMS).
- Suspected confusions:
  1. Tutoring Platform (human tutors, marketplace mechanics) — different executor of pedagogy.
  2. LMS — institutional course management; pedagogy executed by human teachers.
  3. Homework-helper apps (answer/explanation on demand) — no learning-progress responsibility.
  4. General AI chat assistants used as tutors — no curriculum structure or persistent learner state.
- Key unknowns:
  1. Does "AI" require LLM conversation? (Historical check needed: pre-LLM adaptive products.)
  2. Is a persistent learner-progress/mastery model part of the defining core, or only common?
  3. Is diagnosis/placement part of the core?
  4. Is human involvement (teachers/parents) excluded by definition?

## Research Questions

1. What pedagogical acts does the software itself execute (pose problems, evaluate answers, hint, explain, select next)?
2. How is the subject structured inside the product (courses, skills, knowledge points, topics)?
3. How is the learner represented (mastery state, knowledge state, progress), and how does that state drive what comes next?
4. What is the core interaction loop, step by step?
5. Which AI mechanisms are used (LLM dialogue, cognitive-model adaptive engine, knowledge-point system, knowledge-space model) — and which of these is defining vs. implementation?
6. What feedback / hint / scaffold machinery exists?
7. Who are the customers (consumer, school, learning center), and what do teachers/parents see and do?
8. Where are the boundaries with LMS / MOOC / content platforms / tutoring marketplaces / homework helpers?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, different customer layers, and different eras of "AI tutoring" technology:

| Product | Vendor | Philosophy / mechanism | Customer layer | Era |
|---|---|---|---|---|
| Khanmigo | Khan Academy (nonprofit) | LLM conversational tutor, Socratic policy, layered on a free content library | Consumer (parents) + school districts | LLM era (2023–) |
| MATHia | Carnegie Learning | Cognitive-science adaptive engine, skill-by-skill, blended with classroom | Schools (supplemental, grades 6–12) | Pre-LLM lineage (long-running adaptive product line; exact founding decade not verified from fetched pages) |
| Squirrel AI | Squirrel Ai Learning | Knowledge-point (nano-level) adaptive system + physical learning centers with human teachers | Consumer via franchise learning centers (China origin; US expansion) | Pre-LLM core + LLM-era model layer (LAM, 2024; founding year not stated on fetched pages) |
| ALEKS | McGraw Hill | Knowledge Space Theory assessment/learning system | K-12 + Higher Ed + independent use | Pre-LLM (vendor states 26 years of accumulated interaction data) — historical check |

Boundary-case products discussed but not used as primary sample: Duolingo (Language Learning Application), Photomath / Socratic by Google (homework helpers), ChatGPT (general assistant used as tutor).

## Sources

All fetched 2026-09-06 via WebFetch. Evidence layers: A = directly observed on an official source for a specific product; B = cross-product commonality; C = canonical inference.

Khanmigo (Khan Academy):
- https://www.khanmigo.ai/ (product page + FAQ) — A
- https://www.khanmigo.ai/learners (learner-facing product page + FAQ) — A
- https://support.khanacademy.org/hc/en-us (help center root) — A
- https://support.khanacademy.org/hc/en-us/search?query=Khanmigo%20student (help center search results: Khanmigo Activities, teacher reports, chat-history viewing, conversation flagging, focus mode) — A (titles/snippets only; full articles not fetched)

MATHia (Carnegie Learning):
- https://www.carnegielearning.com/ (root; solution family structure) — A
- https://www.carnegielearning.com/solutions/math/mathia (product page) — A
- https://support.carnegielearning.com/help-center/ (help center root) — A
- https://support.carnegielearning.com/help-center/math/home-connection/mathia-support22/mathia-for-students/article/getting-started-mathia-students/ (student help article) — A

Squirrel AI:
- https://squirrelai.com/ (product page + platform/technology/FAQ sections) — A
- Note: US site is franchise/recruitment-oriented; detailed end-user operational documentation (tablet software manual) not reachable. Assertions about in-lesson mechanics are kept at marketing-description strength.

ALEKS (McGraw Hill):
- https://www.aleks.com/about_aleks (about page) — A
- https://www.aleks.com/about_aleks/HowALEKSWorks_TextDescription (official video transcript describing the working model) — A

Not fetched (avoided per network-limitation rule): Duolingo, Photomath, Socratic — used only as boundary references at low assertion strength.

---

## Product Observations

### Product A — Khanmigo (Khan Academy)

Key observations (Evidence A unless noted):

- Positioned as "AI-powered personal tutor and teaching assistant"; learner side is "always-available tutor on just about every topic".
- Explicit anti-answer pedagogical policy: "doesn't just give answers... guides learners to find the answer themselves"; "never gives you the answer. It's built to help you learn." Repeated across home, learners, and parents pages.
- Anchored to a structured content library: "personalized tutoring on every exercise, video, and article on Khan Academy"; subjects listed as math, science, coding, history, humanities; "elementary school through college".
- Tutoring surface is a chat; also writing coach (real-time feedback, debate, collaboration), code review (JS, HTML, Python, SQL), career/college coaching.
- Speech-to-text and text-to-speech ("You talk, Khanmigo types... will read out its responses").
- Chat history accessible to the user.
- Gamification tied to the host platform: energy points earned by watching videos / completing practice; cosmetic "hats" for Khanmigo.
- Access model: consumer access via parent subscription (parent enables access for children under 18; up to 10 children per parent account; US-only billing for consumers); teachers get free access in many countries; classroom/student access only through school or district implementations.
- Teacher side (from FAQ + help center search results): lesson planning, rubrics, exit tickets, on-demand summaries of recent student work; "Khanmigo Activities" assignable to students; reports on Khanmigo use; teachers can view student Khanmigo chat history (district feature); "focus mode" to disable Khanmigo; conversation flagging with notification alerts to parents/schools.
- Under-18 access is gated by parents or district partnership — a deliberate safety/supervision posture.

### Product B — MATHia (Carnegie Learning)

Key observations (Evidence A):

- Positioned as "The 1-to-1 math coach"; "intelligent math software"; supplemental instruction for grades 6–12 within Carnegie Learning's math solutions (blended with classroom instruction).
- "MATHia adjusts to every action they take in the software"; "uses sophisticated AI technology to adapt at a very detailed, skill-by-skill level"; "personalized just-in-time feedback and contextual hints".
- Student-facing structure (help center, student article):
  - Content organized into **workspaces**; a workspace contains problems of one kind.
  - Learning supports inside workspaces: **Step-by-Step** examples (student completes a problem guided), **Worked Examples** (read then answer), **Animations** (concept explainer, rewatchable), **Explore Tools** (interactive models).
  - **Hints**: "Hints usually have 3 three levels... you can go to the next level by selecting the Next button."
  - **Just-in-Time hints**: "A message related to a mistake you made... your answer was close but not quite correct. Or, the mistake... is a very common mistake."
  - **Answer History**: all previously tried answers on a question are inspectable.
  - Glossary; Expression Editor for entering math (fractions, calculations); decimal-accuracy conventions.
- **Progress Meter**: "Students see their progress toward multiple skills" — mastery is tracked per skill and shown to the student.
- Educator side: Session, Skills, Student Detail, and Standards Reports; **APLSE Report** ("accurately predicts how far students will progress by the end of the year"); Leadership Report for administrators.
- **LiveLab**: "live facilitation tool" for teachers — in-the-moment data (students working/idle), real-time alerts when students need extra support, milestone notifications.
- Research grounding: "Rooted in research from Carnegie Mellon University"; "cognitive and learning science" (vendor page does not detail the cognitive model internals — do not overclaim).

### Product C — Squirrel AI

Key observations (Evidence A for marketing-level descriptions; in-lesson mechanics not directly observed):

- Positioned as an "Intelligent Adaptive Learning System (IALS)" + physical learning centers ("3,000+ worldwide self-study centers", franchise model).
- Subject structure: IALS "can break down knowledge points at the nano-level, refining hundreds of original knowledge points into tens of thousands of smaller and more precise ones"; targets "what they don't understand" and skips "knowledge points they've already mastered".
- Entry: "personalized roadmap designed by our IALS, based on detailed insights from their initial diagnostic test".
- Closed loop on a smart-learning tablet: "integrating assessment, practice, learning, testing, and teaching phases seamlessly within a single device".
- Platform sections: Accessing (tablet at home or in centers), Learning (tailored paths), Practicing ("targeted, interactive exercises... Real-time feedback"), Testing ("Track mastery with ongoing assessments that adapt to your child's progress, ensuring readiness before moving to new challenges"), Tutoring ("Combining expert guidance and AI-driven tools").
- Hybrid human+AI: "While AI customizes the learning path, the teaching comes from mini lessons by award-winning educators" (in centers); FAQ: system "available 24/7... explain concepts in virtually unlimited ways until the student fully understands".
- Parent side: "24/7 Parent Access... round-the-clock access to detailed learning analytics".
- Technology branding: LAM ("Large Adaptive Model", launched Jan 2024), MCM (Mode of Thinking, Capacity, Methodology). Numbers (43M users, 20B learning behaviors, 10k nano objectives) are vendor marketing claims — not independently verified; keep out of canonical claims.
- Subjects: math, science, reading, English; in the US currently PreK-5 math (per FAQ).

### Product D — ALEKS (McGraw Hill)

Key observations (Evidence A; the official "How ALEKS Works" transcript is unusually explicit):

- Positioned as "an artificially intelligent learning and assessment system" for Math, Chemistry, Statistics, Accounting; markets: K-12, Higher Ed, Independent Use.
- Core concept: **knowledge state** — "everything he already knows in Algebra 1"; course consists of "several hundreds of topics"; feasible knowledge states organized into a **learning space** (Knowledge Space Theory), which "specif[ies]... which topics a student is ready to work on".
- **Initial individualized assessment**: "ALEKS intelligently chooses each question based on the student's responses to all previous questions to determine what the student has mastered, not mastered, and exactly what topics he is ready to learn."
- Learner-facing progress surface: "multicolored pie chart" divided into subject branches; shaded = mastered; "a box... with the topics" available; students pick from "Ready to Learn" topics.
- Continuous loop: "ALEKS continually updates Sam's knowledge state and ready to learn possibilities. ALEKS constantly watches Sam and records his successes and failures, and this information is used to guide Sam along one of his optimal learning paths."
- "Because of this constant evaluation, ALEKS only presents topics that the student is actually ready to learn" — the anti-framing claim (not too easy, not too hard).
- **Periodic re-assessment** ("Knowledge Checks") to confirm retention; "a cycle of individualized assessment and adaptive learning continues throughout the course".
- Input posture: "ALEKS Avoids Multiple Choice" — "authentic problems" with subject-specific input tools (e.g., graphing tools).
- Educator/parent side: "real-time, detailed reports"; **ALEKS Insights** alerts educators to at-risk students: (a) not succeeding, (b) ceased succeeding, (c) excessively procrastinating, (d) learning "unusually" fast.
- Vendor success-rate claims (≥90%, often >95% mastery of offered topics) are marketing statistics — not used as canonical claims.

---

## Cross-product Comparison

| Dimension | Khanmigo | MATHia | Squirrel AI | ALEKS |
|---|---|---|---|---|
| AI mechanism | LLM conversational tutor | adaptive engine, skill-by-skill ("adjusts to every action") | knowledge-point adaptive system (+ recent "LAM") | Knowledge Space Theory assessment/learning |
| Subject structure | Khan Academy content library (courses → units → exercises/videos/articles) | workspaces → skills within course modules | nano-level knowledge points (10k+ claimed) | course topics in a knowledge space |
| Learner state | host-platform mastery + chat history | per-skill mastery (Progress Meter) | knowledge-point mastery map | knowledge state (pie chart) |
| Primary interaction | free-form chat + on-content tutoring | structured problem solving in workspaces | tablet lessons + practice + tests | open-response problems (no multiple choice) |
| Feedback machinery | Socratic dialogue, no direct answers | 3-level hints, just-in-time hints, answer history | real-time feedback; "explain... in virtually unlimited ways" | correctness evaluation; ready-to-learn selection |
| Adaptation trigger | conversation context + content being studied | every student action, skill-level | diagnostic test + ongoing assessments | assessment + constant success/failure recording |
| Diagnosis/placement | not observed | implicit in workspace flow | initial diagnostic test | initial assessment + periodic Knowledge Checks |
| Progress surface for learner | energy points, host mastery system | Progress Meter | tablet progress screens | pie chart |
| Adult-facing surface | parent account; district reports; chat-history viewing; flagging alerts | teacher reports (Session/Skills/Standards/APLSE); LiveLab live alerts | parent analytics 24/7 | reports; Insights at-risk alerts |
| Human role | none required; parent/teacher supervise | teacher runs blended classroom; LiveLab | human teachers deliver mini-lessons in centers | teacher/parent monitor; institution assigns |
| Customer channel | consumer subscription + districts | schools (supplemental) | franchise learning centers + home tablets | K-12 + higher ed + independent |
| Guardrails | conversation flagging, focus mode, parent gating, under-18 gating | LiveLab alerts | parent access | Insights alerts; LockDown Browser support listed |

### What is shared by all four (candidate core, Evidence B)

1. An identified learner pursuing a subject/skill, with a persistent record in the product.
2. The subject is structured into learnable units (topics / skills / knowledge points / content-anchored exercises).
3. The software itself poses questions/problems and evaluates the learner's responses.
4. The software produces instructional responses — feedback, hints, explanations — not just right/wrong verdicts.
5. What the learner works on next is conditioned on the learner's observed performance (in-the-moment and/or via a persistent mastery state).
6. Progress is made visible to the learner (pie, progress meter, points).
7. An adult-facing monitoring surface exists (reports, alerts, analytics) in every product, though its depth varies.

### What varies (candidate variant space)

- AI mechanism (LLM vs. adaptive engine vs. knowledge-space model) — implementation layer.
- Interaction form (free chat vs. structured problem-solving vs. tablet lesson flow).
- Customer channel (consumer / school / franchise center).
- Human-in-the-loop posture (none required / teacher-supervised blended / human mini-lessons hybrid).
- Diagnosis (explicit placement test vs. implicit continuous assessment vs. none observed).
- Subject breadth (multi-subject vs. math-only vs. language).
- Deployment surface (web, mobile, dedicated tablet hardware).

---

## Abstraction Hierarchy

### L0 — Defining Invariant

An AI Tutoring Application is a learning application in which **the software itself performs the tutoring role**:

1. **Identified learner with a learning objective in a subject/skill domain** — the application serves a specific person learning something, with a persistent record.
2. **Subject structured into learnable units** — the domain is organized (topics, skills, knowledge points, or content-anchored exercises) so instruction can be targeted.
3. **Software-executed instructional interaction** — the system poses questions/problems/prompts, evaluates the learner's responses, and produces instructional responses (feedback, hints, explanations, next steps). No human executes these pedagogical acts.
4. **Performance-conditioned instruction** — what the system presents or says next is conditioned on the learner's observed performance, in the moment and/or through a persistent learner-progress state.

Removal tests:
- Remove (3) → content platform / eLearning course / human-tutor marketplace (pedagogy executed elsewhere).
- Remove (4) → static interactive course or homework helper (no instructional responsibility for progress).
- Remove (2) → general AI chat assistant (no subject structure to teach against).
- Remove (1) → anonymous quiz/practice tool (no persistent learner to be responsible for).

### L1 — Common Mature Structure

Present in most/all sampled products, not required for recognition:

- Hint/scaffold machinery (3-level hints, Socratic questioning, unlimited re-explanations).
- Mastery/progress tracking with a learner-visible progress surface (pie chart, progress meter, points).
- Practice/exercise engine with instant evaluation.
- Learning supports: worked examples, step-by-step demonstrations, explainer content.
- Adult-facing monitoring: reports, dashboards, alerts (at-risk / idle / flagged-conversation).
- Curriculum/standards alignment (grade levels, standards reports).
- Diagnosis/placement (explicit initial assessment in some; implicit continuous assessment in others; not observed in the LLM-chat pole).

### L2 — Variant / Optional Structure

- AI mechanism: LLM conversational tutor vs. adaptive exercise engine vs. knowledge-space/knowledge-point model.
- Interaction form: free-form chat vs. structured problem-solving workspace vs. tablet lesson flow.
- Customer channel: consumer subscription, school/district license, franchise learning center.
- Human-in-the-loop posture: unsupervised consumer use, teacher-supervised blended classroom, human mini-lesson hybrid.
- Subject breadth: multi-subject vs. single-domain (math) vs. language-domain siblings.
- Deployment: web, mobile, dedicated tablet hardware.
- Guardrail posture: conversation flagging, focus/disable modes, parent gating, lockdown/proctoring adjacency.
- Purpose overlays: test-prep alignment, course-credit embedding (product used as a graded course component).

### L3 — Vendor-specific (research notes only)

- Khanmigo: GPT-4 under the hood; $4/month consumer pricing; up to 10 children per parent account; US-only consumer billing; energy points + cosmetic hats; "Khanmigo Activities"; Writing Coach; focus mode; Common Sense Media 4-star rating (marketing).
- MATHia: LiveLab; APLSE Report; Progress Meter; Answer History; Expression Editor; decimal-accuracy conventions; RAND study marketing; Carnegie Mellon lineage.
- Squirrel AI: IALS / LAM / MCM branded systems; nano-level knowledge points ("tens of thousands"); smart-learning tablet hardware; franchise learning centers; 43M users / 20B behaviors / 51.3-pt score gain (unverified marketing numbers).
- ALEKS: Knowledge Space Theory; pie chart; Knowledge Checks; ALEKS Insights (US Patent No. 10,713,965); LockDown Browser support; ≥90%/95% success-rate claims; 26 years / 50M students (marketing).

## Rejected Findings

- **"AI Tutoring requires LLM conversation"** — rejected. ALEKS and MATHia are pre-LLM products that clearly instantiate the Type; the AI mechanism is an implementation layer, not the invariant.
- **"AI Tutoring requires an explicit placement/diagnostic test"** — rejected as core. Khanmigo shows no placement flow; ALEKS/Squirrel do. Diagnosis is common, not defining.
- **"AI Tutoring excludes humans"** — rejected. Squirrel AI is explicitly hybrid (human mini-lessons + AI paths); MATHia is blended with classroom teaching. The invariant is that the *software executes the pedagogy*, not that no humans participate.
- **"AI Tutoring = gamified app"** — rejected. ALEKS has no points/streaks; its pie chart is a progress surface, not gamification.
- **"AI Tutoring = homework helper"** — rejected. Homework helpers (Photomath/Socratic pattern) react to a submitted problem with a solution/explanation but hold no curriculum, no persistent learner state, and no responsibility for progress. Boundary case, not the Type.
- **"24/7 availability" as defining** — rejected; trivially true of all software, marketing emphasis only.

## Boundary Findings

1. **vs Tutoring Platform** — A Tutoring Platform brokers *human* tutors: tutor profiles, search/matching, booking, sessions, payments; the pedagogy is executed by the human tutor. In an AI Tutoring Application the software executes the pedagogy. Test: remove software-executed pedagogy (pedagogy performed by booked humans) → Tutoring Platform. Note: hybrid products exist (Squirrel AI centers; Carnegie Learning's "High-Impact Tutoring" is a *service*, not the software Type).
2. **vs LMS** — An LMS manages institutional courses: enrollment, content delivery, assignment submission, gradebook; pedagogy is executed by human teachers. An AI tutor executes pedagogy itself and is learner-facing. They coexist (Khanmigo inside district implementations; MATHia inside school math solutions) without merging.
3. **vs MOOC Platform / Educational Content Platform** — content consumption (videos, articles, lectures) with at most static quizzes; no software-executed instructional loop, no performance-conditioned selection. Khan Academy itself is a content+exercise platform; Khanmigo is the AI tutoring layer on top — a useful illustration that the tutoring loop, not the content, defines this Type.
4. **vs Homework-helper / Answer Engine** — reactive answer/explanation on demand (Photomath, Socratic, ChatGPT-as-tutor). No curriculum structure, no persistent learner state, no instructional responsibility. Test: remove curriculum + learner-progress state → homework helper / general assistant. This is the sharpest "remove X and it becomes another Type" boundary.
5. **vs Language Learning Application** — modern language apps execute the same loop (adaptive practice, feedback, mastery state) in the language domain. Language Learning Application is a subject-domain sibling Type; overlap occurs when a language app runs the full tutoring loop. Flagged for STATUS Boundary Issues.
6. **vs Test Preparation Platform** — test prep adds exam-specific scoring/prediction/strategy; an AI tutor can be pointed at test prep (Khanmigo + SAT content). Purpose overlay rather than a structural boundary.
7. **vs Assessment Platform** — ALEKS performs assessment, but assessment exists in service of selecting what to teach next; standalone assessment (proctoring, item banking, scoring at scale) is a different Type.

Historical/market-sample check (per §24): the L0 holds for pre-LLM products (ALEKS — decades of accumulated interaction data per its own materials; MATHia — long-running adaptive lineage; Squirrel AI — pre-LLM adaptive core with a recent LLM-era model layer) and for the LLM era (Khanmigo). A modern LLM chatbot *without* curriculum structure and learner-progress responsibility (general assistant used as a tutor) does **not** fit — confirming that the invariant is software-executed, performance-conditioned pedagogy against a structured subject, not any particular AI technique. The academic literature's term for this family is "Intelligent Tutoring System (ITS)"; the market now says "AI tutor". (Note: ITS terminology and specific product founding dates are general context, not verified from the fetched pages.)

Cross-reference: this Type has the same abstract shape as AI Fitness Coach (already documented): a known individual + software-composed program + guided execution with performance capture + system-driven adaptation. Domain differs (fitness vs. academic subjects); recorded as a family resemblance, not a merge.

## Uncertainties

- Khanmigo's learner-state depth: whether the chat tutor itself maintains a persistent learner model beyond the host platform's mastery system was not directly observed (help-center articles on reports/chat history were seen as titles only). Assertions kept weak.
- Squirrel AI in-lesson mechanics (how the tablet software sequences lessons, what feedback looks like) — only marketing-level descriptions reachable; US site is franchise-oriented. Assertions kept at description strength.
- MATHia's cognitive-model internals — vendor page says "cognitive and learning science" without detail; no overclaim made.
- Whether Khanmigo performs any diagnosis/placement — not observed; treated as absent rather than asserted absent.
- Market numbers (users, score gains, success rates) are vendor claims; excluded from canonical claims.

## Final Synthesis

The AI Tutoring Application is defined by **who executes the pedagogy and how instruction is conditioned**: the software itself teaches — it structures a subject into learnable units, interacts with an identified learner through questions and problems, evaluates responses, and uses the learner's observed performance (in the moment and/or as persistent mastery state) to decide what comes next. Everything else — the AI mechanism (LLM, cognitive model, knowledge space), the interaction form (chat vs. workspace vs. tablet), the customer channel (consumer, school, learning center), the human supervision posture, diagnosis, gamification, adult reporting — is common mature structure or variant space. The Type sits between content platforms (which deliver material but do not tutor), tutoring marketplaces (where humans tutor), LMS/MOOC platforms (which manage courses), and homework helpers (which answer but do not take responsibility for learning progress).
