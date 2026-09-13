# Ethics & Conduct Management

## Overview

An **Ethics & Conduct Management** application is the organization-operated system of record for its ethics and conduct program. It captures what members of the organization declare about their own conduct-relevant situations — conflicts of interest, outside employment and interests, gifts, hospitality and entertainment — routes every disclosure through a program-defined review that ends in a recorded, attributable determination, and keeps those records as durable, auditable registers over time. It also holds the conduct standards the workforce is bound to (the code of conduct and related policies) and tracks each person's acknowledgment of them.

The problems it exists to solve are practical ones: an organization declares standards of conduct, and then needs to know — provably, per person and over time — who has a conflict of interest, who has accepted what gifts from whom, who has attested to the code, and what was decided about each declared situation. Before such software, this lived in spreadsheets, shared inboxes and email approvals; the application turns it into a governed, queryable program record.

Its boundary: it is not the whistleblowing hotline as such, not the investigation workbench, not the policy library, and not the regulatory-obligation register — though it is commonly packaged together with several of these and shares their data.

## Users & Context

**Primary operators — the ethics program function:**

- the ethics / compliance program owner (often a chief ethics & compliance officer) who defines disclosure types, forms, review routes and campaigns, and answers for the program to executives, auditors and regulators
- ethics officers and designated reviewers who assess incoming disclosures, request more detail, and record determinations
- program administrators who configure questionnaires, thresholds, reminders and reporting

**The declared population — employees:**

- disclose conflicts, outside activities, gifts and hospitality, often prompted by onboarding or recurring campaigns
- attest to (or acknowledge) the code of conduct and specific policies
- complete assigned ethics and compliance training
- ask for guidance when unsure whether something needs to be declared
- (where a speak-up channel is bundled) report concerns about others' misconduct, anonymously or identified

**Participating roles:**

- line managers and approving executives who review or approve specific disclosures or gifts
- legal, HR and audit functions that consume registers and outcomes
- executives and the board, who receive program-level reporting
- optionally, outsourced hotline operators and — in extended deployments — suppliers and other third parties who receive the code of conduct and training

The operating context is organization-wide, multi-year, and evidence-minded: almost everything the application does is done so that it can later be demonstrated — to internal audit, an external auditor, or a regulator — that the situation was declared, reviewed, decided and managed.

## Core Model

### The defining core

The application revolves around one recurring loop and one durable record:

```text
Conduct framework (code of conduct + conduct policies)
        │ defines what must be declared
        ▼
Conduct-situation disclosure (employee self-declaration)
        │ routed by program rules
        ▼
Review → recorded determination
        │
        ▼
Durable program register (disclosures, amendments, documents, determinations)
```

Four properties carry the type:

- **Conduct-situation disclosure** — a structured, self-initiated declaration by a member of the organization about a situation relevant to conduct rules: a conflict of interest, an outside job or board role, a family connection to a vendor, a gift received or given, hospitality or travel. Disclosures are captured through configurable questionnaires shaped by disclosure type, policy need and employee group — they capture facts sufficient to assess risk, not just a yes/no answer.
- **Program-defined review routing** — each disclosure is routed, by rules the program configures (disclosure type, employee attributes, region, value), to the person or team responsible for assessing it. Reviewers can request missing detail, attach supporting documents, and see related or previous disclosures for context.
- **Recorded determination** — a review ends in an explicit, attributable outcome: cleared, more information required, managed with mitigation (for example, recusal or transfer of a decision), approved with conditions, or escalated. The outcome, its author and its reasoning stay connected to the disclosure record.
- **Durable program register** — disclosures, their amendments over time, their documents and their determinations persist as an organization-level, searchable, audit-trail-backed register. This register — not any single report — is the product's center of gravity; it is what an audit asks for.

Everything else commonly associated with ethics software — code-of-conduct acknowledgment tracking, training assignment, hotline channels, culture measurement — is layered around this loop and the register.

### Standard capabilities of mature products

- **Conduct framework as a living artifact** — the code of conduct published as a distributable, often interactive document or microsite; conduct policies attached to the disclosure process so that expectations are visible at the moment of declaring.
- **Attestation and acknowledgment tracking** — which person acknowledged which version of the code or policy, and when; attestation state per person, reported at population level.
- **Disclosure and attestation campaigns** — prompt-driven collection moments, commonly at onboarding and on periodic cycles (an annual conflict-of-interest or code-of-conduct affirmation is the archetypal campaign), with reminders for non-responders.
- **In-year updates** — the ability to file an amendment when circumstances change (new outside job, new gift, new relationship) without waiting for the next campaign, with the amendment kept connected to the original disclosure.
- **Speak-up intake and case handling** — reporting channels (web form, mobile app, sometimes a phone hotline) through which employees report suspected misconduct, with anonymity support, triage, assignment and resolution tracking. Widely bundled; not universal (see Related Application Types).
- **Training and communication** — ethics and compliance courses assigned by role, location or risk exposure; completion tracked alongside attestations as part of the same program picture.
- **Program analytics and reporting** — dashboards of disclosure volume, review status and aging, attestation and training completion, patterns by group, role, region or category; audit-ready and leadership/board-facing reports; some products add benchmarking against peers.
- **Employee self-service portal** — one surface where a person discloses, attests, takes training, reads the code, and asks questions.
- **Escalation and reminder machinery** — flags for incomplete or delayed reviews and for outstanding attestations.
- **Integration** — HR systems supply the population and its attributes (joins, leavers, roles, locations); identity systems provide sign-on; audit systems consume the evidence.

### Concept and implementation

The same concept is implemented differently across products, which is why the core is described conceptually:

```text
Concept:  conduct framework
Implementation: code-of-conduct documents, policy libraries, interactive code microsites

Concept:  conduct-situation disclosure
Implementation: COI questionnaires, gift & hospitality log entries, attestation statements

Concept:  program-defined review routing
Implementation: attribute-based routing rules, approval thresholds, escalation paths

Concept:  recorded determination
Implementation: approve / request info / mitigate / accept / escalate decisions with reviewer attribution

Concept:  program register
Implementation: centralized searchable repository with audit trails and submission history
```

## How It Works

### Program setup

```text
Define the conduct framework (code of conduct, conduct policies)
→ define disclosure types (COI, gifts & hospitality, outside employment, …)
→ configure questionnaires per type / employee group
→ configure review routing rules and reviewer assignments
→ configure campaigns (onboarding, periodic affirmations) and reminders
```

### The disclosure loop (the defining workflow)

```text
Program prompts (campaign, onboarding) or employee initiates
→ employee completes a disclosure questionnaire
→ disclosure enters the review queue under routing rules
→ reviewer assesses; may request more detail or consult related disclosures
→ determination recorded and attributed
→ if managed: mitigation conditions recorded (e.g. recusal, transferred decision)
→ register updated; employee and stakeholders informed
→ circumstances change later → amendment filed → loop repeats
→ periodic re-affirmation confirms the record is still accurate
```

The loop never really ends: the register's value comes from being current, which is why campaigns, reminders and in-year updates exist.

### Gifts & hospitality in practice

A gift or a dinner with a vendor is typically the highest-frequency disclosure. Mature products treat it as a lightweight log entry: guided forms capture who gave or received what, of what value, on what occasion, connected to which third party; entries accumulate into a register that reviewers can inspect by person, unit, vendor or period. Some products additionally enforce policy limits (by value, region or relationship) directly in the flow — showing the employee the impact of a proposed gift on limits before submission, auto-approving clearly low-risk entries, and routing exceptions to designated reviewers — and normalize values across currencies for global reporting. The depth of this machinery varies considerably by product.

### Reporting concerns (when bundled)

```text
Employee reports misconduct via web / mobile / hotline (often anonymously)
→ report enters a triage queue
→ program staff assess and assign (investigate internally or hand off)
→ case is worked to an outcome; reporter informed within limits
→ outcome feeds program data and, where relevant, new disclosure rules or training
```

### Program oversight loop

```text
Aggregate register + attestation + training + case data
→ detect patterns (recurring gifts from one vendor, clusters of conflicts in one team, overdue attestations)
→ adjust the program: policy guidance, targeted training, new routing rules
→ report to leadership / board / auditors
```

### Capability tiers

**Defining core** — without these the application stops being this type:

- conduct-situation disclosure intake (structured, configurable)
- program-defined review routing
- recorded, attributable determinations
- durable, auditable program registers

**Standard in mature products:**

- code of conduct / policy acknowledgment tracking
- disclosure and attestation campaigns with reminders; in-year updates
- training assignment and completion tracking
- program dashboards, audit-ready and board-facing reporting
- employee self-service portal
- HRIS / identity integrations

**Common but optional:**

- bundled speak-up channel and case management
- gift-limit enforcement with approvals and currency normalization
- culture measurement (survey-based assessment, engagement analytics on the code)
- third-party extension (supplier codes of conduct, supplier training, screening)
- benchmarking, AI-assisted summaries and intake assistance, mobile apps

## Interfaces

- **Program administration console** — the program owner's surface: disclosure-type and questionnaire builders, routing and threshold rules, campaign configuration, reviewer assignment, reminder and escalation setup.
- **Review worklist** — the reviewer's queue: pending disclosures with type, submitter, routing basis and age; opens into the disclosure record with the questionnaire responses, attached documents, related disclosures, a request-for-detail thread, and the determination action. Escalation flags surface delayed or incomplete reviews.
- **Employee portal** — the workforce surface: current disclosure and attestation status, campaign prompts with due indicators, disclosure and amendment forms, the published code of conduct and policies, assigned training, and a guidance/ask channel. Simplicity is deliberate — most employees touch the system a few times a year and must not need training to do so.
- **Gift & hospitality register** — a list-and-filter surface over accumulated entries (by person, unit, vendor, period, value band), with drill-down into each entry's approval trail.
- **Code of conduct surface** — the published code as a readable (often interactive) artifact, with version awareness and an acknowledgment action.
- **Program dashboards and reports** — cross-cutting views: disclosure volume and mix, review status and aging, attestation and training completion, patterns by group/region/category; exportable audit-ready packs.
- **Reporting channel** (when bundled) — the intake surface for concerns: report form with anonymity option, and a staff-side case view for triage and resolution.

## Important Rules / Behaviors

- **Disclosure is self-initiated, and stale records are a known failure mode.** The application therefore treats "keep it current" as a first-class behavior: campaigns, reminders, in-year amendments connected to the original record, and periodic re-affirmation.
- **Every determination is recorded and attributable.** Who decided, what was decided, when, and on what basis stays with the disclosure. This is what makes the register audit-grade evidence rather than a logbook.
- **Review routing is program-defined, not ad hoc.** Which disclosures go to whom is configured policy (by type, employee attributes, region, value) — reviewers receive work through rules, not inbox forwarding.
- **The conduct framework defines the boundaries of declaration.** What must be disclosed, and what happens when thresholds are crossed, derives from the organization's own code and policies; the application enforces and records the process but the policy content is the organization's.
- **Attestation state is per-person, version-aware, and feeds risk views.** Unacknowledged codes and overdue attestations appear as program-level risk signals, not just completion percentages.
- **Confidentiality and anonymity are structural on the reporting side.** Where a speak-up channel is included, anonymity support and reporter-confidentiality handling are part of the design, not add-ons.
- **Escalation is automatic.** Incomplete or delayed reviews and unanswered reminders escalate rather than silently age.
- **The register is preserved.** Records survive employee departures and organizational change; the historical trail (including superseded amendments) remains retrievable.

## Variants

- **Suite posture** — the same loop ships as a standalone disclosure product, as a full ethics & compliance program suite (disclosures + attestations + training + channel + analytics), or as a module inside a broad governance-risk-compliance platform alongside risk registers, policy management and third-party risk.
- **Speak-up bundling** — with an in-house hotline and case management; with an outsourced hotline operation; or with no reporting channel at all.
- **Regulatory regime** — the same core is tuned by different regimes: US public-company and anti-bribery expectations, the EU whistleblowing directive (channel and confidentiality requirements), UK Bribery Act hospitality sensitivity, French Sapin II. The regime shapes retention, anonymity and reporting emphasis, not the core loop.
- **Industry overlays** — healthcare and life sciences (interactions with practitioners, transfer-of-value registers), financial services (conduct rules and personal-account dealing), government and contractors (disclosure and certification regimes).
- **Gift-register depth** — from a simple log to enforced limits with approvals, pre-submission impact preview and multi-currency normalization.
- **Third-party extension** — extending the code of conduct, attestations and training to suppliers and other third parties.
- **Culture measurement** — survey-based ethical-culture assessment and engagement analytics layered on the program data.
- **Delivery and segment** — cloud multi-tenant vs on-premises; enterprise vs small-business editions; language/localization depth; mobile-app depth.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Whistleblowing / Speak-up Platform | closest sibling; frequently bundled | centered on the *reporting channel + report record + reporter protection + case handling* for reporting others' misconduct; remove the disclosure/attestation/register machinery and keep the channel, and this becomes that type |
| Corporate Investigation Management | downstream sibling | deep investigation machinery (evidence, interviews, findings) — this type hands complex cases off; its reviews end in program-level determinations |
| Compliance Policy Management / Policy Management | upstream sibling | policy authoring, versioning and approval lifecycle; here policies are consumed as the standard being attested to and enforced through disclosure rules |
| Compliance Management Platform | neighboring sibling | regulatory obligations, controls and compliance-activity tracking; conduct/ethics is people-centered while compliance management is obligation-centered — the two coexist inside GRC suites, which is exactly why the seam matters |
| Governance Risk & Compliance Platform | umbrella | the suite layer that risk, audit, policy and ethics programs live inside; this type is the ethics/employee-conduct slice |
| Employee Relations Case Management / HR Case Management | adjacent sibling | HR-owned employee cases (grievances, discipline) vs conduct-integrity matters run under the ethics program; they share people data and sometimes case surfaces |
| Third-party Risk Management | extension neighbor | supplier codes, screening and supplier training borrow this type's attestation machinery, but third-party lifecycle management is a different center |
| Corporate LMS / Employee Learning Platform | capability neighbor | training delivery is one standard capability here; the learning platform's center (content, learners, courses) is not this type's center |

The boundary with the whistleblowing platform is the sharpest, because vendors bundle both sides under one "ethics and compliance" roof. The structural test: the reporting channel plus case handling alone is a speak-up platform; disclosures, attestations and program registers alone are Ethics & Conduct Management.

## Representative Products

- NAVEX (NAVEX One platform — Disclosure Management, EthicsPoint, policy and training products)
- SAI360 (GRC platform with Conflicts of Interest, Gifts & Hospitality, Disclosure Management, Code of Conduct, training and hotline modules)
- LRN (Catalyst suite — disclosures and attestations, interactive code of conduct, training delivery, program analytics; notably without a hotline module)
- Vault Platform (now part of Diligent — boundary-informing sample: a speak-up/misconduct platform without COI/gifts machinery)

The core model was checked against a speak-up-led product (Vault Platform) and against a major ethics-program platform without a hotline (LRN Catalyst) to avoid defining the type by one vendor's packaging; a former ethics-program specialist line (Convercent, acquired by OneTrust) is no longer merchandised as a distinct product family and was used only as market context.

## Sources

Research date: **2026-09-06**

- NAVEX — NAVEX One platform overview: https://www.navex.com/en-us/platform/
- NAVEX — COI Disclosure Management: https://www.navex.com/en-us/platform/coi-disclosure-management-software/
- SAI360 — platform overview: https://www.sai360.com/
- SAI360 — Gifts & Hospitality Compliance: https://www.sai360.com/solutions/compliance-management/gifts-and-hospitality
- LRN — Catalyst product suite: https://lrn.com/products/
- Vault Platform — product overview: https://www.vaultplatform.com/
- OneTrust — current product catalog (ethics-program line absent): https://www.onetrust.com/products/

> Sourcing limitation: evidence rests on official vendor product pages; vendor help-center / support documentation was not retrieved during this research pass. Operational specifics (numeric thresholds, default cycle frequencies, state names, plan-dependent capabilities) are therefore stated qualitatively or omitted, and single-product mechanics are marked as such in the text. Detailed product-by-product observations are recorded in the paired Research Notes.
