# Research Notes — Candidate Assessment Platform

Research date: **2026-09-07**

## Research Goal

Understand the Application Type "Candidate Assessment Platform" (DIRECTORY §09 HR, Workforce & Talent): what the software actually is, who uses it, what core objects and workflows it has, and where its boundaries lie. Special obligations this pass:

1. Discharge this leaf's side of the joint-review flag recorded by the psychometric-assessment-platform pass (§09 siblings: candidate / technical / psychometric assessment — "one delivery mechanics, three leaves").
2. Record the structural test that separates this Type from the psychometric sibling (center of gravity: evaluation workflow vs instrument science).
3. Leave the technical-assessment-platform side of the seam recorded for that leaf's own pass.

## Initial Boundary (hypothesis before research)

- Hypothesis: employer-side software used during hiring to evaluate job candidates through standardized assessments (skills tests, work samples/simulations, cognitive/behavioral instruments, structured questions) and to turn results into comparable decision-support signals (scores, rankings, fit matches) feeding the hiring funnel.
- Closest confusions: Psychometric Assessment Platform (same delivery mechanics, different center), Technical Assessment Platform (coding pole), Assessment Platform §23 (education), ATS (pipeline owner), Interview Management / Video Interviewing, Survey Platform, Background Check Platform.
- Unknowns: whether per-role assessment composition is definitional or common; whether candidate ranking/shortlisting is definitional; how deep in-platform pipeline management goes (Criteria hinted at "manage your candidate pipeline"); whether custom test authoring is definitional (eSkill makes it first-class; Wonderlic claims "no customization necessary" — a philosophy split); automation depth (Harver auto-advance).

## Research Questions

1. What is the unit of work — the test, the assessment (bundle), the job/role configuration, or the candidate evaluation?
2. How is an assessment composed for a role (library selection, custom questions, pre-configured role packages, vendor-configured)?
3. How are candidates invited and how do they complete (link, ATS trigger, device, supervision)?
4. What does scoring produce (scores, percentiles, fit levels, rankings) and what comparison surfaces exist (shortlists, benchmarks, custom baselines)?
5. What roles exist (admin, recruiter, hiring manager, candidate) and what interfaces serve them?
6. What rules matter (same criteria for all takers, human-led decisions, integrity signals as context, fairness/compliance regimes, overrides)?
7. How does the platform integrate with the ATS (trigger-in / results-out)?
8. What adjacent modules are bundled (video interviews, resume scoring, reference checking, sourcing, development)?
9. Where are the boundaries vs psychometric / technical / education assessment, ATS, interviews, surveys, background checks?
10. Does the minimal core survive the paper-era historical check (pre-digital pre-employment testing)?

## Representative Products

| Product | Segment / philosophy | Documentation reached |
|---|---|---|
| TestGorilla | Self-serve SMB/mid-market; skills-forward library; assessment builder + ranked shortlist; integrity stack | Assessments product page + Job Simulations Library (Tier 1 product pages, deep) |
| Criteria Corp | Mid-market suite; science-forward (I/O psychology); Assess + Interview + Develop platform | Homepage + The Platform page (Tier 1 product pages, deep) |
| Harver | Enterprise volume hiring (BPO/contact center/retail); matching/profile-centric; services-led with People Science team | Homepage + Predictive Assessments page (Tier 1 product pages) |
| eSkill | Test-library + customization pole; broad industry coverage; anti-cheat suite | Homepage + platform feature navigation (Tier 1 product page) |
| Wonderlic | Heritage pole (vendor claims 85 years of science); out-of-the-box role-specific insights; Select/Develop split | Homepage + navigation (Tier 2, positioning-level) |

Market context only (not sampled this pass): **Vervoe** (work-sample/AI-graded job-simulation pole — www.vervoe.com transport error ×2, abandoned per network rule; zero claims), **SHL / Mercer \| Mettl** (psychometric sibling pass — straddle evidence carried from research/psychometric-assessment-platform.md), **HackerRank / Codility / CodeSignal** (technical pole — belongs to the technical-assessment-platform leaf), **The Predictive Index** (unreachable in the sibling pass).

## Sources

- TestGorilla — https://www.testgorilla.com/assessments/ ; https://www.testgorilla.com/job-simulations-library/ (fetched 2026-09-07)
- Criteria Corp — https://www.criteriacorp.com/ ; https://www.criteriacorp.com/platform (fetched 2026-09-07)
- Harver — https://harver.com/ ; https://harver.com/assessments/ (fetched 2026-09-07)
- eSkill — https://www.eskill.com/ (fetched 2026-09-07)
- Wonderlic — https://www.wonderlic.com/ (fetched 2026-09-07)
- Sibling research: research/psychometric-assessment-platform.md (joint-review flag + straddle evidence); research/assessment-platform.md (§23 education boundary language); research/recruitment-marketing-platform.md (apply-event seam)

Source-access limitation: no help-center-level operational articles were fetched this pass (TestGorilla's support portal timed out in the sibling pass; this pass used product/solution pages, which are unusually detailed for this market). All evidence is product-page level: Layer A for existence and structure of capabilities; no help-center-level workflow detail. Numeric claims observed (test counts, candidate volumes, duration ranges, outcome percentages) are vendor marketing figures and are kept as claims in these notes only — none are asserted as operational facts in the final document.

## Product Observations

### TestGorilla (Layer A — deepest workflow description in sample)

- Self-description: "A skills assessment is a structured step in your hiring process that measures what a candidate can actually do instead of relying on a resume or a first impression in an interview."
- **Assessment as composed bundle per role**: "TestGorilla combines skills tests, AI interviews, resume scoring, and identity verification into one assessment. Each one is scored against the same criteria, so you get one true picture of every candidate before you decide who to interview."
- Composition flow: create a job (company + role details) → AI builder recommends tests/questions based on job requirements → combine from library (vendor figure: 350+ tests across cognitive ability, communication, technical, role-specific skills, software, language, personality) → add custom questions in multiple formats → qualifying questions "that screen out anyone who misses a hard requirement early".
- Candidate flow: "candidates receive a direct link to their assessment with clear instructions for each step and question" — self-scheduled, remote, unsupervised by default; any-device; duration controlled by the employer (vendor figure: most assessments 10–45 minutes).
- Scoring: "Explainable scoring on every step... You see the result, you see how it was reached, and you can override it. Combined, you see one comparable score per candidate, and you walk into interviews with a ranked short list you can defend."
- Resume scoring: reads each resume against the job description, ranks on fit, "you can always override it to stay in complete control."
- Job simulation library (work-sample pole): "Browse realistic job scenarios scored on real performance" — e.g., Tech Collaboration Simulation, Customer Service Immersive Job Simulation, Spreadsheet Simulation (Google Sheets, "complex on-the-job tasks, completed live"), Conflict Handling for CS, B2B Account Management, Algorithmic Reasoning. Tagged "Real challenges to test job readiness."
- ATS integration: "Trigger assessments and see scores from inside your ATS, with results syncing to the candidate record automatically" (Greenhouse, Workable, Lever, Teamtailor named).
- Integrity ("Trust Layer"): ID verification (government ID + live selfie before starting), AI-assistant blocking, full-screen monitoring, copy-paste blocking, randomized question pools, timestamped behavior signals — "A flag is context, not a verdict... you decide what it means."
- Decision posture: "No remote test is completely tamper-proof — so instead of a single pass/fail verdict, you get the signals and make the call."
- Adjacent products: Sourcing (skills-tested talent profiles), AI interviews, resume scoring; candidate-side TestGorilla Profiles.
- Vendor figures (claims): 17.5M candidates assessed/year, 70M tests taken, 2-in-3 companies cut mis-hires.

### Criteria Corp (Layer A)

- Self-description (footer): "Web-based Pre-Employment Testing Software-as-a-Service (SaaS)". Positioning: "The Talent Signal Platform".
- Platform structure: **Assess** (Cognitive Aptitude CCAT, Personality, Emotional Intelligence, Risk, Skills, Game-Based, AI Proctoring) + **Interview** (Async Video, Real-Time Video, AI Interview Agent "coming soon", AI Scoring add-on) + **Develop** (Weekly Manager Check-ins, TEAMscan, Coach Bo).
- Platform mechanics (The Platform page):
  - Real-time results: "The moment a candidate completes the assessments, you can view the results in the platform or get the reports right in your email."
  - Score reports: "easy to understand... No need for hours of training to interpret a report."
  - Candidate pool comparison: "compare your candidates based on their scores. You can also establish custom baselines using results from your current workforce."
  - **In-platform pipeline management**: "Within our platform, you can send emails to your candidates, move them through the hiring pipeline, and even send them reminders to complete their assessments."
  - Reporting/analytics: hiring metrics, candidate feedback, recruiting efficiency.
  - Candidate experience: any device; candidate support team by phone/email; branded assessment experience (employer logo/branding).
- ATS/HRIS integrations: "seamlessly integrate assessments into your current systems and processes."
- Science posture: dedicated I/O psychology team + Scientific Advisory Board; "Every talent decision remains human-led"; ISO 42001 certified (vendor claim); MRAB © Harvard licensed instrument.
- Sales motion: free trial + demo; regional platform logins (HireSelect NA/SA/EU/Africa vs APAC app); Enterprise/Mid-Market/Small Business tiers.
- Vendor figures (claims): 80M+ assessments, 6B+ data points, 4,000+ organizations, 60 countries.

### Harver (Layer A)

- Self-description: "Talent Assessment Platform for Faster, Better Hiring"; "predictive assessments and matching".
- Center of gravity: **matching candidates to role profiles** — "Candidates are then matched in minutes to your ideal role profile, like a compatibility-based matchmaking system... instantly see who fits best."
- Assessment suite (450+ assessments vendor figure) organized by what is measured: Work Behavior (Traditional Behavioral, Gamified Behavioral/pymetrics), Work Ability (Cognitive, Realistic Job Previews), Work Knowledge & Skills (Job Knowledge & Skills, Language, Agent Simulation and Typing, Content Moderator), Remote Work & Preferences (Work From Home, Internet Speed, System Diagnostics, Availability & Location).
- Role profiles: "900+ ready-now job profiles or request a bespoke profile tailored to your unique hiring needs" — role-specific configurations by industry, job level, competencies.
- Process (homepage): Screen (job-relevant questions) → Automate ("Automatically prioritize qualified candidates to a virtual interview, reducing bias") → Assess → Analyze → Schedule → Hire.
- Automation: "customizable automation that progresses qualified candidates based on your criteria."
- Continuous-improvement loop (services-led): Assess → Select → Analyze → Adjust — "We optimize models to ensure continual improvement"; People Science team (30+ I-O psychologists, psychometricians, neuroscientists, data scientists) "continuously enhances your hiring process."
- Compliance posture: EEOC, UGESP, Int 1849, NYC LL-144 ("All employment decisions made using Harver's solutions are fully explainable and defensible"); debiasing methods; documentation for defensibility.
- Product family: AI PREVAIL, Harver for Volume Hiring, Harver Assess, Video Interview, pymetrics games, Checkster reference checking; Outmatch merged in.
- Segments: BPO/contact centers, retail, hospitality, financial services, healthcare, government/education — volume-hiring core.
- Vendor figures (claims): 100M+ candidates processed, ~40% time-to-hire reduction, up to 25% early-attrition decrease.

### eSkill (Layer A)

- Self-description: "the ai-powered assessment platform... Comprehensive tests for hiring. Hard skills, job ability, and behavioral fit. All put to the test."
- Library pole: "600+ subjects and 70,000 questions" (vendor figures); subject-based and job-based assessment search; industry coverage pages (manufacturing, government, healthcare, engineering, construction, utilities, financial services, transportation, education, staffing, call centers, hospitality, retail, legal).
- Assessment types: Skills, Cognitive, Behavioral, Personality, Aptitude, Job simulation.
- **Customization as first-class capability**: "Create pre-employment tests that perfectly align with your job roles and organizational goals. Mix and match questions, upload existing questions, or create them from scratch."
- Anti-cheat suite + AI-powered proctoring; One-Way Interviews module; Assessment Experts (consultation, analysis, refinement — services layer).
- Reporting: "Signal Map — see the skills that set your best hires apart"; "Skill Match — find the best fit, faster."
- AI layer: "Linea" intelligence layer ("Linea reports to you, not the other way around").
- Use-case evidence: government screening of large applicant pools (county government case study), English-proficiency compliance testing for truck drivers, tiered specialist role alignment.
- Client portal: "testcenter" login for assessment takers.

### Wonderlic (Layer A — positioning-level)

- Heritage pole: "From 85 years of proven science to the forefront of talent innovation" (history page) — paper-era pre-employment testing lineage, now a SaaS platform.
- Products: Wonderlic Select (hiring assessment: cognitive ability, personality, motivation insights) + Wonderlic Develop + Team Dynamics.
- **Out-of-the-box philosophy (counter-pole to eSkill)**: "role-specific insights. No one-size-fits-all, generic results. Our assessments predict on-the-job performance out of the box - no customization necessary."
- Ease posture: "The Wonderlic platform is easy to use for everyone in your organization - with no lengthy training or certification required" — while also selling Foundations Certification workshops (deepen assessment expertise).
- Candidate-facing: Candidate Hub (FAQ, how to prepare, practice tests); "Candidates... receive insights on the assessment results as a thank you for their participation."
- Staffing-agency evidence: Manpower among named customers — the Type serves staffing firms evaluating candidates for client placements, not only direct employers.
- Vendor figures (claims): customers include Allstate, Bosch, Delta, Nestlé.

### Cross-product Comparison

| Dimension | TestGorilla | Criteria | Harver | eSkill | Wonderlic |
|---|---|---|---|---|---|
| Employer-side operation for own hiring | Yes | Yes | Yes (+ staffing/BPO) | Yes (+ staffing/government) | Yes (+ staffing: Manpower) |
| Assessment bound to a role/hiring evaluation | Per-role assessment builder | Tests by position/industry + baselines | 900+ ready-now job profiles + bespoke | Job-based + subject-based tests; custom tests | Out-of-the-box role-specific insights |
| Standardized same-criteria scoring | "scored against the same criteria" | Same test, comparable scores | Validated assessments, matching | Objective, data-driven scoring | Fixed scoring (heritage instruments) |
| Comparable per-candidate results | One comparable score + ranked shortlist | Score reports + candidate-pool comparison | Fit match vs role profile | Scores + Signal Map/Skill Match | Role-specific score insights |
| Library of standardized instruments | 350+ tests (claim) + simulations | Multi-family (cognitive/personality/EI/risk/skills/game) | 450+ assessments (claim), 4 measurement categories | 600+ subjects / 70,000 questions (claim) | Cognitive/personality/motivation instruments |
| Custom content authoring | Custom + qualifying questions | Not emphasized on fetched pages | Bespoke profiles (vendor-configured) | First-class (mix/match, upload, create) | Explicitly "no customization necessary" |
| Remote unsupervised completion via link | Core flow | Yes (any device) | Yes (mobile-friendly, engaging) | Yes | Yes |
| Integrity/anti-cheat machinery | Trust Layer (ID verification, signals) | AI Proctoring module | Not observed on fetched pages | Anti-cheat suite + AI proctoring | Not observed |
| ATS integration | Trigger + score sync (named ATSs) | Yes (ATS/HRIS partners) | Yes (integrations page) | Yes (integrations page) | Not observed on fetched pages |
| In-platform candidate pipeline management | Not observed (ATS-hosted) | Yes (emails, move through pipeline, reminders) | Yes (screen→automate→assess→schedule→hire) | Not observed | Not observed |
| Automation of candidate progression | Not observed | Not observed | Yes (auto-prioritize/auto-advance by criteria) | Not observed | Not observed |
| Video/one-way interviews bundled | AI interviews | Interview module (async/real-time + AI scoring) | Video Interview product | One-Way Interviews | Not observed |
| Resume scoring bundled | Yes | Not observed | Not observed | Not observed | Not observed |
| Human makes the decision | "you get the signals and make the call" | "Every talent decision remains human-led" | "fully explainable and defensible" decisions | Decision-support framing | Decision-support framing |
| Fairness/compliance apparatus | EEOC/UGESP/SIOP framing (sibling pass) | Science team + advisory board | EEOC/UGESP/NYC LL-144/Int 1849 + debiasing | Validated content + trust center | Legal & regulatory page |
| Development-side reuse | Not emphasized | Develop module | Talent Development use case | Not observed | Wonderlic Develop |
| Services layer | Self-serve | Demo + support | People Science team (services-led) | Assessment Experts | Certification workshops |
| Customer tier / motion | Free plan, self-serve SMB | Free trial, mid-market tiers | Enterprise sales-led, volume hiring | Sales-led, mid-market/enterprise/government | Sales-led, broad |

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **Employer-side operation for hiring decisions** — operated by the hiring organization (or a staffing firm acting for employers) to evaluate candidates for its own employment decisions; candidates are the measured population, never the operators.
2. **Standardized assessment administered to identified candidates** — each candidate for a given evaluation receives the same standardized instrument(s)/criteria (selected or composed for that hiring evaluation), delivered as a completable assessment.
3. **Standardized scoring producing comparable per-candidate results** — responses are evaluated by the same fixed scoring for every taker, yielding per-candidate results that are comparable across the candidate pool.
4. **Decision-support consumption in the hiring funnel** — results surface as comparisons (scores, rankings, fit levels) that the employer uses to decide which candidates advance — the platform supports, never makes, the decision.

Remove #1 → education assessment or consumer testing. Remove #2–3 → unstructured resume review/interviewing (no standardized measurement). Remove #4 → a testing/quiz tool with no hiring purpose.

Historical check (§24): paper-era pre-employment testing — employment-agency typing/shorthand tests, trade tests, hand-scored cognitive tests scored against printed norm tables (Wonderlic's claimed 85-year lineage) — satisfies 1–4 with zero digital machinery: employer-side, standardized instrument, fixed scoring, results deciding who advances. Government civil-service examinations and staffing-agency testing fit the same loop. The modern SaaS layer (ATS integration, remote link delivery, integrity machinery, AI scoring, auto-advance automation) is all L1/L2 — none of it is required for the Type to be recognizable.

### L1 — Common Mature Structure

- **Standardized assessment library** spanning multiple families: job-specific skills, cognitive/aptitude, personality/behavioral, situational judgment, language, typing/office skills, job simulations/work samples.
- **Per-role assessment configuration**: composing an assessment for a role from library tests + custom/qualifying questions (builder pattern), or selecting pre-configured role packages/job profiles, or vendor-configured bespoke profiles.
- **Candidate invitation + remote unsupervised completion**: direct link delivery (often triggered from the ATS on application), any-device completion, clear instructions.
- **Auto-scoring with per-candidate result reports**: immediate results, explainable scores, employer-readable reports.
- **Candidate comparison surfaces**: ranked shortlists, side-by-side comparisons, benchmarks/custom baselines (including baselines from the employer's own workforce).
- **ATS integration**: trigger assessments from the ATS; scores sync automatically to the candidate record.
- **Integrity machinery for unsupervised remote completion**: browser/device checks, behavior signals, question randomization; ID verification/camera/proctoring in some products.
- **Admin console with roles**: admin, recruiter/user, hiring-manager viewer; candidate support channels.
- **Candidate-facing experience**: instructions, practice/preparation resources, support, feedback results.
- **Reporting/analytics**: funnel metrics, candidate feedback, hiring efficiency.
- **Fairness/compliance apparatus**: validated content claims, adverse-impact/fairness monitoring, explainability documentation, regime alignment (EEOC/UGESP, NYC LL-144-class, GDPR).

### L2 — Variant / Optional Structure

- **Content emphasis**: skills-forward library vs science/psychometrics-forward portfolio vs simulation/work-sample forward vs matching/profile-centric.
- **Composition philosophy**: self-serve builder with custom authoring (eSkill pole) vs out-of-the-box role insights with no customization (Wonderlic pole) vs vendor-configured bespoke profiles (Harver pole).
- **Customer tier and sales motion**: free-tier self-serve SMB vs enterprise sales-led with embedded People Science services.
- **Segment machinery**: volume hiring (BPO/contact center/retail/hourly), campus/graduate hiring, government large-pool screening, staffing agencies.
- **Automation depth**: score-based auto-advance/auto-prioritization rules (observed in Harver); in-platform pipeline management (observed in Criteria, Harver).
- **Adjacent bundled modules**: video/one-way interviews (with AI scoring), resume scoring, reference checking, sourcing/talent pools, development modules (reuse of instruments for employee development).
- **AI posture**: AI scoring of open-ended/video responses against rubrics, AI proctoring, AI assessment builders, AI interviews, AI intelligence layers.
- **Benchmarking posture**: vendor norms vs employer custom baselines.
- **Compliance regimes**: US selection-procedure guidelines, AI-transparency regimes (NYC LL-144-class), EU data protection, AI management-system certification (vendor claims).

### L3 — Vendor-specific (Research Notes only)

- TestGorilla: Trust Layer specifics (honesty agreement, AI-agent blocking, integrity tiers, timestamped signals); AI interviews + resume scoring + Sourcing + candidate Profiles products; "350+ tests / 17.5M candidates a year / 70M tests taken" claims; 10–45-minute duration guidance; named ATSs (Greenhouse, Workable, Lever, Teamtailor).
- Criteria: HireSelect platform + regional logins (NA/SA/EU/Africa vs APAC); CCAT; MRAB © Harvard license; On-Demand Assessment trademark; Develop module (Coach Bo, TEAMscan, check-ins); AI Interview Agent "coming soon"; ISO 42001 claim; "80M+ assessments / 6B+ data points / 4,000+ organizations" claims.
- Harver: pymetrics game-based assessments; Checkster reference checking; Outmatch merger; AI PREVAIL; "450+ assessments / 900+ job profiles / 100M+ candidates" claims; People Science team (30+ scientists); Assess→Select→Analyze→Adjust service loop; NYC LL-144 / Int 1849 compliance claims; outcome stats (40% time-to-hire, 25% attrition).
- eSkill: "600+ subjects / 70,000 questions" claims; Linea AI layer; Signal Map / Skill Match reporting names; One-Way Interviews; Assessment Experts service; testcenter portal; industry page lattice (14 industries); case studies (county government, English-proficiency compliance, wind-specialist tiers).
- Wonderlic: "85 years" heritage claim; Select/Develop/Team Dynamics product split; Foundations Certification; out-of-the-box/no-customization positioning; Manpower customer evidence; candidate feedback reports ("as a thank you").
- Vervoe: unreachable — work-sample/AI-graded simulation pole as market context only, zero claims.

## Rejected Findings

- **"Candidate assessment platform = psychometric testing platform"** — rejected as identity. Same delivery mechanics, different center of gravity: psychometric products center vendor-owned normed psychological instruments with norm-anchored interpretation (science-house posture, selection + development reuse, often consultant-delivered); candidate assessment products center the per-role evaluation workflow in the hiring funnel (compose → deliver → score → compare → advance). The market straddles deliberately (TestGorilla, Criteria, Harver all include psychometric families; SHL/Mettl sell skills families) — the leaves separate centers, not feature sets. See Boundary Findings.
- **"The platform decides who to hire"** — rejected: every sampled product frames human-led decisions (TestGorilla "you get the signals and make the call"; Criteria "Every talent decision remains human-led"; Harver "fully explainable and defensible"). Auto-advance automation (Harver) progresses candidates by employer-configured criteria but the hire decision stays human.
- **"It's just online quizzes"** — rejected: standardized scoring, role-fit machinery, comparability guarantees, integrity apparatus, and compliance documentation distinguish the Type from quiz/survey tools.
- **"Coding tests are the core"** — rejected: only one segment of the market; the sampled Type spans all job families (eSkill's 14 industries; TestGorilla "Any role, not just technical ones"). The coding-measurement environment center belongs to the Technical Assessment Platform sibling.
- **"Video interviews are definitional"** — rejected: video/one-way interviewing appears in-sample only as a bundled adjacent module (Criteria Interview, eSkill One-Way Interviews, Harver Video Interview, TestGorilla AI interviews); Wonderlic shows the Type works without it.
- **"Custom test authoring is definitional"** — rejected: eSkill makes it first-class while Wonderlic explicitly positions "no customization necessary" — a philosophy split, not the core. What is common is *configuration for the role* (select/compose/adopt), not authorship.
- **"Integrity/proctoring is definitional"** — rejected: ranges from none/lightweight (Wonderlic, Harver pages) to dedicated suites (TestGorilla Trust Layer, eSkill anti-cheat); scales with stakes and segment.
- **"In-platform pipeline management is definitional"** — rejected: only Criteria (lightweight: emails, reminders, move through pipeline) and Harver (automation-centered) show it; TestGorilla/eSkill defer pipeline ownership to the ATS. It is an optional depth, not the core.

## Boundary Findings

- **vs Psychometric Assessment Platform (§09 sibling, processed — joint-review flag)**: the recorded seam holds and is now documented from this side. Psychometric centers **what is measured and how interpreted**: vendor-owned normed psychological instruments, reference-anchored interpretation (norms/competency profiles), science-house posture, selection + development reuse, often consultant-delivered (Hogan has no assessment builder and no candidate ranking at all). Candidate assessment centers **the evaluation workflow**: per-role assessment configuration, applicant delivery, standardized scoring, candidate comparison/advancement in the funnel. Structural test: remove the per-role composition + candidate comparison/advancement workflow and keep normed instruments with norm-anchored interpretation → psychometric platform; remove the instrument-science center and keep the role-scoped evaluation loop → candidate assessment platform. Market straddling is real and deliberate (TestGorilla/Criteria/Harver include psychometric families; SHL/Mettl include skills families) — the joint-review question (three leaves vs spectrum/consolidation) remains open for joint review; this pass adds the candidate side's structural test.
- **vs Technical Assessment Platform (§09 sibling, unprocessed)**: the coding/technical pole — products centered on a technical measurement environment (code execution sandboxes, playback, plagiarism detection) for technical roles. Candidate assessment is role-agnostic across job families. Left for that leaf's pass; flagged.
- **vs Assessment Platform (§23 education, processed)**: different population (applicants/candidates vs students), different purpose (selection vs learning/certification), different instrument ownership (vendor library + employer configuration vs educator-authored scored tests). Consistent with the education pass's recorded boundary ("same mechanics, different population and purpose").
- **vs ATS**: the ATS owns requisition/pipeline/candidate records; the assessment platform is the measurement step integrated into it (trigger-in/results-out). Criteria's in-platform pipeline management is a convenience layer for the assessment workflow, not a pipeline system of record; TestGorilla explicitly hosts the loop inside the customer's ATS.
- **vs Interview Management Platform / Video Interviewing**: recorded interview answers for human review vs standardized scored instruments; video interviewing appears in-sample only as a bundled module. Structured interview guides with scorecards (Interview Management) are human-judgment capture, not standardized instrument scoring.
- **vs Background Check Platform / Employment Verification Platform (§09)**: verification of factual records vs measurement of capability/fit; different object entirely (consistent with sibling passes).
- **vs Survey Platform / Employee Survey Platform**: opinions with aggregate reporting and no correct answers vs standardized scored evaluation of identified individuals with per-person comparable results.
- **vs Recruitment Marketing Platform (§09, processed)**: pre-application attraction vs in-funnel evaluation; the seam sits at the application/assessment trigger (RMP hands off at apply; assessment begins once candidates are in the funnel).
- **vs Employee development/assessment reuse**: instruments reused for development (Wonderlic Develop, Criteria Develop, Harver talent development) — the defining population remains candidates in hiring; development-side reuse is a variant, and deep development-centering belongs to the psychometric sibling's recorded territory.
- **Boundary test (remove-what-to-become-another-Type)**: remove employer-side hiring purpose → education/consumer testing; remove standardized scoring → unstructured interviews/resume review; remove the assessment instrument and keep requisition/pipeline → ATS; remove scoring keys and keep question delivery → survey; narrow the environment to code execution → Technical Assessment Platform; recenter on normed psychological instruments + norm-anchored interpretation → Psychometric Assessment Platform.

## Uncertainties

- No help-center-level operational documentation was fetched this pass; all mechanics are product-page level. The final document deliberately avoids precise numbers (test counts, durations, retention windows, outcome percentages) — vendor figures stay here as claims.
- Exact scoring implementations (IRT vs classical, cut-score tooling, norm construction) were not directly observed; described qualitatively.
- Wonderlic evidence is positioning-level; its in-product workflow mechanics are kept general.
- Harver's integrity machinery was not observed on fetched pages — kept hedged (likely exists given volume-hiring stakes, but no evidence taken).
- Whether the directory should hold Candidate / Technical / Psychometric Assessment Platform as three leaves or fold them into one talent-assessment spectrum remains unresolved — joint-review flag stands; this pass records the candidate side's structural test and the market-straddle evidence.
- Criteria's in-platform pipeline depth (beyond emails/reminders/move) unknown — kept as "lightweight convenience layer" without further claims.
- Accommodations/accessibility depth not directly observed this pass (sibling pass observed SHL's Neurodiversity Hub only) — kept hedged.

## Final Synthesis

A Candidate Assessment Platform is the hiring funnel's measurement step: an employer (or staffing firm acting for employers) configures standardized assessments for a role — composed from a vendor library plus custom content, or adopted as pre-configured role packages — delivers them to identified candidates (usually via link, often triggered from the ATS), scores every candidate against the same criteria, and consumes the results as comparable decision-support signals (scores, rankings, fit matches) that decide who advances — with the hire decision remaining human. Around that loop, mature products add multi-family instrument libraries, candidate comparison surfaces with benchmarks, ATS integration, integrity machinery for unsupervised remote completion, candidate-facing experience, reporting/analytics, and fairness/compliance apparatus; variants span content emphasis (skills vs psychometric vs simulation vs matching), composition philosophy (self-serve authoring vs out-of-the-box vs vendor-configured), customer tier (self-serve SMB vs enterprise services-led), segment machinery (volume hiring, government pools, staffing), automation depth, and adjacent modules (video interviews, resume scoring, reference checking, development reuse). The Type is distinct from the psychometric sibling (evaluation workflow vs instrument science), from the technical sibling (role-agnostic vs coding-environment-centered), from education assessment (population and purpose), from the ATS (measurement step vs pipeline owner), from interviews (standardized scoring vs recorded human judgment), and from surveys (scored evaluation vs opinion gathering).
