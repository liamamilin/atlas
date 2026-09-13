# Security Awareness Platform

## Overview

A **Security Awareness Platform** is the organization-side system for running its security-awareness program: it holds the workforce as a managed learner population, delivers security training to that population, runs benign simulated attacks against it to measure how people actually behave, and aggregates both sides into program metrics and risk scores for the security team.

The problem it solves is specific: most security incidents involve a person clicking, replying, entering credentials, or mishandling data, and technical controls cannot measure whether the organization's people would resist such an attempt. The platform makes human security behavior visible and improvable — by teaching (training content), by testing (simulated attacks delivered into real inboxes and phones), and by measuring (per-person and organization-wide outcomes over time).

The defining core is small:

```text
Employee learner population (managed, grouped, addressable)
├── Security training → assigned → completed (tracked)
├── Simulated attack exercises → per-learner behavior recorded
└── Program measurement → metrics, risk scores, trends
```

Everything else commonly associated with the category — phishing-template libraries, report buttons, gamification, AI-generated content, peer benchmarking, compliance packaging — is standard or optional structure layered on that loop, not what makes the Type.

The boundary in one sentence: remove the simulated-attack measurement and what remains is a security-content LMS; remove the training and what remains is a one-off phishing-test tool; the Type is the two legs run together against one managed population, with measurement closing the loop.

## Users & Context

**Primary operator:** the security awareness program owner — typically a security team member (awareness lead, security manager, or CISO delegate). This person configures the population, builds training and simulation campaigns, monitors results, and reports upward. The platform is their system of work; they may run it daily or in campaign cycles.

**Secondary operators:**

- executives and boards — consumers of program reporting (risk trends, completion, benchmarking), not hands-on users
- in larger organizations, delegated group administrators or regional program managers who run campaigns for their part of the workforce
- in some deployments, the SOC or mail-security team, which receives the real threats employees report

**The population being worked on:** all employees — commonly extended to contractors. Employees are not "users" in the administrative sense; they are the subjects of training and simulation, and simultaneously actors in their own surfaces (their real inbox, a training player, a report button). Their behavior — completing training, falling for or reporting a simulation — is the raw material the platform records.

**Context:** the platform operates inside the organization's real working environment. Simulations must arrive in the actual mail client (or SMS inbox, chat, phone) to be meaningful, which makes the customer's own email infrastructure part of the delivery path. Programs are typically continuous (recurring simulations and training refreshers) with peaks around compliance deadlines and awareness events. In regulated industries, program output doubles as audit evidence.

## Core Model

The platform's world contains one central person-object and two active work-objects, joined by outcome records and rolled up by measurement.

### Learner (employee record)

The central object: a named employee held as an addressable record with attributes — role, department, location, language, employment status — used to personalize and target. Learners are typically created by upload or synchronization from directory/HR systems, and organized into **groups** (departments, sites, job roles, risk tiers). Groups are the practical targeting unit: a campaign rarely targets "everyone" individually; it targets groups, and attributes drive personalization (a finance employee and an engineer see different lures and different courses).

### Training content

The education leg: a library of security-specific learning units — courses, modules, micro-lessons, videos, quizzes — covering topics such as phishing and social engineering, password and credential hygiene, data handling, physical security, and compliance subjects. Mature products carry large multi-language libraries and increasingly generate custom content (including from the organization's own policies). Content is the *material* of the program; it does nothing until assigned.

### Training assignment

The work-object of the education leg: content bound to a learner population with a schedule — due dates, reminders, and completion tracking. An assignment turns content into an obligation whose fulfillment is recorded per learner. Completion state is a first-class fact: it feeds metrics, enforcement (reminders, manager visibility), and compliance evidence.

### Simulation campaign

The work-object of the measurement leg: a planned run of simulated attacks against a chosen population over a schedule. A campaign binds **attack templates** (the lures — a phishing email with a link, an attachment, a credential-harvesting page, a QR code, a text message, a voice script) to targets and a delivery window. Campaigns may be one-shot or ongoing (continuous drip). The simulation is deliberately benign: links lead to controlled landing pages, and any data entered is captured by the platform, not an attacker.

### Simulation outcome

The record that makes the program measurable: for each learner reached by a simulation, the platform records what they did — received, opened, clicked, submitted data on the landing page, replied, or **reported** the message. Outcomes are attributed to the named learner and timestamped. A failed interaction typically triggers an immediate consequence in the learner's surface (a teachable-moment page) and a program consequence (remedial training).

### Report action

The positive-behavior counterpart: the employee flags a suspicious message — simulated or real — through a report button installed in their mail client (and commonly mobile). Reports are recorded per learner as a success signal, and the reported *real* messages often flow onward to security operations as threat signals.

### Program metrics and risk scores

The measurement layer that makes the four pieces a *program*: completion rates, failure rates (the share of learners who interacted with a simulation), report rates, and composite per-learner risk scores built from training state plus simulation behavior. Metrics roll up from learner → group → organization, are tracked as trends over time, and are packaged for executive and board reporting; mature products also benchmark against peer organizations.

### How the objects relate

```text
Directory / HR sync
      ↓
Learner records ── grouped into ──▶ Groups (targeting unit)
      │                                   │
      │            ┌───────────────────────┤
      ▼            ▼                       ▼
Training assignment              Simulation campaign
 (content + schedule)             (templates + schedule + window)
      │                                   │
      ▼                                   ▼
Completion record            Outcome record (opened / clicked /
      │                      data entered / replied / reported)
      │                                   │
      └───────────────┬───────────────────┘
                      ▼
        Program metrics & risk scores
        (learner → group → organization, over time)
                      ▼
        Executive / board / compliance reporting
```

The learner is the hub; the training assignment and the simulation campaign are the two engines; the outcome and completion records are what turn activity into a measurable program.

## How It Works

An awareness program runs as a repeating cycle. The steps below describe the typical loop; terminology and exact mechanics vary by product.

### 1. Establish the population

The program owner populates the platform with the workforce — usually by synchronizing user records from a directory or HR system, or by upload — and organizes people into groups. Attributes (role, department, location, language) are kept current because they drive both targeting and personalization downstream.

### 2. Assign and track training

The owner selects content for each population slice and assigns it with due dates. The platform delivers the assignment to learners (email notification, training portal), sends reminders, and records completion per learner. Enforcement depth varies: some programs simply track; others escalate — reminders, manager visibility, or blocking consequences handled outside the platform. Completion feeds the metrics layer and, where relevant, compliance evidence.

### 3. Run a simulation campaign

The owner composes a campaign: choose attack templates (from a library, customized, or generated), choose the target groups, set the schedule and the activity-tracking window. When the campaign starts, the platform sends the simulated messages through the organization's mail environment into real inboxes (or via SMS, voice, QR, or other channels where supported). From that moment the platform watches for interactions — opens, clicks, data entry, replies — within the tracking window, and records each learner's outcome.

### 4. Respond to the outcome

The moment of failure is treated as the moment of learning. A learner who clicks typically lands on a page that reveals the simulation and delivers a short lesson; many platforms then automatically enroll the learner in remedial training matched to what they fell for. A learner who *reports* the simulation receives positive feedback — reporting is scored as the desired behavior. Some products extend this responsiveness further, delivering coaching in chat channels when risky behavior is detected in real time.

### 5. Measure, report, adjust

The owner watches dashboards: failure and report rates per campaign, completion rates per assignment, per-learner and per-group risk scores, and trends across months. This is what gets presented to executives and boards, and what guides the next cycle — harder lures for resilient groups, basic content for failing ones, more frequent simulation where risk concentrates. The cycle then repeats; awareness programs are continuous by design, because one-off training decays.

### The loop in one line

```text
provision → train → simulate → record behavior → remediate/coach → measure → adjust → simulate again
```

## Interfaces

Two interface families dominate: the administrator's console and the learner's surfaces. Exact layouts and names vary by product.

### Admin console

The program owner's system of work.

- **Dashboard** — program health at a glance: current failure/report rates, completion state, risk trends.
- **Users & groups** — the learner population: records, attributes, group membership, per-learner history and risk score.
- **Training campaigns** — create and manage assignments: content selection, audience, due dates, reminders; completion tracking per learner and per group.
- **Simulation campaigns** — create and manage attack runs: template selection, targets, schedule, tracking window; live status, failures, and reports per campaign.
- **Content library** — browse and manage training content and attack templates; in mature products, author or generate custom items.
- **Reports** — the reporting engine: campaign results, program trends, per-group comparisons, exportable and scheduled reports for executives and auditors.

### Learner surfaces

What employees actually encounter — deliberately lightweight.

- **The real inbox** — where simulations arrive, indistinguishable in placement from real mail; the report button lives here as an add-in in the mail client.
- **Teachable-moment page** — the landing page after a failed simulation: reveals the exercise and delivers a short lesson on the spot.
- **Training player / portal** — where assigned courses are taken: video, interactive lessons, quizzes; progress and completion recorded automatically.
- **Progress / engagement app** — in engagement-driven products, a gamified surface (points, streaks, leaderboards) that frames participation positively.

### Executive reporting surface

Scheduled or on-demand summaries of program outcomes — risk trend lines, completion, benchmarking — shaped for boards and auditors rather than operators.

## Important Rules / Behaviors

- **Simulations are benign but realistic.** Lures mimic real attacks, including credential-harvesting pages; any data a learner enters is captured by the platform as an outcome, never used maliciously. Realism is the point — a simulation that is easy to spot measures nothing.
- **Delivery depends on the customer's mail environment.** Simulations must reach real inboxes, so the platform's sending infrastructure must be allowed through the organization's own mail filters; allow-listing the platform is a standard setup step, and a misconfigured filter silently invalidates results.
- **Failure is defined by interaction within a tracking window.** A campaign records opens, clicks, data entry, and (optionally) replies only during its configured window; what counts as "failing" is a program decision, not a fixed rule.
- **Reporting is the scored success behavior.** Reporting a simulation — or a real suspicious message — is recorded per learner as a positive outcome and usually rewarded with immediate feedback; programs increasingly treat report rate as a headline metric alongside failure rate.
- **Failure triggers remediation.** The standard consequence of a failed simulation is immediate in-the-moment feedback plus (commonly) automatic enrollment in remedial training; the loop from outcome back to education is what distinguishes a program from a test.
- **Outcomes attach to named learners.** Every recorded behavior is attributed to an identified employee; this is what makes per-learner risk scores possible, and it makes the platform a holder of personal behavioral data — programs differ in how they configure and govern that data.
- **Compliance is an output, not the core.** Training completion records and campaign history are routinely used as audit evidence, and compliance deadlines shape program calendars; but the platform's center of gravity is behavior change and measurement, with compliance as a downstream consumer.

## Variants

Common shapes of the Type:

- **Balanced train-and-test platforms** — the mainstream shape: full training library plus simulation engine plus measurement (the majority of the market).
- **Simulation-first products** — descended from phishing-simulation origins; strongest at realistic, threat-intelligence-derived attack simulation, with training built around it.
- **Content-first products** — descended from training-content and courseware heritage; strongest at curriculum, methodology, and assessments, with a phishing platform as a companion line.
- **Engagement/gamification-led products** — continuous, high-frequency, personalized simulation framed as a game; behavioral-science positioning.
- **Suite modules** — awareness training sold inside a broader security platform (email security, human-risk suites), sharing identity and telemetry with neighboring products.
- **Managed programs** — the vendor (or a partner) operates the program on the customer's behalf, common in enterprise and regulated segments.
- **Compliance-driven deployments** — programs run primarily to satisfy regulatory training obligations; the same platform, a different center of gravity.
- **Channel breadth** — email-only programs vs multi-channel programs adding SMS, voice, QR, USB, and chat-borne simulations.
- **AI-era operation** — generated content and simulations, automated campaign operation, and real-time coaching are becoming standard in current products; older and simpler deployments run entirely on curated libraries and manual campaigns.

A variant stops being a variant when it drops one of the defining legs: a product with only simulation is a testing tool; a product with only training is a security-content LMS.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Corporate LMS / Employee Learning Platform | closest neighbor | delivers arbitrary courses and tracks completion; no attack simulation, no security behavior measurement — the awareness platform's training leg alone |
| Breach & Attack Simulation | same domain, different target | exercises technical controls and defenses; the awareness platform exercises people |
| Email Security Gateway / email security products | complementary | blocks real attacks; the awareness platform sends benign simulated ones and measures behavior; sometimes same vendor, different objects |
| Security Compliance Platform | downstream consumer | consumes completion evidence for compliance management; does not run the awareness program itself |
| Cyber Incident Response / email incident response | adjacent hand-off | real messages employees report flow into incident-response workflows; some awareness products bundle triage, but response is a different system of work |
| Insider Risk Management | different measurement object | observes actual employee behavior for risk indicators; no training or simulation program loop |
| Security Program Management / GRC | governance umbrella | manages the security program as a whole; the awareness platform is one program's engine inside it |

The LMS boundary is the most important one, because the two Types overlap on courses and completion tracking. The structural difference: an LMS has no simulated-attack leg and no security behavior measurement — it cannot answer "would our people fall for this?" and that question is the awareness platform's reason to exist.

## Representative Products

- **KnowBe4** — Security Awareness Training (KSAT): market-leading pure-play; training library + phishing simulation + risk scoring; extensive public documentation.
- **Proofpoint** — ZenGuide (Security Awareness Training): risk-based training inside a broad human-risk security suite.
- **Cofense** — Phishing Training (PhishMe SAT): simulation built from real intercepted threats; part of a phishing-defense platform.
- **Hoxhunt** — gamified, high-frequency adaptive simulation; self-labels as a human risk management platform.
- **SANS Security Awareness** — training-content and program-methodology heritage; phishing platform offered alongside curriculum and assessments.

These five were chosen to span the Type's main philosophies (balanced, risk-led, threat-led, engagement-led, content-led) and market positions (pure-play, suite vendor, enterprise, modern challenger, content institute).

## Sources

Research date: **2026-09-09**

- KnowBe4 — AI-Native Security Awareness Training (product page): https://www.knowbe4.com/products
- KnowBe4 Knowledge Base — Phishing Security Test (PST) Overview: https://support.knowbe4.com/hc/en-us/articles/236271227
- KnowBe4 Knowledge Base — Phishing Campaigns Overview: https://support.knowbe4.com/hc/en-us/articles/360051262754
- KnowBe4 Knowledge Base — Security Awareness Training category: https://support.knowbe4.com/hc/en-us/categories/200060614
- Proofpoint — Security Awareness Training / ZenGuide (product page): https://www.proofpoint.com/us/products/security-awareness-training
- Cofense — PhishMe Security Awareness Training (SAT) Platform (product page): https://cofense.com/phishme-security-awareness-training-(sat)-platform
- Cofense — platform overview: https://cofense.com/products/
- Hoxhunt — platform home (product pages): https://www.hoxhunt.com/
- SANS Institute — Security Awareness Training: https://www.sans.org/security-awareness-training/

> Sourcing limitations: vendor help centers for Hoxhunt (HTTP 403) and Proofpoint (login-gated support portal) could not be reached; operational detail for those products rests on their official product pages. Detailed console mechanics cited in this document are grounded in KnowBe4's public knowledge base; equivalent mechanics in other products are described at the level their public pages support. Vendor-published outcome statistics were treated as claims and are not stated as facts in this document. Precise product-specific limits, settings, and branded metrics are recorded in the paired Research Notes.
