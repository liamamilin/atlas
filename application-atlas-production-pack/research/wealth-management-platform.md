# Research Notes — Wealth Management Platform

Research date: 2026-09-08
Slug: `wealth-management-platform`
Directory leaf: Wealth Management Platform (§08 Finance, Banking, Insurance & Investment)

Joint-review obligations carried into this pass (from STATUS.md Boundary Issues):

1. **financial-advisor-platform** (§08, processed 2026-09-06): "probable partial overlap flagged — market vocabulary straddles … recommend joint review when wealth-management-platform is processed."
2. **robo-advisor** (§08, processed 2026-09-07): "open item for the wealth-management-platform pass: the advice-spectrum seam (robo = low-touch automated pole vs advisor-led comprehensive practice) plus the hybrid-advice-tier pattern should be decided there."
3. **retirement-planning-application** (§08, processed): "joint review recommended on the embedded-planner capability-overlap pattern."
4. **portfolio-management-system** (§08, processed): "the wealth-side 'portfolio rebalancing & trading' category … satisfies this Type's L0 … treat the rebalancing engine as a PMS-shaped slice, not a separate Type."
5. **investment-management-platform** (§08, processed): "those are client-centric suites … The IMP is investment-centric … the extension pattern, not a merger."

All five are discharged below (Boundary Findings #1–#5).

---

## Research Goal

Understand what a Wealth Management Platform actually is as an Application Type — the system a wealth business (wealth management firm, bank wealth division, trust company, broker-dealer wealth channel) runs its business on — and decide, with direct evidence, whether it is a distinct Type or an alias/variant of the sibling Financial Advisor Platform. Produce a vendor-neutral canonical model: what exists inside it, who operates it, how work flows, which rules matter, and where the boundaries with the neighboring §08 investment/wealth Types lie.

## Initial Boundary (hypothesis before research)

- Working hypothesis (inherited from the financial-advisor-platform pass): the leaf names the **institution-side wealth business platform** (broker-dealer/bank home office, product shelf, supervision) as distinct from the advisor practice system. Market vocabulary also uses "wealth management platform" for the portfolio+reporting stack (Addepar, Black Diamond) — the straddle must be resolved with evidence.
- Nearest neighbors: Financial Advisor Platform (practice system), Portfolio Management System (rebalancing slice), Investment Management Platform (investment-centric books), Robo-advisor (consumer self-service pole), Brokerage Platform (self-directed + custody), Retirement Planning Application (embedded planner), Investor Portal (client-facing slice), CRM (relationship record without wealth substance).
- Unknowns going in: Is the operator distinction (advisor vs institution) the real seam? Does the Type require custody/processing, or is the data/reporting stack the same Type? What does "platform" mean across the poles? Is the advisory work-product loop (the FAP defining leg) present in this Type?

## Research Questions

1. RQ1 — What is the central record: client/household, account, portfolio, or the business itself?
2. RQ2 — What does the platform consolidate (accounts, positions, valuations, performance; public + private; on-platform vs held-away)?
3. RQ3 — What business machinery sits on the record (billing/fees, trading/rebalancing, custody/settlement, compliance/supervision, operations)?
4. RQ4 — Who operates it (advisor, operations, compliance, executives, client) and what does each role see?
5. RQ5 — What client-facing surfaces exist (reporting, portals, D2C channels)?
6. RQ6 — How does data enter (custodian feeds, aggregation, on-platform custody, manual)?
7. RQ7 — Does the Type require the advisory work-product loop (plan/proposal) that defines the Financial Advisor Platform?
8. RQ8 — Where exactly are the seams vs FAP / PMS / IMP / robo-advisor / brokerage / retirement planning?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers + regional spread:

| Product | Philosophy / pole | Customer tier | Directly researched? |
|---|---|---|---|
| Addepar | data/reporting-centric platform (aggregation + analytics + reporting + billing + portal; no custody, no plan engine) | wealth firms, banks, family offices; UHNW-weighted | Yes — addepar.com root, /wealth-management, /platform-overview |
| SS&C Black Diamond Wealth Solutions | suite pole (CRM + portfolio mgmt & reporting + trading & rebalancing + compliance + trust + alts servicing) | RIAs → broker-dealers → banks & trust companies | Yes — sscblackdiamond.com root + /solutions/portfolio-management-reporting/ |
| SS&C Wealth Platform (GIDS, UK) | processing/infrastructure pole (UK wrap: custody + wrappers + back office + API front-end) | fund managers, DFMs, IFA consolidators, D2C (UK) | Yes — ssctech.com/solutions/wealth-platform |
| FNZ | global end-to-end processing platform (book-of-record + custody + wrappers + fee/tax engines + advisor hub + onboarding; D2C/intermediated/workplace channels) | banks, wealth managers, insurers, asset managers (global) | Yes — fnz.com root, /wealth-management-platforms, /wealth-platform |
| SEI Wealth Platform | front/middle/back office in one infrastructure + operations outsourcing + investment solutions | banks, wealth managers, independent trust companies (US/global) | Yes — seic.com root, /banks-and-wealth-managers/overview, /banks-wealth-managers/what-we-do/wealth-management-technology-and-operations |

Vocabulary anchor (not a Type instance): **Orion** — orion.com/wealth-management fetched to test the sibling pass's "Orion runs both poles as separate divisions" note. Finding: Orion's two divisions are **Advisor Tech** (the software platform: portfolio accounting, Redtail CRM, trading, compliance, planning, portals — the Financial Advisor Platform Type) and **Wealth Management** (**investment services**, not software: TAMP/OCIO/Custom Indexing/proprietary investments via Orion Portfolio Solutions LLC and TownSquare Capital LLC, both SEC-registered investment advisers). This corrects the sibling note's characterization and is recorded under Boundary Findings #1 and Vendor-specific Findings.

## Sources

Tier 1/2 (official vendor pages, fetched 2026-09-08):

- Addepar — https://addepar.com/ ; https://addepar.com/wealth-management ; https://addepar.com/platform-overview
- SS&C Black Diamond — https://www.sscblackdiamond.com/ ; https://www.sscblackdiamond.com/solutions/portfolio-management-reporting/
- SS&C Wealth Platform (GIDS) — https://www.ssctech.com/solutions/wealth-platform ; https://www.ssctech.com/ (industry page: "Wealth Management — 2,700+ firms served with $3.2T in AUM")
- FNZ — https://fnz.com/ ; https://fnz.com/wealth-management-platforms ; https://fnz.com/wealth-platform
- SEI — https://www.seic.com/ ; https://www.seic.com/banks-and-wealth-managers/overview ; https://www.seic.com/banks-wealth-managers/what-we-do/wealth-management-technology-and-operations
- Orion (vocabulary anchor) — https://orion.com/wealth-management

Fetch failures recorded: ssctech.com/products/black-diamond 404 (recovered via sscblackdiamond.com); seic.com/en-us/wealth-platform and /en-us/wealth 404 ×2 (recovered via root + banks-and-wealth-managers paths). No Tier-1 help-center/user-guide documentation was reachable for any sampled product (all evidence is official product/solution/FAQ pages); operational fine structure (exact fee schedules, reconciliation cadences, permission matrices, state machines) is therefore not asserted anywhere.

---

## Product A — Addepar (data/reporting-centric pole)

### Key observations (evidence layer A unless noted)

- Self-positioning: "Addepar is a global data and AI platform empowering investment professionals to turn complex financial information into actionable intelligence." Wealth-management solution page: "Addepar brings your data, workflows and reporting into one platform so you can scale faster, manage complexity with confidence and deliver a more elevated client experience."
- FAQ self-placement inside the category: "What makes Addepar different from traditional wealth management platforms? … Traditional systems often rely on fragmented tools and manual processes … Addepar brings data, insights and workflows together in one platform."
- The wealth picture: "Unify public and private investments in one place so your team can analyze performance, understand exposures and make decisions with a complete view of the portfolio." Alternatives: "Capture and standardize alternative investment data alongside public investments in one unified view. Understand portfolio exposures, performance, and liquidity."
- Data in: "Addepar integrates with hundreds of global custodians, banks and administrators for automated daily data feeds. We also partner with leading market data and pricing providers for up-to-date portfolio valuations, FX rates and benchmark comparisons." Private fund benchmarking against "Addepar's proprietary, anonymized universe of 15,000 private funds."
- Business machinery on the record: billing — "Simplify and automate complex billing. Drive operational efficiency with a dedicated fee management system designed to handle complex fee schedules, asset exclusions and valuation methods. Streamline the bill calculation and review process across accounts to pinpoint discrepancies and audit calculations with access to all underlying data." Reporting — "Deliver personalized reporting that reflects your firm's standards … Automate workflows to streamline the generation and distribution process." Workflows — "Intelligent workflows that drive action. Automate manual work."
- Client experience: "Elevate engagement with a branded client portal. Provide clients with a live view of their net worth and portfolio evolution through an interactive portal. Link external accounts and crypto to present a full portfolio picture … via web or mobile."
- Ownership structures: "Model client and asset structures to mirror real-world ownership and provide a more holistic representation of holdings."
- Roles & governance: role pages for Financial Advisors, Executives, Investors, Operations. "Addepar uses a permissioned data model with granular, role-based access controls so you can manage who sees what across clients, portfolios and entities. This allows advisors, operations and leadership teams to access the right information while maintaining control … and alignment with compliance requirements."
- Firm solutions: Wealth Management, Banks ("Unify client assets, scale advisor and operational capacity"), Family Offices ("Transform multi-custodial data, illiquid alternatives and complex legal entities into a secure, single source of truth powering holistic portfolio management"), Fund Managers, Institutional Allocators.
- What it does NOT claim: no custody, no trading/rebalancing engine, no CRM, no financial-plan engine (Navigator is "advanced scenario modeling" — projections, not the advisory plan workflow).

## Product B — SS&C Black Diamond Wealth Solutions (suite pole)

### Key observations (evidence layer A)

- Self-positioning: "SS&C's award-winning wealth management platform" (SS&C parent nav); "The Cornerstone of a Successful Business. Build your wealth management business your way with all essential functions from one trusted provider." "Complete, Single-Source Solution — Break down product silos and streamline operations across wealth and investment management."
- Scale claims: 1M active users; $4.6+T AUM; 3,300+ firms; "Where Every Corner of Your Firm Connects" — solution wheel: Alternative Asset Servicing, Client Experience & Communications, Trading & Rebalancing, Business Intelligence & Research, Billing & Revenue Management, CRM, Investment Management Services, Trust & Retirement, Compliance, Data Aggregation & Accounting, Portfolio Management & Reporting.
- Solution groups: **Elevate** (CRM, Advisor Client Experience, Annuities & Insurance Marketplace, Black Diamond AI, Integrations); **Streamline** (Portfolio Management & Reporting, Trading & Rebalancing, Investment Management); **Optimize** (Operations & Business Insights, Compliance & Surveillance, Alternative Investments Servicing); **Expand** (Trust Services, Unique Assets/MineralWare, Retirement & Benefits Payments).
- Portfolio Management & Reporting page: "Access all client data, reports, communication, and portfolio management tools from a single command center." "Use an endless combination of data points and date ranges from reliable, clean data." "Full-Service Support — Get back-office support to audit your data, run and batch quarterly statements, and post reports to your client's portal." Reporting = "illustrate your client's complete wealth picture"; branded, batch, or ad-hoc reports.
- Who We Serve: RIAs, Breakaway Advisors, Broker-Dealers, Family Offices, Banks & Trust Companies, Asset Managers, Retirement Services Providers, Foundations.
- No native financial-plan engine observed — planning arrives via integrations (per the FAP pass: MoneyGuidePro/eMoney PDF import; RightCapital lists Black Diamond as an aggregator integration partner). Planning is not among the fourteen solution-wheel entries.

## Product C — SS&C Wealth Platform, GIDS (processing pole, UK)

### Key observations (evidence layer A)

- Self-positioning: "A Complete Platform to Manage All Operational Investment Needs. Technology allied to a regulated service, the SS&C Wealth Platform gives you unparalleled access to powerful technology that energizes your investment capability." "API-first platform, powering advised and D2C propositions" (parent nav).
- Served business models: Fund Managers ("Promote and distribute your fund range or your managed portfolios on your own platform"); Discretionary Fund Managers ("Your own white-labeled platform to distribute your managed portfolio range … directly to intermediaries or direct to retail investors (D2C)"); Advised or D2C Platforms ("Use our API to enable your own front-end user journey, with the SS&C Wealth Platform delivering a regulated back office and custody service"); IFA Consolidators & National IFA Groups ("Power your own white-labeled investment platform").
- Product wrappers: "supports a full wrapper range including GIA, ISA, JISA, SIPP, Offshore Bond + auto bed & ISA + access to 3rd party products … With over 30 third-party DFMs and access to ~3,000 UK funds, all UK-listed (fractional ETFs); Foreign listed."
- Enabling technology list: API Integration, D2C & Advised Proposition Support, DFM Automation, Fractional ETF Trading, Multi-Asset/Multi-Wrapper/Multi-Currency, White Labeling, Floating Model Portfolios.
- Reading: the platform IS the regulated back office and custody layer under white-labeled front ends — the wealth business runs on the vendor's regulated infrastructure.

## Product D — FNZ (global end-to-end processing pole)

### Key observations (evidence layer A)

- Self-positioning: "We are wealth's growth platform … So we provide a global, end-to-end wealth management platform that integrates modern technology, business and investment operations. All in a regulated financial institution which connects to a universe of investment products." Scale: "over US$2.5 trillion in assets on platform … nearly 30 million people across all wealth segments." Clients: Santander, CFS, Vanguard, Aviva, Aberdeen, Barclays, LGT, Swedbank, Raymond James Ltd, Quilter, Lloyds, BMO, UniCredit.
- Wealth Platform page: "A single, integrated platform powering the entire wealth management lifecycle with end-to-end digital scale."
  - "Consolidate fragmented systems into a single, digitized book-of-records platform that supports direct-to-consumer, intermediated, and workplace channels … seamless scalability across markets, brands, and investor segments."
  - "Automate core processes such as custody, reporting, tax, and fee management … Full back-office and infrastructure support ensures reliable, scalable system performance and regulatory compliance."
  - "Support a wide range of product wrappers, asset types, and jurisdictions … Built-in tax and fee engines … including tax wrappers for retirement and savings goals, with integrated performance and risk metrics."
- Features list: Automation of administration ("fully digitized book-of-records solution"); End-to-end product wrapper support; Multi-asset type support ("traditional and alternative assets across multiple exchanges worldwide, with integrated market data services and corporate action processing"); Full back office & infrastructure ("payments, transfers, reconciliations, and regulatory compliance"); Single, digitized book-of-records system ("Centralize client and account data, providing full accounting capabilities, valuations, and performance metrics in one place"); Multi-channel enablement (D2C, intermediated, workplace); Flexible custody options ("FNZ holding assets on your behalf or in your name, with sub-custodian and central securities depository options"); Automated fee & tax engines; Configurable & extensible architecture (cloud-native, API-enabled).
- Companion modules: Advisor Hub ("Fully digitized workspace for Advisors and Central Functions to support the Investment Management process at scale"); Portfolio Manager ("Centralized tools for creating, monitoring, and rebalancing tailored client portfolios, with automated compliance and real-time analytics"); Onboarding ("automation and digitization of customer registration, complying with regulatory requirements"); Digital Advisor; Advice AI.

## Product E — SEI Wealth Platform (institution infrastructure + outsourcing pole)

### Key observations (evidence layer A)

- Self-positioning: "Outsourced technology, operations, and investment solutions to help wealth management firms power growth." Scale: "$8.1 trillion assets on our wealth management platforms"; "9 of top 20 U.S. banks are clients."
- "Built from the ground up, the SEI Wealth Platform℠ is a unified, end-to-end solution that enables your firm to provide a comprehensive, modern and fully integrated advisor and client experience that supports front-, middle-, and back-office services all within a single infrastructure. Integrating technology, operations outsourcing, and asset management in one solution."
- Platform-in-action transcript (operational loop): "By simply logging-in to the Platform, Wealth Managers can access their client's account, their portfolio, and all workflow information … your wealth managers can react, making changes to a client's account with confidence and knowing that the system will process the trades, flag and route any exceptions, and rebalance automatically. Hundreds of transactions are taking place daily across your firm and the SEI Wealth Platform seamlessly processes each and every change. Your CEO can review performance dashboards, examine the firm's growth and with one click they can explore business trends and drill down into client details at the household level."
- Roles: "Explore dashboards for CEOs, COOs, advisors, risk and compliance officers, investment managers and end clients."
- Companion offers: Investment solutions ("curated investment strategies … portfolios tailored to client goals, risk profiles, and preferences"); Professional services; SEI Data Cloud; Managed IT services (SEI Sphere).

## Product F — Orion (vocabulary anchor; not a Type instance)

### Key observations (evidence layer A)

- orion.com/wealth-management: "Orion Wealth Management is the investment back office and operational support behind practices that want flexibility in how they deliver investment management. It runs the full spectrum — from advisor-led open architecture (Investment Portal, Trade Desk, Cash and Credit) through guided partnership (OCIO, Custom Indexing, Strategists, Tailored Allocation Portfolios) to fully outsourced turnkey (TAMP, Wealth Advisory, Proprietary Investments). Services are provided by Orion Portfolio Solutions and TownSquare Capital, both SEC-registered investment advisors."
- Division split: Advisor Tech (software: Portfolio Accounting, Redtail CRM, Trading, Compliance, Risk Intelligence, Planning, Client Portal, Advisor Portal) vs Wealth Management (investment services). "The two divisions integrate … investment data flows through the same Denali Data Layer … Can I use Orion Wealth Management without using Orion Advisor Technology? Yes."
- Reading: "wealth management" in Orion's vocabulary names **investment services** (OCIO/TAMP — investment manufacturing/distribution), not an institution-side software platform. The software platform pole is Orion Advisor Tech, which is the Financial Advisor Platform Type. This corrects the sibling pass's "Orion runs both poles [institution-side platform vs advisor practice system] as separate divisions" — the second pole is investment services, adjacent to the product shelf, not a WMP software instance.

---

## Cross-product Comparison

| Dimension | Addepar | Black Diamond | SS&C Wealth Platform (GIDS) | FNZ | SEI Wealth Platform |
|---|---|---|---|---|---|
| Central record | client portfolios/entities ("model client and asset structures to mirror real-world ownership") | client data + CRM households ("all client data … from a single command center") | client + account data on the platform book ("Centralize client and account data") | client + account data, "single, digitized book-of-records" | client account + portfolio + workflow, "drill down into client details at the household level" |
| Consolidated wealth picture | public + private/alts unified; multi-custodial feeds | portfolio mgmt & reporting; "complete wealth picture"; data aggregation & accounting | on-platform positions (custody + wrappers) | book-of-record with accounting, valuations, performance | client's account + portfolio on-platform |
| Wealth picture sourcing | custodian/bank/administrator feeds (hundreds) + market data | custodian feeds + aggregation + back-office data audit | on-platform custody (regulated back office) | on-platform custody (flexible: vendor-held or in client's name; sub-custodian/CSD) | on-platform (platform processes trades/settlement) |
| Fee/billing machinery | dedicated fee management (complex schedules, exclusions, valuation methods, audit) | Billing & Revenue Management | (fee machinery within back office) | automated fee & tax engines | operations outsourcing incl. billing |
| Trading/rebalancing | none observed | Trading & Rebalancing | DFM automation, fractional ETF trading, floating model portfolios | Portfolio Manager (create/monitor/rebalance + automated compliance) | "process the trades, flag and route any exceptions, and rebalance automatically" |
| Custody/settlement | none (multi-custodial) | none observed (custodian-connected) | regulated back office + custody service | custody + payments/transfers/reconciliations + corporate actions | front/middle/back office + operations outsourcing |
| Compliance/supervision | permissioned data model; "alignment with compliance requirements" | Compliance & Surveillance | regulated service | automated compliance in Portfolio Manager; regulatory compliance in back office | risk and compliance officer dashboards; exception routing |
| Client experience | branded client portal (net worth, portfolio evolution, external accounts + crypto, web/mobile) | Advisor Client Experience; client portal posting; batch quarterly statements | white-labeled front ends via API | multi-channel: D2C, intermediated, workplace | advisor and client experience; end-client dashboards |
| Advisory work products (plan/proposal) | none native (Navigator = scenario modeling) | none native (planning via integrations) | none | planning tools as one module | investment solutions, not plan engines |
| Roles served | advisors, executives, investors, operations | advisors, ops, compliance, leadership (firm-wide wheel) | fund managers, DFMs, consolidators, D2C operators | advisors + central functions; D2C end investors | CEOs, COOs, advisors, risk/compliance, investment managers, end clients |
| Who it serves | wealth firms, banks, family offices, fund managers, allocators | RIAs → broker-dealers → banks & trust companies → asset managers | fund managers, DFMs, IFA consolidators, D2C (UK) | banks, wealth managers, insurers, asset managers (global) | banks, wealth managers, independent trust companies |
| Deployment posture | software over multi-custodial data | software suite | technology + regulated service | platform in a regulated financial institution (+ operations) | technology + operations outsourcing + investment solutions |

### Stable commonalities (evidence layer B — cross-product)

1. **The wealth business's client relationships of record.** Every sampled platform holds persistent identified client/household records for the firm's book (Addepar client/entity structures; Black Diamond "all client data … single command center"; FNZ "centralize client and account data"; SEI household-level drill-down; SS&C GIDS client/account data on the platform book).
2. **The consolidated wealth picture bound to each relationship.** Accounts, positions, valuations, performance — spanning public and private/alternative assets — held as data on the relationship record, however sourced (custodian feeds, aggregation, on-platform custody, back-office data audit).
3. **The business machinery carried on that record.** Every sampled platform runs the firm's revenue and service operations against the record at business scale: fee/billing machinery (Addepar fee management; Black Diamond Billing & Revenue Management; FNZ fee & tax engines), client reporting/experience produced from the record (all five), and the firm's investment/operational processes (trading/rebalancing where present; custody/settlement in the processing poles; compliance/supervision throughout) — with role-scoped access across the firm's functions and out to the client.
4. **Multi-role, firm-wide operating surface.** The record serves every function of the wealth business — advisors, operations, compliance, leadership — plus the end client (SEI's role dashboard list is the explicit statement; Addepar's role pages; Black Diamond's "every corner of your firm"; FNZ's Advisor Hub "for Advisors and Central Functions").
5. **Governance and control as structure.** Permissioned/role-based data models, audit trails, exception handling (SEI "flag and route any exceptions"; Orion's NIGO metric in the same market), regulatory alignment.

### What varies (candidate L2)

- Center-of-gravity pole: data/reporting-centric (Addepar) vs suite (Black Diamond) vs processing/infrastructure (FNZ, SEI, SS&C GIDS).
- Book-of-record posture: custodian-fed aggregation (the platform holds a consolidated copy; custody stays at third parties) vs on-platform custody (the platform IS the book and often the regulated back office).
- Software vs platform+regulated-service (operations outsourcing; custody included; "technology allied to a regulated service").
- Trading/rebalancing depth (none → PMS-shaped engine).
- Advisory work products (absent native in 4/5; one module in FNZ).
- Channel mix: advised / D2C / workplace.
- Regional wrapper regimes (US feeds vs UK GIA/ISA/JISA/SIPP/Bond; superannuation in adjacent markets).
- Client segment: mass affluent → HNW → UHNW/family office.
- Trust/fiduciary operations depth (Black Diamond Trust Services; banks & trust companies as a served segment).
- Investment-services attachment (Orion's division pattern; SEI investment solutions; FNZ asset-management distribution).

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

A Wealth Management Platform is the wealth business's system of record, organized around three jointly-held structures:

1. **The wealth business's client relationships of record** — persistent, individually identified client/household records held by the wealth business (firm, bank wealth division, trust company, broker-dealer wealth channel), accumulating the relationship over time. Not anonymous users; not the firm's own investment books.
2. **The consolidated wealth picture bound to each relationship** — the client's accounts, positions, valuations, and performance held as data on the relationship record, spanning asset classes (public and private/alternative) and however sourced (on-platform custody, custodian feeds, aggregation, manual/back-office entry).
3. **The business machinery carried on that record** — the wealth business's revenue and service operations executed against the record at business scale: fee/billing machinery computing the firm's revenue from the record, client reporting and client experience produced from it, and the firm's investment/operational processes (trading/rebalancing, custody/settlement where on-platform, compliance/supervision) run on it — under role-scoped access spanning the firm's functions and reaching the client.

Jointly-held is load-bearing:

- 1 alone = CRM (relationship records without wealth substance or business machinery).
- 2 alone = a portfolio data/analytics engine (PMS / performance & attribution territory).
- 3 alone = generic business operations software.
- 1+2 without 3 = a consolidated reporting utility / the advisor's practice slice (Financial Advisor Platform territory).
- 2+3 without 1 = the firm's own investment operations (Investment Management Platform territory).
- 1+3 without 2 = business operations on relationships with no wealth substance.

Historical check (§24): the paper-era private bank / trust company — client master files, consolidated statements of holdings, fee ledgers, trust accounting, periodic client reporting — satisfies all three legs at analog level. UK wrap platforms and non-US private-banking systems satisfy without US vocabulary (SS&C GIDS evidence is UK-native). Addepar (no custody, no plan engine) and SS&C GIDS (no planning, no CRM) satisfy from opposite poles. The definition is not overfit to any single era, region, or pole.

### L1 — Common Mature Structure (very common, not defining)

- Custodian/custody data feeds with reconciliation; back-office data audit
- Client reporting (branded, batch quarterly statements, ad-hoc) + branded client portal (web/mobile)
- Trading/rebalancing engine over client portfolios (the PMS-shaped slice)
- Fee/billing engines (complex fee schedules, exclusions, valuation methods, bill review/audit)
- Compliance/surveillance/supervision surfaces; exception handling (NIGO-class)
- Onboarding/KYC and account opening; wrapper/account administration
- Model portfolios / strategists / investment solutions (the product shelf)
- Alternatives data management (capture, standardization, servicing)
- Firm-level dashboards (executive/COO/CEO business views)
- Role-based permissions, audit trail, security frameworks
- Integration ecosystem + APIs; AI assistance entering the sample

### L2 — Variant / Optional Structure

- Center-of-gravity pole (data/reporting vs suite vs processing/infrastructure) — same Type, different poles
- Book-of-record posture: custodian-fed aggregation vs on-platform custody
- Software vs platform+regulated-service (operations outsourcing, custody included)
- Channel mix: advised / direct-to-consumer / workplace
- Regional wrapper and tax regimes
- Client segment packaging (mass affluent → HNW → UHNW/family office)
- Trust/fiduciary operations depth
- Investment-services attachment (OCIO/TAMP-class offerings adjacent to the platform)
- Planning/projection modules (embedded-planner pattern)

### L3 — Vendor-specific (research notes only)

- Addepar: Addison (AI insights), ADX (connected financial intelligence), Alts Data Management, Navigator (scenario modeling), Private Fund Benchmarks (15,000-fund anonymized universe), Sandbox; "hundreds of global custodians, banks and administrators"; SOC 2 Type II alignment claim.
- Black Diamond: Elevate/Streamline/Optimize/Expand solution groups; Annuities & Insurance Marketplace; MineralWare (unique assets); Retirement & Benefits Payments; 1M active users / $4.6+T AUM / 3,300+ firms claims; bdreporting.com login.
- SS&C GIDS Wealth Platform: GIA/ISA/JISA/SIPP/Offshore Bond wrapper set; auto bed & ISA; 30+ third-party DFMs; ~3,000 UK funds; fractional ETF trading; floating model portfolios; white labeling; Hubwise acquisition context.
- FNZ: FNZ Atlas (10-stage delivery lifecycle), Advisor Hub, Advice AI, Digital Advisor, Q-Hub (retirement product integration), FNZ Select; $2.5T AoP / ~30M end investors claims; flexible custody (vendor-held vs in client's name; sub-custodian/CSD).
- SEI: SEI Wealth Platform℠; SEI Data Cloud; SEI Sphere (managed IT); $8.1T platform assets; 9-of-top-20 US banks claim; investment solutions via SEI Investments Management Corporation.
- Orion: division structure — Advisor Tech (software) vs Wealth Management (investment services via Orion Portfolio Solutions LLC / TownSquare Capital LLC, SEC RIAs); TAMP/OCIO/Custom Indexing/Trade Desk/Cash & Credit (Uptiq); Denali Data Layer as the shared data spine.

---

## Vendor-specific Findings

See L3. None promoted to the canonical model. Vendor scale claims (AUM, firm counts, NIGO rates, growth stats) are marketing assertions and were not carried into the final document.

## Boundary Findings

1. **vs Financial Advisor Platform (joint review DISCHARGED — keep both, seam = center of gravity).** The FAP is the advisor's practice system: its defining core requires the advisory work-product loop (household → position → plan/proposal/reports maintained over the relationship). The WMP is the wealth business's system of record: its defining core requires the business machinery (fee/billing, reporting, investment/operational processes at firm scale) — and does NOT require the work-product loop. Cross-check against the samples: 4/5 WMP products have no native plan/proposal engine (Addepar: none; Black Diamond: planning via integrations; SS&C GIDS: none; SEI: investment solutions; FNZ: one module among many), while the business machinery that defines WMP leg 3 is only L1/L2 in the FAP (absent in planning-led FAPs such as RightCapital). Conversely, a planning-led FAP lacks WMP leg 3 entirely. Removal tests hold both ways: strip the business machinery from a WMP → an advisor practice tool (FAP slice); add the work-product loop as the center → FAP. Straddle zone: all-in-one products (Orion Advisor Tech, Black Diamond, Envestnet-class) carry both structures and are sold into both readings — the seam is the center of gravity, not a wall. **Correction to the sibling pass's evidence note:** Orion's two divisions are Advisor Tech (software platform = FAP Type) and Wealth Management (**investment services** — OCIO/TAMP via SEC-registered adviser affiliates, not an institution-side software platform). The "same vendor, two divisions" observation stands, but the second division is investment services adjacent to the product shelf, not a WMP software instance.
2. **vs Robo-advisor (advice-spectrum seam DECIDED — boundary held).** The robo-advisor is the consumer-side, self-service, automated pole: the service constructs and maintains the portfolio; no human advisor operates the account; the record is the consumer's account. The WMP is the business-side system of the advisor-led pole: human advisors operate over the platform; the record is the business's client-relationship book. Hybrid human-advice tiers in robos (CFP 1:1) do not collapse the boundary — the account remains self-service-operated. Conversely, D2C channels on wealth platforms (FNZ multi-channel; SS&C GIDS D2C) do not collapse it either — the platform's center remains the business operating many client relationships, with the D2C channel as one served surface. Decision-authority + operator tests hold across the sample.
3. **vs Retirement Planning Application (embedded-planner flag DISCHARGED — boundary held structurally).** Planning/projection capability appears inside wealth platforms (Addepar Navigator "project future outcomes with advanced scenario modeling"; FNZ "planning and portfolio tools") as an embedded module. The object of record remains the client relationship + wealth picture, not the household plan. Same capability-overlap pattern the robo pass confirmed; the planner remains the retirement Type's artifact wherever it is packaged.
4. **vs Portfolio Management System (slice note CONFIRMED).** The trading/rebalancing engines inside wealth platforms (Black Diamond Trading & Rebalancing; FNZ Portfolio Manager "creating, monitoring, and rebalancing tailored client portfolios, with automated compliance"; SEI "process the trades … and rebalance automatically") satisfy the PMS L0 — portfolios, intent (models/risk profiles), forward loop. Per the PMS pass's recorded note, they are treated as a PMS-shaped slice inside the wealth platform, not a separate Type.
5. **vs Investment Management Platform (consistent with the IMP pass).** Client-centric (the wealth business's client relationships of record) vs investment-centric (the investment organization's own books and lifecycle). FNZ and SEI serve asset managers as an extension (distribution; investment solutions), the extension pattern the IMP pass documented (Aladdin Wealth; Charles River wealth solution) — not a merger. Removal test: strip the client relationships and center on the firm's own books → IMP territory.
6. **vs Brokerage Platform.** The brokerage is the self-directed trading and custody/account infrastructure for investors acting on their own decisions. The processing-pole wealth platforms include custody/trading infrastructure, but bound to the client-relationship record and the advisory business machinery; strip the relationship record and advisory machinery → brokerage/custody infrastructure territory.
7. **vs CRM.** The relationship record without the wealth picture or the business machinery. Wealth platforms consume/embed CRM (Black Diamond CRM module; the FAP pass's Wealthbox/Redtail) — the CRM is a component, not the Type.
8. **vs Investor Portal.** The client-facing portal/reporting surface is one output of the wealth platform (all five samples produce one); the portal alone is the slice, not the Type.
9. **vs Trust/fund-administration systems.** Trust services and alts servicing appear as modules (Black Diamond Trust Services, Alternative Investments Servicing); fund administration remains the administrator's books-and-investor-register Type. Adjacent, not merged.

Taxonomy observations (for STATUS Boundary Issues):

1. The vocabulary straddle flagged by the FAP pass is **confirmed and sharpened**: "wealth management platform" in market usage names (a) the wealth business's platform of record (this Type — all five sampled products), (b) sometimes the advisor practice stack (FAP — all-in-one products straddle), and (c) sometimes investment services (Orion's division naming). Keep-both WMP/FAP is ratified with the work-product-loop vs business-machinery seam; the Orion correction is recorded.
2. The Type is naturally a **stack/spectrum of poles** (data/reporting → suite → processing/infrastructure), realized differently by segment and region; the canonical model is the record + machinery, with pole as variant posture — same modeling decision as the FAP pass made for stack composition.

## Uncertainties

- No Tier-1 help-center/user-guide documentation was reachable for any sampled product; all evidence is official product/solution/FAQ pages. Operational fine structure (exact fee-schedule mechanics, reconciliation cadences, permission matrices, order/exception state machines, wrapper tax rules) is therefore not asserted anywhere.
- Addepar's billing/trading boundary: billing is explicit; the absence of a native trading/rebalancing engine is an observation of the fetched pages, not a verified product fact (integrations may supply it).
- Black Diamond's data-sourcing mechanics (custodian feed list, aggregation partner) were not fetched in detail; the FAP pass's integration evidence (RightCapital lists Black Diamond as an aggregator) is cross-source.
- SEI's platform internals (module list, wrapper support) are evidenced by the overview + platform page + video transcript; deeper module documentation was not reachable.
- Non-sampled poles: InvestCloud, Avaloq, Temenos wealth, Envestnet enterprise — not fetched; the processing pole is evidenced by FNZ/SEI/SS&C GIDS and should generalize, but the sample may under-represent core-banking-adjacent wealth systems.
- Regional depth beyond US/UK (Swiss, Asian private-banking platforms, Australian platforms) not directly sampled; the historical/regional check rests on the UK evidence + abstraction reasoning.

## Final Synthesis

A Wealth Management Platform is the wealth business's system of record: the platform on which a wealth business holds its client relationships and their consolidated wealth picture, and runs the business machinery — fee/billing, client reporting and experience, investment and operational processes, compliance — against that record at business scale, under role-scoped access that spans the firm's functions and reaches the client. The market realizes the Type on a spectrum of poles: data/reporting-centric platforms over multi-custodial data, all-in-one wealth suites, and end-to-end processing infrastructures where the platform is also the regulated back office and custody layer. The defining core is the record + machinery, not any pole: the advisory work-product loop that defines the Financial Advisor Platform is absent natively from most of this sample, and the business machinery that defines this Type is only optional structure in the FAP. The Type sits at the business-side center of the advice spectrum (self-directed brokerage → robo self-service → advisor-led wealth business), carries the PMS as its investment slice, and is the client-centric counterpart to the investment-centric Investment Management Platform.
