# Research Notes — Third-party Risk Management

Research date: **2026-09-08**

---

## Research Goal

Understand what a Third-party Risk Management (TPRM) application actually is as an Application Type: what the "third party" object is, how relationships enter the system, how risk is evaluated per third party, what the program loop looks like (assessment → decision → monitoring → disposition), who the users are (including the third parties themselves), and where the Type's boundary sits against its neighbors — especially Governance Risk & Compliance Platform (umbrella), Supplier Risk Management (§10), Third-party Cyber Risk Platform (§15), Due Diligence Platform (§11 sibling), Vendor Management System (§9), and Contract Lifecycle Management (§11).

This leaf carries two recorded joint-review flags from prior passes that this research must respond to:

1. **From governance-risk-compliance-platform (§11, processed)**: TPRM was flagged as a "child-module pattern" leaf — all five sampled GRC platforms (Archer, LogicGate, Optro, Diligent, LogicManager) ship third-party risk as a module. Candidate outcomes: keep-both or documented containment.
2. **From supplier-risk-management (§10, processed 2026-09-08)**: flagged as "the sharpest live seam." Proposed seam: subject universe + operating frame. TPRM is GRC-side (any third party, engagement/contract-centric assessment-and-acceptance cycles); Supplier Risk Management is procurement-side (buyer's supplier base as standing portfolio, continuous supply-market monitoring, disruption response, sourcing/onboarding integration). Cyber-led TPRM products belong to Third-party Cyber Risk Platform (§15).

---

## Initial Boundary (pre-research hypothesis)

- **What**: an organization-side system for managing the risk arising from relationships with external third parties (vendors, suppliers, service providers, partners, contractors) — inventory, tiering, due-diligence assessment, risk acceptance, ongoing monitoring, lifecycle offboarding.
- **Who**: third-party risk / vendor risk managers (GRC or infosec), business owners of relationships, procurement (secondary), and the third parties themselves (assessment response).
- **Nearest neighbors**: GRC Platform (umbrella), Supplier Risk Management (procurement-side), Third-party Cyber Risk Platform (cyber lens), Due Diligence Platform (investigation service), VMS (workforce supply), CLM (contracts).
- **Unknowns**: whether continuous external monitoring is definitional or common-mature; how central the third-party-facing portal is; whether risk acceptance is a formal first-class structure; relationship to procurement onboarding.

---

## Research Questions

1. What object represents the third party (entity? relationship? engagement/contract?) and what does its record hold?
2. How does tiering / criticality work, and what does it drive?
3. What does due diligence look like — questionnaires, document requests, evidence, external intelligence feeds?
4. What is the assessment lifecycle — states, review, scoring, acceptance/approval decision?
5. How does ongoing monitoring work — periodic reassessment vs continuous external signals? What happens on an incident?
6. Who uses it — internal roles and third-party participation? Is there a vendor portal?
7. What risk domains are covered, and is there a standard domain set?
8. What happens to findings — issues, remediation, tracking to closure?
9. What regulatory regimes anchor the programs (DORA, NIS-2, LkSG, APRA CPS 230, financial-services outsourcing guidance)?
10. Where do the boundaries sit: GRC umbrella, supplier risk, cyber TPRM, due diligence services, CLM, VMS?

---

## Representative Products

| Product | Vendor / family | Pole | Why selected |
|---|---|---|---|
| Prevalent (TPRM) | Mitratech | pure-play TPRM, full lifecycle, threat-intelligence-led | market-representative pure-play; SPARK Matrix Vendor Risk Management Leader (vendor-cited) |
| Third-Party Risk Management | OneTrust | compliance/privacy-suite pole, assessment-first | suite philosophy different from pure-plays; large mid-to-enterprise customer base |
| Vendor Risk Management (VRM) | ProcessUnity | pure-play, assessment-workflow-led, pre/post-contract framing | financial-services-heavy, configurability philosophy; Forrester Wave™ TPRM Platforms Leader (vendor-cited) |
| Third-Party Risk Management (3rdRisk) | Diligent | GRC-suite pole, newest AI-native line | suite module that is itself a named product; Gartner MQ TPRM Tools Leader (vendor-cited) |

Cross-reference (from prior passes, B-layer): the GRC pass (2026-09-08) observed Archer, LogicGate, Optro, Diligent (pre-3rdRisk), LogicManager all shipping third-party risk modules; Diligent's suite also carries separate "Third Party Manager" (compliance-led monitoring) and "Third-Party Risk Intel" (agentic screening) products beside 3rdRisk — evidence that the TPRM subject matter is distinct enough inside one suite to split across multiple named products.

---

## Sources

Fetched 2026-09-08 (all official vendor product pages; single fetch each, all successful):

- Mitratech Prevalent — https://www.prevalent.net/platform/vendor-risk-management/ (redirects to Mitratech Prevalent product page; includes product FAQ)
- OneTrust — https://www.onetrust.com/solutions/third-party-management/ (solution page; `/products/third-party-risk/` is 404 — current URL taxonomy uses "Third-Party Management")
- ProcessUnity — https://www.processunity.com/products/vendor-risk-management/
- Diligent — https://www.diligent.com/products/third-party-risk-management/

Attempted and abandoned per network rules:

- ServiceNow TPRM — product page timed out once; docs.servicenow.com is a JavaScript application (no content reachable). **No ServiceNow-specific claims are made.**
- Archer — guessed URL 404; not retried. Archer's third-party module is known from the prior GRC pass (B-layer) only.

Prior-pass cross-references: research/governance-risk-compliance-platform.md, research/supplier-risk-management.md, research/ethics-conduct-management.md (STATUS.md flags).

> Sourcing limitation: all four sampled products were observed at product-page/FAQ depth, not help-center depth. Evidence below is therefore A-layer at the capability/structure level; precise operational details (state names, numeric limits, scoring formulas, plan gating) were not verified and are **not** asserted.

---

## Product Observations

### Mitratech Prevalent (pure-play TPRM) — A-layer

- Self-definition (FAQ): "Third-party risk management is the process of identifying, assessing, and mitigating risks that arise from working with external vendors, suppliers, and partners. It covers the full vendor lifecycle: sourcing, onboarding, ongoing monitoring, and offboarding." Also: "purpose-built for TPRM, not a module within a broader GRC solution."
- Lifecycle stage map (product page sections): **Sourcing & Selection** (centralize RFP/RFI distribution; add demographic, 4th-party, ESG, business, reputational, financial, cyber intelligence) → **Intake & Onboarding** (intake form available to all internal users; single source of truth per vendor centralizing contracts and firmographic, business, financial, reputational, compliance, ESG, cyber risk data) → **SLA & Performance Management** (SLAs, KPIs, KRIs tracked centrally) → **Inherent Risk Scoring** (tier and categorize all vendors; inherent and residual risk scores from likelihood/impact of security, compliance, operational incidents) → **Monitor & Validate** (correlate assessments with continuous monitoring of cyber threats, business risks, financial problems, regulatory findings, reputational concerns) → **Assess & Remediate** (library of 800+ assessment templates; AI-completed assessments; built-in recommendations; escalation to human review) → **Offboarding & Termination** (contract assessments and offboarding procedures to reduce post-contract exposure) → **Risk Analytics & Insights** (dashboards, executive reporting).
- **Vendor participation**: vendor portals, real-time messaging and status updates, standardized digital questionnaires — "vendors can submit documentation and track their progress through a dedicated portal."
- **Continuous monitoring engine** (Vendor Threat Monitor): 30,000+ adverse media/news sources, 1.8M+ PEP profiles, 1,000+ enforcement/sanctions lists (vendor-claimed numbers); AI false-positive detection; monitoring spans financial health, cyber security, ESG, regulatory actions, reputational signals.
- **Incident response**: "Technology Tags" — when a technology provider has an outage/security incident, the solution cross-references vendor technology-dependency profiles against live incident intelligence, surfaces affected vendor relationships, and initiates configured remediation workflows (CrowdStrike outage July 2024 cited as example).
- **Assessment exchange**: "vendor intelligence networks" — thousands of pre-completed standardized assessments available on demand to complement 1:1 assessments.
- **Managed services**: expert-managed services to run the TPRM program on the customer's behalf (product posture, not capability).
- **Native CLM module** (Contract Essentials): AI-assisted contract risk analysis, e-signature integration, executed contracts stored against vendor records.
- Signs-of-outgrown-spreadsheets framing: too many vendors chasing assessments; risk data scattered in inboxes/Excel/file cabinets; regulatory pressure to demonstrate third-party due diligence to auditors; unclear vendor ownership; rising third-party incidents.

### OneTrust Third-Party Risk Management (compliance-suite pole) — A-layer

- Positioning: "Automate third-party risk assessment and lifecycle management to build a more resilient, secure, and scalable third-party ecosystem." Featured product: "Third-Party Risk Management — manage and automate the end-to-end third-party lifecycle, including onboarding, assessment, risk treatment, reporting, monitoring, and offboarding." (Solution line is branded "Third-Party Management"; the TPRM product is the core of it.)
- **Intake & onboarding automation**: automate intake screening against risk-rating and compliance databases; "contextually tier and triage third parties to guide workflow priority and assessment depth"; AI ingestion of external risk evidence; fast-track "low-risk" third parties through auto-approval workflows.
- **Issues & risks**: "Assess third parties across multiple risk domains to evaluate security, privacy, ethics, compliance, and more"; assign owners and track issues, risks, and tasks across internal and external teams; integrated assessments streamline third-party communication and follow-up; "**enable collaborative risk acceptance and clear accountability**."
- **External ratings integration**: out-of-the-box cybersecurity ratings from RiskRecon, SecurityScorecard, HackNotice (integrated via a separate product, Third-Party Risk Exchange); inform/validate inherent and residual risk scoring with external data; critical-event triggered automation rules (vendor claims 9.2M critical event workflows processed per year across customers).
- **Ethics & compliance due diligence**: pre-built integration with Dow Jones Risk & Compliance databases; PEP, sanctions, watchlist screening; adverse media & reputational monitoring; in-app enhanced due diligence research and reporting. (Suite also sells a separate "Third-Party Due Diligence" product on the same content.)
- **Risk insights**: guide onboarding/assessments with inherent and domain-specific risk insights; "strengthen risk acceptance and approval decisions with clear risk visibility"; "equip procurement and sourcing teams with relevant insights to make risk-informed decisions."
- **Register**: FAQ mentions "a vendor risk register full of thousands of third-party Trust Profiles" (pre-built profiles).
- FAQ subject universe: "automating vendor risk management across your entire value and supply chain – from onboarding to offboarding for technology partners, service providers, and more."

### ProcessUnity Vendor Risk Management (pure-play, assessment-led) — A-layer

- Positioning: vendor risk management "with close ties to information technology and cybersecurity"; "assess and monitor both new and existing vendors – from initial onboarding to ongoing due diligence and monitoring."
- Lifecycle framed as **Pre-Contract** (Vendor Onboarding — standardized enterprise-wide process for introducing a service provider into the vendor database; Pre-Contract Due Diligence; Risk Domain Screening — e.g. financial stability and security; Sourcing/RFx) and **Post-Contract** (Continuous Vendor Monitoring — objective post-contract cadence; Vendor Performance Management — SLA comparison on a common platform; Issue Management — document issues, assign responsibilities, track actions/status, report to stakeholders; Post-Contract Due Diligence for internal analysts, vendors, suppliers, and fourth parties).
- **Assessment machinery** (the product's center): intelligent questionnaires replacing surveys/spreadsheets; "automatically determining the scope of assessments based on inherent risk scores and vendor criticality tiers"; preferred responses score submissions in real time; built-in content library plus import of custom methodologies (SIG Lite/SIG Core from Shared Assessments); **third and fourth parties complete assessments through a secure online portal, with delegation to multiple contacts and supporting-document attachment**.
- **External intelligence connectors**: BitSight (cyber ratings), RapidRatings (financial health), Dun & Bradstreet (identity), Refinitiv (screening), EcoVadis (ESG); alerts on critical changes in vendors' financial or cybersecurity health.
- **Program governance/reporting**: pre-configured reports on vendor criticality, assessment status, findings, issues, requests, action items, contract review status, risk by geographic location, compliance ratings; "demonstrate the existence of a consistent, reliable, and repeatable vendor risk management program to regulators and stakeholders."
- **Platform posture**: no-code configuration (100% end-user configurable), hands-free automation of assessment scoping and evidence collection, enterprise integration via API, Reporting-as-a-Service.
- **Adjacent platform lines that mark the boundary**: **Global Risk Exchange** (assessment-sharing network; ProcessUnity Risk Index), **Threat & Vulnerability Response** (gauge exposure when threats/vulnerabilities emerge across the third-party ecosystem), **Cybersecurity Risk Management** (own-organization cyber program — separate product), **Affiliates/Intragroup Risk Management** ("detect, assess, and govern risk across affiliates, subsidiaries, and internal service providers" — same machinery pointed inward at group entities).
- **Regulatory anchors sold as solutions**: DORA, APRA CPS 230, ABAC (anti-bribery), LkSG (German Supply Chain Act).
- Audience taxonomy on site: TPRM executives, TPRM analysts, procurement teams/CPO, infosec/CISO, risk & compliance teams, **third-party vendors / client-assurance teams** (the assessed side).

### Diligent Third-Party Risk Management / 3rdRisk (GRC-suite pole) — A-layer

- Positioning: "3rdRisk, Diligent's AI-native third-party and vendor risk management software… to manage every component of your third-party relationships"; "efficiently assess, monitor and mitigate with vendor risk management software."
- Value props: complete view of every third-party relationship in a centralized automated platform ("stop managing vendor risk in spreadsheets"); "bring all third-party data, documents, risks and SLAs into one secure repository"; leadership real-time visibility; "continuously monitor vendor risk with automated alerts and built-in compliance frameworks including NIST, ISO, NIS-2 and DORA"; "unify vendors, teams and risk owners in one branded workflow, with automated surveys, clear sign-offs, and Microsoft Teams/Slack integration."
- Three-step program frame: **Overview** (central view of every third-party relationship — manual add, bulk import of supplier lists, or API pull from existing systems) → **Insight** (AI-driven analysis; automated alerts; SOC-2 analysis; external risk ratings; real-time intelligence on vendor security, financial stability, ESG, compliance status; configurable dashboard) → **Manage** (centralized issue and action-plan management; remediation tracked end-to-end; AI-assisted questionnaires; structured workflows; branded portals; Teams/Slack-integrated).
- Features: AI third-party risk profiles (automatic segmentation to assess inherent risk from the moment a third party enters the platform); AI assessment populator; risk-based assessment automation; country risk profiles with real-time alerts; branded, trusted environment ("fully branded" for the customer).
- Program-blog framing: "a successful third-party risk management (TPRM) program extends way beyond just the onboarding process; organizations need to be invested in the total TPRM lifecycle — from start to finish."
- **Suite-internal boundary evidence**: Diligent's own product taxonomy separates **Third-Party Risk Management (3rdRisk)** (Risk family) from **Third Party Manager** ("systemize and automate third-party monitoring and compliance processes," Compliance family) and **Third-Party Risk Intel** ("automated third-party screening and risk triage powered by agentic AI") and **Due Diligence** ("due diligence services fueled by AI capabilities and human investigational skills") — the same vendor sells the risk-program layer, the compliance-monitoring layer, the screening layer, and the investigation-service layer as distinct products.

---

## Cross-product Comparison

| Structure / capability | Prevalent | OneTrust | ProcessUnity | Diligent 3rdRisk | Evidence | Tier judgment |
|---|---|---|---|---|---|---|
| Persistent third-party/vendor record as system of record ("single source of truth", "complete view of every relationship", "vendor database", "central view") | ✓ | ✓ | ✓ | ✓ | B (4/4) | **L0** |
| Subject universe beyond suppliers: service providers, technology partners, partners; fourth parties | ✓ (4th-party intel; "vendors, suppliers, and partners") | ✓ ("technology partners, service providers, and more") | ✓ (assesses "vendors, suppliers and fourth parties") | ✓ ("every component of third-party relationships") | B (4/4) | **L0** |
| Risk tiering / criticality driving assessment depth & workflow priority | ✓ (inherent+residual scores; tier & categorize) | ✓ (contextually tier & triage → workflow priority + assessment depth) | ✓ (scope auto-determined by inherent risk scores + criticality tiers) | ✓ (AI segmentation → inherent risk; risk-based assessment automation) | B (4/4) | **L0** |
| Due-diligence assessment machinery (questionnaires, evidence/document collection, scoring) | ✓ (800+ templates; AI-completed; human review) | ✓ (AI questionnaire population; auto-approval for low risk) | ✓ (intelligent questionnaires; SIG import; real-time scoring) | ✓ (AI-assisted questionnaires; automated surveys) | B (4/4) | **L0** |
| Decision/approval structure on the relationship (acceptance, sign-off, approval gates) | ✓ (escalation to human review; remediation mgmt) | ✓ explicit ("collaborative risk acceptance", auto-approval workflows, approval decisions) | ✓ (pre-contract due-diligence gate; issues→actions) | ✓ ("clear sign-offs") | B (4/4; wording varies) | **L0** (as evaluation→decision loop; "acceptance" as named object is OneTrust-specific) |
| Issues/findings → remediation tracked to closure | ✓ | ✓ (issues, risks, tasks with owners) | ✓ (dedicated Issue Management) | ✓ (issue & action-plan management) | B (4/4) | **L0** |
| Ongoing monitoring feeding the record | ✓ (continuous engine) | ✓ (ratings + critical events) | ✓ (continuous + connectors) | ✓ (continuous monitoring + alerts) | B (4/4) — but all current-market | **L1** (periodic reassessment alone satisfies the Type; continuous external monitoring is the mature form) |
| External intelligence integration (cyber ratings, financial health, screening lists, ESG) | ✓ (native engine) | ✓ (RiskRecon/SecurityScorecard/HackNotice; Dow Jones) | ✓ (BitSight, RapidRatings, D&B, Refinitiv, EcoVadis) | ✓ (external ratings; SOC-2 analysis; country risk) | B (4/4) | **L1** (providers differ; integration is standard-mature) |
| Third-party-facing participation (portal, questionnaires, document upload, status) | ✓ | ✓ (communication/follow-up through integrated assessments; external-team tasks) | ✓ (secure online portal; delegation) | ✓ (branded portal; vendors unified in workflow) | B (4/4) | **L1** |
| Assessment-sharing / pre-completed profiles network | ✓ (vendor intelligence networks) | ✓ (Trust Profiles register) | ✓ (Global Risk Exchange + Risk Index) | not observed on page | B (3/4) | **L1/L2** |
| Relationship lifecycle stages beyond assess: sourcing/RFx, onboarding, performance/SLA, offboarding | ✓ (all) | ✓ (onboarding…offboarding; SLA via repository) | ✓ (all, incl. RFx + SLA) | partial (onboarding, surveys, remediation; sourcing/offboarding not explicit on page) | B (3–4/4) | **L1** lifecycle span; L0 holds the gates (intake, acceptance, disposition) |
| Incident → affected-third-party exposure response | ✓ (Technology Tags) | ✓ (critical event workflows) | ✓ (Threat & Vulnerability Response line) | ✓ (alerts; country risk) | B (4/4; depth varies) | **L1/L2** |
| Regulatory-regime packaging (DORA, NIS-2, LkSG, APRA CPS 230, ABAC) | not explicit | not explicit | ✓ (four named solutions) | ✓ (NIST/ISO/NIS-2/DORA frameworks) | B (2/4) | **L2** |
| Native CLM | ✓ (Contract Essentials) | — | — (contract review status reported) | — (documents/SLAs held) | A (1/4) | **L2** (adjacent Type absorbed as module) |
| Managed assessment/program services | ✓ | — | — | — | A (1/4) | **L2** (service wrapper, not product structure) |
| Intragroup/affiliates as a separate application of the same machinery | — | — | ✓ (Affiliates/Intragroup Risk Mgmt product) | — | A (1/4) | **L2/L3** |
| Vendor-specific numbers (800+ templates; 30k+ sources; 9.2M workflows; 70% faster; 10-day go-live; 20M+ insights) | ✓ | ✓ | — | ✓ | A | **L3** — never promoted |

**Pattern across the sample**: every product is organized around (a) a standing population of third-party relationship records, (b) a per-relationship risk evaluation (tier → assessment depth) that produces a comparable standing, and (c) a governed loop that turns evaluation into decisions and tracked responses over the relationship's life. Everything else — external feeds, portals, exchanges, SLAs, regime packaging — clusters onto that spine.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The third-party relationship inventory of record** — persistent, individually identified records of the organization's external relationships (vendors, suppliers, service providers, partners — not limited to goods suppliers), each carrying business context (what the relationship is, who owns it, contracts/documents, status), forming the standing population the program runs on. *Remove → a document store or an assessment tool with no subject of record.*
2. **Per-relationship risk evaluation producing a comparable risk standing** — criticality/inherent-risk tiering plus due-diligence assessment (questionnaires, evidence and document collection, optionally external intelligence) evaluated into scores/levels that make the risky subset prioritizable and that calibrate how deep each relationship is assessed. *Remove → a vendor contact list with attachments; nobody can say which third parties are risky or why effort is allocated.*
3. **The governed decision-and-response loop over the relationship lifecycle** — evaluation results become recorded decisions (approval/risk acceptance or rejection, with accountable owners) and tracked responses (issues and remediation actions, reassessment/revalidation triggers, disposition up to restricting or terminating the relationship), retained as an audit-ready trail of the program. *Remove → one-off due diligence or a raw ratings feed; the "management" is gone.*

Jointly-held is load-bearing: 1 alone = vendor list / supplier master; 2 alone = assessment service or ratings dashboard; 3 alone = generic workflow tool; 2+3 without 1 = GRC machinery with no third-party subject of record; 1+2 without 3 = due-diligence library, below the Type.

### L1 — Common Mature Structure (standard in current products, not definitional)

- Continuous external risk monitoring (cyber ratings, financial health, sanctions/PEP/adverse media, ESG signals) with alerts and incident-to-portfolio exposure response.
- Third-party-facing portal: questionnaire completion, document upload, delegation, status tracking, messaging.
- Lifecycle span beyond the loop: sourcing/RFx support, SLA/performance tracking, contract documents held on the record, offboarding/termination procedures.
- Assessment-exchange / shared profiles (pre-completed standardized assessments or trust profiles from a network).
- Program governance layer: dashboards, board-ready reporting, regulator-facing demonstration ("consistent, repeatable program"), configurable content libraries and frameworks (NIST/ISO/SIG-class).
- Issue/finding classification with owners, severity, due dates, corrective-action workflows.

### L2 — Variant / Optional Structure (segment, regime, or posture dependent)

- Regulatory-regime packaging: DORA, NIS-2, APRA CPS 230, LkSG/CSDDD-class supply-chain due diligence, anti-bribery (ABAC), financial-services outsourcing/TPRM guidance.
- Cyber-led weight: some deployments run the whole program from the cyber lens; ratings-led intake screening as the primary triage (the §15 boundary case).
- Fourth-party (subcontractor) visibility and 4th-party intelligence.
- Intragroup/affiliates mode (same machinery pointed at group entities and internal service providers).
- Native contract lifecycle management absorbed as a module.
- Managed services (analyst-led program operation) as commercial wrapper.
- Auto-approval fast-tracking of low-risk third parties; AI-generated questionnaire answers/evidence ingestion (era-current).
- Onboarding-gate integration with procurement systems (pull vendor data via API/bulk import) — integration depth varies.

### L3 — Vendor-specific (Research Notes only)

- Prevalent: Vendor Threat Monitor scale claims (30,000+ sources, 1.8M PEP profiles, 1,000+ lists), Technology Tags (CrowdStrike 2024 example), Contract Essentials module name, 800+ template count, AI FastTrack (15 prior assessments → 200+ recommended answers), ARIES survey automation, "44% faster / 50% less manual" customer claims.
- OneTrust: RiskRecon/SecurityScorecard/HackNotice/Dow Jones integrations as branded products (Third-Party Risk Exchange, Third-Party Due Diligence), 9.2M critical-event workflows/year, 20M+ out-of-the-box insights, "Trust Profiles."
- ProcessUnity: Global Risk Exchange + ProcessUnity Risk Index, no-code 100% configurable platform claim, SIG Lite/SIG Core import, named connector brands (BitSight, RapidRatings, D&B, Refinitiv, EcoVadis), Reporting-as-a-Service, Affiliates/Intragroup product line, DORA/ABAC/LkSG/APRA solution SKUs.
- Diligent: 3rdRisk brand lineage, 10-day go-live claim, Teams/Slack virtual assistant, branded-environment emphasis, suite siblings (Third Party Manager, Third-Party Risk Intel, Due Diligence).

---

## Vendor-specific / Rejected Findings

- **"70% faster assessments" / "9.2M workflows" / "30,000+ sources" / "10 days to live"** — vendor marketing numbers; never promoted to the canonical model.
- **Native CLM as part of TPRM** — only Prevalent ships it natively (A, 1/4); held as optional module; contract data on the record is the common form.
- **"Purpose-built, not a GRC module"** (Prevalent's self-description) — a vendor positioning claim, used only as boundary evidence, not as a structural fact.
- **Sourcing/RFx as definitional** — only 2/4 sampled expose RFx execution; held as lifecycle extension (L1), not core.
- **"Vendor risk management" vs "third-party risk management" as different Types** — the same products use both labels interchangeably (ProcessUnity page title "Vendor Risk Management Software" under a "TPRM Platform" menu; Diligent page mixes "third-party" and "vendor" in one sentence). Rejected as a Type split; held as naming overlap within one Type, with the note that "vendor" flavors skew the subject universe toward IT/cyber-relevant suppliers.

---

## Boundary Findings

### vs Governance Risk & Compliance Platform (§11 umbrella) — flag from the GRC pass, DISCHARGED here

- The GRC pass observed all five of its sampled platforms shipping TPRM as a module. This pass confirms the other pole: standalone pure-play TPRM products exist and are recognized as their own analyst category ("Third-Party Risk Management Platforms" — Forrester Wave, vendor-cited on ProcessUnity's page; "Third-Party Risk Management Tools" — Gartner MQ, vendor-cited on Diligent's page). **Keep-both ratified** with a centered-object seam: the GRC umbrella's core is the interlocking risk × control × requirement record core plus evaluation-and-issue loops across all programs; TPRM centers the third-party relationship — its subject universe (external relationships), its evaluation (tier + due diligence), and its loop (acceptance → monitor → disposition) hang from the relationship record, not from the enterprise risk/control register. TPRM-as-GRC-module and TPRM-as-standalone are packaging poles of the same Type (consistent with the supplier-risk pass's "suites bundle both — packaging does not dissolve the seam" logic).
- Corroborating suite-internal evidence: Diligent sells 3rdRisk (risk-program TPRM) beside Third Party Manager (compliance-led monitoring) and Due Diligence (investigation service) — the module boundary is real inside a single suite.

### vs Supplier Risk Management (§10) — sharpest seam, DISCHARGED from this side

- The supplier-risk pass proposed: seam = subject universe + operating frame. This pass's evidence supports ratifying it: all four sampled TPRM products define their universe in terms of *relationships with any external party* ("vendors, suppliers, and partners" — Prevalent; "technology partners, service providers, and more" — OneTrust; "vendors, suppliers and fourth parties" — ProcessUnity), and their operating frame is the *engagement/contract lifecycle* (pre-contract → post-contract; onboarding → offboarding) with assessment-acceptance-reassessment cycles — not the procurement-side standing supply-market portfolio, disruption response, or sourcing/onboarding integration that supplier-risk products center. OneTrust even words it as equipping "procurement and sourcing teams with relevant insights" — TPRM feeds procurement, does not run it.
- The convergence zone is real and acknowledged: Prevalent's own page brands itself for "third-party vendor and supplier risk management"; Diligent/3rdRisk supports bulk import of supplier lists. Both passes ratify keep-both with this seam. Cyber-led TPRM products (SecurityScorecard-class) are confirmed out of scope here → §15.

### vs Third-party Cyber Risk Platform (§15)

- Clean seam, visible *inside* the products: the sampled TPRM tools *integrate* cyber ratings providers (OneTrust embeds RiskRecon/SecurityScorecard; ProcessUnity connects BitSight) — they are consumers of the §15-class ratings machinery, not its operators. When a product's center becomes external attack-surface scanning and security-rating computation, it is the §15 Type; when the center is the relationship program with cyber as one domain, it is this Type.

### vs Due Diligence Platform (§11 sibling)

- Distinct: the Due Diligence sibling is an investigation/screening *service* (human-investigation skills, per Diligent's own description); TPRM is the *program system of record* that consumes screening content (Dow Jones-class lists, PEP/sanctions) as one input among questionnaires and evidence. OneTrust splitting "Third-Party Due Diligence" from "Third-Party Risk Management" at product level confirms the seam.

### vs Vendor Management System (§9) / Supplier Management Platform (§10) / Contract Lifecycle Management (§11)

- VMS: workforce/staffing supply chain is the subject; here risk programs over any third party. Clean.
- Supplier Management Platform: lifecycle/record center over the supplier population (onboarding data, qualification documents, performance); TPRM adds the risk-evaluation-and-disposition loop as the center. The supplier-risk pass already drew the supplier-management ↔ supplier-risk seam; the same logic extends to TPRM's side.
- CLM: contract lifecycle is its own Type; TPRM holds contract facts/SLAs as attributes on the relationship record (3/4 sampled), with native CLM an optional module (Prevalent only).

### "去掉什么就变成另一个 Type" 判据 (remove-what test)

- Remove the *external-relationship* subject and keep the machinery → GRC risk-assessment machinery (or, if procurement-side monitoring is added, Supplier Risk Management).
- Keep the subject but remove the *risk evaluation* → vendor/supplier master data (Supplier Management territory).
- Keep subject + evaluation but remove the *governed loop* → due-diligence service or ratings portal (§15/Due Diligence territory).
- Re-center on cyber ratings/attack surface as the *product's own* machinery → Third-party Cyber Risk Platform.

---

## §24 Historical / Market-Sample Check

Would older, regional, platform-native or differently-positioned products still fit the L0?

- **Paper-era vendor risk files**: a vendor register with one file per provider; due-diligence questionnaire + financial statements + insurance certificates collected at engagement; criticality tiers deciding review depth; a risk/procurement committee's written approval; annual re-review; incident-driven file pulls — satisfies all three L0 legs with paper alone. This is the recognizable thin ancestor (and is still the operating mode TPRM tools advertise themselves against: "stop managing vendor risk in spreadsheets" — Diligent; "outgrown spreadsheets, shared drives, and email chains" — Prevalent).
- **Financial-services outsourcing due diligence** (regulator-driven vendor-risk programs in banking) — questionnaire + tiering + board-approved acceptance + periodic revalidation predates the modern tooling; fits the core; explains why "risk acceptance with accountable sign-off" is structural rather than a modern SaaS affectation.
- **No continuous external monitoring in the core** — pre-intelligence-feed programs ran on periodic reassessment; therefore continuous monitoring is the mature modern form (L1), not definitional. All four sampled products being current-market makes this check necessary; the historical form passes.
- **Cloud/AI era-current features** (AI questionnaire population, AI segmentation, agentic screening) — all L2-era capabilities; none needed for recognition.

---

## Uncertainties

1. **Exact assessment state models** (state names, escalation deadlines, approval hierarchies) were not verified at help-center depth for any product; the final document deliberately describes lifecycle stages conceptually without asserting product state lists.
2. **Whether the third-party portal is universal** — evidenced in all four sampled (B 4/4), but the sample is current-market; whether some deployments run closed (analyst-mediated only) programs was not verifiable. Held L1.
3. **Auto-approval of low-risk third parties** — explicit only in OneTrust (A 1/4); held as variant until more evidence.
4. **ServiceNow and Archer module detail** — unreachable in this pass; no claims made. The GRC-module pole rests on the prior GRC pass's cross-observation (B) plus Diligent as a directly-observed suite pole.
5. **Diligent's three product split (3rdRisk vs Third Party Manager vs Third-Party Risk Intel)** — observed as current positioning (A); whether customers must buy all three or whether 3rdRisk absorbs the others' functions was not verifiable; used only for boundary evidence.
6. **Assessment-exchange prevalence** — 3/4 sampled; may be under-observed for Diligent (page depth). Held L1/L2 rather than L1 firm.

---

## Final Synthesis

A **Third-party Risk Management application** is the organization-side system of record for managing the risk that comes from its relationships with external third parties. Its defining core is three jointly-held structures:

1. the **third-party relationship inventory** — persistent identified records of external relationships (vendors, suppliers, service providers, partners), the standing population the program runs on;
2. **per-relationship risk evaluation** — criticality/inherent-risk tiering plus due-diligence assessment (questionnaires, evidence, external intelligence) producing a comparable risk standing that calibrates assessment depth and prioritizes the risky subset;
3. the **governed decision-and-response loop over the relationship lifecycle** — recorded approval/risk-acceptance decisions with accountable owners, issues and remediation tracked to closure, reassessment and monitoring feeding disposition (approve / restrict / remediate / terminate), all retained as the program's audit-ready trail.

Around that core, mature products add continuous external monitoring with incident-to-portfolio response, third-party-facing portals, lifecycle span (sourcing support, SLA tracking, contract facts, offboarding), assessment-sharing networks, and program governance/reporting. Regulatory regimes (DORA/NIS-2/LkSG/APRA CPS 230/ABAC class) shape variants rather than the core. The Type is realized both as standalone pure-play products and as modules of GRC platforms; the boundaries that matter: GRC = the umbrella's interlocking risk×control×requirement core (TPRM centers the relationship instead); Supplier Risk Management = procurement-side standing supplier portfolio and supply-market loop (TPRM = relationship/engagement-centric loop over any third party); Third-party Cyber Risk Platform = the ratings/attack-surface machinery TPRM consumes; Due Diligence Platform = the investigation service TPRM's program consumes. Historical check passed: paper-era vendor risk files with tiered due diligence and committee acceptance satisfy the core, so no current-market feature (continuous feeds, portals, AI) is definitional.
