# Research Notes — Commercial Loan Origination

Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what lender-side software for originating commercial (business) loans actually is and how it works: what objects exist, what the pipeline does from intake to booking, how credit analysis and approval machinery is structured, who operates it, and where its boundary runs against loan management (post-funding), generic/consumer/mortgage origination, credit decisioning, credit monitoring, and CRM.

Prior-pass context:
- The commercial-loan-management pass (2026-09-07) confirmed the funding seam (origination = pre-funding pipeline; management = post-funding servicing ledger) and flagged joint review when this leaf is processed. nCino was sampled there as the origination pole.
- The commercial-banking-platform pass flagged that the loan lifecycle is owned by loan-lifecycle systems on the bank-staff side, joint review recommended when origination/management are processed.

This pass discharges the origination side of both flags.

---

## Initial Boundary (hypothesis before research)

- Hypothesis: a Commercial Loan Origination application is the lending institution's staff-side pipeline system for business credit requests — intake, borrower/relationship capture, financial analysis (spreading), credit memo, approval workflow under credit policy, deal structuring/pricing, closing documentation, and booking/disbursement handoff to servicing. Its center of gravity is pre-funding; the funded loan book belongs to Commercial Loan Management.
- Nearest neighbors: Commercial Loan Management (downstream, funding seam), Loan Origination System (generic sector-neutral leaf), Consumer Lending Platform, Mortgage Origination Platform, Credit Decisioning Platform, Credit Risk / Portfolio Monitoring platforms, Commercial Banking Platform (client-facing channel), CRM (relationship/deal view overlap), Insurance Underwriting Workbench (same word, different sector).
- Unknowns going in: (a) whether covenant/monitoring machinery belongs to origination or monitoring/management; (b) whether collateral machinery is a documented common structure; (c) how deep borrower-facing intake goes; (d) whether pricing/profitability machinery is common; (e) whether a decisioning layer (auto-approve/decline) is definitional or common.

---

## Research Questions

1. What is the central pipeline object (application / deal / request) and what stages does it move through?
2. What is the borrower record — entity, related parties, principals, guarantors?
3. How is credit analysis done — spreading, global cash flow, coverage ratios, scoring models, stress tests?
4. How does the approval decision work — credit memo, policy rules, approval workflow, auto-approve/decline/manual-review parameters?
5. What loan product structures does a commercial request take (term loan, revolver, CRE, small business, government-guaranteed)?
6. How do pricing/profitability, deal structuring, and covenants appear pre-funding?
7. What happens at closing — documents, e-signature, conditions, exceptions/ticklers?
8. Where does origination end (booking/disbursement handoff), and what integrations mark the seam?
9. Who operates the system (lenders, credit analysts, underwriters, loan operations) and in what institutions (banks, credit unions, finance companies)?
10. What interfaces exist (pipeline boards, deal workspaces, spreading worksheets, memos, queues)?
11. Where are the boundaries vs management/monitoring/decisioning/CRM?

---

## Representative Products

Selection rationale: market representativeness (the cloud-LOS category leader + a heritage mid-market lending specialist + an analytics-led global risk vendor), different product philosophies (platform suite vs mid-market LOS vs risk-analytics-first vs documentation specialist), different customer tiers (large/regional banks vs community banks & credit unions vs finance companies).

1. **nCino (Commercial Lending / CLOS)** — the category-defining cloud "Commercial Loan Origination System"; enterprise platform pole; also the boundary pole vs monitoring (sampled in the management pass; re-fetched here for origination depth).
2. **Baker Hill (UN/FY / NextGen commercial LOS + Statement Spreading)** — 40+ year heritage lending specialist serving banks, credit unions, finance companies; mid-market pole; documents deal management, spreading, tickler/exception machinery unusually explicitly.
3. **Moody's Lending Suite (Loan Origination)** — risk/analytics-first pole from a global credit-data vendor; documents a complete four-stage origination workflow and an explicit origination/monitoring split inside one suite.
4. **Finastra LaserPro (+ Originate Business Loans)** — documentation/closing specialist pole; a document-generation engine with compliance warranty used across commercial/consumer/mortgage; evidences the closing-documentation machinery as a separable product family. (CreditQuest was the intended sample but its URL 404'd; LaserPro + the "Originate Business Loans and Deposits" product page fill the same vendor-family role.)

**Abrigo** (major risk-led competitor, banks/CUs) was selected originally but abandoned: www.abrigo.com returned 502 on three attempts (root, /lending/, /products/loan-origination-software/) on 2026-09-07. Recorded per the network-retry rule; no claims rest on Abrigo. (LaserPro's page confirms in passing that its document engine "integrates with 70+ core systems and platforms like nCino and Abrigo" — a third-party mention, not evidence about Abrigo's own design.)

---

## Sources

All fetched 2026-09-07. All official vendor product/marketing pages (Tier 2). No Tier-1 operational documentation (logged-in help centers, user guides) was reachable; consistent with prior finance passes.

- nCino Commercial Lending — https://www.ncino.com/solutions/commercial-lending
- Baker Hill commercial LOS — https://bakerhill.com/commercial-lending
- Baker Hill Statement Spreading — https://bakerhill.com/statement-spreading
- Baker Hill root (solution taxonomy, integrations) — https://bakerhill.com/
- Moody's Lending Suite — https://www.moodys.com/web/en/us/solutions/lending.html
- Moody's Lending Suite Loan Origination — https://www.moodys.com/web/en/us/solutions/lending/loan-origination.html
- Finastra LaserPro — https://www.finastra.com/lending/solutions/laserpro
- Finastra Lending (portfolio taxonomy) — https://www.finastra.com/lending

Failed / abandoned (recorded per network-retry rule):
- abrigo.com root, /lending/, /products/loan-origination-software/ → 502 ×3, abandoned
- finastra.com/lending/solutions/fusion-credit-quest → 404 (site restructure; LaserPro substituted within the same vendor)
- moodysanalytics.com/lending-suite → redirected to moodys.com corporate root; correct solution pages found via footer navigation

**Source-access limitation**: every claim rests on official product pages (positioning, feature text, workflow descriptions, FAQs). Operational precision — stage-count defaults, dollar thresholds, posting conventions, specific document templates — is not observable from these pages and is deliberately not asserted. Assertion strength is calibrated throughout; no memory-filled operational detail was substituted.

---

## Product A — nCino (Commercial Lending / CLOS)

Vendor self-positioning: "Commercial Loan Origination System" (CLOS); "Intelligence Built for Commercial Lending". Marketing metrics ("$3.3T in loans in a period of 12 months", "2,700+ customers") are vendor claims, recorded only.

### Key observations (evidence layer A unless noted)

- **Pipeline automation**: "Onboards new customers and assesses their needs faster with preconfigured workflows"; "Automates pre-qualifications and credit approvals based on your institution's policy rules"; "Identifies parameters in which a loan should be automatically approved, declined, or recommended for manual review."
- **Deal Management** (within the CLOS): "access and manage the overall deals of your clients' loan and treasury products in real time"; "complete view of the relationship in a single location"; "structur[ing] and management of credit/non-credit deals and products"; "supports creation of sub-loans, information cloning, and bulk editing of details for shared records"; "provides commercial bankers with a way to easily navigate through large numbers of records."
- **Credit analysis**: "Seamlessly integrated into the commercial loan origination workflow, nCino's Spreads contains a suite of powerful credit analysis tools to produce faster, higher-quality decisions." Separate **Automated Spreading** solution: "reduces the time it takes to spread financials, enabling portfolio growth by improving the speed and quality of credit decisions."
- **Compliance machinery**: "integrated document repository that incorporates your institution's policies and leaves a visual audit trail for auditors and teammates"; "generates automatic notifications to remind users when a covenant is approaching its due date and serves as a record of compliance for auditing purposes"; "provides regulators and auditors with loan reports."
- **Collaboration framing**: "Improves collaboration and transparency across front, middle, and back offices."
- **Portfolio layer**: "real-time reporting for better portfolio management"; sibling page (sampled in management pass) markets monitoring ("from origination to monitoring") with **no servicing ledger documented** — boundary evidence.

### Interpretation

nCino documents the origination pipeline as preconfigured workflows around deals (credit and non-credit products of one relationship), with policy-rule-driven decisioning (auto-approve/decline/manual review), integrated spreading as the credit-analysis engine, and document/compliance machinery. Covenant notifications exist as reminders/records at origination, not as a servicing ledger. The deal object spans the whole relationship (loan AND treasury products) — the platform pole.

---

## Product B — Baker Hill (UN/FY / NextGen commercial LOS + Statement Spreading)

Vendor self-positioning: "Commercial Loan Origination System… powered by UN/FY"; "Purpose-Built for Commercial and Small Business Lending"; 40+ years heritage claim; serves banks, credit unions, finance companies; roles: lending, credit, operations, risk, marketing, executive.

### Key observations (evidence layer A unless noted)

Commercial LOS page:

- **Deal management**: "UN/FY provides a single, centralized platform to manage all parties, documents, and workflows" ("Unified Deal Management").
- **Spreading**: "Our system intelligently extracts, standardizes, and analyzes financial data from complex documents, ensuring accuracy and consistency."
- **Smart Workflow Management** (enumerated features): "Tickler/Exception Items; Credit Policy Enforcement; Covenant Monitoring; Automated Task Routing."
- **Document management**: "secure storage, easy retrieval, and efficient organization of loan documents, **supporting credit memo creation** and broad loan documentation needs."
- **Portfolio management**: "always-on, proactive risk monitoring and alerts" (adjacent layer, not a servicing ledger).
- **Client Relationship Management**: "Import core data and get a complete view of complex commercial borrower relationships to make well-informed decisions."
- **FAQ definition**: "A Loan Origination System (LOS) is a digital tool designed to streamline the process of loan application, approval, and disbursement for commercial lending."
- Edition pole: "UN/FY Accelerate" — pre-configured LOS built on industry best practices.

Statement Spreading page:

- **What is spread**: "Spread tax returns and financial statements to gain insights into your borrower's performance."
- **Analysis outputs**: "analyze data to calculate GDSC and GCF while maintaining data integrity and traceability" (global debt-service coverage; global cash flow).
- **Projections**: "Run Projections… to understand how possible future performance impacts financial risk."
- **Covenants at spreading**: "Create the appropriate covenants while spreading to keep a pulse on your portfolio."
- **Document intake**: "easily collect the documents you need from borrowers with a client portal."
- **Benchmarks**: "Pull in RMA data to compare your borrowers' performance to the performance of their peers" (US market data provider).
- **Consistency machinery**: "Control spreading templates"; "Trace Data Back to the Source — know where data came from, how it changed, and where it's used"; "Enter Data Once, Use It Everywhere — push data from your spreads to your credit memo seamlessly."
- FAQ: spreading as "a first step in digitizing your processes to create consistency and streamline underwriting decisions."

Root/integrations: Equifax, Experian, DocuSign, Alloy, Encapture (bureaus, e-signature, identity, document capture). Small business lending described as "Scored, Judgmental, & SBA."

### Interpretation

Baker Hill documents the mid-market commercial LOS with the clearest enumeration of the operating machinery: deals with parties/documents/workflows; spreading of tax returns and financials with global cash-flow/coverage analysis, projections, and covenant creation at underwriting; tickler/exception items; credit-policy enforcement; task routing; credit memos fed directly from spreads; relationship view importing core-system data; and a definition that ends at disbursement. Small-business scoring (vs judgmental) and SBA sit as segment machinery within the same platform.

---

## Product C — Moody's Lending Suite (Loan Origination)

Vendor self-positioning: "an end-to-end loan origination system" making "confident credit decisions"; suite split into **Loan origination** and **Monitoring** solutions — the origination/monitoring seam documented inside one vendor's own packaging.

### Key observations (evidence layer A unless noted)

- **The complete origination workflow is explicitly documented in four stages**:
  1. **Borrower engagement** — "Digital loan application; Secure document collection; Target for profitability; Proactive KYC screening."
  2. **Spreading and scoring** — "AI-enabled spreading automation; Robust financial analysis; Integrated content; Model lifecycle management"; "in-house or Moody's award-winning models."
  3. **Underwriting and decisioning** — "Deal structuring; GenAI-generated credit memo; Loan conditions and policy expectations."
  4. **Loan operations** — "Complete data compilation; Auto-generated loan documents; Document exchange; E-signatures; **Core banking integration**."
- **Lifecycle framing**: "a modern, convenient, and transparent process from the initial credit request through to documentation, information gathering, decision-making, and closing."
- **Scoring**: "data, forecasts, scorecards, and stress-testing tools"; "integrated risk metrics for scoring credit applications."
- **Credit memo**: "GenAI combined with Moody's insights to generate comprehensive credit memos… automating the gathering of information, enriching the content, and writing narratives."
- **Risk framing**: "robust financial and credit risk analysis capabilities… comprehensive understanding of your borrowers' risk profiles."
- **Asset classes** (packaged variants): Commercial Real Estate; Agriculture; Small Business.
- **Monitoring** (separate solution): "Automated covenant management; Early risk detection; What-if analysis; Data ingestion."

### Interpretation

Moody's is the risk-analytics-first pole and — unusually — documents the entire origination workflow as four named stages ending at closing and core-banking integration. It also shows the seam inside one suite: origination (pre-funding pipeline) vs monitoring (covenant management, early risk detection over the book). The credit memo, deal structuring, conditions, scoring, and spreading are all first-class named objects.

---

## Product D — Finastra LaserPro (+ Originate Business Loans)

Vendor self-positioning: "Complete loan document management solution"; "loan document generation engine" with "40 years of compliance expertise"; suite FAQ: "For US consumer and commercial lending, the main solutions are LaserPro, Mortgagebot, and Originate."

### Key observations (evidence layer A unless noted)

- **Document generation as the core**: "Produce accurate loan documents faster with automated checks that reduce manual work, support compliance, and streamline commercial, consumer, and mortgage lending."
- **Compliance-first design**: "backed by a 50-state, up to $5 million warranty"; "continuous updates aligned with evolving regulations like Section 1071"; "nationwide network of compliance attorneys."
- **Closing-pipeline machinery around the engine**: **LaserPro Exchange** — "secure file requests, uploads, and sharing from application to close"; **LaserPro Conductor** — "automate document review and approvals… move loan packages faster"; **LaserPro Connect** — "transfers loan data from select LOS partners into LaserPro, enabling fast, accurate generation of compliant closing documents."
- **Spreading adjacency**: **LaserPro Analyze** — "automating the traditionally manual spreading process critical to lending decisions."
- **Related product**: "Finastra Originate Business Loans and Deposits — a unified, compliant platform for commercial deposit and loan applications… automated workflows and real-time decisioning."
- Integration evidence (third-party mention): "integrates with 70+ core systems and platforms like nCino and Abrigo."

### Interpretation

LaserPro shows that the closing-documentation layer of commercial origination is large and mature enough to be a standalone product family with its own compliance economy — generation from data, review/approval workflow, document exchange with borrowers, and intake connectors from upstream LOS platforms. The phrase "the traditionally manual spreading process critical to lending decisions" is also independent confirmation of spreading's centrality to commercial credit.

---

## Cross-product Comparison

| Dimension | nCino (CLOS) | Baker Hill (UN/FY) | Moody's Lending Suite | Finastra LaserPro |
|---|---|---|---|---|
| Center of gravity | cloud platform, relationship-centric deals | mid-market commercial LOS | risk-analytics-first origination | closing documentation engine |
| Pipeline object | deals (credit + non-credit products), sub-loans | deals w/ parties, documents, workflows | credit request → closing, four named stages | loan packages application → close |
| Spreading | Spreads + Automated Spreading, integrated into workflow | tax returns + financials; GDSC/GCF; projections; templates; traceability | AI-enabled spreading + scoring/scorecards/stress tests | Analyze module (adjacent) |
| Decision machinery | policy rules → auto-approve / decline / manual review | credit policy enforcement; task routing | deal structuring; loan conditions & policy expectations; scorecards | (review/approval of document packages) |
| Credit memo | (document repository context) | explicit; memos fed from spreads | explicit; GenAI-generated | — |
| Conditions / exceptions | covenant due-date notifications; audit trail | tickler/exception items | loan conditions; document exchange | file requests; review/approval workflow |
| Closing | document repository w/ audit trail | document management | auto-generated loan documents; e-signatures; core banking integration | document generation; compliance warranty |
| Relationship view | "complete view of the relationship" (loan + treasury) | complete view of complex borrower relationships; core-data import | relationship/origination framing (softer) | — |
| Scoring/models | policy-rule parameters | small business: scored vs judgmental | in-house or vendor models; model lifecycle | — |
| Segment packaging | banks/CUs of all sizes (marketing) | banks, CUs, finance companies; SMB/SBA | CRE / Agriculture / Small Business editions | community banks + CUs (40%+ claim) |
| End state | portfolio reporting (post-booking monitoring adjacent) | "application, approval, and disbursement" | closing → core banking integration | compliant closing documents |
| Servicing ledger | absent (boundary evidence) | absent (portfolio monitoring only) | absent (monitoring is a separate solution) | absent |

Reading: the pipeline-of-deals + spreading + policy-governed approval + closing/booking chain appears in every sampled product family in some form — this is the stable common structure. The credit memo is explicit in three of four (nCino's fetched pages imply it via document/policy context but do not name it — kept at layer B). Tickler/exception machinery is explicit in Baker Hill and echoed in Moody's (conditions) and LaserPro (file requests/review) — layer B. Scoring/models: three of four (all but LaserPro). Borrower-facing intake: three of four (Moody's, Baker Hill client portal, LaserPro Exchange) — common, not definitional. Collateral machinery: **not surfaced on any fetched page** — recorded as an uncertainty, not asserted. Pricing/profitability: only Moody's ("Target for profitability") — product-specific within sample.

---

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

A Commercial Loan Origination application is the lending institution's staff-side system for carrying a business credit request from intake to a funded, booked loan. Smallest structure without which the Type stops being recognizable:

```text
Business borrower (+ related parties: principals, guarantors, affiliates)
└── Credit request / deal in a managed lender-side pipeline
    (staged, institution-defined; the system of record for in-flight requests)
    └── Credit assessment built on the borrower's financial and risk information
        (characteristically: spreading financial statements and analyzing
         cash-flow / coverage; the evidence base for the decision)
        └── Approval decision under the institution's credit policy
            (recorded approve / decline / conditions through an approval
             workflow; policy rules may auto-route simple requests)
            └── Execution to funding
                (terms assembled, closing documentation produced and executed,
                 conditions tracked; the request ends as a booked loan handed
                 to the servicing/booking system — or is declined/withdrawn)
```

Five properties:

1. **The business borrower as subject** — the population under assessment is organizations (with related parties), not consumers. This is what makes the leaf commercial.
2. **The credit request as a managed pipeline object** — a staged, institution-defined process owned by lender staff; the system is the record of in-flight credit work. Without a managed pipeline the product is a point tool, not origination.
3. **Credit assessment from borrower financial information** — the decision rests on analyzed evidence of the borrower's financial condition; in commercial lending the characteristic form is financial-statement spreading and cash-flow/coverage analysis.
4. **The approval decision under credit policy** — a recorded decision produced through the institution's approval machinery (policy rules, routing, conditions). Without policy-governed approval it is a generic application tracker.
5. **Execution to funding with a booking handoff** — approved requests are assembled into closable, fundable loans and handed to booking/servicing; declined/withdrawn requests are recorded outcomes. Without this terminal credit execution the product drifts toward CRM or decision-engine territory.

L0 is deliberately era- and region-neutral: a paper credit memorandum analyzed from manually spread statements, approved by a loan committee, closed from a document checklist, and booked into the loan ledger satisfies the conceptual core; the software digitizes and automates this loop.

### L1 — Common Mature Structure

Present across the sample (two or more products) but not definitional:

- **Financial spreading machinery** — extraction/standardization of tax returns and financial statements into analyzable form; templates; traceability; automated spreading is the modern realization (4/4 families; manual spreading is the degenerate case).
- **Global cash-flow / coverage analysis** — borrower-level analysis aggregating across entities and income sources (GDSC/GCF-class calculations; Baker Hill explicit, Moody's "robust financial analysis", nCino credit-analysis suite).
- **Credit memo authoring** — the structured analysis document supporting the decision; fed directly from spread data (Baker Hill, Moody's; nCino implied via document/policy context).
- **Scoring / risk-rating models** — scorecards, stress-testing, in-house or vendor models; policy parameters for auto-approve/decline/manual-review routing (nCino, Baker Hill, Moody's).
- **Task routing / approval workflows** — automated task routing, review steps, notifications (Baker Hill explicit; nCino policy-driven; Moody's "seamless approval workflows").
- **Tickler / exception tracking** — tracked conditions and outstanding items through closing (Baker Hill "tickler/exception items"; Moody's loan conditions; LaserPro file requests/review workflow).
- **Document management and generation** — repository, generation of closing documents from data, e-signature (Moody's, LaserPro, Baker Hill; nCino repository).
- **Covenant setup at underwriting** — covenants created at spreading/underwriting with due-date notifications (Baker Hill "create covenants while spreading"; nCino covenant notifications; Moody's conditions) — the setup act belongs to origination; ongoing monitoring sits adjacent.
- **Relationship / deal view across products** — one view of the borrower relationship spanning credit and non-credit products; core-system import (nCino Deal Management; Baker Hill CRM "import core data").
- **Digital borrower intake** — application forms, secure document exchange with the borrower (Moody's borrower engagement; Baker Hill client portal; LaserPro Exchange).
- **Industry benchmarking** — borrower performance vs peer data (Baker Hill/RMA in the US market).
- **Integration spine** — core-banking/booking handoff, bureau/e-signature/identity/document-capture connectors, upstream-LOS→document-engine connectors (Moody's "core banking integration"; LaserPro Connect; Baker Hill integration wall).
- **Audit trails and compliance reporting** — document repositories with audit trails; reports for regulators/auditors (nCino, Moody's framing).
- **Role separation** — lending, credit, operations (and risk/executive) as distinct operating roles (Baker Hill role taxonomy; nCino front/middle/back-office framing).

### L2 — Variant / Optional Structure

Depends on segment, geography, product family, era:

- **Small-business scored lending** — score-driven, high-volume small-business/SMB variants alongside judgmental commercial credit (Baker Hill "Scored, Judgmental, & SBA"; Moody's Small Business edition).
- **Government-guaranteed programs** — SBA lending support (US-regional; Baker Hill).
- **Specialty asset classes** — CRE, agriculture editions with domain-specific analysis (Moody's packaged asset classes; CRE specialty noted in the management pass for Loan IQ).
- **Syndicated/participation origination** — deal structuring for shared lending (deep books live in Loan IQ-class platforms; origination-side structuring is the lighter form).
- **Borrower self-service depth** — from document exchange to full digital application journeys (Moody's borrower engagement; Baker Hill digital experiences).
- **Pricing / profitability analysis** — deal profitability targeting (Moody's; single-product within sample).
- **Portfolio monitoring adjacency** — "from origination to monitoring" suites; monitoring is a separate solution layer (Moody's split; nCino CPM; Baker Hill portfolio monitoring).
- **CRM depth** — the platform pole embeds relationship management (nCino's CRM-platform heritage).
- **AI assistance** — automated spreading, GenAI credit memos, assistants (current-era layer across the sample).
- **Deployment posture** — cloud SaaS vs vendor-hosted vs on-premise heritage; pre-configured editions for faster go-live (UN/FY Accelerate).
- **Regional regime machinery** — US compliance artifacts (Section 1071, RMA data, 50-state warranty context) as regional realizations; nothing in L0 requires a specific jurisdiction.

### L3 — Vendor-specific (research notes only)

- nCino: CLOS branding on a CRM-platform heritage; Deal Management module; sub-loans / information cloning / bulk editing; Automated Spreading as a separate solution; agentic-AI marketing layer ("Digital Partners", "Banking Advisor", "Continuous Credit Monitoring"); market metrics ($3.3T/12 months, 2,700+ customers).
- Baker Hill: UN/FY platform name; My Hub workspace; "Ask BKR" AI assistant; UN/FY Accelerate pre-configured edition; NextGen heritage branding; 20K+ bankers / "$200B loans decisioned" claims; case-study metrics (TowneBank, IncredibleBank, Rally CU).
- Moody's: GenAI Automated Credit Memo; "award-winning models" and model lifecycle management; asset-class suite packaging (CRE/Ag/Small Business); "world's largest datasets of financial and non-financial firms" claim; Chartis recognition badges.
- Finastra: LaserPro brand family (Exchange / Analyze / Conductor / Connect); 50-state compliance warranty "up to $5 million"; "40% of U.S. community banks and credit unions" claim; Section 1071 alignment; Originate Business Loans and Deposits as the sibling product; 70+ core-system integrations.

---

## Vendor-specific Findings

1. **The origination stack splits into separable product families**: a document-generation engine can exist as a standalone product consuming data "from select LOS partners" (LaserPro Connect) — evidence that pipeline and closing documentation are separable layers, commonly assembled.
2. **One vendor's own packaging splits origination from monitoring** (Moody's: Loan Origination vs Monitoring as separate solutions) — direct evidence for the origination/monitoring seam, echoing the management pass's origination/management seam.
3. **A relationship platform can be the substrate**: nCino's deal object spans credit and non-credit products of one relationship (loan + treasury), making origination one workflow on a relationship platform — the pole where the pipeline object widens beyond the single credit request.
4. **Spreading is the signature capability**: every sampled family documents it in some form (even the documentation-specialist vendor ships a spreading module and calls spreading "the traditionally manual process critical to lending decisions").
5. **Decisioning depth varies**: from policy-rule parameters (auto-approve/decline/manual review) to scorecards/stress tests; no sampled product documents the decisioning layer as a separate rules-engine product — decisioning lives inside the pipeline here.

---

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Commercial Loan Management (processed) | funding seam: origination's pipeline ends at booking/disbursement (Baker Hill FAQ "application, approval, and disbursement"; Moody's final stage = core banking integration); management owns the funded book (servicing ledger). Funded-position test applied: none of the four origination-led products documents payment application/accrual/a servicing ledger | strip the pipeline/approval/analysis machinery, keep the servicing ledger → loan management; strip the servicing loop, keep the pipeline → origination |
| Credit/portfolio monitoring (Credit Risk platforms) | lifecycle seam: pre-funding pipeline vs observational layer over the funded book. Moody's splits them as separate solutions; covenant machinery straddles the seam — setup-at-underwriting (origination) vs ongoing management (monitoring) | remove the request pipeline, keep covenant management/early-risk detection over the book → monitoring |
| Loan Origination System (§08 generic leaf, unprocessed) | sector seam inside one origination family. Adopted working distinction: commercial = business borrower + financial-statement credit assessment + policy/committee approval machinery; consumer = individual borrower + bureau-scored high-volume decisioning. When that leaf is processed, apply the population test (narrowing the sector must not change the core model) and consider variant/alias treatment | narrow the borrower population and drop financial-statement analysis machinery → generic/consumer origination |
| Consumer Lending Platform (§08, unprocessed) | same funding-family seam at the consumer pole; joint review recommended with the generic LOS leaf | — |
| Mortgage Origination Platform (§08, unprocessed) | collateral-regime seam: residential amortizing machinery (escrow, disclosures, investor/GSE workflows) vs commercial facility machinery. Commercial CRE lending is a variant of commercial origination (property income analysis), not a separate Type | replace facility/financial-statement machinery with amortizing residential-collateral machinery → mortgage origination |
| Credit Decisioning Platform (§08, unprocessed) | layer seam: a decision engine (rules/models as a service) vs the full pipeline. Decisioning is a capability inside origination; a standalone decisioning product has no pipeline, memos, documents, or closing | strip everything but the decision rules/models → decisioning platform |
| Commercial Banking Platform (processed) | operator/surface seam discharged: the banking platform is the client-facing relationship channel (surfacing held credit); origination is lender-staff pipeline work on prospective credit. Discharges the platform pass's flag | move the operator to the client organization and drop the pipeline → client channel |
| CRM | object seam: CRM manages relationships/opportunities generically; origination carries credit-policy approval machinery, financial-statement analysis, and closing execution that CRM lacks. The platform pole (nCino) shows CRM-heritage substrate, not identity | drop credit policy, assessment, and closing machinery → CRM |
| Underwriting Workbench (§15 insurance leaf) | sector seam: same word, different domain (insurance risk selection vs credit approval). Joint review only if insurance-side pass claims shared structure | swap credit machinery for insurance risk machinery → insurance workbench |
| Deal Management for PE/VC (§08) | managed-object seam: investment deals vs credit requests under lending authority | swap credit machinery for ownership/deal economics → PE deal management |

**Joint-review discharges recorded for STATUS.md**:

1. **Discharge (origination side)** of the commercial-loan-management pass flag: the funded-position test was applied — no sampled origination-led product documents a servicing ledger; the funding seam holds; covenant machinery straddles the seam (setup vs monitoring) and is documented as such on both sides.
2. **Discharge (origination side)** of the commercial-banking-platform pass flag: origination is confirmed as lender-staff-side pipeline work; the banking platform only surfaces/serviced held credit client-side.
3. **New flag**: Loan Origination System (generic) + Consumer Lending Platform + this leaf form one origination family split by sector in the directory; recommend joint review / population test when those leaves are processed.

---

## Historical / Market-Sample Check

- **Generational evidence**: commercial credit origination predates software — paper credit memoranda, manually spread financial statements onto standardized analysis sheets, loan committee approval minuted by hand, tickler files for conditions and renewals, document checklists at closing. LaserPro's own language ("the traditionally manual spreading process critical to lending decisions", 40 years of document machinery) and Baker Hill's 40+ year heritage anchor the pre-cloud era. A spreadsheet-era lender (Excel spreading + email approvals + Word memos) also satisfies the conceptual core; the software digitizes, enforces, and records the loop. L0 contains no cloud, AI, portals, or e-signature. Historical check passes.
- **Regional check**: the sampled market is US-weighted (SBA, RMA data, Section 1071, 50-state warranty, community banks/CUs). None of these enter L0. International relationship banking runs the same conceptual loop (credit request → analysis → credit approval → documentation → drawdown); regional machinery is L2.
- **Scale check**: a community bank approving a $250K revolver via a two-person credit chain and a large corporate bank running committee-governed complex facilities both satisfy the core; complexity is a variant axis (echoing the management pass's bilateral↔syndicated edition ladder).
- **Anti-overfitting check**: spreading automation, GenAI memos, digital intake, and scoring models are dominant today but are implementations of L0's assessment node, not definitional — a lender whose analysts hand-spread statements still runs the same Type.

---

## Uncertainties

- **No Tier-1 operational documentation reachable** (help centers/user guides); all claims rest on product/marketing pages. Precise stage names, approval-threshold amounts, document templates, and tickler-state names are NOT asserted.
- **Collateral machinery** — expected industry practice in commercial origination (recording collateral/guarantees at underwriting) — was not surfaced on any fetched page of this sample; deliberately not asserted as common. Uncertainty recorded; revisit if a Tier-1 source becomes reachable.
- **Abrigo unreachable** (502 ×3) — a major risk-led vendor is unrepresented; the risk-analytics pole is covered instead by Moody's. No claim depends on Abrigo.
- **Pricing/profitability depth** unknown beyond Moody's "Target for profitability"; likely common in the category but evidenced for only one product — kept at single-product strength.
- **Borrower-portal depth** varies; whether full self-service application journeys are now majority behavior is unverified (three of four families document some intake surface, depth unstated).
- **The generic-vs-commercial split** (LOS leaf) is a taxonomy judgment recorded for joint review, not settled here.

---

## Final Synthesis

A Commercial Loan Origination application is the lending institution's staff-side pipeline for business credit: it carries a credit request from intake through assessment, decision, and closing to a booked loan. Its defining core is small — the business borrower and related parties; the credit request as a staged, managed pipeline object; credit assessment built on the borrower's financial information (characteristically spread financial statements and cash-flow analysis); the approval decision produced under the institution's credit policy through its approval machinery; and execution to funding — terms assembled, documents produced and executed, conditions tracked — ending with a booking handoff to the servicing system (or a recorded decline). Around this core, mature products add the machinery commercial lending is actually operated with: automated spreading and global cash-flow analysis, credit memos fed from analysis data, scoring/scorecard models with policy parameters that auto-approve, decline, or route for review, task routing and tickler/exception tracking through closing, document generation and e-signature, covenant setup at underwriting, relationship views spanning the borrower's credit and non-credit products, peer benchmarking, audit trails, and an integration spine reaching core banking, bureaus, e-signature, and document engines. The market realizes the Type along a segment axis (mid-market commercial LOS ↔ relationship-platform suites ↔ analytics-led suites ↔ documentation specialists), a complexity axis (small-business scored/SMB lending ↔ large judgmental corporate credit), and a geography axis (US regime machinery as one regional realization). The boundary that matters most is funding: the origination pipeline ends where the servicing ledger begins — the same seam the management pass confirmed from the other side, and the seam the monitoring layer observes after booking. The Type predates all modern artifacts; what the software changed is enforcement and memory, not the loop.
