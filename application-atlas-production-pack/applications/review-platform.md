# Review Platform

## Overview

A **Review Platform** is a public platform where people who have firsthand experience with a business, product, or service publish an evaluation of it — a rating together with a written account — and where those evaluations accumulate, on the platform's own record of the reviewed entity, into a corpus that prospective buyers read before they decide.

The defining structure is small:

```text
Reviewed-entity record (held by the platform, independent of the entity)
└── First-hand evaluation records (rating + account, by non-affiliated users)
    └── Accumulating public corpus, operated for prospective buyers
```

Three properties. If any one is removed, the product is no longer recognizable as a review platform:

- **Reviewed-entity record** — the platform maintains a persistent, identified record for each reviewed business, product, or provider, and that record exists whether or not the entity ever participates. Entities cannot generally have their records removed. Without this, evaluations float free and the product becomes a comment feed; with only this, the product is a directory.
- **First-hand evaluation records** — each review is a rating plus an account of the reviewer's own experience, submitted by a registered user who is neither the reviewed entity nor affiliated with it, admitted under the platform's eligibility and authenticity rules. Without this, the site becomes a catalog of bare scores or a board of self-promotional testimonials.
- **A public corpus serving third-party decisions** — reviews persist and accumulate on the entity's record, and the platform operates that corpus for prospective buyers — people considering a transaction with the reviewed entity, not the entity itself. Without this public, third-party-serving posture, the same records become a private customer-feedback channel.

Aggregate scores, rankings, verification programs, review-invitation tooling, incentives, and monetization are widespread in modern products but are not what makes the product a review platform — they are the machinery that makes the corpus usable and sustainable, and they vary substantially between products.

## Users & Context

Three distinct user groups, with the platform mediating between them:

**Reviewers** — people with firsthand experience of the reviewed entity: customers of a business, users of a software product, clients of a service provider. They contribute evaluations voluntarily, sometimes in exchange for incentives, sometimes as part of an invited collection program. Their standing depends on their real experience, not on any relationship with the entity.

**Readers** — prospective buyers evaluating an entity they may transact with: consumers choosing a contractor, or professionals shortlisting enterprise software. They arrive through search, categories, or rankings and read the corpus — individual accounts plus the aggregate picture — as decision input.

**The reviewed entities** — the businesses, products, and providers the records describe. They can usually claim their record, respond publicly to reviews, invite their customers to review, and purchase additional services from the platform. They are participants with commercial stakes, not authors of the record: platform rules exclude them and their affiliates from reviewing their own offering.

The context is transactional research: the corpus matters because a transaction (purchase, contract, employment, booking) is being contemplated, and experience of strangers is being substituted for personal acquaintance.

## Core Model

### The Defining Core

**Reviewed-entity record.** A persistent, identified record describing one evaluated thing — a company, a product, a service provider. The platform, not the entity, is the custodian: records are created for entities that never signed up, remain when entities disengage, and are not removable on request. This is load-bearing because reviews must always be *of something* that persists; it also creates the platform's characteristic tension — records of entities that never asked to be reviewed.

**The review.** The unit of contribution. Conceptually it is an evaluation record with three faces:

- a **rating** — a valence judgment on the platform's scale (scales vary widely: five-star, ten-point, and derived scales all exist);
- a **written account** — the reviewer's description of their own experience, from a sentence to a structured, question-by-question survey response; media attachments are common;
- **attribution and provenance** — the review is bound to a registered user and to the entity record, and carries whatever provenance the platform assigns: how it was collected, whether identity or purchase was verified, whether the reviewer is flagged as having a business relationship with the vendor.

The reviewer is subject to the platform's eligibility frame: firsthand experience only, no reviewing of one's own or affiliated entities, identity held under the platform's policy — which at some products permits public anonymity behind verified registration, and at others requires a real name on display.

**The corpus and its service.** Reviews are not ephemeral feedback; they persist, accumulate per entity, and are published to third parties. The platform invests in the corpus's trustworthiness — moderation before or shortly after publication, conflict-of-interest screening, fraud detection — because the corpus's only value is that readers can act on it. Every product researched operates an authenticity gate of some kind; whether it holds reviews back before publication or filters them afterward varies.

### Capabilities Shared by Mature Products

These are standard in modern products without defining the Type:

- **Aggregate summary** — an average score and review count per entity, so the corpus compresses into one comparable signal. Mechanisms differ widely: plain averages, recency-weighted blends, decay curves, or ranking-point systems.
- **Discovery surfaces** — categories, search, top/ranked lists; at business-software products, alternatives and comparison pages built on the same corpus.
- **Rankings, badges, and reports** — derived presentations of the corpus (category leaders, quadrant reports, annual awards) at many products.
- **Entity participation** — claiming the record, responding publicly to reviews, inviting customers, collecting reviews through approved channels (invitation links, widgets, in-app prompts, integrations).
- **Trust machinery** — identity verification options, proof-of-purchase evidence, automated fraud detection, community flagging, labeling of how each review was collected and whether it counts toward scores.
- **Reviewer lifecycle self-service** — editing, updating, or deleting one's own reviews.
- **Age sensitivity** — recent reviews commonly count for more; several products expire old reviews from rankings or weight them down.

### One Structure, Many Implementations

```text
Concept:   Reviewed-entity record
Realized:  business/site profile, software product profile, service-provider profile

Concept:   Rating
Realized:  5-star, 10-point, derived stars from a recommend-question

Concept:   Written account
Realized:  free-form narrative, structured survey form with scored questions,
           long-form pros/cons review, interview write-up

Concept:   Authenticity control
Realized:  pre-publication human moderation, automated fraud filtering,
           identity/LinkedIn/business-email validation, ID verification,
           screenshot evidence, purchase-proof badges, collection-channel labels

Concept:   Aggregate presentation
Realized:  simple average, recency-weighted score, decay-weighted score,
           points-based category rankings, quadrant reports
```

## How It Works

### A reader evaluates an entity

```text
Arrive by search / category / ranking
→ open the entity's record
→ see the aggregate picture (score, count, distribution, highlights)
→ read individual accounts (sorted and filtered)
→ optionally compare with alternatives
→ decide
```

### A reviewer contributes

```text
Register / sign in (identity under platform policy)
→ find the entity's record
→ give a rating and write the account (+ media / evidence / structured answers)
→ submit
→ review enters the platform's authenticity gate (moderation, verification, fraud screening)
→ published — or rejected with a reason and resubmittable
→ reviewer can later edit, update, or delete
```

### The reviewed entity engages

```text
Discover the platform's record of itself
→ claim it (free at the researched products)
→ respond publicly to reviews
→ invite customers / install collection channels (within anti-cherry-picking rules)
→ request verification of suspicious reviews
→ optionally purchase visibility, collection, or data services
```

The entity can influence the *volume* and *collection quality* of its corpus but not its *content*: platforms document that payment buys services, not removal or ranking outcomes.

### The platform's own loop

Moderation and fraud review keep the corpus authentic; collection machinery (invitations, campaigns, interviews, integrations) feeds volume; aggregation and ranking machinery recompute as reviews arrive and age; and monetization converts corpus attention into revenue from the reviewed side — subscriptions, sponsorships, leads, and buyer-intent data — under published rules about what money can and cannot buy.

## Interfaces

### Entity profile / review page

The primary surface readers and reviewers share.

- aggregate score and count, rating distribution, highlights or extracted pros/cons
- the review list with sorting (recency, helpfulness, rating) and filtering
- provenance labels per review (collection channel, verified badges, conflict-of-interest flags)
- primary actions: read reviews, leave a review, respond (entity side), report a review

### Review submission form

- rating control on the product's scale
- free-text account; structured/scored questions at business-software products
- evidence attachments (screenshots, photos, video), which may earn a verification badge
- display options (public name or anonymous display, where offered)

### Reviewer account

- the reviewer's contributions and their status (in moderation, published, rejected with reason)
- edit / update / delete controls; incentive fulfillment where applicable

### Entity dashboard

- claimed-record management, review responses, invitation and collection tools, verification requests, reporting on traffic and leads where the platform sells them

### Discovery surfaces

- category listings and search; ranked leaderboards or report pages; alternatives/comparisons pages where present

## Important Rules / Behaviors

### Firsthand and unaffiliated only

Reviews must describe the reviewer's own experience; second-hand accounts are removed, and the reviewed entity's employees, former employees, and direct competitors are excluded — at some products from submitting at all, at others from counting toward scores (flagged as having a business relationship). This rule is what keeps the corpus an evaluation record rather than a marketing surface.

### The reviewed party cannot erase the record

As a rule, entities can neither delete reviews nor pay for their removal or suppression, and the platform-held record is not taken down on request — several researched products state this explicitly, and none of the researched products offers entity-side deletion. The entity's designated remedies are public response, verification requests against suspicious reviews, and guideline-violation reporting — with the platform, not the entity, deciding. Reviewers, by contrast, control their own reviews and can edit or delete them.

### Authenticated contribution, moderated corpus

Every researched product gates the corpus: registration with verifiable identity, pre-publication moderation or post-publication filtering, duplicate prevention (one review per person per product at the products that document it), and rejection reasons communicated to the reviewer. Investigations can temporarily hide reviews; factual disputes between reviewer and entity are generally not arbitrated — the public response is the designated remedy.

### Money is firewalled from outcomes

The reviewed side commonly pays the platform — subscriptions, sponsorship, leads. The characteristic rule set that keeps the Type coherent: payment must not buy review removal, ranking placement, or review sentiment; customer-solicitation must not be cherry-picked toward likely-positive reviewers; incentives, where allowed, must not be contingent on the rating and must be disclosed; each review's collection channel is labeled so readers can judge provenance.

### Recency matters

Corpora age. Products commonly weight recent reviews more heavily, expire old reviews from rankings, or reset an evaluation's weight when the reviewer updates it — because the corpus is read as evidence about the entity *now*.

### Provenance is displayed

Collection-channel labels, verified-purchase and verified-identity badges, conflict-of-interest flags, and sponsored-content labels expose how each evaluation entered the corpus — trust is managed by labeling rather than by silent curation.

## Variants

- **Consumer-general platforms** — any business with a web presence can be recorded; organic and invited consumer reviews; identity and purchase verification optional.
- **Local/vertical consumer platforms** — restaurants, home services, travel (travel reviews are developed further under their own Application Type with stay-specific semantics).
- **Business-software review platforms** — structured survey-style reviews by verified professionals; scoring often combines review satisfaction with firmographic "market presence" into category rankings and quadrant reports; incentives and collection campaigns are common; the reader is a buying committee.
- **Enterprise-technology platforms with editorial involvement** — verified real-user reviews with minimum depth and mandatory balanced pros/cons; editorial staff titles or writes up phone interviews; published ranking methodologies.
- **Curated consumer platforms** — reviews collected through forms and interviews, human-vetted for substance, then curated into buyers guides and matching tools (drifting toward comparison semantics on top of the review corpus).
- **Employer-review platforms** — the same structure with employees reviewing employers; anonymity options are more central.
- **Embedded realizations** — marketplaces, app stores, and map/social platforms host the identical structure (product/listing/place record + attributed rating/account + aggregate) as a capability of a transaction or discovery product; the standalone Type is distinguished by the corpus being the product itself.
- **Collection philosophy** — organic walk-in reviews, entity-invited programs, incentive campaigns, platform-run interviews; most products mix several, labeled by channel.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Comparison Platform | aligned multi-option presentation to choose *among many* alternatives; a review platform accumulates first-hand evaluations read to judge *one* entity. Comparison products commonly embed user reviews as a capability — the seam is the center of gravity, not feature overlap |
| Directory Application | entity records and discovery without an evaluation corpus as the center; a review platform's records exist to anchor the corpus |
| Travel Review Platform | domain sibling with stay/inventory-specific record semantics and booking adjacency; developed as its own Type |
| E-commerce Storefront / Marketplace | hosts product reviews as a capability of a transaction platform; the review corpus is not the product |
| Voice of Customer Platform | company-side, private collection and analysis of customer feedback; no public third-party-serving corpus |
| Q&A Community | question records answered by a community; evaluations of named entities are not the unit of record (though Q&A may coexist alongside reviews) |
| Online Forum / Community Platform | discussion threads as the unit; may contain evaluative content but does not bind it to entity records as a governed corpus |
| Customer Advocacy / Testimonial Tools | the entity's own collection and publishing of endorsements — no non-affiliated corpus, no platform custody of records |

## Representative Products

- **Sitejabber (SmartCustomer)** — consumer-general reviews of any business with a website; invitation-labeled collection, verification badges, explicit pay-never-removes policy
- **ConsumerAffairs** — curated consumer reviews vetted by human moderators, layered into buyers guides and brand services
- **G2** — business-software reviews via structured survey forms with verified professionals, scoring, and category reports
- **PeerSpot** — enterprise-technology reviews from verified real users with editorial titles, published ranking methodology, and no-advertising posture

The defining core was checked against older and differently positioned samples — the same products' own multi-decade heritage (mid-1990s and mid-2000s origins) and the embedded review structures of map, marketplace, and app-store platforms — so the definition does not depend on any one era's machinery (star scales, incentive campaigns, AI features, or specific verification vendors).

## Sources

Research date: **2026-09-08**

- Sitejabber / SmartCustomer — official FAQ (reviews, ratings, verification, business side): https://www.sitejabber.com/faq
- ConsumerAffairs — official About (collection, moderation, heritage): https://www.consumeraffairs.com/about/
- G2 — official documentation: purpose & platform, writing a review, how G2 ensures authentic reviews, review submission process and timeline, why reviews are rejected, research scoring methodologies: https://documentation.g2.com/ (help/docs/…, docs/research-scoring-methodologies)
- PeerSpot — official FAQ, Community Guidelines, Ranking Methodologies, homepage: https://www.peerspot.com/faq , https://www.peerspot.com/guidelines , https://www.peerspot.com/methodology

> Sourcing limitation: several prominent platforms could not be fetched from the research environment on 2026-09-08 (Trustpilot, Yelp, Capterra, Glassdoor, TrustRadius, Google Maps review help — bot walls, timeouts, or script-rendered pages). No mechanics specific to those products are asserted in this document; claims about consumer-local and platform-native realizations are kept structural, and precise operational details observed at the researched products (scoring formulas, moderation turnaround times, inclusion thresholds, incentive terms) are deliberately omitted here and retained in the paired Research Notes.
