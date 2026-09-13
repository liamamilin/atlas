# Research Notes — Customer Advocacy Platform

## Research Goal

Understand what a Customer Advocacy Platform actually is as an Application Type: its core objects (advocates, asks/activities, participation records), the workflows of operating a customer advocacy program (recruiting, asking, participating, reviewing, recognizing, fulfilling reference requests), and the boundaries against Referral Marketing Platform, Loyalty Program Management, Influencer Marketing Platform, Voice of Customer, Employee Advocacy, and the §25 Advocacy Platform (name collision).

Prior context from STATUS.md that this pass must honor:

1. **referral-marketing-platform (§06, processed)** flagged a joint review: "advocacy seam = referral-first program machinery (offer design/attribution/reward fulfillment) vs reviews/UGC/references bundled as one advocacy motion (Mention Me straddles by positioning referral as the core of customer advocacy)".
2. **advocacy-platform (§25)** recorded the name collision: §25 = policy mobilization (supporters → decision-maker targets); §06 = commercial advocacy (references/reviews/referrals). NOT aliases; this pass must document the collision from the §06 side.

## Initial Boundary

Initial hypothesis before research:

- Core use: a brand (mostly B2B) operates a program that mobilizes its existing customers to perform advocacy actions — reference calls for sales, reviews, testimonials, case studies, referrals, speaking, community answers — and manages/recognizes those customers.
- Users: customer marketing / advocacy program managers (operator side); sales/marketing/CS as internal consumers of advocacy; customers as advocates.
- Nearest neighbors: Referral Marketing Platform (referral as one activity vs the whole program), Loyalty Program Management (what the reward attaches to), Influencer Marketing Platform (customers vs creators), Employee Advocacy (employees vs customers), Voice of Customer (feedback signals vs advocacy actions), Advocacy Platform §25 (name collision).
- Unknowns: is gamification/rewards definitional or common? Is reference-request routing definitional or a B2B-pole capability? Is there a rewards-less pole that would break a rewards-inclusive definition? Does the Type include consumer/ambassador-style programs (BrandChamp-class) or only B2B reference programs?

## Research Questions

1. What are the core objects? (advocate, ask/challenge/activity/request, participation record, reward, advocacy output/proof)
2. What is the defining workflow? (recruit → profile → ask → participate → review/approve → recognize → consume/measure)
3. What activity types exist? (reference calls, reviews, testimonials, case studies, referrals, speaking, social shares, community answers, beta/feedback, advisory boards)
4. How does the B2B reference-request flow work? (request intake from CRM/Slack, routing, account-team approval, fulfillment tracking, overuse avoidance)
5. What role do rewards/gamification play — definitional or common?
6. What rules govern advocate use? (preferences, permissions, use limits, profile currency, job changes)
7. What interfaces exist for program managers, internal requesters, and advocates?
8. Where are the boundaries with referral, loyalty, influencer, affiliate, employee advocacy, VoC, and §25 advocacy?

## Representative Products

Selected for market coverage across customer tier and product philosophy:

| Product | Tier / posture | Why sampled |
|---|---|---|
| Influitive | enterprise advocate-hub pole; the market-defining "customer advocacy platform" (AdvocateHub lineage) | gamified challenges/points/rewards; broadest use-case framing (reviews, references, referrals, social, stories, feedback, training) |
| SlapFive | enterprise "CMA system of record" pole | advocate & proof system of record + reference automation + revenue influence; richest request-routing description |
| ReferenceEdge (Point of Reference) | Salesforce-native reference-management pole | advocate database + request routing + close-the-loop + rewards inside Salesforce; the "reference desk" philosophy |
| BrandChamp | self-serve ambassador/advocate pole (consumer brands) | only reachable Tier-1 help center; documents the activity lifecycle (create → complete → approve → reward) in operational depth |

Rejected / unreachable samples (recorded):

- **Rockerbox** (reference management) — rockerbox.com is now a marketing-measurement vendor (MTA/MMM/testing, "DV Synergy"); the reference-management vendor no longer occupies the domain. Product mismatch; not usable.
- **UserEvidence** (customer-evidence pole) — userevidence.com returned 403, then timed out. Abandoned per network rules; the customer-evidence sub-pole is under-sampled.
- **Ambassify** — now positioned as **Employee Advocacy** software (EU market leader; use cases: employee advocacy, employer branding, dealer advocacy). Product mismatch for this Type; useful only as evidence that employee advocacy is a separate market.
- **G2 category page** — 403; market-category composition not independently verified.

## Sources

All research performed 2026-09-08 via live fetch.

Tier 1 (operational documentation):

- BrandChamp Knowledge Base (Help Scout) — https://support.brandchamp.io/ (category index)
- BrandChamp — "Walk Through - Creating a Social Media Activity" — https://support.brandchamp.io/article/28-walk-through-creating-a-social-media-activity
- BrandChamp — "Walk Through - Completing and Approving an Activity" — https://support.brandchamp.io/article/29-walk-through-completing-and-approving-an-activity

Tier 2 (official product pages):

- Influitive — https://influitive.com/ (homepage)
- Influitive — Customer Advocacy Platform — https://influitive.com/customer-advocacy-platform/
- Influitive — Brand Advocacy Tools (features) — https://influitive.com/customer-advocacy-software/features/
- Influitive — Advocate Marketing Dictionary — https://influitive.com/dictionary/
- SlapFive — https://www.slapfive.com/ (homepage)
- SlapFive — Customer Advocacy — https://www.slapfive.com/customer-advocacy/
- SlapFive — Customer Reference Management — https://www.slapfive.com/customer-reference-management-software/
- SlapFive — Platform — https://www.slapfive.com/platform/
- ReferenceEdge (Point of Reference) — https://www.referenceedge.com/ (homepage + features/benefits)
- BrandChamp — https://brandchamp.io/ (homepage)

Source-access limitations:

- Influitive's support desk (influitive-supportdesk.zendesk.com) is **closed** ("this help center no longer exists"). Influitive evidence is homepage/features/dictionary level (Tier 2).
- help.slapfive.com — transport error. SlapFive evidence is product-page level (Tier 2).
- ReferenceEdge — no public help center found; evidence is the features page (Tier 2, unusually detailed).
- userevidence.com — 403 + timeout; abandoned.
- www.g2.com — 403.

Per evidence rules: claims drawn only from product pages are marked B (cross-product commonality from pages) or kept product-specific; no precise numeric limits are asserted for the B2B pole in the final document.

## Product Observations

### Influitive (Tier 2: homepage, customer-advocacy-platform, features, dictionary)

Evidence layer: A for dictionary definitions (official educational docs); B for product structure (marketing pages).

- Positioning: "The market-leading advocacy, community, and engagement platform"; "customer advocacy platform"; G2 leader badge in Customer Advocacy.
- Use-case taxonomy (site nav, stable across pages): Get More Reviews; Amplify Social Media; Grow Product Adoption; **Manage Customer References**; Get Customer Feedback; Onboard/Train & Empower Customers; Drive More Customer Referrals; Nurture Impactful Customer Stories.
- Program model: "**Discover, nurture, and mobilize** advocates"; "gamified campaigns that drive value"; guided customer journeys; customer community/engagement.
- Features page: social-share amplification with tracking; "**Write a Review' activity**" targeting G2, TrustRadius, Gartner, TrustPilot; testimonials; **referrals/introductions pushed to CRM** or Multichannel Marketing Hub; **reference pool** growth + "leverage our Salesforce app… matches the right reference to the right opportunity and helps you measure impact"; UGC/speaker sourcing "our gamified activities will help you source, interview, and reward contributors".
- Customer-advocacy-platform page: "Discover new advocates and build **data-rich profiles** on each… gather **zero-party data** and learn how/when to engage them **on their terms**"; "Build a powerful **reference pool**… recruit new referenceable customers"; "Gather referrals… members can track each milestone"; customer quotes describe: salespeople requesting "specific kinds of product references" from a "community of customers who have already raised their hands"; "create, manage, and track our customer advocacy efforts with a single solution"; "cultivate super-users/customers that step up for any advocacy opportunities".
- Dictionary (official vocabulary, evidence A):
  - **Advocates**: "customers, partners, employees, influencers and other stakeholders who are willing to publicly support, endorse or recommend your company, products, or services."
  - **Asks**: "the fuel of an advocate marketing campaign… requests for your advocates to take action such as participate in a case study, testimonial or survey, write a product review or another piece of content."
  - **Challenges**: "targeted 'asks' that motivate advocates to outperform one another."
  - **Badges / Gamification / Rewards**: incentives for participation; "rewards are incentives that encourage advocates to perform certain tasks."
  - **Advocate Recruitment**: "not every customer is suited to be an advocate… identify those who would be the most effective."
  - **Advocate Experience**: "what makes it fun, enjoyable and rewarding to participate."
  - **Customer Reference Program**: "applies structure to the process of finding right references" when "a prospect asks for references."
  - **SAPS** motivators (Status, Access, Power, Stuff) for choosing asks.
  - **Advocate Marketer**: the operator role — "manage a company's happiest customers and motivate them to help the company achieve business objectives."
- Separate product lines on the same site: Customer Community, Customer Loyalty, Customer Experience, Customer Success, **Employee Advocacy** — vendor itself separates advocacy from loyalty and from employee advocacy.

### SlapFive (Tier 2: homepage, customer-advocacy, reference-management, platform)

Evidence layer: B (official product pages).

- Positioning: "Customer Voice Intelligence — the **verified system of record for customer advocacy and proof**"; "CMA (Customer Marketing & Advocacy) System of Record"; "Run advocacy like a system, not a spreadsheet."
- **Advocate & Proof System of Record**: "Track advocate **preferences, permissions, limits & activities** — plus verified customer content — synced with signals from third-party apps."
- **AI-Charged Advocate Sourcing**: "listen for signals across communities, call recordings & more — identifying and engaging the right advocates automatically."
- **Reference Automation**: "Automate **requesting, fulfilling, approving, and scheduling references** for sales and marketing, with **revenue influence tracked automatically**."
- Customer Advocacy page (four-part motion):
  1. **Segment customers** on the fly: demographic attributes of customers and their companies; activity types selected as preferences; topics of interest; history of activities performed.
  2. **Offer opportunities to perform acts of advocacy**: right opportunity/right customer/right time via preferred channels; auto-send on engagement milestones; triggered from events/scores in Salesforce, Gainsight, ChurnZero; embedded inside Vanilla/Higher Logic, Khoros communities.
  3. **Recognize customers**: track and score advocacy activities; recognize at engagement or revenue-influence levels; automate appreciation gifts via gifting services (XOXODay, Sendoso, Alyce).
  4. **Gamify**: hub of advocacy opportunities; points per activity; leaderboard ranked by Engagement Score.
- Reference management page ("Random Acts of Customer Proof" vs a managed process):
  - Anyone submits a request from any system or web page — sales reps request reference customers and content **from a Salesforce Opportunity**; auto-notification; reference managers log requests sent by email/Slack.
  - Find the best customers/content: filter on demographics and activity history; **forward a request to the Account Executive or CSM to approve use of their customer**; send the opportunity to the customer and track their response; **see historical and pending requests to avoid overuse**; requester tracks status from the Salesforce Opportunity.
  - **Recorded References**: storyboards of video snippets answering top reference-call questions; available 24×7 in Salesforce, Highspot, Seismic, or any sales portal; notify reps when prospects view.
  - Program optimization: track reasons requests weren't fulfilled; measure fulfillment time and fulfillment rate; dashboards of customer/content influence on revenue and pipeline; assess reference pools for coverage gaps.
- Platform page: workflow automation (advocate outreach → content approval); AI (content analysis, advocate matching, performance predictions); integrations (Salesforce, HubSpot, Marketo, Zendesk); CMS for advocate-generated content with brand consistency/quality control; dedicated Salesforce app; enterprise governance (permissions, approval workflows); revenue influence analytics.
- Other named products: Customer Programs, Customer Content, Customer Campaigns, **Advocate Job Change Tracker**, Community Connector, Salesforce App; use cases include Peer Review Programs, Customer Advisory Boards, Case Studies, Voice of the Customer, Sales Win-Wires.

### ReferenceEdge / Point of Reference (Tier 2: homepage + features — detailed)

Evidence layer: B (official product page, feature-level depth).

- Positioning: "Customer Advocacy Platform"; "ReferenceEdge centralizes **advocate data** and streamlines workflows… **From recruiting to request management**"; "Built for Everyone Who Relies on Advocates — marketers find/request advocates for events, reviews, social content, testimonials; sales teams get… **vetted advocates for reference calls**"; "100% Salesforce Native" (installed into the customer's Salesforce environment, not a plug-in).
- **Advocate database**: "Keep track of who is considered an advocate, their current status, and **for which advocate activities they are available**"; tag accounts/contacts as program members; activate/deactivate status; metadata tags (industry, use cases, product, persona).
- **Search**: filter by industry/product/region + keywords; contacts tagged with advocate activities such as "event speaking, reviews, press releases, reference calls, quotes, site visits, product betas".
- **Recruiting automation** (4 features): Nominations (any user nominates a customer); Reference Lead Finder (auto follow-up on recently closed/won opportunities to assess referenceability); Reference Prospector (internal campaign to gauge account referenceability); Profile Update Minder (automates routine review/update of reference profiles).
- **Request management**: "accelerate, track, and manage customer reference activities"; "automated **peer-to-peer request routing**, real-time tracking, and built-in process management… initiated from within Salesforce, or Slack, using our ReferenceBot app."
- **Close the loop**: automatic feedback after each activity — outcomes: didn't/won't happen; will happen later; went well; didn't go well.
- **Rewards (dual-sided)**: customers earn points for "reference calls, webinars, and case studies"; **internal ReferenceEdge users** earn points for "nominating advocate candidates, assisting with arranging a reference activity, or periodically updating reference profile information"; Salesforce leaderboards; redemption "cash, prizes, event attendance, or services."
- **Content**: search/share tagged customer content (videos, reviews, case studies, press releases, quotes) via **microsites** that capture click activity and visitor ratings.
- **Program Health Monitor**: set program goals, track progress; "26 quick start templates covering the most common program motions such as nominations, reference recruiting, requests, and reference searches."
- **Win/loss insights**: Data Collector configurable surveys; results become searchable content.
- **Data currency**: profile info "has a shelf life"; Profile Update Minder engages CSMs/account managers/sales to keep profiles current.
- **Integrations**: Slack, Microsoft Teams, Marketo, Eloqua, Gainsight, Influitive, UserEvidence, Salesforce Experience Cloud, CRM Analytics, Agentforce (AI agents wrangling "advocate requests, customer nominations, profile updates").
- **Advocacy Gap Predictor** (AI): scans opportunity data to "forecast where advocate firepower will be needed in 60, 90, and 120 days" and pairs with the advocate pool to guide recruitment.

### BrandChamp (Tier 1: KB articles; Tier 2: homepage)

Evidence layer: A for KB mechanics; B for positioning.

- Positioning: "The Word-of-Mouth Revenue Platform" — "Run **ambassador, advocate, affiliate, and referral programs** on one platform. Manage it yourself, or let our experts handle it"; program types: Advocacy & Ambassador Programs; Affiliate & Referral Programs; Customer Advocacy & Loyalty Programs; Creator & Influencer Programs. Use cases include "Customer Advocacy & LTV Growth".
- Platform modules: Referral Tracking; Branded Mobile App; **Activities & Campaigns**; Rewards & Incentives; Community; Communication; **Gamification**; Analytics; Workflow Automation; API & Webhooks.
- KB — Activity Type creation (admin side):
  - Activity Types defined in the admin "Activities" page; pre-defined templates (e.g., Social Share Activity) or Custom Activity; some types (Referral, Onboarding) creatable only once.
  - General: title (becomes permalink), instructions (what to do: networks, images, hashtags), icon/image, **Resources** (shareable assets incl. referral links and discount codes), activity categories (for advocate filtering/discovery), sorting order.
  - **Tasks**: completion instructions; completion format — **web address / text / file upload**; "Pick" buttons let advocates authenticate with Instagram/Facebook/Twitter and select their post (pre-fills the link with preview).
  - **Automated approval** optional; otherwise manual review.
  - **Rewards & Limits**: completion limits per period (Monthly / Weekly / Daily / Any) with per-advocate caps; reward = **points** (redeemable from a rewards catalog later) OR an **Activity Reward token** (e.g., a discount voucher) OR a **USD cash balance**.
  - **Availability**: BrandChamp tag filters (tiers; tags invisible to advocates), start/end dates, availability toggle; live preview of the advocate-portal rendering.
- KB — completion & approval lifecycle:
  - Advocate opens the activity in their portal, reads instructions, completes the task with proof (post link via Pick or paste), submits.
  - Admin reviews in the "**Awaiting Review**" queue with inline preview of the post; **Approve or Reject** (rejection requires a comment, e.g., missing hashtags); advocate is emailed, sees the rejected task "In Progress", edits and **Resubmits** (or deletes the submission); resubmissions re-enter the queue; on approval the reward is credited (e.g., 50 points balance).
  - Multi-task activities: reward only when **all required tasks** are approved.
  - Next step in KB: advocate claims/uses points from the rewards catalog.
- Referral tracking module: "Equip participants, automate attribution, and reward performance for any type of referral."
- KB categories confirm the object set: Activities, Activity Templates, Rewards, Cash Payments, Referrals, BrandChamps (participants), BrandChamp Tiers, Emails, Configuration, Integrations.

## Cross-product Comparison

| Structure | Influitive | SlapFive | ReferenceEdge | BrandChamp |
|---|---|---|---|---|
| Advocate population of record | ✔ "data-rich profiles", zero-party data, "on their terms" | ✔ "preferences, permissions, limits & activities" | ✔ program-member tags on accounts/contacts, status, availability per activity, metadata | ✔ BrandChamps with tiers (tags), profiles |
| Advocate sourcing/recruiting | ✔ "discover… advocates", recruitment (dictionary) | ✔ AI sourcing from communities/call recordings | ✔ nominations, closed-won follow-up, prospector, profile-update automation | ✔ onboarding activity; enrollment |
| Advocacy asks as managed objects | ✔ challenges/asks (dictionary), gamified activities | ✔ "acts of advocacy" opportunities, hub | ✔ advocate-activity tags; requests; program templates | ✔ Activity Types with tasks, templates, categories |
| Targeting/segmentation | ✔ personalized journeys | ✔ segment on demographics/preferences/topics/history | ✔ metadata filters (industry/product/region/persona) | ✔ tag filters, start/end dates |
| Advocate-side surface | ✔ advocate hub/portal (implied by challenges/points) | ✔ hub of opportunities; community embeds | ✔ (lighter; Salesforce-mediated; Engagement Essentials comms/polls) | ✔ portal with activities, submission, points, rewards catalog |
| Completion proof & review gate | ✔ gamified activities source/interview/reward | ✔ requests routed to Trusted Contacts for review/approval; track customer response | ✔ close-the-loop feedback after each activity | ✔ submit → Awaiting Review → approve/reject with comment → resubmit |
| Participation recorded per advocate | ✔ track advocacy efforts; milestones | ✔ activity history; scoring | ✔ activity tags; request history | ✔ activity instances, points balance |
| Recognition/rewards | ✔ points/badges (dictionary), rewards | ✔ points, leaderboards, gifting integrations | ✔ points for customers AND internal users; leaderboards; redemption | ✔ points / reward tokens / cash; rewards catalog |
| Internal request intake (reference desk) | ✔ Salesforce app matches references to opportunities | ✔ requests from Salesforce Opportunity/email/Slack; status tracking | ✔ peer-to-peer routing from Salesforce/Slack (ReferenceBot) | ✘ (referral tracking instead) |
| Overuse/consent governance | ✔ engage "on their terms" | ✔ preferences, permissions, limits; avoid overuse via history | ✔ activity preferences, use limits, availability per activity | ✔ per-activity completion limits; tier visibility |
| Data currency | ✔ zero-party data profiles | ✔ Advocate Job Change Tracker | ✔ Profile Update Minder | ✔ (tags/profiles; less emphasized) |
| Advocacy content/proof outputs | ✔ reviews, testimonials, stories, UGC | ✔ verified customer content; CMS; Recorded References | ✔ tagged content (videos/reviews/case studies/quotes) shared via microsites | ✔ UGC via social activities |
| Program measurement | ✔ track advocacy efforts; ROI calculator | ✔ fulfillment rate/time, unfulfilled reasons, revenue influence, coverage gaps | ✔ Program Health Monitor (goals, 26 templates), win/loss insights | ✔ analytics module |
| Revenue influence attribution | ✔ measure impact (Salesforce app) | ✔ revenue influence tracked automatically | ✔ "reference activity tied directly to closed-won deals" | ✔ referral sales attribution |
| Community embedding | ✔ customer community platform (separate line) | ✔ Community Connector (Vanilla/Khoros embeds) | ✘ | ✔ Community hub module |
| Referral as activity | ✔ referrals pushed to CRM | ✔ Customer Referrals product | ✘ | ✔ referral tracking module |
| Platform substrate | standalone SaaS + Salesforce app | standalone SaaS + Salesforce app | 100% Salesforce-native | standalone self-serve SaaS |
| Customer tier / posture | enterprise, services-led | enterprise, services-led | enterprise (Salesforce shops) | self-serve SMB/consumer brands + managed option |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A brand-side system of record for operating a customer advocacy program. Minimal structure — three jointly-held parts:

```text
Advocate population of record
  (identified customers held as managed program members:
   standing, advocacy-relevant attributes, preferences/limits, participation history)
└── Advocacy ask (the unit of work)
    (brand-defined request for a specific advocacy action:
     reference call, review, testimonial, case study, referral,
     speaking, social share, community answer, beta/feedback…)
    └── Managed ask → participation loop
        (ask targeted/offered to suitable advocates
         → advocate responds and completes with proof/output
         → review/approval gate
         → participation recorded against the advocate and the program)
```

Tests:

- Remove the advocate population of record → an anonymous campaign tool or a CRM segment; no program.
- Remove the ask → a contact database with activity history (CRM territory).
- Remove the managed loop (targeting, response, review, recording) → one-off outreach; no overuse protection, no measurement, no program memory.

Jointly-held is load-bearing: advocates + asks without the loop = a mailing list with a wish list; asks + loop without advocate records = a campaign tool; advocates + loop without asks = a CRM.

Not in L0 (deliberately):

- **Recognition/rewards (points, badges, levels, gifts)** — present in 4/4 sampled products and central to the advocate-hub philosophy, but a rewards-less reference program (spreadsheet-era or a bare reference tracker) still satisfies the core. Rewards are the loop's motivator, not its skeleton.
- **Reference-request routing from sales** — the defining workflow of the B2B reference pole (SlapFive, ReferenceEdge, Influitive's Salesforce app) but absent in the ambassador/self-serve pole (BrandChamp), where the program pushes activities rather than fulfilling internal requests.
- **Gamification** — a participation philosophy (hub + challenges + leaderboards), not the Type's skeleton.
- **Advocacy content management, revenue-influence analytics, community embedding, AI sourcing** — mature additions.

Historical check (§24-style): the pre-software customer reference program — a reference list (spreadsheet/CRM notes), a reference manager arranging calls, a log of who spoke where, and thanks to the advocates — satisfies all three parts without gamification, portals, cloud, or AI. Early-2000s reference-management tools satisfy it without social/challenges. The definition does not over-fit the gamified-hub era.

### L1 — Common Mature Structure

Present across most sampled products; needed to make the Type operational, not definitional:

- Recognition & rewards machinery: points, badges, levels, leaderboards, reward catalogs, gifting-service integrations; ReferenceEdge extends points to internal users (nominating, arranging, updating profiles).
- Advocate portal/hub: available activities, submission with proof, points balance, rewards catalog, profile/preferences.
- Advocate sourcing & recruiting: nominations, closed-won follow-up, internal referenceability campaigns, profile-update automation, AI listening across communities/call recordings.
- Reference-request management (B2B pole): request intake from CRM/Slack/email, routing to program managers, account-team (AE/CSM) approval before use, fulfillment tracking, overuse avoidance via historical/pending request visibility.
- Advocate data currency: profile-update automation, job-change tracking.
- Advocacy content management: verified customer content (stories, quotes, videos, reviews), tagging, microsites/sales-portal distribution (Highspot/Seismic), recorded-reference storyboards.
- Program measurement: activity counts, engagement scores, fulfillment rate/time, unfulfilled reasons, coverage-gap analysis, program health goals, revenue influence attribution.
- Integrations: CRM (Salesforce, HubSpot), marketing automation (Marketo, Eloqua), CS platforms (Gainsight, ChurnZero), communities (Khoros, Vanilla/Higher Logic), gifting services (Sendoso, Alyce, XOXODay), sales-content portals, review sites (G2, TrustRadius, Gartner, Trustpilot), messaging (Slack, Teams).
- Community embedding of advocacy opportunities.
- AI (era-current): advocate sourcing/matching, content generation, agents wrangling requests/nominations/profile updates.

### L2 — Variant / Optional Structure

Depends on segment, philosophy, substrate, scale:

- Program philosophy: gamified advocate hub (challenges/points/community — Influitive) vs request-driven reference desk (ReferenceEdge, SlapFive reference automation) vs self-serve ambassador/advocate programs (BrandChamp) vs customer-evidence platforms (UserEvidence — under-sampled this pass).
- Participant population: customers only vs customers + partners + employees + influencers (Influitive's dictionary includes all four).
- Activity mix: reference/review/story-heavy (B2B) vs social/UGC/referral-heavy (consumer brands).
- Platform substrate: Salesforce-native (advocate data lives in Salesforce objects) vs standalone SaaS with CRM sync vs self-serve multi-program platform.
- Referral machinery depth: referral as one activity vs a full referral program with offer/attribution/reward fulfillment (seam to Referral Marketing Platform).
- Services posture: self-serve vs advisor-led vs managed program services.
- Community as adjacent surface vs embedded channel.
- Employee advocacy as a separate product line (different Type).

### L3 — Vendor-specific Structure

Kept out of the final document; examples:

- Influitive: AdvocateHub lineage, Groovy AI agent, BAMMIE awards, Fearless 50, Virtual EventHub, SAPS framework, "zero-party data" framing, Next-Gen Elevate platform naming.
- SlapFive: CMA System of Record, CustomerX community, Recorded References storyboards, Advocate Job Change Tracker, AEO (answer-engine optimization), Universal MCP access, Minute Booth service, "Random Acts of Customer Proof" coinage.
- ReferenceEdge: ReferenceBot, Reference Lead Finder, Reference Prospector, Profile Update Minder, Advocacy Gap Predictor (60/90/120-day forecasts), Data Collector, RefEdge DM, Program Health Monitor (26 templates), Engagement Essentials, 100%-Salesforce-native security posture.
- BrandChamp: "BrandChamps" participant terminology, tier tags (invisible to advocates), Activity Reward tokens, PayPal mass payments, "Pick" social-post buttons, Help Scout KB structure.

## Vendor-specific Findings

- **Dual-sided gamification** (points for internal users, not just advocates) is directly documented only in ReferenceEdge; treat as product-specific/optional.
- **Recorded references** (video storyboards replacing live reference calls) is directly documented only in SlapFive; product-specific.
- **Job-change tracking** of advocates is directly documented only in SlapFive (named product); ReferenceEdge's Profile Update Minder addresses the same data-currency problem differently; treat the problem as common, the mechanisms as variant.
- **Rewards-less operation**: no sampled product markets a rewards-less mode, but the reference-management pole's core (database + requests + tracking) is structurally separable from its rewards module (ReferenceEdge lists rewards as one feature among many). This supports holding rewards out of the defining core.
- Influitive's dictionary defines the market's own vocabulary (advocates, asks, challenges, recruitment, advocate experience, customer reference program) — used as Tier-A evidence of the Type's self-understanding.

## Boundary Findings

1. **vs Referral Marketing Platform (§06 sibling — DISCHARGES the referral-side joint-review flag from this side)**: referral appears inside advocacy platforms as one activity among many (Influitive "Drive More Customer Referrals" use case; SlapFive Customer Referrals product; BrandChamp referral tracking module). The Referral Type's world is the referral program itself — offer design, the advocate's personal trackable identity, attributed conversion, reward fulfillment. The Advocacy Type's world is the advocate relationship and the breadth of asks managed against advocate records. Test: if the only ask is "refer" and the machinery centers on offer/attribution/reward fulfillment → Referral Marketing Platform; if referral is one activity in a multi-ask program bound to advocate records → Customer Advocacy Platform. Straddle zone is real (BrandChamp runs both on one platform; SlapFive sells both); the participant-and-program-scope test separates the Types.
2. **vs Loyalty Program Management**: loyalty rewards the customer's own repeat purchase; advocacy rewards contributions to the brand's commercial motion (evidence, references, referrals). Influitive ships Customer Loyalty as a separate solution — vendor-confirmed separation. Shared currencies (points) and shared vendors make the straddle real; the test is what the reward attaches to.
3. **vs Influencer Marketing Platform**: advocates are existing customers; influencers are external creators with audiences. Asks differ accordingly (reference/review/story vs content collaboration/campaigns). Influitive's dictionary explicitly distinguishes influencer marketing (thought leaders) from advocate marketing.
4. **vs Affiliate Management Platform**: affiliate participants are registered external partners earning commissions on tracked sales; advocates are the brand's own customers. Different enrollment, economics, and relationship.
5. **vs Employee Advocacy (adjacent market, no directory leaf)**: employees sharing brand content vs customers providing proof. Influitive and Ambassify both ship employee advocacy as a separate product/solution — vendor-confirmed separation. Ambassify's pivot to employee-only positioning corroborates that these are different markets.
6. **vs Voice of Customer Platform / Customer Feedback Management**: VoC's primary object is the feedback signal (surveys, NPS, verbatims analyzed at scale); advocacy's primary object is the advocacy action. Feedback/beta tests appear here as one activity type; systematic feedback analysis is VoC territory. SlapFive lists "Voice of the Customer Programs" as a use case — a gradient, not a wall.
7. **vs Advocacy Platform (§25) — NAME COLLISION, NOT ALIASES**: §25 mobilizes supporters toward policy decision-makers (legislators/regulators) with civic action types; §06 mobilizes customers toward commercial outcomes (references, reviews, referrals) with no policy targets. Confirms the structural test recorded by the §25 pass from this side.
8. **vs Review Platform (§02.10)**: review platforms are consumer-facing discovery surfaces; advocacy platforms are brand-side mobilization systems that drive customers to write reviews ON those platforms (Influitive's 'Write a Review' activity targeting G2/TrustRadius/Gartner/Trustpilot).
9. **vs Customer Community Platform**: community's primary object is member-to-member discussion; advocacy embeds opportunities inside communities (SlapFive Community Connector; Influitive community line) but the advocate record + ask loop is the advocacy Type's core. Vendors ship both as separate products.
10. **vs CRM**: advocate records ride on CRM accounts/contacts (ReferenceEdge is Salesforce-native; SlapFive syncs with Salesforce). CRM holds the relationship; advocacy holds the program (standing, asks, activities, outputs, governance). Remove the asks and the loop → CRM tags and activity history.
11. **vs Sales-enablement content libraries**: advocacy produces customer proof that sales consumes; the distribution surface (Highspot/Seismic/sales portals) is where outputs go, not where advocate records live.

## Uncertainties

1. **Tier-1 depth is one-sided**: only BrandChamp yielded operational help-center docs. Influitive's help center is closed; SlapFive's help center was unreachable; ReferenceEdge publishes no public KB. Claims about the B2B pole's internal mechanics (request lifecycle states, approval chains, portal details) are calibrated to product-page level; no precise numeric limits asserted for that pole.
2. **Customer-evidence sub-pole under-sampled**: UserEvidence unreachable (403 + timeout). The "customer proof points/stats" variant is described from integration mentions (ReferenceEdge integrates UserEvidence) only; held as a named variant with reduced confidence.
3. **Rockerbox (reference management) no longer occupies rockerbox.com** (now a marketing-measurement vendor). The reference-management market's shape rests on ReferenceEdge + SlapFive evidence.
4. **Rewards definitional?** Near-universal in the sample (4/4) but held out of the defining core on structural grounds (rewards-less reference programs satisfy the core; ReferenceEdge's rewards are one module). If the directory ever revisits, this is the seam to re-test.
5. **G2 category composition** not independently verified (403). The sampled four are drawn from the market's self-identified cluster (Influitive's G2 badge in Customer Advocacy; ReferenceEdge's self-positioning; SlapFive's positioning; BrandChamp's program-type taxonomy).
6. **Advocate-portal mechanics for the B2B pole** (Influitive/SlapFive/ReferenceEdge) are known at marketing-page depth; the final document describes them conceptually without asserting specific states or limits.

## Final Synthesis

A Customer Advocacy Platform is a brand-side system of record for operating a customer advocacy program. Its world contains three jointly-held structures: a managed population of advocates — the brand's own customers, held as program members with advocacy-relevant attributes, preferences, limits, and participation history; advocacy asks — brand-defined requests for specific advocacy actions (reference calls, reviews, testimonials, case studies, referrals, speaking, social shares, community answers, beta/feedback); and the managed loop that connects them — asks are targeted to suitable advocates, advocates respond and complete with proof, completions pass a review/approval gate, and participation is recorded against the advocate and the program. Around that core, mature products add recognition and rewards (points, badges, levels, gifting), advocate portals, recruiting automation, reference-request routing with account-team approval and overuse protection, advocacy-content management and distribution, program-health and revenue-influence measurement, and integrations across the CRM/marketing/CS/community stack. The market splits into recognizable poles — the gamified advocate hub, the request-driven reference desk, the self-serve ambassador/advocate platform, and the customer-evidence platform — but all realize the same three-part core. The Type's edges are held by participant identity and program scope: referral-only offer machinery is a Referral Marketing Platform; own-purchase rewards are Loyalty; external creators are Influencer Marketing; employees are Employee Advocacy; policy targets are the §25 Advocacy Platform; feedback-signal analysis is Voice of Customer.
