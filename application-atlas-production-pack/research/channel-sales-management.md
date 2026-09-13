# Research Notes — Channel Sales Management

Research date: 2026-09-07
Slug: channel-sales-management
Directory leaf: "Channel Sales Management" (§07 Sales, Customer & Revenue)

## Research Goal

Understand what the software behind "channel sales management" actually is as a structure: what objects exist, who operates them on which surfaces, how the selling work flows between a vendor and its indirect channel partners, which states and rules govern it, and — critically, because a prior pass flagged it — whether this leaf is a distinct Application Type, an alias of Partner Relationship Management / PRM, or an umbrella over several channel-software categories.

## Initial Boundary (pre-research hypothesis)

- Inherited flag (from the PRM pass, 2026-09-06): "channel sales management" names the practice PRM implements; all three PRM-pass products self-identify as PRM and contain channel sales as one functional area (Channeltivity literally organizes its PRM into a "Channel Sales" area). Probable alias/superset — this pass must resolve it.
- "Channel" is polysemous: (a) indirect sales channel = resellers/distributors/referral partners (the §07 reading, next to PRM); (b) e-commerce sales channels = marketplaces (covered by §05.23 Multi-marketplace Seller Platform); (c) hotel distribution channels = OTAs (§26 Hotel Channel Manager). Directory context (§07, adjacent to PRM) disambiguates to (a).
- Suspected umbrella risk: "channel management" as a go-to-market domain also covers channel incentives (rebates/SPIFF/MDF), channel data management (sell-through/POS data from distributors), and through-channel marketing automation (TCMA). If the leaf is the umbrella, the document must say so; if it is the sales-motion slice, the umbrella members are boundary neighbors, not this Type.

## Research Questions

1. Do products self-identify as "channel sales management" / "channel sales" / "channel management" software? Which ones, and is that name coextensive with PRM or a distinct population?
2. What structures do vendors enumerate under the "channel sales" name (objects, workflows, states)?
3. Is there a "channel sales management" product WITHOUT the PRM structure (partner registry + partner-side participation + approval-gated co-selling) — e.g., a vendor-side-only channel operations tool?
4. Where does the selling-motion core (deal registration, lead distribution, referrals, channel pipeline) sit relative to the wider channel umbrella (incentives, data, marketing)?
5. What are the boundaries vs CRM, sales pipeline/forecasting, affiliate management, dealer commerce portals, and marketplace-channel seller tools?

## Representative Products

Selected for market representation, documentation accessibility, different product philosophy, and different customer tiers. Because the population under test is the PRM/channel-management category, the sample overlaps the PRM pass deliberately — the alias question requires observing the same products under the "channel sales" name.

| Product | Segment / philosophy | Evidence level reached |
|---|---|---|
| Channeltivity | Pure-play PRM branded "Intelligent Enterprise Channel Management"; modular, configuration-first; Growth (~100 partners) → Mid-Market → Enterprise | Tier-2 this pass (homepage + Channel Sales solution page) + Tier-1 help center carried from PRM pass (2026-09-06) |
| Unifyr (Zift Solutions) | Marketing-led heritage (Zift = TCMA pioneer), now "AI-native PRM" platform with agentic AI; Emerging → Mid-market → Enterprise | Tier-2 (homepage + Channel Sales solution page) |
| Impartner | Enterprise "PRM 3.0 / partner revenue management" suite; journey-led lifecycle | Tier-2 (homepage; carried from PRM pass) |
| Magentrix | PaaS PRM positioned "The Data Foundation for Channel Sales"; CRM schema mirroring | Tier-2 carried from PRM pass (2026-09-06) |

Boundary probes (not samples): 360insights (channel incentives), Vendavo (ex-Model N; channel data management).

## Sources

Fetched 2026-09-07:

- Channeltivity homepage — https://www.channeltivity.com/
- Channeltivity "Channel Sales Software" — https://www.channeltivity.com/channel-sales/
- Unifyr (Zift Solutions) homepage — https://www.ziftsolutions.com/
- Unifyr "Channel Sales" — https://www.ziftsolutions.com/solutions/channel-sales/
- Impartner homepage — https://impartner.com/
- 360insights homepage — https://360insights.com/
- Vendavo (modeln.com redirects to Vendavo) homepage — https://www.modeln.com/solutions/channel-data-management (landed on Vendavo high-tech revenue management homepage)

Carried from the PRM pass (fetched 2026-09-06, same products):

- Channeltivity Knowledge Base — https://help.channeltivity.com/support/solutions (deal registration, partner approval & onboarding, MDF articles)
- Magentrix homepage + Deal Registration feature page — https://www.magentrix.com/ , https://www.magentrix.com/features/deal-registration
- Impartner PRM product page — https://impartner.com/partner-relationship-management/

### Source-access Limitations

- Bing search (CN-localized) returned irrelevant results for "channel sales management" software (fashion-brand noise); DuckDuckGo timed out in the prior pass. Search engines are effectively unusable from this environment; product discovery relied on known category vendors and their own site navigation.
- Allbound returned 403 (second failure across passes) — abandoned per network rules.
- Impartner has no /solutions/channel-sales-management/ page (404); its channel-sales content lives under Pipeline Management (/lead-management/) and the journey graphic.
- Salesforce Partner Cloud / Oracle / Zoho suite-embedded PRM help centers remain unreachable (JS-rendered/404, per PRM pass) — the enterprise suite-embedded segment is evidenced only indirectly.
- Channeltivity blog article on channel sales management guessed-URL 404; not pursued further.
- Consequence: no claims about products other than the four samples + two boundary probes; no numeric limits (protection windows, SLA durations, report counts) asserted as universal — vendor-claimed figures stay in these notes.

## Product A — Channeltivity (Tier-2 this pass + Tier-1 carried)

### Key observations

**Naming (Tier-2, homepage):** homepage title "Intelligent Enterprise Channel Management"; tagline "Recruit, enable, and activate partners with the enterprise controls you need to grow your channel revenue". Product navigation splits the platform into three named areas: **Partner Enablement** (/partner-enablement/), **Channel Marketing** (/channel-marketing/), **Channel Sales** (/channel-sales/) — plus Integrations. Segment framing: Growth ("building your partner or dealer network", ~100 partners), Mid-Market, Enterprise. Vendor stats: "$4B+ active channel revenue managed".

**The "Channel Sales" area (Tier-2, /channel-sales/):** page title "Channel Sales Software". Key sentence: "Channeltivity's **PRM software** comes with everything you need to run a successful **channel sales operation**." — the vendor itself equates channel sales software with its PRM. Enumerated modules:

- **Deal Registration** — "protect partner opportunities and prevent channel conflict"; streamlined submission workflow; "admins get complete visibility into the pipeline"; automated notifications for status changes and expiring registrations.
- **Lead Distribution** — "route qualified leads to the right partners at the right time"; "automated routing rules based on geography, product specialization, partner tier, or custom criteria"; "track lead acceptance, follow-up, and conversion to measure partner performance and optimize your lead distribution strategy".
- **Referrals & Commissions** — "tracking partner-sourced opportunities and calculating payouts"; partners submit referrals through the portal; admins define commission structures, track deal progression, process payments; reporting on referral performance and commission accruals.
- **Distributor Management** — "for vendors who sell through a two-tier distribution model"; "track inventory, manage pricing and discounts, and collaborate with distributors and their downstream resellers".

CRM integrations named on the page: HubSpot, Salesforce, Dynamics 365.

**Carried Tier-1 (help center, 2026-09-06):** deal registration form fields (end-customer account + contact, deal name/amount/stage/close date), Registration Status as vendor-controlled approval workflow, stage field partner-editable or read-only (configurable), History & Notes change log, deal expiration configurable; partner lifecycle (prospective → vetting stages → Make Active → contacts promoted to users → groups); MDF credit transactions with expiration and reimbursement debits; distributor module interplay with deal registrations.

## Product B — Unifyr / Zift Solutions (Tier-2)

### Key observations

**Naming (homepage):** title "Partner Ecosystem Management Platform with AI – Unifyr"; self-description "The AI-native PRM for partner growth". Solutions nav: Partner Management, **Channel Sales** ("Drive partner-sourced revenue"), Channel Marketing, Partner Portals, Learning Management, Agentic AI. So "channel sales" is again a named solution area inside a self-described PRM.

**The "Channel Sales" solution page (Tier-2):** title "Channel Sales Software & Enablement Platform". Claim: "Channel sales comprise 75% of the world's trade" (vendor marketing figure — not evidence of structure). Enumerated elements:

- **Lead & deal visibility** — "complete visibility into their pipeline — from lead registration through deal closure… track progress, forecast revenue".
- **Deal registration** — "fast deal registration", "identify deal conflicts early", "holistic views to track progress".
- **Lead distribution** — "funnel hot leads to the right partners"; "automations and agentic AI… optimized lead and opportunity hand-off". Related-solutions card: "auditable assignment rules, acceptance SLAs, and closed-loop pipeline tracking".
- **Analytics dashboards** — vendor claims "13 built-in dashboards, 40 built-in reports" (product-specific figure); "unify PRM, LMS, and TCMA data".
- **Partner portal** — "on-demand training, co-brandable collateral, customized portal pages".
- **CRM connections** — bi-directional sync with Salesforce, Microsoft Dynamics, HubSpot, Zoho, SugarCRM; "sync leads and opps" (vendor says daily updates — product-specific claim).
- **Success Plans** — portal feature with goals, partner progress, steps; **Partner Explorer** — vendor-side tool to identify active partners and drill into individual partner revenue/marketing metrics.

**FAQ (vendor's own answers):** "What types of sales partners can be managed with Unifyr?" — "Resellers and Value-Added Resellers (VARs), Managed Service Providers (MSPs), Distributors, System Integrators (SIs), Affiliate Partners, and Referral Partners." "How does Unifyr help increase partner-sourced revenue?" — automating lead distribution, TCMA, deal registration, analytics. KPIs tracked: partner-sourced pipeline and revenue, lead acceptance and conversion rates, campaign engagement, training/certification progress, engagement scores.

Vendor stats (marketing): $25B+ total deal value, 3M+ deals, 30M+ leads generated, 800K+ partners, 1M+ users.

## Product C — Impartner (Tier-2)

### Key observations

**Naming (homepage):** "PRM 3.0 — The only end-to-end partner revenue management platform". Footer: "Impartner is the fastest-growing, most award-winning **channel management solution provider** on the market." — the vendor uses "channel management" and PRM interchangeably for the same product.

**Where the selling motion sits:** the partner-journey graphic places **"Manage Pipeline — Lead Distribution, Deal Registration"** as one stage between "Generate Demand" (TCMA, MDF, Marketplace, Referral Management) and "Co-Sell"; "Sell & Transact" carries CPQ. Applications list: Pipeline Management (/lead-management/ — "Sync deal registration and partner leads with CRM"), Referral Automation, MDF, Tiering and Compliance, Partner Business Planning, Training & Certification, Impartner Marketplace, HyperscalerGTM, Aimi AI, Orchestration Studio.

Industries named: Cyber Security, High Tech, Manufacturing, FinTech, Telecom.

## Product D — Magentrix (Tier-2, carried from PRM pass)

### Key observations

Positioning: "The Data Foundation for **Channel Sales**" — a PRM vendor explicitly naming its category "channel sales". Deal registration with four submission paths (portal form; ungated public page with cookieless tracking; email-to-portal; CSV bulk); **Deal Exclusivity Tracking** (exclusive rights for the sourcing partner; protection period starts after vendor approval + conversion into an opportunity; expiry notifications to both sides); **Deal Amendment** (partners update close date/value/stage under permission-based field controls; CRM opportunity owner alerted); **Deal Inbox** (internal team assigns incoming registrations/opportunities to partners; partner accepts or rejects); lead conversion with CRM account/contact merge; CRM schema mirroring (Salesforce/Dynamics).

## Boundary probes

**360insights (channel incentives — NOT this Type):** self-describes via FAQ as a "channel incentive management platform": "helps brands coordinate and optimize MDF & Co-Op, rebates, SPIFFs, and other incentive programs across partner, distributors, resellers, dealers, and service providers". Three suites: Experience (engagement), Incentives (B2B rebates, co-marketing funds, consumer promotions, loyalty/rewards, pricing & promotions), Services. No deal registration, no lead distribution, no co-sold pipeline — it is the money/motivation layer of the channel umbrella. Its existence as a separately named category confirms "channel management" the domain is broader than "channel sales management" the Type.

**Vendavo (ex-Model N — channel data management, NOT this Type):** modeln.com now redirects to Vendavo ("High-Tech Revenue Management Software"); Vendavo's nav lists **Channel Data Management** as a distinct solution; AMD quote on the page: "helps us manage our channel… with CDM, we can engage them all around the world". CDM = vendor-side collection/normalization of sell-through/POS/inventory data from distributors — no partner portal, no co-selling workflow. Second umbrella member confirmed as a separate category. (Model N brand absorbed into Vendavo — market-consolidation observation only.)

## Cross-product Comparison

| Structure | Channeltivity | Unifyr (Zift) | Impartner | Magentrix | Layer |
|---|---|---|---|---|---|
| Self-identifies as PRM while branding itself "channel management" / "channel sales" | ✓ homepage "Channel Management" + "Channel Sales" nav; page says "Channeltivity's PRM software… channel sales operation" | ✓ "AI-native PRM" + "Channel Sales" solution | ✓ "PRM 3.0" + footer "channel management solution provider" | ✓ "Data Foundation for Channel Sales" | A (4×) |
| Partner-sourced deal registration with vendor approval + protection/exclusivity | ✓ (Registration Status workflow, expiration, notifications) | ✓ (fast registration, conflict identification, progress views) | ✓ (Pipeline Management app) | ✓ (Exclusivity Tracking, protection period, expiry alerts) | A (4×) |
| Vendor→partner lead distribution with routing rules, acceptance, closed-loop tracking | ✓ (rules by geography/specialization/tier/custom; acceptance/follow-up/conversion) | ✓ (auditable rules, acceptance SLAs, closed-loop tracking) | ✓ (journey stage "Manage Pipeline") | ✓ (Deal Inbox, accept/reject) | A (4×) |
| Referral capture with attribution/payout linkage | ✓ (Referrals & Commissions module) | ○ (referral partners as type; referral in suite) | ✓ (Referral Automation) | ✓ (referral links, payouts) | B (3× strong + 1 weak) |
| Channel pipeline visible to both sides | ✓ (admin pipeline visibility; partner stage progress) | ✓ ("from lead registration through deal closure"; partners forecast) | ✓ (Pipeline Management) | ✓ (Pipeline Summary Pages) | A (4×) |
| Sourced-revenue attribution to the partner | ✓ | ✓ (partner-sourced pipeline/revenue KPI) | ✓ (partner-sourced revenue framing) | ✓ | A (4×) |
| Distributor / two-tier handling | ✓ (Distributor Management module) | ✓ (distributors as partner type) | ✓ (Disti Connect, PRM pass) | — | B (3×) |
| CRM bi-directional sync | ✓ (SF/HubSpot/Dynamics) | ✓ (SF/Dynamics/HubSpot/Zoho/SugarCRM) | ✓ (SF/Dynamics/HubSpot) | ✓ (schema mirroring) | A (4×) |
| Channel analytics (partner performance, sourced revenue, lead conversion) | ✓ (Performance Analytics) | ✓ (dashboards/reports, Partner Explorer) | ✓ (Reporting and Analytics) | ✓ (Analytics/Reports/Dashboards) | A (4×) |
| Partner portal as the partner-side surface | ✓ | ✓ | ✓ | ✓ | A (4×) |
| Partner registry with lifecycle (recruit/onboard/activate) | ✓ (Tier-1: prospective → active) | ✓ (onboarding workflows, agentic onboarding) | ✓ (Recruit→Enroll→Onboard journey) | ✓ (self-registration, segmentation) | A (4×) |
| Enablement/marketing/incentive modules adjacent to the sales core | ✓ (separate nav areas: Partner Enablement, Channel Marketing) | ✓ (separate solutions: Channel Marketing, Learning, MDF) | ✓ (separate applications) | ✓ (features) | A (4×) — adjacent areas, not the sales core |
| AI assistance | — (not surfaced this pass) | ✓ (agentic AI, Unifyr IQ) | ✓ (Aimi) | ✓ (AI deal intake, AI ops) | B (3×, optional) |

Reading: the "channel sales" name consistently denotes the same selling-motion structures (deal registration, lead distribution, referrals, channel pipeline, attribution) inside products that are, by their own self-description, PRMs. No sampled or probed product sells "channel sales management" without the PRM substrate.

## Canonical Abstraction

### L0 — Defining Invariant

A Channel Sales Management application is recognizable only when all of the following hold:

1. **A managed roster of external selling partners** — identified organizations (resellers, distributors, referral partners, agents) that the vendor sells through, each carried as a record with a governed program status. Without it, there is no channel — only the vendor's own pipeline.
2. **Shared selling objects that pass between vendor and partner under vendor-controlled acceptance, with the partner side acting inside the system** — partner-sourced deal registrations (submitted → approved/denied → protected), vendor-distributed leads (assigned → accepted → worked), referrals. Without the partner side participating in the system, this collapses into the vendor's CRM.
3. **A co-managed channel pipeline with attribution** — deal progress visible to both sides; closed revenue attributed to the sourcing partner, feeding commissions and channel reporting. Without it, the structures in (2) are just message-passing, not sales management.

Removal tests:
- Remove (1) → a lead-routing/CRM tool; no channel.
- Remove (2) → channel analytics or a partner directory; no co-selling.
- Remove (3) → a partner communication portal; the "sales management" property disappears.

### L1 — Common Mature Structure

Present across the sample; expected by the market but not definitional:

- Deal registration lifecycle detail: conflict checking against existing pipeline, protection/exclusivity windows with expiry notifications, stage tracking with partner-editable or read-only fields, close → payout linkage.
- Lead-distribution routing rules (geography, specialization, tier, custom criteria), acceptance/decline, acceptance SLAs (one product), closed-loop conversion tracking.
- Referral links and commission/payout structures.
- Distributor (two-tier) handling: distributor layer between vendor and resellers; assignment logic; inventory/pricing visibility (one product documents inventory tracking under distributor management).
- Channel analytics: partner-sourced pipeline and revenue, lead acceptance/conversion, partner performance/engagement, drill-down partner scorecards.
- The PRM substrate that makes the selling motion operable: partner onboarding/activation, portal, permissions, notifications.
- CRM bi-directional sync (registrations ↔ opportunities; partners ↔ accounts); SSO; multi-language; notifications/reminders.

### L2 — Variant / Optional Structure

- Partner-population mix: reseller/VAR-led, referral-led, distributor-led, SI/MSP-led programs; affiliates appear as one partner type in B2B-flavored products.
- Sales-motion emphasis: deal-registration-led (conflict/protection centric) vs lead-distribution-led (routing centric) vs referral-led (payout centric).
- Two-tier depth: distributor inventory/pricing collaboration vs simple distributor records.
- Packaging: standalone product vs CRM-embedded module vs extensible platform; channel-marketing (TCMA), MDF, training sold as adjacent modules of the same suite.
- Segment: first-program/Growth (~100 partners) → mid-market → global enterprise; industry tuning (high-tech/SaaS heartland, security, manufacturing, telecom, fintech).
- AI assistance: agentic onboarding, AI deal intake, coaching, recommendations.
- Adjacent umbrella categories (separate Types, sometimes same vendor): channel incentives (rebates/SPIFF/co-op), channel data management (sell-through data), through-channel marketing automation.

### L3 — Vendor-specific (research notes only)

- Channeltivity: "Intelligent Enterprise Channel Management" branding; three-area nav (Partner Enablement / Channel Marketing / Channel Sales); module names (Deal Registration, Lead Distribution, Referrals & Commissions, Distributor Management); Growth/Mid-Market/Enterprise framing; "$4B+ active channel revenue managed" claim; Tier-1 module mechanics carried from the PRM pass (Registration Status workflows, MDF Credit Transactions, SPIFF, Agreements).
- Unifyr (Zift): "AI-native PRM" positioning; Unifyr IQ agentic suite (Onboarding IQ, Campaign IQ, Ask IQ); Success Plans; Partner Explorer; "13 built-in dashboards, 40 built-in reports" and "sync leads and opps with daily updates" (product-specific claims); "channel sales comprise 75% of world trade" (marketing claim); legacy Zift/Unifyr brand history; $25B+/3M+ deals/800K+ partners marketing stats.
- Impartner: "PRM 3.0"/"Partner Revenue Management" rebrand; Aimi AI; journey-stage taxonomy; HyperscalerGTM; Disti Connect; Forrester TEI figures; "fastest-growing, most award-winning channel management solution provider" self-claim.
- Magentrix: "Data Foundation for Channel Sales" tagline; Deal Inbox; Smart Sync 15-minute default (product-specific); cookieless ungated registration page; PaaS IDE/CLI.
- 360insights: "channel incentive management platform" FAQ definition; Experience/Incentives/Services suite taxonomy; 22M+ incentive transactions claim.
- Vendavo: Model N brand absorption; CDM as a named solution; AMD customer quote.

## Boundary Findings

1. **vs Partner Relationship Management / PRM (sibling leaf) — the inherited flag, now resolved from this side.** Finding: **alias / practice-name relationship, not two Types.** Evidence: (a) every product that sells "channel sales" capability in the reachable market is a self-described PRM (Channeltivity: "Channeltivity's PRM software comes with everything you need to run a successful channel sales operation"; Unifyr: "The AI-native PRM" with a "Channel Sales" solution; Impartner: "PRM 3.0" with footer "channel management solution provider"; Magentrix: "Data Foundation for Channel Sales"); (b) "channel sales" appears as a named functional area INSIDE PRM products (Channeltivity nav, Unifyr nav, Impartner journey stage "Manage Pipeline"); (c) no product was found that self-identifies as "channel sales management" software while lacking the PRM structure (partner registry + partner-side participation + approval-gated co-selling). Reading: "channel sales management" names the practice (managing selling through indirect partners); PRM names the product category that implements it; the two directory leaves cover one product population with different emphasis lenses — PRM leads with the relationship program (recruit → onboard → enable → incentivize → govern), channel sales management leads with the selling motion (register → distribute → co-sell → attribute). Recommendation for the taxonomy owner: keep both leaves as live market names with cross-reference (as done for ATS/recruiting-management), or consolidate; do not treat them as two independent Types. This discharges the PRM pass flag.
2. **vs CRM.** CRM's pipeline is the vendor's own direct end-customer motion; channel sales management's pipeline is co-sold with external partners and requires partner-side participation and vendor approval gates. Deal registrations sync into CRM opportunities; partner organizations mirror CRM accounts. Remove partner-side participation → CRM with partner fields remains.
3. **vs Sales Pipeline Management / Sales Forecasting Platform (§07 siblings).** Those manage the direct pipeline owned by the vendor's own reps (stages, forecast categories); this Type manages a pipeline whose deals are sourced and worked by external organizations under program rules. Channel forecasting exists here as partner-sourced pipeline reporting, not as quota/forecast-category machinery.
4. **vs Affiliate Management Platform (§06).** Affiliates are individual promoters tracked by links and paid commissions on consumer reach; channel partners here are organizations in a governed program co-selling B2B deals. Affiliates appear as one partner type inside channel products (Unifyr FAQ names "Affiliate Partners").
5. **vs Dealer / Distributor Commerce Portal (§05.17).** Commerce portals center the catalog→order transaction for dealers buying stock; this Type centers the co-selling relationship and pipeline. Distributors appear as a managed partner type (with assignment logic and, in one product, inventory/pricing visibility), not as order-placing commerce principals.
6. **vs Channel Incentives (360insights-class; §06-adjacent category).** Incentives platforms coordinate rebates, SPIFFs, co-op/MDF, loyalty — the money/motivation layer. They lack deal registration, lead distribution, and the co-sold pipeline. MDF inside PRM/channel products is the overlap seam (funds tied to deals for ROI), but the incentive platform as a category is a separate structure.
7. **vs Channel Data Management (Vendavo/Model N-class).** CDM collects and normalizes sell-through/POS/inventory data from distributors — vendor-side-only, no partner participation, no selling workflow. A separate category under the same "channel" word.
8. **vs Multi-marketplace Seller Platform (§05.23) — name collision.** In e-commerce, "channel management" means managing product listings across marketplaces (a different population and structure). The directory already places that under §05.23; this leaf's §07 placement (next to PRM) disambiguates to the partner-channel reading. Recorded so a future reader does not conflate the two.
9. **vs Partner Portal / Customer Portal.** The portal is the partner-side surface of this Type, not the Type itself; portal + content without the selling workflow is a thinner structure (PRM pass demonstrated the same portal machinery sold pointed at customers).

## Historical / Market-Sample Check

- Would older or thinner products fit the L0? Early-2000s PRM/deal-registration modules (Siebel/Oracle-era partner portals with deal reg and lead assignment) fit: roster + shared selling objects + approval + attribution. Distributor deal-desk tools with assignment logic fit. Pure order-entry dealer systems do not (commerce, not co-selling). Spreadsheet-era channel management (deal reg by email/spreadsheet) is the pre-software practice, not the Type.
- The definition does not depend on current-era vocabulary (agentic AI, hyperscaler marketplaces, TCMA) — those are variant/optional. The "channel sales" name itself predates the AI era (deal registration and lead distribution were the core of 2000s PRM), so the selling-motion lens is not an artifact of today's sample.

## Uncertainties

- Enterprise suite-embedded offerings (Salesforce Partner Cloud, Oracle) remain unreachable; their channel-sales structure is inferred only from positioning references. Assertions about that segment are kept weak.
- Allbound (403 ×2) and other SMB-tier pure-plays (Kiflo — transport error in prior pass) could not be checked; the SMB pole is evidenced via Channeltivity's Growth segment framing and Unifyr's Emerging tier, not via those products' own docs.
- Whether any regional (e.g., Asian distributor-management) product self-identifies as "channel sales management" with a different structure could not be verified — search engines unusable; the L0 is kept abstract to accommodate them, but this remains unverified.
- Vendor-claimed figures (75% of world trade, 13 dashboards/40 reports, daily sync, $4B+ managed) are marketing/product-specific and are NOT carried into the final document as structural facts.

## Final Synthesis

"Channel sales management" is the practice-name for the software category the market mostly calls PRM. The researched products are PRMs that brand themselves "channel management" and expose "Channel Sales" as a named functional area; no product was found selling "channel sales management" without the PRM structure. The Type's defining core is the co-sold pipeline: a managed roster of external selling partners, shared selling objects (partner-sourced deal registrations under vendor approval and protection, vendor-distributed leads, referrals) that pass between the two sides inside one system, and attribution of closed revenue back to the sourcing partner. Around this core, mature products add routing rules, conflict detection, distributor two-tier handling, channel analytics, CRM synchronization, and — as adjacent modules of the same suites — the wider channel umbrella (enablement, marketing, incentives). The leaf is best documented as the selling-motion lens on the PRM structure, with the alias relationship recorded for taxonomy-level review rather than silently merging the two directory entries.
