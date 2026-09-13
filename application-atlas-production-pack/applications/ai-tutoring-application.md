# AI Tutoring Application

## Overview

An **AI Tutoring Application** is a learning application in which the software itself performs the tutoring role: it structures a subject into learnable units, interacts with an identified learner through questions and problems, evaluates the learner's responses, and uses the learner's observed performance to decide what to present next.

The defining structure is small:

```text
Identified learner with a learning objective
└── Subject structured into learnable units
    └── Software-executed instructional interaction
        (system poses → learner responds → system evaluates → system responds instructionally)
        └── Performance-conditioned instruction
            (what comes next depends on how the learner is doing)
```

Everything else commonly associated with the category — conversational AI chatbots, hint ladders, mastery dashboards, placement tests, gamification, parent/teacher reports — is widespread in current products but is not what makes the product an AI tutor. The category long predates modern large language models: adaptive learning systems built on rules, cognitive models, and mathematical models of knowledge instantiate the same core, and a general-purpose AI chatbot used informally as a tutor does **not** (it lacks the subject structure and the responsibility for learning progress).

When the pedagogy is executed by a human brokered through the app, the product is a Tutoring Platform; when the software only delivers content for a human teacher to teach with, it is an LMS or content platform; when it only answers submitted questions without tracking learning progress, it is a homework helper or answer engine.

## Users & Context

The primary user is a **learner** — a student working toward competence in a subject: school-age children in core subjects (most commonly mathematics), higher-education students in quantitative courses, and adults learning skills such as programming or writing.

Typical reasons to open the application:

- work through practice on a subject with immediate feedback and help when stuck
- catch up on prerequisite material the learner was never solid on
- get unstuck on homework **in a way that teaches** rather than just supplies an answer
- prepare for an exam or course placement
- extend beyond grade level (enrichment)

Secondary users surround the learner:

- **parents** — enable and supervise a child's access, monitor progress analytics
- **teachers** — assign or recommend the work, monitor class progress, receive alerts about students who are struggling or idle, and integrate the software into classroom instruction
- **administrators** — oversee usage and outcomes across schools or districts

The work environment is typically a web or mobile session of focused practice (tens of minutes), often recurring daily or several times a week; some products extend this to dedicated tablet hardware in physical learning centers, and school-embedded products run inside scheduled class or homework time.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as an AI tutoring application:

- **Identified learner with a learning objective** — the application serves a specific, persistent person who is trying to get better at something. Without a persistent identified learner, the product is an anonymous quiz or a one-shot answer tool.
- **Subject structured into learnable units** — the domain is organized into topics, skills, knowledge points, or content-anchored exercises, so instruction can be targeted at something specific. Without this, the product is a general-purpose chat assistant.
- **Software-executed instructional interaction** — the system itself poses questions or problems, evaluates what the learner does, and responds instructionally: feedback, hints, explanations, next steps. The pedagogy is executed by the software, not by a human tutor and not by a static lesson. Without this, the product is a content library or a human-tutor marketplace.
- **Performance-conditioned instruction** — what the system presents or says next is shaped by the learner's observed performance, either within the ongoing interaction or through a persistent record of what the learner has mastered. Without this, the product is a fixed interactive course with no responsibility for progress.

### Standard Capabilities in Mature Products

A typical modern product carries most of the following. They make tutoring practical; they do not define the Type.

- **Practice engine with instant evaluation** — a steady stream of problems or prompts, each answered by the learner and judged immediately.
- **Hint and scaffold machinery** — layered help that reveals more only as needed: multi-level hints (each level more explicit than the last), just-in-time messages triggered by recognizable mistakes, and — in conversational products — Socratic questioning that guides toward the answer instead of stating it.
- **Explanations and worked examples** — step-by-step demonstrations, rewatchable animations, and reference explanations the learner can consult before or while solving.
- **Mastery and progress tracking** — a persistent per-unit record of what the learner has demonstrated, surfaced to the learner as a progress visual (for example, a course-coverage chart divided by topic branch, or per-skill progress indicators).
- **Diagnosis or placement** — an initial assessment that locates the learner before instruction begins, in some products; in others, placement happens implicitly through continuous assessment during use.
- **Retention checks** — periodic re-assessment of previously learned material to confirm it has stuck.
- **Adult-facing monitoring** — reports and dashboards for teachers and/or parents: progress by skill or topic, time-on-task, and alerts for students who are struggling, stalling, or flagged for safety.
- **Curriculum alignment** — units mapped to grade levels, courses, or academic standards so the work fits an institutional syllabus.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Products realize each concept differently:

```text
Concept:            Subject structured into learnable units
Implementations:    course topics, skills within workspaces, fine-grained
                    knowledge points, content-library exercises/videos/articles

Concept:            Learner-progress state
Implementations:    knowledge-state model over topics, per-skill mastery,
                    knowledge-point mastery map, host-platform mastery levels

Concept:            Software-executed instruction
Implementations:    LLM conversational tutor, adaptive problem-solving engine,
                    knowledge-point lesson/practice/test cycle

Concept:            Performance-conditioned selection
Implementations:    "ready to learn" topic offering, skill-by-skill adaptation
                    to every action, diagnostic-driven learning path,
                    in-conversation responsiveness to what the learner says
```

A reader who has only seen one implementation — for example, a modern chatbot-style tutor — should still be able to recognize older adaptive learning systems, and vice versa, from the Core Model.

## How It Works

### Place the learner

```text
Learner (or parent/school) creates an account
→ subject and level are chosen or assigned
→ placement: either an explicit diagnostic assessment,
   or location happens implicitly as the learner works
→ the system establishes a starting picture of what the learner knows
```

School-embedded products typically receive learners through institutional rostering; consumer products gate children's access through a parent account.

### The tutoring loop

The core loop repeats continuously:

```text
System presents a problem, question, or prompt
→ learner responds (constructed answer, steps, or conversational reply)
→ system evaluates the response
→ system responds instructionally:
     correct  → confirmation, possibly a harder next step
     close but wrong → targeted correction for that specific mistake
     stuck    → hints, one level at a time; explanations; worked examples
→ the learner's record is updated
→ the next presentation is conditioned on all of the above
```

In conversational implementations the loop is a dialogue: the learner states a problem or asks about the material, and the tutor questions, probes, and guides the learner to produce the answer rather than handing it over. In engine-style implementations the loop is problem-solving: the system selects the next problem or topic, watches every action the learner takes, and intervenes with contextual hints at the moment of difficulty.

### Accumulate mastery

Across sessions, successful work moves units from "not yet" to "demonstrated" in the learner's persistent record. The learner sees this as a filling progress visual; the system uses it to keep offering work at the boundary of what the learner is ready for — hard enough to be productive, not so hard as to cause frustration, and skipping what is already mastered. Periodic re-assessments verify that earlier gains were retained, and the cycle of assessment and learning continues for the length of the course.

### The adult oversight loop

```text
Learner works
→ system records performance and behavior
→ teachers/parents view reports and analytics
→ alerts surface learners who are struggling, stalling, or flagged
→ the adult intervenes (re-teaching, encouragement, access changes)
```

In school deployments this loop is the teacher's main surface; in consumer deployments it is the parent's. Some products also give teachers live in-session visibility and the ability to switch the tutor off for a period of focused work.

### Tiers of capability

**Defining core** — without these, not an AI tutoring application:

- identified learner with a learning objective
- subject structured into learnable units
- software-executed instructional interaction (pose → respond → evaluate → instructional response)
- performance-conditioned instruction

**Standard in mature products**:

- practice engine with instant evaluation
- hint/scaffold machinery and worked examples
- mastery tracking with a learner-visible progress surface
- diagnosis/placement (explicit or implicit)
- retention checks
- adult-facing monitoring and alerts
- curriculum/standards alignment

**Variant / optional**:

- conversational chat as the primary surface
- dedicated tablet hardware or physical learning centers
- human teachers delivering companion instruction alongside the system
- gamification (points, streaks, cosmetics)
- speech input/output
- test-prep alignment or use as a graded course component

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Tutoring surface

The learner's primary working surface — either a **problem workspace** (a problem statement, an answer input with subject-appropriate entry tools such as expression editors or graphing inputs, hint buttons, and learning supports alongside) or a **chat conversation** (message thread with the tutor, often anchored to a specific exercise, video, or article being studied).

- typical information: the current problem or topic, the learner's working area, available hints, related learning supports
- primary actions: answer, request a hint, view an explanation or worked example, ask a question in words, move to the next item

### Progress surface

The learner's map of the course.

- typical information: units/skills/topics with mastered / in-progress / not-yet states, overall course completion
- primary actions: choose what to work on next (where the product allows choice), review progress

### Learning supports

Reference and demonstration material reachable from the working surface: worked examples, step-by-step demonstrations, animations, glossaries. Reusable on demand, not part of the score.

### Adult dashboard

The teacher/parent surface.

- typical information: per-learner and per-class progress by skill or topic, time spent, alerts (struggling, idle, at-risk, flagged conversations)
- primary actions: assign or recommend work, inspect a learner's history (in some products including tutor conversations), adjust access, message or intervene

### Settings / safety controls

Access and supervision controls: parent gating for minors, conversation flagging with notifications, the ability to disable the tutor during focused work, and privacy configuration.

## Important Rules / Behaviors

### The tutor guides; it does not just answer

The most consistent pedagogical rule across the researched sample: the system's responses are designed to produce learning, not just output. Conversational products explicitly withhold final answers and question the learner toward them; engine products gate help behind hint levels so the learner attempts the work first, and correct the *specific* mistake made rather than restating the solution. A product whose primary behavior is to emit complete solutions on demand has left this Type.

### Progression is earned, not browsed

What the learner may work on next is constrained by their demonstrated state. Topics or skills become available as prerequisites are mastered; the system keeps the learner at the edge of their ability. In several products the learner cannot freely jump ahead to unearned material.

### Constructed responses over guessing

Several products deliberately avoid multiple-choice formats, requiring the learner to construct answers with subject-appropriate input tools, so that evaluation reflects real understanding rather than elimination.

### Retention is checked, not assumed

Previously mastered material is periodically re-assessed; a learner who has forgotten something regresses in the record and the material re-enters the loop.

### Adults see aggregate truth, learners see encouragement

Progress surfaces are split by audience: the learner sees motivating progress; adults see detailed performance data and risk alerts. In products serving minors, conversations may be monitored and flagged, with notifications to parents or schools — supervision is a structural feature, not an afterthought.

### The record is persistent and consequential

The learner's history — what was attempted, what was mastered, what was forgotten — persists across sessions and drives everything the system does next. This persistence is what makes the system accountable for learning progress, and it is the main behavioral line between this Type and answer-on-demand tools.

## Variants

Common forms of the Type:

- **Conversational LLM tutor** — free-form dialogue anchored to a structured content library; Socratic guidance; writing and coding coaching alongside subject tutoring; consumer subscription or district licensing.
- **Adaptive problem-solving engine** — structured workspaces of problems with layered hints and skill-level mastery; typically school-embedded and blended with classroom teaching.
- **Knowledge-point adaptive system** — the subject decomposed into fine-grained knowledge points; diagnostic-driven personalized paths; often delivered through dedicated tablets, sometimes paired with human instructors in physical learning centers.
- **Knowledge-space assessment-led system** — an explicit mathematical model of feasible knowledge states; initial and periodic assessments locate the learner; open-response problems; common in higher education and as a graded course component.
- **Hybrid human + AI** — the system owns the learning path and practice; human teachers deliver companion instruction (learning-center model).
- **Subject-domain siblings** — language-learning applications run the same loop for language acquisition; when they do, they sit at the boundary of this Type (see Related Types).

A variant remains a variant as long as the defining core holds. If the pedagogy moves to a human (marketplace), the content stops adapting (course library), or the progress record disappears (answer tool), the product has crossed into a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Tutoring Platform | pedagogy is executed by human tutors brokered through the app (profiles, matching, booking, sessions, payments); here the software executes the pedagogy |
| Learning Management System / LMS | institutional course management (enrollment, content delivery, assignments, gradebook); teachers execute the pedagogy; an AI tutor is learner-facing and self-executing, and may live alongside an LMS |
| MOOC Platform | course catalog with video lectures and quizzes at scale; content consumption rather than a software-executed, performance-conditioned tutoring loop |
| Educational Content Platform | videos, articles, and reference material for consumption; no instructional loop and no responsibility for progress (a content library is often the substrate an AI tutor is layered onto) |
| Test Preparation Platform | exam-specific purpose overlay (scoring, prediction, strategy); an AI tutor can be pointed at test prep, but test prep adds objects and goals this Type does not require |
| Language Learning Application | subject-domain sibling: modern language apps execute the same adaptive loop for language; overlap occurs when the full loop is present — the subject, not the structure, differs |
| Assessment Platform | assessment as the product (item banking, proctoring, scoring at scale); here assessment exists in service of selecting what to teach next |
| AI Research Assistant / Answer Engine | responds to queries with information or solutions; no curriculum, no persistent learner state, no instructional responsibility |
| Homework-helper applications | reactive solution/explanation for a submitted problem; no learning-progress record — the sharpest boundary of this Type |

The boundary with **homework helpers and general AI assistants** is the most important one, because modern chatbots blur it visually (both are conversational). The structural test: does the product hold a structured subject and a persistent learner record, and is what happens next conditioned on the learner's progress? If not, it answers questions; it does not tutor.

## Representative Products

- **Khanmigo** (Khan Academy) — conversational LLM tutor layered on a free content library; consumer and district channels
- **MATHia** (Carnegie Learning) — adaptive problem-solving engine for school mathematics, blended with classroom instruction
- **Squirrel AI** (Squirrel Ai Learning) — knowledge-point adaptive system delivered via tablets and physical learning centers with companion human instruction
- **ALEKS** (McGraw Hill) — knowledge-space-theory assessment-led learning system for K-12 and higher education

The defining core was checked across a pre-LLM generation (ALEKS, MATHia, Squirrel AI's pre-LLM core) as well as the current LLM generation, so the definition does not over-fit to today's chatbot-style implementations. Homework-helper products (camera-based math solvers, search-based study helpers) and general AI assistants were examined as boundary cases and deliberately excluded from the Type.

## Sources

Research date: **2026-09-06**

- Khanmigo (Khan Academy) — https://www.khanmigo.ai/ , https://www.khanmigo.ai/learners , https://support.khanacademy.org/hc/en-us (incl. help-center search results on Khanmigo Activities, teacher reports, chat-history access, conversation flagging, focus mode)
- MATHia (Carnegie Learning) — https://www.carnegielearning.com/solutions/math/mathia , https://support.carnegielearning.com/help-center/math/home-connection/mathia-support22/mathia-for-students/article/getting-started-mathia-students/
- Squirrel AI — https://squirrelai.com/ (product, technology, and FAQ sections)
- ALEKS (McGraw Hill) — https://www.aleks.com/about_aleks , https://www.aleks.com/about_aleks/HowALEKSWorks_TextDescription

> Sourcing limitations: Squirrel AI's end-user operational documentation (in-lesson software behavior) was not reachable; claims about its internal mechanics are kept at the vendor-description level. Khan Academy help-center articles were observed as search-result titles and snippets rather than full pages. Vendor marketing statistics (user counts, score gains, success rates, pricing) were deliberately excluded from this document. Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
