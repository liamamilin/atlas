# Research Notes — Sales Prospecting Platform

Research date: **2026-09-07**

---

## Research Goal

Understand what a Sales Prospecting Platform actually is as an Application Type: what objects exist inside it, what the prospecting workflow looks like end to end, where the work starts and where it deliberately ends, and — critically — how it differs from the three already-processed sibling leaves of the same market family (Sales Data Enrichment Platform, Sales Intelligence Platform, Sales Engagement / Outreach Sequencing Platform) and from Contact Discovery Platform (unprocessed sibling, softest seam in the family).

This pass also carries a **joint-review obligation** recorded twice in STATUS.md Boundary Issues (sales-data-enrichment-platform pass 2026-09-07; sales-intelligence-platform pass 2026-09-07): the sales-data family (enrichment / contact discovery / sales intelligence / sales prospecting) shares one external data substrate, vendors self-label the whole family "sales intelligence" (Cognism flagship line; Lusha home page), and vendor naming does not respect the directory split. The enrichment and SI passes adopted "direction of the loop + primary job" as the family discriminator and left the discovery/prospecting flags open. This pass must take a position from the prospecting side and discharge or restate those flags.

## Initial Boundary

- **What this Type probably is:** the seller-side workflow application for building outbound target populations — sourcing prospect records (companies/people) the organization does not yet have, organizing them into maintained lists, qualifying/completing them, and handing them into the outbound motion (CRM, sequences, dialer, exports).
- **Prior-pass pre-agreed framing:** the sales-intelligence pass defined prospecting as "the outreach-preparation workflow (build lists → find contacts → hand to engagement)"; the enrichment pass defined prospecting as the "broader workflow" of which enrichment is one data step; the sales-engagement pass defined prospecting tools as "upstream feeders. They find and enrich contacts; the SEP contacts them." This pass must confirm or refine that framing from direct product evidence.
- **Nearest neighbors:** Contact Discovery Platform (sibling, unprocessed), Sales Data Enrichment Platform (processed), Sales Intelligence Platform (processed), Sales Engagement Platform / Outreach Sequencing Platform (processed), CRM / Lead Management Platform, Lead Generation Platform (§06), ABM Platform, Directory Application.
- **Suspected taxonomy risk (carried from two prior passes):** the discovery/prospecting seam may be one workflow split into two directory leaves; needs an explicit position and a flagged recommendation, not a silent merge.

## Research Questions

1. What is the unit of work — the search? the list? the individual prospect record?
2. How do prospect records get sourced (database search, extension capture, import, lookalike, AI)?
3. How are sourced prospects organized and maintained over time (lists, statuses, tags, dedup, assignment)?
4. How does the platform prepare prospects for outreach (contact data, verification, enrichment, prioritization)?
5. Where exactly does the platform end — what is the handoff, and what does it hand off to?
6. What role do signals/intent/saved-search alerts play vs. the SI Type's decision loop?
7. What team/territory/permission machinery exists at the org level?
8. Where are the exact seams vs enrichment, discovery, SI, SEP, CRM, Lead Generation, ABM, Directory?

## Representative Products

Selected for market representativeness + different product philosophies + different customer tiers:

| Product | Pole | Tier | Evidence level |
|---|---|---|---|
| Apollo.io | data-bundled all-in-one platform (database + prospecting + engagement + deals in one product) | SMB / mid-market | Tier-1 knowledge base, fully reachable |
| Hunter.io | domain-first, email-centric narrow pole (database + Leads "soft CRM" + native sequences) | SMB / self-serve | Tier-1 help center, fully reachable |
| Lusha | extension-first freemium pole (browser capture over LinkedIn/sites + workspace tables) | SMB / mid-market | Tier-1 docs portal (new Knowledge Hub) + Tier-2 site |
| Cognism | EMEA / compliance-led database pole (phone-verified data, DNC coverage, enterprise posture) | Enterprise / mid-market | Tier-2 product pages only (help center timed out in two prior passes; not retried) |

ZoomInfo was not attempted: all four official domains returned 403 in the enrichment pass and again in the SI pass on the same date (2026-09-07). Per the network-access rule the source was abandoned; the enterprise owned-database pole is represented indirectly and no claims are made from it.

## Sources

**Apollo (Tier 1)**
- Knowledge base root: https://knowledge.apollo.io/
- "How to Prospect in Apollo": https://knowledge.apollo.io/hc/en-us/articles/27155177775885
- "Create and Use a List": https://knowledge.apollo.io/hc/en-us/articles/4409728608525
- "Search and Prospect" category structure (Search for People/Companies; Save/Share/Set Alerts for Searches; Personas; Buying Intent; Suggested Leads; Record Management; CSV import/export; Territories)
- Developer docs root: https://docs.apollo.io/ (people/company search, enrichment, convert-to-contact endpoints)

**Hunter (Tier 1)**
- Help center root: https://help.hunter.io/
- "Hunter Leads overview": https://help.hunter.io/en/articles/9503647
- "Find companies using Hunter Discover": https://help.hunter.io/en/articles/9123069
- "How to save leads or companies in Hunter": https://help.hunter.io/en/articles/9492140
- "Use filters to target specific leads for your email sequence": https://help.hunter.io/en/articles/9497708

**Lusha (Tier 1 docs + Tier 2 site)**
- Knowledge Hub root: https://docs.lusha.com/ (Search Layer; Deep Intelligence; Workspace AI table building; Extension; Engage & Sequences; Lookalike API; Prospecting endpoint)
- "Getting started with Lusha's extension": https://docs.lusha.com/user-guide/extension/getting-started-with-lushas-extension
- Home page (positioning): https://www.lusha.com/

**Cognism (Tier 2 — marketing/product pages only)**
- Home page: https://www.cognism.com/
- Sales Intelligence product page: https://www.cognism.com/sales-intelligence
- Sourcing limitation: help.cognism.com was not reachable in the enrichment and SI passes on 2026-09-07 and was not retried here. All Cognism-specific claims in these notes are positioning-level and marked accordingly.

**Carried from sibling passes (context, not new evidence):**
- research/sales-data-enrichment-platform.md, research/sales-intelligence-platform.md, research/sales-engagement-platform.md, research/outreach-sequencing-platform.md — family framing, prior joint-review flags.

---

## Product Observations

Evidence layers: **A** = directly observed in official source for that product; **B** = cross-product commonality; **C** = canonical inference.

### Apollo.io — "How to Prospect in Apollo" (KB, updated 2026-02-03), "Create and Use a List" (KB, updated 2026-07-28), Search and Prospect category, developer docs

Key observations (A):

- The KB defines the prospector's job as: know exactly who each key player is, find their contact information, develop a plan to connect — i.e., preparation for outreach, distinct from the outreach itself.
- Vendor-scale claim on the KB page: "over 275 million contacts, more than 73 million accounts, and over 2 million data contributors" (vendor number — kept here, not in the final document).
- Six-step prospecting checklist: (1) ICP + personas → (2) save searches with alerts + build lists → (3) TAM via Data Health Center → (4) research contacts/accounts → (5) lead scoring models → (6) Chrome extension.
- **Search** is the sourcing engine: filter families include personas, buying intent, keywords, technologies, job postings, fundings; results update live as filters apply.
- **Saved searches + alerts**: "Save search" → "Search Subscription Alerts" with a selectable frequency; later, "Saved searches" → "Net New" tab shows prospects newly matching the criteria.
- **Lists** are first-class: "Lists allow you to consolidate related people and companies in a common location so you can easily prospect and engage." Created from search results ("Add to list"), from the Lists hub, or via CSV upload. List actions enumerate the workflow: add/remove members, add to sequence, find people at companies, AI research, assign owner, email, enrich, set stage, export CSV, export to CRM, custom fields, tasks, delete or merge duplicates. Lists are visible organization-wide (created-by filter for Team).
- **Handoff is explicit**: from search results — "Save them to a list … Send them an email or enroll them in a sequence … Enrich them … Sync them to your CRM … Export them to a CSV file."
- **Data Health Center**: after connecting a CRM, shows "remaining available target addressable market (TAM)" across personas and account segments — a market-gap view over the customer's own coverage.
- **Research surfaces**: contact profile (contact info, company info, insights, activity, signals, tasks); account profile (overview, "Recommended new prospects" inside the account, insights, activity, signals).
- **Scoring**: AI-powered auto-scores from historical wins + manual scoring models with point weights; scores usable as search filters. Stages maintained manually, via plays, or CRM sync.
- **Extension**: works "across the internet" (websites, company pages), Gmail, Google Calendar, and inside Salesforce/HubSpot.
- API surface (developer docs): people/company search, enrichment, mobile phone retrieval, waterfall enrichment, "convert people to contacts", LinkedIn profile retrieval — programmatic forms of the same sourcing/record-creation loop.
- Org machinery: "Create Territories to Control Prospecting Access" — territories gate which users may prospect which market slices.

### Hunter.io — Help center (Leads, Discover, save-leads, sequence-targeting articles)

Key observations (A):

- Self-describes the Leads section as "a **soft CRM**": save leads in Hunter or import them from a file; "manage all of your prospects, enrich them, verify them and keep them organized in different lists."
- **A lead is "a potential contact for you and your organization."** People leads + company leads are parallel record families.
- **List machinery**: static lists ("don't change") vs dynamic lists ("rule-based or filter-driven views … update automatically whenever a lead matches (or stops matching)"); folders; favorites; uncategorized; "Save as list" from any selection; CSV/TXT import with column mapping, destination list, enrich-on-import, verify-on-import, find-missing-emails, and duplicate handling preferences.
- **Sourcing channels enumerated**: (1) automatic save on reveal in Discover / Domain Search / Email Finder / Find Similar; (2) browser extension save with destination list; (3) manual lead creation (email, or name + company); (4) file import; (5) save companies from Discover for later email discovery.
- **Discover** (database search): company filters with Include/Exclude semantics (name, lookalike "Companies similar to", HQ location, industry, size, type, year founded, keywords, technologies, job openings, funding, saved-companies exclusion); AI Assistant turns a plain-language audience description into filters; saved searches; company profiles with email tabs, People/Decision Makers/Generic filters, verification-status filters, phone/full-name filters, "hide already saved" dedup filters; bulk "Find all people" and "Reveal All" with credit-cost preview.
- **Credits**: searching is free; credits are consumed on reveal (email addresses). Bulk limits differ by plan (vendor numbers — kept here).
- **Verification**: statuses enumerated (Valid / Accept-all / Unknown / Webmail / Disposable / Not verified / Invalid); automatic verification on add (configurable); paid plans get automatic monthly re-verification of previously verified leads; verification-status filtering explicitly framed as bounce-risk reduction.
- **Signals**: company profiles have a Signals tab (new job openings, newly found emails); "Follow this company" for timing outreach; framed as "Follow before you reveal" to time outreach before spending credits.
- **Lookalikes**: "Companies similar to" filter; "Find similar leads (lookalikes)" — expand lists from best existing leads.
- **Handoff into native sequences**: filter leads (job title, sending status, company, verification, tags) → "Add to a sequence" / "Create a new sequence" — from the Leads section or from inside a sequence's Audience section ("From leads"). Sending-status filter has "Never contacted" as default to avoid re-contacting. CRM sync via native integrations automates lead sync.
- Duplicate flagging: on save, alert if the lead exists elsewhere in the account; dot indicators both ways.

### Lusha — docs.lusha.com Knowledge Hub (extension guide, hub structure) + lusha.com home

Key observations:

- **Positioning (Tier 2, A at positioning level)**: "Lusha is the B2B data and intelligence layer for GTM teams and AI agents"; two data layers — "Search Layer" (universal verified contacts/companies/signals) and "Deep Intelligence" (scoring & recommendations tailored to the business). Home-page prompt: "Ask Lusha to … describe the list you want to build / find my best leads for today."
- **Extension (Tier 1, A)**: "reveal verified contact details directly from LinkedIn profiles, Sales Navigator, company websites, and your CRM — without leaving the page." After revealing: **save to a table** (existing or new, optional tag), **export to CRM** (record type Lead/Contact/Account), **add to a sequence** (Engage; contact count cap per add — vendor detail), or view later in the Activity tab. "Wishlist: saving contacts with no available data" — a lead can be saved even when data is unavailable (explicit capture-without-data capability). Job-change indicator appears for recent role changes. Extension works inside Salesforce/HubSpot/Pipedrive for enrichment-in-place. "Lusha Everywhere" extends the extension beyond LinkedIn.
- **Platform structure (Tier 1, A at hub level)**: Workspace with "AI-powered table building"; Prospecting dashboard ("Lusha Prospecting Platform" at /prospecting/contacts); Engage & Sequences; CRM integrations; team management with roles/permissions; Lookalike API ("find similar companies and contacts"); Prospecting endpoint in the API; billing/credits system; recruiting-specific extension guide ("Lusha extension for recruiters") — adjacent-audience reuse.
- **Compliance posture (Tier 2)**: GDPR/CCPA/ISO/SOC certifications marketed; recruiting use case named in FAQ.
- Lusha markets "Outbound", "Lookalikes", "Territories", "ICP scoring" as solution pages (Tier 2, positioning level).

### Cognism — cognism.com + /sales-intelligence (Tier 2 only)

Key observations (positioning level; no help-center access):

- Headline frames the prospecting loop directly: "Turn your market into a **list** of the accounts and contacts that matter."
- "How Cognism works" is a five-step prospecting workflow: **01/ Build your target lists & persona** (web app, precision segmentation, personas) → **02/ Standardise best practices** ("Assign target companies and personas to your chosen teams") → **03/ Discover new opportunities** ("The browser extension combines buying signals with quality contact data, and works over LinkedIn and websites") → **04/ Accelerate outreach with AI** ("AI Search … searching, preparing and dialling faster") → **05/ Export and action, fast** ("Integrate with leading CRM or sales engagement tools").
- Product pillars: Sales Intelligence (prospecting), CRM Enrichment (separate product line — completing held records), Data-as-a-Service (API/batch delivery) — the vendor itself separates the prospecting product from the enrichment product.
- Data posture as differentiator: phone-verified mobiles, 30-day refresh for director-level data, Do-Not-Call coverage across Europe, GDPR/CCPA compliance, "compliance-first posture, built in"; "Filter, segment and perfect your target accounts and assign them in seconds"; signals = intent, hiring, job join, funding.
- Segment packaging: separate SMB / Mid-Market / Enterprise pages ("Find contacts, build lists, and grow pipeline fast" for SMB).
- Engagement is external: outreach is done in "CRM or sales engagement tools" — Cognism does not run the sequences.

---

## Cross-product Comparison

| Dimension | Apollo | Hunter | Lusha | Cognism | Evidence |
|---|---|---|---|---|---|
| Prospect list as standing unit | Lists hub (people/companies), org-visible, full action menu | Leads = "soft CRM"; static/dynamic lists, folders, favorites | Workspace tables; extension save-to-table; Activity tab | "Turn your market into a list"; target lists + personas + assignment | A×4 → B |
| Net-new sourcing: database search | Search with broad filter families | Discover (company filters incl./excl., AI assistant) | Prospecting dashboard + API Prospecting endpoint | Web app segmentation + AI Search | A×4 → B |
| Net-new sourcing: extension capture | Chrome extension across websites/CRM/Gmail | Chrome + Firefox extension save-to-list | Extension over LinkedIn/Sales Navigator/sites/CRM, "Lusha Everywhere" | Extension over LinkedIn/websites | A×4 → B |
| Net-new sourcing: file import | CSV import of contacts/accounts into lists | CSV/TXT import with mapping + enrich/verify options | (via API/CRM; import present at platform level) | (not evidenced — positioning only) | A×3 → B, C qualified |
| Lookalike expansion | Suggested Leads; AI list building | "Companies similar to"; Find similar leads | Lookalike solution page + Lookalike API | Recommended prospects/accounts | A×4 → B |
| Saved searches + alerts | Saved searches + subscription alerts ("Net New" tab) | Save this search; Follow company → Signals | Signals (named, dated events) | Signals (intent/hiring/funding) | A×4 → B (alert cadence varies) |
| Dedup vs owned records | "Saved companies" exclusion; merge duplicates | "Hide already saved"; duplicate flags both ways; import dup handling | "Saved leads" exclusion filters (extension/database) | (positioning-level: CRM alignment) | A×3 → B |
| Contact data + verification | Email status tiers; verification; phone retrieval | Verification statuses; auto re-verification | Verified fields; job-change indicator | Phone-verified mobiles; 30-day refresh | A×4 → B (mechanism varies) |
| Credit metering on data | Email credits; credit usage pages | Free search / paid reveal; credit preview | Credits & plans docs | (pricing by package; "no hidden cost") | A×3 → B |
| Prioritization machinery | Personas; custom/AI scores; buying intent | Verification/sending-status filters; Signals timing | ICP scoring; Deep Intelligence layer | Personas; signal-driven targeting | A×4 → B (depth varies) |
| TAM / market-gap view | Data Health Center (TAM per persona/segment) | — | (not evidenced) | (not evidenced) | A×1 → product-specific |
| Handoff: CRM sync/export | Bidirectional CRM sync; CSV export; list→CRM | Native CRM integrations; sync config | Native Salesforce/HubSpot/Pipedrive; record-type choice | "Integrate with leading CRM"; export | A×4 → B |
| Handoff: native sequences | Sequences native (add list to sequence) | Sequences native (Leads → sequence; "Never contacted" default) | Engage & Sequences native | **None** — external engagement tools | A×3 + Cognism explicit absence |
| Team machinery | Territories gating prospecting access; teams; permissions | Team plan structure | Roles/permissions; team management | Assign targets/personas to teams; admin dashboards | A×4 → B (territory gating A×1) |
| AI assistance | AI Assistant list creation; AI research; Outbound Copilot | AI Assistant filter generation | AI chat table building; Ask Lusha | AI Search | A×4 → B (era-typical) |
| Adjacent audience reuse | (sales-centric) | (sales-centric) | Recruiting extension guide; recruiting FAQ | (sales-centric) | A×1 → variant |

## Abstraction Levels

### L0 — Defining Invariant (must stay minimal)

**A Sales Prospecting Platform is a seller-side sourcing-and-preparation application whose defining core is exactly three structures:**

1. **The prospect list as the standing unit of work** — named, persistent, editable collections of sourced sales targets (companies and/or people) that a seller or team builds up, organizes, works through, and draws down from; statuses/tags/owners/notes and dedup state accumulate on the list membership. *Remove it → a search/lookup surface over a database (Directory-like), with no accumulated work.*
2. **Net-new sourcing of prospect records from beyond the organization's own records** — machinery that produces prospect records the customer did not previously have: search/filter over a vendor-maintained database, in-context capture (browser extension over professional networks and websites), lookalike expansion, file import of externally obtained lists, or AI-directed sourcing. *Remove it → list building / segmentation over records the organization already owns — a CRM capability, not this Type.*
3. **Outreach preparation as the purpose, ending at the handoff** — the workflow exists to qualify, complete contact details for, prioritize, organize, and hand prospects into the outbound motion (CRM sync, export, native or external sequence/dialer enrollment); the platform deliberately ends where contacting begins. *Remove it → a sales engagement platform (runs the outreach) or a generic list manager.*

Support: each structure directly observed in 4/4 sampled products (layer B); the abstraction itself is layer C. Removal tests applied below.

### L1 — Common Mature Structure

- Search & filter over company + person records with include/exclude and boolean-style combination
- Saved searches with reuse; alert/subscription or signal-based notification when new matches appear
- Static lists + rule-driven (dynamic) list views; folders/favorites; bulk actions; list sharing with team visibility
- Contact data supply (emails and/or direct dials) with verification states and credit/usage metering
- Verification machinery (verify on save/import, re-verification, verification-status filtering framed as bounce-risk control)
- Browser extension for in-context capture and one-click save
- Lookalike / similar-account / suggested-lead expansion
- Buying signals and event intelligence (funding, hiring, job changes, intent) as filters and timing aids
- Prioritization machinery: personas/ICP frameworks, scores, signal-driven ranking
- Handoff machinery: CRM sync (sometimes bidirectional), CSV export, native sequence enrollment (in data-bundled poles)
- Duplicate detection against the account's saved records
- AI assistance (natural-language list building, AI research, recommendations)
- Team machinery: shared lists, roles/permissions, assignment of targets to sellers/teams; territory-style access gating at the enterprise pole

### L2 — Variant / Optional Structure

- Sourcing-substrate emphasis: large owned database vs web/domain-derived data vs professional-network capture
- Engagement bundling: data-bundled platforms run sequences/dialers natively; others explicitly integrate with external CRMs/engagement tools
- Compliance posture as market differentiator (GDPR/CCPA certification programs, Do-Not-Call coverage, phone-verified regional data — EMEA-led poles)
- Customer tier packaging: freemium/self-serve SMB vs sales-led mid-market/enterprise with admin dashboards and territory governance
- TAM / market-coverage analytics over the customer's own penetration (one sampled product)
- Adjacent-audience reuse: recruiting teams sourcing candidates; fundraising/investor-list building (one sampled product documents recruiting directly)
- Record-family emphasis: people-led vs company-led vs dual (people + company lists as parallel objects)
- AI posture: assistant-as-filter-builder vs AI research vs agentic list building

### L3 — Vendor-specific (kept in these notes only)

- Apollo: "Living Contributor Network" data sharing; Data Health Center TAM view; Outbound Copilot; Play-driven stage auto-updates; "Net New" saved-search tab; territories as access control; bidirectional Salesforce/HubSpot sync with stage mapping; email-credit mechanics; 275M-contact claim.
- Hunter: "soft CRM" self-description; Domain Search heritage; accept-all/webmail/disposable status taxonomy; "Never contacted" default filter in sequence targeting; follow-before-reveal workflow; 50 custom attributes; free-search/paid-reveal credit split; bulk limits by plan (100/25,000 companies).
- Lusha: Wishlist (save-with-no-data) with explicit docs page; side-panel extension rollout; "Lusha Everywhere"; Deep Intelligence vs Search Layer two-layer data framing; MCP/AI-connector distribution (Claude/ChatGPT/Gemini/Perplexity); recruiting extension; 290M-contact / 98%-email-accuracy FAQ claims.
- Cognism: phone-verified "Diamond-class" positioning; 30-day director-level refresh claim; DNC coverage as compliance differentiator; Data Fusion Engine description; 5-step prospecting narrative on the product page.

## Removal Tests (L0 validation)

1. Remove the standing prospect list (keep search + data + handoff): the product becomes a lookup/query surface — find a person, reveal an email, leave. That is a Directory/data-provider experience, not a prospecting workflow. Hunter's own framing ("soft CRM" where work accumulates) confirms the list is load-bearing. **List survives as invariant.**
2. Remove net-new sourcing (keep lists + handoff, sourced records restricted to ones the org already has): the product becomes CRM list building/segmentation. The enrichment pass used exactly this discriminator from the other direction ("completing records the customer holds"). **Net-new sourcing survives as invariant.**
3. Remove the outreach-preparation purpose/handoff (keep sourcing + lists, but no contact data, qualification, or handoff machinery): the product becomes a generic list manager or a marketing audience builder; the reason this Type exists — feeding outbound selling — disappears. **Preparation-purpose survives as invariant.**

## Historical / Market-Sample Check (older, regional, platform-native)

- **Pre-database era**: a seller working printed trade directories, D&B-style reference volumes, or purchased mailing lists — extracting companies into a card box or spreadsheet, completing phone numbers, then dialing — performs the same three structures: sourcing from beyond the org's own records (a purchased file/directory), a maintained list, preparation for outreach. The L0 deliberately says "vendor-maintained database, capture, lookalike, file import, or AI-directed sourcing" rather than "a web search UI", so the list-broker/directory era satisfies the core. ✓
- **Regional**: EMEA compliance-led products (Cognism/Lusha posture) vs US-led volume products — same core; compliance posture is an L2 variant. ✓
- **Platform-native**: CRM vendors ship list building and segmentation inside the CRM — but over records the organization already owns; that is precisely what removal test 2 excludes. The boundary holds historically. ✓
- **List-broker era**: buying a list file and importing it = the file-import sourcing channel, already in L0's sourcing enumeration. ✓
- Conclusion: the definition is not over-fitted to the modern database-search pattern.

## Vendor-specific Findings

See L3 above. None of these enter the final document.

## Rejected Findings

- **"Prospecting = having a large proprietary contact database"** — rejected. Hunter's heritage is domain-crawl-derived emails; extension capture and file import are full sourcing channels; the L0 abstraction is "sourcing from beyond the organization's own records."
- **"Prospecting = running outreach sequences"** — rejected. Cognism explicitly positions export-to-engagement-tools as the final step; Hunter/Apollo/Lusha bundle sequences but their prospecting documentation consistently ends at the handoff. Bundling is packaging.
- **"Prospecting = intent data"** — rejected as definitional. Signals appear in all samples but as filters/timing aids; the SI pass already owns the decision-delivery loop ("who merits attention, when, with what context").
- **"Credits/free-search-paid-reveal is the business model of the Type"** — rejected; metering is common but an implementation/commercial detail (L1/L2 at most, and mostly L3).
- **"AI list building is the new core"** — rejected; AI is era-typical across all four samples but every sampled workflow remains fully executable manually.

## Boundary Findings

1. **vs Sales Data Enrichment Platform** — DISCHARGED from this side, consistent with the enrichment pass's adopted discriminator: enrichment starts from records the customer already holds and completes them (match-and-append write-back); prospecting starts from the market and produces records the customer does not yet have. Same vendors, same substrate, both capabilities shipped by all sampled products (Apollo Lists-CSV-enrichment, Hunter import-with-enrich, Lusha CRM-enrichment-in-place, Cognism CRM Enrichment line). **Keep-both** on loop direction + primary job.
2. **vs Contact Discovery Platform** — the softest seam in the family (flag carried from two prior passes, still open because that leaf is unprocessed). Position taken this pass: contact discovery names the **sourcing act** (search/capture that yields net-new records); prospecting names the **surrounding workflow** (sourcing + maintained list + qualification + handoff). Every product that does prospecting does discovery as one of its steps; a pure discovery product without list/organization/handoff machinery would not satisfy L0 structure 1. **Joint review remains recommended when contact-discovery-platform is processed** — candidate outcomes: keep-both (discovery = sourcing capability named as product emphasis; prospecting = workflow), or documented overlap zone. No directory restructuring performed.
3. **vs Sales Intelligence Platform** — confirmed from this side, matching the SI pass's own table: prospecting is the outreach-preparation **workflow**; intelligence is the **decision layer** (which accounts merit attention, when to act, with what context) delivered over a managed target population. SI products ship prospecting workflows as capabilities (documented in the SI pass for Apollo/Cognism/Lusha). Keep-both.
4. **vs Sales Engagement Platform / Outreach Sequencing Platform** — preparation vs execution: the prospecting platform ends at the handoff; the engagement platform owns the per-prospect outreach program and enrollment state. The data-bundled pole (Apollo, Hunter, Lusha-with-Engage) bundles both — a packaging variant, exactly as the SEP pass recorded.
5. **vs CRM / Lead Management Platform** — the CRM is the system of record for owned relationships and pipeline; list building inside a CRM over owned records is a capability, not this Type. Prospecting platforms source from beyond the org's records and hand off into the CRM (sync/export). Apollo's Data Health Center (CRM-import + market-gap comparison) shows the seam explicitly.
6. **vs Lead Generation Platform (§06)** — outbound target sourcing (finding people worth contacting) vs demand capture (collecting inbound expressions of interest via forms/ads/content). Different population direction: seller-chosen targets vs buyer-initiated demand.
7. **vs ABM Platform** — ABM orchestrates marketing over named target accounts (advertising, web personalization, sales-marketing alignment); prospecting equips individual sellers to build and work outbound lists. Target-account selection overlaps; the machinery and user do not.
8. **vs Directory Application** — a directory is a lookup surface over standing entity records (find one business's phone); a prospecting platform is a workflow over sourced populations accumulating toward outreach. Search UIs resemble each other; the unit of work differs (entry lookup vs maintained list).

## Uncertainties

- **Cognism operational detail**: help center unreachable in this pass (and in the two prior sibling passes); all Cognism-specific workflow claims are positioning-level. The five-step narrative on the sales-intelligence page is strong corroboration for the workflow shape but is not operational documentation.
- **ZoomInfo pole**: never directly researched (403 across both prior passes); the "enterprise owned-database platform" variant is described structurally without product claims.
- **Import/CSV sourcing channel at Lusha and Cognisn**: evidenced at API/CRM level for Lusha; not directly evidenced for Cognism — the sourcing enumeration in L0 lists file import as *one* channel, so the L0 does not depend on it.
- **Territory-gated prospecting access**: directly observed at Apollo only ("Create Territories to Control Prospecting Access"); Cognism's "assign target companies and personas to teams" is adjacent positioning-level evidence. Kept as enterprise-pole L1/L2 machinery, not definitional.
- **TAM/market-gap analytics**: directly observed at Apollo only → product-specific; excluded from the final document's core and mentioned, qualified, as an enterprise capability where relevant.
- **Whether "dynamic lists" (rule-driven auto-updating membership) are universal**: directly observed at Hunter; Apollo lists are manually curated with saved-search+alerts as the adjacent mechanism; treated as a common implementation shape, not an invariant.

## Final Synthesis

A Sales Prospecting Platform is defined by three structures: **a maintained prospect list as the unit of work** (named, persistent, organized, worked by sellers/teams), **net-new sourcing of prospect records from beyond the organization's own records** (database search, extension capture, lookalike expansion, file import, AI-directed sourcing), and **outreach preparation ending at the handoff** (qualification, contact-data completion, prioritization, then CRM/sequence/export handoff — the platform deliberately stops where contacting begins). The family seam with enrichment (held records vs net-new records) is discharged from this side under the family discriminator agreed in the two prior passes; the seam with contact discovery (sourcing act vs surrounding workflow) is the softest and remains flagged for joint review; the seams with sales intelligence (workflow vs decision layer) and sales engagement (preparation vs execution) are confirmed from this side. Historical check passed: directory-era, list-broker-era, and regional compliance-led realizations satisfy the core, so the definition is not over-fitted to the modern vendor-database UI.
