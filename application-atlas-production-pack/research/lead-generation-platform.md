# Research Notes — Lead Generation Platform

## Research Goal

Understand what a Lead Generation Platform (§06 Marketing, Advertising & Growth) actually is as an application type: its defining core, the objects and workflows inside it, and its boundaries against the neighboring types that share its vocabulary — Lead Capture Platform (processed sibling and designated boundary counterparty), Lead Management Platform (§07, unprocessed), the §07 sales-data family (Contact Discovery / Sales Prospecting / Sales Intelligence, all processed), Landing Page Builder / CRO, and advertising-management types.

Special obligation this pass: STATUS.md records the lead-capture-platform pass's terminology-drift flag naming this document as its boundary counterparty ("capture = the intake mechanism…; generation = the supply side…; the lead-generation pass should treat this document as its boundary counterparty and ratify or refine"). This pass must ratify or refine that split with direct product evidence.

## Initial Boundary (hypothesis before research)

- The market label "lead generation platform" is polysemous. Products marketed under it include: capture widgets ("lead generation software for websites"), landing-page/funnel builders, B2B contact databases, ad-platform native lead forms, pay-per-lead marketplaces, and lead-gen agencies (services, not software).
- Hypothesis to test: the only coherent software structure not already owned by a processed sibling is the one where the **platform itself operates the surface where the prospect expresses interest** (ad-platform native forms; platform-owned demand destinations selling resulting leads), with delivery of lead records into the business.
- Unknowns: is ad-platform lead gen (lead ads/lead gen forms) the same Type as pay-per-lead marketplaces? Is "the business's own website is not the venue" the load-bearing discriminator vs capture? Are lead marketplaces a software platform or a service?

## Research Questions

1. Where does the prospect encounter the business — on the business's own touchpoint or on a surface the platform operates?
2. What does the platform deliver to the business, and how (download, sync, email, portal, call transfer)?
3. What does the business control (volume, targeting, forms, delivery), and what are the per-lead economics?
4. What separates "generating" leads from "capturing" them (Lead Capture Platform) and from "sourcing" them from a database (§07 family)?
5. Why do page builders and capture tools self-label "lead generation" — is the label stable?
6. Historical check: do pre-web lead brokers (phone rooms, faxed lead sheets, mail-in request cards) still fit the definition?

## Representative Products

| Product | Pole | Customer tier | Evidence quality |
|---|---|---|---|
| LinkedIn Lead Gen Forms (Marketing Solutions / Campaign Manager) | ad-platform-native lead generation: lead-gen objective, native pre-filled forms, download/CRM sync | B2B advertisers, SMB → enterprise | strong — Tier-1 help center (27-article Lead Gen Forms topic + leads/analytics article) |
| insuranceQuotes / NetQuote (All Web Leads family) | pay-per-lead marketplace: platform-owned consumer destination (NetQuote), agent-side lead-buying portal | insurance agents/carriers, SMB → carrier | strong — Tier-1/2: consumer site, agent portal pages, full FAQ (billing, returns, delivery, schedules, bids, reporting) |
| Leadpages | boundary sample — self-labeled "lead generation" historically; 2026 positioning is "AI Landing Page Builder" | SMB marketers | strong — full product homepage fetch |
| Apollo.io | boundary sample — "find leads" software that self-labels "AI Sales Platform" (database + outreach), not lead generation | B2B sales teams | moderate — homepage fetch (positioning + pillar structure + FAQ) |

Not fetched (unreachable after network rules): Meta Business Help Center (transport error ×2 — lead ads could not be verified directly), Google Ads Help (timeout ×2), TikTok Ads Help (timeout ×2), Thumbtack help (JS-rendered, empty), Typeform. Consequence: cross-ad-platform commonality of the lead-form machinery is asserted only at canonical-inference strength; only LinkedIn's machinery is directly verified.

## Sources

Research date: 2026-09-07. Fetch results as noted above.

- LinkedIn Marketing Solutions Help root — https://www.linkedin.com/help/lms
- LinkedIn — View and download leads, metrics, and analytics for Lead Gen Form ad sets (a425750) — https://www.linkedin.com/help/lms/answer/a425750
- LinkedIn — Lead Gen Forms topic (a136072, 27-article index) — https://www.linkedin.com/help/lms/topic/a136072 (article titles/snippets observed: overview a423447, create a427102, fields a425337, hidden fields a421421, specifications a423364, CRM/MA integration a425316, test lead a420737, permissions a421620, privacy policy a420012, data collection & retention a7478965, appointment booking a7462413, product-page lead gen form a590241, status definitions a427322)
- NetQuote — consumer homepage (quote-request flow, "up to five quotes") — https://www.netquote.com/
- insuranceQuotes for Agents — agent portal homepage (positioning, leads + calls) — https://agents.insurancequotes.com/
- insuranceQuotes for Agents — How It Works (overview infographic page) — https://agents.insurancequotes.com/how-it-works/
- insuranceQuotes for Agents — Lead Types (insurance lines, targeting/filters) — https://agents.insurancequotes.com/insurance-leads/
- insuranceQuotes for Agents — FAQ (lead origin, shared vs exclusive, billing, returns/credits, pausing, delivery, schedules, Max Bid, calls, reporting, cancellation) — https://agents.insurancequotes.com/faq/
- Leadpages — homepage (2026 positioning as AI landing page builder; lead-generation as a use-case nav item) — https://www.leadpages.com/
- Apollo.io — homepage (self-label "AI sales platform"; Outbound/Inbound/Data Enrichment/Deal Execution pillars) — https://www.apollo.io/

---

## Product Observations

### LinkedIn — Lead Gen Forms (ad-platform pole)

Evidence layer: A (direct observation of official help-center articles).

- **Positioning**: "Lead Gen Forms simplify the process of capturing high-quality leads by automatically populating contact and profile information when a member clicks the call-to-action button on your ad. There is no additional cost for LinkedIn Lead Gen Forms outside of the costs for the associated ad sets." [A]
- **Lead generation is an ad-set objective**: "Choosing Lead generation as your ad set objective allows you to attach an existing custom Lead Gen Form to your ad creative or create a new one. When a member clicks on your ad's call-to-action (CTA), a native digital form will open." [A]
- **The form is a reusable asset**, not the ad: forms are built from the Assets page ("Content & Assets → Lead generation forms") for reuse across ad sets, or created during ad-set setup. Asset lifecycle documented: create, duplicate, edit (edited forms on active ad sets are resubmitted for ad review), archive, unarchive, status definitions (whether an ad is attached and whether ad review approved it). An "Associations" column shows how many ads are associated with each form. [A]
- **Identity is platform-supplied**: forms "automatically populate contact and profile information" from the member's profile when the CTA is clicked — the prospect does not re-type identity fields the platform already holds. [A]
- **Form machinery**: up to 12 informational fields (sections such as "Lead details"); custom field names on download/sync to align with CRM/MA fields; hidden fields to carry campaign/source/agency metadata into the leads report; personalization macros for headline/details/confirmation; live preview. [A for existence; numeric limit recorded here, kept out of the canonical document]
- **Delivery out of the platform**: download leads as CSV by form (with date range) or by ad set (Export → Report Type: Leads); or sync automatically to marketing-automation/CRM partners via the Marketing Partner Directory ("manage leads, start workflows, and build relationships without manual uploads"); test leads can be sent to verify integration end-to-end. [A]
- **Business-side metrics**: completion rate, cost per lead, "Conversion & Leads" columns on ad sets; filter by status/type/objective. [A]
- **Permissions**: two-plane access — ad-account permission (Viewer+) AND Company Page role ("Lead Gen Forms manager"+). [A]
- **Privacy/consent machinery**: a privacy policy URL is required when creating a form; the advertiser must describe how leads will be used and manually enable per-use consent toggles; "Collected member profile data can only be stored for one year because of our member privacy policy" (analytics persist beyond that); a dedicated data-collection-and-retention article documents encryption, data isolation, and storage in LinkedIn data centers. [A; the numeric retention window is recorded here and kept qualitative in the canonical document]
- **Extensions of the same machinery**: appointment booking can be attached to a Lead Gen Form (scheduling tool integration after completion); lead gen forms can be attached to Document ads; a lead gen form can be created for the company's Product Page ("collect quality leads from members who visit your Product Page… pre-filled form"). [A]
- Take: the encounter (ad → CTA → native form) happens entirely inside the ad platform; identity comes from the platform's own member profile; the platform packages and delivers the lead; the advertiser's systems receive it. The lead-supply machinery lives inside the ads product but is documented as its own feature family with its own permissions, asset lifecycle, and metrics.

### insuranceQuotes / NetQuote (All Web Leads) — pay-per-lead marketplace pole

Evidence layer: A (official pages and FAQ of the vendor's own properties).

- **Two-sided structure**: consumer side (NetQuote — "Compare Insurance Quotes. Fast and Easy."; consumer fills one form, "start to receive quotes based on your info… as many as five insurance quotes from major providers within your area") and agent/buyer side (insuranceQuotes for Agents portal). The marketplace is the same company's product: footer/FAQ identify the family ("NetQuote, InsureMe, AgentInsider or InsuranceAgents"). [A]
- **Where leads come from (vendor's own account)**: "We make ourselves as visible as possible both in the media and online to enable consumers to find our websites and ultimately find you. Interested individuals then complete online forms and submit them for competitive quotes. Our proprietary validation system then screens the submissions for validity and only passes on true comparison shoppers right into your inbox." [A] — the platform operates and promotes the demand destination; submissions are screened before supply.
- **The lead and call as delivered products**: "We source high-intent customers as both leads and live calls delivered to your agency." Call product ("Qualified Concierge Calls / live transfers"): the platform's call center vets consumers who filled a form, "they then only send you consumers who have confirmed they are looking for quotes, want to speak with an agent, and have time to speak"; if the consumer declines at any point the call is not transferred. [A]
- **Multi-sell distribution policy**: "Each lead is sold to only 3–4 agents on average… We will of course never sell the same lead to the same carrier within the same area." Zip-code exclusivity "no longer supported" on the current platform. [A; numeric multi-sell figure recorded here, qualitative in canonical doc]
- **Delivery machinery**: "you will begin to see leads and calls flow into your email or lead management system"; multiple lead-delivery email addresses; text-message alerts for new leads; direct integration "with many different 3rd party lead management systems"; secure web gateway ("primary access to your account… leads, account scheduling and all other changes"). [A]
- **Business-side controls — the lead profile**: profiles combine product line (auto/home/health/medicare/life/small business), "lead areas" (geography, add/remove), carrier/criteria filters ("target customers based on your business needs and underwriting requirements"; "leading carrier specific filtering options"), daily and weekly delivery limits, day-of-week delivery schedules (and time-of-day for calls), per-profile and account-level pause. [A]
- **Volume machinery — Max Bid**: "set the highest total price you are willing to pay for a lead or call in this profile. If there is another agent in your area competing for the same lead or call, we will increase your price enough to beat their price, up to your Max Bid. You will only pay what you need to pay… to win the lead." Plus Profile/Account "Opportunity Reports" showing where additional volume exists. [A]
- **Per-lead economics**: "You are billed for all leads and calls sent to your account"; credit and prepay payment types with automatic recharge; bi-weekly invoicing; billing history shows "the individual cost per lead, as well as credits received back". Monthly Service Plan adds unlimited pausing, weekend lead discounts, delivery scheduling, per-profile pause. [A]
- **Return-for-credit (lead quality remedy)**: "we encourage you to take advantage of our fair and easy return policy that gives agents credit for invalid leads"; return via the lead's ID page with a reason; separate return policies for leads vs calls; lead statuses include New, Open, Return – Credited. [A]
- **Reporting**: Lead Data Report (CSV export of received lead data), Daily Summary (calls and cost by day), Notes Summary (recording of the lead's vetting call), Transfer Details (per-call cost breakdown), Volume Opportunity Reports. [A]
- **Buyer-side urgency framing (vendor guidance, not operational fact)**: FAQ advises calling leads immediately and persistent multi-attempt follow-up; "many of our leads close months after initial submission". [A for the advice existing; the percentages in the FAQ are vendor research claims and are not adopted here]
- Take: a marketplace where the platform owns and feeds the consumer destination, packages screened submissions into lead (and call) products, distributes them under a multi-sell policy to buyers who configure profiles/limits/bids, bills per delivery, and remedies quality through credits. The buyer's gateway is an operational console around the lead flow, not a CRM.

### Leadpages (boundary sample — terminology drift)

Evidence layer: A (homepage).

- 2026 positioning: "AI Landing Page Builder & CRO… describe your campaign and our AI landing page builder turns it into a live, branded landing page… A/B testing, Smart Traffic… heatmaps." Product nav: AI Page Builder, A/B Testing, Smart Traffic, Heatmaps, Analytics, Personalization, DTR, Visitor Intelligence, Form Collection, Ecommerce, Sites, Custom Domains, Ad Studio, Optimization Score, MCP Server. [A]
- The encounter surface is the **business's own campaign page** (hosted under the business's custom domain); traffic is attracted by the business's own ads/email. "Lead Capture + Integrations: Forms, webhooks, CSV export. Leads go straight to HubSpot, Salesforce, Mailchimp…" [A]
- The word "lead" is everywhere (9.1M+ leads/mo marketing claim; "Lead Generation" as a Solutions use-case nav item; "Lead Capture"), but the *structure* is page-builder + capture: the venue belongs to the business. Notably the vendor has moved its primary self-label from "lead generation platform" (historical marketing) to "landing page builder". [A]
- Also notable: "Visitor Intelligence — see who's visiting your pages. Company name, industry, job title… Powered by Customers.ai IP resolution… before they fill a form" — an identification capability (different mechanism, cf. the capture pass's Leadfeeder finding) now bundled into a page-builder product. Confirms that "lead" vocabulary freely crosses mechanism boundaries in market positioning. [A]
- Take: boundary evidence for the drift pole. A "lead generation" label on a page-builder product describes the outcome, not the structure. The leaf's definition must not absorb page builders.

### Apollo.io (boundary sample — database sourcing)

Evidence layer: A (homepage).

- Self-label: "The AI sales platform for smarter, faster revenue growth… Everything you need, from finding leads to winning deals." Pillars: Outbound (AI-powered multichannel campaigns, deliverability guardrails, task lists), Inbound (anonymous visitor identification, real-time form enrichment, instant routing, nurture sequences), Data Enrichment (contacts/companies counts, verified emails/phones — marketing figures), Deal Execution. Footer "Use Cases": B2B Database, Lead Scoring, Inbound Lead Router, Sales Engagement, Meetings Scheduler, Deal Management, Dialer, Website Visitor Identification… [A]
- Take: "finding leads" software self-organizes under sales-platform labels. The database pole involves **no prospect-side expression of interest at a platform demand surface** — records are sourced from a maintained supply. This matches the processed §07 family (Contact Discovery / Sales Prospecting / Sales Intelligence), not this leaf. Boundary confirmed by self-labeling, not assumed.

---

## Cross-product Comparison

| Dimension | LinkedIn Lead Gen Forms (ad-platform pole) | insuranceQuotes/NetQuote (marketplace pole) | Leadpages (drift sample) | Apollo (drift sample) |
|---|---|---|---|---|
| Who operates the encounter surface | the ad platform (native form opens in-platform from an ad CTA) | the platform's own consumer destination (NetQuote), promoted via content/SEO/media | the business's own campaign page | none — no demand surface; database sourcing |
| Prospect-side intent event | yes — member clicks CTA and submits pre-filled form | yes — consumer completes quote application; screened | yes — form fill on the business's page | no |
| Identity source | platform member profile (auto-populated) | volunteered form fields + platform-side validation screening | business's form fields (+ IP-resolved visitor data) | maintained contact database |
| What is delivered to the business | lead records: CSV download / CRM-MA sync / test leads | lead records and vetted live calls: email, gateway, LMS integration, text alerts | lead records to connected CRM/email/webhook | records/enrichment into CRM and sequences |
| Business-side controls | form assets (fields, hidden fields, privacy URL, consent toggles); ad-set targeting/budget | lead profiles: product line, areas, filters, daily/weekly limits, schedules, pause, Max Bid | page design, forms, display rules | search filters, lists, sequences |
| Economics | no incremental cost beyond ad spend; CPL metric | billed per lead/call delivered; credits for invalid; prepay/credit billing; auction (Max Bid) | subscription for the tool | subscription + data credits |
| Distribution policy | each lead to its own advertiser | shared multi-sell with same-carrier/same-area exclusion; exclusivity no longer offered | n/a | n/a |
| Not system of record | metrics persist; member profile data retained for a bounded period; leads sync out | leads flow into the buyer's inbox/LMS; gateway is access + control, not CRM | leads exported/synced out | CRM is system of record |
| Structure vs this Type | **in Type** (ad-platform realization) | **in Type** (marketplace realization) | out — page builder/capture on business-owned surface | out — §07 sales-data family |

Findings across the researched sample (evidence layer B where noted):

- The encounter surface is operated by the platform, not the business (B: both in-Type poles).
- A prospect-side expression of interest is present in both in-Type poles — absent in the database pole (B).
- The platform packages each expression of interest into a lead record and delivers it into the business's follow-up hands; the platform is never the system of record for the resulting relationship (B).
- Business-side control over volume and quality is an operational console in both poles — form/asset + ad-set machinery on one side; profiles/limits/schedules/bids on the other (B).
- Per-delivery economics and quality remedies attach to individual leads — CPL metrics on one side; per-lead billing + return-for-credit on the other (B).
- Delivery spans multiple channels in both poles (download, sync, email, portal; calls as a premium format) (B).
- Consent/privacy machinery is first-class: platform-required privacy policy URL and per-use consent toggles; consumer-side unsubscribe; bounded retention of collected profile data (B).

## Canonical Model

### L0 — Defining Invariant

Three properties. Remove any one and the product stops being a Lead Generation Platform:

1. **Platform-operated demand surface.** The prospect encounters the business at a surface the platform itself operates and populates with its own audience — a native lead form inside an advertising platform reached through its paid distribution, or a request/quote flow on a consumer destination the platform runs and promotes. The business's own website is not the venue. Remove → the product arms or instruments the business's own touchpoints: Lead Capture Platform (intake at owned touchpoints) or Landing Page Builder (page authoring).
2. **The lead as a supplied record.** Each expression of interest is screened/packaged into a lead record — contact identity plus request/intent context — that the platform delivers to the business as the unit of value it sells/supplies. Remove → the product is an audience/advertising product or a content destination, not lead supply.
3. **Delivery into the business's follow-up hands.** Leads arrive where follow-up happens — download/export, direct CRM/marketing-automation sync, delivery email/portal, or live call transfer — and the platform's involvement ends at delivery; it is a lead supplier, not the system of record for the customer relationship. Remove → dead-end audience product, or (if it keeps the lifecycle) Lead Management.

### L1 — Common Mature Structure

- Native request/form machinery on the platform side (field selection, custom/hidden fields for attribution, privacy policy and per-use consent, preview, test leads)
- Identity assistance (auto-population from the platform's own profile data; platform-side validation/screening of submissions before supply)
- Multi-channel delivery (CSV export by date range/asset, CRM/MA partner sync, delivery email addresses, notifications/alerts)
- Business-side control console (asset library with lifecycle/status; profiles with geography, filters, limits, schedules, pause)
- Per-lead economics and quality remedies (cost-per-lead metrics; per-delivery billing; return-for-credit policies; billing statements)
- Performance and volume reporting (completion rate, cost per lead, volume-opportunity visibility)
- Distribution policy (exclusive vs shared multi-sell with category/area exclusion)

### L2 — Variant / Optional Structure

- Demand-side ownership: advertiser-configured campaigns (ad-platform pole) vs platform-owned consumer destination selling to many buyers (marketplace pole)
- Lead format: form records vs vetted live call transfers vs forms with attached appointment booking
- Multi-sell depth and exclusivity (shared leads across several buyers; historical zip exclusivity, dropped by the sampled vendor)
- Auction-style volume purchasing (dynamic bidding up to a cap)
- Vertical tuning of the request flow (insurance quote applications in the sampled marketplace; by extension other lead-buying verticals, not verified this pass)
- Additional platform surfaces (lead forms on product/company pages; document-attached forms)

### L3 — Vendor-specific (research notes only)

- LinkedIn: 12-field limit; 1-year member-profile-data retention; "Lead Gen Forms manager" Company Page role; ad-review resubmission on edit; appointment-booking tool integration; Product Page forms; no incremental cost beyond ad sets.
- All Web Leads family: "Max Bid" name and mechanics; "Qualified Concierge Calls"; Service Plan subscription (unlimited pausing, weekend discounts); bi-weekly invoicing; credit level ($50 starting figure) and 25%-of-recharge auto-bill triggers; 3–4 agent average multi-sell; specific report names (Lead Data, Daily Summary, Notes Summary, Transfer Details, Opportunity Reports); 60-second/5-attempt follow-up advice with vendor-claimed percentages.
- Leadpages: Smart Traffic, Optimization Score, Customers.ai-powered Visitor Intelligence — page-builder capabilities, irrelevant to this Type's core.
- Apollo: pillar names, contact-count marketing figures.

## Vendor-specific Findings

See L3 above. Also: the market label instability is itself a finding — Leadpages historically traded under "lead generation" positioning and in 2026 leads with "AI Landing Page Builder"; Apollo markets a "lead generation" content surface while self-labeling an AI sales platform. The leaf name maps to a market outcome ("more leads"), not to a stable product category; the Type is defined by the platform-operated-encounter structure instead.

## Boundary Findings

1. **vs Lead Capture Platform (processed; counterparty ratified with refinement).** The capture pass's proposed tri-partite split (capture = intake; generation = supply; management = lifecycle) is ratified, but "supply side" is sharpened: the load-bearing discriminator is **whose surface hosts the prospect's encounter**. Capture = designed prompts at the *business's own* marketing touchpoints (site pages, embedded widgets), converting traffic the business already attracts. Lead Generation = the platform *itself* operates the demand surface and supplies the audience (native ad-platform forms; platform-owned consumer destinations), converting the *platform's* audience into delivered leads. Both types share the lead record and the handoff — the venue is what separates them.
2. **vs Contact Discovery / Sales Prospecting / Sales Intelligence (§07, processed).** Database-sourced "lead generation" (find B2B contacts, enrich, sequence) has **no prospect-side expression of interest at a demand surface** — the mechanism boundary the capture pass drew for visitor identification extends here. The sampled database product self-labels an AI sales platform. The presence of a prospect-side intent event on a platform-operated surface is the discriminator.
3. **vs Landing Page Builder / Landing Page Optimization (§04.16 / §06, processed).** Page builders author conversion surfaces under the business's own domain; their traffic comes from the business's own campaigns. Directly observed drift: a page-builder product self-labels with lead-generation language while structuring as page authoring + capture + testing. Out of this Type.
4. **vs Advertising Campaign Management / Media Buying / DSP (§06 siblings).** Ad platforms contain the lead-gen objective as one conversion mechanism inside the ads product; those Types are about planning, buying, and optimizing media. This leaf is defined by the lead-supply machinery (form asset → record → delivery → per-lead economics), not by media management. Overlap zone acknowledged: the ad-pole realization ships inside ad tooling.
5. **vs Lead Management Platform (§07, unprocessed — flag carried forward).** This Type ends at delivery of the net-new lead; management owns the downstream lifecycle (qualification, scoring, routing, nurture, conversion). The sampled marketplace explicitly names the buyer's "lead management system" as the receiving system — supporting the seam. To be ratified from the management side in its own pass.
6. **vs Event Lead Retrieval (§26, processed).** Badge-keyed, exhibitor-operated, time-boxed event capture — no platform-operated demand surface, no ongoing supply relationship. Distinct.
7. **vs Online Form Builder (§03.11, processed).** A neutral form tool collects answers for any purpose; here the platform runs the demand side and the record is the sold/supplied product. The form is machinery inside this Type, never its definition.
8. **Taxonomy problem (recorded for STATUS).** "Lead Generation Platform" as a market label is polysemous: capture widgets, page builders, contact databases, and agencies all trade under it. This leaf is defined by the platform-operated-encounter structure; the other label usages belong to their own Types. No directory restructuring performed.

## Historical / Market-Sample Check

- **Pre-web lead brokering**: the sampled marketplace itself documents generational depth ("over 70 years of combined insurance lead delivery experience" across predecessor brands). The pre-portal realization — platform operates demand (ads, phone rooms), packages inquiries as lead sheets, delivers by fax/mail, bills per lead, credits invalid ones — satisfies L0 without portals, CSV, or auctions. Controls consoles are L1, not definitional.
- **Print-era analog**: magazine/newspaper reader-response cards ("request literature from advertisers") package reader interest as leads for advertisers through a media platform's machinery — fits the same L0.
- **Ad-platform lead gen is newer** (mid-2010s native lead forms), but its defining properties (native form on the platform's surface, profile-supplied identity, delivered records) are documented this pass from official docs rather than assumed.
- Conclusion: the definition is not over-fitted to the current SaaS implementation.

## Uncertainties

- **Ad-platform breadth**: the lead-form machinery was verified directly only in LinkedIn's help center. Meta Business Help (transport error ×2), Google Ads Help (timeout ×2), TikTok Ads Help (timeout ×2) were unreachable. The claim "ad platforms commonly offer a lead-generation objective with native pre-filled forms" is therefore canonical inference, not a cross-product observation.
- **Marketplace vertical breadth**: only the insurance vertical was sampled. The pay-per-lead marketplace pattern in other verticals (local services, real estate, mortgage, legal) is plausible but was not verified this pass and is not asserted product-specifically.
- **Agency-shaped "lead generation" services** (done-for-you outbound/lead-gen vendors) are services, not software platforms; they were not sampled and this document does not cover them.
- Typeform and Thumbtack help centers were not fetched (JS-rendered / time-boxed).

## Final Synthesis

A Lead Generation Platform is a **platform-side lead supply system**: it operates (or arms within its own ads product) the demand surface where prospective customers express interest, packages each expression into a lead record, and delivers those records into the buying business's follow-up systems under per-lead economics the business actively controls. Its two realizations — the ad-platform lead form and the pay-per-lead marketplace — differ in who configures the demand (the advertiser's campaigns vs the platform's own consumer destination) and in distribution policy (single-buyer vs shared multi-sell), but share the same three-part structure: platform-operated encounter → supplied lead record → delivery and handoff. It is bounded against Lead Capture (whose venue is the business's own touchpoints), against the §07 sales-data family (which sources records with no prospect-side intent event), against page builders (which author the business's own surfaces), and against Lead Management (which owns the lifecycle after delivery). The market label is unstable and polysemous; the structure is stable.
