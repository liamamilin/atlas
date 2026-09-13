# Pet Insurance Customer App

## Overview

A **Pet Insurance Customer App** is the policyholder-facing application of a pet insurance relationship: a personal, authenticated surface in which a pet owner holds and manages the insurance policy covering their animal, files claims against veterinary bills, and follows each claim to its money outcome.

The defining core is small — three structures that only exist together:

```text
Insured pet's policy / coverage of record
    (held in the customer's account, readable, with policy documents)
        ↓ anchors
Claim filed against a veterinary bill
    (itemised invoice + the pet's veterinary history)
        ↓ resolves through
Claim-to-money loop
    (insurer assessment → decision → payment to the customer and/or the vet)
```

Remove the policy and the app becomes a pet profile tool. Remove the claim and the insurance promise is unexercisable. Remove the money outcome and only a submission drop box remains.

Everything else commonly associated with these apps — claim dashboards, document libraries, self-service administration, direct vet payment, telehealth lines, records storage, perks — is standard capability or optional packaging, not what makes the Type. The paper-era lineage of pet insurance (a policy document kept at home, a claim form posted with a vet invoice, a reimbursement cheque in return) contains the same three structures; the app is their modern customer-facing realization, not a redefinition of them.

## Users & Context

**Primary user**: the pet owner who holds the policy. They open the app in three recurring situations:

- to check what their pet's policy covers, what it costs, and when it renews
- after (or during) a veterinary visit, to get the bill reimbursed or paid
- to keep their details, payment method, and documents current

**Secondary participants**:

- a second household member on the same policy, using the same account
- the veterinary clinic — an external party inside the claim loop, not a user of the customer surface. The clinic may submit the claim on the owner's behalf through a separate vet-facing portal, may receive the insurer's payment directly, and may be asked for the pet's full medical history. Some products surface the vet's view of the customer's coverage (limits, excess) through that vet-side portal.

**Context**: consumer, mobile-first but commonly paired with a web account on the same identity. The emotional context matters for the design: claims are usually filed when the animal is sick or injured, so the claim flow is built to work under stress, and money speed is a headline product differentiator.

The insurer's own staff are *not* users of this Type — they work in operator-side claims and policy systems on the other side of the glass.

## Core Model

### The Defining Core

**Policy / coverage of record.** The center of the model is the insurance relationship itself: which pet(s) are covered, under which plan, at what limits, with which excess/deductible and reimbursement terms, from what date, until which renewal. The customer can read this state at any time, and the policy documents (schedule, terms, regional summary documents) are the authoritative statement of it. A policy typically covers one animal; multi-pet arrangements exist under one customer account.

**Insured pet.** The policy is anchored to an individually identified animal — name, species, breed, age, and status details. The pet is the subject the coverage attaches to and the subject every claim is about.

**Claim.** The unit of work. A claim binds a veterinary visit or treatment to the policy and asserts a right to money. Its anchor document is the **itemised veterinary invoice** — paid, or in some flows "final" (issued after treatment but before the owner pays). Supporting evidence commonly includes the pet's veterinary history. Claims are not limited to vet fees in all products: benefit claims (death of the pet, missing or stolen pet, holiday cancellation, boarding while the owner is hospitalised) anchor to different evidence — purchase receipts, cause-of-death documentation, boarding or travel receipts.

**Claim-to-money loop.** Every submitted claim is assessed by the insurer against the policy terms and resolves into a decision and a money movement: payment to the customer (reimbursement, or in some products an advance before the vet is paid), direct payment to the veterinary practice, or a denial with reasons. The customer can see where the claim stands throughout.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Claim tracking** — a claim list or dashboard showing each claim's progression, with notifications when something changes.
- **Policy document library** — the policy schedule, terms/handbook, and regional summary documents, viewable and downloadable.
- **Self-service administration** — updating contact and address details, pet details (e.g., neutering status), payment method and upcoming payment dates, reviewing renewal changes in advance, adjusting excess/co-pay at renewal, and cancelling the plan.
- **Coverage-rule surfaces** — waiting periods, excess/deductible, co-payment or reimbursement percentage, exclusions (pre-existing conditions, routine care), and annual limits, all readable before and during claiming.
- **Medical records attachment** — uploading or storing the pet's veterinary records to speed claim assessment.
- **Vet-side rails** — a vet-facing claim portal and/or direct payment of approved claims to the veterinary practice.
- **Multi-pet handling** — several animals under one customer account, sometimes with a discount.
- **Telehealth / 24-7 vet video line** — bundled or attached as a separate non-insurance service.
- **Perks and referrals** — discounts, reward programs, refer-a-friend.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Customer surface
Implementations:    mobile app, web account portal, or both on one identity

Concept:            Claim submission rail
Implementations:    customer self-submission, vet-submitted via a vet portal,
                    phone/email, paper claim form (where retained)

Concept:            Money path
Implementations:    reimbursement to the customer, direct payment to the vet,
                    advance paid to the customer before the vet bill is settled

Concept:            Coverage knobs
Implementations:    UK-style policy types (accident-only, time-limited,
                    per-condition max, lifetime) vs US-style accident-&-illness
                    plans with deductible / reimbursement-% / annual-limit choices
```

A reader who has only seen one implementation (say, a US reimbursement-style plan) should still recognize a UK lifetime policy with a vet-portal claim rail as the same Type.

## How It Works

### Set up the relationship

```text
Enroll the pet (species, breed, age, health disclosure)
→ policy issued with coverage terms, waiting periods, and price
→ customer account created
→ payment method and payout method configured
→ optionally: pet's medical records uploaded, direct deposit set up
```

From this point the app is the customer's standing window onto the relationship: coverage state, documents, payments, and the pet's claim history.

### File and follow a claim — the defining loop

```text
Vet visit happens
→ obtain the itemised invoice (paid, or "final" where the product allows)
→ submit the claim:
     - customer submits in the app (visit details + invoice upload), or
     - the vet submits through the insurer's vet portal on the owner's behalf
→ insurer assesses against the policy
     (coverage, waiting periods, exclusions, excess/deductible/co-pay,
      supported by the pet's veterinary history)
→ decision: approved (in whole or part) or denied, with reasons
→ money moves:
     - reimbursement to the customer, or
     - direct payment to the vet, or
     - an advance to the customer before the vet bill is settled (some products)
→ customer follows the claim's progression throughout
```

Ongoing conditions repeat this loop: many products support continuation claims linked to the original claim, filed per treatment or batched. Duplicate submission is a real failure mode — if the vet has already filed, the customer filing again delays the claim.

### Service the policy

```text
Renewal approaches
→ the app surfaces the upcoming changes (price, terms, excess/co-pay)
→ customer reviews, adjusts what is adjustable, and confirms or cancels
→ between renewals: update details, payment method, download documents
```

### Read the coverage

Before claiming, the customer consults the coverage surfaces: what is covered, the limits, the excess/deductible, the co-pay or reimbursement percentage, the waiting periods, and the exclusions. The policy documents remain the authoritative answer; the app's coverage pages are the practical one.

### Capability tiers

**Defining core** — without these, not this Type:

- policy/coverage of record visible in a personal account
- claim filing anchored to a veterinary bill
- claim-to-money loop with customer-visible progression

**Standard capabilities** — present in most mature products:

- claim tracking, document library, self-service administration
- coverage-rule surfaces, records attachment
- vet-side rails (vet portal and/or direct vet payment)
- multi-pet handling, telehealth line, perks

**Optional / variant** — depends on product, market, and philosophy:

- advance-before-payment urgent pay
- pre-authorisation of treatment
- paper claim forms as a first-class channel
- pet-life super-app wrapper (social, discovery, gamification, lost-pet tag)
- wellness/preventive add-on programs
- species breadth beyond dogs and cats

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Home / dashboard

The account's entry surface: the insured pet(s), coverage status, upcoming renewal, recent claims, and shortcuts to the most common actions (file a claim, view documents, contact support).

### Pet & policy view

The coverage-of-record surface: plan name, coverage limits, excess/deductible, reimbursement or co-pay terms, policy dates, waiting-period status, and links to the policy documents. Primary actions: review terms, update pet details, view documents.

### Claim submission flow

A guided multi-step form: choose the pet, describe the visit/condition, enter amounts, upload the itemised invoice (and any history), choose the payee where the product allows (customer or vet), confirm. Some products route this through a conversational assistant; the structure is the same.

### Claim list / claim detail

The tracking surface: each claim with its date, condition, amount, and current stage; detail view with the submitted documents, the decision, the payout breakdown (gross, minus excess/co-pay), and the payment method used. Primary actions: submit a new claim, add documents to an open claim, link a continuation claim.

### Documents

Policy schedule, terms/handbook, regional summary documents, and claim-related correspondence. Primary actions: view, download.

### Payments & billing

Premium payment method, upcoming payment dates, and (where exposed) payment history; payout method for claims (direct deposit details).

### Coverage & rules

Waiting periods, exclusions, limits, and claim conditions in readable form — the practical companion to the policy documents.

### Extras surface

Telehealth/vet-video entry, perks and discounts, referrals — commonly present, always secondary to the insurance core.

## Important Rules / Behaviors

### Waiting periods gate new coverage

Claims for accidents are commonly excluded for the first days of a new policy, and claims for illnesses for the first weeks; the exact windows are product-specific. Waiting periods apply at first purchase, not at renewal; switchers with continuous prior coverage may be exempt with evidence.

### Pre-existing conditions are the central exclusion

Conditions that showed signs before coverage started are excluded. The treatment of *curable* pre-existing conditions varies substantially by product — some re-cover them after a defined symptom-free period, some carve out specific condition classes permanently. This is the most consequential coverage rule in the Type and a leading source of claim denials.

### The invoice is the claim's anchor

An itemised veterinary invoice is the minimum document; a "final" invoice issued before the owner pays is accepted in some flows. The pet's full veterinary history is commonly required for assessment. Missing or incomplete documentation is the main cause of delayed claims.

### Excess, deductible, and co-pay shape the payout, not the limit

The customer's share (fixed excess per claim or per year, annual deductible, percentage co-payment) is deducted from the payout; it does not reduce the coverage limit. Senior-pet co-payments are common in some markets. The breakdown appears on the claim decision.

### Claims have submission windows

Claims must be submitted within a defined time from treatment; late claims are not payable. The window length is product-specific.

### Direct vet payment requires the vet's cooperation

Paying the vet directly is possible only when the practice participates (submits through the vet portal or accepts direct payment). If the vet declines, the customer pays and claims reimbursement. Submitting both ways causes duplicates and delays.

### Pre-authorisation is optional machinery

Some products let the vet pre-check coverage before treatment proceeds; others explicitly do not offer it. Its absence does not put a product outside the Type.

### The policy documents are authoritative

The app's coverage pages summarize; the policy terms decide. Disputes resolve against the documents, and the app's document library is the customer's permanent access to them.

### Non-vet-fee benefit claims anchor to different evidence

Death-of-pet claims need purchase proof and cause-of-death documentation; missing-pet claims may need a waiting period before payout; boarding claims need hospitalisation proof; travel-cancellation claims need receipts. The claim object generalizes beyond the vet invoice, but the vet-fee claim remains the center.

## Variants

- **Reimbursement-first (mainstream default)** — the customer pays the vet, submits, and is paid back. The baseline money path across the sample.
- **Direct-vet-payment-first** — claims flow through the vet portal and the insurer pays the practice; the customer may never handle the money. Common where vet participation is high.
- **Advance-before-payment** — an urgent-pay path deposits the covered amount to the customer before the vet bill is settled, inverting the usual sequence for large bills. Product-specific in the sample.
- **Account-portal vs super-app** — some products keep the surface strictly on insurance; others wrap it in a pet-life app (records, reminders, social, discovery, lost-pet tag). The wrapper is optional; the insurance core is not.
- **Regional policy taxonomy** — UK-style policy types (accident-only, time-limited, per-condition max benefit, lifetime) vs US-style accident-&-illness plans tuned by deductible, reimbursement percentage, and annual limit. The knobs differ; the claim loop does not.
- **Species breadth** — dogs and cats everywhere; some products extend to horses with their own claim scenarios (rider injury, tack, third-party liability).
- **Wellness add-ons** — preventive-care programs sold beside the insurance, usually as legally separate non-insurance products; they ride on the same customer account.
- **Paper-channel persistence** — most products have eliminated paper claim forms; some retain them as a first-class channel alongside digital rails.
- **Brand vs underwriter structure** — some customer apps are operated by licensed agencies riding on underwriters' policies; others by regulated insurers. This shapes legal disclosures but not the app's core model.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Insurance Claims Management | the operator-side mirror: insurer staff handle claim assignment, assessment, and adjudication; this Type is the customer's window onto the same claim object |
| Insurance Policy Administration System | the insurer-side system of record for the policy book (products, rating, lifecycle); the customer app reads from it and triggers actions but does not administer the book |
| Insurance Quote Platform | purchase-side: comparison and buying before a policy exists; this Type services an existing policy (quote/purchase may appear as a flow inside the same brand surface, but it is not the center) |
| Insurance Marketplace | multi-insurer comparison venue; no per-customer policy of record of its own |
| Pet Health Application | shares the pet-profile vocabulary (records, reminders, vet advice) but has no insurance relationship; the hardest boundary — a records-and-reminders app with no policy/claims is not this Type, and a customer app whose insurance core dissolves into lifestyle features drifts toward it |
| Mobile Banking Application | structural rhyme (consumer app of a financial institution) but the objects are deposits, payments, and accounts — not coverage and claims |
| Customer Portal / Self-service Support Portal | the generic container (account, documents, support) without insurance domain objects; strip the policy and claims and only the generic portal remains |

The boundary with Insurance Claims Management deserves emphasis: both hold claims, but on opposite sides of the glass. If the surface's primary actor is the insurer's staff working a queue, it is Claims Management; if it is the policyholder filing and following their own claims, it is this Type.

## Representative Products

- **Figo Pet Insurance** (US) — app-first "Pet Cloud": insurance plus records, telehealth, and lifestyle features
- **ManyPets** (UK/US/Sweden) — account-centric self-service with a vet-portal claim rail; explicitly no pre-authorisation and no paper forms
- **Pumpkin** (US) — pay-before-you-pay urgent-advance model (PumpkinNow) on a member portal
- **Animal Friends** (UK) — traditional multi-channel: vet portal (Pawtal), online account, and paper claim forms; pre-authorisation; multi-species including horses

The core model was checked against the paper-era lineage of pet insurance (policy document + posted claim form + vet invoice + reimbursement cheque) to avoid over-fitting the definition to the current mobile-app generation. Trupanion and Lemonade — two widely referenced products with distinct philosophies (default direct vet pay; AI-instant claims) — could not be reached during research and are not drawn upon.

## Sources

Research date: **2026-09-09**

- Figo Pet Insurance — https://figopetinsurance.com/ , https://figopetinsurance.com/pet-cloud/
- ManyPets — https://www.manypets.com/ , https://www.manypets.com/uk/how-to-claim/ , https://www.manypets.com/uk/existing-customers/
- Pumpkin Pet Insurance — https://pumpkin.care/ , https://www.pumpkin.care/claims
- Animal Friends — https://www.animalfriends.co.uk/ , https://www.animalfriends.co.uk/existing-customers/claims/

> Sourcing limitation: official sites for Trupanion, Lemonade, Healthy Paws, Embrace, Pets Best, ASPCA Pet Insurance, and Petplan UK were unreachable from the research environment (blocked or transport errors) and are excluded. No authenticated in-app screens were observed; interface and rule descriptions come from official product pages, how-to pages, and FAQs. Numeric specifics (waiting periods, thresholds, processing targets, coverage percentages) quoted in vendor-facing sources are product-specific and are not generalized in this document. Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical check are recorded in the paired Research Notes.
