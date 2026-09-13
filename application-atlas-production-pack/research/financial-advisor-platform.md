# Research Notes — Financial Advisor Platform

Research date: 2026-09-06
Slug: `financial-advisor-platform`
Directory leaf: Financial Advisor Platform (§08 Finance, Banking, Insurance & Investment)

---

## Research Goal

Understand what a Financial Advisor Platform actually is as an Application Type: the system financial advisors (planners, RIAs, wealth advisors) use to run their practice — not the institution-side wealth platform, not the consumer-facing money app. Produce a vendor-neutral canonical model: what exists inside it, what users do, how work flows, which rules matter, and where the boundaries with neighboring Types lie.

## Initial Boundary (hypothesis before research)

- Core use: advisor-side practice system — manage client relationships, hold the client's financial picture, produce and maintain advisory work products (plan / proposal / report).
- Primary users: financial advisor, paraplanner, operations/client service, compliance.
- Nearest neighbors: Advisor CRM (Redtail, Wealthbox), Portfolio Management System (Black Diamond, Addepar, Orion Portfolio Accounting standalone), Wealth Management Platform (institution-side), Robo-advisor (consumer self-service), Retirement Planning Application (slice), Personal Finance Management (consumer side), Financial Planning & Analysis Platform (corporate FP&A — false friend on the word "planning").
- Unknowns going in: Is the central object the client/household or the plan? Is account aggregation defining or common? Where exactly is the line to the portfolio-management Type?

## Research Questions

1. What is the central managed record — client, household, plan, account, portfolio?
2. How does client financial data enter the system (custodian feeds, aggregators, manual entry, client self-entry, document import)?
3. What is a financial plan made of (inputs, projections, scenarios, outputs)?
4. How does the advisor produce advice (proposal, what-if, recommendations) and how does it connect to account opening / implementation?
5. What reporting is produced, for whom, from what data?
6. What is the client-facing surface (portal, vault, tasks) and who controls it?
7. What practice-management layer exists (tasks, workflows, meetings, service requests, compliance)?
8. Which roles and permissions matter (advisor, planner, ops, compliance, firm leadership)?
9. How do billing / trading / rebalancing relate — core or adjacent modules?
10. How does the platform relate to custodians and to the surrounding tool stack?

## Representative Products

Selected for market position + documentation quality + different product philosophy + different customer tier:

| Product | Philosophy / pole | Customer tier | Directly researched? |
|---|---|---|---|
| Orion Advisor Technology | all-in-one platform (portfolio accounting at the core + planning + CRM + trading + compliance) | solo RIA → enterprise broker-dealer | Yes — orion.com main, Planning, Portfolio Accounting, Advisor Portal, Client Portal pages (Tier 1–2) |
| RightCapital | planning-led platform (plan as the product; portfolio data flows in) | boutique → mid-market RIA; broker-dealer channels | Yes — help.rightcapital.com: Getting Started, Creating Plans & Data Entry, Planning Modules, Integrations, Client Experience (Tier 1) |
| Wealthbox | CRM-first workspace (boundary anchor: what a CRM lacks) | solo → enterprise firms, aggregators, banks | Yes — wealthbox.com main + Contact Management feature page (Tier 2; help center timed out ×2) |
| eMoney Advisor | planning-led market leader (cash-flow modeling) | mid-market → enterprise | No — emoneyadvisor.com 403 ×2, help.emoneyadvisor.com transport error ×1. Market context only, via Orion FAQ + RightCapital PDF-import + Wealthbox integration pages |
| MoneyGuidePro (MoneyGuide) | goals-based planning leader (broker-dealer/IBD channels) | broker-dealers, IBDs | No — moneyguidepro.com timeout ×2. Market context only, via Orion FAQ + RightCapital PDF-import + Orion integration description |

Black Diamond (SS&C) attempted (404 + wrong-company site) — abandoned; kept as market context via RightCapital/Orion/Wealthbox integration pages and Orion's comparison FAQ.

## Sources

Tier 1 (official operational documentation):

- RightCapital Help Center — https://help.rightcapital.com/ (home; /getting-started/creating-plans-and-data-entry; /getting-started/client-plan-overview; /integrations/overview; /client-experience/client-experience-overview)
- Orion — https://orion.com/ (main; /advisor-tech/planning; /advisor-tech/portfolio-accounting; /advisor-tech/advisor-portal; /advisor-tech/client-portal)

Tier 2 (official product pages):

- Wealthbox — https://www.wealthbox.com/ (main; /features/contact-management)
- Orion product/FAQ pages (same URLs as above carry FAQ blocks with operational detail)

Cross-source (market context, not directly fetched):

- eMoney: described in Orion Planning FAQ ("standalone financial planning tool focused on cash-flow modeling", integrates via API), Orion integration page ("pulls account balance and performance data… Orion reports on demand inside eMoney… eMoney vault"), RightCapital data-entry page (eMoney PDF Report import), Wealthbox integrations.
- MoneyGuidePro: described in Orion Planning FAQ ("goals-based planning tool, common in broker-dealer and IBD channels"), Orion integration page ("pushing Household/Account level data… pull back Financial Plan report elements including Plan Summary, Monte Carlo Results, Net-Worth Summary, Insurance Information"), RightCapital data-entry page (MoneyGuide PDF Report import).
- Black Diamond: appears as SSO/aggregator integration partner (RightCapital), comparison target (Orion FAQ: "SS&C's Black Diamond Wealth Platform" with its own Client Experience).

Fetch failures recorded: emoneyadvisor.com 403 ×2 + help subdomain transport error ×1 (abandoned per network rule); moneyguidepro.com timeout ×2 (abandoned); wealthbox.com/help timeout ×2 (fell back to feature pages); sscadvisors.com 404 + wrong company (abandoned).

---

## Product A — Orion Advisor Technology (all-in-one pole)

### Key observations (evidence layer A unless noted)

- Positioning: "all-in-one wealthtech platform behind more advisor firms than any other… CRM, planning, portfolio accounting, trading, compliance, and AI — built to work as one." Twelve products organized in three groups: Run Trading & Operations (Portfolio Accounting, Trading, Compliance, Risk Intelligence); Power with Data + AI (Denali Data Layer, Denali AI, Strategic Insights); Manage Client Relationships (Redtail CRM, Client Portal, Advisor Portal, Planning, Summit Experience).
- Who it serves: financial advisors, RIAs, broker-dealers, banks and trust companies, family offices; roles include CCO, COO, CTO.
- Portfolio Accounting: "performance reporting, AUM fee billing, household-level data, and direct-custodian reconciliation in one engine." Billing = "calculate, collect, and post advisory fees." Reconciliation with custodians happens overnight; positions reconciled before US market open on a typical day (vendor claim). Trading = "household-level rebalancing, asset location optimization, tax-intelligent trading." Data foundation for Trading, Reporting, Billing, Client Portal, Advisor Portal, Planning, Risk Intelligence — "all Orion products read from the same source of truth."
- Planning (Advizr-based): "hybrid by design (goals-based for clients, cash-flow under the hood)… Plans read live portfolio data, so every client conversation runs from the same source of truth as your back office." BeFi tools embedded (BeFi20, 3D Risk Profile, PulseCheck, Protect-Live-Dream). Client-ready customizable branded reports; Document Vault. Client Portal: clients view plan, track goals, run hypothetical scenarios; advisors send workflows (retirement planning, education savings) for clients to complete and configure what each client sees.
- Advisor Portal (the unified advisor workspace): six core modules — Dashboard and Client views; New Account Opening and Proposal Generation; Trading and Model Management; Servicing Requests and Forms Library; Reporting; Investment Research. Proposal → New Account Opening flow: client info pre-populated from Redtail CRM or Orion Planning; goals and risk tolerance; custodian and account type selection; investment selection from the firm's universe; paperwork delivered digitally to the custodian or routed through DocuSign (wet-signature also supported). Service Request system for day-to-day admin tasks with book-of-business-wide activity dashboard. Payout dashboard, RMD dashboard, Query tool.
- Client Portal: white-labeled, mobile-first; portfolios, financial plan, goals, statements under the firm's brand; advisor configures the experience; event-based automated notifications (text/email); interactive performance presentations.
- Data in: direct custodian connections (Schwab, Fidelity, Pershing — daily data files, trade files, advisory fee billing files, digital account opening); aggregation via Morningstar ByAllAccounts ("held away" assets, 360-degree view); two-way sync with CRMs (Redtail, Salesforce) at household and account level; planning tools (eMoney, MoneyGuide) exchange household/account data and plan report elements (Plan Summary, Monte Carlo Results, Net-Worth Summary, Insurance Information).
- New Account Center: "creating a household and launching required forms through Quik! or LaserApp" (from Redtail integration description).
- Comparison anchors in Orion's own FAQ: vs Black Diamond (Orion = deeper integrated stack), vs Addepar (Addepar concentrates on UHNW/family offices), vs Tamarac (Envestnet platform), vs Advyzon (integrated all-in-one). Confirms the market structure: portfolio platforms and all-in-one platforms are distinct poles.

## Product B — RightCapital (planning-led pole)

### Key observations (evidence layer A)

- Positioning: "Financial planning software done right… simplify planning, enhance client engagement, help advisors scale." Works with Schwab, XYPN, Commonwealth, Morningstar, Advisor360.
- Central object: the **household**. Advisor Portal → Planning → Plans tab → "+ New Financial Plan" → enter client + co-client names → "This will generate a new household." Household findable/reopenable from the Plans tab.
- Optional client self-entry: enter client email → "Invite your client(s) to start" → client/co-client enter their own information remotely into their client plan.
- Initial data entry: six steps — **Family** (names, birthdays, planning horizons, resident state; add children/grandchildren as participants), **Income** (salary, Social Security, self-employment, pension, bonus), **Savings** (401(k) employee+employer, IRA, Roth, taxable, 529, HSA), **Net Worth** (bank accounts, credit cards, investment accounts, stock plans, loans, properties, insurance policies, businesses), **Expenses** (pre-retirement living expenses, medical, tax filing status, local taxes, AUM fees), **Goals** (retirement age, retirement expenses, health care & LTC costs, education, travel, relocation, asset purchases).
- Data sources for Net Worth: (1) Account Aggregation (premium/platinum subscribers) — clients link accounts, "automatically pull in current balances and position-level account data"; (2) advisor-level integrations — link accounts to the plan; (3) manual entry ("Accounts can always be added manually… selecting an account type").
- Data Import: Smart Import (AI — upload reports, plan notes, meeting transcripts to auto-populate a plan), eMoney PDF Report import, MoneyGuide PDF Report import.
- Client plan = modular workspace. Profile tab (revisitable data entry) + Blueprint tab (consolidated client-friendly summary of inputs). Modules: **Dashboard** (Snapshot one-page summary, Balance Sheet, Liquidity Analysis, Budget Analysis, Tasks), **Investment** (Asset Allocation, Allocation Path, Risk Analysis questionnaires, Sector & Style, Concentration, Tax Allocation, Holdings), **Retirement** ("heart and soul": Retirement Analysis with probability of success, what-if scenarios, current-vs-proposed comparison; Stress Test; Social Security optimization; Medicare; Cash Flows), **Insurance** (Life, Disability, LTC, Property & Casualty), **Education** (per-student funding analysis, action items, apply proposal into Retirement Analysis), **Tax** (Tax Estimate, Tax Strategies — asset location / withdrawal sequence / Roth conversions, Tax Analyzer scanning 1040s), **Estate** (Checklist for will/POA/living will/healthcare proxy/trust, Beneficiary designations, Estate Analysis), **More** (Debt Management, Student Loans, Stock Plans, Business, Human Life Value calculator, Notes), **Vault** (Shared folder visible to client; Private folder advisor-only).
- Client experience: portal invite, data collection template, custom branding, checklists, risk questionnaires, RightFlows (client-facing workflow), email notifications; portal + mobile app (send updates, assign tasks, upload documents, budgeting view).
- Integrations (Tier-1 page, explicit categories): **Asset Custodians** — "pulls in individual accounts for each client… holdings-level data for each account, updating the information daily" (Schwab, Fidelity, Pershing, LPL, Raymond James, SEI, RBC, IBKR, Altruist, Apex, Axos, Betterment, …); **Aggregators** — "collect account information from multiple custodians and institutions… pulls in all investment accounts… holdings-level… daily" (Addepar, Black Diamond, Orion, Tamarac, Nitrogen, Wealth Access, Blueleaf, …); **CRMs** — "pulls in client information: contact info, date of birth & resident state for everyone associated with the client's household" (Redtail, Wealthbox, SmartOffice); **Data Management** — contact info + plan information (goals, income, expenses) to/from (PreciseFP, Jump, Zocks); **Risk Management Solution** — import model portfolios, translated to asset classes via Morningstar breakdown, stored under 'Models' menu; **Portfolio Analytics** — Morningstar Advisor Workstation reporting data; **SSO** partners.
- Firm-growth layer: RightFlows (workflows), RightIntel (firm intelligence), RightExpress (prospecting); Iris AI planning agent; Double Check (data-entry concern detection).

## Product C — Wealthbox (CRM-first pole, boundary anchor)

### Key observations (evidence layer A)

- Positioning: "CRM built for the way advisors actually work… Organize clients, automate workflows… AI built in." Firm types: independent advisors, enterprise, RIA aggregators, broker-dealers, OSJs, banks & credit unions, trust companies, family offices. Roles: advisors, founders/firm leaders, compliance, operations & client service, marketing, technology.
- Contact record: phone calls, emails, files, financial information in one layout; quick note-taking.
- **Households & Relationships**: "Built for households, not just contacts. Link individuals to households, companies, and trusts, and see the full web of relationships around every client, with a role on each connection."
- Activity stream: real-time team collaboration; automatic email sync (Gmail/Outlook); filter by type.
- Workflows & tasks: automated recurring processes, task assignment ("The right person gets the right task at the right time").
- Opportunities & pipeline: track prospects and AUM opportunities.
- Meetings & calendar; email & calendar sync; AI meeting prep (client activity: notes, tasks, meetings, relationships, financial information).
- Permissions & privacy: record-level visibility controls, role-based access, audit trails.
- Integrations: Addepar, Envestnet, MoneyGuide, RightCapital, eMoney, Black Diamond, Schwab, Fidelity, Altruist, Betterment, LPL ClientWorks, Nitrogen, Trust & Will, etc. — the CRM consumes portfolio/plan data from adjacent tools rather than holding it natively.
- What it does NOT have (boundary evidence): no native account aggregation/holdings, no financial plan engine, no performance reporting — those come from integrated partners. This is exactly the slice that separates Advisor CRM from Financial Advisor Platform.

## Product D/E — eMoney & MoneyGuidePro (market context only — evidence layer B, degraded)

Not directly fetched (see fetch failures). Cross-source observations only:

- eMoney: standalone financial planning tool focused on cash-flow modeling (Orion FAQ); holds account balance/performance data for planning; has a Vault; runs Orion reports inside it; integrates with portfolio platforms via API; its PDF reports are importable into RightCapital plans.
- MoneyGuidePro: goals-based planning tool common in broker-dealer and IBD channels (Orion FAQ); receives Household/Account level data pushed from portfolio platforms; returns plan report elements (Plan Summary, Monte Carlo Results, Net-Worth Summary, Insurance Information); PDF reports importable into RightCapital.
- Both confirm: planning tools hold household-scoped client data + plan engines, and interoperate with portfolio/CRM tools through household/account-level data exchange. No precise operational claims made for either product.

---

## Cross-product Comparison

| Dimension | Orion (all-in-one) | RightCapital (planning-led) | Wealthbox (CRM-first) | eMoney / MGP (context) |
|---|---|---|---|---|
| Central record | household + account (portfolio accounting core) | household (plan container) | household + relationships (contact core) | household (per integration descriptions) |
| Client financial position | native (custodian feeds, reconciliation, holdings) | native (aggregation / integrations / manual; holdings-level, daily) | not native (via integrations) | native (per descriptions) |
| Financial plan engine | native (hybrid goals/cash-flow) | native (modular plan; retirement core) | none | native (cash-flow / goals-based) |
| Proposal / recommendation workflow | native (proposal → account opening → paperwork) | plan proposals inside modules (current vs proposed) | none | plan proposals (per descriptions) |
| Performance reporting | native (core) | investment analytics inside plan (allocation, holdings) | none | some (per descriptions) |
| Client portal | native, white-labeled, mobile | native, branded, mobile | none | vault + portal (per descriptions) |
| Practice management (tasks/workflows) | Advisor Portal service requests; Redtail CRM | Tasks module; RightFlows | core (workflows, tasks, pipeline, activity) | — |
| Billing (AUM fees) | native core | AUM fee as plan input only | none | — |
| Trading/rebalancing | native core | none (model import only) | none | — |
| Compliance | native module | — | audit trails, workflows | — |
| Roles | advisor/ops/CCO/CTO; enterprise tiers | advisor + client; firm tiers | advisor/ops/compliance/marketing/tech | — |
| AI | Denali AI, Strategic Insights | Iris agent, Smart Import, Double Check | AI Assistant, AI Notetaker | — |

### Stable commonalities (evidence layer B — cross-product)

1. **Household as the central relationship record.** RightCapital creates "a new household" per plan; Wealthbox links individuals to households/companies/trusts with roles; Orion carries household-level and account-level data as its two data grains; eMoney/MoneyGuide exchange "Household/Account level data." The household (not the individual, not the account) is the unit around which the advisor's book is organized.
2. **A structured client financial position attached to the household** — accounts (bank/investment/credit/loan/property/insurance/business) with balances and holdings, however sourced (custodian feed, aggregator, manual, client self-entry, document import).
3. **Advisory work products derived from the position** — plan (goals + projections + scenarios), proposal/recommendation, client-ready reports. Present in every planning-capable product; absent in the CRM-only pole.
4. **Client-facing portal** with advisor-controlled visibility (RightCapital invite/settings; Orion white-label + per-client configuration).
5. **Integration fabric** — custodians, aggregators, CRMs, planning tools, portfolio tools exchange household/account-level data; SSO across the stack.
6. **Practice workflow layer** — tasks, workflows, meeting notes, service requests; audit trail.
7. **Roles & record-level permissions**; firm-level administration.
8. **AI assistance** entering all three directly-researched products (data entry, meeting notes, planning agent, firm intelligence).

### What varies (candidate L2)

- Center of gravity: planning-led vs portfolio-led vs CRM-led vs all-in-one.
- Billing, trading/rebalancing, compliance: core in portfolio-led/all-in-one; absent or input-only in planning-led; absent in CRM.
- Client self-service data entry (invite client to input) — optional everywhere observed.
- Regional/regulatory depth: the researched sample is US-shaped (Social Security, Medicare, 529, Roth, RMD, 1040, resident state tax). Non-US regimes not observed — treat as unknown, not as defining.
- Firm scale packaging: solo → enterprise (stacks/tiers, selling-agreement management, aggregator firms).
- AI depth.

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

A Financial Advisor Platform is an advisor-operated system organized around:

1. **Advisor-held client household record** — identified people (client, co-client, dependents) grouped as a household, plus the relationship context (roles, connections, notes). Not anonymous users; the advisor's book of named client relationships.
2. **Structured client financial position bound to that household** — accounts, assets, liabilities (with balances/holdings), however sourced. The household's financial picture as data.
3. **Advisory work products derived from the position and maintained over the relationship** — at minimum a financial plan or proposal/recommendation expressing what the advisor advises against the client's goals and situation, plus client-facing reports; updated as the position and the relationship evolve.

Test: remove #2 and #3 → advisor CRM (different Type). Remove #1's relationship primacy and center on accounts/portfolios → portfolio management system (different Type). Remove the advisor (client self-service) → PFM / robo-advisor (different Type). Remove work products but keep position+reports only → portfolio reporting (different Type). All three properties are needed.

Historical check (§24): 1990s-era advisor planning software (client data manually entered + retirement projection printed for the client) satisfies all three without aggregation, portals, billing, or compliance modules. Older, non-US, and boutique products fit. The definition is not overfit to the modern integrated stack.

### L1 — Common Mature Structure (very common, not defining)

- Account aggregation / custodian data feeds (holdings-level, refreshed on a regular cycle; reconciliation in portfolio-led products)
- Client portal (branded/white-labeled, mobile) + document vault (shared vs advisor-private)
- Performance reporting and client statements (portfolio-led) / plan reports and one-page summaries (planning-led)
- Risk tolerance assessment (questionnaires, risk scores)
- Proposal generation (recommendation → presentation; in integrated stacks: proposal → account opening → e-signature paperwork to custodian)
- Tasks / workflows / meeting notes / service requests (practice management)
- Model portfolios (imported or managed); rebalancing/trading in portfolio-led products
- Integration ecosystem (custodians, aggregators, CRMs, planning, portfolio analytics) + SSO
- Roles & record-level permissions; audit trail
- AI assistance (data entry, meeting capture, planning agents, firm intelligence)

### L2 — Variant / Optional Structure

- Center-of-gravity posture (planning-led / portfolio-led / CRM-led / all-in-one) — the same Type, different poles
- AUM fee billing; trading/rebalancing execution; compliance suite (portfolio-led & all-in-one; enterprise)
- Client self-service data entry; client-facing workflows
- Plan methodology: goals-based vs cash-flow vs hybrid (product philosophy, not Type difference)
- Regional/regulatory module depth (US sample: Social Security/Medicare/529/Roth/RMD/1040; other regimes unobserved)
- Firm-scale packaging (solo → enterprise; stacks/tiers; aggregator/broker-dealer home-office deployments)
- Document import from competing planning tools (eMoney/MoneyGuide PDF import)
- Marketing/prospecting extensions (pipeline, lead capture)

### L3 — Vendor-specific (research notes only)

- RightCapital: Snapshot™, Blueprint™, RightRisk™, Smart Import™, RightFlows®, RightIntel®, RightExpress™, Iris™ AI, Cash Flow Map, Tax Analyzer, six-step data-entry sequence (Family/Income/Savings/Net Worth/Expenses/Goals), Shared/Private vault folders, premium/platinum tier gating of aggregation.
- Orion: Denali Data Layer, Denali AI, Redtail CRM, Advizr-based Planning, BeFi20 / 3D Risk Profile / PulseCheck / Protect-Live-Dream, Insight, Summit Experience, Orion Stacks (Foundation/Essentials/Advantage; published starting prices $13k/$18k/$28k), New Account Center, Quik!/LaserApp form launch, AltExchange (alternatives), RMD dashboard, Payout dashboard, Query tool, overnight reconciliation before market open (vendor claim), 99% reconciliation stat (vendor claim).
- Wealthbox: AI Assistant, AI Notetaker, activity stream, opportunity pipeline, record-level visibility controls.
- eMoney / MoneyGuidePro: no vendor-specific claims (not directly researched).

---

## Vendor-specific Findings

See L3 above. None promoted to the canonical model. Vendor scale/market-share claims (#1 T3 survey etc.) are marketing assertions and were not carried into the final document.

## Boundary Findings

| Neighboring Type | Sharpest seam | "Remove what → becomes the other" |
|---|---|---|
| Advisor CRM (Redtail, Wealthbox) | CRM holds the relationship + workflow but not the financial position or plan engine | Remove position + work products → advisor CRM |
| Portfolio Management System (Black Diamond, Addepar, Orion Portfolio Accounting standalone) | Portfolio-centric (account/portfolio is the unit; performance measurement is the purpose) vs relationship-centric (household is the unit; the advisory relationship is the purpose) | Remove the relationship/plan layer, center on accounts → portfolio system |
| Wealth Management Platform | Institution-side (broker-dealer/bank home office; supervision, product shelf, enterprise distribution) vs advisor practice tool | Same market vocabulary, different operator; Orion spans both poles (Advisor Tech vs Wealth Management divisions) — joint-review flag |
| Robo-advisor | Consumer self-service automated advice vs advisor-operated practice system | Remove the advisor as operator → robo-advisor |
| Retirement Planning Application | Single-purpose planning slice vs whole-practice platform | Strip non-retirement practice scope → retirement planning app |
| Personal Finance Management Application | Consumer manages own finances vs advisor manages many client households | Remove the advisor-side multi-client book → PFM |
| Financial Planning & Analysis Platform | Corporate FP&A (company budgets/forecasts) — false friend on the word "planning" | Different domain entirely; no shared core |
| Investment Research Platform | Content/analytics about markets vs system of record for client relationships | Remove client records → research platform |

Taxonomy observations (for STATUS Boundary Issues):

1. **Wealth Management Platform vs Financial Advisor Platform**: probable partial overlap. Market usage: "wealth management platform" often names the institution-side or the portfolio+reporting stack; "advisor platform / advisor tech stack" names the practice-side system. The sampled market (Orion's own two divisions; Black Diamond vs Orion comparisons) supports treating them as distinct poles, but the seam deserves joint review when the sibling leaf is processed.
2. The category is naturally a **stack of point solutions** (planning + portfolio + CRM + portal + billing + compliance). "Financial Advisor Platform" as a Type is best modeled at the practice-system level (household + position + work products), with stack composition as variant posture — not as a fixed module list.
3. eMoney/MoneyGuidePro are planning *tools* that are components of advisor platforms; the directory has no separate "Financial Planning Software" leaf, so planning-led products are legitimately instances of this Type (planning-led variant).

## Uncertainties

- eMoney and MoneyGuidePro were not directly researched (fetch failures). Their internal structures are inferred from integration descriptions on three other vendors' official pages — adequate for market context, not for product-level claims.
- Non-US / regional advisor platforms (e.g., UK, EU, Asia advisory tools) were not sampled; the US regulatory module set (Social Security, Medicare, 529, Roth, RMD, 1040) must be treated as sample-shaped, not defining.
- Compliance depth (suitability/best-interest documentation workflows) was observed only as module presence (Orion Compliance; Wealthbox audit trails); detailed compliance workflows were not researched.
- Billing mechanics (fee schedules, proration, in advance/arrears) observed only as capability presence, not rules.
- Wealthbox help center unreachable; its capability detail rests on Tier-2 feature pages.

## Final Synthesis

A Financial Advisor Platform is the advisor-side practice system for running an ongoing financial-advisory relationships business. Its defining core is small: the advisor's book of named client households; each household's structured financial position; and the advisory work products (plan / proposal / reports) derived from that position and maintained as the relationship evolves. Everything else commonly bundled — aggregation feeds, client portals, performance reporting, billing, trading, compliance, AI — is mature market structure that varies by product philosophy (planning-led, portfolio-led, CRM-led, all-in-one) and customer tier (solo RIA → enterprise broker-dealer). The Type is relationship-centric: the household is the unit of organization, the position is the substance, the work product is the output, and the ongoing review cycle is the rhythm.
