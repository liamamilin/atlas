# Research Notes — Review Platform

Research date: 2026-09-08

## Research Goal

Understand what a Review Platform (directory §02.10 Reviews & Comparison) actually is by studying real products: what records it holds, what a review is, who may write one, how the corpus is governed and served, what the reviewed party does, and how the Type differs from the processed sibling Comparison Platform (joint-review flag recorded 2026-09-07: "evaluation of one vs comparison across many — sibling unprocessed").

## Initial Boundary

- Hypothesis: a public platform where users submit ratings and written accounts of businesses/products/services, accumulated per identified entity record and served to prospective buyers.
- Nearest neighbors: Comparison Platform (§02.10 sibling, processed), Directory Application (§02.11), Travel Review Platform (§26 sibling leaf), e-commerce/marketplace embedded product reviews, Q&A Community (processed), Voice of Customer Platform (§07), Online Forum / Community Platform.
- Known unknowns at start: whether B2B "software review" sites share the same core as consumer review sites; whether aggregation/rankings are definitional; how review eligibility is enforced per product.

## Research Questions

1. What is the reviewed entity record — who creates it, can it exist before the entity claims it, can the entity remove it?
2. What constitutes a review — rating, narrative, media, structured questions; what attribution is required?
3. Who is eligible to review — first-hand experience, identity, conflicts of interest, recency of use?
4. What is the review lifecycle — submission → moderation → publication → edit/update/removal?
5. How is the corpus served — aggregate scores, rankings, sorting, discovery?
6. What trust machinery exists — verification, anti-fraud, moderation, disclosure?
7. What does the reviewed party do — claiming, response, review collection, paid services; and what is the platform's stance on pay-vs-influence?
8. How do platforms make money, and how is the reviewed-party-pays tension handled?
9. Boundaries: vs Comparison Platform, Directory, embedded commerce reviews, VOC, forums, Q&A.

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Sitejabber (consumer site branded SmartCustomer) | consumer/general business reviews, organic + invitation-labeled collection, since 2006 | largest reachable general-consumer sample; unusually deep official FAQ |
| ConsumerAffairs | curated consumer reviews + editorial buyers guides, since 1998 | curated/verified posture; shows drift toward comparison/editorial layer |
| G2 | B2B software/services reviews, structured survey-style forms, incentive campaigns | dominant B2B pole; deep official documentation (seller + reviewer + methodology) |
| PeerSpot | B2B enterprise-tech reviews, verified real users, editorial involvement, published ranking methodology | contrasting B2B philosophy (interviews, editorial titles, no ads) |

Not sampled (unreachable, recorded below): Trustpilot, Yelp, Capterra, Glassdoor, Google Maps reviews, TrustRadius.

## Sources

Tier 1 (official product documentation, fetched 2026-09-08):

- Sitejabber/SmartCustomer official FAQ — https://www.sitejabber.com/faq (sitejabbber/SmartCustomer are the same service; FAQ served via smartcustomer.com branding) — very deep: ratings, removal policy, invitation labels, verification, business side.
- ConsumerAffairs About — https://www.consumeraffairs.com/about/ (Tier 2 positioning; includes founding 1998, review collection/moderation description, brand-side services).
- G2 documentation (Document360 KB):
  - https://documentation.g2.com/help/docs/understanding-g2s-purpose-and-platform.md
  - https://documentation.g2.com/help/docs/writing-a-review-on-g2.md
  - https://documentation.g2.com/help/docs/how-g2-ensures-authentic-reviews.md
  - https://documentation.g2.com/help/docs/review-submission-process-and-timeline.md
  - https://documentation.g2.com/help/docs/why-was-my-review-rejected.md
  - https://documentation.g2.com/docs/research-scoring-methodologies.md
  - https://documentation.g2.com/docs (get-started: review generation, profiles, widgets)
- PeerSpot:
  - https://www.peerspot.com/faq (Tier 1)
  - https://www.peerspot.com/guidelines (Tier 1)
  - https://www.peerspot.com/methodology (Tier 1, published ranking methodology)
  - https://www.peerspot.com/ (Tier 2 homepage: verification claims, review depth posture)

Source-access limitation (2026-09-08): the following were unreachable after 1–2 attempts each and were abandoned per policy — Trustpilot (support subdomain JS/CSS error; www 403), Yelp (help transport error; www 403), G2 main site help.g2.com (403 — but documentation.g2.com KB reachable), TrustRadius (403), ProductReview.com.au (403), Glassdoor help (403), Google Maps review help (timeout ×2), Indeed support (403). Capterra not attempted (same Gartner network as blocked domains per comparison-platform pass). Consequence: assertions about the consumer-local pole (Yelp-class) and platform-native reviews (Google Maps-class) are kept conceptual; no mechanics of those products are asserted.

## Product A — Sitejabber / SmartCustomer (consumer-general)

Evidence layer: A (direct, official FAQ).

Key observations:

- Purpose: "helps buyers make informed purchasing decisions, backed by real reviews"; "anyone who's had a firsthand experience with a business can write a review"; "you can review anything that has a website."
- Reviewed entity record: business/site profiles exist platform-initiated — "In the spirit of transparency, we list all kinds of company profiles and sites"; businesses cannot have their listing removed ("buyers have the right to research and review experiences on any website"). Any company with a website can register/claim.
- Review anatomy: overall rating + written account; optional proof of purchase → "verified purchase badge"; optional identity verification via third-party ID+biometric service → "verified user badge."
- Eligibility rules: first-hand only (second-hand reviews removed); no reviewing your own business or connected businesses; conflicts of interest (employees/former employees) removed.
- Lifecycle: reviews "generally posted within 48 hours"; some flagged for investigation up to ~30 days and may "move in and out" of the page; reviewer can edit (in place) or update (append) or delete own review anytime.
- Removal policy: removal only for guideline violations — second-hand, duplicates, conflicts of interest, incentivized (company reviews), personal attacks, irrelevance; plus algorithmic fake-review filtering. Platform does not arbitrate factual disputes; businesses respond publicly instead.
- Invitation labels: every review labeled by collection channel — No Invitation / Automated Invitation (verified) / Manual Invitation (not auto-verified) / Unconfirmed Invitation (not verified).
- Aggregate presentation: weighted rating = 50% all-time average + 25% last-12-months + 25% last-30-days (neutral value when a window has no reviews); category rankings combine review count + rating; "Instant Feedback" point-of-sale reviews are split into a separate labeled score (FTC-driven) and excluded from the overall rating.
- Trust machinery: automated fake-review detection + human spot checks + community reporting; identity verification partner; review-manipulation consequences (account loss, public flag, search demotion).
- Business side: free claiming → respond publicly, request verification (time-windowed, usage-capped on free plan), collect reviews via approved tools; paid plans for collection/publishing; explicit rule: businesses can never pay to remove/suppress reviews; cannot ask reviewers to remove/update; reputation-management firms have no influence.
- Incentives: incentives of any kind disallowed for company reviews; limited incentives allowed for product reviews/testimonials/images if not tied to rating/sentiment, FTC-compliant, and disclosed in the review.
- Community: contributor levels + contribution points (first-to-review, reviews, answers, helpful votes).
- Monetization: free for buyers and businesses; business upgrades for collection/publishing. Section 230 / CRFA framing for dispute posture.
- Heritage: "Since 2006."

## Product B — ConsumerAffairs (curated consumer)

Evidence layer: A- (official about page; positioning + some mechanics), partially B.

Key observations:

- Purpose: "give consumers a buying advantage"; reviews as foundation of buyers guides and matching tools.
- Review corpus: "3+ million consumer reviews... Collected via detailed submission forms and phone interviews, vetted and verified by human moderators and only earn publication if they contain real insight." (A for collection/moderation posture.)
- Layering: reviews curated into authoritative buyers guides and matching tools (drift toward comparison semantics on top of the review corpus).
- Business side: businesses "respond to them and improve"; free claiming of business account; "For Brands" paid services; disclosure that "Companies displayed may pay us to be Authorized or when you click a link..." (monetization disclosure posture).
- Heritage: founded 1998 (founder bio: "founded ConsumerAffairs.com in 1998").

## Product C — G2 (B2B software)

Evidence layer: A (official documentation KB).

Key observations:

- Purpose: "unbiased user reviews and insights on B2B software, hardware, and services, empowering professionals to make confident buying decisions."
- Reviewed entity record: product/service profiles with taxonomy categories, pricing, features, media; listing process (a review of a product "not currently approved to be listed" is held until the product exists); seller-side product profile setup documented.
- Review anatomy: structured survey-style form — satisfaction attributes (Ease of Use, Meets Requirements, Quality of Support, Ease of Admin/Setup, Ease of Doing Business With), Likelihood to Recommend (1–10), Direction of Product, plus factual questions (time to go live, ROI/payback, adoption %); open text; optional video review; optional screenshot evidence (never public; validated screenshots → "verified current user" label).
- Eligibility: real identity (business email / LinkedIn / Gmail sign-in; real name required — anonymous display possible by hiding name/face); recent professional use "within the last 2 years"; one review per person per product; current/former employees and direct competitors rejected; business partners (resellers etc.) may review but reviews carry a "Business Partner" label and do not count toward any scores; guest users labeled similarly; AI-generated reviews rejected outside a documented exceptions program.
- Lifecycle: every review manually moderated (typical turnaround up to 3 business days); approved → published; rejected → reason via My Reviews; resubmission re-moderated; reviews editable; gift-card rewards delivered after approval (campaign reviews; direct "Leave a Review" submissions not gift-card eligible).
- Trust: multi-step moderation; conflict-of-interest checks by humans; FTC guidelines referenced (segmentation of customers to solicit positive reviews violates guidelines → removal).
- Aggregate/ranking machinery: G2 Score = Satisfaction (weighted by volume, recency decay, review quality/readability, review source; current-user and unincentivized reviews weighted up) + Market Presence (review counts plus third-party firmographics — employees/revenue/web presence); normalized 0–100 within category; star rating derived from Likelihood-to-Recommend (halved, rounded to half star); Pros/Cons extraction (category-level, 18-month window, five pros/five cons, monthly refresh); Overall Review Sentiment panels; category sorting (G2 Sort / popularity / satisfaction); Alternatives and Comparisons pages; Grid® reports plotting Satisfaction × Market Presence; segment/regional/momentum grids; Index reports; Best Software awards; review decay (documented curve; update resets decay).
- Seller side: my.G2 dashboard — review campaigns (self-serve), in-app review prompts and integrations (Medallia/Pendo/HubSpot/Marketo), review collection widgets, review syndication to partner sites, response (vendor support), competitor tracking, buyer intent signals, leads (gated content/contact requests), badges/widgets for marketing, paid promotions; "Why G2 Grid placement cannot be changed manually" (pay ≠ placement).
- Community: Discussions; reviewer profile management.

## Product D — PeerSpot (B2B enterprise tech)

Evidence layer: A (official FAQ, community guidelines, published methodology).

Key observations:

- Purpose: "Buying Intelligence and Reviews for Enterprise Technology... Reviews, Discussions, and Advice from Real Users"; no banner advertising, no pay-to-play listing.
- Reviewed entity record: product/vendor records; inclusion criteria published (vendor ≥50 employees; product ≥10 enterprise customers; enterprise defined by size/revenue); "Any vendor can be listed as long as it offers an enterprise-class solution with real customers"; vendors cannot delete reviews or remove their company.
- Review anatomy: 1–10 rating + long-form text (positioned at an average of ~600 words) with mandatory balanced pros & cons; reviews may be submitted anonymously for display ("you can post anonymously") behind verified identity; voice-AI-assisted review submission offered.
- Eligibility: free membership with valid work email or LinkedIn; reviewers must be real users who used or evaluated the product within the past 12 months; vendors must self-identify; vendor employees cannot review their own or competitor products (may review categories where they have no offering); consultants/analysts may review if not vendor-paid; reviewers must disclose financial incentives.
- Verification: LinkedIn/company-email validation cross-checked; every post reviewed before publication (up to ~3 business days); community flagging ("Inappropriate?" link); "err on the side of quality" (unverifiable → not published); public red badge on vendors suspected of planting fake reviews.
- Editorial involvement: PeerSpot editorial staff write review titles after reading reviews (rules keyed to rating bands); vendor-initiated phone interviews written up as reviews (small disclosed minority; per-review disclosure of how each review was created).
- Vendor response: allowed and encouraged; vendor comments clearly marked with vendor badge.
- Aggregate/ranking machinery: published methodology — weighted aggregate of rating (25 pts), review count (15), words/review (10), comparisons (25), views (25); reviews older than 24 months expire from rankings; reseller reviews fully excluded; small-sample point reductions; monthly recalculation; "Leader" badges (≥50 points); historical methodology changes documented; rankings-by-company-size views.
- Community: Q&A/discussions, private messaging between members.
- Monetization: vendor services (interview-based review collection), sponsored labels on comparison pages, 100% opt-in lead generation, buyer-intent data subscriptions; explicit "no pay to play" on listing/ranking.

## Cross-product Comparison

| Structure | Sitejabber | ConsumerAffairs | G2 | PeerSpot | Strength |
|---|---|---|---|---|---|
| Platform-initiated reviewed-entity records (exist unclaimed, not removable by entity) | A — "we list all kinds of company profiles", removal refused | A- — company profiles displayed, unclaimed | A — listing process; held reviews for unlisted products | A — inclusion criteria; vendor cannot remove company | 4/4 A → Core |
| Review = rating + written first-hand account bound to entity | A | A- (forms/phone interviews) | A (survey form + open text) | A (1–10 + long text, pros/cons required) | 4/4 → Core |
| Attributed to a registered platform user (display may be anonymized; identity verified) | A (badges optional) | A- | A (real name; anonymous display option) | A (work-email/LinkedIn; anonymous display option) | 4/4 → Core |
| First-hand + no-conflict eligibility (entity staff/competitors excluded or quarantined) | A (removal reasons) | A- (human vetting) | A (rejection reasons; partner/guest labels) | A (vendor rules; reseller exclusion) | 4/4 → Core |
| Publication gate / authenticity control on the corpus | A (48h posting; investigation filtering) | A- (human moderation gate) | A (every review manually moderated) | A (every post pre-reviewed) | 4/4 → Core posture (mechanism varies) |
| Accumulating public corpus served to prospective buyers | A | A | A | A | 4/4 → Core |
| Aggregate summary (score + count) over the corpus | A (weighted recency formula) | B/A- | A (score + star from form question) | A (points-based ranking) | 4/4 → Standard capability (mechanisms differ widely) |
| Rankings/awards/badges/reports | A (category top lists) | — | A (Grid®, Index, Best Software) | A (Leader badges, methodology page) | Common |
| Discovery: categories/search; comparisons/alternatives | A (categories) | A (guides/matching) | A (categories/alternatives/comparisons) | A (categories/comparisons/Q&A) | Common; comparison surfaces = capability, not center |
| Reviewer incentives (gift cards / points) | A (contribution points; incentives banned for company reviews) | — | A (gift cards for campaign reviews) | A (gift cards via interview program) | Common, policy varies sharply |
| Review collection machinery for entities (invitations, widgets, prompts, integrations) | A (invitation labels) | — | A (campaigns, in-app prompts, widgets, syndication) | A (interview program, invites encouraged) | Common |
| Entity claiming + public response | A | A | A | A (response with vendor badge) | 4/4 → Common (not definitional: unclaimed records still accumulate reviews) |
| Pay-vs-influence firewall (pay ≠ removal/ranking) | A (explicit) | A- (disclosure posture) | A (grid placement not manually changeable; guidelines) | A (cannot delete; methodology published; sponsored labeled) | 4/4 → Key behavior |
| Reviewer community/reputation layers | A (levels/points) | — | A (discussions) | A (Q&A, messaging) | Optional |
| Review age weighting/expiry | A (recency weighting) | — | A (decay curve) | A (24-month expiry) | Common (mechanism product-specific) |

## Canonical Model

### L0 — Defining Invariant (minimal; jointly-held, remove any leg → different Type)

1. **Reviewed-entity record** — a persistent, identified record of a third-party offering/experience (business, product, service, provider), held and operated by the platform, existing and accumulating independent of the entity's participation; the entity cannot remove it.
   - Remove → listings with no evaluation = Directory Application territory.
2. **First-hand evaluation record (the review)** — a rating plus a written account (media common), submitted on the platform by a registered user who is neither the reviewed entity nor affiliated with it, describing their own experience; eligibility and authenticity governed by platform rules (first-hand-only, conflict-of-interest exclusion, identity under platform policy).
   - Remove first-hand/non-affiliation → testimonial board/marketing asset, not a review platform. Remove the record entirely → catalog of bare scores with no underlying accounts.
3. **The public decision-serving corpus** — reviews persist and accumulate on the entity record; the platform operates the corpus for the benefit of prospective buyers evaluating that entity (third parties to any transaction), publishing individual accounts and summaries. Not a private feedback channel for the entity.
   - Remove public third-party serving → Voice-of-Customer / private feedback collection territory.

Jointly-held load-bearing checks: 1 alone = directory; 2 alone = free-floating feedback stream; 1+2 without 3 = private/internal review collection; 2+3 without 1 = unanchored commentary (social/comment territory); 1+3 without 2 = aggregate-scores-only catalog (degenerate).

### L1 — Common Mature Structure (near-universal in sample, not definitional)

- Aggregate summary over the corpus (average score + count) — universal in sample, mechanism varies (simple average, recency-weighted, points-based, derived-from-form-question).
- Moderation/authenticity control before or shortly after publication — 4/4, with pre-publication gates documented at 3–4/4 and investigation-driven filtering documented too.
- Reviewer registration and identity verification under some policy (email/LinkedIn/ID); anonymous display options at 2/4.
- Discovery surfaces: categories, search, top/ranked lists; comparison/alternatives pages at 2/4 (and documented as capability inside the Comparison sibling).
- Entity-side participation: claiming, public response, review invitations/collection tools, usage rules against cherry-picking/segmentation.
- Age weighting/expiry of reviews in aggregates (3/4 documented).
- Anti-fraud machinery (automated detection, human review, community reporting) (4/4).
- Review lifecycle self-service: edit/update/delete by the reviewer (3/4 documented explicitly).

### L2 — Variant / Optional Structure

- Domain scope: general consumer (any business), consumer-vertical (restaurants, travel — travel split into its own leaf), B2B software, enterprise tech services, employers (Glassdoor-class — unreachable this pass, variant asserted only structurally).
- Collection philosophy: organic walk-in reviews vs entity-invited/automated invitations vs incentive campaigns (gift cards) vs platform-run interviews (editorial write-ups).
- Rating scale and aggregate philosophy (5-star vs 10-point; weighted recency vs decay curves vs points ranks vs quadrant reports).
- Editorial involvement (staff-written titles, curation into guides, phone interviews).
- Monetization model (seller subscriptions, sponsorships, opt-in leads, buyer-intent data, no-ads pledges).
- Community layers (contributor levels, Q&A, discussions, private messaging, reviewer reputations).
- Media depth (photos, video reviews, voice-AI submission).
- Anonymous display, verified-purchase badges, verified-identity badges.
- Regional platforms and platform-native embedded realizations (map/social/commerce platforms hosting the same structure as a capability).

### L3 — Vendor-specific (Research Notes only)

- Sitejabber/SmartCustomer: 50/25/25 rating weighting; 48-hour posting norm; ~30-day investigations; invitation-label taxonomy; Persona ID verification; Instant Feedback separate score; FTC cooperation posture; contribution-point values; Section 230/CRFA framing; free-plan verification-request caps.
- ConsumerAffairs: phone-interview collection; concierge service; "Authorized" paid brand designation; NMLS licensing disclosures (adjacent monetization).
- G2: Flesch-Kincaid readability weighting; review-decay curve (90-day/18-month/3-year→~3% shape); star = recommend-question ÷ 2 rounded to half star; Grid thresholds (10+ reviews/product; 150+ per category; 6+ products); segment definitions (≤50 / 51–1000 / 1001+ employees); Pros/Cons 18-month window + 30-day refresh cadence; Market Presence third-party sources (ZoomInfo/LinkedIn/Crunchbase/Moz/Similarweb/STAT); AI Users Trust badge program (beta); review syndication partner program; MCP server; merger/acquisition handling rules.
- PeerSpot: methodology points 25/15/10/25/25; 24-month expiry; reseller exclusion; vendor inclusion criteria (≥50 employees, ≥10 enterprise customers, enterprise = ≥1000 employees or ≥$250M revenue); ~600-word review depth target; editorial titles keyed to rating bands; red fake-review vendor badge; interview-review share (<10%) disclosure; sponsored-label rules.

## Rejected Findings (overfit risks examined and rejected)

- "Reviews must be star-rated on a 5-point scale" — rejected: scales differ (5-star, 10-point, derived stars); the invariant is a rating, not a scale.
- "Reviews must be short organic accounts" — rejected: G2 survey-style and PeerSpot ~600-word interview-supported reviews are in-type; the invariant is first-hand evaluation, not length/organic origin.
- "Aggregation must be a simple average" — rejected: weighted recency, decay curves, points systems all in-sample; only the existence of a summary is common, and even that is presentation, not definition.
- "Reviewers must be incentivized" — rejected: incentive regimes conflict across sample (banned for company reviews at one pole, gift-card campaigns at another).
- "The platform must refuse any payment from the reviewed party" — rejected: all sampled platforms monetize seller-side; the invariant is the firewalled influence (pay ≠ removal/ranking), not zero payment.
- "B2B review sites are a different Type" — rejected: same three-leg core; differences (structured forms, verified identity, firmographic ranking) are L1/L2.
- "Critics' review aggregators belong in-type" — rejected (boundary): external editorial reviews are not submitted on the platform by its own users; fails leg 2.

## Boundary Findings

- **vs Comparison Platform (§02.10 sibling — JOINT REVIEW FLAG DISCHARGED)**: seam = evaluation of one vs comparison across many. Review Platform centers on accumulated first-hand evaluations of single entities read to judge one; Comparison Platform centers on aligned multi-option presentation to choose among many. Cross-evidence: G2 and PeerSpot both ship alternatives/comparisons surfaces, and the Comparison sibling documents user reviews as a standard capability there — the seam is the center of gravity, so keep-both. Consistent with sibling's recorded seam.
- **vs Directory Application (§02.11)**: both hold entity records with discovery; a directory's center is the listing/contact/enrichment record, a Review Platform's center is the evaluation corpus. Remove reviews from a review platform → directory; the reverse does not hold.
- **vs Travel Review Platform (§26 sibling leaf)**: travel reviews carry stay/inventory-specific record semantics and booking adjacency → separate leaf; here held as domain variant evidence only (no deep travel claims made).
- **vs embedded commerce/marketplace/app-store reviews**: identical structure realized as a capability inside a transaction platform (reviewed entity = product listing); the standalone Type's corpus is the product itself. Boundary, not merge.
- **vs Voice of Customer Platform (§07)**: VOC = company-side private collection/analysis of feedback; review platform = public corpus served to third parties. 1+2-without-3 test.
- **vs Q&A Community (processed)**: evaluative records bound to entities vs questions with community-produced answer authority; Q&A coexists as capability (PeerSpot/G2 discussions).
- **vs Online Forum / Community Platform**: discussion threads vs entity-bound evaluation corpus; forums may contain reviews but the thread is the unit.
- **vs editorial/critic aggregation**: external professional reviews aggregated (not user-submitted on-platform) = below-type/boundary case; sample contains editorial involvement (titles, curation) only around user-submitted reviews.

## Historical / Market-Sample Check (§24)

- Older/regional products: Sitejabber itself dates to 2006 ("Since 2006") and ConsumerAffairs to 1998 — both satisfy the three-leg core with no modern machinery (no AI, no in-app prompts, no firmographic scoring). Late-1990s/2000s paid-community review sites (Epinsions/Ciao/dooyoo-class) satisfy conceptually: entity + member reviews + ratings + community (conceptual — not directly documented this pass).
- Platform-native realizations (map platforms, app stores, marketplace product reviews): structurally identical (entity record + attributed rating/account + aggregate) as an embedded capability; no precise claims made (Google help unreachable).
- Pre-web analog: published consumer-advocacy columns/letters collecting customer accounts about named businesses — conceptual lineage, satisfies legs conceptually; not asserted as in-type history.
- Definition names no star scale, no moderation SLA, no incentive scheme, no "free-to-list", no specific verification vendor, no web/SaaS form, no AI — all era/market machinery.

## Uncertainties

1. Yelp and Trustpilot — the two most-cited consumer review platforms — could not be fetched; consumer-local mechanics (e.g., Yelp's review-recommendation filtering, Trustpilot's invitation/label system) are NOT asserted anywhere in the final document. Consumer-general evidence rests on Sitejabber/ConsumerAffairs + B2B commonality.
2. Glassdoor (employer reviews) unreachable — employer-review pole asserted only as a structural variant.
3. Platform-native reviews (Google Maps) — timeout ×2; embedded-capability boundary documented conceptually only.
4. Whether anonymous-display reviews are common or variant — documented at 2/4 (G2, PeerSpot); held variant-leaning-common, not generalized.
5. Whether pre-publication moderation vs post-publication filtering splits by segment — sample shows pre-publication gates everywhere, with investigation-filtering on top at Sitejabber; held as "mechanism varies" without segment generalization.
6. Incentive regimes conflict (banned-for-company-reviews vs gift-card campaigns); documented as variant, no normative claim.

## Final Synthesis

A Review Platform is the public system of record for first-hand customer evaluations of third-party offerings. Its defining core is three jointly-held structures: (1) platform-held reviewed-entity records that exist and accumulate independent of the entity; (2) first-hand, non-affiliated, attributed evaluation records (rating + account) admitted under platform eligibility and authenticity rules; (3) a public corpus operated for prospective buyers — individual accounts plus summaries, not a private feedback channel for the reviewed party. Everything else — aggregate formulas, rankings and reports, verification depth, incentives, collection machinery, editorial curation, monetization — is standard capability or variant machinery layered on that core. The sharpest boundary is the processed sibling Comparison Platform (evaluation of one vs comparison across many, keep-both); other seams: Directory (records without the corpus), VOC (corpus without the public third-party serving), embedded commerce reviews (structure as capability), forums/Q&A (different record units).
