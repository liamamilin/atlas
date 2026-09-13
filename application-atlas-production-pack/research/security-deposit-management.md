# Research Notes — Security Deposit Management

Research date: 2026-09-09
Leaf: Security Deposit Management (DIRECTORY §17 Construction, Real Estate & Facilities)
Slug: security-deposit-management
Methodology: v1.1 (update-v1/)

---

## Research Goal

Understand what a Security Deposit Management application is as an Application Type: what the unit of record is, how the deposit moves through collection → custody → disposition, who the actors are, how regulatory governance shapes the product, and where the Type's boundaries sit against Residential Property Management (RPM), Rent Collection, Rental Application, Property Inspection, Tenant/Resident Portal, Lease Administration, and deposit-replacement products.

This pass also must resolve a FORWARD FLAG left by the residential-property-management pass: *"security-deposit-management (trust-held refund-governed deposit lifecycle as primary record vs deposit as charge-at-move-in + disposition-at-move-out inside RPM)"* — i.e., is this a real separable Type, or only a module of RPM?

## Initial Boundary

Working hypothesis before research:

- Core use: hold and release tenants' security deposits correctly — collect at lease start, keep the money safe and separate, decide at lease end how much is returned vs claimed, document and comply with the applicable rules.
- Primary users: landlords / letting agents / property managers; in some regimes a third-party custodian (scheme operator or government body); tenants as the counterparty with visibility and dispute rights.
- Nearest neighbors: Residential Property Management (deposit as one charge among many), Rent Collection (money-in), Tenant/Resident Portal (payer-facing surface), Property Inspection (condition evidence feeding deduction claims), Lease Administration (commercial deposits as lease terms), deposit-replacement/insurance products (a market substitute, likely a different Type).
- Main unknowns: (1) do standalone deposit-centric systems exist in the market, or is deposit handling always embedded in PM software? (2) is the two-sided claim/dispute structure definitional or only a scheme/regime feature? (3) how much of the product is jurisdiction machinery vs Type structure?

## Research Questions

1. What is the unit of record — the deposit fund, the tenancy, the property, the ledger?
2. What custody realizations exist (trust/escrow account in PM software, custodial scheme, insured scheme, government bond authority)?
3. What is the deposit lifecycle, state by state, from collection to closure?
4. How do claims/deductions work — who proposes them, how are they justified, how are they resolved?
5. What does the tenant (payer) see and do?
6. What regulatory machinery appears in-product (deadlines, caps, prescribed information, interest) — and is it definitional or variant?
7. How do PM suites realize the same structures when the deposit is a module, not the product?
8. Where exactly does the deposit-replacement/insurance product category diverge?

## Representative Products

Selected for market representativeness across the two real system families plus the boundary category, with different customer tiers and different philosophies:

| Product | Family | Customer tier / philosophy |
|---|---|---|
| The DPS (Deposit Protection Service, depositprotection.com) | statutory custodial/insured deposit scheme (England & Wales) | scheme operator; deposit protection as the entire product; authorized by government; serves landlords + letting agents + tenants |
| RentRedi (help.rentredi.com) | property-management suite, deposit as module | US self-managing small landlords; consumer-grade PM; deposit handled through payments/ledger machinery |
| Jetty (jetty.com) | deposit replacement / insurance (boundary product) | US institutional property managers; swaps cash deposits for premium-based coverage; merged with Rhino |

Context frames (not sampled as "products" but used as statutory/market frames):

- GOV.UK tenancy deposit protection guidance (the statutory frame that defines the UK scheme market).
- Prior §17 sibling passes recorded in STATUS.md / research/residential-property-management.md (Buildium/AppFolio/Rent Manager/TurboTenant official-doc observations; deposit-in-RPM seam), rent-collection-platform pass (deposit accounts explicitly NOT definitional to rent collection), rental-application-platform pass, property-inspection-application pass (inspection findings feeding deposit/damage documentation), lease-administration pass (commercial lease administration core has no deposit disposition leg).

## Sources

Tier 1 (official operational documentation, directly fetched 2026-09-09):

- GOV.UK — "Tenancy deposit protection" — https://www.gov.uk/tenancy-deposit-protection (fetched; includes approved-scheme list, protection duty, holding-deposit treatment, dispute protection, return timing)
- The DPS — https://www.depositprotection.com/ (fetched; service structure, custodial vs insured, actor surfaces)
- The DPS — "Protecting deposits" — https://www.depositprotection.com/how-to-use-our-service/protecting-deposits (fetched; full registration flow, caps, Prescribed Information, bulk upload, API, interest FAQ)
- The DPS — "The repayment process" — https://www.depositprotection.com/tenants/repayments/the-repayment-process (fetched; both-direction repayment flow, claim/deduction review, dispute resolution, statutory declaration, closure)
- RentRedi Help Center — https://help.rentredi.com/ (fetched; payments/charges navigation: deposit charge type, separate deposit payment account, deposit tracking, refund/Send Money, 1099-K income question)
- RentRedi — "Create Charge for Security Deposit" — https://help.rentredi.com/en/articles/4942818 (fetched)
- RentRedi — "Create a Separate Payment Account for Security Deposits" — https://help.rentredi.com/en/articles/4409262 (fetched)
- Jetty — https://www.jetty.com/ (fetched; deposit replacement positioning, Jetty Deposit, Jetty+Rhino merger notice, insurance-agency compliance footer)

Tier 1 attempted, failed (recorded per source-access limitation rules; no memory-filling):

- The DPS at thedepositprotectionservice.co.uk — transport error (official domain is depositprotection.com; fetched successfully there)
- NSW Fair Trading rental bonds (two URL variants) — 404; RTBA Victoria — transport error; Tenancy Services NZ bond page — 404; mygov.scot tenancy deposits — empty response. AU/NZ/Scotland government bond-custody pole therefore NOT directly observed this pass; treated as class-level market context only, with reduced assertion strength.
- Buildium Help Center — SPA/JS blocked ("CSS Error"), consistent with the prior RPM pass's recorded limitation (that pass used official Help Hub summaries instead).

Secondary (prior sibling passes' official-doc observations, recorded in STATUS.md / research files):

- residential-property-management — 2026-09-09 — Buildium "Accept security deposits via online payment"; trust-accounting compliance (book-locking); deposit as move-in charge + move-out disposition inside RPM; forward flag for this leaf.
- rent-collection-platform — 2026-09-09 — "separate deposit accounts" listed as optional/variant, not definitional to rent collection.
- property-inspection-application — 2026-09-09 — inspection findings consumed by "deposit/damage documentation".
- lease-administration — 2026-09-08 — core has lease abstract + financial schedule + critical dates; no deposit-disposition leg.

---

## Product A — The DPS (statutory deposit scheme)

Evidence layer A (direct observation) unless noted.

### Key observations

- **The deposit is the unit of record, bound to a tenancy.** Registration flow: create account → "Create a new tenancy in your online account" → "Add the tenancy details, including rent amount, deposit amount and contact information for each tenant" → "Pay the deposit to us." Each deposit is an individually tracked protected object with statuses (e.g., 'Deposit Protected'; "mark the deposit as closed in our system").
- **Custody variants inside one product:** free **Custodial** scheme (scheme holds the money) and **Insured** scheme (landlord/agent holds the money; scheme insures it; per-deposit fee paid; separate account required). Both are "deposit protection".
- **Statutory framing is pervasive but external:** the duty to protect with a government-authorised scheme, the deposit cap, Prescribed Information, and penalties are law (Tenant Fees Act, Renters' Rights Act, Housing Act machinery); the scheme product operationalizes them: pre-registration checks ("Is the deposit within the deposit cap limits?", "Do you have a written tenancy agreement?"), deposit cap calculator, Prescribed Information generated from the tenancy record and downloadable as a form, penalty warning ("one and three times the amount of the deposit").
- **Time-window machinery:** protect within 30 days of receiving the deposit; Prescribed Information within 30 days; instalment/individual payments added to the existing deposit with updated Prescribed Information.
- **The tenant is a first-class system actor:** tenant contact details are mandatory at registration because "They'll need to log in to take action on the deposit in the future"; tenant accounts (activating your tenant account); lead/nominated tenant designation ("responsible for dealing with any actions required regarding the deposit"); tenants can check "Is my deposit protected?"; tenant transfer process mid-tenancy.
- **Money ownership is explicitly the payer's:** FAQ — "During the tenancy, the deposit remains the property of the tenant, so any interest accrued is payable to them" (custodial interest payable to tenants after a holding threshold; interest paid at end once repayment completes).
- **End-of-tenancy disposition is a two-sided decision procedure with both entry points:**
  - Tenant-initiated: nominate who acts for tenants → "tell us how you want the deposit to be split" → bank details per tenant → for any amount going to the landlord, "an amount and a reason for each deduction" → submit → landlord/agent reviews → confirm → "we'll repay the deposit as you've instructed".
  - Landlord/agent-initiated: they decide how the deposit should be repaid; if claiming, "provide the amount for each deduction they're claiming and the reasons why"; tenant reviews and confirms/agrees/disagrees per deduction, may propose different amounts with reasons.
  - Agreement → repay as instructed → deposit closed. Disagreement → **Dispute Resolution Service**: "free to use and avoids the need for court action"; both sides "submit evidence to support your position to a dispute adjudicator" (scheme-employed adjudicators; evidence-based; guidance pages on what makes a reasonable claim and what adjudicators do).
  - Unresponsive counterparty → **Statutory Declaration** path: tenant can still start repayment; after non-response and re-contact attempts, a statutory declaration instructs release.
- **Evidence-culture content:** "Keeping good records" guidance, check-in/check-out record emphasis, "What makes a reasonable deposit claim?", news: "Cleaning main cause of tenancy deposit deductions for a fifth year running" — claims are justified against documented condition evidence.
- **Bulk/portfolio operations for agents:** Multiple Tenancy Upload tool (spreadsheet, one row per tenancy, payment reference auto-allocation, manual "allocate funds" reconciliation of bank payments to deposits); API connecting CRM/letting software ("If you use CRM software to manage your deposits, our API can connect your CRM solution directly to our deposit protection platform") — integrations with letting/PM software names (10Ninety, Acquaint, AgentOS, Estates IT, Flatfair, Goodlord, PayProp, etc.).
- **Scheme transfers:** deposits can move between providers (create tenancy + deposit ID → old scheme transfers money; status becomes 'Deposit Protected').
- **Insurance-scheme registration differences:** register deposit details (start/end dates, rent, deposit value, date received), pay premium by card/cheque/direct debit; "The deposit is protected once your payment has cleared" (insured) vs confirmation once money received (custodial).

## Product B — RentRedi (deposit as module inside a PM suite)

Evidence layer A.

### Key observations

- **Deposit is a distinct charge type, not rent:** "Create Charge for Security Deposit" — Charge Type **Security Deposit**, amount, description defaulting to "Security Deposit"; created against the tenant like other charges ("Create charges for Moving-in Tenants" bundles move-in charges).
- **Segregation is a bank-account-level structure:** "Create a Separate Payment Account for Security Deposits" — "Need to keep security deposits in a separate payment account from rent or other charges"; a designated security-deposit payment account "receives payments for charges labeled **'Tenant Security Deposits Held'**" — the ledger vocabulary itself marks the deposit as money *held*, not earned.
- **Held-money status leaks into tax rails:** help article "1099-K: Why is the security deposit counting towards collected income?" — the deposit must be distinguished from rent income in payment-platform reporting; the product has to explain why a refundable held sum appears in gross payment totals. This is the held-liability nature surfacing operationally.
- **Disposition = refund with charges:** refund path lives under "Send Money" — "How to Refund a Security Deposit, Pay a Vendor, or Make an Owner Distribution" — i.e., deposit return is a money-out instruction from the landlord side; deductions are handled through the normal charge/refund machinery of the ledger (create charges, edit, delete, refund via payment rails). No in-product claim/adjudication procedure was observed; disputes are not a product surface.
- **Tracking/visibility:** "Deposit Tracking!" article; tenant ledger downloads; tenants see their charges/payments in the tenant app (tenant-side visibility of ledger exists, though no dedicated deposit-status surface was observed).
- **No statutory machinery in-product:** no protection deadline, cap calculator, prescribed-information generator, or interest machinery observed. Compliance posture is informational (state-specific lease/law resources). The Type's regulatory depth is regime-dependent, not product-family-wide.

## Product C — Jetty (deposit replacement — boundary product)

Evidence layer A (homepage + positioning).

### Key observations

- "Jetty Deposit — The security deposit replacement that swaps expensive cash deposits for a low monthly or one-time payment." The renter pays a premium (monthly or one-time) instead of a refundable cash deposit; the property manager receives "financial protection for your assets".
- Merged with Rhino — "the largest security deposit insurance company in the market" — the category self-identifies as insurance; underwriting/insurance-agency compliance disclosures in the footer.
- **No refundable fund of record exists for the payer:** nothing is held to be returned; there is no disposition step; the premium is not tracked as the payer's money. The defining structures of the deposit Type are absent by design — this is a market substitute operating on the same pain point (move-in capital + damage risk), not the same Type.

## Context frame — GOV.UK statutory guidance

Evidence layer A (for the UK statutory frame; layer B when used to describe the market).

- Landlord "must put your deposit in a government-approved tenancy deposit scheme (TDP)"; three schemes listed for England & Wales (DPS custodial, MyDeposits, TDS) — "They make sure you'll get your deposit back if you meet the terms of your tenancy agreement, do not damage the property, pay your rent and bills."
- Protection within 30 days of receiving the deposit; "Your landlord must return your deposit within 10 days of you both agreeing how much you'll get back"; "If you're in a dispute … your deposit will be protected in the TDP scheme until the issue is sorted out."
- Holding deposits are NOT protected while they are pre-tenancy money; "Once you become a tenant, the holding deposit becomes a deposit, which they must protect." — observed boundary between pre-tenancy money and the security deposit of record.
- Third-party-paid deposits (e.g., rent deposit schemes, parents) are still protected — the payer/obligor binding is to the tenancy, not to the source of funds.
- Separate schemes exist in Scotland and Northern Ireland (regime fragmentation is the norm).

## Context frame — prior §17 sibling passes (layer B/C)

- **RPM pass:** deposits appear inside RPM as "a chargeable item at move-in and a disposition at move-out (Buildium: 'Accept security deposits via online payment')"; trust-accounting compliance machinery (Buildium book-locking "in compliance with trust accounting rules") exists at the professional tier; move-out/deposit-disposition directly observed at AppFolio (bulk move-outs with charges/credits). The pass left the forward flag that this pass discharges.
- **Rent Collection pass:** tenancy-bound charges + payment capture + collection status; "separate deposit accounts" explicitly classified optional/variant — the deposit is NOT the money-in-income record.
- **Rental Application pass:** application machinery ends at the accept/decline decision; move-in money (including deposit) belongs to post-lease systems. GOV.UK's holding-deposit rule corroborates the seam.
- **Property Inspection pass:** inspection findings consumed by "deposit/damage documentation" — condition evidence is an input to deduction claims.
- **Lease Administration pass:** lease abstract + financial schedule + critical dates; no deposit-disposition leg in its core (commercial deposits as ledger items are a variant realization, weakly evidenced this pass).

---

## Cross-product Comparison

| Dimension | The DPS (scheme) | RentRedi (PM module) | Jetty (replacement) |
|---|---|---|---|
| Unit of record | the protected deposit, bound to a tenancy + tenants (individually tracked, statused, closed) | the deposit charge on the tenant ledger + its separate payment account | none (premium; coverage) |
| Custody realization | scheme holds money (custodial) or insures landlord-held money (insured) | separate payment account receiving "Tenant Security Deposits Held" charges | no held money |
| Who holds | third-party custodian / insured party | landlord/PM (their bank, via product rails) | insurer |
| Money ownership | "remains the property of the tenant" | held money distinguished from rent income (1099-K article) | n/a |
| Collection | landlord/agent pays the deposit into the scheme; instalments allowed; auto/manual allocation reconciliation | tenant charged "Security Deposit" via payment rails; recorded-external payments possible | renter pays premium |
| Disposition | two-sided procedure; deductions need amount + reason per item; both parties can initiate; agreement → repay → close; disagreement → in-scheme adjudication; unresponsive → statutory declaration | landlord-side refund via Send Money; deductions via normal ledger charges; no in-product dispute procedure | n/a (claims go through insurance) |
| Tenant (payer) surface | first-class: account, protection status, claim review, repayment initiation, transfer | tenant app shows charges/payments; no dedicated deposit-status surface observed | renter account (policy, not fund) |
| Statutory machinery in-product | pervasive (caps calculator, 30-day windows, Prescribed Information, penalty warnings) | none observed (informational resources only) | insurance regulation only |
| Interest on the fund | yes, to tenant (custodial, after holding threshold) | not observed | n/a |
| Bulk/portfolio ops | multi-tenancy upload; API from CRM/letting software; scheme transfers | portfolio-wide dashboards, reports, exports | property-manager network scale |
| Regulatory posture | exists BECAUSE of statute (authorized operator) | generic PM software; regime-agnostic | insurance/underwriting regime |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures. Removing any one collapses the Type:

1. **The security deposit fund of record** — a persistent, individually identified sum of money collected from one party (the payer — typically the tenant household) against a specific lease/tenancy, carried on the system from collection through to closure. Remove → generic charges/payments (rent-collection / RPM ledger territory).
2. **Held-for-the-payer custody** — the fund is tracked as the payer's money held as security, not earned income: segregated in custody from the holder's operating/income money and releasable only under the lease's conditions. Custody *realizations* vary (separate/trust/escrow account; custodial scheme; insured register) but the held-liability status is the invariant ("Tenant Security Deposits Held", "the deposit remains the property of the tenant"). Remove → deposit is just a move-in charge that the holder may spend (no protection semantics).
3. **End-of-lease disposition against claims** — the lifecycle terminates in a release decision: claimed deductions are identified against the fund (with reasons in mature implementations), the remainder is returned to the payer, and the deposit is closed. Unresolved disagreement escalates (in-scheme adjudication where the product is a scheme; outside the system otherwise). Remove → a locked box (custody with no endgame), or prepaid rent.

Jointly-held load-bearing checks:

- 1 alone = a tenancy charge with a name → RPM/rent-collection slice.
- 2 alone = an escrow/trust account tracker → accounting tooling.
- 3 alone = move-out billing → RPM turnover step.
- 1+2 without 3 = custody with no release path (not a functioning deposit practice).
- 1+3 without 2 = deposit as income/charge (the pre-protection regime; loses the defining "held money" semantics).
- 2+3 without 1 = escrow machinery unbound to any tenancy.

### L1 — Common Mature Structure

Very common in mature implementations, not definitional:

- itemized deduction claims (amount + reason per item) and an evidence/records culture (check-in condition records justifying claims)
- two-sided confirmation of the disposition (proposed split reviewed by the counterparty) — structural in schemes, absent/one-sided in simple PM modules
- payer-facing visibility and self-service (protection status, accounts, repayment initiation, per-tenant bank details)
- partial/instalment collection into an existing deposit; mid-tenancy party transfer
- interest accrual for the payer; statutory/prescribed information notices generated from the record
- deadline machinery (protection/registration windows, return-after-agreement windows) and cap/amount-rule computation
- dispute resolution procedure with neutral adjudication (in-scheme ADR) and evidence submission
- portfolio/bulk operations for agents; API/integration from PM/CRM software; scheme-to-scheme transfers
- closure/archive state; audit trail of status changes

### L2 — Variant / Optional Structure

Depends on jurisdiction, market segment, product family:

- regime machinery specifics: protection deadlines (30 days observed), return-after-agreement windows (10 days observed), caps (5/6 weeks' rent observed in England), penalty multipliers (1–3× observed), interest rules (183-day threshold observed) — jurisdiction-specific numbers, NOT definitional
- custody actor: private authorized scheme vs government-operated bond authority (AU/NZ-class; NOT directly observed this pass) vs landlord-held with insurance vs self-held trust account (US small-landlord)
- custodial vs insured scheme split (fee-based protection of landlord-held funds)
- commercial-lease deposits tracked as lease-administration ledger items (variant realization; weakly evidenced this pass)
- short-stay damage deposits implemented inside booking platforms (adjacent realization; not sampled this pass)
- statutory-declaration / unresponsive-counterparty paths; tribunal/court escalation outside the product
- deposit replacement/insurance as a market substitute (adjacent category — see Boundary Findings)

### L3 — Vendor-specific (Research Notes only)

- DPS: Multiple Tenancy Upload spreadsheet tool with payment-reference auto-allocation; named CRM/letting-software API partners; insured-scheme per-deposit fees (£18.75 / £27.75 / £11.75+VAT observed); 183-day custodial interest threshold; deposit-cap calculator; Welsh "Required Information" terminology; six-month placeholder end-date practice under the Renters' Rights Act; 'Deposit Protected' status vocabulary.
- RentRedi: "Tenant Security Deposits Held" charge label; security-deposit payment-account type; refund via Send Money rail; 1099-K gross-payment interaction.
- Jetty/Rhino: merger into the largest deposit-insurance company; underwriting by named carriers; two million units claim.
- GOV.UK: APT replacing AST terminology (May 2026); valuable-items-in-lieu rule for non-APT tenancies.

## Rejected Findings

- "Security deposit management = UK deposit protection schemes" — rejected; PM-suite modules realize the same L0 without any scheme machinery.
- "Two-sided in-product dispute adjudication is definitional" — rejected; adjudication is scheme-family (DPS); PM modules and most US practice resolve disputes outside the product. Only "disagreement escalates somewhere" is abstracted into L0 leg 3.
- "Interest accrual is definitional" — rejected; observed at DPS only in the sample; regime-dependent.
- "Deposit caps/deadlines are definitional" — rejected; jurisdiction machinery (L2); the US sample carries none in-product.
- "The tenant always has a portal surface" — rejected as definitional; strong at DPS, weak at RentRedi (ledger visibility only). L1.
- "Deposits are only residential" — rejected; commercial deposits tracked as ledger items exist (variant, weak evidence); the L0 is deliberately lease-type-agnostic.

## Boundary Findings

- **vs Residential Property Management** — RPM's record is the managed stock + tenancy + rent cycle + turnover; the deposit appears as one move-in charge and one move-out disposition inside that record. Here the **deposit fund itself is the record**: scheme systems have no property-management function at all (no units, marketing, maintenance, owners), and the PM-suite pole shows the deposit structures (separate held account, held-status labeling, refund path) standing as their own sub-record with their own vocabulary. Remove the deposit-centric record and put the tenancy at the center → RPM. Remove the tenancy/portfolio spine and keep the deposit lifecycle → this Type. **Keep-both ratified; forward flag discharged.** Same capability-layer pattern as prior §17 capability passes.
- **vs Rent Collection Platform** — rent charges are income debts settled by payment; the deposit is held money returned at end (the rent-collection pass itself classifies deposit accounts as outside its core). Remove held-for-payer custody + disposition → rent collection.
- **vs Rental Application Platform / pre-tenancy money** — holding deposits before the tenancy are NOT the security deposit of record (GOV.UK: protected only "once you become a tenant"). The Type's record begins at the executed lease.
- **vs Property Inspection Application** — condition evidence feeds deduction claims (DPS records guidance; inspection pass names deposit/damage documentation as a consumer of findings). Inspection is an evidence producer; this Type is the money machinery.
- **vs Tenant/Resident Portal** — payer-facing visibility is a surface of this Type (strong in schemes); the portal's record is the resident relationship, not the fund.
- **vs Lease Administration** — commercial deposits are lease financial terms in that Type's lens; the disposition-at-exit lifecycle is this Type's center (weak direct evidence for the commercial pole this pass).
- **vs Deposit Replacement / Insurance products (Jetty/Rhino-class)** — premium in, coverage out; no refundable fund, no custody, no disposition. The closest market substitute and the sharpest boundary: remove the refundable held fund and the product leaves this Type entirely.
- **Remove-test for the whole Type:** take away the held-liability custody status and the end-of-lease refund/claims disposition — what remains is a move-in fee, i.e., RPM's charge-at-move-in. Take away the lease binding — what remains is generic escrow. This is the minimal defining frame.

## Taxonomy Assessment

The leaf is a **legitimate capability-centric Type**, not a pure RPM alias: (a) standalone systems exist whose entire record is the deposit (statutory schemes; scheme operators run the product because the law makes the deposit a protected object of record); (b) the held-liability + disposition structures carry their own vocabulary and flows even inside PM suites; (c) the RPM pass's forward flag is discharged with keep-both. Residual risk noted: in markets without statutory scheme machinery (e.g., much of the US), the deposit exists mainly as an RPM module; the Type's center of gravity there is thinner. Recorded in STATUS.md Boundary Issues.

## Uncertainties

- AU/NZ/Scotland/NI government bond-authority pole not directly observed (all fetches failed: 404/transport/empty). The claim "in some jurisdictions custody itself is run by a government body" is class-level market context only; kept out of the final document's strong assertions.
- Buildium/AppFolio professional-tier deposit flows not directly fetched this pass (SPA blocks); reliance on the RPM pass's recorded observations (which themselves noted Buildium move-out flows were "not surfaced"). Professional-tier US practice is therefore layer-B.
- Commercial-lease deposit disposition flows: no direct evidence this pass; variant status is inferred from the lease-administration pass's core definition, not from commercial product docs.
- Short-stay damage deposits: not sampled; presence in booking platforms assumed from market structure, not verified.
- Exact jurisdiction numbers (caps, deadlines, penalties) are observed only for England & Wales via DPS/GOV.UK; they are recorded as regime examples, never generalized.

## Final Synthesis

A Security Deposit Management application is the system of record for a **protected deposit fund bound to a lease**: money collected from a payer at tenancy start, held — by the holder or a third-party custodian — as the payer's money (segregated from income, releasable only under the lease's conditions), and carried to a terminal disposition at lease end where claimed deductions are identified against the fund, the remainder is returned to the payer, and the deposit is closed. Around that core, mature implementations add the claim-justification and evidence culture, two-sided confirmation and dispute paths, payer-facing visibility, statutory notice/deadline/cap machinery, interest handling, bulk/API operations, and custody variants (custodial scheme / insured register / trust-escrow account). The market implements the Type in two families — statutory deposit schemes (deposit as the entire product) and PM-suite modules (deposit as a held-liability sub-record) — plus an adjacent substitute family (deposit-replacement insurance) which fails the core and is a different Type.
