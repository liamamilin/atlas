# Research Notes — Cap Table Management

Research date: 2026-09-07
Leaf: `Cap Table Management` (DIRECTORY.md §08 Finance, Banking, Insurance & Investment)
Slug: `cap-table-management`

---

## Research Goal

Understand what cap table management software actually is as an application type: the artifact it maintains (the capitalization table), the objects inside it, the events that change it, the derived outputs users need from it, the interfaces each role works in, and the rules that govern it — then abstract a vendor-neutral model with a minimal defining core.

## Initial Boundary (pre-research hypothesis)

- Core use: a company-side record of who owns the company (shares, option grants, convertible instruments) and how that ownership evolves.
- Primary users: founders / CFO / finance-ops at private companies; counsel; employees and investors as portal users.
- Nearest neighbors: Investor Portal (distribution surface to investors), Fund Administration Platform (fund-level LP/GP accounting), Deal Management for PE/VC (investor-side), public-company equity/share plan administration (Shareworks-style), Accounting/General Ledger (expense reports downstream).
- Known unknowns: exact event taxonomy; whether scenario modeling is definitional or common; where the private/public seam sits; how deep the document/signature machinery goes; whether pools/plans are definitional or just universal in venture-backed companies.

## Research Questions

1. What is the cap table artifact: rows, columns, semantics?
2. What security/holder types exist across products?
3. What events mutate the table, and how are they recorded (typed transactions? draft/publish? audit trail?)
4. What is derived from the table (ownership %, fully diluted, dilution, waterfalls, expense reports, tax forms, valuations)?
5. What modeling/scenario features exist?
6. Who uses what interface (admin vs employee vs investor vs advisor)?
7. What rules matter (pools, vesting, conversion semantics, authorization, confidentiality/access)?
8. How do products vary (segment, geography, private vs public, ecosystem breadth)?

## Representative Products

| Product | Why selected | Segment / philosophy |
|---|---|---|
| Carta | Market-dominant incumbent; full private-capital ecosystem | US; all-in-one (equity + fund admin + valuations + transfer agent); startup → late stage |
| Pulley | Startup-focused challenger; publicly rich help center | US; product-led, startup-first, transparent pricing |
| Ledgy | European leader; private → public span | EU/UK; multi-jurisdiction compliance; extends to public-company share plans and executive comp |
| Eqvista | Value segment; valuation-led philosophy | US; free cap table tier + 409A valuation services; SEC-registered transfer agent |

Shareworks by Morgan Stanley (enterprise/public-company pole) was targeted as a fifth sample but its site timed out twice and was abandoned (see Source-access Limitation). Ledgy's Public Company Admin Guide partially covers that pole.

## Sources

### Carta (Tier 2 — product pages; no operational help-center pages fetched)

- https://carta.com/ (home: positioning, ecosystem, scale figures) — fetched 2026-09-07
- https://carta.com/cap-table/ (cap table product page: feature claims, compliance list, FAQ) — fetched 2026-09-07

### Pulley (Tier 1 — Intercom help center)

- https://help.pulley.com/en/ (help center home: collection map) — fetched 2026-09-07
- https://help.pulley.com/en/collections/2714799-recording-securities (Recording Securities: shares, convertible notes, warrants, SAFEs, RSUs/RSAs, options, share classes, equity plan, profit interests, phantom stock) — fetched 2026-09-07
- https://help.pulley.com/en/collections/3437018-cap-table-flows (Transfers/repurchases/cancellations, conversions, terminations, exercise workflows, reprice, reclassify, spreadsheet mode, NPM liquidity) — fetched 2026-09-07
- https://help.pulley.com/en/collections/2714801-fundraising-modeling (fundraising modeler: equity rounds, SAFE conversion, pro-rata, dilution, multi-currency, Excel version) — fetched 2026-09-07

### Ledgy (Tier 1 — Intercom help center + Tier 2 marketing site)

- https://www.ledgy.com/ (product map: cap table, equity plan automation, share plan admin, trading & settlement, compliance, financial reporting, valuations, IPO prep, executive comp, AI) — fetched 2026-09-07
- https://help.ledgy.com/en/ (help center home) — fetched 2026-09-07
- https://help.ledgy.com/en/collections/1079721-admin-guide (Admin Guide, 165 articles: stakeholder mgmt, cap table & share classes, transactions, HRIS, reports, documents, pools & plans, equity events, company settings, public-company admin, AI) — fetched 2026-09-07
- https://help.ledgy.com/en/articles/20511-what-transaction-types-can-i-add-on-ledgy (full transaction-type taxonomy) — fetched 2026-09-07

### Eqvista (Tier 2 — product/services pages)

- https://eqvista.com/ (services map: cap table, cap table transfer, 409A/valuations, transfer agent registration, compliance list, waterfall & round modeling, board resolutions) — fetched 2026-09-07

### Not accessible

- https://www.shareworks.com/ (Morgan Stanley Shareworks) — timed out twice 2026-09-07; abandoned. No Shareworks-specific claims are made anywhere in this research.

### Source-access Limitation

- Carta and Eqvista evidence rests on official product/services pages (Tier 2), not operational help centers; feature-level claims from them are kept coarse.
- Pulley and Ledgy evidence is Tier 1 (operational help centers), including one complete transaction taxonomy (Ledgy).
- Consequently the strongest structural claims in the synthesis are anchored on Pulley + Ledgy, with Carta/Eqvista used to confirm cross-product commonality at coarser granularity.
- No precise numeric limits (share counts, prices, fees, time windows) are asserted in the final document; none were needed.

---

## Product Observations

### Carta

**Key observations (evidence layer A unless noted):**

- Positioning: "ERP for private capital" — a suite spanning equity management, fund administration, portfolio management, and legal/compliance services; "connected" data as the differentiator (home page).
- Cap table product page: "view, track, and issue equity"; explicit anti-spreadsheet framing ("No more spreadsheets, no more errors").
- Core feature set claimed: cap table and security holder management; electronic issuing of shares to stakeholders; stock transfers; employee equity plan generation; electronic exercising.
- Growth-stage features: automatic stakeholder updates via HRIS and payroll integration; secure money movement (SEC-registered transfer agent; ACH/wire); data room, board consents, investor updates.
- Compliance features claimed: 409A valuations, GAAP and IFRS reporting, QSBS attestation, Rule 701 management, 83(b) form, Form 3921.
- Core feature list on the same page: SAFE financings (issue "in three clicks"), 409A valuations, financial reporting ("stock-based compensation reports on demand"), scenario modeling ("understand the impact of future fundraising rounds on your ownership").
- FAQ: free tier for early-stage companies (Carta Launch); support for LLCs and private equity; onboarding via implementation team.
- Scale claims (home): 50,000+ companies, 1.7M+ equity holders, 9,000+ funds/SPVs — ecosystem extends well beyond a single company's cap table.
- Customer quote (Kayne Anderson VP): capital activity at a portfolio company reflects in the cap table "within a day or two" — network-side data flow; treated as vendor claim, not a rule.

### Pulley

**Key observations (evidence layer A — operational help center):**

Help-center collection map gives the product's own taxonomy of concerns:

- Onboarding: "upload your cap table" (first-time setup) — migration is a first-class flow.
- Recording Securities collection: general granting of new securities; recording previously signed shares; restricted stock purchase agreements; convertible notes; warrants; SAFEs (incl. pre- vs post-money distinction, MFN, YC SAFEs, per-field guidance, SAFE compliance alerts); RSUs (settling RSUs, recording past settlements); RSAs; options (recording grants, granting, ISO/NSO split calculation, exercise period choices); share classes (adding, amending, creating a class that does **not** contribute to fully diluted); equity plan (record, edit/amend, sizing guidance, termination); profit interests; phantom stock plans.
- Cap Table Flows collection: transfers, repurchases (conduct + reflect past), cancellations, forfeitures; modify/delete securities; converting SAFEs and notes (+ undoing a conversion); employee terminations; option exercising — holder side (submit payment, tax implications, post-termination exercise) and admin side (exercise requests setup, status page, undo exercise, NSO tax withholding management, e-signing exercise documents); option repricing; share reclassification; assigning **reviewers to securities** (review workflow); NPM (secondary liquidity for shareholders); spreadsheet mode for bulk editing.
- E-signing on Pulley: issuing documents for signing inside the platform.
- Compliance collection: Rule 701, Form 3921, and related.
- 409A Valuations collection: obtaining a 409A on Pulley (service integration).
- Fundraising & Modeling: model an equity round (e.g., Series A); model SAFEs (post-money SAFE conversion math); pro-rata rights and their dilution effect; dilution education; multi-currency modeling; Excel version of the modeler.
- Stakeholder Experience collection: adding stakeholders to Pulley (portal).
- Data Room collection; Company Profile Setup & Settings; Managed Services ("let us manage your cap table"); Token Cap Tables & Crypto collection (26 articles).
- Stock Based Compensation collection: SBC tooling.

### Ledgy

**Key observations (evidence layer A — operational help center + marketing site):**

Marketing site product map:

- For private companies: Equity Plan Automation, Employee Engagement (dashboard), IPO preparation, **Cap Table Management** ("keep your cap table accurate and up to date").
- For public companies: Share Plan Administration, Employee Communications, Trading and Settlement, SAYE.
- Reporting/compliance: cross-jurisdiction equity compliance, Financial Reporting (IFRS 2 expensing named in FAQ), Company Valuations (service).
- Executive compensation: equity + deferred compensation + carried interest ("world's first unified platform for all non-cash compensation").
- Finance/legal/people framing: "single source of truth" shared across finance (IFRS 2, exit distributions), legal (grant types, automated granting incl. contracts and signatures, single-click compliance reports), people (employee dashboard).
- HRIS integrations (70+ named in FAQ); migration service (4-stage: setup, extraction, import, validation); security posture (ISO 27001, SSO/SCIM, role-based access).
- AI: Ledgy Agent & MCP (query live equity data, automate admin).

Admin Guide structure (help center):

- **Stakeholder Management**: adding/bulk-importing stakeholders; groups; custom fields; inviting to dashboard / revoking access; previewing a stakeholder's dashboard; sharing information with groups; sharing KPIs with stakeholders; creating and sharing investor updates; FATCA/CRS tax certification collection; offboarding collection.
- **Cap Table & Share Classes**: importing the cap table; adding/editing share classes; share numbering; creating super-voting shares; **anonymising stakeholders when sharing the cap table**; exporting the cap table.
- **Transactions** (single most important collection — full taxonomy from the dedicated article):
  - Financing round: define event name, share class, share price; each investment records stakeholder, amount, number of shares; option to set up an employee pool with the round.
  - Issue shares (exercises also appear as share issuances); Decrease shares (cancellation reduces total).
  - Share transfer (between stakeholders/entities; optional transfer price).
  - Convertible loan (cap, discount, interest, expiry; "Convert to Shares" creates a linked share-issuance transaction).
  - Issue grants: options, phantoms, warrants, SAR, BSPCE, RSU, RSA, UK growth shares, EMI — with time-based or custom vesting, strike/exercise price, purchase price.
  - Cash settlement of grants (incl. returning settled amounts to the pool).
  - Valuation events: company valuation, 409A (US), EMI (UK), CSOP (UK), fair value.
  - Class conversion; Stock split (auto-adjusts earlier-dated transactions); Dividends (per share class, filterable); Payout (cash to a stakeholder).
  - Bulk import of transactions; edit transactions; **audit trail per transaction**; beneficiaries; multi-currency transactions; custom fields; "publish transactions" (draft → published lifecycle); equity settlement import with signatures; Share Lots.
- **HRIS integrations**: BambooHR, Personio, Workday, SAP SuccessFactors, HiBob, etc.
- **Reports**: valuation report; compliance / operational / financial report categories; anonymized report access.
- **Documents**: grant letter templating + DocuSign signing workflows; digital share certificates; document upload/share/attach; Document Auditor (audit equity documentation); bulk grant import with auto-generated grant letters; signature, templating, holding confirmations, data room collections.
- **Equity Pools & Plans**: pools vs plans distinction; creating/increasing/decreasing pools; multiple plans per pool; pools from reserved shares of stakeholders; creating plans; grant presets; automated granting; **excluding pools from the cap table**; Employee Benefit Trust (EBT); STAK Foundation; EMI scheme (UK); performance-based vesting conditions; document templates on plans; vesting schedule configuration; grants & exercising collections.
- **Equity Events**: dividend equivalents; Tax Rules setup; DRIP (dividend reinvestment); selling windows.
- **Company Settings**: collaborator roles (default + custom); SCIM; SSO; fractional shares; base currency; stakeholder scenarios (modeling); stakeholder bank details collection; session length; anonymized financial-reporting access.
- **Public Company Admin Guide**: trading restriction periods; release election windows for RSU/PSU settlements; self-managed trading; limit orders for share sales.

### Eqvista

**Key observations (evidence layer A on listed service structure, coarse — marketing/services pages only):**

- Positioning: "equity management and valuations"; "pricing infrastructure for private markets"; #1 409A provider (G2/Clutch) — valuation-led philosophy; SEC-registered transfer agent (footer).
- Cap Table services: Cap Table, Cap Table Transfer (migration from other providers or spreadsheets), One-Time Setup, Financial Modeling, Equity Advisory, All Cap Table Services.
- Cap Table Management feature list: Cap Table & ESOP management, vesting schedules, shareholder accounts, **board resolutions & voting**, 83(b) election / Rule 701 / Form 3921 / ASC 718, **waterfall & funding round modeling**.
- Valuation services around the table: 409A valuation, real-time company valuation app, fair market valuation, software/IP valuation, gift & estate tax valuation, portfolio/ASC 820 valuation, QSBS attestation letters.
- Liquidity programs: company-sponsored tender offers; Eqvista 100.
- Employee dashboard named in customer reviews (transparency to employees).
- Free tier ("Get Cap Table — It's free!").

---

## Cross-product Comparison

| Dimension | Carta | Pulley | Ledgy | Eqvista | Assessment |
|---|---|---|---|---|---|
| Subject of record | company cap table + security holders | company cap table | company cap table & share classes | company cap table | All: company-side ownership record |
| Holders modeled | stakeholders | stakeholders | stakeholders (individuals/entities, groups, custom fields, beneficiaries) | shareholders | Common (names differ) |
| Ownership shares | shares | shares (incl. restricted stock purchase agreements) | shares in classes (super-voting, non-FD classes) | shares | Common; class structure common-mature |
| Equity awards | equity plans, electronic exercising | options (ISO/NSO), RSUs, RSAs, profit interests, phantom | options, RSU, RSA, warrants, SAR, BSPCE, UK growth shares, EMI, phantoms | ESOP/option mgmt | Common; award-type breadth varies by market |
| Convertibles | SAFE financings as first-class issue flow | SAFEs (pre/post-money, MFN) + convertible notes + conversion + undo | convertible loans (cap/discount/interest/expiry) + linked conversion | implied by round modeling | Common in VC-shaped markets |
| Mutating events | issue, transfers, exercising | grants, transfers, repurchases, cancellations, forfeitures, conversions, exercises, terminations, repricing, reclassification | financing rounds, issue/decrease shares, transfers, convertible loans, grants, cash settlements, class conversions, splits, dividends, payouts | issuance, board actions | All: typed, dated events; taxonomy varies |
| Record integrity | platform-managed | drafts; reviewers on securities | draft → published transactions; per-transaction audit trail; document auditor | board resolutions & voting | Common pattern: recorded, attributable changes |
| Pool/plan capacity | equity plan generation | equity plan record/amend/terminate | pools vs plans, pool sizing, exclude from FD | ESOP management | Common |
| Vesting | equity plan machinery | vesting schedules collection (acceleration, legends) | time/custom/performance vesting, tranche builder | vesting schedules | Common |
| Ownership math | implied by table UI | fully diluted concept (classes can be excluded) | fully diluted concept (pools can be excluded) | implied | Common: outstanding + fully diluted aggregation |
| Valuations | 409A as connected service | 409A collection | valuation **events** on the timeline (409A/EMI/CSOP/company/fair value) | 409A + valuation suite (core of product) | Common: recorded valuations underpin option pricing; type names are jurisdictional |
| Compliance outputs | 409A, GAAP/IFRS reporting, QSBS, Rule 701, 83(b), 3921 | Rule 701, Form 3921, 83(b) (federal exemptions guidance) | country-specific compliance reports, IFRS 2, FATCA/CRS collection | 83(b), Rule 701, 3921, ASC 718, QSBS | Common category; specific forms are jurisdictional |
| Scenario modeling | scenario modeling (fundraising impact) | fundraising modeler (equity/SAFE rounds, pro-rata, multi-currency) | stakeholder scenarios; exit distributions named in finance framing | waterfall & funding round modeling | Common across all four |
| Stakeholder portal | investor updates, board consents | stakeholder experience collection | stakeholder dashboards, invite/revoke, preview, KPIs | shareholder accounts, employee dashboard | Common |
| Documents & signatures | board consents; docs implied | e-signing collection; previously signed share recording | grant letters, DocuSign, digital share certificates, holding confirmations, data room | implied (board resolutions) | Common; depth varies |
| Migration | implementation team onboarding | upload your cap table; managed services | cap table import; 4-stage migration service | cap table transfer service | Common: switching is a designed workflow |
| Adjacent scope | fund admin, SPVs, transfer agent, AI plugins | token/crypto cap tables, NPM liquidity, data room | public-company share plans, trading & settlement, executive comp, DRIP, selling windows, AI agent/MCP | tender offers, valuation suite, banking | Variant — defines each vendor's pole, not the Type |

---

## Canonical Model (L0–L3 abstraction)

### L0 — Defining Invariant (deliberately minimal)

The smallest structure without which the software is not recognizable as cap table management:

```text
Issuing company (the subject of the record)
└── Stakeholders — identified holders (individuals or entities)
    └── Securities — the ownership instruments the company has created
        (shares, and contract-style ownership instruments)
        └── Holdings — the binding of a stakeholder to a quantity of a security,
            with terms (dates, prices, conditions)
    └── Computed ownership — percentages derived from holdings
        (per class and in aggregate)
└── Maintained over time — the record persists and is updated as
    ownership changes (the "management" in cap table management)
```

Five properties. Remove any one:

- no issuing-company record → it is not about a company's equity;
- no identified stakeholders → an instrument registry, not an ownership table;
- no securities/holdings → no cap table artifact at all;
- no computed ownership → a raw instrument list, not a capitalization **table**;
- no maintained-over-time dimension → a static snapshot generator, not management software.

**§24 historical check.** Pre-software practice: share ledgers / registers of members maintained in corporate records, and founder spreadsheets tracking share issuance round by round — all satisfy this core (holders × securities × holdings, computed ownership, updated as ownership changes). Regional instruments (e.g., UK EMI options, French BSPCE, German-listed company registers) change the instrument vocabulary, not the structure. Therefore the core must not encode: venture-backed round structures, preferred-share liquidation stacks, option pools, 409A, or US forms — a two-founder company with a single common class is still fully within the Type.

### L1 — Common Mature Structure

Present across the researched sample; expected of any mature modern product; not definitional:

- **Share classes** with distinct rights (e.g., voting vs non-voting; super-voting shares; classes excluded from fully-diluted math).
- **Typed, dated transaction machinery** mutating holdings: issuance, transfer (optionally with price), exercise, conversion of convertibles, cancellation/repurchase/forfeiture, class conversion, stock split (auto-adjusting history), dividends/payouts; bulk import; draft → published lifecycle; per-transaction audit trail.
- **Equity plan / option pool** as reserved, unallocated capacity that grants draw down; pool sizing and amendment; ability to exclude pools from fully-diluted figures.
- **Vesting** on awards (time-based schedules, tranches, acceleration; performance conditions in some products); post-termination exercise handling.
- **Financing round as a composite event** (name, share class, price, multiple investments, optional pool top-up) rather than N disconnected issuances.
- **Convertible instruments** (SAFEs, notes) held as pending instruments with conversion semantics (cap/discount; pre- vs post-money distinctions) and a recorded conversion step.
- **Recorded valuations** on the timeline that underpin award pricing (409A in the US; EMI/CSOP/company/fair-value types elsewhere).
- **Compliance & tax outputs**: share-based-payment expense reporting (US GAAP / IFRS 2), issuance-exemption tracking (e.g., Rule 701), participant tax forms (e.g., 83(b), 3921), eligibility attestations (e.g., QSBS).
- **Scenario modeling**: pro-forma rounds and dilution; SAFEs' conversion effect; pro-rata; waterfall/exit distributions (waterfall explicitly named by two of four).
- **Stakeholder portals**: employees/investors see their own holdings, vesting, documents; invite/revoke; admins can preview.
- **Document generation & e-signature**: grant letters, certificates, exercise documents; holding confirmations; data room.
- **Confidentiality & governance**: role-scoped admin access; anonymized sharing of the table; auditability.
- **Migration as a designed workflow**: import from spreadsheets or a competitor; sometimes a white-glove service.
- **Cap table views & exports**: the ownership table itself (outstanding vs fully diluted, per class, over time); export/share.

### L2 — Variant / Optional Structure

Depends on segment, geography, stage, or business model:

- **Public-company extension**: share plan administration at scale, trading restriction/blackout windows, release election windows, settlement & broker integration, limit-order support, SAYE.
- **Jurisdiction-specific schemes and forms**: US (409A, QSBS, 83(b), 3921, Rule 701, ASC 718), UK (EMI, CSOP, growth shares), France (BSPCE), FATCA/CRS collection; multi-currency records.
- **Instrument breadth**: profit interests (LLCs), phantom stock, SARs, token/crypto cap tables.
- **Ecosystem breadth**: fund administration & SPVs (Carta pole), executive/deferred compensation & carried interest (Ledgy pole), valuation service suite (Eqvista pole).
- **Liquidity machinery**: company-sponsored tender offers, secondary-market programs (NPM), selling windows, DRIP.
- **Corporate-form machinery**: board resolutions & voting; employee benefit trusts; STAK foundations.
- **Integrations**: HRIS (grant population from HR), payroll, e-signature providers; AI agents/MCP over live equity data (era-common).
- **Managed services**: vendor runs the cap table for the customer.
- **Free tiers** for early-stage; managed onboarding as competitive differentiator.

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Carta: "ERP for private capital" framing; Carta Launch free tier; Carta Plugins for Claude; SEC transfer agent status; scale figures (50,000+ companies, 1.7M+ equity holders); Kayne Anderson "day or two" data-flow quote.
- Pulley: spreadsheet mode; reviewers assigned to securities; NPM; YC SAFE specifics; Excel version of the fundraising modeler; token cap table collection (26 articles).
- Ledgy: Tranche Builder grant cards; Document Auditor; EBT/STAK setup; share lots; super-voting share creation; anonymized report access; Ledgy Agent & MCP; ISO 27001/SSO/SCIM posture; 70+ HRIS integrations claim; "world's first unified platform for all non-cash compensation" claim; Edge Summit.
- Eqvista: Real-Time Company Valuation® (registered trademark); free tier; #1 409A provider (G2/Clutch) claim; 25,000+ customers claim; Eqvista 100; banking (Cheqly) / venture debt adjacency.

### Anti-overfitting notes

- SAFEs/convertibles are universal in the *sample* because the sample is venture-shaped; a cap table for a family company has none. Convertible support is therefore L1 (common), not L0 — the L0 phrase "securities" covers instruments generally.
- Financing rounds are the signature *event* of this market but a composite of issuances; kept in L1.
- 409A appears in every product (3 as service, 1 as valuation-event type) but is US-specific → L1 as "recorded valuations," L2 as "409A" specifically.
- Employee portals are present in all four but are derivative of the record (a window onto holdings) → L1.

---

## Vendor-specific Findings

See L3 above. None of these entered the canonical core.

---

## Boundary Findings

| Neighbor Type | Overlap observed | Distinction — the seam | "Remove X" test |
|---|---|---|---|
| **Investor Portal** (same directory section) | Cap table products ship investor/stakeholder dashboards (Ledgy investor updates & KPI sharing; Carta investor updates; Pulley stakeholder experience) | The portal is a distribution/communication surface *onto* records; its defining core is the investor-facing delivery of holdings/reports/documents, not the maintenance of the ownership record. Cap table management's defining core is the record itself. | Strip the ownership ledger and keep only investor-facing distribution → you have an Investor Portal. Strip the portal and keep the ledger → still unmistakably cap table management. |
| **Fund Administration Platform** | Carta sells both; VC funds appear as cap table stakeholders | Fund admin's subject is a fund's LP/GP structure, capital calls, NAV, fund accounting. Cap table management's subject is one operating company's equity. Different objects, different operators, different math. | Replace the company's shareholder ledger with LP capital accounts & fund financials → different Type. |
| **Deal Management for PE/VC / Private Market Investment Platform** | Investors touch cap tables of portfolio companies (Carta's investor-side views) | Those types are investor-side, pipeline/deal-shaped; the record owner is the investor, not the issuing company. | The operator flips from issuer to investor → different Type. |
| **Public-company share plan administration** (Shareworks pole; Ledgy extends here; directory has no dedicated private-cap-table leaf to conflict with) | Same record object (securities, holders, grants) | For public companies the record is a registry of listed-share plan participants with trading/settlement machinery; the defining workflow centers on plan administration and market transactions, not round-by-round private ownership evolution. Ledgy/Shareworks span both — a packaging choice, not evidence the types are one. | Remove private-round financing mechanics and add exchange trading/settlement → plan administration Type. |
| **Accounting Software / General Ledger** | Cap table products produce expense reports (ASC 718/IFRS 2) that feed accounting | The ledger records the company's money; the cap table records the company's ownership. Expense reports are an *output*. | Replace ownership record with double-entry journaling → different Type. |
| **Board / Corporate Governance Platform** | Eqvista does board resolutions & voting; Carta does board consents; both sit next to governance workflows | Governance platforms' subject is board/committee operations across matters; equity machinery here is bound to the ownership record only. | Keep only consents/resolutions, drop the ledger → governance Type. |
| **Legal Entity Management** | Both keep corporate records | Entity management covers entities' statutory data, officers, filings across an org; cap table covers one company's equity instruments. | Strip securities/holdings, keep entity/officer registry → different Type. |

**Taxonomy note:** the directory places Cap Table Management, Investor Portal, Fund Administration Platform, and Deal Management for PE/VC as siblings in §08. Research supports keeping them separate (distinct defining cores above), with heavy product-level bundling (Carta sells four of them). No merge or restructure is proposed.

---

## Uncertainties

1. **Shareworks / enterprise pole not directly researched** — site unreachable (2 timeouts). The public-company variant is inferred from Ledgy's Public Company Admin Guide + the directory's own structure; Shareworks-specific behavior is unknown and unclaimed.
2. **Carta & Eqvista feature depth** rests on Tier-2 pages; operational details (e.g., exact transaction types in Carta) were not directly observed. Cross-product claims treat them as coarser confirmations.
3. **Waterfall modeling depth** — explicitly named by Eqvista ("waterfall & funding round modeling") and Ledgy ("exit distributions"); Carta's "scenario modeling" page focuses on fundraising impact; Pulley's modeler covers rounds/dilution with waterfalls not directly confirmed in the fetched pages. Treated as common-but-varying.
4. **Legal weight of the record** — some products register as transfer agents (Carta, Eqvista) suggesting the record can approach official register status in some jurisdictions; the exact legal standing of a software record per jurisdiction was **not** researched and is deliberately not asserted.
5. **Precise rules** (exercise windows after termination, withholding defaults, pool sizing norms) were intentionally not pinned; they vary by product/plan and none were directly evidenced across the sample.

---

## Final Synthesis

Cap Table Management is the **company-side system of record for corporate equity ownership**. Its world model: an issuing company holds a registry of **stakeholders** (identified holders), the **securities** it has created (shares in classes; awards such as options/RSUs; convertible instruments), and the **holdings** binding holders to securities under terms — from which **ownership** (per class, outstanding, fully diluted) is computed, and which is **maintained over time** through typed, dated, auditable equity events.

Around that core, mature products converge on: share classes with rights; a transaction machinery covering issuance → transfer → exercise → conversion → cancellation → split → distribution; an equity plan/pool with vesting; financing rounds as composite events; recorded valuations; compliance/expense/tax outputs; scenario modeling of future rounds and exits; stakeholder portals; document generation with e-signature; confidentiality with role-scoped and anonymized sharing; and migration as a first-class workflow.

Products diverge along a packaging axis (focused startup tooling vs private-capital suite vs valuation-led vs private-to-public equity platform), a geography axis (US forms vs EU/UK schemes), a stage axis (formation → IPO), and an instrument axis (plain shares → options/convertibles → profit interests → tokens).

The defining core is deliberately instrument- and market-agnostic: a two-founder common-shares company, a UK EMI plan, a token cap table, and a four-class venture-backed stack are all the same application type.
