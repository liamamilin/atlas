# Research Notes — Referral Marketing Platform

## Research Goal

Understand what a Referral Marketing Platform actually is as an Application Type: its core objects, the referral workflow from advocate enrollment to reward fulfillment, the operator-side program machinery, and the boundaries against Affiliate Management Platform, Loyalty Program Management, Customer Advocacy Platform, and Lead Generation Platform.

## Initial Boundary

Initial hypothesis before research:

- Core use: brands run "refer-a-friend" style programs — existing customers share personal links/codes, friends convert, both sides get rewards.
- Users: marketers / growth / retention teams on the brand side; consumers as advocates and referred friends.
- Nearest neighbors: Affiliate Management Platform (who participates?), Loyalty Program Management (what is rewarded?), Customer Advocacy Platform (reviews/UGC vs referral), Lead Generation Platform (channel vs program machinery).
- Unknowns: is two-sided reward definitional? Is e-commerce checkout the canonical conversion event? Is the platform always a standalone product or often a module? Where exactly does affiliate end and referral begin, given products increasingly run both?

## Research Questions

1. What are the core objects? (program/campaign, advocate, referral link/code, referred friend, referral/qualifying action, reward)
2. What is the defining workflow? (enrollment → share → track → attributed conversion → qualification → reward → payout)
3. What reward types and incentive structures exist? One-sided vs two-sided? Tiers/milestones?
4. How does attribution work? (links, coupon codes, name-based/offline matching?)
5. What eligibility/fraud rules govern rewards? (review periods, new-customer requirement, self-referral, leaked codes)
6. What interfaces exist for merchant, advocate, and referred friend?
7. How do variants differ by industry (e-commerce vs services vs SaaS vs offline) and by customer tier (self-serve app vs enterprise platform)?
8. Where are the boundaries with affiliate, loyalty, advocacy, and lead-gen Types?

## Representative Products

Selected for market coverage across customer tier and product philosophy:

| Product | Tier / posture | Why sampled |
|---|---|---|
| ReferralCandy | self-serve SaaS app, e-commerce (Shopify-centric), since 2010 | deepest public help center; canonical e-commerce referral app |
| Friendbuy | D2C / mid-market & enterprise; referral + loyalty + influencer on one platform | suite-posture pole; services-led onboarding |
| Extole | enterprise "offer management" platform | broadest program surface (refer-a-friend + ambassador + employee + friends-and-family + loyalty + sweepstakes); developer/API depth |
| Mention Me | enterprise, services-led, EMEA | measurement-first philosophy (offline/name-based capture, benchmarking, eLTV) |
| ReferralRock | SMB/mid-market operator-focused; referral + ambassador + affiliate | advisor-led posture; explicit multi-program-type platform; boundary anchor vs affiliate |

Additional market context (observed, not part of the core sample): ReferralHero (self-serve multi-industry referral/affiliate/waitlist/contest; homepage). Known names not fetched this pass: Buyapowa, GrowSurf, SaaSquatch, Viral Loops, Talkable, Yotpo referrals, Ambassador.

## Sources

All research performed 2026-09-07 via live fetch.

Tier 1 (operational documentation):

- ReferralCandy Help Center (Intercom) — full collection index: https://help.referralcandy.com/en/
- ReferralCandy — "When will referral rewards be sent to an advocate?" — https://help.referralcandy.com/en/articles/2457782-when-will-referral-rewards-be-sent-to-an-advocate
- ReferralCandy — "Campaign states" — https://help.referralcandy.com/en/articles/8469203-campaign-states

Tier 2 (official product pages):

- ReferralCandy — https://www.referralcandy.com/
- ReferralHero — https://www.referralhero.com/
- Friendbuy — https://www.friendbuy.com/
- Extole — https://www.extole.com/
- Mention Me — https://www.mention-me.com/
- ReferralRock — https://referralrock.com/

Known but not used this pass (listed for future deepening): support.friendbuy.com, developers.friendbuy.com, docs.mention-me.com, success.extole.com, docs.extole.com, support.referralhero.com, referralrock.com/product pages.

Source-access limitations:

- support.extole.com (Zendesk help center) returned an empty response on first fetch; www.extole.com was used instead. Extole operational detail below is homepage-level (Tier 2), not help-center depth.
- ReferralHero, Friendbuy, Mention Me, Extole, ReferralRock observations below are homepage/product-page level (Tier 2). Per evidence rules, claims drawn only from those pages are marked B (cross-product commonality from pages) or kept product-specific; no precise numeric limits are asserted for them in the final document.

## Product Observations

### ReferralCandy (Tier 1: help center + homepage)

Evidence layer: A (direct observation of official operational docs).

Core concepts:

- **Campaign** is the configuration unit. Multiple campaigns can run in parallel, each with its own target audience (segments: targeted and excluded), themes, rewards. Campaign states: **Stopped** (default for new; editable, invisible to customers), **Live** (enrollment, referrals, rewards processing work; emails/widgets/pages accessible), **Paused** (enrollment disabled; pages show paused notice; reward emails for pre-pause purchases still sent; post-pause purchases marked non-rewardable). Deleting a campaign is not possible — deactivate via stop/pause.
- System auto-stops live campaigns when: friend coupon code expires, single-use coupon codes run out, account suspended, a selected Shopify collection is deleted, or a subscription integration (Recharge/Bold/PayWhirl) errors or disconnects.
- **Contacts (customers)**: searchable list; import customers; edit; ban a contact; subscribe/unsubscribe; download lists. Contacts can be grouped into segments used as campaign audiences.
- **Advocates & affiliates**: hold a unique referral link and referral code (customizable); sign in to advocate/affiliate portals; view earned rewards. Merchant can look up which discount code belongs to which advocate.
- **Friend offer**: what the referred friend gets (offer types; promo link; coupon application at checkout).
- **Referral reward** (advocate reward): types = coupon (created in Shopify Discounts after each successful referral), store credit (applied to advocate's customer account), cash (PayPal, Tremendous), gift cards (via Tremendous), free product (send a SKU), custom (merchant fulfills manually). **FlexiTiers** = tiered rewards (advocate must reach a minimum number of referrals per tier; a non-rewarding referral triggers a "referral progress" email).
- **Reward lifecycle** (high-value rules, directly observed):
  1. A referred purchase must qualify as rewardable AND the **purchase review period** must end (auto-elapse, or merchant manually approves the referral on Shopify). No reward of any type is issued before that.
  2. Then by reward type: coupon / store credit issued immediately; custom sends alerts to both parties with merchant-side fulfillment; cash adds payout-rail steps — PayPal (queued; paid after merchant pays the monthly cash-rewards invoice; PayPal processes in 1–3 days), Tremendous invoice-funded (after monthly invoice) or balance-funded (immediate if funded), self-managed (affiliate campaigns only: export payout CSV, pay outside, re-upload marked paid).
  3. Non-rewardable conditions (explicit statuses): exceeds the allowed number of rewardable friend purchases; below minimum purchase amount; purchase refunded/cancelled/deleted; advocate banned; purchase made while campaign paused.
  4. Other reward blockers: referred friend already an existing customer (only new customers eligible); tier minimum not reached; PayPal email not linked (advocates can only set PayPal email via portal after first reward).
- **Marking purchases as referred + approving referrals**; deleting a purchase and disqualifying a referral (manual correction paths).
- **Fraud prevention**: automated fraud prevention mechanisms; fraud history views; "how to handle fraud"; homepage claims detection of self-referrals, suspicious spikes, and codes leaked to coupon sites before payout.
- **Emails** (campaign email settings): welcome email, reminder emails, reward emails, win-back email; marketing email preferences; custom email domain; spam-prevention measures.
- **Widgets/surfaces**: post-purchase popup (e.g., on Shopify thank-you page), embedded signup, floating referral widget, join block, friend-offer landing page and popup, customer referral details extension; themes/Liquid customization; editable social sharing messages (X, Facebook, WhatsApp); A/B testing.
- **Integrations**: store platforms (Shopify one-click, WooCommerce plugin, BigCommerce, Magento/Adobe Commerce, Cratejoy, Squarespace, LearnWorlds, Acuity, custom via email/JavaScript/API), subscription apps (Recharge, Bold, sticky.io, PayWhirl, Seal, Loop, Skio, Awtomic, Stay AI…), ESP/CRM (Klaviyo with referral events/properties, Mailchimp, Customer.io), analytics (Google Analytics, Meta Pixel, AdRoll, Google Ads), reward rails (Tremendous), Zapier.
- **Adjacent program types in the same product**: affiliate campaigns (sign-up page, affiliate signup management, custom coupon codes affiliates can "say out loud", commissions by product/tier/per-affiliate, automated payouts via PayPal/Venmo/Tremendous virtual Visa/bank transfer, "one invoice to you, no 1099 paperwork", self-managed payout CSVs) and loyalty campaigns (Shopify; reward repeat purchases with store credit).
- **Account/store settings**: currency, multiple languages, time zone, program subdomain, custom domain for the referral portal, plans/billing, 1099s & tax reporting, 2FA.
- Homepage analytics surface: advocates, share page visits, shares, referrals, revenue from referrals over time; "every reward traces back to a verified sale".

### Friendbuy (Tier 2: homepage)

Evidence layer: B (official product page).

- Positioning: referral, loyalty, and influencer/creator programs "built on a unified growth platform"; enterprise-leaning with white-glove onboarding (dedicated Onboarding Manager and Solutions Architect), migration of historical customer data.
- Referral product bullets: Advocate Activation; Rewards & Incentives; Testing & Optimization; Fraud Prevention; Product Sharing.
- Rewards: "any reward type, including coupons, account credit, points, 3rd party gift cards, and custom rewards"; rules-based rewards engine incentivizing "referrals, purchases, birthdays, and milestones"; SKU-based rewards, VIP tiers.
- Analytics: track program impressions, shares, referral visits, conversions; goals such as new customer acquisitions, referral purchases, revenue; A/B test offers, email subject lines, and the referral funnel; measure LTV of advocates and referred friends.
- Integrations: Shopify (Plus), Klaviyo, Attentive, Braze, Recharge, Segment; rewards like discounts, account credit, free products, auto-applied free months; add acquired emails/phones to CRM; incentivize email/SMS subscription or review submission.
- Industries beyond e-commerce: financial services, consumer services, telecom, travel & hospitality, retail & e-commerce.
- Claims (vendor-stated, not verified): 5–25% of new-customer acquisition driven by referral programs on the platform; 25x average ROI.

### Extole (Tier 2: homepage; help center unreachable)

Evidence layer: B (official product page).

- Positioning: "enterprise offer management platform" for referral, loyalty, and other incentive-based programs; personalization, automated rewards, performance analytics.
- Program catalog (named program types): Refer-a-Friend; Influencer & Ambassador Programs; Employee Ambassadors; Drop-a-Hint; Welcome Offer (acquisition); Friends and Family; Loyalty; Nominations; Sweepstakes (retention).
- Platform features: Flow Builder; Reward Bank; Full API ("three REST APIs: server, consumer, and management"; OpenAPI spec; scoped bearer tokens); SDKs (JavaScript, iOS, Android, React Native); CLI (inspect rewards, trace a reward from earned to redeemed, stream events/webhook activity, run reports in JSON/JSONL/CSV); MCP server (operate programs from AI assistants with the user's permissions); Go Extole mobile app.
- Industries: banks & credit unions, consumer fintech, telecom, retail, travel & hospitality, franchisor.
- Security posture: ISO/IEC 27001, GDPR/CCPA/EU-US DPF, scoped permissions and audit logging.
- Notable workflow language: reconciliation ("why don't our qualified accounts match our fulfilled rewards"), click-spike investigation, per-reward traceability (find-coupon, trace earned→redeemed).

### Mention Me (Tier 2: homepage; docs.mention-me.com listed but not fetched)

Evidence layer: B (official product page).

- Positioning: enterprise "Referral Marketing Platform"; measurement-first. Claims: £4bn+ revenue driven, 58m+ advocates identified, 45,000+ programmes optimized, 500+ brands, 13 years (vendor-stated claims).
- Named capabilities: **NameShare®** (capture offline word-of-mouth — "just say my name at checkout" — tracked without a link); **Earned Referral** (measure organic/dark-social word of mouth happening outside the program); **A/B Testing & Optimisation** (built on a cross-network test base); **Benchmarking** (program performance vs category); **eLTV** (expected lifetime value of referred customers); **Global Readiness** (localization, governance, compliance across markets).
- Attribution claim: "Every referral is tied to a named advocate and a unique conversion path."
- FAQ: most brands go live in 1–3 days (claim); pricing tailored to AOV and referral volume; dashboard covers share → new customer acquisition → revenue → referred-customer lifetime value; native ESP/CRM integrations.
- Integrations: Klaviyo, Emarsys, Braze, Bloomreach, Salesforce Marketing Cloud, Attentive, Meta, Google Ads, TikTok, Dotdigital, Ometria, mParticle, Feefo, Trustpilot.

### ReferralRock (Tier 2: homepage)

Evidence layer: B (official product page).

- Positioning: "referral program software that runs in the background" for operators (home services, professional services, clinics/healthcare, financial services, franchises/multi-location, agencies, SaaS, e-commerce); dedicated advisor on every plan (advisor-led setup).
- Program types on one platform: **Customer referral**, **Brand ambassador** (invite-only; customers/partners/employees/influencers), **Partner & affiliate** (own portal for partners).
- Enrollment machinery: automated invites "only to customers who haven't joined yet"; **Program Recruiters** — frontline/service teams enroll customers with credit to the rep; passwordless one-click access (no account to create).
- Member experience: branded member portal; share by link, email, text, or social; track every referral and reward in real time; notifications.
- Reward machinery: two-sided, tiered, and milestone rewards; automatic payouts in gift cards, cash, or credit ("no commission taken").
- Service/B2B shape: "reward at any CRM stage: a new lead, a closed deal, or a completed job"; native HubSpot & Salesforce sync — conversion is not checkout-only.
- Fraud: IP tracking, duplicate-entry detection, suspicious-activity monitoring.
- Integrations: 50+ (CRM, e-commerce, email) — HubSpot, Salesforce, Shopify, Zapier, Mailchimp, Stripe.
- Multi-org: separate program per location/branch/brand, consolidated reporting, single admin dashboard.
- FAQ claims (vendor data, keep as claims): of 952 programs analyzed, 54% rewarded only the referrer; gift cards most popular member reward (61%); 92% use fixed amounts; stalled programs mostly from inconsistent promotion (82% claim); metrics listed: shares, unique people reached, referrals, conversion rates, CAC via referral, LTV of referred customers, program revenue and costs.

### ReferralHero (Tier 2: homepage — market context only)

Evidence layer: B.

- Journey: customers sign up → get a unique referral link → share (word of mouth, text, social) → friend becomes a new customer (books a service, starts a subscription, makes a purchase) → original customer unlocks a reward.
- Growth tools: referral, affiliate, waitlist & contest (viral-loop campaign style). Industries: dentists, fintech, home services, med spas, mobile apps, offline business, SaaS. Plug-and-play widgets or full API integration; analytics dashboard; NPS module.

## Cross-product Comparison

| Structure | ReferralCandy | ReferralHero | Friendbuy | Extole | Mention Me | ReferralRock |
|---|---|---|---|---|---|---|
| Program/campaign as config unit | Campaign (multi, with segments) | Campaign (referral/affiliate/waitlist/contest) | Program (referral/loyalty/influencer) | Program (offer program types) | Programme | Program (customer referral/ambassador/affiliate) |
| Advocate = existing customer with personal trackable identity | ✔ unique link + customizable code | ✔ unique referral link | ✔ advocate activation + sharing | ✔ | ✔ "named advocate" + NameShare (name instead of link) | ✔ member with link + portal |
| Friend-facing offer/landing surface | ✔ friend offer landing page & popup | ✔ | ✔ product sharing | ✔ (Drop-a-Hint etc.) | ✔ | ✔ landing/sharing pages |
| Referral attribution recorded per conversion | ✔ purchases & referrals page; mark as referred | ✔ | ✔ attribution & measurement | ✔ events API + reward trace | ✔ named advocate + conversion path | ✔ tracked back to source |
| Conversion event shape | e-commerce purchase (checkout, coupon/link) | purchase / signup / booking | purchase + other incentivized actions | program-defined events (API events) | purchase (incl. offline name redemption) | purchase OR CRM-stage event (lead/deal/job) |
| Reward types | coupon, store credit, cash, gift cards, free product, custom | reward unlock (types vary) | coupons, account credit, points, 3rd-party gift cards, custom | Reward Bank (automated rewards) | incentives (testing-led) | gift cards, cash, credit |
| Reward gating before issuance | ✔ review period + rewardable conditions (explicit statuses) | qualifying action | not detailed on page | reconciliation/trace language | not detailed on page | automated payout rules |
| Eligibility rule: referred must be new customer | ✔ explicit | ✔ (friend becomes "new customer") | implied (acquisition framing) | implied (acquisition) | ✔ (advocates bring "new customers") | implied |
| Fraud prevention | ✔ automated mechanisms + fraud history | not detailed | ✔ product bullet | ✔ reconciliation / spike investigation | not applicable framing | ✔ IP/duplicate/activity |
| Advocate-side portal | ✔ advocate & affiliate portals | ✔ participant dashboard | ✔ | ✔ Go Extole app / share surfaces | ✔ (share pages) | ✔ branded member portal |
| Program emails | ✔ welcome/reminder/reward/win-back | — | via ESP integrations | — | via ESP integrations | ✔ built-in campaigns |
| Analytics | shares/visits/referrals/revenue dashboard | ✔ dashboard | impressions/shares/visits/conversions/LTV | reports + AI queries | share→acquisition→revenue→eLTV + benchmarking | shares→reach→referrals→CAC/LTV |
| A/B testing | ✔ | — | ✔ | ✔ (Flow Builder-era; testing bullet in referral) | ✔ flagship capability | not stated as product feature |
| Enrollment automation | post-purchase prompt, import, segments | sign-up widgets | advocate activation | program types | advocates identified | automated invites + recruiters |
| Affiliate/ambassador in same product | ✔ affiliate campaigns | ✔ affiliate | ✔ influencer & creator | ✔ influencer & ambassador, employee ambassadors | ✘ (referral-first) | ✔ ambassador + partner/affiliate |
| Loyalty in same product | ✔ loyalty campaigns (Shopify) | ✘ | ✔ loyalty programs | ✔ loyalty | ✘ | ✘ |
| Offline / non-link referral capture | ✘ | ✘ | ✘ | ✘ (not on page) | ✔ NameShare | ✘ |
| Multi-location / multi-program governance | multi-campaign | — | — | enterprise | global readiness | ✔ per-location programs + consolidated reporting |
| Developer surface | email/JS/API integration | API + widgets | integrations + developers portal | three REST APIs, SDKs, CLI, MCP | integrations | 50+ integrations, Zapier |
| Services posture | self-serve SaaS | self-serve + support | white-glove onboarding | enterprise platform | expert-led / outsource pitch | advisor on every plan |
| Customer tier | SMB/D2C e-commerce | SMB/startup | mid-market/enterprise D2C | enterprise | enterprise | SMB/mid-market |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A brand-operated system that turns existing customers into a tracked, rewarded acquisition channel. Minimal structure:

```text
Brand-operated referral program (configured incentives & eligibility)
└── Advocate: an existing customer/member holding a personal, trackable referral identity
    (unique link and/or code — or an equivalent personal token)
    └── Share surface: the advocate passes the offer to people they know
        └── Referral attribution: the referred person's qualifying conversion
            (typically a purchase or signup) is recorded as belonging to that advocate
            └── Reward: the program grants the configured incentive
                when the referral qualifies
```

Tests:

- Remove the advocate's personal trackable identity + attribution → it is just a discount/promo campaign (Promotion Management), not a referral platform.
- Remove rewards/incentives → it is a share-link tool or analytics gadget, not a marketing program platform.
- Make the participants registered external partners instead of the brand's own customers → Affiliate Management Platform.
- Reward the customer's own repeat purchases instead of bringing others → Loyalty Program Management.

Not in L0 (deliberately):

- **Two-sided rewards** — the two-sided "give $, get $" pattern is the category's most common shape and best practice, but one-sided programs are first-class in the sampled products (ReferralCandy's reward conditions explicitly handle advocate-only tiers; ReferralRock's own published analysis states most real programs reward only the referrer). Reward symmetry is a program design choice.
- **E-commerce checkout as the conversion event** — canonical conversion is "the referred person's qualifying action", which can be a purchase, signup, booking, subscription start, or a CRM-stage event (ReferralRock rewards at lead/closed-deal/completed-job stages; ReferralHero names bookings and subscriptions).
- **Unique URLs / cookies** — Mention Me's NameShare tracks referrals with a spoken name instead of a link; the invariant is the *personal trackable identity*, not the link mechanics.
- **Widgets, emails, languages, A/B testing, fraud tooling depth** — all mature-market additions, not definitional.

Historical check: pre-web "member-get-member" programs (paper forms / member codes at telcos, banks, ISPs) and early web-era programs (e.g., unique referral links granting account credit) satisfy this minimal core without any of the modern app-store/widget machinery. The definition does not over-fit the current Shopify-app era.

### L1 — Common Mature Structure

Present across most sampled products; needed to make the Type operational, but not definitional:

- Program/campaign as the configuration unit: incentive design (advocate reward + friend offer), eligibility conditions, target audience/segments; program states (live/paused/stopped) with system auto-stop on misconfiguration (expired coupons, broken integrations).
- Enrollment/activation machinery: post-purchase prompts, embedded widgets/blocks, automated invites to not-yet-joined customers, customer import/segments.
- Advocate-side experience: personal portal/dashboard with the unique link/code, share channels (link copy, email, social, messaging), reward status and progress toward tiers.
- Friend-facing surface: offer landing page / popup that carries the friend offer into checkout or signup.
- Referral tracking & attribution: link click-through and/or coupon-code redemption tied back to the advocate; per-conversion referral records; manual correction (mark as referred, approve, disqualify).
- Reward fulfillment machinery: multiple reward types (discount coupon, store credit, points, cash, gift cards, free product, custom), payout rails and queues, and a qualification gate (review period / approval / rewardable conditions) before issuance.
- Eligibility & fraud rules: referred person must be a new customer; self-referral detection; duplicate/IP/leaked-code detection; advocate banning; minimum purchase amounts; caps on rewardable referrals per advocate.
- Analytics: share → click/visit → referral → conversion → revenue funnel; referred-customer quality (LTV, repeat rate); CAC; export/reporting.
- Program communication: welcome/reminder/reward/win-back emails (built-in or via ESP integrations).
- Integrations: e-commerce platform / CRM / billing as the source of conversion events; ESP/SMS for communication; analytics pixels; reward payout services.
- A/B testing and optimization of offers, placements, and messages.
- Adjacent program types shipped by the same products: affiliate, ambassador, influencer, loyalty, employee advocacy, sweepstakes/friends-and-family.

### L2 — Variant / Optional Structure

Depends on segment, geography, business model, or customer scale:

- Industry shape: e-commerce checkout-triggered (ReferralCandy/Friendbuy) vs CRM-stage-triggered for services/B2B (ReferralRock) vs in-person/offline name redemption (Mention Me) vs mobile-app/SaaS event-based (ReferralHero, Extole SDKs).
- Program scope of the product: referral-only vs referral+affiliate hybrid vs referral+loyalty+influencer unified growth suite vs enterprise offer-management platform with many program types.
- Campaign style: evergreen refer-a-friend vs time-boxed viral loops (waitlists, contests, milestone ladders).
- Measurement philosophy: execution-first (run the program) vs measurement-first (dark-social attribution, offline capture, cross-category benchmarking, eLTV modeling).
- Services posture: self-serve SaaS app vs advisor-led onboarding vs white-glove enterprise with dedicated architects vs outsourced program management.
- Scale/governance: multi-campaign with audience segments vs multi-location/franchise program hierarchies with consolidated reporting vs global multi-market localization/governance/compliance.
- Developer depth: drop-in widgets vs REST APIs/SDKs/CLI/event streams (mobile-app programs) vs AI/MCP-operated consoles.
- Reward economics: merchant-funded discounts/store credit vs cash via third-party payout rails vs points currencies bridging into loyalty.
- Compliance surface: payout tax reporting (e.g., 1099 handling), marketing-consent handling, regional privacy regimes.

### L3 — Vendor-specific Structure

Kept out of the final document; examples:

- ReferralCandy: FlexiTiers, specific campaign-state table and system auto-stop triggers, PayPal/Tremendous funding mechanics ("pay monthly cash-rewards invoice first"), purchase review period mechanics, specific widget names, loyalty campaigns on Shopify, "one invoice, no 1099" affiliate payout framing.
- Mention Me: NameShare®, Earned Referral, benchmarking claims (45,000+ tests), Referral Engineering® positioning, £4bn/58m advocates claims.
- Extole: Reward Bank, Flow Builder, Go Extole app, MCP server, Drop-a-Hint and Welcome Offer program names, three-API split.
- Friendbuy: unified referral+loyalty+influencer framing, receipt scanning, wallet passes.
- ReferralRock: Program Recruiters, advisor-on-every-plan, 952-program dataset claims (54% referrer-only, 61% gift cards, 92% fixed amounts), 3 P's of promotion.
- ReferralHero: waitlist/contest campaign types, per-industry landing pages, NPS module.

## Vendor-specific Findings

- Two-sided rewards are the marketed norm, but the sampled evidence (ReferralCandy's explicit one-sided tier handling + ReferralRock's published program analysis claiming a majority of programs reward only the referrer) indicates one-sided remains widespread. The final document should present two-sided as common and recommended, not definitional.
- The referral-vs-affiliate convergence is structural: three of six sampled products ship affiliate programs natively in the same platform (ReferralCandy, ReferralRock, Extole; ReferralHero and Friendbuy too). The Type boundary is in the participant population and incentive shape, not in the vendor packaging.
- Reward gating (review period before payout) is directly documented only in ReferralCandy; other products show reconciliation/trace language (Extole) or payout automation (ReferralRock) without publishing the gating model. Treat "reward lifecycle with a qualification gate" as strongly evidenced for e-commerce pole and structurally implied elsewhere; avoid asserting specific gating rules as universal.

## Boundary Findings

- **vs Affiliate Management Platform** (sharpest seam): affiliate participants are external registered partners (creators, publishers, media buyers) who apply to a program and earn commissions on tracked sales; referral participants are the brand's own customers sharing with personal contacts, with rewards typically taking the form of discounts/credit/gifts for both sides. Same tracking mechanics (links/codes) — different participant population, enrollment flow (application/approval vs automatic from the customer base), and incentive semantics (commission vs friend reward). Because the same platforms ship both, the products cannot be used to separate the Types; the participant/incentive test must be used. If the directory treats them as one Type, referral becomes a participant-variant; as two Types, the seam is participant population.
- **vs Loyalty Program Management**: loyalty rewards the customer's own repeat behavior (points on purchases); referral rewards the arrival of *other* people. Overlap: shared currencies (points/store credit) and shared vendors (Friendbuy, ReferralCandy's loyalty campaigns). Test: what action does the reward attach to — own purchase vs referred person's qualifying action.
- **vs Customer Advocacy Platform**: advocacy platforms bundle reviews, UGC, references, community, and referral as one motion among several; a referral platform's world is the referral program itself (offer design, attribution, reward fulfillment). Mention Me straddles by positioning referral as the core of customer advocacy.
- **vs Lead Generation Platform**: referral is one acquisition channel with its own program machinery; lead-gen platforms are broader multi-channel capture/qualification systems. Referral products generate leads as a byproduct (ReferralRock's CRM-stage rewards) but are not lead-gen systems.
- **vs Promotion Management / discount tooling**: a referral platform's offer is bound to a personal relationship (advocate→friend), not to a general promo; without advocate identity + attribution it degrades into promotion software.
- **vs plain share-link tools / in-product referral features**: many SaaS products embed "invite friends, get credit" natively. A Referral Marketing Platform is the standalone system that brands adopt to run such programs across channels with reward fulfillment, fraud control, and reporting — the feature inside a SaaS product is an instance of the same pattern, not a competing Type.

## Uncertainties

1. Reward-gating details outside ReferralCandy (review periods, approval queues) are not directly observed; the generalization "a qualification gate precedes reward issuance" is inferred structurally (fraud + refund-prone purchases make it necessary) and supported by Extole's reconciliation language — kept at moderate strength in the final document.
2. Mention Me's docs (docs.mention-me.com) were not fetched this pass; NameShare mechanics are known only at marketing-page depth. No mechanics claims made in the final document beyond "tracks name-based offline referrals".
3. Extole's help center was unreachable; its reward-bank/reconciliation mechanics are described only structurally.
4. Whether "only new customers are rewardable" is universal: explicit in ReferralCandy; acquisition framing implies it elsewhere, but products may allow existing-customer rewards in loyalty-adjacent setups. Final document states it as a common eligibility rule, not a universal law.
5. Market-size/coverage numbers on vendor pages (ROI, program counts, percentages) are vendor claims; none are carried into the final document as facts.

## Final Synthesis

A Referral Marketing Platform is a brand-operated system for running customer referral programs. Its world contains: a configured program (incentives, eligibility, audience); advocates — the brand's own customers — each holding a personal trackable referral identity; a share surface through which the offer reaches friends; recorded attribution tying each referred person's qualifying conversion (purchase, signup, booking, or CRM-stage event) back to the specific advocate; and a reward engine that grants configured incentives once the referral qualifies, with fraud and eligibility rules protecting the economics. Around that core, mature products add enrollment automation, advocate portals, friend landing pages, reward fulfillment rails, program emails, analytics, A/B testing, and integrations with the commerce/CRM stack. Products range from self-serve e-commerce apps to enterprise offer platforms, and routinely bundle affiliate, ambassador, loyalty, and influencer programs alongside referral — but the referral participant (existing customer, personal identity, personal-network sharing) and the referral reward (attached to the referred person's qualifying action) are what make the Type.
