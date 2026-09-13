# Research Notes — Talent Sourcing Platform

Cross-references (joint-review obligations discharged in this pass):

- research/candidate-search-platform.md §Boundary Findings #2 — flagged this leaf as "unprocessed sibling"; proposed the **center-of-gravity test** (searches-and-results machinery vs engagement workflows over identified people) and named Fetcher the instructive middle case.
- research/candidate-profile-platform.md §Boundary Findings #3 — flagged this leaf: "record layer vs identification/outreach activity; products bundle both — same joint-review pass recommended."

Both obligations are discharged below (Boundary Findings #1 and #2).

## Research Goal

Understand the Application Type the directory leaf "Talent Sourcing Platform" names, as distinct from its two already-processed siblings (Candidate Search Platform, Candidate Profile Platform) and its other neighbors (ATS, Recruitment Marketing, sales-side Outreach Sequencing). Establish the smallest defining core, the standard capability set, the variant axes, and the boundary seams — with direct product evidence for the engagement/sequence machinery that the sibling passes identified as this Type's center of gravity but did not themselves research.

## Initial Boundary

Working hypothesis before research (to be tested, not asserted):

- A Talent Sourcing Platform is the recruiting operation's **outbound engagement machinery**: it takes people who have been identified as worth pursuing and drives them toward a response through planned, repeated, multi-channel touches.
- Nearest confusions: Candidate Search Platform (upstream: finding people), Candidate Profile Platform (record layer: remembering people), Recruitment Marketing (audience-scale attraction), sales Outreach Sequencing Platform (same machinery, different subject), ATS (downstream pipeline of record).
- Open question: is the sequence/campaign the managed object, or is it the person-with-engagement-state?

## Research Questions

1. What is the platform's unit of work — the sequence/campaign, the person, the search, or the reply?
2. How does a sequence/campaign actually work: stages, channels, timing, automatic vs manual steps, stop conditions?
3. How do replies get handled — detection, stop-on-reply, conversation surfaces, handoff?
4. What deliverability/compliance machinery is structural (throttling, sender reputation, unsubscribe, bounce handling, sending windows)?
5. Where do the pursued people come from (extension capture, search-tool handoff, own database, managed delivery), and where do responses go (ATS/CRM sync)?
6. What metrics does the platform hold itself accountable to (response rate, open/click, campaign comparison)?
7. How do agency-side and in-house-side deployments differ (client/BD outreach vs candidate outreach)?
8. Where exactly is the seam vs Candidate Search Platform (center-of-gravity test) and vs Candidate Profile Platform (record vs activity)?
9. Historical check: does the core hold for pre-digital and email-era sourcing?

## Representative Products

Selected for market representativeness, documentation quality, and — critically — coverage of the two sibling seams:

| Product | Pole in the market structure | Why sampled |
|---|---|---|
| **SourceWhale** | Pure-play engagement layer (recruitment agencies; integrates over external CRMs/ATSs and search tools) | The clearest "engagement is the product" pole; agency-side variant incl. client/BD outreach |
| **Gem** | Outreach + candidate CRM (started as sourcing/CRM tool, now all-in-one with ATS) | The bundle case: engagement + record layer in one product; richest sequence documentation |
| **Fetcher** | Managed sourcing service (AI + expert team deliver candidate batches; email campaigns attached) | The sibling pass's designated middle case — tests the center-of-gravity seam with direct evidence |
| **hireEZ** | Search-first suite (Sourcing Suite vs EZ Engagement split; campaigns packaged as "Talent CRM" / "High-Volume Nurturing") | The search pole's own packaging of the engagement layer; confirms the market separates the two |

Counter-poles for boundary calibration (Candidate Search Platform: hireEZ Sourcing Suite, Fetcher's search lifecycle; Candidate Profile Platform: Gem CRM, hireEZ Talent CRM) are sampled from the same four products — no fifth product needed; Beamery's record-layer pole was already documented by the sibling pass (its helpdesk was unreachable there; not re-attempted here).

## Sources

Research date: 2026-09-08. All Layer-A sources fetched live this pass.

- SourceWhale — marketing site (sourcewhale.com root, /outreach/), Help Center (help.sourcewhale.app: home, Getting Started collection + article)
- Gem — marketing site (gem.com root, /product/crm), Help Center (help.gem.com home, /outreach directory, Sequences overview article)
- Fetcher — marketing site (fetcher.ai root, /product-tour), Help Center (help.fetcher.ai home, "Fetcher Leads & Self Sourced Leads" article)
- hireEZ — marketing site (hireez.com root, /automated-campaigns/), Help Center (help.hireez.com home)
- Sibling research notes (prior passes, same repo): research/candidate-search-platform.md, research/candidate-profile-platform.md

Not fetched / limitations:

- Gem individual help articles beyond the Sequences overview (directory titles used as evidence of surface structure; article bodies not all read).
- SourceWhale campaign-specific help articles (the help-center home lists modules; campaign mechanics taken from the Outreach product page + Getting Started article — both Layer A).
- Beamery, Entelo (defunct), sales-side engagement platforms (Outreach.io/Salesloft) — not fetched; sales-engagement kinship reasoned structurally.
- Vendor numeric claims (Gem "98% delivery rate", Fetcher "40% average response rate", SourceWhale "56% increase in response rates") are marketing claims, recorded as claims only.

## Product Observations

### SourceWhale (recruitment agencies; engagement layer over external systems)

Key observations (Layer A unless noted):

- **Positioning**: "AI recruitment platform built on full context… Every call, email, note, and interview – from sourcing to placement – captured natively in one place." Customer base: "thousands of recruitment agencies" (staffing-agency pole).
- **Module decomposition** (nav + help center): Sourcing / Data (verified contact details) / **Outreach** ("personalized outreach sequences") / Inbox Agent / Conversations (calls, one-off SMS, WhatsApp — transcribed to CRM/ATS) / Notetaker / Data Refresh / CRM & ATS (own AI-native CRM & ATS *or* integrate the existing one).
- **Outreach module** (product page): "Multichannel recruitment outreach sequences that personalize automatically and trigger at the right moment." Multi-step sequences across email, SMS, phone (image caption adds LinkedIn). "Deliverability tools built in. Sender reputation protected." "Duplicate proven campaigns across the team instantly"; "to-do workflows that guide execution"; "automation handles the routine, people handle the relationships."
- **Personalization from context**: "draws on the full context of every previous call, email, note, and reply"; "real behavioral signals surface the right moment to reach out."
- **Boundary line, vendor's own words**: "Your CRM & ATS stores what happened. SourceWhale drives what happens next." — the engagement/execution layer vs the record layer, stated by the vendor.
- **Hotlist** (vendor-specific): flags contacts most likely to respond now. **AI To-Dos**: extracts commitments from emails into a task list. **Dashboard**: "what's landing and what isn't."
- **Getting Started (help center)**: login *with Gmail / Microsoft 365 / Exchange credentials* (the mailbox is the transport); email-signature capture; Chrome extension with email-finding credits (work/personal email choice, auto-search); CRM/ATS integration syncs "contacts and email activity"; SendGrid integration documented for sending.
- **Help-center module descriptions**: CRM & ATS module "organizes Contacts/Candidates into Jobs and **Business Development Projects**" — the agency variant pursues clients with the same machinery. Conversations module = "calls, one-off SMS messaging, and WhatsApp."
- **Metrics** (marketing): response-rate increase, pipeline generation, admin hours saved — engagement-operations metrics.
- **Integrations page**: Bullhorn, Crelate, Firefish, Greenhouse, **hireEZ**, HubSpot, Indeed, JobAdder, JobDiva, Mercury, PCRecruiter, Top Echelon, Vincere — composes with both agency ATSs and search tools.
- G2 category badges displayed: "Recruiting Automation", "Candidate Relationship Management".

### Gem (outreach + candidate CRM; now all-in-one)

Key observations:

- **Positioning**: "Gem is the AI-first recruiting platform… combines ATS, CRM, sourcing, scheduling, fraud detection, and pipeline analytics." FAQ: "Gem **started as a sourcing and CRM tool**." Packaging: "Gem + Your ATS" (agents/CRM on top of existing ATS) or all-in-one.
- **CRM product page**: Rediscovery (past candidates, silver medalists; NL search over own database), **Engage** ("Personalized sequences… Gem drafts the message automatically"; Talent Communities; Nurture campaigns), Manage (deep bi-directional ATS sync; auto-enriched profiles; "Unified activity feed — emails, InMails, texts, interviews, and notes").
- **Help-center product split**: separate directories for **Outreach** ("Engage candidates with personalized messages"; product URL gem.com/**sequences**) vs **People** (projects, pools) vs **Talent Marketing** (career sites, events; URL /campaigns) vs ATS vs Scheduling. The market product itself separates engagement (sequences) from audience marketing (campaigns) and from records (People).
- **Sequences overview article (Layer A, full text read)**:
  - "Sequences are divided into **stages**. Each contains a templated message and a scheduled delivery time."
  - Outreach methods: **Automatic** ("messages are sent automatically by Gem (e.g., emails and texts)") vs **Manual** ("Gem prompts you to take an action (e.g., sending an InMail, making a phone call, or sending a LinkedIn connection request)").
  - **Stop conditions** (vendor-documented): sequence automatically stops when (1) the prospect responds, (2) stages are exhausted, (3) the user manually marks a response. "If a prospect replies, the Sequence stops immediately to prevent over-messaging." Pause available at any time.
  - Personalization via **custom tokens** (with blank-token fallbacks documented).
  - Sequences dashboard: Your / Shared / Top (admin view, up to 200 incl. Confidential) — sequence sharing/collaboration is a first-class surface.
- **Outreach help directory** (surface structure): edit/create/send sequences; **manual stages ("To-dos")** inside sequences; different senders per stage; **send-on-behalf-of (SOBO)** incl. multi-account for agencies; holiday settings; **unsubscribe links**; attaching sequences **to ATS jobs**; **nurture sequences**; **bounce handling** ("what happens when an email sequence to a candidate bounces"); **automatic reply-status tracking**; InMail sequences + InMail activity tracking; **SMS sequences**; WhatsApp Business; **call forwarding** (candidate calls reach a Gem phone number); premium email finding with auto-send-when-found; email deliverability best practices; Gmail/Outlook aliases and signatures; open/click tracking, outreach stats, content stats.
- **Sourcing side** (for the seam): Chrome extension to add candidates from LinkedIn/sourcing sites/Indeed (incl. candidates without LinkedIn profiles); AI Sourcing Agent (800M+ profiles claim); AI rediscovery over own database.
- **Deliverability claim** (marketing): "2x better email coverage… 98% delivery rate" — vendor claim, not a Type property.

### Fetcher (managed sourcing; the sibling pass's middle case)

Key observations:

- **Positioning**: "AI-powered talent sourcing platform sorts inbound applicants and shifts to outbound sourcing when you need to reach passive talent." Audiences: people teams, small-business operators, staffing firms. New "inbound recruiting" product (AI screening of applicants) alongside outbound.
- **Managed delivery (Layer A, help article "Fetcher Leads & Self Sourced Leads")**:
  - Two lead categories: **Fetcher-sourced** ("we'll add people & you can too" — proactively delivered; default 30/week, adjustable 10–100/week) vs **Self-sourced** (Chrome extension / Fetcher database only).
  - **Search lifecycle**: open a search → calibration (extension additions "help calibrate the results") → delivery cadence → pause/hold goals → close. "Most searches are able to be closed once connection has been made with ~10 interested candidates."
  - Lead buckets/counters; seat-based packages.
- **Engagement side**: "add them to an email campaign, then set it and forget it until I start seeing responses in my inbox" (customer quote); "40% average response rate from Fetcher's automated email sequences" (vendor claim); email integration (Gmail/Outlook) so replies land in the recruiter's own inbox; ATS/CRM/email/Slack integrations.
- **Help-center structure**: "Search Management — managing searches and campaigns, including **submission, calibration and metric tracking**" (17 articles); "Directory & Email Campaigns"; "Sourcing from Fetcher Database"; "Sourcing from Chrome Extension"; ATS Integrations.
- **Reading**: the operational unit is the **Search** (with delivery quotas and calibration); the campaign is attached to the search's output. Confirms the sibling pass's classification: marketed as managed sourcing, operationally search-organized — a delivery-model variant of the sourcing outcome, not a counter-example to the engagement core.

### hireEZ (search-first suite; engagement packaged as Talent CRM)

Key observations:

- **Positioning**: "Agentic AI Recruiting Platform… One Talent Acquisition Platform… on top of your ATS… one System of Actions, with unified talent data underneath."
- **Suite decomposition** (nav): Sourcing (Open Web/Deep Search/Partner Networks, "45+ platforms") / Career Site & Landing Pages / **Talent CRM** (URL /automated-campaigns: "Nurture pipeline, resurface past applicants, and internal mobility") / Applicant Review / Conversational AI / AI Scheduler / Hiring Process Management / Hiring Intelligence / EZ Agent. Help-center footer naming: "High-Volume Nurturing."
- **Automated Campaigns page**: "Build personalized campaigns at scale"; "multi-channel campaigns spanning **email, text messaging, and InMail**"; AI outreach balancing speed and personalization; nurture talent communities and events; "Track open rates, responses, and overall engagement"; "Identify top-performing campaigns and refine strategies."
- **Help-center categories**: EZ Onboarding / EZ Integration-SSO / **Project** ("EZ Projects express TA workflow and candidates pipeline") / **EZ Engagement** ("Email Integration, **Campaigns, SOBO**, Calendar") / Sourcing Suite. Common topics: "Sourcing filters, **Response rate**, Search results, Collaboration."
- **Reading**: hireEZ itself splits the recruiting stack into a **Sourcing Suite** (discovery) and **EZ Engagement** (campaigns/SOBO/email integration) — the vendor's own architecture maintains the search-vs-engagement seam this pass needs. The engagement layer is packaged under a CRM name ("Talent CRM") because it operates over the employer's accumulated talent data (rediscovery, past applicants) — the record-layer/name collision the sibling pass predicted.

## Cross-product Comparison

| Dimension | SourceWhale | Gem | Fetcher | hireEZ |
|---|---|---|---|---|
| Primary market | recruitment agencies | in-house TA (+ staffing) | in-house + staffing (SMB/mid) | in-house TA (+ staffing/RPO) |
| Unit of work | campaign/sequence over contacts | **Sequence** (stages) | **Search** with delivered lead batches + campaigns | **Campaign** inside Projects |
| Channels observed | email, SMS, WhatsApp, phone, LinkedIn | email, SMS, WhatsApp, InMail, phone (manual stage + call forwarding), LinkedIn connection (manual) | email (campaigns); replies via own inbox | email, text messaging, InMail |
| Automatic vs manual steps | automation + to-do workflows | explicit Automatic/Manual stage types (InMail, call, connection request) | managed service delivers; user runs campaigns | AI outreach + agent execution |
| Stop-on-reply | implied ("replies get buried… keep things moving"; Conversations module) | **documented**: reply stops the sequence | implied (responses in inbox) | implied (response tracking) |
| Reply/conversation surface | Conversations module (calls/SMS/WhatsApp) + Inbox Agent | reply-status tracking; one-off messages; manual touchpoint logging; unified activity feed | own email inbox (integration) | response tracking, engagement analytics |
| Personalization | AI on full interaction history | custom tokens + AI drafting | campaign templates | AI-personalized campaigns |
| Deliverability machinery | deliverability tools, sender reputation, SendGrid, email throttling, holiday settings, signature sync | bounce handling, unsubscribe links, aliases, deliverability best practices, SOBO | email integration (Gmail/Outlook) | email integration, SOBO |
| Where people come from | extension capture (credits), external CRMs/ATSs, own Data module | extension capture, AI sourcing agent, rediscovery of own database | managed delivery (10–100/week), extension, Fetcher database | sourcing suite (open web/partner networks), rediscovery, ATS enrichment |
| Where responses go | sync to external CRM/ATS (or own CRM & ATS) | deep bi-directional ATS sync; sequences attach to ATS jobs | ATS integrations (Greenhouse, Lever, …) | "on top of your ATS"; hiring process management |
| Metrics | response rates, pipeline, dashboard | open/click/reply tracking, outreach stats, content stats | search metrics, response rate (claim) | open rates, responses, top-performing campaigns |
| Record layer | external CRM/ATS primary (own CRM optional) | own candidate CRM (People) | thin (leads inside searches) | Talent CRM over accumulated talent data |
| Compliance surfaces | GDPR/CCPA pages; sending-on-holidays | unsubscribe links, holiday settings | opt-out page | GDPR/CCPA/own-your-data pages |

Convergent findings (Layer B — cross-product commonality):

1. The **sequence/campaign over identified people** is the organizing object in every sampled product (names vary: sequence, campaign, engagement).
2. **Multi-channel execution with a mixed automatic/manual step model** is universal; email is the automatic backbone; LinkedIn (InMail/connection), SMS/WhatsApp, and phone appear as automatic or prompted steps depending on product.
3. **Reply handling** is universal: responses are tracked, and (where documented at article depth) they stop the sequence.
4. **Deliverability and sending discipline** (mailbox connection, throttling, signatures, bounce handling, unsubscribe, sending windows/holidays) is a structural concern in every product — because the platform sends from the recruiter's own identity.
5. **Activity sync to the ATS/CRM record layer** is universal (SourceWhale's whole integration catalog; Gem's deep sync; Fetcher's ATS integrations; hireEZ's "on top of your ATS").
6. **Engagement-operations metrics** (open/click/reply, campaign comparison) are universal.
7. **The people enter from somewhere else** — extension capture, search tools, databases, or a managed team. None of the four products requires its own search to feed its engagement layer; SourceWhale even integrates *with* hireEZ.

Divergent findings (variant axes):

- Delivery model: self-serve (SourceWhale, Gem, hireEZ) vs managed (Fetcher).
- Record-layer posture: external-record engagement layer (SourceWhale) vs bundled CRM (Gem, hireEZ Talent CRM) vs thin (Fetcher).
- Market: agency (client/BD outreach included) vs in-house (candidate only).
- Suite scope: engagement-only module vs all-in-one platform.
- Era-current AI: AI-drafted personalization everywhere; agentic end-to-end execution emerging (hireEZ EZ Agent, Gem agents).

## Canonical Model (abstraction layers)

### L0 — Defining Invariant (deliberately small)

1. **The pursued-candidate working population** — identified people the recruiting operation engages *by name* (typically passive, not-yet-applicants; in the staffing-agency variant also client contacts), held as addressable recipients. Remove → anonymous-audience marketing tools or a bare contact list.
2. **The planned engagement effort as the unit of work** — a defined, reusable, time-spaced series of touches (sequence/campaign) aimed at specific people, executed per person through automatic and human-prompted steps. Remove → one-off messaging or a contact database.
3. **The response loop** — replies are detected/captured, the engagement is organized around eliciting them, and a response becomes workable conversation feeding the hiring workflow. Remove → fire-and-forget bulk sender.

Jointly-held is load-bearing: 1 alone = contact list; 2 without 1 = generic sequence engine (sales-engagement machinery over a different subject); 3 without 1+2 = an inbox; 1+2 without 3 = bulk mailer; 1+3 without 2 = ad-hoc outreach with no repeatable process.

### L1 — Common Mature Structure

- Multi-channel step vocabulary (email, LinkedIn InMail/connection, SMS/WhatsApp, phone) with automatic vs prompted steps
- Personalization machinery (merge tokens, AI drafting on context)
- Deliverability/sending discipline (mailbox connection, throttling, sender reputation, bounce handling, unsubscribe, sending windows/holidays, SOBO)
- Reply detection + stop-on-reply + conversation surfaces
- Sequence/campaign library with sharing, duplication, templates (team process standardization)
- Engagement analytics (open/click/reply, campaign comparison, dashboards)
- Capture and handoff rails (browser extension in; ATS/CRM sync out; sequences attachable to jobs)
- Cadence controls (pause, stop conditions, per-stage senders, manual to-dos)

### L2 — Variant / Optional Structure

- Delivery model: self-serve vs managed service (expert team + AI deliver batches)
- Corpus attachment: own database/rediscovery vs external search-tool integration vs none (pure engagement layer)
- Channel mix by region/product (WhatsApp, SMS availability)
- Agency variant: same machinery aimed at client contacts (BD projects)
- Nurture/evergreen campaigns vs req-driven campaigns; talent-community nurturing (high-volume end, near the Recruitment Marketing seam)
- Phone-number provisioning / call handling
- Agentic execution (era-current): agents run search→engage loops

### L3 — Vendor-specific (research notes only)

- SourceWhale Hotlist, Inbox Agent, Notetaker, Data Refresh, SendGrid setup flow, signature-capture workflow
- Gem: Top Sequences admin view (≤200, incl. Confidential), premium email finding auto-send, Gem phone number with call forwarding, blank-token fallbacks
- Fetcher: lead buckets (Fetcher-sourced vs self-sourced), weekly delivery quotas (10–100), hold goals, "~10 interested candidates" closing heuristic
- hireEZ: EZ Agent command center, "45+ platforms / billion-plus profiles" scale claims, High-Volume Nurturing naming

## Vendor-specific / Rejected Findings

- **"Sourcing = search"** — rejected as this Type's identity. Search machinery belongs to Candidate Search Platform (sibling pass). Every sampled product separates them structurally (hireEZ: Sourcing Suite vs EZ Engagement; Gem: sourcing vs Outreach products; SourceWhale: Sourcing vs Outreach modules; Fetcher: search lifecycle vs campaigns).
- **"800M+/1B+ profiles, 45+ platforms, 98% delivery, 40% response rate, 56% response lift"** — vendor scale/performance claims; not Type properties.
- **"Multi-channel is definitional"** — rejected at L0; the *sequence* concept is definitional, channel breadth is maturity (historical check: phone+letter era satisfies the core).
- **"AI personalization is definitional"** — rejected; era-common implementation of personalization (tokens → AI drafting).
- **"Managed delivery is definitional"** — rejected; it is one delivery-model variant (Fetcher) of the same outcome.
- **"Talent CRM = this Type"** — naming collision noted: hireEZ packages its engagement layer as "Talent CRM"; the Candidate Profile Platform pass already documented the record-layer Type. The engagement machinery, not the CRM name, is this leaf's identity.

## Boundary Findings

1. **vs Candidate Search Platform (joint review — DISCHARGED, keep both Types).** The sibling pass's center-of-gravity test is confirmed by direct evidence. The search Type organizes workflows/data/analytics around *searches and their results* (saved searches, corpus choice, calibration, result windows); this Type organizes them around *engagement over identified people* (sequences, campaigns, reply handling, response rates). Evidence: (a) hireEZ's own architecture splits Sourcing Suite from EZ Engagement; (b) Gem ships sourcing and Outreach as separately documented products; (c) SourceWhale ships Sourcing and Outreach as separate modules and integrates *with* hireEZ — the market composes search tools + engagement layers; (d) Fetcher, the sibling's designated middle case, is confirmed search-organized (search lifecycle, submission/calibration/metric tracking, delivery quotas) with campaigns attached to search output — a managed-delivery variant of the sourcing outcome, not a counter-example. Capability lists coincide (every search tool attaches outreach; every engagement tool needs people), so the seam is the center of gravity, not features. Products bundle both; the Types remain distinct.
2. **vs Candidate Profile Platform (joint review — DISCHARGED, keep both Types).** Record layer vs activity layer, as the sibling pass proposed. The sourcing platform deposits activity (touches, replies, outcomes) onto person records but does not require owning the record layer: SourceWhale runs over external CRMs/ATSs; Fetcher holds thin lead records inside searches. Conversely the profile platform's value is the maintained record, not the engagement motion. Gem and hireEZ bundle both (CRM + engagement), which is packaging, not Type merger. SourceWhale's own boundary line — "Your CRM & ATS stores what happened. SourceWhale drives what happens next" — is the vendor-articulated version of the seam.
3. **vs Recruitment Marketing Platform.** Marketing = audience-scale attraction (career sites, employer brand, talent-community broadcasts); sourcing = individual-addressable pursuit. Gem itself separates Talent Marketing (/campaigns) from Outreach (/sequences). The near-seam is high-volume nurturing of talent communities (hireEZ "High-Volume Nurturing"): still individual-addressable (each recipient has an engagement state), so it stays in this Type; a broadcast with no per-person engagement state would be marketing.
4. **vs Applicant Tracking System.** ATS = pipeline/system of record for applications in process; sourcing = upstream activity that creates applicant flow. Handoff is structural (Gem sequences attach to ATS jobs; SourceWhale syncs activity; hireEZ sits "on top of your ATS") but the managed objects differ (application/requisition vs engagement).
5. **vs Outreach Sequencing Platform (sales, §07).** Identical machinery (sequences, deliverability, reply handling, SOBO) over a different subject and destination: sales prospects→deals/CRM vs candidates→hiring/ATS. Recruiting adds candidate-privacy compliance posture, LinkedIn/InMail channel depth, and ATS handoff. Pattern-level kinship; different directory family; no joint review required.
6. **vs Job Board / Career Site (inbound).** Direction of initiation: candidate-initiated application vs recruiter-initiated pursuit. Fetcher's new "inbound recruiting" product (screen inbound applicants, switch to outbound) bridges both directions — recorded as a packaging variant, not a Type merger.
7. **Taxonomy note.** "Talent Sourcing Platform" is a reasonable market-adjacent name (the market says "sourcing tool", "outreach/engagement tool", "recruiting automation", "candidate engagement"), but the market's dominant naming for the engagement layer is "sequences"/"campaigns"/"engagement". The leaf is real and commercially central (an entire product category — SourceWhale-class — exists for it); the identity rests on the engagement workflow, not the name.

## Historical / Market-Sample Check

- **Pre-digital staffing agency**: a sourcer's card file of identified people + a planned call/letter/call cadence + the returned call becoming a conversation + placement as the goal — satisfies the core with zero digital machinery. No multi-channel breadth, no analytics, no AI in the core.
- **Email-era (2000s) recruiter**: spreadsheet of prospects + mail-merge follow-up cadence from Outlook + replies in the inbox + logging into the ATS. Satisfies the core.
- **Modern era**: multi-channel sequences, AI drafting, deliverability tooling, engagement dashboards, agentic execution — era-common implementations, not invariants.
- Therefore the canonical core — pursued identified people + planned engagement effort + response loop — is era-robust.

## Uncertainties

- Beamery's engagement side was not directly observed this pass (sibling pass documented its record-layer pole; its helpdesk was unreachable there). The record-vs-activity seam rests on SourceWhale/Gem/hireEZ/Fetcher evidence plus the sibling pass's Gem/Beamery/Eightfold observations.
- Deliverability internals (warmup schedules, IP pools, verification vendors) only partially observed (SendGrid integration documented at SourceWhale; Gem deliverability best-practices article title only). Kept generic in the final document.
- Whether a single-channel-only sourcing product exists in the current market was not established; all sampled products are multi-channel. Multi-channel stays at L1.
- Stop-on-reply is directly documented only by Gem; for the others it is implied by reply tracking + conversation surfaces. The final document states stop-on-reply as a common implementation, not a universal rule.
- Numeric delivery/response claims are vendor marketing; no Type-level numeric claims are made anywhere in the final document.

## Final Synthesis

A Talent Sourcing Platform is the recruiting operation's **engagement-execution system**: it takes candidate people who have already been identified as worth pursuing — captured via browser extension, handed off from search tools, drawn from the employer's own database, or delivered by a managed service — and drives them toward a response through planned, time-spaced, multi-channel engagement sequences that mix automated sends with human-prompted steps, while managing deliverability from the recruiter's own identity, capturing replies into workable conversations, syncing every touch to the ATS/CRM record layer, and measuring the engagement motion itself (delivery, opens, replies, response rates, campaign performance). Its center of gravity is the engagement workflow over identified people — not the search that finds them (Candidate Search Platform), not the record that remembers them (Candidate Profile Platform), not the audience broadcast that attracts them (Recruitment Marketing), and not the pipeline that processes their applications (ATS). The staffing-agency variant aims the same machinery at client contacts as well as candidates. The core is era-robust: card-file-and-telephone sourcing satisfies it as fully as AI-drafted multi-channel sequences.
