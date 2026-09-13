# Research Notes — Contact Discovery Platform

Research date: **2026-09-07**

---

## Research Goal

Understand what a Contact Discovery Platform actually is as an Application Type: what its unit of work is, how sourcing machinery works, what the deliverable is, and — critically — how it differs from the three already-processed sibling leaves of the same sales-data market family (Sales Data Enrichment Platform, Sales Intelligence Platform, Sales Prospecting Platform).

This pass carries a **joint-review obligation** recorded three times in STATUS.md Boundary Issues (sales-data-enrichment-platform, sales-intelligence-platform, and sales-prospecting-platform passes, all 2026-09-07): the sales-data family shares one external data substrate, vendors self-label the whole family "sales intelligence" (Cognism flagship line; Lusha home page), and vendor naming does not respect the directory split. The enrichment and SI passes ratified keep-both on "direction of the loop + primary job"; the prospecting pass ratified keep-both on "sourcing act vs surrounding workflow" and left the discovery seam explicitly open as "the softest seam in the family". This pass must take a position from the discovery side and discharge or restate that flag.

## Initial Boundary

Working hypothesis at start:

- **Is:** a sourcing application whose primary job is producing contact records (business people, commonly companies) that the customer organization does not yet hold — the customer states who to find (criteria and/or identity), the platform's external data supply yields matching records with verified reachability data (emails, direct dials), and the records are taken away into the customer's own tools.
- **Closest neighbors:** Sales Prospecting Platform (the surrounding outreach-preparation workflow — the open flag), Sales Data Enrichment Platform (completing records the customer already holds), Sales Intelligence Platform (decision support over a managed target population), Lead Generation Platform (§06, demand capture), CRM / Lead Management (system of record), Directory Application (entry lookup), Sales Engagement Platform (outreach execution), ABM Platform (marketing activation over target accounts).
- **Suspected taxonomy risk (carried from three prior passes):** "discovery" is also a capability inside every sibling product; the leaf may be a capability named as a Type. This pass must either ratify the leaf on a defensible primary job or record a capability/variant problem.

## Research Questions

1. What is the unit of work — the search? the individual record? the record set? What does the user walk away with?
2. What sourcing channels exist (database search, identity lookup, extension capture, URL/import sourcing, lookalike, AI-directed)?
3. What does the external data supply look like (owned database, provider aggregation, AI research), and what record families does it cover (people, companies)?
4. How does reachability data work — verification states, grades, teaser/previews, pay-on-yield vs pay-per-reveal economics?
5. How do results leave the platform (export, CRM/ATS sync, API, sequence handoff), and how does the platform prevent re-sourcing records the customer already has (exclusions, dedup vs previous downloads and synced records)?
6. What compliance machinery shapes the supply (regional exclusion toggles, suppression lists, opt-out, DNC)?
7. Where exactly are the seams vs enrichment, prospecting, SI, lead generation, CRM, directory applications, and sales engagement?
8. Historical check: do list-broker-era, printed-directory-era, and crowd-sourced-database-era realizations satisfy the definition, or is it over-fitted to the modern search-UI pattern?

## Representative Products

Selection rationale: the three prior passes repeatedly sampled Apollo, Lusha, Cognism, and Hunter (plus Clay, Bombora, LinkedIn Sales Navigator). To avoid a fourth pass over the same sample and to represent the **discovery-primary pole** properly, this pass samples four fresh products at that pole, with the family anchors carried from the sibling passes' research notes as cross-check evidence.

| Product | Pole / philosophy | Tier | Evidence |
|---|---|---|---|
| UpLead | Search-first B2B database ("B2B Database & Business Contact Data Provider"); accuracy-guarantee positioning; SMB/mid-market | Tier 1 help center (Intercom) + Tier 2 product pages | A (help center) + B (site) |
| RocketReach | Identity-lookup pole: search → per-person contact lookup; API-first; broad-market (sales, recruiting, healthcare) | Tier 1 API documentation (markdown-native) | A |
| Snov.io | SMB freemium all-in-one: discovery as the entry layer of an outreach suite; multi-channel LinkedIn sourcing | Tier 1 knowledge base + Tier 2 product pages | A (KB) + B (site) |
| ContactOut | Extension-led + search portal; dual audience (sales + recruiters); data-supply disclosure | Tier 2 product pages + FAQ | B |
| Carried anchors: Apollo, Hunter, Lusha, Cognism, Clay | Family context from the three sibling passes | — | carried, marked |

ZoomInfo was **not attempted** this pass: all four official domains returned 403 in the enrichment pass and again in the SI pass on the same date (2026-09-07); the prospecting pass also skipped it. Per the network-access rule the source stays abandoned; the enterprise owned-database pole is represented indirectly and no claims are made from it.

## Sources

**UpLead (Tier 1 unless noted)**
- Help center root: https://support.uplead.com/en/ — fetched 2026-09-07 (A)
- "How to Perform a Contact Search on UpLead" — https://support.uplead.com/en/articles/10682337 — fetched 2026-09-07 (A)
- "Exclusions in UpLead" — https://support.uplead.com/en/articles/13257586 — fetched 2026-09-07 (A)
- Lead Management collection index (24 articles: contact/company search, filters, intent, saved searches, lists, enrichment, CRM export, downloads, extension) — https://support.uplead.com/en/collections/11804439 — fetched 2026-09-07 (A, structure)
- Product pages: https://www.uplead.com/ , https://www.uplead.com/prospector/ — fetched 2026-09-07 (B, positioning)

**RocketReach (Tier 1)**
- API docs index: https://docs.rocketreach.co/llms.txt — fetched 2026-09-07 (A)
- People Search API — https://docs.rocketreach.co/reference/people-search-api.md — fetched 2026-09-07 (A)
- API root — https://rocketreach.co/api — fetched 2026-09-07 (A)

**Snov.io**
- Knowledge base: "How to use LinkedIn Search to find emails" — https://snov.io/knowledgebase/how-to-use-linkedin-search-to-find-emails/ — fetched 2026-09-07 (A)
- Home page / product structure — https://snov.io/ — fetched 2026-09-07 (B)
- https://snov.io/b2b-lead-finder — timed out (1 failure; abandoned per network rule)

**ContactOut (Tier 2)**
- Home page + FAQ — https://contactout.com/ — fetched 2026-09-07 (B)

**Carried from sibling passes (context, not new evidence)**
- research/sales-data-enrichment-platform.md, research/sales-intelligence-platform.md, research/sales-prospecting-platform.md — family framing, prior joint-review flags, Apollo/Hunter/Lusha/Cognism/Clay observations.

---

## Product Observations

Evidence layers: **A** = directly observed in an official source for that product; **B** = cross-product commonality / positioning-level; **C** = canonical inference.

### UpLead (evidence layer: A — help center; B — product pages)

- Positioning: "B2B Database & Business Contact Data Provider"; the discovery product pillar is literally named **Prospector** ("Search +200 million contacts with 95% data accuracy" — vendor numbers, kept here). Accuracy guarantee: "If we don't find the right email for your leads, we don't charge you"; "Friendly Credits — we'll refund you for bounces and poor data" (pay-on-yield economics).
- **Contact search workflow (help center, A):** access Contact Search → apply criteria via search bar + filters (name search with Includes/Exact match) → browse results → click a contact for detail with direct contact details → export (download specific number / selected / all) or save to a list within UpLead.
- **Filter families (A):** name/title (job title, job function, management level, contact skills); location (country/region/state/county/metro/city/zip, multiple locations); company (name, URL, URL-list upload, My Lists); industry (category, name, tags, SIC, NAICS); type (public/private/government/nonprofit; Fortune 100/500/1000); employees range; revenue range; technologies (technographics); funding range; year founded; social-links presence.
- **Facet filters (A):** filter options update dynamically with selections to prevent zero-result queries; display-column selection; contacts-per-company display cap (1–5 or all); "select records with phone/mobile numbers present"; sort by name/title; randomize.
- **Real-time verification (A):** "UpLead verifies emails in real-time"; "Anytime you export leads, we verify their emails for guaranteed accuracy"; AI-verified-as-you-search claim (B).
- **Saved searches (A)** — save parameters for reuse.
- **Exclusions (A — the most detailed dedup machinery observed):** exclude by keyword per field (contact name, company name, title, industry, company/contact city/state/zip); **Exclude EU/EEA contacts & companies** toggle ("commonly used for compliance or regional targeting"); upload exclusion lists (emails, company phones, company URLs); **Exclude Connected List Contacts** (Salesforce-connected lists — exclude contacts already matched and synced); **Exclude From Previous Downloads — by default all previous downloads are excluded automatically** unless disabled in profile settings; hard cap of 200,000 total excluded items (vendor number).
- **Adjacent pillars (B):** Data Enrichment (real-time CRM enrichment — the held-records direction, shipped as a separate pillar), Email Verification, Email Finder (by company/URL), Bulk Lookup, Chrome Extension ("capture leads as you browse the web"), Intent Data, API ("real-time lookup, enrichment, and intent signals"), done-for-you outbound service (commercial variant).
- Integrations (B): Salesforce, HubSpot, Pipedrive; Mailshake, Outreach, Reply; Zapier; CSV.

### RocketReach (evidence layer: A — API documentation)

- Self-description: "Email & Contact Lookup… search and retrieve contact info for 700M+ professionals and 60M+ companies" (vendor numbers; a second page says 35M companies — inconsistent, kept here only).
- **Two-stage search→lookup model (A — the cleanest documentation of the discovery economics):** "The result is always a list of possible matches, **without any contact info**. In order to retrieve contact information for someone in the list, please make a separate call to lookup that person." Search = criteria-driven candidate discovery; lookup = contact-data retrieval (the metered act). The lookup endpoint is labeled "Person Enrichment API" — vendor naming blurs discovery/enrichment again.
- **Search filter breadth (A):** name (with exact-match quoting and typo tolerance), keyword, current/previous/or-previous title, current/previous employer, company domain/website/email/ID, geo (with radius modifier), industry + NAICS/SIC codes, company size, revenue, funding min/max, intent topics (37,000 topics claim), job-posting signals (department + time window), news signals (25 categories + time window), department growth signals, job-change signal (company change / promotion, one-week/one-month/three-month windows), skills (AND/OR), degree, school, major, management levels, departments, years of experience, connections count, **email grade** (A/A-/B with professional-only/personal-only modifiers), **phone grade**, **contact method** (mobile / direct dial / office phone / personal email / work email, AND/OR logic), update_time (records updated since a date), healthcare vertical fields (health credentials, licenses, NPI numbers, specializations).
- **Ordering (A):** relevance / popularity ("decision makers, executives and managers… closer to the top") / score.
- **Teaser (A):** search results carry preview contact data (partial emails/phones, premium-phone availability flag) before lookup.
- **Suppression (A):** a `suppressed` flag marks profiles "blocked by a suppression list filter".
- **Delivery machinery (A):** bulk people lookup by criteria; async lookup with status endpoint + webhooks; company search/lookup endpoints; universal credits; **MCP server with Claude Code setup docs** (supply of the same data to AI agents).
- API-first posture: the UI "behaves similarly to the search in our UI" — the API documents the same loop the app runs.

### Snov.io (evidence layer: A — knowledge base; B — product pages)

- Positioning: "Find leads. Enrich them with emails & phone numbers. Send outreach campaigns" — discovery as the entry layer of an SMB outreach suite (finder tools + verifier + warmup + deliverability + drip/multichannel campaigns + light CRM).
- **Discovery channels (A + B):** Database Search (owned B2B database with filters); Email Finder (name + company → email); Bulk Email Finder; Phone Number Finder; LinkedIn Email Finder extension; **LinkedIn Search in-platform** with three modes (A): by specific profile URL, by LinkedIn filters (requires a connected LinkedIn account; keyword + connections degree + location + company), and by **importing a LinkedIn search-results URL** (paste the filtered LinkedIn search URL; the platform harvests the results) — plus **bulk file import** of LinkedIn profile links (CSV/TXT, one column, up to 20,000 lines — vendor number; supports standard and Sales Navigator profile links).
- **Capture without contact data (A):** the extension's "Save without emails" saves prospects with their LinkedIn URLs only — a record can exist before any reachability data is attached.
- **Pay-on-yield (A):** "You aren't charged for prospects with invalid emails or no emails found"; saving contacts without emails uses no credits; LinkedIn-only prospecting is unlimited under the LinkedIn Automation subscription.
- **Lists as destination (A):** every sourcing run requires selecting "an existing prospect list or create a new one where the new prospects will be added"; progress bar with stop-and-keep-partial behavior; error files downloadable for failed imports.
- Verification (B): 98% accuracy rate claim; regional posture (B): 12 locales including a Chinese site; GDPR/CCPA certifications marketed.

### ContactOut (evidence layer: B — product pages + FAQ)

- Identity: "Email Finder… Find emails & phone for 350M professionals" (vendor number); dual audience: "1.4M recruiters and sales reps" — sales AND recruiting use cases are first-class.
- **Surfaces (B):** Chrome extension ("get email and phone numbers for 75% of people online; add prospects to an email campaign in one click"); **Search Portal** ("instant access to 350M professionals from 40M companies with the right contact details"); API ("200M emails, 100M phone, 40M company records" updated hourly — vendor claims); MCP; AI personalizer.
- **Data attributes (B):** 20+ search points — job titles, companies, revenue, skills, locations, company size, departments, technologies used.
- **Sourcing-model disclosure (B, FAQ):** "sourced from publicly available professional information and partner datasets, for professional B2B use only"; "triple-verified with 99% confidence"; SOC 2; GDPR/CCPA compliant "with opt-out and suppression support".
- **Delivery (B, FAQ):** "feed into your CRM, ATS, sequencer, or AI agents" — ATS delivery confirms the recruiting-side record destination.
- Adjacent features (B): email campaigns, Gmail enrichment, cloud dialer, data enrichment (CRM/ATS completion of existing records — separate feature), ContactSheets; freemium credit model ("5 free credits daily"); famous-people/company SEO directory pages as marketing surfaces (not the product core).

### Carried family anchors (from sibling passes — context)

- **Apollo:** People/Company search over its own database with broad filter families; saved searches + subscription alerts; personas; lists with full action menus; extension; lookalikes (Suggested Leads); territories gating prospecting access; Data Health Center TAM view; enrichment pillar (Data Health Center, waterfall); sequences/dialer bundled. (enrichment + SI + prospecting passes, Tier 1)
- **Hunter:** Discover (company filters with include/exclude, "Companies similar to" lookalike, AI assistant filter generation); Domain Search / Email Finder heritage; verification statuses; "Follow before you reveal"; Leads as "soft CRM"; native sequences. (prospecting pass, Tier 1)
- **Lusha:** extension-first capture over LinkedIn/Sales Navigator/sites/CRM; workspace tables; Prospecting endpoint + Lookalike API; Search Layer vs Deep Intelligence; recruiting extension guide. (all three passes, Tier 1)
- **Cognism:** flagship line named "Sales Intelligence"; separate CRM Enrichment product line; DaaS; phone-verified data; compliance-first posture; five-step prospecting workflow narrative. (all three passes, Tier 2 only — help center unreachable)
- **Clay:** no owned contact database; aggregation of 150+ external providers + AI web research; waterfall across providers; Find/Audiences. (enrichment pass, Tier 2 + training docs)

---

## Cross-product Comparison

| Dimension | UpLead | RocketReach | Snov.io | ContactOut | Carried: Apollo / Hunter / Lusha / Cognism / Clay | Evidence |
|---|---|---|---|---|---|---|
| External contact-data supply | Owned DB (200M+ claim) | Owned DB (700M+ claim) | Owned DB + LinkedIn-derived | Owned DB + partner datasets ("publicly available professional information and partner datasets") | Owned DB (Apollo/Hunter/Lusha/Cognism); provider aggregation, no owned DB (Clay) | A×4 + carried → B |
| Criteria-driven search over the supply | Contact + company search, 50+ filters, facet filters | People/company search, very broad filter set incl. grades & signals | Database Search with filters; LinkedIn Search by filters | Search Portal, 20+ attributes | All ship database search (A in carried passes) | A×4 → B |
| Identity-driven lookup (find a specific person) | Name search (Includes/Exact) | Two-stage search→lookup by name/keyword/employer | Email Finder (name+company); profile-URL import | Extension reveal on a profile; email finder | Hunter Email Finder; Lusha extension reveal; Apollo LinkedIn-URL enrichment | A×3 + carried → B |
| In-context capture (extension) | Yes ("capture leads as you browse") | (API-first; extension exists per product pages — not directly observed) | Yes (LI Prospect Finder; "Save without emails") | Yes (flagship surface) | Apollo/Hunter/Lusha/Cognism all ship extensions (A in carried passes) | A×3 + carried → B |
| Net-new direction (records the customer didn't hold) | Yes — plus default exclusion of previously downloaded records | Yes — search yields candidates; lookup yields contact data | Yes — results land in prospect lists | Yes — "target and reach the right buyers" | Yes — sourcing act documented in all carried passes | A×4 → B |
| Reachability data as the decisive output | Verified emails + mobile/direct dials; real-time verification on export | Emails/phones with grades; teaser previews; contact-method filters | Verified emails + phones; "not charged for no/invalid emails" | Verified emails + direct dials; triple-verified claim | Verified contact data is the family's core commodity (carried A) | A×4 → B |
| Verification machinery | Real-time verification; accuracy guarantee; refunds for bounces | Email/phone grades (A/A-/B); revalidation on lookup | 98% claim; verifier tooling in-suite | Triple-verified 99% claim | Verification states across all carried products | A×3 + B → B |
| Search unmetered / yield metered | Credits on leads; refunds for bad data | Search returns no contact info; lookup consumes credits | No credits for saves without emails or failed finds | 5 free credits daily; credits on reveal | Hunter free-search/paid-reveal; Apollo email credits (carried A) | A×4 → B |
| Dedup vs records the customer already has | Exclusions: previous downloads (default ON), Salesforce-connected lists, uploaded lists, keyword excludes | Suppression list filter | "Skip profiles already in your lists" | Suppression support (FAQ) | Hunter "hide already saved"; Apollo saved-companies exclusion (carried A) | A×4 → B |
| Compliance shaping of the supply | EU/EEA exclusion toggle | Suppression lists | GDPR/CCPA; 12 locales | GDPR/CCPA opt-out + suppression; "professional B2B use only" | Cognism DNC Europe; Lusha certifications (carried B) | A×2 + B → B |
| Lists as containers for the yield | Save to list; download verified lists | (API returns result sets; lists in app not directly observed) | Prospect lists required as destination | (campaign import) | Lists first-class in Apollo/Hunter/Lusha (carried A) | A×3 + carried → B |
| Delivery out | CSV; CRM (Salesforce/HubSpot/Pipedrive); outreach tools (Mailshake/Outreach/Reply); Zapier; API | API (search/lookup/bulk/webhooks); MCP | CRM sync; campaigns; API; MCP | CRM/ATS/sequencer/AI agents; API; MCP | CRM sync/export/sequences across carried products | A×4 → B |
| Lookalike / expansion | (not directly observed) | (not directly observed) | (not directly observed) | (not directly observed) | Hunter "Companies similar to"; Lusha Lookalike API; Apollo Suggested Leads (carried A) | carried → B (not promoted to core) |
| Signals as search filters | Intent Data pillar | Intent topics, job-posting/news/growth/job-change signals | (not directly observed) | (not directly observed) | Buying intent at Apollo; signals at Lusha/Cognism (carried) | A×2 + carried → B |
| AI assistance | AI-verified-as-you-search claim | MCP + AI-agent supply; embedding query param | "Discover prospects with AI"; AI search | AI personalizer; MCP | AI list building across carried products | A×2 + B → B |
| Audience beyond sales | (sales-centric) | Healthcare vertical (NPI/credentials); recruiting usage | Recruiting use cases (positioning) | Recruiters first-class; ATS delivery | Lusha recruiting guide (carried A) | A×2 + B → B |
| Suite bundling around discovery | Enrichment + verification + intent + DFY outbound | (lookup API + credits; app) | Verifier + warmup + campaigns + light CRM | Campaigns + dialer + enrichment + ContactSheets | Apollo sequences/dialer; Hunter sequences; Lusha Engage (carried A) | A×4 → B |

---

## Canonical Abstraction

### L0 — Defining Invariant (must stay minimal)

**A Contact Discovery Platform is a sourcing application whose defining core is exactly three structures:**

1. **An external supply of business contact records the customer does not own** — a maintained body of structured records about business people (and commonly companies), carrying identity attributes (name, title, employer, location) and reachability data (emails, direct dials), held by the platform as its defining asset: owned proprietary database, aggregated provider network, or AI-researched compilation. *(Remove it → list building/segmentation over records the organization already owns — a CRM capability; a filter UI over nothing.)*
2. **The sourcing act as the primary job: criteria- or identity-driven yield of net-new records** — the customer expresses who to find (attribute filters, a specific name/company, a profile URL, an imported list of identities, a lookalike seed, or a natural-language/AI description) and the platform produces matching records the customer did not previously hold. *(Remove it → enrichment, which starts from records the customer holds; remove the criteria/identity machinery → a static purchased list file, which is the historical fulfillment form of the same act.)*
3. **The yielded record set with verified reachability data as the unit of value, taken away for external use** — the deliverable is the records themselves (with contact details), exported/synced/pushed into the customer's own tools (CRM, ATS, sequencer, spreadsheets, campaigns); the platform does not run the outreach, own the relationships, or deliver selling decisions. *(Remove the record delivery → a directory lookup utility; remove the reachability data → market mapping, not contact discovery; make the deliverable a decision → Sales Intelligence; make the deliverable a standing worked list → Sales Prospecting.)*

All three are necessary. The abstraction is layer C; each structure is directly observed in 4/4 fresh samples and in all carried anchors (layer B).

Not in L0: filter breadth, verification grades, credits, extensions, lookalikes, saved searches, alerts, signals/intent, AI, MCP, compliance certifications, team machinery, lists as standing workflow, sequences, enrichment of held records.

### Removal Tests (L0 validation)

1. **Remove the external supply** (keep search UI + delivery): the product becomes a query surface over the customer's own records — CRM segmentation. The net-new direction is the family's agreed discriminator from the enrichment pass. **Supply survives.**
2. **Remove the sourcing act as primary job** (keep supply + delivery, but the customer only completes records it already holds): the product becomes a Sales Data Enrichment Platform — the ratified sibling. **Sourcing-act survives.**
3. **Remove the record-set deliverable** (keep supply + sourcing, but deliver decisions/alerts/context instead): the product becomes a Sales Intelligence Platform. **Record deliverable survives.**
4. **Remove the standing-workflow exclusion** — i.e., confirm the L0 does NOT require a maintained prospect list, qualification stages, or handoff-into-outreach machinery: RocketReach's search→lookup→export loop, ContactOut's extension→campaign flow, and Snov's finder→list→export flow all satisfy the L0 with lists as transient containers, not standing workflow objects. The prospecting leaf's L0 structure 1 (standing list) and structure 3 (preparation purpose) are strictly stronger. **Act-vs-workflow discriminator holds.**

### Historical / Market-Sample Check (per §24)

- **List-broker / mailing-list era:** the customer submits criteria on an order form; the broker compiles names + postal addresses/phones from its compiled sources and delivers a list file. This satisfies all three structures: external supply (the broker's compilation), criteria-driven sourcing (the order form), record-set output with reachability data taken away. The self-serve search UI is a realization, not the definition. ✓
- **Printed trade/phone directories + D&B reference volumes:** the directory is the external supply; the discovery act is extracting matching entries into a card box or prospect file. This also anchors the boundary vs Directory Application: the directory is the substrate; contact discovery is the act of sourcing record sets from such a substrate for organizational work. ✓
- **Crowd-sourced contact-database era (Jigsaw → Data.com class):** search + credits + export without AI, intent, extensions, or MCP. ✓
- **Platform-native:** CRM-native "find new leads" features operate over owned records or are capability realizations of the same external-supply pattern; the net-new-vs-held test holds. ✓
- Conclusion: the definition is not over-fitted to the modern database-search UI.

### L1 — Common Mature Structure

- **Filter families over people + company records**: role/title/function/seniority, geography (down to postal code, multi-region), industry (with standard code systems), company size/revenue, funding, technology usage (technographics), founding year.
- **Verification machinery**: verification states/grades on emails and phones; real-time verification at reveal or export; accuracy guarantees with refunds/credits-back for bad data.
- **Search-unmetered / yield-metered economics**: browsing and filtering typically free; credits consumed on reveal/lookup/export; pay-on-yield (no charge for no-find or invalid data) as the documented pattern.
- **Dedup/exclusion machinery**: exclusion of previously downloaded records (in one sampled product by default), exclusion of CRM-synced records, uploaded exclusion lists, keyword excludes, suppression-list filtering.
- **Saved searches** for reuse; **alerts on new matches** in the family's fuller implementations (carried).
- **Browser extension** for in-context capture over professional networks and websites, including capture without contact data.
- **Lists as containers** for the yield (existing or created at save time); bulk operations; downloads with verification applied.
- **Delivery machinery**: CSV export, native CRM sync, outreach-tool handoff, ATS delivery (recruiting pole), REST API (search + lookup + bulk), webhooks, MCP/AI-agent supply.
- **Teasers/previews** of contact data before the metered reveal; ordering that surfaces decision-makers.
- **Compliance posture**: regional exclusion toggles, suppression/opt-out support, certification programs; "professional B2B use only" scoping.
- **AI assistance**: natural-language search, AI verification, AI-agent supply (MCP-class).
- **Team machinery**: seats, shared lists, roles (family-level; thin at the discovery-primary pole).

### L2 — Variant / Optional Structure

- **Supply model**: owned proprietary database vs provider-network aggregation (no owned DB) vs AI-researched compilation vs hybrid.
- **Audience extension**: sales-centric vs recruiting-first-class (ATS delivery, healthcare credentials/NPI vertical) vs multi-use (fundraising, event invitation lists).
- **Suite bundling**: standalone discovery tool vs discovery as the entry pillar of an outreach suite (verification, warmup, campaigns, light CRM) vs data-suite member (enrichment + DaaS siblings).
- **Regional/compliance orientation**: global volume posture vs EU/compliance-led (phone-verified regional data, DNC coverage — carried).
- **Customer tier**: freemium self-serve SMB (daily free credits) vs sales-led mid-market vs enterprise packages.
- **Reachability emphasis**: email-led vs phone/direct-dial-led vs both; personal vs work email distinction.
- **Record-family emphasis**: people-led vs dual people+companies.
- **Commercial posture**: pay-on-yield vs pay-per-reveal vs subscription + credits; done-for-you outbound as a service variant (one sampled product).

### L3 — Vendor-specific (kept in these notes only)

- **UpLead**: 95% accuracy guarantee mechanics; "Friendly Credits" refunds; default-exclude-previous-downloads; 200,000 exclusion-item cap; Fortune 100/500/1000 filter; facet contacts-per-company display cap; EU/EEA one-toggle exclusion; done-for-you outbound service; 200M+/160M inconsistent contact-count claims across pages.
- **RocketReach**: two-stage search→lookup API separation with "no contact info in search results"; teaser schema; email/phone grades with professional/personal modifiers; popularity ordering; suppression flag; healthcare NPI/credential vertical; universal credits; MCP + Claude Code setup docs; 700M/60M vs 35M inconsistent company-count claims; lookup endpoint labeled "Person Enrichment API".
- **Snov.io**: LinkedIn-search-URL import mode; bulk profile-link import (CSV/TXT, 20,000-line cap, 10 MB); "Save without emails"; LinkedIn Automation credit bundles (50 credits/100 recipients); 12-locale footprint incl. Chinese site; 98% verifier claim.
- **ContactOut**: 5-free-daily-credits freemium; hourly-refresh claim; triple-verified 99% claim; "75% of people online" claim; ContactSheets; Gmail enrichment; famous-people/company SEO directories; 350M/40M/200M/100M scale claims.
- **Carried**: Apollo Data Health Center TAM, waterfall ordering invariant, territories; Hunter follow-before-reveal, status taxonomy; Lusha Search Layer/Deep Intelligence split, MCP docs; Cognism 30-day refresh claim, DNC Europe; Clay pay-per-found, provider marketplace counts.

## Vendor-specific Findings

See L3. None promoted into the final document. Vendor scale numbers, caps, guarantee percentages, and refresh cadences stay here.

## Rejected Findings

- **"Contact discovery = having a large proprietary contact database"** — rejected as definitional. Clay (carried) satisfies the sourcing act with no owned database (provider aggregation + AI research); ContactOut discloses partner-dataset sourcing. The invariant is the external supply, whatever its compilation model.
- **"Contact discovery = the whole prospecting workflow"** — rejected. That is the ratified sibling leaf; discovery-primary realizations exist with lists as transient containers and no qualification/handoff machinery (RocketReach, ContactOut).
- **"Contact discovery = intent data / signals"** — rejected. Signals appear as search filters and timing aids; the decision-delivery loop belongs to Sales Intelligence (ratified).
- **"Verified-email accuracy guarantees are definitional"** — rejected. Verification machinery is common (L1); the guarantee-with-refund mechanics are vendor-specific commercial posture (L3).
- **"Discovery is inherently LinkedIn scraping"** — rejected. Extension capture is one sourcing channel among several; owned-database search and identity lookup are at least as central in the sampled set.
- **"AI search is the new core"** — rejected; era-typical across samples; every documented workflow remains fully executable manually.

## Boundary Findings

1. **vs Sales Prospecting Platform — the open family flag, DISCHARGED from this side.** Position ratified: **keep-both** on the act-vs-workflow discriminator proposed by the prospecting pass. Contact discovery names the **sourcing act as a product's primary job** (external supply + criteria/identity-driven yield of net-new records + record-set delivery; use-agnostic — sales, recruiting, list building); prospecting names the **surrounding outreach-preparation workflow** (standing prospect list worked over time + qualification/prioritization + handoff into the outbound motion as the purpose; sales-specific). Evidence: discovery-primary realizations exist where list/qualification/handoff machinery is minimal or transient (RocketReach search→lookup→export; ContactOut extension→campaign; Snov finder→list→export), while the prospecting leaf's own L0 requires the standing list and the preparation purpose — strictly stronger structures. **Overlap zone documented**: every prospecting product ships discovery as its sourcing step; discovery products commonly add lists (as containers), CRM export, and sometimes light sequences (Snov); vendor naming blurs the seam in both directions (UpLead names its discovery pillar "Prospector"; RocketReach labels its lookup endpoint "Person Enrichment API"). The directory split is by primary job, not by vendor label. No directory restructuring performed.
2. **vs Sales Data Enrichment Platform — confirmed** (flag from the enrichment pass already ratified there and in the SI/prospecting passes): loop direction. Discovery starts from the market and yields records the customer does not hold; enrichment starts from records the customer holds and completes them (match-and-append write-back). Same vendors ship both as separate pillars (UpLead Prospector vs Data Enrichment; ContactOut search vs data-enrichment feature; Cognism Sales Intelligence vs CRM Enrichment lines). Keep-both.
3. **vs Sales Intelligence Platform — confirmed** (ratified in the SI pass): unit of value. Discovery delivers records (who exists + how to reach them); SI delivers selling decisions over a managed target population (whom/when/why + context). Signals appear on both sides as filters (documented overlap zone). Keep-both.
4. **vs Lead Generation Platform (§06)** — direction of the population: discovery sources seller-chosen targets from an external supply; lead generation captures buyer-initiated demand (forms, ads, content). Different populations, different machinery.
5. **vs CRM / Lead Management Platform** — the CRM is the system of record for owned relationships and pipeline; discovery sources from beyond the org's records and hands records into the CRM. CRM list building over owned records is excluded by the net-new direction. Lead management progresses captured/inbound leads; discovery operates before any relationship exists.
6. **vs Directory Application / people-search utilities** — a directory is a per-lookup reference surface over standing entity records (find one business/person; consumer/utility posture; no organizational workflow, export machinery, or team seats). Discovery is organizational sourcing of record sets with export/handoff, verification, dedup, and supply-scale machinery. The seam is soft: lookup-style products (RocketReach, ContactOut) straddle it with consumer-style search surfaces; the org-workflow + delivery + supply machinery is the discriminator. Flagged as a soft seam, both Types stand.
7. **vs Sales Engagement Platform / Outreach Sequencing Platform** — sourcing vs execution: discovery ends at the record handoff; the engagement platform owns per-prospect outreach programs. Snov.io bundles both (packaging variant, as recorded in the SEP/prospecting passes).
8. **vs ABM Platform** — target-account selection overlaps; ABM orchestrates marketing activation and measurement over named accounts; discovery equips individual users to source people/records. Different user, different machinery.
9. **Family-level note (closes the three-pass joint review):** the sales-data family (enrichment / contact discovery / sales intelligence / sales prospecting) shares one external data substrate and vendors bundle all four jobs under overlapping labels ("sales intelligence", "prospector", "enrichment"); the directory keeps four leaves distinguished by **primary job** (complete held records / source net-new records / deliver selling decisions / run the outreach-preparation workflow). All four pairwise flags are now discharged or confirmed from both sides. Capability-vs-Type overlap zone documented; no taxonomy change proposed.

## Uncertainties

- **ZoomInfo pole**: never directly researched (403 across the enrichment and SI passes; not attempted this pass per the network rule). The enterprise owned-database pole is represented indirectly (competitor-comparison pages published by sampled vendors). No claims made.
- **Cognism**: remains positioning-level only (help center unreachable in three prior passes; not retried). Its discovery-side mechanics are not asserted.
- **RocketReach app-side surfaces** (lists, saved searches, team features) were observed via API documentation only; the API "behaves similarly" to the UI per the docs, but app-specific behaviors were not directly verified.
- **UpLead company-search and downloads articles** were read at collection-index level; the two fetched articles (contact search, exclusions) carry the load. Company-search specifics beyond the filter list are not asserted.
- **Snov.io B2B lead finder page** timed out (1 failure; abandoned); its database-search filter specifics come from the product page and KB cross-references, not a dedicated article.
- **Lookalike/expansion at the discovery-primary pole**: not directly observed in any fresh sample (carried evidence only: Hunter, Lusha, Apollo). Kept out of the defining core; listed as family-level common machinery.
- **Whether "default exclusion of previous downloads" is industry-wide**: directly observed at UpLead only; dedup machinery itself is cross-product, but the default-on behavior is treated as product-specific.
- Exact credit prices, list-size caps, refresh intervals, and accuracy percentages are vendor numbers kept in research notes only.

## Final Synthesis

A Contact Discovery Platform is defined by three structures: **an external supply of business contact records the customer does not own** (owned database, provider aggregation, or AI-researched compilation), **the sourcing act as the primary job** (criteria- or identity-driven yield of net-new records — database search, identity lookup, in-context capture, URL/import sourcing, lookalike, AI-directed), and **the yielded record set with verified reachability data as the unit of value, taken away into the customer's own tools** (export, CRM/ATS sync, API, campaign import). The Type is use-agnostic (sales, recruiting, list building) and deliberately ends at the record handoff. The three-pass family joint review is discharged from this side: keep-both vs prospecting on the act-vs-workflow discriminator, with the overlap zone documented; enrichment (held records) and SI (selling decisions) seams confirmed under the family's primary-job split. Historical check passed: list-broker, printed-directory, and crowd-sourced-database eras satisfy the core, so the definition is not over-fitted to the modern search-UI pattern.
