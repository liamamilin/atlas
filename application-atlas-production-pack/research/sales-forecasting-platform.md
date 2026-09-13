# Research Notes — Sales Forecasting Platform

Research date: 2026-09-07
Slug: sales-forecasting-platform
Directory location: §07 Sales, Customer & Revenue

---

## Research Goal

Understand what a Sales Forecasting Platform actually is as an application structure: what the forecast object is, where its data comes from, how it is structured (periods, categories, hierarchy), what users do in the recurring forecasting loop, what rules govern it, and where it begins and ends against neighboring Types — especially Revenue Intelligence Platform (pending joint-review flag from the RI pass), Quota Management, Budgeting & Forecasting / Financial Planning & Analysis (pending secondary flag from both §08 passes), CRM, and Sales Pipeline Management.

---

## Initial Boundary (hypothesis before research)

- Hypothesis: a sales-side application that produces the organization's projected revenue for coming periods, derived from the CRM pipeline (deals with amounts, close dates, stages) and/or direct human submission, aggregated up the sales management hierarchy, compared against quotas/actuals, and restated on a recurring cadence (typically weekly) until the period closes.
- Likely confusion set: Revenue Intelligence Platform, CRM (system of record), Quota Management (target vs prediction), Budgeting & Forecasting / FP&A (finance-model projection vs sales-pipeline projection), Sales Pipeline Management (progression vs projection), Sales Performance Management / Sales Compensation (umbrella / payout), BI.
- Prior-pass constraints to address:
  - RI pass adopted discriminator: Sales Forecasting Platform = forecast production/roll-up as the primary object, typically working directly on CRM fields without a captured-engagement foundation; CRM-native forecast modules and spreadsheet roll-ups belong to the forecasting side. Joint review recommended — this pass must ratify or revise.
  - Budgeting-forecasting / FP&A passes flagged: finance-side revenue projection inside the financial planning model vs sales-owned CRM-pipeline forecasting; sales-quota/account-planning modules inside budgeting platforms straddle. Secondary flag remains open for this leaf — this pass must resolve or explicitly hold it.

---

## Research Questions

1. What exactly is the managed object — "the forecast"? Is it one number, a set of category numbers, a grid, a saved record?
2. What are the inputs: which deal fields feed it, how are closed actuals incorporated, how do human judgments (submission/adjustment) enter?
3. How are periods structured? What is the restatement cadence? Is forecast history retained?
4. How does the hierarchy work (org-chart vs territory), and what can each level do?
5. What role do quotas/targets play? (Relationship to Quota Management Type.)
6. Where does machine prediction sit relative to human judgment?
7. How is the forecast surfaced (grid, drill-down, dashboards, mobile) and shared (permissions, exports, handoff to finance)?
8. Boundary checks per the flags above; historical/market-sample check (spreadsheet roll-ups, pre-AI CRM forecast modules).

---

## Representative Products

| Product | Sample rationale | Realization posture | Evidence tier reached |
|---|---|---|---|
| Microsoft Dynamics 365 Sales Forecasting | CRM-native enterprise pole; richest reachable operational docs; canonical "forecast as configured object" | module inside CRM suite | Tier 1 (Microsoft Learn: overview, configure, view, adjust) |
| HubSpot Forecasting (Sales/Service Hub) | Mid-market CRM-native; different philosophy (lightweight forecast tool, multi-pipeline, service teams) | module inside CRM suite | Tier 2 (official product page + FAQ) |
| Clari Forecast | Dedicated forecasting platform; forecast-centric heritage; enterprise | standalone platform over CRM | Tier 2 (official product page; KB gated per RI pass) |
| Aviso Revenue Forecasting | AI-native standalone pole; forecasting-heritage; consumption/usage revenue models | standalone platform over CRM | Tier 2 (official product pages) |
| Salesforce Forecasting (Sales Cloud) | Most-cited CRM-native realization in the market — retained as named representative | module inside CRM suite | NOT reached (help JS-gated; developer docs 403) — no operational claims drawn |

Market-structure note: two of five sampled forecasting-heritage vendors (Clari, Aviso) also appear in the Revenue Intelligence sample — the market sells forecasting as both standalone products and modules of wider revenue platforms. This is the documented seam, not a sample defect.

---

## Sources

Tier 1 (official operational documentation):

- Microsoft Learn — Dynamics 365 Sales: "Sales forecasting overview" (project-accurate-revenue-sales-forecasting), "Configure forecasts in your organization" (configure-forecast), "View and manage a forecast" (view-forecasts), "Adjust values in a forecast" (adjust-values-in-forecast). https://learn.microsoft.com/en-us/dynamics365/sales/ — fetched 2026-09-07

Tier 2 (official product/positioning pages):

- HubSpot — Forecasting Software product page with FAQ (forecast categories/models, team rollup, forecast permissions, weighted pipeline, historical snapshots, multi-pipeline, goal templates, AI forecasting). https://www.hubspot.com/products/forecasting — fetched 2026-09-07
- Clari — Forecast product page ("Forecasting intelligence for every revenue model"; automated forecast roll-ups; one-click top-line to individual deals; scenario modeling; subscription/consumption/usage ARR; Salesforce + warehouse integrations). https://www.clari.com/products/forecast/ — fetched 2026-09-07
- Aviso — platform root + "Revenue Forecasting" product page (automatic rollups across reps/categories/teams with best case, most likely, pacing; Winscore explanations; toggle deals in/out of commits; consumption→ARR/MRR; mobile forecasting; bidirectional Salesforce sync). https://www.aviso.com/ , https://www.aviso.com/product/revenue-forecasting — fetched 2026-09-07

Not reached (recorded limitations):

- Salesforce Help (help.salesforce.com) — JS/CSS error page; developer.salesforce.com — 403. Consistent with the account-management-crm pass finding ("Salesforce official docs unreachable (403)"). Salesforce therefore named as representative but contributes no operational evidence; no memory-filled claims.
- Zoho CRM forecasting — help KB (help.zoho.com portal) returned empty/JS-gated; zoho.com marketing paths 404; search engines unusable (DuckDuckGo timeout; Bing CN market ignored site: operator). Zoho dropped from the sample rather than evidenced from memory.
- Clari Knowledge Base (clari.my.site.com) — gated (inherited limitation from RI pass); Clari held at product-page scope.
- HubSpot Knowledge Base article URLs 404 on this date; HubSpot evidence rests on its official product page + FAQ.

---

## Product Observations

### Microsoft Dynamics 365 Sales Forecasting (Tier 1 — strongest operational evidence)

Evidence layer A unless noted:

- **Definition as shipped**: "forecasting gives teams a shared, near real-time view of expected revenue by combining pipeline activity, forecast categories, quotas, and hierarchy rollups." Forecasts help sellers track quota performance, managers coach on pipeline gaps, directors anticipate trends, leadership adjust projections for investors/stakeholders.
- **The forecast is a configured, activated object**: under App Settings > Performance management > Forecast configuration. Configuration steps: select a template (e.g., Org chart forecast / Territory forecast) → define and schedule a forecast model → provide access permissions → configure columns and layouts → configure and manage drill-down entities → advanced settings → activate the forecast and upload data. Forecast based on **revenue or quantity** (forecast type). A ready-made Sample Forecast can be activated for experimentation.
- **Out-of-the-box forecast**: every user gets an unconfigurable current-month forecast with zero setup (org-chart template, opportunity as rollup entity, near real-time, quota = previous month's won amount, max 50,000 records, not saved). Contrast table with configured forecasts: saved for several forecast periods and viewable anytime; custom rollup entity; permission-gated; updated every 24h or manual recalculate; custom quota values. → Evidence that (a) the minimal core needs no AI, no heavy config; (b) history/saved periods are a configured maturity step.
- **The forecast grid**: rows = users in the hierarchy (Manager field), expandable to direct reports' rolled-up forecasts; totals "aggregated by user or by territory, at each level of the hierarchy and for each period." Default columns: **Quota** (target per owner per period), **Committed** (revenue from high-confidence opportunities — forecast category Committed), **Best Case** (medium confidence), **Pipeline** (early-stage), **Omitted** (excluded from forecast), **Won** (closed-won actuals), **Lost** (closed-lost). Guidance per column (e.g., "Compare [Quota] with Committed to see the gap that needs to be closed").
- **Hierarchy attachment**: "Every forecast is attached to an organization-defined hierarchy that rolls up the values level by level." Org chart template → User.Manager field; Territory template → Territory manager lookup. Manager sees own + direct reports' roll-ups; expansion shows rolled-up forecasts.
- **Adjustments**: "An adjustment provides sales managers or sellers the ability to estimate the final amount that they expect for a forecast's opportunities to bring in at the close of the forecast period." Sales managers can adjust their own or a direct report's forecast; changes roll up to the parent record and up the hierarchy. Adjustment types: **Direct Adjustment** (edit a specific cell, revertible), **Indirect Adjustment** (propagated from above, visible in History), **Calculated value** (system-computed with no adjustments). Editable columns configured via "Allow adjustments". Cannot adjust above your level. Notes attached; History tab; Reset/rollback with recorded reason. Guidance: adjust for knowledge not yet in the system (verbal commitment, paused deal); do NOT adjust to mask stale opportunities — update the opportunity or close it Lost.
- **Currency/recalculation mechanics**: "Last updated" timestamp; immediate recalculation for adjustments and Forecast-page record changes; manual Recalculate after changing underlying opportunities or the hierarchy; multi-currency real-time conversion (administrator/forecast-manager enabled).
- **Quota handling**: quota uploaded via Excel template per owner per period; quota is a column compared against Committed/Won.
- **AI posture**: basic forecasting vs "premium forecasting" (predictive forecasting under Dynamics 365 AI for Sales — "Analyze revenue outcome by using predictive forecasting") documented as a separate, premium layer. → AI is optional add-on, not core. (Layer A for the split; premium-forecast page itself not fetched.)
- **Scope/legal notes**: not supported on mobile or GCC; feature "isn't intended for use in making decisions that affect the employment of an employee... including compensation, rewards, seniority" (product-specific legal framing). Forecast API (msdyn_ForecastApi) exists for programmatic access.
- Sharing: forecast owner can share view/adjust access with colleagues outside the natural hierarchy.

### HubSpot Forecasting (Tier 2 — official product page + FAQ)

- Positioning: "Sales forecasting software that turns pipeline data into reliable revenue predictions so you consistently hit your quarterly targets"; "Eliminate spreadsheet forecasting with an easy-to-use projection interface."
- Use framing: "checking progress toward your goal, estimating where you'll end up this quarter, or looking for a home base for your one-on-one meetings."
- **Customizable forecast categories and models**; forecast permissions ("Maintain control through forecast permissions, ensuring accurate submissions"); team **rollup view** by team with drill-down; **multiple pipelines** (sales revenue by month/quarter; service teams track renewals/upgrades in their own pipeline); forecast **reporting and analytics**: "forecast categories, weighted pipelines, historical snapshots, and customizable filters"; AI forecasting surfaces.
- FAQ (Layer A statements, official page):
  - Hierarchy: "The forecasting tool uses the team hierarchy set up in users and teams. This allows you to roll up deals and drill down through multiple levels of your team hierarchy without needing to change permissions."
  - Permissions: "team managers can update any of their sales reps' forecasts, but a rep can only edit their own" — i.e., submission/adjustment authority follows the hierarchy.
  - Beyond sales: services teams forecast their renewal pipeline "using the same forecast categories as your sales team."
  - Multiple forecast types: sales (monthly/quarterly revenue), service (renewals, upgrades, **ticket resolution times**), custom categories (enterprise vs SMB, new vs renewal), **goal templates** (meetings booked, tickets closed, response times) → non-revenue forecast objects exist.
  - Accuracy: "weighted pipeline calculations and customizable forecast categories help teams achieve reliable quarterly projections."
- Premium functionality lives in Sales Hub / Service Hub (module posture).

### Clari Forecast (Tier 2 — official product page; module of Clari platform)

- Nav positioning: "Forecast — Forecasting and pipeline management"; page: "Forecasting intelligence for every revenue model... helps revenue teams predict, manage, and fuel growth."
- "Automated forecast roll-ups. Get one-click visibility from top-line views to individual deals so teams can forecast faster, present confidently, and drive predictable results."
- "Scenario modeling"; reps get "clear insights, accurate projections"; "promote org-wide accountability."
- Revenue-model breadth claim: "the only forecasting solution built for every revenue model, including subscription and consumption — predict existing ARR, deal-based ARR, and usage-based ARR" (single-vendor claim; breadth itself corroborates the ARR/consumption variant axis).
- Integrations: Salesforce + Microsoft Excel, SQL Server, PostgreSQL, Databricks (data-plane reach beyond CRM).
- Marketing claims (accuracy %, customer counts) recorded but NOT promoted (single-vendor marketing figures).

### Aviso (Tier 2 — official platform root + Revenue Forecasting product page)

- "Revenue Forecasting — Commit with clarity. Get the flexibility to execute advanced forecasting models at your preferred cadence."
- "Aviso automatically rolls up your forecast across every rep, category, and team, complete with best case, most likely numbers and pacing against the number. And updates your forecast in real-time across all reports."
- Forecast meetings framing: "Conduct More Insightful Forecasting Meetings... Focus less on gathering data and more on guiding reps to de-risk deals and make stronger commits during meetings."
- **Winscore Explanations**: "go beyond basic CRM scoring by incorporating CRM data, multi-channel engagement, conversations, and historical deal trends"; "Toggle deals in and out of commits in 1 click based on deal score. Spot upside and pull-in deals to replace at-risk deals." → human judgment exercised as deal-level commit composition, atop AI-computed numbers.
- **Consumption forecasting**: "Translate Product Consumption Into ARR/MRR... combine consumption forecasting with traditional revenue forecasting models."
- Mobile: "Run Forecast Calls And Deal Reviews From Your Car" — drill down to direct reports from mobile.
- Data: bidirectional Salesforce sync; "Unifies data from multiple CRM instances and data lakes."
- Note: Aviso also carries conversation/relationship intelligence etc. (platform breadth) — same as RI-pass observation; here only the forecasting machinery is the object of study.

### Salesforce Forecasting (named representative — no direct evidence)

- Market-canonical CRM-native forecasting module. Official docs unreachable from this environment (JS-gated help; 403 developer docs). No operational claims drawn anywhere in this research. Market-structure corroboration only: competing/complementary products (HubSpot, Clari, Aviso) position against CRM-native forecasting and spreadsheets generically, not against Salesforce specifics.

---

## Cross-product Comparison

| Dimension | Dynamics 365 | HubSpot | Clari | Aviso | Evidence |
|---|---|---|---|---|---|
| Realization posture | CRM-native module (configured feature) | CRM-native module (Hub in which it's premium) | Standalone platform over CRM | Standalone platform over CRM | A (Dynamics, HubSpot premium tiers) / A-page (Clari, Aviso) |
| Primary object | The forecast: configured, per-period, per-hierarchy record with category columns | The forecast: per-pipeline, per-period projection view with rollups | The forecast roll-up: top-line → deal drill-down, per revenue model | The forecast number: auto-rolled-up per rep/category/team with pacing | A/B |
| Data source | Own CRM opportunities (rollup entity configurable) | Own CRM deals, multiple pipelines | Salesforce + warehouses/databases | Salesforce bidirectional + multiple CRMs/data lakes | A (Dynamics) / A-page (rest) |
| Period structure | Forecast periods configured (default current; OOTB = current month only); periods selectable in dropdown | Monthly/quarterly views | Quarter cadence (implied by accuracy-by-week-2 claims) — held at positioning strength | "Your preferred cadence" — configurable | A (Dynamics) / B (period-boundedness across all) |
| Category structure | Committed / Best Case / Pipeline / Omitted + Won + Lost columns | Customizable forecast categories | Commit/best-case/pipeline language (category machinery implied by roll-up + RI-pass module docs) | Best case, most likely + pacing against the number | A (Dynamics explicit) / B (confidence-category structure across sample) |
| Hierarchy roll-up | Org-chart (User.Manager) or Territory template; level-by-level aggregation | Team hierarchy from users/teams; rollup + multi-level drill-down | Automated roll-ups, top-line views | Rolls up across every rep, category, and team | A (Dynamics, HubSpot) / A-page (Clari, Aviso) |
| Quota/target comparison | Quota column + Excel quota upload; "compare with Committed to see the gap" | Goal templates; progress toward goal | Targets/pacing (RI-pass evidence: target columns) | "Pacing against the number" | A (Dynamics) / A-page (Aviso) / B |
| Human judgment entry | Adjustments (direct/indirect, notes, history, rollback); editable columns | Forecast submission permissions (managers update reps' forecasts) | Submission/adjustment machinery (per RI-pass Gong/Clari docs) | Toggle deals in/out of commits; stronger commits | A (Dynamics, HubSpot) / B (judgment layer universal) |
| Machine projection | Premium predictive forecasting as separate add-on | AI forecasting surfaces; weighted pipeline | AI-powered insights core to pitch | AI models core ("advanced forecasting models", Winscore) | A (Dynamics split) / A-page (rest) → AI is optional layer, L2 |
| Drill-down to deals | "View and manage underlying opportunities" | Drill into team performance | "One-click visibility from top-line views to individual deals" | Drill down to direct reports; Winscore per deal | A/B — near-universal |
| Forecast history / snapshots | Configured forecasts "saved for several forecast periods and can be viewed anytime"; OOTB not saved | Historical snapshots | Snapshotting/time-series (RevDB, RI-pass) | Real-time updates across reports (history strength not evidenced) | A (Dynamics) / A-page (HubSpot) / B |
| Multiple simultaneous forecasts | Dropdown of multiple configured forecasts | Multiple pipelines; separate forecast types | Multi revenue models (subscription/consumption/usage ARR) | Consumption + traditional combined | A/B |
| Currency handling | Multi-currency real-time conversion | Not evidenced | Not evidenced | Not evidenced | product-specific (A-Dynamics) |
| Mobile | Explicitly NOT supported | Not evidenced | Not evidenced | Mobile forecasting flagship | variance evidence — NOT definitional |
| Sharing/permissions | Forecast-level permissions; share view/adjust | Forecast visibility + submission permissions | Enterprise readiness posture | Not evidenced | A (Dynamics, HubSpot) / B |
| Finance handoff | Not evidenced | Not evidenced | Warehouse/data-plane integrations (Excel/SQL/PostgreSQL/Databricks) | CFO-spend-reduction customer quote | B/L2 |

## L0 / L1 / L2 / L3 abstraction

### L0 — Defining Invariant

Minimal structure without which the product is not a Sales Forecasting Platform:

1. **The forecast as a managed record** — a quantified projection of revenue (or a countable measure) for a defined future period, held in the system as a named, revisitable object rather than a one-off calculation. The period structure inherently carries two anchors: revenue already won in the period (closed actuals) and the projection of the remainder. (Remove → a pipeline report or revenue dashboard, not a forecast.)
2. **Pipeline-derived projection** — the projection is computed from the sales organization's own in-flight deal data (amount, expected close date, stage/confidence) plus human judgment applied to that data, rather than from a finance-owned planning model. (Remove → finance-side revenue projection inside a planning model = Budgeting & Forecasting / FP&A Type.)
3. **Organizational roll-up** — forecast values aggregate through the sales organization's defined hierarchy (management chain or territory structure), each level's number attributable to its owner, so the top-line number is composed of accountable sub-numbers. (Remove → an individual rep's personal deal-projection widget, not an organizational forecasting system.)
4. **Recurring restatement with retained history** — the forecast is restated as the period progresses (recalculated from changing deals and/or re-committed by people), and prior statements are retained as the record against which accuracy and movement are read. (Remove → a one-time projection calculator or static report.)

Four invariants. Everything else is capability or variant.

### L1 — Common Mature Structure (across the sample; not definitional)

- **Confidence forecast categories** distinguishing committed judgment from upside: commit / best case / pipeline ladder plus an omitted/excluded state — near-universal across sampled products (Dynamics explicit; HubSpot customizable categories; Clari/Aviso category language), but a minimal single-number forecast still satisfies L0, so categories stay L1.
- **Quota/target comparison** — targets as columns/values, gap-to-goal and pacing views; quota is consumed as input (the sibling Quota Management Type owns its definition and allocation).
- **Manager adjustments/overrides with audit** — managers correct or override computed values within their span; notes, history, rollback; subordinates' values propagate upward.
- **Drill-down from any aggregate to its composing deals** — the number and its underlying opportunities are never separated.
- **Multiple simultaneous forecasts** — lines of business (new business vs renewals), regions, product lines, revenue vs quantity vs custom measures.
- **Forecast-vs-actual analytics** — restatement history, attainment trends, per-rep views feeding 1:1s and forecast calls.
- **CRM integration spine** — native module reading the suite's own CRM, or sync with external CRMs; data-plane extensions (warehouses) at the enterprise pole.
- **Permissions aligned to hierarchy** — who sees which numbers, who may adjust whose forecast.
- **Sharing and exports** — sharing forecasts with non-hierarchy colleagues, report/dashboard export; finance handoff at some poles.

### L2 — Variant / Optional Structure

- **AI/predictive projection** — from none (Dynamics basic) to premium add-on (Dynamics premium; HubSpot AI surfaces) to AI-native core (Aviso, Clari positioning). Deliberately NOT definitional — Microsoft's own basic/premium split documents the optionality.
- **Delivery posture** — CRM-native module vs standalone platform over CRM vs analytics-suite module (market's dominant packaging axis).
- **Projection philosophy** — human-submission-first (submit a number) vs adjustment-of-computed-values vs AI-first (toggle deals into commits atop machine numbers).
- **Revenue model** — deal/bookings-based vs subscription/ARR vs consumption/usage forecasting; combined models.
- **Hierarchy type** — org-chart (manager field) vs territory-based; multi-currency for regional orgs.
- **Forecast object type** — revenue vs quantity vs non-revenue measures (one product's goal templates forecast meetings booked / tickets closed / resolution times).
- **Surfaces** — web grids universal; mobile apps and conversational AI present in some products, absent in others (Dynamics explicitly not on mobile).
- **Scale tier** — SMB CRM widget to enterprise platform with data-warehouse reach.

### L3 — Vendor-specific (Research Notes only)

- Dynamics: OOTB-vs-configured forecast contrast table (50,000-record limit, 24h refresh, quota-from-previous-month on OOTB); adjustment taxonomy (Direct/Indirect/Calculated); "not supported on mobile/GCC"; "not intended for employment decisions" legal note; msdyn_ForecastApi; Excel quota template; sample forecast; forecast naming ("My FY2024 February forecast").
- HubSpot: goal templates (meetings booked, tickets closed, response times); service-team renewal forecasting with shared categories; premium-tier gating.
- Clari: "98% forecast accuracy by week two", "75,000+ teams", "12x" accuracy-boost claims (marketing figures — rejected from canonical text); Excel/SQL Server/PostgreSQL/Databricks integration strip; Salesloft merger banner.
- Aviso: Winscore branding; "nearly 100% accuracy" headline; 450+ revenue teams; MIKI assistant; "save 30% CRM spend" customer claim; 13-week cadences (RI-pass).
- Salesforce: no operational facts recorded (docs unreachable).

---

## Rejected Findings (considered and NOT promoted)

- **AI/ML projection as definitional**: the strongest anti-example is within-sample — Dynamics ships forecasting without AI and documents predictive forecasting as a premium add-on; HubSpot leads with categories/rollups and treats AI as a surface. → L2.
- **The exact commit/best-case/pipeline ladder as definitional**: universal in the sample but implementation-specific; a single-number forecast satisfies L0-1. → L1 with the ladder as the common realization.
- **"Weekly cadence" as fixed rhythm**: cadence is configurable ("your preferred cadence" — Aviso; scheduling in Dynamics forecast model config). → L1, phrased as recurring.
- **Quota machinery inside the definition**: quota is the sibling Type's object; forecasting consumes it as a column/input. Dynamics works without uploaded quotas (OOTB derives from last month's won). → L1.
- **Spreadsheet-import/export as definitional**: interface detail. → L1/L2.
- **Multi-currency, mobile, AI assistants**: variance evidence only.
- **Accuracy-percentage claims** ("98%", "nearly 100%"): single-vendor marketing. → rejected entirely from canonical text.
- **"Pipeline management" as part of the definition**: Clari's nav says "Forecasting and pipeline management" — pipeline inspection is adjacent capability; the Type's object is the projection, not deal progression.

## Historical / Market-Sample Check

- Test products of earlier eras:
  - **Spreadsheet roll-ups** (manager collects reps' numbers weekly, sums them, saves the week's sheet): satisfies L0-1 (period projection, won-vs-remaining), L0-2 (the org's deal data, hand-maintained), L0-3 (management hierarchy), L0-4 (weekly restatement, retained sheets). The market's own positioning confirms this is the baseline being replaced: HubSpot "eliminate spreadsheet forecasting", Aviso "without the spreadsheet struggle". The spreadsheet era is the practice this Type digitizes — not an earlier form of a different Type.
  - **Pre-AI CRM forecast modules** (Dynamics basic forecasting; older CRM "expected revenue" roll-ups): satisfy all four invariants with no AI. Microsoft's own documentation of basic vs premium-predictive forecasting is direct within-sample evidence that the Type predates and stands without AI.
  - **Whiteboard/verbal commit culture with a written number**: satisfies the practice structurally; the software Type is its system-of-record realization — consistent with L0-4 ("retained record").
- Counter-check for over-fitting: L0 does not require CRM integration per se (the invariant is *pipeline-derived data* — in principle any maintained deal list), does not require AI, categories, quotas, cloud delivery, or any specific surface. A future product forecasting from different deal-data sources still fits.
- Regional check: nothing in the sampled realization is US-specific; multi-currency handling (Dynamics) and territory hierarchies indicate regional fitness. Quota-upload formats are implementation detail.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove what → becomes the other" test) |
|---|---|---|
| Revenue Intelligence Platform | ratified seam (resolves the RI pass's joint-review flag) | Adopted discriminator confirmed by this pass's evidence: **Revenue Intelligence Platform = captured-engagement data foundation + deal/pipeline inspection + projection together** (an insight layer that *observes* selling activity); **Sales Forecasting Platform = forecast production/roll-up as the primary object on CRM pipeline data, without a captured-engagement foundation**. Every forecasting-side realization in this sample (Dynamics, HubSpot) carries no captured-engagement machinery in its forecasting feature; the two vendors that do (Clari, Aviso) sell forecasting as a module of a wider platform and are sampled here at forecasting-module scope. A forecasting tool without captured engagement is this Type; a platform whose defining part is the captured-engagement foundation + inspection + projection is RI. The seam is genuinely blurred at module level (RI vendors ship forecasting modules; both documents cross-reference). |
| Customer Relationship Management / CRM | host/record vs forecast machinery | The CRM owns deals, contacts, accounts and runs the selling workflow; forecasting reads deal data and produces the projection + commit cadence. Remove the forecast record/roll-up/restatement → what remains is the CRM (indeed, the dominant delivery posture is the forecast module *inside* the CRM). Remove deal/contact record ownership → a forecasting platform that must sync to a CRM. |
| Quota Management | target vs prediction (held clean, consistent with the quota pass) | Quota Management's defining object is the target itself and its allocation machinery across the org; forecasting's object is the projection. Quota enters forecasting as an input column (quota per owner per period; gap/pacing views) — remove quota and forecasting still fully functions (Dynamics OOTB works without uploaded quotas). Forecasting enters quota management only as attainment context. |
| Budgeting & Forecasting Platform / Financial Planning & Analysis (§08) | resolves the §08 passes' secondary flag | Both project revenue, but the **data source, owning function, and cadence differ**: FP&A projects inside a governed financial planning model (accounts × time × organizational segments), owned by finance, on an annual/quarterly planning cycle with versioned plan data; Sales Forecasting projects from the sales-owned deal pipeline, operated by the sales org, restated in-period (weekly-class cadence) on CRM data. Sales/quota planning modules inside budgeting platforms (e.g., sales planning apps in EPM suites) straddle the seam: where the object is quota/target allocation over the planning model → Quota Management/FP&A side; where the object is the in-period pipeline projection → this Type. Finance handoff (forecast → finance model) is an integration seam, not a merger. |
| Sales Pipeline Management | progression vs projection | Pipeline management concerns running the deal flow as a process (creation, stages, hygiene, coverage); forecasting concerns projecting the outcome and committing to a number. Forecast views appear inside pipeline tools and pipeline inspection inside forecasting tools; the primary object differs (the deal flow vs the number). |
| Sales Performance Management / Sales Compensation | projection vs comp machinery | SPM owns quota planning, territories, and commission calculation (sibling passes). Sales Compensation computes pay from credited outcomes and consumes pipeline only for forward-earnings estimates. Forecasting produces the projected number; several products document it must not drive compensation decisions (Dynamics legal note — product-specific framing, kept in research notes). |
| Business Intelligence Platform | generic vs forecast-native | BI connects arbitrary sources to dashboards/analyses; it does not carry the forecast record semantics — periods with committed categories, hierarchy roll-up of accountable numbers, the restatement cadence, or the commit workflow. A BI layer can *display* exported forecast data; it cannot run the forecast. |
| Conversation Intelligence Platform | unrelated machinery | No direct relationship; conversation data enters forecasting only via revenue-intelligence platforms (L2 in RI), not in this Type's core. |

**Boundary Issues to record in STATUS.md:**

1. RESOLVES the revenue-intelligence-platform joint-review flag (from the RI side): ratified the adopted discriminator with forecasting-side evidence — CRM-native forecast modules and standalone forecasting platforms carry no captured-engagement foundation; forecast production/roll-up is their primary object. Two Types stand; RI document already cross-references. Residual note: at module level the market sells forecasting inside RI platforms; both documents treat that as packaging, not Type merger.
2. RESOLVES the budgeting-forecasting / financial-planning-analysis secondary flag (from the §08 side): the seam is held on data source (deal pipeline vs financial planning model), owning function (sales vs finance), and cadence (in-period restatement vs planning cycle); sales/quota planning modules inside budgeting platforms classified by object (quota allocation → quota/FP&A side; in-period pipeline projection → this side). Candidate outcome for taxonomy owner: keep all three as separate Types with cross-references (no product partition problem comparable to the FP&A/B&F umbrella case was observed — forecasting-side products are distinctly CRM-pipeline-native).

---

## Uncertainties

- Salesforce Forecasting: official documentation unreachable (help JS-gated; developer docs 403) — retained as named representative with zero operational claims; the CRM-native-enterprise evidence burden is carried by Dynamics.
- Clari and Aviso rest at Tier-2 (product pages): their submission/adjustment mechanics, period configuration, and history semantics are not directly documented here; category and cadence claims held at positioning strength (Clari's operational forecast mechanics are better evidenced in the RI pass via Gong docs, not Clari's own).
- HubSpot: evidence is the official product page + FAQ only; KB articles 404 on research date; submission workflow detail (vs permission statements) unverified.
- Whether any shipped product runs a purely machine-generated forecast with *no* human judgment layer at all is unconfirmed; all sampled products expose a judgment mechanism (submission, adjustment, or commit composition). L0-2 therefore phrases human judgment as part of the pipeline-derived input mix, and the "human commit" is treated as the Type's operating practice rather than a separate invariant.
- Forecast-accuracy analytics depth (beyond snapshots and history) varies and was only partially evidenced; kept generic.
- Pre-2020 products not directly researched (out of budget); the historical judgment rests on within-sample evidence (Dynamics basic-vs-premium split) and the market's own positioning against spreadsheets.

---

## Final Synthesis

A Sales Forecasting Platform is the sales organization's system of record for its projected revenue: a quantified projection for each coming period, derived from the organization's own in-flight deal data and the human judgment applied to it, aggregated level by level through the sales hierarchy into an accountable top-line number, restated on a recurring cadence as deals change and judgments firm up, retained as history, and read against quotas and closed actuals until the period resolves into fact. Its defining core is deliberately small — forecast record, pipeline-derived projection, hierarchy roll-up, recurring restatement — and is realized today most commonly as a forecast module inside CRM suites (the spreadsheet roll-up digitized) as well as standalone platforms that sync to the CRM. Machine prediction is an optional layer that raises the projection's sophistication without changing the structure: the number someone must stand behind remains the object.

Canonical object sketch:

```text
CRM of record (deals: amount · close date · stage/confidence · owner)
   │ read (native module or sync) + human judgment (submission / adjustment)
   ▼
FORECAST RECORD (per period, per forecast)
   ├── periods (month/quarter) with closed actuals (Won) as anchor
   ├── confidence categories (Committed / Best Case / Pipeline / Omitted — common, not definitional)
   ├── hierarchy roll-up: rep → manager → … → top line (org-chart or territory)
   ├── quota/target column + gap & pacing (input from Quota Management)
   └── restatement history (snapshots; accuracy vs actuals when the period closes)
   │
   ▼
Surfaces: forecast grid (rows = hierarchy) · period selector · deal drill-down ·
          adjustment dialog with notes/history · dashboards/reports · share/export ·
          (optional: predictive AI layer, mobile, conversational surfaces)

People: rep (own number & deals) · manager (roll up, adjust, coach) ·
        director/executive (commit, board number) · RevOps/admin (configure) · finance (consumer)
Cadence: recurring restatement inside the period (weekly-class rhythm, configurable)
```
