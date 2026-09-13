# Research Notes — Rent Collection Platform

Research date: 2026-09-09
Slug: rent-collection-platform
Directory leaf: Rent Collection Platform (§17 Construction, Real Estate & Facilities)

## Research Goal

Understand the Rent Collection Platform as an Application Type: what its defining core is (the smallest structure without which it stops being recognizable), what mature products commonly add, where the boundary runs against full property-management systems, lease administration, generic billing/AR machinery, and consumer payment apps — and how the Type varies across customer tiers (DIY landlords → small landlords → enterprise operators).

## Initial Boundary Hypothesis

- Core guess: a platform that (a) holds recurring rent obligations per tenancy, (b) gives the tenant a payment channel, (c) tracks paid/unpaid/partial/overdue status per obligation, with money remitted to the landlord.
- Likely nearest neighbors (per prior passes):
  - Residential Property Management / Commercial Property Management — the full operating system; rent collection is the money-in slice.
  - Lease Administration — administration of obligations (terms, schedules, dates) vs payment execution.
  - Tenant / Resident Portal — the tenant-facing surface of a management system.
  - Billing / Invoicing / Accounts Receivable — domain-agnostic money machinery.
  - Peer-to-peer Payment Application — money movement with no obligation structure.
  - Security Deposit Management, HOA/Community Association Management, Short-term Rental Management — adjacent money/tenancy Types.

## Research Questions

1. What objects exist? (property/unit, tenant, charge, payment, deposit, payment account, late-fee rule, ledger/balance)
2. How does the money flow work end-to-end: charge creation → tenant payment (methods, fees) → payout/deposit → reconciliation?
3. What happens on non-payment: reminders, late fees, arrears, partial payments, payment blocking?
4. What do the two sides (landlord / tenant) each see and do?
5. What failure/exception modes exist (failed autopay, ACH returns, chargebacks, refunds, rent forgiveness, outside payments)?
6. What adjacent capabilities creep in (leasing, screening, maintenance, accounting, credit reporting) and how do they relate to the core?
7. Where is the line vs full PM suites, vs generic billing, vs P2P payment apps?
8. Historical check: does the definition survive the paper rent book / in-person cash era?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers.

| Product | Tier / philosophy | Evidence reached |
|---|---|---|
| RentRedi | DIY/independent landlords; mobile-first landlord+tenant app pair; rent collection inside a broader landlord suite | Product page (Layer A) + full help-center article tree (Layer A) |
| Azibo | DIY landlords; free-collection platform; broader landlord suite | Rent-collection product page + FAQ (Layer A); help center closed/moved (limitation) |
| PayRent | DIY landlords; payments-only minimal probe with legal-flavored payment controls | Product page + FAQ (Layer A); help center fetch returned empty (limitation) |
| RentPayment (MRI Software) | Enterprise resident-payments pole for property managers (1–750 / 750+ units); payment layer integrated with PM systems, multi-vertical | Product pages (Layer A) |

Rejected/unreachable samples: Avail (avail.co 403, support.avail.co 404 — abandoned per network rule), TurboTenant (503 ×2 — abandoned). Cozy (discontinued, not sampled).

## Sources

- RentRedi — https://www.rentredi.com/rent-collection/ (product page, fetched 2026-09-09)
- RentRedi Help Center — https://help.rentredi.com/ (collections/article tree, fetched 2026-09-09; article titles used as structural evidence; individual article bodies not fetched)
- Azibo — https://www.azibo.com/rent-collection (product page + FAQs, fetched 2026-09-09)
- Azibo Help Center — https://azibo.zendesk.com/hc/en-us/... — "Help Center Closed" (moved; unreachable)
- PayRent — https://payrent.com/ (product page + FAQs, fetched 2026-09-09)
- PayRent Help Center — https://support.payrent.com (fetch returned empty — unreachable)
- RentPayment (MRI Software) — https://mrisoftware.rentpayment.com/ (fetched 2026-09-09); property-manager and resident-benefit pages linked from it
- Avail — https://www.avail.co/rental-payments/ (403), https://support.avail.co/hc/en-us (404) — abandoned
- TurboTenant — https://www.turbotenant.com/rent-collection/ (503 ×2) — abandoned

Source-access limitation: no Tier-1 help-center article bodies were retrieved for Azibo/PayRent/RentPayment; RentRedi's help-center tree was retrieved at collection/title level. Therefore the final document avoids asserting precise fee percentages, exact status vocabularies, exact payout windows, and product-internal workflow parameters beyond what the reached pages state.

## Product Observations

### RentRedi (Layer A unless noted)

Positioning: "Online Rent Collection" inside a broader landlord suite (landlords app + tenants app).

From the product page + FAQ:
- Tenants pay via ACH (bank transfer), credit card, debit card, or cash at 90,000+ retail Chime locations (product-specific count).
- Card payments carry convenience fees; ACH presented as the lowest-cost option; tenants see the total before submitting.
- Tenant-side Auto-Pay withdraws rent automatically each month; landlords create recurring charges so rent and utilities are billed automatically each cycle.
- Late fees: automatically applied "based on your lease terms"; landlords customize grace periods, payment schedules, notifications; automatic reminders; block payments.
- Landlords track deposits and payment status in real time from one dashboard; FAQ states ACH deposits typically 2–3 business days (vendor-stated; do not generalize as industry fact).

From the help-center tree (structure = evidence of the object model):
- Inventory hierarchy: Portfolios → Properties → Units (unit codes, unit notes, archive/delete).
- Tenants: invite/resend/declined-invite states, connect tenant to lease, link multiple tenants to a unit, link a prior tenant, archive prior tenants, tenant app preview, tenant payment-record visibility, block payments for a tenant, obtain tenant information for eviction.
- Charges (the obligation object): Create a Charge (recurring marked with a recycle symbol), security-deposit charge, charges for individual tenants, month-to-month lease charges, weekly charges, prorated rent, charges with past due dates, automatic utility collection, one-time charge, automatic rent increases, Section 8 charges, roommate charges (joint and separate), charges for moving-in tenants.
- Viewing: transactions, payments, charges per unit, charges per tenant, tenant ledger download, overdue charges, deposit tracking, find individual payments inside a deposit, separate transfers for deposits, payment history; new tenants do not see prior tenants' charges.
- Payment accounts & deposits: multiple payment accounts, separate payment account for security deposits, deposit tenant payments into different bank accounts, payment account connected to a property, account under-review/underwriting states, EIN/SSN requirements, deposits on hold.
- Fees & settings: credit-card convenience fee guide, pay the $1 ACH convenience fee for tenants (product-specific), ACH-only setting, make tenants pay oldest charges first, payment link on the landlord's website.
- Recording outside payments: add a payment received, record multiple months paid outside the platform, mark multiple charges as paid, add Section 8 payments, record overpayments and outside payments.
- Late fees: automatic setup, late-fee rules, when fees apply, ensure tenants pay rent and late fees together, late fee as separate charge, delete a late fee rule / a tenant's late fee.
- Editing & deleting: edit charge, delete charge / all future charges / duplicate charges, update a charge for rent forgiveness, delete a payment, void/refund via Stripe and ProPay (processor names).
- Exceptions: ACH returns 101, clawbacks (platform reclaims deposited funds on return), tenant-initiated disputes/chargebacks, manually document a returned payment, bank response codes, card-absent-environment fraud.
- Send Money (outbound): refund a security deposit, pay a vendor, owner distribution.
- Accounting (suite context): expenses, bank-feed import, Schedule E report, P&L, 1099-K forms for payment processors.
- Troubleshooting: rent charges & time zones, tenant connected to charges, auto-pay not running, authorized payments on behalf of tenant, changing rent amount affects tenant's auto-pay.
- Suite context (not the collection core): leasing (listings, syndication to Zillow, applications, screening), maintenance requests, documents, ID verification, 2FA/SSO.

### Azibo (Layer A unless noted)

Positioning: "Free rent collection — unlimited units, no fees."

From the product page + FAQ:
- Methods: ACH / bank transfer, Cash App, cash, credit & debit; tenants can enable autopay.
- Rent deposited directly into the landlord's bank account; no limit on linked bank accounts; payouts "as fast as 2 business days" (vendor-stated).
- Payments automatically tagged & categorized into reporting/bookkeeping.
- Automatic reminders when rent is due and when it is late; tenant pays from the email in a few clicks.
- Real-time payment statuses on one dashboard: who paid, who hasn't, who made partial payments.
- Late fees: one-time or recurring (daily, weekly, monthly cadence), automatically added once rent is late.
- Partial payment blocking, with an explicitly stated legal rationale: partial payments are "a common way for tenants to avoid eviction," and blocking protects the landlord if an eviction happens.
- Ancillary billing: "billing for ancillary items as they crop up" (testimonial-level evidence).
- Credit building: rent reporting tied to card payments / credit-builder feature (tenant side has Credit Boost).
- Pricing: free for property owners; tenants may incur a fee for certain payment methods.
- Tenant-initiated onboarding: renters can sign up and "Invite Your Landlord."
- Suite context: rental applications, tenant screening, lease creation, document storage, maintenance & messaging, financial management, accounting, collaborate, insurance, marketplace.
- Market-boundary artifact: a dedicated "vs Venmo" comparison page — autopay, automated late fees, due/late reminders, and partial-payment blocking as the differentiators vs P2P apps.

### PayRent (Layer A unless noted)

Positioning: "The easiest way to collect & pay rent online" — payments-only posture, built for independent landlords, no unit minimums.

From the product page + FAQ:
- Tenants pay by bank transfer (ACH, "from any U.S. bank or credit union") or credit card; can schedule payments ahead of the due date; automatic reminders before rent is due.
- Landlord dashboard: occupancy, tenant balances, and upcoming charges "at a glance"; collected vs outstanding amounts; upcoming charges list; exportable reports that "work with virtually every accounting system."
- RentDefense™ controls (product-specific name): refuse partial payments automatically; block payments; landlord's personal details never shared with renters (privacy); "bank-grade encryption."
- Split rent: roommates each pay their share.
- Credit reporting: on-time rent reported to all three major credit bureaus (free for on-time renters); flexible schedules via Livable partnership (product-specific).
- Fees: card fees are the tenant's responsibility, never the landlord's; option to cover ACH fees for tenants.
- Market-boundary artifact: a ranked "best ways to pay rent online" list — online rent collection (recommended) vs Zelle (limits, partial payments, shared personal details, misdirected funds) vs Venmo/PayPal/CashApp (personal payments, business fees, partial-payment exposure) vs checks vs cash. The vendor itself articulates the P2P boundary.
- FAQ explicitly discusses chargebacks ("a renter disputes a charge and you have to show it was legitimate").
- Help center exists at support.payrent.com but fetch returned empty (limitation).

### RentPayment — MRI Software (Layer A unless noted)

Positioning: "Online rent payment software" for property managers; the enterprise resident-payments pole.

From the product pages:
- For property managers: resident self-service payments "instead of collect[ing] from your residents," highly detailed reporting, marketing tools, resident-adoption programs, dedicated support/relationship managers.
- For residents: pay 24/7 from any device through the online portal; debit, credit, ACH, bank bill payments, Flexible Rent payments, checks, and cash; auto payments; email and text reminders ("no more late fees").
- Verticals: Multifamily, Commercial, HOA, Self Storage — the money-in machinery extends beyond residential rent (vendor extension of the same payment spine).
- Integrates with leading property-management systems (MRI, Yardi, RealPage, TOPS, AMSI, Property Boulevard shown) — inside a PM stack, this product is the payments layer on top of the PM system's lease/tenancy records.
- Pricing posture: tiered by unit count (1–750 / 750+), tailored/negotiated ("Your Price, Your Way").
- Product-specific: RentPayment Rewards powered by Piñata (renter loyalty platform).
- Testimonial evidence: electronic payments for faster cash flow, late-fee avoidance, remote drop-off elimination.

## Cross-product Comparison

| Aspect | RentRedi | Azibo | PayRent | RentPayment (MRI) |
|---|---|---|---|---|
| Owed-money object | Charges: recurring (monthly/weekly), one-time, security deposit, utilities, late fee, prorated, rent increases, Section 8, roommate joint/separate | Rent + ancillary billing; one-time or recurring late fees | Tenant balances + upcoming charges per unit | Charges carried via PM-system integration; Flexible Rent |
| Charge substrate | Tenant linked to unit/lease in portfolio (Properties → Units) | Tenant of a property owner | Unit + tenant (12-unit portfolio mock: "Unit 4B · Maria S.") | Resident/account inside a PM system |
| Payment methods | ACH, card, cash at retail locations | ACH, Cash App, cash, card/debit | ACH, credit card | ACH, card, debit, bank bill pay, Flexible Rent, checks, cash |
| Autopay / scheduling | Tenant Auto-Pay; recurring landlord charges; rent-increase handling | Tenant autopay | Schedule payments ahead | Auto payments |
| Reminders | Automatic; late-fee automation | Automatic due + late reminders | Automatic pre-due reminders | Email + text reminders |
| Late-fee machinery | Rules: grace periods, when applied, separate charge, deletion/forgiveness | One-time or recurring (daily/weekly/monthly), auto-added | (controls emphasized instead) | (not surfaced on public page) |
| Partial payments | Block payments for a tenant | Block partial payments — eviction rationale explicit | Refuse partial automatically (RentDefense™) | (not surfaced) |
| Outside payments | Recorded: cash/check/Section 8/housing authority, overpayments | Cash method; (recording implied) | (not the posture — digital rails only) | Checks and cash accepted/processed |
| Payout / deposits | Payment accounts (multiple, underwriting/verification), deposit tracking, batched deposits, deposits on hold | Direct deposit, unlimited linked bank accounts, "as fast as 2 business days" | Funds to landlord (window not stated on reached pages) | To property manager/owner via platform |
| Failure/reversal handling | Deep: ACH returns, clawbacks, chargebacks, disputes, void/refund | (not surfaced publicly) | Chargebacks discussed in FAQ | (not surfaced) |
| Tenant surface | Tenant app: charges, pay, autopay, history | Renter signup, invite-your-landlord, pay from email | Pay from any connected device | Portal, 24/7 |
| Landlord surface | Dashboard: status/deposits/overdue; tenant ledger; exports | One dashboard: paid/unpaid/partial | Dashboard: balances, upcoming charges, collected vs outstanding, reports | Reporting, adoption tools |
| Credit reporting | Credit Boost | Credit builder | 3 bureaus for on-time payers | (resident benefits programs) |
| Split payments | Roommate charges joint & separate | (methods support) | Split rent (roommates) | (not surfaced) |
| Fee bearing | $1 ACH fee landlord-payable; card fees tenant-side typically | Free for landlords; tenant fees on some methods | Card fees tenant's responsibility; optional landlord-covered ACH | Negotiated ("Your Price, Your Way") |
| Scope beyond collection | Leasing, screening, maintenance, documents, accounting (suite) | Applications, screening, lease, maintenance, accounting (suite) | Minimal — reports/exports only | Verticals (MF/commercial/HOA/storage), rewards, PM-system integrations |
| Tier | DIY landlords | DIY landlords, free | DIY landlords | Enterprise PM (1–750 / 750+ units) |

Stable commonalities (all four): recurring rent charges bound to tenant+unit; tenant-side payment initiation with autopay or scheduling; reminders; per-obligation paid/unpaid status visible to the landlord (dashboard) and the tenant (history); funds ultimately routed to the landlord/manager's bank account.

Near-universal (3/4): multiple payment methods incl. ACH + card; late-fee machinery or payment controls; partial-payment handling; split/roommate payments; credit reporting (RentRedi, Azibo, PayRent — not surfaced at RentPayment); fee-bearer asymmetry (platform fee falls on one side, commonly the tenant for card).

Single-product-depth (mark product-specific): ACH-returns/clawback machinery (RentRedi); $1 ACH fee (RentRedi); Chime retail cash network (RentRedi); Cash App method (Azibo); RentDefense™ (PayRent); Livable flexible-schedule partnership (PayRent); Piñata rewards (RentPayment); eviction-information tooling (RentRedi); oldest-charges-first rule (RentRedi); separate deposit payment account (RentRedi).

## Canonical Model (abstraction layers)

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The tenancy-bound rent charge of record** — a persistent, individually tracked money obligation for rent (and directly related recurring charges) bound to a specific ongoing tenancy: an identified tenant occupying an identified rental unit in the landlord's/manager's portfolio, carrying an amount, a due date, and a recurrence; the tenancy's charges and payments accumulate into a running balance.
   Remove → generic invoicing/billing with rental vocabulary; no tenancy substrate, no portfolio context.

2. **Rent payment capture against the charge** — the tenant's rent payment is made through the platform (dominantly online methods: bank transfer, card; commonly cash networks) or recorded into it (cash/check/off-platform payments), and is applied against the tenancy's charges.
   Remove → a passive ledger/spreadsheet; no collection.

3. **Per-obligation collection status** — every charge is tracked to a payment state (paid / unpaid / partial / overdue — labels vary by product), so the landlord can see at any time who has and hasn't paid across the portfolio, and both sides can see balances and payment history.
   Remove → a payment page/checkout or P2P transfer that moves money but keeps no per-obligation record; the "collection" dies.

Jointly-held load-bearing tests:
- 1 alone = recurring invoicing (rent-shaped billing with no payment rail).
- 2 without 1+3 = P2P transfer / payment link (money moves, nothing is tracked).
- 3 without 1+2 = a manual tracker over nothing the platform manages (the paper rent book's record-keeping half).
- 1+2 without 3 = a checkout rail with no arrears/balance picture.
- 1+3 without 2 = the paper rent book (ancestor: obligations + recorded in-person payments; no platform rails).

### Historical / market-sample check (§24 discipline)

- Paper-era ancestor: the landlord's rent book / rent roll — monthly obligations listed per tenant, cash or check paid in person, payment recorded (signature/receipt), paid/unpaid status visible per month. Satisfies structures 1+3 with the payment leg realized as in-person recording. Therefore L0 must NOT require: online rails, autopay, reminders, late fees, dashboards, credit reporting, cloud delivery.
- Regional forms: UK rent books, in-person cash collection with manual receipts, informal landlord ledgers — all fit structures 1+3 + recorded payment.
- Enterprise pole: RentPayment carries the same spine (charges/resident accounts + payment methods + reporting) inside a PM stack — the PM system holds lease/tenancy records while the platform holds the money-in machinery; still this Type.
- Conclusion: L0 stands as abstracted; modern machinery (autopay, ACH/card rails, deposit batching, dashboards) is the dominant implementation of the legs, not the definition.

### L1 — Common Mature Structure

- Recurring auto-billing of rent from lease terms (monthly dominant; weekly and other cycles observed); automatic rent increases.
- Tenant autopay; payment scheduling ahead of the due date.
- Automatic reminders (due, late, pre-due).
- Automatic late-fee rules: grace periods, fixed or recurring cadence, late fee as separate charge, deletion/forgiveness.
- Multiple payment methods: ACH/bank transfer, credit/debit card, cash (retail cash networks or recorded); convenience-fee handling with a fee-bearer choice.
- One-time and ancillary charges: utilities, fees, moving-in charges, security-deposit charges.
- Split/roommate obligations (joint and separate), partial-payment handling incl. blocking.
- Payment/deposit accounts: verified landlord deposit accounts (underwriting/identity states observed), multiple accounts, property-to-account mapping.
- Deposit/payout machinery: batched deposits, deposit tracking, hold states.
- Payment recording for outside payments (cash, checks, subsidy programs).
- Receipts/payment history and tenant ledger; balances per tenant and portfolio-wide.
- Landlord dashboard: who paid / hasn't / partial, upcoming charges, collected vs outstanding.
- Reporting/exports feeding accounting (and tax-form outputs in the US sample).
- Tenant-facing app/portal and payment links.
- Credit-bureau rent reporting (US market; common but not definitional).
- Privacy posture: landlord's personal banking details hidden from tenants (contrast with P2P).

### L2 — Variant / Optional Structure

- Fee-bearer model: free-for-landlord with tenant-paid method fees (Azibo/PayRent-flavored), landlord-paid fees, or negotiated enterprise pricing.
- Cash infrastructure: retail cash-network acceptance vs manual recording only.
- Subsidy-aware charges: Section 8 / housing-authority charge splits (US).
- Flexible rent: schedule alignment to paydays, rent splitting/installments (partner-driven at PayRent; "Flexible Rent" as a method at RentPayment).
- Separate security-deposit handling on dedicated payment accounts.
- Eviction-support artifacts: payment blocking, partial-payment refusal as legal posture, tenant-information export for eviction (RentRedi).
- Vertical extensions at the enterprise pole: HOA dues, self-storage, commercial rent through the same payment spine.
- Tenant-initiated onboarding (renter invites landlord).
- Rewards/loyalty programs for residents.
- Suite bundling: rent collection shipped as one module inside all-in-one landlord suites (leasing, screening, lease creation, maintenance, accounting).
- US regulatory machinery: 1099-K issuance for processed volume (era-current).

### L3 — Vendor-specific (research notes only)

RentDefense™ controls (PayRent); Piñata-powered rewards (RentPayment); "90,000+ retail Chime locations" (RentRedi); $1 ACH convenience fee (RentRedi); Livable partnership (PayRent); Cash App as a method (Azibo); unit codes & portfolios (RentRedi); Schedule E report generation (RentRedi); AI property creation (RentRedi); MRI/Yardi/RealPage integration roster (RentPayment); "62% more on-time payments" marketing claims (PayRent — excluded from final doc as unverifiable marketing); Stripe/ProPay as underlying processors (RentRedi).

## Vendor-specific Findings

- RentRedi is the only sampled product exposing the full failure/reversal machinery publicly (ACH returns, clawbacks, chargeback disputes, bank response codes) — a common problem class handled everywhere, but documented in depth by one product; do not promote specific mechanics to the Type core.
- PayRent's identity is the payments-only minimal posture with legal-flavored controls; its "ranked payment methods" page is vendor marketing that nonetheless documents the market's own P2P boundary.
- Azibo's "vs Venmo" page is the same market-boundary artifact from another vendor.
- RentPayment generalizes the spine across verticals (HOA/self-storage/commercial) — a vendor extension, not the residential-rent center of the Type.

## Boundary Findings

- vs **Residential Property Management** (broader system of record): RPM holds units/tenancies/maintenance/leasing/accounting as one operating system; this Type holds the money-in slice. Directional tests: add leasing + maintenance + full accounting as the center → RPM; strip everything but charges/payments/status → this Type. Consistent with the commercial-property-management pass's recorded seam ("Rent Collection Platform (money-in slice only)").
- vs **Commercial Property Management**: commercial rent is lease-structured (escalations, recoveries, percentage rent) and billed by lease-driven machinery inside commercial PM; this Type centers periodic rent charges against ongoing tenancies. RentPayment's commercial vertical shows the payment spine generalizing, but the Type's center remains periodic-rent collection.
- vs **Lease Administration** (processed 2026-09-08): that pass recorded the seam as "administration of obligations vs payment execution" — corroborated from this side: the sampled platforms hold simple recurring charge schedules, not abstracted lease terms, options, or critical dates; none present lease-review/notice machinery. The lease-administration pass's evidence-gap note (lessor-side lease-admin structures inside PM suites unobserved) is only partially corroborated here — this pass's sample corroborates the payment-execution side of the seam, not the lessor-side lease-administration structures.
- vs **Tenant / Resident Portal** (unprocessed sibling): the portal is the tenant-facing surface of a management system (announcements, documents, requests); this Type's tenant surface is payment-focused. Inside PM stacks the payment platform is typically reached through the portal — surface vs money-machinery layering.
- vs **Billing Platform / Invoicing Application / Accounts Receivable Management**: domain-agnostic money machinery; the rent charge's meaning comes from the tenancy (tenant × unit × portfolio) and its controls encode landlord-tenant practice (late fees, partial-payment legal posture). A billing tool can be configured to look like this; the market ships a dedicated Type because the tenancy substrate and the payment-control surface are the product.
- vs **Peer-to-peer Payment Application**: structurally decisive — P2P apps move money between individuals with no charge/balance structure, no arrears, no late fees, no receipts against a lease, no portfolio view, no landlord privacy layer. Two sampled vendors publish dedicated comparison pages making exactly this contrast (Azibo vs Venmo; PayRent's ranked list). Market-articulated boundary, not just analyst-drawn.
- vs **Security Deposit Management** (unprocessed sibling): deposits are trust-held/escrow-governed and refunded at end of tenancy; in this Type a deposit is at most another chargeable item (RentRedi's separate deposit payment account shows the accounting seam).
- vs **HOA / Community Association Management**: member assessments vs rent under a rental agreement; RentPayment serving HOA is a vertical extension of one vendor.
- vs **Short-term Rental Management**: transient nightly bookings vs periodic tenancies; different charge shape (per-stay vs per-period) and different relationship duration.
- vs **Mortgage Servicing / borrower-payment surfaces** (neighboring family): the "recurring obligation + payment + status" shape is shared, but the relationship is a loan against property, not a tenancy; no unit/lease/portfolio context, no landlord-tenant controls.
- Suite-bundling seam: standalone collection platforms exist because the money-in slice alone serves small landlords; when a product centers leasing/maintenance/accounting, it belongs to the PM-suite Types even if it bundles collection.

## Uncertainties

- Avail and TurboTenant (both major free-DIY players) were unreachable; the listings-led and free-platform philosophies are represented only by Azibo's free posture. If those help centers become reachable, expect no structural change but more charge-schedule detail.
- Help-center article bodies were not fetched (RentRedi tree at title level only); status vocabularies (scheduled/processing/deposited/overdue etc.) are known to vary and exact names were deliberately not asserted.
- Payout windows: vendor-stated figures (RentRedi "2–3 business days" FAQ; Azibo "as fast as 2 business days") are marketing-level; the final document only claims "a few business days, varying by method and product."
- Whether partial-payment refusal or blocking is universal is unconfirmed (absent/not-surfaced at RentPayment's public pages); documented at 3/4 sampled products → written as common, not definitional.
- Enterprise resident-payments mechanics (concessions, resident wallets, integrated billing against PM charges) were only partially visible on public pages; kept at posture level.
- Rent amount currency/geography: the sample is US-centric (ACH, Section 8, 1099-K, credit bureaus); other markets' rails (SEPA, BACS, UPI-style) were not sampled — the final document keeps payment methods as examples, not invariants.

## Final Synthesis

The Rent Collection Platform is the money-in system for rental housing: it holds each tenancy's rent charges (amount, due date, recurrence) as tracked obligations, gives the tenant a payment channel through which rent is paid online (or recorded when paid outside), tracks every charge to a paid/unpaid/partial/overdue state on a running per-tenancy balance visible to both sides, and routes collected funds to the landlord's or manager's verified deposit account. Everything else — autopay, reminders, late fees, multiple rails, dashboards, credit reporting, controls like partial-payment blocking — is mature market structure layered on that spine; the standalone Type exists because the money-in slice alone serves a large market of independent landlords, while the same slice appears as a module inside property-management suites and as an enterprise payments layer on top of PM systems.
