# Research Notes — Digital Risk Protection

Research date: **2026-09-08**

## Research Goal

Understand what a Digital Risk Protection (DRP) application actually is as an Application Type: what objects exist inside it, what the operational loop is, who operates it, and where its boundaries sit against the neighboring security Types already documented in the Atlas (dark-web-monitoring, attack-surface-management) and the neighboring marketing/social Types (social listening, brand reputation management), plus unprocessed siblings (threat-intelligence-platform, email-security-gateway).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: DRP = external threat monitoring focused on the organization's *brand/identity footprint* (domains, social accounts, apps, executives) rather than its *infrastructure*, with some form of removal/enforcement action against found abuse.
- Likely confusions: Threat Intelligence Platform (knowledge about threats vs protection of own identity), Dark Web Monitoring (source-scope overlap), Brand Reputation Management (namesake "brand" + "protection"), Social Listening (external observation), Email Security (phishing overlap), Attack Surface Management (both "outside-in"), Fraud Prevention (both "abuse").
- This leaf carries an open joint-review flag from the dark-web-monitoring pass: "clear-web brand abuse + takedown workflow (DRP)" vs "subject's exposures surfacing in hidden/illicit source economies (DWM)"; the source-scope removal test was to be applied in this pass.

## Research Questions

1. What is the protected object — what does the customer configure for monitoring? (the "footprint")
2. What sources do products collect from, and which are definitional vs optional?
3. What does a "finding" look like and what lifecycle does it carry?
4. Is the takedown/enforcement path definitional or optional? Who executes it (customer, vendor analysts, automation)?
5. How do DRP products integrate with the wider security stack (SIEM/SOAR/ticketing)?
6. Where exactly are the seams vs dark-web-monitoring, TIP, ASM, social listening, brand reputation management, email security?
7. Would older/regional/platform-native products still fit the definition (historical check)?

## Representative Products

Chosen for market representation + different product philosophies + different packaging poles:

| Product | Pole | Access this pass |
|---|---|---|
| **Axur** (Takedown / Brand Protection platform; LatAm-origin pure-play, now Infoblox-owned) | pure-play DRP suite with takedown as flagship pillar | ✅ product pages (home, /takedown, /brand-protection), rich |
| **Fortinet FortiRecon** | platform-suite module ("Brand Protection" + "Takedown Services" inside CTEM/exposure-management bundle) | ✅ product page, rich |
| **Proofpoint Email Fraud Defense / DRP heritage (PhishLabs)** | email-security vendor pole: lookalike-domain detection + "Virtual Takedown Service" adjacent to DMARC/gateway products; legacy "Digital Risk Portal" login still listed | ✅ product pages + DRP glossary article |
| **ZeroFox** (market-leading pure-play; absorbed Digital Shadows + IntSights) | unreachable: site 403 + docs transport error (×2 attempts) | ❌ structural position recorded via sibling passes |

Additional anchors: Recorded Future (TIP with brand module) — support + main site timed out ×2, abandoned per network rules. Check Point (Cyberint heritage, now "Exposure Management") — deep-link 404; nav confirms re-packaging; not pursued further.

## Sources

- https://www.axur.com/ (product suite nav: Takedown, CTI, Deep & Dark Web, Online Piracy, EASM, Brand Protection, Threat Hunting, Executives & VIPs, Data Leakage, API & Integrations) — fetched 2026-09-08
- https://www.axur.com/en-us/takedown — fetched 2026-09-08
- https://www.axur.com/en-us/brand-protection — fetched 2026-09-08
- https://www.fortinet.com/products/fortirecon — fetched 2026-09-08
- https://www.proofpoint.com/us/products/email-protection/email-fraud-defense — fetched 2026-09-08
- https://www.proofpoint.com/us/threat-reference/digital-risk ("What Is Digital Risk?") — fetched 2026-09-08
- Sibling-pass recorded observations: STATUS.md entries for dark-web-monitoring (2026-09-07), attack-surface-management (2026-09-06), brand-reputation-management (2026-09-06), social-listening-platform (2026-09-07)

**Source-access limitations:** ZeroFox (site 403, docs unreachable), Recorded Future (timeouts ×2), Check Point deep links (404), Axur docs portal (redirect loop, abandoned after 2 attempts). Evidence therefore rests on Tier-2 official product pages (rich, multi-page) for three reachable products, not on Tier-1 help-center articles. Per the evidence rules: no precise operational numbers from vendor marketing are carried into the final document; all quantitative vendor claims (SLAs, success rates, monitored-domain counts) stay here in Research Notes as vendor marketing claims, not verified operational facts.

## Product A — Axur (Evidence Layer A: directly observed)

From /takedown and /brand-protection pages:

- **Suite structure** (separate pillars sold side by side): Takedown, Brand Protection, Cyber Threat Intelligence, Threat Hunting, Deep & Dark Web Intelligence, Online Piracy, Executives & VIPs, External Attack Surface Management, Data Leakage, API & Integrations. DRP-shaped work is explicitly decomposed into "Takedown" (enforcement) and "Brand Protection" (detection of impersonation/phishing/abuse).
- **Monitored scope configuration**: "brand scopes (names, domains, variations)" configured as rules; automation rules configurable by brand, country, or business line.
- **Monitored source classes**: URLs/domains (typosquatting, cybersquatting, phishing pages), social media (fake profiles, fraudulent ads), app stores + APK mirror sites (unofficial/malicious apps), marketplaces (counterfeit listings), paid search/ads, malware distribution URLs, C2 infrastructure, deep & dark web.
- **Detection claims**: AI model detecting visual brand abuse "even when there are no keywords, logos, or direct references" (claims that 70% of malicious sites don't carry the brand in the domain, 18% not in the HTML — vendor marketing, not verified).
- **Evidence capture**: automated screenshots, HTML, headers, WHOIS/hosting data, "emulated across devices, languages, and geolocations"; "ready for legal notifications".
- **Takedown workflow** (the flagship loop): detect → decide actionable (filter false positives/out-of-scope fraud) → craft notification → send to host/platform → read response → interpret outcome → escalate/follow-up/close. "One-click or zero-touch takedowns"; incident timeline with real-time status; "stay-down" monitoring with automatic re-takedown if content resurfaces; "Web Safe Reporting" notifies browsers/antivirus vendors (Google Safe Browsing-class red screens) "even before the URL's content is fully removed".
- **Enforcement channels**: direct reporting channels with major platforms (Meta named), marketplaces (Mercado Livre named), hosts/registrars, "15+ top-tier entities" for browser-alert reporting (vendor claim).
- **Integrations**: Splunk, QRadar, Microsoft Sentinel, InsightIDR, Elastic, ServiceNow, n8n, webhooks — SIEM/SOAR/ticketing/collaboration.
- **Roles/tenancy**: role-based access, unlimited users claimed; MSSP partner program ("Become an MSSP"); multi-brand operation.
- **Verticals**: finance/fintech (phishing, fake apps), e-commerce/retail (fake profiles, ads, marketplace listings), SaaS/tech (fake support domains, cloned login pages).
- **Vendor marketing numbers** (kept out of final doc): first notification <4 min; 98.9% takedown success; 9h median removal; 15-day stay-down guarantee; pay-only-for-successful-takedowns commercial model; 2M+ lifetime takedowns; 40M new sites/day ingested; 88k fake profiles/year.

## Product B — Fortinet FortiRecon (Evidence Layer A: directly observed)

From the FortiRecon product page:

- **Packaging**: SaaS "threat exposure management" (CTEM) service with four modules — Attack Surface Management, Adversary Centric Intelligence, **Brand Protection**, Security Orchestration. DRP work = the Brand Protection module + "Takedown Services" feature.
- **Brand Protection module scope**: "monitor, detect, and take down fake domains impersonating real ones"; "brand and executive impersonations, rogue mobile applications on multiple app stores, data leaks in code repositories, open bucket exposures, phishing campaigns, and helps protect executive online presence."
- **Feature list**: "Identification & Mitigation of Brand Attacks — Alerts and takes down threats to your brand such as fake websites, mobile apps, social media accounts"; "Takedown Services — Provides rapid response using FortiGuard Labs' takedown services" (vendor-operated enforcement via the vendor's threat-research organization).
- **Adjacent capabilities in same bundle**: dark web / OSINT / technical intel (ACI), ransomware intel, leaked credentials & card-fraud monitoring on darknet marketplaces, supply-chain/vendor risk, MITRE ATT&CK mapping, SIEM/SOAR orchestration.
- **Positioning drift**: product now titled "Threat Exposure Management"/CTEM, not "DRP" — the DRP capability set is preserved but re-labeled inside the exposure-management umbrella.

## Product C — Proofpoint (Evidence Layer A: directly observed)

From Email Fraud Defense page + "What Is Digital Risk?" glossary:

- **Email Fraud Defense** (current packaging of the email-adjacent slice): continuous domain monitoring across "more than 650 million domains across WHOIS data sources" (vendor claim); "dynamically identify lookalikes of your domains registered by people outside of your organization"; "see which of your domains attackers have attempted to hijack"; **"proactively address malicious lookalikes of your domain with our Virtual Takedown Service."** Supplier lookalike risk visibility. Hosted SPF/DKIM/DMARC. Gateway integration for inbound enforcement.
- **Heritage**: login list still carries a "Digital Risk Portal" (v1.us1.digitalrisk.proofpoint.com) — the legacy DRP platform surface (PhishLabs heritage) persists alongside the repositioned email-fraud product.
- **Field framing** (glossary, vendor's own definition of the category): DRP forms include digital footprinting (discovering/mapping exposed digital assets), continuous monitoring of exposed assets, threat intelligence, "digital risk protection service (DRPS)" as a comprehensive *managed service* form "that typically offers a platform…to spearhead cybersecurity threat prevention", multidimensional threat analysis, sensitive data leakage monitoring.
- **Boundary-relevant**: DMARC/email-authentication machinery is about authorizing the org's *own* sending; lookalike detection + takedown is about *others'* abuse of the org's identity — both sold by the same vendor as distinct products.

## Product D — ZeroFox (unreachable; structural record)

Site 403, docs transport error. Position recorded from the sibling dark-web-monitoring pass (2026-09-07): ZeroFox (with Digital Shadows SearchLight and IntSights absorbed) sells "Dark Web Monitoring" and "Brand Intelligence & Protection" as **distinct solutions** — i.e., the market's leading pure-play itself separates the DWM Type from the DRP Type. No new claims made from this product this pass.

## Cross-product Comparison

| Dimension | Axur | FortiRecon | Proofpoint (EFD/DRP) |
|---|---|---|---|
| Monitored object = customer's external brand/identity footprint (domains, social personas, apps, executives) | ✅ brand scopes: names/domains/variations, per brand/country/business line | ✅ brand + executive impersonation, fake domains/apps | ✅ own domains + lookalikes registered by outsiders |
| Standing external detection of impersonation/abuse | ✅ multi-source (domains, social, app stores, marketplaces, ads, malware, D&W) | ✅ fake domains, rogue apps, phishing campaigns, code-repo leaks, bucket exposures | ✅ lookalike domain monitoring at scale |
| Enforcement-to-removal path with tracked case lifecycle | ✅ flagship: notify→track→verify→re-takedown, incident timeline | ✅ "Alerts and takes down" + Takedown Services | ✅ Virtual Takedown Service |
| Evidence capture per finding (screenshot/HTML/WHOIS/hosting) | ✅ automated forensic evidence | ✅ (implied: detection module outputs; not detailed on page) | ✅ domain registration detail (WHOIS-class) |
| Triage/actionability decision step | ✅ explicit (filter false positives, out-of-scope fraud) | ✅ prioritization via orchestration | ✅ risk classification of lookalikes |
| SIEM/SOAR/ticketing integrations | ✅ named SIEMs, ServiceNow, webhooks, n8n | ✅ orchestration module w/ playbooks | ✅ gateway + email ecosystem integration |
| Dark web / leaked-data sources included | ✅ as separate pillar + source class | ✅ as separate module (ACI) | ✅ heritage DRP platform; EFD itself is email/domain-focused |
| EASM as sibling | ✅ separate pillar | ✅ separate module | ✖ (not in EFD) |
| Vendor-operated enforcement service framing | ✅ (platform-first, agentic) | ✅ explicit (FortiGuard Labs' takedown services) | ✅ explicit ("Virtual Takedown Service") |
| Packaging pole | standalone pure-play suite | platform CTEM module | email-security vendor adjacent product |

**Cross-product commonality (Layer B):** every reachable sample = (1) customer-configured external brand/identity footprint, (2) standing detection of third-party impersonation/abuse of it across public external sources, (3) an enforcement path that ends in removal, tracked as a case. Evidence capture, triage, integrations, and roles recur across samples. Dark-web and data-leak sources appear as *adjacent modules/pillars*, separable from the brand-abuse core — consistent with the dark-web-monitoring pass's finding.

## Canonical Model (abstraction)

### L0 — Defining Invariant (jointly-held; remove any → different Type)

1. **The protected external footprint** — the customer's brand/identity as it exists *outside* its perimeter (domain names, social platform identities, mobile apps, executive personas, customer-facing email domains), configured as the monitoring subject. Remove → threat intelligence has no protected subject; ASM has no own-infrastructure inventory.
2. **Standing detection of third-party impersonation/abuse of that footprint** — continuous collection across public external sources producing findings attributed to the protected footprint (fake domains, fake profiles, rogue apps, phishing pages abusing the brand). Remove → nothing to protect.
3. **The enforcement-to-removal path** — action taken against found abuse through abuse-report channels (hosters, registrars, platforms, app stores, browser/AV blocklist reporters) with a tracked case from detection to resolution. Takedown is the characteristic action; who executes (customer, vendor analyst, automation) is variant. Remove → monitoring/alerting only — brand-abuse listening, not protection.

Jointly-held is load-bearing:
- 1+2 without 3 = brand-abuse monitoring/alerting service (social listening in security dress)
- 1+3 without 2 = a takedown filing service with no detection engine
- 2+3 without 1 = generic anti-phishing clearinghouse / blocklist reporting with no owned protected subject

### L1 — Common Mature Structure

- Multi-source collection fabric: newly registered/lookalike domains, social platforms, app stores & APK mirrors, marketplaces, ad/paid-search platforms, phishing kits/pages, code-repository leaks, open storage buckets
- Per-finding evidence capture (screenshots, page HTML, WHOIS/registration + hosting data, headers), captured forensically for notification/legal use
- Triage/actionability decisioning (false-positive filtering, severity/impersonation scoring, prioritization)
- Case lifecycle with status tracking, escalation/follow-up, resolution verification, and stay-down re-checks
- Integration spine: SIEM/SOAR/ticketing/webhooks/API; role-based access; multi-brand/multi-entity scoping
- Reporting on removal outcomes and exposure trends

### L2 — Variant / Optional Structure

- **Source-breadth extensions**: dark web/deep web watching, credential & data-leak monitoring, card-fraud monitoring (overlaps dark-web-monitoring as sibling Type, commonly bundled as module/pillar), piracy/counterfeit enforcement (legal/IP flank)
- **Delivery posture**: self-operated platform vs DRPS managed service (vendor analysts run detection+enforcement) vs MSSP packaging — the DRPS managed-service form is named as such in the field's own vocabulary
- **Automation level of enforcement**: manual filing → one-click vendor filing → fully automated notification → AI-agent end-to-end (current-gen drift)
- **Channel emphasis**: email-domain-centric (lookalike + takedown adjacent to DMARC), social-centric, domain-centric
- **Commercial model**: per-seat vs per-takedown/outcome-based (one sampled vendor)
- **Suite repackaging drift (2024–2026)**: big-portfolio vendors fold DRP under "Exposure Management / CTEM / External Risk Management" umbrellas (Fortinet, Check Point) while pure-plays keep DRP-shaped pillars
- **Vertical tuning**: finance/fintech, e-commerce/retail, SaaS

### L3 — Vendor-specific (research notes only)

- Axur: "Clair" visual AI model; "Web Safe Reporting" (browser/AV pre-removal blocklist notification); 15-day stay-down guarantee; pay-only-on-success billing; "Axur University" training; claims: <4min notification, 98.9% success, 9h median, 2M+ takedowns, 40M sites/day, 88k profiles/year.
- Fortinet: FortiGuard Labs takedown services; Adversary Centric Intelligence module; MITRE ATT&CK mapping; card-fraud monitoring on darknet marketplaces; CTEM framing.
- Proofpoint: "Virtual Takedown Service"; Supplier Risk Explorer; Hosted SPF/DKIM/DMARC; 650M-domain monitoring claim; legacy "Digital Risk Portal" login surface.
- ZeroFox/Digital Shadows/IntSights/Recorded Future: unreachable this pass; only structural positions from sibling passes.

## Historical / Market-Sample Check

- **Pre-"DRP" era (late 2000s–2010s)**: phishing-takedown service firms (detect phishing targeting the brand → email abuse desks of hosters/registrars → track to removal) satisfy all three L0 structures without AI, cloud dashboards, or dark-web sources — enforcement was analyst-operated email/fax-class correspondence. Domain-monitoring/brand-protection firms (typosquat watch + UDRP/enforcement) also fit.
- **Platform-native / regional**: regional pure-plays (LatAm sample) fit directly; platform-suite module packaging (Fortinet pole) fits as module.
- **Counter-examples that must NOT fit** (boundary validation): a credential-leak alerting service with no clear-web footprint protection and no enforcement → dark-web-monitoring; a sentiment/mention listening tool → social listening; a DMARC deployment tool alone → email-authentication territory; vulnerability scanning of own assets → ASM/VM.
- Conclusion: the definition survives the historical check; enforcement-as-a-service (manual era) and enforcement-as-automation (current) are postures of the same invariant.

## Vendor-specific Findings

See L3 above. The most consequential: outcome-based commercial models tied to takedown success (single-product evidence → product-specific); browser/AV pre-removal blocklist reporting as a distinct enforcement channel (single-product evidence on a named page → product-specific, though other vendors offer comparable "takedown + blocklist" combos per market knowledge — not asserted).

## Boundary Findings

| Neighbor | Test / distinction | Status |
|---|---|---|
| **dark-web-monitoring** (processed) | Source-scope removal test: restrict monitoring to hidden/illicit source economies (dark web, underground forums, closed chats) → dark-web-monitoring; restrict to clear-web brand impersonation + enforcement → this Type. Vendors keep them as separate pillars/solutions (both sampled suites; ZeroFox per sibling pass). Dark-web sources may appear *inside* DRP as optional module — overlap zone is brand terms watched on illicit sources. | DISCHARGES the dark-web pass's joint-review flag from this side; keep-both ratified |
| **threat-intelligence-platform** (unprocessed) | TIP = curated knowledge about actors/IOCs/vulnerabilities for the security program (no protected footprint, no enforcement); DRP = protection loop over the customer's own external identity with enforcement. Straddle: TIP vendors sell brand-intelligence modules (Recorded Future per market structure; unreachable this pass). | Flag joint review for the TIP pass |
| **attack-surface-management** (processed) | ASM = discovery/exposure of the org's *own* infrastructure from outside; DRP = detection of *third-party* abuse of the org's identity. Consistent with ASM pass's "brand abuse vs infrastructure" row. Same suite bundles both as separate modules (FortiRecon; Axur pillar). | Confirmed from this side |
| **brand-reputation-management** (processed) | Reputation loop = external feedback signals + per-signal organizational response (public replies, review solicitation) + tracked sentiment; DRP = malicious abuse findings + enforcement. Namesake overlap only. | Confirmed (consistent with that pass) |
| **social-listening-platform** (processed) | Listening = standing queries over public conversation for *insight*; DRP = abuse findings feeding *enforcement*. Observation vs operation; different finding semantics (impersonation/fraud vs sentiment/themes). | Held |
| **email-security-gateway / email-authentication-DMARC-management** (unprocessed) | Gateway = inbound message filtering; DMARC management = authorizing own sending. DRP overlaps at lookalike-domain detection + takedown, sold as a distinct adjacent product by the email vendor (Proofpoint evidence). DRP's deliverable is removal of external abuse, not mail-flow control. | Flag for both passes when processed |
| **fraud-prevention-platform / account-abuse-protection** (unprocessed) | Those types decide on *customer activity* (transactions/logins) inside the org's own systems; DRP acts on *external attacker infrastructure impersonating the org*. Complementary, distinct protected objects. | Held (brief) |

## Uncertainties

1. Whether "alert-only" DRP tiers exist as genuine no-enforcement products, or whether enforcement is always purchasable somewhere in the Type. Sampled evidence: all three reachable products include takedown; tier-level gating (enforcement as paid add-on) is plausible but not directly evidenced → final doc treats enforcement as definitional at Type level and notes tier/plan gating as packaging.
2. ZeroFox/Recorded Future evidence is structural, not direct; the pure-play market-leader pole is under-evidenced this pass (documented limitation; no numeric or workflow claims made from them).
3. Precise SLA/success/coverage numbers are vendor marketing; deliberately excluded from the final document.
4. Exact legal instruments behind enforcement (ToS-based platform reports vs trademark/UDRP claims vs registrar abuse policies) vary by channel; products did not expose this detail on public pages → final doc describes channels generically.

## Final Synthesis

Digital Risk Protection = the security-side protection loop over an organization's external identity: configure the protected brand/identity footprint → standing external detection of impersonation/abuse → evidence-rich triage → enforcement (takedown) tracked to verified removal → integrate outcomes into the security program. Its defining trio is footprint + abuse detection + enforcement; everything else (dark web, EASM, piracy, managed service, automation depth, channel emphasis) is variant or adjacent-module. The Type is the clear-web, enforcement-carrying sibling of dark-web-monitoring and the identity-abuse sibling of attack-surface-management.
