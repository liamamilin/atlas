# Research Notes — Voice of Customer Platform

Research date: 2026-09-08
Directory leaf: Voice of Customer Platform (§07 Sales, Customer & Revenue)
Slug: voice-of-customer-platform

---

## Research Goal

Understand what a Voice of Customer (VoC) Platform actually is as an Application Type — what objects exist inside it, who uses it, how the work flows, what rules govern it — by studying real products' operational documentation, and separate the defining structure from common mature capabilities, variants, and vendor specifics.

Special attention owed to boundary disambiguation, because this leaf sits in a dense neighborhood: Survey Platform (§03.11, unprocessed), Customer Feedback Management (§07, processed 2026-09-08 — flagged a joint review with this pass), Complaint & Escalation Management (§07, processed — flagged), Customer Experience Management Platform (§07 sibling, unprocessed), Employee Survey Platform (§09, processed), Customer Success Platform / Customer Health Monitoring (§07, processed), Support Conversation Analytics (§06→07 adjacent, processed — recorded a "VoC-program framing" note), Social Listening Platform (§06, processed — flagged "solicited private structured feedback vs unsolicited public conversation" for this pass), Brand Reputation Management (§06, processed), Market/Consumer Research Platform (§06, processed), Online Form Builder (§03.11, processed).

## Initial Boundary (hypothesis before research)

- A VoC platform is the organization-side system for continuously asking its own customers structured questions about their experience, scoring the answers into experience metrics, and acting on the results.
- Likely confusions: survey tools (same instrument), customer-feedback-management (same "customer voice" language), customer-success (same customer-relationship seat), social listening (same "listening" metaphor).
- Unknowns at start: is the closed-loop/action layer definitional or just common? Is the metric layer definitional? Is solicited-vs-unsolicited the right substrate seam?

## Research Questions

1. What objects exist? (programs/campaigns, instruments, contacts, responses, metrics, themes, alerts, tickets, dashboards)
2. How are instruments deployed — what channels, what triggers, what campaign postures?
3. How are responses attributed (identity, interaction context)? Is anonymity a variant?
4. What metrics are computed and how are they tracked (trends, segments, per-customer history)?
5. What analysis machinery exists (text themes, sentiment, driver analysis, AI)?
6. What does "close the loop" mean concretely in each product — individual follow-up, systemic routing, both?
7. Who uses the product (program manager, frontline, executive, analyst) and what surfaces do they get?
8. What rules govern operations (throttling, opt-out, frequency, permissions, response-rate management)?
9. Where does this Type end and Survey Platform / Customer Feedback Management / Customer Experience Management begin?

## Representative Products

Selection: market representation + documentation accessibility + different product philosophies + different customer tiers.

| Product | Tier / posture | Philosophy | Evidence level reached |
|---|---|---|---|
| Qualtrics | Enterprise flagship | Broad experience-program platform ("listen → understand → act"), research heritage | Tier-1 (support site) + Tier-2 (VoC capability page) |
| Forsta (Forsta Plus; family incl. InMoment, ReviewTrackers, Rio SEO) | Enterprise, research heritage (Confirmit lineage) | Full-service research-grade CX with named VoC product page | Tier-2 (product/VoC pages); help center unreachable |
| AskNicely | SMB / multi-location service businesses | Frontline-operational: collect → respond → assess → transform → grow | Tier-1 (help center home/categories) + Tier-2 (site) |
| Retently | SMB / lightweight, NPS-first | Campaign + audience + trend machinery, self-serve | Tier-1 (help center, collections + article titles) |

Sample-width note: InMoment is now inside the Forsta family (login surface listed on forsta.com footer) and was not studied as an independent product. Delighted has been **discontinued and absorbed into Qualtrics** (delighted.com now redirects to a Qualtrics "Customer Feedback Software" page) — recorded as market-drift evidence, not used as a sample.

## Sources

Fetched 2026-09-08 (all URLs fetched live unless noted):

Qualtrics
- Support home: https://www.qualtrics.com/support/
- Getting Started with CX Dashboards: https://www.qualtrics.com/support/vocalize/getting-started-vocalize/vocalize-introduction/
- Getting Started with Surveys: https://www.qualtrics.com/support/survey-platform/getting-started/survey-platform-overview/
- VoC capability page (Tier-2): https://delighted.com/ (redirect target = Qualtrics "Customer Feedback Software / Voice of Customer" page)

Forsta
- Company/platform home: https://www.forsta.com/
- Voice of customer (Forsta Plus) page: https://www.forsta.com/platform/customer-experience/voice-of-customer/

AskNicely
- Product site: https://www.asknicely.com/
- Help Center home (Zendesk, Tier-1): https://asknicely.zendesk.com/hc/en-us

Retently
- Help Center home: https://help.retently.com/
- Survey campaigns collection: https://help.retently.com/en/collections/126058-survey-campaigns
- Customer management, segmentation collection: https://help.retently.com/en/collections/126045-customer-management-segmentation

Access limitations (evidence-degradation notes):
- Medallia: www.medallia.com returned HTTP 403 — not sampled; market anchor only. No Medallia-derived claims appear below.
- help.delighted.com returned HTTP 410 (product discontinued).
- Forsta help center (help.forsta.io) timed out twice — Forsta evidence is Tier-2 (product pages), so Forsta-specific mechanics stay out of cross-product core claims and Forsta observations are marked Tier-2.
- AskNicely category-level help pages timed out twice — AskNicely evidence is Tier-1 at category-description level (the help-home category tree text) plus Tier-2 product pages.
- InMoment: not fetched (absorbed into Forsta family per forsta.com footer login links).

---

## Product observations

### Qualtrics (Tier-1 support site + Tier-2 VoC page) — evidence layer A for product-specific claims

Key observations:

- Survey projects are the instrument container: question types, display logic, quotas, access control; edits previewed and **published with versions** (survey-publishing-versions documented).
- Distribution tab sends surveys via **email, SMS, or a single anonymous link**; "Depending on the distribution method, you may want to create a contact list first" — the contact list is the addressed customer audience.
- Workflows (Actions module) automate on survey events: documented examples include *sending another survey a number of days after a respondent completes the first* and *creating a ticket for the support team if a customer expresses dissatisfaction* — Tier-1 confirmation of both re-survey sequencing and dissatisfaction→ticket closed-loop routing.
- **Tickets** are a first-class object: "a means of tracking tasks in the Qualtrics XM platform… including them in your Qualtrics CX Program can help you action insights you gather from customer feedback."
- CX Dashboards (Dashboards projects): datasets combine data sources — surveys, imported data, **tickets, directories, other external sources**; fields map to survey questions/metadata; filters; recode values; roles for dashboard access; project administrators vs view-only dashboard users. Dashboards are the reporting surface "most often used in CX solutions."
- Vendor's own CX definition (support site): "satisfaction, digital experience, NPS data, customer churn and retention, customer journeys" — NPS named as a structured metric class.
- VoC capability page (Tier-2) frames the product as **Listen → Understand → Act**: "unifying solicited customer surveys with unsolicited mentions into one VoC platform" (digital intercepts, contact center calls, IVR, chat, SMS, email, social, review sites); AI theme/sentiment/impact analysis combined "with structured metrics like NPS and CSAT"; Act = **inner loop** (real-time individual responses to survey feedback) + **outer loop** (route recurring issues to teams enterprise-wide), intelligent ticketing into ServiceNow/Zendesk/Salesforce, and role-based dashboards — "executives see impact, managers see coaching opportunities, frontline sees next actions."
- Conversational feedback (AI follow-up probes on low-detail responses) is an era-current capability (Tier-2).

### Forsta (Tier-2 product/VoC pages) — evidence layer A for page-level claims, no Tier-1 mechanics

Key observations:

- The vendor sells a product literally titled **"Voice of customer: Forsta Plus"**: "Listen across every touchpoint, uncover sentiment, and act fast to improve experiences… strengthen CX, close the loop, and fuel business growth."
- Named modules on the VoC page: **SmartHub** ("capture and unify customer data from surveys, call centers, social media, purchase history, and more"), **Survey Designer** ("create surveys tailored to your brand and goals. Simple or in-depth, no coding required"), **Studio** ("design reports, dashboards, and workflows… breaking down data silos"), **Panel Management**, **Action Management** ("automate actions to initiate, coordinate, and accelerate feedback responses across your organization").
- Real-time feedback "at every touchpoint": customized brand surveys, "capture feedback across channels," 250 languages, accessibility compliance, full-service or self-service support mix.
- AI text analytics (Narrative HX): sentiment, emotion, intent, effort, emerging themes from unstructured feedback; triggers "action workflows… operational response and issue resolution"; sentiment tracked over time.
- Suite adjacency: the same CX platform section offers Digital Feedback (embedded surveys), Contact Center, Omnichannel Analytics, Crowdsourcing; Brand Experience handles reviews/listings — i.e., reputation/review machinery is packaged as a sibling module, not the VoC core.
- Family consolidation: forsta.com footer lists InMoment, ReviewTrackers, Rio SEO login surfaces under Forsta — the classic VoC mid-market player InMoment now sits inside the Forsta group.

### AskNicely (Tier-1 help-center home + Tier-2 site) — evidence layer A for category-structure claims

Key observations:

- The help center's own category tree is the product's declared operating loop: **Collect** ("send surveys, gather responses, maximize response rates") → **Respond** ("take action & close the loop… address customer concerns quickly and resolve complaints with automated workflows before they escalate") → **Assess** ("dashboards, reports, and insights… spot trends… measure success at every level") → **Transform** ("frontline behavior & service delivery… transparent, actionable feedback loops that motivate, highlight coaching opportunities") → **Grow** ("reviews & reputation management").
- Plus: Contacts & Data Management; Integrations & Technical Configuration (Salesforce knowledge hub promoted); Account Administration/User Management/Security & Privacy.
- Product site: "NPS and CSAT measurement programs that keep your whole team in the loop"; built for multi-location service businesses with views "from the head office, to the branch manager, to individual customer-facing employees"; real-time sentiment converted into "simple, daily actions"; employee activation (leaderboards, coaching, rewards — "team leads actually compete to get to the top of the AskNicely leaderboard"); reputation/review generation as an adjacent product line.
- Survey logistics surfaced at Tier-1 home: Multiple Survey Templates, CSV Importer (contact import), Sending Surveys From Your Email Domain, Focus Areas.

### Retently (Tier-1 help center) — evidence layer A

Key observations (from collection home + article titles):

- **Campaigns** are the program unit: "Regular Survey Campaigns" (recurring email/in-app sends on a schedule) vs **Transactional Survey Campaigns** (event-triggered: "Send a survey when a Shopify order is delivered"; triggers documented for Salesforce, Chargebee, Freshdesk, Zendesk, HubSpot, Zoho CRM, Klaviyo, Segment, Yotpo, Zapier, generic webhook, API — "trigger transactional NPS surveys" via API).
- Channels: email, SMS, in-app/web surveys, embeds, link surveys (identified or **anonymous**), **kiosk mode** on shared devices, website feedback button.
- **Audience** = the customer population of record: contacts imported via CSV/CRM, customer properties/tags/attributes (with historical attribute values), campaign audience filters, audience sampling, opt-out ("customers who opted out"), "Last survey date" filters, "At Risk" customer status, **Customer profile** showing "the dynamics of his satisfaction with your product or service" — per-customer score history.
- **Accounts Page / Companies**: company records grouping contacts, company profiles, merge — the B2B account layer.
- **Responses/feedback management**: alerts (customizable email alert body/subject; filtered by contact attributes and by topics assigned to responses; outbound-webhook export of survey data), **autoresponders/autoreplies** ("automatically follow-up on customer feedback"), new-response notifications.
- **Measurement**: "Customer Experience metrics you can track with Retently" (NPS-class among them); Reports & Analytics organized as **Trends and Trend Groups**.
- **Text analysis**: "Automated topic & sentiment classification — automatically analyze your text feedback and categorize it into industry-specific topics and identify the feedback sentiment."
- **Anti-over-surveying**: "Survey throttle and how it can help over-surveying", throttling and imported feedback, daily survey limits.
- Survey logistics: reminders, time frames, scheduling, multi-language surveys, campaign folders/views.

---

## Cross-product Comparison

| Structure | Qualtrics | Forsta | AskNicely | Retently | Reading |
|---|---|---|---|---|---|
| Org-configured question instruments fielded to own customers | Survey projects + Distributions | Survey Designer | Survey templates (Collect) | Campaigns with survey templates | Universal |
| Experience-metric questions as a distinct class (NPS/CSAT/CES-class) | "structured metrics like NPS and CSAT" | "monitoring CSAT or NPS" (brand page); VoC page | "NPS and CSAT measurement programs" | "Customer Experience metrics you can track" | Universal as metric class; no single metric definitional |
| Standing customer audience of record | Contact lists (Tier-1) | SmartHub/CRM unification (Tier-2) | Contacts & Data Management (Tier-1 category) | Audience with properties/segments/opt-out (Tier-1) | Universal |
| Event/transaction-triggered fielding alongside recurring fielding | Workflows example: re-survey days after completion | "real-time feedback at every touchpoint" | Collect category (response-rate maximization); integration-driven sends | Regular vs Transactional campaigns, explicit trigger-service catalog | Universal as two postures |
| Identified response records bound to customer + context | Contact-list distributions; embedded data | Tier-2 ("unify customer data") | Contacts & survey linkage (Collect/Assess) | Customer profile with satisfaction history; customer identification options for link surveys; anonymous link as variant | Universal; anonymity = variant |
| Metrics tracked as trends over time, segmented | CX Dashboards (datasets, fields, filters) | Studio dashboards; sentiment over time | Assess (AI dashboards, reports, "every level") | Trends and Trend Groups | Universal |
| Open-text theme + sentiment analysis | Text iQ / Assist (Tier-1 + Tier-2) | Narrative HX | NiceAI | Automated topic & sentiment classification | Universal (era-current AI forms; rules-based predecessor) |
| Individual-response follow-up routing (alerts / tickets / auto-replies) | Workflow → ticket on dissatisfaction; Tickets object | Action Management | Respond: close the loop with automated workflows | Alerts + autoresponders + webhook routing | Universal — 4/4 |
| Systemic action layer (reports to owners, enterprise routing) | Outer loop (Tier-2); dashboard roles (exec/manager/frontline) | "accelerate feedback responses across your organization" | Transform (frontline coaching); Assess per-level | Filtered alerts; trend reports | Universal in posture, depth varies |
| Response-rate/over-surveying governance | (not verified this pass) | (not verified this pass) | "maximize response rates" (category text) | Survey throttling, last-survey-date, daily limits | Documented in 2/4; held as common, not definitional |
| Opt-out handling | (not verified this pass) | (not verified this pass) | (not verified) | Opted-out customers viewable | Documented 1/4 explicitly; held as expected norm, not definitional |
| B2B account layer (companies over contacts) | (not verified this pass) | (not verified this pass) | (not verified this pass — multi-location org hierarchy instead) | Accounts Page / Companies | Held Optional / segment variant |
| Review/reputation extension | Social/review listening inside VoC umbrella (Tier-2) | Brand Experience as sibling module | Grow category (reviews & reputation) | — | Adjacent module, not definitional |
| Multi-language / branding / white-label | (not verified this pass) | 250 languages, brand-matched surveys | (not verified) | Multi-language surveys; white-label collection | Common; not definitional |
| AI assistance (conversational probes, NL Q&A over feedback) | Qualtrics Assist, Conversational Feedback | Narrative HX, Forsta AI | NiceAI / NiceAI Agents | Fin; MCP connector (help center) | Era-current layer, not definitional |

## Abstraction Hierarchy

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being a VoC platform:

1. **The experience program of record.** Standing, organization-configured question instruments — carrying experience-metric questions (NPS/CSAT/CES-class) and open text — fielded by the organization **to its own customers** across defined touchpoints, operated continuously in two canonical postures: relationship-cadence (recurring sends to the customer base / segments) and transaction- or event-triggered (fired from business-system events at interaction endpoints). Remove → a generic survey/form tool; nothing "customer-experience-program" remains.
2. **The attributed response record.** Each response is held as an identified record bound to (a) the customer — a contact, and where supported the company/account — and (b) the context of the rated interaction (the event/trigger, channel, touchpoint), accumulating into per-customer and program-level history. Remove → anonymous poll or aggregate tabulation — measurement without a customer-relationship substrate.
3. **The experience measurement layer.** Responses are continuously computed into experience metrics (scores tracked as trends over time, segmentable by touchpoint/segment/cohort) and open-text is classified into themes/sentiment — the quantified "voice." Remove → a raw response archive / collection bucket.
4. **The follow-up routing loop.** Individual responses — especially adverse ones — are routed outward to accountable people for action (alerts, auto-replies, tickets/cases, frontline follow-up queues), alongside reporting surfaces that drive systemic action ("close the loop" in every sampled vendor's own vocabulary). Remove → research-style measurement and reporting with no operational follow-up — the below-Type thin ancestor.

Jointly-held is load-bearing:
- 1 alone = survey platform (§03.11 territory)
- 2 without 1 = CRM/contact store with response log
- 3 without 1+2 = a scoring model with no program behind it
- 4 without 1+2+3 = an alerting workflow on raw form submissions
- 1+2 without 3+4 = a survey tool pointed at customers
- 2+3 without 1+4 = research tabulation of collected responses
- 1+4 without 2+3 = send surveys and ping people, no measurement (unstable, not observed)
- 2+3+4 without 1 = scoring/alerting over unsolicited data = support-conversation-analytics territory

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Relationship + transactional program pairing deployed across multiple channels: email, SMS, web/app intercepts & embeds, link pages, kiosk/QR, in-product surfaces
- Contact/audience management: import (CSV/CRM sync), attributes, tags, segments, audience filters, sampling
- Role-scoped dashboards and reporting tiers (executive / manager / frontline), shareable views
- Response-rate management and over-surveying governance (throttling, frequency rules, last-survey-date logic, reminders)
- Per-customer profile with personal score/response history; at-risk style flags
- Text analytics at theme/topic + sentiment granularity, feeding dashboards and alerts
- Integrations spine: CRM/helpdesk/commerce events in (trigger surveys), tickets/cases out (follow-up), webhooks/APIs both ways
- Multi-language instruments, branding/white-labeling
- Program governance surfaces: users/roles/permissions, opt-out handling, security/privacy settings

### L2 — Variant / Optional Structure

- **Posture poles** (all in-Type): enterprise multi-touchpoint program platform; research-heritage full-service platform (Forsta Plus; service-led delivery); lightweight self-serve metric tool (NPS-first campaigns); frontline-operational multi-location pole (coaching/leaderboards)
- **Solicited-heavy vs unified-listening posture**: some products unify unsolicited sources (social, reviews, call-center conversations) with solicited surveys under one VoC umbrella — a packaging variant that blends into Social Listening / Support Conversation Analytics without erasing the solicited core
- B2B account-experience variant (company/account-level scores over contact-level responses) — evidenced in sample at 1/4 (Retently Accounts Page), product-class-anchor in the account-experience niche; held Optional
- Review/reputation extension (review generation, publishing) — adjacent module in several products, out of core
- Vertical configurations (hospitality, healthcare, insurance, retail) and industry topic models for text classification
- Benchmarks / comparative norms — present in the class but not verified this pass; do not assert

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Qualtrics: CX Dashboards/Vocalize naming; Dashboards data modeler (joins/unions), recode, field types & widget compatibility; Tickets task object; Text iQ Topics Starter Packs; Experience Agents intelligent ticketing (ServiceNow/Zendesk/Salesforce); Conversational Feedback claims (85% AI-prompted follow-up response, 42% richer insights); inner-loop/outer-loop framing; free account tiering; Brand Administrator / user-permissions model
- Forsta: SmartHub, Narrative HX (+90% accuracy / 2x recall claims), Studio, Panel Management, Action Management; Digital Focus Groups, Crowdsourcing, Omnichannel Analytics (Spotlight), Contact Center; 250-language claim; "99.6% predictive accuracy" agentic-AI claim; family brands (Research HX/FocusVision, InMoment, ReviewTrackers, Rio SEO); account-director service model
- AskNicely: NiceAI / NiceAI Agents; NiceReferral; Focus Areas; leaderboard/employee-activation mechanics; start.asknice.ly login domain; own-email-domain sending; multi-location hierarchy (head office / branch / employee views); Cinch NPS −13.7 → 40+ customer story
- Retently: throttling rules and daily-limit reset times; kiosk mode on shared devices; feedback button script/template management; Segment/Chargebee/Shopify/Freshdesk/Zendesk/HubSpot/Zoho/Klaviyo/Yotpo trigger-service catalog; generic inbound webhook contact-data mapping; historical customer attributes; outbound-webhook alert export; "At Risk" audience status; Fin/MCP AI surfaces; 100k+ CSV import guidance

## Rejected Findings

- **"VoC = NPS software."** NPS is one common metric realization. Retently (NPS-first) documents "Customer Experience metrics" plural; AskNicely pairs NPS with CSAT; Qualtrics names NPS and CSAT. The definitional abstraction is "experience-metric question," not any named metric. (Anti-overfitting rule: the NPS-first pole is a market posture, not the Type.)
- **"VoC platforms own all feedback channels."** Qualtrics' Tier-2 page unifies social/review/call-center data, but that is a suite-packaging posture; Forsta packages reputation/contact-center as sibling modules; Retently/AskNicely cores are survey-fed. The defining substrate is the solicited instrument to the org's own customers; unsolicited unification is a variant posture.
- **"Closed loop = marketing language only."** Rejected as a dismissal — the follow-up routing loop is documented as first-class machinery in 4/4 sampled products (named modules, help categories, workflow objects), so it is held inside the defining core rather than waved away as messaging.
- **"VoC = Customer Experience Management."** Deferred to the joint review with the unprocessed customer-experience-management-platform sibling (see Boundary Findings). This pass does not collapse them by assumption.
- **"AI analysis is definitional."** All sampled products now ship AI theme/sentiment surfaces, but the 2000s EFM generation ran rules-based classification and still satisfies the L0; AI is an era-current implementation layer.

## Historical / Market-Sample Check (per §24 reasoning, applied)

- **Paper-era ancestor**: guest comment cards collected at checkout (instrument at a defined touchpoint), cards tied to registered guest identity (attributed response), monthly CSAT tallies and trend charts reviewed by management (measurement layer), and follow-up calls/letters to named dissatisfied guests (routing loop). All four legs hold at analog level with zero modern machinery.
- **2000s EFM (Enterprise Feedback Management) generation** (Confirmit-heritage class): survey authoring + panel/contact distribution + real-time alerts on low scores + score reporting — satisfies the four legs without AI, social unification, intercept builders, or cloud delivery.
- **Consequence for the core**: no AI, no NPS specificity, no specific channel set, no cloud/SaaS, no intercept builder, no benchmarks in the defining core. NPS/CSAT/CES are the common modern realizations of "experience-metric question."

## Boundary Findings

| Neighboring Type | Relationship | Seam / "remove what to become the other" |
|---|---|---|
| Survey Platform (§03.11, unprocessed) | closest shared machinery | Both author instruments and collect responses. VoC is defined by the **standing experience program on the org's own customer base** (program of record + attributed response + experience metrics + follow-up routing). Remove the program posture/customer anchoring/metric+loop layers and only general-purpose survey machinery remains → Survey Platform. Joint review recommended from this side (survey-platform pass not yet run). |
| Customer Feedback Management (§07, processed 2026-09-08) | sibling, seam confirmed from both sides | Their unit of record = **item-level volunteered feedback** (request/idea/problem) aggregated into demand signals tracked to product decisions. This Type's unit of record = **response to an organization-fielded instrument**, scored into experience metrics and routed for follow-up. Asked vs volunteered; metric vs item. DISCHARGES that pass's joint-review flag: keep-both ratified from this side (UserVoice-class products span both — packaging straddle, not Type collapse). |
| Customer Experience Management Platform (§07, unprocessed) | sharpest taxonomy risk | The market labels Qualtrics/Medallia-class products both "VoC platforms" and "customer experience management platforms." This pass defines VoC at the solicited-experience-program machinery level. Whether CEM is (a) an alias of this Type, (b) a broader journey/orchestration-centered Type, or (c) a suite level must be decided by that pass. **Taxonomy flag recorded; joint review required.** |
| Complaint & Escalation Management (§07, processed) | adjacent; discharge | That pass governs **formal dissatisfaction individually to resolution** with statutory/regulated response lifecycle and escalation paths. VoC's follow-up loop is service-recovery routing (alerts/tickets), not governed complaint adjudication; a low score may feed a complaint record, but VoC neither opens nor manages the regulated case. DISCHARGES that pass's joint-review flag against both feedback siblings. |
| Employee Survey Platform (§09, processed) | same machinery, different population | That Type is employee-anchored (HRIS-synced population, engagement programs). VoC is customer-anchored (CRM/commerce-synced population, experience metrics). Same instrument substrate; population + purpose define the Type. Some platforms (Qualtrics, Forsta) ship both as sibling solution areas — confirming the seam. |
| Customer Success Platform (§07, processed) | consumer/producer seam | CS aggregates multi-source signals (incl. survey results) into account health and runs managed relationship work (plans, plays, book reviews). VoC **produces** the solicited experience signal itself and routes individual follow-ups; it does not own account health definitions or success planning. CS platforms consume VoC output; seam held. |
| Customer Health Monitoring (§07, processed) | signal vs account-state | VoC metrics are survey-derived experience measures over the response program; CHM maintains per-account multi-signal health states with monitoring loops. A VoC per-customer score history is a signal input to health, not a health definition. |
| Support Conversation Analytics (processed) | solicited vs unsolicited, discharge | That pass recorded "VoC-program framing — the analytics layer operated as the organization's voice-of-customer engine for the unsolicited channel, paired with survey platforms for the solicited channel." DISCHARGED from this side: VoC = the **solicited** channel's program system; conversation analytics = the unsolicited conversation corpus. Qualtrics' unified-listening packaging blends both without merging the Types. |
| Social Listening Platform (§06, processed) | discharge | Standing watch over **public third-party conversation** vs fielded instruments to **own customers** (private, structured, consented). DISCHARGES that pass's flag: substrates differ (third-party public speech vs first-party solicited response), despite "listening" vocabulary shared by vendors. |
| Brand Reputation Management (§06, processed) | public review loop vs private program | That Type operates on public review/rating signals with per-entity response. VoC operates on private solicited responses. Review-generation modules inside VoC products (AskNicely Grow, Forsta Brand Experience) are adjacent packaging. |
| Market/Consumer Research Platform (§06, processed) | own customers vs platform-supplied audiences | Consumer research studies consumers via platform-supplied panels/syndicated datasets for brand/category decisions; VoC instruments the organization's own customer base for its own experience operations. A satisfaction study inside consumer research = one-off research; a VoC program = standing operational system. |
| Online Form Builder (§03.11, processed) | instrument substrate only | Form builders collect structured submissions from anonymous respondents by default; VoC's response records are customer-attributed experience data inside a metric-and-loop program. A feedback form is the thin capture end; the program machinery is the Type. |
| Contact Center / IVR platforms | adjacent systems | Post-interaction surveys sometimes fire from contact-center events and VoC programs ingest call metadata (Forsta SmartHub lists call centers as a data source; Qualtrics lists IVR/calls). The survey program remains VoC; the conversation/routing machinery is contact-center territory. |

## Uncertainties

- **Medallia** could not be fetched (403). The classic three-way enterprise shape (Qualtrics / Medallia / InMoment) is anchored from Qualtrics/Forsta evidence and the InMoment-into-Forsta consolidation, but no Medallia-derived claim is used. Enterprise-pole breadth (e.g., operational data integration depth) is asserted only at the level the fetched evidence supports.
- **Benchmarks**: several vendors in this class market industry benchmarks; not verified this pass — excluded from all claims.
- **B2B account-layer prevalence**: evidenced at Tier-1 only in Retently; the account-experience niche (CustomerGauge-class) was not fetched. Held Optional/variant; prevalence unknown.
- **Driver analysis / key-driver statistics**: present in the class per marketing vocabulary ("impact rankings" — Qualtrics Tier-2), not verified at Tier-1 depth; held as analysis-layer capability without method claims.
- **Qualtrics contact-frequency / throttling machinery**: not verified this pass (only Retently documents throttling at Tier-1; AskNicely documents response-rate maximization at category level). Over-surveying governance held Common, not definitional.
- **Prospective/non-customer audiences** (e.g., market-prospect surveys inside VoC tools): not verified; the core is written as "the organization's own customers," with the note that the audience is org-defined.

## Final Synthesis

A Voice of Customer Platform is the organization's standing solicited-experience program system: it fields organization-configured question instruments — carrying experience-metric questions and open text — to the organization's own customers at defined touchpoints (recurring relationship cadence and event-triggered transaction moments), holds every response as an identified record bound to customer and interaction context, continuously computes those responses into tracked experience metrics and text themes, and routes individual responses — adverse ones above all — to accountable owners for follow-up while reporting program-level results to the owners of the experience.

The four structures are jointly held: instruments without attribution is a survey tool; attribution without measurement is a log; measurement without routing is research reporting; routing without program is an alerting pipe. The market realizes the Type on a spectrum from enterprise program platforms through research-heritage suites to lightweight NPS/CSAT campaign tools and frontline-operational systems — one core, four postures. The defining core excludes AI, any named metric, specific channels, cloud delivery, and unsolicited-channel unification; all are era-current or variant layers confirmed against the paper-era ancestor (comment cards + tallies + follow-up calls) and the 2000s EFM generation.

Market drift recorded: Delighted (lightweight NPS tool) discontinued/absorbed into Qualtrics; InMoment absorbed into the Forsta family; suite vendors increasingly repackage VoC as part of broader "experience" platforms — consolidation is shrinking the number of independent pure-plays while the machinery of the Type remains stable.
