# Research Notes — Renewal Management Platform

## Research Goal

Understand what a Renewal Management Platform actually is as an Application Type: what objects exist inside it, who operates it, how the renewal motion is executed and recorded, and where its boundary sits against Customer Success Platforms, Subscription Billing Platforms, CRM opportunity management, and Contract Lifecycle Management. The directory leaf sits in §07 Sales, Customer & Revenue between Customer Health Monitoring and Customer Training / Academy Platform.

## Initial Boundary

Working hypothesis before research:

- The Type is vendor-side: the operator is the company that sells the recurring product, managing renewals of its own customer base.
- The core object is the renewal event: an expiring recurring agreement (subscription/contract) with a decision date and an amount at stake.
- The system exists to make renewals deliberate rather than automatic: see them coming, assign ownership, work them ahead of the date, forecast the outcome, record the result.
- Likely confusion surfaces: Customer Success Platform (renewal modules inside CS suites), Subscription Billing (auto-renewal mechanics), CRM (renewals as opportunities), CLM (renewal of contracts generally).

## Research Questions

1. What is the unit of record — a renewal opportunity, a renewal event, a lifecycle status on the account, or a line in a revenue report?
2. What data anchors a renewal: contract/subscription, renewal due date, amount (which amount — up-for-renewal vs final), owner?
3. What outcomes are recorded and how (renewed / churned / upsell / downsell; churn reasons; close date vs due date)?
4. How does forecasting work (forecast categories, probability, period, ML health-based predictions, GRR/NRR-style metrics)?
5. What execution machinery exists (playbooks, CTAs/tasks, campaigns, reminder communications) and what triggers it (time-to-renewal, risk)?
6. How do renewal types differ (high-touch manual vs auto-renewal vs hybrid) and how does auto-renewal change the motion?
7. Which roles operate the system (renewal manager vs CSM vs sales leadership vs finance)?
8. How does the system relate to CRM and billing systems (two-way opportunity sync, billing amounts/dates as source)?
9. Where does the renewal decision end and the money execution begin (boundary vs billing)?
10. Historical check: do pre-SaaS renewal motions (license/maintenance renewals, any recurring B2B contract) fit the same structure?

## Representative Products

Selected for market representativeness, documentation quality, and different structural philosophies:

| Product | Philosophy / pole | Customer tier | Evidence tier |
|---|---|---|---|
| Gainsight (Renewal Center / "Renewals") | CS-platform add-on, CRM-opportunity-centric renewal forecasting (ML likelihood-to-renew) | Enterprise | Tier-1 official help docs (multiple pages) |
| Totango (Renewals SuccessBLOC + Revenue Center) | Lifecycle/engagement-centric renewals: types, roles, stages, plays; account-level forecast states | Mid-market→enterprise | Tier-1 official help docs (multiple articles) |
| ChurnZero (Renewal and Forecast Hub) | Reporting/forecast-workbook-centric renewals built on contractual-history table, health-score-integrated | Mid-market | Tier-1 help center (intro + glossary) + Tier-2 product page |
| Stripe Billing (boundary pole, not a renewal platform) | Billing-side pole: subscription lifecycle, auto-invoicing, dunning — what renewal management is NOT | All segments | Tier-1 official docs |

Salesforce renewal functionality was considered as a CRM-side pole but was not directly fetched (no reachable exact article); the CRM boundary is argued from Gainsight's and ChurnZero's documented Salesforce integrations plus ChurnZero's own "unlike a CRM" positioning. Zuora (billing-side) was dropped after two attempts against its JS-rendered documentation portal; Chargebee support search returned 404. Stripe Billing substitutes as the billing-side anchor.

## Sources

- Gainsight Help Center — Customer Success → Renewal Center (category), Renewal Center Overview, Renewal Center User Guide — https://support.gainsight.com/gainsight_nxt/Renewal_Center/01About/Renewal_Center_Overview , https://support.gainsight.com/gainsight_nxt/Renewal_Center/03User_Guides/Renewal_Center_User_Guide (fetched 2026-09-07)
- Totango Help Center — Renewals: SuccessBLOC Setup, Set revenue forecasts (+ search results for renewal-tag/segment practices) — https://support.totango.com/hc/en-us/articles/17369253780116-Renewals-SuccessBLOC-Setup , https://support.totango.com/hc/en-us/articles/14441057667860-Set-revenue-forecasts (fetched 2026-09-07)
- ChurnZero Help Center — Introducing Renewal and Forecast Hub, Glossary of Renewal Hub Terms; product page "Customer renewal forecasting" (Renewal Hub) — https://support.churnzero.com/hc/en-us/articles/13756401461773-Introducing-Renewal-and-Forecast-Hub , https://support.churnzero.com/hc/en-us/articles/13590394878349-Glossary-of-Renewal-Hub-Terms , https://churnzero.com/features/renewal-hub/ (fetched 2026-09-07)
- Stripe Docs — How subscriptions work — https://docs.stripe.com/billing/subscriptions/overview (fetched 2026-09-07)
- Not directly reachable: Zuora knowledge center (JS-rendered portal, 2 attempts), Chargebee support search (404), Salesforce renewal help article (no exact URL resolved)

## Product Observations

### Gainsight — Renewal Center (evidence layer A unless noted)

- Renewal Center is a licensed add-on to the Customer Success platform; renamed "Renewals" in end-user navigation. It is positioned as the tool for renewal teams to "deeply analyze and accurately forecast their renewal business."
- Core object: the renewal **Opportunity**. Data is imported from the Salesforce Opportunity object (RC Opportunity object mirrors Salesforce fields; data types must match). An admin configures field mappings, forecast tables, detail views, and filters. There is also a documented "Deploy Renewal Center Without Salesforce" path (A: documented as an admin guide; internals not fetched).
- The platform "enriches CRM data with a predictive customer health score to identify risky customers earlier." A Machine Learning algorithm produces a **likelihood-to-renew** score per open renewal opportunity, based on customer health measures, and learns from past business outcomes.
- Two main pages: **Analyze** (metrics + charts) and **Forecast** (renewal opportunity list).
  - Analyze metrics: **Renewals Due** (sum of renewal target amounts for all renewal opportunities), **Renewal forecast** (roll-up by configured forecast categories/probability methods), **Upsell forecast** (kept separate so Gross/Net Renewal rates stay meaningful), **Gainsight Forecast** (ML-based), **Gross Renewal Rate** ("percentage of opportunities renewed in the period"; excludes upsell), **Net Renewal Rate** ("rate at which customers are renewing and expanding").
  - Analyze charts: Renewals Due (by stage / forecast category), Forecast by Booking Type, Late Renewals (close date after renewal due date, bucketed in weeks), Churn Forecast (by configured churn reason), Renewal Waterfall (renewals due → lost → downsell → gross renewal → upsell → net renewal; actual + forecast), Renewals Due by Health (exposes misalignment between health and forecast category).
  - **Action Cards**: Potentially Missing Renewals (companies with upcoming renewal dates but *no renewal opportunity* — with an ADD action to create one), Overdue Unresolved Renewals (past due date, not closed), Potentially Late Renewals (accounts recently late), Opportunities Missing Forecast, High Churn Risk Renewals.
  - Actuals section: Renewals (final amount of won renewals), Churn (lost renewals + downsells), Upsell (upsell opportunities + renewals closed above target).
- Forecast page: list of renewal opportunities at opportunity and account level ("Company View" account-based forecasting); editable fields sync back to Salesforce and save only if Salesforce validation rules pass; users can add opportunities (name, stage, close date, owner required); product line items editable only in Gainsight-only sync mode; Scorecard (health) editable inline; Timeline activities creatable from the opportunity detail.
- Amount semantics: **Target Amount** vs **Forecast Amount** vs **Final Amount**; multi-year deals need opportunities created on anniversaries to appear in anniversary-period metrics (documented limitation).
- Forecasting performed at the Opportunity level, not product line items (documented limitation).
- Link opportunity to Cockpit **CTA** (work item): rules engine can identify opportunities needing action and create/attach CTAs automatically; CSMs can link/add opportunities to CTAs.
- License tiers: Viewer+Analytics license gets read-only Analyze access without Forecast page; full access requires upgrade. Global filters support viewing a team's book of business; custom fiscal periods supported.

### Totango — Renewals SuccessBLOC + Revenue Center (evidence layer A)

- Renewal management is delivered as a **SuccessBLOC** (a packaged program: segments, canvas, SuccessPlays, campaigns) plus revenue analytics in **Revenue Center**.
- Setup article defines three **renewal types** that shape the whole motion (A: explicit vendor taxonomy):
  - **High Touch**: "No contractual mechanism for a renewal beyond the expiration date. Requires a manual renewal process" — typically strategic accounts over a certain contract value; examples: long-term contract expiration, auto renewal that has "opted out", first-year pilot deals.
  - **Auto**: "Standard auto renewal language, which allows for the renewal of said agreement without the execution of new paperwork. Auto renewals typically have opt out periods"; notes rising re-paper likelihood as agreements age.
  - **Hybrid/Digital**: digitally alert the customer that a renewal is upcoming; based on renewal intent, a Renewal Manager takes action. Requires one renewal event (account), one internal owner, and at least one customer contact.
- **Renewal roles** (A): Renewal Manager (main POC for high-touch renewals; maintains contract drive, project-manages renewal events per cycle, identifies focus accounts, partners with CSM on value/ROI story and renewal risk, point person on negotiations, drafts renewal order forms, liaises with finance); CSM (value/adoption, keeps RM updated on risk, schedules the renewal discussion); Account Manager (supports business reviews); Service Delivery Manager (non-CSM accounts); Accounting/Finance (billing questions).
- **Renewal stages** as a lifecycle status attribute (A): Pre-renewal → Negotiation → Renewal Risks → Closed-Won / Closed-Lost, with per-type stage activities (proposal prep, contract prep, overdue renewal, upcoming renewal at risk / in poor health, missed payment reminder, celebration, post-mortem, win-back). Stages trigger related SuccessPlays and communications; time-in-stage is tracked for KPIs (clock stops at end stage).
- Automation examples (A): trigger SuccessPlay 90 days out to review the account for renewal barriers before the automated "Upcoming renewal reminder" email; risk plays engage executive sponsor and sales/AM to build a save plan.
- Renewal-risk practice example (A, vendor-published example, not a platform constant): a "renewal-risk" tag defined as paying customers with a renewal date in the next 90 days.
- Best practices (A): use the native Salesforce connector; each account (opportunity) must have one owner managing the process across all products (consolidated opportunity); **co-term contracts** to avoid over-communicating; align process across regions.
- **Revenue Center / forecast states** (A): a forecast state documents the expected change on the account: **Upsell** (expected increase to contract value), **Renewal** (no change expected), **Downgrade** (expected decrease), **Churn** (paying status to canceled). A **forecast period** (monthly/quarterly) says when the change is expected. Once the period closes, the forecast state is permanently captured for that period; forecasts cannot be set retroactively; an account has one forecast state at a time; forecasts can be set for current or future periods.
- **Renewable account** classification (A): an account is renewable for a period when its contract start date (or create date) is before the period AND its contract renewal date falls within the period. Accounts missing a forecast get visible "forecast needed" prompts on the profile and in Revenue Center.
- Suggested forecasts based on recent poor-health days can appear (A: feature observed in the article's walkthrough).
- Release notes observed in search: business definitions for risk, renewal date, and renewal window are configurable (A: configuration surface exists; details not fetched).

### ChurnZero — Renewal and Forecast Hub (evidence layer A; product page = A/Tier-2)

- Delivered as a reporting-and-workbook module: "purpose-built revenue reporting that empowers your team to confidently forecast, consistently renew, and proactively expand at scale."
- Renewal reports are built by admins on a single **controlling table** capturing "customers' contractual history" — the source of all renewal, upsell, downsell, and forecast data. Configuration sections: Report Details, Renewals, Upsells, Downsells, Actuals Categories, Forecast Categories, Churn Reasons.
- Renewal definition (A, glossary): "a decision tied to contractual dates. It is the revenue the company is charged with renewing and what they ultimately manage to retain."
- Amount/date fields (A): **Up for Renewal Amount** (total that could/should be renewed; recurring dollars only), **Renewal Amount** (expected/actual renewed), **Renewal Due Date** ("the date by which the renewal should be decided"), **Renewal Close Date** ("the date on which the renewal was decided. ChurnZero does not track this automatically, so you have an explicit field").
- Status/timing semantics (A): Open (due today/future) vs Overdue (due in past) while open; once closed: **Early Decision** (close before due), **On-Time Decision** (equal), **Late Decision** (close after due). Outcome semantics vs Up-for-Renewal Amount: **Renewed with No Change** (equal), **Renewed with Upsell** (greater), **Renewed with Downsell** (less).
- Mid-term expansions/contractions ("upsell and downsells … OUTSIDE of a renewal event") are tracked as separate decision records with their own amounts and close/start dates (A).
- Forecast vs actuals (A): forecast includes open + closed records — for open records, expected amount × assigned probability, combined with actuals; actuals include only closed records (won or lost, per configured closed-won/closed-lost definitions).
- Permission gating (A): all users can view/export active renewal reports; only users with the "Renewal Hub" permission can create/edit/delete renewal reports.
- Workbook tab (A): interactive view to review grouped data, filter, and "take action on individual or multiple records."
- Health integration (A): report can integrate ChurnScores into forecast reporting; ChurnScores "calculate the likelihood that your customer is going to renew" (help center). Product page: "Unlike a CRM, its analytics incorporate ChurnZero's health scores for greater accuracy" (vendor positioning, Tier-2).
- CRM integration (A): CRM account fields (e.g., Salesforce `Renewal_Date__c`) map to "Next Renewal Date" in ChurnZero; renewal reports can be shared to Salesforce. Product page claims CRM sync every 15 minutes (vendor claim, not verified).
- Forecast categories customizable; forecast-vs-actual comparisons for NRR/GRR, upsells, downsells; review by week/month/quarter/year; drill-down to individual opportunities (product page, Tier-2).

### Stripe Billing — billing-side boundary pole (evidence layer A)

- A subscription "moves through a predictable set of states" managed by the billing platform: statuses (trialing, active, incomplete, incomplete_expired, past_due, canceled, unpaid, paused), automatic invoice generation per billing cycle, payment retry/dunning ("smart retries"), cancellation (immediate or end of cycle), entitlements provisioning.
- The billing layer executes the money mechanics of recurring revenue automatically — including renewal-period billing — but contains no commercial renewal motion: no renewal owners, no forecast categories, no renewal outcomes taxonomy, no churn reasons, no plays/tasks to secure a decision. Renewal as a *decision* is simply not an object here; the closest concepts are price changes and cancellation.
- This confirms the boundary: auto-renewal execution is billing machinery; renewal management governs the human/commercial decision layered around the expiry.

## Cross-product Comparison

| Dimension | Gainsight | Totango | ChurnZero | Stripe Billing (pole) |
|---|---|---|---|---|
| Unit of record | Renewal Opportunity (synced with CRM) | Renewal event on account + lifecycle stages + forecast state | Renewal/upsell/downsell records in a contractual-history "controlling table" | Subscription object (no renewal decision object) |
| Date anchor | Renewal due date / close date on opportunity | Contract renewal date on account; stage transitions | Renewal Due Date + explicit Renewal Close Date | Billing period boundaries (automatic) |
| Amount anchor | Target / Forecast / Final Amount on opportunity | Contract value; expected new value for up/down | Up for Renewal Amount vs Renewal Amount (recurring only) | Invoice amounts (automatic) |
| Outcomes | Closed won/lost; churn reasons; upsell separate | Closed-Won/Closed-Lost stages; forecast states Renewal/Upsell/Downgrade/Churn | Renewed No Change / with Upsell / with Downsell; churn reasons | canceled / active (no decision semantics) |
| Forecast | Category/probability roll-up + ML likelihood-to-renew; GRR/NRR | Forecast states per account per period; Revenue Center roll-ups | Amount × probability over open + closed; NRR/GRR comparisons | — |
| Risk context | Health scorecard + ML; renewals-due-by-health chart | Health profiles; poor-health-based suggested forecasts; renewal-risk segments | ChurnScores integrated into reports | — |
| Work machinery | Cockpit CTAs linked to opportunities; Rules Engine | SuccessPlays + campaigns per stage; time triggers (e.g., 90-day pre-renewal) | Workbook actions on records; journeys with renewal-preparation steps | — |
| Renewal types | Opportunity-driven (manual motion; auto handled upstream) | High Touch / Auto / Hybrid taxonomy | Decision records regardless of type | Auto-execution only |
| CRM relation | Two-way Salesforce opportunity sync w/ validation; without-Salesforce mode possible | Native Salesforce connector; consolidated opportunity per account | CRM field mapping (renewal date); share reports to Salesforce; "unlike a CRM" positioning | — |
| Governance | License tiers (Viewer+Analytics vs full); editable-field config | Plan/permission framing; stage config in Data Modeler | "Renewal Hub" permission gates report creation | — |

### Evidence-layer B (cross-product commonality)

- Every renewal-management implementation centers a **dated renewal decision** on a recurring agreement: a due/decision date distinct from the close date, with an amount of recurring revenue at stake.
- Every implementation records **outcomes with an amount dimension**: renewed at same / more / less / lost, with configurable churn reasons; mid-term upsell/downsell tracked as sibling decisions.
- Every implementation maintains a **forward view**: pipeline/forecast roll-ups (category/probability or per-account states) and retention metrics (GRR/NRR style).
- Every implementation **feeds risk context into prioritization**: health scores / ML likelihood-to-renew aligned against renewal timing.
- Every implementation has **action machinery** ahead of the date: plays/tasks/CTAs/workbooks, time-triggered reminders and risk plays.
- Every implementation is **anchored to external systems of record**: CRM (opportunity/renewal-date sync) and billing (amounts, contract dates).

### Evidence-layer C (canonical inference)

The renewal is conceptualized consistently as a **decision the vendor must secure before the recurring agreement lapses** — the sample's own words ("a decision tied to contractual dates", "the date by which the renewal should be decided"). The Application Type is therefore best modeled as the management layer around that decision: renewal events as managed records, an outcome taxonomy, a forward-looking pipeline/forecast of the renewal book, and machinery to work each renewal ahead of its date — deliberately sitting between CRM (which holds generic opportunities), billing (which executes money), and customer success (which manages the relationship).

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

1. **Renewal events as managed records**: each identified customer's recurring agreement contributes a renewal record binding customer × recurring amount at stake × decision date (the date by which renewal must be secured).
2. **Recorded renewal outcomes**: the renewal is closed with an outcome (retained vs lost) and an amount result (same / more / less), producing the system of record for what the renewal book actually did.
3. **Forward-looking renewal book**: the set of upcoming renewals is visible as a whole (what is due, when, for how much, owned by whom) — the "manage" in the Type name.
4. **Pre-decision motion**: machinery that drives work on each renewal ahead of its decision date (ownership, tasks/plays/reminders, risk flags) — without this it is a billing report, not renewal management.

Remove #1/#2 → it is a CRM report. Remove #3/#4 → it is billing/history reporting. Remove the recurring-agreement anchor → it is generic pipeline management.

### L1 — Common Mature Structure

- Renewal pipeline & forecast machinery: forecast categories, probability weighting (expected amount × probability), target vs forecast vs final amounts, period-scoped roll-ups
- Retention metrics: gross renewal / net renewal style rates; renewal waterfall (due → lost → downsell → gross → upsell → net)
- Outcome analytics: churn reasons, late-renewal measurement (close vs due), actuals vs forecast review
- Risk integration: health scores, ML/data-science likelihood-to-renew, health-vs-forecast misalignment views
- Action/play machinery: time-triggered pre-renewal plays (e.g., N-days-out review), risk-driven save plays, linkage of renewal records to work items
- CRM two-way synchronization (opportunity-level, with validation rules on write-back); billing data as source for amounts/dates
- Gap detection: accounts with renewal dates but no renewal record ("potentially missing renewals")
- Role structure: renewal owner distinct from relationship owner; manager/leader roll-ups; read-only analyst licenses
- Administrative configuration: field mappings, stages/forecast categories, churn-reason lists, custom fiscal periods, permission gating

### L2 — Variant / Optional Structure

- Renewal-type taxonomy (high-touch manual vs auto-renewal monitoring vs hybrid/digital) — explicit vendor taxonomy in one sample, structurally present elsewhere
- Renewal-stage lifecycle with time-in-stage KPIs (lifecycle-status implementation)
- Mid-term upsell/downsell tracked as first-class sibling decision records (vs folded into renewal opportunity)
- Quote/proposal/order-form generation for re-papered renewals; renewal negotiation support (documented as role duties in one sample; quote tooling lives in CPQ/CLM neighbors)
- Auto-renewal execution mechanics (notice windows, opt-out handling, automatic re-charges) — belong to billing; renewal management may monitor them
- Co-terming support, multi-currency, custom renewal windows/risk definitions, multi-year anniversary handling
- Executive dashboards (revenue center/team views), report sharing to CRM, AI suggestions (suggested forecasts, era-current)
- Deployment shape: CS-suite add-on module vs reporting module vs standalone — market structure, not structure of the Type

### L3 — Vendor-specific (research notes only)

- Gainsight: "Renewal Center" module name/add-on licensing, RC Opportunity object mirroring Salesforce, Viewer+Analytics license tier, Cockpit CTA linkage, Rules Engine auto-CTA creation, product-line-item read-only in Salesforce sync mode, multi-year anniversary limitation, "Renewals" nav renaming, Gainsight Forecast (ML) as a distinct metric, renewals-due-by-health chart.
- Totango: SuccessBLOC packaging (Marketplace "Manage Contract Renewals" / "Automate Renewals"), renewal types/roles/stages recommended tables, Risk Status attribute in Data Modeler, forecast-state permanence at period close, renewable-account formula (start before period AND renewal date in period), telescope-icon forecast UI, "renewal-risk" tag definition (90-day example), co-terming best practice, suggested forecasts from poor-health days.
- ChurnZero: "Renewal and Forecast Hub" naming, controlling-table architecture, Timing Categories (early/on-time/late decision), Aging Categories (custom buckets of days-late), "Renewal Hub" permission, Workbook tab, share-reports-to-Salesforce, ChurnScores 0–100 likelihood framing, 15-minute CRM sync claim, "unlike a CRM" positioning.
- Stripe: subscription status lattice, 23-hour incomplete window, smart retries, entitlements — billing machinery, documented only as the boundary contrast.

## Vendor-specific Findings

(See L3; none of these promoted to the canonical document except as neutral examples where structural.)

## Boundary Findings

- **vs Customer Success Platform** (sharpest seam; joint-review flag): all three sampled implementations ship renewal management *inside* CS platforms (Gainsight add-on, Totango SuccessBLOC, ChurnZero module). The test: the CS platform's center is the managed customer relationship (health, adoption, success plans, engagement at any time in the lifecycle); renewal management's center is the renewal decision event (dates, amounts, outcomes, forecast of the renewal book). Health/adoption data flows *into* renewal risk, but a CS platform without renewal-decision machinery would still be a CS platform, and a renewal tool needs no full CS stack. Because the module-convergence is so strong, this leaf risks being judged a module of Customer Success Platform; counter-evidence: vendors market renewals as separately licensed modules with distinct objects (opportunity/decision records, forecast categories) and dedicated renewal-manager roles exist as a job function. **Recorded as a boundary issue for joint review.**
- **vs Subscription Billing Platform**: billing executes recurring charging, auto-renewal continuation, dunning, cancellation (observed directly via Stripe's lifecycle docs). Renewal management manages the *commercial decision* and its pipeline; it does not invoice, retry payments, or enforce entitlements. The amount fields in renewal management are explicitly "recurring dollars at stake," not invoices. Auto-renewal execution mechanics (notice windows, re-charges) sit on the billing side.
- **vs CRM / Sales Pipeline Management (Opportunity Management)**: renewals often *are* opportunities in the CRM; renewal management layers renewal-specific structure on top: up-for-renewal vs final amount semantics, renewal due vs close dates, early/on-time/late timing semantics, renewal outcome taxonomy with churn reasons, GRR/NRR-style retention metrics, health-driven likelihood-to-renew, and renewal-specific action machinery. Gainsight syncs two-way with Salesforce opportunities; ChurnZero explicitly positions its hub as "unlike a CRM." A CRM without this renewal-specific structure does not manage the renewal book as such.
- **vs Contract Lifecycle Management**: CLM governs contract documents through their lifecycle for all contract types (creation, negotiation, execution, obligations, renewal/amendment). Renewal management is revenue-motion-centric and typically is not the contract-document system of record; it consumes contract terms (dates, amounts, auto-renew posture) as context. Totango's Renewal Manager "maintains contract drive" and "drafts renewal order forms" — document handling is peripheral, not central.
- **vs Customer Health Monitoring**: health monitoring produces risk signals; renewal management consumes them for prioritization and forecast. One renewal-specific distinction: health metrics misaligned with forecast categories are surfaced as a renewal-management concern (Gainsight's renewals-due-by-health view) — evidence of direction of consumption.
- **vs Customer Onboarding Platform**: pre-renewal (onboarding/value delivery) is upstream context; the renewal window is a distinct motion with its own object.
- **"去掉什么就变成另一个 Type" 判据**: remove the renewal-decision record + outcome taxonomy → CRM reporting; remove the pre-decision motion → billing/BI reporting; remove the recurring-agreement anchor (renewal dates/amounts) → generic opportunity management; remove the vendor-side posture → nothing left (customer-side renewal does not exist as a market surface; subscribers see cancellation flows, which belong to billing/retention machinery).

## Historical / Market-Sample Check (§24-style)

- Would pre-SaaS renewal motions fit the L0? Annual software license/maintenance renewals and support-contract renewals tracked in spreadsheets/CRM as renewal opportunities with due dates, owners, and won/lost outcomes: yes — the defining core (renewal records on recurring agreements + outcomes + forward book + pre-decision motion) holds without SaaS-specific concepts. Health scoring and ML likelihood-to-renew are era-current L1, not definitional.
- Regional/industry breadth: any recurring B2B agreement (maintenance contracts, service agreements) fits the abstract core; insurance policy renewals also fit the abstract pattern but live inside policy administration/broker systems — a different Type (boundary recorded).
- Auto-renewal-dominant consumer subscriptions (no human decision motion): fit billing, NOT renewal management — supporting the boundary, not the definition.
- Overfitting risk avoided: "ARR" and "SaaS" kept out of the defining core; the sample's vocabulary (recurring dollars, contract renewal date, decision date) generalizes.

## Uncertainties

- No standalone pure-play renewal platform was directly documented; the reachable sample shows renewal management as modules of CS platforms (Gainsight, ChurnZero, Totango) plus CRM-native renewal opportunities (not fetched). Market may contain standalone renewal products; their existence would not change L0 but affects the Variants section — kept generic there.
- Zuora's billing-side renewal mechanics (renewal orders, auto-renew settings) were not directly observed (JS-rendered portal); the billing boundary rests on Stripe Billing's documented lifecycle plus structural reasoning. Billing-side claims kept structural, no vendor-specific billing mechanics asserted.
- Salesforce's own renewal functionality was not fetched; the CRM boundary is argued from sampled vendors' documented CRM integrations and ChurnZero's positioning.
- Precise operational defaults (notice-period lengths, standard forecast windows, standard stage names) are deliberately not asserted; Totango's 90-day examples are vendor-published practices, reported as examples only.
- ChurnZero's "syncs with your CRM every 15 minutes" is a marketing-page claim (Tier-2), not independently verified; kept out of the final document's factual claims.

## Final Synthesis

A Renewal Management Platform is the vendor-side management layer around the renewal decision on the vendor's own recurring customer agreements. Its defining core is small: renewal records binding customer × recurring amount × decision date; recorded outcomes (retained/lost, amount result, churn reasons); a forward-looking renewal book (what is due, when, for how much, owned by whom); and pre-decision motion (ownership, plays/reminders, risk flags) that works each renewal before it lapses. Around that core, mature products add renewal pipelines and forecasts (probability-weighted, ML-health-informed), retention analytics (gross/net renewal, waterfalls, churn reasons, late-renewal measurement), CRM two-way sync, and configurable governance. The type sits deliberately between CRM (generic opportunities), billing (money execution incl. auto-renewal), and customer success (the ongoing relationship), and its strongest taxonomy risk is module-convergence with the Customer Success Platform — recorded as a boundary issue rather than resolved unilaterally.
