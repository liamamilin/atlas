# Research Notes — Nonprofit Fund Accounting

Research date: 2026-09-08

## Research Goal

Establish what a Nonprofit Fund Accounting application actually is as an Application Type: what records it keeps, how "funds" structure the books, how donor restrictions are carried through accounting, what outputs it produces and for whom, and where its boundaries lie against neighboring Types (General Ledger System, Accounting Software, Donor Management System, Nonprofit Grant Management, Grantmaking Platform, Fund Administration / Investment Fund Accounting, Public Financial Management).

This pass is also responsible for three prior-pass flags:

1. **general-ledger-system pass (joint review recommended)**: "nonprofit-fund-accounting (§25, unprocessed) is a probable GL variant (funds as balancing dimensions + encumbrance) — joint review recommended when that leaf is processed." → Must be discharged or confirmed from this side.
2. **fund-administration-platform pass**: "nonprofit-fund-accounting (§25) is a terminology false friend only (restricted-fund ledgers, no pooled investor capital/NAV)." → Confirm from this side.
3. **donor-management-system pass**: "Relationship/gift-intent records vs books. The bridge is a handoff (ledger codes, lump-sum reports, accounting exports)." → Confirm from the accounting side.

## Initial Boundary (hypothesis before research)

- Core use: the official books of a nonprofit organization, structured around funds (restricted / purpose-bound pools of resources) rather than a single profit-measuring bottom line.
- Users: nonprofit bookkeepers, finance directors, treasurers (often volunteer), executives, auditors, boards.
- Nearest neighbors: General Ledger System (engine), Accounting Software (SMB money capture), Donor Management System (gift intent), Nonprofit Grant Management (grant lifecycle), Fund Administration (false friend on "fund accounting").
- Unknowns: whether fund self-balancing is definitional or one implementation; how deep restriction machinery goes in real products; whether government (GASB) fund accounting is the same Type or an adjacent one.

## Research Questions

1. What is a "fund" in the accounting sense inside these products? Is it a self-balancing set of accounts, a dimension, a record?
2. How do products represent donor restrictions (net asset classes) and the release of restrictions?
3. What money-capture machinery exists (cash receipts/disbursements, AP/AR, bank reconciliation, payroll)?
4. What budgeting machinery exists (budget by fund/grant, encumbrance, budget-vs-actual)?
5. What reports are the deliverables (statements, functional expenses, Form 990, grant reports)?
6. How do these systems connect to fundraising/donor systems (the intent→money handoff)?
7. What controls exist (audit trail, period close, role permissions, close of books)?
8. Where is the line vs commercial accounting software, per the vendors' own definitions?
9. What organizational range does the Type serve (small volunteer treasurers → enterprise; nonprofits vs associations vs municipalities vs schools)?

## Representative Products

| Product | Vendor | Tier / posture | Why selected |
|---|---|---|---|
| MIP Accounting (formerly MIP Fund Accounting) | Momentive Software (formerly Community Brands) | Mid-market specialist; nonprofits, associations, municipalities; 40+ years heritage | The specialist incumbent; explicit fund-accounting positioning; FAQ gives a vendor-stated definition of the Type |
| Blackbaud Financial Edge NXT | Blackbaud | Enterprise; large nonprofits, higher ed, healthcare, K-12 | Largest nonprofit-vendor finance arm; segmented CoA + subfund structure; publishes a fund-vs-commercial-accounting FAQ |
| FastFund Accounting | Araize | Small/mid cloud SaaS; budget-priced modular | Deepest publicly documented feature detail; states fund self-balancing machinery explicitly |
| Denali Fund | Cougar Mountain Software | On-premise heritage; small nonprofits and municipalities/townships | On-prem/modular pole within the same vendor family as a for-profit product (Denali Business), giving a within-vendor contrast |

Rejected as samples this pass:
- **Sage Intacct** (intended dimensional-GL pole) — sageintacct.com unreachable (403 ×2). Not sampled.
- **Aplos** (intended SMB cloud pole) — aplos.com and support subdomain unreachable (403 / transport errors ×2). Not sampled.
- **MoneyMinder** — mymoneyminder.com now serves a personal expense-tracker product; the nonprofit treasury software could not be verified at the fetched surface. Dropped as a product mismatch rather than risk wrong identity.

## Sources

All accessed 2026-09-08. Official vendor surfaces only (product pages, solutions pages, vendor FAQ sections). Vendor help-center / documentation portals were not reachable this pass (Aplos support transport errors; Sage Intacct 403; deeper Blackbaud NXT docs not fetched), so observations are drawn from the reachable official layer.

- MIP Accounting product page — https://momentivesoftware.com/products/mip-accounting/
- MIP Accounting solutions/FAQ page — https://momentivesoftware.com/solutions/accounting-software/
- Momentive Software corporate site (product taxonomy; MIP positioning) — https://momentivesoftware.com/
- Blackbaud Financial Edge NXT product page (incl. FAQ on segmented CoA, subfund accounting, fund vs commercial accounting) — https://www.blackbaud.com/products/blackbaud-financial-edge-nxt
- Blackbaud Fund Accounting solutions page (restricted revenue, endowment accounting) — https://www.blackbaud.com/solutions/financial-management/fund-accounting
- FastFund Accounting product page (GL standard features; FAQs) — https://araize.com/fastfund-nonprofit-fund-accounting/
- FastFund Nonprofit Software overview page (comparison table; modules) — https://araize.com/
- Denali Fund product page — https://www.cougarmtn.com/denali-fund/
- Cougar Mountain corporate site (Denali Fund vs Denali Business taxonomy) — https://cougarmtn.com/

## Product Observations

### MIP Accounting (Momentive Software)

Key observations (evidence layer A unless noted):

- Positioning: "Fund accounting for nonprofits and associations"; "Close your books faster with accounting built for nonprofit fund structures"; "Stay audit-ready with compliance tools designed specifically for nonprofits and municipalities." Serves nonprofits, associations, and government agencies/municipalities ("Its fund accounting structure, audit controls, and compliance reporting capabilities meet government accounting standards").
- Defining contrast to generic accounting, vendor-stated (FAQ): "MIP Accounting is built specifically for nonprofit and governmental fund accounting. Unlike general-purpose accounting tools, MIP handles fund-based chart of accounts structures, grant management, functional expense reporting, and the compliance requirements unique to nonprofits—without requiring extensive customization."
- Canonical definition of the Type, vendor-stated (FAQ): "Nonprofit accounting software is centered on fund accounting, a specialized system that prioritizes accountability and stewardship over simple profitability. Unlike commercial tools like QuickBooks that track a single 'bottom line,' nonprofit-specific platforms treat each fund as an independent accounting entity with its own balance sheet and income statement." (A; consistent with Blackbaud FAQ → B-level cross-product commonality)
- "Track every dollar by fund, grant, program, or project without workarounds." Multi-fund and multi-entity structures with consolidated reporting.
- Reporting deliverables: "statement of functional expenses, budget-versus-actual by fund, and grant-specific reports," with "hundreds of templates."
- Budgeting: "plan and track budgets by fund, program, and grant in the same system where the actuals live. Compare budget to actual in real time"; FAQ adds "budget tolerance alerts."
- Compliance framing: "From FASB to GASB and GAAP regulations"; FAQ: platforms "automate FASB net asset classifications," and provide "grant-specific tracking that monitors indirect costs and unique reporting periods."
- Encumbrance named as a key feature class (FAQ): "encumbrance accounting allow[s] organizations to reserve funds for future commitments to prevent overspending."
- Controls: "approvals, allocations, and recurring entries... Audit trails are built in, so every action is tracked"; "role-based access and read-only executive view licenses for auditors."
- Money capture: payroll providers, Bill.com, Ramp integrations; AP via Bill.com class tools; nonprofit payroll module; HR module; school accounting variant.
- Donor/membership handoff (FAQ): "donor contributions flow instantly into the general ledger" from fundraising platforms (GiveSmart); "integrations with AMS platforms like YourMembership, NetForum, or Personify ensure member data and dues are synchronized." Documents the fundraising→books bridge from the accounting side.
- Customer evidence (vendor-published quotes): CFO of a community action agency — "we're able to adapt to each funding stream's unique conditions... funding sources typically have diverse requirements, and even interpret regulations differently, sometimes within the same federal department." Executive director — "multiple programs... foundations... grants... individual donors... report even in different fiscal years versus calendar year... board reports."
- Heritage claim: "Built with 40+ years' experience serving purpose-driven organizations."

### Blackbaud Financial Edge NXT

Key observations (A):

- Positioning: "Fund accounting for nonprofits." Value pillars: Compliance, Stewardship, Internal Controls, Transparent Reporting, Automated Processes.
- Compliance: "track restricted funds and provide detailed reporting to your funders"; "Track grants, projects, and endowments in granular detail with flexible subfund functionality"; "Create a single source of truth for all of your revenue sources."
- Subfund accounting (FAQ): "Subfund accounting is a hierarchical structure within your general ledger that allows you to carry the revenue, expense, and equity related to a restricted fund. Valuable for endowments, grants, contracts, and agency funds... In addition to improving the clarity of your restricted revenue accounting, subfund records also help track programs and special projects funded by that restricted revenue. Using a record for each subfund allows you to track qualitative data, such as spending guidelines, key dates, and contact information, along with the detailed financial data."
- Segmented chart of accounts (FAQ): "Financial Edge NXT uses a segmented chart of accounts... associates certain parts of your account string together and prevents associations of those that should not be linked."
- Fund vs commercial accounting (FAQ): "Nonprofits emphasize accountability, fund segregation, and mission-driven financial transparency, whereas for-profits focus on unified systems and profitability for owners and shareholders. Nonprofit organizations typically use a fund accounting system, which segregates financial resources into separate funds, each dedicated to specific purposes or programs. This separation allows nonprofits to track the financial performance and accountability of each fund independently. By contrast, for-profit businesses typically use a single accounting system to record all financial transactions, regardless of their purpose."
- Internal controls: "Attach supporting documentation to transactions to create a strong audit trail"; "Role-based access... enforce separation of duties"; "AI-powered anomaly detection and spending controls to prevent... over spending and restrict fund use."
- Transparent reporting: "real-time financial reports using built-in templates designed for nonprofits"; "Maintain a clean, standardized chart of accounts"; view-only licenses for ad hoc report consumers.
- Money capture: invoice capture automation, payments, bank and credit card reconciliation, budget checking on expense submission.
- Fund accounting solutions page: "Accounting software built for commercial businesses doesn't have the sub-fund capabilities nonprofits need to manage donor restrictions. Sub-fund accounting gives you detailed reporting and program-based budgeting to support your internal controls and donor-restricted spending rules." Revenue streams organized as: Contribution Revenue, Government Grants and Contracts, Non-Government Grants, Program Fees, Endowments and Scholarships, Tuition.
- Endowment depth: "For endowed funds, track the original gift amount separate from appreciation to ensure unintended overspending" (corpus vs spendable); "Share reports automatically with beneficiaries and donors on spendable balances."
- Grant machinery: "Track revenue by each restricted grant or contract"; "Budget by grant... even across fiscal years"; "Retain equity to easily manage multi-year grants."
- Handoff to fundraising: repeated "Connect your fund accounting system and fundraising CRM to easily manage donor restrictions" (Raiser's Edge NXT integration).
- Serves nonprofits, higher ed, healthcare, arts & culture, K-12.

### FastFund Accounting (Araize)

Key observations (A) — the most structurally explicit of the sample:

- "True Fund Accounting and Functional Accounting" as the headline of the GL feature set.
- Six-segment chart of accounts: "six account segments representing funds, programs, funding sources, departments, sites and accounts" (table-driven, user-defined).
- Automatic fund balancing: "FastFund Accounting is a true fund accounting application with the ability to set up multiple funds. Each fund is treated as its own entity within your organization, with separate trial balances and financial statements. All inter-fund transactions automatically create a fund balancing entry to keep your funds in balance. You can print a detailed audit trail of all fund balancing entries and source entries."
- Year-end close by fund: "Whether you have one fund or a thousand funds, each fund's excess or deficiency is closed out to its own net asset fund balance."
- FASB statements: "Statement of Activities and Changes to Net Assets, Statement of Financial Position (Balance Sheet), Statement of Activities (Revenue and Expense), Functional Expenses and Statement of Cash Flow," with comparative periods and cross-fiscal-year runs.
- IRS Form 990: "Generate all the data you need to complete IRS Form 990 N, 990-EZ and 990."
- Functional expense: "track expenses by both natural classification, such as salaries, rent, and supplies, and functional classification, including programs, administration, and fundraising"; benefits listed include "Analyze program efficiency and overhead ratios," "Meet grant and board reporting requirements," "Eliminate manual spreadsheet allocations."
- Money capture in the GL core: cash receipts ("grouped for deposits and posted in total to the cash account... Multiple cash accounts"), cash disbursements, recurring entries, reversing entries ("Internal controls and audit trails are built to track and link reversing entries").
- Budgets: "Create budgets for each of your grants, departments, programs and funds with automatic roll-up for funds and organizational totals"; "multiple budgets for a fiscal year to track major budget revisions"; "Lock-in budget amounts for strict internal controls"; budget comparison reports.
- Projects: "Projects can be grants, short term activities, sites or other operations within your organization that are independent of the chart of accounts."
- Controls: "Soft close the books to prevent entries by non-administrative personnel. Permanently close the books to prevent all users from posting transactions. Strict internal controls prevent the editing or deleting of linked or cleared transactions." "13th-Month Year-End Entries: Separate year end audit adjustments from normal entries to generate pre and post audit reports." Full audit trail "of all data entered, modified or deleted by each user."
- Bank integration (Plaid) and bank reconciliation with revert capability.
- Modules/add-ons: AP, AR (accrual), direct and indirect cost allocations ("allocating expenses and revenue" across cost centers, postable as journal entries), purchase orders, fundraising bundle, payroll with "allocations by fund, grant, or program."
- Restriction terminology (FAQ): "FastFund helps nonprofits manage restricted, temporarily restricted, and unrestricted funds while providing clear reporting and financial visibility."
- Customer evidence (vendor-published): "FastFund facilitates the tracking of our restricted funds; we do not need to do all the double entries that our old software package required." — a university association. "It meets all our needs for accounting for multiple government grants."
- Vendor comparison table (marketing but structurally informative; treat as B/C): rows "True Fund Accounting," "Chart of Accounts Segments" (FastFund 6, QuickBooks 1, Financial Edge 6, Aplos 2), "Restricted & Unrestricted Funds," "FASB-Compliant Reports," "Budgeting by Funds & Grants," "Board & Audit-Ready Financial Statements," "Labor Allocation by Fund, Grant or Program" — with QuickBooks marked absent across the nonprofit rows.

### Denali Fund (Cougar Mountain Software)

Key observations (A):

- Positioning: "Denali Fund is designed as a bespoke solution for non-profit organizations that are trying to stay on top of their fund accounting, such as federal grants, private grants and corporate sponsorships."
- "True Fund: Have all your funds tracked and accounted for at all times, with no gaps."
- Encumbrances: "Keep track of all encumberances in your non-profit, so that none of your funds go unaccounted for."
- "Achieve complete reliability and transparency through comprehensive GAAP and FASB compliance."
- Modular architecture: "Payroll, General Ledger, Bank Reconciliation, Accounts Receivable, and Accounts Payable can all work independently as stand-alone modules"; purchase orders, order entry, job cost as further modules.
- On-premise heritage with a cloud option; "unbreakable audit trail" as corporate positioning.
- Within-vendor contrast: the same vendor sells **Denali Business** ("comprehensive accounting solution made specifically for small to mid-sized businesses") as a separate product from **Denali Fund** — the market itself splits commercial accounting from fund accounting at the product level. Serves nonprofits, townships, government accounting, small business, accountants as industries.

## Cross-product Comparison

| Structure / capability | MIP | Financial Edge NXT | FastFund | Denali Fund | Evidence |
|---|---|---|---|---|---|
| Books organized around funds | ✔ "fund-based chart of accounts structures" | ✔ segmented CoA + subfunds | ✔ funds as CoA segment; "true fund accounting" | ✔ "True Fund" | B (4/4) |
| Fund as independently reportable accounting entity | ✔ FAQ: "each fund as an independent accounting entity with its own balance sheet and income statement" | ✔ FAQ: "track the financial performance and accountability of each fund independently" | ✔ "separate trial balances and financial statements"; auto fund-balancing entries | ✔ "funds tracked and accounted for at all times" | B (3/4 explicit, 4th supportive) |
| Donor-restriction / net asset accounting | ✔ "automate FASB net asset classifications" | ✔ "manage donor restrictions"; restricted funds | ✔ "restricted, temporarily restricted, and unrestricted funds" | ◐ via GAAP/FASB compliance framing (restriction machinery not itemized on reachable page) | B (3/4 explicit) |
| Nonprofit financial statements (Financial Position / Activities / Functional Expenses) | ✔ statement of functional expenses + templates | ✔ "built-in templates designed for nonprofits" | ✔ full named statement set | ◐ GAAP/FASB compliance | B (3/4 explicit) |
| Budget by fund/grant + budget-vs-actual | ✔ "budget-versus-actual by fund"; tolerance alerts | ✔ program-based budgeting; budget checking | ✔ budgets per grant/program/fund, roll-up, comparison | ◐ (budget module exists; not itemized) | B (3/4 explicit) |
| Encumbrance / commitment reservation | ✔ FAQ names encumbrance accounting | ◐ spending controls / budget checking | — (not observed on reachable page) | ✔ Encumbrances feature | A (2 explicit) → common, not definitional |
| Grant/project tracking in the books | ✔ | ✔ grants/contracts/endowments/subfunds | ✔ projects + grant budgets | ✔ federal/private grants named | B (4/4) |
| Functional expense classification | ✔ | ◐ implied by templates/compliance framing | ✔ program services / management & general / fundraising | — | B (2 explicit) → common |
| Audit trail + close-of-books controls | ✔ "every action is tracked"; audit-ready | ✔ attach documentation; role-based access; separation of duties | ✔ soft/permanent close; 13th month; linked-transaction protection | ✔ "unbreakable audit trail" | B (4/4) |
| Cash receipts/disbursements, bank reconciliation | ✔ (via financial management + integrations) | ✔ bank/credit card reconciliation | ✔ in GL core | ✔ Bank Reconciliation module | B (4/4) |
| AP / AR / payroll | ✔ modules + Bill.com/Ramp/payroll integrations | ✔ AP automation, payments; payroll via marketplace | ✔ AP/AR/payroll add-ons with fund allocation | ✔ standalone-capable modules | B (4/4) → common, packaging varies |
| Fundraising/donor system handoff | ✔ contributions flow into GL (GiveSmart FAQ) | ✔ connect fundraising CRM for donor restrictions | ✔ integrated fundraising module (optional) | — | B (3/4) |
| Government/municipal (GASB) posture | ✔ municipalities, government standards | ◐ schools/higher ed | ◐ government grants customers | ✔ townships, government accounting | B (2+ explicit) |
| Deployment heritage | cloud (40+ yr heritage) | cloud (suite) | cloud SaaS modular | on-prem + cloud | variant |

## Abstraction Hierarchy

### Level 0 — Defining Invariant (jointly held; minimal)

Three jointly-held structures. Remove any one and the product stops being recognizable as nonprofit fund accounting:

1. **Fund-structured double-entry books.** The organization's ledger is partitioned into funds — pools of resources bound to a purpose or restriction — each carried through the books as a separately reportable accounting entity (its own balances/trial balance/statements in classic implementations; realized through fund segments or subfund records in others), with the organization's books always balancing as a whole. Remove → a conventional commercial ledger (single pool, profit orientation).
2. **Donor-restriction-aware accounting.** The books distinguish resources available for general use from donor-restricted resources (net asset classes), and carry restriction through the ledger — recording restricted revenue, spending it per its rules, releasing it when earned/satisfied, and reporting restricted vs unrestricted net assets. Remove → project/segment accounting with no restriction semantics (an internal ledger; the vendors themselves define the Type by this capability).
3. **Stewardship-reporting orientation.** The system's outputs are accountability artifacts for non-owner stakeholders — boards, funders, donors, auditors, regulators: fund-level statements of financial position and activities, functional expense classification, budget-vs-actual per fund, and audit-ready trails — not owner profit measurement. Remove → an internal bookkeeping engine with fund fields but no accountability deliverable.

Jointly-held is load-bearing:
- 1 without 2+3 → segmented commercial GL / project accounting.
- 2 without 1 → restriction tracking without books (donor CRM / spreadsheet territory).
- 3 without 1+2 → a reporting layer over nothing.
- 1+2 without 3 → fund-tagged internal ledger; the market's own definitional statements (MIP FAQ, Blackbaud FAQ) center accountability as the purpose.

### Level 1 — Common Mature Structure

Very common across the sample, but not what makes the Type:

- Multi-segment chart of accounts (fund / program / grant / department / location variations)
- Cash receipts and disbursements; multiple bank accounts; bank reconciliation
- Accounts payable, accounts receivable (accrual), recurring and reversing journal entries
- Budgeting by fund/program/grant with roll-ups and budget-vs-actual reporting
- Grant / project / contract tracking attached to the ledger
- Functional expense classification (program services / management & general / fundraising)
- Standard nonprofit statement templates (Financial Position, Activities, Functional Expenses, Cash Flows) and Form 990 support (US)
- Audit trail of every entry/edit/delete; period and year-end close; soft/permanent close; audit-adjustment separation
- Role-based permissions, approval workflows, read-only auditor access
- Multi-entity and multi-fund consolidated reporting
- Integrations from fundraising/donor systems and membership systems into the ledger (the intent→money handoff)
- Optional modules: payroll with labor allocation by fund/program, purchase orders, cost allocation engines, HR

### Level 2 — Variant / Optional Structure

- Deployment: cloud SaaS vs on-premises heritage; modular (buy the GL alone) vs suite
- Regulatory frame: FASB (US nonprofits) vs GASB (municipalities/government) — MIP and Denali explicitly serve both; the same fund structure carries over
- Organizational scale: volunteer treasurer simplicity (small church/club) through enterprise multi-entity controls
- Endowment accounting depth (corpus vs spendable/appreciation separation; spendable-balance reporting)
- Encumbrance/commitment accounting depth
- Cash-basis vs accrual-basis operation
- Sector funding-source mixes: donations, grants, dues, program fees, tuition, events
- Country/regulatory surface (US Form 990 is US-specific; other jurisdictions have their own filings — not directly researched this pass)

### Level 3 — Vendor-specific (research notes only)

- MIP: FASB/GASB compliance suite; Momentive ecosystem integrations (GiveSmart, NimbleAMS, YourMembership, NetForumAMS); HR/payroll/school modules; budget tolerance alerts; read-only executive licenses; "40+ years" heritage claim.
- Financial Edge NXT: "subfund" records carrying qualitative data (spending guidelines, key dates, contacts); segmented account strings with link-prevention; Payment Assistant; SKY Developer platform; Power Automate; AI reconciliation/anomaly claims.
- FastFund: six named segments (funds, programs, funding sources, departments, sites, accounts); automatic fund-balancing entries with printable audit trail; 13th-month year-end entries; Plaid bank integration; duplicate search & merge; project codes independent of the CoA; published per-module pricing.
- Denali: module independence (GL/BR/AR/AP usable standalone); on-prem + cloud licensing; township/government industry focus; within-vendor Denali Business split.

## Rejected Findings (considered and NOT promoted)

- **"Fund accounting = encumbrance accounting"** — only 2/4 sampled products evidence encumbrance machinery explicitly; it is commitment-budgeting depth, not definitional. Kept at L1/L2. (Also already characterized as in-GL machinery by the general-ledger-system pass.)
- **"Fund accounting = grant management"** — grants are one funding source; all four track them, but the defining structure is funds + restrictions, of which grants are an instance. Grant *lifecycle* management (applications, reports to funders as workflow) belongs to Nonprofit Grant Management.
- **"Fund accounting includes payroll/HR"** — universal as optional modules/integrations, absent from every definitional statement. L1 optional module.
- **"Funds must be self-balancing sets of accounts"** — strongly evidenced in classic implementations (FastFund's explicit fund-balancing entries; MIP FAQ "independent accounting entity with its own balance sheet"), but modern dimension-based realizations were not directly sampled (Sage Intacct unreachable). Phrased at L0 as "separately reportable accounting entity (realized as self-balancing ledgers, subfund records, or fund segments)" to avoid overfitting to one implementation.
- **Aplos's exact two-segment structure** — asserted only in a competitor's marketing table; not verified from Aplos itself. Not used.

## Boundary Findings

1. **vs General Ledger System (§08) — JOINT REVIEW DISCHARGED.** The GL pass flagged this leaf as "a probable GL variant (funds as balancing dimensions + encumbrance)." This pass's finding is more precise: the shared part is the ledger engine (CoA, balanced journal posting, periods, close), but the defining overlay here is stronger than dimensions-plus-encumbrance — funds are carried as separately reportable accounting entities, restriction is an accounting semantic (net asset classes, releases), and the deliverable orientation is stewardship reporting. None of these is definitional in the GL leaf's own sampled population (Dynamics, Workday, Oracle, SunSystems); conversely, the GL leaf's definitional core is fully contained inside this Type. Verdict: **keep-both as engine-sharing siblings, not alias, not strict subset** — the direction of specialization is one-way (adding fund/restriction/stewardship semantics to a GL product yields this Type; removing them from this Type yields a GL), and the market realizes the specialization as its own named product category (both MIP and Blackbaud publish FAQs drawing the line; Cougar Mountain splits Denali Fund from Denali Business). Cross-reference both documents; no directory change from this side.
2. **vs Accounting Software (§08).** Confirmed adjacent, sharing money-capture furniture (AP/AR/bank rec/payroll). The vendors' own definitional statements draw the line on structure and purpose: single bottom line / profit for owners vs fund segregation / accountability to non-owners. A commercial tool can be configured toward nonprofit bookkeeping (the comparison tables mark QuickBooks "limited"), but then the fund/restriction machinery is the workaround being sold against. Held.
3. **vs Fund Administration Platform / Investment Fund Accounting (§08).** False friend confirmed from this side: "fund" here is a partition of one organization's own books (restricted/purpose-bound pools), not a pooled investment vehicle. No investor register, no capital accounts, no NAV/dealing machinery anywhere in the sampled products. The fund-administration pass note stands.
4. **vs Donor Management System (§25).** Held from the accounting side: the DMS records gift intent and constituency; the books record money by fund. The bridge is a handoff — MIP FAQ documents contributions flowing from fundraising platforms into the GL; Financial Edge documents connecting the fundraising CRM to "manage donor restrictions"; FastFund sells fundraising as an optional adjacent module. Ledger codes/exports are the seam per the donor pass; this pass confirms the same seam from the other direction.
5. **vs Nonprofit Grant Management / Grantmaking Platform (§25).** Grant lifecycle (applications, awards, funder compliance workflow, grants out to grantees) vs grant-as-funding-source inside the books (restricted revenue, grant budgets, indirect costs, financial reporting to the funder). The grantmaking pass's note ("the money-pool ledger") matches. Held.
6. **vs Public Budgeting Platform / Public Financial Management System (§24).** Government fund accounting (GASB) is the closest external discipline — same fund structure, different regulatory frame and users (public agencies). MIP and Denali serve municipalities explicitly, showing the machinery is shared. The nonprofit leaf is FASB/nonprofit-oriented; no merge, but the adjacency is recorded. If a government-finance pass later claims the same fund-ledger core, the two leaves may need a shared-family note.
7. **vs Nonprofit Management Platform / Nonprofit CRM (§25).** Whole-organization platforms bundle fundraising, membership, events, sometimes accounting as a purchasable module (precedent: congregation-membership pass observed fund accounting as a separate ChMS module). This leaf is the finance/ledger slice regardless of packaging. Held.
8. **Removal tests (summarized).** Remove funds → commercial ledger. Remove restrictions → project/segment accounting. Remove stewardship outputs → internal ledger. Add pooled investor capital + NAV + register → investment fund accounting (different Type). Add grantee-side lifecycle → grant management. Remove books but keep gift intent → donor management.

## Historical / Market-Sample Check (per §24)

- The fund-accounting discipline predates software: paper-era nonprofit and governmental bookkeeping — a ledger per fund, receipts/disbursements journals, restriction notes in the minutes, an annual report to the board or town meeting — satisfies all three defining legs at analog level (conceptual inference, C; no primary historical source fetched this pass).
- The sampled products' own heritage claims support the Type's pre-cloud existence: MIP "40+ years," Araize "Serving Nonprofits for 30+ Years," Denali as on-premises software with a modular 1990s-style architecture. None of the defining legs depends on cloud, AI, or modern integration.
- Government/municipal fund accounting (GASB-era) fits the same fund structure; the Type as defined does not overfit to modern US nonprofit cloud products.
- Era machinery (AI reconciliation, natural-language queries, Plaid-class bank feeds, ecosystem marketplaces) appears only at L1/L2 and is named nowhere in the definition.

## Uncertainties

1. **Dimensional-GL realization unverified.** Sage Intacct and Aplos (the intended poles for funds-as-dimensions) were unreachable. The L0 wording deliberately allows both realizations, but the claim that "modern products realize fund separability through segments/dimensions" rests on the segmented-CoA evidence in Financial Edge NXT (direct) plus FastFund's competitor table (indirect). Reduce assertion strength accordingly in the final document.
2. **Net-asset terminology varies by era of documentation**: FastFund FAQ uses "restricted, temporarily restricted, and unrestricted"; MIP FAQ says "FASB net asset classifications" without naming classes. Current FASB terminology ("with/without donor restrictions") was not observed verbatim in any fetched source — the final document uses generic phrasing.
3. **Whether every fund-accounting product enforces restriction at transaction time** (vs reporting it after the fact) could not be verified from the reachable surfaces; Financial Edge's "spending controls to... restrict fund use" is direct but single-product. Final document says controls "commonly include" budget/spend checks, marked as common.
4. **Non-US regulatory surface** (SORP in UK etc.) not researched; Form 990 statements are kept US-scoped in the final document.
5. **Historical check is conceptual** (no primary archival source); recorded at C-level inference.

## Final Synthesis

Nonprofit Fund Accounting is the nonprofit organization's official books, built on a double-entry ledger whose organizing partition is the fund rather than the profit center: every dollar sits in a fund (general operating, a donor-restricted gift, a grant, an endowment), funds are carried as separately reportable accounting entities, the books distinguish donor-restricted from unrestricted net assets and carry restriction through recording, spending, and release, and the system's deliverables are accountability artifacts — fund-level statements, functional expenses, budget-vs-actual per fund, audit-ready trails — produced for boards, funders, auditors, and regulators rather than for owners. Money-capture furniture (receipts/disbursements, AP/AR, bank reconciliation, payroll) and grant/project tracking ride on this structure as standard capabilities; deployment, regulatory frame (FASB/GASB), and scale are variants. The Type shares its engine with the General Ledger System and its money-capture surface with Accounting Software, but is defined — by the vendors' own statements and the market's product split — by fund segregation, restriction accounting, and stewardship reporting.
