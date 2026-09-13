# Research Notes — Candidate Search Platform

## Research Goal

Understand what a "Candidate Search Platform" is as an Application Type: what is searched (the corpus), how the recruiter expresses what they need (query forms), what comes back (results), what users do with results (actions and handoff), which rules shape the search (corpus rights, metering, result windows, compliance), and where the Type's boundaries lie — especially against the jointly-flagged sibling Candidate Profile Platform (processed 2026-09-07) and the unprocessed Talent Sourcing Platform.

## Initial Boundary (working hypothesis before research)

- Hypothesis: the Type is the employer-side application whose defining activity is **query-driven discovery of candidate people over a searchable corpus** — answering "who matches this need?" — with results feeding hiring workflows (contact, save, handoff).
- Expected nearest neighbors: Candidate Profile Platform (persistent person-record layer — joint review flagged), Talent Sourcing Platform (identification + outreach activity), Job Board (candidate-side search over postings), Contact Discovery Platform / Sales Intelligence (same machinery, sales corpus), Professional Social Network (the member graph itself), ATS (pipeline record; rediscovery slice), general web search engines (X-Ray style people search).
- Known risks: (1) the sampled market bundles search + outreach + record management, so the leaf could collapse into the sourcing platform; (2) "search" is a capability inside ATS and profile platforms, so the leaf must be anchored in products where the search engine *is* the product's center.

## Research Questions

1. What is the corpus? (product-operated member network / external public-web index / licensed specialized databases / job-board resume bank / employer's own ATS-rediscovered records) — and does the Type require the employer to *maintain* person records, or only to *query*?
2. How is the query expressed? (keyword, Boolean strings, structured filters, one-click signal filters, natural-language persona, job-description paste, agent-delivered batches)
3. What do results look like and what actions follow? (profile preview, match indicators, save to project/position, metered contact, outreach, export, hide/similar)
4. What persistent artifacts exist? (saved searches, projects/positions, shared pipelines, notes)
5. What rules matter? (corpus access rights, contact metering/credits, result-window limits, data freshness/provenance, compliance surfaces — GDPR, diversity classifiers, bias reduction, AI-hiring usage terms, calibration obligations in managed delivery)
6. Who uses it and in what roles? (recruiter/sourcer, hiring manager, admin; agency mode)
7. Where are the boundaries listed above, and is the joint-review seam with Candidate Profile Platform resolvable?

## Representative Products

| Product | Philosophy | Customer tier | Evidence level reached |
|---|---|---|---|
| LinkedIn Recruiter | network-native search suite over the product's own member graph; projects + metered InMail | Enterprise / Lite (SMB) | Tier-1 help center ×3 |
| hireEZ | outbound AI sourcing suite; open-web search + ATS rediscovery + agentic EZ Agent | Mid-market/enterprise | Tier-1 help center structure + Tier-2 product pages ×2 |
| SeekOut | search-first standalone people-search engine; multiple specialized talent pools; AI + Boolean dual mode | Enterprise/mid-market | Tier-1 help center ×2 (+ sibling pass ×3) |
| Fetcher | managed/automated sourcing — vendor+AI run searches and deliver calibrated batches | SMB/mid-market | Tier-1 help center ×2 + Tier-2 product page |
| Juicebox (PeopleGPT) | AI-native natural-language people search; CRM + agents around it | SMB→enterprise, agencies | Tier-2 product page (help center/docs exist but not fetched) |
| Indeed resume search / Smart Sourcing | job-board resume-database pole | SMB→enterprise | Unreachable (403 ×1) — market context only, no product claims |

Selection rationale: incumbent network-native pole (LinkedIn), standalone search-engine pole (SeekOut), outbound-suite/agentic pole (hireEZ), managed-batch service pole (Fetcher), AI-native NL pole (Juicebox), plus the older job-board resume-bank pole as market context (Indeed — unreachable). Four different product philosophies, three customer tiers, and one deliberately cross-cutting product (SeekOut) for the flagged joint review with Candidate Profile Platform.

## Sources

- LinkedIn Recruiter Help — https://www.linkedin.com/help/recruiter (root); "AI features in LinkedIn Recruiter" /help/recruiter/answer/a7784112; "Projects in Recruiter and Recruiter Lite" /help/recruiter/answer/a412509; "Run a standard search for candidates" /help/recruiter/answer/a413329. Fetched 2026-09-07.
- hireEZ — https://help.hireez.com (help center root + Sourcing Suite category /hc/en-us/categories/4403289910043-Sourcing-Suite); https://hireez.com/ai-sourcing/ (Open Web Sourcing product page); platform overview via site navigation. Fetched 2026-09-07.
- SeekOut — https://support.seekout.com/en/ (help center root); Search collection /en/collections/14279673-search (Search Databases, AI Search, Boolean Search, Search Filters, Search Insights, Power Filters, Chrome Extension, Search FAQ sub-collections). Fetched 2026-09-07.
- Fetcher — https://www.fetcher.ai (root product page); https://help.fetcher.ai/ (help center root); Search Management category /category/4zus4y8tml-search-management. Fetched 2026-09-07.
- Juicebox — https://www.juicebox.ai (root product page incl. FAQ); docs.juicebox.ai and help.juicebox.work exist but were not fetched. Fetched 2026-09-07.
- Indeed — https://support.indeed.com/hc/en-us returned 403; abandoned after one attempt. Indeed resume search / Smart Sourcing is treated as market context only.
- Sibling pass (record layer anchor): research/candidate-profile-platform.md — Gem, SeekOut, Beamery, Eightfold, Greenhouse evidence.

## Product Observations

### LinkedIn Recruiter (Tier-1 — help center ×3)

Evidence layer: A (directly observed in official help articles).

- **Search entry points**: global search bar → "Start a Recruiter search with filters" or "Start a new AI-assisted search"; Recruiter Lite adds "Search by ideal candidate" / "Advanced filters". Mobile app: keyword search, advanced filter search, continue previous searches.
- **Standard search mechanics**: filters in a left pane (add/remove/adjust filters to view different candidate pools); **Spotlights** above results narrow candidates by signals — Open to work, Active talent, Rediscovered candidates, Internal candidates, Interested in your company, Have company connections (subset in Lite).
- **AI-Assisted Search**: "describe the type of candidate you're looking for, or paste a job description… AI-Assisted Search analyzes and interprets what you enter, instantly applying the right search filters based on your input, context, and intent."
- **Recommended Matches** (inside projects): recommendations tailored to the open job; save/hide/message; "When you message a candidate in the recommended matches list, you use an InMail credit"; list refreshes after actions on candidates.
- **Projects**: "manage your sourcing in one place. Your search results, job applicants, and leads from your media campaigns are hosted in a central location." Pages: Overview (activity, InMail trends, pipeline, candidate demographics), Talent pool (Leads, Recruiter search, Applicants, Recommended Matches, Hidden candidates), Pipeline (saved + imported candidates; "Active stages"; "Recruiter defaults the profile to the first status that has been set by your admin"; Change stage), Job post, Talent Insights (report "generated using the search filters you've selected in your Talent pool search").
- **Project governance**: Private/Public visibility; settings for workflow, imports, project members; archive; reassign owner; no stated limit on project count.
- **Roles**: admin (sets pipeline statuses, product settings); Hiring Manager role ("share profiles and projects directly with other users who have a Hiring Manager role"); bulk actions on profiles in projects.
- **Contact metering**: "Every LinkedIn Recruiter and Recruiter Lite license comes with an allotted number of InMail credits each month based on the type of Recruiter account." Messages can be sent from search results, project Talent pool/Pipeline pages, or a profile.
- **Adjacent in-product surfaces**: Jobs tab (post/edit/close jobs), Hiring Assistant add-on (project creation, sourcing, outreach, prescreening, application review — "available as an add-on for LinkedIn Recruiter and RPS+ customers" with a required permission).

### hireEZ (Tier-1 help structure + Tier-2 product pages)

Evidence layer: A for help-center structure and page claims; positioning-level for unobserved article internals.

- Help center categories: EZ Onboarding; EZ Integration/SSO (ATS + sourcing apps, SSO); **Project** ("EZ Projects express TA workflow and candidates pipeline"); **EZ Engagement** (Email Integration, Campaigns, SOBO, Calendar); **Sourcing Suite** (with a Rediscovery subcategory). Common topics: "Sourcing filters, Response rate, Search results, Collaboration."
- Product positioning: "One Talent Acquisition Platform. Agentic AI on top of your ATS… Every suite runs on one System of Actions, with unified talent data underneath. No rip-and-replace."
- Sourcing module: "Open Web, Deep Search, and Partner Networks across 45+ platforms" (vendor claim).
- **EZ Agent** (agentic sourcing): "Bring your job description and candidate persona, and instantly surface the strongest talent across the open web and your ATS." "AI review evaluates every profile, matches by fit… surfacing the most qualified candidates." "No more blind keyword matches. EZ Agent surfaces candidates by true fit and shows you exactly how and why they match the role." "Go from sourcing to engagement in one click. Launch personalized campaigns directly from EZ Agent."
- **Rediscovery** product line: resurface past ATS applicants.
- **Sourcing analytics**: "tracks every search and pipeline movement"; team performance metrics; salary benchmarks; outreach performance; time-to-fill.
- Suite spans Career Site & Landing Pages, Talent CRM, Applicant Review, Conversational AI (voice screening), AI Scheduler, Hiring Process Management, Hiring Intelligence — search sits inside a broad TA suite.
- Vertical solutions pages: healthcare, RPO/staffing, defense & aerospace ("cleared candidates"), insurance, financial, manufacturing, energy.

### SeekOut (Tier-1 — help center ×2 this pass, +3 sibling pass)

Evidence layer: A.

- **Search collection (40 articles)** organized into: **Search Databases**, **AI Search**, **Boolean Search**, **Search Filters**, **Search Insights**, **Power Filters**, **Chrome Extension**, **Search FAQ**.
- **Multiple specialized corpora ("Talent Pools")**: Public Talent Pool (public profiles, all roles); Expert Talent Pool ("untapped subject matter experts across fields like engineering, biotech, medicine, and finance"); Healthcare Talent Pool ("enriched NPI data and new healthcare prospects"); **Internal Talent Pool** (current employees' skills/background); **GitHub Talent Pool** (find developers "in a completely new way"; Coder Score 1–5 stars from GitHub contributions).
- **Dual query modes with a switch**: Smart Match — "find talent, with the option to switch between AI search and Boolean keywords." SeekOut Assist — "simplifies the process of generating targeted searches and writing engaging messaging"; Conversational search — "ask SeekOut Assist to find candidates as if you were having a conversation with a coworker."
- **Boolean depth**: beginner guide; "Boolean Syntax & Field-Based Search — Enter keywords and our AI ranks the most relevant results. For deeper control, try SeekOut's advanced Boolean search syntax"; advanced syntax; field-based search per pool (Expert, Healthcare, GitHub).
- **Filter system**: overview of filters across categories; Manage Filters (customize/reorder); **Diversity Filters**; **Bias Reducer** ("formerly blind hiring mode — helps reduce unconscious bias by hiding indicators of race or gender in candidate evaluation"); Experience/Education filters; Years of Experience; **Company Alumni filter** ("people who left a specific company… where they went next"); **"Likely Open to New Roles"** ("AI to predict candidates likely to change jobs within 12 months"); Region (international sourcing supported); Industry; Time Zones.
- **Power Filters**: "one-click access to key candidate attributes… without writing complex Boolean strings"; custom Power Filters saved from searches and shared org-wide; **Security Clearance Filters** ("12 levels incl. Public Trust, Secret, Full Scope Poly & Yankee White").
- **Search Insights**: People Insights — "bird's eye view of any talent pool. From any search, you can zoom out to see the aggregate data."
- **Result window**: FAQ — "Most search engines—including SeekOut, Google, and LinkedIn—limit visibility to the first 1,000 results, even when thousands more may exist."
- **Chrome Extension**: "save candidates to a SeekOut project and get contact info for candidates you find online."
- **X-Ray search comparison** article: the product positions itself against hand-built Google/Bing people-search strings.
- From sibling pass: projects as workspaces; profile upload + enrichment; contact-info retrieval is credit-metered and "SeekOut is not a primary source of candidate contact info"; export PDF/CSV/ATS; diversity classifiers FAQ.

### Fetcher (Tier-1 — help center ×2, + Tier-2 product page)

Evidence layer: A for help articles; positioning-level for page claims.

- **Managed/automated sourcing philosophy**: "Our advanced AI technology streamlines the candidate screening process, while our expert team, paired with AI, efficiently sources high-quality candidate profiles tailored to your hiring needs." Customer quote: "I can review a batch in 15 minutes or less, add them to an email campaign, then set it and forget it."
- **Search = position with lifecycle**: "Viewing Your Positions" (dashboard lists searches); **Search Status: Open, Hold, Closed** — "Changing the status of a search from Open to Hold or Closed prevents wasting leads and reduces the percentage of Unvetted candidates. If you don't calibrate we aren't able to adjust the results…" — calibration (feedback on delivered profiles) drives result adjustment.
- **Search Pace**: "control the quantity of prospects delivered on a weekly basis"; Automatic Hold (define triggers that auto-hold a search).
- **Batches**: "A batch is a collection of leads. Generally one batch contains 10 leads, however they may vary according to necessity."
- **Lead types**: Fetcher Leads ("targeted provided by Fetcher for an open search") vs Extension Leads (sourced via the Fetcher Chrome extension) — a search's lead type can be changed.
- **Search workspace**: tabs — Profiles (all profiles added to the search), Analytics, and more; search team management (add users to searches, change owners); notes on searches; editing search criteria from dashboard/search/outreach settings; copying a candidate into a different search.
- **Built-in outreach**: email scheduling with automatic follow-ups; response templates; pause emails; cancel scheduled emails; managing responses in-product.
- **Corpus & self-serve poles too**: "Sourcing from Fetcher Database" category; "Maximizing the Fetcher Database Feature (Starter Plan)" top article; Chrome Extension sourcing; "Use Fetcher's AI to screen candidates when there are plenty of job seekers, or switch to outbound sourcing when talent is harder to find" (inbound + outbound modes).
- **Ownership/handoff rule**: "The candidates you source through Fetcher are yours to use in perpetuity. The best way to ensure you'll always have access to those leads is to transfer them to an Applicant Tracking System (ATS)…"
- **Compliance**: "Fetcher and GDPR" top article; diversity search criteria ("Add specific diversity goals to your searches"); Opt Out page for data subjects.
- Integrations: ATS, CRM, email, Slack.

### Juicebox / PeopleGPT (Tier-2 — product page incl. FAQ)

Evidence layer: A for page claims; positioning-level (no help-center fetch).

- Positioning: "AI recruiting platform… understands who you're looking for. Level up your team with Search, CRM, and Agents." Product schema self-describes PeopleGPT as "AI-powered people search with natural language queries across 800M+ profiles and 30+ data sources" (vendor claims).
- **Search experience**: natural-language prompt ("Who are you looking for?"); results as people cards with match scores (100%/90%/85%… in product imagery) and fit labels ("Good Match", "Not a Match" with reasons like "Specialized in digital transformation"); filters layer ("Software Engineer in San Francisco (+5 more filters)"; "Search Results (428)").
- **Enriched profiles**: "Juicebox builds enriched candidate profiles using high-signal filters focused on impact and achievements."
- **CRM component**: "collaborate on searches, shortlist candidates, and coordinate your outreach campaigns" (team plans).
- **Agents**: "AI recruiting agents search through 800M+ profiles across 30+ sources, managing the workflow end-to-end"; run "24/7 in background" with "Profiles Ready for Review"; "learn from every action, refining searches"; "handle outreach and follow-ups automatically."
- **Outreach**: multi-step sequences; tracking opens/replies/engagement.
- **Integrations & export**: "integrates with 41 ATS systems and 21 CRMs. Alternatively, you can export to detailed CSVs in seconds, with or without contact info" (FAQ claims).
- **Compliance/usage surface**: "Hire for Good" terms page; privacy choices; AI audit center — recruiting-AI usage policy exists as a product surface.
- Vertical data: "Introducing Healthcare Data in Juicebox" (blog); developer-data filters.

### Indeed resume search / Smart Sourcing (market context only — docs unreachable)

- support.indeed.com returned 403; abandoned per source-access rules. No operational claims. Structural role in this research: represents the **job-board resume-database pole** — employer-side keyword search over a bank of candidate-authored resumes with per-contact economics — the historically dominant form of the Type from the late-1990s job-board era onward. Recorded as market context; the historical check below relies on structural reasoning, not Indeed claims.

## Cross-product Comparison

| Dimension | LinkedIn Recruiter | hireEZ | SeekOut | Fetcher | Juicebox |
|---|---|---|---|---|---|
| Corpus | product's own member graph (network-native) | open web across "45+ platforms" (claim) + partner networks + ATS rediscovery | multiple specialized pools: public, expert, healthcare, internal (employees), GitHub | Fetcher-operated database + extension-sourced + vendor-team-run web sourcing | aggregated external index ("800M+ profiles, 30+ sources" — claim) |
| Who curates person records | LinkedIn (platform); employer saves results into projects | hireEZ projects/CRM; ATS sync | SeekOut projects/profiles (straddle toward record layer) | candidates land in searches; export to ATS recommended ("yours in perpetuity") | shortlists/CRM; export CSV/ATS |
| Query forms | filter search; AI-Assisted Search (NL/JD → filters); ideal-candidate search; in-project search; recent/saved searches | search + EZ Agent (JD + persona); sourcing filters | AI/conversational search switchable with Boolean; field-based Boolean; power filters | submitted search criteria (position), vendor-calibrated; database search; extension | natural-language prompt; filter layer; agents |
| Signal/semantic filters | Spotlights: Open to work, Active talent, Rediscovered, Internal, Interested in your company, Company connections | AI review with fit rationale; "how and why they match" | likely-to-move prediction (12-month horizon claim); diversity classifiers; bias reducer; alumni; clearance levels | diversity goals on searches | match scores + fit reasons (imagery) |
| Results shape | people list w/ spotlight badges; Recommended Matches list | AI-reviewed candidate set | ranked results, keyword highlighting, ~1,000-result visibility window | batches of leads (~10) delivered on a weekly pace | ranked cards w/ % match |
| Actions on results | message (InMail, credit-metered), save to project pipeline, hide, bulk actions | launch campaigns from results; add to projects | save to project, get contact info (credits), outreach messaging | add to email campaign; copy between searches; export ATS | contact, shortlist, sequence outreach, export CSV/ATS |
| Persistent artifacts | projects (talent pool/pipeline/stages), saved searches, Talent Insights reports from filters | projects expressing TA workflow; campaigns | projects, saved custom Power Filters, searches | positions/searches with Open/Hold/Closed; notes; team roles per search | searches, shortlists, campaigns |
| Rediscovery / internal | Spotlight filters: Rediscovered candidates, Internal candidates | dedicated Rediscovery product line | Internal Talent Pool; (ATS rediscovery per sibling pass) | — (inbound applicant screening is a separate product mode) | ATS/CRM integrations for sync (claims) |
| Contact economics | InMail credits per license/month | campaigns via integrated email; response-rate analytics | contact-info credits; "not a primary source" disclaimer | email sending with schedules/follow-ups (no stated credit metering) | CSV export "with or without contact info" (contact access gated by plan) |
| Delivery model | self-serve search | self-serve + agentic | self-serve | managed/automated: vendor team + AI deliver batches, recruiter calibrates | self-serve + background agents |
| Collaboration | project members, hiring-manager share/feedback, private/public projects | projects + team collaboration | project sharing (view/comment per sibling pass) | search team (add users, change owners), notes on searches | team plans: collaborate on searches/shortlists/campaigns |
| Insights | Talent Insights report from search filters; Overview metrics (InMail trends, demographics) | sourcing analytics (search/pipeline metrics, salary benchmarks, outreach performance) | People Insights aggregate view over any talent pool | per-search Analytics tab | talent insights per query |
| Compliance surfaces | (AI compliance FAQ exists — not fetched) | GDPR FAQ, CRM data security FAQ, AI assurance page | GDPR posture, diversity classifiers, Bias Reducer | GDPR article, data-subject opt-out, diversity goals | "Hire for Good" usage terms, AI audit center |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Searchable candidate corpus** — a queryable body of candidate-bearing records (people profiles / resumes). The corpus may be operated by the product vendor (member network, aggregated public-web index, licensed database, resume bank) or drawn from the employer's own records; ownership is not the invariant — queryability over candidates is.
2. **Query-driven discovery of candidate people** — the hiring-side user expresses a need (keywords, structured filters, Boolean, natural-language persona) and the system returns a set of **identified people** who match. The query → people-results loop is the defining interaction.
3. **Candidate-bearing results** — each result identifies a specific person with enough background (role/skills/experience signals) to support a fit judgment. Not documents, companies, postings, or sales contacts.
4. **Hiring-side operation** — operated by the hiring organization's recruiting function (or a staffing firm acting for it); results exist to feed a hiring workflow (evaluation, contact, pipeline handoff).

Removal tests:
- Remove #1 (no corpus; the employer only posts jobs and receives applications) → job board.
- Remove #2 (no query loop; users browse a feed or self-presentation graph) → professional social network.
- Remove #3 (results are documents/companies/sales contacts rather than candidate people) → general web search / sales contact discovery.
- Remove #4 (candidates search for jobs) → job board / candidate-side search.

### L1 — Common Mature Structure

- **Multi-mode query expression**: structured filters; keyword/Boolean strings (often field-based); natural-language / AI-assisted / conversational search; job-description or persona paste that compiles into filters; recent & saved searches.
- **Signal and constraint filters**: role/title, skills, location/region, current & past employer (alumni), experience years, education; behavioral/semantic signals (open-to-work, active, likely-to-move); diversity filters and bias-reduction modes; security clearance; industry.
- **Results as people cards**: ranked lists, match/relevance indicators, keyword highlighting, aggregate result windows bounded like search engines.
- **Actions on results**: open full profile; save to project/position/shortlist; hide/dismiss; find similar; contact through a metered channel; add to outreach; export.
- **Persistent working artifacts**: projects/positions where sourced people accumulate (sometimes with lightweight pipeline stages); saved searches; team-shared filter presets.
- **Rediscovery and internal slices**: past applicants and current employees surfaced as searchable corpus segments (spotlights, dedicated pools, dedicated product lines).
- **Contact/outreach attachment**: metered messaging or contact retrieval (credits/allowances); integrated email sequences; response tracking.
- **Insights**: aggregate views over result sets (talent-market/composition data) and search/outreach performance analytics.
- **Capture extension**: browser extension to identify/save/enrich people found on other sites.
- **Handoff**: export (CSV/PDF) and ATS/CRM integration pushing identified people into the application pipeline.
- **Collaboration**: share searches/projects; per-search teams; hiring-manager feedback loops; notes.

### L2 — Variant / Optional Structure

- **Corpus posture**: network-native (vendor operates the underlying graph) vs external aggregated index vs specialized licensed pools vs employer's own records vs hybrid; multiple parallel pools selectable per search.
- **Query-era posture**: manual Boolean → guided filters → AI NL/conversational → agentic (agents run searches continuously and deliver reviewable candidates).
- **Delivery model**: self-serve search vs managed/automated sourcing (vendor team + AI run searches and deliver calibrated batches on a pace; searches have Open/Hold/Closed lifecycle; calibration feedback is load-bearing).
- **Vertical specialization**: healthcare (clinical identifiers), software development (code-forge signals), cleared/defense, experts, sales.
- **Inbound extension**: AI screening of incoming applicants as a companion mode (outbound discovery remains the core).
- **Compliance posture depth**: GDPR programs, data-subject opt-outs, diversity classifiers, bias-reduction modes, published AI-hiring usage terms.
- **Metering shape**: messaging credits, contact-retrieval credits, per-seat licensing, plan-gated contact data.
- **Agency/staffing mode**: search on behalf of client employers.
- **Suite vs standalone**: search as standalone subscription vs one module of a TA suite.

### L3 — Vendor-specific (research notes only)

- LinkedIn Recruiter: InMail credit model tied to license type; Spotlights set; Recruiter Lite vs Recruiter feature splits; Recommended Matches refresh-on-action rule; pipeline stage defaults set by admin; Hiring Assistant add-on + permission; Talent Insights report generated from a project's search filters.
- hireEZ: "EZ Agent" branding; "45+ platforms" claim; System of Actions positioning; SOBO (sender on behalf of) in engagement; salary-benchmark analytics; industry solution pages (cleared candidates, healthcare…).
- SeekOut: named Talent Pools (Public/Expert/Healthcare/Internal/GitHub); Coder Score (1–5 stars); "Likely Open to New Roles" 12-month prediction; Bias Reducer (ex-blind-hiring mode); Security Clearance Filters with named clearance levels (incl. Public Trust, Yankee White); ~1,000-result visibility window FAQ; X-Ray search comparison; Power Filters org-sharing; contact-info letters/sources and no-credit-on-failed-lookup (sibling pass); "not a primary source of contact info" statement.
- Fetcher: batch ≈10 leads; Search Pace weekly quantity control; Automatic Hold triggers; Open/Hold/Closed search status; calibration-required rule ("If you don't calibrate we aren't able to adjust the results"); Fetcher Leads vs Extension Leads; "yours to use in perpetuity" ownership statement; $20k/17-hours/40%/23-seconds marketing stats.
- Juicebox: PeopleGPT name; 800M+/30+ sources claim; match-percentage cards; Agent 4.0; 41-ATS/21-CRM integration counts; MCP server; "Hire for Good" terms.
- Cross-vendor: SeekOut FAQ states the ~1,000-result visibility cap is common to "SeekOut, Google, and LinkedIn" — the only place in the sample where a vendor generalizes a search-engine mechanic across the Type.

## Rejected Findings (not promoted)

- **"800M+ / 1B+ profiles / 45+ platforms"** — vendor scale claims (Juicebox, hireEZ, SeekOut marketing); not a Type property; older and smaller-corpus products (job-board resume banks, agency card files) satisfy the core.
- **"Natural-language AI search"** — the 2026-era dominant query form, but Boolean/filter search remains fully supported in the same products (SeekOut's explicit AI↔Boolean switch documents coexistence); AI is era-common, not defining.
- **"Agentic sourcing"** — present in three of five sampled products (hireEZ EZ Agent, Juicebox Agents, LinkedIn Hiring Assistant) and Fetcher's managed service, but structurally an *automation of* the search loop, not the loop itself; era-common implementation of the delivery model.
- **"Integrated outreach/sequences"** — attached in all sampled products, but outreach machinery is owned by the sourcing/engagement layer (see Talent Sourcing Platform boundary); a search platform can hand off instead (export/ATS push).
- **"Diversity filters"** — recruiting-distinctive and common, but compliance-shape varies by jurisdiction and product; variant, not core.
- **"Contact info included"** — contradicted by at least one vendor's explicit disclaimer and metering; contact retrieval is optional/metered.
- **"Resume bank as corpus"** — one historical pole; modern products index profiles aggregated from the public web or operate member graphs; the corpus concept must stay implementation-agnostic.

## Boundary Findings

1. **vs Candidate Profile Platform (joint review — resolved).** The sibling pass proposed the managed-object seam: persistent person record vs query over a corpus. This pass confirms and sharpens it. The test is: **can the product fulfill its purpose without the customer curating a persistent one-record-per-person layer?** LinkedIn Recruiter (corpus owned by the platform; employer saves *results*, no dedup/merge mandate), Juicebox, Fetcher, and job-board resume search all pass — they are corpus lenses. Gem, Beamery, Eightfold fail — they are record layers with search as a capability. **SeekOut straddles by design**: search-first product (this pass: pools, Boolean, filters, insights) whose projects/profile layer (sibling pass: upload+enrichment, notes/tags/statuses, merge semantics) constitutes a lightweight record layer; the straddle is a packaging posture (search-first suite with an attached record layer), not evidence of one Type. Both passes agree the seam is the managed object, not any capability list. Joint-review outcome recorded for the taxonomy owner.
2. **vs Talent Sourcing Platform (unprocessed sibling — joint-review flag raised).** Sourcing is the *activity* Type: end-to-end identification + engagement workflows (sequences, cadences, response handling, sourcing ops metrics). Candidate Search Platform is the *machinery* Type: the query→corpus→results discovery engine. In the sampled market every search product attaches outreach (hireEZ, Juicebox, Fetcher, SeekOut, LinkedIn InMail) and every sourcing tool needs search — the capability lists coincide almost perfectly, which makes this the sharpest unresolved seam in the cluster. Proposed seam for the joint review: the **center of gravity test** — if the product's workflows, data model, and analytics are organized around *searches and their results* (saved searches, result pipelines, corpus choice, calibration of result quality), it is the search Type; if organized around *engagement workflows over identified people* (sequences, deliverability, reply rates), it is the sourcing Type. Fetcher is the instructive middle case: marketed as managed sourcing, but its operational unit is the Search/Position with Open/Hold/Closed lifecycle and calibration — search-organized machinery delivering the sourcing outcome.
3. **vs Job Board.** Job board = candidate-side discovery over employer postings + application flow; candidate search = employer-side discovery over people corpus. The resume-search product is the job board's employer-side search layer sold as a separate subscription; direction of search and the searched object (people vs postings) are the seam. Indeed evidence was unreachable (403); boundary reasoned structurally.
4. **vs Contact Discovery Platform / Sales Intelligence (§07).** Identical machinery (query → identified people → contact) over a different corpus and intent: sales roles at companies, deal workflows downstream; recruiting adds hiring-specific corpus slices (resumes, employees, past applicants), compliance surfaces (candidate-privacy GDPR posture, diversity, clearance), and pipeline handoff into hiring. Pattern-level kinship recorded; no joint review required (different directory families).
5. **vs Professional Social Network.** The network is the person's self-presentation surface and the corpus substrate; the candidate search product is a separately licensed tool over that substrate with sourcing-specific controls (signal spotlights, metered outreach, project artifacts). LinkedIn ships both as distinct products — the market itself maintains the seam.
6. **vs Applicant Tracking System.** ATS = pipeline/system-of-record for applications in process; candidate search = discovery of people upstream/adjacent to process. The interlock runs both directions (rediscovery indexes ATS candidates into search; search results export into ATS pipelines). LinkedIn's Spotlights ("Rediscovered candidates", "Internal candidates") and hireEZ's Rediscovery line document the interlock without collapsing the Types.
7. **vs General Web Search / X-Ray search.** SeekOut publishes an X-Ray-vs-product comparison: hand-built search-engine strings find public profiles but without recruiting-structured fields, signal filters, result actions, or compliance surfaces. The Type's value is the structured recruiting corpus + recruiting-native query vocabulary + action/handoff rails, not open-web crawling itself.
8. **Two-sided candidate-authored talent marketplaces** (employers browse candidate-owned, opt-in profiles): different Type (marketplace family) — the corpus is candidate-authored and consent-first, the platform operates matching on both sides. Reasoned structurally; not sampled; consistent with the sibling pass's note.
9. **Taxonomy note.** "Candidate Search Platform" is not the market's category name — the market says "sourcing tool", "talent search", "people search", "AI sourcing", "outbound recruiting", or sells the same referent as "Recruiter" (LinkedIn) / "Smart Sourcing" (Indeed). The referent is real and commercially central (the dominant incumbent's core product is exactly this), but the leaf name is a descriptive construction. The Type is real specifically where the search engine is the product's center of gravity: standalone people-search engines, network-native recruiter search, managed batch sourcers, and job-board resume search.

## Historical / Market-Sample Check

- **Pre-digital staffing agency** (card file / resume shelf, queried by a recruiter per client request: person records + a matching act + employer-side operation) satisfies the minimal core with zero digital machinery. The definition holds.
- **Late-1990s–2000s job-board resume databases** (employer keyword-searches a bank of candidate-authored resumes, pays per contact): corpus = resume bank; query = keyword; results = people; hiring-side operation. Fits the core without AI, external indexing, or agentic delivery.
- **X-Ray era** (recruiters hand-building Boolean people-search strings against public profiles on general search engines): query loop over a public corpus, recruiting intent — fits conceptually, though without the structured corpus and action rails; the sampled market itself treats X-Ray as the Type's primitive ancestor (SeekOut publishes the comparison).
- **2026 agentic era** (agents run searches continuously, deliver batches for review): fits — the query loop is automated, not redefined.
- Therefore the canonical core — queryable candidate corpus + query-driven people discovery + candidate-bearing results + hiring-side operation — is era-robust. AI, NL query, external indexing, agents, credits, and compliance tooling are era-common implementations.

## Uncertainties

- **Indeed (job-board resume-bank pole) unreachable** (403 ×1, abandoned): the resume-database pole is documented structurally and as market context; no Indeed-specific operational claims are made anywhere.
- **Juicebox evidence is product-page level**; docs.juicebox.ai / help.juicebox.work were not fetched. Numeric claims (800M+, 30+ sources, 41 ATS/21 CRM) are vendor FAQ claims, recorded as claims.
- **hireEZ help-center articles were not fetched** (category structure + product pages only); internal search mechanics (exact filters, saved-search behavior) not directly observed.
- **Metering details** vary and were only partially observed (LinkedIn InMail credits: direct; SeekOut contact credits: direct via sibling pass; Juicebox/Fetcher: plan-gating implied, not observed). The final document states metering generically.
- **Result-window caps**: the ~1,000-result claim comes from one vendor's FAQ generalizing across search engines; kept qualitative ("bounded result windows") in the final document.
- **Whether a pure self-serve search product exists with no outreach and no record layer at all** was not established in the sample; even the purest poles (Juicebox, LinkedIn) attach outreach. The Type is documented as a discovery core with commonly attached contact/outreach capability.

## Final Synthesis

A Candidate Search Platform is the hiring side's **discovery machinery for people**: a queryable corpus of candidate-bearing profiles (product-operated network, aggregated public-web index, specialized licensed pools, resume bank, or the employer's own records), a query layer that spans structured filters, Boolean, and natural-language persona, ranked candidate-bearing results, and the action rails that move identified people into the hiring workflow (save to project, metered contact, outreach, export/ATS handoff). Rediscovery (past applicants, current employees) and collaborative artifacts (saved searches, projects/positions, shared filter presets) make the loop organizational. Around the core, the market varies along corpus posture, query-era (Boolean → AI-NL → agentic), delivery model (self-serve vs managed calibrated batches), and compliance tooling. The defining seam against the Candidate Profile Platform is the managed object (corpus lens vs maintained record layer — confirmed in joint review, with SeekOut as the deliberate straddle); against Talent Sourcing Platform it is the center of gravity (searches-and-results machinery vs engagement-activity workflows — joint-review flag recorded); against job boards it is search direction and object; against sales contact discovery it is corpus and downstream workflow.
