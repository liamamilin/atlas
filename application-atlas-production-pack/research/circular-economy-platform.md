# Research Notes — Circular Economy Platform

Research date: 2026-09-07

## Research Goal

Understand what software products marketed as "Circular Economy Platforms" actually are and do, from real product documentation. Determine whether "Circular Economy Platform" is one coherent Application Type, an umbrella over several structures, or a variant/alias of a neighboring leaf — and produce the canonical model + final document.

## Initial Boundary

Initial hypothesis (pre-research, to guide sampling):

- Core use: help organizations keep products, components, and materials in productive use (reuse, resale, recycling, recovery) instead of linear take–make–dispose.
- Likely users: corporate sustainability teams, facilities/workplace teams, supply-chain compliance teams, recyclers/traders.
- Nearest neighbors in DIRECTORY §21: Waste Management Platform, Hazardous Waste Management, Recycling Operations Management, Waste Hauling Management, Resource Efficiency Management, Sustainability Management Platform, ESG Reporting Platform. Also §05 Marketplace / §05.19 Resale, §03.15 Files-adjacent inventory systems.
- Obvious unknowns: is the market one product shape (marketplace? tracker? measurement tool?) or several? Does "platform" imply multi-party networks?

## Research Questions

1. What are the core "things" inside such a system (objects, participants, loops)?
2. What does a user actually do: list, trade, measure, trace, report?
3. Do money movement and logistics belong to the Type, or only to some poles?
4. How do regulatory frameworks (EU DPP, ESRS E5, EPR, ISO 59020, CTI) shape the product?
5. How is trust established (verification, custody, auditability)?
6. What is the boundary against Waste/Recycling Operations software, Sustainability/ESG platforms, Marketplaces, and Recommerce?
7. Would older/regional circularity software (waste exchanges, surplus catalogs, industrial symbiosis networks) still fit the definition?

## Representative Products

Selected to cover different poles, philosophies, geographies, customer layers:

| Product | Pole | Geography | Customer layer |
|---|---|---|---|
| Rheaply | asset inventory + internal/external reuse exchange + disposition | US | enterprises, universities, healthcare, venues |
| Circular IQ (CTI Tool) | circularity measurement, assessment, reporting | NL/EU | corporate sustainability teams + consultants |
| Circularise | n-tier supply-chain traceability, chain of custody, Digital Product Passports | NL/EU | manufacturers/brands (batteries, textiles, polymers) |
| ScrapAd | B2B trading marketplace for scrap / recyclable metals | ES/global | recycling industry traders, purchasers, scrap holders |
| Empower / Jörð.tech | collection-network traceability + EPR compliance + impact credentials (deposit incentives) | NO/global | collector-network orgs, brands, PROs, informal sector programs |

Rejected/dropped candidates: Topolytics (waste-flow analytics; site returned empty on two fetch attempts — abandoned per network rule; possible additional "waste-movement mapping" pole remains unsampled). Madaster (building material passports — considered; construction-vertical, overlaps Circularise pole; not fetched given time). Loop by TerraCycle (consumer reuse program — service-heavy, marginal software platform).

## Sources

All fetched 2026-09-07:

- Rheaply homepage — https://rheaply.com/ (Tier 1/2 mix: positioning + module descriptions)
- Rheaply Help Center (Intercom) — https://support.rheaply.com/en/ (Tier 1: collection structure, article counts, functional descriptions)
- Circular IQ homepage — https://circular-iq.com/ (Tier 2)
- Circular IQ baseline assessment page — https://circular-iq.com/baseline-assesment/ (Tier 2)
- Circularise homepage — https://www.circularise.com/ (Tier 2)
- ScrapAd homepage (EN) — https://scrapad.com/en/ (Tier 2)
- Empower Foundation / Jörð.tech — https://www.empower.eco/ (Tier 2; site now presents Jörð.tech "System of Material Intelligence" as the technology layer and Empower Foundation as the program layer)

Source-access limitations:

- No deep operational help centers reachable except Rheaply (Intercom help center). Circular IQ's app (app.ctitool.com), ScrapAd's marketplace (marketplace.scrapad.com), and Circularise's product UIs are login-gated.
- Consequently: measurement mechanics (indicator formulas, scenario behavior), escrow specifics, passport data schemas are NOT directly observed. Precise numbers below are quoted from vendor marketing and stay in these notes; the final document avoids precise operational claims.

## Product Observations

### Product A — Rheaply (asset reuse / disposition)

Evidence layer: A (directly observed on official pages).

- Self-description: "Operational efficiency starts with knowing what you own"; "full end-to-end lifecycle management platform… built for workplace and real estate teams to see what you own, where it is, and what it's worth" — reduce over-purchasing, faster operations.
- Solution set (site nav): Inventory management; Internal reuse; Decommissions; Sustainable disposition; Reuse marketplaces (cities); Sustainability consulting.
- Inventory management: tracks every asset's location, condition, and value; "eliminate blind spend"; searchable asset data; replaces spreadsheets.
- Internal reuse: "more than a private marketplace — a management system that powers collaboration, approvals, and asset control"; approval workflows; "organized, trackable redeployment".
- Sustainable disposition: "End-of-life doesn't mean end-of-story; rehome your resources"; match with buyers or nonprofits; recover value from surplus; "prove outcomes with audit trails and real-time impact data".
- Decommissions: manage moves/clear-outs; reuse/redeploy decommissioned assets; "prove impact with carbon and cost data"; network of "3,400+ network partners" (vendor claim).
- Impact metrics surfaced on site: weight diverted from landfill; items exchanged; carbon emissions avoided; procurement dollars avoided; value donated; "reuse moments".
- Internal module vocabulary visible: Visibility (inventory), Circulate (internal reuse), Next Life (disposition), Consulting, Decommissions.
- Help Center (Tier 1) collections: Getting started (12 articles); Posting items for reuse — "Sell, donate, or make items available for internal reuse" (19); Shopping for reused items — "Search and browse for reused items" (13); Account & Profile (9); Admin — "Manage your organization, users, and teams" (5); Inventory Management (16).
- Case-study customers: university, medical center, healthcare system, bank, sports venue, retail chain. Reuse savings claims ($530k university; $193k+ healthcare) — vendor claims, not independently verified.

### Product B — Circular IQ / CTI Tool (measurement & reporting)

Evidence layer: A for positioning/features; operational depth not observed.

- Self-description: "Measure your circular economy performance"; "Circular Economy Made Simple"; "The fastest, easiest way to understand what drives your performance and how to improve it".
- Named flow (homepage steps): Set a circularity baseline → Activate your supply chain (priorities based on "good quality data") → Optimize your efforts (allocate time/resources) → Compliant with leading standards ("Effortlessly create reports in line with ESRS E5, GRI, ISO 59020").
- Product: "All your circularity data in one place"; streamlined tool that "fits with your current infrastructure and workflow".
- Services around the tool: Gap Analysis ("We fill your data gaps with proxy values from our expertly-researched database"); Baseline assessment (product-based or organization-wide); "Circular data success" playbook ("auditable material composition insights").
- Framework: implements WBCSD's Circular Transition Indicators (CTI) — confirmed by WBCSD testimonial ("Circular IQ is a valuable partner… our Circular Transition Indicators… helping us bring CTI to life").
- Outputs: "Get insights / Create scenarios / Get easy to understand reports".
- Pricing: "plans start at €11.700 per year" (vendor FAQ claim).
- Customers shown: Microsoft, Sony, BP, Deloitte, KPMG, etc. (logos only).

### Product C — Circularise (traceability / DPP)

Evidence layer: A for positioning/features; no operational UI observed.

- Self-description: "Supply chain traceability software for faster compliance".
- Three named solutions: Collect ("Collect n-tier supplier data such as declarations, evidence, and due diligence data at scale"), Trace ("Maintain auditable Mass Balance / Chain of Custody for claims across transformations and allocation"), Share ("Publish Digital Product Passports, permissioned disclosures tied to identifiers and QR/data carrier").
- Homepage model: Suppliers → You → Customers (n-tier chain).
- Use cases mapped to regulations: EU Battery Regulation (Battery Passport), Critical Raw Materials Act (CRM Passport), ESPR (Digital Product Passport), EURO7 (Environmental Vehicle Passport), ELV Regulation, ISCC PLUS & ISCC EU, US Section 232 tariffs.
- Case studies: Honda (battery passport readiness ahead of 2027), Samsonite (DPPs for luggage), Teijin ("traced materials from the factory to recycled content… large-scale traceability").
- Lead-gen tool: "Get your compliance map" — summary of modules and evidence needed per selected regulation.
- No marketplace, no payment, no logistics anywhere on the site.

### Product D — ScrapAd (secondary-material trading marketplace)

Evidence layer: A for positioning/features; marketplace UI login-gated.

- Self-description: "Your global trading partner for buying and selling scrap and recyclable metals… in more than 45 countries" (vendor claim). "Transforming waste into global opportunities".
- Service chain: "From verifying companies and materials to securing advance payments and managing logistics"; "Find and negotiate with companies in the industry for the materials you need, we'll take care of the rest".
- Named mechanisms: "Deal with verified professionals" (all members "passed a thorough verification process"); "Secure payments and deposits" ("Transactions are carried out securely through our platform, guaranteeing your money throughout the process"); "Integral logistic management" ("We collect the material from the seller's facilities and deliver it to the buyer").
- Marketplace: published sell ads ("I want to sale") with material taxonomy: stainless 304, HMS1 cuttings, rails, aluminium wire/cable, Zorba (shredded nonferrous), copper/aluminium radiators, ingots; free registration to view ads.
- Extras: metal price pages (copper, aluminium, lead, zinc, tin, nickel); Android/iOS app; site counters for "CO2 avoided" and "millions of kWh saved"; B-Corp certification; BIR (Bureau of International Recycling) membership badge.
- Users quoted: managers, owners, purchasing managers — B2B recycling industry.

### Product E — Empower / Jörð.tech (collection networks, EPR, impact credentials)

Evidence layer: A for positioning; program- and module-level only.

- Site now framed as: Empower Foundation ("Formalising the informal sector to create traceable, inclusive, and impactful waste collection networks worldwide") powered by Jörð.tech ("The System of Material Intelligence for recycled-material value chains").
- Foundation mechanics: "Register and verify individual waste collectors with digital identities"; "digital infrastructure for real-time, immutable, data capture"; "Incentivise responsible waste management through premium payments"; "Ensure fair pricing and transparent payment through traceable transactions"; "Create direct market access to brands seeking verified social plastic"; "Generate verified environmental and social impact credentials"; build "collection points, sorting facilities, and training".
- Impact stats (2022–2025, vendor claims): 1.2m tons material registered; 356k transactions processed.
- Enterprise solutions (Jörð.tech nav): SMI Enterprise; EPR Compliance; Collect & Recycle; PRO Portfolio; Assurance Central.
- Knowledge hub topics: EPR, CSRD, PPWR, ESPR, Digital Product Passport, Recycled Content, EU Compliance Guide.
- Pilots referenced: plastic waste deposit system (BBC Reel), snus-box deposit pilot, clean-up dashboard. Chain-of-custody framing: "Every kilogram collected is logged, verified, and linked to a specific collector and location… chain of custody documentation brands need to make credible claims."

## Cross-product Comparison

| Dimension | Rheaply | Circular IQ | Circularise | ScrapAd | Empower/Jörð |
|---|---|---|---|---|---|
| Primary circular object | workplace assets (furniture, equipment) | product/material composition data | materials/components across n-tier chain | scrap / recyclable metal lots | collected recyclable material (kg) + collector identities |
| Operator/user | workplace, facilities, sustainability teams | corporate sustainability + consultants | manufacturer/brand compliance teams | scrap traders, recyclers, purchasers | collector-network orgs, brands, PROs |
| Core verbs | inventory → post → request/approve → transfer → measure impact | assess baseline → fill data gaps → compute indicators → report | collect declarations → maintain custody/mass balance → publish passport | list lot → negotiate → escrowed payment → logistics → delivery | register collectors → log kg → incentivize → certify impact |
| Money movement | optional (internal transfer / donation / sale) | none | none | central (negotiation + secured payment/deposits) | central (premium payments) |
| Logistics | optional | none | none | platform-managed | collection networks |
| Trust machinery | org admin, approvals, audit trails | vetted proxy-value database | auditable mass balance, permissioned disclosure | member verification, secured payments | collector digital identity, immutable logs |
| Circular outcome recorded | items exchanged, landfill diversion, carbon avoided | circularity indicators, ESRS E5-style reports | custody records, DPPs, claims | trades, CO2 avoided counters | kg registered, transactions, impact credentials |
| Regulatory anchor | none required | ESRS E5, GRI, ISO 59020, CTI | EU Battery Reg, ESPR, CRM Act, ELV, ISCC | none (market-driven) | EPR, PPWR, CSRD |

Cross-product commonalities (Evidence layer B unless noted):

- B1. All five manage **identified physical circular objects** (assets, material lots, collected material, or the materials inside products) — never abstract "sustainability" alone.
- B2. All five orient those objects toward **restorative loops** (reuse, resale, recycling, recovery, verified recycled content) — disposal appears only as the outcome to avoid or account for.
- B3. All five **record circular outcomes as evidence**: transactions/audit trails (Rheaply, ScrapAd), indicators/reports (Circular IQ), custody/passports (Circularise), registered kg/credentials (Jörð). The evidence object differs; the recording obligation is universal.
- B4. All five in practice connect **multiple parties** (org units, member organizations, n-tier suppliers, traders, collectors, brands). No sampled product is single-user.
- B5. All five carry some **trust/verification layer** appropriate to their pole.
- B6. All five surface **circularity/impact metrics** of some form.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Circular Economy Platform is a multi-party software system whose managed world is:

1. **Circular objects** — identified physical products, components, or material lots held by participants, carrying recoverable circular value (state, condition, composition, location/custody).
2. **Loop pathways** — the system represents or routes these objects toward restorative outcomes (reuse, redeployment, resale, recycling, recovery, verified circular claims); disposal is not the terminal success state.
3. **Recorded circular outcomes** — events that move or account for objects across loops (transfers, custody changes, recoveries, measured restorative flows) are recorded, forming the evidence base for circularity visibility.

Ask (per invariant): remove it → still the Type?

- Remove circular objects (only org-wide ESG metrics, no material/product objects) → Sustainability/ESG Management Platform. So (1) is definitional.
- Remove loop orientation (objects routed to disposal/treatment as the normal terminal state) → Waste Management Platform. So (2) is definitional.
- Remove outcome recording (listings/matching with no memory of what circulated) → a bulletin board, not a circular economy platform; no impact, no audit, no claims. So (3) is definitional.

Note: multi-party participation is near-universal (all 5 sampled) but a conceivable single-organization circularity tracker would still be recognizable; kept out of L0 deliberately (anti-overfitting).

### L1 — Common Mature Structure

Present across the sampled products (B), expected in mature modern products, not definitional:

- multi-party network with participant identities and verification (organizations, members, suppliers, traders, collectors)
- object catalog / listing & discovery (browse/search by material, condition, location, grade)
- transfer machinery (requests, approvals, matching, negotiation; payment where trading)
- circularity/impact metrics and reporting outputs (diversion, carbon avoided, indicators, credentials)
- audit/evidence trail behind every outcome claim
- data-quality machinery where data comes from others (proxy/reference values, supplier declarations, immutable logs)

### L2 — Variant / Optional Structure

- Product pole: internal asset reuse exchange | secondary-material trading marketplace | supply-chain traceability & DPP | circularity measurement & reporting | incentivized collection/EPR networks
- Regulatory context: EU regulation-driven (Battery Regulation, ESPR/PPWR, ESRS E5, EPR, ISCC) vs voluntary frameworks (CTI, GRI, ISO 59020) vs market-driven (scrap prices)
- Money & logistics depth: none → escrowed payments → platform-run logistics → deposit/premium incentive models
- Network openness: closed/internal (one organization) vs open external marketplace vs managed program network
- Object granularity: item-level assets vs material lots vs aggregated material flows
- Geography: EU-heavy compliance features vs global trading
- Delivery: standalone SaaS vs tool+consulting services hybrid vs program/foundation layer

### L3 — Vendor-specific (research notes only)

- Rheaply: module names Visibility / Circulate / Next Life; "3,400+ network partners"; impact-counter vocabulary (reuse moments); Intercom help-center structure; customer savings claims.
- Circular IQ: "CTI Tool" branding; WBCSD partnership; proxy-value database; €11,700/year starting price claim; app at app.ctitool.com.
- Circularise: Collect/Trace/Share suite names; compliance-map lead tool; specific regulation module list incl. EURO7 EVP and US Section 232; QR/data-carrier disclosure; Honda/Samsonite/Teijin case studies.
- ScrapAd: metal price pages; B-Corp + BIR badges; mobile app; 45+ countries claim; CO2/kWh counters; free registration for ad access.
- Empower/Jörð.tech: "System of Material Intelligence" branding; SMI module names (EPR Compliance, PRO Portfolio, Assurance Central); informal-collector digital identity program; BBC-documentaried deposit system; 1.2m tons / 356k transactions claims.

## Rejected Findings

- "CEP = reuse marketplace" — rejected; two of five poles have no marketplace at all.
- "CEP = blockchain traceability" — rejected; only immutable-log/QR language appears, blockchain is not universal or emphasized as necessary.
- "CEP must handle payments/logistics" — rejected; absent in measurement and traceability poles.
- "Digital Product Passports definitional" — rejected; regulation-driven variant (EU ESPR/Battery Regulation era).
- "ESRS E5/GRI reporting definitional" — rejected; only the measurement pole.
- "CEP = waste software" — rejected; none of the sampled products runs waste collection/disposal operations; disposal is the outcome they exist to avoid.

## Boundary Findings

- **vs Recycling Operations Management** (§21 sibling, unprocessed): that Type runs the recycler's own plant/operations (intake, processing, outputs). CEP is the circulation/visibility layer *between* holders. Discriminator: whose operations does the software run? If you remove cross-holder circulation and bind the software to one processing facility's operations, it becomes Recycling Operations Management.
- **vs Waste Management Platform**: waste software routes discarded material to collection/treatment; terminal state = disposed/processed. CEP's terminal success state = object re-entering use; disposal is the failure path being measured against. Remove the restorative orientation → Waste Management Platform.
- **vs Sustainability Management Platform / ESG Reporting** (§21 siblings): org-wide ESG measurement; circularity is one topic among many. CEP's managed world is the material loops themselves. The Circular IQ pole is the closest to this boundary — flagged in STATUS.md.
- **vs Carbon Accounting Platform** (processed 2026-09-07): unit of account = the organization's emissions (activity data × factors → inventory). CEP's unit of account = material objects/flows. Both feed ESG reports but do not converge into one Type.
- **vs Recommerce Platform** (processed 2026-09-07): brand-operated consumer resale of secondhand goods (trade-in → grade → branded resale surface → payout). CEP's exchange poles are organization-internal redeployment and B2B secondary-material trading; audience is business/organizational, surfaces are network/marketplace, and outcome accounting is circularity-oriented rather than brand-revenue-oriented.
- **vs Online Marketplace / Resale Marketplace**: the ScrapAd pole is marketplace-shaped. Distinguishing residue: goods carry secondary-material identity (grades, specs, verification) and the platform accounts circular outcomes. Strip those and it is a generic B2B marketplace — flagged in STATUS.md.
- **vs Inventory Management System**: Rheaply's inventory pole resembles asset inventory. Distinction: the registry exists to route items into reuse loops across parties and to account outcomes; strip the exchange/loop machinery and it collapses into fixed-asset/inventory software.

## Historical / Market-Sample Check

Ask: would older, regional, platform-native products still fit the L0?

- Pre-digital waste/by-product exchanges (catalog-based industrial exchanges), industrial symbiosis networks, university surplus/reuse catalogs, scrap-broker ledgers: they hold circular objects (by-product lots, surplus items), orient them to loops (find next user), and record outcomes (broker books, transfer records) — they satisfy L0 without any of the digital machinery (impact dashboards, passports, escrow). So L0 does not over-fit the current EU-compliance era. (Canonical inference — no direct fetch; marked C.)
- Conversely: a pure DPP data-sharing tool with no loop orientation would drift out of the Type toward supply-chain compliance software — a drift risk for the traceability pole.
- Conclusion: L0 survives the historical check; the sampled products describe the current market, not the timeless definition.

## Uncertainties

1. Whether the market will keep "circular economy platform" as one label or split into measure/trace/trade/reuse products. Treated here as one Type with pole variants; umbrella risk flagged.
2. Operational depth of Circular IQ (indicator formulas, scenario mechanics) — marketing pages only; no help center reachable.
3. ScrapAd escrow/dispute mechanics beyond homepage description — marketplace login-gated.
4. Jörð.tech enterprise modules (EPR Compliance, PRO Portfolio, Assurance Central) described at marketing level only.
5. Rheaply approval-workflow specifics — inferred from marketing copy + help-center collection titles, not article bodies.
6. Possible unsampled pole: waste-movement analytics/mapping (candidate source unreachable).

## Final Synthesis

The leaf is a real Application Type but umbrella-shaped: five distinct product poles share one minimal core. The canonical definition: **a multi-party platform whose defining core is (1) identified circular objects (products, components, material lots) held by participants, (2) loop pathways that route or evaluate them toward restorative outcomes rather than disposal, and (3) recorded circular outcomes that make circulation visible, auditable, and claimable.** Marketplaces, passports, indicator frameworks, payments, logistics, and incentive programs are standard capabilities or variants, not the definition. Boundary issues recorded: umbrella structure (pole fragmentation risk), Circular IQ pole vs Sustainability/ESG Management, ScrapAd pole vs Marketplace, plus processed-leaf contrasts (carbon accounting, recommerce).
