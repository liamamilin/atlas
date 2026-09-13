# Research Notes — Mortgage Borrower Portal

## Research Goal

Understand what borrower-facing software for residential mortgage loans actually is: who operates it, who uses it, what objects exist inside it, what borrowers can see and do, how the surface behaves across the loan's life (application in flight → funded loan → payoff), how loan servicing transfers change it, and where its boundary runs against the generic customer portal, the staff-side mortgage origination/servicing systems, banking portals, and collections surfaces.

## Initial Boundary

Working hypothesis at start:

- This is the borrower-side self-service surface of the mortgage relationship — the "portal family" member for the mortgage domain (family shape established by the processed Customer Portal pass: identified customer + account space + self-service action; industry realizations held as their own Types).
- Likely two poles: a **servicing pole** (funded-loan account management: payments, escrow, statements, payoff, assistance) and an **origination pole** (in-flight application: status, document requests, e-signature). Both borrower-facing; the directory has no other leaf for the borrower-facing origination surface.
- Nearest neighbors: Mortgage Servicing Platform and Mortgage Origination Platform (both staff-side, both unprocessed at pass time), Customer Portal (generic family), Online Banking Portal (bank channel), Digital Collection Portal (delinquency business), Loan Management System (whose docs name the borrower portal as a companion surface).

## Research Questions

1. Who operates the surface — lender, servicer, subservicer, or a software vendor under white label? Who is the direct user?
2. What is the core object — the funded loan account, the in-flight application, or both?
3. What can borrowers see (balance, schedule, escrow, statements, tax forms, milestones)? What can they do (pay, autopay, upload documents, e-sign, apply for assistance, request payoff, update profile)?
4. What cannot be done self-service (the boundary of borrower power)?
5. How does the surface behave when the loan transfers between servicers? When the servicer is acquired?
6. What identity machinery gates it (registration, MFA, SSO, co-borrower accounts)?
7. Which capabilities are defining vs merely universal in the current US market (escrow, assistance, e-sign, paperless)?
8. Historical check: would early-web, IVR-era, and non-US or bank-embedded realizations satisfy the definition?

## Representative Products

| Product | Role in sample | Pole | Customer tier |
|---|---|---|---|
| PennyMac | Top-scale direct lender + servicer with a deep home-grown servicing portal and a separate application portal | servicing (+ origination portal) | national scale |
| Planet Home Lending | Lender/servicer whose borrower portal login points to a vendor's white-label servicing portal under Planet's brand | servicing, white-label | mid-size |
| Carrington Mortgage Services | Servicer with strong loan-transfer/onboarding posture; portal rebranded at servicer transfer; web + app + phone triad | servicing | national, non-prime heritage |
| Floify | Mortgage point-of-sale vendor; borrower-facing portal sold to lenders under the lender's brand (vendor pole, origination phase) | origination, vendor/white-label | small/mid lenders |

Context samples (boundary evidence, not full products): Mr. Cooper (sunset page after Rocket acquisition — portal retirement/redirect), Better Mortgage (lender that does not service most loans; "looking for your payment portal?" FAQ — portal follows the servicer of record).

## Sources

Research date: 2026-09-08. All Layer A below is official vendor web documentation fetched directly.

- PennyMac — homepage; "Manage Your Account" (https://www.pennymac.com/my-account); "Making Payments" (https://www.pennymac.com/my-account/making-payments); "Tax & Insurance Information" (https://www.pennymac.com/my-account/tax-and-insurance). [A]
- Floify Help Center — root; "Using Floify" collection (210 articles); "Portal Overview For Borrowers" (https://help.floify.com/en/articles/15141516); "Review My Milestone Updates" (https://help.floify.com/en/articles/15141148). [A]
- Planet Home Lending — homepage with Account Login URL (https://planethomelending.com/; login to loansphereservicingdigital.bkiconnect.com/planetservicing). [A, positioning level]
- Carrington Mortgage Services — homepage and top navigation (payment options, payoff statements, mortgage/disaster assistance, new-customer onboarding, transfer banner). [A, positioning level]
- Mr. Cooper — sunset/redirect page (mrcooper.com/help-center.html). [A]
- Better Mortgage — FAQ index and "Looking for your payment portal?" (https://better.com/faq/loan-servicing/looking-for-your-payment-portal; body JS-blocked, only page structure read). [A, limited]

Source-access limitations: Rocket Mortgage (rocketmortgage.com/help → 500; rocket.com/help → 403), LoanCare (403), Freedom Mortgage (403), Guild Mortgage (403), Lakeview (403), SPS (timeout), ICE Mortgage Technology product pages (404 ×2). No claims are made about those products. Portal interiors (post-login dashboards) were not directly observable for any product — all in-portal capability claims rest on the operator's own public descriptions of what the account provides.

## Product Observations

### PennyMac (servicing pole, deep) [A]

- **Two separate borrower-facing portals on one site**: "Manage my existing loan" (log in / register) vs "Apply for a new loan" — "Log in to my application", "Register", Application Center ("My Home By Pennymac will guide you through each step of the application process"). The split application-vs-loan structure is explicit.
- **Online account capability list** (operator's own enumeration of what the account provides): make a one-time payment; set up AutoPay; manage pending payments; go paperless and access statements; view documents; track loan activity; get eDisbursement refunds; check current loan balance; calculate amortization; send secure messages; manage escrow, tax and insurance payments; update email address; update mailing address. 24/7 from computer/tablet/smartphone; mobile app distributed via app stores.
- **Payments**: AutoPay enrollment (bank account + routing number, choose the date); one-time payment from checking/savings via browser or mobile app; pay by mail (three lockbox addresses + overnight address, loan number required, payment coupon mention for transferred loans); automated pay-by-phone (IVR one-time payment from checking/savings); Western Union Quick Collect. "State restrictions may apply" on online payments.
- **Payoff is gated separately**: "This page is for making monthly payments. Your specific payoff information and instructions are available by logging in." Payoff is a distinct in-portal object, not public content.
- **Escrow/tax/insurance machinery**: in-portal navigation "Escrow, Homeowner's/Hazard Insurance(s), and Responsible Party" and "Escrow, Taxes, and Responsible Party" — who pays what is answerable in-portal. Annual proof-of-coverage requests; supplemental/interim/new-construction one-time tax bills handled by sending a copy via in-portal Secure Message (or fax/phone/mail); after escrow disbursement "we will reanalyze your escrow account. If a shortage exists, your monthly payment will be adjusted to cover the difference." Mortgagee clause and insurance-verification companion site for uploading declarations; insurance-claim check negotiation companion site.
- **Assistance**: dedicated "Payment Assistance" / "Mortgage Relief and Disaster Assistance" program area ("several mortgage relief programs... keeping customers in their homes"); scam-protection rules: no fees for modification or loss-mitigation plans, no Money-Gram payments, funds always payable to the servicer.
- **Servicing-side business**: subservicing arm marketed to banks/CUs/IMBs ("brand-safe borrower experiences") — the portal is part of what a subservicer sells.
- Phone/IVR as a parallel self-service channel with the same facts (balance, last payment, next due, payment amount, year-end tax and insurance information).

### Floify (origination pole, vendor white-label) [A]

- The borrower portal is documented from the borrower's side inside the vendor's help center: "Using your secure portal, you can complete a loan application, make adjustments to your account, and view and respond to requests for documentation from your lender."
- Access via "your specific lender's site" → Login — the lender's brand/domain; vendor configuration includes company subdomain, white label, borrower-facing flow labels, color scheme. Borrower MFA and SSO exist; session inactivity timeouts configurable; audit logs on the lender side.
- **Loan flow** is the unit: multiple loans per borrower account ("If you have multiple loans with your lender(s), you will need to select the loan flow"); each flow shows date started, property address, deadline, required/outstanding items.
- **Document-request loop with a three-state lifecycle**: Docs Owed (requested, awaiting borrower action) → Docs Pending Review (uploaded, awaiting lender review) → Docs Accepted. Categories organize requests (e.g., Assets, Income, Misc). Upload with title + optional message; "Add New Doc" for unrequested documents; borrower can declare a request Not Applicable with a reason, which "will be sent to your lender for further review." Lender side can accept or reject documents; conditions can sync from the LOS into document requests; auto-approval rules exist.
- **Milestones**: lender-defined progress stages rendered as checkmark bubbles with completion dates; email/text notifications on completion; milestone sets configurable per company; milestones sync with the LOS. Realtor/partner portals can view a borrower's milestone updates (third-party visibility variant).
- **Application completion and signing**: complete/edit the loan application (1003); e-consent and credit-check authorization flows; borrower disclosure signing process; e-sign requests (native or DocuSign); viewing closing documents.
- **Account self-service**: edit profile (name, email, mobile, timezone), reset password, manage email/text notification preferences, switch between borrower and co-borrower accounts, delete own account, lender-branded progressive web app.
- AI-era features (Co-Pilot application editing, AI autofill) exist but sit on top of the request/milestone/document core.

### Planet Home Lending (servicing pole, white-label vendor portal) [A, positioning]

- The site's "Account Login" button does not lead to a Planet-built app: it points to a vendor-hosted borrower servicing portal (`loansphereservicingdigital.bkiconnect.com/planetservicing`) rendered under Planet's brand. The borrower portal market includes vendor white-label portals embedded in the servicer's own site.
- "Transferred to Planet? Start here" loan-transfer onboarding page; Existing Customers area (Make a Payment, Access My Existing Loan, Homeowners Assistance, FAQ, printable forms, concerns form).

### Carrington Mortgage Services (servicing pole, transfer posture) [A, positioning]

- Transfer banner for acquired portfolios: previously-Valon borrowers "sign in at myloan.servicedbycarrington.com to access your account. Your account experience remains the same, now with Carrington branding." The borrower portal changes operator/brand at servicing transfer while continuity of experience is maintained.
- Top navigation "Manage My Mortgage": Payment Options, Payoff Statements, Schedule of Fees, Mortgage Assistance, Disaster Assistance, plus "New to Carrington onboarding" for transferred loans.
- Self-service resource triad: paperless statements, auto-pay, email/text alerts; holiday banner lists three access channels — website, mobile app ("make payments with the swipe of a finger, gain access to important documents"), automated phone payment system.

### Mr. Cooper (context: servicer absorption) [A]

- mrcooper.com retired after the Rocket acquisition: "The Mr. Cooper site and app are no longer available. Sign in or create a Rocket account to manage your loan going forward"; "Your loan number and payment details stayed the same"; tax documents (1098) accessed "through your Rocket account." Portal identity follows the servicer entity; the account (not the portal) is the continuity anchor.

### Better Mortgage (context: lender that does not service) [A, limited]

- FAQ index carries a dedicated servicing question, "Looking for your payment portal?", under Loan Servicing, beside "How will my loan be serviced after closing?" and "What is the role of a servicer, and what is a subservicer?" — i.e., a lender whose loans move to external servicers must tell borrowers where their payment portal now lives. The portal belongs to the servicer of record, not the originator brand. (Body JS-blocked; only structure observed — no portal claims made.)

## Cross-product Comparison

| Dimension | PennyMac | Floify (via lender) | Planet | Carrington |
|---|---|---|---|---|
| Operator of the surface | servicer/lender itself | software vendor, lender-branded | vendor white-label under servicer brand | servicer itself (rebranded at transfer) |
| Direct user | borrower (person) | borrower + co-borrower | borrower | borrower |
| Phase | servicing + separate application portal | origination (application in flight) | servicing | servicing |
| Core object presented | funded loan account (+ escrow, documents) | loan flow (application: requests, milestones, deadline) | loan account (via vendor portal) | loan account (payments, payoff, fees) |
| Borrower actions observed | pay (one-time/AutoPay), escrow/tax/insurance management, secure messages, profile updates, paperless, statements/documents | complete application, upload/respond to document requests, N-A declaration, e-sign, e-consent, profile/notifications | account access, payment (via "Make a Payment" surface) | payments, paperless, auto-pay, alerts, payoff statements, assistance entry |
| Documents | statements, tax/insurance info, view documents | requests + uploads + acceptance states + closing docs | (vendor portal) | "important documents" via app |
| Notification machinery | paperless + notifications | email/text on milestones, configurable | alerts (Carrington analog: email/text) | email/text alerts |
| Identity | register/login, secure messages in-portal | borrower login, MFA, SSO, co-borrower switch | vendor portal login | portal login; IVR as parallel channel |
| Assistance/loss mitigation | dedicated relief & assistance area | n/a (origination phase) | Homeowners Assistance area | Mortgage + Disaster Assistance areas |

Layer-B cross-product commonalities (observed across ≥2 sampled products):

- Authenticated borrower self-service surface operated by (or branded for) the servicer/lender of record — all five.
- The borrower's own loan as the standing scoped object; multiple loans per account supported where documented (PennyMac implied by account, Floify explicit loan-flow list).
- Payment self-service in the servicing pole (PennyMac, Carrington, Planet's "Make a Payment"); document-request/response machinery in the origination pole (Floify).
- Statements/documents delivery through the surface (PennyMac, Carrington, Floify).
- Onboarding of transferred loans as a first-class flow (Planet, Carrington; corroborated by Better's FAQ topic and Mr. Cooper's migration page).
- Parallel assisted channels (phone/IVR, secure messages) alongside the portal (PennyMac, Carrington).
- Paperless + alert preferences as a standard layer (PennyMac, Carrington, Floify notifications).

## Canonical Model (four layers)

### L0 — Defining Invariant

Three jointly-held structures:

1. **Borrower-operated, operator-run surface.** The mortgage servicer or lender operates an authenticated self-service surface whose direct user is the borrower — an external customer, never staff. (remove → staff-side servicing/origination systems, or a marketing site)
2. **The borrower's own mortgage position as a standing, scoped account space.** A persistent per-borrower window onto their own mortgage relationship — a funded loan account (balance and payment standing at minimum) and/or an in-flight application — scoped so a borrower sees their own position, persisting across sessions and following the loan's life. (remove → one-off payment page or a statement mailer; the standing window is gone)
3. **Self-service action that lands in the operator's systems.** The borrower performs enabled actions on their own position — payments against the loan in the servicing pole; application tasks and document responses in the origination pole — and what they do posts to the operator's servicing/origination records. (remove → read-only lookup, the self-service is gone)

Jointly-held is load-bearing: 1 alone = staff system or marketing site; 2 alone = document archive; 3 without 1+2 = anonymous payment gateway; 1+2 without 3 = read-only statement site (the thin pole below the full Type); 1+3 without 2 = payment page with no account.

The mortgage-domain object is load-bearing for the leaf: the position is a mortgage loan (escrow/tax/insurance machinery, payoff, assistance) or a mortgage application. Remove the domain object and the surface collapses into the generic Customer Portal family shape.

Historical/§24 check: the early-web "account access" page (view balance, make a payment, view statements) and IVR phone self-service satisfy the core — no autopay, paperless, apps, escrow tools, or assistance centers are definitional. Pre-web servicing (coupon books, mailed statements, phone calls) is the pre-history that fails the borrower-operated-surface leg — correctly, since the Type *is* the digitization of borrower self-service. Bank-embedded realizations (a bank serving its own mortgage borrowers from within its banking channel) satisfy the core when the loan account space and loan actions are present.

### L1 — Common Mature Structure

Present across the sample; not definitional:

- **Payment machinery depth**: one-time + recurring (AutoPay) + pending-payment management; bank-account funding; mobile-app payment.
- **Statements, notices, and tax documents** delivered through the surface; paperless election.
- **Escrow, tax, and insurance management** (servicing pole): responsible-party visibility, proof-of-insurance submission, escrow analysis/shortage adjustment communication. The signature machinery of mortgage servicing, but escrow-waived loans and origination-phase portals exist without it.
- **Payoff information as a distinct gated object** (servicing pole).
- **Assistance/loss-mitigation entry** (servicing pole): relief/assistance program areas and application entry points.
- **Document-request workflow with review states** (origination pole): owed → pending review → accepted; categories; not-applicable declarations.
- **Milestone/progress presentation** (origination pole): lender-defined stages with completion dates and notifications.
- **E-consent, credit authorization, and e-signature** (origination pole).
- **Secure messaging** between borrower and servicer/lender.
- **Profile and preference self-service**: contact details, notification/alert preferences, password/MFA.
- **Co-borrower accounts** and multiple-loan accounts.
- **Loan-transfer onboarding** of newly transferred borrowers.
- **Mobile app** as a companion form factor; **IVR/phone self-service** as a parallel channel.

### L2 — Variant / Optional

- Phase mix: servicing-only portal vs origination-only portal vs both on one operator's site (separate portals, as observed at PennyMac, or one continuum).
- Portal provenance: operator-built vs vendor white-label embedded under the servicer's brand (both observed).
- Form factor emphasis: web-first, app-led, PWA-installed, IVR-parallel.
- Identity substrate: email+password registration, MFA, SSO, co-borrower switching.
- Regulatory-posture packaging by market/regime (US-centered sample: escrow analysis conventions, tax-form delivery, assistance program framing; the abstract core does not depend on any single regime).
- Adjacent commerce/ecosystem tie-ins from the portal login (home search, insurance, agent matching) — affiliate extensions, not portal substance.

### L3 — Vendor-specific (Research Notes only)

- PennyMac: "My Home by Pennymac" application center; three lockbox payment addresses + overnight address; Western Union Quick Collect; mycoverageinfo.com proof-of-insurance companion; insuranceclaimcheck.com claim-check negotiation; eDisbursement refunds; specific IVR phone number; "state restrictions may apply" on online payments; scam-protection wording.
- Floify: up-to-10-documents-per-request limit; Co-Pilot AI editing; Dynamic AI Autofill; company milestones vs team milestones; MISMO 3.4 export; Encompass conditions→requests sync; Disclosures Desk; realtor/partner co-branded portals; PWA download.
- Planet: login URL to a vendor-hosted servicing digital portal (bkiconnect Servicing Digital class) under Planet's brand; loan-transfer landing page; Everest-hosted concerns form.
- Carrington: myloan.servicedbycarrington.com transfer-rebrand URL; Vylla Home affiliate SSO from portal login; specific fee schedule page; app store apps.
- Mr. Cooper: retirement page with Rocket-account migration and 1098 access through the successor's account.

## Vendor-specific Findings

See L3. None of these carry into the final document beyond neutral, operator-abstracted descriptions.

## Rejected Findings

- "Borrower portal = part of the Mortgage Servicing Platform" — rejected as a definitional claim: the servicing pole's portal is a companion surface, but origination-phase borrower portals exist whose operator side is an origination platform, and vendor white-label borrower portals are sold standalone. The portal is its own surface Type spanning both phases.
- "Escrow management defines the Type" — rejected: escrow-waived loans and application-phase portals satisfy the Type without any escrow machinery; escrow is signature servicing capability, not the invariant.
- "The portal belongs to the original lender" — rejected by evidence: the surface follows the servicer of record (transfer rebranding, retirement migration, lender-that-doesn't-service FAQ).
- "Assistance application is definitional" — rejected: present in servicing poles as program areas, absent in the origination pole; a paid-current loan's portal need not carry it.

## Boundary Findings

| Neighboring Type | Relationship | Distinction / seam |
|---|---|---|
| Customer Portal (processed) | family vs domain instance | family shape (identified customer + account space + self-service action) is shared; this leaf carries the mortgage-domain object — loan account with payment/escrow/payoff/assistance machinery and application-phase request/milestone machinery — plus the servicing-of-record posture. Swap the domain object out → generic customer portal |
| Mortgage Servicing Platform (unprocessed sibling) | other side of the same records | staff-side system of record running the servicing loop vs borrower-facing surface presenting and accepting actions on that record. Loan-management-system pass already holds "borrower self-service portal" as a companion surface of the servicing engine. Packaging overlap: servicing platforms often bundle a borrower portal — packaging, not identity. Recommend cross-reference when that leaf is processed |
| Mortgage Origination Platform (unprocessed sibling) | other side of the same case | staff-side origination pipeline vs borrower-facing application surface feeding it (LOS pass holds "borrower self-service" as an intake channel). Same keep-both seam |
| Loan Origination System (processed) | consumes the surface's intake | LOS documents borrower self-service as one intake channel; this leaf owns the channel itself |
| Online Banking Portal / Mobile Banking (processed) | channel-scope seam | bank channel over the customer's whole account set vs loan-centered surface over the mortgage position, often operated by a servicer that is not the borrower's bank. Bank-serviced loans inside a banking portal satisfy this Type's core only insofar as a loan account space + loan actions exist |
| Digital Collection Portal (processed family) | delinquency business vs standing relationship | collection machinery centers arrears pursuit; the borrower portal serves the standing loan including hardship entry pre-delinquency. Assistance flows inside the servicing portal are its hardship extension, not a collections operation |
| Investor Portal (processed) | family member, different external party | investors in private vehicles vs mortgage borrowers; operator is sponsor/administrator vs servicer/lender |
| Tenant/Resident Portal | family member, different domain object | lease/rent machinery vs mortgage loan machinery |

## Uncertainties

- Portal interiors (post-login dashboards) were not directly observable; in-portal capability sets rest on operators' own public descriptions. In-portal layouts, exact section names, and limits are not asserted.
- Non-US markets were not sampled; regional realizations (e.g., UK/EU servicer portals, regime-specific tax-form machinery) are inferred from the abstract core, not observed. Evidence reduced accordingly in the final document.
- Bank-embedded realizations (bank serving its own loans inside its banking channel) were not directly sampled — bank sites were unreachable; the boundary statement is reasoned from the processed banking-portal pass and this pass's core, not from a fetched bank example.
- The origination pole's strongest documentation comes from one vendor (Floify); other POS vendors (Blend, ICE Consumer Connect, nCino Mortgage) were unreachable. The origination-phase shape is asserted at cross-product strength only for the request/milestone/document pattern, which is standard industry vocabulary, but the pass holds its universality at "common in the documented sample" strength.
- Whether the directory ultimately prefers one mortgage-family leaf spanning borrower self-service vs separate leaves per phase cannot be decided in this pass; the evidence supports one Type with two phase poles (both shapes are marketed under "borrower portal"), recorded for joint review.

## Final Synthesis

A Mortgage Borrower Portal is the mortgage servicer's or lender's borrower-operated self-service surface over the borrower's own mortgage position. Its defining core is three jointly-held structures: an operator-run authenticated surface whose direct user is the borrower; a persistent, borrower-scoped account space presenting the borrower's own mortgage position (funded loan — balance and payment standing — and/or in-flight application); and borrower-initiated actions that land in the operator's servicing or origination systems. The Type spans two phase poles — servicing (payments, escrow/tax/insurance, statements and tax documents, payoff, assistance) and origination (application completion, document requests with review states, milestones, e-consent and e-signing) — realized by operator-built portals and by vendor white-label portals under the servicer's brand. The surface follows the servicer of record: transfers rebrand it, acquisitions migrate it, and lenders that do not service must point their borrowers to whoever holds the portal. Escrow management, assistance programs, paperless, mobile apps, and AI helpers are the era's standard layers, not the definition.
