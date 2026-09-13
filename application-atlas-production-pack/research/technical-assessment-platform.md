# Research Notes — Technical Assessment Platform

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand the Application Type "Technical Assessment Platform" (DIRECTORY §09 HR, Workforce & Talent): what the software actually is, who uses it, what core objects and workflows it has, and where its boundaries lie. Special obligations this pass:

1. Determine whether this leaf is a distinct Type or a variant of the already-processed Candidate Assessment Platform / Psychometric Assessment Platform siblings, and **discharge or update the §09 three-leaf joint-review flag** (psychometric pass flagged it 2026-09-06; candidate pass updated it 2026-09-07 leaving "coding-environment center" for this pass).
2. Stay consistent with the education-side Assessment Platform pass (§23), which kept the hiring-audience leaves distinct as audience variants, and with the skills-management pass boundary ("external-candidate skill testing vs internal workforce inventory").

## Initial Boundary

Working hypothesis before research:

- Core purpose: evaluating **technical (mainly software-engineering) skill of candidates** for hiring decisions, by having candidates produce and run real technical work (code) in an environment the platform provides.
- Likely users: recruiters / talent acquisition, engineering hiring managers, interviewers; candidates as takers.
- Nearest confusions: Candidate Assessment Platform (role-agnostic sibling), Psychometric Assessment Platform (instrument-science sibling), ATS (pipeline owner), Interview Management / Video Interviewing (human-judgment sessions), education Assessment Platform (§23, learning population), and — on the §12 software side — Software Test Management / Load Testing (which "test" systems, not people). Also developer practice/certification platforms (HackerRank community side, CodeSignal Learn) which serve the developer, not the employer.

## Research Questions

1. What are the core objects? (assessment/test, question/task, environment, candidate, invitation, submission, evaluation/result, interview session?)
2. What does the technical environment add beyond generic candidate assessment — is the code-execution environment definitional or incidental?
3. How does the main workflow run end-to-end (compose → invite → candidate works → evaluate → review → decision)?
4. How is technical work scored — machine (test cases, auto-grading, static analysis) vs human (structured review, playback)?
5. What is the role of the live collaborative coding interview relative to the asynchronous screen?
6. What integrity machinery is standard (plagiarism, proctoring, identity, AI-era controls)?
7. What role does AI play in 2026 — as threat (cheating), as assessed skill (AI-assisted coding), as evaluator (AI interviews)?
8. Historical check: would pre-platform technical hiring practice (whiteboard + emailed take-home + manual review) satisfy an abstracted core?

## Representative Products

Selected for market representativeness, documentation depth, different product philosophies, and different customer tiers:

| Product | Philosophy / position | Customer tier |
|---|---|---|
| HackerRank | Full "developer skills platform" suite (Screen / Interview / Engage / SkillUp / Chakra) | Enterprise + free self-serve entry |
| Codility | Engineering-hiring specialist (Screen / Interview / Skills Intelligence); VS Code-based real IDE; I/O-psychologist positioning | Mid-market/enterprise |
| CodeSignal | "AI-native skills platform"; certified/validated assessments; screen-to-develop pole | Enterprise + startup/SMB plans |
| CoderPad | Interview-first heritage; Screen + Interview in "one flow" | Startup → enterprise |

Market context only (not sampled; zero claims carried): TestDome, HackerEarth, iMocha, Devskiller, AlgoExpert-style consumer prep.

## Sources

Evidence layers: **A** = directly observed on official source of a specific product; **B** = observed across multiple products; **C** = canonical inference.

| Source | Tier | Result |
|---|---|---|
| HackerRank products page (hackerrank.com/products/) | 2 | Fetched 2026-09-08 (A) |
| HackerRank Knowledge Base root (support.hackerrank.com/hc/en-us) | 1 | Fetched (A) — collections: Screen 88, Interview 57, Chakra 11, SkillUp 19, Library 51, Integrations 95 articles |
| HackerRank KB "Screen" collection | 1 | Fetched (A) — sub-collections: Managing Tests, Test Integrity, Test Reports, Test Settings, Invite Candidates, Best Practice Guides |
| HackerRank KB "Execution Environment" article | 1 | Fetched (A) — richest technical evidence |
| HackerRank KB "Interview" collection | 1 | Fetched (A) |
| Codility root (codility.com) | 2 | Fetched (A) |
| Codility support/help center (support.codility.com) | 1 | Transport error + timeout ×2 — **abandoned per network rule** |
| CodeSignal root (codesignal.com) | 2 | Fetched (A) |
| CodeSignal Technical Assessments page | 2 | Fetched (A) — includes product FAQ |
| CodeSignal Knowledge Base (support.codesignal.com) | 1 | Transport error + timeout ×2 — **abandoned per network rule** |
| CoderPad root (coderpad.io) | 2 | Fetched (A) |
| CoderPad docs (docs.coderpad.io) | 1 | 525 error ×2 — **abandoned per network rule** |
| CoderPad Technical Screening page (coderpad.io/platform/technical-screening/) | 2 | Fetched (A) |

Source-access limitation: no help-center-level operational docs were reachable for Codility, CodeSignal, or CoderPad (repeated transport/SSL/timeout failures). Only HackerRank provided Tier-1 operational documentation. Consequence: cross-product workflow detail is calibrated at Tier-2 strength; no precise numeric limits, durations, or defaults are asserted as facts in the final document; vendor-claimed figures (question counts, language counts, accuracy/completion percentages) are recorded below as vendor claims only, kept out of the canonical document.

## Product Observations

### HackerRank (A — products page; A — KB Tier 1)

- Positions as "developer skills platform" for tech teams; products: **Screen** ("save time and accelerate your hiring" — pre-screen), **Interview** ("conduct stellar technical interviews"), **Engage** (hackathons/tech brand — adjacent), **SkillUp** (internal mobility/upskilling — adjacent pole), **Chakra** (AI interviews for pre-screen — era-current).
- **Certified Assessments**: "launch standardized, role-based tests in minutes" — standardized role-based tests as a packaged capability.
- **Plagiarism Detection** as named feature ("AI-powered"); anti-impersonation, content-leakage protection; vendor-claimed "95% accuracy" figure (L3, not carried).
- **Real-World Questions**: "assess technical hires with real-world coding questions... in an environment that mimics day-to-day work."
- Skills taxonomy mapped to roles; "centralized admin controls"; "cut-off scores and question performance" insights; ATS/HR-tool integrations + API.
- KB structure for Screen mirrors the operational loop: **Managing Tests → Invite Candidates → (candidate takes) → Test Reports → Test Integrity** (+ Test Settings, Best Practice Guides). Interview has its own collection (New Experience / Legacy).
- KB "Execution Environment" (Tier-1): platform provides a comprehensive execution environment supporting dozens of languages and frameworks with per-language time/memory limits; question types span algorithmic coding, SQL/database, **front-end, back-end, full-stack (real OS instances with frameworks/databases: PERN/MEAN/MERN, Spring Boot, Rails, Django...), mobile (Android/iOS/React Native/Flutter), data science, QA automation (Selenium/Cypress/Playwright), DevOps/cloud, and generative-AI/RAG** tasks; submissions size-capped; question types run on real Ubuntu LTS instances with preinstalled toolchains. (Exact limits/versions = L3.)
- AI era posture: assess "human and human+AI skills" — code review, debugging, "simulate real-world tasks like debugging a Jira ticket with an AI assistant"; responsible-AI/bias-audit positioning.

### Codility (A — root page; help center unreachable)

- Products: **Screen** ("filter candidates before technical interviews" — "candidates work through real problems in their own time"), **Interview** ("structured technical interviews in VS Code"), **Skills Intelligence** (internal engineering-team capability mapping — internal pole).
- **Real IDE powered by VS Code**: "package installation, terminal access, multi-file projects, documentation... You see how someone works, not how they cope with artificial constraints."
- **Automated code analysis** evaluating "quality, maintainability, and complexity" — beyond pass/fail test cases.
- Integrity framing: "Identity verification, impersonation detection, proctoring... The signal is the person"; "Integrity means knowing who is at the keyboard, not policing which tools they use."
- AI-era posture: customer chooses how AI fits in ("Define how AI is used in your assessments"); AI-specific task library (prompt engineering, evaluating AI-generated code); "Not generic coding puzzles with an AI wrapper."
- Assessment science/compliance positioning: "Assessments designed by I/O psychologists with documented methodology and auditable scoring"; SOC 2/ISO 27001/GDPR/WCAG claims; API access; "Plugs into your existing tech stack, from applicant tracking to HRIS."
- Candidate-side testimonials mention **test cases validating edge cases** and multi-language support; custom questions "based on real problems we face" (G2 reviews quoted on-site).
- Vendor claim: "powers over 20,000 engineering teams" (L3).

### CodeSignal (A — root; A — Technical Assessments page incl. FAQ)

- Positions as "AI-native skills platform" / "agentic skills validation & development"; structure: **Screen** (AI Interviewer / AI Phone Screens / AI Video Avatars), **Assess** (Technical / Business / Agentic / Behavioral Assessments), **Interview** (Live Tech Interviews + AI agents), **Develop** (Learn assessments/academies/courses — internal-development pole), **Skills Intelligence** (benchmarking).
- Technical Assessments page: "real-world IDE where they can build, run, and test applications as they would on the job"; **Certified Assessments** "written by subject matter experts and validated by IO psychologists" (vendor-claimed research hours = L3); **Advanced cheating and fraud detection**: "proctoring, identity checks, and plagiarism detection that flags suspicious and AI-assisted behavior."
- FAQ (Tier-2 but operational in substance): cheating prevention stack = Suspicion Score, full-service proctoring with ID verification, dynamic question rotation ("thousands of variations"), IP tracking, copy/paste disabling option, Leak Sweep monitoring for leaked content; ATS integration "send assessments directly from your ATS and automatically sync results to candidate profiles"; implementation "fully operational within a few weeks" using pre-built Certified Assessments.
- Question-type catalog (A): Bug fix, Conversation, Filesystem, Filesystem Frontend, Matrix, Output only, Progressive Filesystem, Quiz, Recovery, Simple Front-end, Single-Function, SQL, Whiteboard, Writing — spanning coding, databases, frontend, design/whiteboard.
- Coverage catalog (A): ~40 coding languages; database engines (MSSQL/MongoDB/MySQL/PostgreSQL/shells); skills taxonomy (programming fundamentals → system design → security → MLOps → LLMs); roles list (backend/frontend/fullstack/mobile/QA/data/ML/DevOps/SRE/cloud/prompt engineer...).
- Assessment catalog (A): General Coding Assessment, Industry Coding, AI-Assisted Coding (Full-stack), ML Engineering, Data Analytics, System Design, AWS Engineering — each mapped to roles and skills. Public "Assessment Explorer" to browse assessments.
- AI posture (A): "Traditional assessments prohibit unauthorized AI use and detect AI-generated code. We also offer AI-Assisted Assessments with Cosmo... so you can evaluate how candidates leverage AI tools" (product-branded assistant = L3).

### CoderPad (A — root; A — Technical Screening page; docs unreachable)

- Self-describes as "Coding Interview & Technical Assessment Platform"; heritage philosophy: real engineering work over algorithm puzzles; "Filter candidates based on their coding skills, in 99+ languages" (vendor claim = L3).
- **Interview** (heritage center): "real-time, collaborative coding sessions" — collaborative IDE, multi-file environment, built-in interviewer tools: "structured scoring, private notes, and **code playback**"; AI-enabled: candidates use AI inside the pad, prompt history/outputs captured for review.
- **Screen**: "reliable coding assessments built around real-world engineering tasks" — question bank (vendor claim 4K+ validated questions across 70+ skills), **gamified exercises** ("cheat-resistant, engagement-friendly coding games"), **Projects** ("multi-file, auto-graded, bring-your-stack tasks — AI-enabled", customizable environments with preloaded dependencies); "auto-graded + rubrics for standardized, fast scoring"; benchmarking against others who took similar assessments; reports of strengths/weaknesses ("decide who advances to the next round").
- Integrity (Screen): "code playback, plagiarism detection and copy/paste tracking", AI webcam analysis, AI follow-up questions verifying the candidate understands their own submitted code; "tests independently reviewed for fairness and validity."
- Explicit funnel framing (A): "One flow from screen to interview": basic screening call → async screen with Projects → **handoff to live interview** → final decision. ATS + scheduling integrations.
- Candidate-experience positioning: completion-rate/vendor-claim stats (L3).

## Cross-product Comparison

| Dimension | HackerRank | Codility | CodeSignal | CoderPad | Layer |
|---|---|---|---|---|---|
| Serves employer-side hiring evaluation of candidates | yes | yes | yes | yes | **L0** |
| Candidate produces real technical work (code) as the evidence | yes (real-world questions, projects) | yes (real problems, multi-file) | yes (build/run/test in IDE) | yes (tasks/projects/live pad) | **L0** |
| Platform-provided code-execution environment (sandbox/IDE/pad where work runs) | yes (execution environment, dozens of languages; fullstack/mobile/QA/AI environments) | yes (VS Code real IDE, terminal, packages) | yes (real-world IDE, build/run/debug) | yes (collaborative pad, multi-file, bring-your-stack) | **L0** |
| Assessment bound to identified candidate; result retained & consumed in hiring funnel | yes (Screen tests, reports, cut-off scores) | yes (candidate tests, results) | yes (ATS-triggered, synced results) | yes (Screen reports, handoff to interview) | **L0** |
| Machine evaluation of the work (test cases / auto-grading) | yes | yes (test cases per candidate testimony; automated code analysis) | yes (auto-scored certified assessments) | yes (auto-graded Projects + rubrics) | **L0-ish** (see note) |
| Asynchronous pre-screen + live collaborative interview as two surfaces of one product | yes (Screen + Interview) | yes (Screen + Interview) | yes (Assess + Live Tech Interviews) | yes (Screen + Interview, "one flow") | **B common** |
| Question/challenge library + custom question authoring | yes (Library; custom) | yes (custom questions on real problems) | yes (certified catalog + Assessment Explorer) | yes (bank + gamified + own questions) | **B common** |
| Role-based pre-built/standardized assessments | yes (Certified Assessments) | yes (role tasks) | yes (Certified Assessments catalog) | yes (role/seniority-organized bank) | **B common** |
| Integrity machinery (plagiarism, proctoring/identity, playback, AI-era controls) | yes (plagiarism detection, impersonation, leakage) | yes (identity verification, impersonation detection, proctoring) | yes (Suspicion Score, proctoring, rotation, leak monitoring) | yes (playback, plagiarism, copy/paste tracking, webcam AI) | **B common** |
| Results reporting: scores, strengths/weaknesses, benchmarks/cut-offs | yes | yes (auditable scoring) | yes (skills validation, benchmarking) | yes (benchmarks, strengths/weaknesses) | **B common** |
| ATS integration + API | yes | yes | yes (ATS-triggered + synced) | yes | **B common** |
| Fairness/validity apparatus | yes (bias-audit claims) | yes (I/O psychologists, auditable) | yes (IO-validated certified) | yes (independent review) | **B common** |
| Automated code-quality/static analysis beyond test cases | — | yes (named capability) | — | — | product-specific |
| Gamified exercise format | — | — | — | yes (named pole) | product-specific |
| Internal-team capability/skills-intelligence pole | yes (SkillUp) | yes (Skills Intelligence) | yes (Develop + Skills Intelligence) | — | L2 variant pole |
| AI-run interviews (agentic) | yes (Chakra) | — | yes (AI Interviewer/agents) | — | L2 era-current variant |
| Whiteboard/diagram and system-design task types | — (roles directory suggests breadth; not observed) | — (not observed) | yes (Whiteboard, System Design assessments) | — | A/one-product — treat as optional |
| Take-home project depth ("bring your stack") | yes (projects environments) | yes (multi-file projects) | yes (filesystem question types) | yes (Projects) | **B common** |

Note on machine evaluation: auto-grading/test-case evaluation is universal across the asynchronous screen surfaces (all four). In the live-interview surface, evaluation is human (structured scoring/notes) with the platform rendering the artifact reviewable (playback). The invariant is therefore "the platform renders the produced work as evaluable evidence" — with machine auto-evaluation as the standard mature implementation on the async side.

## Abstraction

### L0 — Defining Invariant (minimal)

Four jointly-held structures; jointly-held is load-bearing:

1. **Employer-side hiring evaluation** — the platform is operated by a hiring organization (or a service firm acting for employers) to evaluate identified candidates' technical skill for its own hiring decisions. Remove → developer practice/certification platform (serves the developer) or internal-learning territory.
2. **Technical work-product demonstration in a platform-provided execution environment** — the candidate's evidence is real technical work (code at minimum) produced inside an environment the platform provides, where the work can actually be run (code execution sandbox/IDE/pad). Remove the environment → role-agnostic Candidate Assessment Platform (quiz/survey-style instruments). Remove the execution capability → static quizzes or whiteboard-only tooling; the "technical" center dissolves.
3. **Evaluation that renders the work as comparable decision evidence** — the platform mechanically evaluates the produced work (test cases, auto-grading, code analysis) and/or renders it reviewable (playback, structured scorecards) so results are comparable across candidates for the same assessment. Remove → a shared editor/pastebin tool or interview-scheduling ops, not a measurement platform.
4. **The managed evaluation event** — an assessment (a defined set of technical tasks, commonly role-based) bound to an identified candidate as a persistent event that carries invitation, submission, evaluation, and result retained as the hiring record for that candidate. Remove → anonymous one-off challenges; the "platform" (candidate records, funnel consumption) disappears.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- question/challenge library + custom question authoring
- role-based pre-built/standardized assessment catalog
- multi-language, multi-framework support; time limits; per-language execution limits
- asynchronous screen + live collaborative interview as two surfaces of one product
- integrity machinery: plagiarism detection, proctoring/identity verification, playback, copy/paste tracking, question rotation; AI-era: AI-use policy controls, AI-behavior detection
- results reporting: scores, rankings/benchmarks/cut-offs, strengths/weaknesses, question performance
- ATS integration + API; admin/team roles
- fairness/validity apparatus (expert-reviewed/validated content, accessibility, compliance posture)

### L2 — Variant / Optional Structure

- philosophy: screen-first vs interview-first; suite vs focused tool
- environment depth: lightweight editor/pad vs full real IDE (VS Code) with terminal/packages/multi-file projects
- AI posture: prohibit-and-detect vs allow-with-capture vs AI-run interviews (agentic) — era-current axis, all three poles observed in-sample
- format variety: gamified exercises, take-home projects, whiteboard/system-design diagrams, SQL/database tasks, QA-automation environments
- served-population extension: internal mobility/upskilling pole (SkillUp / Skills Intelligence / Learn) — drifts toward skills-management/learning territory
- segment machinery: university/campus hiring, volume hiring
- adjacent bundling: hackathons/talent-brand events

### L3 — Vendor-specific (kept out of final document)

- HackerRank: Chakra AI interviews; Engage hackathon platform; SkillUp Certifications; certified-assessment "95% AI plagiarism accuracy" claim; 2,500 customers/25M developers/172,800 daily assessments claims; exact language versions/time/memory limits (KB table); submission size caps; Safelist/IP articles; New-vs-Legacy interview split.
- Codility: VS Code partnership branding; "20,000 engineering teams" claim; I/O-psychologist staffing claim; SOC2/ISO/GDPR/WCAG badge set; "how AI fits into technical assessment" content marketing.
- CodeSignal: Suspicion Score, Leak Sweep, Cosmo AI assistant (branded); "2,800 hours of research" per certified assessment claim; Assessment Explorer; AI Phone Screens/Video Avatars/agent personas; pre-built assessment catalog names (GCA, Industry Coding...); ATS names in FAQ.
- CoderPad: "99+ languages", "4K+ questions/70+ skills", "96% completion / 97% prefer / 60% higher" claims; gamified-exercise pole; "$30K+ per hire / 30% faster" marketing stats; SOC-2 badge; named case-study customers.

## Rejected Findings

- **"AI interviews are the core"** — rejected: only two of four sampled products ship agentic AI interviewers; the asynchronous code-evaluation loop is the center everywhere. AI interviews are an L2 era-current variant.
- **"Real IDE is definitional"** — rejected as stated: Codility/CodeSignal emphasize real IDEs, but the sampled set also runs on lightweight pads/editors; the invariant is the execution-capable environment, not IDE depth. IDE depth is an L2 axis.
- **"Psychometric-style norming is required"** — rejected: unlike the psychometric sibling, none of the sampled products centers norm-referenced psychological instruments; validity claims attach to task content, not attribute norms. This cleanly separates the sibling.
- **"Plagiarism/proctoring is definitional"** — rejected as definitional (it is universal-in-sample standard capability), because the core loop is complete without it and thin/legal-market deployments vary in its depth; held at L1.
- **"This is just candidate assessment with coding questions"** — rejected: the execution environment changes the object (work-product vs instrument response), the evaluation mechanism (machine execution vs keyed scoring), and the user (engineering interviewers as first-class reviewers). The candidate-assessment pass itself reserved "narrow the environment to code execution" for this leaf.
- **"Live collaborative interview is a different Type"** — rejected for the technical case: the live pad shares the same environment/artifact/record center; the funnel ("screen → interview handoff") is observed inside single products. Interview *operations* (scheduling, panels, generic scorecards for all roles) remain the Interview Management boundary.

## Boundary Findings

- **vs Candidate Assessment Platform (§09 sibling — JOINT REVIEW DISCHARGED from this side)**: the recorded seam holds and is now documented from both directions. Candidate assessment = role-agnostic evaluation workflow in the hiring funnel (configure → deliver → score → compare → advance) across instrument families; technical assessment = the coding-environment-centered pole where the **platform-provided code-execution environment and the machine-evaluated work product** are the organizing center, and engineering interviewers are first-class users. Boundary test: remove the execution environment → candidate assessment; add non-technical role families as the center → candidate assessment. Market straddling exists (TestGorilla/Criteria-class platforms include coding questions; CoderPad self-describes with the generic label "technical assessment platform") but product centers are distinct. **Three-leaf question resolved as three Types with a documented spectrum**: psychometric (vendor-owned normed attribute instruments) / candidate (role-agnostic funnel evaluation loop) / technical (code-execution work-product environment) — the delivery mechanics overlap, the centers do not. No consolidation recommended; a "spectrum view" note is recorded for the atlas maintainers.
- **vs Psychometric Assessment Platform**: attribute measurement with vendor-owned normed instruments + norm-anchored interpretation vs work-product demonstration with execution-based evaluation. Held.
- **vs ATS**: measurement step vs pipeline owner; results flow *into* the ATS (trigger-in/results-out observed at multiple products). Held.
- **vs Interview Management Platform / Video Interviewing**: interview ops (scheduling, panels, human-judgment capture) vs technical measurement environment. The in-product live coding interview stays in-Type because environment + artifact + retained record are the center. Held, consistent with sibling passes.
- **vs education Assessment Platform / Examination Platform (§23)**: population (candidates vs students) and purpose (selection vs learning/certification); the §23 pass already recorded the audience-variant split. Held.
- **vs Software Test Management / Test Automation / Load Testing (§12)**: those systems test *software*; this Type tests *people* by having them write software. Same words ("test cases"), opposite subject. Explicit disambiguation recorded — this is the most dangerous name-collision in the atlas for this leaf.
- **vs Skills Management Platform (§09, boundary recorded by that pass)**: external-candidate skill *events* vs internal workforce skill *inventory*. The internal-mobility/upskilling poles of sampled suites (SkillUp, Skills Intelligence, Learn) drift toward that Type and are held as L2 poles here.
- **vs Developer practice/certification platforms** (HackerRank community, CodeSignal Learn for individuals, consumer prep): served population flips (developer self-improvement vs employer evaluation); practice content may be shared, the record and decision-loop are not. Held as outside boundary; the Learn/SkillUp suite poles sit on the seam.

## Historical / Market-Sample Check

- **Whiteboard coding interviews** (pre-platform standard): human judgment on ephemeral work; no platform environment, no machine evaluation, no retained candidate record → fails L0 legs 2–4; correctly the thin ancestor.
- **Emailed take-home exercises reviewed manually** (still common): work-product demonstration exists but no platform execution environment, no mechanical evaluation, no managed multi-candidate record → thin ancestor; the platform's defining delta over this baseline is exactly legs 2–4.
- **Online judges / competitive-programming arenas** (long-standing, regional variants included, e.g. university OJ systems used for campus recruiting): execution environment + machine scoring exist; they become instances of this Type only when bound to an employer-side hiring evaluation with candidate records (leg 1 + 4). Confirms legs 1/4 are load-bearing and that the core is not cloud/AI-era-specific.
- **Paper-era programming aptitude tests** (hand-scored code-writing exams at hiring boards): leg-1 + leg-3-human form; without the execution environment they are the ancestor pole, reinforcing that leg 2 (execution-capable environment) is what makes the *platform* Type recognizable.
- Historical check **passed**: the L0 requires no AI, no cloud, no VS Code, no proctoring; a self-hosted code-runner + candidate roster + scored submissions satisfies the core.

## Uncertainties

- Codility operational workflow details (help center unreachable) — its screen/interview mechanics are calibrated at Tier-2 strength; no rule-level claims made.
- CodeSignal/CoderPad operational detail (KB/docs unreachable) — same calibration; FAQ-derived mechanics (rotation, copy/paste option) treated as vendor-stated capability, not verified procedure.
- Whether "playback" exists in all four products' async screens (observed at CoderPad explicitly; HackerRank interview-side; not confirmed for Codility/CodeSignal) — held as common-not-universal.
- Whiteboard/system-design task types: only confirmed at CodeSignal this pass; possibly present elsewhere — held optional.
- The exact per-product split of "skills intelligence"/internal poles vs the hiring core — suite packaging differs; held as L2 pole, not structurally compared.

## Final Synthesis

A Technical Assessment Platform is the hiring organization's instrument for evaluating candidates' technical skill by having them demonstrate real technical work — code at minimum — inside a code-execution environment the platform provides, with the platform rendering that work as comparable decision evidence (machine-evaluated where possible, reviewable always) and retaining the evaluation as a per-candidate record consumed in the hiring funnel. Around that core, mature products add question libraries and certified/role-based catalogs, an asynchronous-screen-plus-live-collaborative-interview product pair, integrity machinery that has been reshaped by AI (plagiarism/proctoring/identity plus AI-use policy and detection), benchmarking and reporting, ATS integration, and fairness/validity apparatus; variants span screen-first vs interview-first philosophies, environment depth (pad vs real IDE), AI posture (prohibit/detect vs allow/capture vs AI-run), task-format breadth (gamified, projects, whiteboard/system design, QA/data/cloud environments), and an internal-mobility/upskilling pole that drifts toward skills-management territory. The Type is distinct from the candidate-assessment sibling (role-agnostic loop, no execution-environment center), from the psychometric sibling (attribute instruments vs work products), from the ATS (measurement step vs pipeline), from interview operations, from education assessment (population/purpose), and — critically — from §12 software-testing Types that "test" systems rather than people. The joint-review flag with the two sibling leaves is discharged from this side: three Types, documented spectrum, product-level straddling acknowledged.
