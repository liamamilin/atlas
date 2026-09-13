# Research Notes — Insurance Claims Management

Slug: insurance-claims-management
Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what an Insurance Claims Management application really is, from real products: what objects exist inside it, who uses it, how a claim moves from first notice to financial resolution, what rules govern the work, and where its boundaries sit against neighboring Types (especially the already-processed Claims Adjuster Platform, which recorded a joint-review flag against this leaf).

## Initial Boundary (hypothesis before research)

- Hypothesis: this is the payer-side (insurer/TPA/program-administrator) system of record for the claim lifecycle: intake (FNOL) → registration → coverage verification → assignment → investigation → reserving → payment/settlement → recovery → closure.
- Nearest neighbors: Claims Adjuster Platform (the workbench), Insurance Policy Administration System (policy lifecycle), Underwriting Workbench / Insurance Underwriting Platform (pre-binding), Payer Claims Processing (healthcare — same word, different domain), Construction Claims Management (same word, different domain), Insurance Agency Management (agency-side claims logging only).
- Known unknowns: how deep the financial layer (reserves/payments) sits in the definition; whether the adjuster workbench is a facet of this Type or a separate Type; how far the Type extends beyond P&C carriers (TPAs, risk pools, self-insureds, guaranty funds).

## Research Questions

1. What is a "claim" as an object in these systems? What does it bind to (policy, parties, loss event)?
2. What is the canonical lifecycle from FNOL to closure? Which stages are universal vs product-specific?
3. What is the financial model: reserves, payments, recoveries, deductibles? Is the financial layer definitional?
4. How does intake work (FNOL/FROI): channels, validation, duplicate detection, triage?
5. How does assignment/routing work, and what role do SLAs/diary play?
6. How do coverage verification, fraud signals, and litigation fit in?
7. Who are the users (adjusters, supervisors, managers, executives, TPAs, policyholders) and what surfaces do they use?
8. How do products differ: carrier core systems vs cloud-native platforms vs RMIS-style claims administration?
9. Where is the seam vs the Claims Adjuster Platform (joint-review flag)?
10. Would older/regional/non-carrier products still fit the definition (historical check)?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

1. **Duck Creek Claims** (+ Agentic First Notice of Loss) — enterprise P&C core-suite claims module (carrier tier; suite-native philosophy). Fetched: product page + FNOL product page.
2. **Snapsheet Claims Platform** — cloud-native complete claims system for carriers/MGAs/TPAs/fleet (mid-market tier; no-code configuration philosophy; also sells virtual appraisals — the overlap zone with the adjuster platform). Fetched: home + platform product page.
3. **Origami Risk — Claims Administration (P&C Insurance) + Claims Management (RMIS)** — multi-constituency claims platform: carriers, MGAs, risk pools, TPAs, and self-insured/risk-manager side (broadest operator spread; RMIS philosophy). Fetched: root + claims administration page + RMIS claims management page.
4. **Sapiens ClaimsMaster** — global enterprise claims system for personal and commercial lines, standalone or inside IDITSuite (EMEA/global tier; suite + standalone philosophy). Fetched: ClaimsMaster product page.
5. **Guidewire ClaimCenter** — the largest P&C claims market anchor. NOT directly fetched: product page returned HTTP 429 twice; docs.guidewire.com is a JavaScript app (no content reachable). Used as market anchor only; no vendor-specific claims asserted from memory.

## Sources

- Duck Creek — Claims Management Software: https://www.duckcreek.com/product/claims-management-software/ (fetched 2026-09-07)
- Duck Creek — Agentic First Notice of Loss: https://www.duckcreek.com/product/agentic-first-notice-of-loss/ (fetched 2026-09-07)
- Snapsheet — home: https://snapsheetclaims.com/ (fetched 2026-09-07)
- Snapsheet — Claims Platform: https://snapsheetclaims.com/products/claims (fetched 2026-09-07)
- Origami Risk — home: https://www.origamirisk.com/ (fetched 2026-09-07)
- Origami Risk — Claims Administration: https://www.origamirisk.com/solutions/insurance/claims-administration/ (fetched 2026-09-07)
- Origami Risk — RMIS Claims Management & Claims Administration: https://www.origamirisk.com/solutions/rmis/claims-management-claims-administration/ (fetched 2026-09-07)
- Sapiens — ClaimsMaster: https://sapiens.com/property-and-casualty/claimsmaster/ (fetched 2026-09-07)
- Guidewire — product page: https://www.guidewire.com/products/claimcenter (429 ×2, abandoned); docs: https://docs.guidewire.com/ (JS app, no content)
- Prior pass context: research/claims-adjuster-platform.md (§Boundary Findings — joint-review flag), applications/claims-adjuster-platform.md, STATUS.md boundary issue line.

Evidence layers used below: **A = directly observed** on a fetched official page of a specific product; **B = cross-product commonality** across the sampled products; **C = canonical inference** from comparison + boundary reasoning.

## Product Observations

### Duck Creek Claims (evidence layer A)

Positioning: "modern P&C claims management software"; one of four CORE Intelligent Applications (Policy, Rating, Billing, Claims) — claims is a core system alongside policy and billing. Target: insurers ("Claims & Operations Leaders").

Observed feature blocks (product page):

- **Assignment & Routing** — rules-based routing powered by coverage type, expertise, and real-time workload data; automated escalation and load balancing; "faster time-to-contact".
- **Coverage Verification** — "confirm coverage in seconds"; "catch coverage gaps early and resolve disputes before they escalate".
- **Investigation Management** — "a single hub for every task, document, and stakeholder"; collaboration across adjusters, vendors, and third parties; "built-in analytics and intelligent risk indicators" for fraud.
- **Reserves & Payments** — "set accurate reserves from the start"; "end-to-end audit trails"; payment automation; "configurable authorization thresholds and compliance safeguards".
- **Subrogation & Recovery** — surface recovery opportunities; purpose-built workflows; "proactive diary management and built-in follow-up automation".
- Pre-configured content: "over 1200 Coverage Types, over 100 Tasks, over 1000 Business Rules, including Straight-Through Processing, automated coverage verification, reserving and payments, FNOL Dynamic" (vendor figures — L3).
- Low-touch/no-touch FAQ: "Low-complexity claims can be automatically triaged, adjudicated, and paid—while higher-complexity cases are seamlessly routed to adjusters with the right context and controls"; automation levels tailorable "by product, region, or loss type".
- CAT FAQ: cloud-native elastic scaling; "automated intake, prioritization, and assignment" during catastrophe events. Vendor scale claims (30M+ claims processed; 60K+ claims/day during CAT) — L3, not asserted in final doc.
- Omnichannel communications; digital-first status updates.
- Ecosystem: partner integrations (data providers, vendors); part of Intelligent Core with Policy/Billing — claims references policy data.

Duck Creek Agentic FNOL (separate product page):

- FNOL framed as "the most manual, fragmented moment in claims"; intake capability that "captures, validates, triages, and routes claims from first contact".
- **Intake & Validation**: capture loss details, photos, claimant information, supporting context; check completeness, policy context, duplicate claim risk, required information.
- **Validate & Enrich**: automatically validate policy coverage, required claim information, claimant details, documentation; detect missing data, inconsistencies, fraud indicators, duplicate claim risk "before the claim progresses".
- **Triage & Handoff**: route based on complexity, severity, confidence thresholds, and carrier rules; "send structured, enriched claim data into Duck Creek Claims or connected systems".
- Explainability: confidence scoring, decision traceability, human-in-the-loop, "full regulatory compliance through complete audit trails"; "human checkpoints for complex losses".
- Scope note: current Agentic FNOL focused on Personal Auto FNOL (vendor statement — L3).

### Snapsheet Claims Platform (evidence layer A)

Positioning: "complete claims system" replacing "patchwork solutions"; "built for the way claims work"; customers: P&C carriers, MGAs, TPAs, fleet & logistics; personal + commercial lines. Also sells Virtual Vehicle Appraisals and Total Loss Settlement as separate products (the adjuster-workbench overlap zone).

Observed platform structures (platform page):

- **Unified claim view** — "documents, communications, notes, vendors, claim updates, and actions are captured, logged, and quickly searchable in a single file".
- **No-Code Workflow Engine** — configure workflows "for every claim type, rule set, and scenario via a point and click interface and if-then logic".
- **Smart Assignment** — route "based on skill set, licensing, geography, claim type, complexity, and vendor involvement"; assignment profiles "based on dozens of attributes"; specialty rules for "CAT events or luxury vehicles".
- **Customizable Work Queues** — "role-based queues for adjusters, administrators, and managers".
- **Transparent Claim History** — "complete, time-stamped history of every action on a claim for full visibility and compliance".
- **Omnichannel Communications** — "send and store emails, text messages, and letters directly from the claim file".
- **Integrated Financials** — "automate reserves, digital payouts, and vendor payments directly within the platform".
- **Adjustable Claim Types** — "define claim, loss, and exposure types to reflect your internal models" (claim/exposure structure is customer-configurable).
- **Custom Fields**, **Claim Tags** (auto-tag for grouping/analysis), **Emergency Services** (triggers and service question flows by claim type), **Vendor Management** (incl. tax information), **Integrated SLAs** ("track, enforce, and manage SLAs directly in every claim"), **Role-Based Dashboards**, **Settlement Tracking** ("visibility into negotiations, communications, and outcomes").
- **Payments** — "instant digital payouts triggered by configurable logic aligned with your payment rules and policy guardrails".
- **Integrations & APIs** — direct integrations; "update connected systems instantly whenever a claim is updated"; event webhooks.
- Built-in accuracy: "SLA adherence, compliance guardrails, and automated validations are embedded in workflows".
- Vendor scale claims (10M+ monthly automated actions; $75B+ premiums supported; 12-week implementation) — L3.

### Origami Risk — Claims Administration + RMIS Claims Management (evidence layer A)

Positioning: one platform for "risk, insurance, and safety"; P&C Insurance solutions for **carriers, MGAs, risk pools, TPAs**; RMIS solutions for risk managers/self-insureds. Claims Administration recognized as P&C Claims System Luminary in consecutive Celent reports (vendor-cited analyst recognition — context, not structure).

Claims Administration page (carrier/program side) — the lifecycle is presented as an explicit capability sequence:

- **Claim Submission** — "Simplify FNOL and FROI with a flexible AI-assisted claim intake process" (FROI = workers' comp First Report of Injury).
- **Policy Coverage Verification** — "Verify policy coverage in the adjudication workflow using any data source".
- **Involved Parties** — "Invite anyone needed for claim resolution to collaborate and share".
- **Assignment** — "AI-enabled smart triage, so the right claim gets to the right adjuster every time".
- **Adjudication** — "Document and access loss information to recommend optimal outcomes".
- **Reserves Management** — "Streamline the reserving process with embedded tools and automated workflows".
- **Payments and Disbursements** — "comprehensive settlement support tools".
- **Deductible Management & Billing** — deductibles and payments tracking.
- **Loss Control** — reporting and recommendations.
- **Recovery** — "tools for managing salvage and subrogation".
- **Quality Assurance** — "tools for auditing claims and sharing results".
- **Fraud Investigation** — "tracking fraud and special investigation unit referrals".
- **Closure** — "AI-assisted workflows that automate final communication issuance and reserves updates".

RMIS Claims Management page (self-insured/risk-manager side) — same object world, oversight posture:

- "Whether your team self-administers or you're looking to improve how you manage and report on data from TPAs and carriers" — the RMIS posture includes both in-house administration and oversight of external administrators' claim data.
- Claims financials tracking (reserves, payments, financial trends); AI claims summary; subrogation & recovery tracking; **claim litigation management** ("centralize legal documentation and track litigation status"); leave-of-absence management; lost-time tracking; return-to-work management; claim benchmarking; claim audits; adjuster performance analysis.
- Claims Administration offerings (in-house handling): payment processing ("accuracy, timeliness, and compliance with internal and external requirements"); reserve management ("audit trails and approval workflows"); OFAC sanctions search on payees; 1099 production; ISO Claims Search ("identify duplicate claims and uncover potential fraud or prior incidents"); CMS-111 Medicare reporting; ODG treatment-guideline integration; jurisdiction-specific state forms; indemnity benefit calculations; electronic injury reporting (EDI FROI/SROI).
- Case studies confirm constituency spread: Harford Mutual (carrier, 10 states/10 LOBs), AEU (longshore/workers' comp), PERMA (public-employer risk pool), IIGF (guaranty fund; migrated 100K claims).

### Sapiens ClaimsMaster (evidence layer A)

Positioning: "advanced, end-to-end claims management solution designed for insurers handling both personal and commercial lines"; "streamlines the entire claims lifecycle from FNOL to settlement while supporting complex case handling, fraud detection, regulatory compliance, and digital customer engagement"; "can operate as part of Sapiens IDITSuite or as a standalone claims system". Users: "claims teams, adjusters, and supervisors".

Observed:

- "Intelligent, rules-driven workflows powered by AI-driven insights to enable seamless claim assignment and straight-through processing".
- Rules-based workflows "automate task assignment, verification, and escalation"; "supports role-based and straight-through processing"; "directly trigger tasks to the right contacts at the right time".
- "Case management for complex scenarios"; configurable rules "trigger tasks related to fraud detection, limit checks, and regulatory compliance".
- Dashboards: "workloads, financial exposure, and operational performance".
- Role-based navigation; staff "reassign during peak events or CATs without significant retraining".
- Metadata/rules configuration; service-oriented architecture; pre-integrated with DigitalSuite (omnichannel communication, self-service portals, mobile engagement).
- Celent 2024 quote (vendor-cited): "a comprehensive, flexible, and highly automated P&C claims management solution".

### Guidewire ClaimCenter (no direct evidence — market anchor only)

Product page 429 ×2; docs site JS-rendered. Market position (leading P&C claims core system) is common knowledge in the industry and is used only as an anchor for market structure, not as a source of any specific structural claim. No vendor-specific details asserted.

## Cross-product Comparison

| Dimension | Duck Creek Claims | Snapsheet | Origami Risk | Sapiens ClaimsMaster |
|---|---|---|---|---|
| Claim as record | claim with coverage type context; FNOL Dynamic intake | unified claim view; claim/loss/exposure types customer-definable | claim submission (FNOL/FROI) → adjudication → closure sequence | claim lifecycle FNOL→settlement; case management for complex scenarios |
| Intake | Agentic FNOL: capture, validate, enrich, triage, handoff | intake via workflows; emergency-service triggers; custom fields | FNOL + FROI intake, AI-assisted | FNOL; digital engagement via DigitalSuite |
| Coverage verification | explicit feature ("confirm coverage in seconds") | "validate coverage" as real-time automation action | explicit stage ("verify policy coverage in the adjudication workflow") | verification automated within rules-driven workflows |
| Assignment/routing | rules-based routing by coverage type/expertise/workload; escalation, load balancing | smart assignment by skill/licensing/geography/type/complexity/vendor; work queues | AI-enabled smart triage to adjusters | automated task assignment; role-based |
| Reserves | explicit ("set accurate reserves"; audit trails) | integrated financials (reserves automated) | reserves management; RMIS reserve management with approval workflows | financial exposure dashboards; reserves implied in lifecycle |
| Payments | payment automation; authorization thresholds | digital payouts triggered by rules/policy guardrails; vendor payments | payments & disbursements; payment processing with compliance | settlement support (less explicit on page) |
| Recovery/subrogation | explicit feature block | (not surfaced on fetched pages) | explicit (salvage & subrogation; RMIS recovery tracking) | (not surfaced on fetched pages) |
| Fraud | risk indicators in investigation; FNOL fraud signals | guardrails/validations (fraud not headline) | fraud investigation + SIU referrals; ISO Claims Search duplicate detection | fraud-detection rule triggers |
| Litigation | (not surfaced) | settlement tracking | claim litigation management (RMIS) | complex case handling |
| CAT/event handling | elastic scaling; automated intake/prioritization/assignment | CAT assignment profiles | (not headline) | staff reassignment during CATs |
| STP/automation | low-touch/no-touch triage→adjudicate→pay | no-code automation; 10M+ actions claim | AI-assisted workflows; closure automation | STP of all major lines |
| Communications | omnichannel; digital-first status updates | emails/texts/letters from claim file | involved-party collaboration; closure communications | omnichannel via DigitalSuite |
| Audit/compliance | end-to-end audit trails; compliance safeguards | time-stamped claim history; SLA adherence | audit trails; QA/claim audits; OFAC/1099/CMS-111/state forms | regulatory-compliance rule triggers |
| Operator constituency | carriers (suite) | carriers, MGAs, TPAs, fleet | carriers, MGAs, risk pools, TPAs + self-insured (RMIS) | insurers (personal + commercial) |
| Packaging | core-suite module (Policy/Rating/Billing/Claims) | standalone platform + appraisals/total-loss products | platform suite (insurance + RMIS + EHS + GRC) | standalone or IDITSuite module |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately minimal)

The payer-side claims system of record. Three properties; remove any one and the product stops being recognizable as this Type:

1. **Claim record** — a registered report of a loss/event against the organization, binding the parties (claimant/policyholder/insured), the loss details, and a **coverage/program context that determines entitlement** (policy, plan, or program). Without the coverage binding it is a generic incident/complaint case system, not claims.
2. **Governed lifecycle to financial resolution** — the claim is carried through a managed progression (intake → verification → adjudication → resolution → closure, with reopen) in which actions are recorded and attributed. Without the lifecycle it is a ledger, not a management system.
3. **Recorded financial position** — the claim carries a maintained money dimension: estimated obligation (reserve) and amounts paid, tracked and adjusted over the claim's life. Without the financial position it is case tracking, not claims management.

Historical check (§24): the pre-digital claims department already had all three — paper claim files binding loss report + policy, adjuster reports moving the file through a workflow, and reserve sheets + payment vouchers recording the money. Multi-channel digital intake, STP, AI triage, portals, and cloud delivery are modern additions, not definitional. Older/regional products (mutuals, Lloyd's-market claims, state funds, paper-era carriers) satisfy the core.

### L1 — Common Mature Structure (standard capabilities; cross-product B evidence)

- **FNOL / multi-channel intake** — guided capture of loss details, parties, photos/documents across channels (call center, web, mobile, agent); completeness checks; duplicate-claim detection (Duck Creek FNOL duplicate risk; Origami ISO Claims Search).
- **Coverage verification** — validating the claim against policy/coverage data before progression (Duck Creek, Origami explicit; Snapsheet as automation action; Sapiens within rules).
- **Assignment & routing** — rules-based routing by type/severity/geography/expertise/licensing/workload; role-based work queues; escalation and load balancing.
- **Task/activity management** — tasks triggered by rules and workflow; diary/SLA tracking on the claim (Snapsheet integrated SLAs; Duck Creek diary in subrogation; Origami QA).
- **Investigation support** — single hub for tasks/documents/stakeholders; involved-party collaboration; vendor orchestration.
- **Fraud signals & SIU referral** — risk indicators at intake and during handling; special-investigation referral tracking (Duck Creek, Origami, Sapiens).
- **Reserve management** — set/adjust reserves with audit trails and approval workflows (Duck Creek, Origami, Snapsheet).
- **Payment processing** — settlement/disbursement execution with authorization thresholds and compliance safeguards (Duck Creek, Origami, Snapsheet).
- **Subrogation/recovery/salvage** — recovery opportunity surfacing and pursuit workflows (Duck Creek, Origami).
- **Litigation management** — legal documentation and litigation status on the claim (Origami RMIS; Sapiens complex-case handling).
- **Policyholder/claimant communications** — omnichannel messages, letters, status updates sent and stored from the claim file (all four).
- **Document management** — claim-scoped document/photo storage with search (all four).
- **Quality assurance / claim audits** — auditing tools and adjuster performance analysis (Origami explicit; Snapsheet guardrails; Sapiens dashboards).
- **Reporting & dashboards** — workloads, financial exposure, cycle times, loss trends (all four).
- **Straight-through processing** — low-complexity claims auto-triaged/adjudicated/paid; complex ones routed to adjusters (Duck Creek, Sapiens, Snapsheet).
- **CAT/event handling** — event-scale intake, prioritization, surge staffing support (Duck Creek, Snapsheet, Sapiens).
- **Integration seams** — policy admin (coverage data), billing, estimating/valuation ecosystems, fraud/data providers, payment rails, APIs/webhooks (all four).
- **Role-based access + audit trail** — attributed, time-stamped actions (Snapsheet explicit; Duck Creek audit trails; Origami admin portal governance).
- **Configuration surface** — business users configure claim types, workflows, rules without code (Snapsheet no-code; Duck Creek low-code; Sapiens metadata/rules; Origami admin portal).

### L2 — Variant / Optional Structure

- **Line of business** — P&C personal/commercial dominant in sample; workers' comp adds FROI/SROI, state forms, indemnity benefit calculation, return-to-work/lost-time machinery (Origami); life/disability claims exist in the market but were not directly sampled.
- **Operator constituency** — carrier vs MGA vs TPA vs risk pool/guaranty fund (Origami case studies) vs self-insured risk manager (RMIS posture: in-house administration or oversight of TPA/carrier data).
- **Packaging** — core-suite module (Duck Creek CORE, Sapiens IDITSuite) vs standalone platform (Snapsheet) vs multi-domain risk platform (Origami).
- **Workbench posture** — embedded claim-file/adjuster surfaces (Snapsheet unified claim view) vs attach-to-external-workbench/estimating ecosystems (suite products integrate estimating vendors).
- **Deployment** — cloud SaaS dominant in sample; legacy on-prem replacements are the sales narrative (Origami Harford Mutual/IIGF case studies).
- **Region** — US regulatory machinery (state forms, CMS-111, OFAC, 1099, FROI/SROI) vs EMEA/multilingual/multicurrency (Sapiens).
- **Self-service** — policyholder/claimant portals and status tracking (Duck Creek Policyholder Portal; Sapiens DigitalSuite).
- **AI depth** — era-common: AI summaries, agentic intake, explainable decisioning with human-in-the-loop (Duck Creek, Origami, Sapiens).

### L3 — Vendor-specific (research notes only; not in final doc)

- Duck Creek: pre-configured content counts (1200+ coverage types, 100+ tasks, 1000+ business rules); 30M+ claims processed via OnDemand; 60K+ claims/day CAT scaling; <1 day rule-change claim; Agentic FNOL currently Personal-Auto-focused; "Intelligent Core" framing; FNOL Dynamic.
- Snapsheet: 10M+ monthly automated actions; $75B+ premiums supported; 12-week implementation; 170+ customers incl. 16 of top-20 P&C carriers; claim tags; emergency-services triggers; virtual appraisals & total-loss settlement product line; Celent Luminary 2026.
- Origami: OFAC sanctions search; 1099 production; CMS-111; ISO Claims Search; ODG integration; EDI FROI/SROI; deductible management & billing; RMIS suite framing (TCOR, allocations, exposure); Celent Luminary consecutive years; IIGF 100K-claim migration.
- Sapiens: ClaimsMaster naming; IDITSuite/PolicyMaster/BillingMaster/DigitalSuite coupling; Celent 2024 Luminary quote; metadata/rules architecture.
- Guidewire: unreachable — no vendor-specific claims recorded.

## Boundary Findings

1. **vs Claims Adjuster Platform (§08 sibling, processed; joint-review flag)** — DISCHARGED from this side with **keep-both**. The whose-work seam holds in both directions:
   - Claims management centers the **claims organization's lifecycle and book of claims**: intake, registration, coverage verification, assignment, reserving, payment ledger, recoveries, QA, reporting. The adjuster is one role inside it; the system owns the financial position and the lifecycle of record.
   - The adjuster platform centers **one adjuster's assessment-to-settlement loop on one file**: loss assessment evidence, valuation/estimate construction, review/QA of estimates, negotiation, settlement disposition reported back to the payer.
   - Overlap zone confirmed: Snapsheet sells both a complete claims system (this Type) and virtual appraisals/total-loss settlement (adjuster-side valuation); suite products embed claim-file work surfaces. Feature lists cannot separate the Types; the whose-work test can.
   - Structural tells observed this pass: claims systems speak in **reserves/payments/recoveries/coverage verification** (money-of-the-payer vocabulary); adjuster platforms speak in **estimates/scopes/depreciation/pricing data** (valuation-of-the-loss vocabulary). A claims system can run a book with no estimate machinery (e.g., life/disability, liability settlements); an adjuster platform cannot run without valuation machinery.
   - Recommendation recorded: keep both Types; the adjuster platform is the workbench facet that attaches to (or is embedded in) the claims system of record.

2. **vs Insurance Policy Administration System** — different lifecycle object: policy (quote→bind→endorse→renew) vs claim (loss→resolution). Claims reference policy data; every sampled suite sells policy admin as a separate module (Duck Creek CORE Policy; Origami Policy Administration; Sapiens PolicyMaster/IDITSuite). Boundary: which lifecycle is the system of record.

3. **vs Underwriting Workbench / Insurance Underwriting Platform** — pre-binding risk selection/pricing vs post-loss adjudication. Opposite ends of the policy lifecycle; no object overlap beyond the policy reference.

4. **vs Payer Claims Processing / Provider Claims Management (§22 healthcare)** — same word "claims", different object world: healthcare claims are billing adjudication of medical encounters (codes, remittance, provider networks); insurance claims are loss adjudication (coverage, reserves, adjusters). No structural overlap; no merge risk. Recorded so future passes don't conflate.

5. **vs Construction Claims Management (§17)** — contractual claims/disputes on projects; unrelated object world.

6. **vs Insurance Agency Management / Broker Management Platform (§08, processed)** — agency systems carry a claims-*logging* capability linked to policies (recorded in that pass); the claims system is the payer-side system of record where the claim is actually adjudicated and paid. Direction of work differs (agency forwards/track vs payer adjudicates).

7. **vs generic Case Management / Complaint & Escalation Management** — without the coverage-entitlement binding and the reserve/payment financial position, a claims tool degenerates into generic case management; those two properties are the discriminators.

8. **vs Fraud Detection Platform (§15)** — fraud engines are integrated data/decision providers; the claims system records indicators and SIU referrals but detection modeling is the adjacent Type.

9. **Internal naming note** — the market uses "claims management" and "claims administration" interchangeably for this Type (Origami uses "Claims Administration" for the carrier-side product and "Claims Management" for the RMIS-side oversight of the same object world). The directory leaf name is fine; no alias problem.

## Uncertainties

- **Guidewire ClaimCenter** (largest market anchor) could not be fetched (429 ×2; JS docs). Market-structure claims about it are anchors only. If a later pass reaches Guidewire docs, the L0/L1 should be re-checked against ClaimCenter's actual object model (its exposure/financials modeling is reputedly richer than the sampled products' marketing surfaces).
- **Exact lifecycle stage names** vary by product; no universal stage list is asserted. The canonical progression (intake → verification → adjudication → resolution → closure) is a C-layer inference consistent with all four samples, not a vendor-standard taxonomy.
- **Reserve mechanics depth** (case reserves vs IBNR, reinsurance recoverable booking) not directly evidenced on fetched pages; the final doc speaks of "estimated obligation recorded against the claim" without asserting the case/IBNR split.
- **Life & pensions claims** not directly sampled; the evidenced Type is P&C + workers' comp centric. The definition is written to not exclude life claims (claim record + lifecycle + financial position holds), but the sample is P&C-heavy — recorded as a sampling limitation.
- **Payment execution depth** varies (some products execute payouts in-platform; others hand off to payment rails/billing); treated as variant, not definitional.

## Final Synthesis

Insurance Claims Management is the **payer-side claims system of record**: it registers reported losses as claims bound to coverage/program context, carries each claim through a governed lifecycle from first notice to financial resolution, and maintains the claim's financial position (reserves and payments) as the authoritative record. Around that core, mature products add multi-channel FNOL intake with validation and duplicate detection, coverage verification, rules-based assignment with queues and SLAs, investigation and collaboration hubs, fraud signals and SIU referrals, subrogation/recovery, litigation management, omnichannel communications, QA/audits, straight-through processing for low-complexity claims, catastrophe surge handling, and deep integration with policy admin, estimating ecosystems, and payment rails. The Type spans carriers, MGAs, TPAs, risk pools, guaranty funds, and self-insured operators; packaging ranges from core-suite modules to standalone cloud platforms to multi-domain risk platforms.

The joint-review flag with Claims Adjuster Platform is discharged with keep-both: the claims system owns the organization's claim lifecycle and ledger; the adjuster platform owns the individual adjuster's assessment-to-settlement loop and attaches to (or is embedded in) the claims system.
