# Research Notes — Hotel CRM / Loyalty Platform

Leaf: Hotel CRM / Loyalty Platform (§26 Travel, Hospitality, Food Service & Events)
Slug: hotel-crm-loyalty-platform
Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand what a Hotel CRM / Loyalty Platform actually is as an Application Type: the operator-side system hotels, chains and groups use to hold guest relationships and operate guest loyalty programs. Establish the smallest defining core, separate it from common mature structure and variants, and hold the boundaries against Hotel PMS, generic Loyalty Program Management, generic CRM, hotel CDP, and guest-experience/concierge Types.

## Initial Boundary Hypothesis

- Core use hypothesis: guest profiles of record anchored on stays + loyalty program operation (membership, earn, tier, redemption) + stay-anchored engagement.
- Nearest neighbors: Hotel PMS (profiles/stays live there operationally), Loyalty Program Management (§05.15, processed 2026-09-08), Customer Relationship Management (§07, processed 2026-09-08), Customer Data Platform (§06), Hotel Guest Experience Platform / Digital Concierge (§26 siblings), Hotel Booking Engine / CRS.
- Key unknown going in: is a full points-based loyalty program native to every "hotel CRM" product, or is loyalty a separable half?

## Research Questions

1. What is the central object (guest profile? membership?) and what does it carry (stays, preferences, consent, loyalty standing)?
2. How does stay data enter (PMS/CRS/POS integration vs manual)? Which system remains the record for stays?
3. What does the CRM half do: segmentation, journeys, attribution, service recovery?
4. What does the loyalty half do: program config, enrollment, accrual (base, bonus, tier vs award points), expiry, redemption (rate/package/upgrade/pay-with-points/outlet), tier qualification/renewal, claims/exceptions?
5. What interfaces exist (marketer console, program admin, profile view, booking-time redemption surfaces, dashboards)?
6. What rules matter (identification gates earning, award cancellation mechanics, qualification windows calendar vs rolling, consent/GDPR, franchise data sharing, profile merge/anonymization)?
7. How do products differ in packaging (standalone hotel CRM/marketing vs PMS-suite loyalty subscription vs horizontal loyalty platform vs hospitality-suite loyalty module)?

## Representative Products

Selected for market representation, documentation quality, different product philosophies and different customer tiers:

1. **Revinate** — the archetype standalone hotel guest-data/marketing platform (independent hotels → groups; SMB→mid tier). Has repositioned its language from "hotel CRM" to "hotel CDP" + marketing automation. Evidence: product pages + FAQ (Tier 2).
2. **Oracle Hospitality OPERA Cloud (with Loyalty)** — PMS-suite pole; enterprise chains. Evidence: official User Guide Release 26.3, Tier 1.
3. **Salesforce Loyalty Management (Customer Loyalty Platform)** — horizontal loyalty platform with hospitality customers (Omni Hotels shown). Evidence: product page + FAQ (Tier 2).
4. **Agilysys Loyalty & Promotions** — hospitality-suite loyalty/promotions module (hotels, multi-amenity resorts, casinos, cruise; integrated with its PMS + POS). Evidence: product page + FAQ (Tier 2).

Context (unreachable this pass, recorded as market context only, no claims drawn): Cendyn (cendyn.com 403; success.cendyn.com transport error) — enterprise hospitality CRM & loyalty suite; Sabre Hospitality (root rebranded "Aven Hospitality"; product docs not fetched); Infor (products page 404); Revinate help centers (support.revinate.com transport error; help.revinate.com timeout).

## Sources

| Source | Tier | Status |
|---|---|---|
| https://www.revinate.com/ (root) | 2 | Fetched |
| https://www.revinate.com/hotel-software/cdp/ (CDP page + FAQ) | 2 | Fetched |
| https://www.revinate.com/hotel-software/marketing-automation/ (Pathways page + FAQ + product-tour transcript) | 2 | Fetched |
| https://docs.oracle.com/en/industries/hospitality/ (docs home) | 1 | Fetched |
| OPERA Cloud Services 26.3 — User Guide TOC (ocsuh/toc.htm) | 1 | Fetched |
| OPERA Cloud 26.3 — "Membership (Loyalty Cloud Service)" (c_about_loyalty_new.htm) | 1 | Fetched |
| OPERA Cloud 26.3 — "Redeeming Loyalty Awards" (t_managing_reservations_redeeming_loyalty_awards.htm) | 1 | Fetched |
| https://www.salesforce.com/loyalty-management/ (product page + FAQ) | 2 | Fetched |
| https://www.agilysys.com/en/products (portfolio) | 2 | Fetched |
| https://www.agilysys.com/en/products/loyalty-and-promotions/ (product page + FAQ) | 2 | Fetched |
| cendyn.com, success.cendyn.com | 1/2 | 403 / transport error — abandoned |
| sabrehospitality.com (→ "Aven Hospitality" title) | 2 | Root fetched, no product content |
| infor.com/products/hospitality | 2 | 404 |
| support.revinate.com / help.revinate.com | 1 | transport error / timeout — abandoned |

## Product Observations

### Revinate (Tier 2 — product pages + FAQ; help centers unreachable)

- Self-positioning: "hospitality's leading direct booking platform"; AI-powered **hotel customer data platform**. Product family: Revinate Core (CDP), Revinate Marketing (email), Revinate Pathways (marketing automation), Revinate Chat (virtual concierge), Revinate Feedback (reputation/surveys), Reservation Sales / RezForce (voice channel). [A]
- **Rich Guest Profile**: unified per-guest profile ingesting data from PMS, restaurant, spa, golf systems; PMS is the system of record (most integrations one-way PMS→Revinate, some two-way); 140+ PMS/spa/restaurant/golf providers listed as integration surface. [A]
- **Identity resolution**: ML merge of duplicate profiles including masked OTA emails ("OTA email unmasking"), typos, name changes, misaligned fields; ">1M OTA profiles merged" claim (marketing figure, not operational fact). GDPR/CCPA posture claimed. [A]
- **Segmentation**: 100+ guest attributes (spend, loyalty, booking habits, demographics, geography at postcode level), exclusion filters, "everyone except" logic. [A]
- **Loyalty tiers**: built with the same segment-builder filters; customizable qualifying timeframe; tier/status surfaced on the profile with icons; FAQ explicitly frames loyalty tiers as able to "serve as a rewards program and as an internal tool" — i.e., tier/classification-based recognition, **no points ledger, no redemption machinery evidenced**. [A]
- **Group hierarchies**: group/enterprise accounts view aggregated data across properties; property-level access controls; profiles roll up into a master profile per guest. [A]
- **Pathways (marketing automation)**: omnichannel journeys over Revinate Core data — visual workflow builder; triggers at stay-lifecycle moments: booking, pre-arrival, check-in/checkout, booking-engine/website cart abandonment, cancellation recovery, "we miss you"/OTA winback, birthday, **"qualifications"** (loyalty qualification as a journey trigger), lapsed guests. Email + promotional SMS (WhatsApp on roadmap); condition nodes (consent checks incl. double opt-in, future-stay status, opens/clicks), delay nodes; merge tags; dynamic content by stay dates; country-specific quiet hours; revenue attribution tying journeys to reservations, room nights, outlet revenue (rooms, spa, golf, restaurant); multi-property hierarchy for centralized campaigns with property-level tracking; Starter/Pro packages. [A]
- Positioning against "general CRM/PMS": claims general CRMs and PMS lack hospitality-native data models, automatic identity resolution, OTA unmasking, multi-system unification, advanced segmentation, real-time profile updates. [A — vendor comparative claim]

### Oracle Hospitality OPERA Cloud (Tier 1 — User Guide 26.3)

- "Client Relations" chapter carries the guest-relationship machinery: Profiles (guest/contact/sales-account profile types), creation/management, identification & personal details (incl. ID document scanning), **preferences**, communications, correspondence & privacy options, external emails, **profile merge** (with prerequisites + match list), **profile anonymization (de-identification)**, profile purge, future & past stays views, **profile history stay & revenue statistics**, profile notes/attachments, flexible dynamic fields, batch profile update, Smart Profiles, profile credit-card wallet, AR accounts, e-certificates, negotiated rates, profile relationships, ownership records, service requests, profile subscriptions. [A]
- **Membership (Loyalty Cloud Service)** — chain-level loyalty under an OPERA Cloud Loyalty subscription (requires profile sharing/chain config): [A]
  - Tier management incl. **upgrades, downgrades, renewals (calendar or rolling)**; tier benefits.
  - **Points calculation rules for enrollment and stay (base and bonus, tier and award points)**, earning based on **nights, stay, revenue or enrollment**.
  - Awards: **Rate, Package, Upgrade, Payment, and Other (third-party)** redemption.
  - Calculating or expiring membership points and issuing awards; membership claims; membership exceptions; suspended membership profiles.
  - Reporting in OPERA Cloud Reporting and Analytics.
- **Redeeming Loyalty Awards** (Reservations): awards consumed **at the time of booking**; offered based on validity dates, member tier/level, other factors. Award types: Rate, Package, Room Type Upgrade, **Payment (Pay with Points)**, Other. Detailed cancellation mechanics documented: cancellation → award cancelled and points returned less cancellation penalty; night reduction → proportional return; rate change to non-award → award cancelled; **date change does not cancel/reissue the award** (worked examples given). [A]
- **Managing Reservation Memberships**; **Viewing Reservation Awards**; prerequisites for redeeming loyalty awards; prerequisites for **enrolling guests in external loyalty programs**; "Guest Loyalty Programs" related topic (external program memberships on profiles). [A]
- Note: OPERA Cloud's loyalty is a separate subscription product over the PMS — marketing campaign automation is NOT part of the OPERA Cloud core (no campaign/journey machinery found in the guide TOC).

### Salesforce Loyalty Management / Customer Loyalty Platform (Tier 2 — product page + FAQ)

- Positioning: design and run loyalty programs — "Loyalty Management software ... manages the design, definition, configuration, execution, and analysis of omnichannel loyalty programs"; explicitly **not the same as CRM software** but built into the platform so programs tie back to the CRM for "a single view of each member". [A]
- Program machinery: points, tiers, rewards; configurable **accrual rules, redemption rules, tier qualification thresholds**; custom reward currencies (dollars, percentages, vouchers); points-based, tiered status, cash-back, visit/punch-card, or hybrid programs; non-purchase behaviors (referrals, reviews, social, app activity); multiple programs/incentives across brands and partners; gamification, clubs/communities. [A]
- Member experience: member snapshot dashboards, disengagement-risk prediction, personalized journeys; loyalty events (tier upgrade, points milestone, expiring reward, new enrollment) trigger marketing journeys; member data (tier status, point balance, expiry dates) personalizes email/SMS; Data 360 unification mentioned. [A]
- Hospitality presence: Omni Hotels & Resorts shown among loyalty customers; industry templates for segment activation. [A]

### Agilysys Loyalty & Promotions (Tier 2 — product page + FAQ)

- Positioning: "hospitality loyalty software" for hotels, resorts, casinos, F&B venues; part of Agilysys hospitality suite ("100% hospitality focused" for 40 years). Integrated with Agilysys PMS and InfoGenesis POS. [A]
- Program machinery: **tier-based, points-based, or hybrid** structures with customizable **earning rules, expiration schedules, redemption logic, tier benefits**; enterprise program management (multi-property programs, centralized rules with property-level flexibility). [A]
- **Real-time earn & redeem across PMS and POS transactions** — rooms, F&B, spa, golf (and retail) outlets; guests see balances update immediately. [A]
- Unified guest data: offers based on visit frequency, spend thresholds, behavior patterns; AI-driven segmentation ("segment-of-one"). [A]
- **Precision promotion engine**: item-specific/outlet-specific/post-type promotions, BOGO, conditional discounts, timed incentives — framed as margin protection vs broad discounts; capture "total wallet share" beyond rooms. [A]
- Insights: redemption rates, guest engagement, revenue impact via Agilysys Analyze. Teams named: marketing, revenue managers, GMs, ops, executives. Customer example: Carnival UK (cruise) using InfoGenesis + Loyalty & Promotions. [A]

## Cross-product Comparison

| Structure / capability | Revinate | OPERA Cloud Loyalty | Salesforce Loyalty Mgmt | Agilysys Loyalty & Promotions | Layer |
|---|---|---|---|---|---|
| Guest profile of record (persistent, identified, cross-source) | ✔ (Rich Guest Profile, CDP) | ✔ (Profiles: guest/contact/sales account) | ✔ (member = CRM person; unified view) | ✔ (unified guest data via PMS/POS) | L0 |
| Stay history / stay & revenue statistics on profile | ✔ (ingested stays) | ✔ (past/future stays, stay statistics) | (stay data via customer's CRM data model) | ✔ (PMS/POS data) | L0 (stay anchoring) |
| Guest preferences / service data on profile | ✔ (attributes) | ✔ (preferences, service requests, notes) | (via platform data model) | ✔ (behavior/patterns) | L1 |
| Operated loyalty program standing per guest | ✔ (loyalty tiers, qualifying timeframe, status on profile) | ✔ (membership, tiers, points) | ✔ (membership, points/tiers) | ✔ (membership, points/tiers/hybrid) | L0 |
| Tier qualification + upgrade/renewal machinery | ✔ (qualifying timeframe; status display) | ✔ (calendar or rolling; upgrades/downgrades/renewals; tier benefits) | ✔ (tier qualification thresholds) | ✔ (tier benefits; custom rules) | L1 (tier classification thin pole in Revinate) |
| Points ledger (earn rules, expiry) | ✘ (not evidenced) | ✔ (base/bonus, tier & award points; nights/stay/revenue/enrollment; expiry) | ✔ (accrual rules, custom currencies) | ✔ (earning rules, expiration) | L1 |
| Redemption at booking (rate/package/upgrade/pay-with-points) | ✘ | ✔ (five award types; booking-time consumption; cancellation penalty mechanics) | (redemption rules configurable; channel execution via customer stack) | (redemption at outlets via POS; booking side via PMS) | L1 |
| Real-time earn/redeem at outlets (POS) | ✘ | (integration-dependent) | (via customer stack) | ✔ (real-time across PMS+POS) | L1 |
| Identity resolution / profile merge / dedup | ✔ (ML identity resolution, OTA email unmasking) | ✔ (merge, match list; external email mgmt) | (platform identity stack) | ✔ (unified guest data) | L1 |
| Segmentation engine over profile/loyalty attributes | ✔ (100+ attributes, exclusions) | (query/reporting, batch update; not a marketer segment tool at core) | ✔ (segments via platform; industry templates) | ✔ (behavior-based targeting) | L1 |
| Stay-lifecycle journey automation (pre/during/post-stay, win-back) | ✔ (Pathways: triggers incl. "qualifications", cart abandonment, OTA winback) | ✘ (not in OPERA core) | ✔ (loyalty events trigger journeys) | (promotions engine adjacent) | L1 |
| Revenue/outlet attribution of engagement | ✔ (journeys → reservations/room nights/outlet revenue) | (reporting/analytics) | (conversion analytics claimed) | ✔ (wallet share, redemption ROI via Analyze) | L1 |
| Promotions/discount engine (offer terms, margin protection) | ✘ (offers via campaigns) | (negotiated rates, e-certificates adjacent) | (offers/referrals bundled in suite) | ✔ (item/outlet/post-type promotions, BOGO) | L1/L2 |
| Consent/privacy machinery | ✔ (double opt-in, quiet hours, GDPR/CCPA) | ✔ (correspondence/privacy options, anonymization, purge) | (platform compliance) | (not evidenced) | L1 |
| Multi-property / chain hierarchy & governance | ✔ (group roll-up master profiles) | ✔ (chain-level program, profile sharing required) | ✔ (multi-program/multi-brand) | ✔ (centralized rules, property flexibility) | L1 |
| Member-facing surfaces (portal/app/enrollment UX) | ✘ (not evidenced) | (booking-engine integration implied, not evidenced) | ✔ (loyalty experiences claimed) | (not evidenced) | L2 |
| Claims / missed-credit / exceptions handling | ✘ | ✔ (membership claims, exceptions, suspended profiles) | (program ops via platform) | (not evidenced) | L1 (product-specific depth) |
| Integration spine (PMS/CRS/booking engine/POS/outlets) | ✔ (140+ providers) | ✔ (native PMS; awards at booking; external programs) | (platform ecosystem) | ✔ (native PMS+POS) | L1 |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Two jointly-held structures; jointly-held is load-bearing:

1. **The guest profile of record** — a persistent, individually identified record per guest held by the lodging operator (property or chain/group), accumulating **stay history** and **guest preferences/standing data**, consolidated from the operator's systems (PMS, outlets) and across properties. Remove → an address book or generic contact database; remove the stay anchoring → generic CRM/CDP territory.
2. **The operated guest loyalty program** — the operator maintains a recognition/rewards program **of record** over its guest population: guests are enrolled as members (membership attached to the guest profile), and the system maintains each member's **program standing** — qualification-based status (tier/level) and, in the dominant implementation, earned value (points) — under configured program rules, extending program benefits/offers to members. Remove → hotel marketing/CDP platform (profile-only); remove profiles → a generic loyalty ledger with no lodging subject.

Removal tests:
- Profile without program standing → hotel CDP/marketing platform (Revinate's pole minus its tier machinery) — below this Type.
- Program standing without the operator's own guest profiles (member = anonymous ledger entry) → generic Loyalty Program Management (§05.15) / wallet territory.
- Both, but the record is the *stay/folio* rather than the standing relationship → Hotel PMS.

Historical check (§24): the pre-cloud realization — PMS guest history (profile + preferences + stay counts + notes) plus a chain frequent-guest program (card-number membership on the profile, tier status, stay certificates/vouchers) — satisfies both structures without any cloud, AI, segmentation engine or marketing automation. Paper-era equivalents (guest index cards + punch/scratch member cards) satisfy the abstract core. Check passed; no modern mechanism in L0.

### L1 — Common Mature Structure (evidence B: cross-product)

- Identity resolution / duplicate merge across systems and properties (ML-based at 1 sample; merge/match-list machinery at 2; all four consolidate).
- Segmentation over profile + loyalty attributes; exclusion/consent logic.
- Stay-lifecycle engagement: pre-arrival, in-stay, post-stay, cancellation/win-back journeys across email/SMS/messaging; loyalty events as triggers; revenue/outlet attribution.
- Points machinery where programs are points-based: earn rules (nights/stay/revenue/enrollment; outlet spend), base/bonus/tier/award classes, expiry.
- Redemption machinery: booking-time awards (rate/package/upgrade/pay-with-points) and/or outlet redemption (POS real-time), award cancellation/penalty handling.
- Tier machinery: qualification windows (calendar or rolling), upgrades/downgrades/renewals, tier benefits.
- Privacy/consent: correspondence/privacy controls, anonymization/deletion, double opt-in, quiet hours.
- Multi-property/chain hierarchy: chain-level program config, property-level flexibility, group master profiles.
- Integration spine: PMS (system of record for stays), CRS/booking engine, POS/outlets, spa/golf systems.
- Program analytics: redemption/engagement/revenue reporting.

### L2 — Variant / Optional Structure

- Program currency form: points vs tier-only recognition vs hybrid vs cash-back/custom currencies.
- Accrual base: room nights/room revenue vs total property wallet share (F&B/spa/golf/retail); casino-gaming-earn heritage exists in the market (Agilysys serves casinos; not directly evidenced this pass — recorded as uncertainty).
- Redemption locus: booking-time (CRS/PMS) vs outlet POS vs generic rewards.
- Packaging: standalone hotel CDP/marketing platform; PMS-suite loyalty subscription; horizontal loyalty platform with industry configuration; hospitality-suite loyalty module.
- Customer tier: independent/SMB pole vs chain/enterprise pole.
- Member-facing surfaces: enrollment UX, member portal/app (evidenced at 1 sample → optional).
- Claims/missed-stay credit handling depth (product-specific depth).
- Promotion-engine coupling (loyalty + margin-protected promotions in one module vs offers via campaigns).
- Regional compliance packs (SMS consent regimes etc.).

### L3 — Vendor-specific (research notes only)

Revinate: "Rich Guest Profile" branding, OTA-email-unmasking ROI claims (30%+ reachable, >1M merged, 90-day ROI, 5-20X ROI), $14B direct-revenue claims, RezForce/Reservation Sales voice products, Pathways Starter/Pro packaging, SOC2/AWS posture claims.
OPERA Cloud: "Loyalty Cloud Service" subscription naming, OPERA Control prerequisites, worked cancellation examples (100 points/night), Smart Profiles, profile purge, ID document scanning, OHIP developer portal, Loyalty badge in docs.
Salesforce: Agentforce/Data 360 bundling, Silver/Gold/Platinum tier example, "Spin the Wheel" gamification, industry templates, Gartner MQ claims, Omni Hotels logo use.
Agilysys: S.P.E.N.D. booking technology award, Analyze/DataMagine companion products, Carnival UK success story, "40 years / 100% hospitality" claims.

## Vendor-specific Findings

- Revinate's loyalty tiers are **classification-only** (no points ledger or redemption evidenced) — an important calibration: the market's leading "hotel CRM" currently operates loyalty as profile-level standing rather than a full program. This keeps the points/redemption machinery in L1 rather than L0.
- OPERA Cloud's loyalty is a separately licensed, chain-level subscription requiring profile sharing — evidence that program-of-record + hierarchy governance is structural (gated by configuration, not incidental).
- Revinate markets itself as CDP, not CRM — naming drift toward CDP vocabulary in the hotel market; the population of products is continuous with what was called "hotel CRM" (the FAQ explicitly positions against "hotel CRM" as a lesser category). Recorded as market-language drift, not a different Type.

## Boundary Findings

1. **vs Hotel PMS (§26 sibling, unprocessed)** — sharpest seam. The PMS's world is the stay: reservation → stay → folio → room operations; its guest profile is the operational slice feeding check-in. This Type holds the *standing relationship*: profile + program membership surviving across stays and properties, plus program/engagement machinery. OPERA itself demonstrates the seam: the same vendor splits "OPERA Cloud Property" (stay operations) from the chain-level Loyalty subscription and requires profile sharing as the integration gate. Removal tests both directions recorded. Pre-hung seam for the Hotel PMS pass; joint review recommended if that pass draws the guest-profile slice differently.
2. **vs Loyalty Program Management (§05.15, processed 2026-09-08)** — the generic loyalty core (program of record, enrolled member, behavior-triggered accrual, redemption under rules) is the shared machinery of the loyalty half here. The hotel instantiation earns from stays and on-property spend (nights/stay/revenue/enrollment; outlet POS), redeems against bookings (rate/package/upgrade/pay-with-points — booking-time consumption with cancellation penalty mechanics is lodging-specific) and outlets, and is anchored on the operator's own consolidated guest profiles across properties. Consistent with that pass's "program machinery vs issued offers" seam vs promotions; this leaf is the lodging-domain instance, not a duplicate.
3. **vs Customer Relationship Management (§07, processed 2026-09-08)** — CRM family shape (person-centric records + interaction history + progression) is shared; the hotel variant anchors on stays and hospitality semantics (preferences, stay-driven segmentation, pre/post-stay lifecycle), has no deal pipeline as center. Consistent with that pass's family note listing domain instantiations (nonprofit-crm, donor-management-system, real-estate-brokerage-crm, constituent-relationship-management). Salesforce's own FAQ ("loyalty is not CRM but ties back for a single member view") corroborates the separation of centers.
4. **vs Customer Data Platform (§06)** — Revinate self-describes as a hotel CDP; the data engine of this Type and the CDP overlap on unified profiles + segmentation. The seam: horizontal CDPs hold identities/segments without operating a loyalty program of record or lodging stay anchoring; this Type's products carry the program standing. Recorded as naming-drift zone; no directory change proposed.
5. **vs Hotel Guest Experience Platform / Digital Concierge (§26 siblings)** — in-stay messaging, service fulfillment and concierge surfaces center the *current stay's service loop*; this Type centers the standing relationship and program. Revinate Chat and OPERA service requests sit adjacent (capabilities/companions), not the center.
6. **vs Hotel Booking Engine / Hotel CRS (§26 siblings, unprocessed)** — loyalty awards are *consumed* at booking (OPERA evidence); the booking transaction and channel/distribution machinery belong to those Types. This Type supplies member standing + award validity/tier gating to the booking moment.
7. **vs Email/SMS Marketing Platform / Marketing Automation (§06)** — channel execution is a capability (or companion product) here; the center is the operator's own guest population + program. Revinate Pathways' hospitality-native triggers/attribution do not change the Type's center.
8. **Casino-resort loyalty** — the gaming pole (slot/table earn via player-tracking) shares resort-loyalty machinery but is anchored in gaming management systems; Agilysys serves casinos from the same hospitality suite, but slot-earn machinery was not directly evidenced this pass. Held as an adjacent pole / uncertainty; no claim made.

## Uncertainties

- Cendyn (the enterprise hospitality CRM & loyalty suite) and Sabre/Aven hospitality products unreachable — the "chain CRM suite" pole is covered structurally via OPERA/Salesforce/Agilysys but not sampled directly; no claims drawn from those vendors.
- Revinate help centers unreachable — all Revinate evidence is product-page/FAQ tier; operational details (exact segment limits, tier mechanics depth) not asserted.
- Member-facing portal/app machinery only weakly evidenced (Salesforce "loyalty experiences") — held optional, not core.
- Casino gaming-earn loyalty machinery not directly evidenced; market pole recorded as uncertainty.
- Salesforce evidence is horizontal (industry-agnostic product with hospitality customers); hotel-specific workflow depth in Salesforce was not directly observed.
- Precise program parameters (point values, qualification thresholds, expiry periods) deliberately not asserted: they are operator-configured, and only OPERA documents them as configuration classes, not defaults.

## Final Synthesis

The Type is the lodging operator's system of record for the **guest relationship and the operated loyalty program**: two jointly-held structures — the consolidated guest profile of record anchored on stays (identity + stay history + preferences across properties) and the guest loyalty program of record (enrolled members with maintained, qualification-based standing — tier status and, dominantly, earned points — plus program benefits and award redemption at booking/outlets). Around that core, mature products add identity resolution, segmentation, stay-lifecycle journeys with revenue attribution, consent/privacy machinery, chain/property governance, the PMS/CRS/POS integration spine, and program analytics. Packaging varies across four poles (standalone hotel CDP/marketing; PMS-suite loyalty subscription; horizontal loyalty platform; hospitality-suite loyalty module), which is the Type's realization spectrum, not four Types.
