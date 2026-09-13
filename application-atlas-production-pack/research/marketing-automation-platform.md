# Research Notes — Marketing Automation Platform

## Research Goal

Understand what a Marketing Automation Platform (MAP) really is as an Application Type: the objects inside it, the work that flows through it, the rules that govern it, and where its boundaries sit against neighboring Types (Email Marketing Platform, Marketing Campaign Management Platform, CRM, CDP, channel marketing platforms, sales engagement, lead platforms, marketing analytics).

## Initial Boundary

Initial hypothesis before research:

- Core use: a marketer defines automated, multi-step marketing programs (nurture sequences, behavior-triggered follow-up, lifecycle campaigns) that execute against a database of known contacts without per-send manual effort.
- Users: marketing teams (demand gen, lifecycle, marketing ops); sales as a downstream consumer.
- Nearest neighbors: Email Marketing Platform (same family, channel-centric), Marketing Campaign Management Platform (planning layer), CRM (relationship/deal record), CDP (data layer), SMS/Push Marketing Platforms (channel platforms), Sales Engagement Platform (sales-side sequences), Lead Management/Capture/Generation (pipeline intake/supply), Marketing Analytics Platform (measurement).
- Unknowns: whether the contact database is definitional or just common; whether event triggers are definitional or only the time-based drip is; whether lead scoring / MQL machinery is definitional or a B2B variant; how the MAP/Email Marketing seam should be drawn given products span both.

## Research Questions

1. What is the "thing" a MAP automates — what is the unit of work?
2. What does the MAP hold? Is a person-level marketing database definitional?
3. How is a program defined (entry criteria, steps, waits, branches, actions)?
4. What per-contact state does the system keep, and what rules govern progression and re-entry?
5. Which channels are definitional? Is email required?
6. What consent/suppression machinery is structural?
7. Which capabilities are common-mature but not defining: scoring, MQL/lifecycle stages, forms/landing pages, CRM sync, analytics, AI?
8. Where exactly do the boundaries with Email Marketing, Campaign Management, CRM, CDP, Sales Engagement, and the lead platforms sit?
9. Would older / thinner products (autoresponder-era drip tools) still satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Adobe Marketo Engage | Enterprise B2B demand-gen classic | the canonical "MAP" category definition; rich official docs |
| HubSpot Marketing Hub | Mid-market all-in-one suite (inbound philosophy) | workflows tool documented in depth; suite-embedded realization |
| ActiveCampaign | SMB/mid-market automation-first | automation + CRM + channels bundle; SMB tier |
| Klaviyo | Ecommerce/B2C lifecycle marketing | event/store-data-driven flows; B2C pole |
| Customer.io | Developer/data-driven engagement | API-first, event-pipeline realization; engineer+marketer pole |

Not directly researched this pass (documented as a limitation; no product-specific assertions made about them): Salesforce Account Engagement (Pardot), Oracle Eloqua, Braze, Iterable, Mailchimp, Brevo, GetResponse, Mautic.

## Sources

All fetched 2026-09-08. Evidence layer A unless noted.

- HubSpot Knowledge Base — "Create workflows" — https://knowledge.hubspot.com/workflows/create-workflows
- Adobe Experience League — Marketo Engage Product Docs — "Understanding Smart Campaigns" — https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/understanding-smart-campaigns
- Adobe Experience League — "Marketo Engage Glossary" — https://experienceleague.adobe.com/en/docs/marketo/using/getting-started/things-to-know/marketo-engage-glossary
- ActiveCampaign Help Center — "What are automations in ActiveCampaign? An overview" — https://help.activecampaign.com/hc/en-us/articles/218788657-What-are-automations-in-ActiveCampaign-An-overview ; Help Center root (category map) — https://help.activecampaign.com/hc/en-us
- Klaviyo Help Center — Flows category — https://help.klaviyo.com/hc/en-us/categories/115000312411 ; "Getting started with flows" — https://help.klaviyo.com/hc/en-us/articles/115002774932
- Customer.io Documentation — docs root — https://docs.customer.io/ ; "Automation concepts & settings" — https://docs.customer.io/messaging/send/automations/overview.md

Fetch failures (abandoned per network rules, no memory-fill): two guessed ActiveCampaign article URLs 404'd before the help-center root resolved canonical links; one Klaviyo article ID 404'd before the category page resolved the current ID; two guessed Marketo URLs 404'd before the docs home resolved canonical paths; Customer.io root path guess 404'd before docs root resolved. All five products ultimately reached at Tier 1.

## Product Observations

### Adobe Marketo Engage (A)

- "If Marketo Engage is a car, the Smart Campaign is its engine." Smart Campaign = 3 areas: **Smart List** (who: filters = batch qualification "at the present time", triggers = "the moment someone does something, fire the flow immediately"), **Flow** (steps incl. Wait steps and split choices), **Schedule** (one-time, recurring batch, or trigger-fired).
- **Database**: "home to all of your **person** records" (person = formerly "lead"). **Activities** = log of all trackable actions per person (email opens, clicks, form fills, web page visits); activities feed smart lists, triggers, filters.
- Anonymous web visitors cookied via **Munchkin** tracking; become **known persons** on identifiable action (form fill, tracked-link click, API association). **Acquisition Program** records who acquired the person (first-touch attribution).
- **Lists**: smart lists (dynamic, filter-defined, constantly change) vs static lists; constraints narrow filters.
- **Programs** = containers for a marketing initiative; four types: **Event Programs**, **Engagement Programs**, **Email Programs** (one-time sends), **Default Programs**. Programs hold local assets, tags (channel), period costs.
- **Engagement Program** (nurture): **streams** = prioritized content collections; **cadence** = frequency/timing per stream (e.g., weekly Tuesdays 9am); **cast** = the event of sending; content exhaustion ("received every piece of content"); **engagement score** (proprietary algorithm over opens/clicks/success vs unsubscribes).
- **Scoring**: behavior score (actions), demographic score (attributes), scoring models; **MQL** = "exhibited the behavior and characteristics to meet your success criteria in order to be passed off to your sales organization".
- **CRM sync**: native integration with exactly two CRMs — Salesforce and Microsoft Dynamics. Opportunities enter via CRM or API. **Sales Insight** surfaces engagement data (interesting moments, lead scores) inside the CRM.
- **Design Studio**: global assets — emails, landing pages, forms, snippets, images/files. Landing pages Marketo-hosted and tracked; forms embedded on Marketo pages or external sites, submissions trigger smart campaigns and update records.
- Email governance: **Unsubscribed** status honored by marketing email; **operational emails** ignore Unsubscribed/Marketing Suspended (critical/auto-response only); **durable unsubscribe** survives record deletion/recreation; **Marketing Suspended** (manual mute); **Email Suspended** (24h block after hard bounce); **Blocklisted** person receives nothing incl. operational; **Suppression List** excluded regardless of targeting; **Subscription Center** (category-level preferences). Deliverability apparatus: dedicated IPs, IP warming, seed lists, DMARC/SPF/DKIM, spam-trap education.
- **Segmentation + Dynamic Content + Snippets + Tokens** (My Tokens per program/campaign folder) + **Velocity Scripting** for advanced personalization.
- **Qualification Rules**: limit how many times a person can run through a smart campaign's flow.
- **Nested Campaigns**: Execute Campaign flow step calls another smart campaign (modular logic). **Engagement Map**: flowchart of complete campaign logic.
- **Workspaces + Person Partitions**: partitions act like separate databases; no de-dupe across partitions (multi-brand/region architecture).
- Add-ons: **TAM** (named accounts, account score, account smart lists — ABM), **Web Personalization** (known + anonymous visitor targeting), **Dynamic Chat** (conversational), **Sales Connect** (sales-side multi-step sequences — explicitly a different campaign concept), Predictive Audiences, Advanced BI Analytics, Performance Insights.
- Reporting: program performance, people performance (database growth), campaign email performance; **attribution** first-touch/multi-touch assigning credit to programs for pipeline/revenue.
- **Audit Trail** (who changed what when); SAML SSO; sandbox instances; REST/SOAP APIs.

### HubSpot Marketing Hub (A)

- **Workflows** tool under **Automation**. Create from scratch, with AI (Breeze Assistant, "When [this happens], then [do this]" prompt), or from template library (filterable by plan/objective; Marketplace templates).
- **Enrollment triggers**: filter-based, event-based, based-on-a-schedule, webhook-based; or manual enrollment. Trigger set + object type chosen together.
- **Object types**: contact-based default; "certain workflows, such as quote or contract based workflows require specific subscription types"; actions can target **associated records** ("updating an enrolled contact's associated company"); can create a deal in-workflow then reference it in later actions ("use records created earlier in the same workflow").
- **Re-enrollment/unenrollment**: default = enroll once; re-enroll toggle with its own triggers; "Records that are currently enrolled in a workflow cannot be re-enrolled into that same workflow until they complete the workflow"; unenrollment criteria toggle; re-enrollment only after completion.
- **Actions**: send marketing email, assign records/users, create tasks, set/update record data, data variables from multiple object sources; locked actions per subscription tier.
- **Publish**: Review and publish; choose enroll-existing-now vs future-only; static list auto-created of contacts meeting criteria; scheduled workflows enroll on schedule.
- **History**: workflow action logs and enrollment history retained on defined windows (90 days / 6 months / 2 years+ — precise vendor numbers, kept here only); workflow changes reviewable.
- **Permissions**: Edit vs Publish workflow permissions; Super Admin.
- Minimap for large workflow architecture; undo/redo (30 days); placeholder actions must be completed before turn-on.
- Related content separates **Sequences** (sales-side, 1:1) from workflows; workflows can enroll contacts into sequences.
- Positioning: Marketing Hub inside the CRM platform (Smart CRM, Data Hub, Revenue Hub); marketing contacts pricing model; Breeze AI across.

### ActiveCampaign (A)

- "Automations is what we call our Marketing & Sales Automation feature." "An 'automation' is a chain of events that runs when triggered by starting conditions you define… created by combining **triggers, actions, and logic**."
- Runs "with no input from you" once set up — "extremely high-leverage".
- Marketing use cases: intelligent follow-up ("rather than a basic drip sequence… treats contacts differently depending on who they are and what they have done" — branch on which link clicked); react to behavior in real time (page visits, email opens, form submissions); gather data into profiles (tag by interest → targeted follow-up).
- Sales use cases: **multi-dimensional lead scoring** (score rises with site/email interaction; at threshold "a deal can be created, and the lead can be assigned to a salesperson"); **deal automation** (auto-add notes/tags/tasks, move deals through pipeline stages); contact insight for sales.
- **Site Tracking** connects website activity to contacts ("see" what contacts do on your site).
- Help-center category map confirms the bundle: Automation, Contact Management (add/segment/clean lists), CRM (Deals), Email Marketing, SMS Marketing, WhatsApp Messaging, Website (signup forms, landing pages, site tracking), Ecommerce, Reports, AI (Active Intelligence — autonomous campaign/automation building).
- Dedicated article distinguishes **automations vs campaigns vs transactional emails vs 1:1 emails** — automations = "a sequence of events to be followed… pre-sale nurturing… post-sale"; campaigns = one-off sends.
- Double opt-in via form action; plans Starter/Plus/Pro/Enterprise.

### Klaviyo (A)

- "A **flow** is a sequence of automated actions (e.g., sending messages) that is triggered by certain behavior or event… also known as automations or drip campaigns." "Any data syncing to your Klaviyo account can be used to trigger and target automated flows."
- **Trigger types** (5): list-triggered (added to a list), segment-triggered (added to a dynamic segment), metric-triggered (performed an action, e.g., Placed Order), date property-triggered (birthday etc.), price-drop-triggered (viewed/checkout item dropped in price).
- **Trigger filters + profile filters**: checked when someone triggers; non-qualifiers "filtered out immediately"; profile filters **re-checked before each component** and at send time ("skip anyone who fails these filters at send time"); trigger filters NOT re-checked at send time.
- **Flow actions, 3 types**: **Messages** (send; per-action status), **Data** (update profile property or list, internal alert, webhook), **Logic** (time delays; **splits** routing into up to 20 paths using profile data and, in metric-triggered flows, event data).
- **Time delays**: schedule steps relative to trigger/each other; 24-hour vs calendar-day semantics; delay until time-of-day/specific weekdays; back-to-back components fire simultaneously.
- **Statuses**: draft / manual / live — per action or whole flow. Manual = active but sends queue for human review ("Needs Review" — Send All / Cancel All / per-recipient). Draft messages in a live flow are skipped.
- **Recipient activity**: Waiting (queued at a delay), Skipped, Needs review; per-action analytics on the canvas; 30-day snapshots; flow analytics report.
- **Back-population**: retroactively add past profiles that would have triggered. Flows "can only be entered once" — welcome series split into separate email and SMS flows because opt-ins are separate per channel.
- Default/pre-built flows: welcome series, abandoned cart, post-purchase, winback, browse abandonment, back-in-stock (unique delay component); Flow Library by goal/integration/channel; **Flows AI** natural-language building.
- Platform self-description: B2C CRM; "Klaviyo Marketing … marketing automation"; KDP (data platform); Marketing Analytics; reviews; helpdesk; push notifications; WhatsApp; social marketing. Smart Sending; UTM tracking; benchmarks vs aggregated customer data.

### Customer.io (A)

- Self-description: "a messaging automation platform for sending targeted email, push notifications, SMS, in-app messages, and webhooks based on customer behavior and data attributes." "Customer.io decides **who** gets a message, **what** it says, and **when** it sends."
- **Automation** = workflow with 4 components: **Trigger** (who enters + when/frequency; filters optional), **Goals** (conversion = event/segment-entry/segment-exit within a conversion window; per-delivery-type attribution), **Exit criteria** (leave early when goal achieved), **Workflows** (messages + actions; the person's passage = a **journey**).
- **Trigger types**: attribute/segment match, event (app/site activity), form submission (connected forms, Facebook Lead Ads), important date (attribute-based), geofence (premium), **object updated** and **relationship added/changed** (custom objects like accounts/courses; "only profiles enter into journeys, not objects" — audience selectable among related profiles), **webhook** (external data; "data, not profiles, is the subject… don't typically send messages directly; rather… associate data with profiles, which can trigger subsequent automations").
- **Current vs future additions**: enroll profiles already matching at start vs only future matches; date-triggered always both; backfill semantics documented for imported data.
- **Workflow builder**: messages, webhooks, attribute updates, time delays; per-message settings: open/click tracking, **sending behavior** (automatic / queue draft / don't send), subscription-topic override, **holdout tests**.
- **Liquid** personalization (`{{customer.full_name}}`); event attributes usable in content; event attributes can override `from_address`/`recipient`/`reply_to`.
- **Subscription preferences**: workspace subscription center topics; "If profiles are unsubscribed from the topic, they won't get messages… They would, however, continue to receive in-app messages"; non-message actions still apply to unsubscribed profiles; "send messages to unsubscribed profiles [only] in transactional use cases… can violate local laws (GDPR, CAN-SPAM)".
- **Governance**: workspace **message frequency limits** (max messages per profile per period) + **per-automation rate limits** per channel (documented range 1–60,000/min — vendor number, kept here); rate-limited sends still advance the journey unless "Wait before continuing journey" is set.
- Scheduling: automations can start/stop at set dates (time-bound initiatives). Metrics tab with CSV export; **reporting webhooks** stream delivery/engagement data out; warehouse syncs / Data Pipelines destinations.
- Data-in: identify people, record events, custom objects; SDKs (iOS/Android/RN/Flutter/JS) incl. push + in-app; transactional messages as a separate API surface; CLI + MCP for agent access (era-current).

## Cross-product Comparison

| Structure / capability | Marketo | HubSpot | ActiveCampaign | Klaviyo | Customer.io | Layer |
|---|---|---|---|---|---|---|
| Persistent person-level marketing database (profile + consent + activity history) | ✓ (Database, Activities) | ✓ (contacts + activity) | ✓ (contacts + site tracking) | ✓ (profiles, lists, metrics) | ✓ (profiles, events, attributes) | B |
| Consent/subscription state on the record, enforced on marketing sends | ✓ (unsubscribed/operational/durable) | ✓ (marketing email, subscription status) | ✓ (double opt-in, list subscribe) | ✓ (per-channel opt-in) | ✓ (subscription topics) | B |
| Reusable multi-step program defined once (entry criteria + steps + waits + branches) | ✓ (smart campaign; engagement program) | ✓ (workflow) | ✓ (automation) | ✓ (flow) | ✓ (automation) | B |
| Program steps execute marketing messages across ≥1 channel | ✓ (email native; SMS via providers) | ✓ (marketing email; more in suite) | ✓ (email/SMS/WhatsApp) | ✓ (email/SMS/push/etc.) | ✓ (email/push/SMS/in-app/webhook) | B |
| Per-contact execution state (entered/waiting/branched/skipped/completed) + re-entry rules | ✓ (qualification rules, membership) | ✓ (enrollment history, re-enroll/unenroll) | ✓ (automation state) | ✓ (Waiting/Skipped/Needs review; entered once) | ✓ (journey state, exit criteria) | B |
| Dynamic segmentation / criteria query layer | ✓ (smart lists) | ✓ (lists/filters) | ✓ (segments) | ✓ (segments) | ✓ (segments/attribute triggers) | B |
| Time-based scheduling of steps (waits/delays, recurring batch) | ✓ (wait steps, schedule tab) | ✓ (schedule-based triggers, delays) | ✓ (waits) | ✓ (time delays) | ✓ (time delays) | B |
| Event/behavior triggers (real-time reactivity) | ✓ (trigger campaigns) | ✓ (event-based triggers) | ✓ (behavior reactions) | ✓ (metric triggers) | ✓ (event triggers) | B |
| Record-update / internal-notification actions in programs | ✓ (flow steps, alerts) | ✓ (set properties, tasks, notify) | ✓ (tags, notes, deal updates) | ✓ (data actions, alerts) | ✓ (attribute updates, webhooks) | B |
| Per-program + per-message analytics | ✓ (reports, attribution) | ✓ (workflow history/metrics) | ✓ (reports) | ✓ (flow analytics, benchmarks) | ✓ (metrics, reporting webhooks) | B |
| Draft → review → live status lifecycle | ✓ (activate campaigns; asset approval) | ✓ (review and publish) | ✓ (activation) | ✓ (draft/manual/live) | ✓ (review/start; draft-queue option) | B |
| Message/asset editors + templates | ✓ (Email Designer, templates) | ✓ (email editor, templates) | ✓ (email designer) | ✓ (templates, library) | ✓ (editors, liquid) | B |
| Personalization (merge variables/tokens/scripting) | ✓ (tokens, velocity, dynamic content) | ✓ (personalization tokens) | ✓ (personalization fields) | ✓ (dynamic data) | ✓ (liquid) | B |
| Lead scoring + MQL/sales handoff | ✓ (behavior/demographic scores, MQL) | ✓ (lead scoring via properties; handoff) | ✓ (multi-dimensional scoring → deal) | ✗ (predictions instead) | ✗ | B (segment-dependent → L2) |
| Nurture streams / cadence machinery | ✓ (engagement programs) | — (via workflows) | — (via automations) | — (via flows) | — (via automations) | A (product-specific packaging) |
| Forms / landing pages as capture modules | ✓ | ✓ | ✓ | ✓ (forms; pages limited) | ✓ (connected forms only) | B (module, not core) |
| Native CRM sync / built-in CRM | ✓ (SFDC + Dynamics only) | ✓ (native suite CRM) | ✓ (built-in Deals CRM) | partial (store/CDP data) | partial (objects, pipelines) | B (module) |
| Multi-channel breadth beyond email | partial (SMS via partners, ads audiences) | partial (suite-dependent) | ✓ (SMS, WhatsApp) | ✓ (SMS, push, WhatsApp, social) | ✓ (push, SMS, in-app, LINE, Slack) | B (variant depth) |
| Web personalization / on-site surfaces | ✓ (add-on) | — | — | — | — | A (add-on) |
| AI assistance / agents | ✓ (agents, gen AI) | ✓ (Breeze) | ✓ (Active Intelligence) | ✓ (Flows AI, Marketing Agent) | ✓ (CLI/MCP agent access) | B (era-current) |
| Anonymous-visitor staging → known person | ✓ (Munchkin) | ✓ (via tracking) | ✓ (site tracking) | — (identified store events) | — (identify API) | B (implementation variant) |
| Object-based programs (deals/accounts/quotes) | partial (TAM accounts add-on) | ✓ (deal/quote/contract workflows) | ✓ (deal-triggered automations) | — (custom objects in triggers) | ✓ (object/relationship triggers) | B (variant) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a MAP:

1. **The marketing person database of record** — persistent, identified person records (prospects and customers) each carrying profile attributes, consent/subscription state, and a recorded history of marketing-relevant activity (message engagement, site/app events, form fills, purchases); the standing audience against which marketing executes. (Remove → a workflow engine or a sending gateway with no audience memory.)
2. **The reusable automated program** — a multi-step workflow defined once by the marketer: entry criteria, then steps that execute marketing touches (messages across one or more channels), waits/delays, conditional branches, record updates, and internal notifications — executed per contact without per-send manual effort. (Remove → one-off broadcast campaigns or manual sends.)
3. **Per-contact program execution state** — each person's individual progress through each program: entered, waiting at a delay, branch taken, skipped at a filter check, completed or exited early; re-entry/qualification rules; and an execution log of what was done to whom. (Remove → scheduled batch sends with no per-person memory.)

Jointly-held is load-bearing:
- 1+2 without 3 = program templates replayed as broadcasts (scheduled email marketing).
- 2+3 without 1 = an automation engine acting on anonymous/ephemeral events with no person of record (event-processing utility / CDP-adjacent journey tool).
- 1+3 without 2 = a contact database with activity history but no programs (CRM/CDP territory).

Channel-agnostic: email is the historically dominant and still-central channel, but the invariant is "marketing touches executed as program steps across one or more channels", not email itself (Customer.io leads with push/SMS/in-app; Marketo executes SMS via providers; sibling passes already ratified "MAP = channel-agnostic orchestration" against the SMS and push passes).

### L1 — Common Mature Structure

Present across the sample (or nearly) but not definitional:

- dynamic segmentation / criteria query layer over the database
- email channel with deliverability apparatus (authentication, bounce handling, suppression)
- per-program and per-message analytics; program-level conversion/revenue attribution
- message/asset editors, templates, reusable content blocks
- personalization machinery (merge variables → tokens → scripting)
- forms and landing pages as capture modules feeding the database
- CRM sync or a built-in lightweight CRM
- A/B testing of program sends
- send governance: frequency caps, quiet hours, rate limits, smart-send suppression
- program template libraries; draft/review/live status lifecycle; audit/history
- AI assistance for building programs and content (era-current)

### L2 — Variant / Optional Structure

- **lead scoring + MQL/lifecycle stages + sales handoff** (B2B demand-gen pole; absent in ecommerce pole)
- **nurture streams/cadence packaging** (B2B classic; others express nurture as ordinary programs)
- **ecommerce event flows + revenue attribution** (welcome/abandoned-cart/post-purchase/winback/back-in-stock; store-data triggers)
- **object-based programs** (deals, companies/accounts, quotes as enrollment subjects — HubSpot; object/relationship triggers — Customer.io; TAM accounts — Marketo add-on)
- **multi-channel breadth** (SMS, push, in-app, WhatsApp, RCS, social retargeting, ad audiences)
- **web behavior capture incl. anonymous-visitor staging → known person** (B2B implementation pattern)
- **web personalization / conversational chat** (add-on modules)
- **workspaces/partitions, agency multi-tenancy, distributed marketing** (multi-brand/regional governance)
- **open-source / self-hosted deployment** (Mautic pole)
- **developer-facing surfaces** (APIs, SDKs, CLI/MCP)

### L3 — Vendor-specific (research notes only)

- Marketo: Munchkin, streams/cadence/cast/exhaustion/engagement score, person partitions, Engagement Map, nested campaigns (Execute Campaign), Sales Insight/Connect, TAM, Velocity scripting, period costs, exactly-two-CRM native sync, 24h email suspension after hard bounce.
- HubSpot: Breeze Assistant, workflow minimap, undo/redo window, placeholder actions, action-log retention windows (90d/6mo/2yr+), locked actions by tier, marketing-contacts pricing.
- ActiveCampaign: site tracking, tags-as-interest model, Active Intelligence, deal-automation specifics, plan-tier gating.
- Klaviyo: back-population, smart sending, price-drop triggers, 20-path splits, calendar-day vs 24-hour delay semantics, Needs-Review manual queue, benchmarks, per-channel welcome-flow separation.
- Customer.io: Liquid, geofence triggers, holdout tests, per-automation rate-limit range (1–60,000/min), event-attribute header overrides, webhook-subject data automations, reporting webhooks, CLI/MCP.

## Rejected Findings (considered for the core, rejected)

- **Email as the defining channel** — rejected: the thin historical pole (autoresponder drip) is email-only and still the Type; modern poles lead with other channels; sibling passes ratified channel-agnostic orchestration. Email's centrality is documented as dominant-implementation status, not invariant.
- **Event/behavior triggers as definitional** — rejected: a time-based drip sequence (enroll → wait → send → wait → send) has no event triggers and is uncontroversially a MAP program. The invariant is "defined entry criteria", which covers list membership, schedule, and event alike.
- **Lead scoring / MQL machinery** — rejected: B2B-variant; Klaviyo and Customer.io poles lack classic scoring entirely.
- **Landing pages / forms** — rejected: modules; Customer.io has no page builder; capture can be external.
- **CRM sync** — rejected: common but not definitional; Klaviyo/Customer.io are not CRM-centric; Marketo's sync is a two-CRM integration, not a definitional structure.
- **Multi-step branching depth** — rejected: linear sequences satisfy the core; branching depth is maturity, not identity.
- **Anonymous-audience targeting** — rejected: that is DMP/advertising territory; the MAP's subjects are identified persons (anonymous web staging is an implementation of activity capture, not the database).
- **Campaign planning/budgeting/approval** — rejected: that is the Marketing Campaign Management layer; MAP programs are execution machinery.
- **Built-in analytics depth** — rejected: program-level reporting is common-mature; cross-stack measurement is the Marketing Analytics Type.

## Boundary Findings

- **vs Email Marketing Platform** (unprocessed sibling): same campaign-grammar family; the seam is the defining unit. Email marketing's center is the email channel (list + composition + deliverability + campaigns), with automation as an extension; the MAP's center is the program executed per contact across channels, with email as one (dominant) channel. Market products genuinely span both (Klaviyo, ActiveCampaign, Mailchimp self-describe across the seam) — classification must follow center of gravity, not feature presence. **Flag for joint review when email-marketing-platform is processed.**
- **vs Marketing Campaign Management Platform** (unprocessed): planning/coordination layer (briefs, budgets, calendars, approvals, asset orchestration) vs automated execution machinery. The marketing-analytics pass already framed this seam as "execution vs measurement, module bundling is packaging" for both siblings. Flag for that pass.
- **vs CRM** (unprocessed): CRM holds the relationship/deal record of record for sales; the MAP holds the marketing audience and executes programs. Deep interlock: Marketo natively syncs exactly two CRMs and surfaces scores to sellers; HubSpot bundles both in one platform; ActiveCampaign automations create/move deals. Removal test: strip the program machinery from a MAP → a CRM (or contact DB) remains; strip the deal/relationship record from a CRM → the MAP's program machinery remains.
- **vs Customer Data Platform** (unprocessed): CDP = unified cross-source customer data layer whose product is the profile/identity graph feeding other systems; MAP = execution system holding its own marketing database. Convergence is real and documented in-sample (Klaviyo markets a Data Platform; Customer.io ships Data Pipelines; HubSpot has Data Hub) — the seam is data-unification-as-the-product vs program-execution-as-the-product. Flag for the CDP pass.
- **vs Sales Engagement Platform** (processed 2026-07): sales-side per-prospect sequences with human-executed steps and personal-sender 1:1 email vs marketing-side audience programs machine-executed under a brand sender. In-sample confirmation: Marketo ships Sales Connect as a separate sales tool with its own "campaign" concept; HubSpot separates Sequences from Workflows.
- **vs Lead Capture Platform** (processed 2026-07): capture ends at handoff; the MAP is a canonical handoff destination and continues the relationship (nurture). Capture's lead record is intake-shaped; the MAP's person record is relationship-shaped.
- **vs Lead Generation Platform** (processed 2026-07): platform-operated demand surface supplying leads vs the business-side system that markets to the resulting audience.
- **vs Lead Management Platform** (unprocessed): lead lifecycle/routing/distribution of record vs nurture execution. MAPs produce scoring→MQL→handoff as workflow outcomes; lead management owns the lead's lifecycle record. Flag for that pass.
- **vs Marketing Analytics Platform** (processed 2026-09): execution vs measurement — ratified from that side ("vs marketing-automation-platform … execution vs measurement, module bundling is packaging"). MAP reporting is program-level; cross-stack measurement is the analytics Type.
- **vs ABM Platform** (processed): primary object account vs person. In-sample confirmation: Marketo's TAM (named accounts, account scores) is an add-on module on the person-centric MAP — "MAP vendors bundle ABM modules" per that pass.
- **vs SMS / Push Notification Marketing Platforms** (processed 2026-07): ratified seam — channel-agnostic orchestration vs channel mechanics (carrier/OS machinery, consent regimes, sender registration). MAPs execute those channels as program steps but do not own the channel substrate.
- **vs Customer Communication Management** (processed 2026-09): CCM's unit of work is the recurring operational customer document (bills/statements/notices) under governed design; the MAP's unit is the marketing program. Different unit, different governance, different audience semantics.
- **vs Loyalty / Referral / Advocacy platforms** (processed 2026-09): program-specific systems of record; the MAP executes lifecycle campaigns around them and may integrate them.
- **vs generic workflow automation (BPM/iPaaS)**: sharpest negative case — remove the marketing person database and the message-channel semantics → a generic workflow engine remains; add them → a MAP.
- **vs Marketing Personalization Platform** (unprocessed): on-site/in-app content personalization vs outbound program execution; in-sample, web personalization appears as an add-on module (Marketo), supporting module-not-Type treatment.

## Historical / Market-Sample Check

- **Thin ancestor**: autoresponder/drip era — a subscriber list + a pre-written timed sequence + per-subscriber progression + email execution. Satisfies all three L0 structures with none of L1/L2 (no scoring, no forms, no CRM sync, no AI, single channel). In-sample textual support: Marketo glossary defines "Drip Campaign: a direct marketing method that involves sending customers/potential customers a series of correspondence over a long period of time"; Klaviyo: flows "also known as automations or drip campaigns". **Pass.**
- **B2B classic era** (Eloqua/Marketo/Pardot generation): same core + scoring + nurture streams + CRM sync. **Pass.**
- **Older/regional/platform-native**: listserv newsletters with sequential follow-ups; regional email+SMS automation tools. **Pass** — nothing in L0 assumes cloud, AI, multi-channel, or real-time triggers.
- Conclusion: the L0 is era-stable; modern implementations (AI agents, object programs, omnichannel) are L1/L2.

## Uncertainties

- Pardot/Account Engagement, Eloqua, Braze, Iterable, Mailchimp, Brevo not directly fetched this pass; no product-specific claims about them are made anywhere. The five-product sample is judged sufficient (stop conditions: core model, workflows, commonalities, and boundaries all stable; additional products would repeat evidence).
- The MAP/Email Marketing seam is graded in the market; the center-of-gravity test is proposed but needs ratification from the email-marketing-platform pass.
- The positioning of the Marketing Campaign Management Platform leaf (planning layer) is inferred from naming + the sibling analytics pass's framing, not directly researched.
- Precise numeric limits observed (retention windows, rate ranges, path counts) are vendor-specific and deliberately excluded from the final document.

## Final Synthesis

A Marketing Automation Platform is a marketer-side system whose defining core is three jointly-held structures: (1) a persistent person-level marketing database — identified prospects/customers with profile attributes, consent state, and activity history; (2) the reusable automated program — a multi-step workflow defined once (entry criteria; message touches across one or more channels; waits; branches; record updates; internal notifications) and executed per contact without per-send manual effort; (3) per-contact program execution state — each person's progression, filter re-checks, re-entry rules, and an execution log. Everything else — segmentation depth, scoring, MQL handoff, forms/pages, CRM sync, omnichannel breadth, analytics, AI — is standard capability or variant, not definition. The Type sits between the channel marketing platforms (which own delivery substrates), the campaign-management layer (which plans), the analytics layer (which measures), and the CRM (which holds the sales relationship).
