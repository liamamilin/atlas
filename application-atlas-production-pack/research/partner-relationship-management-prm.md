# Research Notes — Partner Relationship Management / PRM

Research date: 2026-09-06
Slug: partner-relationship-management-prm
Directory leaf: "Partner Relationship Management / PRM" (§07 Sales, Customer & Revenue)

## Research Goal

Understand what a Partner Relationship Management application actually is as a software structure: what objects exist inside it, who uses it on which surfaces, how the vendor↔partner workflow flows, which states and rules govern it, and where its boundary lies against CRM, channel sales management, affiliate management, dealer/distributor portals, and supplier portals.

## Initial Boundary (pre-research hypothesis)

- PRM = software a vendor company uses to manage its network of external selling partners (resellers, VARs, distributors, agents, referral partners, affiliates, MSPs, SIs).
- Primary users: vendor-side channel staff (channel account managers, partner operations, partner marketing) plus partner-side users via an authenticated portal.
- Nearest neighbors: CRM (partner records may live there), Channel Sales Management (sibling leaf in §07), Affiliate Management Platform (§06), Dealer / Distributor Commerce Portal (§05.17), Supplier Portal (§10, buy-side), Customer Training / Academy Platform (§07).
- Suspected risk: "Channel Sales Management" may be an alias/superset of PRM; "partner portal" may be a capability rather than a Type.

## Research Questions

1. What is the central record — partner organization, partner user, or program membership? How do they relate?
2. What is the partner lifecycle (recruit → onboard → activate → manage → offboard) and where does it live in the product?
3. How does deal registration work end-to-end (submit → review/approve → protection → stage updates → close → payout)?
4. How does lead distribution work (vendor → partner assignment, acceptance, tracking)?
5. How do MDF/co-op funds work (allocation, requests, approval, reimbursement, ROI)?
6. How deep is the enablement stack (content library, training/certification, co-branded collateral, news)?
7. How are tiers/programs structured and enforced?
8. What roles and permissions exist on both sides?
9. How does PRM relate to CRM (embedded vs standalone vs synced)?
10. What distinguishes PRM from affiliate management, dealer portals, and supplier portals?

## Representative Products

Selected for market representation, documentation accessibility, different product philosophy, and different customer tiers:

| Product | Segment / philosophy | Evidence level reached |
|---|---|---|
| Channeltivity | Pure-play PRM, high-tech channel since 2007; SMB → mid-market → enterprise; modular, configuration-first | Tier-1 (help-center articles) + Tier-2 (product pages) |
| Impartner | Pure-play PRM, mid-market → enterprise; "partner revenue management" positioning; journey/module suite | Tier-2 (product pages, edition table, FAQ) |
| Magentrix | Pure-play PRM, enterprise; PaaS philosophy; CRM schema-mirroring integration as differentiator | Tier-2 (product + feature pages) |

Rejected / unreachable samples (see Source-access Limitations): Salesforce PRM (help center JS-blocked), Zoho CRM PRM (URLs 404), Oracle Partner Management Cloud (docs URL 404), Allbound (403), Kiflo (transport error), Webinfinity (redirects to 360insights marketing).

## Sources

Fetched 2026-09-06:

- Channeltivity homepage — https://www.channeltivity.com/
- Channeltivity PRM product page — https://www.channeltivity.com/partner-relationship-management/
- Channeltivity Knowledge Base root — https://help.channeltivity.com/support/solutions
- Channeltivity, "What is the Deal Registration Module and how does it work?" — https://help.channeltivity.com/support/solutions/articles/3000060309
- Channeltivity, "Partner Approval and Onboarding Guide" — https://help.channeltivity.com/support/solutions/articles/3000070830
- Channeltivity, "What is the MDF Module and how does it work?" — https://help.channeltivity.com/support/solutions/articles/3000074569
- Impartner homepage — https://www.impartner.com/
- Impartner PRM product page — https://impartner.com/partner-relationship-management/
- Magentrix homepage — https://www.magentrix.com/
- Magentrix Deal Registration feature page — https://www.magentrix.com/features/deal-registration

### Source-access Limitations

- Salesforce Help (help.salesforce.com) returns a JS/CSS error to the fetcher; salesforce.com product paths 404 or redirect to a generic resources hub. Salesforce PRM could not be used as an evidence source. It is referenced only as a market-positioning data point via Magentrix's own positioning ("Alternative to Salesforce Partner Cloud").
- Zoho PRM URLs (zoho.com/prm/, zoho.com/crm/prm/, zoho.com/crm/zohopartners/, zoho.com/partner-plus/) all 404; Bing/DuckDuckGo searches did not surface the correct page. Zoho abandoned.
- Oracle "Implementing Partner Relationship Management" docs URL guess 404; search engines (local Bing) returned irrelevant results. Oracle abandoned.
- Allbound 403; Kiflo transport error; Webinfinity redirects to 360insights ecosystem marketing.
- DuckDuckGo HTML search timed out twice; Bing (CN-localized) ignored the site: operator.
- Consequence: the enterprise suite-embedded segment (Salesforce/Oracle) is evidenced only indirectly. All precise operational claims in the final document are anchored on the three reachable samples; no numeric defaults (protection windows, fund amounts, tier thresholds) are asserted as universal.

## Product A — Channeltivity

### Key observations (Tier-1 help center + Tier-2 product pages)

**Module map (product page, three functional areas):**
- Partner Enablement: Partner Recruitment (capture/identify/onboard prospective partners; segment by type, region, user count, certifications, custom fields), Training & Certification (course/certification progress, quiz performance, organization certificates), Business Planning (joint goals, approval workflow, progress reports).
- Channel Marketing: Partner Portal (self-service hub; monitor logins and activity — referrals created, MDF requests, leads opened), Resource Library (permission-gated; ratings/downloads reports), MDF Management (approval process; track new/allocated/reimbursed funds and resulting pipeline), Email Marketing, Co-Branded Collateral.
- Channel Sales: Deal Registration (approval process; sales-cycle position; close dates; track payouts), Referrals & Commissions (capture referrals, monitor referral fees), Lead Distribution (assign leads to partners; track open→close with status changes/comments/files), Distributor Management (integrate distributors into channel pipelines; distributor↔partner relationships).
- Platform: notifications & reminders, analytics & reporting, multi-language, partner dashboards, social sharing & collaboration.
- Integrations: HubSpot (bi-directional sync of Referrals, Leads, Deals, Partners), Salesforce (native sync + Managed Package), Dynamics 365, Zapier, SAML SSO, APIs.

**Partner lifecycle (Tier-1, "Partner Approval and Onboarding Guide"):**
- "Prospective Partner" = a Partner Organization not yet accepted into the program. Applies via public "Become a Partner" form → creates an unassigned Prospective Partner Organization + a Contact record of the submitter. Distinct from "Request Access" form (existing org's user asking for portal access).
- Internal vetting: assign to an Internal User; Prospective Partner Details section holds Stage (vetting pipeline with configurable stages, ending in "Closed Won (make Partner active)"), Expected Close Date, Assigned to (auto-becomes the org's Primary Partner Manager on activation), Expected Yearly Revenue, Description.
- Activation: Actions → Make Active / Make Inactive. On activation, system prompts to promote the org's Contacts to Users (assign to Groups → email activation link).
- Partner Type field categorizes partners (reporting; drives Agreements assignment).
- Agreements functionality: agreement templates assigned to organizations; authorized partner user digitally signs pending agreements at first login; manual upload of signed agreements supported.
- Groups control portal permissions (content access, module access).

**Deal registration (Tier-1):**
- Partner user logs into portal, submits Deal Registration form: prospect details (end-user customer account + contact), deal details (name, amount, Stage, Close Date, custom fields).
- Stage field = completion probability / sales-cycle progress; configurable whether partners can update it or it is read-only for partners.
- Registration Status field = vendor-controlled approval workflow, customizable statuses.
- Deal Overview page: progress bar (stage), Registration Status; History & Notes = timestamped change log + comments + file uploads (vendor↔partner collaboration).
- Deal expiration configurable. Salesforce/HubSpot integrations: deal registration can create a Lead/Deal in the CRM automatically or manually; CRM opportunities can be imported as deal registrations.
- Distributor module interplays with deal registrations (distributor assignment feature).

**MDF (Tier-1):**
- Funds issued to partner accounts via "Credit Transactions" with optional expiration dates (Balances & Fund Expiration features). Account Balance vs Available Balance distinction.
- Partner submits MDF Request Form; internal users review, update Status (configurable approval workflow), assign; comments/document upload in History; reimbursement = setting status to "Reimbursed", which debits funds automatically.
- Automated reminders: new funds available, balance report, expiring balances, expiring requests, stale requests.
- MDF ROI feature: partners link Deal Registrations to MDF-funded activities to compute ROI.

**Other Tier-1 modules:** SPIFF (campaigns, claims with statuses), Training & Certification (courses/lessons/quizzes; user and organization certifications), Lead Distribution (lead details hidden from partner until opened), Referral module (referral links, status workflow), News & Email Marketing, Forum, Business Planning (goals, approval, lock/unlock), Co-Branded Collateral, Multi-Language, GDPR consent tracking, Data API ("create prospective partners"), SAML SSO (as SP or IdP).

**Positioning (Tier-2):** segments Growth (~100 partners, recruiting/onboarding focus) / Mid-Market / Enterprise; "$4B+ active channel revenue managed"; CRM-first integrations (Salesforce, HubSpot, Dynamics, Zoho, NetSuite) + Crossbeam (account mapping), Okta, Stripe, SAP.

## Product B — Impartner

### Key observations (Tier-2 product pages)

**Positioning:** "PRM 3.0 — the only end-to-end partner revenue management platform"; rebrands PRM as "Partner Revenue Management". Forrester Wave PRM Leader (Q3 2023) claim. Editions: Emerge / Ignite / Pro / Enterprise (feature ladder).

**Partner journey stages (homepage journey graphic):** Recruit (partner identification, marketing automation) → Enroll (partner application, terms management) → Onboard (activation, journey orchestration, marketplace) → Engage & Communicate (news on demand, personalized alerts) → Train & Enable (personalized training & certification) → Tech Stack Integration → Propensity to Buy (model creation, scoring) → Generate Demand (TCMA, MDF, partner marketplace, referral management) → Manage Pipeline (lead distribution, deal registration) → Co-Sell → Sell & Transact (CPQ, marketplace transactions, asset library, co-branded collateral) → Motivate & Reward (program compliance, rewards management) → Plan & Optimize (business planning, AI sales coach) → Measure (analytics studio, reporting).

**Applications list:** Partner Lifecycle Management (Journey Builder), Pipeline Management (lead management; sync deal registration and partner leads with CRM), Partner Training & Certification (SCORM courses, quizzes, progress tracking; partner competencies), Market Development Funds (requests, fulfillment, ROI analysis), Impartner Marketplace (lead-gen marketplace on corporate site), Partner Business Planning (shared goals, partner-editable progress), Tiering and Compliance (Program Compliance Manager: code-free tier programs, compliance metrics, progress toward tiers/benefits), Reporting and Analytics, Paid Media for Partners, Referral Automation, HyperscalerGTM (partner-to-marketplace workflows across AWS/Azure/GCP), Aimi (AI layer), Orchestration Studio, Disti Connect (distribution), Impartner CPQ (self-serve quotes, e-signature), Rewards Management, News on Demand, Social on Demand (some purchasable without PRM).

**Edition table (Tier-2):** guided implementation, segmentation, SSO, click-to-agree terms management, multi-language, CMS, reporting & analytics, onboarding workflows, pipeline management, asset library, co-branded collateral, training & certification, journey builder, business planning, partner competencies, currency management, custom object extensibility, program compliance manager, product catalog & pricing models (CPQ), price books with segmentation, hyperscaler GTM, disti connect, MDF, rewards, TCMA, referral management, news/social on demand; integrations with Salesforce, Dynamics 365, HubSpot, Salesforce CPQ/RCA.

**Partner types named:** resellers, referral partners, ISVs, MSPs, affiliates, influencers, distributors, service partners (implementation specialists).

**FAQ (vendor's own definitions):**
- "What is PRM": business strategy + tools; example list: centralizes sales/marketing resources, automates onboarding, simplifies communication, facilitates asset sharing, manages deal registrations, automates referrals, supports business planning, provides performance analytics.
- "CRM vs PRM": CRM manages customer interactions; PRM tailored to partner management needs (lead distribution, deal registration, partner performance tracking).

## Product C — Magentrix

### Key observations (Tier-2 product + feature pages)

**Positioning:** "The Data Foundation for Channel Sales"; PaaS PRM; differentiator = CRM data & schema mirroring (Salesforce, Dynamics; HubSpot via field mapping due to API limits) vs competitors' field-mapping integrations; "Alternative to Salesforce Partner Cloud". SAML/OIDC SSO, RBAC, audit logs, AES-256/TLS, ISO 27001/SOC 2 claims.

**Feature map:** Deal Registration; Partner Pipeline Tracking; Lead Distribution; Partner Program Tiers (e.g., Authorized/Gold/Platinum labels as an example; tier-matched content, commissions, deal registration limits); Training (LMS); Co-branding; Files/Articles/Resources; Automation; Partner Payouts; Partner Self-registration; CRM Integrations; AI Partner Operations; Partner Journeys; Custom Hubs; Partner Segmentation; Role-based Sharing; MDF; Partner Incentives & Redemption; News Feeds; social-style groups & DMs; Marketplace (Partner Locator); PaaS developer console (IDE/CLI); Analytics/Reports/Dashboards.

**Deal registration detail (feature page):**
- 4 submission paths: portal form; ungated public page with cookieless tracking for attribution; email-to-portal (AI-assisted field population); bulk CSV upload.
- Pipeline Summary Pages: partner-facing real-time deal/pipeline status; per-segment custom pages; visual pipeline; metrics (total deals, total revenue, forecast).
- Deal Exclusivity Tracking: exclusive rights for the partner who brought the deal; protection period starts after vendor approval + conversion into an opportunity; expiration date = approval date + agreed duration; expiry triggers automatic notifications to partner and internal team.
- Deal Amendment: partners update close date/value/stage on assigned deals; permission-based field controls; CRM opportunity owner receives automated change alerts; changes sync to CRM.
- Lead Distribution: "Deal Inbox" for internal team to assign incoming registrations/opportunities to partners; automatic partner notification; partner reviews contact details/deal value/expected close; partner can accept or reject (communicating within the record).
- Lead Conversion: internal vetting; merge lead with existing CRM account/contact or create new; optional opportunity creation; field mapping for custom fields.
- CRM sync: bi-directional; "Smart Sync" default interval 15 minutes, adjustable to 1 minute (product-specific default — do not generalize).

**Category map (vendor's own, biased):** lists "Basic PRMs": Impartner, PartnerStack, ChannelScaler/Allbound, Zift/Unifyr, Channeltivity, Mindmatrix, Zinfi, 360insights, "all other PRMs except Salesforce Partner Cloud". Used here only as evidence that these brands form one product category — not for any structural claim.

## Cross-product Comparison

| Structure | Channeltivity | Impartner | Magentrix | Layer |
|---|---|---|---|---|
| Partner Organization as central record with lifecycle (prospective → active → inactive) | ✓ (Prospective Partner stages, Make Active/Inactive) | ✓ (Enroll/Onboard journey stages) | ✓ (self-registration, segmentation) | A (3×) |
| Partner-side authenticated users bound to their organization | ✓ (Contacts promoted to Users, Groups) | ✓ (portal users) | ✓ (RBAC, role-based sharing) | A (3×) |
| Public application/self-registration form | ✓ ("Become a Partner" form) | ✓ (Partner Application) | ✓ (Partner Self-registration) | A (3×) |
| Vendor-controlled approval workflows (partner apps, deals, MDF, plans) | ✓ (status-field workflows) | ✓ (journey/compliance) | ✓ (approval + conversion gates) | A (3×) |
| Deal registration with vendor approval + protection/exclusivity | ✓ (Registration Status, deal expiration) | ✓ (deal registration in Pipeline Management) | ✓ (Exclusivity Tracking, protection period, expiry alerts) | A (3×) |
| Deal/pipeline stages visible to partner | ✓ (Stage field, progress bar, guided selling) | ✓ (pipeline management) | ✓ (Pipeline Summary Pages, amendments) | A (3×) |
| Lead distribution vendor → partner | ✓ (Lead Distribution module; details hidden until opened) | ✓ (Lead Distribution) | ✓ (Deal Inbox; accept/reject) | A (3×) |
| Referral capture partner → vendor | ✓ (Referral module + links) | ✓ (Referral Automation) | ✓ (referral links) | A (3×) |
| MDF / co-op funds lifecycle | ✓ (balances, credit transactions, expiration, reimbursement, ROI→deals) | ✓ (requests, fulfillment, ROI) | ✓ (MDF) | A (3×) |
| Incentives / payouts | ✓ (SPIFF campaigns + claims) | ✓ (Rewards Management) | ✓ (Incentives & Redemption, Payouts) | A (3×) |
| Training & certification (LMS-like) | ✓ (courses/lessons/quizzes; user + org certifications) | ✓ (SCORM, competencies) | ✓ (LMS) | A (3×) |
| Permission-gated content library | ✓ (Library + group permissions) | ✓ (Asset Library) | ✓ (Files/Articles/Resources) | A (3×) |
| Co-branded collateral | ✓ | ✓ | ✓ | A (3×) |
| News / communications to partners | ✓ (News & Email Marketing) | ✓ (News on Demand, Partner Communications) | ✓ (News feeds, groups & DMs) | A (3×) |
| Partner tiers with benefits | (tiered onboarding paths; not a named module) | ✓ (Tiering and Compliance) | ✓ (Program Tiers) | B (2× strong + 1 weak) |
| Joint business planning | ✓ (Business Planning module) | ✓ (Partner Business Planning) | — | B (2×) |
| Partner locator / public marketplace | — (not surfaced) | ✓ (Impartner Marketplace; own Partner Directory) | ✓ (Marketplace / Partner Locator) | B (2×) |
| Agreements / terms management | ✓ (Agreements module, digital signing) | ✓ (Terms Management, click-to-agree) | — | B (2×) |
| Distributor handling | ✓ (Distributor module, assignment) | ✓ (Disti Connect) | — | B (2×) |
| CRM integration (bi-directional) | ✓ (Salesforce/HubSpot/Dynamics) | ✓ (Salesforce/HubSpot/Dynamics) | ✓ (Salesforce/Dynamics/HubSpot, mirroring) | A (3×) |
| SSO (SAML) | ✓ | ✓ | ✓ (SAML/OIDC) | A (3×) |
| Multi-language | ✓ | ✓ | — | B (2×) |
| Forum / community | ✓ (Forum module) | — | ✓ (groups & DMs) | B (2×) |
| CPQ / quotes | — | ✓ (Impartner CPQ) | — | C (1×, optional) |
| Hyperscaler marketplace motions | — | ✓ (HyperscalerGTM) | — | C (1×, optional) |
| Onboarding journey automation | — | ✓ (Journey Builder) | ✓ (Partner Journeys) | B (2×) |
| AI assistance | — | ✓ (Aimi) | ✓ (email deal intake, AI ops) | B (2×, optional) |

## Canonical Abstraction

### L0 — Defining Invariant

A PRM is recognizable only when all of the following hold:

1. **Vendor-side registry of external selling-partner organizations** — each partner is an identified organization record with a governed relationship status managed by the vendor (recruited/prospective → active → inactive), carrying type and program attributes.
2. **Partner-side authenticated users acting for their organization** — the partner organization's own people log in and transact on the system on behalf of their org (two-sided structure: internal vendor console + partner portal).
3. **Shared channel-selling workflow between the two sides** — selling objects (distributed leads, partner-sourced deal registrations, referrals) that pass between partner and vendor with vendor-controlled acceptance (approval gates), creating a co-managed pipeline.

Removal tests:
- Remove (1) → generic portal/community or CRM records; no channel program.
- Remove (2) → internal CRM with partner fields; partners cannot participate.
- Remove (3) → partner enablement portal / training portal / content hub — a different, thinner structure (the same portal machinery pointed at customers exists as a separate product in the sample, showing the portal surface alone does not make PRM).

### L1 — Common Mature Structure

Present in all or nearly all mature products; expected by the market but not definitional:

- Deal registration lifecycle detail: submit → vendor review/approve/deny → protected/exclusive window → stage updates (partner-editable or read-only) → close → payout/commission linkage; expiration and conflict handling.
- Lead distribution (vendor → partner assignment, accept/reject, progress tracking) and referral capture (partner → vendor, incl. referral links).
- Onboarding workflow machinery: public application forms, vetting stages, activation, contact→user promotion, group/role assignment.
- Agreements/terms management (templates, digital acceptance).
- Partner types and segmentation.
- Permission-gated content/resource library; co-branded collateral.
- Training & certification (courses, quizzes, user and organization certifications).
- MDF/co-op funds: allocation to partner accounts (often with expiration), request submission, approval workflow, documentation, reimbursement, ROI linkage to deals.
- Incentives: SPIFF/rewards/payouts with claims.
- Partner tiers with requirements and benefits.
- Joint business planning (shared goals, approval, progress).
- News/announcements and email to partners.
- Partner locator / public marketplace directory.
- Channel reporting & analytics (partner health, pipeline contribution, sourced revenue).
- CRM integration (bi-directional sync of partners, leads, deals); SSO; multi-language; notifications/reminders.

### L2 — Variant / Optional Structure

- Partner-type breadth: resellers/VARs, referral partners, affiliates/influencers, ISVs, MSPs, SIs, distributors — the same machinery, different populations.
- Two-tier distribution: distributor layer between vendor and reseller (assignment logic, deal-reg interplay).
- Commerce depth: CPQ/quotes, price books, product catalogs inside the PRM.
- Ecosystem motions: hyperscaler/cloud-marketplace workflows, account-mapping integrations, co-sell with other vendors.
- Community features: forums, social groups, DMs.
- Portal experience depth: custom hubs per segment/tier, CMS pages, journeys, white-label branding.
- Program governance depth: compliance automation, tiering engines, propensity-to-buy scoring.
- AI assistance: AI deal intake, coaching, content recommendation.
- Packaging/deployment philosophy: standalone SaaS vs CRM-embedded (suite) vs PaaS-extensible; some marketing modules purchasable without the PRM core.

### L3 — Vendor-specific (research notes only)

- Channeltivity: module names (SPIFF, Deal Inbox, "Become a Partner" vs "Request Access" forms), MDF "Credit Transactions", Freshdesk-based KB, Growth/Mid-Market/Enterprise segment framing.
- Impartner: "PRM 3.0"/"Partner Revenue Management" rebrand, Aimi AI, Journey Builder, Orchestration Studio, HyperscalerGTM, Disti Connect, Emerge/Ignite/Pro/Enterprise editions, Forrester TEI figures.
- Magentrix: CRM schema mirroring, Smart Sync 15-minute default (product-specific), 4-way deal submission incl. email-to-portal and CSV bulk, cookieless tracking, PaaS IDE/CLI, "Basic PRMs" competitive list (biased).
- Magentrix's tier example labels ("Authorized, Gold, Platinum") are vendor examples, not industry standards.

## Boundary Findings

1. **PRM vs CRM.** CRM's primary object is the end-customer/prospect relationship worked by the vendor's own sales team; PRM's primary object is the partner organization and the governed channel relationship, with partner-side authenticated participation. Both sampled vendors' own FAQs draw this line (Channeltivity: "CRM software is focused on managing customer interactions… PRM solutions are tailored to… lead distribution, deal registration, and partner performance tracking"; Impartner FAQ equivalent). Structural test: remove partner-side portal access + channel program governance → CRM remains. CRM-embedded PRM (e.g., Salesforce Partner Cloud) is a packaging variant, not a different structure.
2. **PRM vs Channel Sales Management (sibling leaf, §07).** "Channel sales management" names the practice; every researched product self-identifies as PRM and contains channel sales as one functional area (Channeltivity literally organizes its PRM into a "Channel Sales" area). Probable near-alias/superset relationship — flagged for joint review when Channel Sales Management is processed.
3. **PRM vs Affiliate Management Platform (§06).** Affiliate platforms center individual promoters, tracked links, and commission payouts on consumer reach; PRM centers organizations in a governed B2B program with enablement and co-selling. Affiliates/influencers appear inside PRM as one partner type (Impartner names them explicitly). Test: link-tracking + individual payout as the core vs org relationship + enablement + co-selling as the core.
4. **PRM vs Dealer / Distributor Commerce Portal (§05.17).** Dealer/distributor commerce centers the catalog→order transaction; PRM centers the relationship + co-selling workflow. Distributors appear inside PRM as a special partner type with assignment logic (Channeltivity Distributor module), not as order-placing commerce principals. Test: remove the selling-workflow objects → commerce portal remains; remove order/commerce → PRM remains.
5. **PRM vs Supplier Portal (§10).** Direction of the relationship: supplier portal is buy-side (we procure from them); PRM is sell-side (we sell through them). Same "external org portal" shape, opposite commercial direction.
6. **PRM vs Customer Training / Academy Platform (§07).** Partner training is a capability inside PRM (all three samples ship an LMS); the training object is subordinate to the partner relationship. Standalone partner academies exist but lack the registry + selling workflow.
7. **PRM vs "partner portal" as a Type.** The portal is PRM's partner-facing surface, not the Type itself. The same portal machinery pointed at customers exists as a separate product in the sample (Magentrix Customer Management), demonstrating that portal + content alone is a different structure; the channel program + selling workflow is what makes it PRM.

## Historical / Market-Sample Check

- Would older/regional products fit the L0? Early-2000s "partner portals" (Siebel/Oracle-era) and regional distributor-management tools: those with an org registry + partner login + lead/deal sharing fit; pure order-entry dealer systems do not (they are commerce). The L0 is written abstractly (no tiers, no MDF, no LMS required) so older and thinner deployments still fit.
- The definition does not depend on the current "ecosystem/hyperscaler" era vocabulary (Impartner's journey graphic, marketplace motions) — those are L2.

## Uncertainties

- Enterprise suite-embedded PRM (Salesforce Partner Cloud, Oracle Partner Management Cloud) could not be directly researched; its structure is inferred only from positioning references in reachable sources. Assertions about that segment are kept weak.
- Exact protection-period durations, MDF default amounts, tier thresholds, and sync intervals are configurable/product-specific; no universal defaults are stated in the final document.
- Whether the sibling leaf "Channel Sales Management" will be documented as an alias/superset is deferred to its own research pass.
- Regional distributor-management products (manufacturing, telco) were not directly sampled; the L0 is kept abstract to accommodate them, but this remains unverified.

## Final Synthesis

A PRM application is a vendor-operated, two-sided system for running a channel program: a registry of external selling-partner organizations with governed relationship status, authenticated partner users acting for their organizations through a portal, and shared channel-selling workflows (lead distribution, deal registration with vendor approval and protection, referrals) that create a co-managed pipeline. Around this core, mature products add onboarding machinery, enablement (content, training/certification, co-branded collateral), incentives (MDF, rewards), governance (types, tiers, agreements, business plans), communication, a public partner directory, analytics, and CRM synchronization. The Type is bounded against CRM (customer-facing), affiliate management (individual promoters), dealer commerce (order transaction), supplier portals (buy-side), and pure partner portals/communities (no channel program or selling workflow).
