# Research Notes — Payer Claims Processing

Research date: 2026-09-08
Slug: payer-claims-processing
Leaf: Payer Claims Processing (§22 Healthcare & Life Sciences)

## Research Goal

Understand, from real products, what payer claims processing is as an Application Type: what the claims-operations machinery of a health plan (payer) actually consists of — intake, validation/editing, adjudication, payment/remittance, adjustment — what objects and statuses organize it, who operates it, how it relates to the surrounding payer systems (health plan administration, utilization management, payment integrity), and where its boundaries lie. Special duty carried into this pass: discharge the pre-hung boundary flag from the health-plan-administration-system pass (system of record vs claims-operations machinery; candidate keep-both, joint review recommended).

Standing instruction from the health-plan-administration-system pass (STATUS.md Boundary Issues): health plan administration = the payer's system of record (who is covered, under what benefit rules, what the plan has owed and paid — member/eligibility/benefit/premium/obligation record); payer claims processing = the claims-operations machinery (intake → edit → adjudicate → pay → adjust), whether embedded or standalone. This pass tests and ratifies that seam from the machinery side.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: payer claims processing is the payer-side machinery that takes a request for payment for health care services (a claim) and drives it to a recorded determination and settlement, under configurable benefit and payment rules, with adjustment/appeal loops afterwards.
- Expected core: claim as unit of record + rule-driven adjudication + settlement output + adjustment loop.
- Likely confusions: Health Plan Administration System (§22 sibling — the system of record that bundles this machinery in full-core postures), Provider Claims Management / Healthcare Revenue Cycle Management / Medical Coding Platform (provider side of the same claim), Prior Authorization Platform / Utilization Management (authorization status as adjudication input), Insurance Claims Management / Claims Adjuster Platform (§08 — property & casualty claims), Payment-integrity vendors (Availity/Zelis-class), EDI Platform / clearinghouse (transport), Public Benefits Management (§24 — state-run MMIS as government-operated variant).

## Research Questions

1. What is the unit of record? What does a claim carry (member, provider, coded service lines, charges) and how does it persist?
2. What are the stages of the claims-operations lifecycle as vendors actually document them (intake → edit → adjudicate → pay → adjust)?
3. What rule layers does adjudication apply (validity/edits, eligibility, benefit coverage, authorization status, pricing, coordination of benefits) and how are automated vs human decisions organized?
4. What outputs does the machinery produce (payment, remittance/explanation, denial with reasons) and in what standardized forms?
5. How do adjustment, void, reprocessing, and appeals work after a claim is finalized?
6. What statuses and shared vocabularies organize claim state (claim status codes, adjustment reason codes)?
7. How does the machinery relate to the plan's system of record — bundled in a core administration system, standalone engine, or modular suite riding an external core?
8. What machinery is regime-shaped (encounter data, government program reconciliation, audit readiness) and is it definitional?
9. Who operates the machinery day to day, and through which interfaces?
10. Which surrounding functions (pre-adjudication edits, payment integrity, pricing services, connectivity/clearinghouse) are separable market functions rather than parts of the core?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer/market poles. The two dominant legacy claims engines (TriZetto Facets/QNXT, HealthEdge HealthRules Payer) and the BPM pole (Pega) were not reachable (see Sources); no product-specific claims are made from them.

| Product | Vendor | Philosophy / segment | Evidence reached |
|---|---|---|---|
| HealthOS CAPS (+ HealthOS Plan, Sentinel) | HealthAxis | AI-native bundled CAPS: claims adjudication, eligibility, provider management on one core (AxisCore engine); standalone-deployable workspace; Medicare/Medicaid/commercial/TPA poles | CAPS page, Plan page (Tier 2 product pages), evidence layer A |
| Intelligent Gateway + Payment Accuracy | Availity | Connectivity/network pole: national claim-transaction backbone; pre-adjudication claim editing at the gateway, before claims enter the plan's processing environment | Homepage, Payment Accuracy page (Tier 2), layer A |
| Payment Integrity suite (Claims Editing, Expert Claims Review) | Zelis | Payer-side claims cost-management services pole: claims editing, bill review, DRG validation, pricing, payments on behalf of payers and TPAs | Homepage, Payment Integrity page (Tier 2), layer A |
| X12 transaction sets & code lists | X12 (standards body) | Official standard machinery for the claim exchange: 837 claim submission, 835 payment/advice, 276/277 status, 278 review, 269 payer-to-payer coordination; official claim-status and claim-adjustment code lists | Transaction Sets page (Tier 1 for the standards), layer A |
| (context) MarketProminence modular suites, Softheon, Medecision, DXC "CAS" | MHK, Softheon, Medecision, DXC | Modular-suite posture and category anchors from the health-plan-administration-system pass (2026-09-08): market-side suites naming no adjudication module; "Core Administration System (CAS)" as the payer category name; legacy cores contain claims machinery | Prior pass research notes, layer A (recorded there) |

Unreachable (attempts recorded; no claims made from them):

- HealthEdge (HealthRules Payor) — healthedge.com 403 (this pass; also 403 ×2 in the prior pass) — leading cloud-native claims engine; market anchor only
- Cognizant TriZetto (Facets, QNXT) — cognizant.com 404 (this pass; also 404 ×2 prior pass) — dominant legacy CAPS/claims engines; market anchor only
- Pega (claims processing / health care foundation) — pega.com 403, docs.pega.com 403 — BPM-based claims-processing pole; anchor only
- Optum/Change Healthcare payment management — optum.com 406
- Epic ASA, Conduent, Gainwell — unreachable in the prior pass (recorded there); not retried

## Sources

Fetched 2026-09-08:

- HealthAxis — HealthOS CAPS page: https://healthaxis.com/healthos/caps
- HealthAxis — HealthOS Plan page: https://healthaxis.com/healthos/plan
- Availity — homepage: https://www.availity.com
- Availity — Payment Accuracy: https://www.availity.com/payment-accuracy/
- Zelis — homepage: https://www.zelis.com
- Zelis — Payment Integrity: https://www.zelis.com/solutions/payment-integrity/
- X12 — Transaction Sets: https://x12.org/products/transaction-sets (official definitions of 837, 835, 276/277, 278, 269, 270/271, 834, 274; official external code lists incl. Claim Adjustment Group Codes, Claim Adjustment Reason Codes, Claim Status Category/Status Codes, Remittance Advice Remark Codes)

Context sources (already-processed sibling/neighbor leaves, for boundary consistency):

- research/health-plan-administration-system.md (the pre-hung seam; MHK/Softheon/Medecision/DXC observations; HealthAxis AxisCore four-pillar quote)
- applications/payer-care-management.md (clinical-program layer boundary)
- applications/insurance-claims-management.md, applications/claims-adjuster-platform.md (P&C family seams, from the insurance-family passes)

## Product Observations

### HealthAxis — HealthOS CAPS / HealthOS Plan (evidence layer: A)

Category self-identification: "HealthOS CAPS is the core administrative processing system at the center of HealthOS: the single workspace where claims adjudication, eligibility, provider management, and network operations run on one shared data core." Built on the AxisCore engine ("not just a database... the orchestration layer underneath claims adjudication, enrollment, provider management, and financial coordination, running as a single, immutable source of truth"). Standalone deployable: "Can I deploy CAPS on its own? Yes."

Claims machinery observed on the CAPS page:

- Five-step "how work moves" narrative: **Intake** ("A claim, authorization, or eligibility request lands in CAPS from a provider, a member, or a batch feed") → **score** ("AI PASS checks it against eligibility, benefits, and policy and clinical edits before anyone has to") → **auto-clear or route** ("Clean, criteria-matched work clears itself. Anything ambiguous gets routed, not buried") → **reviewer action** ("A reviewer sees AI PASS's reasoning already attached and makes the call") → **"Paid & Logged"** ("The outcome updates the member, provider, and plan record everywhere at once, with a full trail behind it").
- Live-console mockup vocabulary: claims MTD count, clean rate, in-review count; per-claim rows "Auto-adjudicated / Paid", "Coordination of benefits / Review", "Duplicate billing detected / Hold".
- EDI badges: "EDI 837 · 835 · 270 · 271" (both CAPS and Plan pages).
- Modules: Member Administration (incl. Member 360 with claims history, Complaints & Grievances), Clinical, Provider Administration, Network & Contracts, Plan Operations, System Administration. RBAC + "complete audit log across every module."
- HealthOS Sentinel workspace (payment integrity): "FWA detection & claim review" — payment-integrity machinery shipped as a separate workspace of the same suite, reading the same record.
- HealthOS Plan page (government-program pole): "It reads from the same claims and encounter data as HealthOS CAPS"; risk adjustment/HCC gaps "surface directly from claims and encounter data"; MARx reconciliation of "enrollment, disenrollment, and payment transactions"; encounter-to-Star-Ratings flow "A member visit generates a claim or encounter, captured on the same core CAPS uses."
- Vendor claims (recorded as claims, not asserted): 70%+ faster cycle time, 50% fewer manual touches, "45% faster claim cycle / 40–70% faster claims" (Plan page).

### Availity — Intelligent Gateway + Payment Accuracy (evidence layer: A)

Positioning: national healthcare network/clearinghouse backbone ("more than half of U.S. healthcare transactions run" through it — vendor claim); dual-sided connectivity between payers and providers.

Claim-lifecycle evidence (the pass's most valuable external structure): the Payment Accuracy page documents the claim lifecycle as **Claim Submission → Intelligent Gateway and Payment Accuracy Validation → Pre-Adjudication → Adjudication → Post-Payment Review**.

- "Availity delivers claim error prevention through its Intelligent Gateway — evaluating claims at submission **before they enter a health plan's processing environment**."
- Payment accuracy defined: "identifying and resolving claim errors after submission but before adjudication... validates claims pre-adjudication to prevent incorrect payments." Versus payment integrity: "detecting and correcting errors after adjudication, often through post-payment review, audits, or recoveries. Payment accuracy is preventive, payment integrity is corrective."
- Edit packages: Claim Scrubbing ("HCPCS, CPT® codes, National Drug Code (NDC), and duplicate claims"); Clinical & Analytics ("clinical code errors, modifier usage, diagnosis and related services, Fraud Waste & Abuse, Medicare NCD/LCD, and Medicaid state-specific codes"); Payer Guidelines ("claims align with each payer's unique rules, using payer-supplied policies, rosters, and reimbursement guidelines").
- Correction loop: "When an issue is identified, a clear response is returned through the provider's existing EDI workflow... The provider can correct the issue and resubmit the claim."
- Downstream consequences named: "denials, adjustments, or appeals"; "eliminates time pressure that can force health plan claims teams to prioritize speed over accuracy" ("before the processing clock starts" — an operational clock is implied, not asserted).
- Other payer-side solutions: Multi-Payer Portal ("automating core workflows" for provider collaboration), Clearinghouse & Trading Partner Network ("across eligibility, claims, and payments"), CMS-0053-F claims-attachments suite.
- Vendor claims: "95% of payers connected to 3M+ providers' EDI workflows"; case-study figures (30% denial reduction etc.) excluded from canonical claims.

### Zelis — Payment Integrity suite (evidence layer: A)

Positioning: payer-side cost containment: "More than 770 payers rely on Zelis to price, pay, and empower a better healthcare financial experience" (vendor claim); health plans, P&C payers, TPAs, dental payers as audiences.

- "Ensure the accuracy and integrity of claims – **before you pay**. Pre-pay payment integrity solutions..."
- **Claims Editing**: "Improve payment accuracy with a holistic approach to claims editing, using a combination of a growing library of edits, historical data, industry knowledge, and the expertise of a team of certified professional coders, registered nurses, and medical doctors"; "Pay claims on time when they are right and deny when there are potential errors"; "Reduce claim appeals with adherence to coding standards"; "Customize claim editing process to meet in-house guidelines."
- **Expert Claims Review**: "itemized bill review, clinical chart review, and DRG validation in a pre- or post-pay environment"; "comprehensive pre-pay reviews to pay the claim right the first time... also offering post-pay reviews for those more complicated or restrictive reviews."
- Part of "Zelis Intelligent Pricing Platform — Optimize every claim with integrated payment integrity and claims pricing capabilities" (in-network pricing automation, reference-based pricing, out-of-network claims negotiation).
- Payments + Communications: "Deliver faster payments and better communications" — provider payments, claims communications ("help members... understand how their benefits were applied and paid").

### X12 — official standard machinery (evidence layer: A, standards body)

- **837 Health Care Claim**: "submit health care claim billing information, encounter information, or both, from providers of health care services to payers, either directly or via intermediary billers and claims clearinghouses. It can also be used to transmit health care claims and billing payment information between payers with different payment responsibilities where coordination of benefits is required..."
- **835 Health Care Claim Payment/Advice**: "make a payment, send an Explanation of Benefits (EOB) remittance advice, or make a payment and send an EOB remittance advice... from a health insurer to a health care provider either directly or via a financial institution."
- **276 Health Care Claim Status Request**: a provider (or recipient/agent) "can request the status of a health care claim or encounter from a health care payer... The request may occur at the summary or service line detail level."
- **277 Health Care Information Status Notification**: a payer "can notify a provider... regarding the status of a health care claim or encounter or to request additional information from the provider regarding a health care claim or encounter..." — "solicited or unsolicited"; "will not be used for account payment posting."
- **278 Health Care Services Review Information**: transmits review information "for the purpose of request for review, certification, notification or reporting the outcome of a health care services review" (the authorization/review exchange; users include "payors... utilization management").
- **269 Health Care Benefit Coordination Verification**: transmits "claim identification, previous adjudication details, and adjudication verification from one Health Care Payer to another" (payer-to-payer coordination-of-benefits machinery).
- **270/271** eligibility/benefit inquiry and response; **834** benefit enrollment (sponsor→payer); **274** provider information "routinely exchanged for the purpose of maintaining provider data bases for claim adjudication."
- Official external code lists: Claim Adjustment Group Codes, Claim Adjustment Reason Codes, Claim Status Category Codes, Claim Status Codes, Remittance Advice Remark Codes — the standardized vocabularies of claim status, adjustment, and remittance explanation.
- X12 context: standards maintained under the X12N (Insurance) subcommittee; health-care transaction flow diagrams; Clearinghouse and Medicaid caucuses exist as industry groups.

### Context from the health-plan-administration-system pass (2026-09-08)

- MHK MarketProminence: modular market-side suites (enrollment, member maintenance, premium billing) with **no named adjudication module** — the modular posture riding separate claims cores; appeals & grievances as a full suite (CareProminence CAG).
- Softheon: individual-market operations pole; claims adjudication not evidenced on fetched pages.
- Medecision: care/UM/quality platform with no claims adjudication — the clinical layer boundary anchor.
- DXC: "Core Administration System (CAS)" as the payer-side market category; legacy cores as modernization targets ("claims adjudication ships inside" them per market posture).
- HealthAxis AxisCore (prior pass): the four-pillar CAPS quote bundling "claims adjudication, enrollment, provider management, and financial coordination."

## Cross-product Comparison

| Dimension | HealthOS CAPS (HealthAxis) | Availity (gateway/PA) | Zelis (PI suite) | X12 (standards) | Modular suites (prior pass: MHK) |
|---|---|---|---|---|---|
| Claim as unit of record | yes — claims queue, per-claim rows, claims history in Member 360 | yes — claims evaluated per submission at the gateway | yes — claims edited/reviewed per claim | yes — 837 defines the claim record exchanged | implied — shares data with separate claims cores |
| Intake channels | provider, member, batch feed | EDI workflows via network; provider portal ecosystem | EDI connection (testimonial) | 837 direct or via clearinghouses | data sharing with internal systems/subcontractors |
| Pre-adjudication editing | "policy and clinical edits" checked at score step | the product's center (claim scrubbing, clinical edits, payer guidelines) | the product's center (claims editing, bill review) | code lists define vocabularies | not named |
| Eligibility at adjudication | explicit ("checks it against eligibility, benefits...") | upstream (270/271 flows on the network) | not on fetched pages | 270/271; 837 references | n/a |
| Benefit/coverage rules | explicit ("benefits") | payer-supplied policies/reimbursement guidelines | plan policies, regulations, contractual provisions | — | n/a |
| Authorization status input | authorization listed as intake object; Plan page prior auth | IntelligentUM separate solution | not evidenced | 278 review exchange | UM separate suite (CareProminence) |
| Pricing | not detailed on fetched pages | not evidenced | pricing platform (in-network, reference-based, OON negotiation) | — | n/a |
| Coordination of benefits | named (COB review queue; secondary coverage detection) | not evidenced on fetched pages | not evidenced | 837 payer-to-payer; 269 verification | n/a |
| Automated vs human decisioning | auto-adjudication + reviewer routing with reasoning attached | automated validation at gateway; providers correct/resubmit | automated edits + expert human review (coders/RNs/MDs) | — | n/a |
| Determination outcomes | Paid / Review / Hold observed; paid-and-logged | clean vs corrected-and-resubmitted | "pay... when they are right and deny when there are potential errors" | adjudication outcome carried in 835/remittance | n/a |
| Settlement output | "Paid & Logged" (payment + record update + trail) | payments flows on network | provider payments + claims communications | 835 payment + EOB remittance | n/a |
| Status machinery | claims queue with statuses; in-review counts | lifecycle stage names; response through EDI workflow | — | 276/277 status request/notification; status code lists | n/a |
| Adjustment/reprocessing | full trail behind every action | adjustments named as downstream events | post-pay reviews; appeals reduction goal | Claim Adjustment Reason/Group Codes; provider adjustment reason codes | n/a |
| Appeals & grievances | Complaints & Grievances module | appeals named downstream | "reduce claim appeals" | — | full CAG suite (prior pass) |
| Payment integrity / FWA | Sentinel workspace (separate) | post-payment review stage; FWA in clinical edits package | the product's center | — | n/a |
| Government machinery | Plan workspace: encounter data, MARx reconciliation, CMS audit readiness | Medicare NCD/LCD, Medicaid state-specific edits | not evidenced | 837 carries encounter information | CMS machinery (prior pass) |
| Packaging pole | bundled CAPS, standalone-deployable | network platform outside the plan's system | services/suite around the payer's engine | — | modular suites around separate claims cores |

Convergence across the reachable sample:

- The claim is a persistent identified record that carries member, provider, and coded service lines and moves through visible statuses (HealthAxis queue; Availity lifecycle; X12 status machinery).
- The lifecycle intake → validate/edit → adjudicate → pay → adjust is independently visible in every source, in different vocabularies (HealthAxis five steps; Availity five stages; Zelis pre-pay/post-pay editing; X12's transaction set sequence and adjustment code lists).
- Adjudication applies a layered rule stack: validity/edits, eligibility, benefit coverage, authorization status, pricing, coordination of benefits (HealthAxis explicit; Availity/Zelis for the edit layers; X12 for eligibility/COB/auth exchanges).
- Both fully-automated clearing and human exception review are standard realizations; the split is a design point, not a Type boundary (HealthAxis AI-routing; Zelis expert reviewers; Availity preventive gate).
- Settlement produces payment plus an explanation to the claimant (835/EOB officially; claims communications at Zelis; paid-and-logged at HealthAxis).
- Status inquiry and adjustment carry standardized vocabularies (X12 status/adjustment reason codes) — the machinery's shared language.
- Editing, pricing, payment integrity, and connectivity are realized both inside machinery and as separable market products — separable functions, not definitional parts.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Claim as the unit of record
  (persistent identified request for payment for health care services —
   claimant/provider + member/coverage reference + coded service lines
   with charges; status-carrying through its life)
  └── Rule-driven adjudication to a recorded determination
      (the claim evaluated against configurable rule layers — submission
       validity/edits, eligibility, benefit coverage, authorization status,
       pricing, coordination of benefits — to a recorded outcome:
       pay in whole or part, deny, or pend; automated clearing and human
       exception review both standard realizations)
      └── Settlement output & the adjustment loop
          (a finalized determination settles — payment released or denial
           explained — with an explanation of what was paid/denied and why
           returned to the claimant; finalized claims can be re-entered for
           adjustment/void/reprocessing and appealed, adjustments recorded)
```

Three jointly-held invariants:

1. **Claim as the unit of record** — a persistent, individually addressable request for payment for health care services, submitted by a provider (or other claimant) against a member's coverage, carrying the member reference, the servicing provider, and coded service lines (procedures, diagnoses, dates, charges), and moving through explicit statuses. The machinery's memory lives here: without a held claim there is nothing to adjudicate, adjust, or report on. Remove → a generic payment/billing tool or a rules test harness.
2. **Rule-driven adjudication to a recorded determination** — the claim is evaluated against the payer's configurable rule layers, and the evaluation produces a recorded determination (pay in whole/part, deny, or pend for information or another party's action). Whether the evaluation is fully automated, fully human, or a hybrid is a realization choice; the rules-against-claim evaluation with a recorded outcome is the invariant. Remove → claim data-entry shell or inbox with no determination capability.
3. **Settlement output & the adjustment loop** — a finalized determination settles into financial output: payment released (or denial communicated), with an explanation of what was paid or denied and why returned to the claimant; and finalized claims can re-enter the machinery through adjustment, void, reprocessing, and appeal, with the adjustments recorded against the claim's history. Remove → a decision engine that never moves money, or a payment factory with no claim memory (no adjustment, no appeal, no audit).

Jointly-held is load-bearing:

- 1 without 2+3 → a claim registry/document store.
- 2 without 1+3 → a rules engine / test harness.
- 3 without 1+2 → a disbursement factory.
- 1+2 without 3 → adjudication sandbox; determinations never settle and never correct.
- 2+3 without 1 → anonymous transaction processing; nothing to track, adjust, or appeal against.

Historical check (workflow §24-style reasoning): a paper-era claims department — claim forms arriving by mail, clerical examination against the benefit certificate, manual pricing, a check plus an explanation-of-benefits letter, and re-examination on appeal — satisfies all three invariants. Early mainframe adjudication engines satisfy them without EDI, AI, cloud, or portals. A state-run Medicaid claims engine and a non-US statutory insurer's bill-review operation satisfy an abstracted reading (claim in, benefit-rule evaluation, payment out, adjustment on dispute), though the US-shaped sample limits confidence (see Uncertainties). The definition names no EDI transaction, no AI, no cloud, no specific pricing method, and no specific program.

### L1 — Common Mature Structure (standard capabilities)

- Multi-channel intake: standard electronic claim transactions (837-class submission, direct or via clearinghouse), provider/member portal entry, batch feeds, paper/data entry
- Front-end/pre-adjudication editing ("claim scrubbing"): coding checks, duplicate detection, payer-specific policy edits — in-system or via separable edit services
- Real-time eligibility/coverage verification at intake (270/271-class exchanges)
- Claims work queues with statuses, exception routing, and reviewer workbenches (clean-claim rate, aging, throughput as the operational vocabulary)
- Coordination of benefits machinery (secondary-coverage detection, payer-to-payer adjudication detail exchange — 269-class)
- Payment generation and remittance/explanation output (835-class payment + EOB remittance advice)
- Provider-facing claim status inquiry and notification (276/277-class, solicited or unsolicited)
- Adjustment/void/reprocessing machinery with standardized adjustment reason vocabularies
- Appeals & grievances intake and tracking (regulatory rigor deepest in government programs)
- Prior-authorization linkage: authorization status consumed as an adjudication input (278-class review exchange)
- Payment-integrity hooks: pre-payment expert review (itemized bill review, DRG validation) and post-payment review/audit/recovery — commonly separable products
- Operations reporting & dashboards (cycle time, first-pass/clean-claim rate, denial patterns)
- Roles, permissions, audit trails; configuration tooling for edits, pricing, and benefit logic
- Encounter-data handling and government-program reporting where the regime requires it

### L2 — Variant / Optional Structure

- Packaging poles: bundled inside a core administrative processing system (CAPS/CAS), a standalone/connected claims engine, or a modular suite riding an external claims core — packaging, not definition
- Government-program machinery depth: encounter data submission, program reconciliation (MARx-class), audit readiness, program-specific edit libraries (Medicare NCD/LCD-class, state Medicaid codes)
- Line shaping: dental, vision, pharmacy (PBM), behavioral; provider-sponsored plans (payvider)
- TPA/self-funded posture: the same machinery operated for employer-funded plans (no member premium; employer/stop-loss semantics outside the claim machinery)
- Pricing-method variants: contracted fee schedules, reference-based pricing, out-of-network negotiation — separable services in the market
- Delegated/BPO operation: vendor staff run the machinery on the payer's behalf
- Automation posture: straight-through-processing targets, AI scoring/routing, prevention-first gateway editing — modern realizations of the same evaluation leg
- Regional/regime variants beyond the US-shaped sample (low evidence)
- Member-facing explanatory surfaces (explanations of benefits applied)

### L3 — Vendor-specific (research notes only)

- HealthAxis: HealthOS/CAPS/AxisCore/AI PASS naming; six-workspace suite; console mockup values (claims MTD, clean rate percentages, HCC capture figures); 70%+/50% vendor outcome claims; HITRUST/SOC 2 badge wall; "immutable source of truth" phrasing; Sentinel/Plan workspace branding; MARx-by-name reconciliation.
- Availity: Intelligent Gateway branding; Claim Scrubbing / Clinical & Analytics / Payer Guidelines package names; "95% of payers / 3M+ providers / $4T billed claims" network stats; case-study savings figures; CMS-0053-F/0057-F suite branding; Abrasion Index content marketing.
- Zelis: Expert Claims Review®, ZAPP payments platform, Intelligent Pricing Platform℠ branding; 770+ payers claim; Everest/KLAS-class analyst badges; ACS/AmeriBen/BRMS case studies; FDIC-institution payment rail note.
- Unreachable anchors (no claims from them): HealthEdge HealthRules Payer, TriZetto Facets/QNXT, Pega claims processing, Epic ASA, Optum/Change payment management.

## Rejected Findings (not promoted to core)

- "AI/straight-through-processing defines the Type" — rejected: manual paper-era adjudication satisfies the core; automation posture is L2 realization.
- "The five-stage lifecycle naming (submission → validation → pre-adjudication → adjudication → post-payment review) is canonical" — rejected as a specific vendor's stage naming (Availity); canonical states are written conceptually (received → in evaluation → pended → determined → settled → adjusted), exact labels vary.
- "Claim scrubbing/editing is a definitional component" — partially rejected: the evaluation leg is invariant, but the edit library is realized in-system (HealthAxis), at a gateway (Availity), or as an external service (Zelis); keep the layer conceptually, packaging variant.
- "Pricing services (reference-based pricing, out-of-network negotiation) are core" — rejected: separable market services (Zelis pole) feeding the machinery.
- "Payment integrity/FWA detection is core" — rejected: preventive (gateway) and corrective (post-pay) integrity are realized as adjacent products and separate workspaces (Availity, Zelis, HealthOS Sentinel); the core consumes their outputs.
- "Government/CMS machinery (encounter data, MARx-class reconciliation) is definitional" — rejected: regime machinery (L1/L2); paper-era and commercial-only machinery operate without it.
- "Authorization review belongs in this Type" — rejected: the review machinery is utilization management's center; this Type consumes authorization status (X12's own split between 837/835 claim machinery and 278 review machinery corroborates the seam).
- Marketing figures (70%+ cycle time, 30% denial reduction, 95%/3M/770 network stats) — excluded from the final document; vendor claims only.

## Boundary Findings

- **vs Health Plan Administration System (§22, processed — flag discharge)**: the pre-hung seam holds and is ratified from this side. Health plan administration = the payer's system of record (member/coverage/eligibility/benefit rulebook/premium/obligation record — "who is covered, under what rules, what has the plan owed and paid"). Payer claims processing = the claims-operations machinery (intake → edit → adjudicate → pay → adjust). The bundled CAPS reality is acknowledged: in full-core postures the machinery ships inside the system of record (HealthAxis CAPS), while modular suites ride separate claims cores (MHK posture) — so feature lists cannot separate the leaves, and the seam is conceptual: system-of-record center vs operations-machinery center. Joint evidence from this pass: CAPS is independently deployable ("Can I deploy CAPS on its own? Yes"), its five-step narrative is claims-shaped (intake→score→route→review→paid), and the HealthOS suite itself splits enrollment/Plan/Sentinel workspaces away from CAPS. Keep-both ratified; cross-referenced in both documents.
- **vs Provider Claims Management / Healthcare Revenue Cycle Management (§22)**: provider-side claim production/submission and revenue machinery vs payer-side determination and settlement — opposite seats on the same claim transaction. The claim is born on the provider side (837 submitter) and judged on the payer side; no confusion once the seat is named.
- **vs Medical Coding Platform (§22)**: coding production (assigning/validating codes) vs claim evaluation (adjudicating the coded request). Coding feeds adjudication; expert coding review appears in payment-integrity machinery as a separable function.
- **vs Prior Authorization Platform / Utilization Management (§22, unprocessed)**: authorization status is an adjudication input; the review machinery (medical necessity, determinations, appeals of review decisions) is a separate discipline. The X12 corpus itself splits them (278 review vs 837/835 claim machinery). Flag stays for those passes.
- **vs Payment Integrity / FWA (adjacent market, e.g., Availity post-pay, Zelis, HealthOS Sentinel)**: preventive pre-adjudication editing and corrective post-payment review are separable market functions; the claims machinery consumes their outputs (edits applied at intake, reviews gating payment). The core is the determination-and-settlement loop, not the integrity programs.
- **vs EDI Platform / Clearinghouse (§13 adjacent; Availity/Clearinghouse pole)**: transport, routing, and transaction validation vs obligation determination. The gateway validates claims before they enter the plan's processing environment — valuable machinery, but no determination, no settlement, no adjustment of record.
- **vs Insurance Claims Management / Claims Adjuster Platform (§08, processed)**: same adjudication concept family, different object semantics: P&C claims carry loss events, perils, adjuster investigation, coverage against a policy; payer claims carry coded health service lines adjudicated against benefit rulebooks and fee schedules, with provider networks and statutory machinery. Keep-both; the P&C family's adjuster-centered investigation loop has no counterpart here (review is clinical/policy, not loss investigation).
- **vs Public Benefits Management (§24, unprocessed)**: state-run Medicaid MMIS is the government-operated variant of similar claims machinery; this Type remains the payer-side machinery regardless of who funds the plan. Boundary note for that pass.
- **vs Customer Service / Help Desk (§07)**: claim-status inquiry handling is a servicing surface; the center here is the claim record and its adjudication, not the service conversation.

## Uncertainties

- The two dominant legacy claims engines (TriZetto Facets/QNXT, HealthEdge HealthRules Payer) and the BPM pole (Pega) were unreachable (403/404 across both passes) — the main evidence gap. The canonical model rests on the reachable sample (HealthAxis CAPS, Availity, Zelis, X12) plus prior-pass modular-suite context. No product-specific claims are made from unreachable vendors.
- Pricing machinery depth (fee schedules, repricing algorithms) was not detailed on any reachable page; pricing is written conceptually as an adjudication rule layer.
- Exact determination state sets, turnaround-time rules, payment-timeliness and interest rules were not asserted — they are regime- and jurisdiction-specific and were not directly evidenced in the reachable sample.
- The "processing clock" implied by Availity's copy ("before the processing clock starts") suggests regulated timeframes but none were asserted.
- Non-US / statutory-insurer fit is inferred abstraction, not product observation; the sample is US-shaped (consistent with §22's US payer vocabulary).
- Whether MHK's modular posture implies a claims engine inside the MHK platform or strictly external cores could not be confirmed beyond the prior pass's fetched pages.

## Final Synthesis

Payer claims processing is the payer's claims-operations machinery: the system that takes requests for payment for health care services and drives them, under configurable rules, to recorded determinations and settled outcomes. Its world has three jointly-held structures: the claim as the unit of record (persistent, identified, status-carrying: claimant, member, coded service lines, charges); rule-driven adjudication to a recorded determination (validity/edits, eligibility, benefit coverage, authorization status, pricing, coordination of benefits — automated clearing and human exception review both standard); and settlement output with the adjustment loop (payment or explained denial, remittance/explanation to the claimant, and re-entry through adjustment, void, reprocessing, and appeal). Around that core, mature machinery adds multi-channel intake with front-end editing, eligibility verification at intake, work queues with reviewer routing, COB machinery, standardized status and adjustment vocabularies, payment-integrity hooks, operations reporting, and audit trails. The machinery's packaging varies — bundled inside a core administrative processing system, standalone, or modular around external cores — and its regime machinery deepens for government programs. The boundaries that matter: machinery vs system of record (health plan administration), payer seat vs provider seat (provider claims management / revenue cycle), claim evaluation vs code production (medical coding), adjudication input vs review discipline (utilization management / prior authorization), determination loop vs integrity programs (payment integrity), and adjudication vs transport (clearinghouse/EDI).
