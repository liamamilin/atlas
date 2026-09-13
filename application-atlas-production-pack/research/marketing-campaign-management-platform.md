# Research Notes — Marketing Campaign Management Platform

## Research Goal

Understand what a Marketing Campaign Management Platform actually is as an Application Type: what the "campaign" object is in real products, what structures surround it, how campaigns flow from planning to execution to results, who uses the system, which rules matter, and where the Type's boundaries lie against Marketing Automation Platform, Advertising Campaign Management, Content Planning, and generic Project Management.

## Initial Boundary

Working hypothesis before research:

- Core use: marketing teams plan, organize, coordinate, execute, and measure marketing campaigns, with the campaign as the organizing container.
- Likely users: campaign/marketing managers, marketing operations, content/creative teams, channel specialists, executives.
- Nearest neighbors: Marketing Automation Platform (already processed in this atlas: person database of record + reusable automated program + per-contact program execution state), Advertising Campaign Management, Media Buying Platform, Social Media Management Platform, Content Planning Platform, Content Marketing Platform, Project Management Application, Marketing Analytics Platform.
- Known ambiguity: the market uses "campaign management" for two different things — (1) initiative planning/coordination platforms (marketing operations / marketing work management), and (2) cross-channel campaign execution engines (the Unica / Adobe Campaign tradition), which overlap the Marketing Automation Type. This pass targets meaning (1) and records the ambiguity.

## Research Questions

1. What is a campaign in these systems? Which attributes does it carry (name, owner, dates, goal, audience, budget, status)?
2. What structures surround the campaign (calendar, brief, assets, tasks, approvals, budget, channel links, metrics)?
3. Who uses the system, and how do roles affect workflow and permissions?
4. What is the typical campaign lifecycle (plan → brief → produce → approve → activate → measure → review)?
5. How does execution happen — native channel publishing, or orchestration/handoff to external execution systems?
6. How are results held at campaign level (goals, spend, attribution)?
7. Which rules matter (association rules, approval gates, permission-scoped visibility, lifecycle states)?
8. What variants exist (calendar-first SMB, enterprise marketing ops, work-management platforms, automation-suite campaign grouping)?
9. Where exactly is the seam to Marketing Automation Platform?
10. Historical check: would pre-software campaign practice satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

1. **CoSchedule (Marketing Suite / Marketing Calendar)** — calendar-first campaign planning; SMB/mid-market. Philosophy: the marketing calendar as the single source of truth.
2. **Aprimo (Plan / Spend)** — enterprise marketing operations suite (DAM-centered company with planning and spend modules). Philosophy: governance, goals, briefs, budgets at enterprise scale.
3. **Adobe Workfront (Workfront Planning + Workfront Workflow)** — enterprise marketing work management; Planning is a customizable record-based planning layer over Workfront's project execution engine. Philosophy: planning records linked to executable work.
4. **HubSpot (Marketing Hub Campaigns tool)** — mid-market automation suite; campaigns as the grouping + measurement layer over native execution assets. Philosophy: campaign as asset container with built-in attribution. Included deliberately as the boundary specimen showing how automation suites conceptualize campaigns.

## Sources

Research date: 2026-09-08

| Product | Source | Tier | Result |
|---|---|---|---|
| CoSchedule | https://coschedule.com/marketing-suite | 2 (product page) | fetched |
| CoSchedule | https://coschedule.com/marketing-calendar | 2 (product page) | fetched |
| CoSchedule | https://support.coschedule.com/ and /hc/en-us | 1 (help center) | FAILED twice (transport error) — abandoned per network rule |
| Aprimo | https://www.aprimo.com/ | 2 (product page) | fetched |
| Aprimo | https://www.aprimo.com/platform/plan | 2 (product page + FAQ) | fetched |
| Aprimo | https://help.aprimo.com/ | 1 (help center) | FAILED (401) — abandoned |
| Adobe Workfront | https://experienceleague.adobe.com/en/docs/workfront | 1 (docs home) | fetched |
| Adobe Workfront | https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-planning/planning-information | 1 (docs) | fetched |
| Adobe Workfront | https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-planning/adobe-workfront-planning-general-information/planning-overview | 1 (docs) | fetched |
| Adobe Workfront | https://experienceleague.adobe.com/en/docs/workfront/using/basics/campaigns/campaigns-overview | 1 | FAILED (404) — used Planning docs instead |
| Adobe Workfront | https://business.adobe.com/products/workfront/marketing-work-management.html | 2 | FAILED (timeout) |
| HubSpot | https://knowledge.hubspot.com/campaigns/create-campaigns | 1 (knowledge base) | fetched |
| HubSpot | https://knowledge.hubspot.com/campaigns/analyze-campaigns | 1 (knowledge base) | fetched |
| HubSpot | https://knowledge.hubspot.com/campaigns/use-your-marketing-calendar | 1 (knowledge base) | fetched |

Source-access limitations: no Tier 1 help-center documentation was reachable for CoSchedule or Aprimo; their observations rest on official product pages (Tier 2), which cannot alone prove detailed operational workflows. Assertion strength for these two products is calibrated accordingly. Workfront evidence is Tier 1 but centers on the Planning module; Workfront's own execution-side details (projects, approvals) are only lightly evidenced here.

## Product Observations

### CoSchedule (Marketing Suite / Marketing Calendar) — evidence layer A− (Tier 2 product pages only)

Key observations:

- Positioning: "all of your marketing — projects, campaigns, social media, and events — in one software"; "a unified calendar of record" showing "past, current, and upcoming campaigns."
- The marketing calendar is the primary surface: multiple calendars per team/department/initiative; table view of scheduled and unscheduled work; drag-and-drop rescheduling; permissions limiting access to specific projects/social platforms/tools.
- Campaigns: "Instantly Create Campaigns" (social campaigns scheduled to multiple networks); "Measure Performance: run social media reports to track the success of your social campaigns"; insights dashboards for social metrics.
- Production machinery: Kanban boards ("manage work through every stage of your creative process"), approval workflows ("require manager approvals... before publish"), request forms for internal project requests, team dashboards/reports.
- Content/asset layer: built-in DAM ("store, index, and share your content, files, and deliverables"); integrations with WordPress, ActiveCampaign, Mailchimp, Canva; content ideation-to-publish workflow.
- Native execution: social publishing to major networks, best-time scheduling, ReQueue (automated re-publishing); email via integrations rather than a native email engine.
- Strategy linkage: "Prove your value to stakeholders by demonstrating how projects and campaigns align with strategic business goals."
- AI: copy/image generation, prompt library, AI assistant (era-current features).
- Agency management is a marketed use case (agency calendar).

### Aprimo (Plan / Spend) — evidence layer A− (Tier 2 product pages + on-page FAQ; help center unreachable)

Key observations:

- Positioning: "Unify marketing goals, campaigns, and content"; "AI-powered marketing planning platform for strategic alignment, real-time visibility, and cross-functional collaboration." Company-level positioning is DAM/content-operations-first; Plan is the campaign-planning module.
- Campaign planning structures: "Align strategic goals with programs and campaign plans across business units and global teams"; "Program and Objective Management: connect every plan to business goals. Track initiative progress and version updates in real-time."
- Briefs: Intelligent Content Brief (ICB) — AI-generated structured campaign/content briefs from brand guidelines, business goals, historical data; "recommends channels, messaging, and content types"; single editable source of truth; "Regional & Channel Briefs: break global campaign briefs into sub-briefs applicable to specific regions, markets, or marketing channels."
- Calendar: "Marketing Calendar: interactive, centralized calendar for planning campaign launches, tracking content milestones, and visualizing strategic initiatives across teams and regions"; customizable global calendars with filters by market, team, campaign, objective.
- Campaign Frameworks: "templated campaign structures to scale best practices across markets and business units for consistent execution."
- Content Planning: "centralized workspace that connects strategy, assets, and teams for faster, smarter campaign execution."
- Task machinery (FAQ): "define tasks, owners, due dates, and dependencies — creating clear accountability and streamlining project execution."
- Insights: "Activity & Campaign Insights: dashboards and reports to track team activity and optimize resource utilization"; "real-time activity and performance data to optimize plans"; content utilization insights to increase "content and campaign ROI."
- Governance: "automated templates, governance models, and role-based access"; approval workflows tie campaigns/activities to business goals.
- Spend module (separate page): "Gain visibility into marketing investments and drive performance with financial control" — budget/financial management is a sibling module, not part of the Plan page claims.
- FAQ positions the product as replacing "spreadsheets and disconnected tools with a real-time, centralized view of all marketing activities, calendars, campaigns, and resource plans."

### Adobe Workfront (Planning + Workflow) — evidence layer A (Tier 1 official docs)

Key observations:

- Workfront Planning is a separately licensed planning layer (standalone or bundled with Workfront Workflow). Purpose: "unlock comprehensive visibility into the operational details of an organization, and answer critical business questions at each stage of the work management lifecycle."
- Canonical example questions from the docs are campaign-shaped: "How many campaigns are we running in EMEA for Q4?", "Do we have any audience overlaps between concurrent campaigns?", "How well are the awareness programs doing right now?"
- Architecture: Workspaces → Record types → Records → Fields; the framework is "fully customizable" (organizations define their own object types, attributes, and connections). Marketing workspace templates exist (workspace templates listed in architecture docs).
- Views over records: Table (default), Timeline, and Calendar views.
- Request forms: users submit requests against a record type's request form to create records (intake).
- Planning→execution bridge: "You can configure automations in Adobe Workfront Planning that, when activated, create objects in Workfront or records in Workfront Planning when triggered from a Planning record" — i.e., a campaign record can spawn executable Workfront projects.
- Connections: record types can be connected to each other and "link to object types from other systems, creating a coherent framework."
- Permissions: layered model — licenses (Workflow vs Planning), access levels, sharing permissions at workspace/record-type/record/view granularity.
- Reporting: Canvas Dashboards and Workfront Data Connect (Snowflake-based) for reporting over Planning data.
- AI: Planning AI Assistant (search/create/update/delete records via commands); MCP server for agentic access; GenStudio for Performance Marketing integration (records manageable in the GenStudio workspace).
- The core Workfront Workflow side (projects, tasks, approvals, portfolios, financials) is the execution engine the planning layer feeds; this pass only lightly evidences that side.

### HubSpot (Marketing Hub Campaigns tool) — evidence layer A (Tier 1 official knowledge base)

Key observations:

- Definition from the docs: "Use the HubSpot campaigns tool to create, manage, and report on a single marketing campaign with multiple assets in one place."
- Campaign object attributes (creation panel): campaign name (unique), campaign color (organizing/prioritizing; colors tasks on the marketing calendar), brand (brands add-on), campaign owner, campaign start date, campaign end date (both reflected on the marketing calendar; campaigns without dates do not appear on the calendar), campaign goal ("summarize the objective"; customizable targets "like the number of contacts or influenced revenue" via the campaign goals tracker), campaign audience ("specify an audience to help your team understand who your campaign is targeting"), currency code (for campaign budget), campaign notes.
- Asset association: emails, blog posts, landing pages, workflows, lists, etc. can be associated from the campaigns tool or from each asset's tool. Rule: "adding assets or content that are already associated with another campaign to a new campaign will remove them from their current campaigns. Only workflows and lists can be associated with multiple campaigns."
- Tracking URLs: created from the campaign, defaulting to the campaign's UTM value, "to measure the effectiveness of your campaigns in driving traffic."
- Marketing calendar: campaigns + tasks + marketing email events; Month/Week/Day/List views; filters by campaign and event type; "events displayed in the marketing calendar are dependent on a user's permissions" (e.g., no social publishing permissions → no social posts visible).
- Measurement (Performance tab): campaign goals progress (total goal progress, goal over time); ROI report (campaign spend total vs revenue/attributed revenue/associated deal value, with a documented ROI formula); revenue and revenue attribution reports (attribution models; Enterprise); influenced contacts; website traffic (sessions/new contacts via first/last touch); contact lifecycle count and lifecycle cost (cost per lifecycle stage from spend); asset reports per associated asset; traffic report over URLs containing the campaign UTM parameter.
- Attribution tab: contact create / deal create / revenue attribution with selectable attribution models and date ranges.
- Important metric semantics: "Campaign analytics... are based on the assets associated with the campaign"; asset data counts only from the association date onward in overview reports (per-asset reports keep full history).
- Collaboration: comments on campaigns; export of performance details (csv/xls/xlsx/PDF).
- Templates: campaign templates guide campaign creation; guided onboarding for first campaign.
- Permissions: Super Admin or Campaign permissions required for the campaigns tool; separate Task permissions for calendar tasks.
- API: Campaigns API for custom solutions; Claude connector can create campaigns, associate assets, and analyze campaign data including attribution.

## Cross-product Comparison

| Aspect | CoSchedule | Aprimo Plan | Workfront Planning (+Workflow) | HubSpot Campaigns |
|---|---|---|---|---|
| Campaign object | campaigns as calendar items on a "calendar of record"; social campaigns | campaign plans tied to programs/objectives; campaign frameworks (templates) | campaign as a customizable record type in workspaces (docs' example questions are campaign-shaped) | campaign record: name, color, brand, owner, start/end dates, goal (+targets), audience, budget currency, notes |
| Planning surface | marketing calendar (multiple calendars, table view, drag-drop) | marketing calendar with market/team/campaign/objective filters | table/timeline/calendar views over records | marketing calendar (campaigns + tasks + email events; month/week/day/list) |
| Goal/objective linkage | strategy-alignment claims (goals) | programs & objectives; plans tied to business goals; progress tracked | planning answers business questions (campaign counts by region/quarter, audience overlap) | campaign goal with configurable targets (contacts, influenced revenue); goal-progress reports |
| Briefs | request forms | AI-generated campaign/content briefs; regional & channel sub-briefs | request forms for record types | campaign notes; campaign templates |
| Assets | built-in DAM; integrations (WordPress, Canva, Mailchimp) | connects strategy, assets, teams (DAM sibling module) | records connect to each other and to Workfront objects; GenStudio integration | associate emails/blog posts/landing pages/workflows/lists; one-campaign-per-asset rule (workflows/lists exempt) |
| Execution | native social publishing; email via integrations | hands to content production (DAM/workflows); not a sending engine | automations create Workfront projects from planning records | assets execute in HubSpot's own tools (emails send, workflows run, pages publish) |
| Budget/money | not prominent | Spend module: marketing investments, financial control | Workfront-side financials (lightly evidenced here) | budget field + currency; spend in ROI/lifecycle-cost reports |
| Measurement | social reports; insights dashboards | activity & campaign insights; content utilization; performance data to optimize plans | Canvas dashboards; Data Connect reporting | performance tab (goals, ROI, revenue attribution, influenced contacts, traffic, lifecycle cost); attribution tab; UTM traffic |
| Collaboration/roles | permissions; approvals; team dashboards | role-based access; governance models; approval workflows | layered sharing (workspace/record type/record/view); licenses | campaign permissions; comments; permission-dependent calendar visibility |
| Templates | request forms | campaign frameworks | workspace templates | campaign templates |
| Hierarchy above campaign | calendars per team/initiative | programs & objectives | workspaces; customizable record-type graphs (portfolios/programs on the Workflow side) | none on the campaign page (brand add-on as a grouping) |
| Customer tier | SMB/mid | enterprise | enterprise | mid-market |

Stable cross-product commonalities (evidence layer B):

1. The campaign is a persistent, identified container for a bounded marketing initiative — carrying identity (name), ownership, a time window, and an intent/goal.
2. A shared planning surface — in every sampled product a calendar is the primary or canonical planning view (calendar-of-record, marketing calendar, calendar view, marketing calendar).
3. The campaign binds planned work: briefs/request forms define intent; assets/content are associated to the campaign; tasks/approvals coordinate production.
4. Activation is channel-oriented: either native publishing (CoSchedule social, HubSpot email/pages) or handoff/orchestration to execution systems (Aprimo to DAM/production; Workfront Planning to Workfront projects).
5. Results are held at campaign level: performance/spend/goal-progress reporting attached to the campaign (universal in sample; depth varies widely).
6. Templates/frameworks for repeatable campaign structures (all four).
7. Role-based permissions and approval gates around publication (all four).

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the product stops being a Marketing Campaign Management Platform:

1. **The campaign of record** — a persistent, individually identified container for one bounded marketing initiative, carrying at minimum: identity (name), an owner, a time window, and a stated goal/intent. Remove → scattered assets/tasks with no initiative container (generic task management, an asset library, or a bare analytics surface).
2. **The campaign plan** — the initiative's planned shape held in the system: what will be communicated (messaging/creative intent, typically captured as a brief or planned-asset set) and where it will run (channel/asset mix), defined before execution and revisable during it. Remove → a label stuck on ad-hoc work; no plan of record.
3. **Coordinated production & activation under the campaign** — the campaign's assets/messages are produced and/or activated through coordinated work (tasks, approvals, collaboration, native publishing, or handoff to execution systems), with progress tracked against the campaign. Remove → a strategy document or idea board; work happens elsewhere with no campaign-bound coordination.

Jointly-held is load-bearing:

- 1 alone = a campaign register/list (e.g., a bare CRM campaign object used only for grouping).
- 2+3 without 1 = generic project/work management with marketing templates.
- 1+2 without 3 = a planning/strategy document (content-planning territory).
- 1+3 without 2 = task management wearing a campaign label.

### L1 — Common Mature Structure

Universal-in-sample or near-universal capabilities that are not definitional:

- **Marketing calendar** as the shared planning surface (4/4 sample; the exact surface differs — calendar-of-record, filtered global calendar, calendar view, marketing calendar tab).
- **Campaign-level results** — performance/spend/goal-progress reporting attached to the campaign (4/4 sample; depth ranges from social reports to full attribution). Held here rather than L0 because a planning-and-coordination product without deep measurement is still recognizable as campaign management; measurement closes the loop but does not define the container.
- **Briefs / intake** — request forms or briefs that capture intent before production (4/4 in some form).
- **Asset association/management** — linking content/assets to the campaign, often with a DAM (4/4).
- **Tasks, approvals, and workflow** for production coordination (4/4).
- **Templates/frameworks** for repeatable campaign structures (4/4).
- **Goals/objectives linkage** above campaigns (3/4 explicit: Aprimo programs/objectives, HubSpot goal tracker, Workfront business-question framing; CoSchedule claims-level only).
- **Roles & permissions** (4/4).
- **Collaboration** (comments, sharing, team dashboards) (4/4).

### L2 — Variant / Optional Structure

- **Execution posture** — native channel execution (CoSchedule social publishing; HubSpot email/pages/workflows) vs orchestration-only handoff (Aprimo → production/DAM; Workfront Planning → Workfront projects). The single most consequential variant.
- **Budget/financial depth** — from a budget field (HubSpot) to a dedicated spend/financial-control module (Aprimo Spend) to work-management financials (Workfront); CoSchedule shows little on fetched pages.
- **Hierarchy above campaigns** — programs/objectives (Aprimo), workspaces and customizable record graphs (Workfront), brands (HubSpot add-on), per-team calendars (CoSchedule).
- **Audience/segment definition** — explicit audience field (HubSpot), audience-overlap questions (Workfront), regional decomposition (Aprimo sub-briefs).
- **Multi-market/regional decomposition** — global briefs broken into regional/channel sub-briefs (Aprimo; Workfront's EMEA example question).
- **AI assistance** — AI briefs (Aprimo ICB), AI content/social drafting (CoSchedule), AI record assistant (Workfront), AI campaign insights (HubSpot) — era-current, not definitional.
- **Agency/external collaboration** (CoSchedule agency management).
- **Deployment shape** — standalone planning product vs module of a marketing-operations suite vs campaign layer inside an automation suite vs planning layer over a work-management engine.

### L3 — Vendor-specific Structure

(Research Notes only; not for the final document.)

- CoSchedule: ReQueue automated re-publishing, Best Time Scheduling, Headline Studio, Hire Mia, free-forever calendar as entry product.
- Aprimo: Intelligent Content Brief (ICB), Librarian/Critic/Compliance/Production AI agents, DAM-first company positioning, Spend as sibling module, life-sciences/regulated-industry emphasis.
- Workfront: fully customizable record-type framework (vs fixed objects), Planning AI Assistant, MCP server, Fusion automations, GenStudio for Performance Marketing integration, Data Connect (Snowflake), Canvas Dashboards, layered license model (Workflow vs Planning vs standalone).
- HubSpot: campaign color coding, brands add-on, UTM tracking URLs, first/last-touch contact attribution, revenue attribution models (Enterprise), contact lifecycle cost reports, Claude connector, guided onboarding, campaigns API.

## Rejected Findings

- "Campaign management = sending messages to segments" (the Unica/Adobe Campaign tradition). Rejected as the definition of this leaf: that market is the campaign-execution engine, structurally the Marketing Automation Type (person database + programs + per-contact execution state). None of the four sampled planning-side products centers per-contact program execution. Recorded as a naming ambiguity / boundary issue instead.
- "A campaign always has a budget." Rejected as definitional: HubSpot has a budget field, Aprimo sells Spend separately, CoSchedule's fetched pages show no budget machinery, Workfront Planning is budget-agnostic records. Budget depth is variant (L2).
- "A campaign always defines its audience/segments." Rejected as definitional: explicit in HubSpot (a descriptive field) and Workfront's example questions, but CoSchedule's fetched material does not center audience definition, and Aprimo's briefs decompose by region/channel rather than segment. Held as common/variant.
- "The platform must natively publish to channels." Rejected: Workfront Planning and Aprimo Plan do not execute; they orchestrate. Native execution is a variant posture.
- "Campaign management = marketing project management." Rejected as an identity claim: the machinery overlaps, but the campaign container (goal, channel mix, asset association, campaign-level results) is marketing-specific and is what the Type adds to generic work management.
- "Attribution modeling is part of the Type." Held as product/segment-specific depth (HubSpot Enterprise), not definitional.

## Boundary Findings

- **vs Marketing Automation Platform** (already processed in this atlas): automation's defining core is the person database of record + reusable automated programs + per-contact program execution state. Campaign management's defining core is the initiative container + plan + coordinated production/activation. The seam: automation executes per contact; campaign management coordinates per initiative. In suites (HubSpot) both exist side by side — the campaigns tool groups and measures assets; workflows execute per contact. Remove the campaign container → still marketing automation. Remove the program engine → still campaign management.
- **vs Advertising Campaign Management** (directory sibling): advertising campaign management is ad-channel execution (targeting, serving, bidding on ad platforms). A campaign management platform coordinates the whole initiative — of which paid ads may be one channel — and owns planning/production/results rather than ad delivery mechanics.
- **vs Media Buying Platform**: media buying transacts placements; campaign management plans and coordinates the initiative that media buys serve.
- **vs Content Planning Platform / Content Marketing Platform** (directory siblings, not yet processed in this pass's scope): content planning centers the content calendar/production pipeline; campaign management centers the initiative container that content work hangs from, with goals/budget/results. Overlap is real (Aprimo markets "content planning" inside Plan; CoSchedule markets content marketing) — flagged as a potential consolidation question for those leaves' own passes.
- **vs Project Management Application**: generic PM lacks campaign semantics — goal with measurable targets, channel/asset mix, asset-to-campaign association rules, campaign-level results. A PM tool with a marketing template is a thin pole of this Type, not the definition.
- **vs Marketing Analytics Platform**: analytics measures without owning the campaign container/plan; campaign management holds results against its own campaigns (often pulling data from execution/analytics systems).
- **vs Brand Management Platform**: brand governance (guidelines, assets, consistency) vs initiative execution.
- **Naming ambiguity (taxonomy note)**: the enterprise "campaign management" market (IBM Unica / Adobe Campaign / Salesforce Marketing Cloud tradition) uses the same words for per-contact cross-channel execution engines. This leaf is documented as the planning/coordination meaning; the execution meaning is served by Marketing Automation Platform and adjacent execution leaves. Recorded in STATUS Boundary Issues.

## Historical / Market-Sample Check

Pre-software campaign practice: a campaign brief (goal, message, audience) + a media/channel plan + a planning calendar or wall board + a budget sheet + production schedules with sign-offs + a post-campaign report. This satisfies all three L0 legs (campaign of record; plan; coordinated production/activation) and the L1 measurement loop (post-campaign report) without any digital calendar, AI, attribution modeling, or cloud. Early-2000s marketing resource management (MRM) systems — the lineage Aprimo itself comes from — carried the same core as campaign-planning modules. The definition therefore does not over-fit to the current calendar/AI era. Check passed.

## Uncertainties

- CoSchedule and Aprimo observations rest on Tier 2 product pages; detailed operational rules (exact approval mechanics, campaign field schemas, state machines) could not be verified against Tier 1 help centers (support.coschedule.com unreachable; help.aprimo.com 401). Claims about these two products are kept at the level the pages support.
- Workfront's execution-side (projects/approvals/financials) was only lightly evidenced; the Planning module was the reachable Tier 1 surface. The planning→execution bridge is documented; execution-side detail is not asserted.
- Whether campaign-level measurement should sit in L0 or L1 is a judgment call; this pass holds it in L1 (universal-in-sample but not container-defining). If a future pass finds planning-only products marketed as campaign management without any results surface, L1 placement is confirmed; if not, revisit.
- The exact relationship to the not-yet-processed Content Planning Platform and Content Marketing Platform leaves is flagged, not resolved.
- HubSpot's campaign object is one implementation of "campaign as asset container"; whether automation-suite campaigns are a variant of this Type or a thin pole is recorded as a variant, not fully resolved.

## Final Synthesis

A Marketing Campaign Management Platform is the marketing team's system of record for campaigns as bounded marketing initiatives. Its defining core is three jointly-held structures: (1) the campaign of record — a persistent identified container carrying identity, owner, time window, and goal/intent; (2) the campaign plan — the initiative's planned shape (messaging/creative intent via briefs, channel/asset mix) held before and through execution; (3) coordinated production & activation under the campaign — tasks, approvals, collaboration, and/or activation of channel executions, with progress tracked against the campaign. Around this core, mature products standardly add: a shared marketing calendar as the planning surface, campaign-level results (performance/spend/goal progress), asset association, templates/frameworks, goals/objectives linkage, roles/permissions, and collaboration. The deepest variant is the execution posture: native channel execution vs orchestration/handoff to execution systems. The Type is distinct from Marketing Automation (per-contact program execution), from advertising campaign management (ad-channel execution), from content planning (content pipeline without the initiative container), and from generic project management (no campaign semantics).
