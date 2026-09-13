# Research Notes — SaaS Management

## Research Goal

Understand, from real products, what a SaaS Management application is: what lives inside it, what its defining structure is, how the estate-management loop actually flows, and how it differs from the neighboring types it converges with (IT Asset Management, FinOps, SSPM, Application Portfolio Management, ITSM, Spend Management, TEM).

Counterparty obligations carried into this pass:
- **it-asset-management** (processed 2026-09-08) left a sibling note: expected seam = "SaaS-subscription-first objects (subscriptions/usage/spend/optimization as the estate itself) vs ITAM treating subscriptions as one asset class among many"; this pass must test whether subscription management is ITAM variant-breadth or a distinct Type.
- **endpoint-management-uem** (processed 2026-09-08) noted: "saas-management: distinct objects (SaaS subscriptions/usage vs devices)."

## Initial Boundary

Initial hypothesis: SaaS Management is the IT/finance-side application whose object is the organization's own SaaS application estate — discovering which SaaS apps are in use, holding subscription/license/spend facts, allocating seats to users, tracking usage, optimizing licenses, managing renewals, and executing lifecycle actions (provision/deprovision access).

Nearest neighbors: IT Asset Management (§14, processed), Cloud Cost Management / FinOps (§14), Application Portfolio Management (§14), SaaS Security Posture Management / SSPM (§15), IT Service Management (§14, processed), Spend Management (§8), Telecom Expense Management (§19), SSO/IAM (§15).

## Research Questions

1. What is the central object — the app record? What facts does it carry (vendor, contract, spend, renewal, seats, owner, status)?
2. How is the estate discovered (SSO/IdP scan, expense scan, browser extension, direct integrations, agent, manual)?
3. How are users allocated to apps (seats/licenses), and how does usage data attach?
4. What lifecycle actions exist (provision/deprovision, license reclamation, renewal management, cancellation)?
5. What optimization loop exists (unused licenses, right-sizing, consolidation, savings tracking)?
6. What roles use it (IT, procurement, finance, security, app owners)?
7. What are the seams vs ITAM / FinOps / SSPM / APM / ITSM / spend management?
8. Is there a recognized market category? (Gartner MQ "SaaS Management Platforms", G2 SMP category.)

## Representative Products

| Product | Pole | Customer tier | Status |
|---|---|---|---|
| Zylo | pure-play enterprise SMP; "system of record for software & AI spend"; finance-grade | enterprise | active; Gartner MQ Leader for SMP 2024/2025/2026 |
| Torii | automation-first SMP for IT/procurement/security; deep Tier-1 API docs | scale-up → enterprise | active; Gartner MQ Leader 2026 |
| Flexera One SaaS Management | SAM incumbent's dedicated SaaS-management product line (Snow Software absorbed into Flexera) | large enterprise | active; Gartner MQ Leader 2026 |
| BetterCloud | SaaS-operations pole: user automation, file governance, spend optimization | mid-market/enterprise IT | active; G2 SMP Momentum Leader |
| Cledara | finance-led SMB pole; payments/virtual cards + application directory | SMB/startup | active; G2 SMP EMEA Leader |

Dropped: **Productiv** — ceased operations August 6, 2026 (wind-down notice on productiv.com); platform access terminated, data destroyed. Recorded as a market-consolidation signal, not usable as evidence.

## Sources

Research date: **2026-09-09**. All sources fetched live on this date.

- Zylo — homepage https://www.zylo.com/ ; product page https://www.zylo.com/product/ (Tier 2)
- Torii — homepage https://www.toriihq.com/ ; SMP product page https://www.toriihq.com/products/saas-management-product (Tier 2); API documentation index + reference https://developers.toriihq.com/llms.txt , https://developers.toriihq.com/reference/introduction-1 (Tier 1 — official operational/API documentation)
- Flexera — Flexera One SaaS Management product page https://www.flexera.com/products/flexera-one/saas-management (Tier 2); snowsoftware.com URL redirects to Flexera (absorption observed)
- BetterCloud — homepage https://www.bettercloud.com/ (Tier 2)
- Cledara — homepage https://www.cledara.com/ ; "What is SaaS Management" guide https://www.cledara.com/saas-management (Tier 2)
- Productiv — wind-down notice https://www.productiv.com/ (market note)

Sourcing limitations: Torii support docs (support.toriihq.com) timed out ×1; Tier-1 depth obtained instead from Torii's official developer/API documentation. Zylo/Flexera/BetterCloud/Cledara evidence is product-page level (Tier 2); no Tier-1 help-center articles were fetched for them. Per evidence rules, no precise numeric limits, default values, or state-machine details are asserted for those products beyond what their pages state.

## Product Observations

### Zylo (evidence layer A unless noted)

- Self-positioning: "The Leading Enterprise SaaS Spend Management Platform"; "The System of Record for Software & AI Spend"; "financial-grade visibility". Gartner MQ Leader for SaaS Management Platforms 2024/2025/2026 (vendor-stated).
- Discovery: "AI-powered discovery continuously analyzes financial systems—including ERP, accounts payable, and expense platforms—to identify software purchases entering the organization. Proprietary machine learning models match spend to applications and automatically categorize them." (A)
- Four pillars: Establish Complete Visibility / Control Ongoing Software Costs / Turn Renewals into Savings / Ensure Governance & Audit Readiness. (A)
- Objects surfaced on dashboards: applications with annual payments and users (Salesforce CRM, Microsoft 365, Zendesk, Google, Okta shown), total/projected cost with actual-vs-forecast lines, identified vs realized savings, upcoming subscription renewals on a calendar, apps without owners, apps not reviewed. (A, screenshots)
- License economy: "40M+ licenses normalized & tracked"; case study: ModMed "avoided $1.4M in unnecessary costs by reclaiming 2,800 unused licenses via automation". (A, vendor claims)
- Users/personas: For IT & SAM, For FinOps, For Procurement. Use cases: shadow IT, renewal savings, license waste, AI costs, cost allocation, application redundancy, M&A. (A)
- Governance: "Application ownership, contract terms, license entitlements, and spend data are documented in one place… enforce software policies, demonstrate compliance, and prepare defensible records for internal reviews and external audits." (A)
- Category boundary, vendor-stated FAQ: "ITSM, procurement, and finance systems track parts of the software lifecycle but rarely provide a complete view of SaaS spend. A SaaS Management Platform like Zylo connects financial data, contracts, licenses, and usage insights in a single system of record." (A)
- AI extension: AI consumption cost management, Clarity AI assistant, MCP interface. (A)

### Torii (evidence layer A; API docs = Tier 1)

- Self-positioning: "SaaS Management for IT, Procurement, and Security"; "discovers your entire SaaS and AI stack, reclaims wasted spend, and automates onboarding and offboarding — all from one place." Gartner MQ Leader 2026 (vendor-stated).
- Four capability areas: Continuous App Discovery / Seamless Access Management / Continuous Cost Optimization / Cost Control for AI Tools. (A)
- Discovery sources (architecture diagram): identity & people (IdP, HRMS, MDM, directory), finance & procurement (ERP, accounting, expense, contracts), ops & apps (ticketing, assets, endpoints), shadow-IT signals (browser extension, OAuth grants, unsanctioned usage). "Hundreds of pre-built integrations, an AI builder, API or CSV." (A)
- Central layer: "Software Intelligence Database — Every app, license, identity, contract and cost, in one source of truth." (A)
- License-level usage: "Torii ties each app to license-level usage by tier, true ownership, and contract terms, so Procurement and IT can right-size against what people actually use. You see what to downgrade, reclaim, or cut, with the savings impact of each." FAQ: "A login tells you someone opened an app, not whether they use the seat you are paying for." (A)
- JML automation: "no-code workflow. The right apps and group memberships get provisioned on day one, adjusted when someone changes roles, and fully revoked on the last day, including the apps your IdP never saw. Every step is logged." (A)
- Tier-1 API object model (developers.toriihq.com):
  - **Apps**: "list of apps used in the organization", filterable by `state=discovered`; custom app fields; `includeLicenses=true` aggregated license summary; app catalog search; "similar apps" endpoint (redundancy detection); app fields predefined + custom.
  - **Licenses** (custom-integration file schema): license = {name (tier, e.g. Pro/Basic/Corp), unassignedAmount, users[{email, licenseStatus: active/inactive/deleted}], pricePerUser}; user = {email, externalStatus, roles, lastUsedDate}.
  - **Contracts**: bound to app (`idApp`), status (active), amount + currency, custom contract fields; CRUD.
  - **Transactions**: recognized expense transactions mapped to apps (`idApp`), mappingStatus mapped/unknown/archived; expense-file parsing (automatic/manual column matching).
  - **Workflows**: triggers include "User meets criteria", "User joins", "User left", "Closed app in use", "License not in use", "App event", "Application meets criteria", "New app discovered", "Contract meets criteria"; action execution logs; workflow edit history.
  - **Access request policies**: approvalFlow, eligibilityGroups, accessDurationsConfig; eligibility enforced (400 NOT_ELIGIBLE_FOR_POLICY).
  - **Access review campaigns**: bucketed executions, per-app CSV/PDF report ZIPs.
  - **Browser extension settings**: dlp, blockedSites, usersFilter.
  - **Audit logs**, **user anonymization requests** (GDPR), **SCIM users**, **plugins/custom integrations**.
  - AI-assisted classification guides: SSO classification (Yes/No/Not Supported/Not Known), hosting type (SaaS/On-Prem/PaaS), AI module classification (AI Native/AI Enabled/No AI).
- Competitive set (vendor's own alternatives pages): Zylo, BetterCloud, Zluri, Productiv, Flexera/Snow Software. (A)

### Flexera One SaaS Management (evidence layer A)

- Positioning: "Flexera's market-leading SaaS management solution to detect known and shadow SaaS and AI waste"; "See every SaaS app, seat and dollar spent… Reclaim unused seats, renegotiate with evidence, and shut down shadow SaaS before the next renewal cycle." Gartner MQ Leader 2026, second year in a row (vendor-stated).
- Capabilities: comprehensive SaaS and AI discovery "using multiple discovery methods - including financial data, API connectors (including a Universal Connector), browser extension, connections to SSO and CASB technologies and the Flexera agent"; deep usage insights across known and shadow apps (application recognition/enrichment database); hybrid application usage and cost metrics (online + installed usage for Microsoft 365, Adobe Creative Cloud); actionable optimization recommendations (underused licenses, downgrade from expensive bundles); renewal and contract management (AI-based invoice/contract ingestion; SAP Concur, Coupa integrations); unified SaaS, ITAM and FinOps insights. (A)
- How-it-works: "continuously discovers, analyses, and optimizes your SaaS environment": 1. Discover everything in use (expense, SSO, HR systems) → 2. Analyze usage, spend, and risk → 3. Optimize and take action (right-size licenses, eliminate unused applications, improve renewal outcomes). (A)
- Lifecycle: FAQ — "apply policies, automate workflows, and manage the full SaaS lifecycle - from onboarding to offboarding." (A)
- **Seam evidence**: Flexera ships SaaS Management and IT Asset Management as separate solution areas of the same platform, with separate product pages and separate datasheets; FAQ: "Flexera goes beyond standalone SaaS management by bringing SaaS, IT asset management (ITAM), and FinOps together in a single platform." The SAM incumbent itself treats SaaS Management as its own discipline. (A)
- Snow Software absorbed: snowsoftware.com redirects to Flexera; Snow Atlas listed as a separate login. (A)

### BetterCloud (evidence layer A)

- Positioning: "The world's only end-to-end SaaS Management Platform"; "Govern every SaaS app, user and AI agent in one platform… a single intelligent workspace to understand, act on, and govern everything (users, apps, spend, and AI actors)." (A)
- Modules: IT Agent (natural-language query + human-in-the-loop actions with approval and reverse); User Automation (no-code drag-and-drop workflow builder; onboarding/offboarding automation; library of hundreds of workflow actions, triggers, templates); Workspace Management (Google); Spend Optimization ("full visibility into what you're spending, what you're using, and what you can cut, before it auto-renews"; eliminate redundant subscriptions, reclaim unused licenses, benchmark spend, surface shadow IT); File Governance (scan files, user roles and granular permissions per SaaS app). (A)
- Integration scale: "100+ integrations and 1,000+ actions provided out-of-the-box." (A, vendor claim)
- Use cases: onboarding & offboarding automation, security & compliance, SaaS cost control, M&A, shadow IT/shadow AI. (A)
- Primary user: IT teams. (A)

### Cledara (evidence layer A)

- Positioning: "The SaaS Management Platform for Spend & Risk"; "Software Subscription Management, built for Finance." G2 SMP EMEA Leader, SaaS Spend Management Small-Business leader badges. (A)
- Definition (vendor guide): "SaaS management is the process of managing the cloud-based software applications for your company. This includes managing your SaaS spend, performing the necessary admin tasks like tool onboarding and bookkeeping, and monitoring risks linked to third party tools." (A)
- **The SaaS management journey** (vendor's own four-step lifecycle): Discover → Buy → Manage → Cancel. (A)
- Application Directory: "a complete directory of your software tools"; UI shows per-app usage level and renewal date; approved vs unapproved app status. (A)
- Pipeline: purchase requests → approvals → budgets → usage alerts → payments (virtual cards, spend limits, cancel in a click) → invoices (auto-captured, synced to accounting) → reimbursements. (A)
- Usage & security: Cledara Engage (software usage data), Onboarding (manage access to every tool), Software Security, Software Compliance (vendor certifications, questionnaires, ISO27001/SOC2 templates). (A)
- **Pre-software baseline documented by the vendor**: "In the very early stages of a startup, software subscription information typically lives in a spreadsheet… this is not a great long term solution, as a spreadsheet won't scale with you as you grow." Spreadsheet failure modes: no reliable source of truth, manual admin, payment risk, limited usage visibility. (A)
- Users: Finance, Procurement, IT, Operations. (A)

## Cross-product Comparison

| Structure | Zylo | Torii | Flexera One SM | BetterCloud | Cledara | Strength |
|---|---|---|---|---|---|---|
| SaaS app inventory of record (per-app records w/ commercial facts) | A | A (Tier-1) | A | A | A | Core (5/5) |
| Multi-source discovery (finance/expense + identity + direct integrations + browser/agent signals) | A (ERP/AP/expense) | A (Tier-1: IdP/HRMS/ERP/expense/browser/OAuth) | A (expense/SSO/HR/browser/agent/CASB) | A (implied; 100+ integrations) | A (payments-side capture; directory) | Core-mechanism (5/5, methods vary) |
| License/seat allocation to identified users | A (40M+ licenses; reclamation) | A (Tier-1 license objects: tier, unassigned, per-user status, price) | A (seats, right-size) | A (reclaim unused licenses) | A (underused seats) | Core (5/5) |
| Usage evidence attached to allocation | A (active users, usage trends) | A (Tier-1 lastUsedDate; license-tier usage) | A (usage insights, hybrid installed+online) | A (what you're using) | A (Engage usage data) | Core (5/5) |
| Contracts/renewals bound to apps | A (renewal calendar, contract ingestion) | A (Tier-1 contracts CRUD, renewal triggers) | A (AI invoice/contract ingestion, Concur/Coupa) | A (before it auto-renews) | A (renewal dates, renegotiation) | Core (5/5) |
| Optimization loop (reclaim/downgrade/consolidate/cancel + savings) | A | A (Tier-1 "License not in use" trigger) | A | A | A (cancel in a click, duplicates) | Core (5/5) |
| Access lifecycle (provision on join / revoke on leave) | A (deprovision workflows shown) | A (Tier-1 JML triggers) | A (FAQ: full lifecycle onboarding→offboarding) | A (flagship module) | A (onboarding module) | Core-family (5/5, depth varies) |
| Governance: owners, sanctioned/unsanctioned status, approvals | A (app owners, % without owners) | A (Tier-1: owners, discovered state, access policies) | A (unsanctioned apps dashboard) | A (approval processes) | A (approved/unapproved) | Core-family (5/5) |
| Access requests / reviews (ITSM-like) | not observed at page level | A (Tier-1) | not observed | A (roles/permissions) | A (access requests) | Common (3/5 confirmed) |
| Spend/payment execution (virtual cards, limits) | not observed | not observed | not observed | not observed | A (flagship) | Variant pole (1/5) |
| Security posture depth (file governance, DLP, blocked sites) | not observed | A (extension dlp/blockedSites) | A (risk framing) | A (file governance module) | A (software security module) | Variant drift (4/5, shallow) |
| AI-spend management (2026-era extension) | A | A | A | A | A (AI strategy content) | Common-new (5/5, emerging) |
| Benchmarking against market data | A ($75B dataset) | A (benchmarking) | not observed | A (industry data) | A (Data Hub) | Common (4/5) |
| Cost allocation / chargeback | A (allocate costs use case) | A (org drill-downs) | A (FinOps alignment) | not observed | A (budgets) | Common (4/5) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The SaaS application estate as inventory of record** — persistent, individually identified records, one per SaaS application/subscription the organization uses or pays for, each carrying its commercial facts (cost/spend, contract terms, renewal date, license quantities) and its governance facts (owner, sanctioned/unsanctioned status, category). Remove → an expense feed or spreadsheet with no app-level estate.
2. **The seat allocation with usage evidence** — the estate's licenses/seats are held against identified users, with usage evidence (last used, activity level, license tier) attached to the allocation. Remove → a subscription-bill tracker; the seat economy that makes optimization possible is gone.
3. **The estate-management loop** — the system drives recurring decisions and actions on the estate: rationalization (duplicates/overlap), license optimization (reclaim, downgrade, right-size), renewal management (review/negotiate before renewal, cancel), and access lifecycle (provision on join, adjust on move, revoke on leave). Remove → a static register or dashboard; the "management" gone.

Jointly-held load-bearing:
- 1 alone = SaaS spreadsheet / static asset register (the documented pre-software baseline)
- 2 without 1 = per-app seat lists with no estate context
- 3 without 1+2 = generic spend-cutting advice
- 1+2 without 3 = visibility/reporting without action
- 1+3 without 2 = portfolio-level rationalization without seat-level action (drifts toward APM)
- 2+3 without 1 = scattered license cleanups with no system of record

### L1 — Common Mature Structure (not definitional)

- Multi-source automated discovery (finance/expense systems, SSO/IdP, HRIS, direct API integrations, browser extension, endpoint agent, CASB feeds, OAuth-grant scans) — universal in current products, but the spreadsheet baseline shows the Type predates automation; discovery is the mature mechanism for populating leg 1, not the definition.
- Usage analytics depth (active users, license-tier usage, hybrid installed+online usage)
- Renewal calendars, alerts, savings tracking (identified vs realized)
- App categorization, vendor normalization, benchmarking data
- Dashboards/reports; audit trails; role-based access to the SMP itself
- AI-spend management (fast-converging 2026 extension across all five sampled)

### L2 — Variant / Optional Structure

- Access request/approval workflows and access reviews (ITSM-like machinery; deep in Torii/BetterCloud/Cledara, lighter elsewhere)
- Spend/payment execution: virtual cards, spend limits, one-click cancel (Cledara pole)
- Procurement intake/purchasing approval flows (Cledara, Zylo-for-procurement)
- Security-posture extensions: file governance, DLP in browser extension, blocked sites (drift toward SSPM)
- Compliance machinery: vendor certification checks, questionnaires, ISO27001/SOC2 templates (Cledara)
- Non-human identities / service accounts (Torii)
- Cost allocation/chargeback to business units; M&A support
- Employee self-service app catalog
- Estate breadth: desktop apps and hybrid (installed+online) applications alongside pure SaaS (Torii, Flexera)
- Agentic/natural-language interfaces (BetterCloud IT Agent, Torii Eko/MCP, Zylo Clarity AI)

### L3 — Vendor-specific (research notes only)

- Torii: "Software Intelligence Database", Collect/Refine/Act-and-Monitor engine stack, Eko agentic engine, `state=discovered` app-state vocabulary, SSO/hosting/AI classification GPT actions, "SSO tax" analysis guide
- Zylo: $75B+ spend dataset, Clarity AI, SaaS Negotiator service, SaaS Operations managed service, 2026 SaaS Management Index
- Flexera: Technopedia knowledge catalog, Universal Connector, Snow Atlas lineage, hybrid-usage recognition database
- BetterCloud: 3x-ROI-in-90-days guarantee, IT Agent, Workspace Management for Google
- Cledara: Modulr/PayrNet card issuance rails, Data Hub, software marketplace
- Vendor research stats (not asserted as facts): Zylo "476 SaaS renewals/year average"; Cledara "57 subscriptions average, 20+ unknown", "45% believe they overspend"; Flexera "pay for 2–3× more SaaS than they use"

## Historical / Market-Sample Check

- **Spreadsheet baseline**: Cledara's own guide documents that software subscription tracking starts as a spreadsheet (app name, cost, renewal, seat holder) — satisfying leg 1 and a manual form of leg 3 at analog level. The Type's definition therefore cannot require automated discovery, cloud delivery, or AI.
- **Early-2010s generation**: manual SaaS portfolio trackers and license registers (renewal calendars + seat lists) fit all three legs without discovery automation.
- **SAM-incumbent lineage**: Flexera/Snow's SaaS management descends from software-license management; it fits the same three legs with discovery methods extended by agents/CASB.
- **Regional/tier spread**: US enterprise (Zylo, Flexera), Israel-origin scale-up (Torii), US mid-market IT ops (BetterCloud), UK SMB finance (Cledara) — all fit.
- Conclusion: no modern machinery (browser-extension discovery, AI, virtual cards, agentic interfaces) enters L0.

## Vendor-specific Findings

See L3 above. Notable market facts: Gartner has published a Magic Quadrant for SaaS Management Platforms since at least 2024 (Zylo, Torii, Flexera named Leaders 2026 by the vendors themselves); G2 maintains an SMP category. Productiv's August 2026 cessation shows consolidation. Torii's own alternatives pages treat Zylo/BetterCloud/Zluri/Productiv/Flexera-Snow as one competitive set — the market itself recognizes a single Type.

## Boundary Findings

**vs IT Asset Management (counterparty obligation — DISCHARGED):**
- ITAM's inventory spans hardware + software licenses + subscriptions as asset classes, with acquisition→retirement lifecycle and entitlement reconciliation. SaaS Management's estate is SaaS-app-first: the unit is the application subscription with its seat allocation and usage, and the daily loop is optimization (reclaim/downgrade/consolidate) + renewal + access lifecycle.
- Decisive seam evidence: Flexera — the SAM incumbent — ships **SaaS Management and IT Asset Management as separate solution areas** with separate product pages, datasheets, and FAQs. Subscription tracking inside ITAM products (AssetExplorer's Microsoft 365 subscriptions, Device42 cloud discovery) is variant breadth; the subscription-first discipline with seat/usage optimization is a distinct Type. Keep-both.
- Convergence zone: SaaS management products adding contract/procurement depth; ITAM products absorbing subscription tracking; unified platforms (Flexera One) bridging both. Zylo explicitly serves "IT & SAM" personas.

**vs Cloud Cost Management / FinOps:** FinOps's object is cloud infrastructure spend (compute/storage/commitments); SaaS Management's object is application subscriptions with seats and users. Convergence: vendors position "SaaS and cloud spend" together (Zylo "$75B+ in SaaS and Cloud spend"; Flexera unified platform); AI spend spans both. Distinct objects, adjacent disciplines.

**vs SSPM (SaaS Security Posture Management):** SSPM's object is security posture of sanctioned SaaS (misconfigurations, OAuth risk, data exposure); SaaS Management's object is the estate's commercial/operational lifecycle. Drift zone: browser-extension DLP/blocked sites (Torii), file governance (BetterCloud) — security capabilities inside SMPs; discovery feeds shared.

**vs Application Portfolio Management:** APM governs the application portfolio at strategy level (invest/retain/retire decisions, business capability mapping); SaaS Management operates the estate day-to-day (seats, renewals, access). A SaaS estate view can feed APM; the operational seat/usage/renewal loop is not APM.

**vs ITSM:** ITSM fulfills requests and runs service workflows; SaaS Management holds the estate those requests act on. Access-request machinery inside SMPs (Torii policies, Cledara access management) borrows ITSM patterns; Zylo's own FAQ draws the line: ITSM tracks "parts of the software lifecycle" but not the complete SaaS spend view.

**vs Spend Management / corporate cards:** Spend management's object is company spend in any category; SaaS Management's object is the software estate specifically (apps, seats, usage, renewals). Cledara straddles both (software payments + general spend) — the software-specific estate structures (licenses, seats, usage) are what make it SaaS Management.

**vs Telecom Expense Management:** historical sibling discipline (managing recurring service expenses); TEM's object is telecom services/devices, not the SaaS application estate.

**vs SSO/IAM:** IdPs control authentication and are a *discovery source* for SMPs; the SMP holds the estate record, not the identity plane.

**Remove-test:** remove the seat/usage allocation and optimization loop → ITAM-style subscription register or a spend dashboard; remove the SaaS-app binding (any vendor spend) → generic spend management; remove the estate record (discovery + actions only) → point solutions; remove the commercial facts (keep usage/access only) → IAM/SSPM territory.

## Uncertainties

1. App-state vocabularies beyond Torii's `state=discovered` not directly observed at Tier-1; state machines likely vary by product (held as implementation detail).
2. Whether access-request/review machinery is now universal: confirmed A-level in 3/5 (Torii Tier-1, BetterCloud, Cledara); not observed at Zylo/Flexera page level. Held as Common, not Core.
3. Discovery-source mixes vary (no browser extension claimed on Zylo's page; agent/CASB only at Flexera); the *multi-source principle* is cross-product, the exact source set is not.
4. Numeric market claims (average subscription counts, renewal counts, overspend percentages) are vendor-research figures — recorded in L3, not asserted.
5. Productiv's wind-down removes a formerly prominent usage-intelligence pole from the live market; its structural contribution (employee-centered usage data) is represented by survivors' usage features, but the pole itself is unsampled-live.
6. SSPM leaf (§15) unprocessed at time of writing; the seam recorded here is one-sided and should be ratified by that pass.

## Final Synthesis

SaaS Management is the organization's system of record and action loop for its own SaaS application estate. The defining core is three jointly-held structures: (1) the SaaS application estate as a managed inventory of record — one persistent identified record per application/subscription, carrying commercial facts (spend, contract, renewal, licenses) and governance facts (owner, sanctioned status); (2) the seat allocation with usage evidence — licenses held against identified users with usage attached, making waste visible and attributable; (3) the estate-management loop — recurring rationalization, license optimization, renewal management, and access lifecycle actions executed against that record. Everything else — multi-source discovery, usage analytics depth, benchmarking, AI-spend management, access requests, payments, security extensions — is common mature structure or variant, not definition. The Type is distinct from ITAM (which treats subscriptions as one asset class among many), from FinOps (cloud infrastructure), from SSPM (security posture), and from APM (strategy-level portfolio governance) — a separation the market itself maintains (Gartner SMP category; Flexera's own product split).
