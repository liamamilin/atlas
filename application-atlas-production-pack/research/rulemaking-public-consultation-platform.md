# Research Notes — Rulemaking & Public Consultation Platform

Research date: 2026-09-09
Methodology: WORKFLOW v1.1 / WRITING_GUIDE v1.1 (internal reference only — not part of the final document)

## Research Goal

Understand what a Rulemaking & Public Consultation Platform actually is as an Application Type: what the system of record is, who operates it, what the public sees, how a consultation/rulemaking procedure moves from drafting to disposition, and where the boundary lies against the sibling leaves already processed in §24 (petition-public-comment-platform, civic-engagement-platform, legislative-tracking-platform, 311-citizen-service-request-platform).

This pass carries a **joint-review obligation**: petition-public-comment-platform (processed 2026-09-09) flagged a seam — "citizen-facing input campaign (petitions + public comment periods as participation surfaces) vs agency-side statutory docket machinery (docket management, comment aggregation/analysis obligations, disposition synthesis inside a rulemaking procedure); Regulations.gov is this leaf's public-comment face and the docket machinery behind it belongs to the sibling — joint review expected on that side." civic-engagement-platform (processed) flagged: "rulemaking: statutory docket comment vs project-based advisory engagement." Both must be discharged from this side.

## Initial Boundary (hypothesis before research)

- Core use: an institution (agency, department, local authority, planning body) runs a formal procedure — a rulemaking filing or a public consultation — in which it publishes a proposal/draft, collects public input during a bounded window, analyzes the input, and records/publishes a disposition.
- Primary users: institution staff (policy/consultation officers, rulewriters, planners, analysts); secondary: the consulted public.
- Nearest neighbors: petition-public-comment-platform (public input campaigns), civic-engagement-platform (composed engagement spaces), survey-platform (measurement instruments), legislative-tracking-platform (external watching of lawmaking), Government Meeting/Agenda Management (hearing comment), FOI/Public Records Request (records access), Regulatory Change Management (the watched corporate side).
- Unknowns: whether the leaf is really "agency-side docket machinery" (as the petition pass assumed) or the broader institution-side consultation machinery; whether the analysis tooling is definitional; how the statutory (US notice-and-comment) pole relates to the international consultation-SaaS pole.

## Research Questions

1. What is the unit of record in each product (docket? filing? consultation? activity? project? document)?
2. What does the institution publish (draft rule text, policy document, questions, supporting materials, notices)?
3. How is public input collected (question forms, comment submission, document annotation, meetings, imported offline input)?
4. What machinery exists for processing input (tagging, categorization, quantitative/qualitative analysis, AI analysis, moderation, response publishing)?
5. How is the disposition produced, recorded, and published (results report, "We Asked, You Said, We Did", response to comments, final rule / effective date / codification)?
6. What is the lifecycle of the procedure (states, date-driven transitions, statutory stages)?
7. Who are the users on each side (institution roles vs public), and what interfaces does each face?
8. What rules matter (comment windows, attribution/consent, moderation, statutory notice/comment minimums, records retention)?
9. How do products differ across jurisdictions and postures (statutory rulemaking vs advisory consultation; US vs UK/EU/AU vs local)?
10. Where exactly is the seam vs petition-public-comment-platform and civic-engagement-platform?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers/jurisdictions:

1. **Delib Citizen Space** — consultation & engagement SaaS (UK-origin, international; central government departments, local authorities, agencies). Philosophy: end-to-end consultation management (publish → collect → analyze → report back). Strong official documentation (Delib Knowledge Base).
2. **Granicus EngagementHQ** (now marketed "Sentiment & Feedback") — engagement/consultation platform (AU-origin, global local government). Philosophy: engagement-hub with omnichannel tools across the IAP2 participation spectrum + AI analysis. Official product documentation.
3. **Konveio** — document-centric engagement platform for plans & policies (US local government, state agencies, planning consultants, universities). Philosophy: the draft document is the object; comments attach in context; AI analysis; plan library through implementation. Official product site.
4. **Utah eRules + Administrative Rules Register** (Utah Office of Administrative Rules) — a real government-operated statutory rulemaking system (US state). Philosophy: the rule filing as the legal unit of record; agency-side filing workflow + public portal + statutory docket (Register). Official help documentation.
5. **Regulations.gov / US federal eRulemaking (FDMS)** — the canonical federal notice-and-comment system; **unreachable** (HTTP 403 ×3 across two research passes: 2026-09-09 this pass; also unreachable in the petition pass). Held as a market anchor only; no operational claims filled from memory.

Also checked and classified as **adjacent, not in-sample**: Zencity (community sentiment/insights analytics — Listen/Ask/Communicate; no consultation procedure of record → civic-engagement/sentiment territory). **PublicInput** (transportation/NEPA public involvement) — unreachable (403 ×2), noted as a likely hearing/comment-management pole, unverified.

## Sources

Layer A (directly observed, official):

- Delib — Citizen Space product page: https://www.delib.net/citizen_space (fetched 2026-09-09)
- Delib Knowledge Base: https://help.delib.net/ — structure; articles: "Activity types" (/article/171), "The status of your activity — Open, Closed and Forthcoming" (/article/345), "Publishing results and outcomes" (/article/308), "Response publishing — what is it?" (/article/103); categories "Creating and managing activities" (/category/25), "Analysis and reporting back" (/category/71), "Response publishing" (/category/76) (fetched 2026-09-09)
- Granicus — Sentiment & Feedback (EngagementHQ) product page: https://granicus.com/product/sentiment-feedback-engagementhq/ ; product directory: https://granicus.com/products/ (fetched 2026-09-09)
- Konveio — product site: https://konveio.com/ (fetched 2026-09-09)
- Utah Office of Administrative Rules — "eRules Help" (https://rules.utah.gov/help/agency-resources/erules-faqs/), "Rulemaking Process – The Basics" (https://rules.utah.gov/help/rulemaking-process-the-basics/), "Participate in Rulemaking" (https://rules.utah.gov/help/participate-in-rulemaking/) (fetched 2026-09-09)

Unreachable / limitations:

- Regulations.gov: https://www.regulations.gov/about → 403 (this pass); previously 403 ×2 in the petition-public-comment-platform pass. Abandoned per network rules. The federal docket model's operational machinery is NOT verified; the docket concept is instead evidenced via Utah's statutorily defined "docket of rule filings" (Administrative Rules Register, 63G-3-402).
- PublicInput: https://www.publicinput.com/ → 403 ×2; https://help.publicinput.com/ → transport error. Abandoned.
- EU "Have Your Say" portal: JS-rendered, empty fetch. Not usable.
- Granicus EngagementHQ legacy URL (bangthetable.com): transport error; granicus.com/solution/engagementhq/ → 404; correct URL found via product directory.

## Product Observations

### Delib Citizen Space (Layer A unless noted)

Positioning: "a consultation and engagement platform that transforms how governments connect with citizens… From high-profile national conversations to neighbourhood issues." "End-to-end consultation and engagement: everything you need from publishing information to asking questions and analysing responses with access to our data API and AI enhanced analysis." Use cases: "Statutory consultation & research — policy development, legislation research, calls for evidence"; "Community engagement"; "Govtech processes — permitting and licensing." Customers: UK central departments (Defra, DfE, DESNZ), local authorities (Edinburgh), NZ Ministry of Health, Police Scotland, Australian Government.

Key observations:

- **The activity is the unit of record.** Staff create "activities" (with an owner, a URL, a theme, clone support, private/public visibility). Core activity types: Survey, **Consultation**, Form, Event registration, Call to Action page. The Consultation type is "designed for running formal consultation activities, with a custom timeline feature… for projects or processes that have defined phases or key milestones. The timeline functionality helps participants clearly follow progress and understand where they are in the consultation journey." Activity templates exist "for things like statutory consultation, permits and licensing."
- **Activity lifecycle is date-driven**: Forthcoming (open date in future; auto-opens at midnight on start date) → Open (accepting responses; auto-closes at 23:59 on close date) → Closed (call-to-action replaced by "What Happens Next" or "We Asked, You Said, We Did" information). Editing a published/open activity carries warnings.
- **The activity page holds the proposal**: overview page with introductory text, related documents and links, embedded content, call-to-action box; question pages (surveys with skip logic); geospatial option.
- **Analysis machinery in-product** (category "Analysis and reporting back", 42 articles): view responses, **tagging** ("What is tagging?", "How to tag responses"), filtering/grouping, responses organised by question or by respondent, **analyst/"hidden" questions** (questions not shown to respondents, used by analysts), postcode normalisation, removing responses, PDF summary report generation. Product page: "Powerful tagging and analysis tools"; AI "First Pass Analysis" to "speed up the analysis process" (tier-dependent).
- **Response publishing** (separate feature, site-enabled): "publish submissions from respondents… responses can be anonymous or published with identifying information if consent is given"; a **consent question** secures permission; analysts can add **publishable replies** to individual published responses; qualitative answers must be **moderated and redacted** before publishing; can publish while open or after close. Rationale given by the vendor: transparency; and "Some activities, such as planning consultations, have a statutory requirement to publish the submitted responses."
- **Disposition published back on the activity** ("Feedback and results" menu): (1) **Publish Results** — file (doc/PDF), URL, and/or text findings; a PDF summary report of responses can be generated in-product and uploaded; (2) **"We Asked, You Said, We Did"** — three text boxes (what was asked / what you said / what we did); auto-displays at the top of the overview page once the activity is closed; site-wide "We Asked, You Said, We Did" tab aggregates outcomes across activities. Both optional; "best practice to feed back results to your respondents" — the vendor calls this "closing the loop."
- **Portfolio management**: dashboards per activity (total responses, responses published, open/close dates, responses over time, analysis block, downloads/exports); site-wide exports ("Download this list of activities" with Publish Results / We Asked You Said We Did columns to audit closure across the portfolio); configurable landing pages; multiple hubs for departments/regions/brands (product page).
- Compliance posture: ISO 27001, GDPR, WCAG 2.2 AA (product page).

### Granicus EngagementHQ / "Sentiment & Feedback" (Layer A)

Positioning (Granicus product directory): "Sentiment & Feedback (EngagementHQ) — Unlock the value of community input at scale and understand what matters and why." Product page: "helps governments ask the right questions, listen to answers, and respond with intent." Use cases: performance management, participatory agenda-setting, **policy and program development**, infrastructure planning and delivery, budgeting, crisis management.

Key observations:

- **Engagement projects/hubs as containers**: organizations "can even create more than one engagement hub catering to different departments, regions, or brands." Participant activity and information live in a "centralized workspace."
- **Omnichannel input tools**: "propose ideas, vote, ask questions, put feedback on a map, submit surveys, allocate budget and comment on priorities" — engagement across "the entire IAP2 public participation spectrum"; participant registration customizable; web/mobile/email/social.
- **Moderation**: "human-eye and AI moderation… enforcing community guidelines… 24/7 in Spanish, English, Welsh, and French languages for all public discussions."
- **Analysis and report-back**: "Measure and track sentiment and **report back on key themes**"; "Categorize responses with AI-powered text and sentiment analysis"; pre-built dashboards per tool; "Aware, Informed, and Engaged" (AIE) framework; share dashboards/reports with stakeholders.
- Straddle note: EngagementHQ also carries ideas/voting/participatory-budgeting tools — composed engagement spaces (civic-engagement-platform territory) alongside consultation machinery. Granicus bundles both in one product; the bundle is vendor packaging, not type identity.

### Konveio (Layer A)

Positioning: "Engagement Platform for Plans & Policies… the Planner's engagement platform, designed to simplify how communities engage with stakeholders throughout the full plan lifecycle." Two hubs: **Engagement Hub** ("Collect stakeholder input, from early-stage workshops to draft reviews") and **Plan Hub** ("Publish Engaging Plans as an AI-Connected Framework" / Plan Library for adopted plans).

Key observations:

- **The draft document is the object**: "Context-specific Feedback — collect productive, informed comments, directly on your materials" (in-context annotation on uploaded existing documents: "All based on existing materials — no need to change how you work!"). Popular uses: Draft Reviews, Design Reviews (30/60/90% designs), Interactive Plan Viewer, Hybrid Open Houses (upload open-house materials/poster boards), Stakeholder Workspaces, Development Reviews.
- **Multi-source input consolidation**: "AI Transcribe and Import — import comments from events, letters, emails or other sources, then analyze everything in one place."
- **Analysis machinery**: "Extract insights quickly with AI analysis tools… design the ideal comment reporting workflows"; "Export your data to CSV or download annotated PDF reports"; AI-assisted analysis highlighted as new.
- **Disposition / close the loop**: "Track Implementation — seamlessly post amendments, new versions or updates and provide continuous progress reports to close the loop and build trust."
- Privacy/visibility settings ("Smart privacy, visibility, and participation settings"), WCAG compliance, translations (ES/FR/DE + Google Translate), ArcGIS integrations.
- Customers: cities (Denver, Austin, Sacramento, Lacey WA), state agencies, US Fish & Wildlife Service, counties, planning consultants (Kimley-Horn), universities. Staff quote: "straightforward for our staff to collate and respond to the feedback we received."

### Utah eRules + Administrative Rules Register (Layer A)

Positioning: "eRules is the official rule filing service used by agencies to submit rule filings to the Office of Administrative Rules. It also hosts the Utah Administrative Code on the Public Portal, allowing the public to search, browse, view, and download Utah's administrative rules."

Key observations:

- **The rule filing is the legal unit of record**: agency staff (UtahID-gated) work in a "Work Queue" and file typed filings: Proposed Rule, Change in Proposed Rule (CPR), Emergency Rule, Nonsubstantive Change, Five-Year Review, Five-Year Extension, Notice of Effective Date. Each filing gets a five-digit file number assigned by the Office; "View Rule Filing History" — the filing persists with its history.
- **Statutory docket**: the Administrative Rules Register is, per statute (63G-3-402(1)), a "docket of rule filings arranged chronologically" in which the Office records "the receipt of all agency rules, rule analysis forms, and notices of effective dates" and makes it "available for public inspection."
- **Statutory lifecycle** (Rulemaking Process – The Basics): pre-proposal → public notice (publication in the Utah State Bulletin; direct notice to affected/requesting parties) → procedural review (Office → Governor's Office content review → GMB fiscal review → final review) → **public comment period** (minimum 30 days for proposed rules; public hearings optional/mandated with request thresholds) → **7-day review period in which "an agency will review any comments that they received"** → notice of effective date (bounded window after publication) → codification into the Administrative Code.
- **Public side**: Public Portal (search/browse/view/download rules), Bulletin/Digest publications (comment start/end dates, contact info, fiscal impacts, rule text per filing), "Participate in Rulemaking" guidance.
- **Comment collection is channel-plural, not form-bound**: "Some public comments are made at public meetings, others contain one-sentence or one-paragraph comments, while others contain thousands of pages with detailed analysis, with supporting documents submitted as attachments." Comment guidance: "The comment process is not a vote — one well supported comment is often more influential than a thousand form letters."
- Note: in this statutory pole, the in-platform analysis tooling is minimal/absent — the comment review happens in the agency's own process; the system holds the record, the window, and the disposition trail (effective date, codification). This is important calibration for the L0/L1 split.

### Regulations.gov / US federal eRulemaking (NOT observed — anchor only)

Unreachable (403 ×3 across passes). Known market position: the federal portal for dockets, notices, and public comments on US federal rulemaking (the public face of the eRulemaking program's FDMS). **No operational claims are made from memory.** The petition-public-comment-platform pass independently recorded it as "this leaf's public-comment face," with the docket machinery behind it attributed to this leaf — that attribution is treated as a hypothesis to check, not evidence.

## Cross-product Comparison

| Dimension | Citizen Space | EngagementHQ | Konveio | Utah eRules/Register |
|---|---|---|---|---|
| Unit of record | Activity (Consultation/Survey/Form types) with owner, URL, dates, status | Engagement project inside (possibly multiple) engagement hubs | Draft/adopted document inside a project; Plan Library across projects | Rule filing (typed) with file number + filing history; statutory Register (docket) |
| Published proposal | Overview page: intro text, related documents/links, embedded content, call-to-action | Project pages with engagement tools | The document itself (annotated, interactive, translated) | Bulletin/Digest notice: rule text, fiscal impact, comment dates, agency contact |
| Input channel | Question pages/surveys (skip logic), geospatial responses | Surveys, ideas, votes, questions, map pins, budget allocation, priorities | In-context document annotation; imported events/letters/emails | Comments via meetings/email/attachments (channel-plural; not form-bound) |
| Bounded window | Date-driven Forthcoming→Open→Closed, automatic | Project phases (IAP2 spectrum) | Review phases (draft reviews, 30/60/90% designs) | Statutory comment period (min 30 days) + review period |
| Attribution/identity | Anonymous or identified; consent question for publishing | Participant registration/profiles, customizable | Privacy/visibility/participation settings | Attribution per channel; public record |
| Analysis machinery | Tagging, filtering/grouping, analyst (hidden) questions, exports, PDF report, AI First Pass Analysis | AI text/sentiment analysis, dashboards, AIE framework | AI analysis, CSV export, annotated PDF reports | Minimal in-platform; agency reviews comments in its own process (7-day review period) |
| Moderation/response publishing | Moderate + redact; publish individual responses (consent-gated); publishable replies | Human + AI moderation of discussions | Visibility settings | Comments part of the public record (Register/inspection) |
| Disposition on the record | Publish Results (file/URL/text) + "We Asked, You Said, We Did"; site-wide outcomes tab | "Report back on key themes"; shared dashboards/reports | Progress reports, amendments/new versions posted to close the loop | Notice of effective date; codification into the Code; filing history |
| Posture | Statutory + advisory consultations, research, permits/licensing | Policy/program development, planning, budgeting, agenda-setting | Plan/policy lifecycle (draft review → adoption → implementation) | Statutory rulemaking only (binding rules) |
| Operator | Government SaaS (institution staff) | Government SaaS (institution staff) | SaaS for governments/consultants/agencies | Government-operated system (state) |

Cross-product commonalities (Layer B): every sampled product (1) holds a persistent identified container for the procedure bound to one proposal; (2) publishes the proposal with supporting materials; (3) operates a bounded input window with a structured channel; (4) retains attributed input on the record; (5) records/publishes the institution's disposition back on the record. Analysis tooling is present in the three commercial products but absent (in-platform) in the statutory filing system — so analysis tooling is common-mature, not definitional. Date-driven window automation, consent-gated response publishing, AI analysis, moderation, registration, geospatial, multi-hub — all vary by product/tier.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The consultation/rulemaking procedure as the institution's unit of record** — a persistent, individually identified container (consultation, engagement project, draft-document review, rulemaking filing/docket) bound to one specific proposal or draft instrument, holding the procedural materials (draft text, supporting documents, notices) and carrying the institution's lifecycle. Remove → a campaign host (petition territory) or a document library / records archive.
2. **The institution-operated public input window against the published proposal** — the institution publishes the proposal and operates a structured input channel (question form, comment submission, in-context document annotation, meeting/imported input) during a bounded, date-driven window; input is attributed and retained on the procedure's record. Remove → an internal workflow/records system (no public consultation), or an always-open feedback wall (no procedure).
3. **The disposition recorded back on the record** — the institution's handling of the input (review, analysis, response, decision) is recorded on the procedure and the outcome (results report, "we asked / you said / we did", response to comments, final rule / effective date / codification) is published back on the record, closing the procedure. Remove → a submission collector/inbox; the consultation loop never closes.

Jointly-held load-bearing tests:

- 1 alone = document/records library
- 2 without 1 = public comment form / petition host (petition-public-comment-platform territory)
- 3 without 1+2 = analysis over nothing
- 1+2 without 3 = submission collector; the procedure never closes in the system
- 1+3 without 2 = internal procedure tracker — not "public consultation"
- 2+3 without 1 = free-floating campaigns (petition-leaf posture)

### L1 — Common Mature Structure

- Structured question forms/surveys (question types, skip logic) and/or comment submission and/or in-context document annotation
- Analysis tooling: tagging/categorization, filtering/grouping, quantitative + qualitative views, exports, summary reports; increasingly AI-assisted (first-pass analysis, text/sentiment analysis, transcription/import of offline input)
- Response publishing: moderated, redacted, consent-gated publication of individual submissions
- Moderation (human and/or AI) of public discussions
- Participant registration/profiles and privacy settings
- Communications with respondents (confirmations, notifications)
- Consultation archives / libraries; portfolio dashboards across activities
- Timelines/milestones for multi-phase procedures
- Accessibility (WCAG-class) and multi-language support
- Geospatial/place-based input (maps)

### L2 — Variant / Optional Structure

- Posture: statutory rulemaking (binding instruments, mandated notice/comment windows, review chains, codification) vs advisory/policy consultation ("what we heard" reports) vs planning/permitting consultations (statutory publication duties) vs internal/stakeholder reviews (private activities)
- Container shape: docket/filing-centric (US statutory), project/consultation-centric (SaaS), document-centric (annotation)
- Jurisdiction machinery: gazette/bulletin publication, typed filings (proposed rule, change in proposed rule, emergency rule, periodic review, effective-date notice), hearing triggers, multi-body review, codification — US-state/federal specific; UK "We Asked, You Said, We Did" convention; EU/other national portal patterns (unverified this pass)
- Hearing/meeting integration (public meetings as comment venues; hybrid open houses)
- Deployment: multi-tenant SaaS vs government-operated custom systems
- Adjacent suite bundling: geospatial modules, budget simulators, ideas/voting spaces (engagement-platform territory), CMS/communications integration

### L3 — Vendor-specific (Research Notes only)

- Delib: activity types taxonomy; "We Asked, You Said, We Did" branding; First Pass Analysis; publishable replies; Participation Plus+ (Easy Read/speech-to-text); 247%/396% marketing claims.
- Granicus: "Sentiment & Feedback" renaming; AIE ("Aware, Informed, Engaged") framework; IAP2-spectrum framing; govCommunity; regional hosting.
- Konveio: Plan Hub / Engagement Hub split; Plan Library; ArcGIS integrations; 30/60/90% design reviews; MURP partnerships.
- Utah: eRules name; UtahID gating; five-digit file numbers; Bulletin/Digest/Register publication triad; 63G-3 statutory citations; specific day counts (30-day comment minimum, 7-day review, 120-day effective-date window).

## Rejected Findings (anti-overfit)

- **In-platform analysis tooling is NOT definitional.** All three commercial products have it, but the statutory filing system (Utah eRules) holds the record, window, and disposition trail without in-platform analysis — the agency reviews comments in its own process. The invariant is the recorded disposition, not the tooling. (Shared-implementation rule: 3/4 co-occurrence ≠ invariant.)
- **Response publishing (publishing individual submissions) is NOT definitional** — site-enabled, tier-dependent feature at Citizen Space; absent in the statutory pole's system mechanics.
- **AI analysis is era-current, NOT definitional** (Citizen Space tier-gated; Konveio "NEW"; EngagementHQ marketing-led).
- **"We Asked, You Said, We Did" is a UK-origin convention, NOT definitional** — the invariant is the published disposition, whose form varies (results report, response-to-comments, final rule).
- **Registration/profiles NOT definitional** (statutory comments accepted via email/meetings without platform accounts).
- **Geospatial, budget tools, ideas/voting NOT definitional** (adjacent suite capabilities; EngagementHQ's breadth is vendor packaging).
- **Statutory machinery (filing types, notice minimums, codification) NOT definitional** — jurisdiction variant; advisory consultations without any of it are still in-type.
- **Document-annotation as the input mode NOT definitional** — one pole (Konveio); form-based poles exist.

## Historical / Market-Sample Check

Paper-era and analog consultations satisfy the L0 without any modern machinery: an agency publishes a proposal in the gazette (notice), receives written submissions during a stated comment window (bounded input window against the published proposal), and issues a consultation response / final rule recorded in the register (disposition on the record). The US statutory docket itself predates the web (Federal Register Act 1935; APA notice-and-comment 1946); Utah's Register is statutorily a "docket of rule filings" available for public inspection. Regional variants (UK policy consultations with "We Asked, You Said, We Did", AU/NZ engagement hubs, US state eRulemaking) all fit. The definition therefore holds at the procedure level and does not depend on online forms, AI, response publishing, or registration. Historical check: **passed**.

## Boundary Findings

### vs petition-public-comment-platform (JOINT REVIEW — discharged from this side)

The petition pass's core: the public-input campaign of record (petition or comment period) + addressing to an institutional decision context + attributed input accumulating with the disposition recorded back. Its flag: "citizen-facing input campaign vs agency-side statutory docket machinery… Regulations.gov is this leaf's public-comment face and the docket machinery behind it belongs to the sibling."

**Ruling: keep-both RATIFIED**, with the seam drawn at the **unit of record and the system's center of gravity**:

- Petition leaf: the **campaign is the only object** — the platform is the participation venue; the campaign's own window + disposition is the whole system; no draft-instrument management, no analysis machinery, no procedure lifecycle beyond the campaign.
- This leaf: the **procedure is the container** — the platform is the institution's system of record for running the procedure end-to-end: the draft instrument and supporting materials, the managed input window as one phase, the analysis machinery, the disposition synthesis, and the lifecycle through finalization/archival. The open window has a before (drafting, notice) and an after (analysis, response, finalization) that the system also holds.

Overlap acknowledged honestly: an institution-initiated comment period satisfies both cores at the campaign level. The discriminator is what the system is for the institution: venue for a campaign vs system of record for a procedure. **Straddler documented**: Delib Citizen Space was classified by the petition pass under the petition leaf ("commercial consultation SaaS… holds the campaign as the primary and only object"). From this side, fresh Layer-A evidence (42-article "Analysis and reporting back" category; consent-gated moderated response publishing; Publish Results + "We Asked, You Said, We Did" outcomes publishing; activity owners/cloning/portfolio exports; statutory-consultation templates) shows Citizen Space operating as institution-side consultation machinery — the procedure container with its before/after — not a bare campaign venue. Recorded as a boundary issue for the taxonomy owner; no directory change made.

### vs civic-engagement-platform

Civic engagement platforms are composed spaces for ongoing community engagement (proposals, debates, participatory budgeting, assemblies, surveys as one mechanism among many). This leaf is the formal consultation/rulemaking procedure machinery. **Straddler documented**: EngagementHQ bundles both (consultation projects with report-back AND ideas/voting/budget spaces); Granicus ships them as one product — vendor bundling, not type identity. Zencity (checked) is sentiment/insights analytics — outside this leaf entirely.

### vs legislative-tracking-platform

The tracker is the external watcher's mirror of lawmaking (bills/regulations as data to watch; the watcher neither authors nor advances). This leaf is the institution's own procedure machinery — the record the institution operates. Complementary, opposite stances; the tracker treats rulemaking as an adjacent data class, this leaf treats it as the managed procedure.

### vs survey-platform

The consultation container (procedure with draft instrument, institutional decision context, disposition) vs the private measurement instrument (respondent sample, question battery, analytics). A consultation may contain a survey-shaped form; the survey platform's world contains no procedure of record. Seam held consistent with the petition pass.

### vs Government Meeting / Agenda Management

Hearing/meeting comment capture is meeting-centric (the agenda/meeting is the record); this leaf is procedure-centric (the consultation/filing is the record; meetings are one input venue). PublicInput (unreachable) appears to bundle both for transportation agencies — noted, unverified.

### vs FOI / Public Records Request Platform

Opposite direction of information flow: the public requests records the institution holds vs the institution collects input from the public. Both produce public records; different objects.

### vs Regulatory Change Management / corporate compliance

The watched side (organizations tracking regulatory obligations) vs the rulemaking side (the institution producing the rules). No shared core.

### vs Government Transparency Portal

Publication of institutional records for inspection vs running the consultation procedure. A transparency portal may publish outcomes; it does not operate the input window or the procedure.

## Uncertainties

1. **Regulations.gov/FDMS operational machinery unverified** (403 ×3). The federal docket model (docket folders, comment aggregation UI, agency-side comment analysis) is asserted nowhere in this pass; the docket concept is evidenced via Utah's statutorily defined Register. If a future pass reaches Regulations.gov, the statutory-pole description should be revisited.
2. **PublicInput unverified** (403 ×2) — the transportation/NEPA comment-management pole (multi-channel comment capture, hearing management, comment matrices) is presumed from market position only and was not sampled.
3. **EU "Have Your Say" / EUSurvey machinery unverified** (JS-rendered empty fetch) — the supranational consultation portal pole is an anchor only.
4. **Whether any commercial product implements the US-federal-style docket** (docket folders with FR notices + bulk comment management) could not be confirmed; the sampled commercial products are project/document-centric.
5. **Citizen Space's classification** (petition leaf vs this leaf) is a genuine straddle; this pass documents the evidence from its side and leaves the consolidation/split decision to the taxonomy owner.
6. EngagementHQ's consultation-specific mechanics (project lifecycle states, response publishing) were observed only at product-page depth; its support KB was not reachable this pass.

## Final Synthesis

A Rulemaking & Public Consultation Platform is the **institution-side system of record for formal public consultation and rulemaking procedures**. Its world has three load-bearing structures held jointly: (1) the procedure as a persistent identified container bound to one proposal/draft instrument, holding the procedural materials and carrying the institution's lifecycle; (2) the institution-operated public input window against the published proposal — bounded, date-driven, structured, with input attributed and retained on the record; (3) the disposition recorded back on the record — the institution's handling of the input (review, analysis, response, decision) recorded on the procedure and the outcome published back on it, closing the procedure. Around this core, mature products add analysis tooling (tagging, filtering, AI-assisted first-pass analysis), response publishing (moderated, consent-gated), moderation, registration, notifications, archives, timelines, accessibility, and geospatial input. The market realizes the type across postures (statutory rulemaking ↔ advisory consultation) and container shapes (docket/filing ↔ consultation project ↔ draft document), with jurisdiction-specific statutory machinery as variant, not core. The type's identity survives the historical check at analog level (gazette notice + written submissions + consultation response + register). The seam vs petition-public-comment-platform holds at campaign-as-only-object vs procedure-as-container; the seam vs civic-engagement-platform holds at formal procedure vs composed engagement space; straddlers (Citizen Space, EngagementHQ) are documented from this side.
