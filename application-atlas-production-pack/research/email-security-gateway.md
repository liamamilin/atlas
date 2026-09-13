# Research Notes — Email Security Gateway

Research date: 2026-09-08
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an Email Security Gateway (ESG / SEG) actually is as an Application Type: where it sits in an organization's mail flow, what objects and verdicts it works with, how administrators and end users interact with it, and how it is bounded against neighboring Types (Email Authentication/DMARC Management, Email Infrastructure Management, DLP, Secure Web Gateway, and the newer API-based email security products).

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: an ESG is a security checkpoint placed in an organization's inbound email flow that inspects each message before it reaches user mailboxes, renders a verdict (spam / malware / phishing / legitimate), and acts on the message (deliver, quarantine, reject, alter).
- Likely confusion points:
  - The newer API-based ("integrated cloud email security") products — same threat mission, different position in the mail flow (post-delivery).
  - Email Authentication / DMARC Management — anti-spoofing appears in both, but that Type manages the org's OWN sending domain.
  - Email Infrastructure Management — that Type is the outbound sending pipeline (processed 2026-09-08); the gateway is the receiving-side control.
  - Consumer/client junk filters — inspection+verdict+action exist there too, but no organizational control plane.
- Carried flag from the digital-risk-protection pass: email vendors sell lookalike-domain detection + takedown as an adjacent product; keep the seams on deliverable-of-record (DRP = removal of external identity abuse; gateway = inbound filtering).

## Research Questions

1. Where exactly does the product sit in the mail flow (MX inline vs API post-delivery)? Is the mail-flow position definitional for "gateway"?
2. What is the processing pipeline for an inbound message (connection → content → attachment → URL → delivery decision)?
3. What verdict taxonomy exists, and what actions can be taken per verdict?
4. What is the quarantine model (holding state, retention, admin vs end-user release)?
5. What is the policy model (scoped policies, priorities, allow/block lists, defaults)?
6. How do users participate (quarantine digests, release, reporting, banners)?
7. What outbound functions exist (outbound spam/malware, DLP, encryption) and are they definitional?
8. How do the sampled products realize the "gateway vs API" split, and is the split a variant within one Type or a boundary between Types?
9. Would older appliance-era / platform-native / open-source relay implementations still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tiers:

1. **Microsoft Exchange Online Protection / Defender for Office 365** — platform-native pole: protection bundled with the mail platform itself; by far the best public operational documentation.
2. **Mimecast (Advanced Email Security / Email Security Cloud Gateway + Cloud Integrated)** — cloud gateway pure-play pole (since 2003); documents BOTH deployment modes explicitly.
3. **Proofpoint (Core Email Protection)** — enterprise suite pole; documents the "via API or secure email gateway (SEG)" duality and SEG-vs-API selection guidance.
4. **Barracuda (Email Protection family)** — SMB/mid-market + MSP pole, appliance heritage lineage; documents the newer API-first mode.
5. **Abnormal AI (formerly Abnormal Security)** — boundary pole: API-only, behavioral, positions itself explicitly as a SEG replacement ("Displace Your SEG"). Sampled to locate the Type's edge, not as a core member.

## Sources

Fetch status on 2026-09-08:

| Product | Source | Tier | Status |
|---|---|---|---|
| Microsoft | learn.microsoft.com/defender-office-365/eop-about (Built-in security features for all cloud mailboxes) | Tier 1 | OK |
| Microsoft | learn.microsoft.com/defender-office-365/anti-spam-protection-about | Tier 1 | OK |
| Barracuda | barracuda.com/products/email-protection | Tier 2 | OK |
| Barracuda | campus.barracuda.com documentation portal | Tier 1 | FAILED — portal restructured; documentation.campus.barracuda.com returned empty (SPA) |
| Proofpoint | proofpoint.com/us/products/email-security-and-protection (Core Email Protection) | Tier 2 | OK |
| Proofpoint | docs.proofpoint.com/docs/email-protection | Tier 1 | FAILED — transport error |
| Proofpoint | help.proofpoint.com | Tier 1 | FAILED — sign-in wall |
| Mimecast | mimecast.com/products/email-security/ | Tier 2 | OK |
| Mimecast | mimecastsupport.zendesk.com (support center + product-update listings + search) | Tier 1-ish | OK |
| Abnormal AI | abnormal.ai (homepage/platform nav) | Tier 2 | OK |
| Abnormal AI | abnormal.com | — | FAILED — domain occupied by an unrelated personal site; product confirmed to have moved |

Source-access limitations: Proofpoint operational/admin documentation is login-gated — all Proofpoint observations are product-page level and weaker. Barracuda technical documentation was unreachable — Barracuda observations are product-page level. Abnormal: no operational documentation fetched; used only as boundary evidence. Microsoft evidence is the strongest (Tier 1 operational docs) and anchors the canonical pipeline description; its specifics are checked for generalization before use in the final document.

## Product Observations

### Microsoft — Exchange Online Protection (EOP) / Defender for Office 365 [Evidence: A — Tier 1 docs]

**Position in mail flow.** "Incoming messages in Microsoft 365 initially pass through connection filtering… The message passes through anti-spam and anti-phishing filtering… A message that successfully passes all of these protection layers is delivered to the recipients." Servers "accept messages on your behalf, providing a layer of separation between the servers that host your organization and the internet." EOP is also sold standalone "to protect on-premises email environments (not just Microsoft Exchange)."

**Processing pipeline (inbound).**
1. Connection filtering — sender/IP reputation; "Most spam is rejected at this point."
2. Anti-malware — message + all attachments inspected; malware → quarantine (admin-only view by default; quarantine policies define what users may do).
3. Mail flow rules (transport rules) evaluated.
4. Anti-spam + anti-phishing filtering → verdict + configured action.
Delivery happens only after all layers pass.

**Verdict taxonomy.** Spam / High confidence spam / Phishing / High confidence phishing / Bulk (BCL threshold). High confidence phishing is "always quarantined" (secure by default); users cannot release it, only request release.

**Actions per verdict (directly documented table).** Move to Junk Email folder; Add X-header; Prepend subject line; Redirect to other recipients; Delete (silently, incl. attachments); Quarantine (with a quarantine policy + retention setting); No action (available for Bulk). Spam filtering cannot be fully turned off.

**Quarantine.** Admin-managed + end-user surfaces ("Find and release quarantined messages as a user"; "quarantine notifications"); quarantine policies define per-verdict what users may do and whether they get notifications; retention is bounded and configurable (documented range: 1–30 days), after which messages are deleted irrecoverably.

**Policy model.** Recipient filters = users / groups / domains (conditions and exceptions with AND/OR logic documented); custom policies with priority order — "Policy processing stops for eligible recipients after the application of the first eligible policy"; a non-deletable default policy "always applied last"; Standard/Strict preset security policies take precedence over custom ones.

**Allow/block lists.** Per-policy allowed/blocked senders and domains + a tenant-wide Tenant Allow/Block List. Direct evidence for a load-bearing rule: "Messages from entries in the allowed senders list or the allowed domains list bypass most email protection (except malware and high confidence phishing) and email authentication (SPF, DKIM, and DMARC) checks… These lists are best used for temporary testing only. Never add common domains… Attackers can easily send spoofed messages from these common domains."

**Outbound.** Outbound anti-spam protection is a separate policy family; control of automatic external email forwarding.

**Post-delivery.** Zero-hour auto purge (ZAP) "able to act on messages *after* they're delivered" for phishing/spam/malware.

**Feedback loop.** Admin submission + user-reported messages ("report false positive / false negative"); anti-spam message headers for diagnosing why a message was filtered.

**Exceptions.** Advanced delivery policy for SecOps mailboxes and phishing simulations; mail flow rules can set the spam confidence level to bypass filtering "if you route email through a non-Microsoft protection service or device before delivery to Microsoft 365" — direct evidence that gateways STACK (third-party gateway in front of platform-native protection).

**Other.** Intra-organizational (internal-to-internal) messages can also be subjected to verdict actions; Directory Based Edge Blocking rejects mail to invalid recipients; message trace and email security reports; anti-spoofing (spoof intelligence) and email-authentication checks are part of inbound processing.

### Mimecast [Evidence: A/B — Tier 2 product page + support-center listings]

**Two product lines confirmed by official support center:** "Email Security Cloud Gateway (MX)" (abbreviated CG) and "Email Security Cloud Integrated" (API-based, abbreviated CI). Product page: "email security delivered with or without a gateway."

**MX-based deployment (the gateway realization).** "All incoming mail routes through Mimecast's secure gateway first — intercepting threats in line." "Deploy across any email platform with advanced mail routing and custom multi-rule policies tailored to your organization." "Stay protected and operational even if your primary mail server goes down, with built-in continuity and inline threat inspection." Supports M365, Google Workspace, on-premise and hybrid.

**API-based deployment.** "Connect via API in minutes — no MX record changes, no mail flow disruption"; "largely pre-configured settings and automated remediation."

**Detection machinery (product page).** AI/ML across "trillions of emails" heritage claim (marketing, not operational); sandboxing; on-click URL protection; computer vision for brand/login-page impersonation; contextual email banners; QR-code phishing; BEC; social-graphing anomaly detection.

**Support-center listings (feature surface confirmation, A-level for existence).** Quarantine operations ("Delete from Quarantine", "Restore Remediated Messages", "Alerts for Malware and Phishing Quarantine"); "Notification Sets - Digest Email"; policy machinery ("Blocked Senders Policy Management", "Block Dangerous File Types", "Custom Header", "Geographical Restrictions Policy Enhancements"); URL protection ("URL Pre-Delivery Action", "Real-Time Scan Details & Verdict Reporting", QR-code scanning in both CG and CI); "DNS Authentication - Inbound Notification" (inbound SPF/DKIM/DMARC evaluation); Account Takeover detection in MX and gateway lines; "Advanced Business Email Compromise Protection" incl. "Monitor Mode Policy" and "User Holds"; DANE on outbound for the gateway; "Case Review" surfaces; end-user portal / personal portal / Outlook add-in; suite pillars: Continuity, DMARC Analyzer (sibling-Type product), Security Awareness Training/Engage, Email Archive, Managed Threat Response (analyst service), SIEM/XDR integrations.

### Proofpoint [Evidence: A at page level / B overall — Tier 2 only; admin docs gated]

**Deployment duality (headline).** "Deploy industry-leading email protection via API or secure email gateway (SEG)."

**SEG vs API selection guidance (FAQ — direct quote-level evidence).**
- Choose API: "Rapid deployment without MX changes; Tight integration with Microsoft 365 or Google Workspace; Strong post-delivery detection and automated remediation; Low maintenance."
- Choose SEG: "Fine-tuned pre-delivery filtering and routing control; Rich DLP and policy customization; Additional support for hybrid or complex email systems."
- "Many organizations adopt a hybrid model, combining API-based post-delivery coverage with SEG pre-delivery defenses."

**Post-delivery detection (FAQ).** Rescan of delivered messages with updated intelligence; "Automated quarantine: once confirmed malicious, the message is pulled from all inboxes, including forwarded copies"; behavioral anomaly detection on internal messages to flag account takeover.

**Detection scope.** BEC, ransomware, phishing, account takeovers; sandboxing for malicious URLs and attachments; lookalike domain analysis; computer vision; prompt-injection defense; "Integrated outbound protections" (comparison table).

**End-user layer.** "Real-time coaching for suspicious mail, with behavioral learning for spam and graymail"; misclassified-email handling (malicious/suspicious/safe); agentic automation for abuse-mailbox review.

**Adjacent modules (separate products).** Email Fraud Defense (brand/DMARC/lookalike domains), Adaptive Email DLP, Account Takeover Protection, Secure Email Relay, awareness training (ZenGuide), archiving/compliance (Digital Communications Governance). This confirms the product-straddle pattern flagged by the digital-risk-protection pass.

### Barracuda [Evidence: A at page level — Tier 2 only; technical docs unreachable]

**Product family.** "Barracuda Email Protection" with use-case modules: "Spam, Malware, and Advanced Threat Protection"; "Integrated Email Protection" (marked New — API-based); "Incident Response"; "Account Takeover Protection"; "Domain Fraud Protection (DMARC)"; "Security Awareness Training"; "Email Encryption"; "Cloud Archiving"; "Microsoft 365 Backup."

**API-first mode.** "Connects to Microsoft 365 or Google Workspace with no mail exchange (MX) changes — operational in minutes"; "Automated Remediation — agentic clawback removes threats across all mailboxes in near real-time"; bulk actions across mailboxes/tenants.

**Post-delivery framing.** "Modern attacks look legitimate at delivery. Later, links rewrite and payloads activate… point-in-time detection is insufficient — continuous monitoring is required." Barracuda IQ "continuously re-evaluates risk after delivery."

**Deployment breadth.** Dedicated "Protect Microsoft 365" and "Protect Google Workspace" pages; site-wide "On-Premises Deployment Options… cloud-connected appliances and software" (weak, site-level evidence for the appliance/on-prem pole).

### Abnormal AI [Evidence: A at page level — Tier 2; boundary pole]

**Not a gateway.** "Cloud-Native API Architecture — ingests thousands of behavioral signals"; "Activate in minutes — no agents, no MX changes." Has a dedicated solution page: "Displace Your SEG — Modern email security"; customer story: "Valvoline Replaces SEG with Autonomous AI."

**Capability span overlaps the gateway Type's threat classes.** Inbound Email Security (phishing, malware, BEC, QR, GenAI attacks), Account Takeover Protection, AI Security Mailbox (autonomous triage & response), Email Productivity (reduce unwanted email), AI Phishing Coach, Posture Management (identifies misconfigurations), Misdirected Email, Email DLP Rules, Messaging Security (Slack/Teams).

**Interpretation.** The API-pole competes for the same mission (protect the organization from email-borne attacks) but occupies a different position (post-delivery, no mail-flow checkpoint). It is the sharpest live boundary for the leaf: remove the inline mail-flow checkpoint and the product is a different deployment family — the vendors themselves frame it as SEG replacement vs SEG.

## Cross-product Comparison

| Dimension | Microsoft EOP/MDO | Mimecast | Proofpoint | Barracuda | Abnormal |
|---|---|---|---|---|---|
| Position in mail flow | inline (platform-native, before mailbox delivery) | MX-based gateway (CG) — "routes through… first — intercepting threats in line" | "via API or secure email gateway (SEG)" | classic MX gateway heritage + new "no MX changes" API mode | API only — "no MX changes" |
| Connection-level filtering (IP/reputation) | yes (documented) | gateway heritage implies yes; not directly re-fetched | not visible at page level | not visible at page level | n/a (no connection role) |
| Content verdicts (spam/phish/malware classes) | yes — named verdict ladder | yes — graymail/spam/malware/phish categories named in updates | yes — malicious/suspicious/safe + BEC/ransomware | yes — spam/malware/advanced threats | yes — behavioral verdicts |
| Enforcement actions | deliver / junk / tag / redirect / delete / quarantine | deliver / quarantine (hold) / delete / restore-remediated | block / quarantine / pull from all inboxes | block / quarantine / clawback | auto-quarantine/remediate post-delivery |
| Quarantine as holding state | yes, with per-verdict user rights + bounded retention | yes — CG quarantine + digest notifications | yes | yes | yes (post-delivery quarantine) |
| Admin policy model | recipient-scoped policies + priority + default + presets | custom multi-rule policies, user segmentation, blocked-sender policies | "rich DLP and policy customization" (SEG pole) | plans/policies; bulk operations | largely pre-configured posture |
| Allow/block lists | yes (per-policy + tenant-wide) | yes (blocked/allowed senders) | implied (misclassified-mail handling) | implied | allow/block sender actions documented in updates for peers; Abnormal has suppression via productivity module |
| End-user surface | quarantine notifications, self-release (restricted for high-risk verdicts) | digest email, end-user portal, Outlook add-in | real-time coaching | training/awareness split out | AI Security Mailbox triage; AI Phishing Coach |
| Feedback loop (FP/FN) | submissions (admin + user) | reported-emails analysis + case review | misclassified-email pipeline + abuse-mailbox agents | incident response module | autonomous triage with confirmation |
| Post-delivery re-evaluation | ZAP (documented) | remediation ("Restore Remediated Messages") | post-delivery detection FAQ | "continuously re-evaluates risk after delivery" | native mode of operation |
| Outbound filtering | yes (outbound anti-spam, forwarding control) | yes (gateway handles outbound; DANE) | "integrated outbound protections" | yes (family-level) | yes (Misdirected Email, Email DLP Rules, account-takeover outbound signals) |
| Impersonation/BEC/lookalike | anti-phishing/spoof intelligence (EOP); impersonation in MDO | Advanced BEC + impersonation (computer vision) | BEC + lookalike domain analysis | impersonation/"13 email threat types" | core strength (behavioral) |
| Inbound email-auth checks (SPF/DKIM/DMARC as signals) | yes (documented: allowed senders bypass these checks) | DNS Authentication inbound notification | not visible at page level | not visible at page level | uses identity graph instead |
| URL/attachment deep inspection | MDO adds URL/attachment protection (referenced; not page-detailed) | on-click URL protection, safe attachment handling, QR scanning | sandboxing for URLs and attachments | link protection, intent analysis | attachment/QR detection in inbound module |
| Bundled adjacent pillars | awareness (MDO plans), DLP (suite) | archive, continuity, DMARC Analyzer, training, managed response | Email Fraud Defense, DLP, archiving, training, ATP | DMARC, training, encryption, archiving, backup, XDR | identity security, AI governance, posture |
| Bundling substrate | part of the mail platform (also standalone) | independent cloud service over any platform | independent cloud service (SEG or API) | independent cloud service (+MSP) | independent cloud service (API) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **Checkpoint position in the organization's inbound mail flow.** The product is deployed so that email addressed to a defined organizational user population passes through it before it reaches user mailboxes; the organization's administrators, not individual recipients, control it. Realizations: MX-inline relay (canonical — cloud or appliance), platform-native protection service fronting the mail system, or an inline stage in a hybrid/on-prem mail topology. Remove → post-delivery API inspection (a different deployment family), mailbox-level junk filtering, or endpoint AV — no longer a gateway.
2. **Message-level inspection producing security verdicts.** Every message is evaluated against classes of unwanted or malicious content — unwanted bulk mail, malware, phishing/social engineering, spoofing/impersonation — yielding a per-message verdict from analysis of connection, sender identity, content, attachments, and URLs. Remove → a plain relay (the sending-side Email Infrastructure Management twin) with no security judgment.
3. **Verdict-driven enforcement on the message.** The verdict determines the message's fate: deliver; hold in a quarantine; reject/block/discard; or alter-and-deliver (junk routing, header/subject tagging, redirect, stripping). Remove → detection/alerting only, "the gateway" gone.

Jointly-held is load-bearing: 1+2 without 3 = monitoring surface; 2+3 without 1 = mailbox/endpoint-level filter or a post-delivery API product; 1+3 without 2 = a routing-only relay with fixed actions and no inspection.

### L1 — Common Mature Structure

Present across the sample, expected in the market, but not definitional:

- Admin console as the control plane over a synced user/group directory (recipient-scoped configuration).
- Policy model: scoped policies (user/group/domain) with priority ordering, a fallback default, and often preset baseline policies.
- Allow/block sender and domain lists at per-user and organization level, overriding detection — with documented spoofing risk when allow-listing.
- Quarantine administration: bounded retention, per-verdict user rights, end-user notifications/digests, release (or release-request for high-risk verdicts).
- Message trace / search and reporting dashboards (volumes, verdicts, threats).
- False-positive/negative feedback loop: user reporting buttons, admin submissions, misclassified-mail workflows.
- Impersonation/BEC protection and inbound email-authentication checks (SPF/DKIM/DMARC evaluated as signals on INBOUND mail).
- URL protection beyond delivery-time scanning (rewriting, on-click re-check, QR-code handling) and attachment sandboxing/detonation.
- Post-delivery re-evaluation and remediation (re-scan delivered mail, pull/restore across mailboxes).
- Outbound filtering (spam/malware, mass-mail/forwarding control) and account-takeover signals on internal mail.
- DLP and email encryption as commonly attached capabilities (often as separate SKUs).

### L2 — Variant / Optional Structure

- Deployment substrate: cloud service (dominant) vs on-premises/virtual appliance lineage; hybrid and on-prem mailbox protection.
- Deployment mode: gateway-only vs dual-mode (gateway + API) vs API-only (the boundary pole — a different deployment family competing for the same mission).
- Bundling substrate: platform-native (bundled with the mail platform) vs third-party independent service; stacking of a third-party gateway in front of platform-native protection is an explicitly documented pattern.
- Scale/segment: SMB/MSP-oriented vs enterprise; managed-service wrappers (analyst review of user-reported mail).
- Email continuity during mail-system outage (some products).
- Adjacent pillars sold beside the gateway: archiving, security awareness training, DMARC management for the org's own domain, backup, encryption, threat-intelligence services.
- End-user posture: passive digest + release vs active coaching/banners vs autonomous triage.

### L3 — Vendor-specific (Research Notes only)

Named verdict ladders (SCL/BCL values, "high confidence phishing"), quarantine retention ranges (documented 1–30 days at one vendor), module brand names (URL rewriting and safe-attachment brand names, "agentic clawback", "Barracuda IQ", "Threat Protection Workbench"), efficacy claims ("99.999%", "attacks bypassed SEGs each month" — vendor marketing, not citable), customer-count claims, specific integration partner lists.

## Rejected Findings

- "An ESG is defined by sandboxing / AI / behavioral analysis" — REJECTED. All are detection-machinery generations; appliance-era filtering satisfies the Type without them (historical check below).
- "Outbound filtering is definitional" — REJECTED. Universal in the current sample but the historical inbound-only relay satisfies the Type; the definitional orientation is inbound protection. Outbound is common-mature.
- "Quarantine with end-user digest is definitional" — REJECTED as invariant: connection-level rejection never quarantines; the invariant is the action set. Quarantine is the common mature holding state.
- "Gateway = any email threat protection" — REJECTED. The API-only pole (Abnormal) shares the mission but explicitly defines itself against the SEG on deployment mechanics ("no MX changes"; "Displace Your SEG"); the mail-flow checkpoint is what the market calls a gateway.
- "DMARC/anti-spoofing capability proves overlap with DMARC Management" — REJECTED as Type-merging. Inbound authentication evaluation is one inspection signal; managing the org's own sending-domain authentication is a distinct deliverable (sibling leaf; separate products at all sampled vendors).

## Historical / Market-Sample Check

- Founding-generation form: an on-premises appliance or hardened relay placed at the MX, performing connection checks (RBL-class), content/attachment filtering, and holding suspicious mail in a quarantine, administered by the mail admin for the org's users. This satisfies L0 fully — no cloud, no URL rewriting, no sandboxing, no AI. Check passed.
- Open-source minimal form: an SMTP relay in front of the mail store with reputation list checks + content filter + hold/reject actions satisfies the core. Check passed.
- Consumer webmail junk filter: fails leg 1 (not deployed as an organizational checkpoint under administrative control) — correctly outside the Type.
- API-only behavioral products (current era): fail leg 1 as-is; they are the documented boundary pole. No over-fitting to the inline-only pattern occurs because the Type's own market explicitly distinguishes "with or without a gateway" (two sampled vendors sell both modes as distinct product lines).

## Boundary Findings

| Neighboring Type | Relationship | Removal test / distinction |
|---|---|---|
| API-based integrated email security (no dedicated directory leaf; nearest current category usage: "email security platform") | adjacent, same mission | Remove the inline mail-flow checkpoint → API-based post-delivery product; vendors themselves frame it as "displace your SEG". Product straddle: gateway vendors sell both modes as separate product lines. |
| Email Authentication / DMARC Management (sibling leaf, unprocessed) | complementary | ESG evaluates inbound authentication as one signal; DMARC Management governs the org's own sending-domain authentication posture. Separate products at all sampled vendors (Domain Fraud Protection / DMARC Analyzer / Email Fraud Defense). |
| Email Infrastructure Management (processed 2026-09-08) | opposite side of the mail flow | That Type = outbound sending pipeline/relay operated on the org's behalf; ESG = receiving-side security checkpoint. Gateway outbound filtering ≠ sending infrastructure. |
| Data Loss Prevention | channel-of | Gateway DLP is the email channel slice; DLP as a Type spans channels/endpoints/cloud. Sold as attached capability in the sample. |
| Secure Web Gateway | same pattern, different protocol | HTTP(S) traffic vs SMTP mail; "gateway" naming shared, objects and enforcement differ. |
| Endpoint Protection / EDR | different locus | Mail-flow checkpoint vs endpoint processes; complementary layers. |
| Mail-client junk filtering | personal-scale subset | No organizational control plane, no deployment position in the org's mail flow. |
| Malware Analysis Sandbox | component of | Detonation is one detection technique, sometimes a separate product; not a mail checkpoint. |
| Digital Risk Protection (flag discharged) | different deliverable | Impersonation/lookalike detection appears in both; DRP's deliverable is takedown/removal of external identity abuse; the gateway's deliverable is filtering the mail stream. Confirmed: sampled gateway vendors sell lookalike-domain detection (inbound) while takedown machinery sits in DRP products. |

## Uncertainties

- Proofpoint and Barracuda operational details (policy engines, quarantine mechanics, connection filtering specifics) could not be verified — admin documentation gated/unreachable. All claims about those two products are page-level and marked as such.
- The on-premises appliance pole is weakly evidenced in fetched sources (site-level deployment pages; historical reasoning). Treated as a variant with reasoning-level confidence.
- Whether the directory needs a leaf for API-only email security products (the Abnormal pole) is a taxonomy question, not resolvable here.
- Exact universal presence of connection-level filtering across non-Microsoft gateways was not re-verified per product (gateway heritage makes it near-certain but evidence is indirect).

## Final Synthesis

An Email Security Gateway is the organization-administered security checkpoint in its own inbound email flow. Three structures define it: it sits in the mail path before user mailboxes for a defined user population; it inspects each message and renders a security verdict across spam/malware/phishing/spoofing classes; and it enforces the verdict on the message — deliver, quarantine, reject, or alter-and-deliver. Everything else in mature products — policy engines, allow/block lists, quarantine digests and release rights, impersonation/BEC detection, URL/attachment deep inspection, post-delivery re-evaluation, outbound filtering, DLP/encryption — is common mature structure layered on that checkpoint. The Type's live edge is the API-based post-delivery family: same mission, different position, framed by the market itself as SEG replacement vs SEG.
