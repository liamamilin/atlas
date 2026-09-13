# Research Notes — Intellectual Property Management

## Research Goal

Understand what an Intellectual Property Management application (often "IPMS" — IP Management System) actually is as a software Type: its world model (objects), the work its users do (docketing, renewals, prosecution coordination, reporting), its lifecycle and rules, and its boundaries against the sibling leaves Patent Management, Patent Prosecution Management, Trademark Portfolio Management, Legal Matter Management, and Legal Docket Management.

## Initial Boundary

Initial hypothesis (before research):

- Core use: system of record for an organization's IP portfolio (patents, trademarks, designs, and sometimes copyrights, domains, licenses) with deadline/docket tracking, renewal/annuity handling, documents, parties, and reporting.
- Users: corporate IP departments, IP law firms, universities/tech-transfer offices.
- Nearest neighbors: Patent Management (patent-only scope), Trademark Portfolio Management (TM-only scope), Legal Matter Management (any-practice matters), Legal Docket Management (deadline layer), Contract Lifecycle Management (licenses).
- Unknowns: Is the Type's core actually "docketing software"? Is multi-asset-type coverage definitional? Where does invention-disclosure/innovation intake fit? Is renewal-fee machinery core or common?

## Research Questions

1. What is an "asset" / "matter" / "case" record in these systems? What data does it carry?
2. What exactly is docketing, and how does deadline machinery work (generation, calculation, tracking, closure)?
3. How are renewal/annuity fees handled — in-system or via services/associates?
4. Who are the users and how do roles differ between corporate and law-firm deployments?
5. How does work flow with foreign associates/agents and with clients?
6. What lifecycles/statuses do assets pass through?
7. How do office (PTO) data feeds enter the system, and what is their coverage?
8. What reporting/finance/budget capabilities exist at the corporate pole vs the firm pole?
9. What distinguishes this Type from generic legal matter management and from patent/trademark-only specialist systems?
10. Would older / non-cloud / regional products still fit the definition (historical check)?

## Representative Products

| Product | Vendor | Pole | Why selected |
|---|---|---|---|
| AQX Corporate (+ PATTSY WAVE family context) | Anaqua | Enterprise corporate suite | Largest corporate-side IPMS philosophy; suite with innovation intake, portfolio, product-centered IP |
| IPfolio | Clarivate | Corporate platform (Salesforce-based) | Corporate team of all sizes; asset breadth incl. domains/copyrights; country-laws deadline engine |
| FoundationIP | Clarivate (ex-CPA Global) | Law-firm cloud docketing/practice management | Firm-side workhorse; explicit docketing, forms, IDS, renewals, family tree |
| DIAMS Infinity (+ Simple IP / DIAMS iQ context) | Dennemeyer | Corporate/legacy-heritage IPMS, services-entangled vendor | Continental-European heritage; PTO connectivity, data audit, AI assistant; free-tier pole (Simple IP) |
| Prosecution Manager / PM Corporate / Invention Manager / Tandem | AppColl | SMB/lightweight US firm + corporate modules | Small-practice pole; fully public Tier-1 help-center manual; module structure explicit |

Product Mismatch note: "Equinox" (equinoxip.com) was investigated as a candidate mid-market sample but proved to be a Montreal IP law firm, not an IP management software vendor. Dropped; no software evidence taken from it. Attempted Clarivate root paths (clarivate.com/en/ip-management-software/foundationip, ip.clarivate.com) failed (404/transport) before the correct paths were found.

## Sources

Research date: 2026-09-07. All fetches successful unless noted.

1. Anaqua — corporate site: https://www.anaqua.com/ (fetched 2026-09-07)
2. Anaqua — AQX Corporate product page: https://www.anaqua.com/aqx-corporate/ (fetched 2026-09-07)
3. Clarivate — IPfolio product page: https://clarivate.com/intellectual-property/ip-management-software/ipfolio/ (reached via ipfolio.com redirect; fetched 2026-09-07)
4. Clarivate — FoundationIP product page: https://clarivate.com/intellectual-property/ip-management-software/foundationip/ (fetched 2026-09-07)
5. Clarivate — IP Management Software family nav (IPfolio, Unycom, Memotech, The IP Management System, Ipendo / FoundationIP, Inprotech, Patrawin / Forecast, First to File, Docket): visible across 3–4 (fetched 2026-09-07)
6. Dennemeyer — corporate site: https://www.dennemeyer.com/ (fetched 2026-09-07)
7. Dennemeyer — DIAMS Infinity product page: https://www.dennemeyer.com/diams-infinity (fetched 2026-09-07)
8. Dennemeyer — "Your comprehensive guide to IP docketing" (vendor educational article): https://www.dennemeyer.com/blog/posts/the-top-10-rules-of-intellectual-property-docketing (fetched 2026-09-07)
9. AppColl — corporate site: https://www.appcoll.com/ (fetched 2026-09-07)
10. AppColl — Help Center: https://support.appcoll.com (fetched 2026-09-07)
11. AppColl — Prosecution Manager Overview Manual (Tier-1 operational documentation): https://support.appcoll.com/en_US/general-information/appcoll-overview-manual (fetched 2026-09-07)

Source-access limitations: Anaqua (ACE help center), Clarivate (CPA Global Workbench / in-product help) and Dennemeyer in-product documentation sit behind client logins; reachable evidence is vendor product/marketing pages plus AppColl's public operational manual. Marketing claims with precise numbers (e.g., "law updates 3x a year covering 300+ jurisdictions", "150+ managed USPTO forms", "over 100 system reports", DIAMS ROI claims like "100+ hours saved monthly for a team of five") are recorded here as vendor claims only and were NOT promoted into the final document.

## Product Observations

### Anaqua (AQX Corporate; PATTSY WAVE; ideaPoint)

Evidence layer A = direct observation of vendor pages; interpretation tagged where needed.

- Positions itself as "Intellectual Property Management Software"; AQX described as "IP Management Platform" and "Patent & Trademark Management Software". [A]
- AQX Corporate capability map (as marketed): Patent Management ("entire patent lifecycle"), Trademark Management ("search and clearance processes, global insights, infringement tracking"), Innovation Management ("ideation process … move seamlessly into IP protection"), IP Operations ("automated docketing, streamline collaboration, manage large volumes of emails and documents"), Portfolio Management ("classify and organize your IP assets … from a variety of perspectives"), Product-Centered IP ("relationships between IP assets and Products"), plus supporting features: Financial Management, Document Management, Reporting & Analytics, Security & Hosting, Application Integration. [A]
- Segmented deployment surfaces: AQX Corporate / AQX Law Firm / AQX Pharma / PATTSY WAVE (described as patent-and-trademark docketing with dashboards/analytics). [A]
- Services bundled alongside software: Patent Annuity & Trademark Renewal Services, Foreign Filing Services, Docketing and Administrative Services, Data Validation and Portfolio Onboarding, Patent Search Services. [A] — Evidence that portfolio onboarding/data validation and annuity payment are recognized workloads around this Type (delivered here as services, not necessarily in-software).
- ideaPoint / Innovation Management = corporate invention-disclosure intake feeding IP protection. [A]
- Client logos: large corporates (Xerox, GSK, Volvo, Ford, etc.) and law firms. [A]
- Customer testimonial (Novo Nordisk VP Corporate Patents) describes moving "from our current in-house system to a new generation of patent management software … efficient workplace for professionals in our global patent organization". [A] — the incumbent pattern (in-house system) is part of the market story.

### Clarivate IPfolio (corporate)

- Self-description: "premier Clarivate cloud-based IP management platform, tailored for corporate IP teams of all sizes"; built on the Salesforce platform. [A]
- Centralized hub: "Access everything in one place – inventions, patents, trademarks, domain names, and copyrights." [A] — asset-type breadth beyond patents/trademarks is a marketing claim; treat breadth as variant.
- Automation claims: "Automate reports, due date calculations, issue awards, task-based assignments." [A]
- Deadline engine: "Never miss a due date, IPfolio is powered by an extensive country laws engine that monitors and automatically calculates dates and deadlines." [A]
- Data quality: "Integrated Clarivate IP data provides automated data verification and enrichment" and FAQ: "automated data verification and enrichment … allow seamless auto-docketing." [A]
- Analytics/reporting: "real-time decision support with embedded analytics … custom reports and dashboards." [A]
- Integrations: Clarivate software/services and third-party tools (Innography analytics named). [A]

### Clarivate FoundationIP (law firm)

- Self-description: "Cloud based IP practice management for high-performing law firms of all sizes"; claims heritage as "the first cloud-based IP Management software in the market". [A]
- Scope: "Manage patents, trademarks, copyrights and more all in one place. Easily configure … based on client, attorney, office or team." [A]
- Docketing/task machinery (FAQ, Tier-1-adjacent): "one-click docketing from USPTO Private PAIR, docket directly from an e-mail … create internal tasks, automatically launch tasks in related families, leverage conditional logic … search for assigned tasks, view tasks on dashboard, automate task reports, and receive email reminders." [A]
- Deadline law maintenance (vendor claim, precision withheld from final doc): "automatic law updates and recalculations 3x a year, covering 300+ jurisdictions." [A→vendor claim]
- Family/prosecution structure: "Automatically track priority lineage, terminal disclaimers, and visualize relationships with the family tree view." [A]
- Forms & IDS: "150+ managed USPTO forms and over 100 system reports" (vendor claim); "Import hundreds of references … automatically flow to related matters, and generate forms with end-to-end IDS Management." [A→vendor claim for counts]
- Renewals: "Easily manage patent renewals — process patent renewals payment decisions for clients, automatically close and launch renewal dates, and more." [A] — the renewal decision loop is explicit in-software.
- Client access: "you can enable direct client access to information, reducing burden on attorneys and staff." [A]
- Agent coordination: "Send multiple agent instructions at once from a single collaboration portal fully integrated with FoundationIP … check the status of agent activity in seconds" (IP Collaboration Hub). [A]
- Companion products in the family: First to File ("document management designed specifically for the IP industry"), Forecast ("advanced IP cost forecasting"), Docket. [A]

### Dennemeyer (DIAMS Infinity; Simple IP; DIAMS iQ; Octimine; services)

- DIAMS Infinity self-description: "Next-generation IPMS for smarter, faster IP operations"; "AI-native IP asset platform"; FAQ: "Rather than acting as a passive record repository, it actively supports daily IP management." [A]
- Routine-workflow core: "Optimizes routine workflows such as docketing, deadline tracking and task management." [A]
- Data quality via office connectivity: "Direct connectivity to PTO databases ensures high-quality and continuously updated records … data audit feature"; "Automatic checks against patent and trademark office (PTO) records keep your data clean." [A]
- Deadline law: "Country law-aware calculations keep deadlines and procedural rules precise, replacing manual computations with dependable, jurisdiction-specific logic." [A]
- Centralized hub: "All your IP operations centralized, from tasks to matters and documents." [A] — matters/tasks/documents triad explicitly named.
- Collaboration/permissions: "Unlimited guest-user spots … external counsel"; "Interactive, customizable dashboards"; "user management controls simplify access and permissions." [A]
- AI assistant "with full portfolio knowledge" for retrieval; AI natural-language search. [A]
- Product family: Simple IP ("free solution that does not compromise on functionality"), DIAMS iQ (legacy generation), Octimine (AI search), Dennemeyer API. [A]
- Services side: Managed IP = Patent Renewals / Trademark Renewals / IP Support services (docketing services); IP law firm = filing/prosecution/defense services. [A] — same workload (renewals, docketing) sellable as human services, evidence that software + service both carry the same operational loop.
- Scope statement (vendor blog): "IP portfolios can span multiple jurisdictions, legal frameworks and business priorities. They may include patents, trademarks, designs and a range of adjacent matters such as licenses, oppositions, agreements, domain names and other rights that require careful tracking and coordination." [A] — best single vendor statement of asset-type breadth.
- Docketing definition (vendor educational article): "docketing involves the methodical collection, organization and management of data … the methodical management of essential data, deadlines and documentation from registering offices"; "An effective docketing system minimizes the risk of losing valuable IP rights due to missed deadlines or other administrative oversights. It is also instrumental in handling those deadlines … the system acts as an ongoing audit of your adherence to the law." [A]
- Operational rules from the same article: docket from official documents not internal emails; never close a hard deadline without proof; keep an open (status-check) deadline for all active applications; do not inactivate a record without explicit client instructions; notes carry "who, what, when, why". [A] — these are practice rules, useful for the final doc's "rules" section in vendor-neutral form (they are discipline norms, not one vendor's invention — but sourced from a single vendor's guide; mark accordingly).
- Docketing specialist role named: "a role that goes far beyond data entry … responsible for … managing complex portfolios and ensuring that nothing is overlooked." [A]
- Modern docketing feature list (same article): centralized document repository, custom reporting, pre-filled emails/letters to clients, read-only access for transparency, auto-generated intake forms for client onboarding. [A]

### AppColl (Prosecution Manager Pro/Plus; PM Corporate; Invention Manager; Tandem)

- Self-description: "cloud-based intellectual property management system" with "distinct and integrated modules": Tasks, Matters, Prior Art, Files, Billing, Reports, Conflicts, Contacts, Tandem (overview manual). Help-center categories add Trademarks, Finances, Signatures, eOffice Actions, Invention Manager, AI. [A]
- **Task (docket) model (Tier-1):** "The main purpose of the Tasks module is to show your active docket, using 'tasks.' A task is either a) something someone needs to complete … or b) a record of an event … All tasks have a status … If the status is 'Open,' work needs to be done … the status of the task 'Respond to Final Office Action – 2 Month Deadline' may be 'Missed' … Tasks are normally associated with matters … Tasks are usually generated automatically in response to data changing in the system, either through manual changes … when data is imported via an XML file or spreadsheet, or when another task changes status." Plus task types with rules, owners, reassignment, bulk close, notifications (mail-merge emails at status change). [A]
- **Matter model (Tier-1):** "A matter is something associated with a set of tasks and billed separately to one client. Examples would be patent or trademark applications, invention disclosures, litigation cases, licensing agreements, and copyright filings." Unique "Attorney Ref" identifier; roles Attorney/Partner/Paralegal/Contributor; attorney default owner of tasks; status lifecycle "Unfiled, Pending, Published, Issued, Expired" (patent example); family connections ("priority connections … affect the priority date"; relations inferred transitively); bibliographic data imported from USPTO Patent Center/TSDR XML ("Foreign patent and trademark matters must be imported from spreadsheets or manually entered since there are no public databases where AppColl can retrieve this information"); trademarks "updated automatically every 7 days" [A→vendor claim]; parties page (Applicants, Assignees, Licensees, Adverse Parties); patent matters carry Abstract & Claims. [A]
- **Prior Art / IDS module:** database of references stored once and linked to all citing family matters; IDSCount/RefCount/CiteCount columns; generates USPTO SB08A; auto cross-citing to related un-issued US matters. [A]
- **Files:** cloud document store, auto folders per client/matter, revisions never overwritten, docs attachable to tasks. [A]
- **Billing:** billing items (fees, flat fees, expenses, payments, write-offs, adjustments, retainers) → invoices by date window; LEDES e-invoice auto-generated; sent invoices locked; timer for time entry; corporations can "track spending on individual matters by importing invoice and spending data generated outside the system … particularly useful for corporations using outside counsel." [A]
- **Reports:** saved views = saved queries; scheduled report runs emailed/FTP'd; "account activity log of all information changed in the system, including who changed the information and when." [A]
- **Contacts:** all people/firms/corporations with roles defining usage (Patent Attorney, Law Firm, Employee, Docketing Manager, Manager, Paralegal, Account Administrator); admin sets permissions; duplicate contact merge. [A]
- **Tandem:** free portal for the firm's corporate client — "controlled copy of their own IP portfolio information", auto-synced from the firm's account, scope controlled by the attorney. [A]
- **PM Corporate:** "centralizes your portfolio and prosecution … across tasks, matters, prior art, files, contacts, reports, and finances. The Finances module allows you to set budgets, track legal spend, streamline invoice review with configurable approval flows, and forecast future expenses." [A]
- **Invention Manager:** inventors submit disclosures, attach documents, track status; patent committee view. [A]
- **eOffice Actions** (PM Plus/Corporate): processing of electronic office actions. [A]
- Positioning: "Take control of your Matters Tasks Contacts Prior Art Invoices Finances Documents Workflows Files." CSV import/export on every module. No long-term contracts, subscription monthly. [A]

## Cross-product Comparison

| Dimension | Anaqua AQX | Clarivate IPfolio | Clarivate FoundationIP | Dennemeyer DIAMS | AppColl PM |
|---|---|---|---|---|---|
| Asset records (matters/cases) | yes — patent + trademark lifecycle modules; portfolio organization | yes — "inventions, patents, trademarks, domain names, copyrights" | yes — "patents, trademarks, copyrights and more" | yes — "tasks to matters and documents" | yes — matters incl. patent/TM applications, disclosures, litigation, licensing, copyright |
| Deadline/docket tracking | "automated docketing" | due-date engine ("country laws engine") | one-click docketing, task dashboards, reminders | "docketing, deadline tracking and task management" | explicit task/docket module with statuses incl. missed |
| Law-aware deadline calculation | implied (platform) | yes (country laws engine) | yes (vendor claims periodic recalculation across many jurisdictions) | yes ("country law-aware calculations") | rule-driven task types + office XML imports (calculation depth not fully documented) |
| Renewal/annuity machinery | in financial mgmt + annuity services | via Clarivate services | in-system renewal payment decisions + date automation | in-system + Managed IP renewals services | billing items per matter (firm billing; not annuity-payment engine) |
| Family/priority relations | portfolio relationships | data enrichment | priority lineage, terminal disclaimers, family tree | portfolio knowledge | priority connections, transitive related matters |
| Documents | document management module | integrations | First to File companion; doc automation | centralized documents | Files module with revisions |
| Parties/contacts | collaboration | inventors/outside counsel collaboration | client/attorney/office/team config | guest users for external counsel | Contacts module with roles; assignees/licensees/adverse parties |
| Reporting | reporting & analytics | analytics/dashboards | report builder + templates | dashboards | saved queries, scheduled reports, account activity log |
| Office (PTO) data feeds | not documented publicly | "auto-docketing" via Clarivate data | one-click from USPTO Private PAIR | live PTO checks | Patent Center/TSDR XML; foreign via spreadsheets |
| Client/external portal | not documented publicly | integrations | direct client access | unlimited guest users | Tandem client portal |
| Invention disclosure intake | ideaPoint / Innovation Mgmt | inventions in hub | not surfaced | not surfaced | Invention Manager |
| Outside-counsel spend mgmt | financial management | — | — | — | PM Corporate Finances (budgets, invoice approval, forecast) |
| Firm billing | AQX Law Firm | — | practice mgmt incl. billing surfaces | — | Billing module with LEDES |
| Permissions/audit | security & hosting | Salesforce platform security | role-based configuration | user management/permissions | roles + Account Administrator + activity log |

Reading: the matter/asset record, the docket/deadline layer, and lifecycle status are present in every product. Office connectivity, portals, disclosure intake, and spend management are common-but-not-universal. Precision marketing numbers appear in several products and were withheld from the canonical layer.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an IP Management application:

```text
IP Asset Record (one identified right in one jurisdiction:
        bibliographic identity + parties + current legal status)
└── Deadline / Docket Tracking (time-bound obligations tied to the record,
        tracked to completion with visible state)
└── Recorded Lifecycle Progression (status changes / event history
        accumulating over the life of the right)
```

Three properties:

1. **IP asset record.** A persistent, identified record for each registered right (patent, trademark, etc.) in each jurisdiction, carrying bibliographic identity, parties, and current status. Without it there is no portfolio and the product is not an IPMS.
2. **Deadline/docket tracking on those records.** Time-bound obligations (office-action response windows, renewal/maintenance fees) surfaced and tracked to completion. This is the load-bearing discipline of the domain: missed deadlines can extinguish rights. Without it, the product is merely a legal database or document store.
3. **Recorded lifecycle progression.** The record accumulates events/status changes from filing through grant/registration, maintenance, and expiry/abandonment, so the record reflects where each right stands. Without it there is no "management", only snapshots.

Multi-asset-type breadth (patents + trademarks + designs + domains + licenses) is **not** L0: patent-only and trademark-only systems satisfy all three properties and are recognized members of this market (the directory's sibling leaves exist for exactly that scope difference). Cloud delivery, PTO connectivity, fee calculation engines, portals, AI are all absent from L0 — a paper docket book per asset with renewal reminder cards (the pre-software practice this digitized) satisfies the invariant.

Historical / market-sample check: pre-cloud and pre-digital practice (paper docket cards, renewal reminder files, in-house spreadsheets) satisfies all three properties. Desktop-era IPMS products and today's free tiers (Simple IP) satisfy them. The definition is not over-fitted to the modern cloud+PTO-feed pattern.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products; not definitional:

- **Matter/case as the working unit** binding tasks, documents, parties, and (where present) billing to the asset record — explicit in AppColl ("matter … associated with a set of tasks and billed separately"), named in DIAMS ("tasks to matters and documents"), configured by client/attorney/office in FoundationIP.
- **Task system with types, owners, states, reminders** — open/closed states, missed-deadline visibility, automatic generation from data events, notifications. (AppColl Tier-1; FoundationIP; DIAMS.)
- **Multi-jurisdiction portfolio view with family/priority relations** — parent/child and priority-lineage structures, family tree / transitive relations.
- **Renewal/annuity management** — surfacing renewal dates ahead of time, pay/abandon decision support, fee handling (in-system to varying depths), often entangled with outsourced renewal-payment services.
- **Document management** — office communications, certificates, filings stored per matter/task, with revision discipline.
- **Party/contact model with roles** — clients/assignees, inventors, attorneys, paralegals, docketing staff, foreign associates/agents.
- **Reporting/dashboards** — deadline reports, portfolio status, cost reports; scheduled/deliverable outputs.
- **Bulk data import/onboarding and validation** — spreadsheets/XML; the entire "portfolio migration" workload (vendors sell data-validation/onboarding services for it).
- **Permissions and audit** — role-based access; change logs recording who changed what and when.
- **Outbound communications** — reminders, form letters/emails, status notifications.

### L2 — Variant / Optional Structure

Depends on segment, geography, era, deployment:

- **Direct PTO/office connectivity** (live checks, auto-import from office systems) — common in current cloud products but depth and office coverage vary by jurisdiction; foreign matters often still arrive by spreadsheet.
- **Invention-disclosure / innovation intake** (corporate pole front-end feeding filing decisions).
- **Client / stakeholder portals and guest access** (read-only views, client-visible portfolio copies).
- **Outside-counsel spend management** (budgets, invoice review/approval flows, spend forecasting — corporate pole) and **firm billing** (billing items → invoices, legal e-invoicing formats — firm pole). The two poles allocate the same financial workload differently.
- **Prior-art / IDS management** as a dedicated module (patent-heavy firms).
- **IP search/analytics integration** (patent search, competitive analytics) — usually a companion product.
- **Cost forecasting**; **licensing/agreement and domain-name tracking** as adjacent records; **brand-protection/watch integration**; **AI assistants** for retrieval and data audit; **e-signature and e-filing integrations**; **free tiers** as market-entry packaging.

### L3 — Vendor-specific Structure

(Research notes only — none of this enters the final document.)

- AppColl: Tandem free client-portal concept; "Attorney Ref" as the unique matter key; named statuses "Missed"/"Unfiled/Pending/Published/Issued/Expired"; trademark records auto-refreshed on a fixed 7-day cycle; automatic LEDES invoice generation; billing Timer.
- Clarivate FoundationIP: "one-click docketing from USPTO Private PAIR"; family tree view; terminal-disclaimer tracking; vendor claims of law updates 3×/year across 300+ jurisdictions; 150+ USPTO forms / 100+ reports claims.
- Clarivate IPfolio: built on the Salesforce platform; Clarivate-data enrichment/auto-docketing bundling.
- Dennemeyer: DIAMS family naming (iQ/Infinity/Simple IP), AI assistant "with full portfolio knowledge", unlimited guest users, ROI calculator marketing, the "10 rules of docketing" pedagogy.
- Anaqua: AQX edition ladder (Corporate/Law Firm/Pharma), PATTSY WAVE heritage brand, Product-Centered IP (asset↔product mapping), HyperView dashboards, ideaPoint.

## Rejected Findings

- **"IPMS = docketing software."** Rejected as the definition: docketing is the deadline layer inside the Type; products also carry the asset system of record, renewals, documents, and reporting. Several sampled vendors position docketing as one workflow among several.
- **"Multi-asset breadth is definitional."** Rejected: patent-only and trademark-only systems are structurally identical; breadth is a scope variant (see Boundary Findings).
- **"Office/PTO connectivity is definitional."** Rejected: it is a modern common implementation of data quality; AppColl documents that foreign matters have no retrievable public data and arrive by spreadsheet/manual entry; older systems ran without any feed.
- **"Renewal-fee payment execution is definitional."** Rejected: the decision/tracking loop is common, but payment execution is frequently outsourced to renewal services or foreign associates; a system that tracks renewal deadlines and decisions without paying fees is still fully an IPMS.
- **"AI / analytics / dashboards are core."** Rejected: L2; marketing-forward in 2026 but historically absent.
- **"Billing is core."** Rejected: only the firm pole invoices from the system; the corporate pole may only track spend; some deployments do neither.

## Boundary Findings

- **vs Patent Management / Trademark Portfolio Management (directory siblings).** These leaves share the identical L0 (asset record + deadline tracking + lifecycle); the difference is asset-type scope and (for prosecution-focused products) the depth of the filing/prosecution workflow. Evidence: AppColl's single system handles patent *and* trademark matters in one module set; FoundationIP manages "patents, trademarks, copyrights and more"; Anaqua splits Patent Management and Trademark Management as *modules of one platform*, not separate products. **Test:** remove trademark handling from an IPMS → a patent management system (still the same core). Remove deadline tracking from either → no longer this Type. **Recommendation:** treat Patent Management / Trademark Portfolio Management as scope-specialized realizations of the same core when those leaves are processed; joint review recommended.
- **vs Patent Prosecution Management.** Prosecution management emphasizes the active legal workflow of obtaining the right (drafting, filing, office-action responses) typically on the firm side; IP Management as documented here is the ongoing system of record over the whole portfolio life. Products blur this (AppColl self-titles "Prosecution Manager" yet functions as an IPMS). Same-family joint review recommended.
- **vs Legal Matter Management.** A generic matter-management system holds case records with tasks and documents for any practice area. **Test:** remove IP-specific deadline law (renewals/annuities, jurisdiction-aware response windows), family/priority relations, and renewal machinery, and generalize the matter types → Legal Matter Management. The IP-specific legal-time dimension is the seam.
- **vs Legal Docket Management.** Docket management is the deadline layer alone (as Dennemeyer's guide describes it); IP Management is the full asset system of record of which docketing is one discipline. A standalone docketing product without the asset/portfolio system of record is the narrower Type.
- **vs Contract Lifecycle Management.** Licenses/agreements can be tracked inside an IPMS as records attached to the portfolio, but the contract (not the right) is CLM's object of record, with its own lifecycle (authoring, negotiation, execution, obligations).
- **vs IP search & analytics platforms** (not separate directory leaves here, but adjacent market: Derwent, AcclaimIP, Octimine, Innography). Those operate over the world's patent corpus for search/analysis; the IPMS is the system of record for *your own* rights and deadlines. Integration between the two is common (L2).
- **vs Renewal Management Platform (directory leaf in §07/§08 space).** Name collision only: SaaS "renewal management" renews customer subscriptions; IP renewals pay government fees to keep rights alive. Different users, objects, and money paths. No relationship beyond the word.

## Uncertainties

1. **Deadline-calculation depth in lightweight products.** AppColl's public manual documents rule-driven task types and office XML imports but not the full depth of jurisdiction-law date calculation; FoundationIP and DIAMS market law engines. The final document therefore says "mature products commonly calculate deadlines from maintained jurisdiction rules" without asserting uniform depth.
2. **In-system renewal-fee payment vs service-mediated payment.** Vendors sell both; the exact split inside each product's software (vs its services arm) is not fully visible from public pages. Kept qualified.
3. **Office-feed coverage by jurisdiction.** AppColl states USPTO feeds and spreadsheet-based foreign data; other vendors claim broader connectivity. Coverage breadth per office was not independently verified.
4. **University/tech-transfer deployments.** Known market segment but not directly evidenced in the sampled official pages; left as a probable variant rather than an assertion.
5. **Conflicts module** (AppColl lists it in the module set) — depth not researched; conflicts-checking workflows may matter for firm deployments.

## Final Synthesis

An Intellectual Property Management application is the **system of record for a portfolio of registered IP rights**: one identified record per right per jurisdiction; a docket/deadline layer that surfaces and tracks every time-bound obligation attached to those records (because a missed deadline can extinguish a right); and an accumulating lifecycle history that keeps each record aligned with where the right actually stands in the legal world. Around that invariant, mature products add the matter-as-working-unit, task machinery, multi-jurisdiction family/priority structures, renewal/annuity handling, documents, role-modeled parties, reporting, bulk onboarding, permissions and audit; variants add office connectivity, disclosure intake, portals, spend/billing, analytics, and AI. The market splits along an operator axis (corporate IP departments vs IP law firms — the same workloads reappear as "spend management" on one side and "billing" on the other) and a scope axis (patent-only / trademark-only / broad portfolio). The nearest in-family boundaries are the patent/trademark-specialist siblings (scope difference, same core), and the nearest out-of-family boundaries are generic legal matter management (no IP legal-time dimension) and standalone docketing (deadline layer without the asset system of record).
