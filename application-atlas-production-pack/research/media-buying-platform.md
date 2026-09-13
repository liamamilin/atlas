# Research Notes — Media Buying Platform

Research date: 2026-09-08
Slug: media-buying-platform (DIRECTORY §06 Marketing, Advertising & Growth)

## Research Goal

Understand what a "Media Buying Platform" is as an Application Type from real products: what the central objects are (plan, placement, order/IO, vendor, budget, bill), what the buying workflow looks like end-to-end, how channels (traditional / digital direct / programmatic) enter the structure, how money is handled (budgets → commitments → actuals → vendor bills → payment), who uses it, and where the boundary sits against the neighboring advertising-stack leaves in §06 (DSP, SSP, Programmatic, Ad Server, Advertising Campaign Management, SEM Management, Marketing Campaign Management, CMP) and against adjacent non-§06 systems (agency accounting/ERP, media research data services).

## Initial Boundary (hypothesis before research)

- Core use hypothesis: the agency-side (or advertiser-side) operation of buying paid media across many vendors and channels — planning what to buy, committing the buys (insertion orders / platform activation), tracking delivery and spend, reconciling vendor bills.
- Nearest neighbors: Demand-side Platform / DSP (programmatic trading), Advertising Campaign Management (campaign lifecycle on ad platforms), Marketing Campaign Management Platform (initiative planning), SEM Management (search slice), SSP (sell-side), agency accounting systems, media research data services (SRDS/SQAD class).
- Pre-hung seams from already-processed sibling passes:
  - programmatic-advertising-platform: "media buying is the whole buying operation (planning, negotiation, insertion orders, reconciliation across all channel types incl. non-programmatic); programmatic platforms are the trading infrastructure for the programmatic subset. Basis illustrates the layering: an 'advertising operating system' (media-buying breadth) containing a DSP module."
  - advertising-campaign-management: "media buying centers on planning/negotiating media purchases (upfronts, IOs, programmatic deals); campaign management centers on the operational campaign lifecycle."
  - marketing-campaign-management-platform: "media buying transacts placements; campaign management plans and coordinates the initiative that media buys serve."
  - search-engine-marketing-management-platform: "broader negotiation/planning of media across channels (incl. offline) vs the search-auction management slice; no engine-account write-back = media buying/planning."
  - supply-side-platform-ssp: "media buying is the whole buying operation …; the SSP is sell-side infrastructure. No overlap in customer or objects."

## Research Questions

1. What is the central object — media plan? placement? insertion order? campaign? How do they nest?
2. What does "buying" concretely mean in these products: which steps from plan to payment does the system carry?
3. How do channels enter: does one structure hold TV/radio/print/OOH next to search/social/programmatic?
4. How is money handled: budgets, commitment states, actuals, vendor bills, reconciliation, payment, agency commission?
5. Who uses it (agency vs advertiser; planner vs buyer vs finance) and what surfaces do they get?
6. How does programmatic fit: embedded DSP, integration, or absent?
7. What rules matter: authorization/approval gates, budget caps, order terms, reconciliation validation?
8. Where exactly are the boundaries to DSP, campaign management, marketing campaign management, agency accounting, and media research data tools?
9. Historical check: would paper-era media buying (plan book + signed IOs + affidavits + invoice reconciliation) satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophy, and different customer tiers:

1. **Bionic for Agencies** (Bionic Advertising Systems) — agency media planning & buying workflow automation across all channels; the clearest IO-and-reconciliation-centric implementation. Tier-1 knowledge base reachable.
2. **Basis** (Basis Global Technologies, fka Centro) — digital "advertising operating system" with an embedded DSP; planning→payment closed loop for digital channels. Tier-2 product pages + FAQ reachable; help center unreachable.
3. **Camphouse (fka Mediatool)** — advertiser/agency "media operations platform" led by a planning system of record + budget allocation + activation push. Tier-2 module pages reachable.
4. **Strata (FreeWheel)** — cross-media (traditional-heritage) agency platform: planning, activation, optimization, financial management. Tier-2 product page reachable; docs thin.
5. **Mediaocean** (positioning-level only) — enterprise agency system of record; Prisma (digital) + Spectra (traditional) split as named by Bionic's product pages. Direct site unreachable (2× transport error) — used only for category-shape evidence, no operational claims.

## Sources

- Bionic homepage: https://www.bionic-ads.com/ (fetched 2026-09-08)
- Bionic, "The 11 Steps of the Media Buying Process Explained": https://www.bionic-ads.com/media-buying/ (fetched 2026-09-08)
- Bionic Knowledge Base root + Bionic for Agencies user guide TOC: https://help.bionic-ads.com/knowledge , https://help.bionic-ads.com/knowledge/bionic-for-agencies (fetched 2026-09-08)
- Bionic, "Get To Know Bionic Data Structure": https://help.bionic-ads.com/knowledge/get-to-know-bionic-data-structure (fetched 2026-09-08)
- Bionic, "Manage Vendor Bill Reconciliation": https://help.bionic-ads.com/knowledge/manage-vendor-bill-reconciliation (fetched 2026-09-08)
- Basis homepage: https://www.basis.net/ and https://basis.com/technology/platform (fetched 2026-09-08; help.basis.net unreachable — 1 transport error, abandoned)
- Camphouse (fka Mediatool): https://camphouse.io/ , /media-activation , /planning-system-of-record , /budget-allocation (fetched 2026-09-08; login still at app.mediatool.com confirming the Mediatool lineage)
- Strata (FreeWheel): https://www.freewheel.com/strata (fetched 2026-09-08; canonical site gotostrata.com)
- Mediaocean: https://www.mediaocean.com/ and /media-buying-software-prisma — both transport errors (2 attempts, abandoned per network rule); evidence limited to Bionic's named-competitor pages
- Sibling research notes consulted: research/programmatic-advertising-platform.md, research/advertising-campaign-management.md, research/marketing-campaign-management-platform.md, research/search-engine-marketing-management-platform.md, research/supply-side-platform-ssp.md

## Product Observations

### Product A — Bionic for Agencies (evidence layer: A — Tier-1 official docs directly observed)

**Positioning (homepage, Tier 2):** "the only all-in-one software that automates media planning and media buying across all media channels, in all markets." Audiences: ad agencies, advertisers, ad sales (separate seller-side product). Homepage narrative walks the full loop: searchable ad catalog (vendor info, rates, contacts) → RFPs (signed/approved RFP integrates into plan) → flowcharts/PowerPoints/spreadsheets/allocations → client authorization → sending insertion order → launching ads → performance tracking "from PPC to CTV" with problem alerts → adjust in-flight → "automatically reconciles all my vendor bills."

**Domain process definition (vendor learning content, "11 Steps of Media Buying"):** Review Media Plan (verify signed media authorization) → Develop Buying Strategy → Media Research (consideration set; ranker reports; rates) → Send RFPs (inventory availability, pricing, packaging; proposals accepted into the plan) → Finalize Buying Schedule (program name, vendor, flight dates incl. weekparting/dayparting, cost method, pricing, quantity, net media cost) → Prepare IOs (burst plan into IOs — one per vendor/deal; attach terms & conditions incl. 4A's/IAB standard terms; internal approval before sending; create IOs even for programmatic to "capture the deal" and "set baseline for reconciliations"; programmatic IOs just aren't sent to vendors) → Send IOs (vendor approval/signature; e-signature preferred) → Implement Advertisements (deliver creative to spec on time; placement naming conventions; placement tracking IDs cross-referenced to platform IDs) → Track Performance (centralize platform data; compare actuals to plan; daily pacing as early warning) → Reconcile Vendor Bills (did we order this? already paid? did they deliver as promised? priced correctly? more than ordered?) → Campaign Reports. Also documents: planning vs buying historically separate, now merged; digital reduced negotiation (engines won't take IOs; auctions set prices) but IOs persist for governance; integrated multi-channel plans (magazine line 1, TikTok line 2, influencer line 3, radio line 4). Names the market set: "Bionic for Agencies – all media channels; Mediaocean Prisma – digital; Mediaocean Spectra – traditional; FreeWheel Strata – traditional."

**Object model (Tier-1 data-structure doc):** "Follow the money!"
- Organization → Advertisers (hierarchical; clients for agencies, company structure for in-house teams; access control per advertiser node) → Campaigns ("a marketing initiative tied to a particular budget… the 'folder' that stores everything related to it — settings, documents, budgets, RFPs & Proposals, media plan, orders, performance data, and payables"; core components: start/end date, overarching budget, media plan) → Media Plans (composed of **placements** = "the tactical level details"; each placement should represent an individual ad space: "who you are advertising through, details of the ad space, dates the ad is running, the rate you are paying, and the KPI goals"). Placement examples given: a specific Google Ads campaign, a specific Facebook campaign, full-page print ad in the New York Times, WXYZ TV Good Morning America :30, Lamar billboard #123445, Spotify campaign, Trade Desk campaign, WSJ leaderboard, conference event table, webinar — the full channel span in one structure.
- Costs: customizable production, agency commission, delivery fees; gross-to-net discount management; any currency.
- Budget Buckets: strategic allocation of the campaign budget (example: Digital/Video $350k, Social $100k, Programmatic $150k, TV/Radio/Cable $400k); placements allocated to buckets; spend calculated against available funds.
- Outputs from plan data: one-click flowcharts, media authorizations, trafficking sheets; placement naming conventions; tracking URLs.
- Orders: "point and click order generations, approvals, and electronic POs"; order terms library; order changes handled; order totals tied to plan.
- Vendor database: vendors, contacts, programs (researchable catalog).
- RFP workflow: send → review → manage proposals.
- Performance: integrations with 100+ platforms (DSPs — TTD, MediaMath, AdForm, StackAdapt, DV360, Simpli.fi…; walled gardens — Google Ads, Meta, LinkedIn, TikTok, Snapchat, Pinterest, Reddit, Amazon; TV/radio/print/OOH/podcast/e-newsletter/webinar report integrations; manual upload); actuals vs planned; daily pacing; fluid budgets; broadcast ad-spot logtime monitoring (delivery verification for traditional).
- Reconciliation (Tier-1): order details → "how much you ordered for each service period"; performance data → "how much got fulfilled"; vendor bills entered → "calculate the maximum billable amount and reconciled amount to help you validate that what you got billed for is correct" → "communicate to your Accounting department what has been approved for payment" → record payments → review payables → accounting integrations (QuickBooks, Advantage, Workamajig, NetSuite via Celigo).
- Client surfaces: share campaigns with client teams; client dashboards; Bionic for Advertisers companion product.

### Product B — Basis (evidence layer: A for positioning/FAQ claims — Tier-2 official pages directly observed; no Tier-1 operational docs)

**Positioning:** "Advertising Automation Platform for Omnichannel Media"; "The Intelligent Operating System for Autonomous Advertising"; "Basis is an advertising technology platform that unifies campaign planning, media buying, optimization, reporting, billing, and financial reconciliation into a single operating system."

**Channel span:** programmatic display, video, CTV, audio, native, DOOH via its proprietary DSP; search, social, site direct via direct API integrations with walled gardens. "All channels are managed, reported on, and reconciled within a single platform." Digital-only scope ("open web and walled gardens") — no traditional TV/radio/print in the current positioning.

**The DSP seam, vendor-articulated (FAQ):** "A demand-side platform handles programmatic media buying. Basis includes a proprietary DSP but goes much further, connecting media activation with campaign planning, team collaboration, workflow automation, financial reconciliation, and AI-powered optimization across all digital channels… It's built to serve as the operational foundation for an entire advertising organization, not just the buying function."

**Money loop:** "Financial Connectivity: From Planning to Payment — Basis creates a closed-loop system from the first media plan to the final invoice. Push contracts and campaign actuals into ERP systems, automate billing, and normalize reconciliation across the entire media supply chain. Because advertising isn't done until the dollars reconcile." "Financial Integrity: standardizes and validates financial data across the entire campaign lifecycle, flagging discrepancies in real time."

**Workflow automation:** "automates the tasks that eat up time and create the most risk, including campaign setup, trafficking, pacing, QA, reporting and billing." Automated Planning / Automated Performance / Automated Measurement / Automated Billing feature pages exist.

**Users:** mid-to-large agencies and in-house brand teams; roles named: agency & marketing leaders, finance & operations leaders, media directors & team leads, planners/buyers/specialists. Managed-services layer (Unify by Basis; media consulting & activation) optional.

**AI (era-current):** Compass (brief → omnichannel plan draft), SmartBid (cross-channel bidding/budget shifting), governed-AI framing.

### Product C — Camphouse, fka Mediatool (evidence layer: A for positioning/module claims — Tier-2 official pages directly observed)

**Positioning:** "The Intelligent Media Operations Platform"; "data-first advertisers and agencies Allocate, Plan, Activate and Report their paid media campaigns, collaboratively & globally." Audiences: enterprise advertisers, media agencies, advertisers. Login still at app.mediatool.com (Mediatool lineage confirmed).

**Planning system of record:** "consolidate Marketing's strategic vision, Media's execution data, and Finance's budgetary guardrails into a single, interoperable platform… a 360-degree view of Planned vs. Actuals in real-time… every dollar is tracked from the first brief to the final result." Anti-pattern named: plans as "Friday_Final_v3_updated.xlsx" executed in silos ("Media Amnesia"). Automated flowcharts; dimension filtering (media owner, creative asset, campaign type, market clusters); multi-year investment trends; "Media Owner Spend Analysis: understand your total leverage with global partners… how much you are investing with specific vendors across all markets and years."

**Budget allocation (money states):** "See exactly how much of your target budget is **planned, committed, and remaining**." Over-allocation cap: "teams cannot commit more budget than has been authorized"; hard limits at org or client level; real-time validation — "immediate alerts and blocks when a plan exceeds its allocated bucket"; top-down allocation across regions/brands/campaigns; KPI-driven allocation; dynamic adjustments.

**Activation:** "Bridge the activation gap by pushing validated plans directly to the platforms where they live… the taxonomy, budgets, and targeting defined in your plan are executed with 100% accuracy." Direct API deployment to leading ad platforms (one-click publishing to Meta Business Manager, Google Ads, LinkedIn); "Only approved line items can be pushed for activation, ensuring every dollar spent is authorized." Grasp partnership overlay extends to 50+ additional platforms via a Chrome extension enforcing naming taxonomy at the source (TikTok, The Trade Desk, Amazon Advertising), giving "a perfect 1:1 match between your Planned Intent and Actual Performance data"; central oversight "across multiple agencies and 120+ markets"; real-time pacing "against the authorized budget"; "agency-managed flexibility" (agencies execute in their own tools under central governance).

**Not evidenced:** vendor-bill reconciliation / payables in-product (module list: Budget Allocation, Media Planning, Media Activation, Reporting). The money loop is realized as budget authorization + commitment states + pacing + planned-vs-actual, with finance guardrails, not as a vendor-bill close.

### Product D — Strata (FreeWheel) (evidence layer: A for positioning — single Tier-2 page; docs thin)

**Positioning:** "The Strata platform enables cross-media campaign planning, activation, optimization, and financial management, all in one system… combining a data-centric and single-hosted platform, an open integration model, and applied automation." "Comprehensive tools and capabilities for every step of the campaign workflow, from pre-buy through execution."
- Process automation: "automates the complex, manual work behind every campaign – from orders and approvals to trafficking."
- OneStrata Digital: "next-generation digital campaign platform… streamlined planning and buying."
- Financial Bridge: "seamless integration between an agency's media and finance systems, and an API connection ensures accurate media billing and payment information."
- Data enablement: connect attribution tools directly to the Strata database.
- Partnerships: premium supply access (OTT, podcasting); traditional-heritage (TV/radio) platform per Bionic's categorization and FreeWheel's TV lineage.

### Product E — Mediaocean (positioning-level only; site unreachable)

Named by Bionic's process page as one of the "popular Media Buying systems": Mediaocean Prisma (digital media channels) and Mediaocean Spectra (traditional media channels). The programmatic-advertising-platform pass independently recorded Basis/Mediaocean as the media-buying-breadth layer containing DSP modules. No operational claims made; site unreachable (2× transport error).

## Cross-product Comparison

| Structure | Bionic | Basis | Camphouse | Strata |
|---|---|---|---|---|
| Media plan of record (placements × vendors × channels × dates × rates) | Yes — Tier 1 (placements as individual ad spaces; NYT print next to Google Ads next to Trade Desk) | Yes — "first media plan"; Compass drafts plans | Yes — "Planning System of Record"; line items; flowcharts | Yes — "cross-media campaign planning… pre-buy through execution" |
| Multi-vendor, multi-channel span in one structure | Yes — all channels incl. traditional | Yes — digital only (programmatic + search + social + site direct) | Yes — digital platforms; 120+ markets; media-owner spend across vendors | Yes — cross-media, traditional heritage + digital |
| Committed buy (authorized, money-binding commitment) | Yes — orders/IOs: generation, approvals, e-signatures, terms library, changes | Yes — "media contracts" pushed to ERP; campaign setup automated | Yes — "planned, committed, remaining"; over-allocation caps; "only approved line items can be pushed" | Yes — "orders and approvals" |
| Actuals vs plan on the same objects (pacing/variance) | Yes — daily pacing, fluid budgets, spot logtimes | Yes — unified data; pacing automated | Yes — planned vs actuals real-time; pacing vs authorized budget | Yes — reporting/visualization in workflow |
| Vendor-bill reconciliation → payment/accounting handoff | Yes — Tier 1 (max billable/reconciled amounts, payables, payments, QuickBooks/Advantage/Workamajig/NetSuite) | Yes — "closed-loop… to the final invoice"; ERP push; automated billing | Not evidenced (finance guardrails instead) | Yes — Financial Bridge; "media billing and payment information" |
| RFP/proposal workflow | Yes — Tier 1 | Not evidenced on fetched pages | Not evidenced | "pre-buy" implied; not detailed |
| Vendor/program database | Yes — Tier 1 (vendors, contacts, programs, rates) | Not evidenced | Media-owner spend analysis implies vendor dimension | Partnerships/supply access |
| Trafficking handoff (creative, naming, tracking, platform push) | Yes — Tier 1 (ad-server trafficking, naming conventions, tracking URLs) | Yes — automated trafficking | Yes — activation push + taxonomy enforcement | Yes — "orders and approvals to trafficking" |
| Programmatic posture | DSP-agnostic (performance integrations with many DSPs; IOs even for programmatic) | Embedded proprietary DSP | Platform-agnostic push (API + overlay) | Digital module (OneStrata); premium supply partnerships |
| Customer side | Agency (primary) + advertiser companion product | Agencies + in-house brands | Advertisers + agencies (both first-class) | Agencies (traditional-heritage) |
| Client-facing surfaces | Yes — client teams, dashboards, Bionic for Advertisers | Reporting transparency | Yes — brand central oversight over agencies | Reporting |
| Agency economics (gross/net, commission) | Yes — Tier 1 (gross-to-net, agency commission defaults) | Not evidenced | Not evidenced | Not evidenced (financial integrations imply) |
| AI planning/optimization | Yes — collaborative-filtering recommendations | Yes — Compass, SmartBid | Yes — CoPilot | Not evidenced |
| Approval/authorization gates | Yes — order approvals, media authorizations, plan locks/change history | Yes — approvals in connected teams | Yes — authorization caps, approved-line-items-only push | Yes — orders and approvals |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The media plan of record** — the intended buys held as structured placements across multiple independent media vendors and channel types (vendor/program, flight dates, rate/cost, quantity, KPI goals), maintained as the standing record the whole operation works from. Remove → a media research/catalog service or a spreadsheet, not a buying platform.
2. **The committed buy** — plan lines converted into authorized, money-binding commitments to specific vendors: insertion orders with terms and approvals (agency form) or approved line items pushed to ad platforms under budget authorization (digital form). Budget caps prevent committing beyond authorization. Remove → planning advice with no transaction; the "buying" is gone.
3. **The spend-and-delivery accountability loop** — actual spend and delivery captured against the same plan/buy objects (planned vs committed vs actual; pacing; variance), driving in-flight reallocation; in the full agency form the loop closes financially: vendor bills reconciled against orders and handed to payment/accounting. Remove → a plan+order document generator with no operational memory; the platform stops "running" the buying operation.

Jointly-held is load-bearing:
- 1 alone = media planning tool / rate-and-data service
- 2 without 1 = scattered ad-hoc orders, no operation of record
- 3 without 1+2 = marketing analytics or finance reporting
- 1+2 without 3 = document generation, not an operating platform
- 2+3 without 1 = execution tooling with no plan to be accountable to

### L1 — Common Mature Structure (standard capabilities, not definitional)

- RFP → proposal workflow with vendor response tracking (Bionic Tier 1; traditional-buying practice)
- Vendor/program database with contacts, rates, programs (Bionic)
- Media flowcharts, client presentations/authorizations as generated outputs (Bionic, Camphouse, Strata)
- Trafficking handoff: creative association, ad specs, naming conventions, tracking URLs, ad-server/platform push (Bionic, Basis, Camphouse, Strata)
- Performance-data integration from ad platforms/DSPs into the same data model (Bionic 100+ integrations; Basis unified dataset; Camphouse planned-intent↔actual matching)
- Pacing monitoring and budget reallocation / fluid budgets (all four)
- Budget buckets / top-down allocation hierarchies (Bionic, Camphouse)
- Gross-to-net discount and agency-commission economics (Bionic Tier 1; agency pole)
- Vendor-bill reconciliation → payables → payments → accounting/ERP integration (Bionic Tier 1, Basis, Strata — the agency-pole full form of L0 leg 3)
- Approval workflows, authorization gates, change history/audit (Bionic, Camphouse, Strata)
- Reporting/dashboards, client-facing surfaces (all four)
- AI planning/optimization assistance (Basis Compass/SmartBid, Bionic recommendations, Camphouse CoPilot) — era-current

### L2 — Variant / Optional Structure

- Channel scope: all-channel including traditional (Bionic, Strata) vs digital-only (Basis, Camphouse)
- Programmatic posture: embedded proprietary DSP (Basis) vs DSP-agnostic integrations (Bionic) vs platform-push activation (Camphouse)
- Customer side: agency-first vs advertiser-first vs both (Camphouse both; Bionic agency + advertiser companion; Basis both)
- IO form vs activation form of the committed buy (traditional IO with signatures vs approved-push under budget caps; Bionic explicitly creates IOs even for programmatic as governance)
- Multi-currency, multi-market, multi-year structures (Camphouse 120+ markets, multi-year trends; Bionic any currency)
- Delivery-verification machinery for traditional channels (Bionic broadcast spot logtimes)
- Managed-services layer on top of the platform (Basis Unify/consulting)
- Advertiser-side governance over multiple agencies (Camphouse central oversight)

### L3 — Vendor-specific (research notes only)

- Bionic: DEI scorecards, Bionic Academy, "Bionic for Ad Sales" companion, budget-bucket naming
- Basis: Compass, SmartBid, Unify by Basis, Basis Assistant, Communication Portal, Document Storage as named modules; Forrester TEI stats
- Camphouse: Grasp Chrome-extension overlay partnership, "Media Amnesia" framing, "House of" IA
- Strata: OneStrata Digital, Financial Bridge as product names
- Mediaocean: Prisma/Spectra digital/traditional split

## Rejected Findings

- "Media buying platform = DSP" — rejected: Basis's own FAQ separates the two; the DSP is one module/channel posture inside a buying platform; DSPs do not hold cross-channel plans, IOs, or vendor-bill reconciliation.
- "Media buying = campaign management on ad platforms" — rejected: campaign management (per the processed sibling pass) is the advertiser-defined campaign lifecycle (creatives+targeting+budget+schedule) on publisher platforms; media buying holds the cross-vendor commercial operation (who we buy from, terms, reconciliation). Overlap zone acknowledged (both configure and launch campaigns on platforms).
- "Reconciliation is optional garnish" — rejected for the agency pole: it is the traditional heart of the buying job (Bionic's step 10 of 11; Basis's "advertising isn't done until the dollars reconcile"; Strata's Financial Bridge). Held as the full form of L0 leg 3 rather than a separate leg because the advertiser-pole variant (Camphouse) realizes accountability through budget authorization + pacing without an in-product bill close.
- "Planning is a different Type" — rejected: every sampled product integrates planning upstream of the buy; the market treats planning+buying as one continuous operation (Bionic: "the distinctions… have blurred and have become one unified process"). Planning-only tools (rate/data services) are a capability, not this Type.

## Boundary Findings

1. **vs Demand-side Platform / DSP (§06 sibling, unprocessed)** — DSP: per-impression programmatic trading infrastructure (bid requests, auctions, its own bid engine). Media Buying Platform: the whole buying operation across channels with plan/order/money structures. Vendor-articulated seam (Basis FAQ): DSP "handles programmatic media buying"; the buying platform "includes a proprietary DSP but goes much further… the operational foundation for an entire advertising organization, not just the buying function." Layering: a media buying platform may contain a DSP as a module (Basis); a DSP does not contain a buying operation. Remove the plan/order/reconciliation span, keep per-impression bidding → DSP.
2. **vs Advertising Campaign Management (processed)** — campaign management: advertiser-defined campaign (creatives+targeting+budget+schedule) launched and optimized on ad platforms; monitor→adjust loop. Media buying: the cross-vendor commercial operation (plan → commit → reconcile). Overlap zone real (both touch platform campaign setup; Basis automates campaign setup). Seam: campaign management is per-platform execution lifecycle; media buying is the multi-vendor money operation the campaigns serve. Consistent with the pre-hung seam from that pass.
3. **vs Marketing Campaign Management Platform (processed)** — keep-both per that pass's seam: campaign management plans/coordinates the marketing initiative (brief, assets, calendar); media buying transacts the placements the initiative requires. Different central objects (initiative container vs placement/buy).
4. **vs Supply-side Platform / SSP (processed)** — sell-side infrastructure (media owners monetizing inventory); no overlap in customer or objects. Consistent with SSP pass.
5. **vs Search Engine Marketing Management Platform (processed)** — SEM management: third-party management layer over search-engine ad accounts (keyword bids/budgets written back via engine APIs). Media buying: cross-channel incl. offline; search is one channel; no engine-account write-back requirement. Consistent with SEM pass's seam.
6. **vs Ad Server (processed)** — ad server: request-time ad selection/delivery machinery. Media buying: the commercial buying operation. No overlap in objects.
7. **vs Agency accounting/ERP systems (Workamajig, Advantage, Clients & Profits, QuickBooks/NetSuite class; not directory leaves)** — those hold the agency's general ledger, client billing, time/projects. Media buying platforms integrate with them (Bionic: QuickBooks/Advantage/Workamajig/NetSuite; Strata: Financial Bridge; Basis: ERP push) and hand off approved-for-payment data; they do not replace them. The media-side money record (orders, vendor bills, media cost) is the buying platform's; the GL is the accounting system's.
8. **vs Media research/data services (SRDS, SQAD, Nielsen class; not directory leaves)** — rate/audience data and media catalogs are a capability inside buying platforms (Bionic vendor database/programs; research step), not the buying operation itself.
9. **vs Marketing Analytics / Attribution / MMM (processed siblings)** — measurement/modeling layers consume delivery/outcome data; the buying platform's reporting is centered on plan-vs-actual for its own buys, not attribution modeling.

**"Remove what to become the other Type" judgments:**
- Remove multi-vendor plan + IO/reconciliation span, keep per-impression auction bidding → DSP
- Remove the vendor/money/reconciliation span, keep per-platform campaign lifecycle → Advertising Campaign Management
- Remove the placement/buy transaction, keep the initiative container → Marketing Campaign Management
- Remove the buy commitment + money loop, keep research/catalog data → media research service (no leaf)
- Flip the customer to the media owner → SSP territory

## Historical / Market-Sample Check

Paper-era media buying (pre-software): media plan/flowchart as the plan book; typed insertion orders signed by agency and vendor; tear sheets/affidavits/logtimes as delivery proof; vendor invoices checked against orders before payment; agency commission (gross-to-net) as the compensation model; client billing from the same records. All three L0 legs satisfied: plan of record ✓, committed buy (signed IO) ✓, spend-and-delivery accountability incl. bill reconciliation ✓. No software-era specifics (APIs, DSPs, dashboards, AI) are in the L0. Historical check **passed**.

Platform-native / regional checks: an in-house advertiser team running a planning-led platform (Camphouse shape) fits via the budget-authorization form of leg 2 and the pacing form of leg 3; a local agency buying only TV/radio (Strata heritage shape) fits via the IO form; a digital-only agency platform with an embedded DSP (Basis shape) fits with channel scope as a variant. The definition does not depend on IOs specifically (the commitment can be activation-push), on traditional channels, or on agency commission.

## Uncertainties

- **Mediaocean unreachable** (2× transport error): category-shape evidence only (named by Bionic as a media buying system; Prisma/Spectra split). No operational claims.
- **Basis Tier-1 docs unreachable** (help.basis.net transport error): Basis structure known at positioning/FAQ level only; no claims about Basis's internal object model (e.g., whether it exposes IO-like order objects) are made.
- **Camphouse vendor-bill reconciliation not evidenced**: the advertiser-pole money loop is evidenced as budget authorization + commitment states + pacing + planned-vs-actual; whether Camphouse closes the loop to vendor bills in-product is unknown. This drove the decision to hold the bill-close as the full form of L0 leg 3 rather than a separate invariant leg.
- **Strata docs thin** (single product page): structure known at capability level; no operational detail claims.
- **Camphouse/Mediatool rebrand recency**: mediatool.com now serves Camphouse branding; login host still app.mediatool.com. Treated as one product lineage.
- Market-category naming: "media buying platform/software" is vendor-articulated (Bionic's named-systems list; Bionic/Mediatool/Strata/Mediaocean comparison pages) but no independent category registry was fetched; the Type claim rests on the sampled products' self-descriptions and shared structure.

## Final Synthesis

A Media Buying Platform is the buyer-side operating platform for the media buying operation: it holds the media plan of record (structured placements across many independent vendors and channels), converts plan lines into authorized money-binding commitments (insertion orders with terms/approvals, or approved activation pushed to ad platforms under budget caps), and runs the spend-and-delivery accountability loop on the same records — planned vs committed vs actual, pacing, variance — closing financially (in the full agency form) through vendor-bill reconciliation and payment/accounting handoff. Planning is integrated upstream; programmatic is one channel posture (embedded DSP, agnostic integrations, or platform push); traditional and digital channels share one structure. The Type is distinct from DSP (trading infrastructure), from advertising campaign management (per-platform campaign lifecycle), from marketing campaign management (initiative container), from SSP (sell-side), and from agency accounting (GL system) — while integrating with all of them.
