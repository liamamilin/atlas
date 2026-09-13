# Research Notes — Email Authentication / DMARC Management

## Research Goal

Understand what an Email Authentication / DMARC Management application actually is as a software Type: its defining structure, its users, its object model, its operating loop, and its boundaries against adjacent security/email Types. The directory leaf sits in §15 Cybersecurity, Identity & Trust as "Email Authentication / DMARC Management".

## Initial Boundary

Working hypothesis at start:

- This is domain-owner-side software for managing the organization's own email-domain identity — publishing and maintaining SPF/DKIM/DMARC records in DNS, collecting and interpreting DMARC reports from receiving mail systems, inventorying senders who claim the domain, and advancing the domain's DMARC policy to enforcement.
- Adjacent Types to watch:
  - **Email Security Gateway** — inbound threat filtering; opposite side of the mail flow.
  - **Digital Risk Protection** — broader external footprint (lookalike domains, fake profiles) with takedown workflows.
  - **Email Infrastructure Management** — sending infrastructure, not identity policy.
  - **DNS Management** — operates zones; this Type only authors authentication records into DNS.
  - **Deliverability/reputation monitoring** — measures sender reputation; adjacent not identical.
  - **Certificate Lifecycle Management / PKI** — different trust machinery (certificates vs DNS TXT records); notable that one sampled vendor (Valimail) was acquired by DigiCert (a PKI company) in 2025.

## Research Questions

1. What is the core object model? (domain, DNS records, reports, senders/sources, policy)
2. What is the canonical operating loop? (onboard domain → publish records → receive reports → inventory senders → align → enforce → maintain)
3. What exactly is being "managed" — and what does the product NOT touch (mail flow itself? mailboxes? inbound filtering?)
4. Who are the users and what drives adoption (compliance, anti-phishing, deliverability, mailbox-provider mandates)?
5. What are the interfaces (dashboards, report explorers, record wizards, alerts)?
6. Which rules constrain the work (alignment semantics, policy ladder, receiver-side enforcement, DNS as source of truth)?
7. Where is the thin edge (monitoring-only tools) and where is the suite drift (email security bundles)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer layer:

| Product | Philosophy / Layer | Evidence level |
|---|---|---|
| dmarcian | Pure-play pioneer (founded 2012 by a DMARC spec co-author); analytics/journey-led; individuals → enterprises → MSPs | A — root, platform module pages, "Moving through DMARC" + "Advancing Your DMARC policy" docs |
| EasyDMARC | Self-serve SMB→enterprise; all-in-one outbound email security + deliverability positioning; strong compliance framing | A — root + "Understanding and Analyzing DMARC Reports" knowledge article |
| Valimail | Automation/enforcement-first enterprise; Monitor (free) → Enforce → Amplify (BIMI); DigiCert-owned; FedRAMP-certified | A — root + Monitor product page |
| Postmark DMARC / DMARC Digests | Sender/developer-side thin tool from an email-delivery vendor; free weekly digest + paid tier | A — tool site root with full setup flow and tier comparison |

Secondary (named, not directly researched this pass): Proofpoint Email Fraud Defense, Fortra (Agari), Mimecast, Barracuda, Cisco, PowerDMARC, Red Sift, MxToolbox — the pure-play vs email-security-suite landscape is attested via Valimail's own comparison table and EasyDMARC's compliance pages, held at evidence layer B/C.

## Sources

Fetched 2026-09-08 (all successful, evidence layer A):

- dmarcian — https://dmarcian.com/ (root + platform module nav: Domain Overview, Detail Viewer, Source Viewer/email-source-identification, Alert Central, free tools list, mandates page)
- dmarcian — https://dmarcian.com/moving-through-dmarc/ (journey framing: getting started → advancing policy → life after reject)
- dmarcian — https://dmarcian.com/advancing-dmarc-policy/ (policy ladder semantics, alignment, compliance-rate guidance, pct tag, maintenance list)
- EasyDMARC — https://easydmarc.com/ (root: product lines, full tool inventory, compliance/mandate table, MSP programs, managed services)
- EasyDMARC — https://easydmarc.com/blog/understanding-dmarc-reports/ (aggregate vs failure reports, report field anatomy, analysis workflow, four-tab categorization)
- Valimail — https://www.valimail.com/ (root: Monitor/Enforce/Amplify, comparison table, use cases, partnership claims)
- Valimail — https://www.valimail.com/products/monitor/ (monitoring mechanics: sender identification, enforcement status, suspicious IPs)
- Postmark — https://dmarc.postmarkapp.com/ (free digest tool: complete onboarding flow, tier comparison, feature list)

## Product Observations

### dmarcian

Key observations (A):

- Self-description: "Control Your Domain. Secure Your Email." Founded 2012 by "a primary author of DMARC"; "first company dedicated to DMARC"; mission-driven ("DMARC Everywhere").
- Problem framing: "Email was invented… with a lack of built-in identity. By default, anyone can send email pretending to be someone else." DMARC "gives Internet domain owners control over how their domains can be used in email."
- Product = "DMARC Management Platform" with named modules: **Domain Overview**, **Detail Viewer**, **Source Viewer** ("email source identification"), **Alert Central**.
- Free tools: DMARC Domain Checker, DMARC Inspector, **DMARC Record Wizard**, **SPF Surveyor**, DKIM Inspector, DKIM Validator, BIMI tools, **XML to Human Converter** (their origin story tool), DMARC Data Providers.
- The DMARC journey is explicit: Getting started with DMARC → Getting started with dmarcian → Advancing Your DMARC Policy → **Life After Reject** (maintenance phase).
- Policy doctrine (from "Advancing Your DMARC policy"): three policy modes **none / quarantine / reject**, "most traditionally applied in the sequence listed above"; parked/retired domains may start at reject. p=none = "zero protection but affords you the same visibility"; quarantine = receiver accepts but downgrades to spam/quarantine; reject = "outright block", 5XX hard bounce generated.
- **Alignment** defined: "the relationship between the domain in the From Header address and the domains associated with SPF and DKIM records… Only emails that are aligned can pass DMARC."
- Progression guidance: "minimum of four weeks of data" before advancing; advance per-domain when compliance rate ≥ ~98%; **pct tag** for staged rollout (default 100%, 1–100% range; not to be used with p=none; being replaced by the `t` testing-mode tag in the new DMARC RFC).
- Enforcement is receiver-observed: "No notifications are sent to the senders; only the receivers will notice" (quarantine); rejection events appear in DMARC data; the platform tracks quarantine/reject rates in Detail Viewer.
- Maintenance ("Life after Reject"): periodic SPF record checks (against **over-authentication**), approval workflow for SPF changes + alerts on unexpected changes, **DKIM key rotation** monitoring, periodic DMARC data checks for new legitimate sources, configured reporting, internal incident management.
- Audience: individuals & small businesses, organizations & enterprises, **MSPs & IT agencies**; verticals: education, financial services, government, healthcare, NGO, nonprofit, technology, utilities. Multi-domain language: "deploy it across your email domain catalog"; "Deployment Issues: Trouble deploying DMARC across hundreds of domains or even just one".
- Drivers named on homepage: confusion about who sends on your behalf, **compliance** (cyber insurance), fraud ("Customers getting fake emails that are not from you asking for payment"), reputation (spam folder), deployment issues.
- Services wrap: DMARC Deployment, Onboarding, Support, Consultation, Dedicated Support ("manage DMARC-related incidents, editorialize data reviews, embed DMARC into daily operations"); partner/MSP program.
- Vendor claim (not asserted in final doc): "only 30% of organizations who start the process of deploying DMARC ever finish."

### EasyDMARC

Key observations (A):

- Positioning (V3): "One platform for email security, delivery, and governance." Product lines: **EasyDMARC** (outbound email security / DMARC), **EasySender** (deliverability — separate product line), **Touchpoint** (MSP lead generation), MSP program.
- Full tool inventory (free tools): DMARC record checker/generator, **Managed DMARC**, SPF lookup/generator/raw-check, **EasySPF**, DKIM checker/generator, BIMI checker/generator/converter, **Managed BIMI**, **MTA-STS** checker/generator + managed MTA-STS/TLS reporting, TLS-RPT checker/generator, **DMARC Failure Reports**, **DMARC XML Report Analyzer**, report GeoMaps, Domain Scanner, DNS Record Checker, Phishing Link Checker, **Reputation Monitoring**, **Alert Manager**, email deliverability test, email verification, email header analyzer, reputation check.
- **EasySPF**: "simplifies SPF setup and management with a one-time DNS configuration… automatically update it to reflect any changes. EasySPF eliminates issues like the 10 DNS lookup limit by dynamically flattening the record, converting domain includes into IP addresses."
- **Managed DKIM**: "centralizing DKIM record management for multiple domains… automates selector detection."
- **Reputation Monitoring**: tracks domains/IPs against blacklists with real-time checks and email alerts.
- **Managed Services**: "white-glove solution provides a safe and comprehensive setup and management of DMARC, SPF, and DKIM. From configuration to enforcement… A dedicated DMARC Engineer supports you."
- Report mechanics (from the reports article): DMARC reports received by publishing a DMARC record with **rua** (aggregate) and **ruf** (failure/forensic) tags; aggregate reports are XML with no message content; contain reporting ESP, header-from domain, policy/alignment settings, sender IP, auth status, message counts; **ri** tag sets aggregate interval (default 24h, configurable).
- Report field anatomy: PTR/IP source (with ESP name resolution), volume, delivery status (delivered / delivered-to-spam / rejected based on applied policy), DMARC result, SPF result, **SPF alignment** vs **SPF authentication**, DKIM result, DKIM alignment vs DKIM authentication, reporter (ESP), date.
- Analysis workflow: platform replaces the rua address with its own; parses XML into readable data; categorizes into four tabs: **"Compliant", "Non-Compliant", "Threat/Unknown", "Forwarded"**; reverse lookups give source names instead of bare IPs; per-source **configuration guides** ("detailed configuration guides for specific email sources"); filtering by sender (source name, IP, SPF/DKIM domains) and receiver (reporter); XML file upload for migration; data export.
- Deployment doctrine: "Always initiate the DMARC implementation with p=none"; fix non-compliant sources with SPF/DKIM; "Monitor data after each fix… new reports appear under the Compliant tab instead of the Non-Compliant tab"; ensure every legitimate source is compliant (DKIM alignment preferred since "SPF alignment may not be possible with some ESPs"); "gradually enforce their policies until p=reject is achieved."
- Failure reports (ruf): "simple copies of emails that fail authentication checks"; "Often, email services don't provide forensic reports because of privacy concerns"; beginners advised to focus on aggregate reports.
- Compliance framing: mandate table — Microsoft sender requirements (from May 5, 2025), Google & Yahoo sender requirements (Feb 2024, >5,000 daily), GDPR, DORA, NIS2, PCI DSS 4.0, CCPA, GLBA, HIPAA.
- Scale claims (marketing, not asserted): 175,000+ domains, 380K+ daily spoofing attempts blocked, 9B+ daily emails authenticated.
- Channels: SMB → enterprise industries pages, MSP/reseller/wholesale programs, Academy (free courses), developer API, status page.

### Valimail

Key observations (A):

- Positioning: "The Global Leader in Email Trust & Security"; "We continuously operate your email's trust and identity"; DigiCert acquired Valimail (2025); "pioneering automated DMARC in 2015"; FedRAMP-certified ("the only DMARC vendor that meets the highest federal… standards").
- Product ladder: **Monitor** (free — "See all senders on your domain"), **Enforce** ("Stop phishing & impersonation"), **Amplify** ("Add your logo to every inbox" = BIMI).
- Monitor mechanics: "Turn raw IP data into instant DMARC reports"; "instantly identifies areas of vulnerability with detailed views into the **enforcement status** across all your sending domains"; "Global visibility into all senders in your domains — Stop manually sifting through raw IP data in DMARC reports"; "Unmatched discovery of third-party sending services — Monitor instantly identifies thousands of sending services, making it easy to distinguish legitimate senders from bad actors"; "Continuously monitor your enforcement status… which domains are passing and failing DMARC, aligned SPF and DKIM, and overall disposition"; "Global view of suspicious IPs sending as you — unidentified ISPs, open routers, unsecured hacked servers"; readiness check for "Google, Microsoft, & Yahoo's DKIM, SPF, and DMARC requirements"; BIMI logo preview.
- Enforce mechanics: "Authenticate legitimate senders in one-click"; "Use Instant SPF® to override the SPF lookup limit"; "automated DKIM, SPF, and DMARC record management" (patented); "Apply custom quarantine and rejection rules to prevent same domain spoofing"; "One-time DNS setup, one-click sender enablement"; "Authorize 99% of your sending services".
- Sender-authorization philosophy: "Identify thousands of email services by name, not just by IP address"; "Expose every unauthorized third-party email-sending service" (**Shadow IT** use case); "Simplifies the process of authorizing new email services with minimal configuration".
- Customer-voice evidence of the pre-platform pain: "In the past, we had to have one dedicated engineer look at the DMARC reports every week or every day; with Valimail we can just click one button." (Yelp security engineering manager); "DMARC is incredibly frustrating to handle manually, but with Valimail it collects all logs and makes it easier to interpret and find any issues."
- Use cases: anti-phishing, mailbox-provider requirements (Google/Yahoo), brand protection (BIMI), compliance, shadow IT.
- Comparison-table landscape naming (B-level for the named competitors): SMB = EasyDMARC, MxToolbox; mid-market = Mimecast, Dmarcian; enterprise = Proofpoint, Fortra, Cisco. Attributes compared: SPF lookup limit handling (flattening vs hosted SPF vs Instant SPF), sending-service identification, add-new-sending-services flow, record management automation, DNS management burden, BIMI support.
- Integration posture: official Microsoft 365 partnership (full API integration), Google Workspace partner; technology partners incl. Microsoft, Cloudflare, Abnormal, Sublime; MSP program.
- Free domain-checker surface: "Enter your domain to see if it's vulnerable to spoofing or if others are sending emails on your behalf. Instantly check your DMARC, SPF, and BIMI status"; result states include "DMARC NOT AT ENFORCEMENT" vs "DMARC at Enforcement".
- One quoted customer claims "the only DMARC vendor that offers a complete solution for both inbound and outbound email protection" — suite-drift signal (marketing claim; the inbound part belongs to gateway territory).

### Postmark (free DMARC monitoring / DMARC Digests)

Key observations (A):

- Offer: "A free weekly email to help monitor & implement DMARC… We will process reports from major ISPs about your domain's DMARC alignment and turn them into beautiful, human-readable weekly email summaries, absolutely free." Provided by Postmark, "an email service for web apps" (transactional email sender; owned by ActiveCampaign). Paid tier: "DMARC Digests".
- Complete onboarding flow documented on the page: enter domain + email → service generates the DMARC TXT record for you: `v=DMARC1; p=none; pct=100; rua=mailto:<token+lv_…>@inbound.postmarkapp.com; sp=none; aspf=r;` → "Add this TXT record to your domain's DNS at DMARC.domain.com" → service verifies the record ("can take up to 24 hours") → digest email arrives weekly.
- Feature list: Visibility into mail sources ("who's sending emails using your domains and the IPs those emails originate from"), DMARC report history ("View DMARC alignment for your domains over time"), Web Dashboard ("Manage all your domains, view statistics, and inspect mail sources"), Actionable Recommendations ("Learn how to improve DMARC alignment for trusted mail sources"), User Management ("Invite team members"), Email Digests.
- Tier split: Free = top 10 mail sources with 5 IPs each, 7 days of data, email only, weekly; Paid = all mail sources and IPs, 60 days, web dashboard + email, weekly & monthly digests, user management.
- Developer API exists for managing and retrieving reports.
- Framing: "DMARC is a standard that prevents spammers from using your domain to send email without your permission — also known as spoofing."
- What it does NOT do: no sender-authorization workflow, no policy-progression tooling beyond generic recommendations, no record management beyond the initial generated record, no SPF/DKIM machinery. This is the monitoring-only thin edge of the Type.

## Cross-product Comparison

| Dimension | dmarcian | EasyDMARC | Valimail | Postmark DMARC |
|---|---|---|---|---|
| Protected-domain record of record | yes ("domain catalog", Domain Overview, multi-domain) | yes (multi-domain, Managed DMARC) | yes ("all your sending domains") | yes (manage all your domains) |
| DNS record authoring/validation | Record Wizard, SPF Surveyor, DKIM Inspector/Validator, domain checker | record generators + checkers (DMARC/SPF/DKIM/BIMI/MTA-STS/TLS-RPT), domain scanner | automated record management (Enforce), one-time DNS setup | generates the initial DMARC record only |
| Report collection via rua (aggregate) | yes (XML-to-human heritage; Detail Viewer/Source Viewer) | yes (platform replaces rua with platform address; XML analyzer) | yes ("turn raw IP data into instant DMARC reports") | yes (rua points at inbound.postmarkapp.com) |
| Failure/forensic (ruf) handling | not evidenced on fetched pages | yes (failure reports tool; notes privacy limits) | not evidenced on fetched pages | not evidenced |
| Per-source identification with names | yes (Source Viewer / email source identification) | yes (reverse lookups → ESP names) | yes ("thousands of sending services by name") | yes (mail sources + IPs; "top 10 sources" free tier) |
| Alignment model surfaced | yes (dedicated alignment doc; SPF/DKIM alignment scores) | yes (SPF/DKIM alignment vs authentication fields) | yes ("aligned SPF and DKIM") | implied (alignment history) |
| Sender authorization workflow | guided (source guides; alerts on changes) | guided (per-source configuration guides) | automated one-click (Enforce) | no (recommendations only) |
| Policy progression tooling/journey | yes (explicit journey docs; pct guidance) | yes (gradual enforcement guidance) | yes (enforcement status + custom quarantine/reject rules) | no (monitoring only) |
| Post-enforcement maintenance | yes (Life after Reject: SPF review, DKIM rotation, alerts) | yes (monitoring after each fix; alerts) | yes (continuous enforcement posture) | no |
| Alerts | yes (Alert Central) | yes (Alert Manager) | yes (monitoring; SPF-change alerts) | not evidenced |
| Hosted/dynamic SPF handling of lookup limit | no (surveyor-based verification instead) | yes (EasySPF dynamic flattening) | yes (Instant SPF, patented) | no |
| BIMI | tools only | managed BIMI | full product (Amplify) | no |
| MTA-STS / TLS-RPT | not evidenced | yes (tools + managed) | not evidenced | no |
| Reputation/blacklist monitoring | no | yes | no | no |
| Deliverability products | no (separate concern) | yes (EasySender product line) | marketing angle only (open rates via BIMI) | company is an ESP (context, not feature) |
| Managed/white-glove service | yes (Deployment/Dedicated Support) | yes (Managed Services, dedicated engineer) | enterprise services | no |
| MSP/multi-tenant | yes (MSP program) | yes (MSP/reseller/wholesale) | yes (MSP program; multi-tenant platform) | team invite only |
| Compliance-driver framing | yes (cyber insurance, mandates pages) | yes (full mandate/regulation table) | yes (compliance use case, FedRAMP) | no |
| Free tier as entry | yes (free tools + trial) | yes (free tier + tools) | yes (Monitor is permanently free) | yes (free digest) |
| Developer API | not evidenced | yes | not evidenced on fetched pages | yes |

Reading of the comparison:

- Four products, four very different shapes, one shared skeleton: protected domain → published authentication records → collected DMARC reports → identified senders → (in three of four) enforcement progression.
- The strongest cross-product invariants: DNS-published records as the control surface; the rua-report collection loop; per-source (sender) identification; the none/quarantine/reject policy vocabulary.
- The most variable parts: automation of sender authorization (manual guidance → one-click); auxiliary protocols (BIMI, MTA-STS/TLS-RPT); hosted-record services (SPF flattening); ruf handling; deliverability/reputation add-ons; service wrapper (managed services, MSP programs).

## Canonical Model

Four-layer abstraction:

### L0 — Defining Invariant (jointly held; minimal)

1. **The protected domain of record with its published email-authentication configuration.** The managed unit is the organization-owned email domain; for it, the application authors/validates the SPF, DKIM, and DMARC records that get published in DNS (directly by the admin, or via hosted-record services). Remove → a DNS record generator / DNS management, not DMARC management.
2. **The DMARC reporting loop.** The application stands as (or proxies) the rua recipient: receiving mail systems send DMARC aggregate reports about mail claiming to be the domain; the application collects and parses them into per-source authentication evidence (volumes, SPF/DKIM results, alignment, disposition). Remove → blind configuration tooling with no feedback.
3. **The sender-and-policy progression loop.** Observed senders claiming the domain are inventoried and classified (legitimate vs not); legitimate ones are brought into alignment (SPF/DKIM configuration guidance or automated authorization); the domain's DMARC policy is advanced along the enforcement ladder (monitor → quarantine → reject) and maintained afterwards. Remove → passive DMARC monitoring (the Type's thin edge, represented by the free-digest class of tools).

Jointly-held is load-bearing: 1 alone = record generator; 2 alone = XML report inbox; 3 without 1–2 = policy checklist with no data; 1+2 without 3 = DMARC monitoring (a real but thin market tier — Postmark-style); 1+3 without 2 = configuration tooling that cannot see who actually sends.

### L1 — Common Mature Structure

- Per-source identification with human-readable service names (reverse lookup / reference data over raw report IPs)
- Record validators and generators (domain checkers, DMARC inspectors, SPF surveyors, DKIM validators) offered as free entry surfaces
- Compliance-rate dashboards with SPF/DKIM pass + alignment breakdown and disposition (delivered / spam / rejected) tracking
- Report history over time with filtering and export
- Alerts (new/unexpected sources, record changes, threat signals)
- Multi-domain management under one account; team/user management; MSP multi-tenant programs
- Guided configuration documentation per sending source/ESP
- Scheduled digests/reports for stakeholders
- Free monitoring tier as the acquisition funnel for the paid enforcement tier

### L2 — Variant / Optional Structure

- Auxiliary authentication/transport protocols: BIMI (brand indicators), MTA-STS, TLS-RPT
- Forensic/failure (ruf) report handling (privacy-limited receiver adoption)
- Hosted/dynamic record services: SPF flattening and hosted SPF (answering the 10-lookup limit), managed DKIM selectors, managed DMARC
- Managed/white-glove service wrappers (deployment projects, dedicated engineers)
- Mailbox-provider sender-requirement readiness checks (Google/Yahoo/Microsoft 2024–2025 era)
- Reputation/blacklist monitoring and deliverability add-ons (drift zone toward deliverability tooling)
- Lookalike-domain finder utilities (drift zone toward Digital Risk Protection)
- Developer APIs, SIEM/ticketing integration, XML file upload for migration
- Vertical/regional packaging (government/FedRAMP posture, regional data residency)

### L3 — Vendor-specific (research notes only)

- Valimail: Instant SPF® (patented lookup-limit override), "zero trust email" framing, official Microsoft 365 partnership, FedRAMP certification, DigiCert ownership, "4x faster" enforcement claims.
- dmarcian: XML-to-Human Converter heritage, regional data centers, DMARC Academy, "only 30% finish" estimate (unsourced vendor claim), Detail Viewer/Source Viewer/Alert Central module names.
- EasyDMARC: EasySPF branding, EasySender/Touchpoint product lines, four-tab report categorization (Compliant / Non-Compliant / Threat-Unknown / Forwarded), $-tier naming, GeoMaps visualization.
- Postmark: $14/month per domain paid tier, Monday-morning weekly digest cadence, 24-hour DNS verification window, ActiveCampaign ownership, tokenized rua addresses (`+lv_…`).

## Vendor-specific Findings

See L3 above. Additionally, Valimail's comparison table positions the whole market (EasyDMARC, MxToolbox / Mimecast, Dmarcian / Proofpoint, Fortra, Cisco), confirming the Type is inhabited by both pure-plays and email-security-suite modules — but the suite-module pole was not directly researched this pass and stays at layer B.

## Boundary Findings

- **vs Email Security Gateway** (§15 sibling): the gateway inspects and filters mail arriving at the organization; DMARC management publishes identity policy about the organization's own outbound domain and reads receiver reports about it. Different side of the mail flow, different objects (message streams vs DNS records/reports). Remove the DNS/report machinery and keep filtering → gateway. Suites ship both; Valimail's customer quote claiming "both inbound and outbound" is suite-packaging, not Type collapse.
- **vs Digital Risk Protection**: DRP monitors the external footprint (lookalike domains, fake profiles, rogue apps) and pursues takedowns. DMARC management operates the org's own domains' authentication. One sampled vendor ships a "Domain Lookalike Finder" free tool — a thin drift surface, not a Type merge.
- **vs DNS Management / DNS & DHCP Management** (§14): DNS management operates zones generally; this Type only authors specific authentication records into DNS and interprets the resulting authentication telemetry. The record-generator-only thin pole is the overlap.
- **vs Email Infrastructure Management** (§14): sending infrastructure (MTAs, IPs, ESP relationships) vs identity/policy layer on top. No sampled product manages the sending infrastructure itself.
- **vs Email Deliverability / sender-reputation monitoring**: deliverability measures whether mail lands in inboxes; DMARC management defines and enforces authentication identity. EasyDMARC's EasySender line and reputation monitoring show the market adjacency; Postmark lives on the ESP side of the seam.
- **vs Certificate Lifecycle Management / PKI** (§14/§15 siblings): different trust machinery (X.509 vs DNS TXT records). Market signal worth recording: DigiCert (PKI company) acquired Valimail — identity-layer convergence, but the objects remain distinct.
- **Thin edge — monitoring-only**: digest/report-viewer tools (Postmark class) do 1+2 but not 3. The market packages them as the entry tier of the same Type (Valimail Monitor is the permanently-free tier of a full platform), so they are documented as the Type's monitoring-only pole/variant, not a separate Type.
- **No leaf conflict found** with the directory as written; the leaf name ("Email Authentication / DMARC Management") matches the market's dual naming (vendors say "DMARC management", "email authentication", "domain security").

## Uncertainties

- Suite-module products (Proofpoint, Fortra/Agari, Mimecast, Barracuda, Cisco) were not directly researched; their DMARC capabilities are attested only through Valimail's comparison table and general market naming. Claims about them stay at layer B and out of the final document's specifics.
- Valimail's enforcement-rate and "4x faster" figures are internal marketing; not asserted.
- dmarcian's "only 30% of organizations finish" is an unsourced vendor estimate; kept out of the final document.
- Exact pricing tiers, retention windows, and alert taxonomies vary by product and plan; precise numbers (except the Postmark page's own published tier table, kept in research notes only) are withheld from the final document.
- The ruf/forensic-report receiver adoption is described as limited by EasyDMARC ("often, email services don't provide forensic reports because of privacy concerns"); no receiver-side documentation was fetched this pass, so receiver behavior is held at this quoted strength.
- The exact status of the new DMARC RFC's `t` tag replacing `pct` is per dmarcian's article; not independently verified against the RFC text.

## Final Synthesis

An Email Authentication / DMARC Management application is domain-owner-side security software whose world consists of: the organization's email domains held as protected records; the SPF/DKIM/DMARC records published in DNS as the control surface; the aggregate DMARC reports that receiving mail systems send back as evidence of who is sending as the domain; the sender inventory built from those reports; and the enforcement ladder (monitor → quarantine → reject) that the domain owner climbs once legitimate senders are aligned and authorized. The application never sends or filters mail itself; its leverage is DNS publication plus report interpretation. Mature products add per-source service identification, record validation tooling, alerts, multi-domain/MSP management, auxiliary protocols (BIMI, MTA-STS, TLS-RPT), hosted-record services for SPF's lookup limits, managed-service wrappers, and compliance framing against the 2024–2025 mailbox-provider sender mandates and security regulations. The Type's thin edge is monitoring-only digest tools; its drift zones are inbound email security (gateways), digital risk protection, and deliverability tooling. Historical check: the pre-platform practice — publish a DMARC record with a personal rua mailbox, open XML report attachments by hand or with scripts, edit DNS manually, advance the policy conservatively — satisfies the defining core without any vendor platform, cloud service, or AI component; open-source/self-hosted report parsers occupy the same structure. The core is era-stable.
