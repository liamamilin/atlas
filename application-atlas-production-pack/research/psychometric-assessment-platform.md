# Research Notes — Psychometric Assessment Platform

Research date: **2026-09-06**

## Research Goal

Understand the Application Type "Psychometric Assessment Platform" (DIRECTORY §09 HR, Workforce & Talent): what the software actually is, who uses it, what core objects and workflows it has, and where its boundaries lie against the neighboring §09 leaves (Candidate Assessment Platform, Technical Assessment Platform) and the already-processed Assessment Platform (§23 education), plus survey, background-check and ATS neighbors.

## Initial Boundary (hypothesis before research)

- Hypothesis: this is hiring-side measurement software built around **standardized psychological measurement instruments** (cognitive ability, personality, motivation/values, behavioral tendencies) rather than job-skill tests, delivered to candidates and scored against norms to support selection/development decisions.
- Closest confusions: skills/coding testing platforms (Candidate/Technical Assessment), general education assessment platforms, survey platforms, ATS.
- Unknowns: exact scoring/norm mechanics per product, ATS integration direction, integrity machinery, role model, whether decision-making is delegated to the platform.

## Research Questions

1. What instrument families exist (ability/cognitive, personality, motivation/values, SJT/behavioral, skills)? How are they described?
2. How is an assessment administered to a candidate (invite, link, ATS trigger, completion surface)?
3. How is scoring standardized (keys, norms, percentiles, benchmarks, profile/fit matching)? What does each side see?
4. What roles exist (admin, recruiter, hiring manager, trained test user, candidate) and what interfaces serve them?
5. What is the lifecycle of an assessment (order/invite → completion → score → report → decision support)?
6. What rules matter (fairness/adverse impact, standards compliance, candidate rights, integrity/anti-cheating, accommodations, retest)?
7. How are results consumed (ranking, interview guides, development planning, reuse across the talent journey)?
8. How does the platform integrate with ATS/HRIS?
9. Where are the boundaries vs skills/technical assessment, education assessment, surveys, background checks?

## Representative Products

| Product | Segment / philosophy | Documentation reached |
|---|---|---|
| SHL | Enterprise; full psychometric-science house + platform; assessment used across talent acquisition AND talent management | Product portfolio + OPQ product page (Tier 2) |
| Mercer \| Mettl | Broad assessment platform with an explicit "Psychometric Assessments" family; multi-region norming; proctoring suite | Psychometric tests page + site structure (Tier 2) |
| TestGorilla | SMB/self-serve; skills-forward library that includes cognitive ability + personality; modern integrity stack | Product pages + science/technology page (Tier 2, deep) |
| Hogan Assessments | Personality-only science pole; consultant/coach-delivered interpretation | Homepage + navigation (Tier 2, positioning-level) |
| Criteria Corp | Mid-market; cognitive/personality/EI/risk/skills/game-based suite + interviews + development | Homepage + full navigation (Tier 2, positioning-level) |

Market anchor only (unreachable): **The Predictive Index** (behavioral+cognitive mid-market pole — help center 530, main site 403; no claims taken). Thomas International abandoned after 403.

## Sources

- SHL — https://www.shl.com/solutions/products/ ; https://www.shl.com/products/assessments/personality-assessment/shl-occupational-personality-questionnaire-opq/ (fetched 2026-09-06)
- Mercer | Mettl — https://www.mettl.com/ ; https://www.mettl.com/psychometric-tests/ (fetched 2026-09-06)
- TestGorilla — https://www.testgorilla.com/ ; https://www.testgorilla.com/assessments/ ; https://www.testgorilla.com/science/ (fetched 2026-09-06)
- Hogan Assessments — https://www.hoganassessments.com/ (fetched 2026-09-06)
- Criteria Corp — https://www.criteriacorp.com/ (fetched 2026-09-06)
- Sibling research: research/assessment-platform.md (§23 education assessment; boundary language reused for consistency)
- Unreachable: help.predictiveindex.com (530) + predictiveindex.com (403) ×1 each; support.testgorilla.com/hc/en-gb (timeout); thomas.co (403); SHL support portal sub-pages not fetched.

Source-access limitation: no help-center-level operational articles were reachable for any sampled product. All evidence is product/solution-page level (Layer A for existence and structure of capabilities; no help-center detail). Numeric claims observed (test counts, durations, language counts, client counts, retention windows) are vendor marketing figures and are kept as claims in these notes only — none are asserted as operational facts in the final document.

## Product Observations

### SHL (Layer A unless noted)

- Portfolio families: Behavioral Assessments, Cognitive Assessments (SHL Verify), Personality Assessments (OPQ — Occupational Personality Questionnaire), Motivational Questionnaire (MQ), Situational Judgment Tests (SJT), Job-Focused Assessments (JFA), Global Skills Assessment, Skills & Simulations (coding, call center, business skills, technical, language), plus Video Interviews, 360 Feedback, Video Feedback.
- OPQ mechanics (product page): participants answer questions about working preferences → strengths/development areas mapped within the Universal Competency Framework (UCF) → "profile matching" against a scientifically chosen target profile for hiring or development needs → hiring managers receive a report on fit, potential, development gaps; integrated with ATS.
- Reusability: "reusable OPQ test data informs hiring decisions and long-term initiatives like high-potential programs and development planning"; "assess talent once" posture across the talent journey.
- Solutions span Talent Acquisition (graduate, manager, tech, professional, volume/BPO/contact-center hiring) and Talent Management (succession, leader development, HiPo, mobility) — i.e., the same instruments serve selection AND development.
- Services: Managed Services, Training Services, **SHL Certification (OPQ/Verify)** — test-user qualification training; Outsourced Assessments (virtual assessment & development centers).
- Candidate-side surfaces: Practice tests (SHL Direct), Candidate Support, Browser Check, Neurodiversity Hub (accommodations-adjacent resource).
- ATS integrations: "over 80 of the most popular ATS platforms" (vendor figure), Workday and SmartRecruiters named.
- Self-serve purchasing exists ("Buy Online"/SHL Online) alongside enterprise sales.

### Mercer | Mettl (Layer A)

- Explicit product family: **Psychometric Assessments** under "Online Assessment Tools" (pre-employment assessment tools to hire and develop talent), with siblings Aptitude, Technical, Communication Skills, Sales — i.e., psychometric is one family inside a broader assessment platform.
- Definition stated on the psychometric page: "Psychometric tests objectively measure personality traits, cognitive abilities, and behavioral tendencies to determine an individual's suitability for a role."
- Instrument families listed: Personality assessments (e.g., Personality Map, Mercer | Mettl Personality Inventory — MPI), Motivations and values (Motivation Inventory), Aptitude assessments (problem-solving, critical thinking, learning agility), Behavioral assessments (leadership potential, teamwork, decision-making).
- Science pillars (named on page): **Norming** ("assessments are normed on a large sample of respondents drawn from different geographies — India, USA, Europe, Latin America, Middle East, South Africa, South-East Asia — representative of age groups, genders, job levels, occupations and industries"), **Validity and reliability**, **Standardization** ("every aspect of the test, from development to interpretation, is in line with global practices... international testing standards... fairness"), **Scoring** ("data-driven, interpretable scores... strengths and suitability for a role or career path"), **Instruments** ("globally recognized psychological models"), **Methodology** ("extensive research, statistical validation, expert reviews").
- Use cases: graduate hiring (cognitive + behavioral + learning agility), sales hiring (MPI), assessment batteries combining psychometric + cognitive + SJT "with an external assessor".
- Platform breadth: separate examination/proctoring products (SecureProctor, Mettl Secure Browser, Proctoring as a Service), coding assessments, campus/lateral hiring, 360 feedback, HiPo identification — the psychometric family is embedded in a large assessment ecosystem.

### TestGorilla (Layer A — deepest operational description in sample)

- Assessment composition: skills tests + AI interviews + resume scoring + custom/qualifying questions (+ optional ID verification) combined into one assessment per role; one comparable score per candidate; explainable scoring with visible reasoning; recruiters can override.
- Library spans cognitive ability, communication, technical, role-specific skills, software, language, personality (vendor figure: 350+ tests).
- Candidate flow: "candidates receive a direct link to their assessment with clear instructions for each step and question" — self-scheduled, remote, unsupervised by default.
- Scoring science (technology page): tests built on precise skill definitions grounded in O*NET/ESCO frameworks; 5-stage development (define → build with SMEs → independent verification → calibrate difficulty via modified Angoff method and/or live data → continuous monitoring); item-drawing algorithm builds unique, difficulty-balanced test instances; **percentile scores reported against calibrated global norms**; ongoing psychometric analyses of reliability, content/construct/criterion validity; demographic fairness checks (group differences, differential item functioning, adverse impact); results published in per-test fact sheets.
- Integrity ("Trust Layer"): honesty agreement, AI browser agents blocked, behavior monitoring (full-screen exits, tab switches, copy-paste, tampering), optional camera snapshots and ID verification; signals roll into integrity tiers — "a flag is context, not a verdict... a human always makes the final call".
- Standards/compliance: EEOC Uniform Guidelines (UGESP), SIOP Principles, Standards for Educational and Psychological Testing; GDPR; SOC 2 Type II; EU AI Act preparation; data-retention windows stated (media 6 months, PII 24 months — vendor figures).
- ATS integration: trigger assessments from ATS (Greenhouse, Workable, Lever, Teamtailor named); scores sync automatically to the candidate record.
- AI posture: AI scores open-ended responses against structured rubrics calibrated to expert scorers; bias/adverse-impact tested; "AI never makes a hiring decision".

### Hogan Assessments (Layer A — positioning-level)

- Personality-only science pole: "measuring the bright side, dark side, and inside of personality" (its three flagship instruments HPI/HDS/MVPI are named elsewhere on the site but not fetched here); "predictive validity" claims; scores shown as interactive dimension sliders with interpretations.
- Talent Acquisition + Talent Development dual use; "strategic self-awareness" language for development.
- Delivery posture: consultant/coach-mediated (Hogan Coaching Network) + certification workshops for users; global scale claims (14M+ assessments, 190 countries, 50 languages — vendor figures).
- Industry-vertical solution pages (banking, healthcare, government...) with outcome stats (vendor claims).

### Criteria Corp (Layer A — positioning-level)

- Assess suite: Cognitive Aptitude (CCAT), Personality, Emotional Intelligence, Risk, Skills, Game-Based, plus AI Proctoring as a separate module.
- Adjacent modules: video interviewing (async/real-time) with AI Scoring add-on; Develop (manager check-ins, team scan, coaching bot).
- "On-Demand Assessment" SaaS trademark; separate regional platform logins; free trial + demo sales motion; Enterprise / Mid-Market / Small Business tiering.
- Candidate-facing resources: candidate resource hub, practice tests, FAQs ("About the assessments", CCAT prep).
- Science: dedicated I/O psychology team + Scientific Advisory Board; "80M+ assessments, 6B+ data points" (vendor figures); licensed instrument (MRAB © Harvard) — evidence that proprietary/licensed instrument content is the product.
- AI posture: "every talent decision remains human-led"; ISO 42001 certified (vendor claim).

### Cross-product Comparison

| Dimension | SHL | Mettl | TestGorilla | Hogan | Criteria |
|---|---|---|---|---|---|
| Instrument library spanning ability+personality+motivation/SJT | Yes (OPQ/Verify/MQ/SJT/JFA) | Yes (personality/MPI/Motivation Inventory/aptitude/behavioral) | Yes (cognitive/personality within skills library) | Personality only (3 instruments) | Yes (cognitive/personality/EI/risk/game-based) |
| Psychometric development methodology claimed | Yes (UCF, 40+ years data) | Yes (norming/validity/standardization/methodology pillars) | Yes (5-stage process, Angoff calibration, continuous monitoring) | Yes (research program, predictive validity) | Yes (I/O team, advisory board) |
| Norm/reference-anchored interpretation | Profile matching to competency framework | Multi-region norm groups; interpretable scores | Percentiles vs calibrated global norms | Dimension scores + interpretation guidance | Scores + benchmark reports (positioning) |
| Candidate self-serve remote completion via link | Yes | Yes | Yes (core flow) | Via assessment link (positioning) | Yes (positioning) |
| Job/role-fit mapping machinery | Target profiles vs UCF | Role suitability use cases | Role-based assessment builder (AI-recommended tools) | Role/industry solutions | Tests by position/industry |
| Recruiter-facing reports (fit/ranking/interview support) | Fit/potential/gap report to hiring managers | Data-driven reports; visual interpretation | Ranked shortlist, explainable scores, overrides | Consultant/coach-delivered reports | Score reports (positioning) |
| Candidate feedback reports | Candidate feedback screens (OPQ) | Implied (development use) | Candidate instructions/results experience | "Strategic self-awareness" feedback | Candidate prep resources |
| ATS integration | Yes (80+ claim) | Yes (hiring platform posture) | Yes (trigger + score sync, named ATSs) | Not observed | Not observed on fetched pages (integrations page exists) |
| Integrity/anti-cheating machinery | Browser check; candidate support | Secure browser + proctoring suite (separate products) | Trust Layer (behavior signals, ID verification, integrity tiers) | Not observed | AI Proctoring module |
| Human makes final decision | Decision-support framing | "informed hiring decisions" | "AI never makes a hiring decision" | Coach-delivered | "human-led" |
| Reuse beyond hiring (development) | Explicit (hipo/development/succession) | Explicit (L&D tools, HiPo) | Not emphasized | Explicit (development pole) | Explicit (Develop module) |
| Test-user certification/training | SHL Certification (OPQ/Verify) | Not observed | Not observed | Certification workshops | Not observed |
| Self-serve free/trial entry | Buy Online | Not observed (sales-led) | Free plan | Sales-led | Free trial |

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **Vendor-maintained standardized measurement instrument(s)** targeting defined psychological attributes of people (cognitive ability/aptitude, personality traits, motivation/values, behavioral tendencies or judgment) — the instrument is developed, owned and maintained by the assessment vendor as product content, under a claimed development methodology (construct definition, validation, fairness analysis).
2. **Administration to an identified individual** (candidate or employee) being evaluated for a work-related decision — invitation/delivery surface plus completion experience.
3. **Standardized scoring** — responses are evaluated by the same fixed key/scoring model for every taker, producing a per-individual result.
4. **Reference-anchored interpretation** — the result is expressed against a reference frame (norm groups, benchmark/competency profiles, fit mappings) that makes it comparable across individuals.
5. **Decision support for selection or development** — results surface as reports/rankings/profiles consumed by the employing organization to support (never autonomously make) hiring or development decisions.

Remove #1–2 and it is not an assessment product at all; remove standardized scoring/reference anchoring (#3–4) and it is a survey/quiz; remove the work-decision purpose (#5) and it drifts to consumer/clinical territory.

Historical check: paper-era occupational psychometrics (publisher-owned tests, trained users scoring against printed norm tables) satisfy 1–5 without any digital platform; the software platform digitizes administration and scoring. Era/regional/platform-native products fit; no L0 item is an artifact of the current SaaS generation.

### L1 — Common Mature Structure

- Instrument catalog spanning multiple attribute families (cognitive/aptitude, personality, motivation/values, situational judgment/behavioral competencies; skills/simulations adjacent).
- Candidate invitation flow (email/link, often triggered from an ATS), self-scheduled remote completion, web/mobile delivery.
- Job/role-fit machinery: competency frameworks, target profiles, benchmarks, role-based assessment templates/builder.
- Recruiter/hiring-manager-facing result reporting: fit/summary scores, rankings/shortlists, profile detail, interview-guide support.
- Candidate-facing instructions, practice resources, feedback reports; support channels; accessibility/accommodation resources.
- ATS integration (trigger assessment from ATS; results sync to candidate record).
- Integrity machinery for unsupervised remote completion (browser/device checks, behavior signals, question rotation; ID verification/camera in some products).
- Admin console with roles (admin, recruiter/user, hiring-manager viewer; sometimes certified/trained test-user designation).
- Scientific documentation layer (fact sheets, validity/reliability statements, norm documentation).

### L2 — Variant / Optional Structure

- Attribute-family emphasis: personality-only science houses vs broad multi-family portfolios vs skills-forward libraries that include psychometric tests.
- Interpretation/delivery posture: platform self-serve vs consultant/coach-delivered reports; test-user certification.
- Customer tier and sales motion: enterprise solutions vs SMB free-tier self-serve.
- Norm regionalization (multi-geography norm samples vs global norms).
- Reuse across the talent journey (assess once; reuse for HiPo, succession, development planning) vs hiring-only use.
- Adjacent bundling: video interviews, 360 feedback, simulations/job simulations, proctoring products, development modules.
- AI-assisted scoring (rubric-based AI scoring of open-ended/video responses) and AI proctoring; game-based formats.
- Segment machinery: graduate/campus hiring, volume/BPO hiring, industry-vertical solution packs.
- Compliance regime emphasis (US selection-procedure guidelines, EU data protection/AI regulation).

### L3 — Vendor-specific (Research Notes only)

- SHL: OPQ/Verify/MQ/GSA/JFA product names; UCF framework; "37 languages / 20 minutes / 10M assessments a year / 80+ ATS integrations" vendor figures; SHL Certification; VADC; Sheldon chatbot; SHL Online.
- Mettl: MPI, Personality Map, Motivation Inventory; norm-geography list; SecureProctor / Mettl Secure Browser / MPaaS; 6000+ clients / 150K+ questions vendor figures.
- TestGorilla: Trust Layer specifics (honesty agreement, AI-agent blocking, integrity tiers); Angoff calibration and item-drawing algorithm claims; per-test fact sheets; "350+ tests"; 6/24-month data-retention figures; named ATSs.
- Hogan: bright-side/dark-side/inside framing (HPI/HDS/MVPI); Coaching Network; certification workshops; bookstore; Fortune-500 and outcome stats.
- Criteria: CCAT/EPP; MRAB Harvard license; On-Demand Assessment trademark; HireSelect regional logins; ISO 42001 claim; Coach Bo/TEAMscan.
- Predictive Index: unreachable — behavioral/cognitive pole as market context only, zero claims.

## Rejected Findings

- "Psychometric platforms are generic quiz builders" — rejected: the sampled products uniformly claim standardized development methodology, validation, fairness monitoring and norm-based scoring; authoring-your-own-instrument is not the center (authoring exists for custom questions, not for the normed instruments).
- "They always include skills/coding tests" — rejected: Hogan has none; skills/simulations appear as adjacent families (SHL, Mettl, TestGorilla, Criteria) pointing at the Candidate/Technical Assessment sibling types.
- "The platform decides who to hire" — rejected: every sampled product frames the platform as decision support (TestGorilla "AI never makes a hiring decision"; Criteria "human-led"); automated decision is explicitly disclaimed.
- "Psychometric assessment = education assessment" — rejected: different population, purpose, and instrument ownership (vendor-published normed instruments vs author-built scored tests for learning) — consistent with the boundary recorded in research/assessment-platform.md.
- "Personality tests here are consumer-style quizzes" — rejected: scientific development, norming, fairness monitoring and use in employment decisions distinguish them; consumer-quiz form factor without the measurement apparatus is not this Type.
- "Proctoring is definitional" — rejected: integrity machinery ranges from none/lightweight to dedicated secure-browser products; it scales with stakes and product line.

## Boundary Findings

- **vs Candidate Assessment Platform (§09 sibling, unprocessed — joint-review flag)**: same delivery mechanics; the seam is what is measured and how it is interpreted. Psychometric platforms center attribute measurement (who someone is / their capacity) with norm-referenced, scientifically validated instruments; candidate assessment platforms center job-skill/work-sample demonstration. The sample straddles deliberately (TestGorilla, Mettl, Criteria sell both) — whether these leaves are distinct Types or a spectrum is a taxonomy question flagged for joint review.
- **vs Technical Assessment Platform (§09 sibling, unprocessed)**: coding/technical skill measurement pole; sharper version of the same seam.
- **vs Assessment Platform (§23 education, processed)**: different taker population (candidates/employees vs students), different purpose (selection/development vs learning/certification), different instrument ownership (vendor-maintained normed instruments vs educator-authored scored tests). Consistent with the sibling's recorded boundary ("same mechanics, different population and purpose").
- **vs Background Check Platform / Employment Verification Platform (§09)**: verification of factual records vs measurement of psychological attributes; different object entirely.
- **vs Employee Survey Platform / Employee Engagement Platform (§09)**: surveys gather opinions with aggregate reporting and no correct answers; psychometric instruments score identified individuals against fixed keys/norms with per-person results.
- **vs ATS**: the ATS owns the requisition/pipeline/candidate-record; the assessment platform is a measurement step integrated into it (trigger-in/results-out). Assessment platforms do not manage the hiring pipeline.
- **vs Interview Management / Video Interviewing**: recorded-interview products capture answers for human review; psychometric scoring is standardized against instruments. Video interviewing appears in-sample only as an adjacent bundled module.
- **Boundary test (remove-what-to-become-another-Type)**: remove vendor-owned normed instruments + norm-anchored interpretation and keep skill work-samples → Candidate/Technical Assessment Platform; change population to students and instruments to author-built → Assessment Platform (education); remove scoring keys/norms entirely → Survey Platform; remove the person-measurement loop and keep the requisition pipeline → ATS.

## Uncertainties

- No help-center-level operational documentation was reachable for any sampled product; all operational mechanics above are product/solution-page level. Final document deliberately avoids precise numbers (test durations, question counts, retention windows, norm sizes) — vendor figures stay here as claims.
- Exact scoring implementations (IRT vs classical, norm-group construction, cut-score tooling) were not directly observed; described qualitatively only.
- Hogan/Criteria evidence is positioning-level; their candidate-side and reporting mechanics are kept general.
- Whether the directory should hold Candidate / Technical / Psychometric Assessment Platform as three leaves or fold them into one talent-assessment spectrum is unresolved — flagged to STATUS.md Boundary Issues, not decided here.
- Accommodations: observed only as SHL's Neurodiversity Hub (candidate resource); depth of in-product accommodation settings unknown — kept hedged.

## Final Synthesis

A Psychometric Assessment Platform is the hiring/development side of the measurement pipeline: a vendor-maintained library of standardized psychological instruments (ability, personality, motivation/values, behavioral judgment) is administered to identified candidates or employees, scored by fixed keys, interpreted against reference frames (norms, competency profiles, role-fit mappings), and returned as reports that support — but do not make — selection and development decisions. Around that loop, the mature market adds role-fit machinery, ATS integration, candidate-facing experience, integrity machinery for unsupervised remote completion, scientific documentation, and (as variants) consultant-delivered interpretation, development-side reuse, and adjacent interview/feedback/proctoring modules. The Type is distinct from skills-testing platforms (what you can do) and education assessment platforms (what you learned), and from surveys (what you think) by the combination of vendor-owned normed instruments and per-person norm-anchored scoring in an employment-decision context.
