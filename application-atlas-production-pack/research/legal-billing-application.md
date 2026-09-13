# Research Notes — Legal Billing Application

## Research Goal

Understand what a Legal Billing Application actually is from real products: what objects exist inside it, how a law firm's work becomes money, what rules shape the process, and where its boundaries sit against Law Practice Management, Legal Spend Management, generic Invoicing, and Time Tracking.

## Initial Boundary

- Hypothesis: this is the **firm-side money loop** of legal practice — time capture → bill generation → payment/trust → firm financials — standing alone from the matter workspace.
- Nearest neighbors: Law Practice Management System (matter workspace fused with the money loop), Legal Spend Management (buyer-side control over the same bills), Invoicing Application (generic invoice document), Time Tracking Application (capture without the money loop), Professional Services Automation (the same loop shape, non-legal).
- Two carried joint-review flags must be discharged:
  1. **law-practice-management-system** (§11, processed 2026-09-07): standalone legal billing/timekeeping products (Timeslips-class lineage) center the time-and-billing loop without the matter workspace/client file; remove the matter container from LPM → legal billing application; add the matter/firm workspace to a billing tool → LPM. This pass should ratify.
  2. **legal-spend-management** (§11, processed 2026-09-08): mirror-image seam — firm-side billing generates the bills (time capture → billing → firm financials, client-anchored); LSM is the buyer's control surface over them; the invoice is the shared artifact. This pass should confirm from its own sample.

## Research Questions

1. What is the unit of record — what does a bill get built from, and what is it attached to?
2. How does work become a bill (capture → draft/pre-bill → review → final → delivery)?
3. What fee arrangements and rate structures exist, and who configures them?
4. How are payments, retainers, and client trust funds handled?
5. What does the firm see as its money position (AR, WIP, realization, collections)?
6. How do client billing guidelines / e-billing formats (LEDES/UTBMS) enter the firm side?
7. Where does the matter workspace end and the billing loop begin (the LPM seam)?
8. What roles use the system (timekeepers vs billing staff vs partners/admin)?

## Representative Products

Selected for market representation, documentation quality, and spread across product philosophy and firm size:

| Product | Pole | Evidence tier reached |
|---|---|---|
| Bill4Time | cloud standalone legal time & billing, solo/SMB | Tier 2 (root + billing feature page, rich FAQ) |
| TimeSolv | cloud time & billing, KB-documented | Tier 1 (KB index + "Creating Invoices" article) + Tier 2 |
| Tabs3 (Billing) | long-lived billing-first suite (desktop heritage, now cloud), SMB–mid | Tier 2 (billing feature page + FAQ) |
| Aderant Expert | enterprise law-firm financial management (Am Law 200) | Tier 2 (root + Work-to-Cash ecosystem pages) |

Rejected/abandoned: CosmoLex (403 ×2), Sage Timeslips (403) — the desktop-heritage pole is instead covered by Tabs3 (billing-first lineage since the 1970s–80s era, on-premises option retained).

## Sources

- Bill4Time — https://www.bill4time.com/ , https://www.bill4time.com/billing-and-invoicing/ (fetched 2026-09-10)
- TimeSolv — https://www.timesolv.com/ , https://help.timesolv.com/ , https://help.timesolv.com/creating-invoices (fetched 2026-09-10)
- Tabs3 — https://www.tabs3.com/ , https://www.tabs3.com/tabs3-cloud/legal-billing-software/ (fetched 2026-09-10)
- Aderant — https://www.aderant.com/ (Expert, iTimekeep, Onyx, BillBlast, Virtual Pricing Director nav) (fetched 2026-09-10)
- Counterparty research: research/legal-spend-management.md §Boundary Findings; research/law-practice-management-system.md §Boundary Findings; STATUS.md entries for legal-matter-management, litigation-management-platform, professional-services-automation.

## Product Observations

### Bill4Time (evidence layer A unless noted)

- Self-definition: "legal time and billing software"; FAQ explicitly contrasts itself with "general billing and accounting platforms" and names the legal-specific additions: **matter-based billing, trust accounting, compliance with bar rules**.
- Time capture: one-click timers (start/pause/stop/resume), batch entry via a Time & Expense grid, calendar events/tasks/emails convertible to entries, mobile; entries tied to **client + matter + activity**; custom billing increments (e.g., 0.1 / 0.25 hour); billable vs non-billable; internal administrative time tracked separately; alerts for unbilled time and missed entries ("revenue leakage").
- Rates: "unlimited billing rates" — by user, client, project/matter, activity type, or individual entry; flat-fee projects (single, recurring, or phased); hybrid flat+hourly; contingency named as a billing mode.
- Bill assembly: system compiles entries into **draft invoices**; review, adjust, finalize individually or in batches ("pre-bill review, batch billing"); branded templates; tax and trust-balance summaries on invoices; LEDES invoicing mentioned in a customer quote (B layer for LEDES).
- Payments: native processor (card/eCheck/ACH), "Pay Now" links, payment plans, client portal; overdue tracking and automated reminders; **trust accounting**: separate trust ledgers per client/matter, every deposit/withdrawal tracked, trust funds kept separate from operating accounts, audit trails, IOLTA/ABA compliance framing.
- Reporting: collections, aging invoices, trust balances, productivity, payment history; QuickBooks sync (invoices, payments, client data) — books posture = external books.
- Adjacent modules sold beside billing: case management, calendaring, CRM, document management, task management — i.e., the matter workspace is a **separate pillar**, not the billing loop itself.

### TimeSolv (evidence layer A)

- KB structure is itself a model of the system: **Clients & Matters → Matter Plans → Time (entries, rates, approvals, activity/task codes) → Expense → Invoicing → Payments (incl. Trust) → Reports (firm, matters, performance, realization, accounting)**.
- Clients & Matters: client and matter records with per-matter **Invoice Settings / Billing Arrangement** (e.g., "Expenses only", "Fixed Fee – Time and Expense"); matters can be moved between clients; deletion of clients/matters/professionals restricted (KB FAQ title) — record-integrity posture.
- Time: activity/task codes, rate management, **time approvals** (supervisory step before billing), time entry reports.
- Invoicing (from "Creating Invoices", Tier 1): draft invoices generated per client-matter for **unbilled entries only**; billing categories; date ranges; include time/expense/time-only/expense-only or matter billing arrangement; **split billing** across multiple parties (master/secondary matters); **fixed-fee invoices** via time entry or **billable milestones in a Matter Plan** (auto-complete milestone → generate invoice); **retainer invoices** as a distinct invoice type with templates and online payment through the client portal; **consolidated invoices** across multiple matters of one client; firm view vs client view invoice templates; hold billing per matter or hold individual entries until next invoice / permanently (mark non-billable); void drafts; delivery by PDF download, email, or paid physical mail; invoice translation via Word export.
- Payments & trust: managing trust accounts & trust payments, trust reports, retainer payment links, credits back to client, bounced-check handling, void-payment constraints ("Remove All References" error) — money-state integrity rules.
- Reports: realization reports (billed vs collected), performance, aging; QuickBooks/Xero sync; LawPay integration; REST API.
- Also ships project management, CRM, client portal, document features — again adjacent pillars beside the billing core.

### Tabs3 (evidence layer A)

- Positioning: "legal billing software that gets you paid faster"; the suite splits **Billing / PracticeMaster (practice management) / Financials (GL, AP, Trust Accounting) / Tabs3Pay** as separately named modules — the market itself decomposes billing from the matter workspace (supports the LPM seam).
- Time & fee tracking: built-in timers converting entries to fees "with a single click"; time entry forms support both **"hours worked" and "hours to bill"** (recorded vs billed distinction); mobile entry.
- Flexible billing: rate tables per timekeeper or timekeeper **level** (partner/associate/paralegal), custom rates per client or case; billing methods: **hourly, contingency, flat fee, retainer, progress billing, split-fee billing, electronic task-based billing**; split billing allocates fees/costs among multiple parties.
- Invoicing: print/email individually or in batch as PDF; password-protected statements for sensitive matters; **draft statements and pre-bill review tools** to catch errors before clients see them; payment allocation across multiple matters/invoices when a client pays once; statement designer (custom layout); mail and email delivery.
- Security & control: role-based access to view/enter/edit/delete billing data; **segregated access for ethical walls** on sensitive/conflicting matters.
- Compensation: rules for originating/primary/secondary timekeepers; fee allocation and payment distribution reports (originating-attorney economics).
- Trust: dedicated Trust Accounting module (separate from operating "Client Funds" feature — vendor distinguishes operating-account retainers from IOLTA trust); three-way-style reconciliation language on the family marketing ("automate three-way reconciliations" is TimeSolv's phrasing; Tabs3 documents trust ledgers, deposits, disbursements, reconciliation).
- Task-based e-billing: UTBMS formats per LEDES Oversight Committee, via a separate **Taskbill** license (A layer — direct FAQ).
- FAQ defines the vocabulary: "timekeeper" = anyone whose time is tracked; matter manager screen shows contact info, recent payments, WIP, AR, client funds, trust balance in one view.

### Aderant Expert (evidence layer A at product-ecosystem level; B for internal mechanics)

- Enterprise pole: "the industry's #1 time & billing solution" under Practice Management; the surrounding ecosystem is organized as **Work to Cash**: iTimekeep (time entry & billing compliance; 100k+ MAU claim — marketing, excluded), Onyx (client-guideline/OCG compliance across time, billing & eBilling), BillBlast (eBilling bill delivery), Virtual Pricing Director (pricing/profitability).
- The ecosystem naming confirms the loop: work captured → compliance-checked against client guidelines → billed → delivered electronically → cash collected; pricing/AI as current-era layers.
- Financial management (Expert Sierra): cloud AR, cloud GL, analytics — the firm's books can live inside the platform (embedded-GL pole; contrast Bill4Time/TimeSolv external-books pole).
- Client base: Am Law 200 / Global 100 firms (marketing figures; used only as tier positioning, not asserted as fact).

## Cross-product Comparison

| Structure | Bill4Time | TimeSolv | Tabs3 | Aderant Expert |
|---|---|---|---|---|
| Client + matter as billing anchor | ✓ | ✓ | ✓ | ✓ |
| Timekeeper as the billing person | ✓ | ✓ ("professionals"/timekeepers) | ✓ (defining FAQ term) | ✓ (iTimekeep) |
| Time/expense/flat-fee entry capture | ✓ | ✓ | ✓ | ✓ |
| Rate tables (by timekeeper/level/client/matter) | ✓ | ✓ | ✓ | ✓ |
| Fee arrangements: hourly / flat / contingency / retainer | ✓ | ✓ (contingency, fixed, retainer, split) | ✓ (+ progress, split-fee, task-based) | ✓ (enterprise variants) |
| Draft/pre-bill review before final bill | ✓ | ✓ (drafts, edits, void) | ✓ (draft statements, pre-bill review) | ✓ (OCG compliance layer) |
| Batch invoicing | ✓ | ✓ | ✓ | ✓ (BillBlast delivery) |
| Split billing / allocation among parties | ✓ (split billing projects) | ✓ | ✓ | ✓ |
| Consolidated multi-matter invoices | — (not observed) | ✓ | ✓ (payment allocation) | ✓ |
| Payments / AR tracking | ✓ | ✓ | ✓ | ✓ (cloud AR) |
| Trust / retainer funds | ✓ | ✓ | ✓ (separate module) | (not observed at fetched level) |
| e-billing formats (LEDES/UTBMS) | ✓ (quote-level, B) | — (not observed) | ✓ (Taskbill, A) | ✓ (Onyx/BillBlast ecosystem) |
| Firm money reports (AR, WIP, realization, productivity) | ✓ | ✓ | ✓ | ✓ |
| Books posture | external (QuickBooks) | external (QB/Xero) | embedded (Financials/GL) or external | embedded (GL) |
| Matter workspace as separate pillar/module | ✓ | ✓ | ✓ (PracticeMaster) | ✓ (separate products) |

**Reading:** the client–matter–timekeeper billing structure, entry capture, rate/fee-arrangement machinery, draft→final bill assembly, payment/AR tracking, and firm money reporting are present across the whole sample (B layer). Trust accounting is present in 3/4 fetched at capability level and is treated as standard-not-definitional (jurisdiction-shaped, consistent with the LPM pass's rejection). Embedded vs external books is a variant axis. e-billing format support is common but implementation-gated (Taskbill license; Onyx as separate product) — L1/L2.

## Canonical Model

### L0 — Defining Invariant (minimal)

The firm-side legal money loop, three jointly-held structures:

1. **The client–matter billing structure with timekeepers** — bills are organized around a client and the matter (the legal unit of work), and the people whose work is billed exist in the system as timekeepers with rates. Remove → generic invoicing (no legal work attribution).
2. **Work capture → bill assembly under fee arrangements** — billable time, expenses, and flat fees are captured as entries against client/matter/timekeeper, then assembled into draft bills, reviewed/adjusted, and finalized as invoices under the matter's fee arrangement and rate rules. Remove → a time tracker or a bare invoice template.
3. **The firm money loop** — issued invoices are tracked to payment (AR), client-held funds (retainers/trust where the regime requires) are administered against bills, and the firm's billing money position (WIP, AR, realization/collections) is held inspectable. Remove → a one-off invoice generator with no firm money view.

Jointly-held is load-bearing: (1) alone = client/matter database; (2) without (1) = generic time & billing; (3) without (1)+(2) = AR spreadsheet; (1)+(3) without (2) = billing registry with no capture; (2)+(3) without (1) = generic professional billing.

### L1 — Common mature structure

- Timers, calendar/task/email-to-entry conversion, mobile capture, unbilled-time alerts
- Billing increments and activity/task codes (UTBMS-style work codes)
- Batch invoicing, invoice templates/branding, statement designers
- Client portal with online payment; native payment processing; payment plans; reminders
- Trust accounting with ledgers, three-way reconciliation posture, audit trails
- Time approvals (supervisory review of entries before billing)
- Firm reports: AR aging, WIP, realization, productivity, profitability, compensation/originating-attorney allocation
- Role-based access and ethical-wall segregation
- e-billing format support (LEDES/UTBMS task-based billing)

### L2 — Variant / optional

- Books posture: embedded GL/AP (Tabs3 Financials, Aderant) vs external books sync (QuickBooks/Xero)
- Enterprise depth: OCG/client-guideline compliance automation, e-billing delivery platforms, pricing/profitability tools (Aderant Work-to-Cash)
- Adjacent pillars bundled by the same vendor: case/matter management, CRM, document management, calendaring, project management
- Matter plans with billable milestones (TimeSolv); progress billing; split-fee arrangements
- Deployment: cloud vs on-premises (Tabs3 retains on-prem); desktop-heritage lineage
- Multi-currency, interest/late fees, invoice translation, physical-mail delivery services

### L3 — Vendor-specific (research notes only)

- Bill4Time Payments branding, "70% faster" marketing claims, per-user pricing
- TimeSolv AutoMail ($1.49/piece), TimeSync desktop tool, Matter Plans naming, TimeSolvPay
- Tabs3 Taskbill license, Matter Manager screen, Client Funds vs Trust Accounting split
- Aderant iTimekeep/Onyx/BillBlast/Virtual Pricing Director product names, Stridyn/MADDI, Harvey partnership, Am Law 200 statistics

## Vendor-specific Findings

1. **The market decomposes billing from the matter workspace in both directions.** Bill4Time, TimeSolv, and Tabs3 each sell case/matter management as a separate module beside billing; Aderant sells time entry (iTimekeep), compliance (Onyx), and bill delivery (BillBlast) as separate products around Expert. The money loop is a nameable, purchasable unit.
2. **Books posture is a real variant** (embedded GL vs QuickBooks/Xero sync), not a definitional property.
3. **Trust accounting is near-universal in the legal-specific market** but is jurisdiction/ethics-shaped; the LPM pass reached the same conclusion independently.
4. **Enterprise firms run the same loop at larger scale with added compliance machinery** (OCG guidelines, e-billing delivery) — the loop shape is invariant; the compliance layer scales with client sophistication.

## Rejected Findings

- **"Trust accounting is definitional"** — rejected: jurisdiction-shaped; a billing system for regimes without client-fund trust requirements would still be this Type. Standard capability (consistent with LPM pass).
- **"LEDES/e-billing is definitional"** — rejected: pre-digital firms billed on paper; formats are era-current machinery. L1/L2.
- **"Matter workspace (documents, deadlines, conflicts) is part of legal billing"** — rejected: it is the LPM seam; sampled vendors ship it as a separate module. Matter appears here as a billing attribution anchor.
- **"Native payments are definitional"** — rejected: desktop-heritage products billed by mail; payments are the current collection layer. L1.
- **"AI time capture is definitional"** — rejected: era marker (Aderant iTimekeep AI capture; Smokeball AutoTime from the LPM pass). L2.
- **"LPM = billing + case management, so billing is a subset of LPM"** — rejected as a Type reading: standalone billing products exist and are the market's own decomposition; the fusion is LPM's differentiator, not this Type's absence.

## Boundary Findings

1. **vs Law Practice Management System (§11, processed) — carried flag RATIFIED from this side: keep-both.** The seam is exactly as the LPM pass proposed: standalone legal billing centers the time-and-billing money loop **without the matter workspace/client file** (no conflicts checking, no court deadlines, no document management as organizing structure). Removal tests confirmed from this side's sample: remove the matter workspace from an LPM → a legal billing application remains (and the market sells exactly that: Tabs3 Billing without PracticeMaster; Bill4Time billing beside its case-management module); add the matter/firm workspace to a billing tool → LPM. The billing loop is LPM's money engine; this Type is that engine standing alone.
2. **vs Legal Spend Management (§11, processed) — mirror-image seam CONFIRMED: keep-both.** This Type is the **firm side**: it generates the bills (time capture → bill assembly → delivery → firm financials, client-anchored). LSM is the **buyer side**: control surface over received bills (review gate, budgets, department money position). The invoice is the shared artifact crossing the boundary — one side generates, the other reviews and approves. Direct evidence of the crossing: Tabs3's UTBMS/Taskbill task-based billing and Aderant's Onyx OCG compliance + BillBlast e-billing delivery exist precisely because corporate clients impose billing guidelines and e-billing formats — the firm-side machinery shaped by the buyer-side gate. Clean split ratified.
3. **vs Legal Matter Management (§11, processed) — consistent, keep-both.** LMM holds the matter record + file + progression (the work). Here matters appear only as billing attribution anchors and rate/fee-arrangement containers (thin records). Remove the money loop from a billing product → matter tracking is not what remains (it was never there); remove matter-file depth → this Type survives intact.
4. **vs Invoicing Application (§08) — adjacent, clean.** Generic invoicing centers the invoice document for arbitrary goods/services. This Type adds the legal billing semantics: timekeeper-based time capture, matter attribution, rate tables by timekeeper level, legal fee arrangements (contingency, retainer, split-fee, progress), pre-bill review, trust/retainer funds, e-billing formats, and firm money reporting (WIP/realization). A generic invoicing tool cannot represent a timekeeper's unbilled WIP.
5. **vs Time Tracking Application (§03.14, processed) — capture vs money.** Time tracking centers capturing and reviewing time; legal billing centers converting captured work into client bills and firm money. Time capture is one leg of this Type; the money loop is the center of gravity.
6. **vs Professional Services Automation (§10, processed) — consistent with that pass's ratification.** Same loop shape (engagement → work → billing → financials), but the legal instantiation carries machinery PSA does not require (matters, timekeeper rate tables, trust funds, contingency semantics, e-billing compliance). Separate Types, cross-referenced.
7. **vs Billing Platform / Subscription Billing (§08, processed) — different money model.** Those center recurring charges against subscriptions/accounts; this centers billable work captured per matter and billed per engagement cycle. No seam conflict.
8. **Naming note.** "Legal billing software" in market usage spans standalone time & billing (Bill4Time/TimeSolv/Tabs3-class) and enterprise financial management (Aderant Expert, which markets itself under practice management). The directory leaf carries the money-loop Type; the enterprise pole is a scale/deployment variant, not a separate Type.

## Historical / Market-Sample Check

- Would a pre-software firm still fit? A 1980s firm with manual time sheets, typed client bills from rate cards, a pre-bill review by the billing partner, a ledger of receivables, and a client-fund/trust ledger: satisfies all three L0 legs. Portals, native payments, LEDES, AI, dashboards are absent → correctly excluded. Check passes.
- Desktop-heritage pole (Timeslips-class, and Tabs3's own on-premises lineage): time entries, client/matter, rate tables, invoice generation, AR — satisfies the core without any cloud machinery. Check passes.
- Regional check: trust regimes vary by jurisdiction (US IOLTA, UK/AU client money — per the LPM pass); a single-jurisdiction billing tool satisfies the core. Multi-currency and tax fields are L2 seasoning. Check passes.
- Non-law-firm check: Bill4Time sells verticals (accountants, architects, consultants, contractors, healthcare) with the same engine — the legal instantiation is the directory leaf; the generic professional time-and-billing engine is the PSA-adjacent territory. The leaf's binding is the legal semantics (matters, timekeepers, trust, contingency), which holds across the whole sample.

## Uncertainties

1. **Tier-1 operational depth for two products only** (TimeSolv KB article; Tabs3 FAQ-level). Bill4Time and Aderant are evidenced at product/FAQ/ecosystem level; internal mechanics (exact invoice state ladders, default approval chains, portal depth) are asserted at capability-family strength only.
2. **CosmoLex and Sage Timeslips unreachable** (403 ×2 each) — the embedded-accounting pole (CosmoLex) and the classic desktop pole (Timeslips) are carried from cross-pass evidence (LPM pass, TimeSolv/Tabs3 footer family) rather than direct observation this pass.
3. **Aderant trust-accounting depth** not observed at fetched level; enterprise trust machinery asserted only via category commonality.
4. **LEDES support at Bill4Time** rests on a customer quote (B layer), not a feature page.
5. Consolidated multi-matter invoicing was not observed at Bill4Time — treated as common-but-not-universal (L1), not a counter-example.

## Final Synthesis

A Legal Billing Application is the law firm's money-loop system of record: it holds the firm's clients and matters as billing anchors with timekeepers and their rates; it captures billable work (time, expenses, flat fees) as entries against that structure; it assembles those entries into draft bills that are reviewed, adjusted, and finalized under each matter's fee arrangement; and it closes the loop — invoices delivered and tracked to payment, client-held funds administered, and the firm's billing money position (work-in-progress, receivables, realization) held inspectable and reportable. Around that core, mature products add timers and mobile capture, activity/task codes, batch invoicing and templates, client portals with online payment, trust accounting with reconciliation, time approvals, ethical-wall access control, e-billing formats, and firm reports including compensation allocation. The Type is the money engine of law-practice management standing alone — real as a standalone product at every firm size, decomposable from the matter workspace in both directions, and the generating counterpart of the buyer-side legal spend management surface.
