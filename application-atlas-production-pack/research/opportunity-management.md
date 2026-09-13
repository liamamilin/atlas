# Research Notes — Opportunity Management

## Research Goal

Understand what the market actually sells under the label "Opportunity Management", and resolve the two pre-hung family flags: (1) the sales-pipeline-management pass (2026-09-07) flagged a probable near-overlap and recommended **this pass decide keep-both vs merge**, proposing candidate discriminators (population/coverage machinery and stage-flow governance on the pipeline side vs deal-record lifecycle depth on the opportunity side); (2) the customer-relationship-management pass (2026-09-08) recorded opportunity-management as a "deal-only slice" sibling whose seam should be re-checked when processed.

## Initial Boundary

Working hypothesis at start: Opportunity Management is a sales-side application centered on the opportunity — the record of one specific potential sale. Immediate boundary awareness:

- **Sales Pipeline Management (§07 sibling, processed)** — its L0 already contains "the deal as managed unit (identified record of one specific potential sale — buyer context, value, expected close, owner — worked over time and ending in a recorded won/lost outcome with reason)". Any opportunity-management L0 risks being a subset.
- **Customer Relationship Management / CRM (§07 sibling, processed)** — its L0 leg 3 is "the managed commercial progression (deals/opportunities with value, owner, expected close moving through customer-defined pipeline stages toward closed-won/closed-lost)".
- **Sales Forecasting Platform (§07 sibling, processed)** — projection vs progression seam already drawn.
- **Homonyms** — "opportunity" appears in unrelated Types (Government Grants Management opportunities, Internal Talent Marketplace opportunities, Spend Analysis "opportunity identification"). Different objects entirely; the homonym is noted, not a boundary problem.

## Research Questions

1. What do products that lead with "opportunity management" actually manage — is there machinery beyond the deal record, stages, progression, and closure?
2. Is "opportunity" a distinct object from the pipeline Type's "deal", or the same object under a second name?
3. Does any sampled realization of "opportunity management" lack the staged pipeline or the population machinery? (If yes, a keep-both L0 becomes possible.)
4. Is there a load-bearing leg for opportunity management that the pipeline Type lacks — e.g., deal-record content depth (buyer roles, products/line items, quote linkage), record-quality/inspection governance, creation-path machinery?
5. Where does the label sit inside a vendor's own product taxonomy (does a vendor that sells "opportunity management" sell "pipeline management" separately)?
6. Would older / differently positioned products (1990s SFA-era opportunity modules, paper pipe books) still fit the candidate definition?

## Representative Products

Chosen for market representation + documentation completeness + different product philosophies + different customer levels:

- **Salesforce (Sales Cloud / Agentforce Sales)** — enterprise CRM-native; the origin point of "Opportunity" as the deal-object term; richest object model expected.
- **HubSpot (Sales Hub / deals)** — mid-market freemium; Tier-1 knowledge base reachable (proven in two prior passes).
- **Pipedrive** — SMB pipeline-first standalone CRM; leads the "deal management" label.
- **Clari (Inspect)** — the revenue-platform pole that names a product "Opportunity management and inspection"; overlay over an external CRM.
- **Microsoft Dynamics 365 Sales / Zoho CRM** — attempted for the enterprise-object and SMB-modular poles; unreachable (see Sources). Treated structurally, consistent with the CRM pass's treatment.

## Sources

Fetch date: **2026-09-08**.

- Salesforce — Sales Cloud / Agentforce Sales product page (modules: Activity Management, Lead Management, **Account and Opportunity Management**, Forecast Management, **Pipeline Management**, Reports & Dashboards, Workflow Automation, Quoting & Contract Approvals; Starter Suite bundle list). https://www.salesforce.com/products/sales-cloud/features/sales-pipeline-management/ — fetched (A).
- Salesforce — opportunity-management-specific marketing URL https://www.salesforce.com/sales/opportunity-management/ — 404.
- HubSpot Knowledge Base — "Set up and manage object pipelines" (last updated 2026-09-04). https://knowledge.hubspot.com/object-settings/set-up-and-customize-your-deal-pipelines-and-deal-stages — fetched (A, Tier 1).
- Pipedrive — "Deal management" product page incl. FAQs. https://www.pipedrive.com/en/products/sales/deal-management — fetched (A).
- Clari — "Inspect — Opportunity management and deal inspection" product page. https://www.clari.com/products/inspect/ — fetched on retry (first attempt timed out) (A).
- Microsoft Learn — Dataverse Opportunity entity reference attempts: /power-apps/developer/data-platform/reference/entities/opportunity (404), /dynamics365/customer-engagement/web-api/opportunity (404, twice with/without query) — **abandoned after 3 path failures**. Note: the CRM pass (2026-09-08) successfully fetched the sibling Account entity page at the same path pattern, so the limitation is URL-path-specific, not site-wide; no opportunity-entity claims are made.
- Salesforce Help / Zoho CRM docs — not attempted this pass (Salesforce Help 403 recorded by both prior sibling passes; Zoho 404×2 recorded by the CRM pass).
- Prior-pass internal evidence relied on: research/sales-pipeline-management.md and research/customer-relationship-management-crm.md (Tier-1 HubSpot + Dataverse observations, Pipedrive/Clari Tier-2 observations).

## Product A — Salesforce (Tier 2 product page; direct observation)

### Key observations

- "Opportunity Management" is a **named feature block of the CRM sales product** — listed as "Account and Opportunity Management": "Move deals forward faster with specific guidance for sellers throughout the sales process. Get deal-specific insights, build account plans, and easily unify opportunity and account data for a single customer profile."
- The same product page lists a **separate** feature block "Pipeline Management": "Maintain and manage pipeline in a single, consolidated view. Track changes over time with built-in charts. Focus on the most important deals with the help of AI and use deal insights to provide proactive coaching." — i.e., one vendor offers "opportunity management" and "pipeline management" as sibling feature labels over the same deal machinery (packaging blocks, not separate products).
- The entry bundle (Starter Suite, $25/user/mo) is sold as "**Lead, Account, Contact, and Opportunity Management**" — opportunity management is one of the four canonical CRM object modules.
- The Opportunity object anchors downstream artifacts: "Quoting and Contract Approvals — Close deals faster with standard and templated quotes **synced to sales opportunities**" (screenshot alt-text shows an opportunity's product upgrade, quote line items, create-PDF/email-quote actions).
- Activity Management: engagement activities are captured "directly in CRM" and "associated to the relevant leads, contacts, accounts, and **opportunities**" — the opportunity is one of the four association targets.
- Forecast Management block exists separately (forecast categories, "increased opportunity alert") — forecasting is its own feature, consistent with the forecasting-sibling seam.

## Product B — HubSpot (Tier 1 KB; direct observation)

### Key observations

- "Pipelines help visualize your processes through stages, which are steps that signal where a record is in a process. For example, create **deal pipelines to track revenue**, ticket pipelines to track customer issues, or listing pipelines to track for-sale properties." — the pipeline primitive is generic; deals are the revenue instance.
- Deals have a **default Sales Pipeline** whose stages each carry a probability; "Stage probability is used to determine the weighted amount shown in board view, which is calculated by multiplying the total amount in each stage by the stage probability." The default pipeline ships seven stages with fixed probabilities, from Appointment scheduled (20%) through Contract sent (90%) to Closed won (100%, Won) / Closed lost (0%, Lost). (Exact numbers recorded here as Tier-1 facts; kept out of the final document as vendor defaults.)
- "To ensure all sales reports, custom deal or revenue reports, and sales analytics tools process your deals correctly, you must include stages for both **Won and Lost** under Deal probability." — terminal states are structurally required for reporting correctness.
- **Stage gates**: "Conditional stage logic" shows and can **require** specific properties when a record is created in or moved to a stage ("If a property is required, users cannot create or update the record until they set a value for it") — record-quality machinery embedded in stage entry.
- **Pipeline rules** tab (control editing access, require approval), pipeline **automations**, **deal tags**, **pipeline access** scoping; a pipeline "can't [be deleted] if it contains records or is used in other HubSpot tools or integrations".
- Multiple pipelines per object; per-subscription pipeline limits (Free 0 custom / Starter 15 / Professional 100 / Enterprise 350 — vendor-precise, recorded here only).
- Objects with pipelines include Deals, Leads, Tickets, Orders, Appointments, Custom objects — the same machinery serves non-sales flows (variant evidence, not definitional).
- AI assistant (Breeze) can create an object pipeline (era-current capability).

## Product C — Pipedrive (Tier 2 product page; direct observation)

### Key observations

- "Deal management software helps companies prioritize, track and close the deals in their **sales pipeline**." The deal-management product page is structurally a tour of pipeline machinery: visualize pipeline, automation ("auto-create deals and move them along your pipeline"), insights, customizable process, forecast.
- **Label mixing, first-hand**: the page's own FAQ — "Sales deal management is the process of tracking and optimizing **sales opportunities** from initial contact to closure." And "Is Pipedrive CRM deal tracking software? Yes, Pipedrive is a CRM… that includes powerful deal-tracking features. The CRM helps businesses manage and monitor **sales opportunities** through every stage of the deal management process, from lead generation to closing deals." — one vendor uses deal/opportunity as synonyms within one page.
- FAQ enumerates a canonical stage set for "deal management" (prospecting → qualifying → reaching out → appointment → needs → presenting → negotiating → winning → aftersales) — stages are the substance of deal management.
- "Use Pipedrive's customizable CRM to add the pipelines, fields and stages you need to manage your deals effectively."
- LeadBooster add-on: "As you capture and qualify leads, you can **convert them to deals** in Pipedrive" — the lead→deal conversion seam.
- Self-identifies: "Pipedrive is a Web-based Sales CRM" (consistent with the CRM pass's observation).

## Product D — Clari Inspect (Tier 2 product page; direct observation)

### Key observations

- The product is literally named "**Inspect — Opportunity management and inspection**" / "Opportunity management and deal inspection": "Clari Inspect centralizes complex revenue data into one insight-rich dashboard for greater alignment and performance across your entire revenue operation."
- Value claims: "complete, real-time view of revenue… robust **inspection capabilities** enable teams to quickly visualize **deal health, identify gaps**, and execute with conviction"; "transforms scattered data into a unified view of your entire **book of business**, helping reps and managers spot risks and prioritize action without switching tools."
- "AI-driven **health scores and risk indicators**"; "Transition from **inspection to action** in seconds — connects data insights directly to revenue workflows, guiding reps to take the right actions."
- "Inspect the details that matter most to you… configure custom views"; customer quote frames Inspect as a better surface than Salesforce reports ("the Inspect tab feels more intuitive").
- "**Inspect seamlessly integrates with Salesforce** and other revenue-critical tools" — overlay posture over an external CRM of record confirmed.
- Vendor's own product tree separates: Inspect ("Opportunity management and inspection") vs Forecast ("**Forecasting and pipeline management**") vs Capture ("Data quality and autocapture") vs Groove ("Sales engagement and prospecting") vs Align ("Buyer collaboration and mutual action plans") vs Copilot ("Conversation intelligence and coaching"). — The vendor that most prominently claims "opportunity management" sells "pipeline management" inside a *different module* of the same platform; both operate on the same CRM pipeline data. This is packaging-level separation, not Type-level.
- Page notes a merger ("One company, one site. This page will redirect on 9/15/26" — Clari/Salesloft); product naming may shift post-merger. Recorded as uncertainty.

## Product E — Microsoft Dynamics 365 Sales / Zoho CRM (structural only)

- Dynamics 365: the Opportunity entity could not be fetched (404 on three path variants — see Sources). Structural presence only: the CRM pass already recorded Dataverse's stage machinery on records (StageId/ProcessId/TraversedPath) and the market-canonical status of the opportunity entity. No product-specific claims from this pass.
- Zoho CRM: not retried (404×2 recorded by the CRM pass). SMB-modular pole treated structurally.

## Cross-product Comparison

| Dimension | Salesforce (T2) | HubSpot (T1) | Pipedrive (T2) | Clari Inspect (T2) |
|---|---|---|---|---|
| Label for the deal object | "Opportunity" (feature: Account & Opportunity Management; bundle: "…and Opportunity Management") | "Deal" (deal pipelines) | "Deal" (FAQ: deal management = tracking "sales opportunities") | "Opportunity" (product: Opportunity management & inspection) |
| Relationship to pipeline machinery | Same module family; separate "Pipeline Management" feature block on the same page | Pipelines are the deals' tracking structure (generic primitive across objects) | Deal management = prioritize/track/close deals in the sales pipeline; stages enumerated in FAQ | Inspection layer over CRM pipeline records; sibling module holds "Forecasting and pipeline management" |
| Staged progression | Structural (not directly fetched) | Org-defined stages; per-stage probability; Won+Lost required for reports; stage-entry required properties | Customizable stages/pipelines; drag board | Reads/derives from CRM stages; health/risk signals per deal (detail not documented at fetched level) |
| Population view | "Pipeline Management" block: consolidated view, charts over time, coaching focus | Board + weighted amount + reports; deletion blocked while records exist | Insights: open deals, stages, "which need attention" | Primary claim: inspection dashboards over the whole book of business |
| Record quality / inspection | "Deal-specific insights" (marketing level) | Stage-entry required properties; delete-blocking references | Insights flagging deals needing attention | Core claim: health scores, risk indicators, gap identification, inspection→action workflows |
| Buyer-context linkage | Opportunities unified with account data into "a single customer profile" | Deals associated with contacts/companies (per CRM-pass T1 evidence) | Deals carry buyer context; email integration | Imports CRM records (Salesforce integration) |
| Downstream artifacts | Quotes "synced to sales opportunities"; contract approvals | Line items with deals (related KB content) | Not detailed at fetched level | Not in scope of the overlay |
| Packaging | CRM suite module (entry bundle sells it by name) | CRM suite (freemium) | Pipeline-first standalone CRM | Overlay/platform module over external CRM |

**Reading of the table**: every column is the same object-and-flow machinery; the columns differ in (a) which word they use for the deal object and (b) which surface leads (record detail vs board vs inspection dashboard). No column reveals machinery that the pipeline Type lacks.

## Abstraction Levels

### Level 0 — candidate defining invariant for "Opportunity Management" (attempted as if a distinct Type)

1. **The opportunity/deal record of record** — a persistent, individually identified record of one specific potential sale, carrying its commercial substance (value, expected close, owner) bound to buyer context, ending in a recorded won/lost outcome.
2. **Managed progression toward the outcome** — the record moves through states/stages toward closure, with movement tracked.

**Load-bearing test and failure**: this candidate L0 is exactly the sales-pipeline-management L0's first two legs — and the pipeline pass's leg 1 already contains the outcome-with-reason semantics ("worked over time and ending in a recorded won/lost outcome with reason"). A subset-L0 cannot define a distinct Type: every pipeline-management product is de facto an opportunity-management product. The search for a third, unique leg failed on all candidates:

- **Record-content depth** (contact roles, products/line items, quote sync): enterprise-pole enrichment, evidenced at marketing level (Salesforce quote sync); the Pipedrive pole is called "deal management" without deep role/line-item structure → fails "would still be recognized".
- **Record-quality/inspection governance** (Clari): a packaging pole of the pipeline Type (its variants list and representative products already include the inspection overlay), and native CRM products carry lighter hygiene machinery instead → a pole, not an invariant.
- **Creation-path machinery** (lead→opportunity conversion): standard capability in the pipeline Type, not core there either.
- **Population machinery**: present in all sampled realizations (even Clari's core claim is population inspection) → shared, not differentiating.

**Result: the candidate L0 is a proper subset of the sibling's L0 → same Application Type.** The label "opportunity management" names the deal/pipeline machinery addressed record-first; "sales pipeline management" names the same machinery addressed flow-first.

### Level 1 — Common Mature Structure (of the shared machinery)

- org-defined staged pipeline; stage open/closed semantics; won/lost terminal states required for reporting (HubSpot T1)
- stage gates: required properties on stage entry (HubSpot T1 "conditional stage properties"); approvals via pipeline rules (HubSpot T1)
- stage probability and weighted pipeline value (HubSpot T1 mechanics)
- buyer-context linkage (deal ↔ contact/company/account)
- activity/next-step attachment; hygiene signals (stale deals, missing next steps — Pipedrive "which need attention", pipeline pass evidence)
- lead→deal conversion (Pipedrive LeadBooster; pipeline pass evidence)
- population analytics: value by stage, conversion, aging, focus/coaching views (Salesforce, HubSpot, Pipedrive, Clari)
- record revision history / movement tracking; access scoping; deletion protections (HubSpot T1: pipeline with records can't be deleted)

### Level 2 — Variant / Optional Structure

- record-content depth: contact roles, products/line items on the deal, quote synchronization (enterprise pole; Salesforce marketing-level evidence "quotes synced to sales opportunities"; HubSpot ships line items as separate related objects)
- packaging: CRM-suite module sold under the name (Salesforce Starter Suite) vs pipeline-first standalone (Pipedrive) vs freemium suite (HubSpot) vs inspection overlay over external CRM (Clari)
- multiple pipelines per process/brand (HubSpot T1, with subscription limits)
- AI layering: deal health scores, risk indicators, AI insights/coaching (Salesforce, Clari; era-current)
- forecast views embedded (Salesforce Forecast Management block; Pipedrive forecast view) — the projection discipline remains the forecasting sibling
- generalized pipelines over non-sales objects (HubSpot T1: tickets/orders/projects/appointments share the primitive)
- methodology encoding through stages/fields; mobile capture

### Level 3 — Vendor-specific (research notes only)

- Salesforce: feature-block taxonomy (Account & Opportunity Management / Pipeline Management / Forecast Management as sibling blocks); Starter Suite $25 bundle list; Agentforce branding ("formerly Sales Cloud"); Einstein score mentions.
- HubSpot: default seven-stage sales pipeline with fixed probabilities (20/40/60/80/90/100/0%); weighted-amount formula; pipeline limits (0/15/100/350 by tier); Breeze assistant pipeline creation; e-commerce integration auto-adds an unmodifiable pipeline; internal pipeline names for APIs.
- Pipedrive: LeadBooster add-on packaging; nine-stage "deal management" FAQ list; "100,000+ companies in 179 countries" claim.
- Clari: module tree (Inspect/Capture/Groove/Align/Copilot/Forecast/Guide); RevDB; "75,000+ revenue team members" claim; Salesloft merger redirect banner (post-merger naming uncertainty).

## Vendor-specific Findings

- Salesforce is the sampled vendor that **sells the module under the "Opportunity Management" name** (bundle line item), while carrying a separate "Pipeline Management" feature block — two labels, one module family, one page.
- Clari is the vendor that claims "Opportunity management" as a **standalone product name** — but the product is a deal-inspection overlay, and its own sibling module ("Forecast") carries "pipeline management". The label is claimed at packaging level inside one platform.
- Pipedrive is the vendor whose **own FAQ text collapses the two labels** ("deal management… tracking and optimizing sales opportunities").
- HubSpot is the only Tier-1-reachable source this pass; its docs confirm stage machinery, gates, probabilities, and deletion protection in operational detail, and show the pipeline primitive is generic across objects (deals being the revenue instance).

## Boundary Findings

1. **vs Sales Pipeline Management (§07 sibling — THE decision this pass was asked to make)**: verdict = **same Application Type; alias/consolidation recommended; keep-both REJECTED from this side.** Evidence: (a) the pipeline pass's proposed opportunity-side discriminator ("deal-record lifecycle depth") is contained within the pipeline Type's own documented deal object, so it cannot separate the Types; (b) no sampled product realized under either label lacks staged progression or population machinery; (c) the market's own texts mix the labels (Pipedrive FAQ; Salesforce's sibling feature blocks; Clari's module tree); (d) the pipeline Type's variants and representative products already include the inspection overlay (Clari Inspect listed there); (e) the candidate L0 is a proper subset of the pipeline L0 (see Abstraction Levels). The residual difference — record-first address (the deal as a worked case: complete it, inspect it, correct it, close it) vs flow-first address (the population as a managed asset) — is an emphasis inside one machinery base, not a Type boundary. Precedent alignment: online-marketplace/multi-vendor-marketplace (same Type, two angles, consolidation recommended, both documents stand cross-referenced). NOT a silent rewrite: both leaves keep their documents; consolidation is left to a taxonomy pass. Consistency check with the pipeline pass's own L0: legs 2–3 (stage-flow governance, population management) are satisfied by every sampled "opportunity management" realization, so nothing is lost by the merge verdict.
2. **vs Customer Relationship Management / CRM (§07 head)**: CRM's L0 leg 3 ("managed commercial progression") makes deal progression one structure over the relationship record; this Type/label centers the deal-first address. The CRM pass's boundary #3 ("those center the deal and its board; remove relationship records → pipeline management territory") is RATIFIED and now resolves to the single pipeline/opportunity Type. The CRM pass's re-check note for this leaf ("deal-only slice vs full relationship system of record") is DISCHARGED: the slice is real but it is the pipeline Type, not a third Type.
3. **vs Sales Forecasting Platform (§07 sibling, processed)**: progression vs projection seam RATIFIED unchanged (per the pipeline pass's ratification of the forecasting pass). Note the supporting nuance: Clari sells forecasting ("Forecast") separately from opportunity management/inspection ("Inspect") — vendor-level confirmation that projection machinery and deal-inspection machinery are distinct product surfaces over the same data.
4. **vs Lead Management Platform (§07 sibling, processed)**: upstream transient pre-qualification population vs the qualified commercial unit; the conversion act (lead→deal) is the designed seam (Pipedrive LeadBooster wording confirms from this side).
5. **vs Deal Desk / CPQ / Proposal Management / Sales Order Capture (§07 siblings)**: quotes, proposals, and order documents are artifacts *inside* a deal (Salesforce: quotes "synced to sales opportunities"); the deal machinery manages the record, the artifact Types manage the documents/pricing. RATIFIED from this side.
6. **vs Revenue Intelligence Platform (§07 sibling, unprocessed)**: flag for that pass — revenue-intelligence vendors brand deal inspection as "Opportunity management" (Clari), which this pass assigns to the pipeline/opportunity machinery family (the overlay packaging pole). Recommended seam for that pass: revenue intelligence = the analytics/projection layer over revenue data; deal inspection = an operating surface of the pipeline/opportunity Type. To be ratified when that leaf is processed.
7. **Homonym hygiene**: "opportunity" in Government Grants Management (funding opportunities), Internal Talent Marketplace (internal roles/gigs), and Spend Analysis (savings opportunities) names unrelated objects; no boundary interaction. Recorded to prevent future mis-merges.
8. **Historical / market-sample check**: the candidate definition was tested against older and differently positioned products. The paper-era pipe book (one card per pending sale: buyer, value, expected close, stage, worked to a recorded outcome) satisfies the candidate core at analog level — the same check the pipeline pass ran, and it passes identically here, which is itself confirmation that the two names digitize the same practice. The 1990s SFA generation sold "opportunity management" modules (opportunity records + stages + forecast) whose structure matches the pipeline core without any modern machinery (conceptual, no fetched source — assertion kept at structural level only). No era-, region-, or vendor-specific pattern entered the definition; the definition names no default stage set, no probability model, and no identity substrate.

## Uncertainties

- Salesforce Help and Microsoft Learn (Opportunity entity) were unreachable, so the enterprise object's internal depth (contact roles, line items, quote products, audit fields) is evidenced only at marketing-page level (Salesforce) and structurally (Dynamics). No field-level or default-value claims are made anywhere in the outputs.
- Zoho CRM remained unreachable; the SMB-modular pole rests on the CRM pass's structural treatment.
- No standalone product was found that manages opportunities *without* stages or population machinery; if such a product exists, it would be the one observation that could revive keep-both. Its absence in a 4-product sample plus two prior passes' evidence is the basis for the verdict — recorded, not claimed as impossible.
- Clari's Salesloft merger (page banner: redirect on 9/15/26) may rename products; the evidence is dated 2026-09-08.
- HubSpot pipeline limits and default probabilities are subscription-dependent and change; recorded as vendor facts in these notes only.

## Final Synthesis

"Opportunity Management" and "Sales Pipeline Management" are two market names for one application: the system that holds the deal — the record of one specific potential sale with value, expected close, owner, and buyer context — and manages it through an organization-defined staged process to a recorded won-or-lost outcome, while the population of open deals is inspected and worked as a whole. The label evidence is uniform: the enterprise CRM term for the deal object is "opportunity" (Salesforce sells "Opportunity Management" as a bundle line item); mid-market and SMB products say "deal" and define deal management as tracking sales opportunities (Pipedrive); the one vendor claiming "opportunity management" as a product name (Clari Inspect) sells a deal-inspection overlay that the pipeline Type already holds as a packaging pole. No machinery exists under one label that is absent under the other; the candidate defining core of opportunity management is a strict subset of the pipeline Type's core. Verdict: alias of Sales Pipeline Management — keep the leaf documented (this file pair), recommend consolidation at a taxonomy pass, and record the seam for the unprocessed Revenue Intelligence Platform pass. The final document therefore describes the shared Type honestly from the record-first angle, stating the label identity plainly, without inventing a separate structure.
