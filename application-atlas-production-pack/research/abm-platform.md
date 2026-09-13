# Research Notes — ABM Platform

Research date: **2026-09-06**

## Research Goal

Understand what an **ABM (Account-Based Marketing) Platform** actually is as an Application Type: its core objects, its primary workflows, its interfaces, its rules, and — critically — how it differs from the neighboring marketing/sales Types (Marketing Automation Platform, DSP / Advertising Campaign Management, Sales Intelligence Platform, CDP, Lead Generation Platform).

## Initial Boundary (hypothesis before research)

- **What it probably is:** a B2B marketing application whose primary object is the **company (account)** rather than the individual lead/contact. Marketing teams define target account lists, run coordinated marketing toward the people at those accounts, and measure engagement and commercial progression at the account level.
- **Who probably uses it:** B2B marketing teams (demand gen / ABM managers / marketing ops), with sales and SDR teams as secondary consumers of account signals.
- **Nearest Types:** Marketing Automation Platform (lead/contact-centric campaign execution), Demand-side Platform / Advertising Campaign Management (audience-targeted ad execution), Sales Intelligence Platform (seller-facing account/contact data), Customer Data Platform (audience identity unification), Lead Generation / Lead Capture Platform (demand capture), Account Management CRM (sales-side account records).
- **Probable boundary:** the unit of targeting and measurement. If the unit is the lead/contact → MAP. If the unit is an anonymous audience/cookie pool → DSP. If the unit is the account → ABM.
- **Unknowns going in:** how account identification (anonymous web visitor → company) actually works; whether advertising execution is defining or optional; how journey/buying-stage models are structured; how deep CRM/MAP integration goes; whether "buying group" is a first-class object or marketing language.

## Research Questions

1. What is the primary audience object (target account list / segment)? How is it built (filters, uploads, CRM sync, models)?
2. How do accounts get identified and enriched (web tag/pixel de-anonymization, intent data, CRM matching)?
3. What signals qualify and prioritize accounts (fit / intent / engagement)? Are scores and stage models customer-configurable?
4. What activation channels exist (own DSP ads, segment sync to external ad platforms, email via MAP/SEP, web personalization, sales alerts)?
5. How does account-level measurement work (engagement, journey stage progression, pipeline influence)?
6. What is the relationship to CRM/MAP (what flows in, what flows out, lead-to-account matching)?
7. What interfaces do marketers vs sellers vs admins get?
8. Where is the exact boundary against MAP, DSP, and Sales Intelligence — what would you remove to turn one into the other?

## Representative Products

Selected for market representativeness, documentation quality, differing product philosophy, and differing customer tier:

| Product | Philosophy | Customer tier | Documentation access |
|---|---|---|---|
| **6sense** | AI/predictive-first ("Revenue AI"): intent data + predictive stages drive everything | Enterprise | Full public KB (support.6sense.com, llms.txt index) — excellent |
| **Demandbase** | ABX suite pioneer; advertising heritage ("only B2B DSP" positioning); buying-group-centric | Enterprise / mid-market | Support KB unreachable (2 failures); official product pages used instead |
| **AdRoll ABM (formerly RollWorks)** | Ad-tech heritage; simplified account-based advertising + insights; self-serve tiers | SMB / mid-market | Full public help center (help.rollworks.com) — excellent |
| **DemandScience (acquired Terminus, 2025)** | Demand-generation conglomerate: advertising + data + measurement studios | Mid-market / enterprise | Help center public shell only; article content gated behind sign-in |

Historical context (background, not fetched evidence): the category consolidated around mid-2010s vendors (Demandbase, 6sense, Terminus, Engagio, RollWorks). Engagio — the "orchestration-first, no-ads" ABM vendor — merged into Demandbase (2020), evidence that orchestration-only and advertising-only are both positions within one Type. MAP vendors (Marketo, HubSpot, Pardot) later shipped ABM modules, evidence that ABM capabilities can exist as features inside a MAP — relevant to the boundary question.

## Sources

### 6sense (Tier 1 — official operational documentation)

- https://support.6sense.com/ (KB home; product-area descriptions) — 2026-09-06
- https://support.6sense.com/llms.txt (full documentation index) — 2026-09-06
- Segments Overview (New): https://support.6sense.com/docs/rev-mktg-ovw-segments-overview-new.md — 2026-09-06
- 6sense Scores Overview: https://support.6sense.com/docs/6sense-scores-overview.md — 2026-09-06
- Predictive Buying Stages: https://support.6sense.com/docs/predictive-buying-stages.md — 2026-09-06
- Account Identification and Enrichment: https://support.6sense.com/docs/account-identification-and-enrichment.md — 2026-09-06
- Compare Audience and Data Workflows and Orchestration: https://support.6sense.com/docs/intelligent-workflows.md — 2026-09-06

### AdRoll ABM / RollWorks (Tier 1 — official operational documentation)

- Help center home: https://help.rollworks.com/ — 2026-09-06
- Account Lists Fundamentals: https://help.rollworks.com/hc/en-us/articles/4415491926157-Account-Lists-Fundamentals — 2026-09-06
- Journey Stages Overview: https://help.rollworks.com/hc/en-us/articles/4415495461261-Journey-Stages-Guide — 2026-09-06
- Advertising category: https://help.rollworks.com/hc/en-us/categories/4413230196109-Advertising — 2026-09-06

### Demandbase (Tier 2 — official product pages only)

- Home: https://www.demandbase.com/ — 2026-09-06
- Marketing (ABM) product page: https://www.demandbase.com/products/account-based-marketing/ — 2026-09-06
- **Limitation:** https://support.demandbase.com/hc/en-us failed twice (transport error, then timeout) on 2026-09-06. Per source-access rules, no operational detail is claimed from Demandbase help docs; Demandbase observations below are limited to positioning, module scope, and marketing-page feature claims, and are marked accordingly.

### DemandScience (Tier 2 — public help-center shell; article content gated)

- Help center home (product-line category descriptions): https://support.demandscience.com/hc/en-us — 2026-09-06
- Central category: https://support.demandscience.com/hc/en-us/categories/41046023276435-Central — 2026-09-06
- **Limitation:** article bodies require platform sign-in; observations limited to public category descriptions.
- Note: support.terminus.com now redirects to the DemandScience help center (Terminus acquired by DemandScience); Terminus is treated as historical context within DemandScience.

## Product Observations

### 6sense — Key observations (evidence layer A unless noted)

**Segments (the account-list object).** A segment is "a list of companies" created in Revenue Marketing, used in activations (ad campaigns, syncing to LinkedIn, etc.). Built three ways: (1) filters over the vendor's Master Company Database (MCD) — firmographic, intent, engagement, CRM/MAP data; (2) external lists — CSV upload (name/domain/country), CRM list sync (Salesforce, Dynamics), CRM report sync; (3) templates (Ideal Customer Profile, Brand Aware, High Engagement, Competitor Intent, High Intent Accounts, Missed Opportunities). Segment statuses: Active (used in ≥1 activation, refreshes nightly), Inactive, Broken (invalid filters). Activations attachable to a segment: 6sense Advertising; segment syncs to Google / LinkedIn / Meta / The Trade Desk; Orchestration; Audience Workflows; Data Workflows; Revenue Marketing alerts; reports; publish. Roles with edit access: Primary Administrator, Administrator, Operation User, Marketing User, Insights User, Sales User; View Only role for read access.

**Account identification.** A JavaScript WebTag on the customer's website identifies anonymous visitors and matches them to companies. Matching to the MCD uses web domain as "the primary identifier," plus country (regional accuracy), company name (validation), and HQ location (consistency). Match rates are affected by VPNs/firewalls; pageview match rate is a tracked metric. (A)

**Scores (prioritization layer).** Predictive scores include: Account profile fit (similarity to ICP via firmographic/technographic + historical opportunities), Contact profile fit, Contact engagement, Account in-market score (buying stage + likelihood of being in-market), Account reach score (outreach quality/quantity/diversity vs patterns of won opportunities), account- and people-level intent scores. Scores export to CRM fields (account/lead/contact records). 6QAs ("6sense Qualified Accounts") = accounts meeting predictive qualification filters. (A)

**Predictive buying stages.** Five stages — Target, Awareness, Consideration, Decision, Purchase — mapped to intent-score bands (0–19 / 20–49 / 50–69 / 70–85 / 86–100). Stages indicate "the likelihood of an account opening or progressing in the next 90 days." Signals: generic and branded searches, links clicked, forms filled, page views. Each stage carries a recommended action pattern (broad awareness messaging → targeted content syndication → banners/social/buyer's-guide content → "air cover" + sales prospecting → phone prospecting/sales touches). (A)

**Advertising.** Ad campaigns run on the vendor's own DSP: banner, dynamic HTML5, native, video, CTV ads; persona targeting (job seniority/function); contextual targeting; brand-safety controls; campaign forecasting; creative validation. Segment syncs push segments to LinkedIn Ads, Google Ads, Meta, The Trade Desk. External media campaigns tracked via pixels; UTM SmartTracking for attribution. (A)

**Orchestration / Intelligent Workflows.** Legacy "Orchestrations" (sunset 2026) did: lead-to-account matching (L2A), lead-to-contact conversion, CRM/MAP enrichment, create accounts/contacts/opportunities, add audiences to MAP lists / CRM campaigns / SEP sequences (Outreach, Salesloft, Gong Engage), push scores/segment names. Successor "Intelligent Workflows" = Audience Workflows + Data Workflows on a visual drag-and-drop canvas: decision logic over 1st/3rd-party intelligence (keywords researched, 6QA status) and CRM/MAP data; multi-step campaigns sequential/parallel/conditional; people-based channels (MAP static lists, CRM campaigns, SEPs, vendor email) and account-based channels (LinkedIn, Google Ads, Meta, vendor display); timer nodes; audience-removal nodes; duplicate-prevention and tie-breaker rules; scheduled (on-demand/daily/weekly) runs; credit consumption for enrichment/contact acquisition/account creation. Supported CRMs: Salesforce, HubSpot, Microsoft Dynamics; MAPs: HubSpot, Marketo, Eloqua, Pardot. (A)

**Sales Intelligence (seller surface).** Dashboards (Accounts, People, Recent Activities, Recommended Actions), Discovery filters (50+), company/people detail pages, contact unlock/export with credits, buying-committee setup, alerts, Chrome extension usable over CRM/LinkedIn, AI writer. (A)

**Reporting.** Buying Stage Movement / Progressions reports, Funnel Insights (account-based pipeline, bottlenecks), Opportunity Trends, Segment Performance, Website Visits, Keywords Activity/Performance, Influenced Form Fills, Value Metrics (accounts/opportunities/campaigns). (A)

**AI Email.** AI agents run conversational email campaigns against audiences, with human review, routing to sales reps, suppression lists, bounce prevention. (A)

### Demandbase — Key observations (evidence layer A for positioning/scope from official product pages; operational detail NOT verified)

**Platform scope.** Demandbase One is organized into Marketing (ABM), Advertising, Sales (sales intelligence), and Data modules. Positioning: "turn signals into prioritized action"; identify in-market accounts, prioritize buying groups, activate coordinated programs, measure what drives pipeline. (A — official product pages)

**Marketing module claims (marketing-page level).** Build dynamic target account lists; prioritize accounts based on intent and activity; orchestrate engagement across channels (advertising, web, sales engagement); personalize web experiences and content based on account behavior, stage, and interests; measure account engagement and progression; connect programs to revenue. (A for *claimed capability*, B for how it actually works)

**Buying groups.** "Buying Groups" has a dedicated product page and is central to positioning — the people layer under accounts is elevated to a first-class concept. (A for positioning)

**Advertising.** Positions itself as a B2B DSP ("Best B2B Ad Tech", "only B2B DSP" claim on comparison page). (A for positioning)

**Journey stages.** Customer case study (SAP Concur) references creating segments "based on journey stage combined with behavioral data" — journey stages exist as a concept; internal mechanics unverified. (B)

**Not verified:** segment/list construction mechanics, identification stack, scoring model, orchestration canvas, CRM sync behavior, reporting structure. Support KB unreachable (2 failures).

### AdRoll ABM (RollWorks) — Key observations (evidence layer A)

**Target account & account list.** "A Target Account is an organization that you have identified as a potential fit… With an ABM strategy, you will focus your Marketing and Sales resources to engage a specific set of accounts, which is called an Account List." Lists built from three signal families: **fit** (ICP Fit Grade A–F scored over the vendor's company database; company attributes; own CRM/MAP data from Salesforce/HubSpot/Marketo), **intent** (Bombora Company Surge, vendor keyword intent, G2 Buyer Intent, account news), **engagement** (ad impressions/clicks; website page views/unique visitors/conversions). List types: **Dynamic** (sources re-synced every 6 hours), **Static** (pulled once), **API** (custom integration). Limits: 1,000 lists per customer; 250,000 accounts per list; 10,000 accounts per Account Group; max 10,000 accounts targetable per list via campaigns/playbooks. (A)

**Account Groups (tiering).** Accounts on a list dynamically route into groups defined by filters — e.g., Tier 1/2/3 by ICP fit and revenue potential; groups also used to segment by Journey Stage, CRM deal stage, intent, engagement. Same account can live in multiple lists/groups. (A)

**Journey Stages.** Default five stages: Unaware, Aware, Engaged, Open Opportunity, Won Opportunity — definitions customer-customizable from data sources (website activity, advertising activity, intent, CRM data). Dashboard tracks progression/regression between two point-in-time snapshots (Progressed / Regressed / Unchanged). Accounts must be on an Account List to appear. Journey Stage can segment Account Groups for advertising (Web, CTV, LinkedIn, Meta); stage data exports to CRM and displays in a CRM Sales Insights widget; stage filters usable in Command Center and as triggers in Workflows (actions in Salesforce/HubSpot/Marketo). "Journey Predictions" forecasts opportunities for prioritization. Package gating: included in paid ABM packages; not in Free Tier; legacy Starter limited to 5 stages. (A)

**Advertising.** Ad Library (web display, CTV video, LinkedIn, Facebook/Instagram); Playbooks (packaged campaign types with settings); Campaigns across Web, LinkedIn, CTV, Facebook/Instagram, DOOH, ChatGPT; BidIQ bid optimization; supply partnerships; Advertising Engagement and Revenue Impact reports. (A)

**Insights & sales surface.** Intent and Engagement identification of in-market accounts; Sales Insights with an "Account Spike" data-science model; Command Center as the account-discovery surface (find in-market accounts not yet in CRM or not targeted; create lists from it). Pixel for website visitor identification; ICP Models; general exclusions; user permissions. (A)

**Integrations.** Salesforce, HubSpot, Marketo, G2, LinkedIn; Orchestration Workflows launched from the platform. (A)

**Commercial tiers.** Free Tier self-serve onboarding exists; paid packages: Account Based Advertising / Account Based Marketing / ABM + Advertising (plus legacy tiers). (A)

### DemandScience — Key observations (evidence layer B; public category descriptions only)

Product lines visible on the public help center: **Advertising** ("coordinated, targeted, & personalized campaigns that reach the right people, at the right accounts"), **Audience Builder** (FKA Klarity; ICP identification, account insights for outreach prioritization), **Central** ("The Intelligence Hub"), **Data Studio** ("integrate, identify, & activate target accounts based on all your 1st and 3rd party data"), **Measurement Studio** ("robust attribution suite" for revenue measurement), **Signature Ads** (turns employee Gmail/Outlook signatures into an ad channel), **Verify** (contact data verification), **Web** ("make any page on your website a personalized… landing page"), Chat Experiences (end-of-life). Article bodies are sign-in gated; no operational mechanics verified. (B)

## Cross-product Comparison

| Dimension | 6sense | Demandbase | AdRoll ABM (RollWorks) | DemandScience |
|---|---|---|---|---|
| Primary audience object | Segment (dynamic company list over vendor MCD; or external lists) | Target account list (dynamic; marketing-page claim) | Account List (dynamic/static/API) | Target accounts via Data Studio / Audience Builder (B) |
| Account identification | WebTag de-anonymization → MCD match (domain primary key) | Claimed; mechanics unverified | Pixel de-anonymization | Claimed (B) |
| Fit/ICP model | Account profile fit score (predictive) | Claimed | ICP Fit Grade A–F | Audience Builder ICP (B) |
| Intent data | Own intent + keywords (branded/generic) | Claimed | Bombora + own keyword intent + G2 + news | Claimed (B) |
| Stage/journey model | Predictive buying stages (5, score-banded, vendor-defined) | Journey stages referenced (B) | Journey Stages (5 default, fully customer-customizable) | Not verified |
| Prioritization output | Scores + 6QA + stages → CRM fields | Prioritized accounts/buying groups (claim) | Fit grade + groups/tiers + stage | Account insights (B) |
| Advertising execution | Own DSP + segment syncs (LinkedIn/Google/Meta/Trade Desk) + external-media pixels | Own B2B DSP (positioning) | Own ad stack (web/CTV/LinkedIn/FB-IG/DOOH/ChatGPT) + playbooks | Advertising product line (B) |
| Email/orchestration to people | Audience Workflows → MAP lists/CRM campaigns/SEPs/own AI email | Claimed orchestration | Workflows triggers into Salesforce/HubSpot/Marketo | Signature Ads; MAP integration unverified (B) |
| Web personalization | Dynamic HTML5 ads (web personalization not verified in fetched docs) | Claimed (web experiences) | Not observed | Web product line (B) |
| Sales-facing surface | Sales Intelligence app + alerts + Chrome extension | Sales module (claim) | Sales Insights + CRM widget + Command Center | Central (B) |
| Account-level measurement | Stage movement, funnel insights, opportunity trends, value metrics | Claimed (engagement → pipeline) | Journey Stages dashboard, Revenue Impact report | Measurement Studio (B) |
| CRM/MAP sync | Salesforce/HubSpot/Dynamics; Marketo/Eloqua/Pardot; L2A; score/segment export | Claimed integrations | Salesforce/HubSpot/Marketo; stage export; workflows | Data Studio (B) |
| Customer tier | Enterprise | Enterprise / mid-market | SMB → enterprise (free tier up) | Mid-market / enterprise |

**Stable commonalities (present in all sampled products, A or B evidence):**

1. The **account (company)** is the primary audience and measurement unit; a named **target account list/segment** object exists.
2. Accounts are qualified/prioritized from **fit + intent + engagement** signal families.
3. **Coordinated activation** toward accounts across multiple channels, always including account-targeted advertising; people-level channels (email/SEP) reached via CRM/MAP/SEP integration.
4. **Account-level engagement measurement** and progression toward commercial outcomes (opportunity/pipeline), with reports tying programs to accounts.
5. **CRM (and MAP) integration** as the data spine: scores/stages/audiences flow out; opportunity/deal state flows in; lead-to-account matching connects people records to accounts.
6. A **sales-facing surface** (alerts, dashboards, CRM widgets) so sellers act on account signals.
7. A **people layer under accounts** (buying committee / contacts at the account).

**Structural differences (implementation, not Type):** who defines the stage model (vendor-fixed predictive vs customer-customizable); whether advertising runs on an owned DSP or is synced out; whether orchestration is a canvas, a trigger system, or a module set; whether contact data acquisition is bundled; free/self-serve vs sales-led entry.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

An ABM Platform is recognizable by exactly this structure:

```text
Target Account (company as identified record)
└── Target Account List / Segment (account-level audience object)
    └── Coordinated activation toward the account across ≥1 channel
        └── Account-level engagement & progression measurement
            (feeding back into prioritization)
```

Three properties. Remove any one and the Type collapses into a neighbor:

- **Account as the audience unit** — targeting is defined and purchased/measured at the company level, not the lead/contact level. Remove → lead-centric Marketing Automation.
- **Activation toward accounts** — the platform executes or orchestrates marketing toward the account (its people/properties) across channels. Remove → account analytics / account intelligence only.
- **Account-level engagement & progression measurement** — engagement and commercial progression are tracked and reported per account, closing the prioritization loop. Remove → generic campaign/ad execution with company targeting.

### L1 — Common Mature Structure (very common, not defining)

- Account identification: website tag/pixel de-anonymization of anonymous visitors into companies (probabilistic, match-rate-bound)
- Intent data: third-party (surge/Bombora-style, G2-style) and/or first-party keyword intent
- Fit/ICP scoring: predictive or rules-based account (and contact) fit grades
- Buying/journey stage model over accounts (vendor-defined predictive or customer-customizable), with progression tracking
- Account-targeted advertising execution: owned DSP or segment sync to external ad platforms (LinkedIn, Google, Meta, CTV…)
- Orchestration/workflows: multi-step, multi-channel campaign logic; triggers into CRM/MAP/SEP
- CRM/MAP integration spine: lead-to-account matching, score/stage/segment export, opportunity state import
- Sales-facing intelligence: alerts, account dashboards, CRM widgets/extensions
- People layer: buying-committee/contact records under accounts, sometimes with contact acquisition/unlock
- Account-level reporting: engagement, funnel/pipeline influence, program performance

### L2 — Variant / Optional Structure

- Web personalization (account-aware website experiences) — present in some products (Demandbase claim, DemandScience Web), not verified in all sampled docs
- Owned DSP vs sync-only advertising posture
- AI email agents / conversational email
- Contact data acquisition (purchase/unlock credits) as bundled data commerce
- Free/self-serve tier vs enterprise sales-led onboarding
- Package/module decomposition (advertising-only, ABM-only, suite)
- CTV / DOOH / emerging channels as ad surfaces
- Customer-data unification modules (data studio) and attribution studios as separate products

### L3 — Vendor-specific (research notes only)

- 6sense: 6QA, Master Company Database, buying-stage intent-score bands (0–19/20–49/50–69/70–85/86-100), Temperature model, RevvyAI, UTM SmartTracking, credit system, nightly segment refresh for active segments, Orchestration sunset (2026) → Intelligent Workflows migration with 12-week windows
- AdRoll ABM: ICP Fit Grade A–F, Account Spike model, Command Center, BidIQ, 6-hour dynamic list sync, 1,000-list / 250k-account / 10k-group limits, Free Tier
- Demandbase: Demandbase One branding, "only B2B DSP" positioning, Buying Groups as named product, ABM Certification/Academy
- DemandScience: Central, Audience Builder (Klarity), Data Studio, Measurement Studio, Signature Ads, Verify; Terminus acquisition/redirect

## Rejected Findings (considered, not promoted)

- **"ABM = intent data + predictive AI"** — rejected as defining. Intent/predictive are L1 implementations of the prioritization loop; RollWorks' free tier and pre-AI-era ABM (CRM lists + ads + engagement reports) satisfy the L0 without them. Historical check: pre-2015 named-account marketing done manually in CRM still fits L0.
- **"ABM = account-based advertising"** — rejected. Advertising is the most common activation channel but Engagio-style orchestration-only ABM (email/SEP/sales plays, no ads) was a recognized position; activation channel mix is L2.
- **"Buying group is a defining object"** — rejected for L0. The people layer under accounts is L1 (all sampled products have it), but only Demandbase elevates "Buying Groups" to a named product concept; the L0 works with "people at the account."
- **"Journey stages must be predictive/vendor-defined"** — rejected. 6sense stages are vendor-computed; RollWorks stages are customer-defined rules. The invariant is "an account-level stage/progression model exists," not who computes it.
- **"ABM platforms don't do lead capture"** — not asserted either way; out of scope for this pass.

## Boundary Findings

| Neighboring Type | Relationship | Distinction | Remove-what test |
|---|---|---|---|
| Marketing Automation Platform | closest overlap | MAP's primary object is the lead/contact and campaign/nurture execution over people; ABM's primary object is the account. ABM platforms *push audiences into* MAPs (6sense AWF adds people to MAP static lists; RollWorks workflows trigger Marketo/HubSpot) rather than replacing them | Remove the account-level unit (target/measurement by company) → MAP |
| Demand-side Platform / Advertising Campaign Management | execution overlap | DSP targets anonymous audiences/segments without company-level identity or account-level engagement reporting; ABM advertising is account-identified targeting with per-account measurement | Remove account identity + account-level measurement → DSP |
| Sales Intelligence Platform | bundled sibling | SI serves sellers (discovery, contact data, outreach context); ABM serves marketing orchestration and measurement. 6sense and Demandbase bundle both; the marketing-orchestration side is the ABM Type | Remove activation + account-level marketing measurement → SI |
| Customer Data Platform | data-layer neighbor | CDP unifies customer/identity data into audiences for activation anywhere; ABM is the B2B company-graph application with built-in account semantics (stages, fit, committee) | Remove B2B account semantics & account measurement → CDP |
| Lead Generation / Lead Capture Platform | funnel-adjacent | Lead gen captures demand (forms, content, contacts); ABM orchestrates toward a chosen account set regardless of inbound capture | Remove target-account selection & orchestration → lead gen |
| Account Management CRM (sales-side) | record-system neighbor | CRM accounts are the sales system of record; the ABM platform consumes CRM accounts/opportunities and adds marketing signal + activation. One-way-ish: ABM enriches CRM, CRM anchors pipeline truth | Remove marketing activation/measurement loop → account records in CRM |
| Marketing Attribution Platform | measurement overlap | Attribution tools measure touchpoint→revenue generically; ABM measurement is account-progression-centric and feeds prioritization, not just reporting | (Attribution leaf not yet processed; note for joint review) |

**Category-level observations for STATUS.md:**

1. MAP vendors bundle ABM modules and ABM platforms bundle execution channels — the boundary is the *primary object* (account vs lead/contact), not feature presence. Gradient, not wall.
2. Category consolidation is active: Engagio→Demandbase (2020), Terminus→DemandScience (2025), RollWorks→AdRoll ABM rebrand. Vendors reposition from "ABM" to "ABX"/"revenue/GTM platform" — naming drift, not structural divergence.
3. Demandbase's own comparison pages (vs 6sense, vs Terminus, vs ZoomInfo) confirm the competitive set spans both ABM platforms and sales-intelligence platforms — the ABM/SI boundary is the blurriest one.

## Uncertainties

1. **Demandbase operational mechanics unverified** (support KB unreachable after 2 attempts). Its L1/L2 presence is inferred from official product-page claims (A for claims, B for mechanics). If Demandbase docs become reachable, verify: segment construction, identification stack, journey-stage customization, orchestration canvas.
2. **DemandScience internals gated** behind sign-in; only public category descriptions observed (B-level).
3. **6sense web personalization** not confirmed in fetched docs (only dynamic HTML5 ads); web personalization is kept at L2 on the strength of Demandbase/DemandScience evidence only.
4. **Exact numeric limits** (6sense segment caps, RollWorks limits) are vendor-specific and time-stamped; deliberately excluded from the final document.
5. **Market-size/positioning claims** (e.g., "only B2B DSP") are vendor marketing, recorded as positioning only.
6. Whether "ABX" (account-based everything) constitutes a distinct Type: current evidence says no — it is Demandbase's repositioning of the same structure. Flagged, not decided.

## Final Synthesis

The ABM Platform is defined by a small invariant: **the company (account) is the audience unit**. Everything else in the category is elaboration:

1. **Select** — build target account lists/segments from fit, intent, engagement signals and CRM data (dynamic filter-based or static imported).
2. **Identify & track** — de-anonymize web visitors into accounts, ingest intent, aggregate engagement at account level.
3. **Prioritize** — score accounts (fit/in-market/engagement) and place them in stage/journey models; tier into groups.
4. **Activate** — run coordinated programs toward accounts: account-targeted advertising (owned or synced), people-level email/SEP via CRM/MAP orchestration, web experiences, and sales alerts.
5. **Measure & sync** — account-level engagement and stage progression reports, pipeline influence, with continuous sync into CRM/MAP so marketing and sales act on the same accounts.

The Type sits between MAP (lead-centric execution), DSP (anonymous-audience advertising), and Sales Intelligence (seller-facing data). It is distinguishable from each by its invariant: account-level targeting *and* account-level measurement *and* multi-channel activation, held together by the target account list.
