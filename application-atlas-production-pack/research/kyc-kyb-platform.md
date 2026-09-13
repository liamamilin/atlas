# Research Notes — KYC / KYB Platform

Research date: 2026-09-08
Leaf: KYC / KYB Platform (§15 Cybersecurity, Identity & Trust), slug `kyc-kyb-platform`

## Research Goal

Understand what a KYC / KYB Platform is as an Application Type: what objects it holds, what users do with them, how the due-diligence workflow actually flows, and where its boundaries sit against the already-processed siblings (Identity Verification, Sanctions Screening Platform, AML Platform, Transaction Monitoring Platform) and other neighbors. A pre-hung coordination note from the identity-verification pass (STATUS.md 2026-09-08) recommends: keep-both, seam at the object model — identity verification centers the verification ACT; KYC/KYB should center the compliance PROGRAM (entity case file, relationship risk classification, screening regime, EDD, ongoing monitoring, regulator-facing records). This pass tests and discharges that note.

## Initial Boundary (hypothesis before research)

- KYC = "Know Your Customer": the regulated due-diligence obligation institutions perform before and during a customer relationship. KYB = "Know Your Business": the same for legal-entity counterparties (registry data, ownership/UBO).
- Hypothesis: the Type is not the verification act (that is the Identity Verification sibling) but the compliance program that wraps verification, screening, risk assessment, decision, and record-keeping into a maintained customer file.
- Nearest confusions: Identity Verification (the act), Sanctions Screening (one step), AML/TM (behavior monitoring after onboarding), Fraud Prevention (loss prevention), Due Diligence Platform (M&A/transaction diligence), Background Check Platform (employment), Customer Onboarding Platform (journey), CRM (customer records without compliance evidence semantics).

## Research Questions

1. What is the central object — attempt, applicant, case, business, file, profile?
2. How does KYB differ structurally from KYC (registry data, UBO, associated parties)?
3. Where does risk classification and the approve/reject decision live? Is it check-level pass/fail or relationship-level judgment?
4. How is screening (sanctions/PEP/adverse media) positioned — a standalone capability or a step inside a program?
5. What happens after approval — ongoing monitoring, rescreening, periodic review, refresh/remediation?
6. What is retained and for whom (regulator/auditor-facing recordkeeping)?
7. How do products that are primarily identity-verification vendors package "KYC"? (Tests the sibling seam.)
8. What is standard vs optional vs vendor-specific?

## Representative Products

Chosen for market representation, documentation completeness, different product philosophies and customer tiers:

| Product | Pole | Evidence depth |
|---|---|---|
| Sumsub | full-cycle compliance platform (KYC + KYB + TM in one product), strong public documentation | Tier-1 docs (direct) |
| Persona | modular identity/compliance orchestration platform (API-first, mid-market/startup) | Tier-1 docs (direct) |
| Middesk | KYB-first business identity & compliance for platforms/fintech | Tier-1 docs (direct) |
| Encompass | enterprise corporate-KYC automation for banks (registry-data-led, perpetual KYC) | Tier-2 product pages (direct) |

Rejected/deferred samples: Jumio (skipped for sample economy; IDV pole already covered by sibling pass), Trulioo/Socure/Veriff (unreachable in sibling pass 2026-09-08, not retried per network rules), Persona marketing KYC solution page (403; substituted by docs evidence).

## Sources

Fetched 2026-09-08:

- Sumsub docs — docs.sumsub.com: /docs/overview, /docs/business-verification, /docs/verify-businesses, /docs/case-management, /docs/aml-screening, /docs/ongoing-aml-monitoring (all fetched as markdown)
- Persona docs — docs.withpersona.com: /, /api-introduction, /inquiries, /accounts, /cases, /workflows, /verifications
- Middesk docs — docs.middesk.com: /, /how-middesk-works, /verify-business, /lifecycle-of-business, /monitor-activity
- Encompass — encompasscorporation.com: homepage (nav/platform structure), /encompass-platform/perpetual-kyc-due-diligence/

Not reachable: withpersona.com/solutions/kyc (403). Persona KYC packaging therefore evidenced from docs pages that reference "Solutions… pre-made inquiry templates for common use cases, like KYC and age verification" and the KYC Solution help-center link in the inquiries page.

## Product Observations

### Sumsub (Evidence layer A — Tier-1 docs)

- Docs root: "Verify users, businesses, and transactions, resolve cases… from a single Dashboard." Products grouped: User Verification, Business Verification, Transaction Monitoring, Travel Rule, Case Management.
- **Applicant** is the central record (individual or company); verification **levels** are configurable flows composed of steps; **Workflow Builder** composes rules/automation; **Case Management** handles KYC/KYB/AML cases with assignment, blueprints, audit trails, "export audit-ready reports".
- KYB page defines Know Your Business as "a due diligence procedure aimed at establishing the structure, ownership, purpose and activities of a given company", tied to AML/CFT regulation, FATF, EU AML directives.
- KYB level types: **Full KYB** (registry + AML screening + manual review), **Registry and AML Check**, **AML Check**. Steps: Company Data (pre-filled from corporate registries), Associated parties (UBOs, shareholders, directors, representatives… with per-role KYC levels), Company documents, Questionnaire, Email/Phone.
- **Ownership thresholds** configure who counts as UBO vs shareholder (ownership-percentage fields); **status synchronization**: company status tied to associated parties (e.g., reject company if any associated party rejected; final decision only after all parties verified).
- Corporate registry check: "Data provided by applicant" vs "Data extracted from corporate registry" (company info, officers, persons with significant control incl. direct/indirect/beneficial ownership percentages); **Expert-assisted KYB** fallback; automated company document reading (ACDR); company tax check.
- AML screening: sanctions, PEP, warnings, fitness & probity, adverse media; provider selection (ComplyAdvantage); name-match fuzziness; auto-screening; resolution rule chains; AML cases; audit events/webhooks.
- **Ongoing AML monitoring**: keeps applicant data up to date with changes to sanctions lists/watchlists/adverse media after approval; alerts on approved applicants move them to Pending/review; auto-disable for rejected; delegable to compliance officers.
- Applicant scoring/risk labels; country/IP restrictions; "Reusable KYC" (reuse verified data across onboarding).

### Persona (Evidence layer A — Tier-1 docs)

- API intro: identity verification + risk assessment + compliance; "onboard customers… comply with KYC/AML regulations".
- **Inquiry** = one instance of a verification flow; **inquiry templates** configure it; "Solutions… include pre-made inquiry templates for common use cases, like KYC and age verification".
- **Account** groups ALL data from a single person **or business**: inquiries, reports, cases, documents — e.g., onboarding inquiry + re-verification a year later linked to one account; custom account types and statuses; spotting patterns across inquiries.
- Inquiry lifecycle: created → approved / declined / needs_review; webhooks; Dashboard review.
- **Cases**: operations teams investigate and decision end users "flagged by a Persona inquiry"; case object collects inquiries, accounts, reports + external JSON data; assignment; case templates; automations; analytics; help-center link "AML Case Management & SAR Filing Overview".
- **Workflows**: trigger→steps automation — approve/decline/mark-for-review inquiries, create cases, run reports ("Person Watchlist and Adverse Media Report"), ingest third-party data, recurring triggers "against a set of matching objects (e.g. accounts…) on a recurring schedule" — the orchestration surface for re-verification/ongoing monitoring.
- **Verifications**: modular check types (government ID, selfie, document, database) with configurable checks.

### Middesk (Evidence layer A — Tier-1 docs)

- Positioning: "Verify identities, prevent fraud, and assess risk with a single API. Build secure onboarding flows, compliance checks, and risk monitoring."
- **Business** is the single primary object: "the Middesk representation of the business entity that you engage with in your platform"; lifecycle Submission → Verification → Approval; statuses open → pending → in_audit → in_review → approved/rejected; auto-resolve or "Analyst in the Loop"; "always provides auditable records of how a Business object changes over time".
- **Orders** trigger additional reports: TIN verification, name+address, international registrations (unified format), sanctions/OFAC screening, adverse media, enhanced screenings (global watchlists + PEP "for a business and its associated people"), **KYC via Socure** "to perform due diligence checks on people associated with a business".
- **Rulesets/Policies**: "Automate business approval decisions using Middesk Policies or with rulesets managed in your backend logic"; review insights feed the client's approval decision.
- **Monitoring**: enroll an approved business; Middesk tracks bankruptcies, SoS registration changes, TIN registration changes, new watchlist hits, UCC liens — "monitor… businesses to watch for relevant activity after the approval stage".
- Use cases framed as KYB; the "client" approves/rejects.

### Encompass (Evidence layer B — Tier-2 product pages; marketing-level claims kept conceptual)

- EC360 "Corporate Digital Identity (CDI) platform" for banks: "Transforming KYC with process automation and CDI profiles"; CDI profile = "real-time digital KYC profile".
- Platform blocks (nav): Dynamic KYC process automation, Global public data, **UBO verification**, PEP/sanctions/adverse media screening, CDI profiles, API, Dynamic audit trail, Data attribute lineage, Intelligent document processing.
- Use cases (nav): KYC onboarding, Customer due diligence, **Enhanced due diligence**, KYC remediation and refresh, **Perpetual KYC**.
- pKYC page: "replaces static, periodic reviews with dynamic, continuous monitoring"; keeps "customer's risk profile and entity data… up-to-date"; **delta analysis** ("compare only what has changed… when it's refreshed"); "audit-ready decision trails… every decision is traceable, explainable, and regulator-ready"; data provenance/lineage; STP for low-risk, analyst attention for higher-risk; integrates with case management (PEGA named); sectors: corporate & investment banking, commercial banking, challenger banks, managed service, correspondent banking.
- Statement of purpose (about): "A full and accurate picture of beneficial ownership is the foundation of effective KYC."

## Cross-product Comparison

| Structure | Sumsub | Persona | Middesk | Encompass | Reading |
|---|---|---|---|---|---|
| Central subject record spanning the whole relationship | Applicant (person or company) | Account (person or business) | Business (+ associated people) | CDI profile (corporate client) | 4/4 — the program file is the Type's spine (A) |
| Diligence steps executed INTO the file | Levels/workflows: registry check, docs, UBO KYC, screening | Inquiries + reports (watchlist, adverse media, DB) run via workflows | Orders: TIN, name/address, sanctions, adverse media, KYC-of-associated-people | Registry data, UBO verification, screening, document processing | 4/4 (A) |
| Risk/standards assessment + recorded relationship decision | Risk score/labels; level types auto-decline; workflow approve/reject/manual review | Approve/decline/needs-review; workflow conditionals on report/inquiry criteria | Policies/rulesets → client approves/rejects; analyst-in-the-loop | Risk-based STP vs analyst; EDD use case | 4/4 — decision gate is program-level, not check-level (A) |
| Manual review/case machinery for exceptions | Case Management (KYC/KYB/AML cases) | Cases | Analyst in the loop (in_audit) | integrates with case management systems (PEGA named) | 4/4 (A/B — Encompass is integration-framed) |
| Screening as a step inside the program | AML screening step in levels + ongoing monitoring | Watchlist/adverse-media reports run in workflows | Sanctions/adverse-media/enhanced watchlist orders | PEP/sanctions/adverse-media screening block | 4/4 — screening embedded, not the center (A) |
| Standing maintenance after approval | Ongoing AML monitoring; re-screening | Re-verification across account lifetime; recurring workflow triggers on accounts | Monitoring: SoS/TIN/watchlist/bankruptcy/lien | Perpetual KYC; remediation & refresh | 4/4 (A) |
| Audit/examiner-facing recordkeeping | Audit trails; audit-ready reports | auditable dashboard history (accounts/cases) | "auditable records of how a Business object changes over time" | Dynamic audit trail; decision trails "regulator-ready"; data lineage | 4/4 (A; Persona at concept level) |
| KYB = same program model, entity subject + ownership graph | company applicant + associated parties + thresholds + status sync | accounts "person or business" | Business + associated people | CDI/UBO as the flagship | 4/4 — KYB is a subject-axis variant, not a separate program (A) |
| Explicit multi-level risk rating as first-class object | yes (risk score/labels) | not observed as first-class (conditions + tags instead) | not observed (policies + insights) | risk profile language, risk-based approach | common-in-mature, NOT definitional |
| Applicant-facing capture UI (SDK/hosted flow) | WebSDK, verification links | hosted/embedded/SDK flows | API-first (client owns UX) | client outreach / document processing | common, packaging-dependent |
| EDD as named escalation path | questionnaire steps + manual review (EDD not named in fetched pages) | not named | not named | named use case | EDD named at product-page level in 1/4; escalation-to-deeper-review common, exact naming varies |

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

The KYC/KYB Platform is the institution's customer-due-diligence program system of record. Four jointly-held structures; removing any one stops the product being this Type:

1. **The due-diligence case file of record** — a persistent, individually identified compliance record per diligence subject (a person as customer, or a legal entity/business as counterparty), held by the relying institution, accumulating the subject's diligence content: declared information, verified identity/registry/beneficial-ownership evidence, collected documents, screening results, and the history of diligence actions. (remove → one-shot verification/screening calls that return results and keep no accumulated program file = identity-verification / screening-API territory)
2. **The diligence regime executed into the file** — the institution's defined steps for establishing who the subject is and whether they may be served — identity/ownership evidence gathering (documents, registry data, UBO determination), questionnaires, sanctions/PEP/adverse-media screening — are carried out and their results recorded into the file, whether performed by the platform's own checks, delegated data sources, or reviewers. (remove → an empty folder/CRM record with nothing diligence-shaped happening)
3. **Risk-based assessment producing a recorded relationship decision** — the institution's configured standards applied to the file yield a risk classification of the subject/relationship and a recorded, attributed, reasoned decision — approve, reject, or escalate to enhanced due diligence — as the program's gate on the relationship. (remove → data collection with check-level pass/fail but no judgment of the relationship = a verification/reporting utility)
4. **Standing, regulator-facing maintenance** — the file is kept current and examinable across the relationship: attributed actions and reasons, retention as compliance evidence, and refresh as diligence obligations recur (periodic review, rescreening, event/registry-change-triggered re-review). (remove → a one-shot onboarding act whose evidence lives elsewhere)

Jointly-held load-bearing:
- 1 alone = a file cabinet / CRM record with compliance flavor
- 2 without 1 = discrete check services (IDV API + screening API, un-accumulated)
- 3 without 1+2 = a scoring model with no evidence trail
- 4 without 2 = an empty review calendar
- 1+2 without 3 = evidence collection with no gate
- 1+3 without 2 = asserted status without evidence
- 2+3 without 1 = stateless screening pipeline
- 1+4 without 2+3 = an archive
- 2+4 without 1 = monitoring with no subject

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Configuration surfaces for the regime: verification levels / inquiry templates / policies / KYC process automation (4/4)
- Applicant-facing capture: embedded SDKs, hosted flows, verification links, outreach/document exchange
- Manual-review/case machinery for exceptions: cases with assignment, notes, SLAs, audit
- Screening content and match resolution: sanctions/PEP/watchlists/adverse media, provider integrations, fuzzy matching, dispositioning
- Risk scoring / risk labels; country/IP rules
- Ongoing monitoring machinery: rescreening on list changes, registry/bankruptcy/lien change monitoring, delta analysis, remediation/refresh campaigns
- Corporate-registry data sources; UBO/ownership-structure determination with configurable thresholds; associated-party KYC with status synchronization (KYB pole)
- Integration spine: APIs, webhooks, case-management/CRM handoffs
- Audit trails, decision trails, data lineage, exportable reports

### L2 — Variant / Optional Structure

- Subject axis: individual KYC ↔ business KYB ↔ both in one platform
- Segment/tier: API-first fintech/platform pole ↔ enterprise bank corporate-onboarding pole ↔ managed-service operation
- Packaging: full-program platform ↔ verification-act vendor packaging a "KYC solution" of templates/programs over its act machinery ↔ registry-data-led corporate pole
- Regulatory regime emphasis (FATF-style CDD, US CIP, EU AMLD/AMLR) and geography of registry/data coverage
- Review model: STP-auto ↔ analyst-in-the-loop ↔ outsourced/expert-assisted review
- Reusable-KYC / verified-identity reuse across services; travel-rule/crypto extensions (Sumsub-observed, optional)

### L3 — Vendor-specific (research notes only)

- Sumsub: KYB level types (Full KYB / Registry and AML Check / AML Check), Expert-assisted KYB, ACDR, Reusable KYC/Sumsub ID, WebSDK, ComplyAdvantage provider wiring, ongoing-monitoring status cycle (auto-disable ~24h after rejection), status names (Approved/Rejected/Requires action/Pending), UBO/shareholder percentage threshold fields, MCP/AI tooling.
- Persona: inquiry/inquiry-template/session model, account custom types/statuses, workflow step library (Trust Device, redaction, Salesforce/Hubspot/Zendesk actions), recurring workflow triggers, "AML Case Management & SAR Filing" help-center article, Person Watchlist & Adverse Media report names.
- Middesk: Business statuses (open/pending/in_audit/in_review/approved/rejected), Orders/report catalog (TIN, name+address, international, OFAC, adverse media, enhanced watchlist, KYC-via-Socure), monitoring set (SoS/TIN/watchlists/bankruptcies/liens), sandbox/enhanced sandbox, Agents (referenced in nav).
- Encompass: EC360/CDI naming, delta analysis, golden-source data, data attribute lineage, EC product split (Public Automation / Private Outreach / Review / CoorpID), PEGA + Capgemini pKYC sandbox integrations, MCP server, client logos/awards.

## Rejected Findings

- "KYB is a different Application Type from KYC" — rejected: all sampled products realize one program model whose subject axis varies (person ↔ legal entity + ownership graph). Sumsub runs both on the same applicant/level/workflow/case model; Persona accounts explicitly span "a single person or business".
- "Real-time/event-driven continuous refresh (perpetual KYC) is definitional" — rejected: it is the modern implementation of the standing-maintenance leg. Paper-era and periodic-review-only programs are recognizably the same Type (see historical check).
- "Explicit multi-level risk rating (low/medium/high) is definitional" — rejected: only Sumsub evidences a first-class risk score/label in-sample; Persona/Middesk express the same judgment as policy conditions + decision outcomes. The invariant is the risk-based recorded decision, not a specific rating taxonomy.
- "Screening is the center" — rejected: sanctions screening is a regime step inside the program in all four products; the standalone determination Type is the sanctions-screening sibling.
- "The applicant-facing capture UI is definitional" — rejected: Middesk and Encompass document API-first/automation-first postures where the platform client owns or delegates the UX.

## Historical / Market-Sample Check

- Paper-era bank account opening: signature card + certified ID copy + customer information sheet; clerk checks name against a (printed) sanctions/watch list; risk note written; account approved/rejected; file retained with periodic-review stamps. Satisfies all four legs at analog level (file, regime executed into file, risk-based decision, standing retained record with refresh obligation). ✓
- 1990s–2000s electronic onboarding: database screening, digital document collection, workflowed approval, audit logs — satisfies without SDKs, AI, or event-driven pKYC. ✓
- Older/regional products: region-specific registry coverage and list sets change, but the program structure does not. ✓
- One-shot IDV products (no program file, no risk decision, no standing record) correctly fail legs 1/3/4 → they are the sibling Type, not this one. ✓
- Definition names no SDK, cloud, AI, pKYC machinery, or specific regulation editions. ✓

## Boundary Findings

- **vs Identity Verification (§15 sibling — coordination note discharged from this side):** ratified keep-both. The seam is the object model: identity verification centers the verification ACT (subject, evidence, checks, decision returned to the relying organization); KYC/KYB centers the compliance PROGRAM — the accumulated due-diligence file, the risk-based relationship decision, the screening regime, EDD escalation, standing maintenance, regulator-facing recordkeeping. In-sample packaging evidence: Persona's docs route "KYC" through pre-made solutions/templates over inquiry machinery; Sumsub's KYB runs KYC checks on associated parties inside the company file; Middesk buys person-KYC from a third party (Socure) while keeping the program record. KYB-adjacent business-entity checks stay a variant here as the KYB subject axis (no claim contested from the sibling).
- **vs Sanctions Screening Platform (§08):** who-is-this-and-may-we-serve-them (program file + risk decision) vs are-you-prohibited (list-membership determination + screening evidence). Screening appears here as one orchestrated regime step whose results feed the file; the sanctions platform centers the screened population and match dispositions as the terminal artifact. Machinery converges; question and artifact differ (consistent with that pass's own boundary note).
- **vs AML Platform (§08):** produces-vs-consumes seam. The AML pass's L0 leg-1 holds "monitored customers with due-diligence context" as *ingested context* for activity monitoring; this Type *produces and maintains* that context (who the customer is, verified; risk classification; screening state) and its terminal artifact is the recorded relationship decision, not the SAR/STR. The aml-platform doc itself states "Customer onboarded (via KYC processes; the AML platform consumes this context)".
- **vs Transaction Monitoring Platform (§08):** behavior surveillance of the ingoing relationship vs diligence on the subject entering it; TM's terminal output is the dispositioned alert, this Type's is the approved/rejected/referred relationship. (Consistent with the TM pass's capability-vs-program test.)
- **vs Fraud Prevention Platform (§08):** compliance obligation (prove diligence to a regulator) vs loss prevention (decide the risky activity). Shared signals, different master.
- **vs Background Check Platform (§09):** records about a person's history for employment decisions vs identity/risk diligence for a regulated service relationship.
- **vs Government Digital Identity (§24):** state-run identity issuance/federation vs an institution's private compliance program over its own customers.
- **vs Due Diligence Platform (§11) / Virtual Data Room:** diligence on a transaction (M&A, investment) vs diligence on a customer relationship for regulatory admission; different object of diligence.
- **vs Customer Onboarding Platform (§07) and CRM:** journey orchestration and commercial relationship records vs the compliance evidence file and its gate. Onboarding tools may *call into* this Type; they do not hold the diligence regime.
- **"Remove-what" criterion:** remove the accumulated program file + risk decision + standing maintenance (keep only evidence capture and check evaluation) → Identity Verification. Remove the file and keep only list screening → Sanctions Screening. Keep the file but replace diligence with behavior monitoring → AML/TM territory.

## Uncertainties

- Persona's KYC *solution* marketing page was unreachable (403); KYC packaging evidence rests on docs pages (solutions incl. KYC; accounts; cases). Assertion strength kept at doc level.
- Encompass evidence is product-page level (Tier-2); workflow mechanics (exact refresh triggers, review queues) kept conceptual; no operational specifics asserted.
- Precise regulatory obligations (retention periods, review frequencies, CIP/AMLD specifics) were NOT asserted — products name FATF/EU AMLD context (Sumsub KYB page) but no exact numbers were verified in fetched pages.
- Whether every product in the market carries in-product case management (vs pure integration into external case tools) is unresolved; Encompass frames case management as an integration. Held as common-not-definitional.
- Exact wording of EDD as a named product feature varies; escalation-to-deeper-review is the structural commonality.

## Final Synthesis

The KYC / KYB Platform is the customer-due-diligence compliance program made into software. Its spine is the accumulated case file per diligence subject — a person or a legal entity — into which the institution's diligence regime (identity/ownership evidence, registry data, screening) is executed and recorded; over that file the institution's configured risk standards produce a recorded relationship decision (approve / reject / enhanced due diligence); and the file stands afterwards as the regulator-facing record, refreshed as obligations recur. KYB is the same program with the legal entity as subject: registry identity, ownership structure and beneficial owners determined (often against configurable ownership thresholds), associated parties each diligenced with their status synchronized into the company's outcome. Around this spine, mature products add configuration surfaces (levels/templates/policies/workflows), applicant-facing capture, screening content and match resolution, manual-review cases, risk scoring, ongoing monitoring (rescreening, registry-change monitoring, delta refresh), and audit/examiner-facing trails. The Type is distinct from the verification act (Identity Verification), the prohibited-party determination (Sanctions Screening), and the behavior-monitoring programs (AML / Transaction Monitoring) — each of which it consumes as a step, a data source, or a downstream consumer of its risk context.
