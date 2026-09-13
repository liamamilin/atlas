# Research Notes — Research Funding Discovery Platform

## Research Goal

Understand what a Research Funding Discovery Platform actually is as an Application Type: what exists inside it, who uses it, how funding opportunities flow from sponsors to seekers, what discovery mechanisms define it, and where its boundaries lie against grant management, grantmaking, and search products.

## Initial Boundary

Working hypothesis before research:

- Core purpose: help funding seekers (researchers, research offices, institutions) discover funding opportunities (grants, fellowships, awards) offered by many sponsors.
- Likely users: principal investigators, research development / pre-award staff, research administrators.
- Nearest neighbors: Research Grant Management (post-award), Grantmaking Platform (funder-side), Government Grants Management, Academic Search Engine, Lead Generation Platform (commercial analog).
- Likely boundary: discovery ends at "found / evaluated / tracked"; application preparation and award administration are out of scope.
- Unknowns: exact structure of an opportunity record; how opportunities enter the corpus; how matching works; whether institutional curation is definitional or optional; whether the nonprofit grant-seeking market (Instrumentl class) belongs to this Type.

## Research Questions

1. What is a funding-opportunity record? What fields does it carry across products?
2. How does the opportunity corpus get assembled (editorial curation, crawling, agency posting, web tracking)?
3. What discovery mechanisms exist: search, facets, saved searches, alerts, profile-based matching?
4. What is the lifecycle/state model of an opportunity?
5. What does the institutional layer do (curation, dissemination, internal opportunities, usage reporting)?
6. Where does discovery end and grant management begin?
7. How does the seeker-side orientation distinguish this Type from funder-side platforms?
8. Is the Type research-specific, or does the same structure serve nonprofit grant seeking?

## Representative Products

Selected for market representation, documentation quality, different data-assembly philosophies, and different customer tiers:

| Product | Vendor | Segment | Access model | Corpus assembly philosophy |
|---|---|---|---|---|
| Pivot-RP | Clarivate | academic research administration | institutional subscription | editorially curated by in-house editors |
| GrantForward | GrantForward | academic research | institutional subscription | data crawling + specialist verification |
| SPIN | InfoEd Global (Digital Science) | academic research | institutional subscription (federated login) | data obtained directly from sponsors, editorial quality check |
| Research Professional | Research Professional (Emap/Research Fortnight) | UK/EU academic research | institutional site license | editorial team + database of live and forecast calls |
| Grants.gov | US federal government (HHS/GSA) | US federal grants | free public portal | opportunities posted directly by federal agencies |
| Instrumentl | Instrumentl | nonprofits, universities, grant consultants | organizational SaaS subscription | aggregation from funder websites + IRS 990 filings, continuous web tracking |

## Sources

Research date: 2026-09-10.

Direct WebFetch of vendor sites was largely blocked (403/404: clarivate.com product URLs, grantforward.org, grants.gov, instrumentl.com, symplectic.co.uk SPIN page). Evidence was obtained from official vendor pages, official help centers, and official product documentation surfaced via web search, plus university library/research-office guides that document institutional usage of these products. Per-source detail:

- Pivot-RP — Clarivate product page (clarivate.com/academia-government/.../pivot-rp-funding/), Pivot-RP factsheet, Pivot-RP help center (pivot-rp.zendesk.com: "Searching for Funding Opportunities"), Ex Libris Knowledge Center "Pivot-RP Profiles" (Pivot product documentation), CASRAI guide comparing Pivot-RP and Grants.gov.
- GrantForward — grantforward.com index/about/subscription_plans pages, GrantForward tutorials page (grantforward.com/support/tutorial).
- SPIN — infoedglobal.com SPIN Global Suite product page, spin.infoedglobal.com access portal, university guides (Toledo, Penn, UNC) documenting SPIN/SMARTS usage.
- Research Professional — Ex Libris Knowledge Center "Funding" product documentation, university guides (Plymouth, King's College London, Reading, Sussex).
- Grants.gov — grants.gov Search Grants page, Online Help articles (Search Grants Tab, Subscribe to Saved Searches, Manage Subscriptions, Subscribe to Opportunities), Grants Learning Center.
- Instrumentl — help.instrumentl.com articles (What are matches, What is a project, Funder Matches, Discover beta, Discover Plan), instrumentl.com/faq.
- Symplectic — symplectic.co.uk products page (fetched directly): SPIN no longer listed as a standalone product; Elements platform includes funding/awards management and Dimensions grants integration.

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison and boundary reasoning.

## Product Observations

### Pivot-RP (Clarivate)

Key observations (evidence layer A unless noted):

- Positioning: "expert-curated source of global research funding opportunities with powerful workflow, intelligence, and discovery tools"; trusted by 700+ research institutions (vendor-stated).
- Corpus: funding opportunities from global sponsors — government agencies, foundations, corporations; grants, fellowships, prizes, and other funding programs, across disciplines and career stages. A dedicated editorial team curates and verifies records; vendor states records are reviewed and updated daily.
- Opportunity record fields observed in search/filters: Title, Abstract, Keywords, Applicant Type, Citizenship, Funding Type, Activity Location, Sponsor, Sponsor Type, Agency, Opp ID (opportunity identifier), Amount, Deadlines, Limited Submission flag, Recently Added date.
- Search: basic text search (with exact-phrase quotes, Boolean OR/NOT, wildcards, proximity operators), advanced search (filters incl. Amount, Deadlines, Limited Submission, Activity Location, Citizenship/Residency, Funding Type, Keywords, Applicant Type, Sponsor Type, Recently Added last 7/14/30 days), search by funder, search by keywords (editorially curated keyword list with autocomplete/browse), a graphical discovery tool (visual rings by category).
- Curated lists: pre-configured lists on home page and Funding page tabs — shared by other users, Advisor-curated (based on user profile), administrator-curated (institution-wide), internal (institution-local), Most Popular, Editor's Pick (editorial team), Related to a researcher, Related to the opportunity being viewed.
- Saved searches: rerun previously saved searches.
- Researcher profiles: Clarivate maintains 3M+ faculty profiles (vendor-stated); users are expected to have profiles; profile keywords are required for the Advisor to suggest opportunities; profiles carry publications, degrees, roles, affiliations; profile accuracy drives recommendation quality.
- AI matching: "Pivot-RP Funding Advisor" recommends opportunities based on researcher profile, discipline, research interests; semantic/natural-language search; AI-generated titles/summaries; vendor states AI operates on curated data "rather than scraped web content".
- Past awards: searchable database of 5M+ previously awarded grants across dozens of international funders (vendor-stated); funder and past-award data surfaced alongside open calls.
- Collaborator discovery: Profile Discovery searches researcher profiles (Web of Science-linked) by expertise, discipline, publication/award history; aimed at building teams, finding co-investigators, locating reviewers.
- Institutional layer: research administrators curate opportunities, share updates/lists, send targeted funding information to researchers (University of Pittsburgh case: "manage and send large amounts of targeted funding information"); institutional customization; policy news for strategic intelligence.
- Access: institutional subscription; individual users create profiles inside the institutional license.

### GrantForward

Key observations (A):

- Positioning: "funding opportunity database and service built by academics for researchers"; database of 30,000+ sponsors (vendor-stated).
- Corpus assembly: "specialized data-crawling technology to constantly update our extensive database of sponsors and funding opportunities"; "Every grant opportunity is thoroughly analyzed and then verified by our team of specialists to ensure accuracy."
- Coverage: federal grants, foundation grants, limited submission opportunities, pre-solicitations, awards.
- Search: simple search + advanced keyword search; adaptive search filters; filter facets observed: Funders, Funder's Country, Categories, Deadline Status, Amount, Funder Types, Grant Types, Applicant Locations, Activity Locations, Citizenships, Limited Submission, Applicant Types. Sort options: Relevance, Deadline, Recently Added, Recently Updated, Funders, Title.
- Profiles & recommendations: researcher profiles with research interests (keywords/phrases, can be generated from publications/CVs); profile-based grant recommendations; "Auto Sign-Up/Auto Profile" service automatically creates accounts and profiles for all institution members; recommendations delivered to 39,000+ researchers (vendor-stated); account vs profile distinction documented; recommendations page allows tailoring via interests + filters.
- Collaborator discovery: Researcher Profiles Search page; collaborators identifiable on each grant detail page.
- Sponsor Directory: search for sponsors/funders by topic.
- Institutional layer: administrators get dissemination tools; can manage internal grants ("curate both internal and external grants in one place and promote them to your faculty"); can set predefined default search filters per user type (Default, Student, Researcher, Staff); usage reports (profiles created, researchers tab); personalized homepage (institution updates, personal updates, user groups, database updates); embeddable search widget for institution websites.
- Access: institution subscription priced by institution size (population + research expenditures); every member can access; AI Assistant present.

### SPIN (InfoEd Global)

Key observations (A for vendor pages; B for university-guide usage documentation):

- Positioning: "World's Largest Database of Sponsored Funding Opportunities" (vendor-stated); approximately 40,000 funding opportunities from 10,000+ (elsewhere 12,000+) government, foundation, and corporate sponsors (vendor-stated).
- Coverage: grants, fellowships, training opportunities, limited submissions; all disciplines, US and international.
- Corpus assembly: "The data in SPIN is obtained directly from the sponsoring agencies to ensure the integrity of information. Each program is updated in SPIN as the sponsor revises it" (Penn guide quoting SPIN); "Data maintained and quality-checked by trained editorial staff" (vendor).
- Search: three modes — Text (full text: title, sponsor name, synopsis, objectives, contact info), Keyword (curated keyword taxonomy of ~3,500 terms for pre-matched/categorized opportunities), Advanced (target multiple criteria: Sponsor Type, Eligibility, Title vs full proposal); Boolean operators and nesting supported.
- Persistent filters: applicant geographic location (continent/country/state), applicant type (faculty, student), project type (endowment, award), project location, citizenship, sponsor type — remain in place across search modes and sessions until edited.
- Alerts: SMARTS automation tool — daily or weekly email alerts of new or modified opportunities; profile-based matching.
- Access: annual institutional subscription to 1,000+ colleges/universities/industry clients (vendor-stated); InCommon federated institutional login; at Penn, accessed through PennERA (the institution's research administration system) — evidence of suite embedding.
- Market note: Symplectic (Digital Science) acquired InfoEd; the Symplectic site no longer lists SPIN as a standalone product; Symplectic Elements now markets funding/awards management and a Dimensions grants integration ("first fully searchable grants data source"). SPIN remains live at spin.infoedglobal.com. (A for both pages; evolution uncertain.)

### Research Professional

Key observations (A for Ex Libris-hosted product documentation; B for university guides):

- Positioning: "an online database of research funding opportunities and a source of international research policy and practice news" (multiple university guides quoting the vendor).
- Corpus: thousands of open calls from UK, EU and global funders; live and forecast opportunities; funding opportunity record summary shows closing date, opportunity name, funder, maximum award amount.
- Search: Simple Search (free-text with suggested terms, suggested funders and disciplines) and Advanced Search (combination of criteria; six most-used criteria as buttons, more under "More options"; Match all / Match any criterion logic).
- Saved searches + alerts: save search results; "Save and alert" option; weekly email containing new opportunities added during the week matching saved searches; emails sent Sundays; single consolidated email by default; email alerts management page with per-search tickboxes.
- Calendar view: at "Networked" subscription level, saved-search results viewable in calendar format (deadline calendar).
- Bookmarks/downloads: bookmark content; download selected results for offline use.
- Magazines: institution-configured channels for internal calls for funding and internal sifts (Plymouth guide).
- Fingerprinting: personalized algorithm based on publicly available research data identifying opportunities relevant to each academic, condensed into weekly email (King's guide).
- News + Funding Insight + Awards: editorial research policy news; Funding Insight (guidance content); Awards section searchable previous award winners (Sussex guide).
- Access: institutional site license; campus access without registration (limited features — cannot save searches); registered accounts unlock saved searches and alerts.

### Grants.gov

Key observations (A):

- Positioning: free, public, US-federal portal; "opportunity-posting and application-submission portal" (CASRAI comparison); the required system of record for US federal proposal submission.
- Corpus: opportunities posted directly by federal grant-making agencies (no third-party curation); coverage limited to US federal grant-making agencies.
- Opportunity record: Opportunity Title, Opportunity Number (FON — Funding Opportunity Number, the identifier), Agency, Assistance Listings (CFDA numbers), Opportunity Status, Funding Instrument Type, Eligibility, Category, posted/close dates, application packages.
- Opportunity statuses (documented): **Forecasted** (planned opportunities not yet an official funding opportunity announcement; "not guaranteed that a grant forecast will become an FOA"), **Posted** (announced FOAs currently open and accepting applications), **Closed** (past due date, no longer accepting applications), **Archived** (historical record of closed FOAs). Closed and Archived not available for saved searches.
- Search: basic criteria (Keyword(s), Opportunity Number, Assistance Listings) + faceted filters (Opportunity Status, Funding Instrument Type, Eligibility, Category, Agency, Date Range); search tips (words, phrases, operators); export results to CSV; related opportunities shown together in results.
- Alerting: saved searches with email notifications; nightly email digest of opportunities posted or modified; three subscription modes — All New Opportunities, Saved Searches, Selected Opportunities (per-opportunity subscription from the opportunity detail page; notifies when the grantor modifies the opportunity, packages added/modified/deleted).
- Application side: Apply button, application packages, registration prerequisites (SAM.gov/UEI per CASRAI) — the submission half of the portal, beyond discovery.
- No researcher profiles, no recommendations, no funder directory — pure opportunity discovery + subscription.

### Instrumentl

Key observations (A):

- Positioning: grant prospecting, tracking, and management for nonprofits, universities, and professional grant writers/consultants.
- Unit of organization: **project** = workspace with two components — a saved search (generating matches) and a grant tracker. Projects map to program areas (e.g., homelessness program, literacy classes) or, for consultants, to clients (Client Profiles).
- Corpus: active/open grants from corporate, private, federal, state sources; eligibility pulled from funder websites and 990s; funder websites tracked continuously ("24/7") with notifications on material changes (deadline or giving preferences) (vendor-stated).
- Matching: smart matching continuously matches project criteria to new opportunities; weekly email summarizing new matches per project; matches list sorted by best match.
- Two match types: **Opportunity Matches** (active public grant opportunities/RFPs with deadlines, application details, eligibility) and **Funder Matches** (foundations aligned by past giving patterns even without open opportunities; data from IRS Form 990 filings; may include invite-only or no-website funders). Mutually exclusive — a funder with an active matching opportunity appears only as an Opportunity Match.
- Review loop: save a match (moves to project Tracker) or hide it (from this project / from all projects; hidden indefinitely, unhideable); opportunity notes carry over to the Tracker.
- Tracker: pipeline of saved opportunities organized by project, fiscal year, deadline, status, amount; application cycles (e.g., LOI + full proposal steps); deadline reminders + weekly deadline digest; tasks with assignees; grant owners; funder history (Funder Notes, Funder Contacts); funder-change notifications; reports (PDF/CSV exports).
- Funder intelligence: 990-based funder profiles (450k+ funder profiles, vendor-stated) with giving rate to new grantees, median grant amount, past grantees, giving by category (NTEE codes), openness to new grantees; Recipient Profiles (reverse search: who funds nonprofits like yours).
- Saving a Funder Match creates a **custom opportunity** in the Tracker (the tracker houses opportunities, not standalone funders) — structural evidence that the opportunity is the native unit of record.
- New Discover experience (beta): AI Prospecting Assistant — describe the project in plain language; guided setup (organization type, funding use, funder types, grant size range); refine matches in real time via chat; deadline confirmation filter ("confirmed deadlines no sooner than 30 days from today").
- Access: organizational SaaS; plan tiers gate features (Funder Matches on Discover plan and higher); most funders US-based.

## Cross-product Comparison

| Dimension | Pivot-RP | GrantForward | SPIN | Research Professional | Grants.gov | Instrumentl |
|---|---|---|---|---|---|---|
| Opportunity corpus | yes (editorial) | yes (crawl+verify) | yes (from sponsors) | yes (editorial) | yes (agency-posted) | yes (web+990 aggregation) |
| Opportunity identifier | Opp ID | (implied) | (implied) | (implied) | FON (explicit) | (implied) |
| Eligibility fields (applicant type, citizenship, location) | yes | yes | yes | yes (applicant nationality) | yes (Eligibility facet) | yes (org type, locations) |
| Deadline data | yes | yes | yes | yes (closing date) | yes (close date + forecast) | yes (incl. confirmed-only filter) |
| Amount data | yes (filter) | yes (filter) | (filter) | yes (max award) | (assistance listings) | yes (grant size range) |
| Sponsor/funder records | yes (funder search, past awards) | yes (Sponsor Directory) | yes (sponsor types) | yes (funder suggestions) | Agency facet only | yes (990 funder profiles) |
| Keyword/advanced search | yes | yes | yes (3 modes) | yes (simple+advanced) | yes (basic+facets) | yes (criteria + AI chat) |
| Saved searches | yes | yes | yes | yes | yes | yes (project = saved search) |
| Email alerts | yes | yes | yes (SMARTS daily/weekly) | yes (weekly) | yes (saved searches + nightly digest + per-opportunity) | yes (weekly match emails + deadline digests) |
| Profile-based matching | yes (Funding Advisor) | yes (recommendations) | yes (SMARTS profiles) | yes (Fingerprinting) | no | yes (smart matching per project) |
| Curated lists / editorial picks | yes | (admin curation) | (editorial QC) | yes (editorial) | no | no |
| Save/track opportunities | yes (lists) | yes | yes (save/export) | yes (bookmarks) | yes (subscriptions) | yes (Tracker pipeline) |
| Institutional admin layer | yes (curate/share/lists) | yes (dissemination, internal grants, defaults, usage) | (admin-managed access) | yes (Magazines, workgroup folders) | no | yes (projects, owners, tasks, reports) |
| Internal (institution-own) opportunities | yes (internal lists) | yes (internal grants) | (not observed) | yes (Magazines) | no | (custom opportunities) |
| Past awards / funder history | yes (5M+ awards) | (awards searchable) | (not observed) | yes (Awards section) | no | yes (990 giving history) |
| Collaborator discovery | yes (Profile Discovery) | yes | no | no | no | no |
| Application submission attached | no | no | no | no | yes | no |
| News/policy content | yes (policy news) | no | no | yes (core feature) | (learning center) | no |
| Access model | institutional subscription | institutional subscription | institutional subscription | institutional site license | free public | organizational SaaS |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Two jointly-held structures over one binding:

1. **The funding-opportunity corpus** — a persistent, organized collection of identified opportunity records, each describing a specific funding offering from a sponsor: what it funds, who is eligible, by when, for how much. The record is the unit of the collection; it persists and is maintained as opportunities change. Remove → a news feed or generic search index with no funding semantics.
2. **Seeker-side discovery over the corpus** — search/browse/filter mechanisms through which a funding seeker (a person or an organization) finds opportunities matching their needs and situation. The platform is held *for the seeker*, aggregating many sponsors, not for a funder running its own programs. Remove → a dataset nobody can discover through, or a funder-side program catalog.

Binding: the corpus is external, multi-sponsor funding opportunities, and the served party is the funding seeker. Remove the binding → funder-side grantmaking or a single agency's program catalog.

Historical check: printed grant directories (annual reference volumes with indexes), library reference shelves of funding guides, and emailed opportunity listservs all satisfy L0 — corpus + manual lookup or push delivery. Nothing modern (profiles, AI, dashboards) is required. Historical check passed.

### L1 — Common Mature Structure

Present across the sample (mostly all six products):

- Saved searches + email alerts (all six; the single most universal capability)
- Advanced/faceted search with eligibility filters: applicant type, citizenship/residency, location, sponsor type, funding type/instrument, amount, deadline window (all six)
- Structured opportunity detail page (sponsor, description, eligibility, deadlines, amount, application info) (all six)
- Seeker interest profile driving recommendations — researcher profile (keywords/interests, often from publications) or organizational project criteria (B: 5 of 6; absent from Grants.gov)
- Save/bookmark opportunities for later (all six in some form)
- Sponsor/funder records or directory alongside opportunities (B: 5 of 6; Grants.gov has only an agency facet)
- Deadline as first-class, user-visible data driving sorting, filtering, calendars, reminders (all six)
- Institutional administration layer: shared/curated lists, dissemination to members, internal opportunities, usage reporting (B: academic products + Instrumentl; absent from Grants.gov)

### L2 — Variant / Optional Structure

- Corpus assembly model: editorial curation (Pivot-RP, Research Professional) vs crawl+verify (GrantForward) vs direct-from-sponsor (SPIN, Grants.gov) vs web+tax-filing aggregation (Instrumentl) — different provenance claims, same function
- Opportunity state model: explicit posted/closed/archived lifecycle (Grants.gov documented; others imply via deadline status filters)
- Forecasted opportunities (Grants.gov explicit; Research Professional "live and forecast")
- Limited-submission flagging (Pivot-RP, GrantForward, SPIN) and internal sift handling (Research Professional Magazines)
- Internal/institution-own opportunity curation (Pivot-RP internal lists, GrantForward internal grants, RP Magazines)
- Funder intelligence from tax filings (Instrumentl 990s; Pivot-RP/RP past-award sections)
- Collaborator/researcher discovery (Pivot-RP, GrantForward)
- News/policy content bundled (Research Professional core; Pivot-RP policy news)
- Application submission attached to the discovery portal (Grants.gov only)
- Pipeline tracking with stages/tasks/owners (Instrumentl Tracker; lighter save/bookmark elsewhere)
- AI assistants: semantic search, profile-based recommendation, plain-language setup chat (Pivot-RP, GrantForward, Instrumentl, RP Fingerprinting)
- Calendar views, embeddable widgets, CSV/API export
- Access models: free public portal, institutional subscription/site license, organizational SaaS with plan tiers

### L3 — Vendor-specific (research notes only)

- Pivot-RP: Funding Advisor®, Opp ID, Editor's Pick, Web of Science-linked profiles, visual-ring discovery tool, ProQuest platform lineage (formerly COS Pivot)
- GrantForward: Auto Sign-Up/Auto Profile, GrantForward AI Assistant, embeddable widget, user-type default filters
- SPIN: SMARTS™ automation, InCommon federated access, ~3,500-term curated keyword taxonomy, PennERA embedding
- Research Professional: Fingerprinting, Research Fortnight/Research Day newsletters, Funding Insight, Networked-level calendar
- Grants.gov: FOA terminology, Assistance Listings (CFDA), SAM.gov/UEI registration prerequisite, Grants 101 learning center, Simpler.Grants.gov next-gen search
- Instrumentl: Prospecting Assistant, custom-opportunity mechanism for saved funders, NTEE codes, Client Profiles for consultants, plan-tier gating

## Vendor-specific Findings

See L3. None of these entered the canonical model. Numeric scale claims (40,000 opportunities, 30,000 sponsors, 5M past awards, 3M profiles, 450k funder profiles, $1B active grants) are vendor-stated marketing figures — recorded here with attribution, not promoted to the canonical document.

## Boundary Findings

- **vs Research Grant Management** (§23 sibling leaf): discovery ends at found/evaluated/tracked; grant management begins at application preparation, submission, and the institution's award portfolio lifecycle. Grants.gov is the clearest hybrid (discovery + submission portal in one); SPIN embedded in PennERA shows discovery being consumed inside a research-administration suite. The seam: if the system's unit of work is the *application/award* (institution-side lifecycle), it is grant management; if the unit is the *opportunity* (seeker-side corpus), it is this Type.
- **vs Grantmaking Platform** (§25): funder-side (designing programs, accepting/reviewing applications, making awards) vs seeker-side (finding opportunities from many sponsors). The same opportunity record exists on both sides of the market; the user, the direction of the workflow, and the corpus ownership differ.
- **vs Government Grants Management** (§24): the government's administration of its grant programs vs the public discovery face of those programs. Grants.gov's search layer is the seeker-facing discovery surface of the federal ecosystem; the management systems behind agencies are a different Type.
- **vs Academic Search Engine / Vertical Search Engine** (§02): literature/document retrieval vs domain-structured funding discovery. The opportunity record's eligibility/deadline/amount semantics, and the alert-on-new-matches loop, are funding-specific.
- **vs Funder directories** (e.g., Candid Foundation Directory — no directory leaf; adjacent market): funder directories hold organizations and their giving history; this Type holds opportunities (calls with deadlines). Instrumentl bridges both (Funder Matches from 990s) but must convert a saved funder into a "custom opportunity" to fit its tracker — structural evidence that the opportunity is the native unit of this Type.
- **vs Lead Generation Platform** (§07): the commercial analog (database + matching + alerts + pipeline tracker), but with sales-lead semantics instead of eligibility/deadline/award semantics. Structurally parallel, domain-distinct.
- **Taxonomy observation**: the leaf name says "research funding", but the sampled structure is not research-exclusive — Instrumentl serves nonprofit program funding with an identical core model. The research binding is the directory's placement (§23), not a structural necessity. Recorded as a boundary issue for the taxonomy: a future "grant discovery platform" generalization could subsume both markets; the research-specific leaf remains valid as the canonical instance.

## Uncertainties

- Exact update cadences are vendor claims (Pivot-RP "reviewed and updated daily"; GrantForward "constantly updated"; Grants.gov nightly digest email is documented behavior). Final document avoids precise cadence claims except where documented.
- Numeric scale figures are vendor-stated and unverified; kept out of the canonical document.
- SPIN's product evolution post-Symplectic-acquisition is unclear (standalone SPIN live, but no longer listed on Symplectic's product pages; funding discovery now also marketed inside Symplectic Elements via Dimensions).
- Whether limited-submission *management* (beyond flagging/filtering) belongs to this Type or to research administration — observed only as a flag/filter plus internal-sift channels; full workflow not observed in the sample.
- GrantForward/SPIN/RP opportunity-record field completeness was observed through search filters and summaries, not full record schemas; field lists in the final document are stated as typical, not exhaustive.

## Final Synthesis

A Research Funding Discovery Platform is the funding seeker's discovery system over a multi-sponsor corpus of funding opportunities. Its defining core is exactly two jointly-held structures: the opportunity corpus (persistent, identified, maintained records of specific funding offerings — what/who-eligible/by-when/for-how-much) and seeker-side discovery (search, filtering, and matching that connect a seeker's situation to opportunities). Everything else — profiles, recommendations, alerts, curated lists, funder intelligence, institutional dissemination, tracking pipelines — is mature structure layered on that core. The Type is bounded on the funder side by grantmaking platforms, on the lifecycle side by grant management, and on the content side by literature search engines. The same core model extends beyond academic research to nonprofit grant seeking (Instrumentl), which the directory's research-specific naming does not capture.
