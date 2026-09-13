# Research Notes — Alumni Management

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what an Alumni Management application actually is, from real products: its central objects (alumni register, relationship records), how alumni records are created and maintained, what engagement machinery institutions run (events, groups, communications, mentoring, giving), the staff and alumni surfaces, the rules that matter (identity verification, data ownership, engagement measurement), and its boundaries against sibling leaves (University Advancement Platform, Donor Management System, Membership Management System, Member Community Platform, Student Information System).

## Initial Boundary (hypothesis before research)

- Core purpose: institution-side software to manage the ongoing relationship with former students — an alumni register, engagement tracking, events, communications, and often fundraising.
- Users: alumni relations / advancement staff; alumni themselves via a portal; volunteers/chapter leaders.
- Nearest types: University Advancement Platform (adjacent leaf in §23 — likely heavy overlap), Donor Management System (§25), Membership Management System / Member Portal / Member Community Platform (§25), SIS (§23 — source of alumni identity), Event Management Platform (§26), Email Marketing Platform (§6).
- Unknowns: is the alumni record the central object or is the "constituent" record? Is fundraising definitional or adjacent? Is a paid-membership model definitional or variant? Does the category include corporate alumni networks (employer-based)?

## Research Questions

1. What is the central object — alumnus record, constituent record, community member profile — and how is it created (graduation handoff, import, signup)?
2. What does an alumni record carry (academic affiliation, contact data, employment, engagement history, giving history)?
3. What lifecycle/states exist (student → alumnus; active/lapsed/lost; do-not-contact; deceased)?
4. What engagement programs do institutions run and record (events/reunions, chapters/affinity groups, mentoring, job boards, newsletters, benefits)?
5. What does the alumni-facing surface look like (portal, directory/map, profile self-service, event registration, giving)?
6. What staff machinery exists (segmentation/smart lists, email campaigns, event management, engagement measurement, data hygiene)?
7. What is the relationship to fundraising/advancement CRMs (system of record vs engagement layer)?
8. What role do memberships/dues play — definitional or variant?
9. What integrations are standard (advancement CRM, SIS, LinkedIn, job boards)?
10. What variants exist across segments (higher ed, K-12, associations, regional markets) and what distinguishes alumni management from corporate alumni networks?

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different customer tiers:

| Product | Segment / philosophy | Evidence quality |
|---|---|---|
| **Almabase** | US higher-ed + K-12 "engagement layer on top of your CRM" (RE NXT/Blackbaud CRM sync); digital engagement programs + events + giving days | Strong — official product site with detailed module pages, integration pages, case studies |
| **Hivebrite** | Community-platform-shaped alumni engagement (also associations, nonprofits, corporate alumni); community hub with groups/directory/events/mentoring | Strong — official product site (help center unreachable; see Sources) |
| **Graduway (Gravyty)** | Branded alumni network + mentoring-first platform with integrated giving; part of a Gravyty advancement ecosystem | Moderate — official product page with FAQ |
| **360Alumni** | All-in-one "Alumni Engagement CRM" for smaller institutions (higher ed, high schools, nonprofits, membership orgs); memberships included | Moderate-strong — official product site + public knowledge-base index (Tier 1) |
| **Blackbaud Raiser's Edge NXT** | Advancement CRM / donor management system of record; alumni outreach feeds supporter records | Strong — official product page with detailed capability/FAQ content |
| **Hoopstr (formerly Vaave)** | Regional (India) alumni engagement platform for institutions and corporates; placements/rankings-outcome emphasis | Moderate — official homepage only |

## Sources

Official (Tier 1/2), fetched 2026-09-06:

- Almabase product site: https://www.almabase.com/ (products: digital engagement programs — alumni directory, job board, mentorship, business directory, affinity groups, news & updates; events; giving day; TrueSync for Raiser's Edge NXT; solutions: alumni relations, annual fund, advancement services)
- Hivebrite product site: https://hivebrite.io/ (platform overview: Build/Launch/Engage; features: member directory, groups, mentoring, AI matching, mobile; industries incl. higher-ed alumni management)
- Graduway (Gravyty) product page: https://www.graduway.com/ (branded alumni community, mentoring, events, giving; FAQ comparing Almabase/Hivebrite; RE NXT + Salesforce integrations; Handshake/Simplicity job-board integrations)
- 360Alumni product site: https://www.360alumni.com/ (solution modules: map & directory, opportunity board, event management, asks & offers/mentorship, groups, memberships, fundraising, email marketing)
- 360Alumni Knowledge Base index (Tier 1): https://www.360alumni.com/resources/admin-help (Getting Started: bulk import with user records template, community setup, guidelines, welcome messages; Admins: adding new records, association fields, managing access, merging/deleting/deactivating records; Features: alumni directory/map/lists, jobs/opportunities, event proceeds, mentorship programs, creating events; Users: event registration, account creation)
- Blackbaud Raiser's Edge NXT product page: https://www.blackbaud.com/products/blackbaud-raisers-edge-nxt (unified supporter record; segmentation; gift processing; moves management; engagement tools; duplicate detection; relationship tracking/soft credits; "connecting marketing, events, alumni outreach… with your donor records")
- Hoopstr (formerly Vaave) homepage: https://www.vaave.com/ (alumni platform, Magic DB, internship activation, corporate alumni program; Indian institution + corporate customers)

Abandoned / failed sources (Source-access Limitation):

- https://support.hivebrite.com/hc/en-us and /hc/en-gb — request timed out / transport error (2 attempts)
- https://help.almabase.com/ and https://support.almabase.com/ — transport error (2 attempts)
- https://www.hivebrite.com/ — 404 (correct domain is hivebrite.io)
- https://hivebrite.io/alumni-management-software/ — 403

Consequence: no deep help-center article was captured for any engagement-platform vendor; operational details (exact field lists, exact state names, numeric limits) are NOT asserted. All product observations below are from official product pages and the 360Alumni KB index; claims are calibrated accordingly.

---

## Product Observations

### Almabase — evidence layer A (official product site)

Positioning: "The integrated, AI-powered platform that works **on top of your CRM** for digital engagement, event management, online giving campaigns — turning thousands of constituents into donors without adding staff." Audiences: Higher Education, K-12, Healthcare, Non-Profits. Solutions: Alumni Relations, Annual Fund, Advancement Services, Advancement Leadership.

- **Digital engagement programs** (self-serve): Alumni Directory ("foster connections and keep information updated"), Job board, Mentorship ("run impactful mentorship programs without hassle"), Business Directory, Affinity Groups ("promote self-serve networking among groups"), News & Updates ("a smarter way to share personalized emails"), custom programs.
- **Event management**: consolidate event operations; auctions; sponsorship management; case-study evidence of self-serve registration, QR check-ins, attendance syncing.
- **Online giving**: giving-day platform; gifts flow into CRM ("send gift information straight into Raiser's Edge gift management portal").
- **Fundraising marketing automation**: personalize at scale, "surface ready donors".
- **Data posture**: "Maintain one source of truth, your CRM" — TrueSync integration with Raiser's Edge NXT / Blackbaud CRM / other CRMs; sync rules ("All data. No junk"); automatic enrichment; engagement activities recorded at scale ("123,000+ engagement activities in a single month"; "3,300+ verified users").
- **Segmentation & measurement**: "Segment based on the donor journey"; monthly participation reports; hyper-segmentation; email automation with real-time reporting.
- **Roles/access**: "Control permissions based on how your team is set-up"; compliance claims (ADA, GDPR, SOC-2 — vendor claims).
- Case-study framing: alumni self-serve communities with "verified users"; migration from NetCommunity (Blackbaud's legacy engagement product) as a common motion.

### Hivebrite — evidence layer A (official product site)

Positioning: "Community Engagement Platform — the community platform built for impact." Industries: Associations, Non-Profit, **Higher Ed ("Turn connection into lifelong engagement" — alumni management software)**, Business (corporate alumni). Customers include universities (e.g., Princeton), NGOs, associations.

- **Build / Launch / Engage** platform model:
  - Build: branding and theming; no-code page builder; **custom user profiles and fields**; roles and permissions.
  - Launch: **signup, SSO and activation**; email invitations; **payment and memberships**; branded mobile app; map directory.
  - Engage: forums; events; messaging; content and people recommendations; AI global search (list continues beyond captured section).
- Highlighted features: Mobile app; **AI Matching** ("spark meaningful 1:1 connections at scale"); **Groups** ("focused spaces for meaningful participation"); **Member Directory** ("find, connect, and grow"); **Mentoring** ("turn community wisdom into momentum").
- Resource library confirms category vocabulary: "The complete guide to alumni management software", "How to measure alumni engagement", "Finding lost alumni", "How an 'Alum from Day One' strategy can transform your alumni engagement", "Managing your Alumni Network: 6 Mistakes to Avoid", corporate alumni network guides.
- CRM integrations emphasized ("How CRM integrations improve community effectiveness").
- Help center (support.hivebrite.com) unreachable — operational detail not captured.

### Graduway (Gravyty) — evidence layer A (official product page)

Positioning: "Alumni Engagement, Community & Mentoring Platform — build a thriving alumni network that actually drives results… a fully branded, always-on digital community."

- **24/7 virtual network**: "secure, branded portal where alumni can register for events, give, and stay connected."
- **Easy sign-up** for members ("seamless onboarding").
- **Mentoring**: "career development and networking are the two most valued services institutions can provide, according to alumni themselves. Offer alumni and students both **flash and formal mentoring** options — easy to match, manage, and scale from one platform."
- **Groups**: "dedicated spaces for shared interests, class years, industries, and more."
- **Communications**: automated digests, newsletters, emails; integrated video messaging.
- **Events**: branded event pages, payments, reminders, RSVPs, real-time attendance reporting.
- **Giving**: integrated giving forms; "build donor pipelines"; part of Gravyty ecosystem (Advance, Gratavid) spanning student → alumni → donor journey.
- **Integrations**: Raiser's Edge NXT and Salesforce ("ensuring alumni data flows smoothly between your engagement hub and your **advancement system of record**"); job boards Handshake and Simplicity.
- FAQ self-positioning: "While Almabase and Hivebrite focus on alumni directories and communities, Graduway combines alumni engagement, mentoring, career resources, and giving tools in one platform."
- Related-search terms on page: "alumni management software", "alumni database management system", "alumni association software" — confirms the market names the category this way.

### 360Alumni — evidence layer A (official product site + KB index, Tier 1)

Positioning: "**The Alumni Engagement CRM** — stay connected to your alumni and centralize profile data, events, groups and fundraising. All in 360Alumni's easy-to-manage online communities." Audiences: Higher Ed, High Schools, Nonprofits, Membership Organizations.

- Solution modules: **Map & Directory**; **Opportunity Board** (job board); **Event Management** (incl. reunions); **Asks & Offers (Mentorship and More)**; **Groups** (affinity groups & chapter management); **Memberships**; **Fundraising**; **Email Marketing**.
- Admin framing: "a branded, customizable platform **built around your alumni data**. Powerful search, smart lists, and communication tools help admins run engagement — and alumni stay connected."
- Knowledge Base (Tier 1 index) confirms operational structure:
  - Getting Started: community setup form, onboarding overview, community guidelines page, sharing news, custom welcome message, **bulk import with the User Records Template**, payment forms (ACH/W-9).
  - Help for Admins: **adding new records**, **association fields**, **managing access in your community**, **merging, deleting & deactivating records**.
  - Help by Feature: about jobs/opportunities, **about the alumni directory, map & lists**, **collecting my event proceeds**, **creating a mentorship program**, **creating an event**, interactive alumni map & directory.
  - Help for Users: event registration, creating an account.
- Dual-surface structure explicit: admin tools vs user (alumni) self-service.

### Blackbaud Raiser's Edge NXT — evidence layer A (official product page)

Positioning: "fundraising CRM / donor management… one system to manage **all your supporter relationships**." (Not an alumni-management product per se — included as the system-of-record pole that alumni platforms orbit.)

- **Unified supporter record**: "brings together giving history, engagement, relationships, and interactions in one system."
- Intelligent segmentation and targeting; forward-looking insights; data governance ("trusted, clean, organization-wide information").
- **Gift processing and management**: integrated payment processing; sustainer programs; online giving experiences; **moves management and portfolio workflows**; pledges, tributes, campaigns.
- **Engagement tools**: email, donations, registrations, memberships built in; donor-friendly portals; "flexible integrations… bringing vital engagement data into one, central hub for a unified view of supporter interactions."
- **Data hygiene**: built-in duplicate detection across online donations/memberships/event registrations/email signups; batch validation; data health services (address and card updates); **relationship tracking and soft credits** connecting households, employers, affiliations.
- Explicit alumni boundary: "Get a 360-degree view of your donors by connecting marketing, events, **alumni outreach**, and more with your donor records" — alumni outreach is an integration surface feeding donor records, not the product's center.
- FAQ: "Online donations, memberships, and event registrations flow directly into donor records, trigger acknowledgements automatically."

### Hoopstr (formerly Vaave) — evidence layer A (official homepage; regional sample)

Positioning: "Global Leader in Alumni Engagement… Activate your Alumni Capital — drive real outcomes — **placements, fundraising, mentoring**." Sides: For Institutions / For Companies / For Alumni-Students.

- Institution products: Alumni Platform, **Magic DB** (data), Internship Activation Program, Hoopstr Live, Hoopstr Advance, Leadership Program.
- Corporate side: Corporate Alumni Program, Boomerang AI, Talent Solutions, Member Benefits.
- Customers: Indian institutions (IISc, IIM Calcutta/Lucknow, NIT Calicut, VIT, Symbiosis) and corporates (Tata Steel, Deloitte, Maruti Suzuki, Bosch) — each with a live public alumni portal.
- Regional emphasis: placements/internships and institutional rankings as headline outcomes (India-specific framing); corporate alumni networks as a sibling market on the same platform.

---

## Cross-product Comparison

| Aspect | Almabase | Hivebrite | Graduway | 360Alumni | Blackbaud RE NXT | Hoopstr |
|---|---|---|---|---|---|---|
| Central object | constituent/alumni record synced with CRM | community member profile (custom fields) | alumni member of branded network | user record ("built around your alumni data") | supporter/constituent record | alumni record |
| Record creation | CRM sync + verification | signup / SSO / email invitations | member sign-up | bulk import template + manual adding | institution database; alumni outreach feeds in | institution data |
| Academic affiliation | implied (class/segment) | profile fields | class years as group basis | association fields | relationship/affiliation data | institution data |
| Directory / map | Alumni Directory | Member Directory + map directory | branded portal | Alumni Directory & Map | — (internal database) | portal |
| Groups / chapters | Affinity Groups | Groups | groups (class year, industry, interest) | Groups (affinity & chapters) | — | — |
| Events | event ops, auctions, sponsorship, QR check-in | events | event pages, RSVPs, payments, attendance | event management & reunions, event proceeds | event registrations flow into records | events |
| Mentoring | mentorship programs | mentoring + AI matching | flash & formal mentoring | asks & offers / mentorship programs | — | mentoring programs |
| Jobs / careers | job board | (jobs module) | career resources + Handshake/Simplicity | opportunity board | — | placements/internships |
| Communications | news & updates, email automation | messaging, newsletters, recommendations | digests, newsletters, video messages | email marketing, news | email engagement tools | communication |
| Giving / fundraising | giving days, online giving | donations module | giving forms, donor pipelines | fundraising | gift processing, moves management (the center) | fundraising |
| Membership / dues | — | payment and memberships | — | memberships | memberships | member benefits |
| Engagement measurement | engagement activities, participation reports | community analytics | engagement→giving reporting | search/smart lists | engagement on supporter record, dashboards | outcomes (placements, fundraising) |
| Data hygiene | sync rules, enrichment | — | profile sync | merge/delete/deactivate, bulk import | duplicate detection, data health | Magic DB |
| System-of-record posture | engagement layer on top of CRM | community platform + CRM integrations | engagement hub + CRM sync | itself the CRM (small orgs) | IS the system of record | platform + DB |

### Findings by evidence layer

**Layer A (directly observed, per product):** all rows above as observed on official pages.

**Layer B (cross-product commonality):**

- Every product maintains a **population of identified alumni/constituent person records** with contact data and affiliation attributes.
- Every engagement-shaped product exposes an **alumni-facing portal/community** (directory/map, profile, groups, events, mentoring, jobs, giving) alongside an **admin surface** (records, segmentation, communications, event management, reporting).
- **Events with registration/attendance** and **direct communications (news/newsletters/email)** appear in all six.
- **Groups/chapters/affinity communities** appear in five of six (all except RE NXT, where groups are not the frame).
- **Mentoring** appears in five of six (all engagement-shaped products).
- **Giving/fundraising** appears in all six, but its position differs: center for RE NXT, integrated module for the engagement platforms.
- **CRM/advancement-system integration** is explicitly positioned by Almabase, Graduway, Hivebrite (and implicitly by 360Alumni's "built around your alumni data"); RE NXT explicitly receives "alumni outreach" data.
- **Data hygiene machinery** (import, merge/dedupe, deactivate, enrichment, "finding lost alumni") is explicitly present in 360Alumni, RE NXT, Almabase, Hivebrite (resource guide), Hoopstr (Magic DB).

**Layer C (canonical inference):**

- The Type is best modeled as: **institution-scoped alumni register + tracked relationship + institution-run engagement loop**, with the alumni portal as the standard self-service surface and fundraising/membership as common-but-adjacent modules.
- The market is structurally **two-pole**: (1) engagement platforms (portal/community-first, often positioned "on top of" a CRM), (2) advancement/donor CRMs (record-first, receiving engagement data). Alumni Management as a Type spans the register+relationship core that both poles share; the leaf is best anchored on the engagement-shaped products while acknowledging the record-shaped pole as the frequent system of record.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

1. **Institution-scoped alumni register** — identified person records for the institution's former students, each carrying the academic affiliation (class year / program / degree) that qualifies the person as an alumnus of this institution.
2. **Tracked relationship per alumnus** — maintained contact data plus a recorded history of the institution's interactions with that person (outreach, event participation, volunteering, giving), continuing the relationship beyond graduation.
3. **Institution-run engagement loop** — the institution organizes programs toward alumni segments (events, communications, groups, mentoring), records participation, and uses the resulting engagement picture to steer further outreach.

Remove 1 → generic CRM/community platform. Remove 2 → a mailing list / event tool. Remove 3 → a static database (no management). Historical check: a mid-20th-century alumni office with card files, printed class directories, mailed newsletters and reunion committees satisfies 1–3; modern SaaS adds portals, self-service, scoring, and integrations on top — the definition does not depend on current packaging. Regional check: Indian "alumni cell" platforms (Hoopstr), UK/EU alumni relations offices, and association-style alumni offices all satisfy 1–3.

### L1 — Common Mature Structure

- Alumni portal / branded community (self-service surface: profile, directory/map, groups, events, giving)
- Directory & map with search; profile self-service updates
- Events (reunions, homecoming, galas) with registration, payments, attendance
- Groups: chapters (regional), affinity groups, class-year groups
- Mentoring programs (alumni↔student, alumni↔alumni)
- Job boards / opportunity boards; career services tie-ins
- Direct communications: news, newsletters, targeted email
- Engagement measurement (participation/engagement scoring, reports)
- Data hygiene: bulk import, merge/dedupe, deactivate, enrichment, lost-alumni recovery
- Giving integration: donation appeals, giving days, gift sync to advancement CRM
- Integrations: advancement CRM (RE NXT, Blackbaud CRM, Salesforce), SIS, job boards, LinkedIn

### L2 — Variant / Optional Structure

- Segment shape: research university vs small college vs K-12/high school vs professional school vs association alumni body
- Membership model: automatic/free lifetime membership vs dues-paying alumni association (memberships module)
- Product-shape pole: engagement layer on top of CRM vs all-in-one small-org CRM vs community platform configured for alumni vs module of an advancement suite
- Regional emphasis: US advancement/fundraising framing vs India placements/rankings framing vs EU alumni-relations framing
- Corporate alumni networks (employer-based alumni) — same machinery, different affiliation basis; adjacent market, not this leaf's center
- Volunteer management depth, benefits/perks programs, legacy/planned-giving tie-ins

### L3 — Vendor-specific (Research Notes only)

- Almabase TrueSync (RE NXT sync with custom rules), giving-day platform specifics, "NetCommunity migration" motion
- Hivebrite AI agents, MCP integration, Orbiit AI matching, Build/Launch/Engage packaging
- Graduway flash mentoring, Gravyty ecosystem (Advance, Gratavid, Raise, PeerPal), white-glove onboarding
- 360Alumni "360 Method", Asks & Offers naming, event-proceeds collection flow
- Hoopstr Magic DB, Boomerang AI, Internship Activation Program
- Blackbaud moves management, Blackbaud ID, Financial Edge integration, data health services

---

## Vendor-specific Findings

- Almabase explicitly markets itself as working "on top of your CRM" with TrueSync as the named integration product — an architecture claim, not a category rule.
- Graduway's FAQ explicitly differentiates from Almabase/Hivebrite (mentoring + giving emphasis) — competitive positioning, useful for variant mapping only.
- 360Alumni sells memberships as a first-class module — dues-based alumni management is real but not universal.
- RE NXT treats alumni outreach as one more engagement feed into donor records — evidence for the two-pole market structure.
- Hoopstr's corporate-alumni line shows the same platform serving employer alumni — boundary evidence, not part of the education leaf.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| University Advancement Platform | sibling (§23), heavy real-world overlap | Advancement centers the fundraising operation (gift pipeline, moves management, campaigns, stewardship) over all constituents; alumni management centers the alumni relationship register and engagement itself. Giving is one engagement outcome among several here. If gift/pipeline machinery is the center → advancement. |
| Donor Management System | adjacent (§25) | Donor management centers donors and gifts; alumni management covers alumni regardless of donor status. Alumni platforms integrate with donor CRMs rather than replace them (Almabase TrueSync; Graduway→RE NXT). |
| Membership Management System / AMS | adjacent (§25) | If dues, membership lifecycle, and member benefits are the center → membership management. In alumni management, membership is usually automatic upon graduation; dues are a variant (360Alumni Memberships; Hivebrite payment & memberships). |
| Member Community Platform | adjacent (§25) | Community platforms serve open or member-defined communities; alumni management requires the institution-verified alumni register derived from academic history and institution-run relationship management. Hivebrite straddles: a community platform configured for alumni. |
| Student Information System | upstream (§23) | SIS holds academic records of enrolled students; the alumni record is derived at graduation and persists as a lifetime relationship record. Handoff, not overlap. |
| Event Management Platform | capability overlap (§26) | Events are one engagement program here, bound to the alumni register; a standalone event platform centers the event, not the relationship. |
| Email Marketing Platform | capability overlap (§6) | Communications are one channel of the engagement loop, bound to segments of the alumni register. |
| Corporate Alumni Platform (not a directory leaf) | adjacent market | Same engagement machinery, but affiliation is former employment, not academic study. Kept out of this leaf's core; noted as adjacent. |

"去掉什么就变成另一个 Type" 判据：去掉学术归属（affiliation 来自学业经历）→ 会员/社区平台；去掉关系记录与参与历史 → 邮件营销/活动工具；把赠与管线放到中心 → University Advancement / Donor Management；把会费与会员生命周期放到中心 → Membership Management。

## Uncertainties

- Exact record-field models, lifecycle state names (active/lapsed/lost/deceased), and engagement-scoring formulas could not be verified — help centers were unreachable; no precise claims made.
- Whether large universities increasingly run alumni relations as a module inside advancement suites (vs standalone alumni platforms) — market-trend claim not verified; recorded as uncertainty.
- The degree to which "Alumni Management" and "University Advancement Platform" should remain separate directory leaves is a taxonomy judgment; evidence shows heavy overlap with distinct centers of gravity. Flagged for Boundary Issues, no directory change made.
- K-12 alumni offices may be volunteer-run with minimal tooling; the minimal definition covers them, but product evidence for that tier is thin (360Alumni high-school customers are the main evidence).

## Final Synthesis

An Alumni Management application is the institution's system for managing its lifelong relationship with former students. Its defining core is small: a register of identified alumni (former students carrying their academic affiliation), a tracked relationship with each (contact data + recorded engagement history), and an institution-run engagement loop (programs toward alumni segments with recorded participation). Around that core, mature products add the standard machinery: a branded alumni portal with directory/map and self-service profiles, events with registration and attendance, chapters and affinity groups, mentoring and job boards, targeted communications, engagement measurement, data hygiene, and — very commonly but not definitionally — giving/fundraising tied into an advancement CRM. The market is two-poled (engagement platforms on top of a CRM vs advancement CRMs as system of record); the Type is anchored on the register+relationship+engagement core that both poles share. Membership dues, regional outcome emphases, and corporate alumni networks are variants or adjacent markets, not the core.
