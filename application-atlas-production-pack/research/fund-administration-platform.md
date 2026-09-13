# Research Notes — Fund Administration Platform

Research date: **2026-09-07**
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what a Fund Administration Platform actually is as an Application Type: what records it keeps, who operates it, how a fund's books move from raw activity to investor-facing output, and how it differs from the neighboring Types in directory section 08 (Investment Fund Accounting, Transfer Agency Platform, Investor Portal, Portfolio Management System, accounting software).

## Initial Boundary (hypothesis before research)

A Fund Administration Platform maintains the official books and records of pooled investment funds — periodic valuation (NAV where applicable), investor share/capital registers, fee calculations, financial statements — on behalf of fund managers, either as software run by a third-party administrator or as software+service used by the manager itself.

Risks identified up front:

- The directory has three sibling leaves in §08 — Fund Administration Platform, Investment Fund Accounting, Transfer Agency Platform — and market usage suggests fund administration *bundles* accounting + registry + investor services. The umbrella/slice relationship had to be tested, not assumed.
- "Fund accounting" also names a different discipline entirely (nonprofit restricted-fund accounting; leaf exists under §25). Not the same Type.
- Some sampled vendors sell administration as a *service* (with software attached) rather than software alone — the Type boundary between "software product" and "administered service" had to be handled at the abstraction level rather than denied.

## Research Questions

1. What are the core objects: fund, share class/series, investor, commitment, subscription/redemption, capital call/distribution, position, capital account, NAV, fee, statement?
2. How is the periodic valuation (NAV strike / financial close) actually produced, and what feeds it?
3. How do open-ended (dealing) and closed-ended (commitment) investor lifecycles differ, and are both one Type?
4. Who operates the system: third-party administrator staff, GP finance staff, or the vendor as a service? How does the multi-tenant vs GP-side packaging differ?
5. Which rules matter: allocations, equalization, fee crystallization, waterfalls, approval workflows, audit trail?
6. Where are the boundaries vs Investment Fund Accounting, Transfer Agency, Investor Portal, Portfolio Management System, and general accounting software?

## Representative Products

| Product | Pole | Client tier | Why sampled |
|---|---|---|---|
| FundCount | Software platform for administrators *and* funds; open- and closed-ended on one ledger | Hedge funds, PE/VC, family offices, independent administrators | Richest operational documentation; administrator-software pole; covers open-ended mechanics (NAV, equalization) |
| Juniper Square | Administration **service** + GPX platform for private markets GPs | Emerging managers to global institutional GPs | GP-side service+technology pole; shows the same core objects packaged as outsourcing |
| Carta | GP-side fund administration: software suite + expert accountants (VC-heavy) | VC/PE funds and SPVs, small to mid | Self-service-adjacent, event-based accounting, formation→tax span; LP portal as product surface |
| Allvue Systems | Suite for GPs and fund administrators (private equity/credit) | Mid to enterprise; administrators serving private capital | Suite-module pole; fund accounting as one module of a wider alternative-investment suite |
| Alter Domus | Classic third-party fund administrator (service firm) | Institutional, global, multi-jurisdiction | The outsourced-administrator pole that the other products sell software *into* |

Coverage across poles: software-for-administrators / GP-side service / GP self-service suite / suite module / pure service provider. Coverage across fund regimes: open-ended (FundCount) and closed-ended (JSQ, Carta, Allvue) and both (FundCount).

## Sources

Tier-1 (fetched 2026-09-07):

- FundCount — https://fundcount.com/ ; https://fundcount.com/industries/fund-administration/ (workflow diagram, capability pages, case studies)
- Juniper Square — https://www.junipersquare.com/ ; https://www.junipersquare.com/solutions/administration ; https://www.junipersquare.com/solutions/administration/fund-accounting
- Carta — https://carta.com/fund-management/ ; https://carta.com/fund-management/fund-administration/
- Allvue Systems — https://www.allvuesystems.com/ ; https://www.allvuesystems.com/solutions/fund-accounting/
- Alter Domus — https://www.alterdomus.com/ (service/technology structure only)

Unreachable / abandoned (per network-restriction rule):

- SS&C (sscinc.com/products/geneva) — 403, abandoned; no claims made about SS&C products
- carta.com/data/fund-administration, carta.com/funds, carta.com/products/fund-administration, junipersquare.com/products/fund-administration, allvuesystems.com/solution/fund-administration — 404 (wrong paths; correct paths found via site navigation)

Source-access limitation: no product's deep help-center/user-guide articles (screen-level operation) were reachable; evidence is strongest at product-page and workflow-diagram level. Precision rule applied: no numeric limits, cycle durations, or default parameters asserted in the final document. Marketing-scale claims (e.g., "$220B+ AUA", "2,300+ GPs") recorded here as vendor claims only, not used in the canonical document.

---

## Product Observations

### Product A — FundCount (evidence layer: A, strong)

Official pages describe a unified accounting and investment platform whose unit of operation is the **client book** (a fund or fund complex). Key direct observations:

- Positioning: "The unified fund administration platform for running hundreds of client books — open- and closed-ended — on one investment-grade ledger." Explicitly sold to **fund administrators** (multi-tenant: "your clients are the users", "each client's book logically isolated") and to funds/family offices directly (shadowing their administrator).
- Named solution modules: Portfolio Accounting, Partnership Accounting, General Ledger, AI Document Intelligence, Reporting, Investor Portal, Data Aggregation.
- Open-ended mechanics: "Strike every NAV, crystallize every fee" — NAV per **fund, class, series and side pocket**; master-feeder, series structures; incentive and management fees; **equalization** listed among NAV & fee calculations.
- Closed-ended mechanics: capital accounts, **waterfall engine** (configurable, "standard and non-standard structures"), partial LP transfers, side pockets, series LLCs, debt-provider participation; **capital calls and distributions**; capital-call and distribution **notices**.
- Data ingestion: custodian/broker feeds (Interactive Brokers, Pershing, Morgan Stanley, Marex), pricing/market data (Bloomberg, Refinitiv) "automated, daily"; PDF capital statements/K-1s from underlying funds extracted by AI ("Turn capital statements into ledger entries").
- Workflow diagram (direct quote structure): source data & capital activity (feeds, positions/transactions/cash/valuations, calls/distributions/subscriptions/redemptions, fees & expenses, multi-entity structures, documents) → unified operating layer (Portfolio Accounting → Partnership Accounting → General Ledger → Reporting → Investor Portal) → client & investor deliverables (NAV & fee calculations, capital account statements fund- and investor-level, identical-format reports, notices, white-label portal delivery, audit-ready output with "drill-down to source on every figure").
- Reconciliation posture: "reconciled by construction, not assembled by hand"; double-entry GL under the investment record so "positions and books never drift apart"; **reconciliation exception queue** with drill-down.
- Portal: white-label per client, MFA, role-based access, document repository, capital-call/distribution notices, capital-account statements.
- Audit posture: "audit-ready by construction", drill-down to source; SOC 2 Type II claimed.

### Product B — Juniper Square (evidence layer: A, strong)

GP-side private-markets administration: a hybrid of a software platform (GPX) and outsourced administration services run on it. Direct observations:

- Positioning: "operations partner for private markets"; fund administration "connected software, data, and fund administration services"; supports "everything from SMAs to large, global, cross-jurisdictional funds".
- Service decomposition under Fund Administration: **Fund Accounting** ("Outsource your fund financials and complex allocations… real-time metrics"), **Treasury Services** ("facilitate capital calls, distributions, and other payments… investors can securely update wiring instructions with secondary approval in their portal"), **Investor Services** ("outsourcing statements and notice preparation and delivery"), Investor Onboarding, AML/KYC, Management Company Accounting, Loan Administration, Waterfall Modeling.
- Fund accounting service page: "single source of truth for your financials, performance metrics, and portal"; "expert preparation of fund financials"; vendor payments (AP outsourcing); "on-demand partner capital account balances" kept current in the portal; "automatic performance metric calculation"; "structured records of your ledger… to your advisors" for tax/audit season; "built-in approval workflows and audit logs".
- Platform modules (GPX): Investor Onboarding, Portal, Investor Reporting, Insights, Distribution Payments, Data Rooms, DDQ, APIs. Fund data model: "Every fund, asset, investor, and position—connected."
- Lifecycle framing: "from first close to final distribution" — closed-ended orientation.
- Scale claims (vendor-stated): 2,300+ GPs, 750,000+ LPs, 45,000+ investment entities.

### Product C — Carta (evidence layer: A, good)

Fund administration for PE/VC as software suite + in-house accountants. Direct observations:

- Positioning: "The end-to-end suite for fund management… the industry's first fund software with **event-based accounting** at its core." Fund admin described as software *and* "a dedicated team… to run your entire fund accounting process".
- GP-side actions: "Initiate capital calls, distributions, investments"; real-time **net and deal IRR, TVPI, DPI**; cash reconciliation agents; SOI (schedule of investments) tagging; year-end tax filings, investor K-1s, audit support; "providing books, records, and supporting documents to your auditor and tax provider".
- LP portal (direct FAQ): LPs "sign subdocs, fulfill capital calls, and view investment performance"; "track total commitment, amount contributed, vintage year, and net asset balance"; documents and fund-level performance data on demand.
- Suite modules: Fund Admin Portal, Fund Tax (Form 1065, K-1s, state filings), Fund Formations (form the fund, administer closings, execute capital calls), Fund Forecasting, Portfolio Valuations ("look-through level data collection, calculations, and reporting"), Management Companies (manco administration), SPVs, KYC/AML services, Deal and LP CRM.
- Structure objects visible: commitments, contributed capital, vintage year, net asset balance, capital calls, distributions, K-1s.

### Product D — Allvue Systems (evidence layer: A, good)

Alternative-investment suite sold to GPs *and* fund administrators; fund accounting is the back-office module. Direct observations:

- Fund Accounting page: "brings together **partnership accounting**, detailed financial statement reporting, a **multi-currency general ledger**, cash management, and workflow standardization into one complete fund accounting system."
- "A true general ledger with a robust library of financial reports and a flexible report writer"; optional **waterfall module** for "carry fee calculations with detailed modeling of LPAs".
- Structures: LP/GP, funds of funds, co-investment vehicles, multi-currency funds, multi-fund environments.
- Quarter-end framing: "automating **capital call processing, distribution calculations, and financial statement generation** — replacing manual spreadsheet workflows"; "reduce your quarter-end reporting cycle".
- Integration: fund accounting ↔ corporate (management-company) accounting ↔ investment accounting ↔ investor portal on one platform; API connectivity.
- Compliance posture: SOC 1 / SOC 2 alignment; cloud (Microsoft Dynamics 365 Business Central / Azure).
- AI: Document IQ extraction (financials, loan notices, credit agreements, capital calls), Andi assistant, agentic workflows.

### Product E — Alter Domus (evidence layer: A for structure, thin for operations)

Classic third-party fund administrator (service firm); software is internal/companion. Direct observations:

- Services tree: Fund Level Services — **Fund Administration**, AIFM Services, Depositary Services, Corporate Services. Technology & Data Solutions — **Fund Accounting**, **Investor Management**, Data Extraction & Harmonization, Asset Monitoring & Covenant Management, Portfolio Data Management, CLO compliance.
- Sector specialization: PE, VC, fund of funds, real estate, infrastructure, private credit.
- Regulatory wrapping around the same core: AIFM/depositary (European regime), corporate services (entity management), multi-jurisdiction (23 jurisdictions claimed).
- Client portal exists (AD Connect); operational detail not publicly documented at screen level.

---

## Cross-product Comparison

| Dimension | FundCount | Juniper Square | Carta | Allvue | Alter Domus |
|---|---|---|---|---|---|
| Fund as administered unit | ✔ per "client book", logically isolated | ✔ funds/entities connected data model | ✔ funds + SPVs | ✔ multi-fund environments | ✔ 40,000 structures (claim) |
| Official fund books / GL | ✔ "one real-time general ledger" under investment record | ✔ ledger as service, "single source of truth" | ✔ event-based accounting core | ✔ "true general ledger" | ✔ fund accounting technology |
| Investor register / capital accounts | ✔ capital accounts, partial transfers, side pockets | ✔ partner capital account balances in portal | ✔ commitment, contributed, net asset balance per LP | ✔ partnership accounting | ✔ investor management |
| Periodic valuation output | ✔ NAV strike by fund/class/series/side pocket + equalization | ✔ financials + performance metrics | ✔ real-time IRR/TVPI/DPI + fund financials | ✔ financial statements, quarter-end cycle | ✔ (implied, service) |
| Investor activity processing | ✔ subscriptions, redemptions, calls, distributions | ✔ capital calls/distributions facilitated (treasury) | ✔ initiate calls/distributions; LP fulfills calls in portal | ✔ capital call processing, distribution calcs | ✔ (service) |
| Fee machinery | ✔ mgmt + incentive, crystallization, equalization | ✔ waterfall modeling service | ✔ carry app | ✔ waterfall module w/ LPA modeling | ✔ (service) |
| Reconciliation | ✔ exception queue, drill-down to source | ✔ (implied, service) | ✔ cash reconciliation agents | ✔ (implied via GL) | ✔ (service) |
| Investor statements/notices | ✔ LP statements, capital-call/distribution notices, K-1 prep | ✔ statements + notices as service | ✔ K-1s, audit/tax packs | ✔ investor reporting | ✔ (service) |
| Investor portal | ✔ white-label, MFA | ✔ "trusted by 650,000+ LPs" | ✔ LP portal w/ subdocs, call fulfillment | ✔ investor portal module | ✔ AD Connect |
| Multi-entity / multi-currency | ✔ | ✔ cross-jurisdiction (incl. Luxembourg) | ✔ (implied) | ✔ multi-currency | ✔ 23 jurisdictions |
| Audit trail / approvals / SOC | ✔ drill-down, SOC 2 | ✔ approval workflows + audit logs | ✔ (implied, audit support) | ✔ SOC 1/SOC 2 | ✔ (service) |
| Regulated services (AIFM/depositary/corporate) | ✘ | AML/KYC ✔ | KYC/AML ✔ (add-on) | ✘ | ✔ |
| Tax preparation depth | K-1 prep ✔ | advisors handoff | ✔ full tax product | ✔ (via corporate accounting adjacency) | ✔ (service) |
| Manager's own books (manco accounting) | ✔ GL for entities | ✔ manco accounting service | ✔ manco administration | ✔ corporate accounting | ✔ corporate services |

Reading: every sampled product, whatever its packaging, maintains the same record set — the fund's books, the per-investor capital position, and a recurring cycle that turns activity into fund-level and investor-level official output. The differences are packaging (software vs service), fund regime emphasis (open vs closed ended), and how much of the surrounding compliance/tax/entity work is bundled.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

A Fund Administration Platform is recognizable only if all four hold:

1. **Administered fund as the organizing record.** The system's world is organized around investment funds (legal pooled vehicles, plus closely attached vehicles like GP entities, co-invest SPVs, master-feeder chains). Not a person, not a deal, not a project — a fund whose records must be kept.
2. **Official books and records of each fund.** A maintained fund-level financial record — positions/investments, cash, income, expenses, liabilities — that serves as the record of truth for auditors, regulators, and investors, distinct from the manager's front-office decision records. This is why GL/reconciliation/audit-trail machinery is inseparable from the Type.
3. **Investor register with per-investor capital position.** Ownership held per investor — units/shares with dealing history, or commitments with contributed/distributed capital — maintained as capital accounts, changed by recorded investor transactions (subscriptions/redemptions, or calls/distributions/transfers).
4. **Recurring production of the fund's official financial output.** On a defined cycle, the system produces fund-level valuation/financials (NAV per share where the fund deals) and investor-level statements derived from the same books.

The L0 workflow: activity (market activity and investor activity) flows into the books and register; a governed cycle converts them into the fund's official financial picture; outputs trace back to source. Every sampled product presents exactly this loop, whether staffed by the administrator or the GP.

Test: remove the investor register → it degrades into a portfolio/accounting system, not fund administration. Remove the official-books posture (audit-traceable GL) → it degrades into an IR/CRM tool. Remove the recurring valuation/statement cycle → it is not administration but a data room. Remove the fund as organizing unit → not this Type at all.

Historical/market-sample check (§24): 1990s-era administrator systems (and a small fund accountant with dedicated software) satisfy all four invariants without portals, automated feeds, waterfall engines, or AI extraction — those are L1/L2, not L0. Open-ended and closed-ended regimes both satisfy the same four invariants with different activity types. Regional administrators (Singapore, Caribbean, Luxembourg — per FundCount case-study clients and JSQ Luxembourg support) also fit. L0 survives the check.

### L1 — Common Mature Structure

Present in essentially all mature sampled products; expected by the market but not definitional:

- double-entry general ledger under the investment record ("reconciled by construction"; positions and books in one record)
- reconciliation machinery: custodian/broker/pricing feeds, exception queues, drill-down to source transaction
- fee engines: management fee accrual, performance/incentive fee crystallization (equalization and series mechanisms in open-ended products)
- waterfall engine for closed-ended funds, modeled on the LPA (carry)
- allocation engine: P&L/expense allocation across classes, series, side pockets, and investor capital accounts
- financial statement generation + audit/tax handoff packs (books/records to auditor; K-1 preparation in the US partnership context)
- investor statements & notices: capital account statements, capital-call notices, distribution notices
- investor (LP) portal: permissioned document library, balances, performance, call fulfillment; MFA/role-based access
- multi-entity, multi-currency, multi-fund structures (master-feeder, series, side pockets, co-invest vehicles)
- document ingestion (feeds plus AI extraction of statements/capital-call PDFs in current-era products)
- roles/permissions, approval workflows, audit logs, SOC 1/SOC 2 posture
- onboarding: subscription document handling, investor onboarding, AML/KYC hooks

### L2 — Variant / Optional Structure

- **Operating model** (the biggest variant): software run by an independent third-party administrator (multi-tenant client books); administration service delivered on the vendor's platform (JSQ, Carta, Alter Domus); software used directly by the GP (in-house administration / shadow accounting — FundCount hedge-fund use case); co-sourcing hybrids (Allvue "co-sourcing" content)
- **Fund regime emphasis**: open-ended dealing funds (NAV cycle, subscriptions/redemptions, equalization) vs closed-ended commitment funds (calls/distributions/waterfall); both supported by some (FundCount), specialized by others
- **Asset class tuning**: hedge, PE, VC, private credit/CLO, real estate/infrastructure, fund of funds, digital assets (FundCount claims), loan administration (JSQ private credit)
- **Regulatory wrapping**: EU AIFM/depositary services, entity/corporate services (Alter Domus), AML/KYC programs (JSQ, Carta)
- **Adjacency bundling**: fund formation/closings, fund forecasting, portfolio valuations service, management-company accounting, treasury/payments services, tax preparation as product, fundraising CRM/data rooms (all present in some products; none definitional)
- **Delivery**: SaaS cloud (dominant in sample; Allvue on Azure, Carta, JSQ, FundCount) vs legacy on-prem era

### L3 — Vendor-specific (research notes only)

- FundCount: AI Assistant, "Sandbox" proving environment, ETL tool, named feed partners, series-LLC/debt-provider participation modeling, "identical-format client output" branding
- Juniper Square: GPX platform name, JunieAI, Headless GPX (MCP), Admin Oversight Agent ("Fay"), Distribution Payments, Managed Close, 94% staff-retention claim, Luxembourg entity
- Carta: "event-based accounting" branding, Carry app, Plugins for Claude/MCP, Fund Formations "six weeks" claim, capital call lines add-on
- Allvue: Andi assistant, Document IQ, Nexius data platform, OneVue workspace, FirmView carry/compensation, Dynamics 365 Business Central substrate
- Alter Domus: AD Connect portal, Solvas CLO compliance, integration of loan agency with fund services

## Vendor-specific Findings

- Only FundCount documents open-ended mechanics at this depth (NAV by class/series/side pocket, equalization, crystallization). Closed-ended products never mention equalization. Treat "equalization/series accounting" as open-ended-regime structure, not Type-defining.
- Only Juniper Square/Carta document the *payment execution* layer (treasury services, distribution payments, LP wire updates with secondary approval). Payment facilitation is common but not universal → L1/L2, not L0.
- Only Alter Domus shows the regulated-services wrap (AIFM/depositary) as a first-class sibling of fund administration; jurisdiction-dependent → L2.
- AI document extraction and agentic reconciliation appear in 4 of 5 sampled products (all but Alter Domus) — era-common, keep in L1 as ingestion/reporting aid; do not put in L0.

## Boundary Findings

| Neighboring Type | Relationship | Sharpest seam ("remove X → becomes the other Type") |
|---|---|---|
| **Investment Fund Accounting** (sibling leaf, §08) | **Slice / umbrella tension.** Fund accounting = the books-and-records + valuation leg of fund administration. Every fund-admin product contains it (FundCount module, Allvue module, JSQ service, Carta core); products branded "fund accounting" (Allvue's own module page) serve fund administrators. | Remove the investor register + investor-facing services (statements/notices/portal) from a fund administration platform → it becomes an investment fund accounting system. Keep them → fund administration. |
| **Transfer Agency Platform** (sibling leaf, §08) | **Slice (open-ended pole).** The official shareholder register + dealing machinery for registered/open-ended funds. Fund administration contains the register function among the rest of the books. | Remove the fund's portfolio books/GL from fund administration → what remains is transfer-agency-shaped (register + dealing + investor statements). |
| **Investor Portal** (sibling leaf, §08) | **Customer-facing slice.** The LP portal is one standard surface of fund administration (4/5 sampled products bundle one). | Extract the portal and drop the books → Investor Portal leaf. |
| **Portfolio Management System** | Front office vs back office. PMS supports investment decisions/monitoring; fund administration is the official record. | Remove official-record posture + investor register → PMS territory. |
| **Accounting Software / General Ledger System** | Generic corporate ledger vs investor-aware fund books. FundCount/Allvue embed a GL; the difference is capital-account/NAV/allocation machinery on top. | A GL cannot compute NAV per class or LP waterfalls; if those disappear, it is generic accounting. |
| **Private Market Investment Platform / Deal Management for PE/VC** (§08) | Deal/front-office pipeline vs books. Carta ships a Deal CRM as adjacent module; JSQ ships deal services. | No fund books + register → deal platform. |
| **Wealth Management Platform / Financial Advisor Platform** | Serves advisors/end investors; not fund books of record. | Clear. |
| **Nonprofit Fund Accounting** (§25 leaf) | False friend: "fund accounting" in the restricted-fund sense. No NAV, no investor register of pooled capital. | Different Type entirely; only terminology overlap. |
| **Investor Onboarding / Fundraising (Managed Close)** | Adjacent, frequently bundled (Carta Formations, JSQ Managed Close). | Onboarding feeds the register but is not the register; subscription execution is the seam. |

**Umbrella verdict (for Boundary Issues):** market evidence supports treating Fund Administration Platform as the umbrella whose accounting leg is Investment Fund Accounting and whose open-ended register leg is Transfer Agency; the three leaves are kept separate, but future joint review should confirm that Investment Fund Accounting's definition excludes the investor-services legs (otherwise it duplicates this leaf).

## Uncertainties

- Screen-level operational documentation (exact NAV-strike steps, permission models, state names) was not publicly reachable for any sampled product; the workflow reconstruction rests on vendor workflow diagrams and service descriptions (strong at structure level, weak at button level).
- Open-ended hedge-fund administration is covered by one sampled product (FundCount) at operational depth; classic hedge-fund administrators (SS&C, Citco, Apex, NAV Consulting) were not reachable (403 / no public docs). Open-ended findings are therefore marked: cross-check before generalizing further.
- Alter Domus' software internals are not public; its pole is argued from its service taxonomy, not operational docs.
- The exact split between "fund administration" and "fund accounting" *as marketed* varies by vendor (Allvue brands its module "Fund Accounting" and sells it to administrators); the boundary above is a structural judgment, not a market-usage law.

## Final Synthesis

A Fund Administration Platform is the system of record for investment funds' official books and their investors' capital positions, and the production line that turns fund activity into recurring official financial output. Its irreducible shape: funds as administered units → official fund books (investment-grade GL, reconciled, auditable) → per-investor capital accounts/register changed by recorded investor transactions → a governed periodic cycle (reconcile, accrue fees, allocate, strike NAV / close the books, generate statements) → fund-level and investor-level deliverables (financials, NAV where applicable, capital statements, notices, audit/tax packs, portal publication).

Around that core, mature products add reconciliation and feed machinery, fee/waterfall/allocation engines, investor portals, multi-entity structures, onboarding/AML hooks, and — depending on operating model — the people who run it (administrator staff or GP finance teams). Packaging varies (software for administrators, GP-side service, GP self-service, outsourced service), fund regime varies (open vs closed ended), asset class varies; the record set and the cycle do not.

The Type is umbilically connected to two §08 siblings: Investment Fund Accounting (its accounting leg) and Transfer Agency Platform (its open-ended register leg). The investor-services legs (register + statements + portal) are what make fund administration the umbrella rather than a synonym of fund accounting.
