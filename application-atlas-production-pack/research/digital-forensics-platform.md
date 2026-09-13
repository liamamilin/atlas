# Research Notes — Digital Forensics Platform

## Research Goal

Understand the Application Type **Digital Forensics Platform** (DIRECTORY §15 Cybersecurity, Identity & Trust) from real products: what objects exist inside it, who uses it, how an examination flows from acquisition to report, which rules make findings defensible, and where the boundary lies against eDiscovery, incident response, malware analysis, EDR/SIEM, evidence custody, and investigation case management.

## Initial Boundary

- Hypothesis: an investigator-facing platform for acquiring, examining, and reporting on forensically preserved digital evidence (disk images, device extractions, cloud exports), organized around cases, with integrity/audit machinery that makes findings legally defensible.
- Nearest neighbors: eDiscovery Platform (§11), Cyber Incident Response Platform (§15), Malware Analysis Sandbox (§15), EDR/XDR (§15), SIEM/SOC (§15), Evidence Management System (§24), Corporate Investigation Management (§11), Legal Hold Management (§11), Backup Management (§14).
- Potential confusions: "forensics" is used loosely by security vendors (EDR "forensics", DLP "forensics", browser "forensics"); the Type here is the classic digital-forensics lab tool.

## Research Questions

1. What is the unit of record — the case? the evidence image? the artifact?
2. What does "forensically acquired" mean operationally (images, extractions, hash verification, write protection)?
3. What does examination actually consist of (search, carving, artifact parsing, timeline)?
4. How do examiners record findings (tags, bookmarks, notes) and how do they become a report?
5. What integrity/audit machinery is structural (hashing, audit logs, chain of custody)?
6. How do multiple examiners collaborate on one case?
7. Which sources do platforms cover (computer, mobile, cloud, vehicle, memory, media)?
8. Where are the boundaries vs eDiscovery / IR / malware sandbox / EDR / evidence custody?

## Representative Products

| Product | Why selected | Sources used | Tier |
|---|---|---|---|
| Magnet AXIOM (+ Axiom Cyber) | Commercial leader; public-safety + enterprise (DFIR) poles; integrated acquisition+analysis | magnetforensics.com product pages (Axiom, Axiom Cyber) | Tier 2 |
| Exterro FTK (Forensic Toolkit + family) | Enterprise/lab-scale pole; corporate + law enforcement; suite boundary with eDiscovery | exterro.com root, FTK product page | Tier 2 |
| X-Ways Forensics | European examiner-centric pole; lightweight/portable philosophy; deep feature documentation | x-ways.net forensics page | Tier 2 (feature-level) |
| Autopsy (The Sleuth Kit) | Open-source pole; free; law enforcement/military/corporate; module architecture | sleuthkit.org (home, features, multiuser) | Tier 1–2 |
| Cellebrite (UFED / Physical Analyzer) | Mobile-forensics market anchor | Site unreachable (403 ×2) — no product claims made | — |
| OpenText EnCase Forensic | Legacy standard; .E01 evidence-file format origin | Site unreachable (444 ×2) — no product claims made | — |

Boundary-informing (not deep samples): Exterro's corporate-investigations use case (per corporate-investigation-management research notes — FTK pole recorded there as Product Mismatch, belonging to this Type); sibling research files cyber-incident-response-platform.md and evidence-management-system.md.

## Sources

- https://sleuthkit.org/autopsy/ (fetched 2026-09-08)
- https://sleuthkit.org/autopsy/features.php (fetched 2026-09-08)
- https://sleuthkit.org/autopsy/multiuser.php (fetched 2026-09-08)
- https://www.magnetforensics.com/products/magnet-axiom/ (fetched 2026-09-08)
- https://www.magnetforensics.com/products/magnet-axiom-cyber/ (fetched 2026-09-08)
- https://www.x-ways.net/forensics/ (fetched 2026-09-08)
- https://www.exterro.com/ (fetched 2026-09-08)
- https://www.exterro.com/digital-forensics-software/ftk-forensic-toolkit (fetched 2026-09-08)
- https://cellebrite.com/en/cellebrite-ufed/ — 403; https://cellebrite.com/en/ufed/ — 403 (abandoned per network rules)
- https://www.opentext.com/what-we-do/products/discovery-security/opentext-encase-forensic — 444; https://www.opentext.com/products/encase-forensic — 444 (abandoned)
- https://www.exterro.com/ftk — 404 (root page used instead)
- Sibling research: research/cyber-incident-response-platform.md, research/corporate-investigation-management.md, research/evidence-management-system.md

## Product A — Autopsy (The Sleuth Kit)

### Key observations (Layer A — official site)

- Self-description: "a digital forensics platform and graphical interface to The Sleuth Kit and other digital forensics tools. It is used by law enforcement, military, and corporate examiners to investigate what happened on a computer."
- Positioning: "end-to-end platform with modules" — built-in modules plus third-party modules; results found "in a single tree"; background tasks run in parallel; results appear as soon as found.
- Analysis features (features.php): Multi-User Cases; Timeline Analysis ("displays system events in a graphical interface to help identify activity"); Keyword Search (text extraction + indexed search, regex); Web Artifacts (history/bookmarks/cookies from common browsers); Registry Analysis (RegRipper — recently accessed documents, USB devices); LNK file analysis; Email analysis (MBOX); EXIF geolocation; File type sorting; Media playback; Thumbnails; File system analysis (NTFS, FAT12/16/32/ExFAT, HFS+, ISO9660, Ext2/3/4, Yaffs2, UFS); Hash set filtering (NSRL known-good, custom known-bad in HashKeeper/md5sum/EnCase formats); Tags ("bookmark"/"suspicious" + comments); Unicode strings extraction from unallocated space; Interesting Files module; Android support (SMS, call logs, contacts, app data).
- Input formats: "disk images, local drives, or a folder of local files. Disk images can be in either raw/dd or E01 format."
- Reporting: extensible reporting infrastructure; default HTML, XLS, Body file; reports include tagged files, comments/notes, bookmarks, web history, recent documents, keyword hits, hashset hits, installed programs, devices attached, cookies, downloads, search queries.
- Multi-user cases (multiuser.php): "create multi-user cases that allow you to see the results that your fellow examiners found in real time"; requires central PostgreSQL, central Solr, central ActiveMQ, central storage.
- Data carving: "Recover deleted files from unallocated space" (via PhotoREC).
- Cost: free; positioned against commercial tools.

## Product B — Magnet AXIOM / Axiom Cyber

### Key observations (Layer A — official product pages)

- Axiom: "Recover, analyze, and report on data from mobile, computer, cloud, and vehicle sources for a complete view of your case." "Bring computer, mobile, cloud, vehicle, and acquired data into a single Axiom case." "Access industry-leading artifact coverage across devices, apps, and cloud services." "AI-powered analysis, Connections, and Timeline." "Uncover the full history of a file or artifact to build your case and establish intent."
- Integrations: "Seamlessly connect with your existing forensic tools and evidence management platforms."
- Magnet ecosystem structure: Acquisition products (Graykey — "access and extract data from iOS and Android devices"; Verakey — consent-based extraction; Autokey — vehicle data; Graykey Fastrak — multi-device), Collection & Analysis (Axiom, Axiom Cyber, Nexus — "remote endpoint collection at scale"), Collaboration (Review), Lab automation (Automate), Platform (Magnet One — links products through the cloud).
- Axiom Cyber: "Analyze digital evidence across remote endpoints, cloud environments, and mobile — reducing time to evidence while preserving accuracy and defensibility." Remote collections from Mac/Windows/Linux "even when they're off the network"; "gathering artifacts from physical drives and memory"; targeted data acquisition ("acquire only the data that matters, using targeted locations"); "artifact-first approach"; "root cause analysis workflows, and YARA rule and MITRE ATT&CK integration"; purpose-built views "Email Explorer, Mobile View, and the IOC Insights Dashboard"; deploy cloud/on-prem/hybrid (AWS/Azure); "available integrations for critical DFIR tools."
- Use cases surfaced: mobile forensics, computer forensics, cloud forensics, media forensics, incident response, eDiscovery, internal investigations. Industries: public safety, federal, military & intelligence, service providers, enterprise.
- User quotes (G2/customers): "digital forensics acquisition and analysis platform"; "we can quickly acquire evidence for any cyber incident and parse artifacts"; "forensically sound, limited data that's focused to our eDiscovery teams" (forensics service provider feeding eDiscovery).

## Product C — X-Ways Forensics

### Key observations (Layer A — official feature page)

- Self-description: "Integrated computer forensics software"; "an advanced work environment for computer forensic examiners"; based on the WinHex hex/disk editor; German product; runs portable from USB; dongle or network dongle licensing.
- Acquisition: disk cloning and imaging; reads/writes .e01 evidence files ("a.k.a. EnCase images"); evidence file containers for logical acquisition ("copy relevant files and directories... retain almost all their original file system metadata... selectively acquire data... or exchange selected files with investigators, prosecution, lawyers"); X-Ways Imager as separate imaging product; Windows FE bootable environment "for triage/preview"; remote analysis via F-Response.
- File systems: FAT12/16/32, exFAT, TFAT, NTFS, Ext2/3/4, CDFS/ISO9660/Joliet, UDF, HFS/HFS+/HFSJ/HFSX, XFS, Btrfs, ReiserFS/4, UFS1/2, APFS, QNX, SquashFS; partitioning MBR/GPT/Apple/dynamic/LVM2; RAID interpretation; lost/deleted partition identification; sector superimposition to parse corrupted structures "without altering the original disk or image."
- Recovery: "various data recovery techniques, lightning fast and powerful file carving"; deleted-file traces via $LogFile (NTFS), .journal (Ext3/4); carving within files; slack space/free space/inter-partition space gathering.
- Integrity: "Write protection to ensure data authenticity"; "Automated activity logging (audit logs)"; mass hash calculation (Adler32…MD5, SHA-1, SHA-256, RipeMD, Tiger…); hash-set matching (NSRL RDS, Project Vic, HashKeeper, ILook; up to 2 internal hash databases); PhotoDNA (law enforcement only); FuzZyDoc hashing; block-hash matching of fragments.
- Examination: physical and logical search (many terms, GREP, operators AND/NEAR/NOTNEAR); indexing; viewer for 270+ file types; registry viewer + automated registry report; Windows event log/lnk/prefetch/$UsnJrnl viewers; SQLite/browser artifact viewers; email examination (Outlook PST/OST, Exchange EDB, DBX, mbox, MSG, EML); metadata extraction/filtering; embedded-file extraction; archive listing; duplicate detection; gallery view (thumbnails); skin-color detection; video frame extraction.
- Timeline: "powerful event list based on timestamps found in all supported file systems, in operating systems (including event logs, registry, recycle bin...), and file contents (e-mail headers, Exif timestamps, GPS timestamps...)"; chronological sorting; calendar view with activity hotspots.
- Case & findings: "Complete case management"; tags, comments, bookmarks, report tables; "Ability to tag files and add notable files to the case report"; case reports importable into any HTML-aware application (e.g., MS Word); CSS report formatting.
- Collaboration: "Support for multiple examiners in cases... distinguishes between different users based on their Windows accounts. Users may work with the same case at different times or at the same time and keep their results (search hits, comments, report table associations, tagmarks, viewed files, excluded files, attached files) separate, or shares them if desired."
- Companion: X-Ways Investigator — "reduced and simplified user interface available for investigators that are not forensic computing specialists"; examiner↔investigator collaboration workflow.
- Extensibility: X-Tensions API (3rd-party add-ons); Excire Forensics AI photo analysis.

## Product D — Exterro FTK (Forensic Toolkit + family)

### Key observations (Layer A — official product pages)

- Positioning: "Quickly locate, collect, and analyze digital evidence"; "the proven leader in digital forensics"; "turning complex data into defensible evidence."
- Value pillars: Deep Evidence Analysis ("Index, search, and analyze massive datasets"); High-Speed Processing ("scalable architecture designed for enterprise and lab environments"); Defensible Workflows ("Maintain chain-of-custody and repeatable processes to ensure findings stand up in court or internal investigations").
- Evidence Processing & Indexing: "high-speed ingestion and distributed processing. Gain total visibility into job statuses and error handling."
- Advanced Search & Analysis: "powerful full-text indexing, granular metadata filtering, and deep artifact analysis."
- Timeline & Visualization: "reconstruct events and correlate activity across multiple sources."
- Connectors: "190+ native connectors to enterprise data sources across email, cloud storage, mobile, and collaboration platforms."
- Portable Case: "Export your data into a portable case for offline review. Any labels and bookmarks created by the reviewers are synced back to the original case."
- System Summary Parsing: "See every application the user opened, internet activity performed, networks the user was connected to, and where and when this activity occurred."
- featureList (schema.org): Mac data review (encrypted/compressed/deleted Apple file systems); image identification (facial/object recognition); mobile data processing for chat apps; automated workflows with scripting; registry data analysis; deleted file recovery through data carving; encrypted content access; BitLocker/McAfee Drive Encryption decryption.
- FTK family: FTK Central ("Enterprise-scale forensic investigations with centralized processing and collaboration"); FTK Connect ("Automate evidence collection and integrate forensic workflows with security tools"); FTK Imager ("Acquire forensic images quickly without altering original evidence"); FTK Imager Pro; FTK Enterprise; ARMOURop (agentic AI "translates natural language queries into controlled forensic action across live endpoints").
- Exterro platform context: eDiscovery + Digital Forensics + Data Governance sold as one "Data Risk Management Platform"; forensics pillar promises "field triage and chain of custody... maintaining integrity from the field to the lab."
- Users: corporate + public sector; law enforcement (FBI case study); Kroll quote: "FTK is the only tool you need to process and parse ALL of your digital evidence – mobile data, computer data, and cloud app data."

## Cross-product Comparison

| Dimension | Autopsy | Magnet AXIOM | X-Ways Forensics | Exterro FTK |
|---|---|---|---|---|
| Unit of record | Case (single- or multi-user) | Single case across computer/mobile/cloud/vehicle | Case ("complete case management") | Case; portable case export |
| Evidence sources | Disk images (raw/dd, E01), local drives, folder of files | Mobile, computer, cloud, vehicle, acquired data; Cyber adds remote endpoints + memory | Disk images (.e01 read/write), drives, evidence file containers (logical) | Computer, mobile, cloud app data; 190+ connectors; FTK Imager for acquisition |
| Integrity machinery | E01 support; hash set filtering | "preserving accuracy and defensibility" | Write protection; audit logs; mass hashing | Chain-of-custody positioning; "without altering original evidence" (Imager) |
| Examination | Ingest modules: keyword search, web artifacts, registry, email, EXIF, carving, file-type sorting | Artifact coverage; Connections; Timeline; AI analysis | Carving, deleted-file traces, search (logical+indexed), registry, email, 270+ file-type viewer | Full-text indexing, metadata filtering, artifact analysis, system summary parsing |
| Timeline | Timeline analysis module | Timeline + Connections | Event list + calendar view | Timeline & visualization |
| Findings capture | Tags + comments | (implied by case/report flow) | Tags, bookmarks, comments, report tables | Labels/bookmarks (portable case sync-back) |
| Reporting | HTML/XLS/BodyFile, configurable | Report on data (stated) | HTML case report, CSS, Word-importable | Defensible findings (stated) |
| Collaboration | Multi-user cases, real-time shared results | Magnet One/Review ecosystem | Multiple examiners per case, per-account separation or sharing | FTK Central centralized processing + collaboration |
| Audience | Law enforcement, military, corporate | Public safety + enterprise (Cyber) | Examiners (professional), investigator companion product | Corporate + public sector, labs |
| Business model | Free/open source | Commercial subscription | Commercial, dongle, portable | Commercial suite |

### Convergent structure (Layer B — cross-product commonality)

All four products share: (1) evidence acquired/preserved as the analysis substrate (images/extractions/containers — never live-only); (2) a case binding evidence + examiner work; (3) examination machinery (search/index, deleted-data recovery, artifact parsing, timeline); (4) findings capture (tags/bookmarks/comments) flowing into a report; (5) integrity/audit posture (hashing, write protection, audit logs, chain-of-custody language); (6) multi-examiner collaboration on cases.

### Divergent structure (vendor/segment)

- Source emphasis: X-Ways = computer/disk pole; Cellebrite-class = mobile pole; AXIOM/FTK = multi-source (computer+mobile+cloud); AXIOM Cyber/FTK Connect = remote/enterprise collection.
- Packaging: single examiner workstation (X-Ways, Autopsy) vs lab/centralized processing (FTK Central, Autopsy multi-user, Magnet Automate).
- Philosophy: lightweight portable examiner tool (X-Ways) vs enterprise processing engine (FTK) vs integrated ecosystem (Magnet) vs free modular platform (Autopsy).
- DFIR-flavored extras: YARA/ATT&CK integration, IOC dashboard (AXIOM Cyber — single-product evidence); agentic AI over live endpoints (Exterro ARMOUR — single-product).
- Law-enforcement-only capabilities: PhotoDNA CSAM hash matching (X-Ways — explicitly law enforcement only).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (four jointly-held structures)

1. **The forensic evidence source of record** — a preserved acquisition of a specific device, media, or account (forensic disk image, device extraction, cloud export, memory capture, logical evidence container) that the platform ingests and examines as a verified copy rather than live data. Remove → live-system monitoring/analysis (EDR/DFIR triage) or generic file analysis.
2. **The case as binding container** — a persistent case record associating evidence sources, examiner actions, notes/tags, and findings; supports multi-examiner work. Remove → disconnected analysis utilities (a carver or hex editor is not a platform).
3. **Examination & reconstruction over the evidence** — parsing file systems and applications, recovering deleted/hidden data, searching (indexed/keyword/regex), decoding application artifacts, and building timelines to reconstruct activity. Remove → storage/transfer tool or bare viewer.
4. **Defensibility posture** — integrity verification (hashing), original-preservation/write-protection, recorded audit trail of analyst actions, and report generation of findings. Remove → generic data-analysis workbench.

Jointly-held is load-bearing: 1+3 without 2+4 = analysis utilities; 2+4 without 3 = case tracker; 3+4 without 1 = live analytics.

### L1 — Common Mature Structure

- Integrated or companion acquisition tooling (imaging, device extraction, cloud collection, remote collection, targeted acquisition)
- Broad artifact coverage (browsers, registry, email, chat apps, system usage) kept current with new app versions
- Hash-set filtering against known-file databases (known good / known bad)
- Gallery/thumbnail views, file-type sorting, duplicate detection
- Email and registry examination modules
- Connections / link analysis across artifacts
- Multi-user cases with per-examiner result separation or sharing
- Processing job management (status, errors, distributed processing)
- Portable/shareable case export
- Integrations with other forensic tools and evidence-management platforms

### L2 — Variant / Optional Structure

- Source emphasis: computer/disk vs mobile vs cloud vs vehicle vs media/DVR vs memory
- Audience packaging: law-enforcement vs corporate/DFIR vs forensic service provider vs multi-audience
- Deployment: examiner workstation vs centralized lab processing vs cloud/hybrid
- Open-source vs commercial; dongle/portable licensing
- DFIR-flavored integrations (YARA, MITRE ATT&CK, IOC workflows) — single-product evidence, treat as variant
- AI layers (photo classification, media identification, AI summaries, agentic endpoint action) — current-generation, uneven
- Law-enforcement-restricted capabilities (e.g., CSAM hash matching)

### L3 — Vendor-specific (Research Notes only)

- Magnet: Graykey/Verakey/Autokey/Nexus acquisition family; Magnet One cloud linking; Magnet Review; Automate
- Exterro: FTK Central/Connect/Imager/Imager Pro/Enterprise naming; ARMOUR/ARMOURop agentic framework; 190+ connectors claim; Exterro Intelligence
- X-Ways: WinHex lineage; X-Tensions API; FuzZyDoc; PhotoDNA interface; F-Response; Windows FE; dongle; Excire
- Autopsy: The Sleuth Kit substrate; PhotoREC carving; RegRipper; central PostgreSQL/Solr/ActiveMQ multi-user stack
- FTK FAQ competitive claims (vs AXIOM/EnCase) — marketing, not recorded as fact

## Historical / Market-Sample Check (§24 reasoning)

- The case + evidence-file + report model predates modern multi-source platforms: EnCase (1990s) established the .E01 evidence-file pattern (X-Ways still documents ".e01 evidence files (a.k.a. EnCase images)" — Layer A); FTK (2000s) the processing/indexing pattern; The Coroner's Toolkit (1996) and manual bit-for-bit copying + hex review satisfy the core (verified copy, documented examination, findings report) without GUI/cloud/mobile/AI.
- Regional: X-Ways (Germany) and Autopsy (US open source) show the Type is not a US-commercial-suite pattern; Cellebrite (Israel) shows the mobile pole. All fit the four-part core.
- Conclusion: the L0 holds across eras and regions; cloud/mobile/AI are L1/L2, not definitional.

## Vendor-specific Findings

See L3 above. Also: Exterro sells forensics inside a legal-tech suite (eDiscovery + governance) — packaging, not structure. Magnet sells acquisition hardware/software (Graykey) as separate products — the platform consumes their extractions; acquisition can be external to the platform (also true of FTK Imager, X-Ways Imager, and Autopsy, which consumes images made elsewhere).

## Boundary Findings

- **vs eDiscovery Platform (§11)**: eDiscovery's unit is the document/ESI item and its goal is relevance review and legal production; forensics' unit is the device/extraction and its goal is technical reconstruction of activity (deleted data, artifacts, timelines). Overlap: forensics collections feed eDiscovery (AXIOM Cyber customer quote: "forensically sound, limited data... focused to our eDiscovery teams" — Layer A); Exterro sells both in one suite. Test: remove device-level examination depth (carving, artifacts, timeline) and keep document review/production → eDiscovery; remove review/production machinery and keep examination → this Type.
- **vs Cyber Incident Response Platform (§15)**: mirrors sibling research — IR platform records and coordinates the response (case lifecycle, tasks, stakeholders); forensics platform acquires/examines evidence. Forensic tooling appears in IR platforms as an integration category. Test: remove the coordination/case-lifecycle record and keep evidence acquisition/examination → this Type.
- **vs Malware Analysis Sandbox (§15)**: sandbox analyzes a single suspicious sample's behavior in isolation; forensics reconstructs activity across a whole device/account within a case. Test: single-sample detonation focus → sandbox.
- **vs EDR/XDR (§15)**: EDR is live, ongoing, agent-based detection/response on endpoints; forensics is retrospective examination of preserved evidence. EDR "forensics" features (timeline capture, triage collection) are a drift zone but the posture differs (live vs preserved). Test: remove the preserved-acquisition-of-record posture → EDR/DFIR triage territory.
- **vs SIEM/SOC (§15)**: SIEM aggregates telemetry for continuous detection/alerting; no case evidence chain, no acquisition. Test: remove acquisition/examination of preserved evidence → SIEM.
- **vs Evidence Management System (§24)**: custody systems track physical/digital evidence items and their chain of custody (property-room function); forensics platforms examine the data. Sibling research (evidence-management-system.md) shows forensic labs as *users* of custody systems. Test: remove examination and keep custody tracking → Evidence Management System.
- **vs Corporate Investigation Management (§11)**: mirrors sibling research — investigation management is the case lifecycle over allegations (intake→fact-finding→determination); forensics is the evidence-analysis machinery that may feed it. Test: remove evidence-processing depth and keep allegation lifecycle → investigation management.
- **vs Backup Management (§14)**: backup products may offer "forensic backups" (imaging as a backup mode); the purpose is restore, not examination. Test: remove examination/report → backup.
- **"Forensics" as loose marketing**: DLP/browser-security/EDR vendors use "forensics" for activity visibility; none carry the case+evidence+defensibility core.

## Uncertainties

- Cellebrite and OpenText EnCase official pages unreachable (403/444) — mobile pole and legacy-standard pole are represented as market anchors only; no product-specific claims made. The mobile-pole structure (extraction → parsing → analysis → report) is inferred from AXIOM/FTK multi-source coverage and ecosystem structure (Magnet acquisition products feeding Axiom), not from Cellebrite's own docs.
- Precise operational details (exact hash algorithms per product beyond those listed, exact report formats, licensing mechanics) intentionally not asserted beyond direct evidence.
- Whether "vehicle forensics" (AXIOM/Autokey) is a stable sub-segment or a niche extension — single-vendor evidence.
- Exterro ARMOUR/ARMOURop agentic AI over live endpoints — current-generation marketing; structure may drift toward live-response; watched as potential boundary drift, not treated as definitional.

## Final Synthesis

A Digital Forensics Platform is an investigator-facing examination platform whose defining core is four jointly-held structures: the forensic evidence source of record (preserved, verified acquisitions of devices/media/accounts examined as copies, not live data), the case as the binding container for evidence and examiner work, examination-and-reconstruction machinery over that evidence (search, deleted-data recovery, artifact decoding, timeline), and the defensibility posture (integrity verification, original preservation, audit trail, findings reporting). Mature products add acquisition tooling, broad artifact coverage, hash-set filtering, collaboration, and integrations. Variants divide by source emphasis (computer/mobile/cloud), audience (law enforcement/corporate/service provider), and packaging (workstation tool vs lab platform vs suite module). The Type is distinct from eDiscovery (document review/production), incident response (coordination), malware sandbox (single-sample behavior), EDR/SIEM (live detection), and evidence custody (tracking without examination).
