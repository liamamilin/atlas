# Research Notes — Patent Management

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Patent Management application really is, from real products: what the central records are, what lifecycle and deadlines the system tracks, who uses it (corporate IP departments vs law firms vs IP service providers), what the standard capabilities are, and where its boundaries lie against neighboring directory leaves (Intellectual Property Management, Patent Prosecution Management, Trademark Portfolio Management, Legal Docket Management).

## Initial Boundary

Initial hypothesis before research:

- Core: a register of patent assets/applications with jurisdiction, family relationships, tracked deadlines (renewals/annuities + prosecution response windows), status, responsible parties, and costs.
- Users: corporate IP counsel, IP paralegals/docketing specialists, patent attorneys in firms, IP administrators.
- Nearest neighbors: Intellectual Property Management (broader, multi-class), Patent Prosecution Management (sibling leaf — suspected overlap), Trademark Portfolio Management (same machinery, different IP class), Legal Docket Management (court-side docketing).
- Main unknowns: whether "prosecution management" is a distinct structure or a stage/emphasis of the same Type; how much renewal-payment execution belongs to the software vs a bundled human service; how deep office-data integration goes.

## Research Questions

1. What is the central record (matter/asset/case) and what identity/bibliographic data does it carry?
2. What lifecycle states does a patent application/patent pass through inside the system?
3. How do deadlines work: where do they come from (rules engine, office data, manual), how are reminders generated, what happens on completion/miss?
4. How do patent family relationships get represented and used?
5. What differs between the corporate side (disclosures, budgets, outside-counsel spend) and the firm side (docketing, billing, client reporting)?
6. How is renewal/annuity management handled — decision, payment, receipts, pruning?
7. What roles and permissions exist?
8. Where is the boundary with Patent Prosecution Management, IP Management, Trademark Portfolio Management, and patent search/analytics tools?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Tier in sample | Position |
|---|---|---|---|
| AQX Corporate (+ AQX Law Firm, PATTSY WAVE) | Anaqua | Enterprise corporate IP operations platform; large multinationals | lifecycle platform + bundled IP services |
| Prosecution Manager / Invention Manager / Tandem | AppColl | Law-firm + small/mid corporate docketing; cloud, modular | firm-side docketing with strong Tier 1 manual |
| Symphony (for Corporations / for Law Firms) + Max-IDS | MaxVal | Mid-tier both-sides IPMS; rules-engine emphasis | country rules + renewals + IDS |
| DIAMS iQ / DIAMS Invent / Simple IP | Dennemeyer | Corporate + firm; renewals-service-rooted vendor (since 1962) | repository + law engine + service bundling |

Clarivate (FoundationIP / CPA Global lineage — the other dominant player) was intended as a fifth sample but its product documentation could not be reached (repeated 404s); see Sources and Uncertainties.

## Sources

Tier 1 (official operational documentation):

- AppColl Help Center — Overview Manual: https://support.appcoll.com/en_US/general-information/appcoll-overview-manual (fetched 2026-09-06)
- AppColl Help Center home (module/category map): https://support.appcoll.com/ (fetched 2026-09-06)

Tier 2 (official product pages):

- Anaqua home: https://www.anaqua.com/ (fetched 2026-09-06)
- Anaqua AQX Corporate: https://www.anaqua.com/aqx-corporate/ (fetched 2026-09-06)
- AppColl home: https://www.appcoll.com/ (fetched 2026-09-06)
- AppColl Invention Manager: https://www.appcoll.com/corporations/invention-manager/ (fetched 2026-09-06)
- MaxVal home: https://www.maxval.com/ (fetched 2026-09-06)
- MaxVal Symphony Docketing: https://maxval.com/symphony-for-patents/docketing/ (fetched 2026-09-06)
- MaxVal Symphony Country Rules: https://maxval.com/symphony-for-patents/country-rules/ (fetched 2026-09-06)
- MaxVal Symphony Portfolio Management: https://maxval.com/symphony-for-patents/portfolio-management/ (fetched 2026-09-06)
- MaxVal Symphony Renewal Management: https://maxval.com/symphony-for-patents/renewal-management/ (fetched 2026-09-06)
- Dennemeyer home: https://www.dennemeyer.com/ (fetched 2026-09-06)
- Dennemeyer DIAMS iQ: https://www.dennemeyer.com/services/digital-ip/diams-iq (fetched 2026-09-06)

Unreachable:

- Clarivate IP management product pages: https://www.clarivate.com/en/solutions/ip-management-software (404), https://clarivate.com/products/foundationip/ (404) — abandoned after two failures per network rules.
- Dennemeyer deep product URLs /en/global/diams-iq/ and /diams-iq/ (404) — root and /services/digital-ip/diams-iq succeeded instead.

## Product Observations

### AppColl (Prosecution Manager / Invention Manager / Tandem) — Evidence Layer A (direct, Tier 1 manual + product pages)

Key observations:

- **Modules**: Tasks, Matters, Prior Art, Files, Billing, Reports, Contacts, Tandem (manual also lists Conflicts). Every module is a table of records with filtering, saved views, CSV/PDF export.
- **Matter = central record**: "something associated with a set of tasks and billed separately to one client. Examples would be patent or trademark applications, invention disclosures, litigation cases, licensing agreements, and copyright filings." Identified by a unique Attorney Ref. Roles on a matter: Attorney (key owner, default task owner), Partner, Paralegal, Contributor.
- **Matter status lifecycle (patents)**: Unfiled → Pending → Published → Issued → Expired (product-documented example).
- **Family connections**: matters can be connected; "priority connections" affect priority date; relations are transitive (A–B, B–C ⇒ A related to C). Connections often auto-generated when importing from USPTO Patent Center / TSDR.
- **Bibliographic data**: normally imported from USPTO Patent Center XML (US) or TSDR (trademarks, auto-refreshed weekly per the manual); foreign matters imported from spreadsheets or entered manually. Patent matters carry inventors and art units; an Abstract & Claims tab shows published/issued claims. Parties tab: Applicants, Assignees, Licensees, Adverse Parties.
- **Task = docket entry**: "a) something someone needs to complete, such as 'Respond to Non-Final Office Action,' or b) a record of an event, such as 'Received Non-Final Office Action.'" Status Open vs closed; a closed status does not imply completion — e.g., "Missed" means the deadline passed and an extension was required. Tasks normally attach to matters; generated automatically when data changes (manual edits, XML/spreadsheet imports, or another task changing status). Deadline fields: reference date, respond-by date, final due date, closed-on date, deadline type. Task types have rules; notifications (templated emails) fire at status changes.
- **Prior Art module**: references stored once, linked to any matter; tracks which references have been cited in IDSs across a matter family (IDSCount/RefCount/CiteCount); generates USPTO SB08A IDS forms; cross-cites references to un-issued related US matters automatically.
- **Billing**: billing items (fees, flat fees, expenses, payments, write-offs, adjustments, retainers) → invoices; LEDES e-invoice generated alongside PDF; invoices locked after being sent; corporations can import outside-counsel invoices to track spend per matter.
- **Reports**: saved views as reports; scheduled runs emailed/FTP'd; account activity log records who changed what and when (audit).
- **Contacts**: role-typed (Patent Attorney, Law Firm, Account Administrator, Docketing Manager, Manager, Paralegal, etc.); inventor contacts auto-created on import, duplicates merged.
- **Tandem**: a no-cost portal giving the firm's corporate client "a controlled copy of their own IP portfolio information," auto-synced from the firm's account; the attorney controls what data transfers and can adjust or stop it.
- **Invention Manager (corporate)**: customizable disclosure form (vendor page documents up to 48 configurable questions), multi-step approval flow with triggered emails, reviewer scoring with weighted attributes, inventor award calculation fed to payroll, reporting (e.g., disclosures per business unit over time), SSO; integrates with Prosecution Manager "from idea to maintenance."
- **eOffice Actions**: electronic processing of USPTO office actions (PM Plus / PM Corporate tiers).
- Positioning: "Start to finish Intellectual Property Management — Matters, Tasks, Contacts, Prior Art, Invoices, Finances, Documents, Workflows, Files."

### Anaqua (AQX Corporate / AQX Law Firm / PATTSY WAVE) — Evidence Layer A (direct, Tier 2 product pages)

Key observations:

- AQX Corporate is organized around **Patent Management** and **Trademark Management** as headline capabilities ("adding more control, IP intelligence, and efficiency to the entire patent lifecycle").
- **IP lifecycle capabilities** (vendor's own decomposition): Innovation Management (ideation → IP protection), IP Operations ("automated docketing, streamline collaboration, manage large volumes of emails and documents"), Portfolio Management ("classify and organize your IP assets to view the portfolio(s) from a variety of perspectives and identify ways to bring more value to the business"), Product-Centered IP ("relationships between IP assets and Products for more contextual decisions, lower risk, and tighter lifecycle planning").
- Supporting features: Financial Management, Document Management, Reporting/Analytics, Application Integration (AQX Sync).
- **Bundled services** (same vendor): Patent Annuity & Trademark Renewal Services, Foreign Filing Services, Docketing and Administrative Services, Data Validation and Portfolio Onboarding, Patent Search Services. This shows renewal payment execution and docketing labor are commonly sold as human services alongside the software.
- Audience split: AQX Corporate vs AQX Law Firm vs AQX Pharma (industry overlay); PATTSY WAVE positioned as docketing-focused ("real-time IP portfolio visibility in dynamic dashboards"); AcclaimIP as separate patent search/analytics.
- Client testimonial (Novo Nordisk, on-page): moving "from our current in-house system to a new generation of patent management software… for professionals in our global patent organization" — confirms the corporate register-replacement job.

### MaxVal (Symphony for Corporations / for Law Firms, Max-IDS) — Evidence Layer A (direct, Tier 2 product pages)

Key observations:

- **Symphony for Corporations — Patent Management decomposition** (vendor's own): Invention Disclosure, Docketing, Portfolio Management, Country Rules, Reporting, Analytics, Renewal Management. **Symphony for Law Firms**: same minus Invention Disclosure. Confirms disclosure intake as the corporate-side differentiator.
- **Docketing**: "auto-docketing and de-docketing features [enable] true 'no-touch' processing of cases based on data synced directly from the US and international patent offices"; "US and international docketing rules are automatically updated"; users can add internal rules.
- **Country Rules (rules engine)**: "a highly-structured set of global intellectual property rules and workflows… updated regularly… cover global statutory intellectual property procedures for each jurisdiction and matter type." Rules "allow for automatic creation of events available in the attorney docket based on the content in the asset record." Smart reminders: "additional 2nd and 3rd-month reminders do not appear on the docket until the 1st reminder is passed." Rule updates are loaded into a QA test environment before promotion to production; custom rules supported. Vendor claims coverage of 200+ jurisdictions plus conventions/treaties (EPC, Paris, PCT, Madrid, Hague, UPC) — marketing figure, not independently verified.
- **Lifecycle stages** (vendor's own categorization): Application Filing, Prosecution, Application Allowance, Post Grant. Rules scope includes renewal rules incl. accumulated annuities, prosecution rules, patent term extension / supplementary protection certificates, expiration term, reinstatement/restoration, opposition period completion, grace periods/further processing, working/use requirements, office-action responses, IDS, priority claims, appeals.
- **Portfolio Management**: "Search, Categorization, Reporting, Ranking, Pruning, and Mapping (patents to products)"; "Projecting and tracking your costs and filings against budgets"; "full access to bibliographic, full specification, and prosecution history (including PDFs of key documents and patent family data)."
- **Renewal Management**: renewal decisions made inside the system; "Project patent family cost, patent lifetime cost"; "Manage the renewal and pruning of IP assets"; "fee payment status and renewal confirmation receipts within Symphony"; automatic renewal instructions; renewal rules updated when country law changes. Renewal payment execution is bundled as a managed service (IP Renewal Services) — software decides, service pays.
- **Max-IDS**: automatically downloads prior-art references, associates them to cases, generates IDS forms.
- Services list mirrors Anaqua's: renewal services, docketing services, paralegal services (filing, recordation, proofreading, patent term adjustment), foreign filing/translations.

### Dennemeyer (DIAMS iQ / DIAMS Invent / Simple IP) — Evidence Layer A (direct, Tier 2 product pages)

Key observations:

- DIAMS iQ described as "your digital IP office": "Integrated IP law engine and wizards for bulk record generation"; "A centralized repository for all IP data, documents, tasks, costs and other matters"; "Powerful search and reporting functionalities and live dashboards"; "Practical workflow and automation features."
- **Audience segmentation** (vendor's own): corporations & universities with R&D focus ("Link invention disclosures directly to IP operations… Coordinate filings, reviews and documentation across regulatory frameworks"); brand owners ("Stay aligned with agents, partners and counsel… Monitor agreements… ensure timely action across jurisdictions… Shape the system according to how your business functions — by region or internal structure"); law firms ("Provide clients with live portfolio insights through a read-only website… Route incoming files and emails directly to the right records using a secure inbox with automated tagging… correspondence templates, high-volume mailings and instant invoicing").
- **FAQ-confirmed behaviors**: data health checks during portfolio import ("limiting the risk of inconsistencies and data damage"); invention disclosure digitization via DIAMS Invent ("a decision workflow portal between inventors / R&D departments and IP colleagues"); an inventor remuneration module (academic/university context).
- Customer testimonial (Rajah & Tann, on-page): "IP management is inherently complex, often involving strict deadlines that must be met to avoid costly errors… DIAMS ensures that we receive timely reminders, allowing us to promptly notify our clients and maintain compliance." Another (Accelleron): smart categorization "links patents and trademarks to projects, products, and components."
- **Simple IP**: a free patent manager "for patent owners who are new to the world of intangibles" — entry-level tier of the same structure.
- Ecosystem: DIAMS Infinity (next-gen IPMS), Octimine (patent search), Dennemeyer API, IP Lounge client center; Managed IP services include Patent Renewals; IP law-firm services include European Patent Validation.
- Vendor blog (contextual, Tier 3): "IP docketing… managing essential data, deadlines and documentation from registering offices"; IPMS blog: portfolios "span multiple jurisdictions, legal frameworks and business priorities… patents, trademarks, designs and a range of adjacent matters such as licenses, oppositions, agreements, domain names."

## Cross-product Comparison

| Structure / capability | AppColl | Anaqua AQX | MaxVal Symphony | Dennemeyer DIAMS | Verdict |
|---|---|---|---|---|---|
| Central patent asset/matter record with bibliographic identity, parties, jurisdiction | ✔ (Matters; Attorney Ref; Applicants/Assignees/Licensees) | ✔ (patent lifecycle management) | ✔ ("asset record", bibliographic + full spec + prosecution history) | ✔ (centralized repository of IP data) | **Defining core** (all four) |
| Per-record status / lifecycle state | ✔ (Unfiled→Pending→Published→Issued→Expired) | ✔ ("entire patent lifecycle") | ✔ (stages: Filing→Prosecution→Allowance→Post Grant) | ✔ (case structure, status) | **Defining core** (all four) |
| Tracked dated obligations + reminders (docket) | ✔ (Tasks; open/closed/missed; auto-generation; notifications) | ✔ ("automated docketing") | ✔ (rules → events on attorney docket; smart reminders) | ✔ ("strict deadlines… timely reminders"; law engine) | **Defining core** (all four) |
| Responsible-party attribution (internal roles + external counsel/agents + client) | ✔ (Attorney/Partner/Paralegal; Law Firm contacts; Tandem client) | ✔ (IP Operations collaboration) | ✔ (rules "meet your and your agent's needs") | ✔ (agents/partners/counsel alignment; secure inbox) | **Defining core** (all four) |
| Patent family / related-matter links | ✔ (priority connections, transitive relations) | implied (portfolio views) | ✔ (patent family data; priority claims) | implied (portfolio structure) | Common mature (explicit in 2, implied elsewhere) |
| Jurisdictional rules engine (vendor-maintained, updatable) | partial (task types + rules; USPTO data import) | ✔ (automated docketing) | ✔ (explicit Country Rules product; QA promotion) | ✔ ("integrated IP law engine") | Common mature (form varies) |
| Office data integration / auto-docketing | ✔ (USPTO Patent Center XML; eOffice Actions) | ✔ (automated docketing) | ✔ (office sync; no-touch auto/de-docketing) | partial (secure inbox tagging; import health checks) | Common mature (depth varies) |
| Renewal/annuity management | not observed as module (firm billing instead) | ✔ (Annuity Services bundled) | ✔ (Renewal Management module + service) | ✔ (Patent Renewals service; DIAMS tracks costs) | Common mature (corporate side); execution often a human service |
| Document repository | ✔ (Files; revisions; per-matter folders) | ✔ (Document Management) | ✔ (PDFs of key documents) | ✔ (documents in repository) | Common mature |
| Prior art / IDS management | ✔ (Prior Art module; SB08A) | not observed on fetched pages | ✔ (Max-IDS product) | not observed on fetched pages | Common (patent-specific; US-weighted) |
| Invention disclosure intake | ✔ (Invention Manager) | ✔ (Innovation Management) | ✔ (Invention Disclosure; corporations only) | ✔ (DIAMS Invent) | Common on corporate side; absent firm-side |
| Reporting / dashboards | ✔ (Reports; scheduled; activity log) | ✔ (Reporting/Analytics) | ✔ (Reporting; Analytics) | ✔ (live dashboards; BI) | Common mature |
| Cost/billing | ✔ (Billing; LEDES; outside-counsel spend import) | ✔ (Financial Management) | ✔ (budgets vs filings; eBilling integration) | ✔ (costs in repository; instant invoicing for firms) | Common mature (form differs by side) |
| Portfolio organization (taxonomy, ranking, mapping to products) | not observed | ✔ (Portfolio Management; Product-Centered IP) | ✔ (categorization, ranking, pruning, mapping) | ✔ (categorization linking to projects/products/components) | Common (corporate-side emphasis) |
| Client/external portal | ✔ (Tandem) | not observed on fetched pages | not observed on fetched pages | ✔ (law-firm read-only client website; IP Lounge) | Common (form varies) |
| Roles & permissions | ✔ (role-typed contacts; Account Administrator) | implied (enterprise) | implied (team standardization) | implied (stakeholder collaboration) | Common mature |
| Multi-IP-class breadth (trademarks, designs, utility models) | ✔ (trademarks in same system) | ✔ (Trademark Management) | ✔ (trademarks; rules cover utility models, designs) | ✔ (patents + trademarks; blog lists designs/domains) | Variant (breadth differs; patent core constant) |
| Bundled human services (renewals, docketing, foreign filing) | not observed | ✔ | ✔ | ✔ | Variant (service-rooted vendors bundle; pure-software vendors less) |
| Free/entry tier | ✔ (Tandem free for firm clients) | not observed | not observed | ✔ (Simple IP) | Variant |

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as Patent Management:

```text
Patent asset register
└── identified patent records (application or granted patent)
    ├── bibliographic identity: number, jurisdiction, parties (applicant/assignee,
    │   inventors, responsible counsel/agent), key dates
    └── lifecycle status (where the asset stands: e.g., unfiled → pending → granted → expired)
+ Tracked jurisdictional deadlines per record
    (renewal/annuity dates, prosecution response windows — computed or recorded)
+ Reminder/alert loop that surfaces upcoming deadlines to a responsible person
```

Test: remove the register → nothing remains (it is the system). Remove deadline tracking + reminders → what remains is a portfolio database or analytics tool, not patent management. Remove status → deadlines lose their anchor. Remove responsible-party attribution → reminders have no addressee and multi-party coordination collapses. All four properties are present in all four sampled products and are the reason the software exists (a missed statutory deadline can forfeit rights).

Historical check: pre-cloud and regional docketing systems (spreadsheet-era and first-generation docketing databases) still satisfy this core — a register of matters with dates, statuses, and reminders. Modern additions (office sync, rules engines, AI) are not needed for the definition to hold. The L0 deliberately does not include: office integration, rules-engine automation, renewals payment, disclosures, multi-class breadth, analytics.

### L1 — Common Mature Structure

Present across the sample (or clearly on one side of the corporate/firm split) but not required to recognize the Type:

- **Docket/task machinery**: tasks auto-generated from record events via rules; open/closed/missed statuses; templated notifications; deadline fields (reference date, respond-by, final due).
- **Jurisdictional rules maintenance**: vendor- or user-maintained rules that compute deadlines per jurisdiction and matter type, updated when laws change; QA/test promotion and custom rules in the most explicit implementation.
- **Patent family / related-matter links**: priority chains, national/regional phase members, transitive "related" views.
- **Office data integration**: import/sync of bibliographic data and events from patent offices (e.g., USPTO Patent Center XML; auto-docketing/de-docketing); manual/spreadsheet import for offices without feeds.
- **Renewal/annuity management**: fee quotes, renewal decisions (renew vs prune), payment status, receipts, auto-renewal instructions, accumulated-cost projection.
- **Document repository**: per-matter folders, revision history, attachments to tasks.
- **Prior-art / IDS management** (patent-specific): references stored once and linked across the family; IDS form generation; citation counts.
- **Reporting & dashboards**: saved queries, scheduled reports, KPI dashboards, audit/activity logs.
- **Cost & billing**: firm side — billing items → invoices (e.g., LEDES), timers; corporate side — budgets, outside-counsel invoice review, spend per matter.
- **Invention disclosure intake** (corporate side): submission forms, approval flows, reviewer scoring, inventor awards, hand-off to filing.
- **Portfolio organization**: configurable taxonomy/categorization, ranking, pruning, mapping patents to products/projects.
- **Roles & permissions**: attorney/paralegal/docketing-clerk/administrator roles; client and external-party roles.
- **External collaboration surfaces**: client portals (read-only portfolio views), secure inboxes routing correspondence to records, agent/counsel networks.

### L2 — Variant / Optional Structure

- **Side emphasis**: corporate IP department vs law firm vs IP service provider — same core, different module emphasis (disclosures/budgets vs docketing/billing vs renewals execution).
- **IP-class breadth**: patent-only vs patents + trademarks + designs + utility models (+ domains, licenses, oppositions as adjacent matters).
- **Renewal execution bundling**: software-only decision support vs vendor-operated renewal payment services.
- **Office-connectivity depth**: manual entry → spreadsheet import → office XML/sync → electronic office-action processing.
- **Industry overlays**: pharma (patent term extension, supplementary protection certificates), universities (inventor remuneration), tech/semiconductors.
- **Regional regimes**: US-weighted features (IDS, patent term adjustment) vs European (validation, opposition periods) vs global PCT/Madrid/Hague coverage.
- **Deployment & tier**: enterprise SaaS, mid-market subscription, free entry tiers for startups, API access.
- **Analytics depth**: portfolio analytics, AI classification, integrated patent search.

### L3 — Vendor-specific Structure (Research Notes only)

- AppColl: Tandem (free client portal), 48-question disclosure forms, eOffice Actions tiering, LEDES auto-generation, "Attorney Ref" as matter key, weekly TSDR auto-refresh.
- MaxVal: "GFW technology" office sync, "4th generation IPMS" positioning, 200+ jurisdiction coverage claim, QA test environment for rules, smart-reminder sequencing (2nd/3rd reminders gated on 1st).
- Anaqua: AQX HyperView dashboards, ideaPoint, AcclaimIP integration, AQX Sync, client-advisory product model (User Group).
- Dennemeyer: DIAMS Invent, IP Lounge, Simple IP (free tier), Octimine, Dennemeyer API, inventor remuneration module, 1962 heritage/agent network.

## Vendor-specific Findings

- Renewal payment execution is sold as a managed human service by three of four vendors (Anaqua, MaxVal, Dennemeyer); the software's role is decision + tracking + receipts. AppColl (firm-side) shows no renewal-execution module in the fetched docs — consistent with firms billing clients for renewals rather than executing them.
- The corporate/firm product split is explicit in three vendors (Anaqua AQX Corporate/Law Firm; MaxVal Symphony Corporations/Law Firms; AppColl Prosecution Manager/Invention Manager + Tandem bridge; Dennemeyer segments its marketing the same way). The split is about which modules are emphasized, not about different core structures.
- Firm→client data sharing appears both as vendor product (AppColl Tandem) and as a firm feature (Dennemeyer law-firm read-only client website) — same job, different packaging.

## Rejected Findings

Candidates considered for the defining core and rejected (with reasons):

- **Patent-office data integration / auto-docketing** — common and increasingly expected, but older and regional products run on manual entry; a patent management product without office feeds is still patent management. → L1.
- **Invention disclosure intake** — absent from firm-side products; corporate-side module. → L1 (corporate-side common), not defining.
- **Renewal payment execution** — frequently a human service, not software structure. → L1/L2.
- **Multi-IP-class breadth (trademarks/designs)** — patent-only products exist and are unmistakably Patent Management. → L2.
- **Portfolio analytics / AI / search** — value-add layers; analytics-only tools (AcclaimIP, Octimine, Relecura) are a different Type. → L2.
- **Budgeting / eBilling** — corporate-side common, not defining. → L1.
- **Client portals** — common but form varies widely; some products lack them. → L1.
- **Rules engine as a named subsystem** — the *function* (deadline computation per jurisdiction) is L0-adjacent, but the *engine as packaged subsystem* is an implementation; older products computed deadlines manually with per-jurisdiction reference tables. Concept in L0, engine in L1.

## Boundary Findings

1. **vs Patent Prosecution Management (sibling leaf, §11)** — the strongest boundary question. Evidence: the sampled firm-side product is literally named "Prosecution Manager," yet its documented structure is the full patent-management core (matters, docket tasks, family links, billing, reports, portfolio). Prosecution (filing → examination → allowance → grant) is one lifecycle stage of a patent asset, and prosecution-stage workflow (office-action response tracking) is a capability inside every sampled product. Structural test: remove prosecution-stage workflow → a renewals-focused patent management system remains (exists in market); remove the register + deadlines → nothing remains. Conclusion: Patent Prosecution Management is best understood as the prosecution-stage / law-firm emphasis of the same Type, not a distinct structure. Flagged for joint review; no taxonomy change made unilaterally.
2. **vs Intellectual Property Management (sibling leaf, §11)** — IP Management is the multi-class superset (patents + trademarks + designs + domains + licenses + oppositions; Dennemeyer's blog enumerates exactly this breadth). Patent Management is the patent-restricted specialization; vendors ship one product with class-specific modules and rules. Gradient, not wall.
3. **vs Trademark Portfolio Management (sibling leaf, §11)** — same machinery (register + deadlines + status + parties + costs) applied to a different IP class with a different lifecycle (renewals vs annuities, use requirements, goods/services). Sibling specialization sharing the pattern.
4. **vs Legal Docket Management (§11)** — court docketing tracks litigation cases and court-imposed deadlines; patent docketing tracks patent assets and statute/office-imposed deadlines. Different central object and different rules source. Patent docketing is the patent-side analog within Patent Management, not the same Type.
5. **vs patent search/analytics tools (no dedicated leaf; Anaqua AcclaimIP, Dennemeyer Octimine, MaxVal Relecura ship them as separate products)** — analytics tools operate on the global patent corpus of third-party patents; Patent Management operates on the organization's own asset records. Different central object; vendors separate them into distinct products.
6. **vs renewal-service providers** — renewal payment execution is a service wrapped around the same data; the software leaf covers the management/decision/tracking layer.

## Uncertainties

- **Clarivate unreachable**: the largest IP-management vendor (FoundationIP/CPA Global lineage) could not be documented directly. The sample still spans four vendors and both sides of the market, but assertions about "all major products" are avoided; cross-product claims rest on the four researched products.
- **Rule-coverage figures** (e.g., "200+ jurisdictions") are vendor marketing claims; not independently verified and kept out of the final document.
- **Renewal payment execution depth** observed only through service pages, not through operational documentation of the payment workflow itself; final document describes decision/tracking/receipts with moderate wording.
- **Historical products** (pre-2000 docketing systems, regional IP-office-native tools) were not directly researched; the historical fit of the L0 is structural reasoning (register + dates + reminders + status), not direct observation.
- **Conflicts module** (AppColl) was listed but not documented in the fetched manual section; treated as unverified detail.
- **Weekly TSDR auto-refresh** and similar cadence details are product-specific operational facts; kept in Research Notes only.

## Final Synthesis

A Patent Management application is organized around a **register of the organization's (or firm's clients') patent assets** — identified records for applications and granted patents carrying bibliographic identity (number, jurisdiction, parties, key dates) and a lifecycle status. Around the register, the system's defining job is **deadline safety**: dated obligations per record (renewal/annuity dates, prosecution response windows) are computed or recorded, surfaced through reminders to a responsible person, and closed out with an auditable outcome — because a missed statutory deadline can forfeit rights. Everything else in mature products extends this spine: docket/task machinery, jurisdictional rules maintenance, family links, office-data feeds, renewal management, documents, prior-art/IDS, reporting, cost/billing, disclosure intake, portfolio organization, roles, and collaboration surfaces. The corporate side emphasizes the front of the lifecycle (disclosures, budgets, portfolio strategy); the firm side emphasizes prosecution docketing and billing; service-rooted vendors bundle renewal execution. The Type's nearest ambiguous neighbor, Patent Prosecution Management, is best understood as a stage/side emphasis of this same structure rather than a separate one.
