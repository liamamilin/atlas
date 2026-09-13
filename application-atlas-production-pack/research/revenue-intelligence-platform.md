# Research Notes — Revenue Intelligence Platform

Research date: 2026-09-07
Slug: revenue-intelligence-platform
Directory location: §07 Sales, Customer & Revenue

---

## Research Goal

Understand what a Revenue Intelligence Platform actually is as an application structure: what data it assembles, what objects exist inside it, what its users do, how the forecast and pipeline-inspection workflows run, what rules govern it, and where it begins and ends against neighboring Types (CRM, Sales Forecasting Platform, Conversation Intelligence Platform, Sales Pipeline Management, Sales Performance Management, BI).

---

## Initial Boundary (hypothesis before research)

- Hypothesis: a B2B sales-side application that sits on top of the CRM, assembles a continuously updated model of in-flight revenue (CRM deals + automatically captured selling activity), and derives inspection/forecast intelligence for revenue leadership.
- Likely confusion set: CRM (system of record), Sales Forecasting Platform, Conversation Intelligence Platform, Sales Pipeline Management, Sales Performance Management, Marketing Attribution, BI Platform.
- Market note: the label "revenue intelligence" consolidated a cluster of older capabilities (sales analytics, forecasting, activity capture, conversation intelligence) around 2019–2021; several vendors have since repositioned as "revenue platform / revenue orchestration / revenue AI". Category label evolution must not leak into the canonical definition.

---

## Research Questions

1. What is the data foundation? What is mirrored from the CRM vs captured from other systems? How is captured activity associated with deals/accounts?
2. What core objects exist (deal/opportunity, account, activity, forecast submission, roll-up, snapshot/trend, target/quota, score/warning)?
3. What are the primary workflows: deployment/connection, continuous deal inspection, the periodic forecast cycle, AI Q&A?
4. Who uses it (rep / manager / manager-of-managers / RevOps / executive) and what can each do?
5. What rules matter: hierarchy visibility, forecast categories, audit/snapshot history, CRM write-back, permissions, capture consent/exclusion?
6. Where is the boundary vs CRM, Sales Forecasting Platform, Conversation Intelligence, Pipeline Management, SPM, BI?
7. Historical/market-sample check: do pre-"revenue intelligence"-label products (spreadsheet roll-ups, CRM forecast modules, CRM-report sales analytics) satisfy the definition?

---

## Representative Products

| Product | Sample rationale | Positioning observed (official surfaces) |
|---|---|---|
| Clari | Enterprise pole; forecast-centric heritage; widest suite | "Revenue Orchestration Platform"; modules Capture / Inspect / Forecast / Copilot / Groove / Align / Guide / RevAI; RevDB "single AI-powered revenue database"; merging with Salesloft (site banner) |
| Gong | Conversation-intelligence heritage; richest public help center | "Revenue AI OS"; "undisputed leader in Revenue Intelligence"; Deals / Forecast / Engage / Enable / Revenue Graph / AI agents |
| BoostUp (now Terret) | Pure-play RI/forecasting pole, now AI-agent-native | "Terret — Answer-to-Action Engine"; Terret Forecast "machine-precision pipeline forecasting"; Terret Conversation Intelligence; "revenue graph" foundation |
| People.ai (now Backstory) | Activity-capture data-foundation pole | "AI Revenue Platform"; auto-captures email/meetings/calls/chat and matches to deals/accounts/contacts; multi-CRM; "built for leaders making commit decisions" |
| Aviso | Forecasting + deal-guidance pole; agentic-AI packaging | "End-to-End AI Revenue Platform"; Revenue Forecasting / Pipeline Inspection / Deal Acceleration / Relationship & Conversation Intelligence; time-series database claim |

Market-structure notes (Layer B): multiple sampled vendors renamed/re-merged during 2025–2026 (People.ai→Backstory, BoostUp→Terret, Clari+Salesloft). The category is consolidating around "revenue platform / revenue AI" wording while keeping the same structural core. Analyst-taxonomy anchors observed on vendor pages: G2 "Revenue Operations & Intelligence" badges (Backstory), Gartner Magic Quadrant for Revenue Action Orchestration (Clari).

---

## Sources

Tier 1 (official operational documentation):

- Gong Help Center (Document360; llms.txt index): Understanding Gong deals; What is Data capture?; Reality-based forecasting; How to forecast; About deal likelihood scores; Set up your pipeline view and begin forecasting; Understanding configurable forecast boards; Gong Forecast and your CRM; About permission profiles; Team hierarchy. https://help.gong.io/ (fetched 2026-09-07)
- Clari product documentation pages: Clari Capture (/products/capture/), Clari Inspect (/products/inspect/), Clari Forecast (/products/forecast/), RevDB (/products/revdb/). https://www.clari.com/ (fetched 2026-09-07)

Tier 2 (official product/positioning pages):

- Clari site navigation & module map (incl. Salesloft merger banner) — fetched 2026-09-07
- Gong — https://www.gong.io/revenue-intelligence/ — fetched 2026-09-07
- Terret (BoostUp) — https://www.boostup.ai/ (root served in place of /forecasting/) — fetched 2026-09-07
- Backstory (People.ai) — https://www.people.ai/ (redirects to backstory.ai; extensive on-page FAQ) — fetched 2026-09-07
- Aviso — https://www.aviso.com/ — fetched 2026-09-07

Not reached (recorded limitations):

- Clari Knowledge Base / Support Portal (clari.my.site.com — Salesforce community, not fetched; JS-gated). Clari operational detail therefore rests on Tier-2 product pages only.
- Terret and Aviso help centers not fetched (not discovered from fetched surfaces within budget). Claims about these products are held at Tier-2 strength.
- Gong help-center pages fetched via .md endpoints; some pages marked "stale" by the publisher — content still treated as official.

---

## Product Observations

### Gong (Tier 1 — strongest operational evidence)

Key observations (evidence layer A):

- **Deals / deal boards**: "Deals incorporates a complete set of solutions to help sales teams visualize, manage, and optimize their sales pipeline. By combining CRM data with Gong's AI-powered insights…" Deal boards are customizable views (filters, tabs, columns) over the pipeline; display deal value, expected close date, sales-methodology (playbook) compliance, activity timelines, AI risk assessments. Drill-down opens deal panels with contact info and conclusions. Deal boards "provide the basis of forecast accuracy".
- **CRM synchronization (bi-directional)**: "Seamlessly update your CRM fields directly from deal boards" (write-back), while CRM data is imported (read) and tracked for field changes (close date, amount, stage tracked-change import documented under deal-likelihood prerequisites).
- **AI warnings**: automated at-risk alerts — lack of engagement, single-threaded relationships, stalled deals, unaddressed pricing concerns; user-configurable warning settings.
- **Data capture**: "the term used for how Gong identifies and imports interactions with your customers." Captured classes: voice activities (telephony calls, web-conference calls incl. metadata and failed attempts), text activities (emails, SMS), digital interactions (CMS/VMS/gifting/CPQ/buyer-intent platforms). Setup = connect Google Workspace / Office 365 company-wide or per-user, web-conferencing providers (Zoom native or bot), telephony providers, dialer; recording settings and consent profiles; exclusion lists (domains, emails); per-member capture settings. CRM integration "enriches activities by adding business context".
- **Captured data use**: deal likelihood, deal warnings, win/loss analysis, insights, coaching "depend on captured data"; emails displayed in activity timeline on deal boards.
- **Forecast**: "Reality-based forecasting" — bottom-up submission across forecast categories used by the business; leaders see reps' forecasts and update their own; roll-up of reps and sales leaders in one place; reminders and update-status; forecast boards configured per line of business (e.g., "New business" vs "Renewals"); **Business total** view aggregates business lines (regions/territories/teams/product lines); each person sees own forecasts, managers see direct reports (granular via permission profiles).
- **Forecast boards mechanics (How to forecast)**: "flexibility of spreadsheets connected to the real-time data of Gong and your CRM". Columns are metric columns (bookings status, targets), submission columns (manual or auto-submit), target columns. Submission flow: select team + period → click submission cell (e.g., Commit) → enter number → see team rollup number, write a note for the manager, view Submission changes over time, progress toward target, drill into the deals composing the cell (opens deal-board view sorted by amount), monthly breakdown of quarterly numbers. Cadence reminders appear in-app and in Slack; reminder clears on submission. Inactive team members auto-hidden unless they carry data for the period (badge); excluded members (no quota / not forecasting that stream) are removed from rollups, analytics, and projections — exclusion requires the Manage Forecast board permission.
- **AI Deal Predictor / deal likelihood scores**: AI agent scoring each open deal on likelihood to close-won in its expected period; a **percentile rank of relative deal health** vs the company's own historical won/lost deals (explicitly not a win probability); positive/negative signals listed under each score; computed from "300+ signals" originating in CRM data, calls, emails, and CI features (warnings, trackers); prerequisites include CRM integration (Salesforce/HubSpot/Dynamics), tracked changes on close date/amount/stage, and minimum historical deal counts (vendor-specific numbers); scored daily; exported to Gong Data Cloud. Surface presence: Forecast page, deal boards, deal pages, pipeline views.
- **Organization/permissions**: team hierarchy; permission profiles; seat types (Call Intelligence seat; Forecast seat; packages Forecast Essentials / Gong Forecast / Deal Execution); provisioning via SCIM/HR systems; workspaces; data protection (consent profiles, redaction, retention, exclude lists).
- **Adjacent modules inside the platform**: Engage (sales engagement: flows, templates, dialer, to-dos), Coaching (scorecards, AI scoring), Insights (team performance, market), Dashboards/"Revenue analytics" (metrics & targets, KPI/funnel/trends/forecast-rollup widgets, dashboard recipes for pipeline health / leadership forecast / retention), AI agent catalog (Deal Monitor, Deal Predictor, Revenue Predictor, Ask Anything, Briefer, Tracker…), MCP server/client, Data Cloud/API.

### Clari (Tier 2 — product pages; nav-confirmed module map)

Key observations (evidence layer A for module existence and self-description; layer B for operational mechanics):

- Platform self-positioning: "Revenue Orchestration Platform"; "One company, one site" banner confirming the Salesloft merger with redirect date 9/15/26.
- **Capture** — "Auto-Capture and Sync Sales Activity to Your CRM": "automatically collects and syncs activity data to CRM"; contact/activity data capture and enrichment; stakeholder-relationship mapping, engagement levels, persona gap pinpointing; positions capture as eliminating manual CRM updates. (Exact capture-source taxonomy not documented on fetched page.)
- **Inspect** — "Opportunity management and deal inspection": "centralizes complex revenue data into one insight-rich dashboard"; "unified view of your entire book of business"; "AI-driven health scores and risk indicators"; connects insights to "revenue workflows"; configurable custom views; marketed vs Salesforce reports ("the Inspect tab feels more intuitive" — customer quote).
- **Forecast** — "Forecasting intelligence for every revenue model": "automated forecast roll-ups"; "one-click visibility from top-line views to individual deals"; "scenario modeling"; supports "every revenue model, including subscription and consumption" (predict existing ARR, deal-based ARR, usage-based ARR); Salesforce + other integrations (Excel, SQL Server, PostgreSQL, Databricks shown in integration strip).
- **RevDB** — "consolidates fragmented data into a single, AI-powered database, powering the entire Clari Revenue Platform"; "consolidating and **snapshotting** data from every source to close data gaps"; "time-series data" fueling AI; positioned as single source of truth. (Marketing page; "snapshotting" and "time-series" are the operationally meaningful terms.)
- **Other modules in map**: Groove (sales engagement/prospecting), Align (buyer collaboration, mutual action plans), Copilot (conversation intelligence & coaching), Guide (AI action hub), RevAI (revenue AI agents for "deal inspection and sales productivity; automate forecasting"), Analytics, Revenue Cadences (cadence methodology), Integrations.
- Teams addressed: RevOps, Sales, Marketing, Post-Sales, Finance, Sales Engineering. Enterprise customer logos across pages.

### Backstory / People.ai (Tier 2 — positioning + unusually explicit on-page FAQ)

Key observations (evidence layer A for the FAQ statements):

- "Is Backstory the same as People.ai? Yes. People.ai is now Backstory."
- Core loop (self-description): "Backstory reads every call, email, and CRM record across the quarter, then surfaces the few moves that actually change your number — each one sourced to the meeting, the stakeholder, and the dollars at stake."
- **Capture + matching**: "captures every email, meeting, call, and chat across your team, maps that activity to your deal history"; "Activity is captured automatically from each system and matched to the right accounts, opportunities, and contacts — so your data is complete without anyone logging anything manually."
- **Multi-CRM**: "connects to multiple CRMs simultaneously and surfaces every sales activity across your org in a single view" (Salesforce, Microsoft Dynamics, Oracle named; Gmail/Outlook/Zoom/Teams/Slack named as sources).
- **Explicit contrast with CRM and forecasting tools** (their FAQ): "Your CRM is only as accurate as what reps enter. Your forecasting tool predicts based on that same incomplete data… Backstory gives you answers backed by what actually happened."
- **Audience posture**: "It's not a rep productivity tool — it's built for the leaders making commit decisions, pipeline calls, and driving revenue strategy" (CROs / VPs of Sales).
- **Solutions taxonomy**: Revenue Decisions (answers + engagement scoring + deal summaries), Pipeline Health & Deal Risk (forecasting, waterfall charts, risk headlines; "which pipeline is real, which is slipping… every status traces back to the activity behind it"), Account Strategy (stakeholder maps, automated account plans, parent-account roll-ups), Opportunity Qualification (MEDDPICC scoring "backed by a real meeting or email").
- **Delivery surfaces**: web app, CRM-embedded, Slack, LLM tools via MCP server; consumption-style pricing narrative (answer caching).
- featureList (schema.org on page): automatic activity capture; AI-powered deal-risk identification; pipeline health monitoring; revenue forecasting; CRM integration; multi-threaded deal tracking; stakeholder engagement analysis; MCP integration.

### Terret / BoostUp (Tier 2 — positioning page; /forecasting/ URL served root content)

Key observations (evidence layer A for self-description, layer B for mechanics):

- Products: **Terret Nexus** ("answer-to-action revenue engine"), **Terret Forecast** ("machine-precision pipeline forecasting"), **Terret Conversation Intelligence**.
- **Machine forecast**: "Where will we land this quarter? Generate a machine forecast and equip the CRO weekly with a board-ready narrative on headwinds, tailwinds, and deal movement"; UI mock shows machine forecast + at-risk deals (−$1.2M) + upside opportunities (+$640K) + forecast narrative.
- **Revenue graph foundation**: "Structured & unstructured data unified; every revenue-facing system connected" (Foundation layer) → answers → agents → execution; "Auto syncing with Salesforce"; CRM updates from agent actions ("Assets associated with opportunities and workflows updated in CRM").
- Signals used: calls (conversation intelligence), meetings, CRM, expansion signals (seat utilization, champion changes, QBR timing) — i.e., same captured-engagement → intelligence loop; agent-executed actions written back to CRM.
- Heavy AI-agent packaging (playbooks generated from won/lost patterns, call briefs delivered to Slack, deals flagged at risk with recommended talk tracks).

### Aviso (Tier 2 — positioning page)

Key observations (evidence layer A for module existence, layer B for mechanics):

- Self-positioning: "End-to-End AI Revenue Platform… agentic AI, forecasting, conversational intelligence, and unified RevOps in one platform"; "time-series database for context and training of models".
- Guidance modules: Conversation Intelligence; Relationship Intelligence ("Engage the right buyers in every account, kill single-threading"); Coaching & Enablement; Marketing Intelligence; Sales Engagement; **Revenue Forecasting** ("flexibility to execute advanced forecasting models at your preferred cadence"; consumption business + ACR named by customer); **Pipeline Inspection** ("Inspect early-stage and mature pipe. Know gaps and red flags. Plan ahead for future quarters"); **Deal Acceleration** ("Guide reps to take the right next step for deal progression, CRM hygiene and forecasting accuracy").
- Mobile app framed as "AI-Powered Revenue Command Center" (predictive forecasting, pipeline management, deal guidance, CI).
- Competitor-comparison pages exist vs Clari, BoostUp, Gong, People.ai, Salesloft, Outreach (confirms shared category membership).

---

## Cross-product Comparison

| Dimension | Gong | Clari | Backstory (People.ai) | Terret (BoostUp) | Aviso | Evidence |
|---|---|---|---|---|---|---|
| Deal model mirrored from CRM | Yes (CRM import, tracked field changes; Salesforce/HubSpot/Dynamics) | Yes (Salesforce + data-warehouse integrations; RevDB) | Yes (Salesforce/Dynamics/Oracle; multi-CRM) | Yes ("auto syncing with Salesforce") | Yes (CRM hygiene write-backs) | A (all) → B |
| Automatic engagement capture | Yes (telephony, web conf, email, SMS, digital interactions) | Yes (Capture module) | Yes (email/meeting/call/chat) | Yes (calls, meetings, digital signals) | Yes (CI + relationship intelligence) | A (all) → B |
| Activity auto-associated to accounts/opportunities/contacts | Yes (CRM entity association, auto/manual) | Yes (capture sync to CRM) | Yes ("matched to the right accounts, opportunities, and contacts") | Yes (assets associated to opportunities) | Yes | A (Gong, Backstory explicit) → B |
| Pipeline/deal inspection surface | Deal boards + drill-downs + warnings | Inspect (unified book of business, custom views) | Pipeline Health (stage-by-stage, waterfall, risk headlines) | Deal flags/at-risk lists inside Nexus | Pipeline Inspection module | A (all) → B |
| AI deal/risk scoring | Deal likelihood scores (percentile of relative health) | AI health scores + risk indicators | Engagement scoring + deal risk | At-risk flags + pattern detection | Win-probability / deal guidance | A (Gong, Clari explicit) → B |
| Forecast with roll-up | Yes (submission columns, cadence, hierarchy rollup, business totals) | Yes (automated roll-ups, scenario modeling, multi revenue model) | Yes (forecasting solution line) | Yes (machine forecast + CRO narrative) | Yes (advanced models, own cadence) | A (Gong, Clari explicit) → B |
| Forecast submission workflow (bottom-up + note + audit) | Documented in detail | Implied by roll-up + scenario language; detail not fetched | Not surfaced | Weekly CRO narrative framing | "at your preferred cadence" | A (Gong) / product-specific depth |
| Snapshot / trend history | Submission changes over time; trend charts | RevDB snapshotting + time-series | Waterfall "exactly what moved" | Headwind/tailwind narrative | Time-series database claim | A (Gong, Clari) → B |
| CRM write-back | Yes (edit CRM fields from deal boards) | Yes (capture syncs to CRM; agents update CRM) | Yes (implied; answers delivered in CRM) | Yes (agents update CRM) | Yes (deal acceleration touches CRM) | A (Gong) → B |
| Hierarchy + permission structure | Team hierarchy, permission profiles, seat types | Enterprise readiness pillar; roles per team page | Leader-first posture (CRO/VP) | CRO-framed narrative | BDR→CRO role framing | A (Gong) → B |
| Conversation intelligence inside | Yes (native heritage) | Yes (Copilot module) | Captured calls analyzed (not a CI-product pitch) | Yes (separate product line) | Yes (module) | A (all) → B |
| Sales engagement inside | Yes (Engage) | Yes (Groove) | No (not surfaced) | Not surfaced | Yes (module) | A (Clari, Gong, Aviso) |
| Buyer collaboration surface | Not surfaced | Yes (Align, mutual action plans) | No | No | No | A (Clari only) → product-specific |
| AI agent layer | Yes (agent catalog, MCP) | Yes (RevAI, Guide) | Yes (assistant + MCP answers) | Yes (Nexus agents) | Yes (agentic workflows, agent studio) | A (all) → B |
| Revenue models supported | Per business line (new business/renewals boards) | Subscription + consumption + usage-based ARR | Not surfaced | Not surfaced | Consumption + ACR | A (Clari, Gong, Aviso) → B |

## L0 / L1 / L2 / L3 abstraction

### L0 — Defining Invariant

Minimal structure without which the product is not a Revenue Intelligence Platform:

1. **Synced revenue-deal model** — a continuously synchronized mirror of the organization's in-flight revenue: opportunities/deals with amount, stage, owner, close date, drawn from the CRM of record, organized under a seller/team hierarchy. (Remove → nothing for the product to be intelligent about.)
2. **Captured engagement record joined to the deal model** — buyer–seller activity (calls, emails, meetings, chat, digital touches) captured automatically from connected systems and associated with deals/accounts/people, forming a record that exists beyond manual CRM entry. (Remove → the product degenerates into CRM reporting/BI or a pure forecasting module; the captured foundation is the category's constituting differentiator.)
3. **Derived revenue intelligence over the combined model** — the platform *computes* the state and trajectory of revenue rather than merely storing it: inspection of pipeline/deal condition (health, risk, movement) and projection of future revenue (forecast). (Remove → an activity-capture/CRM-sync tool, not "revenue intelligence".)

Three invariants only. Seller hierarchy and leadership delivery are carried inside invariants 1 and 3 as orientation, but detailed role/permission mechanics are L1.

### L1 — Common Mature Structure (present across the sample; not definitional)

- Forecast submission cadence: bottom-up number submission per forecast category + notes + reminders; roll-up through the management hierarchy; business-total / multi-line-of-business aggregation; submission-change audit trail; auto-submit option (documented in detail for Gong; roll-up + audit present in Clari framing).
- Configurable board/grid surfaces: deal boards and forecast boards with filters/columns/tabs; drill from any aggregate number to its composing deals.
- AI risk/health scoring on deals + automated warnings (single-threading, stalled, no next meeting, pricing concerns — phrasing varies).
- Targets/quota columns vs actuals; pacing/projection views; dashboards and analytics widgets; snapshot/trend-over-time semantics.
- CRM write-back (edit select CRM fields from the platform; agent-executed CRM updates).
- Stakeholder/relationship intelligence (engagement levels, multi-threading gaps, persona coverage).
- Activity timeline on deals; win/loss analytics; account-level roll-ups and account planning aids.
- Admin layer: capture connections (email/calendar/conferencing/telephony), recording consent, exclusion lists, permission profiles, team hierarchy, seat/plan packaging.
- AI assistant / agent layer (NL Q&A over revenue data, next-best-action, briefs); mobile app; API/Data Cloud/MCP exposure.

### L2 — Variant / Optional Structure

- Conversation-intelligence depth: from light signal extraction to full recording/transcription/coaching product lines (standalone CI products exist outside this Type).
- Sales-engagement modules inside the platform (sequencing, dialer) — present in several suites, absent in pure-play data-foundation products.
- Buyer collaboration surfaces (shared mutual action plans) — one sampled vendor.
- Revenue model coverage: subscription/ARR vs consumption/usage vs committed-revenue variants; multi-CRM support; multi-currency.
- Audience packaging: CRO/leader-first (answers, board narratives) vs rep-inclusive (in-product to-dos, engagement tools).
- Data-plane exposure: warehouse/data-cloud integrations, API/MCP for external LLMs, embedded-in-CRM surfaces.
- Deployment/enterprise posture: SaaS standard; enterprise governance, security certifications as scale features.

### L3 — Vendor-specific (Research Notes only)

- Clari: RevDB branding and "$4T under management" claim; Groove/Align/Copilot/Guide module names; "98% forecast accuracy by week two" customer claims; Salesloft merger; Gartner MQ for Revenue Action Orchestration badge.
- Gong: deal-likelihood score bands (1–29 low / 30–75 fair / 76–99 high), "300+ signals", daily scoring cadence, minimum historical-data prerequisites (50 won / 150 lost over 2 years etc.), package names (Forecast Essentials, Gong Forecast, Deal Execution), credits/MCP specifics, Slack reminder integration.
- Terret/BoostUp: Nexus branding, 48-hour proof-of-concept offer, "45,000 calls across 345 reps" illustrative figures.
- Backstory/People.ai: 2–4 week onboarding claim, "analyzes two years of deal history on day one", consumption pricing with answer caching, MCP-first answer delivery.
- Aviso: 13-week cadences, 30+/50+ agent/workflow counts, AI avatars, agent studio, mobile "command center" framing.

---

## Rejected Findings (considered and NOT promoted)

- "AI agents / agentic AI" as definitional: universal in 2026 packaging but a delivery mechanism of the intelligence layer, not the structure. Older RI predates agents. → L2/L1.
- "Single database / revenue graph" as definitional: every vendor markets a unifying data layer under a brand name (RevDB, Revenue Graph, Backstory foundation). The invariant is the *joined model* (deals + captured engagement), not any specific data-plane productization. → abstracted into L0-1 + L0-2.
- "Percentile-based scoring" as definitional: Gong-specific scoring semantics; Clari/Backstory/Aviso describe scores differently. → L1 with vendor-specific details in notes.
- "Weekly cadence" as definitional rhythm: Gong documents cadence configuration; Aviso claims flexible cadence. Cadence is configurable, so no fixed rhythm belongs in the definition. → L1, phrased as "recurring cadence".
- "Multi-CRM" as definitional: only Backstory foregrounds it. → L2.
- "Rep productivity uplift" (email drafting, dialer): sales-engagement drift. → out of Type (adjacent capability).
- Precise accuracy claims (e.g., "98% forecast accuracy", "12x boost"): marketing figures, single-vendor. → rejected entirely from canonical text.

## Historical / Market-Sample Check (per §24 spirit)

- The "revenue intelligence" label dates to roughly 2019–2021; the structural predecessors are: (a) spreadsheet-based forecast roll-ups over CRM exports, (b) CRM-native forecast modules, (c) standalone sales-analytics dashboards fed by CRM reports.
- Test: do (a)–(c) satisfy the L0? They satisfy L0-1 (deal model, though static/manual sync) and partially L0-3 (forecast), but they **lack L0-2** — no automatically captured engagement joined to deals.
- Resolution: L0-2 is retained as definitional because the category exists precisely as the corrective to manual-entry CRM data ("operate based on reality instead of opinion" — Gong; "Your CRM is only as accurate as what reps enter" — Backstory FAQ; "eliminate the burden of manual CRM updates" — Clari). The spreadsheet/CRM-report era is the *baseline problem* this Type constitutes itself against, not an earlier form of the Type. A product with forecast + inspection but no captured-engagement foundation is classified as Sales Forecasting Platform / sales analytics, not RI.
- Counter-check for over-fitting: L0 does not depend on any 2020s implementation choice — capture channels (email/calendar/calls today; whatever tomorrow), AI techniques, agent packaging, cloud delivery are all outside the definition. A future RI product capturing different signal types still fits.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove what → becomes the other" test) |
|---|---|---|
| Customer Relationship Management / CRM | record system vs insight layer | The CRM *owns* the deal/contact record; RI *mirrors* it, adds captured engagement, and derives intelligence. Remove RI's derived intelligence + capture → you have a CRM. Remove CRM's record ownership (quoting, lead/contact master data) → you have RI. Write-back exists (Gong edits CRM fields from deal boards) but the system of record remains the CRM. |
| Sales Forecasting Platform | overlapping seam — flag for joint review | Both produce forecasts. Working distinction: RI = full revenue model (captured engagement foundation + inspection + forecast); forecasting platform = forecast production/roll-up as the primary object, typically working on CRM fields without a captured-engagement foundation. The market itself blurs the seam (Aviso and Terret sell "forecasting" as a module of RI; Clari began forecast-first). Recorded in Boundary Issues. |
| Conversation Intelligence Platform | input vs end product | CI's primary object is the recorded conversation (transcript, topics, coaching); RI's primary object is the revenue model. When conversation analysis feeds deal/revenue condition → it is a captured signal inside RI (all five sampled products embed it). When conversation analysis/coaching is the end product → standalone CI Type. |
| Sales Pipeline Management | management vs intelligence | Pipeline management concerns the flow/creation/progression of pipeline as managed process (stages, hygiene, creation plays); RI concerns leadership visibility, prediction and derived condition over that pipeline. Overlap is real (RI products include inspection of pipeline); the discriminator is the captured-engagement foundation + projection. |
| Sales Performance Management | number visibility vs comp/quota machinery | SPM owns quota planning, territory, commission calculation. RI consumes targets/quota as inputs (target columns, attainment views) but does not compute compensation. |
| Business Intelligence Platform | generic vs revenue-specific | BI connects arbitrary data sources to dashboards; RI carries a revenue-native data model (deals, activities, forecast categories, seller hierarchy) and capture machinery. An RI deployment can feed a BI layer (Data Cloud/RevDB exports), but generic BI cannot self-capture engagement or run the forecast cadence. |
| Marketing Attribution Platform | same signals, different question | Both read captured touches; attribution answers "which marketing touch produced revenue", RI answers "where will revenue land and what needs action". |
| Customer Health Monitoring / Customer Success Platform | adjacent book-of-business surface | Renewals/expansion signals appear inside RI (renewals boards, expansion signals), but post-sale health management as record-and-workflow system is a separate Type. |

**Boundary Issues to record in STATUS.md:**

1. Revenue Intelligence Platform ↔ Sales Forecasting Platform: heavy object overlap (forecast roll-up lives in both); recommend joint review when sales-forecasting-platform is processed; consider whether Sales Forecasting Platform should be defined as the forecast-production capability (including CRM-native modules) with RI as the platform realization adding capture + inspection.
2. The category label is unstable ("revenue intelligence" → "revenue platform/orchestration/AI"); two of five sampled vendors rebranded and one merged during 2025–2026. The leaf name remains the market-recognizable anchor (Gong still titles its category page "Revenue Intelligence"; G2 category "Revenue Operations & Intelligence"), but reviewers should not expect vendor self-labels to match.

---

## Uncertainties

- Clari operational mechanics (forecast submission flow, permission detail, capture-source taxonomy) rest on Tier-2 product pages; the Clari KB was unreachable. Claims about Clari kept at module-scope strength.
- Terret and Aviso help centers not fetched; their forecast/inspection mechanics inferred from positioning pages only.
- Whether every RI deployment must include a formal *submission* forecast (vs AI-generated projection only) is unconfirmed outside Gong/Clari; Backstory/Terret emphasize machine-generated answers/narratives. The canonical text therefore phrases projection broadly (submission-driven, AI-driven, or both) rather than requiring human submission.
- Pre-2020 products were not directly researched (out of budget); the historical judgment is reasoned from the category's own positioning against manual-entry CRM data rather than from fetched primary sources.

---

## Final Synthesis

A Revenue Intelligence Platform is a revenue-leadership application built on a two-part data foundation — a continuously synchronized mirror of in-flight deals from the CRM of record, plus automatically captured buyer–seller engagement (calls, emails, meetings, chat, digital touches) associated with those deals, accounts, and people — over which the platform derives a computed picture of current and future revenue: pipeline and deal inspection (health, risk, movement) and revenue projection/forecast, delivered through board surfaces, drill-downs, dashboards, and increasingly conversational/agent interfaces, operated on a recurring cadence by sellers, managers, RevOps, and executives, with the CRM remaining the system of record and the platform writing select state back to it.

Canonical object sketch:

```text
CRM of record (external system)
   │ continuous sync (read + selective write-back)
   ▼
Deal / Opportunity ── belongs to ── Account ── people/contacts
   │ amount · stage · owner · close date         │
   │                                             │
Captured Engagement (calls · emails · meetings · chat · digital)
   └── auto-associated to deals / accounts / people
   │
   ▼
Derived Intelligence
   ├── deal health / risk / warnings (scores, signals)
   ├── pipeline inspection (boards, roll-ups, snapshots/trends)
   └── forecast (categories · submissions · hierarchy roll-up · projection)
   │
   ▼
Surfaces: deal boards · forecast boards · dashboards · deal panel ·
          AI Q&A/agents · mobile · embedded-in-CRM · exports/APIs

People: rep → manager → manager-of-managers → executive (+ RevOps admin)
Cadence: recurring submission/inspection loop per period
```
