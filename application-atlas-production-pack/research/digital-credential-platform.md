# Research Notes — Digital Credential Platform

## Research Goal

Understand what a Digital Credential Platform actually is as an Application Type: what objects exist inside it (credential definitions, issued credentials, recipients), how the issuance workflow runs, what "verification" concretely means in these products, what the recipient/earner side looks like, what post-issuance management exists, and where the boundary lies against neighboring Types (certification management, transcript management, ePortfolio, identity verification, LMS, PKI certificate management, event badging).

Directory context: leaf "Digital Credential Platform", section 23 (Education, Research & Knowledge Institutions). Research date: 2026-09-07.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: an organization (issuer) designs digital credentials (badges/certificates) carrying structured metadata, issues credential instances to identified recipients, hosts them as verifiable records, and manages their state; recipients claim/store/share them; third parties verify authenticity.
- Suspected confusions:
  - Certification Management (§25): the certification program lifecycle vs the issued artifact — the prior certification-management pass already recorded the seam "badges are issuance artifacts".
  - Certificate Lifecycle Management (§14): PKI/TLS machine certificates — suspected false friend.
  - Campus Card Management (§23): that pass explicitly flagged this leaf as a "false friend" (physical service-access credentials vs achievement credentials).
  - Transcript Management (§23): official academic record vs individual achievement artifacts.
  - ePortfolio Platform (§23): holder-curated works vs issuer-attested achievements.
  - LMS-native certificates: course-completion certificates as an LMS capability vs a dedicated credential system of record.
  - Event Credential / Badge Management (§26): physical access badges vs achievement credentials.

## Research Questions

1. What are the core objects? (credential design/definition vs issued credential instance vs recipient)
2. How does issuance happen? (manual, bulk, API, LMS triggers, earner-initiated applications)
3. What does verification concretely consist of? (hosted credential page, URL/QR, embedded metadata, blockchain)
4. What does the recipient experience look like? (claim/accept, wallet, profile, sharing, PDF)
5. What post-issuance state management exists? (expiration, renewal, correction/reissue, revocation)
6. What role do standards play (Open Badges 1.x/2.x/3.0, verifiable-credential formats, CLR, blockchain)?
7. How do products differ by segment? (higher ed, corporate workforce, certification bodies, SMB/self-serve, associations, event/training)
8. Which capabilities are definitional vs common vs optional vs vendor-specific?
9. Where exactly are the boundaries with neighboring Types?

## Representative Products

Selected for market representativeness, documentation depth, differing product philosophy, and differing customer levels:

1. **Accredible** — self-titled "Digital Credential Platform"; enterprise leader across higher education, associations, online learning platforms, product certification, employee training, awarding & testing bodies.
2. **Credly (by Pearson)** — workforce/professional-credentialing pole; large issuer network and earner-side network; separate earner and issuer help centers.
3. **Certifier** — self-serve SMB/education pole; certificate-maker origin grown into a credential platform; explicit Open Badge 3.0 compliance.
4. **Open Badge Factory (OBF, Finland)** — open-standards-native, EU/multilingual pole; badge-ecosystem philosophy (organizational sharing/endorsement, earner applications); 1EdTech certified.
5. **Parchment (Instructure) — secondary/boundary sample.** Formerly Badgr (the education-native, standards-pioneer product) is now sold as "Parchment Digital Badges" / Parchment Award inside a records-and-credentials suite. Used mainly for the transcript/credential seam and as a market-structure observation, not as a primary structural sample.

## Sources

Fetched 2026-09-07:

- Accredible — https://www.accredible.com/ (homepage: positioning, feature and service inventory, solutions) — A
- Accredible — https://www.accredible.com/platform (platform detail: award/design, white-labeling, directories, expiration/renewals, sharing, pathways, analytics, integrations) — A
- Accredible — example credential page links observed (credentials hosted on issuer-branded domains, e.g. credential.net / university subdomains) — A (links observed; pages not fetched)
- Credly — https://support.credly.com/hc/en-us (Earner Help Center: accepting badges, earner dashboard, badge/skills wallets, profile, sharing, mobile app, blockchain publish, transcript, outside-badge import) — A
- Credly — https://credlyissuer.zendesk.com/hc/en-us (Issuer/Admin Help Center: category structure only — Getting Started, Badging Basics, Organization Management & Tech Resources, Marketing & Communications, Program & Earner Management) — A- (structure only; article bodies not rendered)
- Credly — https://info.credly.com/ (issuer positioning: Digital Credentials product, network claims, solutions for employers/higher-ed/certification providers/associations/training providers) — A for positioning; scale numbers are marketing claims (B, not independently verified)
- Certifier — https://certifier.io/ (full feature inventory: design→generate→send→share→verify→analyze loop, bulk generation, dynamic QR, credential renewals, OpenBadge 3.0, credential portal, RBAC/workspaces, integrations, API/webhooks) — A
- Open Badge Factory — https://openbadgefactory.com/en/ (create/issue/manage Open Badges; Open Badge / PDF badge certificates / micro-portfolios; issuing methods: bulk, API, badge applications, LMS plugins; Open Badge Passport wallet; organizational sharing/endorsement; ESCO/CASE frameworks) — A
- Parchment/Instructure — https://info.badgr.com/ (redirects to Parchment: "Parchment Digital Badges" login; Parchment Award issues "transcripts and diplomas to digital badges, CLRs, and certificates") — A (market-structure observation)

### Source-access limitations

- Accredible help center (support.accredible.com and help.accredible.com) unreachable: transport error + 401 across two attempts — abandoned per the network rule. Issuer-side operational detail therefore rests on the marketing/platform pages (Tier 2), which are unusually feature-explicit; precise operational parameters (limits, plan gates) are not asserted anywhere.
- Certifier help center (help.certifier.io) transport error on first attempt — abandoned; main site used instead (its feature inventory is detailed).
- Open Badge Factory FAQ path 404; main site used.
- Credly issuer help center returned category navigation only, not article content; issuer-side workflow detail relies on category structure + positioning pages; earner-side detail is Tier 1.
- Badgr's own product documentation was not reachable as a distinct product (info.badgr.com now serves Instructure/Parchment). Badgr is treated as a market-structure observation, not a primary sample. No claims rest on Badgr-specific features.
- No precise numeric limits, plan gates, or retention windows are asserted in the final document; vendor statistics (e.g., "123M+ credentials", "3,700+ issuers") are marketing claims recorded here only.

## Product Observations

### Accredible

Evidence layer: A (official site/platform pages; help center unreachable).

- Self-positioning: "Digital Credential Platform — create, issue, and manage digital certificates and badges at any scale."
- Platform narrative contrasts the "traditional credentialing model" (paper/PDF; "connection ends at issuance"; fraud potential; costly to verify; zero visibility for issuers, learners, employers) with digital, shareable, verifiable credentials — useful for understanding what the Type claims to fix.
- Artifact forms: digital badges and certificates, designed to "showcase acquired skills, earning criteria, and evidence of learning" — metadata beyond the visual artifact.
- Issuance: auto-issue integrated with LMS/CMS/publishing tools; "at any scale"; retroactive credential editing and automated name-change handling; expiration and renewals.
- Recipient experience: "One-Click Acceptance" (their framing: requiring account creation suppresses sharing); one-click social sharing (claimed 40+ platforms); embedding in LinkedIn, websites, transcripts, email signatures; white-labeled credential pages, emails, URLs, learner directories, "digital wallet cards"; credentials hosted on issuer-branded domains.
- Program-growth layer (distinctive emphasis): Spotlight (branded directory of credential holders), Pathways (visualized learning paths with milestone credentials, stackable micro-credentials), Recommendations (advertise credentials to learners), Email Campaigns (sharing reminders, re-enrollment incentives, renewal notices), Job Market Insights, analytics beyond issuance counts (email engagement, social shares, referrals, pathway completions/drop-offs).
- Trust services: "third parties can instantly verify" credentials; Fraud Monitoring service (protect credentials from misuse); Live Credentials service ("keep certifications current with ongoing validation"); print fulfillment for physical certificates.
- Transcripts: verified credential records aggregating learning ("digital credential transcripts").
- Segments: higher education, associations, online learning platforms, product certification, employee training, awarding & testing bodies.

### Credly (by Pearson)

Evidence layer: A for earner side (help center), A for positioning (official site), A- for issuer-side structure (help-center categories).

- Two-sided structure is explicit in documentation: a separate Earner Help Center and a separate Issuer/Admin Help Center (categories: Getting Started, Badging Basics, Organization Management & Tech Resources, Marketing & Communications, Program & Earner Management).
- Earner side (directly observed):
  - badge arrives via notification email → recipient accepts it (with an automatic-accept option); acceptance brings the credential into the earner's account;
  - earner dashboard; Badge Wallet and Skills Wallet as separate managed collections; Credly Profile (public profile with customizable header);
  - sharing: to LinkedIn (including the Licenses & Certifications section), embed in websites, attach to email signature, share the profile;
  - mobile app with wallet, sharing, and an "Explore" surface;
  - publish to Blockchain (an earner-facing action — optional, not a default);
  - Transcript feature (credential aggregation) — including a "Transcript Guide for Registrars", i.e., the transcript is consumed by institutional registrars;
  - import outside badges (add credentials earned from other issuers into the profile) — the profile as a cross-issuer collection;
  - account operations: merge accounts, password reset, notification-email management.
- Issuer side (positioning + category structure): "automatically issue verified digital badges to recognize all kinds of achievements"; solutions packaged per audience (employers: L&D / talent acquisition / workforce planning; higher education; product certification providers; professional associations; training providers); network dimension: searchable catalog of credentials from many issuers, skills ontology (Pearson Ontology), workforce-skills-management extensions.
- The network/marketplace layer is this product's distinctive philosophy: credentials live in a shared earner network rather than only on issuer-branded surfaces.

### Certifier

Evidence layer: A (official site; help center unreachable).

- Self-positioning: "Issue and Manage Digital Credentials… generate verifiable certificates, credentials, and badges… run certifications from one place"; product origins as a certificate maker now spanning the full loop.
- The product's own published loop: Design → Generate → Send → Share → Verify → Analyze.
- Design: certificate/badge builder, template library, custom fonts/branding, dynamic attributes; AI-assisted design.
- Generate: bulk generation (recipient groups; CSV), dynamic per-recipient attributes, dynamic QR codes printed on the credential so even printed/downloaded PDF/PNG copies verify.
- Send: branded email delivery with custom sender details and open-rate tracking; mass-export of PDFs; generation of credential URL lists.
- Share: recipients share to LinkedIn (Licenses & Certifications section + feed), Facebook, X, email signatures.
- Verify: "verifiable digital credentials"; OpenBadge 3.0 standard compliance named explicitly; "transform static PDFs into easily verifiable… digital certificates that are always accessible online"; online hosting with login-free recipient access.
- Recipient side: white-label Credential Portal where recipients access and verify all their certificates and badges.
- Post-issuance: credential renewals — expiration dates, automatic email reminders, renewing expired credentials.
- Issuer ops: RBAC and workspaces (teams, per-workspace branding); analytics (downloads, shares, referrals, recipient interactions); API, webhooks, Zapier/Make/Pipedream; integrations: Google Sheets/Forms, Zoom, Microsoft Excel/Forms, Canvas LMS ("issue certificates when courses end"), and more.
- Segments visible in case studies: universities/CPD, corporate cybersecurity training, webinars, events (participation certificates at scale) — participation achievement, not access control.

### Open Badge Factory (OBF)

Evidence layer: A (official site; FAQ path 404, main site detailed).

- Self-positioning: "online platform that large and small organisations around the world use to create, issue and manage their Open Badges"; tagline "Recognising skills together".
- Standards-native artifact philosophy: an Open Badge is "an image that contains verifiable information" — embedded evidence of learning and achievement plus earner and issuer information; the Open Badges standard is presented as guaranteeing portability and trust. 1EdTech certified.
- Three artifact forms: Open Badge (verifiable image), PDF badge certificates (verifiable certificates carrying the same metadata, downloadable/printable/shareable), and micro-portfolios (badges enriched with documentation, endorsements, testimonials in the companion wallet).
- Issuing methods (four classes directly named): bulk issuing (paste recipient emails or upload CSV); API for custom integrations; badge applications (earner-initiated applications against advertised badges — "transform passive badge recipients into motivated and proactive badge applicants"); LMS auto-issuance (plugins for Moodle, Itslearning, LTI; badges issued automatically on course completion).
- Ecosystem layer (distinctive philosophy): organizations share badges and badge application forms with partner organizations; organizations endorse each other's badges to build badge ecosystems; multilingual badges; open participation — endorsers, reviewers, applicants, recipients can engage without prior registration.
- Earner side: Open Badge Passport — free companion wallet where earners receive, store, and share badges and apply for badges advertised by organizations; mobile app; white-label wallet instances for communities.
- Competency frameworks: ESCO and CASE framework alignment for badges/micro-credentials.
- Multi-country, multilingual (EN/FI/FR/JA), 10+ years operating — the European/regional pole.

### Parchment (Instructure) — secondary observation

Evidence layer: A for market structure.

- Badgr (the education-native digital-badging product long associated with Canvas LMS and Open Badges standards work) is no longer marketed at its former domain; Instructure now sells "Parchment Digital Badges" and Parchment Award, which issues "credentials—from transcripts and diplomas to digital badges, CLRs (comprehensive learner records), and certificates".
- Market-structure takeaways: (1) digital badging consolidates into records/credential-exchange suites; (2) credential artifacts sit on a spectrum with official records (transcripts, diplomas, CLR) — the boundary between "achievement artifact" and "official academic record" is drawn by the institution's registrar function, not by artifact format.
- Not used as a primary structural sample; no claims rest on Badgr-specific features.

## Cross-product Comparison

| Dimension | Accredible | Credly | Certifier | Open Badge Factory | Parchment (Award/Badges) |
|---|---|---|---|---|---|
| Primary audience | higher ed, associations, cert/awarding bodies, online learning, employee training | employers, certification providers, associations, higher ed, training providers | SMB/education self-serve; events, webinars, training, CPD | education bodies, NGOs, public-sector, multi-org ecosystems | K-12, higher ed, governments, business |
| Center object | digital credential (badge or certificate) as issuer-branded verifiable page | digital badge in a shared earner network | verifiable certificate/badge with QR | Open Badge (standards-native) + PDF badge certificate | badges/CLRs within records suite |
| Credential design layer | yes (designer; skills/criteria/evidence metadata) | yes (badge creation; robust metadata; skills ontology) | yes (builder, templates, dynamic attributes, AI) | yes (badge design; embedded evidence) | yes (suite) |
| Issuance methods | manual/auto at scale; LMS/CMS integrations | automatic issuance; integrations (issuer categories) | bulk CSV/groups; Zoom/Sheets/Forms/Canvas triggers; API/webhooks | bulk (emails/CSV); API; LMS plugins (Moodle/Itslearning/LTI); earner applications | suite-integrated |
| Recipient claim/accept | one-click acceptance, no account required | email notification → accept (auto-accept option) | login-free access via link/URL | delivery to Open Badge Passport wallet; applications | suite-dependent |
| Recipient holding | white-label wallet cards; credential pages | badge wallet + skills wallet + profile + mobile app | credential portal (white-label) | Open Badge Passport (+mobile, white-label) | network wallet (suite) |
| Sharing | social platforms (claimed 40+), LinkedIn embed, email signature, websites | LinkedIn, embed, email signature, profile share | LinkedIn/Facebook/X, email signature | share via Passport | network exchange |
| Verification | hosted verifiable page; instant third-party verification; fraud-monitoring service | verified badge; optional blockchain publish | hosted page + dynamic QR on printed copies; Open Badge 3.0 | metadata embedded in badge image; hosted records | verified records network |
| Post-issuance state | expiration, renewals, retroactive editing, name-change handling | (earner-side account ops observed; issuer lifecycle per categories) | expiration, reminders, renewal of expired | create/issue/manage posture | suite lifecycle |
| Aggregation | credential transcripts | earner transcript (registrar-consumable) | portal collects per recipient | micro-portfolios | transcripts/CLR (suite-native) |
| Network/marketplace layer | directories (Spotlight), Recommendations, job-market insights | central philosophy: credential catalog + cross-issuer profile import | issuer profile/portal (no earner network emphasis) | org-to-org badge sharing + endorsement; badges advertised for application | credential exchange network |
| Standards named | (not asserted in fetched pages) | (not asserted in fetched pages) | Open Badge 3.0 explicit | Open Badges native, 1EdTech certified, ESCO/CASE | CLR named |
| Blockchain | — | optional publish (earner-facing) | — | — | — |

### Cross-product commonalities (evidence layer B)

1. Two-sided structure: an issuer organization operating the platform, and recipients (earners) who receive, hold, and present credentials. Every sampled product separates these surfaces.
2. The credential is a managed hosted record, not a static file: verifiable via a hosted page/URL or embedded verifiable metadata; one product extends verification to printed copies via QR.
3. Issuance methods converge on a quartet: manual issuance; bulk (email-list/CSV); API/integration; automated issuance from a learning/activity system (LMS course completion, webinar attendance, form submission).
4. Recipient delivery is email-claim based with increasingly frictionless acceptance (one-click / no-account / auto-accept).
5. Recipient holding + sharing is universal: a wallet/collection surface, LinkedIn sharing, embed, email signature, PDF download.
6. Metadata beyond the artifact: skills, criteria, evidence, issuer identity, dates — the credential carries its own justification.
7. Post-issuance issuer control exists in mature products: expiration, renewal, correction/reissue (Accredible "retroactive credential editing"; Certifier renewals). Revocation was not directly observed in fetched pages this pass (see Uncertainties).
8. Branding/white-labeling is a near-universal commercial requirement: credential pages, emails, portals, directories on the issuer's brand/domain.
9. Program analytics (issuance, engagement, shares, referrals) are common in mature products.
10. Standards support (Open Badges family) is common — explicit in Certifier and OBF — but the workflow does not depend on it in all products.

### Non-universal (product/segment-specific)

Blockchain anchoring (Credly, optional); cross-issuer earner networks and credential catalogs (Credly); organizational badge ecosystems/endorsements/earner applications (OBF); program-growth machinery (Accredible); AI-assisted design (Certifier); registrar-consumable transcripts (Credly/Accredible/Parchment).

## Abstraction (four levels)

### L0 — Defining Invariant

A Digital Credential Platform is an issuer-operated platform for awarding verifiable digital credentials to individuals, with this minimal structure:

```text
Issuer (organization)
└── Credential definition (awardable artifact + metadata: name, criteria, issuer, form)
    └── Issuance act (binds a credential instance to an identified recipient, with date)
        └── Issued credential as a hosted, durable record
            └── Verifiability: a third party can confirm authenticity without contacting the issuer
            └── Recipient delivery/access: the recipient can access and present the credential
```

Four properties. Remove any one and it stops being this Type:

1. **Issuer-side credential definitions** — the organization defines what it awards (a reusable awardable object), rather than producing one-off files.
2. **Issuance act binding credential to recipient** — an identified person holds an instance of a defined credential; the record of who earned what, when, from whom.
3. **Hosted verifiable record** — the credential persists as a record the issuer's platform stands behind; a third party can verify it. Without verifiability the product degrades into a certificate generator/print shop, which is not this Type.
4. **Recipient delivery/access** — the credential reaches the person it names and can be accessed/presented by them (the credential is for someone, not just about someone).

### L1 — Common Mature Structure

Very common in mature modern products; not required for the Type:

- design tooling (templates, badge/certificate editors, dynamic per-recipient attributes)
- bulk issuance (email lists / CSV) and API issuance; automation triggers from LMS/webinar/form systems
- email claim delivery with frictionless acceptance (one-click, no-account, auto-accept)
- recipient wallet/collection + public profile; PDF download
- sharing mechanics: LinkedIn (certifications section + feed), embeds, email signatures
- post-issuance lifecycle: expiration, renewal, correction/reissue
- white-labeling of pages/emails/portals/URLs on issuer branding
- program analytics (issuance, engagement, shares, referrals)
- skills/criteria metadata and competency-framework alignment
- standards support (Open Badges 2.x/3.0, verifiable-credential formats)

### L2 — Variant / Optional Structure

- network/marketplace layer: cross-issuer earner profiles, credential catalogs, labor-market insights
- blockchain anchoring of credentials
- aggregated transcripts (earner-facing or registrar-consumable) and comprehensive learner records
- learning pathways / stackable micro-credential chains / milestone credentials
- organizational badge ecosystems: inter-organization badge sharing, endorsement, earner-initiated badge applications
- directories of credential holders; credential-based marketing (recommendations, campaigns)
- fraud-monitoring / ongoing-validation services; print fulfillment of physical certificates
- AI-assisted design; multilingual credentials; white-label wallet instances
- segment packaging: higher-ed micro-credentialing, corporate workforce skills, certification-body issuance, SMB/event participation

### L3 — Vendor-specific (research notes only)

- Accredible: Spotlight, Pathways, Recommendations, Live Credentials, Fraud Monitoring (service names), One-Click Acceptance, "credential flywheel" framing, issuing domains (credential.net, issuer subdomains), marketing scale stats.
- Credly: Acclaim platform name, Pearson Ontology, Badge Wallet vs Skills Wallet split, Top Earners badge, LinkedIn Premium offer for a partner's earners, network scale stats, mobile-app Explore feed.
- Certifier: RBAC/Workspaces, template-library scale claims, AI certificate maker, ISO 27001/GDPR/AWS posture claims, plan limits, recipient-volume stats.
- OBF: Open Badge Passport, Basic/Premium/Pro service levels, 60-day trial, Moodle/Itslearning plugin names, named case studies (AEFE, UNICollaboration, University of Westminster, OAMK).
- Parchment: Award/Pathways/Services product split, "world's largest credential network" claim, GED/HiSET equivalency packaging.

## Vendor-specific Findings

See L3. Additionally:

- Credly is the only sampled product where blockchain publication is an earner-facing feature — optional, not part of any observed default flow.
- OBF is the only sampled product with earner-initiated badge applications as a first-class issuance method and org-to-org endorsement machinery.
- Accredible is the only sampled product packaging fraud monitoring and ongoing credential validation as named services.
- Certifier is the only sampled product marketing dynamic QR codes on printed/downloaded copies as a verification channel.

## Rejected Findings (anti-overfitting)

- **"Open Badges compliance defines the Type"** — rejected. Explicit OB 3.0 compliance was observed in 2/4 primary products; the workflow does not depend on it; standards support is a portability feature. Historical check: credential platforms predate OB 3.0, and the defining structure holds for non-OB products.
- **"Blockchain = digital credentials"** — rejected. Observed in one product as an optional publish action. The canonical verifiability concept is "a third party can confirm the credential," which hosted verification already satisfies.
- **"The artifact is a badge"** — rejected. Certificates (page/PDF-style) are a first-class artifact form in 3/4 primary products; artifact form is a variant axis, not the core.
- **"The Type is education-only"** — rejected. Directly observed segments include employer workforce credentialing, product certification, associations, event participation, and employee training.
- **"The earner network/catalog is the Type"** — rejected as definitional; it is one product philosophy (Credly). Issuer-branded standalone surfaces (Accredible, Certifier) and org-ecosystem surfaces (OBF) satisfy the L0 without any network.
- **"Verification requires a special technology (QR/blockchain/signed JSON)"** — rejected as definitional; the invariant is the existence of third-party verifiability of a hosted record, not the mechanism.
- **"Email is the identity substrate"** — rejected as definitional; email claim delivery is the dominant implementation, but the canonical concept is recipient delivery/access (implementations: claim links, accounts, wallets).

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- Early-generation credential services (hosted PDF certificates with a verification URL/serial lookup, pre-Open-Badges) satisfy all four L0 properties without badges, standards, blockchain, wallets, or networks. The sampled products themselves include such behavior today (Certifier "transform static PDFs into verifiable documents"; OBF PDF badge certificates).
- Regional/EU open-standards products (OBF) fit without any network layer or proprietary verification tech.
- Suite-embedded products (Parchment Award inside a records suite) fit with the artifact layer as the center.
- Pre-platform practice (paper/PDF certificates emailed with no hosted record, no verifiability, no issuer-managed state) is precisely what the sampled products define themselves against — it is the before-state, not a variant.

The L0 survives the historical check; nothing era-specific (Open Badges version, blockchain, QR, wallets, LinkedIn) is inside it.

## Boundary Findings

**vs Certification Management (§25)** — the most important seam. Certification Management runs the program: eligibility, applications, assessment coordination, grant decisions, renewals/CE, audits, revocation of standing. A Digital Credential Platform runs the artifact: once a grant/achievement exists, it defines the credential, issues instances to people, hosts/verifies them, and manages the artifact's lifecycle. Certification bodies are major customers of credential platforms (Accredible and Credly both package product-certification/awarding-body solutions) — a certification program's badge/certificate issuance is exactly the artifact layer this Type owns; the credential platform does not decide who is eligible or whether they passed. Consistent with the certification-management pass's recorded seam ("badges are issuance artifacts"). Keep both Types.

**vs Transcript Management (§23)** — a transcript is the institution's official academic record (courses, grades, awards) exchanged to authorized requesters; a credential platform manages individual achievement artifacts designed for presentation by the earner and verification by anyone. Overlap zone is real and structural: credential platforms aggregate earner transcripts (Credly transcript consumable by registrars; Accredible digital credential transcripts; Parchment issues both transcripts and badges in one suite), and record-exchange suites absorb badging (Parchment/Badgr consolidation). Working seam: registrar-of-record authority vs earner-presentable artifact. When transcript-management is processed, joint review recommended; Parchment is the straddling case.

**vs ePortfolio Platform (§23)** — ePortfolio centers holder-curated work/evidence; credential platform centers issuer-attested achievements. OBF's micro-portfolios (badges + attached documentation/endorsements/testimonials) show the drift pole from the credential side.

**vs Learning Management System (LMS)** — LMS products can issue course-completion certificates/badges natively (Canvas Credentials class; Certifier's Canvas integration "issue certificates when courses end"; OBF's Moodle plugins). The dedicated credential platform differs by being the cross-program system of record: it carries the issuer's credential taxonomy, verification surface, recipient wallets, and post-issuance lifecycle independent of any course container, and integrates with the LMS as a source. LMS-native badging without a hosted verifiable record and issuer-side lifecycle is a capability, not this Type. Worth a note when the LMS leaf is processed.

**vs Identity Verification (§15) / KYC** — identity verification attests who someone is; a credential platform attests what someone achieved, as issued by an organization. No overlap in object class despite shared "verification" vocabulary.

**vs Certificate Lifecycle Management (§14)** — PKI/TLS machine-identity certificates (keys, CAs, rotation). Vocabulary collision ("certificate lifecycle", "issuance", "revocation") but an entirely different object class (machine trust vs human achievement). False friend.

**vs Campus Card Management (§23)** — the prior pass already flagged this leaf as a false friend: campus cards are physical/service-access credentials evaluated at service points; digital credentials are achievement attestations presented to third parties. No shared core.

**vs Event Credential / Badge Management (§26)** — event badges gate physical access at venues. Credential platforms do issue participation artifacts for events (Certifier event case studies), but as achievement records, not access-control objects. Keep separate.

**vs Academic Accreditation Management (§23)** — accreditation attests institutional/program quality to agencies; credentials attest individual achievement to whoever the earner shows them to. Different subject (institution vs person) and different audience (agency vs anyone). Both are organizational attestations — the subject-of-record test separates them.

**Boundary test (removal test), stated for reuse:** remove verifiability/hosted record → certificate generator, not this Type; remove issuance-to-recipient (award definitions only) → a taxonomy tool, not this Type; remove the artifact layer entirely and keep eligibility/assessment/renewal-of-standing → certification management; keep only course-scoped completion records inside the course container → LMS capability.

## Uncertainties

- **Revocation/withdrawal of issued credentials**: expected in this Type (and standard in the Open Badges spec), but not directly observed in any fetched page this pass (Accredible help center unreachable; Credly issuer articles not rendered). The final document therefore describes post-issuance control generically (expiration, renewal, correction/reissue — directly observed) and treats revocation as likely-but-unverified in this sample.
- **Issuer-side workflow granularity for Credly** (badge template editor, issuance-list mechanics, expiration settings) rests on help-center category structure and positioning pages, not article content. No precise issuer-side operational claims are made about Credly.
- **Standards support for Accredible and Credly** (Open Badges export/import etc.) was not directly observed in fetched pages; not asserted in the final document.
- **Parchment Award's standalone badging UX** (post-Badgr consolidation) was not observed beyond naming; no structural claims made.
- The market is consolidating (Badgr→Parchment; Pearson+Credly; large networks); the sample may under-represent mid-market players (Sertifier, VerifyEd, CanCred, Hyland Credentials class) — not needed for stop conditions, but a future pass could widen it.

## Final Synthesis

A Digital Credential Platform is the issuer-side system of record for awarding verifiable digital achievements to people. Its world contains three anchor objects — the credential definition (what the organization awards, with criteria/metadata and a visual artifact form), the issued credential (an instance bound to one identified recipient at a date, hosted as a durable record), and the recipient (the earner who receives, holds, and presents it). Around these sit a mature capability set: design tooling; issuance through manual, bulk, API, and automation-triggered channels; frictionless email-claim acceptance; wallets/profiles; sharing to LinkedIn/social/embed/signature; post-issuance lifecycle (expiration, renewal, correction); white-labeled surfaces; program analytics; and standards-based portability. Optional layers differentiate philosophies: cross-issuer earner networks (workforce pole), org-to-org badge ecosystems (open-standards pole), program-growth machinery (education-marketing pole), and suite consolidation with official records.

The defining discipline of the Type: the platform's product is the verifiable, recipient-presentable, issuer-managed credential record — everything else is program growth tooling. Verifiability (a third party can confirm what the issuer awarded, to whom, when) is the load-bearing property that separates this Type from certificate generators; issuance-to-a-person separates it from badge-design tools; the artifact layer separates it from certification program management; and earner-presentability separates it from registrar records.

