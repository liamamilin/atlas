# Research Notes — Construction Claims Management

Research date: **2026-09-10**

## Research Goal

Understand what a Construction Claims Management application actually is from real products: what objects exist inside it, what a "claim" is in this domain, what lifecycle a claim follows, who participates, what rules (especially contractual notice/time-bar rules) gate the workflow, how evidence is assembled, and where the boundary lies against neighboring Types (Change Order Management, Construction Contract Administration, Litigation/eDiscovery, Insurance Claims Management, Daily Log, RFI Management).

## Initial Boundary (pre-research hypothesis)

- Core purpose: manage contractual claims on a construction project — assertions by one contracting party that events entitle it to additional payment and/or time under the contract — from notice through substantiation, response, negotiation, and (if unresolved) formal dispute resolution.
- Users: contractors (especially subcontractors and specialist trades), commercial/contract managers, claims consultants, owners/PMO teams, engineers (under FIDIC/NEC-style contracts).
- Neighbors: Change Order Management (the agreed-change path), Construction Contract Administration (broader host), Construction Document Management (storage), Daily Log (evidence supply), Litigation/eDiscovery (post-escalation legal), Insurance Claims Management (same word, different domain).
- Risks: (a) "claims" polysemy — payment claims/progress claims (payment certification) vs contractual claims (disputes); (b) the Type may be mostly a module inside contract administration suites; (c) a wave of AI-era evidence-timeline tools may be reshaping the category.

## Research Questions

1. What is the object model? What exactly is a "claim" record — what fields/structure does it carry?
2. What lifecycle/status states do claims move through, and what gates progression?
3. How do contractual notice requirements and time-bars appear in the software?
4. How is evidence/substantiation handled — linkage to project records, chronology, delay analysis?
5. Who are the parties and roles (claimant, respondent, engineer/contract administrator, consultants)?
6. How does the register/reporting view work, and what commercial reporting exists?
7. How does contract-family specificity (FIDIC, NEC, bespoke) shape the product?
8. Packaging: standalone product, platform app, contract-administration module, AI service?

## Representative Products

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| C-COM | FIDIC/NEC contract administration platform with a dedicated Claims module; multi-party, contract-clause-driven | Defines the contract-procedure-driven model (time-bars, contractual correspondence, registers) |
| Kahua Construction Claims (SuperSet app) | Platform app on a construction management suite; contractor/consultant/supplier audience | Shows the claims app as a platform extension with claim forms, status reports, document consolidation |
| ClaimMaster.ai | Contractor/specialist-subcontractor-facing event-capture product; cause→effect→entitlement structure with defensibility scoring | Live-project claim-building philosophy; strongest articulation of the claim's internal structure |
| ClaimsBridgeHQ | FIDIC/GCC-focused contract-aware monitoring service; notice deadline tracking + live claims register | Deadline/time-bar-centric philosophy; email-ingestion intake model |
| WhiteHelmet Contract & Claim Management | Owner/PMO-side commercial lifecycle platform (Middle East market) | Owner constituency; claims embedded in contract-to-payment lifecycle |

Market-context observations (not deep-sampled): AI evidence-timeline tools (Eviant, Storia, Astora, VitruAI) that assemble source-linked chronologies from the project record; InEight Contract's "Payment claims" module (a different sense of "claims" — payment certification); Procore has no dedicated claims tool (change orders only), confirming claims as a distinct niche Type rather than a core module of the market-leading PM platform.

## Sources

Successfully fetched 2026-09-10:

1. C-COM — FIDIC Contract Management Software product page — https://www.ccom.cloud/fidic-contract-management-software (Tier 2)
2. C-COM — Features page (Claims, Compensation Events, Early Warnings, Instructions, Variations, Daily Diary, Risk Register, Events) — https://www.ccom.cloud/features (Tier 2)
3. Kahua kStore — "Construction Claims & Dispute" app listing (SuperSet Infrastructure) — https://launch.kahua.com/kStore/Detail/971 (Tier 2)
4. ClaimMaster.ai — product site (Event Record Form, defensibility scoring, cause/effect/entitlement/mitigation structure) — https://claimmaster.ai/ (Tier 2)
5. ClaimsBridgeHQ — product site (contract-aware monitoring, deadline alerts, claims register, payment reconciliation) — https://claimsbridgehq.com/ (Tier 2)
6. WhiteHelmet — Contract and Claim Management product page — https://www.whitehelmet.sa/products/contract-and-claim-management (Tier 2)
7. Storia Technologies — Claims & Dispute Resolution product page — https://storiatechnologies.com/en/products/claims-and-dispute-resolution (Tier 2, market context)
8. Eviant — product site (evidence substrate, notice compliance matrix, contradiction detection) — https://eviant.ai/ (Tier 2, market context)
9. Astora — Claims use case page — https://www.astora.app/en/use-cases/claims (Tier 2, market context)
10. VitruAI — Dispute Evidence Timeline use case — https://vitruai.com/use-cases/dispute-evidence-timeline/ (Tier 2, market context)
11. InEight learn site — "Payment claims" module doc — https://learn.ineight.com/Contract/Content/CONT20.2%207/Payment%20claims.htm (Tier 1, polysemy evidence only)
12. Aurigo — owner-side claims-avoidance guide — https://www.aurigo.com/industry-resources/manage-construction-claims/ (Tier 2, market context)
13. Kahua/MTO case study (claims among managed processes) — https://kahua.com/wp-content/uploads/2026/07/ministry-of-transportation-ontario.pdf (Tier 2, market context)

Source-access limitation: no Tier-1 operational help-center documentation was reachable for any sampled product (these are mostly marketing/product pages; ClaimMaster.ai, ClaimsBridgeHQ, WhiteHelmet, C-COM publish no public user manuals). Claims are therefore described at the structural level; precise field lists, default statuses, and numeric time windows are NOT asserted. FIDIC Sub-Clause 20.1 notice mechanics are referenced by the products themselves (ClaimsBridgeHQ, Astora) and are reported as what the products track, not as independent legal verification.

## Product Observations

### C-COM (FIDIC/NEC contract management platform) — Evidence A

- Claims are one module among contract-administration instruments: Compensation Events (NEC), Early Warnings, Instructions, Variations, Daily Diary, Risk Register, Events, Claims.
- Claims module: "advises both parties of their options from initiation to agreement or determination"; generates and issues contractually compliant correspondence; maintains an accurate, current claims register "for real-time commercial intelligence"; automatically maintained timeline per claim.
- Time-bar monitoring is explicit: timely notifications about necessary actions, actions advised "aligned with contract details."
- The surrounding instruments (early warnings, events, daily diary) exist explicitly to feed dispute resolution and claim evaluation: the daily diary is "a searchable record essential for dispute resolution and claim evaluation."
- Authorization workflows: actions not executed until authorization obtained; audit trail of every transaction and communication; late-performed actions clearly indicated in history.
- Both parties use the system (contractor and employer/engineer side).

### Kahua Construction Claims & Dispute (platform app) — Evidence A

- Positioned for "Contractors, Consultants, and Suppliers"; "one-stop source application for the recording, management, and reporting of construction claims."
- Consolidates "comprehensive reference lists of claim-related project records and documents" for use "when issuing or responding to claims" — evidence consolidation is a first-class feature.
- Covers the full process and "sub-processes (review, response, negotiation, and litigation)."
- Visibility into "potential, current, and closed claims" — a status model spanning prospective to closed.
- Features: claim forms, required fields, claim status reports, status/progress reports; rides on the platform's configuration, documents, and reporting.

### ClaimMaster.ai (contractor-side event capture) — Evidence A

- Core object: Event Record Form (ERF) with a fixed internal structure: Event Type, Status, Cause, Effect, Entitlement (contract clause quoted), Substantiation (BoQ, marked-up drawings), Mitigation, notice issued.
- "Capture cause, effect, and entitlement as the work happens" — claim-building moved from end-of-project reconstruction to live capture; records time-stamped with audit trail.
- Defensibility scoring: assesses where a claim position is "likely to break" (e.g., missing substantiation) before submission; gap detection before disputes.
- Approval/review steps, governance, legal holds for larger organizations; whitelabel deployment.
- Audience: MEP, civils, structural, façade, specialist contractors under payment risk; also main contractors, consultants, developers, owners.
- Explicitly positions as a "defensibility layer" alongside existing programme/cost/document systems.

### ClaimsBridgeHQ (FIDIC/GCC monitoring service) — Evidence A

- Builds a structured model of the contract (main contract, particular conditions, subcontracts, BOQ); every incoming document (notices, instructions, payment certificates, letters — ingested by CC-ing a project email address) is reviewed against the contract.
- Auto-extracts contractual time-bars and notice periods; alerts before deadlines (e.g., FIDIC Sub-Clause 20.1 claim-notice windows); tracks response periods.
- Live claims register auto-maintained from project correspondence: status, deadlines, estimated values.
- Draft response letters with clause references; payment reconciliation (claimed vs certified, traced to variations); audit trail of every document processed.
- Regional contract variants (GCC modifications to FIDIC) — geography-specific configuration.

### WhiteHelmet (owner/PMO-side) — Evidence A

- Claims processing workflow: "Submit, review, and approve claims through a structured workflow. Track claim status, supporting documentation, and approval chains."
- Claims sit inside the commercial contract lifecycle alongside variations, interim payment certificates, retention, and final account; dashboard shows original value, approved variations, claims, certified payments, outstanding amounts.
- Claims and valuations: prepare/submit claims with supporting documentation, track valuation progress.
- PMO/contract-administrator constituency; dispute-reduction framing.

### AI evidence-timeline tools (Eviant, Storia, Astora, VitruAI) — Evidence A (market context)

- Shared shape: ingest the full project record (emails, RFIs, notices, minutes, schedules, exports from Aconex/P6/Unifier); assemble a source-linked event chronology; detect contradictions between documents; notice-compliance matrices (which notices served, when, against which clause); missing-evidence reports; draft claim narratives with every assertion cited to a verbatim source.
- Astora adds contract-deadline extraction and monitoring (e.g., FIDIC notification windows) and precedent bases of prior claims.
- Storia frames dual outcomes: settle on facts during the project, or convert the same record into a claim draft.
- These tools deliberately do not decide fault; they structure evidence for human experts — consistent with the claims-consultant constituency.
- They confirm the pain the Type addresses: claims are formalized long after events; reconstruction from hundreds of documents is the bottleneck; traceability of quantum to source documents is the defensibility requirement.

### InEight Contract "Payment claims" — Evidence A (polysemy only)

- "Payment claims" = certification of a vendor's claimed work ahead of invoicing, tied to the schedule of values and payment forms. This is payment certification, not contractual dispute claims. Recorded to prevent conflating the two senses of "claims" within construction software.

## Cross-product Comparison

| Dimension | C-COM | Kahua Claims app | ClaimMaster.ai | ClaimsBridgeHQ | WhiteHelmet |
|---|---|---|---|---|---|
| Claim as object | claim record in register with timeline | claim form + status model (potential/current/closed) | Event Record Form (cause/effect/entitlement/substantiation/mitigation) | claim entries auto-maintained from correspondence | claim in structured workflow (submit/review/approve) |
| Entitlement framing | contract-procedure options (initiation→agreement or determination) | best-practice guideline | explicit clause citation per event | clause-level obligations triggered by documents | commercial lifecycle context |
| Notice/time-bar machinery | time-bar monitoring, action notifications | — (not stated) | notice issuance as part of event capture | core feature: deadline extraction + alerts | not stated |
| Evidence handling | linked instruments (diary, events, early warnings) + attachments | consolidated reference lists of project records | substantiation links (BoQ, drawings), time-stamped | every document classified and cross-referenced | supporting documentation attached |
| Response/adjudication | contractual correspondence generation, both parties | review/response/negotiation/litigation sub-processes | internal approval/governance | draft response letters | review/approve workflow |
| Register/reporting | claims register, commercial reporting | status/progress reports | defensibility scoring, audit trail | claims log + dashboards | contract financial dashboard incl. claims |
| Contract family | FIDIC + NEC specific | generic best practice | contract-agnostic structure | FIDIC/GCC specific | generic commercial |
| Constituency | both contracting parties | contractors/consultants/suppliers | contractors (esp. specialist subs) | contractor commercial teams (GCC) | owner/PMO |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

A Construction Claims Management application is a system of record for **contractual claims on a construction project**: recorded assertions by one contracting party that defined events entitle it to additional payment and/or extension of time under the contract. Removing any of these and it stops being this Type:

1. **Claim record** — a discrete documented claim object tied to a specific contract and counterparty, carrying an event basis (what happened), an entitlement basis (the contractual right invoked), and a claimed impact (money and/or time).
2. **Substantiation linkage** — the claim is backed by references to project records (correspondence, notices, diaries, schedules, valuations); a claim without an evidence trail is not manageable in this Type.
3. **Governed lifecycle to resolution** — the claim moves through recorded stages (notice/submission → substantiation → response/review → negotiation → agreement or escalation), with actions attributed and auditable.
4. **Claims register** — a portfolio view of all claims with status and value, because claims are managed as a set against the contract, not one-off documents.

### L1 — Common Mature Structure

- Contractual notice and time-bar tracking (deadline extraction, alerts, notice-compliance matrices) — present in C-COM, ClaimsBridgeHQ, Astora, ClaimMaster.ai; central to the FIDIC/NEC world.
- Contractually compliant correspondence generation (notices, responses, determinations).
- Event/diary capture feeding claims (daily records, early warnings, events as precursor objects).
- Response-side handling (the counterparty's review/response path, not just the claimant's).
- Status/progress reporting and commercial dashboards (claimed vs certified, outstanding claims).
- Audit trails and time-stamped records for dispute defense.

### L2 — Variant / Optional Structure

- Delay/programme analysis linkage (critical-path impact from schedule updates) — Storia, VitruAI, specialist practice.
- Contradiction detection and missing-evidence analysis across the document corpus (AI-era tools).
- Defensibility scoring / gap detection (ClaimMaster.ai).
- Payment reconciliation (claimed vs certified amounts traced to variations) (ClaimsBridgeHQ).
- Precedent libraries of prior claims/arguments (Astora).
- Contract-family templates (FIDIC Red/Yellow/Silver, NEC compensation events, GCC particular conditions) (C-COM, ClaimsBridgeHQ).
- Litigation/arbitration sub-process support and counsel-facing exports (Kahua app, VitruAI).
- Integration with ERP/payment systems (ClaimsBridgeHQ, WhiteHelmet).

### L3 — Vendor-specific

- C-COM's compensation-event "next step" option engine and quotation explorer (NEC-specific machinery).
- ClaimMaster.ai's Event Record Form (CEESM) branding and £99/user pricing model.
- ClaimsBridgeHQ's email-CC ingestion and iDempiere ERP integration.
- Kahua app's dependency on the Kahua platform's configuration/reporting primitives.
- Astora's specific numeric case-study claims (850 documents, 5 days) — marketing figures, not verified.

## Vendor-specific Findings

See L3 above. Additional: the AI evidence-timeline category (Eviant/Storia/Astora/VitruAI) is young and service-flavored (engagement-based); whether it converges into the Type or remains a distinct "dispute evidence" niche is uncertain.

## Boundary Findings

1. **vs Change Order Management** — the decisive seam is *agreement*. A change order records an agreed change to the contract (counterparty approval gate); a claim asserts entitlement when agreement is absent or contested. Claims machinery exists precisely for the no-agreement path; change-order tools do not adjudicate disputes. Directive instruments (e.g., construction change directives) sit between: imposed work without agreed price.
2. **vs Construction Contract Administration** — contract administration is the broader host: notices, instructions, variations, payment certificates, registers. Claims management is the specialized disagreement-path lane; in C-COM it is literally one module of a contract-administration product. Standalone claims products exist, so the Type stands, but it is frequently a module.
3. **vs Litigation / eDiscovery platforms** — those center the legal case (depositions, productions, admissibility, trial); construction claims management centers the project-level contractual claim before and up to formal proceedings. Claims tools export "counsel-ready" material; they do not run the legal case.
4. **vs Insurance Claims Management / Provider Claims Management** — same word, different object worlds (loss adjudication under a policy; medical billing adjudication). No structural overlap.
5. **vs Payment claims / progress claims (polysemy within construction)** — InEight's "Payment claims," and Australian "progress claims," mean payment certification, not disputes. The directory leaf is read as the contractual-dispute sense; the payment-certification sense belongs to Progress Billing / payment certification territory.
6. **vs Daily Log Application / Construction Field Management** — daily logs are precursor evidence; claims products consume them. C-COM's daily diary exists "to be queried days or years later to resolve disagreements and assess claims" — evidence supply, not claim lifecycle.
7. **vs RFI Management** — questions/information requests, not entitlement assertions.
8. **Seam test**: remove the contractual-entitlement assertion (money/time under a clause) and the dispute posture → you have change order management (agreed) or contract administration (routine). Remove the construction contract/project context → generic legal case management. Remove the dispute and keep only payment certification → progress billing.

## Uncertainties

- No Tier-1 operational docs were reachable; lifecycle stage names, default statuses, and field structures are inferred from product descriptions and are stated at moderate strength in the final document.
- The relative market weight of standalone claims products vs contract-administration modules is unclear; the sample suggests both postures exist.
- The AI evidence-timeline wave may redefine the Type's center of gravity (from register/workflow to evidence assembly); current evidence treats it as a variant posture.
- Owner-side vs contractor-side vocabulary differences (claim vs dispute vs entitlement) are observed but not exhaustively mapped.
- Whether NEC "compensation events" should be treated as a claim variant or a separate instrument family is a taxonomy question (C-COM treats them as a parallel module).

## Final Synthesis

A Construction Claims Management application is the system of record for the *disagreement path* of a construction contract: it captures claims — assertions that events on the project entitle a party to more money and/or time under the contract — preserves the evidence trail that substantiates them (linked project records, notices, chronologies), enforces the contractual procedure that governs them (notice deadlines, response periods, clause-referenced correspondence), and tracks each claim through a governed lifecycle from notice to agreement or escalation, maintaining a register of all claims and their commercial position. Its defining shape is four properties: claim records with event + entitlement + impact, substantiation linkage to the project record, a governed lifecycle to resolution, and a claims register. Around that core, mature products add notice/time-bar machinery, contractual correspondence generation, event/diary precursors, response-side handling, commercial reporting, and — increasingly — AI-assembled source-linked chronologies and contradiction detection. The Type sits between Change Order Management (the agreed path it exists to fall back on), Construction Contract Administration (its usual host and broader sibling), Litigation/eDiscovery (the formal legal proceedings it feeds but does not run), and same-word claims Types in insurance and healthcare (different object worlds).
