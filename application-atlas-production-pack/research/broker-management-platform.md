# Research Notes — Broker Management Platform

## Research Goal

Understand what a Broker Management Platform (insurance context) really is as an Application Type: what objects exist inside it, what its users do with them, how the broker's work flows through the system, which states/rules matter, and where its boundaries lie against neighboring Types (Insurance Agency Management, Insurance Policy Administration System, Insurance Quote Platform, CRM, Underwriting Workbench, Insurance Claims Management, and the name-collision leaves Brokerage Platform / Freight Brokerage Platform).

## Initial Boundary

The leaf sits in DIRECTORY §08 Finance, Banking, Insurance & Investment, directly between "Insurance Agency Management" and "Insurance Quote Platform". Working hypothesis at start:

- The intended meaning is **insurance broker-side back-office software** — the system a brokerage firm runs its business on (clients, policies placed with insurers, commissions, renewals, documents, accounting).
- Not: securities brokerage (that is the separate "Brokerage Platform" leaf), not freight brokerage ("Freight Brokerage Platform" leaf), not insurer-side broker-network management.
- The closest sibling is "Insurance Agency Management" — in market usage, the US term is "agency management system (AMS)" and the UK/Commonwealth term is "broker management system (BMS)"; these may be the same Type under regional names. This had to be tested, not assumed.

## Research Questions

1. What are the core objects? (client, policy, insurer/carrier, quote, commission, document, task, ledger…)
2. What is the placement workflow? (risk capture → quote → bind → in-force → mid-term adjustment → renewal)
3. How does money flow? (premium collection, client money / trust accounting, commission statements, producer splits, insurer settlement)
4. How do insurers connect? (carrier download/EDI, rating hubs, portals, comparative raters)
5. What roles use the system? (producer/account executive, account handler/CSR, accounts, compliance, management)
6. What regulatory machinery exists? (client money, audit trail, E&O documentation, licensing)
7. What does the renewal lifecycle look like as a bulk, recurring operation?
8. Where is the boundary vs Insurance Agency Management — same Type or different?
9. Where is the boundary vs insurer-side policy administration, quote platforms, CRM?

## Representative Products

Selected for market representation, documentation reachability, different product philosophies, and different customer tiers/geographies:

| Product | Market | Philosophy / tier | Evidence tier reached |
|---|---|---|---|
| Acturis | UK (+ international) | SaaS platform for brokers, insurers and MGAs; mid-to-large commercial brokers | Official product pages (Tier 2) |
| SSP | UK (+ global) | Long-established broker/insurer/MGA solution family; high-street to call-centre brokers | Official product pages (Tier 2) |
| HawkSoft | US | SMB independent agencies; simplicity + all-inclusive subscription; desktop app + cloud data | Official product pages (Tier 2) |
| Vertafore AMS360 | US | Mid-market/enterprise AMS; accounting depth + AI agents | Official product page (Tier 2) |
| EZLynx | US | Comparative-rater-first all-in-one system for startup/growth agencies; owned by Applied Systems | Official product pages (Tier 2) |

Applied Epic (Applied Systems; the largest US/UK agency & broker system) was attempted first but the vendor site returned 403 twice — abandoned per the source-access rule. EZLynx (an Applied Systems company) partially covers that vendor family. Open GI (UK) timed out twice — abandoned.

## Sources

All fetched 2026-09-06.

- Acturis — https://www.acturis.com/ (root), https://www.acturis.com/product/ (product page)
- SSP — https://ssp-worldwide.com/ (root), https://ssp-worldwide.com/broker (broker solutions)
- HawkSoft — https://hawksoft.com/ (root), https://hawksoft.com/agency-management-system/ , https://hawksoft.com/accounting/ , https://hawksoft.com/agency-management-system/tour/
- Vertafore AMS360 — https://www.vertafore.com/products/ams360
- EZLynx — https://www.ezlynx.com/

Unreachable / abandoned:

- Applied Systems (Applied Epic) — https://www.appliedsystems.com/en/gb/products/applied-epic and /en/us/... → 403 ×2
- Open GI — https://www.opengi.co.uk/ → timeout ×2

No Tier-1 help-center / user-guide articles were reachable in this pass; all evidence below is from official product/marketing pages. Consequently no precise operational facts (numeric limits, exact state names, default settings, exact reconciliation mechanics) are asserted anywhere.

## Product Observations

Evidence layers: **A** = directly observed on that product's official page; **B** = cross-product commonality; **C** = canonical inference.

### Acturis (UK) — observations (A)

From /product/:

- Positioned as "fully integrated, cloud-based platform" for brokers, insurers, MGAs; commercial and personal lines broking solutions.
- Module list: E-trade ("broad and deep panel of insurers trading on our system… latest insurer products and rating hubs… for both personal and commercial lines"); Digital Distribution (full quote-and-buy portal, customer service mobile apps, build your own digital journey); Product & Scheme Build ("build, host and distribute products across multiple channels from a single product instance… underwriting control"); CRM ("early prospecting right through to the sale and beyond… track performance, identify opportunities"); Customer Communication ("re-uses data across all document types… generate branded documents, emails and SMS automatically… integrated document management facility"); Policy Administration ("fully integrated back-office administration… full-cycle policy management and real-time policy information"); Mobile; Business Intelligence ("configurable reports and dashboards… analytical view of any part of your business"); Claims Management ("links the claim to the policy… capture of data… segmented by claim type, delegated authority or contact"); Accounting ("manage debts and payments, maintain client and office bank accounts, profit and loss, budgets and balance sheets"); Robotics & Automation; Compliance ("support and show your regulatory compliance using workflows, providing audit trails, securing personal data and making client money calculations"); AI.
- Root page: brokers transact "over £18.5bn of premium every year… on the Acturis platform in the UK alone" (vendor stat — L3); "8 out of 10 of the UK's top insurer extranets" built by Acturis (vendor stat — L3).
- Distinctive posture: the same platform family also serves insurers and MGAs — the broker system is embedded in a market-wide trading network (L3 posture, but shows the intermediary connectivity structure).

### SSP (UK) — observations (A)

From /broker:

- "Broker software solutions… manage their clients and policies more efficiently"; "centralised platform for brokers to manage their clients, track policy renewals, and process claims"; "access to a wider range of insurance products, allowing them to compare rates and coverage options from multiple carriers".
- Broker product information list: full policy administration solutions; personal lines insurer products; commercial lines insurer products; **scheme capabilities**; data enrichment through major providers; **accounts solution**; standard reporting pack; access to your data; fully integrated payment solutions; flexible communication methods; digital journeys – quote and buy; document & template creation; **policy management and task flow**; fully hosted and managed.
- Suite functionality named: "policy administration, claims management, and billing to reporting, document management, and customer relationship management".
- Integration: "exchange data with other stakeholders in the insurance value chain… insurers, brokers, reinsurers, external data providers, and regulatory bodies".
- Personal lines scale: "transact through all the major UK price comparison sites" (UK personal-lines variant marker).
- Serves brokers, insurers, MGAs/UMAs, financial advisers (adviser variant manages clients' policies — adjacent posture).

### HawkSoft (US) — observations (A)

From root, /agency-management-system/, /accounting/, /agency-management-system/tour/:

- Self-described "agency management system" for independent agencies; since 1995; SMB focus; all-inclusive subscription (no per-feature menu).
- "Intuitive PL and CL policy management"; "standardizes processes across policies and carriers"; "automates documentation and mitigates E&O"; "helps staff keep track of tasks and schedules".
- Unified Client File; Sales & CRM Pipeline; Personal & Commercial Workflows; Carrier Downloads ("automatically retrieve carrier policy documents"); Submission Tracking; HawkLink (policy data autofill on carrier websites); Home/Auto Rater integration; Workers' Comp.
- Auto-documenting "Action Menu": every client interaction (call, email, text, campaign) logged as history — E&O posture.
- Task management for client & agency tasks; activity tags; document management stored in the system; built-in ACORD form library with prefill; Virtual Printer (PDF writer).
- Commission management & statement importer: "Import Excel or CSV commission statements with fields automatically mapped to HawkSoft's accounting system".
- Accounting: "trust accounting and commission tracking built into HawkSoft, with operating accounting managed in QuickBooks"; invoicing & payments, receipts & invoice reports, daily deposits & bank reconciliation, close-of-month workflows; optional Managed Accounting service (bookkeepers).
- Growth: website lead capture, uprate alerts (premium increases ahead of renewal), email marketing/batch email/texting, cross-sell and upsell reports, retention alerts, sales pipeline reports.
- Agency Intelligence™ reporting/KPI engine + Report Generator; "commissions by carrier, retention, book of business reports".
- Client-facing: Insured mobile app (24/7 access to policies, coverages, ID cards); Agent Portal (browser access for staff); self-service certificates portal (clients add/edit certificate holders, generate approved certificates).
- Platform shape: native Windows desktop app with full features + browser "Agent Portal" with many features; cloud-hosted data; data conversion from legacy systems as a service; export your data on demand.

### Vertafore AMS360 (US) — observations (A)

From /products/ams360:

- "connects your people, processes, and data in one management system"; agency management system for agencies (FAQ: users are "agents, brokers, CSRs, and agency principals").
- Service: "Easily manage your policies' lifecycle — from bind to renewal"; "Eliminate policy entry — carriers directly download new policies, endorsements, claims, and renewals"; advanced search; "Accelerate renewals — prioritize key clients, send proposals, and mass-distribute certificates".
- Accounting: "Automate billing and invoicing… payment tracking and account reconciliation"; "Pay producers accurately — commission splits are auto-calculated and shown in statements"; "Make month-end easy — a general ledger ensures accurate, compliant financial records".
- Leadership/BI: monthly/quarterly/annual trends, KPIs, full financial reports.
- AI agents: Email Agent (interprets incoming emails, summarizes, triggers workflows); Reconciliation Agent ("automatically matches carrier statements to agency transactions to handle revenue, commissions, and payables").
- AgencyOne: connected platform joining AMS360 with other Vertafore and third-party tools; certificates workflow ("create, issue, and manage certificates from a single connected workflow").
- FAQ definition of AMS (vendor's own category definition): "specialized software that helps insurance agencies manage client policies, streamline accounting (billing, commissions, and financial transactions), and automate workflows—all in one centralized platform".
- Vertafore family context: QQCatalyst, Sagitta, BenefitPoint (benefits), Sircon (licensing/compliance), PL Rating & Commercial Submissions (rating), TransactNOW / Carrier/MGA Download / Book Roll (connectivity), ImageRight (document management), InsurLink (client portal), AgencyZoom (sales automation).

### EZLynx (US, Applied Systems) — observations (A)

From https://www.ezlynx.com/:

- "All-in-One Management System" + "Comparative Rater" + Agency Websites; positioned for startup and growth agencies; footer confirms Applied Systems ownership.
- Comparative Rater: "real-time quotes from multiple carriers with just one entry… connects to more carriers (over 330!)" (vendor stat — L3); anti-rekeying pitch.
- Management system: "organizing quotes, policies, documents, service requests, and client communications in one place"; "manage and automate every stage of the insurance policy lifecycle"; policy management, renewal management, accounting, and reporting; EVA embedded AI (account summarization etc.).
- Client Center: 24/7 client self-service connectivity.
- Solutions by stage (new agency → multi-location enterprise) and by use case (servicing & policy management, sales & marketing, renewals & retention, accounting & payments, native rating & submissions).

## Cross-product Comparison

| Structure | Acturis | SSP | HawkSoft | AMS360 | EZLynx | Layer |
|---|---|---|---|---|---|---|
| Client records (unified client file) | ✓ (CRM + client data reuse) | ✓ ("manage their clients") | ✓ (Unified Client File) | ✓ (client management) | ✓ (client communications organized) | B — universal |
| Policy records bound to insurer products, per term | ✓ (Policy Administration, full-cycle) | ✓ (full policy administration) | ✓ (PL & CL policy management) | ✓ (policy lifecycle bind→renewal) | ✓ (policy management) | B — universal |
| External insurers as counterparties (multi-insurer placement) | ✓ (panel of insurers on e-trade) | ✓ ("compare rates… from multiple carriers") | ✓ (carrier downloads, HawkLink to carrier sites, rater) | ✓ (carrier downloads; 200+ carriers named for reconciliation agent) | ✓ (330+ carriers rater) | B — universal |
| Quote/submission workflow toward insurers | ✓ (e-trade, rating hubs) | ✓ (digital journeys; compare rates) | ✓ (submission tracking, rater, HawkLink) | ✓ (Commercial Submissions family; PL Rating adjacent) | ✓ (comparative rater, one entry) | B — universal |
| Renewal as recurring lifecycle operation | ✓ (full-cycle policy management) | ✓ ("track policy renewals") | ✓ (renewal reports, uprate alerts, workflows) | ✓ ("accelerate renewals… send proposals") | ✓ (renewal management) | B — universal |
| Commission tracking & reconciliation | ✓ (accounting module) | ✓ (accounts solution) | ✓ (commission importer, trust accounting) | ✓ (commission splits, Reconciliation Agent) | ✓ (accounting & payments) | B — universal |
| Premium/client accounting (billing, deposits, ledger, month-end) | ✓ (client & office bank accounts, P&L, balance sheets) | ✓ (accounts solution, integrated payments) | ✓ (trust accounting; QuickBooks for operating) | ✓ (billing, GL, month-end) | ✓ (accounting) | B — universal |
| Carrier download / data feed from insurers | — (e-trade is the connectivity) | ✓ (data enrichment providers) | ✓ (carrier downloads) | ✓ (carrier download incl. claims) | ✓ (implied via rater/AMS integration) | B — common (form varies) |
| Document generation & management at policy level | ✓ (branded docs, emails, SMS; integrated document management) | ✓ (document & template creation) | ✓ (ACORD library, virtual printer, drag-drop docs) | ✓ (ImageRight adjacent; certificates) | ✓ (documents organized) | B — universal |
| Task/workflow + interaction logging (E&O) | ✓ (workflows, audit trails) | ✓ (policy management and task flow) | ✓ (Action Menu auto-documentation, tasks) | ✓ (workflows; Email Agent triggers) | ✓ (automation of service requests) | B — universal |
| Claims handling | ✓ (claims management module, linked to policy) | ✓ (process claims) | — (claims arrive via carrier download) | ✓ (claims via download) | ✓ (claims in one place — testimonial) | B — common, depth varies |
| Sales/CRM layer (leads, pipeline, cross-sell) | ✓ (CRM module) | ✓ (CRM in suite list) | ✓ (lead capture, pipeline, cross-sell reports) | ✓ (AgencyZoom adjacent; cross-sell via RiskMatch) | ✓ (sales & marketing) | B — universal |
| Reporting/BI on the book | ✓ (BI module) | ✓ (standard reporting pack) | ✓ (Agency Intelligence, report generator) | ✓ (KPIs, financial reports) | ✓ (reporting) | B — universal |
| Client self-service (portal/app, certificates, ID cards) | ✓ (quote-and-buy portal, customer apps) | ✓ (digital journeys) | ✓ (insured app, agent portal, self-service certificates) | ✓ (InsurLink adjacent; mass-distribute certificates) | ✓ (Client Center) | B — common |
| Roles: producers/CSRs/accounting/admin | implied (multi-module) | implied | ✓ (agency setup & user management) | ✓ (agents, brokers, CSRs, principals) | implied (stage-based) | B — common |
| Regulatory/compliance machinery | ✓ (compliance module: audit trails, client money calculations) | ✓ (regulatory requirements; regulatory bodies integration) | ✓ (E&O documentation posture; trust accounting) | ✓ (compliant financial records) | ✓ (compliance use case) | B — common, regional depth varies |
| Scheme/product building | ✓ (Product & Scheme Build) | ✓ (scheme capabilities) | — | — (MGA Systems is a separate product) | — | product/region-specific (UK) |
| Price-comparison-site trading | — | ✓ (major UK PC sites) | — | — | — | region-specific (UK personal lines) |
| Book roll / M&A machinery | — | — | ✓ (Book Rolls for Carriers resource) | ✓ (Book Roll product) | — | region-specific (US) |
| Comparative rating engine inside the family | ✓ (e-trade rating hubs) | ✓ (quotes/day stat) | ✓ (Rater integration) | ✓ (PL Rating / Commercial Submissions, separate products) | ✓ (core differentiator) | B — common, packaging varies |
| AI assistance | ✓ (AI module) | ✓ (agentic AI news) | — | ✓ (Email/Reconciliation agents) | ✓ (EVA) | B — common (recent) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being a broker/agency management platform:

```text
Client records (the intermediary's policyholders and prospects)
└── Policy/placement records
    │   each binding one client × one external insurer's product
    │   × defined terms (cover, premium) × a policy period
    └── Renewal-driven lifecycle
        (new business → in-force → mid-term change → renewal → cancel/lapse)
```

Three properties:

1. **Client records** — the firm's book is organized around named clients (individuals or businesses) who hold the policies.
2. **Policy/placement records referencing external insurers** — the central object is a record of a policy placed with an outside insurer for a client, for a defined term. The firm is an intermediary: the system manages the firm's book of placed business, not the master policy record (the insurer remains the risk carrier and master record holder). This is what makes the Type different from insurer-side policy administration.
3. **Renewal-driven lifecycle** — policies recur by period and must be renewed, adjusted mid-term, or allowed to lapse; the system's work is organized around this cycle.

Historical check: 1990s-era UK broker systems and DOS-era US agency systems had exactly client + policy + renewal structures (commission and downloads came with maturity), so the L0 does not over-fit the current market. Regional check: UK BMS and US AMS both satisfy it.

### L1 — Common Mature Structure

Present across the researched sample; expected in any mature product but not definitional:

- **Insurer/carrier panel management** — the set of insurers the firm places with, per line of business.
- **Quote & submission workflow** — capture risk data once, send to one or many insurers (rating hubs, comparative raters, carrier portals), compare, bind.
- **Carrier download / connectivity** — policy data, documents, endorsements, renewals (and sometimes claims) fed back from insurers into the policy records.
- **Commission tracking & reconciliation** — commission statements from insurers matched to policies; producer/agent commission splits.
- **Premium & client accounting** — client invoicing, premium collection, trust/client-money handling, bank reconciliation, ledger, month-end close; sometimes delegated to an external accounting package for operating accounting.
- **Document machinery** — generation of policy documents, schedules, certificates of insurance, proposal documents, letters from reusable templates; documents stored against the client/policy.
- **Task/workflow management with interaction logging** — renewal follow-ups, service tasks, alerts; every client interaction logged (E&O/compliance posture).
- **Sales/CRM layer** — leads, pipeline, cross-sell/upsell on the existing book.
- **Reporting/BI** — book of business, retention, production by insurer/producer, financial reports.
- **Client self-service** — portal/app with policy view, ID cards, certificate requests.
- **Claims logging** — claims recorded and linked to policies (full claims handling belongs to insurer-side systems).
- **Roles & permissions** — producers/account executives, account handlers/CSRs, accounting staff, administrators, management.

### L2 — Variant / Optional Structure

- **Regional regulatory machinery** — UK-style client money (statutory trust, client money calculations) and scheme regulation; US-style producer licensing, E&O documentation emphasis, premium finance.
- **Scheme/product building** — brokers/MGAs building their own branded products with delegated insurer authority (UK-flavored).
- **Price-comparison-site trading** — UK personal lines brokers transacting via aggregator sites.
- **Comparative rating depth** — standalone raters inside the family (US PL rating; UK e-trade panels).
- **Book roll / agency M&A machinery** — buying/selling books of business (US).
- **Lines focus** — personal lines vs commercial lines vs benefits vs life & health; wholesale brokerage variant (placing on behalf of retail brokers).
- **Network/franchise posture** — broker networks with shared panels/schemes.
- **Deployment shape** — desktop app + cloud data vs pure SaaS vs fully hosted/managed.
- **Suite posture** — standalone management system vs suite (rating, websites, licensing, document management) vs market-wide platform (broker + insurer + MGA on one network).
- **Client-facing digital journeys** — quote-and-buy portals, self-service depth.
- **AI assistance** — email triage, reconciliation matching, summarization.
- **Adviser variant** — financial advisers managing clients' policies (adjacent posture seen in one sample).

### L3 — Vendor-specific (kept out of the final document)

- Acturis: e-trade panel/extranet posture, £18.5bn UK premium stat, "8 of 10 top insurer extranets", Partners& case study.
- SSP: Keychoice, quotes-per-day stat, RAC/GT/Jigsaw case studies, ISO 27001.
- HawkSoft: Action Menu, HawkLink, Virtual Printer, Agency Intelligence™, Managed Accounting service, 97%/18-year stats, QuickBooks partnership specifics.
- Vertafore: AgencyOne, Velocity AI (Email Agent, Reconciliation Agent), TransactNOW, Book Roll, ImageRight, Sircon, InsurLink, RiskMatch, NetVU, "200+ carriers" reconciliation stat, 26% revenue-growth stat.
- EZLynx: EVA, Rating Engine™, "330+ carriers", "7M+ quotes/month", "25B+ total premium", Client Center, Applied Systems ownership.

## Vendor-specific Findings

See L3 above. Additionally:

- The **same vendor families span multiple directory leaves**: Vertafore sells MGA systems (AIM, MGA Systems, Surefyre) and carrier products (Sircon) as separate products — confirming that broker-side and insurer-side/MGA-side systems are distinct products even within one vendor. Acturis and SSP similarly sell separate insurer/MGA solutions. This supports the boundary vs Insurance Policy Administration System and Underwriting Workbench.
- HawkSoft's embedded-vs-integrated accounting essay shows the accounting boundary is a live design decision (trust/commission in-system vs operating accounting in an external package) — accounting depth varies legitimately within the Type.

## Boundary Findings

1. **vs Insurance Agency Management (sibling leaf, §08)** — The researched market does not support two distinct Types. US vendors call the category "agency management system"; UK vendors call it broker software / broker management system. Vertafore's own FAQ says the AMS is the hub for "agents, brokers, CSRs, and agency principals"; HawkSoft's page says it "keeps agents and brokers on task". Functionally both manage client + policy + carrier + commission + renewal. **Probable regional-naming alias/variant pair — flagged for joint review.** This document therefore treats "broker" and "agency" as one intermediary Type with naming variants, while keeping the broker framing (placement with multiple insurers, commission income) central.
2. **vs Insurance Policy Administration System** — Insurer-side: master policy record, premium accounting, one insurer's products, underwriting authority. Broker-side: book of placed business referencing many external insurers, commission income, no underwriting authority. Remove the multi-insurer intermediary posture and the commission layer → the system becomes (or hands over to) policy administration. Vendor evidence: the same vendors sell these as separate products for separate customers.
3. **vs Insurance Quote Platform** — Quote platforms produce quote transactions (comparative rating, quote-and-buy). The BMS/AMS holds the persistent book. Raters are commonly bundled into the family (EZLynx, Vertafore PL Rating, HawkSoft Rater, Acturis e-trade) but a rater alone is not a management platform: no book, no renewals, no commission ledger.
4. **vs CRM** — A BMS/AMS contains a CRM layer (leads, pipeline, cross-sell), but its center of gravity is the policy record and its money (premium/commission), not the relationship record. A CRM without policy/commission structures cannot run a brokerage.
5. **vs Underwriting Workbench / MGA systems** — Underwriting tools decide risks on behalf of an insurer with delegated authority; the broker system places risks across insurers without underwriting authority. Scheme-building (UK) is the closest approach and is recorded as an L2 variant.
6. **vs Insurance Claims Management** — Claims adjudication/management is insurer-side; broker systems log claims and link them to policies (one sample has a fuller claims module — recorded as common-to-optional, not core).
7. **vs Brokerage Platform (§08, securities) and Freight Brokerage Platform (§18)** — pure name collisions; different domains (securities trading; logistics). The insurance leaf is the intermediary back-office.
8. **vs Financial Advisor Platform** — one sample serves financial advisers managing clients' policies; adjacent posture (different regulatory context, advice-centric), not the same Type.

## Uncertainties

- No Tier-1 operational documentation (help centers/user guides) was reachable in this pass; all evidence is official product/marketing pages. Workflow details are therefore described at structure level, not step level; no exact state names, numeric limits, or default settings are asserted.
- Applied Epic — arguably the market's reference implementation for large agencies/brokers — could not be fetched (403 ×2). EZLynx (same parent) partially covers the vendor family, but Epic-specific structure is unverified.
- Open GI (UK) unreachable (timeout ×2); UK sample rests on Acturis + SSP product pages.
- The exact mechanics of UK client-money handling (trust account operation, calculations) are evidenced only at the level of "client money calculations" / "trust accounting" being named features; deeper mechanics not asserted.
- The directory's intent for this leaf (broker-side software vs insurer-side broker-network management) was resolved by placement context and market usage; if the taxonomy intended the insurer-side meaning, this document's framing would need revision (recorded as a boundary note rather than silently decided).

## Final Synthesis

A Broker Management Platform is the intermediary's operating system for general insurance distribution: it keeps the firm's **book of business** — clients, the policies placed for them with external insurers, and the money those placements generate — and drives that book through a **renewal-driven lifecycle**. Around this core, mature products add the placement workflow (quote → compare → bind), insurer connectivity (downloads, rating), commission reconciliation, premium/client accounting, document production, task/E&O logging, a sales layer, reporting, and client self-service. The US market names this category "agency management system" and the UK market "broker management system"; the researched evidence indicates one Application Type with regional naming and regional regulatory variants, not two Types. The Type is distinct from insurer-side policy administration (master record vs placed-book record), from quote platforms (persistent book vs quote transaction), and from CRM (policy/commission-centric vs relationship-centric).
