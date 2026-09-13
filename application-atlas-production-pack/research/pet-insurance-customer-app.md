# Research Notes — Pet Insurance Customer App

Directory location: §29 Home, Family, Personal & Local Services (siblings: Pet Health Application, Pet DNA Analysis Platform, pet-care operator siblings; distant neighbors in §08: Insurance Claims Management, Insurance Policy Administration System, Insurance Quote Platform, Insurance Marketplace)
Research date: 2026-09-09
Slug: pet-insurance-customer-app

---

## Research Goal

Understand what a "Pet Insurance Customer App" actually is as an Application Type: who operates it, what objects exist inside it, how the policyholder's insurance relationship is represented, how a veterinary bill becomes a claim and then money, what the customer can self-serve, and where the boundary sits against operator-side insurance Types (Claims Management, Policy Administration), purchase-side Types (Quote Platform, Marketplace), and the pet-consumer sibling Pet Health Application.

## Initial Boundary

Working hypothesis at Understand step:

1. Core use: the policyholder-facing application of a pet insurance provider (carrier, agency brand, or broker). The customer manages the policy covering their pet(s), files claims for veterinary bills, tracks claims to a money outcome, and self-serves policy administration.
2. Primary users: pet owners / policyholders (consumers). The veterinary clinic is an external party inside the claim loop (may submit the claim, may receive direct payment) but is not the app's user.
3. Nearest neighbors: Insurance Claims Management (operator side of the same claim object), Insurance Policy Administration System (insurer-side policy lifecycle), Insurance Quote Platform / Insurance Marketplace (purchase side), Pet Health Application (shared pet-profile vocabulary, no insurance relationship), Mobile Banking Application (structural rhyme: consumer app of a financial institution).
4. Likely confusions: is this just a generic customer portal? Is it a Pet Health App with insurance bolted on? Is quote/purchase part of the Type? The center of gravity should decide.
5. Unknowns: claim submission mechanics per product, direct-vet-payment vs reimbursement models, pre-authorisation spread, waiting-period/coverage visibility, policy self-service depth, records storage role.

## Research Questions

1. What is the unit of record — the policy, the pet, the claim, the account?
2. What does a claim consist of, and how does it move from vet bill to money?
3. Who can submit a claim (customer only, or vet on customer's behalf), and through which channels?
4. How does the app expose coverage (limits, excess/deductible, reimbursement %, waiting periods, exclusions)?
5. What money paths exist (reimbursement to customer, direct vet payment, advance-before-payment)?
6. What policy administration is self-service (details, payment, documents, renewal, cancellation)?
7. What pet-level records exist and how do they relate to claims?
8. Which structures are definitional vs common-mature vs variant vs vendor-specific?
9. Does the paper-era lineage (policy document + claim form + vet invoice + reimbursement cheque) satisfy the same structures?

## Representative Products

Selection logic: market representation + documentation depth + different product philosophies + different customer tiers + geographic spread.

1. **Figo Pet Insurance** (US; underwritten by Independence American Insurance Company; Figo Pet Insurance LLC is a licensed agency) — app-first philosophy: "Pet Cloud" app bundles insurance with records, telehealth, social, and lifestyle discovery. Tier-2 root + dedicated Pet Cloud product page.
2. **ManyPets** (UK/US/Sweden; FCA-regulated) — account-centric philosophy: "My Account" web self-service plus a vet-facing Vet Portal as the recommended claim channel; explicitly no pre-authorisation; explicitly no paper forms. Tier-2 root + Tier-1 how-to-claim + Tier-1 existing-customers pages.
3. **Pumpkin** (US; underwritten by IAIC or United States Fire Insurance Company; Pumpkin Insurance Services Inc. is a licensed agency) — pay-before-you-pay philosophy: PumpkinNow urgent-pay service deposits covered claim amounts before the customer pays the vet. Member portal + vet portal. Tier-2 root + Tier-2 claims overview page.
4. **Animal Friends** (UK; FCA-regulated, founded 1998, charity-donation model) — traditional multi-channel philosophy: vet portal (Pawtal) + customer online account + paper claim forms as a first-class channel; pre-authorisation offered; multi-species (dog/cat/horse). Tier-2 root + Tier-1 claims page.

Unreachable (recorded per network rules; no claims drawn from them):
- Trupanion (trupanion.com/en-us/help-center 403; help.trupanion.com 403) — direct-vet-pay philosophy unsampled directly.
- Lemonade (lemonade.com/pet-insurance 403; support.lemonade.com transport error) — AI-instant-claims philosophy unsampled directly.
- Healthy Paws (root + /Claims 403 ×2), Embrace (403), Pets Best (403), ASPCA Pet Insurance (403), Petplan UK (403).
- agria.co.uk resolved to Agria-Werke GmbH (German agricultural machinery maker — same name, different industry); the pet insurer Agria was not fetched.

## Sources

Figo (Tier-2 unless noted):
- https://figopetinsurance.com/ (root; claims positioning, Powerups optional coverage, Live Vet, curable pre-existing rule, underwriting disclosure)
- https://figopetinsurance.com/pet-cloud/ (Pet Cloud app page; claims tracking, digital records, to-dos, live vet, connect/explore, pet tag, claims assistant, mypetcloud.com login, "Live Vet and the Figo Pet Cloud are separate non-insurance services" disclosure)

ManyPets (Tier-1 where noted):
- https://www.manypets.com/ (UK root; plans, excess/co-pay, MoneyBack, Perks, My Account framing, video vet, FAQ with waiting periods and quote data)
- https://www.manypets.com/uk/how-to-claim/ (Tier-1: claim channels, vet portal flow, invoice requirements, direct vet payment, claim window, waiting periods, continuation claims, no pre-auth, no paper forms)
- https://www.manypets.com/uk/existing-customers/ (Tier-1: My Account capability list — pet details, address, contact, payments, documents, renewal info, excess/co-pay adjustment, cancellation; handbooks/IPID; perks; refer-a-friend; video vet)

Pumpkin (Tier-2):
- https://pumpkin.care/ (root; plan structure, reimbursement/deductible/limit model, waiting period, pre-existing rule, no-networks claim, wellness products, underwriting disclosure)
- https://www.pumpkin.care/claims (claims overview; 3-step claim flow; PumpkinNow mechanics incl. "final invoice before payment" and $500+ threshold; member account setup for records + direct deposit)

Animal Friends (Tier-2 root + Tier-1 claims page):
- https://www.animalfriends.co.uk/ (root; policy types, vet fee cover range, excess options, senior co-pay, waiting periods, direct vet payment, Joii video vet, online account, Treat Tin)
- https://www.animalfriends.co.uk/existing-customers/claims/ (Tier-1: claim scenarios per species; Pawtal vet channel; online account channel; paper claim form channel with postal address; repeat medication claims; pre-authorisation mechanics and targets; claim status notifications; co-payment mechanics)

Research limitations:
- No authenticated in-app screens observed; all interface claims come from official descriptive surfaces (product pages, how-to pages, FAQs), not from operating the products.
- Trupanion (direct-vet-pay-by-default model) and Lemonade (AI-instant claims) unreachable; their philosophies are represented only indirectly (direct vet payment evidenced at ManyPets + Animal Friends; fast-claims positioning at Figo/Pumpkin).
- Exact in-app claim state names not observed; claim states are described conceptually.
- Numeric specifics quoted below (waiting periods, thresholds, processing targets) are product-specific vendor statements, not cross-product norms.

---

## Product A — Figo Pet Insurance (US)

### Key observations (Evidence layer A unless noted)

- **Surface structure**: "Pet Cloud" is the customer app (mobile app + web login at mypetcloud.com). Positioned as "The ultimate pet parent toolkit" — "Your pet's life, all in one place. From insurance to play dates and everything in between."
- **Claims (Tier-2, vendor aggregate)**: "Lightning-fast claims… easy-to-use mobile claims process… on average, most claims close in just 3 working days*… keep track of where your claim is in the process" (*Figo Claims Data, 2025 — vendor-reported aggregate, treat as vendor claim). A "Claims Assistant" (named Evie) "walks you through the process."
- **Records**: "Digital Records — Don't lose track of what's important. Vet records and more, all in one spot!"
- **Reminders**: "Pet To-Do's — with reminders, we let you know when the important 'pet stuff' is due."
- **Telehealth**: "Live-Vet 24/7 — chat with licensed veterinary pros, right from the app"; "Included with every insurance policy… direct access to a licensed veterinary professional via text." Legal footer: "Live Vet and the Figo Pet Cloud are separate non-insurance services unaffiliated with IAIC."
- **Lifestyle wrapper**: Connect ("find your pack… share photos, plan play dates"), Explore (pet-friendly places/services directory: Pet Perks, Day Care, Restaurants, Dog Walking, Dog Grooming), Pet Tag (lost-pet reunification tag), Achievements (gamification).
- **Coverage structure (root page)**: plans with reimbursement rates and payout limits; "Coverage for Curable Pre-Existing Conditions — we may cover pre-existing conditions considered curable if they show no signs or symptoms within 12 months of last treatment"; optional "Powerups" (Wellness; Vet Exam Fees for accident/illness visits).
- **Legal structure**: policies underwritten by Independence American Insurance Company; Figo Pet Insurance LLC is a licensed insurance agency; Pet Cloud services supported by Figo. Brand ≠ underwriter.
- **Testimonial (not operational fact)**: "submit this claim in less than two minutes… processed in less than 24 hours."

### Interpretation

Figo shows the maximal "app is bigger than insurance" pattern: the insurance core (claims + policy) sits inside a pet-life super-app. The insurance relationship is still the anchor (claims tracking is the headline feature; the app is gated by policy ownership for insurance features), but the surface drifts toward Pet Health Application + lifestyle territory. This is the key drift-risk sample for the boundary.

## Product B — ManyPets (UK/US/SE)

### Key observations (Evidence layer A; how-to-claim and existing-customers pages are Tier-1)

- **Surface structure**: "My Account" (web login) — "Manage your plan easily… Easy-to-use features, Make changes whenever it suits you, 24/7 access anytime, anywhere." Separate vet-facing "ManyPets Vet Portal" (manyvets.com).
- **Claim channels (Tier-1)**: four — (1) vet submits via Vet Portal ("the quickest and easiest is through your vet… Vets can manage every step"); (2) customer submits via My Account; (3) phone; (4) email. "We don't make you do paper forms."
- **Claim content (Tier-1)**: customer-submitted claims need "as a minimum… a paid, itemised invoice"; optionally "relevant correspondence or health history from your vet." Multi-vet claims: "you can add multiple vets to one claim… You'll need the invoice for every vet involved."
- **Claim tracking (Tier-1)**: "Follow your claim in My Account — log in to My Account to track every step of your claim. We'll update you when something's changed." A "Claim dashboard" exists; vet-submitted claims appear there (may take a day or two).
- **Direct vet payment (Tier-1)**: "Your vet can select themselves as the payee when submitting a claim, so we can pay them directly if your claim is approved." Customer-submitted claims can also "select your Vet as the Payee… up to two different vets"; referral-vet case handled via comments. Duplicate-claim warning: don't submit both vet and self.
- **Vet visibility (Tier-1)**: "Your vet can view everything about your plan through the ManyPets Vet Portal… like your vet fee limit or excess."
- **Claim window (Tier-1, product-specific)**: "You have six months from each treatment or service date to make a claim… We can't pay any claims submitted later."
- **Waiting periods (Tier-1, product-specific)**: no payment for accidents in first 48 hours; no payment for illnesses/behavioural conditions in first 14 days; waiting periods apply at first purchase, not renewal. Switchers with continuous prior cover can claim straight away with evidence.
- **Continuation claims (Tier-1)**: ongoing conditions can be claimed per treatment or as one large claim; "select which claim it relates to"; itemised invoice per treatment.
- **Pre-authorisation (Tier-1)**: "We don't offer pre-authorisation, but it's something we're looking into." — proves pre-auth is NOT definitional.
- **My Account self-service (Tier-1)**: update pet details (e.g., spay/neuter status), change address, update contact details, review/manage payments (payment details + upcoming payment dates), access documents (view/download insurance documents), check renewal information (review changes in advance), adjust co-pay & excess at renewal, cancel plan.
- **Documents**: handbooks + IPIDs downloadable (hosted on account.eu.policies.io infrastructure).
- **Coverage structure (root, product-specific)**: lifetime plans with annual vet-fee-limit refresh; excess once per policy year (not per condition); 20% co-payment from age 7 at renewal; pre-existing condition rules (2-year lookback standard; 3-month variant plan); MoneyBack (20% premium back if claim-free year); Perks discounts; unlimited 24/7 video vet calls ("no excess to pay for using the video vet service"); refer-a-friend with 60-day qualification.
- **Claims stat (vendor claim)**: "We pay 97% of claims."

### Interpretation

ManyPets is the cleanest account-centric sample: the customer surface is a self-service account organized around plan + claims + documents + payments, with the vet portal as the recommended claim rail. It also proves two negative invariants: no pre-auth (still in-type) and no paper forms (still in-type) — so neither is definitional.

## Product C — Pumpkin (US)

### Key observations (Evidence layer A; claims page Tier-2 but operationally specific)

- **Surface structure**: member portal (member.pumpkin.care; "Log in", "Submit a Claim" links into it). Separate Vet Portal (portal.pumpkin.care).
- **Claim flow (claims page)**: "Go to the vet (any licensed vet in the US or Canada) → Submit a claim (complete the claim form with your visit details and upload the itemized invoice) → Get paid quickly (a few days — or in just minutes with PumpkinNow)."
- **PumpkinNow (product-specific)**: "urgent pay service that expedites eligible claims for $500+ vet care… up to 90% of eligible expenses paid in 15 minutes, so you have the funds to pay at checkout." Mechanics: "Ask your vet for a final invoice. Note: an invoice can be 'final' after treatment, even if it's before you pay the bill. Submit your claim as usual selecting 'get payment for treatment received' and attach the final invoice. If $500+ and eligible, we'll process the claim and deposit the covered amount to your account before checkout." — the claim can be paid to the customer BEFORE the customer pays the vet.
- **Member account setup**: "Add your pet's medical records and set up direct deposit in your member account, so we can provide support, coverage clarity, and timely claim payments when care can't wait."
- **No networks (root FAQ)**: "there are no 'networks' of approved veterinary care providers… Pumpkin plans pay you back directly for all covered claims… any licensed veterinarian, specialist, emergency clinic, or hospital in the US or Canada."
- **Coverage structure (root, product-specific)**: 80%/90% reimbursement options; annual deductible; annual coverage limit $5k–unlimited; 14-day waiting period; pre-existing conditions excluded (curable ones covered again after 180 days symptom-free, except knee/hind-leg ligament conditions); dental illness, behavioural, hereditary, parasite, prescription food/supplements, alternative therapies, exam fees included without add-ons; 10% multi-pet discount.
- **Wellness split**: Preventive Essentials ("NOT INSURANCE… only available to pets who are also covered under a Pumpkin Insurance policy"); Pumpkin Wellness Club (standalone membership, separate LLC). Legal structure: agency (Pumpkin Insurance Services Inc.) + underwriters (IAIC / US Fire).
- **Testimonials (not operational facts)**: PumpkinNow "rushing funds into my account within (literal) minutes"; specific paid amounts displayed per story.

### Interpretation

Pumpkin is the money-path innovator: reimbursement-to-customer is the default, but the advance-before-payment path (PumpkinNow) inverts the usual "pay first, claim back" sequence. The claim object still anchors to an itemised/final invoice; the money path is the differentiator. Also the cleanest "no network" statement — any licensed vet.

## Product D — Animal Friends (UK)

### Key observations (Evidence layer A; claims page Tier-1)

- **Surface structure**: online account (hub.animalfriends.co.uk) — "An online account to help manage your policy and claims on the go." Separate vet-facing "Vets Pawtal."
- **Claim scenarios (Tier-1)**: structured by species (dog/cat/horse/rider) and event: vet fees, repeat medication, pre-authorisation, death of pet, holiday cancellation, missing/stolen pet, boarding fees (policyholder hospitalised 4+ consecutive days), overseas vet fees (EU, translated documents), road traffic accident (extra evidence requested: written description, photos of lead/collar/harness, fencing, witnesses, escape history), horse-specific (loss of use, saddlery/tack, trailer, rider injury, third-party property damage via phone).
- **Claim channels (Tier-1)**: (1) vet submits via Pawtal ("the free online claim system for vets… no paperwork required and claims can be dealt with much faster"); customer receives email confirming submission, condition, and amount claimed; (2) customer online account (used for repeat medication claims); (3) paper claim form — signed by policyholder, completed by vet with invoices + clinical history attached, sent by email or post. Paper remains a first-class channel.
- **Documentation requirement (Tier-1)**: "We'll need a copy of your pet's full veterinary history to review any claim."
- **Processing target (vendor claim, product-specific)**: "We will aim to process your claim within 2 working days."
- **Claim status (Tier-1)**: text confirmation of receipt (if mobile number provided), email for Pawtal submissions, status checkable in the online account, email when finalised.
- **Pre-authorisation (Tier-1, product-specific)**: via Pawtal, "pre-authorise any amount of treatment that would be required in a 24-hour period prior to it going ahead"; outcome target within 1 working hour (9am–4pm weekdays; else next working day); paper form route within 5 working days.
- **Co-payment mechanics (Tier-1, product-specific)**: fixed % of vet fees per claim (example: 20% of £200 = £40 paid by customer directly to the vet; insurer pays £160); co-payment does not reduce the vet fee limit; applies to all vet-fee claims including repeat medication; excess still applies.
- **Direct vet payment (root)**: "We are able to pay your vet directly when you claim. However, if your vet would rather you pay… you will need to pay your vet first and then submit your claim to us… we will pay you directly."
- **Coverage structure (root, product-specific)**: four UK policy types (Accident Only, Time Limited, Max Benefit, Lifetime); vet fee cover £1,000–£18,000; six excess options (£69–£299, customer-selectable; increase anytime, decrease only at renewal); 20% co-payment for senior pets (dog 8+/cat 10+); waiting periods (2 days accident, 14 days illness, 14 days cruciate); no pre-existing cover; complementary therapies vet-recommended; Joii free 24/7 video vet; Treat Tin discounts; refer-a-friend; horse insurance extends the species set.
- **Repeat medication claims (Tier-1)**: require a prior claim for the same condition; online account submission with invoices + prescription.

### Interpretation

Animal Friends is the traditional multi-channel pole: digital-first but with paper forms still first-class, pre-authorisation present, and the widest claim-scenario taxonomy (including non-vet-fee benefits: death, missing/stolen, holiday cancellation, boarding, third-party). It shows the claim object is not always a single vet invoice — benefit claims anchor to other evidence (purchase receipt + cause-of-death documentation, boarding receipts, holiday receipts).

---

## Cross-product Comparison

| Structure | Figo (US) | ManyPets (UK/US/SE) | Pumpkin (US) | Animal Friends (UK) |
|---|---|---|---|---|
| Customer surface | Pet Cloud app + web (mypetcloud.com) | My Account (web) | Member portal (member.pumpkin.care) | Online account (hub.animalfriends.co.uk) |
| Policy/coverage visible to customer | yes (insurance inside app) | yes (plan, documents, renewal info) | yes (member account) | yes (policy schedule, documents) |
| Claim anchored to vet invoice | yes (mobile claims) | yes (paid itemised invoice minimum) | yes (itemized invoice; "final invoice" variant) | yes (invoices + full veterinary history) |
| Claim tracking visible to customer | yes ("keep track of where your claim is") | yes (Claim dashboard; change updates) | implied (portal) | yes (status in online account + notifications) |
| Customer self-submission | yes | yes | yes | yes (online for repeat meds; paper for others) |
| Vet-submitted claims | not observed | yes (Vet Portal, recommended) | vet portal exists (role unconfirmed) | yes (Pawtal, recommended) |
| Direct vet payment | not observed | yes (vet as payee, up to 2 vets) | no (pays customer; advance before checkout instead) | yes (direct vet payment) |
| Advance-before-payment | not observed | not observed | yes (PumpkinNow, $500+ eligible) | not observed |
| Pre-authorisation | not observed | no (explicitly not offered) | not observed | yes (Pawtal, 1-working-hour target) |
| Paper claim forms | no | no (explicitly none) | not observed | yes (first-class channel) |
| Waiting periods | curable pre-existing 12-month rule (root) | 48h accident / 14d illness | 14-day | 2d accident / 14d illness / 14d cruciate |
| Excess/deductible/co-pay | reimbursement % + limits (root) | excess once/year; co-pay at 7+ | deductible + 80/90% reimbursement | selectable excess; senior co-pay 20% |
| Medical records role | Digital Records in app | uploaded with claims | added to member account to speed claims | full history required for review |
| Telehealth/vet video | Live Vet 24/7 (non-insurance service) | unlimited 24/7 video vet | virtual exam fees covered (no telehealth line observed) | Joii 24/7 video vet |
| Multi-pet | multi-pet discount not observed | multi-pet insurance product | 10% multi-pet discount | per-pet policies (species pages) |
| Lifestyle/perks extras | Connect/Explore/Tag/Achievements | Perks, MoneyBack, refer-a-friend | Preventive Essentials, Wellness Club | Treat Tin, refer-a-friend, charity donations |
| Species | dog/cat | dog/cat | dog/cat | dog/cat/horse (+rider, tack) |
| Brand vs underwriter | agency + IAIC | FCA-regulated insurer group | agency + IAIC/US Fire | FCA-regulated insurer |

### What is shared (candidate common structure)

1. A personal authenticated customer surface (app or account portal) holding the insurance relationship for the customer's pet(s). (4/4)
2. The policy/coverage of record visible to the customer: what is covered, at what limits, with which documents. (4/4)
3. Claim filing anchored to a veterinary invoice (itemised; paid or "final"), with the pet's veterinary history as supporting evidence. (4/4)
4. The claim's progression to a money outcome: insurer assessment → decision → payment (to customer and/or vet). (4/4)
5. Customer-visible claim tracking. (4/4, though depth varies; Pumpkin's is implied by portal positioning)
6. Self-service policy administration: contact/address/payment details, documents, renewal, cancellation. (observed 3/4 explicitly: ManyPets, Animal Friends via account framing, Pumpkin via member account; Figo implied by app account)
7. Coverage-rule surfaces: waiting periods, excess/deductible/co-pay, exclusions (pre-existing), policy documents as authoritative terms. (4/4)
8. A vet-facing companion rail (vet portal / direct claims) or direct vet payment. (3/4 observed; Figo not observed)
9. Telehealth or vet-video line bundled or attached. (3/4 observed)
10. Perks/discounts/referral extras. (3/4 observed)

### What differs (variant axes)

- Money path: reimbursement-to-customer (all) vs direct vet payment (ManyPets, Animal Friends) vs advance-before-payment (Pumpkin).
- Claim submission rail: customer-first (Figo, Pumpkin) vs vet-first (ManyPets, Animal Friends).
- Pre-authorisation: present (Animal Friends) vs absent (ManyPets) — variant, not invariant.
- Paper channel: first-class (Animal Friends) vs eliminated (ManyPets) — variant/regional.
- Policy taxonomy: UK four types (Accident Only / Time Limited / Max Benefit / Lifetime) vs US accident-&-illness with deductible/reimbursement%/annual-limit knobs — regional.
- Species breadth: dog/cat vs +horse/rider/tack (Animal Friends) — variant.
- App ambition: insurance-only account (ManyPets, Animal Friends) vs pet-life super-app (Figo) vs money-path innovator (Pumpkin) — philosophy.
- Brand/underwriter split: agency brands riding licensed underwriters (Figo, Pumpkin) vs regulated insurer groups (ManyPets, Animal Friends) — market structure, not app structure.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The customer-facing application of a pet insurance relationship holds exactly three jointly-held structures:

1. **The insured pet's policy/coverage as the customer-visible record of the insurance relationship** — a personal authenticated account in which the pet's coverage (what is covered, at what limits, under which terms) is held and readable, with the policy documents as the authoritative statement. Remove → a pet profile app or a marketing site; the insurance relationship is gone.
2. **Claim filing anchored to a veterinary bill** — the customer (or their vet acting on the customer's behalf) submits a claim that binds a veterinary visit/treatment to the policy, with the itemised invoice as the anchor document and the pet's veterinary history as supporting evidence. Remove → an account portal with nothing to claim; the insurance promise is unexercisable.
3. **The claim-to-money loop** — the submitted claim is assessed by the insurer against the policy and resolves into a money outcome: payment to the customer (reimbursement or advance) and/or direct payment to the vet, with the customer able to follow the claim's progression. Remove → a one-way document drop box; the "insurance" is gone, only submission remains.

Jointly-held load-bearing analysis:
- 1 alone = pet profile / account site (Pet Health Application territory)
- 2 without 1 = anonymous claim form with nothing to claim against
- 3 without 1+2 = payment processing, not insurance
- 1+2 without 3 = submission drop box with no outcome
- 2+3 without 1 = claims against no policy of record

### Historical / market-sample check (§24)

Paper-era pet insurance (1970s–80s UK policies; VPI in the US from 1982): the owner held a policy document (the coverage of record), obtained a vet invoice, completed a paper claim form, posted it, and received a reimbursement cheque. All three L0 structures are present — policy of record, claim anchored to a vet invoice, claim-to-reimbursement loop — with the "application" being the insurer's postal/phone customer service. The digital customer app is the modern realization of the same three structures, not a redefinition of them. Therefore nothing era-specific (mobile app, instant claims, direct deposit, telehealth, dashboards) may enter L0. The check passes.

### L1 — Common Mature Structure

- Claim status tracking surface (claim list/dashboard with progression; notification on change)
- Policy document library (policy schedule, terms/handbook, regional summary documents)
- Self-service policy administration (contact/address details, payment method, pet details, renewal review, cancellation)
- Coverage-rule surfaces (limits, excess/deductible, co-pay/reimbursement %, waiting periods, exclusions)
- Medical records attachment (upload pet's vet history / records storage to speed claims)
- Direct vet payment option (vet as payee) and/or vet-submitted claims rail (vet portal)
- Multi-pet handling under one customer account
- Telehealth / 24-7 vet video line (bundled or attached)
- Perks/discounts/referral extras

### L2 — Variant / Optional Structure

- Advance-before-payment urgent pay (PumpkinNow) — product-specific in sample; a money-path variant
- Pre-authorisation (present at Animal Friends, absent at ManyPets) — variant
- Paper claim forms as first-class channel (Animal Friends) — regional/traditional variant
- Pet-life super-app wrapper (social, discovery, gamification, lost-pet tag) — Figo pattern; drift risk toward Pet Health Application
- Wellness/preventive add-ons (riders, standalone wellness memberships) — common optional, legally separated from insurance in vendor disclosures
- Species breadth beyond dog/cat (horse, rider, tack) — variant
- Regional policy taxonomy (UK four policy types vs US deductible/reimbursement model) — regional
- Quote/purchase flows inside the same brand surface — purchase-side capability, adjacent Type's center

### L3 — Vendor-specific (Research Notes only)

- Figo: "Pet Cloud" branding; claims assistant "Evie"; achievements gamification; pet tag; "3 working days" average claim-close stat (vendor data); 12-month curable-pre-existing window
- Pumpkin: PumpkinNow name, $500+ threshold, "15 minutes" and "90%" figures; 180-day curable-pre-existing rule with knee/ligament carve-out; 10% multi-pet discount
- ManyPets: MoneyBack 20%; one-excess-per-policy-year; 6-month claim window; 48h/14d waiting periods; 20% co-pay from age 7; "97% of claims paid" stat; 60-day referral qualification
- Animal Friends: Pawtal name; Treat Tin; £69–£299 excess options; 45-day missing-pet rule; 48h advertising/reward rule; 4-day hospitalisation boarding rule; 2-working-day processing target; 1-working-hour pre-auth target; horse/rider/tack claim scenarios

## Vendor-specific Findings

See L3 above. Additionally: the brand-vs-underwriter legal split (agency brands riding licensed underwriters, with non-insurance services explicitly disclaimed in footers) is a market-structure fact that shapes disclosures but does not change the app's core model.

## Boundary Findings

| Neighbor Type | Relationship | Distinction | "Remove what → becomes the other Type" |
|---|---|---|---|
| Insurance Claims Management | operator-side mirror | same claim object, opposite side: staff-side handling workflow (assignment, adjuster, adjudication) vs customer-side filing/tracking window | remove the customer orientation and expose the insurer's handling workflow → Claims Management |
| Insurance Policy Administration System | insurer-side system of record | administers the policy book (products, rating, lifecycle); the customer app reads from it and triggers actions | move administration of the book into the surface → Policy Administration |
| Insurance Quote Platform / Insurance Marketplace | purchase-side | compare/buy before a policy exists; the customer app services an existing policy | remove the existing-policy relationship; center on comparison/purchase → Quote Platform/Marketplace |
| Pet Health Application | sibling, shared pet-profile vocabulary | pet health records, reminders, vet advice without an insurance relationship | remove policy + claims; keep records/reminders → Pet Health Application (Figo's Pet Cloud shows the drift surface) |
| Mobile Banking Application | structural rhyme | consumer app of a financial institution; object is deposits/payments/accounts, not coverage/claims | swap the insurance objects for bank objects → banking |
| Customer Portal / Self-service Support Portal | generic container | generic account + support; no insurance domain objects | strip the insurance objects → generic portal |
| Customer-to-Business Messaging / Customer Service surfaces | adjacent capability | support chat exists inside these apps but is not the center | center on conversation → support/messaging Types |

Key positive boundary: the insurance relationship (policy of record + claim loop) is what keeps the Type distinct from Pet Health Application even when the surface carries records, reminders, and telehealth. Conversely, a pet app with records and reminders but no policy/claims is not this Type.

## Uncertainties

- Trupanion's direct-vet-pay-by-default model and Lemonade's AI-instant-claims model were unreachable; the direct-vet-payment capability is cross-product evidenced (ManyPets, Animal Friends), but "insurer pays the vet by default without customer involvement" is unverified in this sample.
- Exact in-app claim state names and transition rules were not observed (authenticated screens inaccessible); claim states are described conceptually.
- Pumpkin's vet portal role (whether vets submit claims there) is unconfirmed.
- Figo's claim-tracking depth is evidenced only by marketing copy ("keep track of where your claim is in the process").
- Whether every product exposes premium payment history (vs only payment-method management) is unconfirmed; ManyPets shows "upcoming payment dates," Animal Friends shows policy schedule in account.
- The sample is US/UK/Nordic-heavy; other regional regimes (e.g., EU statutory contexts, APAC) are unsampled.

## Final Synthesis

A Pet Insurance Customer App is the policyholder-facing application of a pet insurance relationship. Its defining core is three jointly-held structures: the insured pet's policy/coverage as a customer-visible record in a personal account; claim filing anchored to a veterinary bill (itemised invoice + veterinary history), submitted by the customer or their vet; and the claim-to-money loop (assessment → decision → payment to customer and/or vet) with customer-visible progression. Everything else commonly seen — claim dashboards, document libraries, self-service administration, direct vet pay, pre-authorisation, telehealth, records storage, perks, super-app wrappers — is common mature structure or variant, not definition. The paper-era lineage (policy document + claim form + vet invoice + reimbursement cheque) satisfies the same three structures, confirming the core is era-independent. The Type's hardest boundary is with Pet Health Application (shared pet vocabulary, no insurance relationship) and with the operator-side insurance Types (same objects, opposite side of the glass).
