# Research Notes — Petition / Public Comment Platform

Research date: 2026-09-09
Leaf: Petition / Public Comment Platform (§24 Government, Public Sector & Civic)
Slug: petition-public-comment-platform

## Research Goal

Understand what a "Petition / Public Comment Platform" is as an Application Type: what the unit of record is (petition? comment? campaign?), who initiates campaigns (citizen or institution), what participation looks like (signing vs commenting), what rules gate formal handling (thresholds, verification, committee review), how the institution's disposition is recorded and published, and where the Type's boundaries sit — especially against the processed sibling **Civic Engagement Platform** (whose pass flagged this leaf for joint review), the unprocessed sibling **Rulemaking & Public Consultation Platform**, **311 / Citizen Service Request Platform**, and adjacent Types (Advocacy Platform, Survey Platform, donation/crowdfunding).

## Initial Boundary

Hypothesis before research: the leaf name combines two faces —

- **petition**: a citizen-initiated demand addressed to a decision-maker, promoted by a signature campaign, with signature thresholds gating formal handling;
- **public comment**: an institution-opened period during which the public submits comments/responses on a specific proposal, which the institution analyzes and answers.

Shared candidate core: a bounded, publicly visible **input campaign of record** addressed to an institutional decision context, collecting **attributed citizen input** that accumulates publicly, with the institution's **disposition published back** onto the record.

Known seams from prior passes:

- civic-engagement-platform (processed) recorded: "the petition Type's defining object is a signature campaign on a specific demand with a threshold and formal handling… Boundary test: if the platform's primary and only object is the petition/signature campaign, it is the Petition Type; if petitions are one mechanism inside composed engagement spaces, it is a Civic Engagement Platform." (research/civic-engagement-platform.md §Boundary Findings)
- government-transparency-portal (processed) recorded: portals publish one-way; engagement mechanisms (petitions, consultations, public comment) are participatory process machinery — a different Type.

## Research Questions

1. What is the unit of record, and do the petition and public-comment faces share one structure or two?
2. Who initiates a campaign, and what does initiation require (supporters, organiser committee, registration, operator publishing)?
3. What admission gates exist before a campaign goes live (standards checks, eligibility registration, technical validation)?
4. What does participation look like — signature vs structured response — and what identity/eligibility rules apply?
5. What gates formal handling: signature thresholds, verification, committee consideration, statutory obligation?
6. What is the formal handling loop: who responds, in what form, on what timeline, and where is the disposition published?
7. What lifecycle states does a campaign move through (draft → admission → open → closed → handled)?
8. What is public on the record: campaign text, input counts, individual inputs, responses, outcomes?
9. Where are the boundaries: vs Civic Engagement Platform, Rulemaking & Public Consultation Platform, 311, Advocacy Platform, Survey Platform, donation/crowdfunding, meeting-centric public comment?
10. Historical check: do paper-era petitions and written-comment procedures satisfy the same core?

## Representative Products

Selection principles applied: market representation across the petition and public-comment faces; documentation completeness; different product philosophies (government-run service vs open-source framework vs commercial SaaS vs open hosting); different customer tiers (parliament, supranational institution, municipality, any campaigner).

| Product | Pole | Why sampled | Evidence tier reached |
|---|---|---|---|
| UK Parliament Petitions (petition.parliament.uk) | government-run petition service with formal thresholds | the canonical parliament-operated e-petition system; help documentation reachable | Tier-1 (official help pages) |
| European Citizens' Initiative (citizens-initiative.europa.eu) | supranational government-run initiative instrument | registration + verification + Commission response machinery; step-by-step official guide | Tier-1 (official how-it-works) |
| Decidim (Initiatives space) | open-source municipal participatory framework, petition-shaped space | the straddling pole for the civic-engagement boundary; docs reachable | Tier-1 (official docs) |
| Citizen Space (Delib) | commercial consultation/public-comment platform for institutions | the consultation face's commercial pole; knowledge base reachable | Tier-1 (official KB) + Tier-2 (product pages) |
| GoPetition | open petition hosting (consumer pole) | consumer-host philosophy; editorial/guidance content reachable | Tier-2/3 (official editorial content) |

Attempted but unreachable (recorded as limitations, not compensated from memory):

- **Change.org** — help.change.org and change.org/about both timed out twice. The largest consumer petition platform is held as a market anchor only; no operational claims asserted.
- **Regulations.gov** — /about and /help both returned 403 twice. The US federal public-comment portal is held as a market anchor only; docket/comment mechanics not asserted.

## Sources

- UK Parliament Petitions — "How petitions work" — https://petition.parliament.uk/help — fetched 2026-09-09 (Tier-1)
- European Citizens' Initiative — "How it works" — https://citizens-initiative.europa.eu/how-it-works_en ; homepage https://citizens-initiative.europa.eu/index_en — fetched 2026-09-09 (Tier-1)
- Decidim Documentation — "Participatory spaces" (Initiatives, Consultations) — https://docs.decidim.org/en/develop/features/participatory-spaces ; "Components" — https://docs.decidim.org/en/develop/features/components — fetched 2026-09-09 (Tier-1, develop branch)
- Delib Knowledge Base (Citizen Space) — "Activity types" https://help.delib.net/article/171-citizen-space-activity-types ; "Response publishing — what is it?" https://help.delib.net/article/103-response-publishing-what-is-it ; "The status of your activity" https://help.delib.net/article/345-the-status-of-your-activity-open-closed-and-forthcoming ; "Publishing results and outcomes" https://help.delib.net/article/308-publishing-results-and-outcomes ; category listings (creating/managing activities; response publishing) — fetched 2026-09-09 (Tier-1)
- Delib — corporate/product pages — https://www.delib.net/ — fetched 2026-09-09 (Tier-2)
- GoPetition — "How to write a petition" — https://www.gopetition.com/how-to-write-a-petition — fetched 2026-09-09 (Tier-2/3, official editorial content)

## Product Observations

### UK Parliament Petitions (petition.parliament.uk) — Tier-1

From the official help page ("How petitions work"):

- Purpose framing: "You can call for action from the UK Government or UK Parliament by creating and submitting an e-petition." The petition is a **call for action** addressed to the Government or Parliament. (A)
- Eligibility: only British citizens and UK residents can create; signers must also be British citizens or UK residents. (A)
- Creation flow: write a clear petition action; provide details about what should happen and why; **get five supporters** so the petitions team can check it; confirm identity details (full name, email, UK postcode); at the pre-publication stage a maximum of 21 people can sign. (A)
- Duplicate control: the form asks creators to "check there isn't already a petition asking for a similar action". (A)
- Admission gate: after five supporters, the petitions team checks the petition against published **standards**; petitions that fail are **rejected** (with reasons; rejected petitions are viewable but not signable). (A)
- Bounded window: once published, the petition is **open for 6 months** to gather signatures. (A)
- Threshold semantics: **10,000 signatures → the Government must respond** (response by the responsible department, published on the same page as the petition with its date); **100,000 signatures → considered for debate** by the Petitions Committee, and "usually debated" (the committee may decide not to arrange a debate, e.g. if recently or soon-to-be debated). (A)
- Formal handling body: the **Petitions Committee** — a group of 11 MPs from government and opposition parties — considers e-petitions and may contact creators. (A)
- Jurisdictional scoping: petitions must ask for action on something the UK Government or Parliament is responsible for (local-council matters are out of scope); the Government is "only obliged to respond to e-petitions started on petition.parliament.uk" — the platform is the official channel of record. (A)
- Paper petitions and recall petitions are explicitly separate tracks outside this website. (A)

### European Citizens' Initiative (ECI) — Tier-1

From the official how-it-works guide:

- Purpose framing: "calling on the European Commission to propose new laws. If an initiative has reached 1 million valid signatures, the Commission will decide on what action to take." (A)
- Step 1 — organisers: an initiative must be launched by a **group of organisers of at least 7 EU citizens living in 7 different EU countries**. (A)
- Step 2 — registration: before collecting signatures, the organisers ask the Commission to **register** the initiative (organiser account; description in an official EU language; details on the group, funding). The Commission "is not obliged to register all initiatives" — it registers those meeting certain criteria; answer within 2 months (or 4 in some cases); registered initiatives are published on the site. (A)
- Step 3 — collection: at least **1 million valid signatures**, with **country-level thresholds in at least 7 countries**; supporters fill a specific **statement of support form**; collection **on paper** (pre-filled forms from the organiser account) or **online** (official online collection system); a kick-off date must be set (at latest 6 months after registration) and notified; **12 months** to collect; signers must be EU citizens old enough to vote in European elections (or at least 16 in some countries). (A)
- Step 4 — verification: statements grouped by nationality and sent to **responsible national authorities** (3 months to submit; authorities 3 months to verify validity and issue **certificates**); the Commission provides a secure file-exchange service for paper-collected statements. (A)
- Step 5 — submission: within 3 months of the last certificate, the initiative is submitted to the Commission with support and funding information. (A)
- Step 6 — answer: within 1 month a meeting with Commission representatives; within 3 months a **public hearing at the European Parliament** (Parliament may hold a plenary debate and adopt a resolution); within 6 months the Commission sets out **what action (if any) it will propose**, with reasons, as a formally adopted communication published in all official EU languages. (A)
- Follow-up: the Commission is not obliged to propose legislation; other (non-legislative) action is possible; Parliament may assess the measures taken. (A)

### Decidim — Initiatives space (and Consultations) — Tier-1

From official documentation (develop branch):

- Decidim's structure: **participatory spaces** (initiatives, processes, consultations, assemblies) containing **components** (proposals, debates, surveys, meetings, budgets, accountability…). (A)
- **Initiatives**: "This participatory space allows citizens to make proposals and collect the requisite number of signatures and/or endorsements depending on type (the various types are set out in the municipal regulations), giving rise to the start of the administrative procedure for its processing and citizen monitoring." (A)
- Initiative flow: any person or citizen association can create one; **several initiative types** with configurable signature requirements; **duplicate avoidance** — the system presents similar initiatives before continuing; the creator receives a URL to invite endorsements; a **map of physical signature-collection points** can be shown. (A)
- Admission gate: after creation, the initiative enters a **technical moderation and validation** stage — staff can approve, reject, or suggest amendments. (A)
- Monitoring: status notifications; the promoter (individual or group) can send newsletters to followers. (A)
- End states: on reaching the end date — **Rejected** ("does not meet the number of signatures required") or **Accepted** (sufficient signatures → "the corresponding procedure will start"). (A)
- Admin machinery: initiative types; promoter's committee; author actions; initiative management (committee members, components, attachments, moderations); **"Answer an initiative"** (institutional answer). (A)
- **Consultations** (separate space): a voting procedure on specific questions, with a gateway to an **external e-voting system** for identity management and verification. (A)
- Reading: the Initiatives space is petition-shaped (signatures, committee, accept/reject, procedure start) inside a composed participatory platform — the straddling evidence for the civic-engagement boundary.

### Citizen Space (Delib) — Tier-1 (KB) + Tier-2 (product pages)

From the official knowledge base:

- Activity model: an **activity** is the unit of work; core activity types: **Survey** (gather feedback/opinions; "tailored to publishing a report, based on full set of responses"), **Consultation** ("designed for running formal consultation activities, with a custom timeline feature"; for "projects or processes that have defined phases or key milestones"), **Form** (collect structured factual data), **Event registration**, **Call to Action page**. (A)
- Activity lifecycle: **Forthcoming / Open / Closed** statuses driven by open/close dates; open activities automatically close at the set date; a closed activity's call-to-action is replaced by text such as "What Happens Next" or **"We Asked, You Said, We Did"** information. (A)
- Activity page: an **Overview page** with introductory text, related documents/links, and a call-to-action box; configurable landing pages; QR codes for activities; private vs public activities; cloning; warnings around editing published activities. (A)
- **Response publishing**: a feature to "publish submissions from respondents… citizens can see what other people have said"; responses anonymous or published with identifying information **if consent is given** (a **consent question** captures permission); full control over which answers are published; qualitative answers go through **moderation and redaction** (moderation workflow, assigned moderators); publishable while the activity is open or after it closes; **publishable replies** let analysts add comments to individual published responses; display customisation; export of moderated/published responses; support for **offline responses and supporting documents**. Rationale given: transparency, showing "what has been done with their input", and "Some activities, such as planning consultations, have a statutory requirement to publish the submitted responses." (A)
- **Publishing results and outcomes**: two mechanisms — **Publish Results** (file/URL/text findings on the overview page; PDF summary report) and **"We Asked, You Said, We Did"** (three text boxes: what was asked, what respondents said, what was done; displayed at the top of the overview page once closed; optionally aggregated on a site-wide outcomes page). Both optional but framed as best practice ("closing the loop"). (A)
- Analysis: "Analysis and reporting back" category (42 articles) — managing and interpreting responses; response exports; communicating with respondents. (A, category structure)
- From product pages (Tier-2): positioning — "Software, service and support for people who run public consultation and engagement activities"; "secure, reliable govtech platforms that meet the exacting standards required for statutory consultation and democratic engagement"; pillars: publish information (accessible formats for complex documents), gather feedback (surveys), analyse responses, build public trust; use cases: Consultations, Public Inquiries, Permitting & Licensing, Community Engagement, Spatial Planning, Calls for Evidence; sectors: central/local/state-federal government, regulatory bodies; "600+ global government organisations", "10M+ citizen responses". (A for positioning claims as vendor statements)

### GoPetition — Tier-2/3 (official editorial content)

From the platform's own guidance pages:

- Petition anatomy: a **preamble** (background information) followed by the body containing the **"core petition text"** — "the exact call for action - the request - that signers will be asked to support"; guidance to describe the situation, suggest what is needed and why, and provide a concise call to action. (A, as vendor guidance)
- Targets: "Governments, parliaments, politicians…; Political parties, presidents…; Educational institutions; Sports organizations; Media organizations; Entertainment producers…; Neighborhood authorities or home owner associations" — petition addressing is not limited to government. (A, as vendor guidance)
- E-signature posture: "The status of electronic signatures… is in its infancy"; the platform "provide[s] for the collection of a variety of data fields… custom software so you can build your own fields and collect the data you need". (A, as vendor guidance)
- Formal standing: consumer-hosted petitions have **"persuasive effect"** even when they "do not strictly comply with jurisdictional standing orders" — the platform explicitly contrasts itself with parliamentary e-petition systems (Scottish e-Petitioner pioneering service; UK E-petitions with the 100,000-signature debate threshold; Queensland parliament e-petitions under Standing Orders; European Parliament petitions under Article 227 TFEU; White House We the People with a 100,000-signature review threshold). (A, as vendor guidance; the parliamentary facts are the vendor's characterizations)
- Monetization posture: free membership to start petitions; **promoted/sponsored petitions** categories in browse. (A, as vendor posture)
- Privacy posture: signer details not used for unsolicited email nor sold; authors must agree to legitimate use. (A, as vendor policy statement)

## Cross-product Comparison

| Dimension | UK Parliament Petitions | ECI | Decidim Initiatives | Citizen Space | GoPetition |
|---|---|---|---|---|---|
| Unit of record | e-petition (call for action) | citizens' initiative | initiative | activity (Consultation/Survey/Form types) | petition |
| Initiator | citizen (British citizen/UK resident) | group of organisers (7 citizens / 7 countries) | citizen or citizen association | institution (consultation operator) | any member |
| Admission gate | 5 supporters → standards check → publish or reject (with reasons) | Commission registration against criteria → registered or refused | technical moderation/validation → approve / reject / suggest amendments | operator publishes (no external admission gate) | membership + author agreement |
| Duplicate control | check for similar petition at creation | — (registration gate instead) | similar-initiative suggestions | — | — |
| Input form | signature | statement of support (paper or online) | signature / endorsement | structured response (survey/form) | signature (custom data fields) |
| Participant eligibility | British citizens / UK residents | EU citizens of voting age (16+ in some countries) | configurable per initiative type | open or registered (site-dependent) | members / signers |
| Bounded window | 6 months open | kick-off ≤6 months after registration; 12 months collection | configurable end date | Forthcoming → Open → Closed by dates | ongoing |
| Threshold semantics | 10,000 → government response; 100,000 → considered for debate | 1 million valid + country thresholds in ≥7 countries → Commission must consider | requisite number per type → administrative procedure starts | none (volume informs analysis) | none formal |
| Verification | identity confirmation at signing (name/email/postcode) | national authorities verify statements and issue certificates | platform authorizations (configurable) | consent question for publishing; moderation/redaction | — |
| Formal handling | government response on petition page; Petitions Committee debate consideration | Commission examination: meeting (1 mo), Parliament hearing (3 mo), formal communication (6 mo) | accepted → administrative procedure starts; institutional answer | analysis → Publish Results / We Asked You Said We Did / response publishing | none in-product ("persuasive effect") |
| Public record | petition page: text, signature count, response, debate outcome | initiative page: registration, collection, Commission response | initiative page: signatures, status, answer | overview page: information, (optionally) published responses, results/outcomes | petition page: text, signatures, updates |
| Paper/physical integration | paper petitions as separate track | paper statement forms + secure file exchange | map of physical signature-collection points | offline responses + supporting documents | — |
| Operator | parliament (institution) | European Commission (institution) | municipality (self-hosted institution) | commercial SaaS operated by institutions | private hosting company |

**Layer B (cross-product commonality) findings.** Across the sampled products, independently and in their own words:

1. A **bounded, publicly visible campaign of record** — petition / initiative / consultation activity — bound to a specific demand or proposal and addressed to the institution or decision-maker responsible (5/5; GoPetition's addressing extends beyond government).
2. **Attributed citizen input accumulating on the campaign** — signatures (petition face) or structured responses/comments (comment face), from participants meeting eligibility or consent rules, accumulating as a visible count (5/5).
3. **An admission gate before the campaign goes live** — standards check (UK), registration (ECI), technical validation (Decidim), operator publishing (Citizen Space); absent only at the open-hosting pole (GoPetition: membership only) (4/5).
4. **A formal handling loop with a published disposition** — government response / Commission communication / administrative procedure start / published results and outcomes (4/5; absent in-product at the open-hosting pole, where handling is external and persuasive).
5. **The campaign record carries the disposition publicly** — responses, debate outcomes, procedure starts, results pages, published individual responses (4/5).
6. **Bounded collection windows** (5/5, values vary).
7. **Eligibility/identity rules on participants** (5/5, depth varies from open to verified).
8. **Duplicate/similarity control** where campaigns are citizen-initiated (2/3 of citizen-initiated products).

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Public-input campaign of record
└── addressed to an institutional decision context
    └── attributed citizen input accumulating on the campaign
        └── institutional handling with a published disposition
```

Three jointly-held properties:

1. **The public-input campaign of record** — a persistent, individually identified, publicly visible campaign (petition, initiative, consultation/comment period) bound to a specific demand or proposal. Remove → an open feedback wall or a social-media post; there is no campaign to sign or comment into.
2. **Addressing to an institutional decision context** — the campaign asks for, or comments on, a specific action by an identified institution or decision-maker responsible for it. Remove → generic petition hosting / advocacy messaging with no decision addressee; the Type's public-sector identity collapses.
3. **Attributed citizen input accumulating, with the disposition recorded back** — signatures or comments from identified/eligibility-gated participants accumulate as a public measure of support or concern, and what the addressed institution did with the input (response, debate, procedure, published outcome) is recorded on the public campaign record. Remove the accumulation → a one-off poll; remove the recorded disposition → a hosting service with no institutional loop (the open-hosting pole keeps the loop external but still tracked as the campaign's purpose).

Jointly-held is load-bearing:

- campaign without addressing → consumer petition host / advocacy campaign territory
- addressing without accumulating attributed input → a published proposal with no participation machinery
- input without campaign-of-record → open comment wall / poll
- input + campaign without disposition → signature counter (the open-hosting pole's minimum; held as the pole where the loop is external)

### L1 — Common Mature Structure

Present in most mature products, not required to define the Type:

- **Admission/moderation gate** before a campaign goes live (standards checks, registration eligibility, technical validation, operator publishing).
- **Threshold semantics** — signature counts that trigger defined handling (response, debate, procedure start); values and consequences vary.
- **Verification of input** — eligibility confirmation, statement verification by authorities, consent gating for publishing.
- **Bounded collection windows** with automatic open/close transitions.
- **Public display of the input measure** — signature/response counts on the campaign page.
- **Formal response published on the campaign page** — government/departmental responses, Commission communications, institutional answers, results/outcomes sections.
- **Duplicate/similarity detection** for citizen-initiated campaigns.
- **Notifications and updates** to campaign creators and followers.
- **Promotion/sharing machinery** — share URLs, QR codes, embeddable calls to action.
- **Offline/paper input integration** — paper statement forms, physical collection points, offline response import.
- **Moderation and redaction of published input** — consent questions, moderation workflows, redaction before publishing individual responses.
- **Analysis tooling** — response analysis, exports, summary reports.
- **Multi-language support** where the jurisdiction requires it.

### L2 — Variant / Optional Structure

- **Operator posture**: institution-operated (parliament, commission, municipality — handling structural) vs commercial SaaS operated by institutions vs open hosting (handling external/persuasive).
- **Initiation**: citizen-initiated (petition face) vs institution-initiated (comment/consultation face).
- **Input form**: signature vs structured response/comment vs statement-of-support form.
- **Threshold consequence**: response-triggering vs debate-triggering vs procedure-starting vs none.
- **Identity depth**: open/anonymous → registered → verified eligibility (citizenship/residency, age, census, document verification).
- **Statutory vs advisory posture**: statutory consultation obligations (e.g. planning consultations' requirement to publish responses) vs advisory engagement.
- **Monetization**: free public service vs subscription SaaS vs freemium with promoted/sponsored petitions.
- **Physical/paper hybrid depth**: paper-only tracks alongside the platform vs integrated paper ingestion.
- **Scope of addressees**: government-only vs any decision-maker (companies, institutions, organizations).

### L3 — Vendor-specific Structure (kept out of the final document)

- UK Parliament: Petitions Committee of 11 MPs; 6-month open window; 5-supporter admission with 21-signer pre-publication cap; rejected-petition visibility; response-by-responsible-department convention.
- ECI: 7-organiser/7-country committee; 2-month (or 4) registration decision; statement-of-support forms; secure file exchange; 1M/7-country thresholds; fixed examination timeline (1/3/6 months); formally adopted communication in all official languages.
- Decidim: initiative types per municipal regulations; promoter committee; answer machinery; similarity suggestions; physical collection-point maps; consultations delegating to external e-voting.
- Citizen Space: activity-type templates (Survey/Consultation/Form/Event registration/Call to Action); "We Asked, You Said, We Did" format; response-publishing consent question; publishable replies; geospatial add-on; private activities; cloning.
- GoPetition: custom signer data fields; promoted/sponsored petition categories; petition-writing editorial guidance.

## Rejected Findings

- **"A petition platform is defined by signature thresholds"** — rejected as definitional: thresholds are the dominant mechanism in government-run products, but the open-hosting pole has none, and the comment face gates handling by analysis rather than counts. The invariant is the *recorded disposition*, not the threshold.
- **"Public comment means the US notice-and-comment docket process"** — rejected as the definition: the sampled consultation face is broader (planning consultations, calls for evidence, public inquiries); the statutory docket machinery belongs to the rulemaking sibling's territory (see Boundary Findings).
- **"The operator must be a government"** — rejected: the open-hosting pole (GoPetition; Change.org as market anchor) is private, and commercial SaaS serves institutions without being one. The Type's identity is carried by the *addressing to institutional decisions*, not by who operates the platform.
- **"Signatures must be legally verified"** — rejected as definitional: verification depth spans none (open hosting) → identity confirmation (UK) → authority verification with certificates (ECI). Verification is a variant posture.
- **"The input must be a signature"** — rejected: the comment face's input is a structured response/comment; the signature is the petition face's realization of "attributed input".
- **"Petitions and public comments are two separate Types"** — not adopted on current evidence: the sampled products share the three-leg core and differ on the initiation/posture axes, which behave as variant axes (who initiates, how input is gated, how handling is triggered). The compound leaf is documented as one Type with two faces; recorded as a taxonomy observation (see Boundary Findings #8).

## Boundary Findings

1. **vs Civic Engagement Platform (§24, processed) — JOINT REVIEW DISCHARGED.** The civic-engagement pass's boundary test holds from this side: this Type's primary and only object is the input campaign (petition or comment period) with its formal handling; the Civic Engagement Platform composes many participation mechanisms inside engagement spaces. Decidim is the straddling evidence, examined from both sides: its Initiatives space is petition-shaped (signatures, committee, accept/reject, procedure start — this Type's shape) but exists as one space-type inside a composed platform with processes, assemblies, proposals, budgets — so Decidim is a Civic Engagement Platform whose Initiatives component realizes this Type's shape. Conversely, UK Parliament Petitions, the ECI, and Citizen Space hold the campaign as the primary and only object → this Type. Keep-both ratified; the seam is "campaign-as-the-only-object vs campaign-as-one-mechanism-inside-composed-spaces".

2. **vs Rulemaking & Public Consultation Platform (§24 sibling, unprocessed) — FLAG FOR JOINT REVIEW.** Seam: this leaf covers the citizen-facing input campaign — petitions and public comment periods as participation surfaces; the rulemaking leaf's territory is the agency-side statutory machinery — docket management, comment aggregation/analysis obligations, disposition synthesis inside a rulemaking procedure. Regulations.gov (the US eRulemaking public portal) is this leaf's public-comment face; the docket machinery behind it belongs to the sibling. Evidence for the seam is moderate this pass (Regulations.gov unreachable; the seam is drawn from the civic-engagement pass's framing plus the Citizen Space statutory-consultation posture). Flag recorded for the sibling's pass.

3. **vs 311 / Citizen Service Request Platform (§24 sibling, unprocessed).** 311's unit is an individual service request with an operational case lifecycle (report → assign → resolve); this Type's unit is collective input on a decision with formal handling — no dispatch/repair case semantics. Confirms the civic-engagement pass's seam from this side.

4. **vs Advocacy Platform (§25, unprocessed) — moderate strength.** Advocacy platforms orchestrate multi-channel campaigns (email/call campaigns, supporter journeys) for organizations; this Type centers the single input campaign of record with institutional addressing and a recorded disposition. The consumer petition hosts (GoPetition; Change.org as market anchor) sit closest to this seam — their petitions are addressed to decision-makers but the platform's role is hosting and promotion, with handling external and persuasive. Change.org unreachable this pass; the seam is recorded at moderate strength and flagged for the advocacy pass.

5. **vs Survey Platform (§03.11, processed).** The comment face's input mechanism is often survey-shaped (Citizen Space's survey activities with skip logic and analysis), but the container is the public campaign of record with institutional addressing and a published disposition; a survey platform's instrument is a private research/measurement tool with no campaign addressee. The survey is the mechanism; the campaign is the Type.

6. **vs Online Donation Platform / Nonprofit Crowdfunding (§25).** Petitions may carry donation asks and consumer hosts monetize around campaigns, but the input of record is signatures/comments, not money; no sampled product's core is a money loop. Moderate strength (monetization observed only at the open-hosting pole).

7. **vs Government Meeting / Agenda Management (§24).** "Public comment" in the meeting sense (speaking at hearings, commenting on agenda items) is meeting-centric; this Type is campaign-centric with a bounded collection window and a recorded disposition. Not directly sampled; recorded as adjacent.

8. **Taxonomy observation — compound leaf.** The directory leaf combines "Petition" and "Public Comment" in one name. The sampled market realizes one shared core (campaign of record + attributed input + recorded disposition) with two initiation/posture poles (citizen-initiated signature campaigns; institution-initiated comment periods). This pass documents the leaf as one Type with two faces and records the observation for a taxonomy pass; no directory change made from this side.

9. **"去掉什么就变成另一个 Type" 判据**:
   - remove the institutional addressing / decision context → generic petition hosting / advocacy messaging territory
   - remove attributed accumulating input → open feedback wall / one-off poll
   - remove the single campaign of record (compose many mechanisms in spaces) → Civic Engagement Platform
   - make the input an operational service case → 311 / Citizen Service Request Platform
   - make the handling a statutory docket with comment-analysis machinery → Rulemaking & Public Consultation Platform
   - remove public visibility of the campaign and its disposition → private survey/feedback collection
   - make the input money → donation/crowdfunding territory

## Historical / Market-Sample Check

- **Paper petitions presented to Parliament** (13th-century England lineage, as characterized by GoPetition's own guidance): a written petition document + signature collection + presentation to the house + recorded handling in the journal — satisfies all three L0 legs at analog level (campaign of record, addressing, attributed input with recorded disposition).
- **Written-objection procedures** (e.g. planning consultations on paper): published proposal + written objections from identified parties + officer report responding to objections — satisfies the comment face's legs.
- **Parliamentary e-petition lineage** (Scottish e-Petitioner as the pioneering parliamentary service; UK E-petitions; Queensland e-petitions under Standing Orders; White House We the People; European Parliament petitions under Article 227 TFEU — all as characterized in GoPetition's guidance): same core, different jurisdictions and threshold regimes.
- The definition names no threshold values, no verification regimes, no web forms, no digital-only machinery — all era/jurisdiction machinery is held at L1/L2. The historical check passes.

## Uncertainties

- **Change.org unreachable** (help and about both timed out twice). The largest consumer petition platform is held as a market anchor only; no operational details asserted. The open-hosting pole's characterization rests on GoPetition (Tier-2/3).
- **Regulations.gov unreachable** (403 twice on /about and /help). The US federal public-comment portal is held as a market anchor only; docket/comment mechanics not asserted; the rulemaking seam is drawn at moderate strength.
- **GoPetition evidence is Tier-2/3** (official editorial/guidance content, not operational help-center docs); consumer-host pole claims are held at moderate strength and marked as vendor guidance where appropriate.
- **Whether petition and public comment are one Type or two** is a taxonomy judgment recorded as an observation, not resolved unilaterally (see Boundary Findings #8).
- Decidim documentation reflects the `develop` branch; feature naming may differ across versions.
- Meeting-centric public comment (hearings, agenda-item comment) was not sampled; its adjacency is recorded without product claims.

## Final Synthesis

A Petition / Public Comment Platform is the public-input channel of institutional decision-making. Its unit of record is a bounded, publicly visible **input campaign** — a petition demanding action, or a comment period on a proposal — addressed to the institution or decision-maker responsible. Citizens contribute **attributed input** — signatures on the petition face, structured responses/comments on the comment face — that accumulates as a public measure of support or concern under eligibility and consent rules. The input is **handled under defined rules** — admission checks, thresholds or verification, committee consideration or analysis — and the **disposition is recorded back on the public campaign record**: a government response, a debate, the start of an administrative procedure, published results and outcomes, or published individual responses.

The market realizes one Type in five poles: parliament-run petition services (UK Parliament), supranational initiative instruments with authority verification (ECI), municipal open-source initiative spaces (Decidim Initiatives), commercial consultation platforms operated by institutions (Citizen Space), and open petition hosting with persuasive rather than formal standing (GoPetition; Change.org as unreachable market anchor). The two faces of the leaf name — petition and public comment — share the three-leg core and differ on the initiation and handling-trigger axes, which behave as variant axes. The Type ends where engagement becomes composed multi-mechanism spaces (Civic Engagement Platform), where input becomes operational service cases (311), where handling becomes statutory docket machinery (Rulemaking & Public Consultation Platform), where campaigns become multi-channel orchestration (Advocacy Platform), and where the instrument becomes a private measurement tool (Survey Platform).
