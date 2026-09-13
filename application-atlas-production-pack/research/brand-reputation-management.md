# Research Notes — Brand Reputation Management

Research date: 2026-09-06
Slug: brand-reputation-management
Directory location: §06 Marketing, Advertising & Growth (flat list under "Marketing, Advertising & Growth")

---

## Research Goal

Understand what a Brand Reputation Management application actually is as a software Type: its core objects, its defining workflow, its users, its interfaces, its rules, and its boundaries against the neighboring Types in §06 (Social Listening Platform, Media Monitoring Platform, Social Media Management Platform, Brand Management Platform, Public Relations Management Platform) and in §07 (Voice of Customer Platform, Customer Feedback Management, Complaint & Escalation Management) and §02.10 (Review Platform).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: an organization-side application that watches what the outside world says about a brand or its locations (predominantly customer reviews and ratings on third-party sites), records those signals as manageable items, lets the organization act on them (respond publicly, solicit new reviews, fix listings, route service issues), and tracks reputation metrics over time.
- Likely confusion points: Social Listening (monitoring without per-signal action), Media Monitoring (press coverage), Review Platform (consumer side of the same review object), Voice of Customer (private structured feedback), Social Media Management (publishing-first), Brand Management Platform (internal brand-expression record — already documented sibling).
- Unknowns: whether "monitoring alone" products count as this Type; how review solicitation fits the definition; whether the corporate "reputation intelligence" pole (media-based) belongs here or to Media Monitoring.

## Research Questions

1. What are the core objects? (review, response, request/invitation, listing, survey, location/entity, score)
2. What is the primary workflow loop? Is it monitor → respond → measure? Where does solicitation fit?
3. What states/lifecycles exist for reviews and responses?
4. What rules constrain the system? (site policies, send limits, opt-outs, permissions, compliance)
5. What surfaces do users work in? (inbox, monitoring table, generation console, dashboards)
6. Who are the users, and how do multi-location hierarchies shape roles?
7. Where is the boundary with Social Listening / Media Monitoring / VoC / Review Platform?
8. Is the Type stable, or is it being absorbed into broader local-marketing suites?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tier:

| Product | Tier / segment | Philosophy | Evidence level obtained |
|---|---|---|---|
| Reputation (reputation.com) | Enterprise multi-location | Broad "reputation performance" platform (reviews + listings + surveys + social + actions + AI score) | Tier 2 product pages (root, /platform/reviews); support portal JS-gated |
| Yext Reviews | Enterprise, listings-first | Reviews as one module on a Knowledge-Graph/listings substrate | Tier 1 help center (Reviews category + Monitoring + Generation articles) + Tier 2 product page |
| ReviewTrackers | Mid-market | Review monitoring/analytics-first with response and generation | Tier 2 product pages (root, /reputation-management-software); help center unreachable |
| SOCi | Multi-location/franchise | Agentic execution across local marketing; reputation as one "Genius Agent" | Tier 2 homepage/product nav |

Boundary-informing sample (not a representative product of this Type):

- Signal AI — corporate "reputation intelligence" for comms/risk teams; media/social monitoring, narrative measurement, benchmarking; no review-response loop. Used to locate the corporate pole relative to Media Monitoring.

Market anchors / drift observations:

- Birdeye — frequently cited competitor (named in Yext's own FAQ comparison). All birdeye.com surfaces blocked (help center transport error; product page and root 403 ×2). Market anchor only; no operational claims.
- Podium — homepage now positions as "AI Lead Generation & Lead Management Platform" (AI Employee for local businesses); reviews no longer appear in homepage positioning; knowledge base JS-gated. Recorded as market drift: a former review/reputation player pivoting toward lead conversion.

## Sources

Fetched 2026-09-06:

- Reputation — https://www.reputation.com/ (root; platform module map, Rep Score, industries, use cases, services)
- Reputation — https://www.reputation.com/platform/reviews (Review Management product page: requests, AI responses, unified inbox, routing, RepScore, benchmarks, reviews+surveys pairing, personas, FAQs)
- Yext — https://www.yext.com/ (root; platform module map incl. Reviews, Scout, Action Center)
- Yext — https://www.yext.com/platform/reviews (AI Reputation Agent page: monitoring/generation/response/marketing/analytics/competitive/action center/mobile; HIPAA-ready claims; FAQ competitor set)
- Yext Help Center (Tier 1) — https://help.yext.com/hc/en-us (category map)
- Yext Help Center (Tier 1) — https://help.yext.com/hc/en-us/categories/115001260503-Reviews (Reviews: Get Started / Monitoring / Response / Generation / Analytics / Integrations)
- Yext Help Center (Tier 1) — https://help.yext.com/hc/en-us/sections/115001611123-Monitoring (article list)
- Yext Help Center (Tier 1) — https://help.yext.com/hc/en-us/sections/115001611143-Generation (article list)
- Yext Help Center (Tier 1) — https://help.yext.com/hc/en-us/articles/48647576506907-Monitor-and-Filter-Reviews (monitoring screen, filters, notifications, bulk actions, review statuses, API)
- Yext Help Center (Tier 1) — https://help.yext.com/hc/en-us/articles/115005986686-Send-Review-Invitations (invitation methods, prerequisites, limits, opt-outs, balancing URL, QR codes)
- ReviewTrackers — https://www.reviewtrackers.com/ (root; feature map, add-ons, use cases)
- ReviewTrackers — https://www.reviewtrackers.com/reputation-management-software/ (aggregation, request campaigns, AI/Smart Response, integrations/API)
- SOCi — https://meetsoci.com/ → soci.ai (Genius agents incl. Reputation Agent; case-study claims)
- Signal AI — https://www.signal-ai.com/ (reputation intelligence positioning; expertise areas; capabilities)

Unreachable / limitations:

- Birdeye — help.birdeye.com (transport error), birdeye.com/products/reviews (403), birdeye.com (403). Abandoned per retry rule. Market anchor only.
- Podium — support.podium.com (transport error); podium.com root fetched but shows pivot to AI lead management; podium.com/knowledgebase JS-gated ("CSS Error"). Positioning-level only.
- ReviewTrackers help center — support.reviewtrackers.com/hc/en-us (timeout, then transport error ×2). Abandoned. ReviewTrackers rests on Tier 2 product pages.
- Reputation support portal — support.reputation.com (JS-gated "CSS Error"). Reputation rests on Tier 2 product pages.
- SOCi help/university — not attempted beyond homepage (SOCi U is login-gated university subdomain).

Consequence: precise numeric limits, default values, and site-coverage counts are asserted only where directly observed (Yext Tier 1), and even there values are recorded as existence-not-number unless the article stated them. Cross-product claims are calibrated to the four documented products.

---

## Product Observations

### Reputation (reputation.com) — evidence layer A (Tier 2 product pages)

Positioning: "AI-Powered Reputation Management Software"; "Reputation Performance Engine"; explicitly "for multi-location brands".

Platform module map (official nav):

- Reputation IQ — "Ask questions, uncover trends, and get AI-powered answers from your customer signals"
- Insights — sentiment, patterns, what to improve next
- Listings — "Keep every location accurate, visible, and ready to be found"
- Reviews — "Build trust with more reviews, better responses, and stronger local ratings"
- Surveys — direct feedback capture
- Social — "Publish, listen, and respond across social channels at scale"
- Actions — "Route issues to the right teams and close the loop faster"
- Rep Score — "Every reputation signal, rolled into one KPI"

Review Management page detail:

- Framing: "Turn Public Feedback into Your Strongest Growth Engine"; "capture the 'silent middle'"; "respond to every customer at scale—automatically"
- Review Requests: "Trigger review requests via SMS or email instantly after a visit"; templates, timing, personalization; uncover top-performing locations and campaigns
- AI-Assisted Responses: "AI Auto-Response analyzes sentiment and drafts a polite, brand-aligned reply"
- Unified Review Inbox: "Centralize reviews from Google, Facebook, Yelp, and industry sites into one feed"; filter by sentiment, keywords, source; "Assign, label, and route reviews efficiently—even across hundreds of locations"
- Competitive + Performance Visibility: "Track volume, sentiment, and response performance by brand, region, and location—then benchmark against competitors"
- RepScore: one brand-health score; monitored at brand/regional/location level; benchmark by location/region/competitor
- Actions: "Instantly convert feedback into tickets and route issues automatically"
- Insights: sentiment shifts, friction moments
- Reviews + Surveys pairing: "Reviews tell you what. Surveys tell you why." — diagnose privately, prompt happiest respondents to leave a public review
- Review streaming: "Automatically stream top-rated reviews to your website and channels"
- Personas: Digital Marketing / Local SEO Lead; CX Leader; Brand / Comms Leader
- Industries: automotive dealers, healthcare, food & beverage, care living, real estate, retail, financial services (all multi-location)
- Managed services: "Set it up. Know what to fix. Let us run the work."
- FAQ: benchmark star rating, volume, response time against a defined competitor set; response rates signal activity for local visibility

### Yext Reviews — evidence layer A (Tier 1 help center + Tier 2 product page)

Positioning: "AI Reputation Agent"; reviews framed as ranking signals for Google and AI search; reviews module on a listings/Knowledge-Graph platform ("Reputation, listings, and direct distribution in one platform").

Help-center structure (Tier 1): Reviews category = "Monitor, measure, and respond to reviews across the web", sections: Get Started / Monitoring / Response / Generation / Analytics / Integrations.

Monitoring article (Tier 1, directly observed):

- Reviews > Monitoring = "the central view for all reviews pulled into Yext across all entities and publishers"
- Table columns: last updated date, site, rating, review content, response status, entity, review labels, status
- Dynamic metrics: Total Reviews, Facebook Recommendations %, Average Rating, Breakdown of Sites, Breakdown of Star Rating; metrics are interactive filters
- AI Summarize: analyzes the most recent 100 reviews matching active filters; surfaces key themes and overall sentiment; re-run per filter context
- Basic filters: Entity (individual/folder/label), Created Date, Site (include/exclude publisher), Rating (comparisons), Status (Live / Quarantined / Removed), Label, Response Status (Awaiting Response / Publishing Response / Response Failed / Response Succeeded / Compliance Pending)
- Advanced filters: Review Content (contains words/phrases; no content; any content), Generated (came through Review Generation), Last Updated Date (edited since last response → may warrant follow-up), Sentiment Keywords / Sentiment Modifiers
- Notifications: criteria-based; recipients = Owner / All Users / Specific User Roles / specific users and emails; delivery in-platform and/or email; frequency options include event-triggered and scheduled digests; inline or spreadsheet attachment
- Bulk actions: Respond, Export (CSV/Excel; some publishers unsupported), Share (email), Manage Review Labels
- Review statuses: Live (published on third-party site or own website for first-party reviews); Quarantined (first-party review held during a quarantine period before publishing to own website; can approve early, flag for removal, or remove per permissions); Removed (reviewer deleted; publisher removed via screening; banned-word screening; user removal; admin-approved removal request)
- Deleted-review behavior configurable (keep as Removed vs permanently delete); GDPR entities: removed reviews always permanently deleted immediately
- API: Reviews: List / Review: Get endpoints with permission gating; for consumer-facing publishing filter status = LIVE and flagStatus = NOT_FLAGGED
- Also in Monitoring section: Review Labels; Manage First-Party Reviews; Set Up Review Monitoring for Your Brand; Manage HIPAA Privacy Settings for Reviews; Manage Booking.com Reviews; User Photos; Export and Share Reviews; Multi-Language Reviews; Google Q&A

Generation article (Tier 1, directly observed):

- Prerequisites: valid privacy policy URL required before any invitations; entities need an active Review Generation license; review balancing algorithm configured
- Limitations: review generation not supported for Yelp; SMS only in supported countries; account-level global send limits per day and per month, with per-entity limits configurable
- Sending methods: single invite; bulk file upload (spreadsheet with required columns storeId/entityId, firstName, lastName, contact; optional templateId, distributionId, transactionId, labelIds, language, delayTime/sendTime, image, titleName); SFTP server connection (scheduled pickup; requires Maximum Contact Frequency to prevent duplicates); API (POS/CRM integration); Review Balancing URL (unique per entity; routes the customer to a publisher per the balancing algorithm; direct-URL reviews not attributed to invitations and excluded from generation metrics); QR codes (stable per entity-publisher combination; downloadable as CSV)
- Pending Invites tab: view and cancel scheduled invitations
- Opt-outs: upload/download opt-out lists (emails and phone numbers)
- BCC: exact blind-carbon-copy of every outgoing invitation email to a specified address
- Also in Generation section: Build Custom Review Collection Pages; Review Generation Settings; Review Generation Templates; Review Generation Analytics; Publish Reviews to Your Website; SMS Availability; SFTP Connection

Product page (Tier 2):

- Review Monitoring: one dashboard across "Google, Facebook, Yelp, and 80+ industry sites"; smart filters; automated alerts; thousands of locations
- Review Generation: smart balancing algorithm routes requests to platforms that most influence visibility; trigger via email, text, or QR code
- Review Response: AI drafts with approval ("AI drafts. You approve."), templates and rules, auto-responses; on-brand
- Reviews Marketing: embed reviews on site, share to social, push star ratings into Google Ads
- Review Analytics: sentiment analysis across locations
- Competitive Intelligence: rolled-up reviews score accounting for review count and depth, average rating, recency, response time, response owner
- Action Center: send AI-generated responses automatically; auto-request reviews when a location falls behind nearby competitors on volume or rating
- Reviews Mobile (Scout app): monitor, get notified, reply with AI
- Governance: role-based access, audit trails, PHI protection, approval workflows; "HIPAA-ready"
- FAQ names the competitive set: "SOCi, Birdeye, or Reputation.com"

### ReviewTrackers — evidence layer A (Tier 2 product pages)

Positioning: "Online Reputation Management Software"; "The success of your brand depends on the voice of your customer."

Feature map (official nav):

- Reputation Management — "Monitor and analyze reviews to build a strong online reputation"
- Local SEO — improve online presence
- Customer Experience Analytics — "Leverage the voice of the customer to improve experiences"
- Competitor Analysis — "Actionable insights to beat the competition"
- Monitor Social + Reviews — "In a single workflow, monitor and manage reviews and social"
- Local Listing Management — "Get up-to-date, consistent online listings"
- Add-ons: Employer Brand Monitoring; Software Brand Monitoring; App Store Monitoring ("Monitor, manage and respond to app store feedback")

Reputation Management page detail:

- "Manage reviews from the top directories that drive revenue" — aggregate reviews from top directories, track what customers say
- "Request reviews to build local search visibility" — automate request campaigns "through numerous direct integrations"
- AI-generated review responses; "personalized Smart Response templates to auto-respond to reviews while staying on brand"
- Integrations: "over 1000 apps, and leverage our API"
- Mobile apps (App Store / Google Play)
- Use cases: crisis control ("Resolve complaints and win back trust"); mitigate risk ("Monitor feedback and reviews for trends that signal violations of compliance... enable your team to escalate and resolve these issues internally"); review widgets on website ("social proof")
- Customer quote (evo): "Being quickly alerted to customer issues through ReviewTrackers, and routing the feedback to the person on our team best equipped to address the concern is a key part of our operations."

### SOCi — evidence layer A (Tier 2 homepage/product nav)

Positioning: "AI-Powered Multi-Location Marketing"; "Agentic Workforce" of "Genius Agents" across local search, social, and reputation.

- Genius Reputation Agent: "Monitor and respond to reviews at scale"; capabilities listed: Respond to Reviews, Solicit New Reviews, Analyze Sentiment, Deploy Surveys, Respond to Chats
- Homepage agent activity mock: "Responding to Review", "Deploying Survey", "Analyzing Sentiment Trend", "Escalating Sensitive Review", "Requesting New Reviews", "Answering Chat" — per-location task execution
- Sibling agents: Local Search Agent (listings, pages, competitors, Google Posts, data health), Social Agent (content, publishing, engagement, DMs)
- Case-study claims: review response rate from 18% → 99% of reviews; review-response time from 10 hours/week to 5 minutes/day; local 3-pack ranking improvements
- Industries: financial services, restaurants, franchise, property management, retail, healthcare
- Reseller/partner programs (agencies)

### Signal AI — boundary-informing sample (Tier 2)

- Positioning: "AI-Powered Reputation Management & Risk Intelligence"; "External Intelligence"
- Data: traditional and social media across many markets and languages
- Expertise areas: Enterprise Risk, Reputation Risk, PR & Comms, ESG, Regulation
- Capabilities: Reputational Threat Sensing, Benchmarking & Measurement, Ongoing Monitoring, Proactive Reporting, Corporate Narrative Planning, "Traditional & Social Media Monitoring"
- Deliverables: platform web app, API, insight reports, dashboards, alerts/newsletters
- Crucially: no review monitoring, no review response, no review solicitation anywhere in the observed positioning. The "reputation" here = media/narrative reputation for corporate comms and risk teams.

### Market-drift observations

- Podium: homepage now "AI Lead Generation & Lead Management Platform" (AI Employee; lead response, appointment booking, database reactivation). Reviews absent from homepage positioning. A historically review-centric local-business platform has repositioned toward conversation/lead conversion. Knowledge base JS-gated, so current review-module status unverified.
- Yext: root positioning now "Enterprise Agentic Marketing Platform"; reviews remain a platform module but the company narrative is verified-data + AI agents + distribution.
- SOCi: reputation is one agent inside a multi-location marketing suite.
- Reputation.com: extends into "GEO readiness" (visibility in AI answer engines) — reputation management absorbing AI-search discoverability.
- Pattern: the review-centric reputation loop persists across all of them, but the Type is increasingly packaged inside broader local-marketing / agentic suites, and "reputation" is extending from review sites toward AI answer engines.

---

## Cross-product Comparison

| Dimension | Reputation | Yext | ReviewTrackers | SOCi |
|---|---|---|---|---|
| Managed entity anchor | brand / region / location | entity (Knowledge Graph record) | brand / location | brand / location |
| External signal capture | reviews from Google, Facebook, Yelp, industry sites | reviews from "80+ platforms"; Google Q&A; first-party reviews | reviews from "top directories"; social; app stores (add-on) | reviews; chats; surveys |
| Per-signal action | respond (AI-assisted), assign/label/route, convert to tickets (Actions) | respond (AI draft + approve or auto), labels, bulk actions | respond (AI + Smart Response templates), routing to team members | agent responds; escalation of sensitive reviews |
| Solicitation | review requests via SMS/email after visit; templates/timing/personalization | invitations via email/SMS/QR/balancing URL/API/SFTP; balancing algorithm; limits; opt-outs | automated request campaigns via direct integrations | agent solicits new reviews |
| Measurement | RepScore (one KPI); volume/sentiment/response by brand/region/location; competitor benchmark | analytics section; sentiment analysis; rolled-up competitive reviews score (count/depth, rating, recency, response time, owner) | CX analytics; competitor analysis; scorecard | sentiment trend analysis; visibility outcomes |
| Private feedback | Surveys module (pairs with reviews) | — (not observed in Reviews scope) | CX analytics (VoC framing) | Surveys |
| Findability | Listings module; location pages | Listings + Pages (core substrate) | Local Listing Management; Local SEO | Local Search Agent (listings/pages) |
| Social | Social module (publish/listen/respond) | Social module (separate) | Monitor Social + Reviews in one workflow | Social Agent |
| Issue routing | Actions: feedback → tickets → teams | — (not observed in Reviews scope; Action Center is AI-recommended platform actions) | escalate internally; route to best-equipped person | escalate sensitive reviews |
| Compliance | HIPAA page in footer; regulated industries | HIPAA privacy settings for reviews; PHI protection; GDPR deletion behavior; role-based access + audit trails | compliance-violation trend monitoring | — (not observed) |
| Delivery | SaaS + managed services | SaaS; reseller program | SaaS; agency/reseller programs | SaaS; reseller/referral |
| Mobile | — (not observed) | Scout mobile app | iOS/Android apps | SOCi Go! app |

Cross-product commonalities (evidence layer B):

1. All four products center on third-party customer reviews as the primary reputation signal, captured into a unified feed/inbox per managed entity.
2. All four support organization-authored responses to individual reviews, with AI-assisted drafting now common.
3. All four support review solicitation (request campaigns) as a first-class capability.
4. All four provide reputation measurement over time (ratings, volume, sentiment) and competitor benchmarking.
5. All four are multi-location-oriented (brand → region → location hierarchy or entity records).
6. All four pair reviews with at least one adjacent signal or module: surveys (Reputation, SOCi), listings (Reputation, Yext, ReviewTrackers, SOCi), social (all four), chats (SOCi).
7. All four expose integrations/APIs to trigger requests or export data.
8. None of the four is a pure monitoring tool: each closes the loop with action on individual signals.

---

## Canonical Abstraction

### L0 — Defining Invariant

An organization-side management loop over the brand's external public feedback:

1. **Managed brand entity** — the organization (or a named brand/location within it) as the entity whose external reputation is being managed. Multi-location hierarchies are common but the entity anchor itself is the invariant.
2. **Captured external feedback signals** — public expressions about that entity (most typically third-party reviews and ratings) pulled into the system as individual, addressable records.
3. **Organizational action on individual signals** — most canonically an organization-authored public response to a review; also routing/remediation of individual signals. Without per-signal action the product is a listening/monitoring surface, not reputation management.
4. **Tracked reputation state** — the entity's ratings/volume/sentiment measured and trended over time, closing the management loop (did our actions move the reputation state?).

Historical check (§24 reasoning applied): pre-review-economy reputation work (press clipping + PR measurement) satisfies "watch external signals + act + measure" but not "per-signal public response on a feedback platform" — that work belongs to Media Monitoring / PR, consistent with those being separate directory leaves. The review-economy loop (capture → respond → solicit → measure) is what makes this Type recognizable today; the review is the dominant signal implementation, not the invariant itself (the invariant is "external public feedback signal").

### L1 — Common Mature Structure

- Unified review inbox / monitoring table aggregating many review sites per entity
- Response tooling: composer, templates, AI-drafted replies, approval and/or auto-response rules, response-status tracking
- Review generation/solicitation: request campaigns via email/SMS (often QR), templates, scheduling/timing, invitation tracking, opt-out management, send-limit governance
- Sentiment/topic analysis over review content
- Competitive benchmarking (ratings, volume, response performance vs defined competitors)
- Multi-location hierarchy with role-based access and per-location views
- Alerts/notifications on new or matching reviews
- Reporting/analytics dashboards
- Integrations/API (POS/CRM-triggered requests; data export)
- Surveys as the private-feedback complement to public reviews
- Review marketing: publish/embed reviews on owned sites, share to social

### L2 — Variant / Optional Structure

- Listings management / local pages (findability module; core in listings-first vendors, absent or light in others)
- Social publishing/engagement module
- Issue routing into ticket/case workflows (handoff to service organizations)
- First-party review collection with moderation/quarantine before publishing to owned sites
- Industry compliance machinery (HIPAA/PHI handling, GDPR deletion behavior, audit trails)
- Managed-service layer (vendor runs the response/generation work)
- AI-answer-engine visibility ("GEO") monitoring/optimization
- Adjacent monitoring add-ons: employer brand, software brand, app-store reviews
- Mobile companion apps
- Agency/reseller/white-label posture
- Chat/messaging and lead-conversion modules (the Podium drift direction — arguably a different Type when dominant)

### L3 — Vendor-specific Structure (research notes only)

- Yext: Review Balancing URL/algorithm; entity/Knowledge-Graph substrate; Quarantined status for first-party reviews with countdown; banned-word screening; configurable deleted-review behavior; GDPR immediate-deletion rule; per-entity send limits inside account-level caps; BCC copies; SFTP scheduled pickup; Maximum Contact Frequency; Streams/Management API permission model; Scout app; Action Center; Google Q&A handling; Booking.com-specific handling
- Reputation: RepScore; Reputation IQ; Review Booster; Actions module; GEO readiness audit; "silent middle" framing
- ReviewTrackers: Smart Response templates; scorecard tool; employer-brand/software-brand/app-store add-ons
- SOCi: Genius Agents (Reputation/Search/Social); Local Visibility Index; per-location agent task feed
- Signal AI: AIQ; Signal AI 500 ranking; report/briefing productization
- Podium: AI Employee pivot (lead conversion)

---

## Vendor-specific Findings

See L3 above. Additionally:

- Yext's FAQ explicitly names the competitive set ("SOCi, Birdeye, or Reputation.com"), confirming that the market treats these as one category despite different substrates.
- Reputation's own FAQ asserts that responding to reviews helps local visibility — a marketing claim, recorded as vendor claim, not adopted as a canonical rule.
- SOCi's case-study figures (18% → 99% response rate) are customer quotes, not product rules.

## Rejected Findings

- "Brand Reputation Management = social listening" — rejected: none of the four documented products is positioned primarily as a social-conversation listening tool; social is one signal source/module. Listening without per-signal action is a different Type.
- "Brand Reputation Management = media monitoring" — rejected for the review-centric center of gravity: the corporate media-narrative pole (Signal AI) has no review loop and belongs with Media Monitoring / Social Listening. Flagged for joint review with those unprocessed siblings.
- "Reputation management requires listings management" — rejected: listings is a common module (3 of 4 documented products) but ReviewTrackers-style analytics-first products and pure review tools exist without it; it is L1/L2, not L0.
- "Reputation management requires surveys" — rejected: surveys are a pairing module, not definitional.
- "AI response drafting is definitional" — rejected: recent common structure (L1); the response loop predates AI drafting.
- "The Type is defined by multi-location" — rejected: single-location SMB usage exists (Birdeye's historical SMB base; Yext small-business accounts per its invitation article); multi-location is the dominant market shape (L1), not the invariant.

## Boundary Findings

1. **vs Social Listening Platform (§06 sibling, unprocessed) — sharpest seam.** Listening products monitor broad social conversation for insight; this Type captures external feedback signals about the managed entity and acts on each signal (respond/solicit/route) while tracking entity-level reputation state. Structural test: remove per-signal organizational action → a listening platform remains; add per-signal response to a listening platform → it drifts into this Type. Flag for joint review when Social Listening Platform is processed.
2. **vs Media Monitoring Platform (§06 sibling, unprocessed).** Media monitoring tracks press/media coverage; the corporate "reputation intelligence" pole (Signal AI-style: narrative sensing, benchmarking, reporting for comms/risk teams) sits between the two and calls itself "reputation management" while having no review loop. This leaf's canonical center is the review/feedback loop; the corporate media-narrative pole should be documented under Media Monitoring (or as its own variant there). Flag for joint review.
3. **vs Review Platform (§02.10).** Same review object, opposite side: the Review Platform is the consumer-facing venue where reviews are published and consumed; this Type is the organization-side management surface over reviews about the managed entity. A travel-review platform's management console for hotels would be an instance of this Type's subject matter, but the venue itself is not.
4. **vs Voice of Customer Platform / Customer Feedback Management (§07, unprocessed).** VoC centers on structured, mostly private feedback programs (surveys, relationship metrics) for experience improvement; this Type centers on public third-party signals and public response, with findability stakes (ratings visible to prospective customers). Surveys appear inside reputation products as a private-feedback complement ("reviews tell you what, surveys tell you why") — a bridge, not the core.
5. **vs Social Media Management Platform (§06, unprocessed).** Social-first products center on publishing/scheduling/engagement across social channels; here social is one signal source among reviews, and the review loop (respond/solicit/measure) is primary. Products bundle both; the center of gravity decides.
6. **vs Brand Management Platform (§06 sibling, processed 2026-09-06).** No object overlap: Brand Management = internal system of record for brand expression (assets, guidelines, templates); this Type = external perception signals and the response loop. The word "brand" collides; the Types do not.
7. **vs Complaint & Escalation Management (§07, unprocessed).** Reputation products convert individual signals into tickets and route them (Reputation "Actions"; ReviewTrackers routing quote), but the case workflow itself belongs to the service side; the reputation tool hands off and tracks closure only as reputation hygiene.
8. **vs Digital Risk Protection (§15).** Security-domain brand abuse (impersonation, phishing, dark-web) shares the words "brand" and "monitoring" but has different signals (infrastructure, threat actor) and different actions (takedown); not this Type.
9. **Consumer/individual ORM services** (search-result suppression for private individuals — the historical "online reputation management" services): different audience (individuals), different object (search results/content), typically service-not-software. Out of this Type's scope; noted because the market uses the same words.
10. **Market drift / absorption.** Podium's pivot to AI lead management and the packaging of reputation into agentic local-marketing suites (SOCi, Yext) show the Type being absorbed as a module. The Type remains recognizable wherever the review loop (capture → respond → solicit → measure) is the center of gravity; when lead conversion or publishing becomes dominant, the product has drifted to a different Type.

## Uncertainties

- Birdeye's current module structure unverified (all surfaces blocked); it is kept as a market anchor only. Its frequently-described shape (reviews + listings + surveys + messaging for local businesses) is consistent with the documented sample but was not directly observed.
- Podium's current review-module status unverified (JS-gated knowledge base; homepage pivot). Treated as market-drift evidence only.
- Exact numeric limits (invitation caps, quarantine durations, site-coverage counts) exist as configurable/observed quantities in Yext's documentation but their values are not recorded here; no numeric claims are made for other products.
- Reputation's operational detail rests on Tier 2 product pages (support portal JS-gated); workflow claims for Reputation are calibrated accordingly.
- Whether the corporate reputation-intelligence pole should eventually be a variant documented under Media Monitoring Platform, or a separate leaf, is a taxonomy question for the sibling passes — recorded in STATUS.md Boundary Issues.
- The strength of "response" as an L0 element rests on the four documented products all having it plus the structural test against listening; a pure-response-less monitoring product marketed as "reputation management" was not observed, but cannot be ruled out market-wide.

## Final Synthesis

Brand Reputation Management is the organization-side application for managing external public feedback about a brand and its locations as an ongoing operational loop: capture external signals (reviews above all) as individual records anchored to the managed entity; act on each signal (public response, solicitation of new signals, routing of issues); and track the entity's reputation state (ratings, volume, sentiment, competitive position) over time. Mature products wrap this loop with a unified inbox, AI-assisted responses, request campaigns with governance (limits, opt-outs), sentiment/topic analytics, competitor benchmarking, multi-location hierarchies, and adjacent modules (listings, surveys, social, review marketing, ticket handoffs). The defining core is small; everything else is common structure or variant. The Type's sharpest boundaries are against Social Listening (monitoring without per-signal action), Media Monitoring (press coverage; corporate reputation intelligence pole), Review Platform (consumer side of the same object), and VoC (private structured feedback). The market is consolidating reputation into broader local-marketing/agentic suites and extending "reputation" toward AI answer-engine visibility, but the review loop remains the recognizable center.
