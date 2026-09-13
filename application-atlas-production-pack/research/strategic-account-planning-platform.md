# Research Notes — Strategic Account Planning Platform

Research date: 2026-09-08
Slug: strategic-account-planning-platform
Directory leaf: Strategic Account Planning Platform (§07 Sales, Customer & Revenue)

## Research Goal

Understand what a Strategic Account Planning Platform actually is as an Application Type: what object(s) it holds, who uses it, what work flows through it, and where its boundaries sit against CRM, ABM, Customer Success, and deal/pipeline tooling. Produce a vendor-neutral canonical model from real product evidence.

## Initial Boundary (hypothesis before research)

- Hypothesis: sales-team-facing software whose object of record is the *plan* for a named strategic/key account — customer business context, relationship objectives, stakeholder/relationship maps, white-space analysis, and an owned action plan — built collaboratively by the account team and refreshed on a cadence.
- Likely confusions:
  - CRM / Account Management CRM (holds the account record; does it hold the plan?)
  - ABM Platform (marketing-side targeting of account lists)
  - Customer Success Platform (success plans — outcome/adoption oriented)
  - Opportunity/Pipeline Management (deal-centric)
  - Generic workspace/whiteboard tools used to write account plans as decks
- Unknowns going in: whether the stakeholder/relationship map is definitional or merely common; whether white-space machinery is definitional; how CRM-native vs standalone products differ structurally; whether CS "success plans" are the same Type under a different name.

## Research Questions

1. What is the core object — the account plan — and what does it contain across products?
2. How is the stakeholder/relationship map represented (people, roles, influence, stance, coverage, strength)?
3. How is white space / growth opportunity modeled, and is it definitional?
4. How are plan objectives set, measured, and rolled up?
5. How do actions/milestones work (ownership, dates, tracking)?
6. What is the relationship to CRM (integration vs native; what syncs, which direction)?
7. How do collaboration and review cadences work (team editing, plan reviews, QBRs, leadership reporting)?
8. What role does methodology play (embedded frameworks, templates)?
9. What analytics exist (plan health/scores, relationship strength, coverage)?
10. Where does this Type end and CRM / ABM / Customer Success begin?

## Representative Products

Selected for market representativeness, documentation reachability, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Kapta | Standalone post-sales key-account-management platform ("system of action" vs CRM record-keeping) | Enterprise B2B account teams |
| Altify (Altify Accounts) | Salesforce-native, methodology-driven strategic revenue execution (TAS heritage) | Enterprise |
| Prolifiq (CRUSH) | Salesforce-native, RevOps-standardized account planning + relationship maps; strong in regulated/vertical industries (med device, pharma) | Enterprise / vertical |
| Gainsight (Success Planning) | Customer-success-suite boundary pole: plan object exists but center of gravity is adoption/health/retention | Enterprise CS orgs |
| LinkedIn Sales Navigator | Thin embedded insight layer: AI account insights + relationship map + notes; mass-market | Individual sellers / mid-market |

Rejected during sampling:
- Revegy (known pure-play) — site unreachable after two attempts; dropped per network rule.
- Mediafly — Product Mismatch: it is a revenue enablement platform (content, value selling, learning), not an account planning platform.
- Salesforce first-party account planning — help center returned a CSS error and the marketing URL 404'd (two failures); dropped. The CRM-embedded pole is instead covered by two third-party Salesforce-native products (Altify, Prolifiq).

## Sources

All fetched 2026-09-08. Tier 2 (official product pages) unless noted; no Tier 1 help-center/user-guide pages were reachable for any sampled product this pass.

- Kapta — https://kapta.com/ ; https://kapta.com/key-account-management-software ; https://kapta.com/key-account-management-software/account-planning-software
- Altify — https://altify.com/ ; https://altify.com/altify-accounts/ ; https://altify.com/relationship-map/
- Prolifiq — https://www.prolifiq.com/
- Gainsight — https://www.gainsight.com/ ; https://www.gainsight.com/customer-success/ ; https://www.gainsight.com/customer-success/success-planning/
- LinkedIn Sales Navigator — https://business.linkedin.com/sell/sales-navigator (reached via /sales-solutions/sales-navigator redirect)
- Failed/abandoned: revegy.com, www.revegy.com (transport errors ×2); help.salesforce.com account-plans article (CSS error); salesforce.com account-management-software (404); business.linkedin.com/sales-navigator (404, succeeded on alternate URL); mediafly.com (fetched, judged Product Mismatch).

## Product Observations

### Kapta (evidence layer A — official product pages)

- Positioning: "The Post-Sales Platform For Customer Retention And Growth"; "system of action"; "Traditional CRMs Were Built for Record Keeping, Not For Growth"; "Kapta picks up where your CRM falls short." Explicitly aimed at "large account teams" and "strategic, long-term customer relationships."
- The "account story" held in one place: stakeholder maps, relationship strength, meeting and QBR history, customer goals, risks, renewals, expansion paths — "so every function operates from the same truth." Anti-pattern named: "spreadsheet tribal knowledge."
- Org Charts: capture "the formal structure and the real buying dynamics behind it — power centers, influencers, blockers, champions, politics, and who's actually driving investment." Team alignment on "who matters most right now, where you're strong versus exposed, what's changed since the last conversation, and what to do next to protect the renewal and drive expansion." Anti-pattern named: "single-thread risk."
- Health Scores: continuous signals — account activity, stakeholder coverage, meeting/QBR cadence, renewal readiness, sentiment, outcomes and commitments — to show "which accounts are healthy, which are drifting, and why"; retention risk surfaced "before it turns into a renewal surprise."
- AI: works "across the account story (QBRs, meeting notes, action plans, risks, stakeholder coverage, renewals, and health signals) to surface what changed, what's at risk, and what to do next"; "outcomes-first" framing.
- QBRs: workflows pull from real-time account data; QBRs tracked over time — "what changed, what was committed, what got done, and where progress is stalling."
- Whitespace Analysis: "Using your contract and opportunity data, Kapta automatically generates a visual view of product and service penetration across your portfolio"; "surface gaps by product line or business unit"; "turn that visibility into focused, coordinated upsell and cross-sell plays." Anti-pattern named: "rebuilding coverage maps in spreadsheets every quarter."
- Account Plans: "customer goals, your strategy to support them, and the milestones that prove progress"; "tied to real-time account activity and updates"; "translate big-picture customer initiatives into clear, owned actions across functions, then track execution over time so the team stays on strategy, on schedule, and accountable to outcomes."
- Account planning page: "Track your customer goals and commitments in real time… translate your customer's big picture goals into ownable action items for your team. Then make sure everyone stays on budget, on time, and on strategy." Feature list: account health scoring, interactive org chart, customizable templates for account planning, deliverables tracking, easy reporting to clients and C-Suite, seamless CRM integration.
- Opportunities: mirrors CRM stages/steps plus customer-specific steps; tracks "pre-revenue" work — stakeholder alignment, value realization milestones, pilots, business case development, procurement readiness, renewal risk mitigation — "even when it's not ready for revenue attribution yet."
- Contracts/Renewals: shared view of every contract and renewal; renewal playbooks; alerts for key dates and obligations; customer lifetime value visibility.
- Integrations: Salesforce, HubSpot, MS Dynamics, MS Teams, Zoho, Slack, Mailchimp, ConnectWise.
- Other modules: QBR Management, Voice of Customer; KAMGenius training (methodology/training arm).

### Altify (evidence layer A — official product pages)

- Positioning: "Strategic Revenue Execution — turn strategy into execution across complex deals and accounts"; "The problem is not planning. It is execution." Methodology-driven; "100% Salesforce native"; Salesforce Crest partner.
- Altify Accounts ("Strategic account growth, executed daily"): "Operationalize an account-based sales strategy with account planning software to uncover new opportunities, deepen relationships and build trust, natively in Salesforce."
- Account plan surface: "Visualize account plan progress, highlighting next steps for potential, current, and won opportunities"; "Review, connect and collaborate on your account plan across the revenue team"; "Gain clarity with objectives, actions and customer insights."
- Whitespace: "Map current, potential and closed won opportunities to identify whitespace"; "Quickly assess account relationship and insight maps to validate the who and why behind opportunities"; cross-sell/up-sell framing.
- Relationship footprint: "Identify gaps in your account relationships with people who have influence, and create actions to develop connections further."
- Account plan reviews: "Identify gaps, vulnerabilities, and recommendations with insight and support from the broader revenue team."
- Relationship Map: "Capture and visualize the people who matter most. Flag key influencers, decision-makers, and blockers"; "Color-code strength indicators"; "Collaborate directly within the relationship mapping software to plan outreach, assign ownership, and strengthen weak links"; "As the relationship changes, so does the map… a living, evolving view of your customer ecosystem." FAQ: a relationship map is "not just an org chart" — org charts show hierarchical authority, relationship maps show influence and relationships "and more importantly, provide next steps on how to improve those relationships."
- Companion structures: Insight Map ("customer priorities and value drivers"), Opportunity Map (whitespace), TeamView ("align teams around the customer journey"), Deal and Account Reviews ("structured, action-oriented reviews that expose gaps").
- Collaboration integrations: Slack (messages between Slack and Altify captured against account plans), Google Docs (pulls in details from linked opportunities and account plans).
- Reporting: managed/unmanaged Salesforce packages; standard reports/dashboards; Einstein/Tableau/BI point-of-view reporting.
- Vendor claims (not generalized): "3x win rate increase when 6 or more key supporters are on the relationship map"; "36% deal size increase when a key supporter is identified."

### Prolifiq (evidence layer A — official product page)

- Positioning: "Account Planning & Relationship Maps in Salesforce"; "100% native to Salesforce" (Sayge Solutions, Inc.); AppExchange-listed.
- CRUSH (Account Planning Suite): "One source of truth your team plans and executes accounts from." Feature set: Relationship Maps, Account Hierarchy, SWOT; Master Account & Opportunity Plans & Account Plan Score; Cross Sell Maps, Objectives, Key Dates & Team Tasks; "Features are reportable Salesforce objects."
- Relationship Maps (also standalone): "Drag-and-drop org chart from Salesforce contacts"; "Influence levels, badges & relationship lines — all reportable"; "Omni View — see a contact's full cross-org profile across all opportunities"; "Embeds on any Salesforce record."
- AI: "AI builds your relationship map and account plan — surfacing stakeholder roles and how contacts connect — so your team starts with a foundation, not a blank page." Demo shows per-stakeholder stance labels (supporter / neutral / champion / blocker / influencer) × influence levels (high / medium / low), generated from CRM contacts.
- Who it serves: Sales Leadership ("Every strategic account is multi-threaded — not riding on one contact"; "Relationship gaps and blockers surface before deals stall"; "One consistent account-planning process across the team"); Revenue Operations ("A repeatable account-planning process inside Salesforce"; "Reporting on coverage, deal risk, and priority accounts"; "Account knowledge retained when reps leave"); Key Account Leaders ("Whitespace and expansion opportunities mapped across every account"; "At-risk accounts spotted early"; "Account knowledge stays in the CRM, not in one rep's head").
- Verticals: medical devices, healthcare/pharma, high tech, professional services, industrial, financial services. Named customers: Boston Scientific, Medtronic, Gong, Parexel, A-LIGN, CoverMyMeds, Equinix, Rocket Software.

### Gainsight (evidence layer A — official product pages; boundary pole)

- Positioning: "The Customer Retention Platform"; Customer Success platform for retention, expansion, efficiency. Center of gravity: health scores, product usage, support history, renewal timelines, stakeholder maps, AI sentiment — adoption/retention operations across the customer base.
- Success Planning & Playbooks: "Create AI-generated Success Plans tied to real business outcomes… Guide teams with repeatable, collaborative playbooks that bring you and your customer together to achieve their goals."
- Success Planning page: "Capture customer goals, correlate activity to outcomes, and ensure end-to-end value realization"; "Guide your customers towards their desired outcomes" — capture customer goals, track activity, share progress; triggered CTAs; templates for repeatable value realization.
- Notably uses the words: "Use prescriptive account plans to make expansion a reality" — trigger success plans at lifecycle milestones; AI-powered playbooks; coordinate actions across multi-channel engagements.
- Business reviews: "Empower CSMs to quickly and easily create business review presentations at scale with Success Snapshots"; "Create visibility and alignment for both leadership and customers."
- Renewals & Expansion: renewal likelihood/risk continuously updated; expansion signals scored; "qualified leads directly into your CRM, so Sales and CS work from the same picture."

### LinkedIn Sales Navigator (evidence layer A — official product page; thin pole)

- Account IQ: "Streamline account research with AI-driven insights"; "Quickly prepare high-level account plans and prioritize your time." Customer quote: "create a pre-sales document, org chart, and share details about the account in minutes — not hours."
- Relationship Map: "a clear view of key decision-makers within an account, helping you build stronger, multi-threaded relationships and move deals forward."
- Account Pages / Account Hub: account insights, buyer intent, prioritization. Notes: "capture and store key details and action items directly on lead and account pages."
- CRM integrations (Salesforce, Dynamics 365, HubSpot, Oracle) on higher tiers.
- Observation is page-level: the presented capabilities are insight/mapping/notes-oriented; the page does not present a structured plan object (objectives/whitespace/owned action tracking). Absence on a marketing page is not proof of absence in the product; treated as "thin embedded layer" with reduced assertion strength.

## Cross-product Comparison

| Structure / capability | Kapta | Altify | Prolifiq | Gainsight | LinkedIn SN |
|---|---|---|---|---|---|
| Plan anchored to a named account | Y | Y | Y | Y (success plan per customer) | Y (account pages) |
| Persistent structured plan object (objectives) | Y ("customer goals… milestones") | Y ("objectives, actions and customer insights") | Y ("Master Account & Opportunity Plans… Objectives") | Y (success plans tied to outcomes) | – (notes only, page-level) |
| Stakeholder/relationship map | Y (org charts, power centers, blockers/champions) | Y (relationship map, influence lines, strength) | Y (org chart, influence levels, stance badges, relationship lines) | Y (stakeholder maps) | Y (relationship map) |
| Relationship coverage / strength assessment | Y ("where you're strong versus exposed") | Y (strength indicators, gaps) | Y (influence levels, coverage reporting) | partial (engagement signals) | partial (multi-thread view) |
| Owned actions / milestones with tracking | Y ("ownable action items… on time, on strategy") | Y (actions; assign ownership) | Y (Team Tasks, Key Dates) | Y (CTAs, playbooks, activity) | partial (notes/action items) |
| White space / cross-sell mapping | Y (whitespace analysis by product line / BU) | Y (opportunity map, whitespace) | Y (cross sell maps) | partial (expansion signals) | – |
| Plan/account health or score | Y (health scores) | Y (relationship strength; deal/account reviews) | Y (Account Plan Score) | Y (health scorecards) | – |
| Team collaboration on the plan | Y (whole-team alignment) | Y (revenue-team reviews; Slack/Google Docs) | Y (team tasks; RevOps standardization) | Y (collaborative playbooks) | partial (team lists) |
| Review cadence (QBR / plan review) | Y (QBR workflows, tracked over time) | Y (deal and account reviews) | implied (reportable reviews) | Y (business reviews, snapshots) | – |
| CRM relationship | integration (multi-CRM) | 100% Salesforce-native | 100% Salesforce-native | CRM sync (leads into CRM) | embeds in CRM (higher tiers) |
| Customer-facing outputs | Y (reports to clients and C-suite) | – (not evidenced) | – | Y (snapshots for customers) | – |
| Renewal/contract visibility | Y (contracts, renewal playbooks) | – (not evidenced on pages) | – | Y (renewal timelines) | – |
| AI assistance | Y | Y (MaxAI) | Y (AI-generated maps/plans) | Y (AI-generated plans) | Y (Account IQ) |
| Methodology/templates | Y (customizable templates; KAM training arm) | Y (embedded methodology, TAS heritage) | Y (SWOT; structured framework) | Y (playbooks) | – |

Legend: Y = directly observed on official pages; partial = related capability observed, structure not evidenced; – = not evidenced on fetched pages.

Cross-product reading:
- Objectives + stakeholder map + owned actions co-occur in every planning-centric product (Kapta, Altify, Prolifiq) and have direct analogs in the CS pole (Gainsight success plans) and the thin pole (notes/action items). This trio is the strongest candidate for the defining structure.
- White space is present in all three planning-centric products but absent (as structured machinery) from the thin pole and only signal-level in the CS pole → common mature structure, not definitional.
- CRM linkage is universal, but its form varies (integration vs native vs embedded) → the *linkage* is common; the *form* is variant.
- Health/score machinery appears in 4/5 → common mature.
- AI appears in 5/5 → era-current common, not definitional (historical check below).
- Collaboration and review cadence appear in all planning-centric products → common mature workflow, not a structure.

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being a strategic account planning platform:

1. **The named strategic account as planning subject.** The plan is anchored to one identified customer organization — a high-value/key account — not to a deal, a territory, or a segment. (Remove → generic project planning or territory planning.)
2. **The account plan as a persistent structured object of record.** Relationship/growth objectives held in the system, versioned and refreshed over time — not a slide deck or a CRM field. (Remove → CRM account record or a document.)
3. **The stakeholder/relationship map of the customer organization.** People at the customer with roles, influence, stance, and the vendor team's coverage/strength against them, held as structured data tied to the plan. (Remove → account research/insight tooling; the "who" layer is the signature structure.)
4. **Owned actions executing the plan.** The plan is worked: actions/milestones with owners and dates, tracked against objectives. (Remove → a research dossier or an org-chart viewer; the "plan" stops being a plan.)

Jointly-held is load-bearing: structures 2+4 without 3 = generic goal/task planning; 3 without 2+4 = relationship mapping/intelligence tooling; 1+3 without 2+4 = account research workspace; 2+3 without 4 = a static dossier.

The plan's purpose — protect and grow the account's value over a multi-year horizon — is carried by structure 2 (objectives) and does not need a fifth structure.

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- White space / cross-sell / up-sell mapping (current vs potential footprint, often product line × business unit)
- Plan/account health scoring and relationship-strength indicators
- CRM linkage (accounts, contacts, opportunities as the data substrate)
- Cross-functional team collaboration on the plan (shared visibility, comments, task assignment)
- Review cadence support: plan reviews, QBRs, business reviews; leadership/C-suite reporting
- Templates and methodology frameworks (SWOT, buying-center roles, KAM/TAS-style processes)
- Renewal/contract visibility feeding the plan
- AI assistance (map/plan generation, "what changed / what's at risk / what to do next")
- Reportable plan objects (plans, maps, actions as queryable/reportable data)

### L2 — Variant / Optional Structure

- Deployment posture: standalone platform (Kapta) vs CRM-native app (Altify, Prolifiq) vs suite module (Gainsight) vs embedded insight layer (LinkedIn Sales Navigator)
- Sales-led vs post-sales KAM-led vs CS-adjacent orientation of the same plan structure
- Vertical tuning (med device/pharma emphasis observed in one product)
- Methodology packaging (TAS heritage in one; KAM training ecosystem in another; market-wide methodology brands like Miller Heiman LAMP exist as context, not sampled products)
- Depth of adjacent modules: opportunity/deal management with pre-revenue stages, contract/renewal management, voice-of-customer/sentiment capture
- Customer-facing plan outputs (shared reports/reviews with the customer)
- Org-chart-first vs influence-graph-first representation of the stakeholder layer

### L3 — Vendor-specific (kept out of the final document)

- Kapta: "system of action" positioning; QBR Rating; KAMGenius training; named integration list; specific health-signal list.
- Altify: MaxAI; Insight Map / TeamView / Opportunity Map module names; "3x win rate with 6+ supporters" and "36% deal size" claims; execution services; Storylane demos.
- Prolifiq: CRUSH brand; Omni View; Sayge Solutions ownership; AppExchange listing IDs; named customers.
- Gainsight: Staircase AI; Atlas agents; Success Snapshots; Agent Studio; MCP; specific stat claims (60%+ capacity, 20%+ churn reduction).
- LinkedIn: InMail, TeamLink, Smart Links, plan-tier gating (Advanced / Advanced Plus), specific stats (5x connections, 65 hours saved).

## Rejected Findings

- "Account planning software = CRM feature." Rejected: two standalone products define themselves against CRM record-keeping; even CRM-native products add a plan object the CRM lacks. The plan-of-record vs record-of-account distinction held across the sample.
- "White space analysis is definitional." Rejected to L1: absent as structured machinery at the thin pole; the minimal plan (objectives + people + actions) remains recognizable without it.
- "AI-generated plans are definitional." Rejected to L1/era-current: the historical check (below) shows the Type's structures predate AI entirely.
- "Account planning is a sales-only concern." Rejected: post-sales KAM pole (Kapta) and CS pole (Gainsight) both plan customer relationships; the orientation varies, the structure holds.
- "Success plans (CS) are the same Type." Rejected as identity, retained as boundary pole: same plan anatomy (goals + actions), different center of gravity (customer outcome realization vs vendor-side growth planning) and different operating population (CSM vs account team). See Boundary Findings.

## Historical / Market-Sample Check

Would older, regional, or pre-software practice still fit the L0?

- Pre-software key account management: account plans maintained as binders/dossiers — customer background, hand-drawn org charts with color-coded relationship ratings, relationship objectives, action lists, quarterly reviews. All four L0 structures present with zero software.
- Methodology era (1990s): Miller Heiman's LAMP (Large Account Management Process) formalized the same structures as paper/workshop practice — background, relationship map, objectives, action plans, review cadence. (Methodology cited as market context, not a sampled product.)
- The modern additions — CRM linkage, whitespace matrices, health scores, AI generation — are all L1/era-current, not definitional.

Historical check: passed. L0 contains no cloud, AI, CRM-integration, or whitespace-matrix dependencies.

## Boundary Findings

- **vs CRM / Account Management CRM.** CRM is the system of record for accounts, contacts, activities, and deals. The planning platform holds the *plan* — objectives, stakeholder map, actions — as its object of record, and treats the CRM as data substrate. Kapta's whole positioning is this seam ("CRMs were built for record keeping"); Altify and Prolifiq live inside Salesforce precisely because the CRM lacks the plan object. Test: remove the plan object → you have a CRM; remove the record-keeping substrate → you have planning. Boundary: adjacent, complementary.
- **vs ABM Platform.** ABM orchestrates marketing campaigns against lists of target accounts (often pre-sale, intent/anonymized data). Account planning is vendor-team-side planning of a named, usually existing, high-value relationship. Test: remove the named-account plan and add campaign orchestration over account lists → ABM. Boundary: different actor (marketing vs account team), different object (campaign vs plan), different lifecycle stage.
- **vs Customer Success Platform.** Gainsight demonstrates the drift zone: success plans share the plan anatomy (customer goals + actions + reviews) and even borrow the name ("prescriptive account plans"). The distinction is the center of gravity: CS plans the *customer's* outcome realization with the product (adoption, health, renewal) across the whole customer base; strategic account planning plans the *vendor's* growth of a named relationship (coverage, white space, expansion) with the account team as operator. Test: strip adoption/health/renewal operations and keep only the plan → the plan layer is shared; keep them → CS platform. Boundary: adjacent with a genuinely shared substructure; naming collision noted.
- **vs Opportunity / Pipeline Management.** Deal-centric, single-transaction horizon, revenue-attribution governed. Account planning is account-centric, multi-year, and explicitly tolerates pre-revenue work (one product tracks stakeholder alignment, pilots, business-case development before revenue attribution). Test: the unit of progression is the deal vs the relationship. Boundary: adjacent; account plans feed opportunities.
- **vs Territory Management.** Territory management allocates and balances portfolios of accounts; account planning goes deep on one account. Portfolio vs depth.
- **vs Sales Intelligence / Prospecting.** Intelligence products research accounts/people (firmographics, signals); planning platforms turn that context into a committed plan with objectives and owned actions. Insight vs commitment.
- **vs generic workspace/whiteboard/deck tools.** Teams do write account plans in slides and spreadsheets — the sample's own anti-pattern language ("spreadsheet tribal knowledge", "rebuilding coverage maps in spreadsheets", "last quarter's story") names this. The platform differs by holding the plan as structured, linked, reportable data connected to CRM records and live activity. Test: unlink the plan from account/people/opportunity data and make it unstructured → a document, not this Type.

## Uncertainties

- Revegy (a known pure-play in this space) could not be reached; the pure-play pole rests on Kapta alone plus two Salesforce-native products.
- Salesforce's first-party account planning capability could not be verified (help center error, marketing 404). The CRM-embedded pole is evidenced via third-party Salesforce-native apps only.
- No Tier 1 help-center/user-guide documentation was reachable for any sampled product; all observations are from official product/marketing pages. Consequently, in-app operational details (exact field names, step sequences, permission models, numeric limits) are NOT asserted anywhere in the final document.
- LinkedIn Sales Navigator evidence is page-level; its full internal capability set (beyond presented features) is unverified.
- Gainsight's "prescriptive account plans" phrasing is treated as naming-collision evidence for the boundary discussion, not as proof of full account-planning functionality.
- Pricing, packaging, and plan-tier details were not researched (not needed for the Type definition).
- Vendor outcome claims (win-rate multipliers, retention percentages) were recorded but never generalized.

## Final Synthesis

A Strategic Account Planning Platform is the account team's planning system of record for a named strategic account. Its defining core is four jointly-held structures: the named account as planning subject; the persistent structured plan (relationship/growth objectives); the stakeholder/relationship map of the customer organization with coverage assessment; and owned, tracked actions executing the plan. Around that core, mature products add white-space mapping, health/score machinery, CRM linkage, team collaboration, review cadences (plan reviews/QBRs), templates and methodology scaffolding, renewal visibility, and AI assistance. The Type spans a deployment spectrum — standalone platform, CRM-native app, suite module, embedded insight layer — and a orientation spectrum from new-logo account-based selling to post-sales key account management. Its nearest neighbors are CRM (the record substrate it plans on top of), Customer Success (which shares the plan anatomy but centers customer outcome realization), and ABM (which shares the account unit but is marketing-side campaign orchestration). The historical check confirms the core predates all modern machinery: a binder with an org chart, objectives, and an action list is already this Type.
