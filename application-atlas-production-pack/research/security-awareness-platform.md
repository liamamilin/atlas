# Research Notes — Security Awareness Platform

Research date: 2026-09-09
Slug: security-awareness-platform
Directory leaf: Security Awareness Platform (Section 15 — Cybersecurity, Identity & Trust)

## Research Goal

Understand what a Security Awareness Platform actually is as an Application Type: what objects exist inside it, who operates it, how an awareness program runs through it, what is measured, and where its boundaries lie against neighboring Types (Corporate LMS, Breach & Attack Simulation, Email Security, Security Compliance tooling).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: an organization-side platform used by a security team to (a) deliver security training to employees and (b) measure employee security behavior, chiefly by sending benign simulated attacks (phishing) and recording who interacts with them.
- Likely confusion neighbors:
  - Corporate LMS / Employee Learning Platform (delivers courses, tracks completion — but no attack simulation, no security behavior measurement)
  - Breach & Attack Simulation (tests technical controls, not people)
  - Email Security Gateway (blocks real attacks; does not simulate or train)
  - Security Compliance Platform (compliance evidence is an output of awareness programs, not the core)
- Unknowns going in: is phishing simulation definitional or merely common? Do training-only or simulation-only products still count as this Type? How do risk scores work? What roles/provisioning exist?

## Research Questions

1. What are the core objects (learners, groups, content, campaigns, templates, outcomes, metrics)?
2. How does a simulated phishing campaign work end-to-end (setup → delivery → tracking → consequence)?
3. How is training assigned, completed, enforced?
4. What metrics/risk scores are computed, at what granularity, and surfaced where?
5. What roles exist (admin vs learner), and what are the main interfaces?
6. How is the population provisioned and grouped?
7. What variants exist (segment, standalone vs suite, simulation-first vs content-first)?
8. Where are the boundaries vs LMS / BAS / email security / compliance tooling?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different heritages/customer tiers:

| Product | Vendor | Why selected | Heritage / philosophy |
|---|---|---|---|
| KnowBe4 Security Awareness Training (KSAT) | KnowBe4 | Market-leading pure-play; richest public documentation | Pure-play SAT since 2010; "train / test / reinforce"; now AI-native framing |
| Proofpoint ZenGuide (Security Awareness Training) | Proofpoint | Large security-suite vendor; risk-based positioning | Wombat Security heritage; human-risk framing inside a broad platform |
| Cofense Phishing Training (PhishMe SAT) | Cofense | Phishing-response heritage; enterprise | PhishMe simulation-first origin; real-threat-derived simulations; part of a phishing-defense platform |
| Hoxhunt | Hoxhunt | Modern behavior-change/gamification pole; European origin | Gamified, high-frequency adaptive simulation; self-labels "Human Risk Management Platform" |
| SANS Security Awareness | SANS Institute | Training-content heritage pole | SANS Institute courseware lineage; content + assessments + phishing platform as separate product lines |

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- KnowBe4 product page — https://www.knowbe4.com/products (AI-Native Security Awareness Training) [Tier 2]
- KnowBe4 KB root — https://support.knowbe4.com/hc/en-us [Tier 1]
- KnowBe4 KB: Phishing Security Test (PST) Overview — https://support.knowbe4.com/hc/en-us/articles/236271227 [Tier 1]
- KnowBe4 KB: Phishing Campaigns Overview — https://support.knowbe4.com/hc/en-us/articles/360051262754 [Tier 1]
- KnowBe4 KB: Security Awareness Training category — https://support.knowbe4.com/hc/en-us/categories/200060614 [Tier 1]
- Proofpoint Security Awareness Training / ZenGuide — https://www.proofpoint.com/us/products/security-awareness-training [Tier 2]
- Cofense PhishMe SAT platform page — https://cofense.com/phishme-security-awareness-training-(sat)-platform [Tier 2]
- Cofense platform home — https://cofense.com/products/ [Tier 2]
- Hoxhunt home — https://www.hoxhunt.com/ [Tier 2]
- SANS Security Awareness — https://www.sans.org/security-awareness-training/ [Tier 2]

Source-access limitations:

- Hoxhunt support center (support.hoxhunt.com) returned HTTP 403 — learner-experience operational detail for Hoxhunt rests on its marketing/product pages only.
- Proofpoint support portal is login-gated; ZenGuide operational detail rests on the product page.
- Cofense detailed product documentation (datasheet PDF) not fetched; SAT observations from product pages.
- No pricing/packaging research performed (out of scope for the Type model).

## Product Observations

Evidence layers: **A** = directly observed on an official source for that product; **B** = cross-product commonality across the sample.

### KnowBe4 (KSAT)

- **[A]** Self-positioning: "AI-Native Security Awareness Training — continuous training, testing and reinforcement"; triad framed as Train / Test / Reinforce.
- **[A]** Training: library of training content localized in many languages (page states both "47+" and "35+" in different sections — treat count as unverified); AI-personalized to role/risk/behavior; generative-AI custom training creation; Compliance Training sold as a separate product line (Compliance Plus).
- **[A]** Simulation: "Real-World Attack Simulations" — AI-generated and personalized phishing and vishing simulations; case study describes setting up "10 very basic phishing templates" and a first test with a large click rate.
- **[A, Tier 1]** PST mechanics: a Phishing Security Test sends an email to users; clicking the link leads to a landing page that tells the user they failed a simulated phishing test and gives inspection tips; results = users who failed ÷ users who received = **Phish-prone Percentage**.
- **[A, Tier 1]** Campaign model: admin creates phishing campaigns in the KSAT console; chooses number of PSTs; customizes with topics and templates; can set up ongoing phishing tests. PSTs are sent once the campaign starts.
- **[A, Tier 1]** Attack vectors table: Phishing Link, Attachment, Data Entry (landing page mimicking a data-entry screen), Spear Phishing, Reply-To, QR Code, Callback Phishing (phone number + callback code), USB Drive.
- **[A, Tier 1]** Tracking: **Track Activity** setting defines the window in which opens/link selections/attachment opens count; optional tracking of replies; failures feed per-user and org-level Phish-prone Percentage (org figure based on active users who received at least one PST; each user also has an individual percentage in their user details).
- **[A, Tier 1]** Reporting behavior: **Phish Alert Button (PAB)** — free add-in in the email client toolbar; users report phishing emails; reporting a simulated phish shows a congratulation message.
- **[A, Tier 1]** Failure consequence: users who fail PSTs can be enrolled in **training campaigns**; **remedial training campaigns** can auto-enroll users who fail.
- **[A, Tier 1]** Console surfaces: Reports tab (wide range of reports, customizable); Phishing > Campaigns (per-campaign status, failures, Phish-prone %); Phishing > Reports (campaign data, failures vs reported comparisons). KB splits **Admin Support** and **Learner Support** sections; a **Training Campaign Overview** article exists (training campaigns are a first-class console object).
- **[A, Tier 1]** Delivery dependency: a **Whitelisting Guide** exists — simulations are delivered through the customer's email environment and must be allowed through its filters.
- **[A]** Measurement: **SmartRisk™** engine produces a dynamic per-user Risk Score combining simulation results, training completion, and coaching response; rolls up to group/org; 60+ built-in reports and executive dashboards; Phish-prone Percentage as headline metric (vendor-claimed averages 33.1% → 4.1% in 12 months — marketing claim, recorded as claim only).
- **[A]** Real-Time Coaching: contextual "SecurityTips" delivered in chat channels (Slack, Google Chat, Teams) when risky behavior is detected — integration with security vendors stated.
- **[A]** AIDA (AI Defense Agents): automation of program operation — content selection, scheduling, follow-up.
- **[A]** Suite context: standalone SAT plus separate email-security products (Defend/Prevent), incident response (PhishER), agent risk products.

### Proofpoint (ZenGuide / Security Awareness Training)

- **[A]** Positioning: "Deploy Automated, Risk-Based Security Awareness Training"; "go beyond basic security awareness training… beyond traditional security awareness training and phishing tests."
- **[A]** Individual human risk: "Measure human risk at the individual user level"; behavioral and role-based risk insights; **threat-informed risk scoring** incorporating threat exposure, vulnerabilities, and phishing performance.
- **[A]** Reporting behavior: **Report Suspicious** button across email and mobile devices.
- **[A]** Adaptive grouping/enrollment: group users by risk, role, and behavior; automatically assign relevant training programs; auto-enroll users in personalized training that adapts to risk levels.
- **[A]** Learning: dynamic learning paths with simulations, assessments, guided learning; micro-learning and just-in-time guidance based on user behavior; gamified engagement; WCAG-based accessibility settings; content across topics, difficulty levels, formats, languages.
- **[A]** AI: turn real attacks into training; Satori Phishing Simulation Agent recommends/builds simulations; AI ThreatFlip.
- **[A]** Outcomes: track behavior change, benchmark against industry peers; **Human Risk Explorer** reveals high-risk users and risky behaviors, tracks changes over time.
- **[A]** FAQ framing: effective programs = role/risk-based content + realistic phishing simulations + just-in-time coaching + ongoing reinforcement with behavior tracking; explicit contrast "measure and drive behavior change — not just course completion."
- **[A]** Suite context: part of Proofpoint Zen platform; bundled with Collaboration Security Prime.

### Cofense (PhishMe SAT / Phishing Training)

- **[A]** Positioning: "Phishing Training — Train Smarter, Defend Better"; employees as "last line of defense"; simulations **based on real threats** with human-vetted intelligence; "leverages real phishing data for adaptive simulations and awareness programs that learn with every incident."
- **[A]** Capability list: Dynamic Content Library; Comprehensive Multi-Channel Simulations; Real-Time Threat Reporting; Responsive Delivery; Streamlined, Insightful Analytics.
- **[A]** Multi-channel simulation: replicate real-world threats including **smishing, vishing, and QR-code phishing**.
- **[A]** Reporting behavior: **Reporter button** — one-click reporting that feeds "a global intelligence network"; improves response times and fosters behavioral change.
- **[A]** Delivery: send phishing simulations "during active email use" (responsive delivery).
- **[A]** Analytics: "robust, board-ready reporting and analytics to track performance, measure risk, and refine training."
- **[A]** Compliance driver (customer quote): regulated organization uses simulations + training content "to add to our compliance."
- **[A]** Suite context: one pillar of the Cofense phishing-defense platform beside Phishing Remediation (PDR), Managed Phishing Defense, Threat Intelligence; homepage contrast: "Generic training weakens employee resilience"; vendor-claimed "26% higher employee resilience — real phish drive lasting behavior change" (marketing claim).

### Hoxhunt

- **[A]** Self-label: "Human Risk Management Platform"; products: Security Awareness Training, Adaptive Phishing Training, Email Incident Response Automation, Behavior Risk Console ("surface risky real-world behaviors beyond email and automate interventions").
- **[A]** Simulation: phishing simulations across **email, SMS, phone calls, or Teams**, AI-mimicking current real-world attacks; personalized per employee based on department, location, training progress, and more.
- **[A]** Failure consequence: "instant micro-trainings solidify understanding and drive lasting safe behaviors."
- **[A]** Training: interactive bite-sized security awareness trainings; library of customizable training packages; generate custom training with AI; framed for "compliance, maximize engagement."
- **[A]** Gamification: "gamified training that employees love"; learner sign-in points to a dedicated game app (game.hoxhunt.com); "carrot approach" praised by customers.
- **[A]** Metrics: failure rates, engagement rates, detect rates; "resilience ratio"; "measurable behavior change outcomes"; admin dashboard and reporting; board reporting driven by awareness results.
- **[A]** Human sensor network: employees report real threats; reports give visibility into real phishing campaigns (URL blocking, IP blacklisting); "human threat detection as an integral part of the whole stack."
- **[A]** Frequency: customer quote — "over 10,000 monthly simulations" to active employees (single-customer anecdote, not a norm claim).
- **[A]** Suite context: standalone platform + email incident-response automation product.

### SANS Security Awareness

- **[A]** Positioning: "trusted risk-driven security awareness training… redefines human risk management… drives a strong security culture"; combines "expert-led, role-specific security awareness training with strategic resources."
- **[A]** Phishing product line: "real-world phishing simulation… continuous training and testing. The platform allows you to control every aspect of your phishing awareness program, with pre-configured or customizable phishing tests, just-in-time training, and automated remedial courses."
- **[A]** Training product line: library of 50+ training modules across 6 tracks, curated by subject-matter experts; translated into 30+ languages (page says "over 34"); engaging formats; end-user + role-based (end users to IT admins and executives).
- **[A]** Assessment product line: Workforce Security Culture & Knowledge Assessments — "establish a baseline and measure progress over time… reveal gaps in behavior, mindset, and understanding."
- **[A]** Program resources: Security Awareness Report (benchmark data from awareness officers worldwide), Security Awareness Maturity Model (stages from compliance-focused to culture change), annual Summit.
- **[A]** Topic scope (FAQ): social engineering (phishing, smishing, vishing), credential theft/weak passwords, data leaks/accidental sharing, ransomware/malware, secure AI use.
- **[A]** Structure note: phishing simulation and training content are **separate product lines** under one awareness offering — supports the two-pillar (train + test) structure of the Type.

## Cross-product Comparison

| Dimension | KnowBe4 | Proofpoint ZenGuide | Cofense PhishMe SAT | Hoxhunt | SANS |
|---|---|---|---|---|---|
| Learner population | users + groups in console | users grouped by risk/role/behavior | employees | employees, personalized by dept/location/progress | end users + role-based tracks |
| Training content | large library, many languages, AI-generated custom | adaptive paths, micro-learning, gamified | dynamic content library | bite-sized interactive, library + AI-generated | 50+ modules, 6 tracks, expert-curated |
| Training assignment | training campaigns; remedial auto-enrollment | auto-enrollment by risk group | awareness programs | triggered trainings + compliance packages | assigned programs; remedial courses |
| Simulation | phishing campaigns; 8 named vectors; templates; ongoing tests | AI-guided simulations built on real attacks | real-threat-based; smishing/vishing/QR | email/SMS/phone/Teams; AI-personalized; high frequency | pre-configured/customizable tests |
| Failure response | teachable landing page; remedial training; real-time coaching | just-in-time coaching; adaptive re-enrollment | adaptive follow-on | instant micro-trainings | just-in-time training; automated remedial |
| Report button | Phish Alert Button | Report Suspicious | Reporter button → global intel network | report → human sensor network | not observed on fetched page |
| Measurement | Phish-prone %; per-user Risk Score; 60+ reports; exec dashboards | individual human risk; threat-informed scoring; benchmarking; Human Risk Explorer | board-ready analytics; risk measurement | failure/engagement/detect rates; resilience ratio | culture & knowledge assessments; maturity model; benchmark report |
| Suite context | standalone + email security/IR products | inside Proofpoint Zen platform | inside Cofense phishing-defense platform | standalone + email IR automation | inside SANS workforce training offering |
| Distinct emphasis | automation + risk scoring | risk-based targeting + benchmarking | real-threat fidelity + intel network | gamification + engagement + frequency | content authority + program methodology |

**B-layer commonalities (observed across all 5):**

1. A managed **employee learner population** organized for targeting (users + groups; attributes like role/department/location/language).
2. A **security training content library** (courses/modules; micro-learning formats; multi-language) with **assignment and completion tracking**.
3. **Simulated attack exercises** delivered into the employees' real working environment (email dominant; SMS/voice/QR/USB also present in-sample), with **per-learner interaction outcomes recorded** (open/click/data-entry/reply/report).
4. **Failure-triggered follow-up**: teachable-moment feedback and/or remedial training, often automatic.
5. A **reporting mechanism** for employees to report suspicious messages (4/5 observed on fetched pages; SANS not observed — held at 4/5).
6. **Program measurement**: per-learner and aggregate metrics (completion, failure/"phish-prone", report rates), risk scores, trends, executive/board reporting; some benchmark against peers.
7. **Admin console + learner-facing surfaces** as the two primary interface families.
8. **Compliance** as a program driver (audit evidence), explicit at Cofense (customer quote), SANS (maturity model stages), Hoxhunt ("compliance goals"), KnowBe4 (separate compliance product line).

**Divergences (variant axes, not Type structure):**

- Simulation source: template libraries vs AI-generated vs derived from real intercepted attacks.
- Simulation cadence: periodic campaigns vs continuous high-frequency drip.
- Channel breadth: email-only vs multi-channel (SMS/voice/QR/USB/chat).
- Philosophy: compliance-first vs engagement/gamification-first vs risk-scoring-first.
- Packaging: standalone vs suite module; SMB self-serve vs enterprise/managed services.
- Scope drift: some products expand toward broader "human risk management" (behavior beyond email, telemetry from other security tools).

## Canonical Abstraction

### L0 — Defining Invariant (jointly-held; deliberately small)

The Type is the organization's system for running its security-awareness program. Four jointly-held structures:

1. **The employee population as the managed unit** — the organization's people held as addressable learner records (individually identified, attribute-carrying, grouped) that both training and simulation target. Remove → an HR roster or a generic LMS user base; no security program substrate.
2. **Security training delivered and completed** — security-specific content (courses/modules on phishing, passwords, data handling, social engineering, compliance topics) assigned to learners, with completion tracked. Remove → a phishing-simulation-only testing tool (the simulation-only pole); the "awareness" leg gone.
3. **Simulated attack exercises with recorded per-learner behavior** — benign simulated attacks (phishing email the dominant medium; SMS/voice/QR/USB common realizations) delivered to learners in their real working environment, with each learner's interaction (opened / clicked / entered data / replied / reported) recorded as an outcome. Remove → a security-content LMS; the behavior-measurement leg gone.
4. **Program measurement** — training state and simulation behavior aggregated into program-level metrics (completion rates, failure/"phish-prone" rates, report rates, per-learner and organizational risk scores, trends over time) surfaced to the program owner. Remove → delivery machinery with no program loop; the "platform" collapses to a sender plus a course player.

Jointly-held load-bearing analysis:

- 1 alone = HR/directory roster (or LMS user base)
- 2 without 1 = a content library with nobody assigned
- 3 without 1 = a one-off phishing test service / simulation-only utility
- 4 without 1–3 = metrics over nothing
- 1+2 without 3+4 = security-content LMS (Corporate LMS territory)
- 1+3 without 2 = phishing simulation tool (simulation-only pole)
- 1+4 without 2+3 = dashboard over nothing
- 2+3 without 1 = unbound content and tests, no managed population
- 1+2+3 without 4 = delivery machinery without the program loop

Anti-overfit notes:

- **Phishing email is NOT definitional** — the invariant is "simulated attack exercise with recorded behavior"; email is the dominant realization, but SMS, voice, QR, USB, and chat-channel simulations are documented in-sample (Cofense, Hoxhunt, KnowBe4).
- **Email as delivery medium is NOT definitional** — same reason.
- **AI generation is NOT definitional** — era-current machinery (KnowBe4 AIDA, Proofpoint Satori agent, Hoxhunt AI generation); template-library poles in-sample.
- **Risk scores with specific formulas are NOT definitional** — every sampled product measures, but the scoring machinery is vendor-specific; the invariant is that training state + simulation behavior aggregate into program metrics.
- **Report button is NOT definitional at L0** — 4/5 observed; held as strong common-mature structure (it is the positive-behavior counterpart of failure tracking).

### L1 — Common Mature Structure

- Learner grouping (departments, locations, roles, risk tiers) as the targeting unit for both legs.
- Training campaigns/assignments with due dates, reminders, and completion enforcement.
- Simulation campaigns with template selection, target selection, scheduling, and a bounded activity-tracking window.
- Teachable-moment landing pages after a failed simulation (instant feedback at the moment of failure).
- Automatic remedial training enrollment on failure.
- Employee report button in the mail client (and commonly mobile), with positive feedback on reporting simulations.
- Per-learner risk/failure metrics rolling up to group and organization level.
- Executive/board-ready reporting; peer benchmarking in mature products.
- Multi-language content and simulations for global workforces.
- Delivery through the customer's own email environment (whitelisting/allow-listing guides are standard operational documentation).
- Admin console (users/groups, campaigns, content, reports) + learner experience (inbox + training player/portal).

### L2 — Variant / Optional Structure

- Simulation source: curated template library vs AI-generated vs derived from real attacks/threat intel.
- Cadence: periodic campaigns vs continuous adaptive simulation.
- Channel breadth: email-only vs multi-channel (SMS, voice/vishing, QR, USB drops, callback, chat).
- Philosophy: compliance-driven vs engagement/gamification-driven vs risk-analytics-driven.
- Packaging: standalone platform vs module of a security suite; SMB self-serve vs enterprise with managed services.
- Compliance training as a bundled or separate product line.
- Real-report handling: some platforms add email incident-response/triage for reported real threats (adjacent capability, sometimes separate product).
- Expansion toward human risk management: behavior telemetry beyond email, integrations with other security products.
- Program methodology services: maturity models, benchmark reports, awareness-month kits.

### L3 — Vendor-specific (research notes only)

- KnowBe4: Phish-prone Percentage™, SmartRisk™, AIDA, Real-Time Coaching SecurityTips, PhishER, Compliance Plus, The Inside Man series, ASAP free tool, free PST for up to 100 users, the 8-vector taxonomy, Track Activity / Track Replies settings, 60+ reports figure.
- Proofpoint: ZenGuide naming, Satori Phishing Simulation Agent, AI ThreatFlip, Human Risk Explorer, WCAG accessibility framing, Collaboration Security Prime bundling.
- Cofense: PhishMe naming, Reporter button feeding Cofense's global intelligence network, PDR platform, managed phishing defense services, "26% higher resilience" claim.
- Hoxhunt: game.hoxhunt.com gamified learner app, resilience ratio, Behavior Risk Console, "20x lower failure rates / 90%+ engagement" claims.
- SANS: Maturity Model, Security Awareness Report, Summit, 6-track/50+ module library structure, Knowledge Assessments product line.
- All vendor-claimed numbers (33.1%→4.1%, 26%, 20x, 10,000 sims/month) are marketing claims or single-customer anecdotes — recorded as claims, never promoted to Type facts.

## Boundary Findings

- **vs Corporate LMS / Employee Learning Platform**: an LMS delivers arbitrary courses and tracks completion; it does not simulate attacks or score security behavior. The SAP's training leg alone is a security-content LMS. Conversely an LMS cannot run a phishing campaign. The seam: **simulated-attack behavior measurement**. Remove simulation from the SAP → LMS territory; add attack simulation to an LMS → it starts becoming this Type.
- **vs Breach & Attack Simulation**: BAS exercises technical controls (attack techniques against infrastructure/defenses); the SAP exercises **people**. People-targeted phishing testing belongs to awareness tooling, not BAS (also independently recorded in the BAS research pass).
- **vs Email Security Gateway / email security products**: the gateway blocks real attacks; the SAP sends benign simulated ones and measures behavior. Complementary, often same vendor, different objects (malicious message vs learner outcome).
- **vs Phishing-simulation-only tools** (e.g., open-source simulation senders): they satisfy leg 3 only — a pole/utility, not the full Type. Early simulation-only offerings (PhishMe's original form) historically sat here before the market converged on train+test.
- **vs Security Compliance Platform / compliance training**: compliance evidence (completion records for audits) is an *output* of awareness programs; compliance-course delivery alone is LMS/compliance-training territory. Compliance is a driver, not the core.
- **vs Insider Risk Management**: observes actual employee behavior for risk indicators; no training/simulation program loop.
- **vs Human Risk Management (emerging umbrella)**: two sampled vendors self-label with human-risk framing (Hoxhunt platform name; Proofpoint "human risk" language). HRM adds telemetry from other security products and broader behavior surfaces; the SAP remains the training+simulation+measurement engine inside it. Recorded as a market-framing drift, not a taxonomy split; the directory leaf remains valid.
- **"Remove what to become another Type" summary**: remove simulation → security-content LMS; remove training → simulation-only testing tool; remove the managed population → unbound content+tests; remove measurement → delivery machinery, no program.

## Historical / Market-Sample Check (§24)

- Would older or differently positioned products still fit? The pre-platform era (classroom/CBT awareness training with attendance and quiz tracking, no simulation) satisfies legs 1+2+4 but not 3 — historically those were "awareness training products," and the *platform* category consolidated precisely when simulation arrived (the sampled vendors' own heritages show this: PhishMe simulation-first 2011-era, KnowBe4 train+test from 2010, Wombat assessment+training, SANS adding a phishing platform beside content). The jointly-held four-leg structure describes the consolidated Type; the training-only pole is recorded as the historical predecessor and LMS seam, not as the Type.
- Regional/platform-native check: European behavioral-science vendors (Hoxhunt, and SoSafe-class products not fetched), North American pure-plays, and content-institute heritage products all satisfy the four legs — no region-specific machinery in L0.
- Medium check: email-dominant era machinery (mail-client report buttons, whitelisting) held at L1, not L0, because multi-channel and non-email realizations are documented.

## Uncertainties

- **Provisioning mechanics**: learner-record creation (CSV upload vs directory/HR sync vs SSO) is standard in the category but was not directly observed on the fetched pages for most products; phrased moderately in the final document ("typically created by upload or synchronization from directory/HR systems").
- **Individual-result visibility/privacy controls**: programs clearly hold per-learner behavior data, but controls over who sees individual results were not directly evidenced; omitted from the final document rather than guessed.
- **SANS report-button**: not observed on the fetched page; held at 4/5 for the report-button commonality.
- **Simulation-only and training-only poles**: existence asserted from category knowledge (e.g., open-source simulation senders; historical CBT products), not from fetched official pages — kept as boundary reasoning, not as product claims.
- **Vendor-claimed outcome numbers**: all recorded as claims; no independent verification attempted (out of scope).
- **Hoxhunt operational detail**: support center 403; learner-experience mechanics rest on marketing pages.

## Final Synthesis

A Security Awareness Platform is the organization-side system of record and operation for its security-awareness program. Its world is built from four jointly-held structures: a managed employee learner population; security training delivered to and completed by that population; simulated attack exercises run against it with each learner's behavior recorded; and program measurement that aggregates both legs into metrics, risk scores, and trends for the program owner. The learner is the central object; the simulation campaign and the training assignment are the two active work objects; the outcome record is what turns activity into a program. Everything else — channels, AI generation, gamification, benchmarking, incident-response handoff, compliance packaging — is common, variant, or vendor-specific structure layered on that loop.
