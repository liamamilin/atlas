# Research Notes — Candidate Profile Platform

## Research Goal

Understand what a "Candidate Profile Platform" is as an Application Type: what the managed object is (the candidate profile), who operates it, how profiles come into existence and are maintained, what users do with them, and where the Type's boundaries lie against the ATS (whose central record is also called a "candidate profile"), candidate search/sourcing platforms, resume builders, and professional social networks.

## Initial Boundary (working hypothesis before research)

- Hypothesis: the Type is the employer-side platform whose central managed object is the **persistent, person-level candidate profile** — a structured record of a potential hire that exists before, between, and after any specific application.
- Expected nearest neighbors: Applicant Tracking System (profile embedded in a requisition pipeline), Candidate Search Platform (search as the managed object), Talent Sourcing Platform (identification/outreach as the managed object), Resume Builder (candidate-side authoring), Professional Social Network (public self-presentation graph).
- Known risk: "candidate profile" is standard vocabulary inside every ATS; the leaf may be a capability slice rather than a standalone Type. The research must establish whether a standalone profile-first market exists (the market calls it Talent CRM / Candidate CRM / Talent Engagement / Talent Intelligence).

## Research Questions

1. What exactly is the managed object? What does a candidate profile contain, and how is it structured?
2. How do profiles come into existence (external search/index, imports, uploads + enrichment, candidate self-service forms, ATS/HCM sync)?
3. Is the profile independent of applications/positions? How do products express the profile-vs-application distinction?
4. How are profiles organized (projects, pools, lists, talent communities) and shared?
5. What do users do with profiles (view, search, tag, status, notes, share, export, outreach)?
6. What rules matter (dedup/merge, data freshness/provenance, consent/privacy, permissions, metering)?
7. Where are the boundaries: ATS, Candidate Search, Talent Sourcing, Recruitment Marketing, Resume Builder, Professional Social Network, sales CRM, two-sided profile marketplaces?

## Representative Products

| Product | Philosophy | Customer tier | Evidence level reached |
|---|---|---|---|
| Beamery | Talent CRM / talent lifecycle, profile-centric ("Talent CRM" product) | Enterprise | Tier-2 product pages (helpdesk unreachable) |
| Gem | Talent engagement platform; CRM (People) + ATS + outreach | Mid-market/enterprise | Tier-1 help center ×3 |
| Eightfold AI | AI talent intelligence; deep inferred profiles | Enterprise | Tier-2 product pages (docs portal login-gated) |
| SeekOut | Search-first talent platform with profile management core | Enterprise/mid-market | Tier-1 help center ×3 |
| Greenhouse Recruiting | ATS anchor — candidate profile as pipeline record | Mid-market/enterprise | Tier-1 help center ×2 |

Selection rationale: two CRM-first poles (Beamery enterprise, Gem mid-market), one AI-intelligence pole (Eightfold), one search-first pole (SeekOut), one ATS anchor (Greenhouse) to document the profile-inside-pipeline contrast. Ashby was dropped after two transport errors.

## Sources

- Beamery — https://beamery.com (root), https://beamery.com/platform/talent-acquisition/talent-crm/ (Talent CRM product page). Fetched 2026-09-07.
- Gem — https://help.gem.com (help center), https://help.gem.com/people (People directory), https://help.gem.com/external/projects-overview, https://help.gem.com/external/gem-talent-community, https://help.gem.com/external/ats-candidate-rediscovery-ats-search. Fetched 2026-09-07.
- Eightfold AI — https://eightfold.ai (root), https://eightfold.ai/products/talent-acquisition/. Fetched 2026-09-07. https://docs.eightfold.ai/ is login-gated (redirects to sign-in).
- SeekOut — https://seekout.com (root), https://support.seekout.com/ (help center), Candidate Profiles collection, Projects collection, https://support.seekout.com/en/articles/1628488-candidate-profile-uploads-and-data-enrichment, https://support.seekout.com/en/articles/11878051-how-to-use-projects. Fetched 2026-09-07.
- Greenhouse — https://support.greenhouse.io/hc/en-us, https://support.greenhouse.io/hc/en-us/articles/30352015432987-Candidate-profile-redesign-overview. Fetched 2026-09-07.
- Unreachable: Ashby help center (transport error ×2, abandoned); Beamery helpdesk support.beamery.com (transport error ×2, abandoned); Eightfold docs portal (login-gated).

## Product Observations

### Gem (Tier-1 — help center)

Evidence layer: A (directly observed in official help articles).

- **People product** = "Organize projects, candidate pools, and hiring workflows in one place." Gem's CRM layer is called People; separate products: Outreach (sequences), ATS, Scheduling, Talent Marketing, Talent Compass.
- **Projects** organize candidates; best practice = one project per open role. Candidates not placed in a project land in a default project called **My Scratchpad**.
- **Candidate profiles** open from project lists (pop-up in same tab or new tab for side-by-side review).
- **Talent Community form**: a customizable careers-page form collects name/email (required — "we can't create new profiles in your Gem project without this info"), phone, LinkedIn URL, company, resume upload ("will upload an attachment to the Gem profile"), and custom questions captured as project custom fields.
- **Duplicate prevention**: "If a person registers who already exists in your Gem instance… a duplicate profile won't be created; we'll just cross-list them into the event project." One person → one profile, many project memberships.
- **Prospect Search** searches across Gem CRM candidates **and** ATS candidates (Greenhouse, Lever, Workday, SuccessFactors, SmartRecruiters, iCIMS). Saved-search automations; filters guide; "Likely to Move" filter.
- **ATS rediscovery**: indexes ATS candidates into search; distinguishes ATS-only candidates from Gem profiles via a "Who added to Gem" column (ATS icon vs user icon). Default result set **excludes candidates with active applications or hired status**; an "Include active candidates" checkbox overrides. ATS-application filters: job (with requisition number), candidate tags, rejection reason, reached interview stage (at-least semantics), scorecard positive-feedback percentage, "exclude strong negative", "last in process" (used to operationalize cool-off periods).
- **Deduplication**: "Gem has robust deduplication efforts… 4 candidates could have the same name, but Gem may collapse them all into one row… if we're confident that they're all the same person."
- **Actions on search results**: add to Project, add to Sequence (outreach), bulk log activity, bulk set reminder.
- CSV upload into projects; custom fields; project fields; cross-domain project sharing; transferring candidates between projects; sharing projects.

### SeekOut (Tier-1 — help center)

Evidence layer: A.

- Help center has a dedicated **Candidate Profiles** collection: "Learn how candidate profiles are created, enriched, and organized in SeekOut. This section covers profile imports, data enrichment, notes, tags, and status management."
- **Profile creation by bulk upload + enrichment**: start from a basic list (name, location, company, title, LinkedIn URL, emails, phones) in a template spreadsheet; upload into a Project; SeekOut "automatically enrich[es] the data with their full background, education, profile photos, and contact information." LinkedIn URL recommended for best match results.
- **Import from LinkedIn Recruiter**: export recruiter-project profiles into SeekOut, "which enriches them with full background, education, photo, and contact info."
- **Profile maintenance**: Private Notes vs Shared Comments (distinct purposes); Tags and Statuses (admin-managed tag/status sets for the organization).
- **Contact information**: plan includes credits for requesting candidate emails/phones; letters next to contact info depict the kind of source found; "SeekOut is not a primary source of candidate contact info and we do not build a database of contact info about candidates"; failed lookups don't consume credits.
- **Export**: candidate profile → PDF (to share with hiring manager; data depends on plan); data → Excel/CSV; export to ATS (credit-counted).
- **Projects**: "A Project in SeekOut is a workspace to save candidates for a job, collaborate with your team, and share talent with hiring managers." Add single/multiple/whole-page candidates; remove; duplicate project or selected candidates; archive (recoverable) vs delete (permanent); search projects by name.
- **Sharing**: share projects with teammates and hiring managers with view/comment control; shared-project access via free account.
- **Clone a candidate** "to find more people with similar experience."
- **Search**: 1B+ external profiles + own ATS (rediscovery); 30+ smart filters (marketing page); Chrome extension to source and enrich profiles from any website.
- **Candidate FAQ**: find a candidate by LinkedIn URL; profile freshness — "Profile discrepancies may occur if a candidate recently changed, privatized, or deleted their public info."

### Beamery (Tier-2 — product pages)

Evidence layer: A for the pages' own claims; treated as positioning-level (no help-center docs reachable).

- Product named **Talent CRM**: "Power skills-based hiring with the candidate data you need to proactively recruit and build pipelines of qualified talent."
- "Assess candidates' skills at a glance through **smart profiles**, fully integrated with your ATS. Create targeted **talent pools**… easily **resurface silver medalists** to shorten your time to hire."
- "Unlock a **360 view of your talent pool**: Gather accurate, up-to-date talent information in one place. **Collect profile updates and preferences directly from individuals or their public profiles**, and **manage consent campaigns** effortlessly. **Integrate employees directly from your HCM** to consider internal and external candidates for every role."
- "Eliminate manual data entry and system switching" (AI assistance, automated workflows).
- Enterprise posture: customizable workflows, compliance automation, flexible user permissions, data residency options, high-volume processing.
- Customer quote (BBVA): "Every employee and potential prospect that ever came to BBVA will be in Beamery's Talent CRM, along with their skills."
- Blog title documents the category seam: "ATS vs CRM: Why do you need a recruitment CRM? — …for compliantly storing the details of people who were not selected for roles, in order to keep in touch."

### Eightfold AI (Tier-2 — product pages; docs login-gated)

Evidence layer: A for page claims; positioning-level.

- Self-description: "agentic talent intelligence company… the intelligence to see, develop, and deploy the full depth of talent."
- Profile-centric data claims: "1.6 billion career trajectories and 1.6 million skills — proprietary data"; "One billion profiles puts the intelligence in AI."
- Talent Acquisition page: "a complete, up-to-date view of talent, so you can look beyond résumés and identify true potential"; "talent rediscovery" (Activision stat); "360-degree view of internal talent"; skills-based matching.
- Products span Talent Acquisition, Talent Management, Resource Management, Workforce Exchange — the profile layer feeds all of them ("Deep talent intelligence powers each decision").

### Greenhouse Recruiting (Tier-1 — ATS boundary anchor)

Evidence layer: A.

- "The candidate profile is one of the most important pages in Greenhouse. It's where recruiters, hiring managers, and the rest of the hiring team come together to participate in structured hiring."
- Profile organized into header (name, pronouns, contact info, time zone, tags; actions: email, add/transfer to another job, update status), main panel (**Stages** — planned interviews, scheduling, scorecards; **Scorecards**; **Offer details** — approvals, documents, offer packet; **Activity feed**), right panel (Candidate details, Application details — applied-when/referrer/recruiter/coordinator, **All jobs** — "a candidate's full history across jobs, including active and past applications with their outcomes", Notes with @mentions, Tasks and reminders, Private mode toggle).
- Merge duplicate candidate profiles (choose primary profile; others merged into it).
- Candidate tags "organize and filter candidates by custom identifiers."
- Interpretation: inside the ATS, the profile is the **pipeline record** — its center of gravity is stages/scorecards/offers for specific jobs; the "All jobs" tab aggregates the person's application history. The person record exists, but the workflow spine is the application.

## Cross-product Comparison

| Dimension | Gem | SeekOut | Beamery | Eightfold | Greenhouse (ATS anchor) |
|---|---|---|---|---|---|
| Managed object | Person profile (candidate/prospect) in CRM "People" | Person profile (sourced/imported/enriched) | Person profile in "Talent CRM" ("smart profiles") | Deep AI profile (skills/potential inferred) | Person profile bound to job pipeline |
| Profile independent of application? | Yes — profiles exist outside ATS; ATS candidates indexed separately; active/hired excluded by default | Yes — sourced profiles pre-application; ATS rediscovery surfaces past applicants | Yes — "people who were not selected for roles" kept compliantly; passive contacts nurtured | Yes — profiles span internal + external talent | No — profile is the pipeline record (stages/scorecards/offers); All-jobs history is a view |
| Population sources | Forms (talent community), CSV upload, Chrome extension, ATS sync/index | External 1B+ index, bulk upload + enrichment, LinkedIn Recruiter import, Chrome extension | Individuals' updates, public profiles, HCM employees, ATS integration | External corpus (1.6B trajectories claim) + internal HCM | Applications, referrals, LinkedIn RSC export, sourcing |
| Organization layer | Projects (+ default Scratchpad), talent pools, custom/project fields | Projects (workspaces per job), tags, statuses | Talent pools (targeted) | (Not directly observed — docs gated) | Jobs/pipelines; candidate tags |
| One-person-one-record rule | Yes — dedup collapses same-person rows; form registration cross-lists instead of duplicating | Implied — enrichment matches on identity (LinkedIn URL "for best results"); merge not directly observed | Implied — "360 view… in one place" | Implied — unified profile per person | Yes — explicit merge-duplicate-profiles machinery |
| Consumption | Prospect Search (CRM + ATS), profile page, project lists | Search (external + ATS), profile page, project lists, PDF/Excel export | Search/pools (page-level claims) | Matching/rediscovery (page-level claims) | Pipeline review per job |
| Collaboration | Share projects, cross-domain sharing, bulk actions | Share projects w/ view-comment control, notes/comments, hiring-manager share | Flexible user permissions (claimed) | (Not observed) | Job-level roles, notes/@mentions, private mode |
| Handoff | Add to Sequence (outreach), export; ATS is a *source* | Export to ATS/spreadsheet/PDF; contact-info credits | ATS integration ("fully integrated") | Feeds TA suite + agents | IS the system of record |
| Metering | Not observed in fetched docs | Contact/export credits | Not observed | Not observed | n/a |
| AI posture | AI overview product line; saved-search automations | AI search/scores/sam screening; clone-similar | AI assistance (claimed) | AI-native intelligence core | AI scorecard summaries, scheduling suggestions |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Person-level candidate profile as the managed object** — one identified record per person (identity + contact), with keeping-one-record-per-person (dedup/merge) as the integrity rule.
2. **Structured profile content about the person** — background (experience/education/skills), documents, and recruiter-added context (notes/tags/status) held on the record.
3. **Persistence across hiring processes** — the profile exists before, between, and after any specific application; it is not bound to a requisition, job, or pipeline stage.
4. **Hiring-organization-side operation and consumption** — the employer's recruiting users create, organize, search, view, and act on profiles.

Removal tests:
- Remove #3 (bind the record to a requisition's pipeline) → the profile becomes the ATS candidate record; the Type collapses into the ATS.
- Remove #1/#2 (no persistent person record; queries over an external corpus without retained profiles) → a candidate search engine, not a profile platform.
- Remove #4 (candidates own and control the surface) → a professional network or two-sided job marketplace.

### L1 — Common Mature Structure

- **Multi-source profile population**: external profile search/indexes; imports (professional-network exports, CSV/bulk upload); automatic enrichment (background, education, photo, contact info) from partial seeds; candidate self-service forms (talent-community signups); sync/index from the ATS; employee records from the HCM for internal-talent use.
- **Organization layer**: projects/pools/talent communities that group profiles (per role, per campaign, per community), with one profile able to belong to many groups; custom fields; tags and statuses.
- **Consumption surfaces**: profile detail page; searchable database/list views; saved searches.
- **Collaboration**: sharing pools/projects with teammates and hiring managers (view/comment granularity in some products); notes/comments; @mentions.
- **Handoff/export**: export to spreadsheet/PDF; push/sync to the ATS; contact-info retrieval for outreach.
- **Dedup/merge machinery** keeping one record per person across sources.
- **Outreach attachment**: sequences/campaigns operate on profile selections (capability shared with sourcing tools).

### L2 — Variant / Optional Structure

- AI depth: enrichment, skills inference, similar-candidate recommendation ("clone"), fit scores, rediscovery ranking, AI screening layers.
- Internal-talent extension: employees as profiles (internal mobility, redeployment).
- Consent/privacy machinery: consent campaigns, data-retention posture, candidate privacy pages.
- Metering economics: contact/export credits (product-dependent).
- ATS relationship posture: one-way export vs two-way sync vs index-only.
- Candidate-facing self-service depth: profile updates, preference collection.
- Agency mode: staffing-firm use (client submission flows).
- Scale posture: giant external corpus vs own-database-only.
- Two-sided marketplace form (candidate-authored profiles browsed by employers) — different Type, see boundaries.

### L3 — Vendor-specific (research notes only)

- Gem: "My Scratchpad" default project; "Who added to Gem" ATS-vs-user icon; "Include active candidates" checkbox; scorecard-percentage and "exclude strong negative" filters (Greenhouse-only option); "last in process" cool-off filter; cross-domain project sharing; supported-ATS list (Greenhouse, Lever, Workday, SuccessFactors, SmartRecruiters, iCIMS); Standard/Advanced CRM package gating.
- SeekOut: bulk-upload template column set; up-to-100-candidates-per-page add; letters next to contact info denoting source kind; no-credit-on-failed-lookup; PDF export contents vary by plan; archive-vs-permanent-delete semantics; clone-candidate; "SeekOut is not a primary source of candidate contact info" statement; 1B+ profiles and 44%-of-hires-from-ATS marketing claims.
- Beamery: "smart profiles"; consent campaigns; data-residency options; 120-countries/25-languages customer claims; Everest "Candidate Engagement Platforms" placement.
- Eightfold: 1.6B career trajectories / 1.6M skills claims; TalentForge build layer; agentic AI positioning; ISO 42001/FedRAMP badges.
- Greenhouse: three-panel profile redesign; keyboard shortcuts (R/X/M); private mode; pronouns/preferred-name fields; AI scorecard summaries.

## Rejected Findings (not promoted)

- "The platform has 1B+ profiles" (SeekOut/Eightfold marketing) — vendor scale claim, not a Type property; profile platforms can operate on employer-owned databases only.
- "Contact info is included" — in at least one product the vendor explicitly states it is *not* a primary source of contact info and meters retrieval; contact retrieval is optional/metered, not definitional.
- "AI matching/skills inference" — present in the AI-intelligence pole and increasingly common, but the CRM-first poles work without it; era-common, not defining.
- "Outreach sequences" — attached in several products but owned by the sourcing/engagement capability; a profile platform without outreach still exists (export-to-ATS-only postures).
- "Talent pools must map to jobs" — pools also organize communities/events/campaigns; job-alignment is a best practice, not a rule.

## Boundary Findings

1. **vs Applicant Tracking System (sharpest seam).** The ATS's candidate profile is the pipeline record: its center of gravity is stages, scorecards, offers for specific jobs (Greenhouse evidence). The standalone profile platform's center of gravity is the person record outside the pipeline: pre-application prospects, silver medalists, passive talent, talent communities. Gem's own docs operationalize the seam: ATS candidates are indexed *into* profile search, flagged as ATS-sourced, and candidates with active applications are excluded by default. Removal test: remove the requisition/pipeline workflow → profile platform; remove the standalone record layer → ATS. The two interlock (CRM feeds ATS at application; ATS feeds CRM at rejection/rediscovery).
2. **vs Candidate Search Platform.** Search is a core *capability* here, but the managed object is the persistent profile record, not the query. A search platform can answer "who matches this query?" over a corpus without retaining curated person records; a profile platform's value is the maintained record. SeekOut straddles deliberately (search-first product with a profile-management core) — flag for joint review when candidate-search-platform is processed.
3. **vs Talent Sourcing Platform.** Sourcing is the identification/outreach *activity*; the profile platform is the *record layer* those activities deposit into and draw from. Products bundle both; the seam is the managed object.
4. **vs Recruitment Marketing Platform (processed 2026-09-07).** Marketing owns pre-application audience attraction (campaigns, career site, distribution); this leaf owns the record layer the attraction converts into. The talent-community signup form is the seam: marketing captures → a profile is created. Consistent with that pass's boundary notes.
5. **vs Resume Builder.** Candidate-side document authoring vs employer-side record management. The resume is one *input artifact* to the profile (uploaded/parsed); the profile is the structured, living record.
6. **vs Professional Social Network.** The social network's profile is the person's public self-presentation on a shared graph; the candidate profile platform's record is the employer's private working record about that person. Public-profile data may *feed* the record (with freshness drift documented by SeekOut's FAQ), but the surfaces, ownership, and rules differ.
7. **vs CRM (sales).** Same record-relationship pattern (person records, pools, notes, activity); different domain object and lifecycle (candidate vs customer/deal). Noted as pattern-level kinship only.
8. **Two-sided profile marketplaces** (candidate-authored profiles that employers browse, e.g. curated talent marketplaces): different Type — the platform operates the marketplace and the candidate owns the profile; not sampled this pass, recorded as a boundary note without product claims.
9. **Taxonomy note.** "Candidate Profile Platform" is not a name the market uses for a category; the market says Talent CRM / Candidate CRM / Talent Engagement Platform / Talent Intelligence Platform, and every ATS also ships a "candidate profile" as its central record. The referent (the standalone profile-record layer) is real and commercially significant, but the leaf name is a descriptive construction, and the Type is real specifically as the profile-first pole outside the ATS pipeline.

## Historical / Market-Sample Check

- A staffing agency's pre-digital candidate card index or resume shelf (person + background + contact + recruiter notes, kept across assignments and clients) satisfies the minimal core with zero digital machinery — no external corpus, no AI, no cloud. The definition holds.
- Regional European recruiting CRMs built around consent-gated talent pools fit the same core (consent machinery is L2, not defining).
- Early ATS-era "candidate databases" (resume banks searched by recruiters) also fit: person records + structured content + persistence + recruiter consumption.
- Therefore the canonical core is era-robust: person-level record + structured content + cross-process persistence + employer-side consumption. External corpora, enrichment, AI, credits, and HCM sync are era-common implementations, not invariants.

## Uncertainties

- Beamery and Eightfold evidence is product-page level only (helpdesk/docs unreachable); their internal profile mechanics (fields, dedup, permissions) are not directly observed and no claims in the final document depend on them.
- Whether a pure-play standalone "profile-only" product exists with no search and no outreach was not established; the sampled market always bundles search and/or outreach. The Type is therefore documented as a record-layer core with common attached capabilities.
- The two-sided marketplace boundary was reasoned structurally, not sampled.
- Exact permission models inside profile platforms (beyond "sharing with view/comment" in SeekOut and "flexible user permissions" claims in Beamery) were not directly observed; kept general in the final document.

## Final Synthesis

A Candidate Profile Platform is the hiring organization's system of record for **people who might be hired** — as distinct from the ATS's system of record for **applications in a hiring process**. Its defining core is small: one persistent, structured, person-level profile per candidate (dedup/merge enforced), existing before/between/after any specific application, operated and consumed by the employer's recruiting side. Around that core, mature products add multi-source population (external indexes, imports, enrichment, self-service forms, ATS/HCM sync), organization into pools/projects/talent communities, search and profile-view consumption, collaboration and sharing, export/ATS handoff, and — in the current era — AI enrichment/matching. The market realizes this Type under names like Talent CRM, Candidate CRM, Talent Engagement, and Talent Intelligence, and the same products usually straddle into search and outreach; the leaf's identity rests on the managed object (the profile record), not on any single capability.
