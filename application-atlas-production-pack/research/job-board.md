# Research Notes — Job Board

Research date: 2026-09-07
Leaf: Job Board (Directory §09 HR, Workforce & Talent)
Slug: job-board

## Research Goal

Understand, from real products, what a Job Board is as an Application Type: what objects exist inside it, how the two sides (employers posting openings, job seekers looking for work) interact through it, what lifecycle the posting has, what machinery has become standard on both sides, and where its boundary sits against adjacent Types (Career Site Platform, Classifieds Platform, Listings Platform, Marketplace, ATS/Recruiting, Candidate Search Platform, Professional Social Network, Association Job Board, Public Employment Service Platform).

## Initial Boundary (hypothesis before research)

A Job Board is a third-party-operated venue where many independent employers advertise job openings as time-limited postings, job seekers search/browse the aggregated population, and each posting carries a response path back to the posting employer. The board is the meeting place, not the hiring system.

Expected confusions:
- Career Site Platform (one employer's own public surface — ownership test flagged by the career-site-platform pass)
- Classifieds Platform (ad-contact model without candidate machinery — flagged by the classifieds-platform pass)
- Listings Platform (generic expiring-offer Type)
- Online Marketplace (transaction mediation)
- ATS / Recruiting Management Platform (employer-side pipeline system of record)
- Candidate Search Platform (opposite direction: employer→people)
- Professional Social Network (profile/feed network with a Jobs surface)
- Association Job Board (membership-org operator variant — flagged by that pass for joint review)
- Public Employment Service Platform (§24, government operator)

## Research Questions

1. What is a job posting — its content structure and its lifecycle/states?
2. Who are the actors and what does each side do?
3. How do seekers discover postings (search, filters, alerts, recommendations, collections)?
4. What response/apply paths exist (in-platform, redirect, email/contact)?
5. What does the employer side look like (account, posting creation, promotion/budgets, applicant handling, performance metrics)?
6. Is a resume/profile database a standard employer-side layer?
7. What monetization shapes exist (per-post, per-click, subscription, credits, free, seeker-pays)?
8. What operator types exist (general commercial, niche, government/public employment service, association, review-attached, aggregator)?
9. Where exactly do the boundaries with the adjacent Types sit, and which prior-pass tests must be adopted?

## Representative Products

Selected for market representativeness, documentation completeness, and different product philosophies / operator models / customer tiers:

| Product | Pole | Evidence tier |
|---|---|---|
| LinkedIn (Jobs surfaces) | professional-network-native board; richest seeker-side mechanics; promoted postings | Tier-1 official Help Center (multiple articles) |
| Monster | classic general commercial board, self-serve employer platform (Monster+), pay-for-performance promotion, resume search product | Tier-1 official hiring site + Help Center articles + product pages |
| USAJOBS | government-operated multi-agency employment site (public-employment pole); structured announcements; application tracking | Tier-1 official Help Center (.gov) |
| RemoteOK | niche (remote-work) board; salary/benefits-attribute filtering; paid posting; minimal machinery | Tier-1 official site itself (self-documenting surface) |

Attempted and blocked (network-restricted environment): Indeed, ZipRecruiter, SEEK, Glassdoor, Craigslist, We Work Remotely, Wellfound, FlexJobs, Dice, Jooble, Adzuna, jobboard.io (403/401/404/timeout/transport errors). Market-context only; no product claims made about them in either file.

## Sources

- LinkedIn Help: "Search and Apply for Jobs" topic (49 articles listed), incl. "Apply for jobs on LinkedIn" (a512388), "Apply to jobs directly on LinkedIn" (a512348), "Job alerts on LinkedIn" (a511279), "Filter and sort job search results" (a507441), "Promoted jobs and the Why am I seeing this job? feature" (a7181681), "Job recommendations based on your preferences and profile" (a512279), "Manage jobs you saved on LinkedIn" (a513247), "Track and organize job opportunities" (a8684146), "What to expect after you apply" (a508716), "Sharing your full profile with job posters" (a512339), "Apply with LinkedIn for members" (a507542), "Share and manage your resumes with recruiters" (a1327213), "Visibility and usage of your uploaded resume" (a506429), "Upload your resume" (a510363), "Manage job alerts" (a1420165), "LinkedIn's Job Library" (a7436022), "Find jobs on LinkedIn – Best Practices" (a509392), "Privately Looking for a Job" (a512233). https://www.linkedin.com/help/linkedin
- Monster: Help Center (https://hiring.monster.com/help-center/), "Getting Started with Monster+" (…/getting-started-with-monster/), "Manage Your Monster+ Job Postings" (…/manage-your-monster-job-postings/), "Post a Job" product page (https://hiring.monster.com/products/post-a-job/), "Resume Search" product page (https://hiring.monster.com/products/resume-search/), seeker homepage (https://www.monster.com/)
- USAJOBS: Help Center "How to…" (https://help.usajobs.gov/how-to), "How to understand the job announcement" (…/how-to/job-announcement), "About USAJOBS" (https://help.usajobs.gov/about)
- RemoteOK: https://remoteok.com/ (front page = the product surface: filters, sorting, salary/benefits attributes, post-a-job, premium, JSON feed)

All fetched 2026-09-07.

**Source-access limitation:** the largest consumer boards (Indeed, ZipRecruiter, SEEK, Glassdoor) and the classifieds pole (Craigslist) could not be fetched. Market-structure statements about them are treated as context only. No precise market-share, pricing, or limit claims are asserted for any blocked product anywhere in the outputs. Precise numbers observed (Monster plan prices/credit costs, USAJOBS activity counts, LinkedIn resume-storage counts) are recorded here in Research Notes only and are not carried into the Application Document as general claims.

## Product A — LinkedIn (Jobs surfaces)

Evidence layer: A (direct, official help articles).

### Key observations
- Two response modes documented explicitly: **Easy Apply** (application submitted inside LinkedIn; popup screens → review → submit) and **Apply** ("you'll be routed to that company's website or job board to continue the application process"). This is Tier-1 evidence that the redirect-to-employer mode and the in-platform mode coexist, and that "job board" is used in market vocabulary as the destination category.
- Application is bound to the poster: "the job poster will have the option to review your application"; for Easy Apply the seeker receives "application updates" including when the poster views the application; applications cannot be edited/withdrawn once submitted.
- Discovery: search with filters (location, remote, part-time, contract…), sort, **job alerts** (daily/weekly, email and/or app notifications), **saved jobs**, **job recommendations** based on profile and preferences with a "Why am I seeing this job?" explainer, curated **job collections**, AI-powered natural-language job search, job-match/skills-match insights.
- Seeker-side privacy posture: job-search activity is private by default; no network updates on applying; "Open to Work" is an explicit opt-in signal (recruiter-visible or network-visible variants); "I'm interested" company signal.
- Resume machinery: resumes uploaded for applications are shared with that hirer; resumes can be stored and reused; a **resume-sharing feature** makes the member's resume appear in recruiter search results (employer-side people search over the board's own seeker population). Apply with LinkedIn prefills external applications from profile data.
- Monetization/posting side: jobs appear with a **"Promoted"** label when they are paid posts promoted by companies; a public **Job Library** documents paid job posts that have run on the platform.
- Job tracker: a seeker-side pipeline over opportunities with five stages (saved, in progress, applied, …) — the seeker tracks their own application flow.
- Posting states are visible implicitly (jobs expire/close) — the help corpus documents seeker-side views; employer posting management lives in a separate help topic.

## Product B — Monster

Evidence layer: A (direct, official help-center articles + product pages).

### Key observations
- Employer platform ("Monster+"): "post your jobs, search for candidates, and manage your applicants" — the three employer-side pillars stated verbatim in official help.
- Posting creation: step-by-step posting flow; essential fields "job title, location, salary, benefits, responsibilities, and qualifications"; required fields marked; the posting includes a "preferred application email address" (email as a response path); posting form completable "in a few minutes"; suggestions for job titles, salary ranges and skills; job-description templates library.
- **Posting states documented explicitly**: Draft (saved, not posted), Open (posted, live), Closed (manually removed before expiration date), Expired (hit expiration date). Status actions: edit, view (live ad, "just as seekers see it"), complete, delete; repost = Closed→Open (choose a new promotion budget); remove = Open→Closed. This is the clearest Tier-1 posting lifecycle in the sample.
- Promotion model: pay-for-performance — "choose a daily average budget, and only pay when candidates click on your job"; budget runs as a promotion with a scheduled end date; promotion can be ended at any time; credits system as one bank across promotions, resume views, and message campaigns.
- Distribution network: postings published "on Monster's website, mobile app, + extensive network of job boards and partner sites"; the Pro plan advertises posting to Monster **and CareerBuilder** (cross-brand distribution).
- Auto-matching: "We'll automatically send your jobs to relevant candidates who are looking for roles similar to yours"; daily job alerts to seekers; new-candidate notifications to employers.
- Applicant management (lightweight, board-level): central Jobs list with per-posting columns — applicants count, "needs review" count, views, paid clicks, daily budget, total cost, status; applicant page to "review, rate, and contact candidates"; messaging to applicants; auto-response tool ("let them know that I received their application").
- **Resume Search** as a separate product: database of millions of candidate resumes; filters (location, job title, skills, education, salary, veteran status, experience level, security clearance, resume-updated recency); match-rate percentage on candidate cards; saved searches + email notifications when matching candidates enter the database; candidate comparison view; messaging/drip campaigns with scheduled follow-ups; activity indicator for recently active candidates; metered resume views (credits).
- Team/multi-user accounts; ATS integration at the enterprise tier ("access Monster's resume database directly from within your applicant tracking system"); employer branding / career-site products exist as adjacent offerings.
- Seeker side (homepage): browse jobs by category/title/location, upload resume ("get noticed by top employers"), resume builder, salary tools, career advice, mobile app with one-touch apply.

## Product C — USAJOBS

Evidence layer: A (direct, official .gov help center).

### Key observations
- Operator: the U.S. Office of Personnel Management; "Federal agencies use USAJOBS to host job openings and match qualified applicants to those jobs" — a multi-employer venue (hundreds of agencies) operated by a third party (the government's employment-services operator), not by any one employer.
- **Job announcement structure documented in six sections**: Overview, Duties, Requirements, How you'll be evaluated, Required documents, How to apply — the most explicit posting-content model in the sample. Plus "who the job is open to" (eligibility/hiring paths), locations, benefits, closing types.
- **Closing types**: announcements close (time-bounded postings); closing date semantics documented.
- Seeker machinery: account + profile (work experience, education, federal/military service, languages, hiring paths); **multiple resumes & documents**; "Make your resume and profile searchable" (employer/agency-side searchability); save a job announcement to Saved Jobs; save a search → job alerts; filters (agency/department, appointment type, hiring path, job type, location, pay, security clearance, series, travel percentage, work schedule).
- **Application machinery with tracked lifecycle**: create/save/update/continue an application; cancel; archive; **check on the status of an application** — application states visible to the seeker; contact-an-agency channel.
- Talent networks: seekers can join agency talent networks (standing interest registration distinct from applying).
- Sector-specific structure: the federal "series", "security clearance", "hiring path" facets are regional/sector tuning of the same filter machinery.

## Product D — RemoteOK

Evidence layer: A (the site itself is the product surface; official).

### Key observations
- Niche board scoped to one labor-market segment (remote work); "Post a job" is the employer entry; paid posting with job bundles.
- Postings carry rich **attributes as filters**: minimum salary, benefits (401(k), 4-day week, equity, crypto pay, equipment budget…), regions and countries; open-salary culture in the brand.
- Discovery: category pages, attribute filters, and multiple sort orders (latest, highest paid, most viewed, most applied, hottest, most benefits) — sort-by-demand-signal is board-native.
- Apply: per-posting "Apply for this job" action (external or contact path per posting).
- Seeker premium tier exists (paid access to a larger job set) — the **seeker-pays** monetization variant.
- Machine-readable posting supply: JSON feed / public jobs API.
- Minimal machinery overall: no seeker profile system comparable to the big boards, no applicant management console beyond what posting owners receive — a useful "thin board" datapoint showing what a board can be without the full modern stack.

## Cross-product Comparison

| Dimension | LinkedIn | Monster | USAJOBS | RemoteOK |
|---|---|---|---|---|
| Operator | commercial (network company) | commercial | government (OPM) | independent niche operator |
| Employer population | many employers + recruiters | many employers | hundreds of federal agencies | remote-first companies |
| Posting object | job post (paid/promoted tiers) | job ad with promotion budget | structured announcement (6 documented sections) | posting with salary/benefits attributes |
| Posting lifecycle | posts expire; promoted tier documented | Draft/Open/Closed/Expired documented verbatim | closing types documented | postings listed until removed (lifecycle thin) |
| Seeker identity | full account + professional profile | account + resume | account + profile + resumes & documents | account optional (premium), anonymous browsing |
| Discovery | search+filters, recommendations, collections, AI NL search, alerts | search, categories, alerts, auto-matching | search+11 documented filter facets, saved searches→alerts, hiring-path eligibility | category + attribute filters + demand-signal sorts |
| Response path | Easy Apply (in-platform) or Apply (redirect to employer site/board) | in-platform applicant flow + per-posting application email | in-platform application with tracked status | per-posting apply action |
| Seeker-side tracking | job tracker (stages); poster-viewed updates | — (not documented seeker-side in fetched pages) | full application status machinery | — |
| Employer-side applicant handling | poster reviews applications; updates sent | applicant page: review/rate/contact/messaging/auto-response | agency contact channel | minimal (posting-owner side) |
| Resume/profile database | resume sharing into recruiter search | dedicated Resume Search product (metered) | searchable profile flag | none |
| Monetization | paid promoted posts | pay-per-click budgets, credits, subscription tiers, enterprise | free (public service) | paid posts + bundles; seeker premium |
| Distribution | within network | site + app + partner network (incl. CareerBuilder) | single venue (statutory) | site + JSON feed/API |

### What repeats across the sample (B-layer candidates)
- Employer-posted openings for many employers on one venue (4/4).
- Posting = structured ad: title, organization, location, employment type, compensation, duties/requirements, application instructions/deadline (4/4 in varying explicitness).
- Time-bounded postings with a managed publish/close/expire lifecycle (Monster + USAJOBS explicit; LinkedIn/RemoteOK implied) — "postings are transitory" is safe at B strength.
- Seeker discovery machinery: search + filters + alerts + saved jobs/searches (4/4; recommendations/matching in the two large commercial ones).
- A response path per posting that returns the seeker to the employer's process (in-platform / redirect / email) (4/4).
- Seeker accounts with resumes/profiles where saving, applying, or being searchable requires one; anonymous browsing commonly possible (3/4 direct; RemoteOK partial).
- Employer-side: posting console + applicant inflow with at least a review/contact surface (Monster, LinkedIn, USAJOBS-with-agency; RemoteOK thin) — strength: common, depth varies.
- Resume/profile searchability as an employer-side layer on mature boards (Monster, LinkedIn, USAJOBS; absent RemoteOK) — common, not defining.
- Paid promotion of postings with performance metrics (Monster, LinkedIn, RemoteOK) — common; free public boards exist (USAJOBS).

## Abstraction

### L0 — Defining Invariant

Three properties; remove any one and the product stops being a Job Board:

1. **A population of job postings from many independent employers on one venue.** The unit of supply is the posting: a time-bounded advertisement of one opening at an identifiable employer. The venue is operated by a party institutionally separate from the hiring employers, and the postings carry the employers' identities (the multi-employer/ownership test: one employer's own surface = Career Site Platform).
2. **A seeker-facing discovery surface over that population.** People looking for work can find and compare openings across employers — browse at minimum, search/filters/alerts in modern form.
3. **A response path from seeker back to the posting employer.** Every posting carries or mediates a way for the seeker's interest to reach the employer (apply through the venue, redirect to the employer's own process, or contact details in the posting). The venue never becomes the hiring party; the hiring decision and process remain with the employer.

Historical check (§24 pass): a newspaper's job-classified section (many employers' ads, browsable section, contact-the-employer response), print trade journals, and public employment-office posting books all satisfy these three properties without accounts, payments, search engines, resume databases, or applications. The L0 survives the historical/regional/platform-native check.

### L1 — Common Mature Structure

Standard in modern products but not required to recognize the Type:
- Structured posting content (title, organization, location, employment type, compensation, description with duties/requirements/qualifications, application instructions/deadline)
- Managed posting lifecycle with visible states (draft → live → closed/expired) and actions (edit, renew/repost, remove)
- Seeker accounts with profile/resume/documents; saved jobs; saved searches; job alerts (email/push)
- Keyword search + filter facets (location, category, employment type, compensation, remote…); recommendations/matching of postings to seeker profiles
- In-platform application (forms, resume attachment, screening questions) with per-posting mode selection; application status visible to the seeker in mature products
- Lightweight employer-side applicant handling: applicant list/inbox with review/contact/messaging (and auto-response); per-posting applicant counts
- Employer-side resume/profile searchability (searchable seeker database)
- Paid promotion of postings with budgets and performance metrics (views/clicks/applications); promoted/sponsored labeling
- Posting-creation aids: templates, suggested titles/salary/skills, best-practice guidance
- Multi-user employer accounts; distribution of postings to partner sites/apps (larger boards)

### L2 — Variant / Optional Structure

- Operator model: general commercial board; niche/vertical board (remote, tech, healthcare…); government/public-employment service; association/member board; review-attached board (company reviews/salaries as community content); job aggregator (postings harvested from employer sources with consent — apply still routes to the source)
- Monetization: employer-pays (per-post, per-click/performance, subscription, credit systems), free/public-service boards, seeker-pays premium, advertising-funded
- Posting source model: direct employer posting vs harvested/aggregated vs agency-posted
- Response-mode mix: in-platform apply vs profile-prefill vs redirect vs email/contact
- Seeker-side privacy posture: private-by-default activity, opt-in availability signals (open-to-work), anonymous/minimum-identity browsing
- Seeker-side application tracking (job tracker / application status machinery) — present at different depths
- Sector/regional tuning: eligibility/hiring-path facets, clearance/series fields (federal), salary/benefits attributes (remote/open-salary), statutory structures
- Machine-readable posting supply (feeds/APIs); posting transparency artifacts (public job libraries)
- Attached community content (company reviews, salary data) and adjacent employer-branding/career-site offerings

### L3 — Vendor-specific (research notes only)

- LinkedIn: Easy Apply submission limits (quality measure); up-to-four stored resumes (documented count); Job Library with targeting parameters and impressions for EU paid posts; AI interviews / Hiring Pro screening; InMail-mediated contact; "Why am I seeing this job?" explainer.
- Monster: Monster+ plan prices and credit pricing ($299/mo Pro with 299 monthly credits; $2 per resume view/action; $10 first-promotion verification charge; 30-day budget windows; 25/50/75/100 message batches; 5/10-day follow-ups; SearchMonster comparison fields; Activity Indicator semantics; CareerBuilder cross-posting).
- USAJOBS: ~1,288 jobs posted/day and ~28,438 open/day (official About page); 16M+ accounts claim; login.gov identity; specific filter facet list; talent networks.
- RemoteOK: premium pricing/bundles, discount codes, JSON feed endpoints, toptal cross-promotion.
None of these numbers belong in the canonical document.

## Vendor-specific / Rejected Findings

Rejected as definitional (tested against the sample and the historical check):
- **Paid posting / per-click pricing** — USAJOBS is a full board with no employer payment; niche boards vary. Variant.
- **Seeker accounts and resume databases** — newspaper-era and thin boards satisfy the core without them. L1/L2.
- **In-platform application as the response mode** — redirect and email modes are first-class (LinkedIn Apply, Monster application email). The invariant is the response path, not any one mode.
- **AI matching / AI NL search** — era-common layer on large boards; thin boards run without it. Not definitional.
- **Job tracker / application-status machinery** — depth varies; absent or minimal in the sample's thin pole. L1 (seeker side), L2 depth.
- **Aggregation-only supply model** — Indeed-model harvesting is a posting-source variant, not the definition (direct-posting boards contradict it).
- **Community content (reviews/salaries)** — attached capability of some operators (Glassdoor-class), not board-defining.

## Boundary Findings

- **vs Career Site Platform (§09)** — ownership test, adopted from the career-site-platform pass and confirmed here: whose openings does the public surface list? One employer's own openings under its own brand/domain = career site; many independent employers behind a neutral venue = job board. ATS vendors' hosted single-employer "(external) job boards" are career-site surfaces. The two Types interlock: boards distribute postings; career sites are the employers' own endpoints (and a posting's redirect target).
- **vs Classifieds Platform (§05.03)** — candidate-machinery test, adopted from the classifieds pass: keep only listings without the candidate machinery (seeker profiles/resumes, apply flows, applicant handling) and the product becomes classifieds (Craigslist's jobs category is exactly this pole). The Job Board is the employment listing Type where the two-sided candidate machinery is first-class.
- **vs Listings Platform (§02.11)** — the Job Board is the employment-domain realization of the expiring-offer listing model (the directory-application pass already recorded standing-vs-expiring as the Directory/Listings seam). Generic Listings Platform remains the broader Type.
- **vs Online Marketplace (§05.02)** — nothing is bought through the venue: no cart/checkout/payment between the two sides; the "match" is not a platform transaction. Boards monetize posting placement/visibility, not the hiring act.
- **vs Recruiting Management Platform / ATS (§09)** — the board is not the employer's pipeline system of record: no requisition/approval/interview machinery as the product's center. Boards expose a lightweight applicant surface and integrate with ATSs (Monster enterprise ATS integration documented); the ATS keeps the pipeline.
- **vs Candidate Search Platform (§09)** — direction+object test from that pass: board = seeker→postings; candidate search = employer→people. A board's resume search is the employer-side search layer over its own seeker population, not a standalone corpus-lens sourcing product.
- **vs Professional Social Network (§01.05)** — LinkedIn's primary object is professional identity/network/feed; Jobs is one surface of it. A board's primary object is the posting population. "Network-embedded Jobs surface" is a delivery variant of the board; the network Type stands separately. Artifact test (from the resume-builder pass): board-embedded resume builders produce portable documents → capability slice, not Type straddle.
- **vs Association Job Board (§25)** — machinery identical (employer-submitted postings, seeker search, apply path, member pricing); difference is operator–audience–purpose (membership organization presenting the board as a member service, non-dues revenue). Per the earlier pass: operator/audience variant kept as a separate leaf; ratified from this side; merge decision left to a future taxonomy pass.
- **vs Public Employment Service Platform (§24, unprocessed)** — USAJOBS demonstrates that a government employment site runs the same machinery (postings, structured announcements, applications with status, alerts, searchable profiles) under a public operator. Whether that leaf is an operator variant of Job Board or a distinct Type (with case-management/referral machinery added) is left for that leaf's own pass; recorded as a boundary note.
- **vs Vertical Search Engine (§02.02)** — a pure search surface over harvested postings (Google-for-Jobs-class, no postings of its own, no apply machinery) leans search engine; boards that aggregate but host the response path stay Job Boards. The aggregator pole sits on this seam; flagged below.

## Uncertainties

1. Indeed/ZipRecruiter/SEEK/Glassdoor evidence was unobtainable; the aggregator pole and the review-attached pole are reasoned structurally (LinkedIn's Apply-redirect documentation + Monster partner-network documentation) rather than observed on those products. No claims about them beyond market-context.
2. Whether today's dominant aggregator boards should eventually be split into a separate Type (aggregation machinery without direct posting relationships) — insufficient access to decide; flagged for a future pass.
3. Exact posting-expiration norms (durations, auto-expiry windows) vary by product and were not consistently documented in the accessible sample; no durations asserted anywhere.
4. Seeker-side application tracking depth on Monster could not be verified (seeker help center JS-unreachable); only employer-side flow asserted for Monster.
5. Seeker-pays monetization is evidenced by one product (RemoteOK premium); treated as a variant that exists, not a market norm.

## Final Synthesis

The Job Board is a third-party employment venue whose defining core is three structures: a population of time-bounded job postings from many independent employers under one operator; a seeker-facing discovery surface over that population; and a per-posting response path that returns the seeker's interest to the posting employer, with the hiring process remaining the employer's own. Around this core, mature products add structured posting content and lifecycle states, seeker accounts with resumes/profiles plus alerts and saved searches, in-platform or redirected application modes, lightweight employer-side applicant handling, searchable resume databases, and paid promotion with performance metrics. Operators, monetization, posting sources, response modes, and niche scoping vary widely — the variation is the Type's main variant axis, while the three-property core is stable from newspaper classifieds to network-embedded modern boards.
