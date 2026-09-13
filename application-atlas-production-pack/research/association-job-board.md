# Research Notes — Association Job Board

## Research Goal

Understand what an Association Job Board actually is as an Application Type: who operates it, who uses it, what objects exist inside it, how a job posting moves from submission to expiry, how membership ties into it, how it generates revenue for the operator, and where its boundary lies against the generic Job Board, AMS suites, member community platforms, and classifieds.

## Initial Boundary

- Placed in DIRECTORY section 25 (Nonprofit, Membership & Religious Organizations), near Association Management System / AMS, Member Portal, Member Community Platform, Member Directory.
- A generic "Job Board" leaf exists in section 09 (HR, Workforce & Talent). The central boundary question: is Association Job Board a distinct Type or merely an audience/operator Variant of Job Board?
- Initial hypothesis: the job-matching machinery (posting, search, application) is shared with generic job boards; what may distinguish the Type is the operator (a membership/professional organization), the audience (its own professional community), the purpose (member benefit + non-dues revenue + engagement), and membership integration (SSO, member pricing, AMS sync).
- Nearest confusions: AMS career-center modules, member community platforms with jobs features, career site platforms (employer-owned recruiting sites), classifieds platforms with a jobs category.

## Research Questions

1. What are the core objects? (job posting, employer account, job seeker/resume, application, categories, packages?)
2. Who are the actors and what does each do? (association staff, employers, job seekers/members)
3. What is the posting lifecycle: compose → submit → review/approve → publish → expire/renew?
4. How does membership bind into the board: SSO, member data sync, member vs non-member pricing, member-gated features?
5. How is the board packaged: standalone career-center vendor, AMS module, community-platform add-on?
6. What revenue mechanisms exist: per-post pricing, packages, featured placement, resume database access, advertising, career fairs; who sells (association staff vs vendor on the association's behalf)?
7. What interfaces exist for each actor?
8. What separates this Type from a generic Job Board?

## Representative Products

| Product | Vendor / position | Why selected |
|---|---|---|
| Careers powered by Momentive (Formerly YM Careers) | Momentive Software (Community Brands lineage) — the dominant association career-center vendor | Market leader; association-only focus; revenue-share model; employer network across ~3,000 associations |
| Web Scribble | Independent career-center software for associations and higher ed | Deep documentation; explicit employer purchasing and seller-operating models; powers the jobs add-on of a community platform (see Higher Logic) |
| Madgex | A Wiley business unit — career centers for associations and publishers | UK/international angle; full-service partner vs technology-only philosophies; publisher-run boards |
| Higher Logic Thrive Jobs | Community platform with jobs add-on powered by Web Scribble | The community-embedded packaging variant |

JobTarget / JobBoard.io was considered as a fifth sample (self-serve job board platform used by associations and its employer-side distribution network). The vendor's main site (employer recruitment platform, 25,000+ board distribution) was reachable, but the job-board-platform product pages were not (403); kept as a representative market mention with a source-access limitation, not as a claim source.

## Sources

- https://www.ymcareers.com/ (root; fetched 2026-09-06) — positioning, modules, network claim, client logos
- https://momentivesoftware.com/solutions/career-centers-software/ym-careers/overview/ (fetched 2026-09-06) — niche association job board positioning, recruitment ad sales team, zero start-up costs
- https://www.webscribble.com/ (root; fetched 2026-09-06) — three-actor structure, outcomes, integrations list
- https://www.webscribble.com/job-board-software (fetched 2026-09-06) — richest operational evidence: actors, employer purchasing items, member rates, admin reports, resume DB, alerts, filters, SSO/AMS, FAQ (explicit generic-vs-association distinction)
- https://www.madgex.com/ → Wiley "Madgex" page (fetched 2026-09-06) — full-service vs technology-only career centers, insights/reporting, employer branding/advertising, scale stats
- https://www.higherlogic.com/thrive/add-ons/ (fetched 2026-09-06) — Jobs listed as an add-on "powered by Web Scribble"
- https://www.higherlogic.com/thrive/jobs/ (fetched 2026-09-06) — jobs in community feed, built-in search, community profile integration, SSO, non-dues revenue, non-member applicant pipeline
- https://www.jobtarget.com/ (root; fetched 2026-09-06) — employer-side multi-board distribution platform (context only)
- https://support.jobtarget.com/jobtarget-help-center (fetched 2026-09-06) — employer help-center categories (context only)

### Source-access Limitations

- ymcareers.com product subpages (/job-board-software/, /revenue-engine/enhancements/) returned 403 after retries; only the root page was used. Product-module claims for YM Careers are therefore kept at the level visible on the root page.
- jobboard.io returned 403 on two attempts; abandoned. No JobBoard.io-specific claims are made.
- help.highestlogic.com (Higher Logic help center) unreachable (transport error); Higher Logic evidence comes from product marketing pages, so its internal mechanics are inferred at lower strength.
- jobs.shrm.org (live YM Careers instance) returned 403; no live-instance observation.
- help.webscribble.com is a Notion page requiring JavaScript; no content retrieved.

Consequence: no precise platform-internal mechanics (approval queue behavior, exact default posting durations across products, billing internals) are asserted beyond what the fetched pages state. All numeric marketing figures are recorded as vendor-reported claims in Research Notes only.

## Product A — Careers powered by Momentive (Formerly YM Careers)

### Key observations (evidence layer A unless noted)

- Positioning: "Job Board Platform for Associations"; describes itself as the #1 job board software provider for professional associations, with ~3,000 professional associations in its employer-facing network (vendor-reported).
- The buyer is the association; the stated value is threefold: grow members' careers, attract new members, and maximize non-dues revenue.
- Modules visible: Job Board Software, Career Planning Portal, Onsite & Virtual Career Fairs, InternBoard, Recruitment Guides, plus a "Non-Dues Revenue Engine" (job board promotion, job posting & career fair sales, revenue-driving enhancements).
- "Zero start-up costs" on the overview page — a revenue-share style commercial model in which the vendor fronts the platform; vendor also operates "the world's largest niche recruitment ad sales team", i.e., the vendor sells job postings/career fair spots to employers on the association's behalf.
- Employer side is a separate surface (network.ymcareers.com): employers can recruit across the network of association boards, not just one.
- Client base spans large professional associations (vendor case studies mention SHRM, ABA, IEEE, ALA, etc.).
- Client testimonials describe the career center as a top revenue generator (marketing claims; recorded as vendor-reported).

## Product B — Web Scribble

### Key observations (evidence layer A)

- Positioning: "Career Center & Job Board Software for Associations… For 20 years, we've done one thing."
- The page states the tri-actor structure explicitly:
  - Members: "Jobs in their profession they won't find on the big boards", alerts by specialty and location, "one login they already have" (SSO with the member account).
  - Employers: "Candidates they can't reach anywhere else. They post, review applicants, and come back to saved resumes. When it works, they renew."
  - Association team: "Our team sells to employers in your name. You approve pricing, read the reports, and keep the revenue."
- Employer purchasing items named: job postings, featured placement, resume database access, career fair spots. "You set the prices; member employers get member rates."
- Member features: search with filters for location, remote, salary, experience; job alerts by specialty and location sent in the association's name; single sign-on with the member account.
- Resume database: "Members upload a resume once. Employers search them, save them, and come back to them."
- Admin portal: "Traffic, applications, employer revenue, and member activity, ready to export."
- Posting economics example shown on-page: "Premium posting sold — $725 · 60 days · resume access" (product-specific example; do not generalize the price or duration).
- Included platform features (vendor's "everything included" list): Google for Jobs indexing, resume database, AI job matching, reports, SEO posture, employer tools, career data (salary data, career-path suggestions), mobile, encryption/GDPR.
- Broader suite on the same login: Career Resources (guides, salary data, offer analyzer, AI career coaching), Mentoring, Career Fairs, Career Paths.
- Integrations: AMS/CRM for SSO and member data (iMIS, Dynamics 365, Personify, Salesforce, Fonteva, MemberClicks, Novi, GrowthZone, Impexium…), community platforms (Higher Logic — "job postings inside your Higher Logic community"), email tools, Google Analytics, Zapier.
- FAQ gives an explicit generic-vs-association distinction (vendor's own words, paraphrased): a generic board serves every industry and sells to everyone; an association job board serves one profession, ties into membership, and the money goes to the association.
- Outcome claims (vendor-reported, do not generalize): average 41% non-dues revenue increase; 99% client retention; case studies with +120% first-year non-dues revenue (NASW), etc.

## Product C — Madgex (Wiley)

### Key observations (evidence layer A)

- Positioning: career centers for associations and publishers; "the global standard in association career centers"; 22 years in recruitment; 12 languages, 14 countries, 500+ leading brands (vendor-reported stats).
- Two operating philosophies offered: "a full-service partner to deliver an engaging career center" (Madgex runs the career center) or "a technology upgrade to your current job board" (technology only).
- Value framing mirrors the Type: career support as "one of the top 3 reasons for joining an association"; niche community reach for employers; non-dues revenue "from your advertisers and service providers".
- Employer-side products beyond posting: employer branding, targeted advertising strategies; a "global team dedicated to promoting your career center to employers" (vendor-sells model again).
- Data/insights: "Build more comprehensive member and customer profiles with our career center data. Our advanced reporting suite gives you full access to your data."
- Example customers include AAAS (Science Careers) — a publisher-run professional job board on Madgex technology.

## Product D — Higher Logic Thrive Jobs

### Key observations (evidence layer A for packaging facts; lower strength for mechanics)

- Jobs is packaged as an add-on to the Thrive community platform: "powered by Web Scribble" — direct evidence that community platforms embed a specialized job board engine rather than build their own.
- Two headline features (product page): "Jobs in the Feed & Built-In Search" (career opportunities stream into the community feed; search within the platform) and "Community Profile Integration" (the community profile becomes the job board profile; single sign-on; one profile for both).
- Value framing: keep members engaged inside the community, "generating a new source of non-dues revenue and a prospective member pipeline" — "Non-members can apply for positions via your job board – generating a new pipeline of potential members" with nurture campaigns attached.
- Revenue attribution: "Your association generates revenue from what sponsoring companies pay to post their jobs."
- Client quote reports engagement lift metrics (vendor/customer-reported).

## Product E — JobTarget / JobBoard.io (context only)

### Key observations (evidence layer A for the main site; limitation noted)

- JobTarget's main platform is employer-side recruitment: post once, distribute to 25,000+ job boards, programmatic advertising, candidate management, compliance (OFCCC/state job banks), analytics. This documents the employer-distribution layer that association boards participate in, but it is NOT the association job board Type itself.
- JobBoard.io (the job board platform product, widely used to run association and niche boards) was not accessible; no claims drawn from it.
- The help-center taxonomy (getting started, advertising & job management, candidate management, billing, compliance, reporting) is consistent with the posting→application→billing→reporting loop seen in Products A–D (weak corroboration, layer B at most).

## Cross-product Comparison

| Dimension | YM Careers (Momentive) | Web Scribble | Madgex | Higher Logic Thrive Jobs |
|---|---|---|---|---|
| Operator of the board | Association (branded career center) | Association (branded career center) | Association or publisher | Association, embedded in community |
| Core object | Job posting (+ career fair, intern board as sibling objects) | Job posting | Job posting | Job posting (surfaced in feed) |
| Audience definition | Association's professional community / network of ~3,000 boards | One profession; members + public | Association/publisher professional audience | Community members + non-member applicants |
| Employer purchase items | Job postings, career fairs (sales run by vendor team) | Postings, featured placement, resume DB access, career fair spots | Postings, branding, advertising | Postings by sponsoring companies |
| Who sells | Vendor's ad sales team on the association's behalf | Vendor's team "in your name"; association sets prices | Vendor's global team (full-service) or association | Community/association; vendor engine |
| Membership integration | Member careers framing; modules like InternBoard | SSO via AMS; member rates; member resumes | Member/customer profiles; data insights | Community profile = job profile; SSO |
| Seeker features visible | Career planning portal, recruitment guides | Search filters, alerts, resume upload, career data | Job posts, career resources | Feed integration, built-in search |
| Admin/reporting | Revenue engine reporting (marketing level) | Traffic, applications, employer revenue, member activity reports | "Advanced reporting suite", full data access | Engagement/revenue framing |
| Packaging | Dedicated vendor platform + revenue engine | Dedicated vendor platform + suite | Full-service partner or technology-only | Community-platform add-on (engine by Web Scribble) |

Stable across the sample (layer B):

- Three actors: association operator, employing organizations (posters), professional job seekers (members and often non-members).
- Job posting as the central, individually managed, time-limited record, submitted by the employer side, not the seeker.
- Paid posting as the standard monetization, with placement tiers and add-ons (featured placement, resume database access, advertising/career fairs).
- Member/non-member price differentiation (member rates).
- Association-side branding and curation; the board is presented as the association's own service ("your name on everything").
- Employer applicant review surface (review applicants, save resumes) — light, not full ATS.
- Seeker-side search/filter, alerts, and a candidate profile/resume.
- Reporting to the association: traffic, applications, revenue.
- Vendor-sells-on-behalf as a widespread commercial pattern (three of four samples advertise a sales team selling in the association's name).

## Canonical Model (conceptual)

```text
Membership Organization (operator)
└── Branded career center / job board as an association service
    ├── Job Posting (employer-submitted, categorized, time-limited, placement tier)
    ├── Employer Account (member employer or external employer; purchases postings)
    ├── Job Seeker (member via SSO, or public visitor)
    │   ├── Candidate Profile / Resume
    │   ├── Search & Alerts
    │   └── Application (routed to the employer)
    ├── Curatorial control by the operator (review/approval, categories, pricing)
    └── Revenue & reporting back to the operator (non-dues revenue)
```

### L0 — Defining Invariant (deliberately small)

1. **Operator is a membership/professional organization**, and the board is presented under that organization's brand as part of its services to its professional community (career center / job board / joblink).
2. **Employer-submitted job postings** exist as discrete, individually managed records (not seeker-generated content, not aggregate feed items).
3. **A defined professional audience** — the operator's member and professional community — is the board's stated reach, which is its value proposition to both sides.
4. **A path from posting to employer** (apply/contact route), completing the employer↔candidate connection the operator brokers.
5. **Operator curatorial control**: the operator governs what is published (review/approval or equivalent policy) and typically sets the terms (pricing, categories).

Historical check: newsletter-era and conference "job mart" listings fit — the association published employer-submitted job ads to its professional audience with contact/apply routes and editorial control, without software search, resume banks, SSO, or in-system payments. Therefore none of those belong in L0.

### L1 — Common Mature Structure

- Search/filter over postings (location, specialty, salary, remote, experience) and posting detail pages
- Job alerts (by specialty/location) sent under the association's brand
- Candidate profile / resume upload; resume database searchable by employers (purchase-gated)
- In-system application and an employer portal to review applicants and save resumes
- Paid posting packages; member vs non-member rate differential; featured/premium placement tiers
- Posting duration/expiry and renewal handling
- Association admin console: moderation/approval queue, category taxonomy, pricing/branding configuration, board content (career resources)
- AMS/CRM integration: SSO, member data sync
- Reporting: traffic, applications, employer revenue, member activity

### L2 — Variant / Optional Structure

- Commercial model: revenue-share "zero start-up cost" vs license; association-sells vs vendor-sells-on-behalf vs self-serve employer checkout
- Packaging: dedicated career-center vendor vs AMS-suite module vs community-platform add-on (jobs in feed, shared profile)
- Employer cross-posting networks across many association boards; distribution into external job boards / Google for Jobs
- Career-center suite extensions: career fairs (virtual/in-person), mentoring, career paths, salary data, intern boards, career planning portals, AI matching/coaching, offer analyzers
- Audience openness: member-only vs public seekers; publisher-operated boards; higher-education campus career centers (same engine, different operator)
- Mobile posture, SEO posture, GDPR/security posture

### L3 — Vendor-specific (Research Notes only)

- Web Scribble: premium posting example "$725 · 60 days · resume access"; "offer analyzer"; AI career coaching; 41% average revenue increase and 99% retention claims; named integration list
- YM Careers: ~3,000-association employer network; InternBoard; Career Planning Portal; MomentiveIQ AI; SHRM 7-figure revenue case study; client logo wall
- Madgex: 22 years / 12 languages / 14 countries / 500+ brands stats; Science Careers (AAAS) instance; "advanced reporting suite"
- Higher Logic: 25%/14%/29% engagement-lift quote from a customer

## Vendor-specific Findings

- The vendor-operated ad-sales model (vendor team sells postings in the association's name; association approves pricing and keeps revenue) appears in three of four sampled vendors (YM Careers, Web Scribble, Madgex) — a strong market pattern but a business-model variant, not part of the definition.
- Community-embedding (jobs streaming into the community feed; community profile reused as job profile) is observed in one sample (Higher Logic + Web Scribble) as packaging evidence; treat as a packaging variant.
- Employer networks spanning many association boards (YM Careers; JobTarget's distribution layer) are vendor strategies, not Type structure.

## Rejected Findings

- "An association job board is an ATS": rejected. Employer-side review is light (view applicants, save resumes); full pipeline/stage management belongs to Recruiting/ATS Types. No sampled vendor documents ATS-grade workflows for the association board itself.
- "Access is member-only": rejected. Higher Logic documents non-member applicants as a designed prospective-member pipeline; YM/Madgex employer pages sell to any employer. Membership shapes pricing and identity, not the existence of the board.
- "Payments always happen inside the software": rejected. In vendor-sells models the transaction happens between vendor and employer; the software records the product. Payment mechanics are implementation.
- "Association job boards are just classifieds": rejected. The dedicated candidate-side machinery (profiles/resumes, applications routed to employers, employer review surface) is absent from generic classifieds' jobs category.
- "Career fairs / mentoring / salary data are part of the job board": rejected as definition. They are sibling modules of a career-center suite sharing the same login and audience; several sampled vendors sell them separately.

## Boundary Findings

| Near Type | Relationship | What distinguishes them | "Remove X" test |
|---|---|---|---|
| Job Board (generic, §09) | Shares nearly all machinery | Operator identity: a membership/professional organization running the board as its own member service, with member-integrated identity/pricing and revenue returning to the operator. Generic boards are commercial media serving open markets | Remove the membership-organization operator/member-services framing and member-integrated audience → it collapses into a generic (niche) Job Board |
| Association Management System / AMS | Complementary system of record | AMS holds membership data/billing; the job board consumes it via SSO/sync and adds posting/application machinery the AMS lacks. AMS suites may bundle a career center, but the posting engine remains a distinct subsystem | Remove the job posting/application machinery → it is just membership management |
| Member Community Platform | Host/variant packaging | Community platforms may embed a job board engine (jobs in feed, shared profile). When the feed/discussion is primary and jobs are only embedded items, the community platform is the primary Type and the job board an embedded subsystem | Remove the discussion/content community → a standalone association job board remains |
| Career Site Platform (§09) | Different operator/purpose | Career site = one employer's own recruiting website. Association board = many employers posting into one association-operated marketplace | Remove the multi-employer marketplace → not a board at all |
| Classifieds Platform | Weak overlap | Classifieds list jobs as one category among many, without candidate profiles/resumes and structured employer-side applicant handling | Keep only the listings without candidate machinery → classifieds |
| Recruitment Marketing Platform (§09) | Adjacent | Employer-side advertising/distribution across many boards; the association board is one destination such platforms distribute into | Remove the association-owned destination → employer ad tech, not a board |
| Vendor Management System / Staffing systems | Different problem | Those manage contingent-labor supply processes; no member audience or postings marketplace | n/a |

**Probable Variant issue (recorded, not silently resolved):** Association Job Board is, by machinery, a Job Board Variant whose distinguishing invariants are the membership-organization operator, the member-integrated professional audience, and the non-dues-revenue/member-benefit purpose. The directory lists both leaves; the practical split used here: machinery belongs to "Job Board", the operator/audience/purpose membership integration defines "Association Job Board". Flagged in STATUS Boundary Issues for a future taxonomy pass.

## Uncertainties

- Approval-queue behavior per product (manual review vs auto-approve defaults) is not directly evidenced; stated only as "operator curatorial control, commonly including review before publishing".
- Whether non-members can upload resumes/searchable profiles varies; Web Scribble documents members uploading resumes; Higher Logic documents non-members applying. Seeker-side membership gating is therefore written as a variant, not a rule.
- JobBoard.io capabilities are unverified (source inaccessible).
- Numeric vendor claims (network size, revenue lifts, retention) are vendor-reported marketing figures and are not treated as Type facts.
- Higher Logic's internal job mechanics rely on marketing pages (help center unreachable); strength reduced accordingly.

## Final Synthesis

An Association Job Board is a job marketplace operated by a professional or membership organization and presented as part of that organization's services under its own brand. Employing organizations — member employers at member rates, external employers at list rates — submit job postings to the board; the operator curates what is published for its professional community; job seekers (members, typically via SSO, plus often non-members) search postings, receive alerts, and apply through a routed path to the employer. Paid postings, placement tiers, resume-database access, and adjacent career-fair/advertising products convert the board into one of the association's standard non-dues revenue lines, reported back to the operator alongside traffic and application metrics. The job-matching machinery is shared with generic job boards; what defines this Type is the operator–audience–purpose triangle: a membership organization, its professional community, and the member-benefit + non-dues-revenue function, usually realized through AMS-integrated identity and vendor-operated or self-operated selling models.
