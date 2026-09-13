# Research Notes — Third-party Cyber Risk Platform

Research date: 2026-09-09
Slug: third-party-cyber-risk-platform
Directory location: §15 Cybersecurity, Identity & Trust

---

## Research Goal

Understand what a Third-party Cyber Risk Platform actually is as an Application Type: what its world is made of, who uses it, how vendor cyber risk flows through it, and where its boundaries sit against the four sibling Types that surround it in the directory (Security Ratings Platform, Third-party Risk Management, Supplier Risk Management, Security Compliance Platform).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: software for assessing, monitoring, and managing the **cybersecurity risk posed by an organization's third parties** (vendors, suppliers, service providers).
- Likely users: TPRM/VRM analysts, security teams, CISO office; secondarily procurement and business owners.
- Nearest neighbors: Security Ratings Platform (§15 sibling — the rating artifact), Third-party Risk Management (§11 — multi-domain relationship program), Supplier Risk Management (§10 — procurement-side supplier base risk), Security Compliance Platform (§15 — vendor security as one program object), Attack Surface Management (§15 — own attack surface).
- Known inherited flags from sibling passes (STATUS.md):
  1. security-ratings-platform (2026-09-09): keep-both RATIFIED from that side — "rating artifact + computation vs vendor-relationship lifecycle — all 5 sampled products bundle TPRM around the rating". This pass must ratify from this side.
  2. third-party-risk-management (2026-09-08): proposed seam — "ratings-as-machinery belongs there [§15], relationship-program center here [§11]; cyber-led TPRM deployments belong to §15".
  3. supplier-risk-management (2026-09-08): proposed seam — "subject universe + operating frame; cyber-led TPRM products belong to §15".
  4. security-compliance-platform (2026-09-09): "vendor-risk center vs vendor security as one program object".

## Research Questions

1. What is the unit of record — the vendor? the assessment? the finding?
2. How does a vendor enter the platform (manual add, bulk import, automatic discovery, intake form)?
3. What are the evaluation inputs — externally observed signals (scanning/ratings) vs vendor-attested evidence (questionnaires, documents, certifications)? Which are definitional?
4. What is the per-vendor output — a rating/grade, risk levels, findings?
5. What happens after evaluation — remediation with the vendor, exceptions/acceptance, reassessment?
6. What roles exist — buyer-side analysts vs vendor-side users (portals)?
7. How do tiering, portfolios, and monitoring cadence structure the program?
8. Where exactly is the seam vs Security Ratings Platform, vs TPRM (§11), vs Supplier Risk Management (§10), vs Security Compliance Platform?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies (ratings-led vs questionnaire-led vs merged) + different customer tiers (enterprise suites vs self-serve).

| Product | Philosophy | Customer tier | Role in sample |
|---|---|---|---|
| SecurityScorecard | ratings-led vendor cyber risk platform (rating + vendor program modules) | enterprise | core sample |
| BitSight | ratings-led origin; Continuous Monitoring + VRM as distinct applications | enterprise | core sample |
| Panorays | cyber-led TPCRM: questionnaires + external attack surface merged into one rating | mid-market/enterprise | core sample |
| UpGuard | ratings + vendor monitoring + remediation/exceptions; self-serve pricing pole | SMB→enterprise | core sample |
| Prevalent (Mitratech) | multi-domain TPRM (financial/ESG/regulatory/reputational/cyber) | enterprise | boundary probe (§11 pole) |

## Sources

All fetched 2026-09-09. Tier-1 (official operational documentation) unless noted.

SecurityScorecard:
- Help Center root: https://support.securityscorecard.com/
- Third-party risk category: https://support.securityscorecard.com/hc/en-us/categories/36963626715803-Third-party-risk
- Vendor management category: https://support.securityscorecard.com/hc/en-us/categories/36996255583003-Vendor-management
- What is third party monitoring? — /hc/en-us/articles/360059302392
- How do I perform a vendor risk assessment? — /hc/en-us/articles/360059720011
- Manage your vendors using All Companies — /hc/en-us/articles/27417932865691
- Use Action Plans to collaborate with your vendors — /hc/en-us/articles/16394329899931
- About the vendor intake workflow (Early access) — /hc/en-us/articles/53914262300571

BitSight:
- Knowledge Base root: https://help.bitsight.com/
- Continuous Monitoring category: https://help.bitsight.com/hc/en-us/categories/4410044050839-Continuous-Monitoring
- Bitsight VRM category: https://help.bitsight.com/hc/en-us/categories/21299763408407-Bitsight-VRM
- VRM App: Vendors — /hc/en-us/articles/17025693904151
- Vendor Profile: Findings — /hc/en-us/articles/21976651568407
- Vendor Profile: Tiering — /hc/en-us/articles/17025827189015
- Life Cycle Stages — /hc/en-us/articles/360040099093

Panorays:
- Homepage (self-labels "Third-Party Cyber Risk & Attack Surface Mgmt"): https://panorays.com/
- How It Works: https://panorays.com/how-it-works/
- Remediation Plans: https://panorays.com/platform/remediation/

UpGuard:
- Homepage: https://www.upguard.com/
- Vendor Risk product page: https://www.upguard.com/product/vendor-risk
- Remediation & Exceptions: https://www.upguard.com/product/vendor-risk/risk-remediation
- Help center exists at https://help.upguard.com/en/ (not deep-fetched; product pages used as Tier-2)

Prevalent (boundary probe, Tier-2 product page):
- https://www.prevalent.net/ (now Mitratech Prevalent; multi-domain TPRM positioning)

Sourcing limitations:
- UpGuard help-center articles not deep-fetched; operational detail asserted only from official product pages (Tier-2). Claims kept at product-page strength.
- Panorays evidence is from official product/marketing pages (Tier-2); no operational help-center articles fetched. Precise mechanics (e.g., exact rating scale, exact plan algorithm) not asserted.
- Prevalent fetched at homepage level only; used solely as a boundary probe, no operational claims.
- BitSight rating scale, SecurityScorecard score ranges: not asserted (methodology pages not fetched).

---

## Product A — SecurityScorecard

### Key observations (Layer A — directly observed, official help center)

**Structure of the help center itself is evidence**: separate top-level categories "Third-party risk — Monitor and manage vendor risk across your ecosystem" and "Vendor management — Track, assess, and collaborate with your vendors", beside "Security posture — Understand scores, findings, and risk signals" (the ratings artifact side).

**Vendor record ("All Companies" / Vendor System of Record)**:
- "The All Companies page lists every company your organization is monitoring, including both partially monitored and fully monitored companies."
- Vendor details pane tabs: Vendor details / Requests ("invitations, questionnaires, action plans, and evidence requests sent by anyone at your organization") / Contacts / Notes.
- Default vendor fields: Business impact (Critical/High/Medium/Low), Data types shared (PII/PHI/Financial/Sensitive), Risk (Critical/High/Medium/Low/None), Assigned team member, Business unit, Vendor ID, External Vendor ID, **Lifecycle status (New, Assess, Respond, Monitor)**, Contract end date, Last assessed date, Portfolios, Custom tags. Custom vendor fields supported.
- Monitoring status: partial vs full monitoring; "If a company is partially monitored, you can start full monitoring by adding it to a portfolio."
- Portfolio permissions: "you will only see companies included in the portfolios to which you have access. Admins can view the complete list."

**Vendor intake workflow (Early access)**:
- Intake form shared with internal business partners; submissions land in an Intake tab; answers "populate the Vendor System of Record (VSOR) automatically".
- Inherent risk scoring from intake answers (points per answer, normalized 0–100) → four risk levels (Low/Medium/High/Critical) → questionnaire template mapped per tier → "the platform tier an incoming vendor and send the right assessment automatically".
- Submitted vendors added as partially monitored; actions: add contacts, add to portfolio, send questionnaire, remove.

**Questionnaires**: send to vendor, build custom templates, review vendor responses; "Last assessed date" field tracks the last completed assessment from the questionnaire module.

**Action Plans (vendor-collaborative remediation)**:
- "Action Plans enable SecurityScorecard users to work with vendors to improve security."
- Targets: overall score/letter grade, factor scores, or resolution of particular issues.
- "When sent, vendors receive an email... Those with SecurityScorecard accounts can log in directly; others receive a link to create a free account."
- Progress: percent complete, issues by status (Open, Under review, Resolved); due date; per-plan and per-issue chat; "Accept as resolved" (entire plan, with reason saved to the conversation); archive/delete.
- Tabs "Created by us" (creator) / "Assigned to us" (vendor).

**Other**: Evidence Locker ("Check compliance for your organization or third parties"); Automatic Vendor Detection ("Find which vendors use pixel and cookie tracking", "Manage supply chain risk with Automatic Vendor Detection"); breach activity column on vendor rows; MAX managed-service tier with a vendor portal.

**Conceptual articles**: third-party monitoring = "continuous observation of partner security postures"; vendor risk assessment documentation spans qualitative (service type, data access, data sensitivity) and quantitative (financial solvency, contract size, IT Security Ratings) — the vendor lifecycle framed as qualifying → engagement → managing delivery → managing finances → terminating.

## Product B — BitSight

### Key observations (Layer A — directly observed, official knowledge base)

**Two distinct applications for this Type**:
- **Continuous Monitoring (CM)**: "identify, quantify and mitigate the inherent risk in sharing sensitive data with vendors and business partners. This automated service analyzes, rates, and monitors the security performance of third parties, all from outside the company."
- **Bitsight VRM**: "an all-in-one, vendor risk management experience."

**CM structure**: Portfolio Risk Matrix, Risk Analytics, Risk Program Setup (**Tiers** on a Tier Settings page; Client/Vendor Access Program links), Portfolio Risk (Dark Web, Compare Companies, Critical Assets, Risk Summaries), Vendor Risk (**Vendor Discovery table** — subscribe/unsubscribe companies), **4th Party Risk** (service providers used by third parties; add cloud services to portfolio), Vulnerability Detection, Collaboration, Alerts, Portfolio Management (folders, subscriptions).

**Life Cycle Stages** (CM): "represent the intersection between Bitsight and your third party risk management (TPRM) program" — **Onboarding** ("due diligence process for establishing a new Third Party"), **Monitoring** ("ongoing monitoring of a Third Party's security posture to identify changes and prioritize remediation"), **Re-Assessment** ("periodic due diligence process for an existing Third Party's security posture to establish a new baseline").

**VRM vendor record**: Vendors page tabs **Managed / Monitored / Incoming Shares** "depending on the connection status"; add vendor by domain, bulk add, vendor connection workflow; revoke connection. Fields: Company, Due Date ("when the vendor is expected to fulfill the requirements"), Life Cycle, Primary Domain, Requirements ("the vendor's progress in meeting requirements"), Review Year, Tags, **Vendor Scores: Impact / Risk / Trust**.

**Vendor Profile**: Overview, **Tiering** ("manage vendor tags, which contain requirements for the vendor"; manual Trust Score adjustment with reason — e.g. unrecorded breach, sanctions), Internal Questionnaires, **Requirements**, **Findings**, Security Profile, Contacts, Internal Documents, Instant Insights.

**Findings (the resolution loop)**:
- Per-vendor findings with Criticality (None/Low/Medium/High/Critical), Reported On (source — can be a questionnaire: Questionnaire/Category/Question/Answer/Comments/Attachments), **Review Status (Open / 90 Days + Remediation / Remediated / Compensating Controls / Will Not Remediate)**, **"Will Remediate By..." ("the vendor's response on remediating the finding")**, Messages, Attachments ("attachments that the vendor uploaded"), Internal Notes.
- Findings can be created manually or generated from Framework Intelligence results / questionnaires.

**Third Party Collaboration**: "Invite Third Parties to Collaborate in the Bitsight Platform"; best-practices and non-response articles exist (vendor participation is a real, managed surface).

**Trust Management Hub** (separate application): "commonly used questionnaire templates, a secure repository to store your..." (questionnaire/evidence exchange with vendors).

## Product C — Panorays

### Key observations (Layer A for self-labeling and lifecycle; Tier-2 product pages)

- Self-labels: "Third-Party Cyber Risk & Attack Surface Mgmt", "Third-Party Cyber Risk. Solved.", "End-to-End Vendor Risk Management", "TPCRM platform" (blog/resources repeatedly use "TPCRM").
- **Platform modules**: Assessment (Risk DNA Cybersecurity Posture, External Attack Surface, Cybersecurity Questionnaires, **Smart Inventory** — "centralized third-party inventory with context"), Engagement (Communication, Remediation), Monitoring (Cybersecurity Monitoring, Reporting & Dashboards, Regulatory Compliance, Portfolio Management), Security Program (Integrations, Professional Services, Trust Center).
- **Merged risk rating**: "Panorays evaluates risk across four key areas: AI-powered questionnaires to capture vendor controls and compliance, external attack surface assessments to detect security gaps, inherent risk based on each vendor's business and technology profile, and your organization's risk policies... merged natively in one platform, providing a single, trusted risk rating."
- **Lifecycle (How It Works)**: 01 Analysis → 02 Engagement ("easy collaboration and rectification of issues... between the organization and third party") → 03 Remediation ("You and your suppliers can challenge or validate findings, receive instructions on how to mitigate cyber gaps and report progress") → 04 Approval ("see which suppliers do not adhere to your company's security policies") → 05 Monitoring ("continuously uncovers and evaluates the supplier... live alerts about any security changes or breaches").
- **Remediation plans**: "Panorays generates a prioritized remediation plan for each vendor with mitigation steps for gaps in both the Smart Questionnaire™ and external attack surface assessment"; customer sets the goal ("if the Cyber Risk Rating is 'bad', you can set a goal to raise it to 'good'"); suppliers receive prioritized tasks; "As your suppliers progress with their remediation plans, the changes are automatically detected and reflected."
- Tiering: "tier vendors, set assessment frequency" (risk-based approach); nth-party visibility ("Panorays AI uncovers hidden third-, fourth-, and nth-party relationships").
- Regulatory compliance checks (DORA use case), Trust Center (shareable proof of security posture).

## Product D — UpGuard

### Key observations (Layer A for product-page structure; Tier-2)

- Vendor Risk self-label: "The holistic TPCRM platform that delivers continuous vendor insights, 360-degree assessments, and efficient AI-powered workflows."
- Product nav: Vendor Risk Assessments / **Vendor Discovery & Onboarding** / Security Questionnaire Automation ("pre-configured questionnaires (including NIST, ISO, SIG, and regional regulations)") / **Remediation & Exceptions** / Continuous Monitoring / Reporting & Program Oversight.
- **Remediation & Exceptions**: "Identifying vendor risks is only half the job. Track fixes to completion, govern exceptions within your risk appetite, and keep a clean, auditable record of every decision." "fixes, waivers, and approvals stay connected to the same findings that uncovered them... one continuous flow from detection to documented closure." "Track the status of every remediation, waiver, and exception in real time – with clear owners, due dates, and supporting evidence tied to the original finding. Automated reminders keep work moving, and on-demand scanning detects when issues are resolved, so you don't wait on vendor updates. A single, traceable history shows what's done, why it was done, and what's still open."
- Ratings: "Objective security ratings... updated multiple times per day"; continuous monitoring: "Daily scanning means you stay up to date on the security changes that matter, even between assessments."
- Sibling products (out of this Type's core): Breach Risk (own attack surface), User Risk, Trust Exchange (vendor-side trust center/questionnaire AI), Risk Automations; "Security ratings" listed as a separate product line.

## Product E — Prevalent (boundary probe, §11 pole)

### Key observations (Layer A homepage; used only for boundary calibration)

- Self-labels: "Third-Party Risk Management (TPRM) Software"; "Mitratech's unified, automated third-party risk management (TPRM) solution".
- **Multi-domain monitoring**: "Monitoring covers financial health, cyber security, ESG, regulatory actions, and reputational signals" — cyber is one domain among five.
- Full vendor lifecycle: Sourcing & Selection (RFP/RFI with "demographic, 4th-party, ESG, business, reputational, financial, and cyber intelligence"), Intake & Onboarding, SLA & Performance Management, Inherent Risk Scoring, Monitor & Validate, Assess & Remediate (800+ templates), Offboarding & Termination.
- Vendor intelligence networks ("thousands of completed, standardized assessments"), managed services, vendor portals/messaging.
- Interpretation: this is the §11 TPRM Type's center (relationship program across domains), not the §15 cyber-lens center. Recorded as a Product Mismatch probe, not a core sample.

---

## Cross-product Comparison

| Dimension | SecurityScorecard | BitSight | Panorays | UpGuard | Prevalent (probe) |
|---|---|---|---|---|---|
| Standing vendor population | All Companies / VSOR + Portfolios | VRM Vendors (Managed/Monitored/Incoming Shares) + CM portfolio | Smart Inventory | Vendor Discovery & Onboarding | vendor records (single source of truth) |
| Relationship context on vendor | business impact, data types shared, owner, business unit, lifecycle status, contract end | Due Date, Life Cycle, Review Year, tags, connection status | business impact indicators, context | vendor profile | firmographic/contract/SLA data |
| External-signal evaluation | scorecard per company (score, factors, findings, breach activity) | Continuous Monitoring ("analyzes, rates, and monitors... from outside the company") | External Attack Surface assessments | security ratings "updated multiple times per day", daily scanning | Vendor Threat Monitor (one of five domains) |
| Vendor-attested evaluation | questionnaires + Evidence Locker | VRM questionnaires + Trust Management Hub + Framework Intelligence | Smart Questionnaire™ | questionnaire automation (NIST/ISO/SIG) | 800+ assessment templates |
| Merged per-vendor standing | score + vendor Risk field | Vendor Scores (Impact/Risk/Trust) | single Cyber Risk Rating (4 factors merged) | security profile + ratings | inherent + residual risk scores |
| Tiering | intake inherent-risk tiers (Low/Med/High/Critical) → template per tier | Tier Settings page; vendor tags carrying requirements | tier vendors, set assessment frequency | (not observed on fetched pages) | inherent risk scoring tiers vendors |
| Resolution loop | Action Plans (vendor-collaborative; accept-as-resolved with reason) | Findings review status (Remediated / Compensating Controls / Will Not Remediate) + "Will Remediate By" (vendor's response) | remediation plans sent to suppliers; challenge/validate findings; auto-detected progress | remediation + waivers/exceptions + auditable record + re-scan verification | assess & remediate stage |
| Vendor-side surface | vendor email/login/free account; MAX vendor portal | Third Party Collaboration invites; vendor uploads attachments, sets remediation date | suppliers receive plans, report progress | (vendor updates referenced) | vendor portals, messaging |
| Monitoring cadence | continuous (partial vs full monitoring) | continuous CM + periodic Re-Assessment stage | continuous + live alerts | daily scanning + on-demand re-scan | continuous (one of five domains) |
| Discovery | Automatic Vendor Detection (pixel/cookie) | Vendor Discovery table | AI nth-party discovery | Vendor Discovery & Onboarding | (sourcing-stage intelligence) |
| nth-party | (supply-chain framing) | 4th Party Risk application | third/fourth/nth-party AI mapping | (not observed) | 4th-party intelligence in sourcing |
| Program reporting | Reporting Center, TPRM dashboard | Portfolio Risk Matrix, Risk Analytics, Executive Summary dashboards | Reporting & Dashboards | Reporting & Program Oversight | Risk Analytics & Insights |

### Cross-product commonality (Layer B)

Across all four core products, without exception:
1. A standing, managed population of third-party/vendor records with relationship context.
2. Per-vendor security evaluation producing a comparable standing (rating/score/risk level), assembled from evidence — always a mix of externally observed signals and/or vendor-attested evidence.
3. A managed resolution loop: evaluation results become tracked findings/risks resolved through decisions (remediate / compensating controls / accept / waive) with the vendor as the dominant counterpart, and a recorded closure.

Across all four: vendor tiering by criticality/inherent risk; portfolio organization; continuous or periodic refresh of the evaluation; program-level reporting. (Layer B — common mature structure.)

Vendor-side participation surfaces (portal/invitations/plan responses) exist in all four core products in some form — dominant mechanism, but implemented very differently (free account vs connection status vs plan tasks vs email updates).

---

## Canonical Abstraction

### L0 — Defining Invariant

The organization's system of record for the cybersecurity risk posed by its third parties. Three jointly-held structures:

1. **The third-party population under cyber assessment** — persistent identified records of external vendors/service providers held as the standing monitored population, each carrying relationship context (business criticality/impact, data shared, owner, lifecycle stage). Remove → a ratings feed or a questionnaire tool with no managed vendor population.

2. **Per-vendor security evaluation producing a comparable standing** — each vendor carries a security evaluation assembled from evidence about that vendor's security posture — externally observed signals (attack-surface scanning/ratings) and/or vendor-attested evidence (questionnaires, documents, certifications) — assessed against the vendor's business context, yielding a per-vendor risk standing (rating/grade/level). Remove → vendor inventory, or raw signal feeds with no evaluation.

3. **The managed decision-and-resolution loop over vendor cyber risk** — evaluation results resolve into recorded decisions (remediate with the vendor, compensate, or accept) and tracked actions carried to a recorded closure, with the vendor party as the dominant counterpart and the trail retained for audit. Remove → one-shot assessment report or a monitoring feed nobody acts on.

Jointly-held load-bearing:
- 1 alone = vendor inventory / vendor CRM
- 2 without 1 = ratings feed / one-off assessment service (Security Ratings Platform territory or an assessment service bureau)
- 3 without 1+2 = ticketing / remediation tracker
- 1+2 without 3 = assessment + monitoring with no management loop (the ratings-artifact pole)
- 1+3 without 2 = vendor management with no cyber evaluation
- 2+3 without 1 = ad-hoc assessments with no standing program

### L1 — Common Mature Structure

- Continuous monitoring of vendor posture (external scanning, breach intelligence, alerts) — with periodic re-assessment as the alternative cadence (BitSight's own Re-Assessment stage)
- Vendor tiering by criticality/inherent risk, driving assessment depth and frequency
- Questionnaire engine with template libraries (SIG/NIST/ISO-class frameworks) and response review
- Vendor-facing participation surface (portal, invitations, plan tasks, evidence upload, remediation-date commitments)
- Portfolio/folder organization with team-scoped permissions
- Vendor discovery (automatic detection of vendors in use; nth/4th-party mapping)
- Program reporting: portfolio risk views, executive/board reporting, audit-ready records
- Evidence/document repository; breach/incident alerts mapped to affected vendors

### L2 — Variant / Optional Structure

- Evidence-channel mix: external-observation-led (ratings-led vendors) vs vendor-attestation-led (questionnaire-led) vs merged — the primary variant axis
- Rating artifact form: standardized platform-scale grade (letter/numeric) vs customer-relative risk levels vs merged composite
- Regulatory-compliance mapping depth (DORA-class financial-services regimes)
- Trust center (vendor-side self-attestation publishing)
- Managed-services layer (vendor-run program operations)
- Intelligence networks / shared completed assessments (marketplace)
- Contract/SLA tracking depth; cyber-insurance use cases; M&A/subsidiary evaluation use cases

### L3 — Vendor-specific (Research Notes only)

- SecurityScorecard: VSOR naming, Action Plans, Score Planner, Evidence Locker, MAX vendor portal, partial-vs-full monitoring, Automatic Vendor Detection via pixel/cookie tracking
- BitSight: risk vectors, Trust Score manual adjustment, connection statuses (Managed/Monitored/Incoming Shares), Trust Management Hub as separate app, 4th Party Risk application, Client/Vendor Access Program
- Panorays: Risk DNA, Smart Questionnaire™, remediation-plan algorithm ("least number of steps"), Cyber Risk Rating naming
- UpGuard: Trust Exchange, Risk Automations, Breach Risk/User Risk sibling products, MFQ multi-framework questionnaire

### Rejected Findings (considered, not promoted)

- "Continuous monitoring is definitional" — REJECTED: BitSight's own lifecycle includes periodic Re-Assessment as a first-class stage; questionnaire-led programs run periodic cycles. The invariant is the standing evaluation refreshed over time, not continuous monitoring.
- "External attack-surface scanning is definitional" — REJECTED: questionnaire-led evaluation (Prevalent's assessment core; BitSight VRM's questionnaire findings) satisfies the Type without external scanning. Scanning is the dominant modern evidence channel, not the invariant.
- "A standardized letter/numeric rating is definitional" — REJECTED: customer-relative risk levels (SecurityScorecard's vendor Risk field; BitSight's composite scores) and merged composites (Panorays) all satisfy; the invariant is a comparable per-vendor standing.
- "Vendor portal is definitional" — REJECTED: participation is implemented as free accounts, connection statuses, plan tasks, or email threads; the invariant is the resolution loop with the vendor as counterpart, not a specific portal surface.
- "Multi-domain risk (financial/ESG/legal) is part of this Type" — REJECTED: that is the §11 TPRM center (Prevalent probe). Cyber posture is this Type's object of evaluation.
- "Contract management / SLA tracking is definitional" — REJECTED: context fields only (SecurityScorecard contract end date; Prevalent's SLA module is the §11 pole's depth).

### Historical / Market-Sample Check (§24)

Would older, regional, or differently positioned products still fit?
- Pre-ratings-era practice: vendor security questionnaires + evidence files + remediation letters tracked in spreadsheets — satisfies all three legs (population, evaluation from vendor-attested evidence, resolution loop) with no external scanning, no cloud, no AI. The external-scanning machinery is era-current (L1/L2), not definitional.
- Questionnaire-led regional products (e.g., European DORA-driven TPCRM tools, assessment-led vendors) fit via the vendor-attestation evidence channel.
- Ratings-only feeds (pure rating artifact with no vendor program) fail leg 1+3 — correctly excluded as Security Ratings Platform territory.
- The definition does not depend on the current ratings-led dominant implementation. Check passed.

---

## Boundary Findings

### vs Security Ratings Platform (§15 sibling) — keep-both RATIFIED from this side

- Ratings platform: the rating artifact + computation for any organization (own posture, third parties, insurance portfolios, national CERTs); unit of record = rated organization + standardized rating on the platform's scale; no vendor-relationship lifecycle, no resolution loop.
- Third-party cyber risk platform: the vendor-relationship program; unit of record = the vendor relationship carrying cyber evaluation + resolution state; ratings are one evidence input.
- Remove the vendor population and resolution loop from this Type → a ratings platform. Remove the rating artifact's standalone generality from the ratings Type → it collapses into this Type's evidence channel.
- Corroboration: the security-ratings pass already RATIFIED keep-both ("rating artifact + computation vs vendor-relationship lifecycle — all 5 sampled products bundle TPRM around the rating"). This pass observes the same bundling from the other side (SecurityScorecard and BitSight both sell the rating artifact AND vendor program modules as distinct help-center categories/applications).

### vs Third-party Risk Management (§11) — keep-both RATIFIED (discharges TPRM pass's flag)

- TPRM: the multi-domain third-party relationship program — relationship inventory + evaluation across financial, legal, compliance, ESG, operational, and cyber domains; center = the relationship and its program.
- Third-party cyber risk platform: the cyber lens — the object of evaluation is the vendor's security posture; cyber signals, security controls, and vendor security remediation are the center.
- Seam (subject universe + operating frame, per the supplier-risk pass's proposal): what the platform evaluates (vendor security posture vs the relationship's multi-domain risk) and which program owns it (security/CISO office vs enterprise/procurement risk program).
- "Cyber-led TPRM deployments belong to §15" — RATIFIED: a deployment bought primarily to manage vendor security (Panorays, UpGuard Vendor Risk, SecurityScorecard/BitSight vendor-risk modules) is this Type even when marketed as TPRM; a deployment bought to run the whole relationship program (Prevalent, OneTrust TPRM-class) is §11 even when it includes cyber signals.
- Prevalent probe confirms the §11 pole: five monitoring domains with cyber as one; full sourcing→offboarding lifecycle; the cyber content is one input among several.

### vs Supplier Risk Management (§10) — keep-both RATIFIED (discharges supplier-risk pass's flag)

- Supplier risk management: procurement-side; subject = the supplier base (existing + prospective) with supply-market monitoring and disruption; operating frame = procurement/supply-chain continuity.
- Third-party cyber risk platform: security-side; subject = vendors as cyber-risk bearers; operating frame = the security program.
- Overlap zone is real (both monitor external entities, both produce per-entity risk standings) but the subject universe (supplier base vs third-party population under cyber assessment) and the operating frame (supply continuity vs security program) keep them separate.

### vs Security Compliance Platform (§15) — keep-both RATIFIED (discharges compliance pass's flag)

- Security compliance platform: the organization's framework-compliance program; third-party/vendor security appears as one program object (evidence the org collects about vendors for its own compliance).
- Third-party cyber risk platform: the vendor's security posture is the center, evaluated and managed per vendor.
- Remove the per-vendor evaluation-and-resolution center → vendor security becomes one evidence object inside a compliance program.

### vs Attack Surface Management (§15) — adjacent

- ASM: the organization's own external attack surface as the analyzed subject.
- This Type: third parties' attack surfaces as one evidence channel feeding per-vendor evaluation. (Consistent with the ratings pass's note that ratings consume ASM-like signals as input.)

### vs Vendor/procurement management — adjacent

- Vendor master data, contracts, SLAs, sourcing appear here only as relationship context fields (SecurityScorecard's contract end date, business unit; Prevalent's SLA module at the §11 pole). The center is cyber evaluation + resolution, not the commercial relationship.

---

## Uncertainties

1. UpGuard's operational detail (help-center level) not fetched; remediation/exception mechanics asserted from product pages only. Claims kept at product-page strength.
2. Panorays' exact rating composition and remediation-plan algorithm not verified beyond vendor's own description (marketing-adjacent pages); no precise mechanics asserted.
3. Whether a pure questionnaire-led product with NO external scanning and NO vendor portal (e.g., an email-and-spreadsheet-era program) exists as a commercial software product in the sample — not directly sampled; the leg structure allows it and the historical check argues it fits, but the modern commercial population appears to always include at least one digital vendor-facing surface. Held as an uncertainty, not asserted either way.
4. The exact market share / category naming ("TPCRM" vs "vendor cyber risk" vs "third-party cyber risk management") varies by analyst; Panorays/UpGuard self-label "TPCRM", SecurityScorecard/BitSight use "third-party risk"/"vendor risk" for the module while the rating artifact carries the brand. No taxonomy change proposed — the directory leaf name is serviceable.
5. BitSight's Trust Management Hub and UpGuard's Trust Exchange are vendor-side trust/questionnaire products — they sit on the seam between this Type (buyer side) and the vendor's own posture proof. Not resolved as separate Types here; recorded for the taxonomy maintainers if a "Trust Center" leaf ever gets processed.

## Final Synthesis

The Third-party Cyber Risk Platform is the buying organization's vendor-cyber-risk system of record. Its world has three load-bearing structures held jointly: (1) the standing third-party population under cyber assessment — vendor records carrying relationship context; (2) per-vendor security evaluation producing a comparable standing, assembled from externally observed signals and/or vendor-attested evidence against the vendor's business context; (3) the managed decision-and-resolution loop that turns evaluation results into recorded decisions and tracked actions — remediation with the vendor, compensating controls, or acceptance — carried to recorded closure with an audit trail.

Everything else the market ships — continuous monitoring, tiering machinery, questionnaire engines, vendor portals, discovery, nth-party mapping, compliance mapping, trust centers, managed services — is common mature structure or variant depth, not the definition. The Type's center of gravity is the cyber lens on vendor relationships: what it evaluates is the vendor's security posture, and what it produces is a managed, auditable resolution of vendor cyber risk inside the buying organization's security program.

All four inherited sibling flags are discharged from this side: keep-both vs Security Ratings Platform (rating artifact vs vendor-relationship program), keep-both vs TPRM §11 (cyber lens vs multi-domain relationship program; cyber-led deployments belong here), keep-both vs Supplier Risk Management §10 (security operating frame vs procurement/supply frame), keep-both vs Security Compliance Platform (vendor-risk center vs vendor security as one program object).
