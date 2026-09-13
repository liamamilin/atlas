# Research Notes — Public Employment Service Platform

Research date: 2026-09-09
Leaf: Public Employment Service Platform (Directory §24 Government, Public Sector & Civic)
Slug: public-employment-service-platform

## Research Goal

Understand, from real products, what a Public Employment Service Platform is as an Application Type: what objects exist inside it, how the two sides (jobseekers, employers) relate to the operating institution, what machinery beyond posting/search/apply distinguishes it, and where its boundary sits against adjacent Types — above all the pre-hung joint review with Job Board (§09, processed 2026-09-07), which left open whether this leaf is an operator variant of Job Board or a distinct Type with added service machinery.

## Initial Boundary (hypothesis before research)

A Public Employment Service Platform is the digital system of a government public employment service (PES): jobseekers register with the service, employers submit vacancies to the service, and the platform intermediates — search/apply at minimum, plus matching, counseling networks, benefit linkage, and labor-market programs. The operator is not a neutral commercial venue but a public institution with a labor-market mandate.

Expected confusions:
- Job Board (§09) — same posting/search/apply machinery; the joint-review leaf
- Government-as-employer recruitment sites (USAJOBS) — government hiring its own workforce
- Government Service Portal (§24) — general gateway to government services
- Public Benefits Management (§24) — unemployment-insurance/benefit administration
- Social Services Case Management (§24) — counselor casework
- Recruiting Management Platform / ATS (§09) — employer-side pipeline
- Candidate Search Platform (§09) — employer→people direction
- Professional Social Network (§01.05) — profile network with a jobs surface

## Research Questions

1. Who operates these platforms and under what mandate? Is the operator a neutral venue or a party with service obligations?
2. How do vacancies enter the system — who submits them, under what registration/verification, at what cost?
3. What is jobseeker registration — a mere account, or a registered status with the service? What identity machinery exists?
4. Is there active intermediation (matching, referral, invitations, counseling) beyond passive search?
5. Is there benefit/unemployment-insurance linkage in or around the platform?
6. Are labor-market programs (job fairs, mobility schemes, subsidies, training) part of the platform?
7. What employer-side machinery exists (candidate search, dashboards, analytics)?
8. What governance exists (verification, fraud control, misuse reporting)?
9. Where exactly is the seam vs Job Board, and how should the joint review be discharged?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different institutional/geographic layers:

| Product | Pole | Evidence tier |
|---|---|---|
| Job Bank (Canada, jobbank.gc.ca) | full national PES platform; self-identified "Canada's national employment service"; matching both directions; EI linkage; employer verification | Tier-1 official site + support hub (multiple pages) |
| EURES (European Union) | supranational PES federation portal over national PES vacancy databases; human adviser network; mobility schemes | Tier-1 official portal (multiple pages) |
| Find a Job (UK, DWP) | thin national PES listing service; minimal machinery; Jobcentre Plus human layer beside it | Tier-1 gov.uk service pages |
| NCS — National Career Service (India, MoLE) | counseling-centric PES platform; Employment Exchange lineage; free-of-cost mandate; fraud governance | Tier-1 official portal surface |
| USAJOBS (US, from job-board pass) | boundary anchor: government-as-employer multi-agency recruitment venue | Tier-1 evidence fetched 2026-09-07 (job-board pass) |

Attempted and blocked: MyCareersFuture Singapore (JS-rendered shell ×2), France Travail (timeout ×2), jobs.service.gov.uk help (403), canada.ca Job Bank description page (timeout), Job Bank help deep-article URLs (session-bound; hub + surfaced answers fetched instead). The "full PES with in-platform benefit registration" pole (France Travail class) is therefore under-sampled; no claims made about unreachable products.

## Sources

- Job Bank: https://www.jobbank.gc.ca/home , https://www.jobbank.gc.ca/aboutus , https://www.jobbank.gc.ca/employers , https://www.jobbank.gc.ca/helpsupport , https://www.jobbank.gc.ca/support/topic?tid=8&mtid=2 (find-a-job support topic with surfaced Q&A)
- EURES: https://eures.europa.eu/index_en , https://eures.europa.eu/jobseekers_en , https://eures.europa.eu/employers/advertise-job_en
- Find a Job (UK): https://www.gov.uk/find-a-job , https://www.gov.uk/advertise-job , https://www.gov.uk/jobcentre-plus-help-for-recruiters
- NCS (India): https://www.ncs.gov.in/ (portal surface incl. navigation, free-of-cost notice, fraud warning)
- USAJOBS: evidence carried from research/job-board.md (fetched 2026-09-07): https://help.usajobs.gov/how-to , https://help.usajobs.gov/how-to/job-announcement , https://help.usajobs.gov/about

All fetched 2026-09-09 unless noted.

**Source-access limitation:** the deepest operational layers (in-platform benefit registration, counselor casework screens, referral workflows) were not reachable in any sampled product. Assertions about them are held at service-layer strength or recorded as uncertainties. No numeric claims about unreachable products.

## Product A — Job Bank (Canada)

Evidence layer: A (direct, official pages).

### Key observations
- Self-identification: "Job Bank is Canada's national employment service, available as a website and mobile app. We help Canadians find work and plan their careers, and we make it easier for employers to recruit and hire across the country." Delivered by Employment and Social Development Canada "on behalf of the Canada Employment Insurance Commission" (the unemployment-insurance governance body), "in collaboration with provincial and territorial governments."
- Institutional history documented on the About page: 1918 Employment Offices Co-ordination Act → local employment offices; 1940 Unemployment Insurance Act → "organizes the country's hundreds of employment offices into a national employment service"; 1996 Employment Insurance Act → Job Bank website launched, provinces assume "high-touch employment assistance like counselling and training"; 2014 "advanced job search features, such as job matching"; 2018 mobile app. Framed as continuity "from the days of paper job postings pinned to boards" with "a hundred years of experience."
- Employer registration is statutory-identity-verified: user account, then an **employer file** requiring the relationship to the business and the **15-digit payroll account number from the Canada Revenue Agency**; legal business name, sector, size; must indicate whether the business is a recruitment or placement agency; file is **pending review → approved**; approved postings advertised with the mention **"Verified job"**. One employer file per business; multiple files manageable from a dashboard.
- Vacancy authoring inside a controlled occupational vocabulary: job titles must come from the **National Occupational Classification (NOC)** — "Job Bank only uses job titles that are found on the NOC… They don't have the option to modify the title"; 30,000+ job titles and 10,000+ skills offered as structured options; postings automatically bilingual; fields include number of vacancies, part/full time, wages, benefits, required skills/education; option to "indicate that the job is part of a government program" and to market to specific audiences (students, apprentices, veterans, Indigenous people, persons with disabilities, newcomers).
- Job Match, employer side: once posted, the job is "instantly matched to job seekers' profiles that are relevant"; profiles ranked "best match"; employer reviews profiles and clicks **"Invite to apply"** — "Job Bank will notify the job seeker that you are inviting them to apply"; Activity Report shows profiles viewed, invitations sent, seeker activity. Matching modes selectable.
- Job Match, seeker side: Plus account + completed/activated job seeker profile (work experience, skills, education, credentials) → matched to postings; "Employers can access your profile and invite you to apply"; matching modes adjustable; opt-out available; invitation carries a unique code.
- Application machinery: per-posting application methods chosen by the employer — "by mail, in person, by telephone, by email, online, by Direct Apply"; **Direct Apply** = on-platform application (Plus account, uploaded or Resume-Builder resume); employer sees only the resume, not the profile; withdrawal possible within 24 hours; "Resume viewed by employer" flag; **Job Bank Plus promises application-status feedback within 30 days** ("retained or not, or if the job was filled or has expired").
- **Employment-insurance linkage (explicit)**: "You might have been subscribed to Job Alerts by Job Bank to help you look for work **if you recently completed an application for Employment Insurance**." And: an account lets you "track your job search activities **that can be used as proof of your job search efforts**" — the platform participates in the benefit system's work-search requirements.
- Statutory identity: the Social Insurance Number (SIN) — "You also need a SIN to access federal government programs and benefits, **such as Job Bank**." Express Entry (immigration) profile number + job seeker validation code integrate with the platform; foreign job seekers without a valid work permit can only apply to postings open to international candidates.
- Human service network: "Find an employment centre" — "Employment centres offer personalized and in-person assistance for Canadian job seekers all over the country. You can locate your nearest employment centre on Job Bank." Provinces deliver the in-person layer (1996 split documented).
- Labour market information & career planning as first-class sections: job prospects by occupation/location, wage comparisons, trends/reports, career quizzes, field-of-study outcomes; **Available Workers Dashboard** for employers ("search an occupation and see how many workers are seeking jobs locally or across Canada").
- Government programs woven in: Canada Summer Jobs postings, Work-Sharing employer training, temporary-foreign-worker program information, apprentice/student/green-job flags.
- Vacancy supply is mixed: postings from registered employers **plus** "external contributors" — agreements with other job boards (Indeed, LinkedIn, ZipRecruiter, Google, Talent.com, public-service jobs…) — two-way sharing ("We also share our employers' jobs to help optimize their reach").
- Governance: "Report a problem with this job posting" on every posting; misuse reporting against Terms of Use; separate seeker/employer terms.
- Free: "Job Bank's services are free."

## Product B — EURES (European Union)

Evidence layer: A (direct, official portal pages).

### Key observations
- Operator: EURES (EURopean Employment Services), managed by the European Labour Authority; a network of the European Commission + the public employment services of 31 participating countries + partners.
- Vacancy sourcing (definitional sentence): "All jobs on the EURES portal come from the job vacancies databases managed by the Public employment services as well as the EURES Members and Partners of 31 countries." Two vacancy types: "'EURES jobs', which are jobs where an employer has expressed an interest in recruiting from another country, or any other jobs advertised in the national jobs databases."
- Employer path: to advertise, employers use the **national PES self-service systems** or contact the local employment service / a EURES adviser; "you will often need to have a user ID to be able to use the self-service systems and that **some countries require you to be registered as an employer in that country** before you can advertise jobs there." Per-country directory of self-service portals and contacts (France Travail entreprise portal, German Jobbörse, Swedish Arbetsförmedlingen, etc.).
- Seeker side: job search across the pooled vacancies; **My EURES account** (EU login, single/two-factor); Europass CV creation; jobseeker services described as "career guidance and support with your CV… assistance is provided to help you find the best job offers that match your skills. Videoconferencing for interviews can be also facilitated… information about the European labour market, along with legal and social security advice."
- **Human adviser network as a first-class service**: "Contact a EURES Adviser" / "Chat with EURES Advisers" — searchable adviser directory; advisers are the human intermediation layer of the network.
- Employer side: "Find candidates" — CV search over registered jobseeker CVs; employer account creation page.
- Programs: **EURES Targeted Mobility Scheme (TMS)** — "EURES funded support" (a funded labor-mobility program); European Job Days (recruitment events/job fairs, online); EU Talent Pool Pilot.
- Labour market information: living & working conditions per country, labour-market information, shortages/surpluses, job-vacancy insights.
- Cost: "Most of these services are free of charge."
- Scale claims (marketing layer): "Nearly 3 million jobs and 5 000 employers registered on EURES."

## Product C — Find a Job (UK, Department for Work and Pensions)

Evidence layer: A (direct, official gov.uk pages; thin service).

### Key observations
- Service definition: "Find and apply for full or part-time jobs in England, Scotland and Wales" — a national government job-listing service; separate service for Northern Ireland (JobApplyNI); Welsh-language availability.
- Employer side: "Advertise and manage your vacancies on the 'Find a job' service" — sign-in required (create sign-in details if none); free ("You can also advertise a job for free with the 'Find a job' service").
- Human service layer beside the platform: **Jobcentre Plus help for recruiters** — "recruitment advice, including support with your vacancies", work trials ("try out potential recruits"), work experience/apprenticeships advice including the sector-based work academy programme (SWAP), Access to Work support for employing disabled people, Disability Confident guidance.
- Benefit adjacency on the same gov.uk estate: related content links to Universal Credit, Jobseeker's Allowance, "Help with moving from benefits to work" — the benefit linkage lives in adjacent services, linked rather than integrated in the listing service itself.
- Seeker-side operational detail not reachable (service subdomain 403); the thin pole is asserted only from the gov.uk service pages.

## Product D — NCS — National Career Service (India, Ministry of Labour & Employment)

Evidence layer: A (direct, official portal surface).

### Key observations
- Operator: Directorate General of Employment (DGE), Ministry of Labour & Employment, Government of India; toll-free helpline 1514.
- Three registered role families: Jobseekers, Employers, and "Others" — Counsellors, Career Centers, Placement Organizations — each with login/registration; registration flowcharts published as PDFs for jobseekers, employers, government employers, and staffing-federation (ISF) members.
- Jobseeker services: registration; job search (domestic; international via **e-Migrate**; government-sector jobs; jobs for differently-abled, ex-servicemen, women); job fairs and events; career tools; **Find Counsellor**, **Find Career Center**, **Find Skill Provider**; advisories for international jobseekers.
- Employer services: registration (incl. government employers and staffing agencies as distinct flows); **Find Candidates** (search the registered jobseeker population); post jobs; participate in job fairs.
- Institutional lineage visible in-product: **Employment Exchange Portal** (eex.ncs.gov.in) + "List Of Employment Exchange" + EEx statistics — the statutory employment-exchange system (the historical PES institution) is folded into the NCS estate.
- Career infrastructure: Model Career Centers list, counsellor portal, career counseling, skill providers, career schemes, employment-generation schemes and programmes.
- Free-of-cost mandate stated as governance: "NCS services are free of cost. NCS does not charge any fee at any stage of registration, job application, interview processing and other employment related services. Jobseekers should not pay fees to employers." Plus a **blacklisted entities** list and an anti-fraud warning about fake NCS associations.
- Extras (era layer): AI resume builder, AI interview coach, employability assessment partner, mentoring programs, mobile app.

## Product E — USAJOBS (boundary anchor; evidence from job-board pass, fetched 2026-09-07)

- Operated by the U.S. Office of Personnel Management; "Federal agencies use USAJOBS to host job openings and match qualified applicants to those jobs" — a multi-agency venue where the **government is itself the employer**; structured announcements (six documented sections), closing types, seeker accounts/profiles/resumes, tracked application lifecycle, alerts, saved searches, hiring-path eligibility, talent networks.
- Used here only to sharpen the seam: government-as-employer recruitment vs public-employment-service intermediation for the general labor market.

## Cross-product Comparison

| Dimension | Job Bank (CA) | EURES (EU) | Find a Job (UK) | NCS (India) | USAJOBS (US) |
|---|---|---|---|---|---|
| Operator | ESDC for the Canada Employment Insurance Commission + provinces | European Labour Authority + national PES network (31 countries) | DWP / Jobcentre Plus | MoLE Directorate General of Employment | OPM |
| Operator role | public employment service (national) | federation of public employment services | public employment service (listing service) | public employment service + career infrastructure | government as employer (recruitment) |
| Vacancy source | registered employers (CRA-verified employer files) + partner boards | national PES vacancy databases; employers register with national PES | employers (free, sign-in) | registered employers (incl. government, staffing agencies) | federal agencies only |
| Vacancy pool scope | general labor market (private + public sector) | general labor market, cross-EEA | general labor market (GB) | general labor market (incl. international via e-Migrate) | operator's own employer side only |
| Seeker identity | account (Standard/Plus); SIN for federal programs; Express Entry integration | My EURES account (EU login) | account (sign in) | registration (flowchart) | account + federal profile |
| Active intermediation | Job Match both directions + invite-to-apply | EURES Advisers (human) + matching assistance | — (search only; Jobcentre Plus beside) | counsellors/career centers beside search | matching claimed, agency-side |
| Human service network | employment centres locator (provincial delivery) | adviser directory + chat | Jobcentre Plus recruiter services (separate pages) | counsellors, career centers, helpline | agency contact channel |
| Benefit linkage | explicit: EI application auto-subscribes Job Alerts; job-search tracking as proof of efforts; EI Commission governance | advisers give social-security advice | related-content links (UC/JSA/moving-to-work) | not observed | not applicable |
| Programs | Canada Summer Jobs, Work-Sharing, TFW programs, apprentice/student flags | TMS funded mobility scheme, European Job Days, EU Talent Pool Pilot | SWAP, work trials, Access to Work | career schemes, employment-generation schemes, skill providers, job fairs | — |
| LMI / career planning | full section + Available Workers Dashboard | living & working, LMI, shortages insights | — | career planning, reports, dashboards | — |
| Fees | free (stated) | "most services free of charge" | free (stated) | free of cost (stated, governance-grade) | free |
| Governance | employer-file review, "Verified job" badge, misuse reporting, NOC vocabulary control | network membership rules, helpdesk | — | blacklisted entities, fraud warning, free-of-cost notice | structured announcement standards |
| Distribution | two-way sharing with commercial boards (Indeed, LinkedIn, ZipRecruiter…) | single federation venue | single venue | single venue + state portals | single venue |

### What repeats across the sample (B-layer candidates)

1. Public employment service as operator — a government institution with a labor-market mandate, not a commercial venue (4/4 PES products; USAJOBS is the deliberate contrast).
2. Employer-submitted vacancy pool from the general labor market — employers register with the service (with identity verification of varying depth) and submit vacancies; the pool spans the economy, not just the operator's own employment (4/4).
3. Registered jobseeker population — accounts/profiles held by the service; registration flowcharts where formalized (4/4).
4. Seeker-facing discovery over the pool + a response path back to the employer (apply on-platform or through prescribed channels); hiring remains the employer's (4/4).
5. Free of charge to both sides, stated as mandate/governance (4/4 explicit).
6. A human service network layer — employment centres / advisers / counsellors / Jobcentre Plus — locatable or reachable through or beside the platform (4/4).
7. Government labor-market programs attached (job fairs, mobility schemes, summer-jobs, apprenticeships, work trials, foreign-worker programs) (4/4 in different forms).
8. Labour-market information / career-planning content (3/4; absent from the UK thin pole).
9. Employer-side visibility into the registered population (candidate search / matched profiles / Available-Workers-class dashboards) (3/4 observed: Job Bank, EURES, NCS).
10. Governance machinery: verification/badging, misuse reporting, fraud warnings/blacklists (3/4 explicit: Job Bank, NCS, EURES network rules).

### What is NOT universal (rejected as definitional)

- **Two-sided algorithmic matching with invitations** — observed only at Job Bank (Job Match). EURES intermediates through human advisers; UK/NCS show none in fetched pages. Common-mature at best, not defining.
- **Statutory identity verification depth** (CRA payroll account, SIN, Express Entry codes) — Job Bank-specific depth; NCS uses registration flowcharts; UK is sign-in only. Variant depth of the same leg.
- **Controlled occupational vocabulary** (NOC-only titles) — Job Bank only. Product-specific.
- **Application-status feedback with a time promise** (30 days) — Job Bank Plus. Product-specific.
- **In-platform benefit administration** — not observed anywhere in the sample; linkage appears as auto-subscription (Job Bank), advisory (EURES), or adjacent links (UK). The platform is not the benefits system.
- **Immigration/foreign-worker machinery** — regional (Job Bank work-permit gating + Express Entry; NCS e-Migrate). Variant.
- **Two-way posting sharing with commercial boards** — Job Bank network. Variant.
- **AI features** (resume builder, interview coach) — era layer (NCS). Not definitional.

## Abstraction

### L0 — Defining Invariant

Four properties; remove any one and the product stops being a Public Employment Service Platform:

1. **Public employment service as operator.** The platform is operated by (or on behalf of) the government's public employment service — a public institution holding a labor-market mandate for the jurisdiction — and its core services are free to both sides. Remove → a commercial job board (the operator is the defining difference from Job Board).
2. **Employer-submitted vacancy pool from the general labor market.** Employers across the economy — not only the government itself — register with the service and submit vacancies that form the service's vacancy stock. Remove → a government-as-employer recruitment site (USAJOBS pole).
3. **Registered jobseeker population.** People register with the service as jobseekers; the platform holds them as accounts/profiles that the service serves (and, in mature forms, mobilizes — matching, invitations, proof-of-search). Remove → an anonymous vacancy bulletin.
4. **Discovery + response path between the two sides.** Registered jobseekers search/browse the vacancy pool and respond to employers (on-platform application or prescribed channels); the hiring decision and process remain the employer's. Remove → a registry plus a vacancy archive with nothing connecting them.

Jointly-held is load-bearing:
- 1 alone = a government website/portal
- 2 alone = a vacancy database
- 3 alone = a registration system
- 4 alone = a search engine
- 1+2 without 3 = a government vacancy bulletin (the pre-registration-era vacancy board — a partial realization, not the service)
- 1+3 without 2 = a jobseeker registry with no vacancies (the declining employment exchange)
- 2+3 without 1 = a commercial job board with accounts
- 1+2+3 without 4 = an archive nobody connects through

Historical check (§24 pass): the paper-era employment office — employers notifying vacancies to the office, the office registering jobseekers on its rolls, counselors referring them to vacancies, all free under public mandate — satisfies all four legs with zero software. Job Bank's own About page documents exactly this lineage (1918 employment offices → 1940 national employment service under the Unemployment Insurance Act → 1996 website), and NCS still operates its Employment Exchange Portal inside the modern platform. The L0 survives the historical/regional check; no era machinery (apps, matching algorithms, AI, cloud) is named in it.

### L1 — Common Mature Structure

Standard in modern products but not required to recognize the Type:
- Employer registration/verification with the service (business identity checks; review; verified-posting badges)
- Structured vacancy records; in some systems authored inside a controlled occupational vocabulary
- Seeker profiles/resumes (upload and/or builder); document storage
- Search + filters + saved jobs/searches + email alerts
- On-platform application alongside prescribed offline channels (mail/phone/in-person/email)
- Application-status visibility to the seeker (mature forms)
- Two-sided matching (profile↔posting) with employer invitations
- Employer-side search over the registered population / CV database; supply dashboards
- Human service network layer surfaced in-product (employment centres, advisers, counsellors — locators, directories, chat)
- Labour-market information and career-planning content (prospects, wages, trends)
- Government program integration (job fairs, mobility schemes, summer-jobs programs, apprenticeships, work trials, foreign-worker program information)
- Governance machinery (misuse reporting, fraud warnings, blacklists, terms per role)

### L2 — Variant / Optional Structure

- Service architecture: single national platform vs supranational federation over national PES databases vs regional/state platforms
- Benefit-linkage depth: auto-subscription + proof-of-search (benefit-claimant integration) vs advisory-only vs adjacent links vs none observed
- Statutory identity depth: payroll-account verification + national insurance numbers vs registration flowcharts vs simple sign-in
- Occupational vocabulary control: mandatory classification titles vs free titles
- Immigration/foreign-worker machinery: work-permit eligibility gating, immigration-program integration, emigration clearance
- Population-targeted services: youth, Indigenous peoples, newcomers, persons with disabilities, veterans, women, ex-servicemen
- Program portfolio shape: funded mobility schemes, wage-subsidy/work-sharing programs, sector academies, skill-provider directories
- Distribution posture: two-way posting sharing with commercial boards vs closed single venue
- Human-layer depth: full counseling network with in-product contact vs locator only
- Era layers: mobile apps, AI resume/interview aids, mentoring, assessments

### L3 — Vendor/product-specific (research notes only)

- Job Bank: CRA 15-digit payroll account number; NOC vocabulary (30,000+ titles, 10,000–14,000+ skills figures); Standard vs Plus account tiers; 24-hour withdrawal window; weekly employer resume notifications; 30-day application-feedback promise; bilingual auto-posting; "Verified job" badge; Available Workers Dashboard; Express Entry profile number + validation code; Canada Summer Jobs; green/apprentice/student job flags; Work-Sharing training; auto-subscribed Job Alerts after EI application; stats (55,000 jobs/month, 371,000 registered employers, 7.1M posting views/month, 2.4M profile views/month); 1918/1940/1996/2014/2018 timeline; partner-board list.
- EURES: ~3M jobs / 5,000 employers claims; 31 countries; 'EURES jobs' vs national-database jobs distinction; per-country self-service directory; TMS; European Job Days; Europass; EU Talent Pool Pilot; EU login 1FA/2FA article.
- UK: separate Northern Ireland service (JobApplyNI); Welsh version; SWAP; work trials; Access to Work; Disability Confident.
- NCS: helpline 1514; e-Migrate; Employment Exchange Portal (eex.ncs.gov.in); Model Career Centers; ISF staffing-federation registration flow; HireMee employability assessment; AI resume builder/interview coach; blacklisted-entities PDF; ministerial branding.
None of these numbers/artifacts belong in the canonical document.

## Vendor-specific / Rejected Findings

Rejected as definitional (tested against sample + historical check):
- **Algorithmic matching / invite-to-apply** — one product in-sample; human-adviser intermediation is the alternative realization. L1.
- **Statutory identity verification (payroll accounts, national insurance numbers)** — depth varies from statutory verification to simple sign-in; the leg is "registered with the service", not any specific identity proof. L2 depth.
- **Controlled occupational vocabulary** — product-specific governance choice. L3.
- **Benefit administration in-platform** — not observed; linkage is the observed form. Uncertainty recorded.
- **Employer-paid services** — contradicted everywhere (free is stated as mandate); paid promotion absent from all sampled PES platforms. If a government site charges for posting, it is drifting toward commercial-board behavior.
- **Job fairs / events / training directories** — common attached services, not the venue's defining structure. L1/L2.
- **AI features** — era layer. L2.

## Boundary Findings

- **vs Job Board (§09) — JOINT REVIEW DISCHARGED (keep both, distinct Types).** The machinery overlaps (postings, search, apply), but three structural seams separate the Types:
  1. *Operator test*: a Job Board is a venue operated by a party institutionally separate from the hirers, which monetizes placement (or runs as a niche/community service); a PES platform is operated by the government's public employment service under a public labor-market mandate, free to both sides as a stated governance property.
  2. *Vacancy-source test*: a board's postings are advertisements placed on the venue by employers (or harvested); a PES platform's vacancy stock is submitted *to the service* by employers registered with the service — in mature forms with statutory identity verification — forming the service's own vacancy pool.
  3. *Client test*: a board's seeker accounts are venue conveniences; a PES platform's registered jobseekers are the service's clients — served by its counseling network, mobilized by matching/invitations, and (where observed) linked to benefit processes (auto-subscribed alerts after an EI application; job-search tracking "used as proof of your job search efforts").
  - USAJOBS is clarified as sitting on a *different* seam: it is government-as-employer recruitment (the operator's own multi-agency vacancies) — an operator variant of Job Board, not a PES platform. The test: whose vacancies? Operator's own employment → government-as-employer board (Job Board variant); general labor market flowing through the public employment service → PES platform.
  - The Types interlock in the market: Job Bank (a PES platform) two-way-shares postings with commercial boards (Indeed, LinkedIn, ZipRecruiter…) — distribution cooperation across the seam, not Type confusion.
- **vs Government Service Portal (§24)** — the PES platform is a domain-specific service system (employment), not the general authenticated gateway to all government services; a government portal links to it as one service among many.
- **vs Public Benefits Management (§24)** — benefit adjudication/payment (unemployment insurance claims) is a separate system; the PES platform links into benefit processes (auto-subscription, proof-of-search, EI-Commission governance) without administering benefits. Institutional linkage ≠ system identity.
- **vs Social Services Case Management (§24)** — counselor involvement exists, but the platform's center is the labor-market venue and its registered populations, not case files; deep casework machinery is not evidenced in any fetched source (uncertainty recorded).
- **vs Career Site Platform (§09)** — ownership test from that pass: one employer's own openings vs the service's multi-employer pool. A government-as-employer site (USAJOBS) is closer to a multi-entity career presence than to a PES platform.
- **vs Recruiting Management Platform / ATS (§09)** — the PES platform is not the employer's pipeline system of record; employers keep their own hiring process; the platform's employer side ends at posting + candidate visibility + application inflow.
- **vs Candidate Search Platform (§09)** — employer-side search over the PES's own registered population is a layer of the platform (direction+object test from that pass), not a standalone corpus-lens sourcing product.
- **vs Professional Social Network (§01.05)** — no social graph/feed; identity is a service registration, not a professional profile network.
- **vs Staffing Agency Management (§09)** — placement agencies register as a role on PES platforms (NCS ISF flow; Job Bank agency flag) but the platform is not an agency's client/order management system.
- **vs Training/LMS-family Types** — skill-provider directories and training resources are attached services; the platform's center is placement intermediation.

## Uncertainties

1. The "full PES with in-platform benefit registration" pole (France Travail class; also Bundesagentur für Arbeit, Platsbanken, MyCareersFuture) was unreachable — benefit-linkage depth is asserted only where observed (Job Bank explicit; EURES advisory; UK adjacent links). Whether any PES platform administers benefit claims in-platform is **not claimed either way**.
2. Vacancy-notification obligations (employers legally required to notify vacancies to the service) are historically known in some jurisdictions but not evidenced in fetched sources — not asserted.
3. Formal counselor-initiated *referral* workflows (counselor assigns a specific vacancy to a specific jobseeker) were not documented in fetched sources; intermediation is evidenced as adviser services (EURES), matching/invitations (Job Bank), and counseling networks (NCS, UK). Held at service-layer strength.
4. NCS deep pages (registration flowchart PDFs, employer FAQ) not fetched — NCS observations limited to the portal surface.
5. UK Find a Job seeker-side help unreachable (403) — the thin pole's seeker machinery asserted only from gov.uk service pages.
6. Seeker-side application tracking on the thin pole unverified; status machinery asserted only for Job Bank Plus.

## Final Synthesis

The Public Employment Service Platform is the government employment service's digital system of labor-market intermediation. Its defining core is four jointly-held structures: a public employment service as operator (public mandate, free to both sides); an employer-submitted vacancy pool drawn from the general labor market; a registered jobseeker population held by the service; and a discovery-plus-response path connecting the two sides, with hiring remaining the employer's. Around this core, mature platforms add verified employer files, controlled vacancy vocabularies, seeker resumes and alerts, on-platform application with status feedback, two-sided matching with invitations, employer-side candidate search and supply dashboards, the human counseling network surfaced in-product, labour-market information, and government labor-market programs. Benefit linkage, immigration machinery, population-targeted services, and distribution deals with commercial boards vary by jurisdiction. The Type is distinct from the Job Board: the operator's public mandate, the service-owned vacancy pool, and the registered jobseeker as the service's client separate the two — while USAJOBS-class sites sit on yet another seam, as government-as-employer recruitment. The paper-era employment office — vacancy notifications in, jobseeker rolls, counselor referral, all free — satisfies the core with no software, and the sampled platforms themselves document that lineage.
