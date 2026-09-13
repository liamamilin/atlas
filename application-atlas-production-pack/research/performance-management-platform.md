# Research Notes — Performance Management Platform

Research date: 2026-09-06
Leaf: Performance Management Platform (Domain 09 — HR, Workforce & Talent)
Slug: performance-management-platform

---

## Research Goal

Understand what a Performance Management Platform actually is as an Application Type: the core objects it operates on, the roles involved, the workflow of a performance assessment from setup to a released outcome, which capabilities are defining vs. merely common in current products, and where its boundaries sit against adjacent HR Types (goal/OKR management, engagement surveys, talent review, HCM suites).

---

## Initial Boundary

Tentative understanding before research:

- Likely core: structured evaluation of employees' performance by attributed evaluators (self / manager / peers / upward), organized in recurring cycles, producing a durable record used for development and talent decisions.
- Expected adjacent Types: OKR / Goal Management Platform, Employee Engagement Platform, Employee Survey Platform, Talent Review Platform, Succession Planning Platform, HRIS, Compensation Management Platform, Skills / Competency Management Platform, People Analytics Platform, Employee Recognition Platform, Performance & Attribution Platform (finance — name collision only), Sales Performance Management (sales-domain).
- Key open questions: Is the review cycle the central object, or is it the goal? Are ratings part of the definition? Is calibration defining? Where exactly does continuous-feedback tooling stop being "performance management"?

---

## Research Questions

1. What is the central object — the review cycle, the evaluation record, the goal, or the ongoing conversation?
2. How is a review cycle configured and run (reviewees, reviewers, directions, templates, timelines)?
3. Who writes evaluations, and how is the reviewer graph determined (org chart, peer nomination, additional managers)?
4. What lifecycle states does an evaluation pass through (draft → submitted → calibrated → shared → acknowledged → finalized → locked)?
5. What visibility rules govern review content (manager-only vs. shared, private manager assessments, peer anonymity, role-restricted exports)?
6. How do ratings, scales, weighted scores and calibration work? Are they defining or optional?
7. How do goals/OKRs, feedback, 1:1s, check-ins relate to the evaluation record — same object or adjacent inputs?
8. How do results flow onward (compensation, promotion, succession, analytics)?
9. What differs across segments (SMB vs. enterprise) and across product philosophies (continuous vs. episodic; review-anchored vs. goal-anchored)?
10. Would older / non-SaaS performance appraisal processes (paper forms, HRIS-embedded appraisal modules) still fit the definition?

---

## Representative Products

Selected for market representativeness, documentation depth, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy / Positioning | Tier |
|---|---|---|
| Lattice | Modern "people success" platform; review cycles + continuous habits (1:1s, feedback, updates) in one system; mid-market/enterprise | Mid-market → enterprise |
| 15Five | Continuous-performance philosophy anchored in manager–employee cadence (check-ins, 1:1s) feeding reviews; mid-market | Mid-market (100–1000+) |
| Betterworks | Enterprise, goal-anchored: goals/OKRs as the backbone of performance; review cycles branded as one module ("Conversations") | Enterprise |
| PerformYard | Review-cycle-centric, deliberately simple and flexible ("built around your process"); SMB/mid | SMB → mid |

Considered and not used: Trakstar Perform (official URL redirected to a thin marketing page — insufficient documentation access); Workday / Culture Amp (HCM-suite / engagement-suite embedding noted as a variant, not sampled in depth to keep the sample balanced).

---

## Sources

Tier 1 (official operational documentation):

- Lattice Help Center — https://help.lattice.com/ — collection "Performance Reviews" (231 articles) and article "Create a Review Cycle" (updated 2026-07-20). Fetched 2026-09-06.
- 15Five Help Center — https://success.15five.com/hc/en-us — category overview "Performance Reviews: Overview" (updated 2026-08-14) and help-center home. Fetched 2026-09-06.
- Lattice product pages — https://lattice.com/products/performance , https://lattice.com/platform/performance/reviews . Fetched 2026-09-06.
- 15Five product pages — https://www.15five.com/product/ , https://www.15five.com/products/perform . Fetched 2026-09-06.
- Betterworks product pages — https://www.betterworks.com/ , https://www.betterworks.com/product/performance-review-software/ . Fetched 2026-09-06.
- PerformYard product site — https://www.performyard.com/ . Fetched 2026-09-06.

Source-access limitations:

- Betterworks operational help center (support.betterworks.com → betterworks.zendesk.com) returned an empty landing page; the category page timed out. Betterworks observations therefore rest on official product pages (Tier 2) only — mechanics claims about Betterworks are correspondingly weaker.
- Trakstar Perform was abandoned after its product URL redirected to an HRIS-integration landing page (1 attempt).
- No pricing/plan-specific or numeric-limit details were researched; none are asserted.

---

## Product Observations

Evidence layer: **A** = directly observed in official docs for that product; **B** = observed on official product pages / cross-product reading (weaker).

### Lattice (A/B)

From Help Center "Performance Reviews" collection + "Create a Review Cycle" article (A):

- The **review cycle** is the orchestrating container, created by Admins (Admin > Performance > Reviews). Two creation modes: **Org Chart review** (auto-assigns self / upward / manager reviewers from the reporting structure) and **Automated Rule** reviews (rule-triggered, e.g. by hire date); also **project-based reviews** (CSV bulk-create) and cycles on an **automatic schedule**.
- **Review templates** hold the questions each review group answers; templates can be **overridden by field** (department etc.).
- **Review directions** are configurable per cycle: self, downward (manager), upward, peer. Sequencing is configurable (e.g., downward reviews completed last).
- **Reviewer graph is locked at cycle creation; fields at launch.** Org-chart changes between creation and launch affect results/exports.
- **Peer selection workflow**: employees can nominate peers (incl. self-nomination), managers/admins approve, reviewers may **decline** peer reviews, the number of peer reviewers can be limited.
- **Scoring** (26 help articles): rating/competency questions, **weighted scores**, **calibrated scores** exportable.
- **Calibration** can be set up inside a review cycle.
- **End-of-cycle mechanics**: review packet **sharing settings**, **Review Packet Acknowledgement**, managers may be allowed to end their direct report's cycle; **reopen requests** (employees can request reopening their review); cycle deletion/duplication; "Review Cycle Data Check".
- **Promotions**: promotion nominations inside review cycles.
- **Visibility**: managers view direct reports' review progress; skip-level managers can view indirect reports' reviews before they're shared (explicit permission model).
- **Reporting**: rating/competency analysis, performance trends, exports, bulk PDF review packets, **sentiment analysis** in review cycles.
- **Reviews Context Panel**: reviewer sees 1:1 notes, feedback, praise, goals as evidence while writing (10 help articles).
- **Notifications**: email/Slack tasks per role.

From product pages (A/B): AI-powered review drafts "grounded in Lattice data" (self/upward/downward); talent reviews (performance × potential) as a distinct surface; PIPs; succession planning; calibration group conflict avoidance; optimized PDF review packets; FAQ positions the product as annual/quarterly/project-based/automated cycles + 1:1s + feedback + praise.

### 15Five (A)

From Help Center "Performance Reviews: Overview" (A) — unusually explicit rule statements:

- "Performance Reviews in 15Five is a structured tool for creating, running, and analyzing employee review cycles."
- Role split (A): **Admins** configure cycles, question templates, rating systems, and are the only ones who can create/launch/edit/delete cycles and templates; **managers and employees** write and submit reviews within defined timelines; **HR/executive users** access results, calibrations, reporting.
- Key rules (A, quoted/paraphrased): managers see results only for their direct reports unless granted extra access; **review results are not visible to participants until an admin or manager explicitly shares and finalizes them**; **calibration sessions must be configured before the cycle launches** (cannot be added mid-cycle); exports/downloads are role-restricted; audit log per cycle.
- **Question templates** (A): default + custom; sections include competency questions, Objectives (goal) questions, Growth & Development; custom answer templates; **Private Manager Assessment** questions (manager-only).
- **Review types** (A): self, manager, peer, upward, additional-manager; **peer-only cycles**; **manager effectiveness** cycles; **Lifecycle Reviews** (automated, e.g., triggered by tenure/new-hire milestones); peer **nomination** flow (nominate → approve/deny/remove → nudge).
- **Ratings** (A): "Performance Ratings+" — configurable formulas, rubrics, custom rating attributes (populated individually or via CSV import).
- **Calibration** (A): calibration sessions with a Calibration Table and Talent Matrix (9-box style), lock session, flag/remove conflicting participants.
- **Results** (A): analyze ratings/competencies, filter by demographic attributes, per-person PDFs, company/team results, "complete, share, and finalize review summaries", **acknowledge** results, unshare, undo share/finalize, remove an answer from shared results, extend/lock cycles, external performance data import (CSV).
- Adjacent same-platform surfaces (A): weekly **Check-ins**, **1-on-1s**, **Objectives/OKRs**, **High Fives** (recognition), **Feedback**, **Career Hub** (growth plans/competencies), **Insights Dashboard**.
- Product pages (B): AI-assisted reviews, calibration & 9-box drag-and-drop, talent matrix, HRIS connector; "Best-Self Review®" is the branded review feature name (renamable per org).

### Betterworks (B — product pages only)

- Review cycles live under the **"Conversations"** module: "Run review cycles that support better feedback and performance decisions"; "flexible templates"; check-ins and AI-surfaced feedback suggestions inside conversations.
- Strong **goal-anchoring**: "View live goal progress, milestones, and recent activity directly inside each conversation to link feedback to measurable results"; goals/OKRs are a first-class sibling module; "AI summaries from 1:1s, feedback, and check-ins"; "evidence-based reviews from dynamic performance signals".
- **Employee-initiated** conversations ("give employees the tools to start and log their own conversations") — a notable inversion of the HR-launched cycle.
- **Calibration** is a separate Talent-Intelligence module ("fair, consistent employee evaluations at scale"), alongside Succession, Skills Intelligence, Unified Talent Profiles.
- Positioning: explicitly against "episodic review cycles" — "real-time performance signals in the flow of work"; enterprise audience.

### PerformYard (B — product pages)

- Core platform = "Reviews, meetings, goals, engagement"; **Performance Reviews** is the flagship: employee appraisals, 360 feedback, quarterly check-ins, annual reviews, project-based reviews, "review cycles built around your timeline", one-on-ones.
- **Review forms/templates** configured by HR; "flexible for HR, easy for employees" positioning; "One Performance Management Platform, Built Around Your Process" (annual / semi-annual / quarterly / project / competency-based / goal check-ins / new hire assessments / PIPs).
- **Reporting**: cycle completion and participation tracking, rating distributions, trend lines, **nine-box and calibration views**.
- **Compensation**: merit cycles tied to performance (comp reviews connected to performance, budgets, approvals).
- Skills & competencies assessed in reviews/check-ins; career pathing on review data.
- HRIS + SSO integrations (ADP, BambooHR, Workday, Gusto, Okta...); SMB/mid audience; explicit anti-suite positioning ("without the complexity of broader HCM platforms").

---

## Cross-product Comparison

| Dimension | Lattice | 15Five | Betterworks | PerformYard | Reading |
|---|---|---|---|---|---|
| Central container | Review cycle (org-chart or rule-created) | Review cycle (admin-created) | Review cycle ("Conversations") + goal backbone | Review cycle ("built around your timeline") | **Common (B)** — the cycle is the shared unit of work |
| Employee population substrate | Org chart; HRIS sync | HRIS sync; org structure | HRIS integrations | HRIS sync (ADP/BambooHR/...) | **Common (B)** — platform runs on org-provided employee data |
| Structured evaluation record | Review templates, questions per review group | Question templates, sections, answer templates | Flexible templates | Review forms/templates | **Common (B)** — org-configured instrument |
| Reviewer graph | self/upward/downward/peer; peer nomination; additional reviewers | self/manager/peer/upward/additional manager; peer nomination | manager + employee-initiated; 360 feedback | 360 feedback; manager reviews | **Common (B)** — attributed evaluators in roles relative to the reviewee |
| Ratings | rating/competency questions, weighted scores, calibrated scores | Performance Ratings+ (formulas, rubrics) | ratings implied (calibration module) | rating scales, rating distributions | **Common (B)** but ratingless/qualitative approaches exist in market; not defining |
| Calibration | in-cycle calibration setup | calibration sessions (pre-launch config), Calibration Table, Talent Matrix | standalone Calibration module | nine-box & calibration views in reporting | **Common (B)** in mature products; depth/placement varies |
| Visibility & release | packet sharing + acknowledgement settings; reopen requests | results hidden until shared → acknowledged → finalized; unshare; remove answer | not directly evidenced (page-level) | not directly evidenced | **Common (A: 15Five, Lattice)** — release is an explicit, controlled act |
| Continuous layer | 1:1s, feedback, updates, praise feed review evidence | check-ins, 1:1s, feedback, high fives feed reviews | check-ins, feedback, 1:1s feed reviews | meetings, continuous feedback feed cycles | **Common (B)** — modern implementations surround cycles with a continuous layer |
| Goals | Goals module; objectives in review evidence; goal questions | Objectives questions in templates | Goals are the anchor of reviews ("align with goals and feedback") | goals tied into reviews | **Common (B)**; but several sampled products sell goal mgmt as a sibling product too → not defining |
| Onward flows | promotions; talent reviews; succession | comp module; growth studio (IDP/PIP/succession) | talent intelligence (succession, skills) | merit/comp cycles; competencies | **Common (B)** — performance results feed other talent processes |
| AI | evidence-based review drafts; sentiment analysis | AI-assisted reviews; meeting assistant | AI summaries, feedback suggestions | AI summaries, review-quality coaching | **Common (B)**, current-generation feature; not defining |
| Special cycle types | project-based, automated-rule/scheduled | peer-only, manager effectiveness, lifecycle/automated | — | new-hire assessments, project-based, PIP | **Variant** |

Stop-condition check: core model clear; main workflow clear; stable commonalities identified; a fifth product would mostly repeat existing evidence; boundaries clear. Research stopped here.

---

## Abstraction Levels

### L0 — Defining Invariant

The smallest structure without which the product is not recognizable as a Performance Management Platform:

```text
Organization-scoped employee population (identified people, org-defined)
└── Assessment occasion (defined cycle/occasion for evaluating performance)
    └── Structured evaluation record per employee (org-configured criteria/questions,
        narrative and/or rating responses)
        └── Attributed evaluators in defined roles relative to the employee
            (self / manager / peer / upward; identified, not anonymous)
            └── Tracked lifecycle to a completed, released outcome
                (progress → completion → shared/acknowledged → durable record)
```

Necessity tests (remove-one test):

- Remove the employee population → a generic survey/form tool.
- Remove the assessment occasion → a continuous-feedback or conversation tool.
- Remove the structured record → a 1:1 meeting tool.
- Remove attributed evaluators → automated metrics/analytics (People Analytics).
- Remove lifecycle tracking/release → a form builder, not a performance process.

The combination is what no neighboring Type has.

### L1 — Common Mature Structure (cross-product commonality, not defining)

- Review templates / question libraries (incl. competency-based questions, answer formats)
- Rating scales with configurable scoring (weighted/computed ratings, rubrics)
- Peer-selection/nomination workflow (nominate → approve → decline/limits)
- Calibration support (calibration sessions/tables; 9-box / talent matrix)
- Controlled release of results: share → acknowledge → finalize; unshare/reopen mechanisms
- Progress monitoring, reminders/nudges, completion dashboards
- Reporting & exports (rating distributions, trends, per-person packets/PDFs, audit logs; role-restricted)
- A continuous context layer feeding evidence into evaluations (1:1s, check-ins, feedback, recognition) — in modern implementations
- Goals/OKR visibility linked into review content
- Onward handoffs: promotion nominations, compensation (merit cycles), talent/succession reviews
- AI assistance: evidence-based drafts, summaries, bias checks (current generation)

### L2 — Variant / Optional Structure

- Cadence philosophy: annual/semi-annual formal cycles ↔ quarterly conversations ↔ continuous real-time ("reviews" as one moment in a stream)
- Center of gravity: review-anchored (PerformYard) ↔ goal-anchored (Betterworks) ↔ habit/continuous-anchored (15Five, Lattice)
- Ratings posture: numeric scales + calibration ↔ lighter qualitative/check-in approaches (ratingless trends exist in the market)
- Packaging: standalone platform ↔ module of an HCM suite (Workday-style) or engagement suite (Culture Amp-style)
- Customer tier: SMB simplicity/flexibility vs. enterprise governance (role-based access, audit, SSO, HRIS depth)
- Special cycle types: peer-only, upward/manager-effectiveness, new-hire/lifecycle/automated, project-based, PIP
- Compensation linkage: from "results exportable" to native merit-cycle workflows
- AI posture: none → drafts → agents/coaching

### L3 — Vendor-specific (Research Notes only)

- 15Five: "Best-Self Review®" branded reviews (renamable per account); Performance Ratings+; Private Manager Assessment; Kona meeting assistant; AMAYA; "calibration must be configured before launch" as an enforced rule.
- Lattice: Habits (1:1s/Updates/Feedback/Q&A) branding; Grow; Lattiverse; automated-rule cycles; "Review Cycle Data Check"; calibration-group conflict avoidance.
- Betterworks: module name "Conversations"; Talent Intelligence framing; Skills Intelligence; MCP integration.
- PerformYard: Intelligence Layer; "2 weeks to first review" claim; mascot/voice; per-industry landing pages.
- Lattice: reviewers locked at cycle creation, fields at launch (implementation detail; other products handle the same problem differently, e.g. mid-cycle participant add/remove in 15Five).

---

## Historical / Market-Sample Check

Question: would older, regional, platform-native or differently positioned performance processes fit the L0?

- Paper/Excel appraisal era: organization had an employee roster, an annual appraisal occasion, a structured appraisal form (criteria + ratings + narrative), the manager (and sometimes self) as attributed evaluators, and a signed/acknowledged filed appraisal. → Fits L0 fully. Modern SaaS specifics (calibration UI, 9-box, AI drafts, continuous check-ins, HRIS sync) are NOT required.
- HRIS-embedded appraisal modules (e.g., performance as a Workday/SAP-style module): same structure inside a suite. → Fits; suite embedding is an L2 packaging variant.
- Regional practices (e.g., self-appraisal-heavy cultures, rank-and-yoke/ranking systems): still population + occasion + record + attributed evaluators + tracked outcome, with distribution rules as additional constraints. → Fits; forced distribution is an L2/L3 policy overlay, not the type.
- Conversely, modern "ratingless continuous feedback" products: keep occasion(s) + structured record + attributed evaluators; drop numeric ratings. → Still fits, confirming ratings are L1, not L0.

Conclusion: the L0 survives the historical/market check; nothing in it is an artifact of the current SaaS generation.

---

## Vendor-specific Findings

(Already listed under L3; summarized for the record: 15Five's enforced pre-launch calibration config, Private Manager Assessment, Best-Self Review naming; Lattice's creation-time reviewer locking and Automated Rule cycles; Betterworks' employee-initiated conversations and Talent-Intelligence bundling; PerformYard's compensation-native merit cycles and anti-suite positioning. None promoted into the canonical model.)

## Rejected Findings

- "Performance management = goal/OKR management" — rejected. Goals are a common (and in one sampled product, anchoring) input, but goal management platforms lack the attributed evaluation record. Multiple sampled products ship goals as a separate sibling product.
- "The review cycle must be annual" — rejected. Sample includes annual, quarterly, project-based, lifecycle-triggered, continuous variants; cadence is variant-level.
- "Ratings are defining" — rejected. Ratings/scoring are common-mature; ratingless approaches remain recognizable instances of the type.
- "Calibration is defining" — rejected. Present in all four sampled products at some depth, but it is a fairness mechanism over results; the type is recognizable without it (SMB tier).
- "360 feedback is a separate type" — rejected for this taxonomy. Multi-rater feedback appears as review directions inside the cycle in every sampled product; standalone 360 tools would be a variant form.
- "PIPs are part of the core" — rejected. PIP modules appear in several products but the defining loop does not require them; closer to an adjacent process object.

---

## Boundary Findings

| Neighboring Type | Boundary test ("remove X and it becomes…") |
|---|---|
| OKR / Goal Management Platform | Remove the attributed evaluation record of people (keep only goals/alignment/progress) → OKR platform. Conversely, a PMP can exist with zero goal features. |
| Employee Engagement / Employee Survey Platform | Invert attribution: engagement measures populations with **confidential/anonymized** responses and no per-person evaluation record; PMP evaluates **identified individuals** with attributed evaluators. |
| Employee Recognition Platform | Recognition is real-time, positive-only, no assessment occasion, no evaluation record. |
| Talent Review / Succession Planning Platform | Talent review assesses **potential/future readiness** (performance × potential matrices, bench strength); PMP assesses **completed performance over an occasion**. They share artifacts (9-box) and often modules. In sampled products, talent reviews are a distinct surface adjacent to performance reviews. |
| HRIS | HRIS is the employment system of record (jobs, comp data, org data); PMP **consumes** it and produces performance records. Suite embedding is a packaging variant, not a merge. |
| Compensation Management Platform | Compensation consumes performance outcomes in merit cycles; the evaluation record is the PMP's product, the pay decision is the comp platform's. Some PMPs add native merit cycles (variant). |
| Skills / Competency Management Platform | Competencies commonly appear as review criteria (L1); a competency platform's defining object is the skill/competency model and gap data, not the evaluation occasion. |
| People Analytics Platform | Analytics reads and aggregates; PMP is the system of action that generates the primary performance records. |
| Time & Attendance / Productivity Activity Trackers | Objective machine-captured activity data vs. attributed human judgment in a structured record; different evidence sources and different objects. |
| Sales Performance Management | Same phrase, different population semantics (quota attainment/comp plans for sales roles); domain-specific and compensation-centric. |
| Performance & Attribution Platform (finance) | Name collision only — investment portfolio performance attribution, an unrelated domain. |
| Employee Relations / HR Case Management | PIPs as managed cases belong to case management; a PMP may host PIP templates as an optional module. |

Probable alias/variant notes for STATUS.md: none — the leaf is a legitimate standalone Type. One adjacent-directory observation: "360 Feedback" is not a directory leaf and functions inside this type as review directions; standalone 360 tools would be a Variant.

---

## Uncertainties

- Betterworks mechanics (visibility rules, cycle states) rest on product pages only; its operational help center was unreachable. Its review-cycle inner mechanics were therefore **not** used to support canonical claims.
- Whether peer-review **anonymity** is a common default could not be established from the fetched evidence (15Five/Lattice pages show identity/visibility controls exist and answers can be excluded when sharing; exact defaults not researched). Final doc stays non-specific.
- The exact relationship between "talent reviews" and "performance reviews" varies (Lattice separates surfaces; 15Five embeds 9-box into calibration). Treated as adjacent-process commonality rather than fixed structure.
- Regional/legal acknowledgment requirements (e.g., signed appraisals in some jurisdictions) were not researched; acknowledgment is documented as a common release mechanism, not a legal claim.
- Market share / segment size claims were avoided entirely.

---

## Final Synthesis

A Performance Management Platform is the organization's system for conducting structured, attributed performance assessments of its employees. Its world is made of: the organization's employee population (normally synced from HR systems); defined assessment occasions (review cycles) with timelines and stages; an organization-configured evaluation instrument (templates, questions, competencies, scales); per-employee evaluation records written by identified evaluators standing in defined roles to the reviewee (self, manager, peer, upward); and a controlled lifecycle that carries each record from assignment through completion, calibration, explicit release (share → acknowledge → finalize), into a durable performance history that feeds promotion, compensation, talent and analytics processes. Everything else modern products carry — templates, ratings, peer-nomination machinery, calibration sessions and 9-box matrices, continuous check-ins/1:1s/feedback feeding evidence, goals linkage, AI drafts, compensation handoffs — is common mature structure or variant, not definition.
