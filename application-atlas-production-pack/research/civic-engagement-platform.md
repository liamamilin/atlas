# Research Notes — Civic Engagement Platform

## Research Goal

Understand what a Civic Engagement Platform actually is as an Application Type: what structures it is built from, who operates and participates in it, how an engagement runs from opening to report-back, and where its boundaries lie against neighboring government/civic Types (Petition / Public Comment Platform, 311 / Citizen Service Request, Rulemaking & Public Consultation, Government Open Data Portal, Community Platform, Survey Platform, Constituent Relationship Management, Election Management).

## Initial Boundary

Initial hypothesis (pre-research):

- A Civic Engagement Platform is software through which a public institution opens participation around civic topics/decisions and residents contribute structured input (ideas, opinions, priorities, budget preferences, map annotations) that the institution aggregates and responds to.
- Nearest confusable Types: Petition / Public Comment Platform (formal signature campaigns), 311 (operational service requests), Rulemaking & Public Consultation (statutory comment periods), Government Open Data Portal (publishing, not soliciting), Community Platform (interest communities, not decision-oriented), Survey Platform (one tool, not a composed engagement), Constituent CRM (individual constituent records for elected offices), Election Management (binding legal voting).
- Unknowns: the top-level organizing unit (project vs portal vs process); toolset composition; lifecycle; identity/verification posture; how the closed loop (report-back) is realized; whether participatory-democracy frameworks (Decidim/Consul) and project-based SaaS engagement platforms share one core model.

## Research Questions

1. What is the top-level organizing unit of the platform (engagement project / participatory process / hub)?
2. What participation tools exist, and how do they compose within one engagement?
3. What lifecycle does an engagement go through (draft → open → closed → results/report)?
4. Who participates, and under what identity posture (anonymous / registered / verified)?
5. How is input moderated, managed, and aggregated?
6. How does the operator close the loop (analysis, decisions, report-back, outcome tracking)?
7. Where are the boundaries against Petition, 311, Rulemaking, Open Data, Community, Survey, CRM, and Election Types?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels:

| Product | Philosophy / position | Customer level | Sources reached |
|---|---|---|---|
| Decidim | Free/open-source participatory democracy framework (Barcelona City Hall origin); whole-of-organization participation infrastructure | Cities/regions self-hosting; also NGOs, universities, cooperatives | Official docs (docs.decidim.org), Tier-1 |
| Go Vocal (formerly CitizenLab) | SaaS community engagement platform for local governments; project-based engagement with participation ladder | Mid-market local governments (600+ claimed, marketing) | Official product/platform pages, Tier-2 |
| Granicus EngagementHQ (now "Sentiment & Feedback (EngagementHQ)") | Enterprise government-experience suite member; engagement + sentiment analytics | Enterprise government (local/state/federal, agencies) | Official product page, Tier-2; legacy help center unreachable |
| Open Point (formerly Social Pinpoint) | Map-first community engagement + stakeholder relationship management; infrastructure/planning-heavy | Governments, utilities, transport, resources/mining | Official product + tools pages, Tier-2 |

Boundary-context products (not sampled, unreachable): Polco (polling-first; fetch returned empty), PublicInput (meeting/comment-centric; 403). Recorded as market context only.

## Sources

- Decidim Documentation — https://docs.decidim.org/ (redirect to /en/develop/index.html), /en/develop/features/participatory-spaces, /en/develop/features/components — fetched 2026-09-07
- Go Vocal — https://www.govocal.com/ (home) and https://www.govocal.com/platform-online-engagement-toolbox (platform page) — fetched 2026-09-07
- Granicus — https://www.granicus.com/solutions/engagementhq/ (404) recovered via https://www.granicus.com/product/sentiment-feedback-engagementhq/ content ("Sentiment & Feedback (EngagementHQ)") — fetched 2026-09-07
- Open Point (formerly Social Pinpoint) — https://www.socialpinpoint.com/ (served Open Point home) and https://www.openpoint.com/products/community-engagement/community-engagement-tools/ — fetched 2026-09-07
- Failed/abandoned: https://support.bangthetable.com/hc/en-gb (transport error ×1), https://polco.com/ (empty response ×1), https://www.publicinput.com/ (403 ×1)

## Product Observations

### Decidim (open-source participatory democracy framework) — Evidence layer A

From official documentation (docs.decidim.org, develop branch):

- Self-description: "a participatory democracy platform created initially by Barcelona City Hall… allows any organization (local city council, association, university, NGO, neighbourhood or cooperative) to create mass processes for strategic planning, participatory budgeting, collaborative design for regulations, urban spaces and election processes."
- **Participatory spaces** are the main participatory channels, shown in the platform's main menu. Types: **Participatory Processes**, **Assemblies**, **Initiatives**, **Consultations** (plus Conferences). "Components work together in the participatory spaces."
- **Participatory Processes**: configured with title, short name/URL, hashtag, descriptions, images, start/finish dates, promoter group, target audience, goal, participatory structure; divided into **stages** (documented example: 1. information and convening; 2. diagnostics; 3. proposals; 4. prioritisation; 5. decision; 6. evaluation; 7. results-monitoring). Stage/component activation is configurable ("total flexibility in designing participatory processes"). **Process statuses**: unpublished/published, open (started), closed (ended but results under way), finished (results complete), future. Process groups (e.g., participatory budgets of different districts); process copying/templates; highlighting.
- **Components** (participatory mechanisms inside spaces): **Proposals** ("Decidim's most important component… the minimum decision unit"; creators: official organization, individual participants, groups, or meetings; moderated/amended/withdrawn; accepted/rejected/evaluating; importable to new phases; creation wizard; version control; similarity detection; connections; endorsements; amendments like pull requests; collaborative drafts), **Budgets** (budget voting by "spending" an amount across projects), **Debates**, **Meetings** (convening, registrations/attendance, agendas, polls, minutes with 4-stage preparation, map/calendar display), **Surveys** (questionnaires, CSV download), **Sortitions** (reproducible random selection), **Pages**, **Blog**, **Accountability** ("turn proposals into results and give official responses"; results subdivided into projects; implementation statuses 0–100%; grouped by categories/scopes; CSV/manual updates), **Conferences**.
- Documented composition example (participatory budgeting process): meetings → survey → categories → proposals → deliberation → budget voting → evaluation meeting → assessment survey → **Accountability** monitoring of execution.
- **Participants/identity**: registration mode configurable; **authorizations** for verified participation: identity documents, code by postal letter, organization's census, ephemeral verifications; impersonations; verification conflicts. Scopes (territorial), areas, taxonomies organize participation.
- **Social features**: comments (rankable, notifications), endorsements, follows, conversations, newsletters, badges, share, hashtags.
- **Transparency features**: statistics, version control, fingerprint; **open data** export; global moderations (reported content, reported participants); AI tools (spam detection, machine translations).
- **Initiatives** (citizen-initiated): proposal + collection of required signatures/endorsements per type; promoter committee; technical moderation/validation by staff (approve/reject/suggest amendments); states: accepted (procedure starts) / rejected (insufficient signatures). This is the petition-shaped space inside Decidim.
- **Consultations**: organization-wide voting on specific questions, with debate and result monitoring; gateway to an external integrated e-voting system for identity management/verification.

### Go Vocal (formerly CitizenLab) — Evidence layer A (product pages, Tier-2)

- Self-description: "community engagement platform" for governments; "Reach residents where they are and turn input into insights"; three pillars: **Engage** / **Configure and manage** / **Decide**.
- **Engage**: "complete toolbox… mix and match participation methods within one project to create a unique flow". Participation ladder (Inform / Consult / Involve / Collaborate / Empower — IAP2-shaped) with tools per rung: Information, Email & messaging, Follow, Events (Inform); Surveys, Paper forms (Form Sync), Polls, Events (Consult); Voting & Prioritization, Option Analysis, Document Annotation (Involve); Ideation, Mapping, Deliberation (Collaborate); Community Proposals, Citizens' Assemblies, Participatory Budgeting (Empower). Also issue-reporter ("Mängelmelder") and project list ("Vorhabenliste") surfaces in the Inform rung.
- **Configure and manage**: roles and permissions for team collaboration; "intuitive project setup… easy CMS builder"; "easy input management and follow-up… centralized oversight, status updates, and moderation"; available in 27 languages with automatic translation of resident content (product-specific detail); project templates based on prior participation projects; WCAG 2.2 AA accessibility compliance (product-specific claim).
- **Decide**: "Sensemaking" — AI to group and summarize input (with confidence scores, links to original input, human correction — product-specific detail); engagement tracking dashboards; Report Builder ("create and share impactful reports"); digitization of offline-captured feedback (hybrid engagement); API access.
- Key feature pages listed: Survey, Ideation, Mapping, Proposals, Participatory Budgeting, Voting and Prioritization, Form Sync, Community Monitor (representativeness monitoring), Sensemaking.
- Positioning: "Inform, involve, and report – all in one place"; "closing the feedback loop"; case studies: settlement-fund allocation (St. Louis), youth participation (Innsbruck), child participation (Waddinxveen).

### Granicus EngagementHQ (now "Sentiment & Feedback (EngagementHQ)") — Evidence layer A (product page, Tier-2)

- Self-description: "helps governments ask the right questions, listen to answers, and respond with intent." Use cases: performance management and prioritization, participatory agenda-setting, policy and program development, infrastructure planning and delivery, budgeting and resource allocation, crisis management.
- **Omnichannel tools**: "engage across the entire IAP2 public participation spectrum… start conversations in varied environments. Customize participant registration… conversations connected no matter where they take place (web, mobile, email, or social)." Tools named: "propose ideas, vote, ask questions, put feedback on a map, submit surveys, allocate budget and comment on priorities."
- **Engagement environments**: Open, Mixed, Closed (sensitivity levels for conversations).
- **Moderation**: "human-eye and AI moderation… contextual vetting… enforcing community guidelines. Available 24/7 in Spanish, English, Welsh, and French languages for all public discussions" (product-specific detail).
- **Unified community view**: participant activity and information in a centralized workspace; capture activity and participant attributes; import existing information; citizen profiles and login; "project recommendations, subscriptions, and contribution history."
- **Reporting and analytics**: pre-built dashboards per tool; purpose-built "Aware, Informed, and Engaged" (AIE) framework; "hundreds of ways to customize metrics, filters, and dashboards"; AI-powered text and sentiment analysis; shareable dashboards/reports; compliance/data-security posture; regional hosting.
- Platform posture: no-code appearance editor; multiple engagement hubs (per department/region/brand); API; integration with Granicus suite (govDelivery communications, OpenCities CMS) and third-party tools; benchmark reporting and strategic support services.
- Suite context: sits in Granicus' "Digital communication & engagement" solution family alongside govDelivery; separate Granicus products cover service requests (govService/OneView), forms (OpenForms), permitting, records — confirming the boundary between engagement and 311/forms Types within one vendor.

### Open Point (formerly Social Pinpoint) — Evidence layer A (product pages, Tier-2)

- Self-description: "digital community engagement and stakeholder management platform helping organisations plan, consult, and collaborate with communities"; "from input, to insight, to impact." Two products: **Community Engagement** + **Stakeholder Relationship Management (SRM)**.
- **Participation tools** (nine): Form (surveys with conditional logic), Social Map (pin comments on interactive map; "trends, hotspots, place-based insights"), Quick Poll, Fund It ("allocate a virtual budget across proposed projects"), Q&A ("ask questions and receive clear, official responses"), Visioner (ideas wall; post/explore/upvote/downvote), Gather (story-driven feedback: experiences, images, videos), Conversation (topic-based discussions with intelligent moderation), Forum (multi-topic discussion hub).
- **Project setup & management**: Project Map (all projects on an interactive map), Events (listings with registration links), News Feed (project updates), Key Dates, Timeline (milestones), Project Profiles (workspace combining community members, engagement records, tasks, updates, reporting).
- **Visual/media and page-structure widgets**: VR View (360° imagery), Video Banner, Gallery, Swipe (before/after), Document Library, Tabs, Sub Nav, etc. — the engagement project page is a composed, CMS-like page.
- **Analytics layer** (from home page): AI-powered feedback analysis of open-text responses/consultation submissions; theme & trend identification; sentiment & issue analysis; multi-source data collection (surveys, consultation portals, emails, documents, transcripts); advanced reporting; interactive dashboards; cross-project analysis; auditability ("clear records of how feedback has been analyzed, categorized and incorporated into reporting and decision-making").
- **SRM product** (drift marker): stakeholder profiles (contact details, project context, relationships, engagement history), timeline, communications (email/SMS linked back to projects), task manager, reports, audit history, Outlook add-in — stakeholder-record management adjacent to CRM.
- Audience: local & state government, transportation, transit, infrastructure planning, resources & mining, energy & utilities — engagement extends beyond government to infrastructure proponents.

## Cross-product Comparison

| Dimension | Decidim | Go Vocal | Granicus EngagementHQ | Open Point |
|---|---|---|---|---|
| Top-level unit | Participatory space (process / assembly / initiative / consultation) with stages | Engagement project (mix-and-match tools, phases) | Engagement projects/hubs (open/mixed/closed environments) | Engagement project page (composed page + tools) + project map |
| Participation tools | Proposals, budgets, debates, meetings, surveys, sortitions, pages, blogs | Surveys, ideation, mapping, proposals, PB, voting/prioritization, polls, document annotation, events | Ideas, voting, Q&A, map, surveys, budget allocation, comments | Form, social map, quick poll, fund-it, Q&A, ideas wall, gather, conversation, forum |
| Contribution unit | Proposal ("minimum decision unit") | Input items per tool (idea/survey response/map pin/vote) | Contributions per tool | Contributions per tool (pins, ideas, stories, comments) |
| Lifecycle | Process statuses: future/open/closed/finished; stages incl. results-monitoring | Project phases; inform→…→empower ladder; report-back | Project-based; AIE measurement (aware→informed→engaged) | Timeline/key dates/news feed; input→insight→impact |
| Identity posture | Configurable registration; authorizations (census, postal letter, ID docs, ephemeral) | Registration + automatic translation; representativeness monitoring | Customizable registration; profiles, attributes, import | Registration posture not detailed on fetched pages |
| Moderation | Global moderations (reported content/users); AI spam detection | Centralized input oversight, status updates, moderation | Human-eye + AI moderation, 24/7, 4 languages | "Intelligent moderation" on conversations |
| Analysis/reporting | Accountability component (results, statuses 0–100%, milestones); statistics; open data | Sensemaking AI, dashboards, Report Builder | Dashboards, AIE framework, AI text/sentiment analysis | AI feedback analysis, themes, sentiment, dashboards, cross-project |
| Deliberation | Comments, endorsements, amendments, collaborative drafts, debates | Deliberation, ideation discussion | Conversations in open/mixed/closed environments | Conversation, Forum, Gather |
| Offline/hybrid | Meetings component (registrations, minutes, attendance) | Form Sync (paper forms), offline digitization, events | Web/mobile/email/social channels | Events listings; field tools via SRM |
| Deployment | Open-source self-host (framework) | SaaS | SaaS (suite member) | SaaS |
| Operator type | City councils, associations, universities, NGOs, cooperatives | Local governments | Governments (local/state/federal), agencies | Governments, utilities, transport, mining, infrastructure |
| Report-back | Accountability results + official responses to proposals | Report Builder; "closing the feedback loop" | "report back on key themes"; sentiment tracking | News feed updates; auditability of how feedback was incorporated |

Cross-product commonalities (Evidence layer B):

1. Institution-opened, bounded engagement unit (space/process/project) with its own lifecycle and public page.
2. A toolbox of participation mechanisms composed within the unit (idea collection, surveys, discussions, Q&A, map input, polls, budget allocation, voting/prioritization).
3. A resident-facing participation surface and an operator-facing management surface (setup, moderation, input management).
4. Moderation of public contributions (human and/or AI).
5. Participant accounts/profiles with configurable identity requirements (where documented).
6. Analysis/aggregation of input (dashboards; increasingly AI-assisted theme/sentiment analysis — present in all four sampled products, era-current).
7. Report-back/outcome surfacing (official responses, results, reports, news updates).
8. Notification/communication machinery (newsletters, follows, email/SMS).
9. Multi-language and public-sector accessibility posture (where documented).
10. Organization of participation by geography/topic (Decidim scopes/areas/taxonomies; Open Point project map; Go Vocal mapping).

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being a Civic Engagement Platform:

1. **Institution-opened participation space** — an operator (public institution or civic body) creates a bounded, identifiable engagement space around a civic topic or decision, with its own lifecycle (not-yet-open / open / closed / reported).
2. **Structured resident contribution** — residents/stakeholders contribute input through participation mechanisms as attributable, aggregatable contributions (an idea, an opinion, a priority, an allocation, a map pin, a survey answer) tied to that space.
3. **Institutional processing toward a decision** — the operator manages, moderates, and aggregates the input to inform a public decision, plan, or policy.
4. **Report-back to participants** — the platform surfaces what was heard and/or decided back to the public (official responses, results, outcome reporting).

Remove (1) and it is a generic community/forum or survey tool; remove (2) and it is a broadcast/transparency portal; remove (3) and it is an unmanaged comment surface; remove (4) and the participatory loop collapses into one-way consultation capture (still engagement-adjacent, but the Type's defining accountability loop is gone — all four sampled products implement it).

### L1 — Common Mature Structure

- Participation toolbox composed within a space: idea collection with support/voting, surveys, discussion threads, Q&A with official answers, map-based input, polls, participatory budgeting, voting/prioritization, document annotation.
- Engagement project lifecycle management: phases/stages, key dates, timelines, status (draft/open/closed), project templates.
- Participant accounts and profiles; configurable registration; contribution history; follows/subscriptions.
- Moderation machinery (reported content, spam/profanity screening; human + AI in current products).
- Notifications and outreach (newsletters, email/SMS, project updates/news feed).
- Participation analytics (dashboards, per-tool metrics, representativeness monitoring) and AI-assisted input analysis (theme/sentiment grouping, summarization) — era-current across all sampled products.
- Report builder / results publishing; outcome tracking (Decidim's accountability statuses; report builders elsewhere).
- Multi-language support; accessibility posture for public-sector compliance.
- Embedding/standalone hub posture on government web estates; APIs for transparency/integration.

### L2 — Variant / Optional Structure

- Deployment: SaaS vs open-source self-hosted framework vs suite module.
- Scope posture: single-project consultation vs whole-of-organization participation portal vs multi-hub (per department/brand/region).
- Identity/verification depth: open/anonymous participation → registered → verified eligibility (census, postal letter, identity documents) — product- and jurisdiction-dependent.
- Operator type: local government (dominant), state/federal agencies, utilities/transport/infrastructure proponents, universities, NGOs/cooperatives.
- Outcome binding: advisory/informal vs formalized procedures (Decidim initiatives triggering administrative procedures; consultations wired to external e-voting).
- Hybrid online+offline engagement (digitizing paper/offline input, event listings, meeting minutes).
- Stakeholder-relationship extension (Open Point SRM) — drift toward Constituent/Stakeholder CRM.
- Polling-first engagement (Polco — not directly sampled) as a market pole.
- Deliberative depth: collaborative drafting, amendments, sortition for assemblies (Decidim), citizens' assemblies (Go Vocal).

### L3 — Vendor-specific Structure (kept out of final document)

- Decidim: assemblies with composition/org-chart displays, initiatives with promoter committees and signature thresholds, sortitions, participatory texts (document→ordered proposals), fingerprint/version transparency, ephemeral verifications, process groups.
- Go Vocal: Sensemaking (confidence scores, human correction), Community Monitor (representativeness), Form Sync, Vocal Point demo platform, 27-language claim, WCAG 2.2 AA certification claims, "600+ governments" marketing.
- Granicus EngagementHQ: AIE (Aware/Informed/Engaged) framework, Open/Mixed/Closed environments, 24/7 moderation in four named languages, govCommunity peer insights, govDelivery/OpenCities integration, regional hosting options.
- Open Point: Visioner, Fund It, Gather, VR View, Swipe, Logo Splash, Faces widgets; SRM product (stakeholder profiles, Outlook add-in); "Social Point" legacy branding.

## Rejected Findings

- **"Civic engagement platform = participatory budgeting tool"** — rejected: PB is one tool among many in every sampled product; most engagements are not budget allocations.
- **"Civic engagement platform = survey tool for government"** — rejected: surveys are one participation mechanism; the Type's defining unit is the composed engagement space with a decision loop, not the questionnaire.
- **"Civic engagement platform = government social network / community"** — rejected: participation is organized around institutional decisions and time-bounded projects, not persistent interest communities or social graphs.
- **"Participation must be verified/eligible"** — rejected as definitional: Decidim makes verification configurable; other products allow open participation. Verification is a variant posture.
- **"The operator must be a government"** — softened: the sampled set includes NGOs/universities/cooperatives (Decidim) and private infrastructure proponents (Open Point). The canonical operator is an institution conducting public-facing engagement; government is the dominant but not exclusive case. The Type remains filed under Government, Public Sector & Civic.
- **"AI analysis is definitional"** — rejected: era-current commonality (all four sampled), but older/regional products function without it; belongs to common mature structure.

## Boundary Findings

- **vs Petition / Public Comment Platform**: the petition Type's defining object is a signature campaign on a specific demand with a threshold and formal handling. Decidim's *Initiatives* space is exactly this shape (signatures, committee, accept/reject) — evidence that petitioning is a *component* inside engagement platforms. Boundary test: if the platform's primary and only object is the petition/signature campaign, it is the Petition Type; if petitions are one mechanism inside composed engagement spaces, it is a Civic Engagement Platform.
- **vs 311 / Citizen Service Request Platform**: 311's unit is an individual service request with an operational case lifecycle (report → assign → resolve). Engagement input informs collective decisions; it has no dispatch/repair case semantics. Go Vocal's issue-reporter surface ("Mängelmelder") is a drift element inside an engagement product; Granicus sells service-request management as a *separate* product family — vendor-side confirmation of the seam.
- **vs Rulemaking & Public Consultation Platform**: rulemaking consultation is a statutory comment period on a proposed rule with docket/comment-aggregation obligations. Civic engagement is broader and project-based (plans, budgets, policies, infrastructure), typically advisory and not statute-bound.
- **vs Government Open Data Portal**: open data publishes datasets for reuse; engagement solicits input. Decidim's "open data" export is transparency machinery inside an engagement product, not a data portal.
- **vs Community Platform (01.06)**: community platforms host persistent interest-based member communities; engagement spaces are institution-opened, decision-oriented, and time-bounded per project. Public discussion tools overlap; the container and purpose differ.
- **vs Survey Platform (03.11)**: surveys are one tool inside the engagement toolbox; the engagement platform composes multiple tools in a public, decision-linked space with moderation and report-back.
- **vs Constituent Relationship Management**: constituent CRM manages individual constituent records/interactions (typically for elected offices); engagement platforms aggregate collective input on topics. Open Point's SRM product is the observed drift case (stakeholder profiles + communications + tasks), sold as a *second product* alongside community engagement — the seam is real but adjacent.
- **vs Election Management System**: elections are binding, legally regulated voting with voter rolls and result certification. Engagement voting (proposals, PB, polls) is advisory/participatory; Decidim's consultation component explicitly delegates binding voting to an external e-voting system — vendor-side confirmation of the seam.
- **"去掉什么就变成另一个 Type" 判据**: remove the institutional decision loop and report-back → community platform / forum; remove resident contribution → transparency/open-data portal; make the contribution a service ticket → 311; make the contribution a threshold signature campaign → petition platform; make the vote legally binding with voter rolls → election management; reduce the space to a questionnaire → survey platform.

## Uncertainties

- Granicus EngagementHQ's detailed help-center documentation was unreachable (support.bangthetable.com transport error; granicus.com/solutions/engagementhq/ 404). Observations rely on the official product page (Tier-2). Per-tool behavior details for EngagementHQ are therefore not asserted.
- Go Vocal's help center was not reached; observations rely on official product/platform pages (Tier-2). Exact project-phase mechanics and admin workflows are not asserted.
- Open Point's participant identity/registration posture was not documented on the fetched pages; not asserted.
- Polco and PublicInput could not be fetched (empty response / 403). The polling-first and meeting-centric market poles are recorded as context only, without product claims.
- Decidim documentation reflects the `develop` branch; minor feature naming may differ across versions.
- Decidim's "Consultations" component delegates to an external e-voting system; the exact integration mechanics are not documented in the fetched pages.

## Final Synthesis

A Civic Engagement Platform is the institutional side of public participation: a public institution (or civic body) opens a bounded engagement space around a civic topic or decision; residents contribute structured input through a composed toolbox of participation mechanisms; the institution moderates, manages, and aggregates that input toward a decision; and the platform surfaces what was heard and decided back to participants.

The defining core is the participatory loop: **space → contribution → processing → report-back**. Everything else — the specific toolbox, phased processes, participatory budgeting, maps, verification regimes, AI analysis, dashboards, multilingual support — is mature structure or variant posture. The Type is distinct from petition platforms (signature campaigns), 311 (service-request cases), rulemaking consultation (statutory comment), open data portals (publishing), community platforms (interest communities), survey tools (single mechanism), constituent CRM (individual records), and election systems (binding voting) — while sharing one mechanism or surface with each.

Market structure: an open-source participatory-democracy pole (Decidim), SaaS project-engagement poles for local government (Go Vocal), enterprise government-experience suites (Granicus EngagementHQ), and map/infrastructure-first engagement with stakeholder-management extension (Open Point). AI-assisted input analysis is era-current across the sample. The operator is dominantly local government but extends to agencies, infrastructure proponents, universities, and civic organizations.
