# Research Notes — Patent Prosecution Management

Research date: 2026-09-06
Slug: patent-prosecution-management (DIRECTORY §11 Legal, Risk, Compliance & Governance)

## Research Goal

Understand what "Patent Prosecution Management" software actually is in the market: what objects it manages, what its central workflow is, who uses it, and — critically, because the sibling leaf `patent-management` was processed on 2026-09-06 — how it differs from (or overlaps with) Patent Management, Legal Docket Management, and the newer AI patent drafting/prosecution tooling.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: prosecution = the filing-to-grant interaction between applicant and patent office (office actions, responses, notices, allowance, appeals). "Prosecution management" would center the pending application and its office-procedural workflow.
- Likely confusions: Patent Management (sibling leaf, already processed — its research flagged this leaf as "stage/side emphasis of the same structure"); Legal Docket Management (litigation docketing); Legal Matter Management; Legal E-filing Platform (the patent office's own systems); AI patent drafting tools that market themselves as "prosecution software".
- Unknowns: whether any product centers prosecution workflow *without* being a register+docket system; how loosely the market uses the phrase "prosecution software".

## Research Questions

1. What does "patent prosecution" mean procedurally (neutral source)?
2. What is the central object of prosecution management software — the case, the portfolio, or the work product?
3. What does the office-communication loop look like inside the software (event ingestion → deadline → response → recording)?
4. What prosecution-specific artifacts exist in the software (office actions, responses, IDS, appeals, USPTO forms, allowance/issue fees)?
5. How do deadlines work (reference dates, offsets, extension sequences, "missed" as outcome)?
6. What role does patent-office data integration play (Patent Center/Private PAIR, TSDR, EPO, WIPO)?
7. Who uses it, and on which side (firm vs corporate)?
8. Where is the boundary with Patent Management, and with drafting/work-product tooling sold as "prosecution software"?

## Representative Products

Selected for market representation, documentation completeness, different philosophies, different client levels:

| Product | Vendor | Why selected | Evidence layer |
|---|---|---|---|
| AppColl Prosecution Manager | AppColl | Literally named for this Type; deep public help center; SMB/boutique firm-side cloud | A (direct observation, official help center) |
| PATTSY WAVE | Anaqua | Long-established firm-side docketing platform (~200 law firms per vendor); mid-market | A/B (official product + feature pages) |
| AQX Law Firm | Anaqua | Enterprise firm-side IP management with explicit prosecution emphasis | B (official product page) |
| Patent Bots (Prep & Pros Pro etc.) | Patent Bots | Prosecution *work-product* tooling (OA shells, IDS forms, examiner statistics) — contrast case | B (official product pages) |
| PowerPatent | PowerPatent | Self-described "patent prosecution software" centered on drafting — boundary/terminology case | B (official product page) |

Neutral domain source: USPTO official patent-process documentation (Tier 1 for the domain process, not for any product).

Note: PATTSY WAVE and AQX Law Firm are the same vendor (Anaqua) — cross-product claims below never count them as two independent confirmations. Effective independent vendors: AppColl, Anaqua, Patent Bots, PowerPatent.

Rejected/abandoned candidates: TurboPatent (turbotent.com is an unrelated camping-tent retailer; turbo-patent.com unreachable — transport error twice, abandoned per network rules); Kluwer IP Wizard (kluweripwizard.com transport error); CPI (cpipatents.com timed out twice). Clarivate FoundationIP was unreachable in the sibling pass (2026-09-06) and was not retried.

## Sources

- USPTO — Patent Basics: https://www.uspto.gov/patents/basics (fetched 2026-09-06)
- USPTO — How to apply for a patent (process overview): https://www.uspto.gov/patents/basics/patent-process-overview (fetched 2026-09-06)
- AppColl Help Center — Prosecution Manager Overview Manual: https://support.appcoll.com/en_US/general-information/appcoll-overview-manual (fetched 2026-09-06)
- AppColl Help Center — Tasks category (59 articles): https://support.appcoll.com/en_US/tasks (fetched 2026-09-06)
- AppColl Help Center — eOffice Actions category: https://support.appcoll.com/en_US/eoffice-actions (fetched 2026-09-06)
- Anaqua — PATTSY WAVE product page: https://www.anaqua.com/pattsy-wave/ (fetched 2026-09-06)
- Anaqua — Achieve Docketing Excellence (PATTSY WAVE features): https://www.anaqua.com/pattsy-wave/achieve-docketing-excellence/ (fetched 2026-09-06)
- Anaqua — AQX Law Firm product page: https://www.anaqua.com/aqx-law-firm/ (fetched 2026-09-06)
- Patent Bots — home/products: https://www.patentbots.com/ (fetched 2026-09-06)
- PowerPatent — home: https://www.powerpatent.com/ (fetched 2026-09-06)
- Sibling research (context, not evidence): research/patent-management.md, applications/patent-management.md (2026-09-06)

## Product Observations

### AppColl Prosecution Manager (evidence layer A — official help center, deep)

Positioning: "cloud-based intellectual property management system" with integrated modules: Tasks, Matters, Prior Art, Files, Billing, Reports, Conflicts, Contacts, Tandem. Product name itself is "Prosecution Manager"; help center says "Patent prosecution docketing items are tasks."

- **Matters**: central record; unique Attorney Ref; bibliographic data (normally imported from USPTO Patent Center XML; foreign matters via spreadsheet/manual); statuses Unfiled → Pending → Published → Issued → Expired; parties (Applicants, Assignees, Licensees, Adverse Parties); Abstract & Claims tab (published/issued claims); family connections (priority connections + others used for IDS); transitive "related matters".
- **Task history = prosecution history**: matter detail shows task history with status, reference date, respond-by date, final due date, closed-on date, owner, deadline type; XML imports from USPTO create event tasks starting with "USPTO…" showing "the prosecution history as recorded by the USPTO".
- **Tasks = docket**: a task is either a to-do ("Respond to Non-Final Office Action") or an event record ("Received Non-Final Office Action"). Statuses: Open, Completed, Not Needed, Transferred, Reviewed, Missed. "Missed" means work not completed by deadline (extension required). Tasks normally associated with matters; auto-generated when data changes (manual entry, XML import, or another task's status change).
- **Task types**: admin-managed; type name, owner default, trigger events, reference date + offset (e.g., "Respond to Final Office Action - 2 Month Deadline" = trigger's reference date offset 2 months), deadline type (internal vs external), notifications (email/calendar invites), default comments, attached forms/form letters. ~189 standard task types listed. Workflow diagrams show parent→child task generation.
- **Extendable deadlines**: system does not auto-create extension tasks (to avoid docket flooding); marking an extendable task "Missed" closes it and creates the next deadline in the sequence (e.g., missing the 3-month response deadline creates the 4-month extension deadline). Explicit guidance that "File Statement of Use"-type tasks should only be marked complete if actually filed.
- **Appeals chain (auto-generated)**: Attend Oral Hearing, File Petition for EOT to File Appeal Brief, File Appeal Brief in Response to Notice of Appeal, File Reply Brief, Pay Appeal Forwarding Fee, Review PTAB Decision.
- **IDS / prior art**: Prior Art module stores references once, links to every citing matter; generates IDS; populates USPTO SB08A form via XML; cross-cites references to all un-issued related US matters automatically; per-matter IDSCount/RefCount/CiteCount (red CiteCount = uncited references exist). "File Supplemental IDS" task auto-generated for pending US applications when a related matter receives certain events (due date 90 days out — product-specific figure).
- **Office data integration**: USPTO Patent Center XML import (patents), TSDR (trademarks, auto-refreshed every 7 days), Espacenet lookups for prior-art metadata; foreign matters manual/spreadsheet ("no public databases where AppColl can retrieve this information").
- **e-Office Action processing** (PM Plus/Corporate tiers): USPTO e-Office Action emails → event task ("USPTO e-Office Action:…"), automatic retrieval of the office action document from Patent Center, bibliographic update; unknown matter → email to admin or auto-create matter (setting); report "USPTO e-Office Actions in Last 7 Days"; USPTO 892 form (List of References Cited by Examiner) scanned by AI model, references extracted.
- **Reconciliation tasks**: "Review USPTO Status Change" (status changed at office), "Review USPTO Communication" (catch-all when no specific task matched), "Review Differences" (discrepancies between stored data and Patent Center/TSDR/Espacenet data).
- **Housekeeping rules**: tasks should not be deleted (keep complete matter history); task generation can be disabled for inactive statuses (Expired, Transferred, Abandoned); overdue tasks stay on the open docket unless auto-close configured; calendar entries generated for external-deadline tasks; client-reporting emails sent to internal users (not directly to clients) when external-deadline tasks are created.
- **Billing**: billing items (fees, expenses, payments, write-offs) → invoices grouped by matter; LEDES e-invoice generated with every invoice; sent invoices locked against changes; timers for time entry.
- **Contacts/roles**: role-typed contacts (Patent Attorney, Paralegal, Docketing Manager, Manager, Account Administrator); duplicate inventor contacts from imports merged via tooling.
- **Tandem**: firm provides client a controlled copy of portfolio data, transferred automatically from the firm's account; firm controls scope, can adjust or stop.

### PATTSY WAVE / Anaqua (evidence layer A/B — official product + feature pages)

Positioning: "patent and trademark docketing software" for IP operations; ~200 law firms (vendor claim); "single-screen design"; docketing team is "the heart of any successful IP operation".

- **AutoDocket & Download**: automatically dockets incoming US patent and trademark activity, saves corresponding documents against the matter, triggers workflow actions matching internal practices; links the system with Private PAIR and TSDR; vendor claims it turns a 10–12 step per-e-office-action process into 3 steps.
- **Web Data Validation**: uses public office websites — USPTO (PAIR & TSDR), CIPO, WIPO (PCT & Madrid), EPO, EUTM "and many more" — to enter and validate data; paired with "filing assistants" for new and historical filings.
- **Mass Compare**: scans all US patent matters against Private PAIR data to identify discrepancies.
- **IDS**: cross-citing references between family members or similar technology areas; generate new or supplemental IDS forms in one step.
- **Forms & correspondence**: one-click USPTO PDF fillable forms; one-click email/letter to clients, foreign associates, outside counsel.
- **Renewals integration**: integrated with Anaqua Renewal Services; renewal data and payment instructions exchanged automatically with the payment service; renewal instructions made directly in the matter record.
- **Reporting**: browser-based, Quick Reports Writer (custom interactive reports).
- **AQX Law Firm (same vendor, enterprise line)**: "Increase prosecution efficiency with AI driven document auto-processing, office action responses, and IDS generation"; client dashboards for portfolio visibility; docketing automation; data accuracy; time & billing; conflicts; document management; client onboarding.

### Patent Bots (evidence layer B — official product pages)

Positioning: "AI-Enabled Tools for Smarter Patent Prosecution" — attorney productivity tooling, not a register/docket system.

- **Prep & Pros Pro**: rule-based + GenAI tools — patent proofreading (e.g., antecedent basis analysis), patent drafting, **OA shell generation**, **IDS form filling**, USPTO form generation.
- **Examiner Statistics**: per-examiner pages with grant rates, difficulty rankings, appeals statistics.
- **Art Unit Predictor**: predicts USPTO art-unit assignment; flags "dangerous words" in claims.
- **PatentPlex**: US/EU patent family trees, prosecution timelines, patent analyzer.
- **PatentLink**: interactive patent lists for portfolio oversight/workload management.
- No case register, no deadline docket, no matter management — confirms a *work-product intelligence* philosophy adjacent to this Type.

### PowerPatent (evidence layer B — official product page)

Positioning: "Patent Prosecution Software that streamlines each step of the process" — but the listed steps are: Invention Disclosure Capture → Flowchart & Drawing Management → Graphical Claim Drafting → Computer-Aided Description Drafting → Diagnostics (§112 and claim issues) → Inventor/Client Collaboration → Private PAIR Integration.

- Center of gravity is **pre-filing drafting and collaboration**, with Private PAIR integration; no docket, no office-event timeline, no response workflow.
- Important terminology finding: the market phrase "patent prosecution software" is used loosely — some vendors apply it to drafting tools. The phrase alone does not identify this Type's structure.

### USPTO (neutral domain source, evidence layer A for the process)

- USPTO itself uses the phrase "the USPTO patent prosecution process" (in the context of needing legal representation to navigate it).
- Process (official overview): decide → understand pendency & fees → search → apply (Patent Center; eFiler registration + identity verification) → **work with the assigned examiner** (respond in writing to office actions and notices; examiner interviews; appeal to PTAB if claims rejected twice) → receive & maintain (Notice of Allowance + fees due within three months of mailing — **not extendable**; failure → abandonment; eGrants; maintenance fees post-grant).
- "Total pendency" = filing date to issue or abandonment — the prosecution window.
- USPTO communicates only with the attorney/agent of record, not simultaneously with the applicant.
- Post-grant maintenance ("Maintain your patent") is presented as a separate phase from prosecution.

## Cross-product Comparison

| Dimension | AppColl Prosecution Manager | PATTSY WAVE / AQX (Anaqua) | Patent Bots | PowerPatent |
|---|---|---|---|---|
| Central object | Matter (case) + task docket | Matter + docket (single-screen) | None (documents/statistics) | Drafting workspace |
| Office-event ingestion | e-Office Action email processing, Patent Center XML, manual | AutoDocket & Download (PAIR/TSDR), Web Data Validation, Mass Compare | n/a (reads public data) | Private PAIR integration |
| Deadline machinery | Task types + triggers + offsets; extendable sequences; Missed status | Docketing automation + workflow actions | n/a | n/a |
| Prosecution work product | IDS/SB08A, USPTO forms, form letters, appeals tasks | IDS cross-citing, IDS forms, USPTO PDF forms, correspondence | OA shells, IDS forms, proofreading, examiner stats | Claims/description drafting, §112 diagnostics |
| Family handling | Priority connections; transitive related matters; cross-citing | Cross-citing between family members | Family trees (PatentPlex) | n/a |
| Billing | Native (billing items → LEDES invoices) | Time & billing (AQX line) | n/a | n/a |
| Client surface | Tandem (controlled data copy), client-reporting emails | Client dashboards (AQX), correspondence | n/a | Inventor collaboration |
| Register+docket core present? | Yes | Yes | No | No |
| Fits "prosecution management" structure? | Yes (named exemplar) | Yes (docketing-centered emphasis) | No — work-product tooling | No — drafting tool |

Reading: the register+docket core (case records + office-driven deadlines + response workflow) is shared by the products that actually *manage* prosecution. Tooling vendors that attach to the prosecution process (drafting, shells, statistics) lack the core entirely — they are adjacent Types even when they use the phrase "prosecution software".

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

The prosecution case loop:

```text
Prosecution case record
  (one identified record per patent application being prosecuted before a patent office;
   bibliographic identity + parties + prosecution status)
└── Office-procedural timeline
    (recorded office events — filing, publication, office actions, notices, allowance —
     and the response deadlines those events trigger)
└── Response/filing workflow through to a recorded outcome
    (prepare, track, and record the responses and filings the office procedure demands,
     advancing the case toward grant, abandonment, or appeal)
```

Three properties. Remove the case record → nothing remains. Remove the office-event/deadline timeline → what remains is a drafting workspace or a document folder, not prosecution management. Remove the response workflow (preparing and recording what the office demands) → what remains is a passive deadline calendar or a portfolio register, not prosecution management.

Historical/market-sample check: an older single-jurisdiction firm docketing system (case cards + office action entries + response dates + calendar) satisfies this core with no office feeds, no IDS tooling, no AI. A modern drafting tool (PowerPatent) and work-product tooling (Patent Bots) do not satisfy it — consistent with treating them as different Types. The core does not depend on US-specific artifacts: IDS, art units, PTAB are US-practice specifics (L2), while "office communication → deadline → response → outcome" is jurisdiction-neutral.

### L1 — Common Mature Structure

Present across the managing products (AppColl, PATTSY WAVE, AQX), expected in the market but not definitional:

- Docket/task machinery: typed tasks (to-do vs event record), trigger events, reference dates + offsets, internal vs external deadline types, staged reminders/notifications, calendar entries
- Jurisdictional deadline rules (statutory response windows, extension mechanisms) maintained by vendor or firm
- Patent-office data integration: import/sync of bibliographic data and events (USPTO Patent Center/Private PAIR, TSDR, EPO, WIPO, national offices where available); auto-docketing from office communications; discrepancy/reconciliation review tasks
- IDS / prior-art citation management (US practice): shared reference store, family cross-citing, IDS form generation
- Document repository with revision history; office communications and filings attached to case and task
- USPTO/office form generation (fillable PDFs, form letters populated from case data)
- Family/continuation links (priority connections, related-matter views)
- Roles: attorney (owner), paralegal/docketing clerk (daily operator), administrator; audit/activity log
- Client-facing surfaces: client-reporting notifications, controlled client data sharing/portals
- Billing integration (firm side): fee events → invoices (LEDES), invoice freeze after send
- Reporting: saved docket reports, aging/backlog views, scheduled delivery

### L2 — Variant / Optional Structure

- Side: firm-side (billing, client portals, foreign-associate correspondence) vs corporate-side (outside-counsel oversight, disclosure intake upstream)
- Regional regime emphasis: US prosecution practice (office actions, RCE, IDS, PTAB appeals, term adjustment) vs EPO practice (examining communications, divisionals, opposition windows) vs PCT national-phase entry; office-feed availability differs by jurisdiction (US feeds rich; many offices manual/spreadsheet)
- AI assistance: e-Office Action document retrieval, 892-form reference extraction, OA shell generation, document auto-processing
- Examiner/art-unit intelligence (examiner statistics, art-unit prediction) — work-product analytics layered on
- Drafting integration upstream (disclosure capture, claim/description drafting) — the PowerPatent end; some suites bundle it
- Appeals support depth (PTAB task chains; oral hearings)
- Post-grant handoff: renewals/annuities handled natively, via bundled service, or handed to a Patent Management/renewals system

### L3 — Vendor-specific (research notes only)

- AppColl: Tandem (firm→client controlled data copy), 892-form AI processing, "USPTO e-Office Actions in Last 7 Days" report, 90-day supplemental-IDS task offset, ~189 standard task types, invoice freeze semantics
- PATTSY WAVE: AutoDocket & Download (10–12 steps → 3 steps vendor claim), Mass Compare, single-screen design
- AQX: AI document auto-processing framing, client dashboards
- Patent Bots: Art Unit Predictor "dangerous words", Examiner Statistics difficulty rankings
- PowerPatent: graphical claim drafting, §112 diagnostics

## Rejected Findings

- "Prosecution management = docketing only": rejected — the researched managing products all carry the response-workflow layer (IDS, forms, response tasks, appeals), not just deadline tracking; but conversely "prosecution management = AI drafting" is also rejected (PowerPatent shows that framing lacks the case/deadline core).
- "Prosecution management is a distinct structure from patent management": not supported — every managing product in the sample implements prosecution inside the same register+docket core as patent management (AppColl Prosecution Manager is AppColl PM; PATTSY WAVE is Anaqua's firm docketing line; AQX prosecution is a module emphasis). The difference is center of gravity, not structure. Recorded as a boundary issue, not silently merged.
- "US-specific artifacts (IDS, art units, PTAB) are definitional": rejected — they are US-practice specifics; the office-communication loop is the jurisdiction-neutral core.
- "Office feeds are definitional": rejected — AppColl explicitly handles foreign matters by spreadsheet/manual entry; older systems ran on manual docketing.

## Boundary Findings

1. **vs Patent Management (sibling leaf, §11)** — the critical boundary. Shared: register of case/asset records, docket machinery, office-data integration, family links, documents, billing, roles. Different center: Patent Management centers the **whole-life asset** (renewals/annuities, renew-or-prune, portfolio strategy, budgets); Prosecution Management centers the **pending application's office-procedural workflow** through grant/abandonment/appeal. Structural tests: remove post-grant renewals → a prosecution-centered system still stands (renewals are post-grant maintenance, outside prosecution per USPTO's own phase split); remove the office-response workflow → what remains is a renewals/portfolio register (Patent Management). Market reality: both are sold as the same product family with different emphases/editions (AppColl PM vs Prosecution Manager naming; Anaqua AQX vs PATTSY WAVE lines). Conclusion: probable stage/side emphasis of one Type rather than two independent structures — flagged for joint review; this document is written around the prosecution-workflow center because the directory keeps both leaves.
2. **vs Legal Docket Management (§11)** — different object and rules source: court cases and court-imposed deadlines vs patent applications and statute/office-imposed deadlines. A litigation docketing product does not manage claims, IDS, or examiner communication.
3. **vs Legal Matter Management (§11)** — broader container for all legal matters; patent prosecution matters are one matter type inside it, without patent-specific deadline rules and office integration.
4. **vs Legal E-filing Platform (§11)** — the patent office's own filing/management systems (e.g., USPTO Patent Center) are the *counterparty* surface; prosecution management integrates with them (XML imports, e-Office Action emails) but is the firm-side system of record for its own workflow.
5. **vs AI patent drafting tools / Legal Drafting Platform** — drafting tools (PowerPatent; drafting modules of Patent Bots) center document production; no case register, no office-deadline timeline, no response workflow. Market terminology warning: "patent prosecution software" is used loosely by such vendors; the phrase does not identify the structure.
6. **vs Patent Search / Analytics tools** — operate on the global third-party corpus (PatentPlex family trees, examiner statistics); prosecution management operates on the organization's own pending cases.
7. **vs Trademark Portfolio Management (§11)** — same register+docket machinery applied to a different IP class; trademark prosecution exists (TM office actions) but the directory's TM leaf is portfolio-framed; patent prosecution's distinct objects (claims, IDS, examiners, art units) keep the classes separate.

## Uncertainties

- TurboPatent (a prominent prosecution-workflow vendor) could not be reached; its structure (prosecution workspace with OA response drafting) is inferred from market position only and was **not** used as evidence.
- Clarivate (FoundationIP/Inprotech) and CPI unreachable — enterprise-firm-side coverage rests on Anaqua's two lines; enterprise claims are therefore weaker than SMB claims.
- No corporate-side prosecution product was directly researched in this pass (corporate-side evidence comes from the sibling pass's AppColl Invention Manager / corporate editions and from AppColl's billing-module note that corporations use it to track outside-counsel spend). Corporate-side prosecution emphasis is asserted at reduced strength.
- Precise figures observed (90-day supplemental-IDS offset, 7-day TSDR refresh, 3-month non-extendable allowance-fee window, ~189 task types) are product- or office-specific and kept out of the final document except where the source is the office itself (USPTO allowance-fee window) — and even there the final document avoids asserting it as a universal rule.
- Whether any standalone product exists that centers prosecution *without* any portfolio register (single-case tool) — not found in this pass; unknown.

## Final Synthesis

Patent Prosecution Management is best understood as the management application for the **office-procedural life of pending patent applications**: a case record per application, an office-event/deadline timeline anchored to it, and the response workflow that moves each case toward grant, abandonment, or appeal. Its daily reality is a docket of office-driven deadlines worked by docketing specialists and patent attorneys, fed by office communications (increasingly automatically), and producing recorded prosecution history that is itself legal evidence. In the current market it is implemented inside the same register+docket product family as Patent Management, distinguished by center of gravity (pending cases and their office loop vs whole-life assets and renewals) and by typical side (law firm vs corporate IP department). Drafting tools and work-product intelligence tools attach to the prosecution process but lack the defining core and are different Types, however they label themselves.
