# Research Notes — Freight Audit & Payment Platform

Research date: 2026-09-07
Leaf: Freight Audit & Payment Platform (Directory §10 Enterprise Operations & Administration, adjacent to Transportation Management System / TMS)
Slug: freight-audit-payment-platform

---

## Research Goal

Understand what a Freight Audit & Payment (FAP) platform actually is and how it works, from real products: what comes into the system, what it is verified against, what happens to discrepancies, how payment is settled, what data objects exist, who operates it, and where its boundary lies against TMS, AP automation, and parcel-refund services.

## Initial Boundary (working hypothesis before research)

- Core use: shippers receive large volumes of freight invoices from carriers; invoices contain errors (rates, fuel surcharges, accessorials, duplicates); the platform audits invoices against contracted rates, resolves discrepancies with carriers, and pays approved invoices.
- Users: transportation/logistics operations + finance/AP.
- Nearest neighbors: TMS (planning/execution; FAP often embedded as a module), Accounts Payable Automation / Invoice Processing (generic supplier invoices), Freight Brokerage / 3PL platforms (move freight vs move money/documents), parcel refund tools (audit-only).
- Unknowns: exact audit→dispute→approve→pay workflow; funding model (does the provider advance funds?); data objects; GL integration depth; whether payment settlement is definitional.

## Research Questions

1. What is the unit of work — what exactly is ingested (EDI, PDF, email, portal feeds)?
2. What is the audit baseline — how are contracted rates/terms represented?
3. What error categories are audited for?
4. What happens to a flagged charge — dispute/claim lifecycle, who acts, how do credits land?
5. How does payment work — approval, payment runs, funding model, remittance?
6. What finance machinery exists — GL coding, cost allocation, accruals?
7. What analytics/reporting does the freight cost record support?
8. What integrations (ERP/TMS/WMS) and data exchange methods are standard?
9. Who operates it — managed service vs self-service software vs hybrid?
10. Where is the boundary vs TMS, AP automation, and audit-only refund services?

## Representative Products

Selected to cover different product philosophies and customer tiers:

| Product | Pole | Customer tier | Evidence |
|---|---|---|---|
| Cass Information Systems — Freight Audit & Payment | managed-service FAP provider (bank heritage, full outsource) | global enterprise | Tier-1: root, FAP hub, Freight Audit page, Freight Payment page (fetched) |
| FreightOptics — Freight Audit and Payment | SaaS platform + managed specialists (hybrid) | mid-market to enterprise | Tier-1: root, FAP solution page (fetched) |
| ShipSigma | parcel invoice audit SaaS, contingency-priced, audit-only (no payment settlement) | mid-market shippers ($100K–$100M parcel spend) | Tier-1: root, Parcel Invoice Audit page (fetched) |
| Shipwell — Settlements | TMS-embedded freight audit & payment module (also standalone) | mid-market/enterprise shippers | Tier-1: root, Settlements page (fetched) |

Attempted but unreachable (abandoned per network-restricted rule after 1–2 failures):
- CTSI-Global — timeout ×3 (ctsiglobal.com, www.ctsiglobal.com)
- nVision Global — root empty/JS, 404 ×2 on section paths
- U.S. Bank Freight Payment — 404 ×2 on guessed paths
- Oracle Transportation Management docs — 404 ×2
- Loop (getloop.com) — timeout ×2
- DuckDuckGo search fallback — timeout

Consequence: sample reduced to 4 products; claims that would have been cross-checked against the bank-owned payment pole (U.S. Bank) or global BPO pole (CTSI/nVision) are written at reduced strength.

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

- Cass Information Systems
  - https://www.cassinfo.com/ (root)
  - https://www.cassinfo.com/freight-audit-payment (FAP hub)
  - https://www.cassinfo.com/freight-audit-payment/services/freight-audit
  - https://www.cassinfo.com/freight-audit-payment/services/freight-payment
- FreightOptics
  - https://www.freightoptics.com/ (root)
  - https://www.freightoptics.com/solutions/freight-audit-and-payment/
- ShipSigma
  - https://shipsigma.com/ (root)
  - https://shipsigma.com/parcel-invoice-audit
- Shipwell
  - https://www.shipwell.com/ (root)
  - https://www.shipwell.com/solutions/settlements

Note: these are product/marketing pages with embedded operational descriptions and FAQs, not full help-center manuals. Workflow and rule claims below are calibrated to that evidence level; no numeric limits, prices, or SLA values from marketing copy are asserted as operational facts in the final document.

---

## Product A — Cass Information Systems (Freight Audit & Payment)

### Key observations (evidence layer A unless noted)

- Positioning: "Full transportation invoice management, validation, audit, accrual, process, and payment." FAP is one specialization alongside utility bill management, waste invoice management, MRO — i.e., the vendor treats freight as one instance of a recurring-invoice audit/pay pattern.
- Canonical definition given by the vendor (Freight Payment page): "Freight payment, also called freight audit and payment, refers to specialized systems and processes that manage high volumes of freight invoices and deliver deep business intelligence about all freight costs. These systems automate and fully integrate the following processes: (1) Invoice receipt and verification, (2) Invoice audits at the charge level, (3) Carrier payments, cycled to terms, (4) Detailed reporting on all aspects of freight costs." — This is the clearest four-part canonical loop found in any source.
- Audit model: "A best-practice freight audit solution provides a closed-loop process to ensure contract compliance... ensure that your freight invoices are paid exactly as prescribed by your supplier contracts... pay no more or no less than the agreed-upon amounts." Software "examines each transaction against a long checklist of possible errors. The system kicks out exceptions to trained freight audit professionals." → rules engine + human exception handling.
- Automation goal: "accurately rate and audit your freight invoices with minimum manual intervention"; system "can be modified to accommodate each client's precise business rules."
- Complex movement handling named: pool shipments, stop-offs, milk runs, intermodal, Rule 11, white glove, spot quotes; "advanced methods for avoiding duplicate payments."
- Modes/move types: "all modes, including ocean, rail, parcel, and multimodal"; "all move types, including outbound, inbound, third party, intercompany."
- Service decomposition (site nav): Freight Audit / Freight Payment / Freight Accounting / Freight Invoice Management / Business Intelligence / Freight Benchmarking; plus Parcel Spend Management and Market Intelligence (SONAR SCI).
- Payment & funds: "Carrier payments, cycled to terms"; "Full protection of funds delivered through SEC and Federal Reserve controls"; Cass is a financial holding company; payment services via wholly owned Cass Commercial Bank; compliant with U.S. Federal Reserve and Dutch Central Bank regulation. Scale claims (marketing): $37B freight spend processed & paid annually; 35M freight invoices; >15,000 carriers in payment network; can pay in 114 currencies across 185 countries.
- Client-facing platforms: CassPort (BI platform: "clear, accurate visibility to detailed cost and shipment information — inbound and outbound, domestic and global, every type of move"; interactive dashboards, multi-dimensional reporting, custom integrations), RateMaker (rate engine portal), FreightClaims portal.
- Freight Accounting service exists as a named service (accruals, cost allocations — implied by hub copy "automated cost allocations and accruals").
- Working capital: "Amplify by Cass" — financing solution extending freight payment terms while paying carriers earlier (financial-services extension).
- Boundary evidence: white paper "9 Reasons it's Risky to use your TMS for freight audit and payment" — vendor explicitly argues TMS-embedded FAP underperforms; confirms TMS↔FAP seam is a live market debate.
- Delivery model: "The delivery of a freight payment solution is a blended model of software and services"; named account teams; benchmarking database access.

## Product B — FreightOptics (Freight Audit and Payment)

### Key observations

- Definition (FAQ): "A freight audit and payment service checks carrier invoices against contract terms, routes exceptions for resolution, and coordinates approved payment. It reduces overbilling and gives finance and transportation teams a clearer record of freight cost and payment status."
- Solution tagline: "Audit, approve, and pay freight invoices"; "recovering up to 7% through automated invoice audit and approved carrier payment execution" (marketing claim).
- Platform concept: "One operating view of transportation spend — Carriers, invoices, contracts, and shipment data in a single record."
- Capability set (FAP page): Automated Invoice Auditing ("checks each invoice against carrier contracts and flags more than 150 potential error types" — vendor claim); Recovery & Dispute Management ("track recovery status while specialists manage eligible claims, carrier follow-up, and credit verification"); GL Code Allocation ("send freight costs to the correct ledger codes and business units with less manual coding"); Unified Carrier Payments ("run weekly payments from approved invoice data. The platform validates each file. Specialists coordinate and track payment").
- Configurable audit & payment logic (illustrated): rate-match tolerance (e.g., ±$2.00 in example graphic), permitted accessorials per rule set, invoice approval limit (e.g., $5,000 in example) → invoices within thresholds "approved and paid," others "held for team review." (Example values are illustrative UI copy, not asserted defaults.)
- Dispute workflow (4 stages, illustrated): error flagged automatically → claim filed with carrier → carrier response tracked in platform → credit verified against the claim.
- Period dashboard states: accrued / audited / in dispute / approved to pay (e.g., $1.31M accrued, $1.28M audited, $61.4K in dispute, $1.22M approved to pay — example figures).
- Analytics: billing accuracy scorecards by carrier; recovered savings trend; recurring error types (example: duplicate charges 31%, accessorials not in contract 24%, reweighs without evidence 18%); "bring recovery evidence into carrier reviews" (claims/credits/patterns as negotiation evidence).
- Error taxonomy (FAQ): duplicate invoices; incorrect fuel, liftgate, residential, and other accessorial charges; dimensional weight errors; misapplied surcharges; service-level guarantee failures.
- Modes: parcel, LTL, truckload, ocean, air. Pre-payment and post-payment audits both supported ("Pre-payment audits catch incorrect charges before payment, while post-payment audits identify recoverable errors that were missed earlier").
- Integrations: ERP (Oracle, SAP), TMS, WMS, order management; data exchange via API, EDI, SFTP. Implementation "typically 4 to 6 weeks" (vendor claim).
- Process (4 steps): Discovery & Integration → Go-Live & Automation (invoices flow; automated audit from first invoice; specialists manage eligible exceptions and coordinate approved carrier payments) → Review Savings and Recovery → Quarterly Performance Review.
- AI agent "IRIS": answers spend questions in plain language, surfaces anomalies, explains cost drivers, links to supporting invoice; "It never closes an exception on its own. Your team decides what happens next."
- Market-posture comparison table (vendor's own): FreightOptics (automated audit + exception handling + payment execution in one workflow) vs Traditional Audit Services (manual audit, recovery separate, outsourced transactional team) vs Self-Service Software (tools for your team to audit and chase recoveries). — Useful evidence for the three delivery postures of the Type.
- Adjacent solutions: Parcel Spend Management, Freight Claim Management ("move valid claims through to settlement" — cargo claims, distinct from billing disputes), TMS, Packaging Optimization, Shipping Insurance, Duty Drawback; white-label/reseller program. SOC 2 Type II, GDPR.
- Client portal: audit.freightoptics.com.

## Product C — ShipSigma (Parcel Invoice Audit)

### Key observations

- Scope: small-parcel (UPS, FedEx) invoice audit; also LTL data; no payment settlement — the shipper pays carriers directly; the platform recovers credits post- or pre-payment via claims.
- Definition (page): "A parcel invoice audit is the systematic review of every line item on a carrier invoice against the shipper's contracted rates, the carrier's published surcharge schedules, and the actual characteristics of each shipment."
- Workflow: "A third-party parcel audit service gains secure access to the shipper's carrier invoice data, typically through a carrier portal integration or an EDI feed authorized by the shipper... every weekly billing file flows through the audit platform automatically. The platform cross-references each invoice against shipment-level data (tracking records, delivery scans, contracted rates, accessorial eligibility) to identify every recoverable discrepancy... Discrepancies are filed as refund claims directly with the carrier's billing system. Claim status is tracked through to resolution, and credits are verified against future invoices rather than left for the shipper to confirm. The cycle repeats weekly."
- Audit objectives (7): late deliveries (guaranteed-service refunds); lost/damaged shipments; incorrect charges (misclassification, e.g., residential surcharge on commercial address); duplicate charges; incorrect address corrections; faulty dimensional weight charges; incorrect rates (failed discount/surcharge cap/tier from the active contract).
- Contract compliance layer: "reconciles each charge against the active contract terms on every invoice" vs carrier published tariff — contract-specific caps/discounts/tiers.
- Time-boxing: "Carrier refund windows for guaranteed service failures and billing disputes are narrow, and a monthly or quarterly review will routinely miss the window" → weekly cadence as operational discipline.
- Manual vs automated comparison: manual = spreadsheets, 5–15 error categories; automated = rules-based logic + ML, dozens of audit points, claims filed automatically.
- Data feedback loop: audit data → service-level mix analysis, accessorial patterns, packaging optimization, contract renegotiation evidence ("Two services, one platform": audit + carrier contract negotiation).
- Pricing model: "no-upfront-cost, contingency-fee model... The auditor earns only when refunds are recovered."
- SaaS portal: audit.shipsigma.com login; dashboards; quarterly reviews with client teams.
- Marketing claims (not asserted as facts): 50+ audit points; 20B data points; 25.2% average savings; $150M saved.

## Product D — Shipwell (Settlements module of TMS)

### Key observations

- Positioning: Settlements is a capability of the Shipwell TMS ("Optimize finances with automated freight audits and payments"), also sold as a standalone module ("you don't need to purchase the complete Shipwell platform").
- Definition: "Shipwell Settlement extracts key data from any invoice format, automatically compares it against shipment financials, and flags exceptions before they clear payment."
- Invoice intake: EDI 210 invoices, PDF invoices submitted in platform, PDF captured from a central email inbox, carrier-generated invoices within the TMS → "consolidate into a single processing queue."
- Matching: "Low Touch First Pass Match" — compares settlement documents against shipment financials; "configurable thresholds so your team defines what counts as an exception"; "invoices that match your thresholds clear automatically"; exceptions flagged "with the relevant discrepancy details."
- Thresholds: "Set payment thresholds by dollar amount or percentage deviation, configure proof of delivery requirements, and define what triggers an exception" — self-service configuration without IT.
- Case-study workflow (PROSOCO): carriers submit invoices via EDI 210 → automatically matched against the rate confirmation → approved invoices move to payment in less than a week; ERP integration called out as high ROI.
- Payment: "Automated payment processing with built-in accuracy checks on every transaction"; "Freight Pay and Audit Managed Services" as an optional managed layer (payment accuracy oversight, compliance assistance).
- Finance: GL code matching; "connects to your existing financial management and payment systems"; "single auditable record of every freight transaction."
- Benefits framing: fewer overpayments, faster carrier payments (carrier-relationship benefit), reduced manual reconciliation.
- Marketing claims (not asserted): up to 30% man-hours reduction; up to 5% freight spend reduction; $111K single-error save (Home Chef).

---

## Cross-product Comparison

| Dimension | Cass | FreightOptics | ShipSigma | Shipwell Settlements |
|---|---|---|---|---|
| Unit of work | freight invoice (all modes) | freight invoice (parcel/LTL/TL/ocean/air) | parcel invoice (UPS/FedEx; LTL data) | freight invoice/settlement doc (TL/LTL focus) |
| Intake | invoice management service (methods not detailed on fetched pages) | API / EDI / SFTP; ERP/TMS/WMS/OMS integrations | carrier portal integration or EDI feed | EDI 210, PDF upload, email inbox, carrier-generated in TMS |
| Audit baseline | client's supplier contracts + business rules ("paid exactly as prescribed by your supplier contracts") | carrier contracts + contract rules | contracted rates + carrier surcharge schedules + shipment characteristics | shipment financials / rate confirmation + configurable thresholds |
| Audit execution | software rules engine → exceptions to audit professionals | 150+ point automated engine (claim) + human oversight | 50-point weekly automated audit (claim) | automated first-pass match vs thresholds |
| Exception handling | kicked out to trained freight audit professionals | routed to claims/dispute workflow; specialists manage carrier side | claims filed automatically; status tracked to resolution | flagged with discrepancy details; team works exceptions |
| Dispute/claim loop | implied (FreightClaims portal exists) | flag → claim filed → carrier response tracked → credit verified | identify → file → track → verify credit against future invoices | exception resolution before payment clears |
| Payment settlement | yes — "carrier payments, cycled to terms"; bank-backed funds | yes — weekly payment runs from approved invoice data; specialists coordinate | NO — audit/claims only; credits against future invoices | yes — automated payment processing; exceptions blocked pre-payment |
| Funding model | provider pays carriers (bank-held funds; scale claims suggest pay-and-recover; mechanics not documented on fetched pages) | provider coordinates payment (funding mechanics not documented) | n/a | client-side payment execution via integrated financial systems |
| GL/accruals | Freight Accounting service; accruals & cost allocations | GL code allocation; accrued/audited/in-dispute/approved-to-pay states | not observed | GL code matching; auditable settlement record |
| Analytics | CassPort BI; benchmarking; freight indexes | dashboards; carrier accuracy scorecards; recurring error patterns | dashboards; savings reports; contract-negotiation evidence | reporting; single source of truth for finance |
| Delivery posture | managed service (blended software + services) | platform + managed specialists (hybrid) | self-serve SaaS + advisory; contingency pricing | TMS module or standalone SaaS; optional managed services |
| Pricing model | not published on fetched pages | not published on fetched pages | contingency (% of recovered refunds) | subscription (module or platform) |
| AI | not emphasized on fetched pages | IRIS agent (answers, surfaces anomalies; never closes exceptions itself) | "AI-powered" audit claims | AI document interpretation; Low Touch First Pass Match |

### Stable commonalities (evidence layer B — across the sample)

1. Carrier freight invoices are the ingested unit of work, normalized into a single processing queue from multiple channels/formats.
2. Every charge is verified against the shipper's contracted rates/terms (contract compliance), not merely against arithmetic validity.
3. A rules/threshold layer decides what passes automatically vs what becomes an exception (tolerances, permitted accessorials, approval limits, POD requirements).
4. Exceptions enter a human-worked resolution loop with the carrier (claim/dispute → response → credit/recovery or acceptance), with credits verified as actually landing.
5. Duplicate-charge detection is a named concern in every product that describes error categories.
6. The validated invoice becomes the freight cost record feeding finance: GL coding/allocation, accruals, payment.
7. Payment settlement of approved payables is the second half of the full-service form (Cass, FreightOptics, Shipwell); ShipSigma deliberately omits it (audit-only posture).
8. Analytics over the resulting shipment-level cost data (spend, carrier accuracy, recovery, recurring error patterns) is universal, and feeds carrier negotiations.
9. Integration with ERP/financial systems (and often TMS/WMS) via API/EDI/SFTP-class methods.
10. Time discipline: claims/refunds are time-boxed (filing windows), driving continuous (e.g., weekly) processing cadence.

### Product-specific observations (kept out of canonical core)

- Cass: bank subsidiary + Fed/Dutch Central Bank regulation; Cass Freight Index / Truckload Linehaul Index (published market indexes derived from its data); Amplify working-capital financing; SONAR market intelligence; RateMaker portal; explicit anti-TMS-FAP marketing.
- FreightOptics: IRIS AI agent with explicit "never closes an exception on its own" posture; white-label/reseller channel; adjacent duty drawback / shipping insurance / packaging optimization; 3PL audit.
- ShipSigma: contingency pricing; UPS Guaranteed Service Refund / FedEx Money-Back Guarantee claim mechanics; carrier-contract negotiation service as twin offering.
- Shipwell: Settlements as TMS module; EDI 210 ↔ rate-confirmation matching; standalone-module packaging; Swifty AI assistant (platform-level).

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

A Freight Audit & Payment Platform is a shipper-side financial operations system whose defining loop is:

```text
Carrier freight invoices (shipment-level payable records, multi-channel intake)
  → charge-level verification against the shipper's contracted rates & terms
      → pass → approved payable
      → exception → discrepancy resolution with the carrier
                    (claim/dispute → carrier response → credit/recovery or acceptance)
  → settlement of approved freight payables (payment executed or driven through the platform)
  → shipment-level freight cost record (feeds GL, accruals, analytics)
```

Minimal invariants — remove any one and it stops being this Type:

1. **Carrier freight invoices as the unit of work** — shipment-level payable records ingested from carriers. Without this there is nothing to audit or pay.
2. **Contract-based charge verification** — every charge checked against the shipper's contracted rates/terms (not just math). Without this it is generic invoice processing.
3. **Discrepancy resolution loop with the carrier** — flagged charges are worked to a recorded resolution (credit, adjustment, or acceptance). Without this the system is a passive checker.
4. **Settlement of approved payables** — the platform settles or drives settlement of validated freight invoices. Without this the product is an audit-only service (a recognized adjacent posture — see Boundary Findings), not the full "audit & payment" form.

Historical check (older/regional products): pre-EDI freight bill pre-audit bureaus (paper tariffs era) received freight bills, checked them against applicable tariffs/rate agreements, corrected/short-paid, paid carriers, and billed the shipper a per-bill fee; post-audit firms recovered overcharges after payment. Both satisfy invariants 1–3; pre-audit bureaus satisfy 4. Modern EDI/cloud/AI machinery is not definitional. ✓

### L1 — Common Mature Structure

- Multi-carrier, multi-modal intake normalization (EDI 210 observed; portal/EDI/PDF/email channels observed) into one queue
- Contract/rate reference data as the audit baseline (rate agreements, discounts, surcharge/accessorial rules, fuel tables)
- Configurable audit rules & tolerances (rate-match tolerance, permitted accessorials, approval limits, POD requirements) → auto-pass vs exception
- Duplicate detection
- Claim/dispute workflow with carrier-response tracking and credit verification
- Approval workflow before payment; payment runs cycled to carrier terms
- GL coding / cost-center allocation; accrual support (accrued vs audited vs in-dispute vs approved-to-pay)
- Freight spend analytics: spend by carrier/mode/lane, billing-accuracy scorecards, recovery reporting, recurring-error patterns; negotiation evidence
- ERP/TMS/WMS integrations; API/EDI/SFTP-class exchange
- Client web portal/dashboard; role split between logistics ops and finance

### L2 — Variant / Optional Structure

- Mode scope: parcel-only ↔ multi-modal (parcel, LTL, TL, ocean, air, rail, intermodal)
- Audit timing: pre-audit (before payment) and/or post-audit (after payment, recovery); both can coexist in one product
- Delivery posture: managed service/BPO ↔ self-service software ↔ hybrid (platform + specialists)
- Funding model: provider advances funds and bills the client (bank-backed pay-and-recover) ↔ client-side execution via integrated financial systems ↔ approval-only
- Pricing: per-invoice/transaction ↔ contingency (% of recovered savings) ↔ subscription
- Geography: domestic ↔ global multi-currency (VAT/duty handling implied at global pole)
- Packaging: standalone platform ↔ TMS-embedded module (also sold standalone)
- Adjacent services: carrier contract negotiation/benchmarking, cargo-claim (freight claim) management, working-capital financing, market indexes, packaging optimization, duty drawback, shipping insurance
- AI assistance: document interpretation, anomaly surfacing, plain-language Q&A agents (era-current across sample)

### L3 — Vendor-specific (research notes only)

- Cass: CassPort / RateMaker / FreightClaims portal names; Cass Freight Index & Truckload Linehaul Index; Amplify by Cass; SONAR SCI; Cass Commercial Bank regulatory framing; scale claims ($37B/35M/15k carriers/114 currencies).
- FreightOptics: IRIS agent; "150+ error types" claim; "4–8% recovery / up to 9% parcel" claims; "38+ carrier integrations" claim; 4–6 week implementation claim; white-label program; example tolerance/approval values (±$2.00, $5,000) are illustrative UI copy.
- ShipSigma: "50-point audit" claim; "20B data points" claim; 25.2% average savings claim; GSR/MBG mechanics; audit.shipsigma.com portal.
- Shipwell: "Low Touch First Pass Match" name; EDI 210 ↔ rate confirmation matching; PROSOCO/Home Chef case studies; 30%/5%/$111K claims.

---

## Vendor-specific Findings

See L3 above. Additional notes:

- Cass explicitly markets against running FAP inside a TMS ("9 Reasons it's Risky to use your TMS for freight audit and payment") — evidence that the TMS/FAP boundary is contested market territory, not a settled taxonomy.
- FreightOptics' own comparison table names the three market postures (full-service platform, traditional audit service, self-service software) — useful as market-structure evidence, vendor-framed.
- ShipSigma's contingency model ties provider revenue to recovered refunds — a business-model variant, not a structural difference in the audit loop.

## Boundary Findings

| Neighbor Type | Relationship | Distinction | "Remove what → becomes the other Type" |
|---|---|---|---|
| Transportation Management System / TMS | adjacent; FAP often embedded as "settlements" module | TMS plans, rates, tenders, executes, and tracks shipments; FAP verifies and settles freight payables after (or before) the move. Shipwell ships both: TMS for execution, Settlements for invoice audit + payment. | Remove the payable audit + settlement loop (keep tender/rate/track) → TMS. Remove planning/execution (keep audit/pay) → FAP. |
| Accounts Payable Automation / Invoice Processing Platform | adjacent | AP automation processes generic supplier invoices (capture, matching, approval, payment) without freight-domain semantics: carrier rate contracts, mode-specific charge structures (fuel, accessorials, DIM weight), carrier dispute/claim channels, freight GL allocation. | Remove freight-specific rate/contract/charge semantics → generic AP invoice processing. |
| Parcel refund / post-audit services (e.g., ShipSigma posture) | audit-only posture of the same machinery | Identifies and recovers billing errors but does not settle freight payables; shipper pays carriers directly; provider earns contingency on recovered credits. | Remove the settlement leg (keep audit + claims) → audit-only recovery service. This is the sharpest internal seam of the Type. |
| Freight Brokerage Platform / 3PL systems | different domain object | Brokerage moves freight (tender, capacity, carrier selection); FAP moves money and documents about freight already moving. | — |
| Shipment Visibility Platform | adjacent | Visibility tracks in-transit shipment state; FAP tracks payable state. Shipment data feeds the audit cross-reference but is not the system of record. | — |
| Freight Claim Management (cargo claims) | adjacent capability | Cargo claims concern loss/damage of goods in transit; billing disputes concern invoice accuracy. Some vendors offer both (FreightOptics lists both); ShipSigma's lost/damaged claims sit at the seam (a lost-package refund is a billing credit for a cargo event). | — |
| Spend Analysis Platform | broader/generic | Generic spend analytics lacks the payable lifecycle, contract-compliance machinery, and carrier dispute channels. | — |

## Uncertainties

1. **Funding mechanics of pay-and-recover** — Cass's pages establish bank-held funds and regulation but do not document the reimbursement cycle (when/how the client reimburses the provider). Written generically in the final doc; no cycle details asserted.
2. **Payment execution depth** — varies from provider-executed payment runs (Cass: "carrier payments, cycled to terms") to coordinated/validated payment files (FreightOptics: "specialists coordinate and track payment") to client-side execution via integrations (Shipwell). Final doc uses moderate wording ("executed or driven through the platform").
3. **EDI transaction-set specifics** — EDI 210 (freight invoice) directly observed at Shipwell; other transaction sets (214, 820, etc.) not observed in fetched pages; not asserted.
4. **Recovery-rate claims** (4–8%, 25.2%, 5%, 30%) are vendor marketing claims; recorded here, excluded from the final document except as clearly attributed vendor claims — actually excluded entirely to avoid false precision.
5. **Global/multi-currency handling** — Cass claims 114 currencies/185 countries (marketing); structural multi-currency support is plausible at the global pole but not operationally documented; final doc mentions global/multi-currency only as a variant pole with qualified wording.
6. **Sample gaps** — CTSI-Global, nVision Global, U.S. Bank Freight Payment, Oracle OTM, Loop unreachable; the bank-owned payment pole and the global-BPO pole are represented only by Cass's own bank-heritage evidence. Claims that would benefit from those sources are written at reduced strength.

## Final Synthesis

The Type is best understood as the **freight payable lifecycle system**: carriers bill; the platform ingests every invoice as a shipment-level payable record; a contract-based rules layer verifies each charge (rates, discounts, fuel, accessorials, duplicates, service-failure credits); exceptions are worked with the carrier to a recorded resolution and verified credit; approved payables are settled on a terms-cycled payment process; and the resulting shipment-level cost record becomes the finance-grade source for GL allocation, accruals, and freight spend analytics that feed carrier negotiations.

The full form (audit + payment) is the market's canonical "freight audit and payment" service; an audit-only posture (post-audit / parcel refund recovery) shares the audit machinery and is best treated as the Type's boundary variant rather than a separate Type, because its objects, workflow, and rules are the same up to the settlement leg.

Delivery posture (managed service ↔ software ↔ hybrid), mode scope (parcel ↔ multi-modal), audit timing (pre ↔ post), funding model, and pricing model are variant axes, not definitional ones.
