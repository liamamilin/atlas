# Research Notes — Email Infrastructure Management

Research date: 2026-09-08
Directory leaf: "Email Infrastructure Management" (Section 14 — IT, Cloud & Infrastructure; neighbors: Message Queue Management, CPaaS Management)
Slug: email-infrastructure-management

---

## Research Goal

Establish what "Email Infrastructure Management" is as an Application Type from real products: who operates it, what objects the operator manages, what the defining work pipeline is, and how it separates from the adjacent email Types in the directory (Email Marketing Platform, Email Security Gateway, Email Authentication / DMARC Management, Email Client / Webmail, Shared Mailbox).

## Initial Boundary (hypothesis before research)

Two candidate readings were identified up front:

1. **Sending/delivery infrastructure reading** — systems for operating the email pipeline that sends application-generated email on an organization's behalf (the "Email API / transactional email / email delivery infrastructure" product class: SendGrid, Mailgun, Amazon SES, Postmark, SparkPost, SMTP2GO...). These vendors literally self-describe as "email infrastructure". Placement next to Message Queue Management and CPaaS Management (infrastructure-services family) supports this reading.
2. **Corporate mail estate administration reading** — administering an organization's internal email service (Exchange / Google admin consoles: mailboxes, mail-flow rules, connectors, licenses). This is platform administration of an employee-facing service, not a standalone commercial category named "email infrastructure management".

Research was designed to test which reading the market supports and whether one Type or two are needed.

## Research Questions

1. What objects does the operator actually create and manage (domains, credentials, IPs, messages, events, suppression)?
2. What is the onboarding gate, and why (authentication, verification)?
3. How do messages enter the pipeline (API vs SMTP vs console)?
4. What feedback loops exist (bounces, events, webhooks, reputation, alerts)?
5. How does the product keep mail deliverable (auth records, IP/reputation management, warm-up, stream separation)?
6. Where is the seam to Email Marketing Platform (contacts/campaigns) and to Email Security Gateway / DMARC Management?
7. Does inbound/receiving belong to the Type or is it optional?
8. Historical check: would a self-run mail relay (Postfix/Exchange-class) administration fit the definition?

## Representative Products

| Product | Owner | Why selected |
|---|---|---|
| Twilio SendGrid | Twilio | Largest market representative; self-identified "email infrastructure" lineage; spans transactional + marketing |
| Mailgun | Sinch | Developer-focused ESP with a distinct product split (Send / Optimize / Validate / Inspect) |
| Amazon SES | AWS | Hyperscaler cloud utility; different customer layer (cost-driven, bare-bones, deep AWS integration) |
| Postmark | ActiveCampaign | Transactional-only philosophy; opinionated positioning (separates transactional vs broadcast on different IP infrastructure) |

Product-philosophy spread: API platform vs developer ESP vs cloud utility vs transactional purist. Customer-layer spread: enterprise suites → startups/side projects → cost-driven cloud workloads.

## Sources

Tier 1 (official operational documentation), fetched 2026-09-08:

- SendGrid: https://www.twilio.com/docs/sendgrid (docs root); https://www.twilio.com/docs/sendgrid/ui/account-and-settings/how-to-set-up-domain-authentication (domain authentication how-to)
- Mailgun: https://documentation.mailgun.com/docs/mailgun/ (docs root); https://documentation.mailgun.com/docs/mailgun/user-manual/intro (user manual TOC); https://documentation.mailgun.com/docs/mailgun/user-manual/domains/ (domain verification)
- Amazon SES: https://docs.aws.amazon.com/ses/latest/dg/send-email.html (set up email sending). NOTE: SES docs root and identity-verification pages returned an empty JS shell on 2026-09-08 (2 attempts) — see Source-access Limitation below.
- Postmark: https://postmarkapp.com/developer (developer documentation root, full API/webhook/user-guide surface)

Source-access limitation: AWS SES documentation pages other than the sending page could not be fetched (JS-rendered shell, 2 failed attempts). SES-specific observations are therefore limited to what the fetched page states (console/SMTP/API sending paths, console used to "manage your sending activity", integration with existing mail servers, per-recipient rejection behavior). No SES-specific detail beyond that page has been asserted from model memory. Cross-product claims below are calibrated accordingly.

---

## Product A — Twilio SendGrid (evidence layer A unless noted)

Docs root + domain-authentication how-to.

- Positioning: "Build transactional and marketing email solutions"; deliverability rate quoted in marketing framing (not treated as evidence).
- **Domain authentication is the onboarding gate**: "verifies the legitimacy of your email servers, messages, and sending addresses". Product generates DNS records (CNAME/TXT/MX) asserting: domain ownership, permission for the sending server to send on behalf of the domain, sender identity verification, tamper-evidence in transit.
- Generated records implement **SPF, DKIM, DMARC** (TXT/CNAME), plus MX/return-path for bounce/unsubscribe routing. "Automated security" option: vendor creates and maintains SPF/DKIM on the customer's behalf; off = customer installs and maintains records manually. Manual verification loop with retry (DNS propagation caveats documented).
- Dedication to sending identity: only the authenticated root domain may be used as from-domain; subdomains do not inherit; custom return-path and custom DKIM selector options; reverse DNS setup documented.
- **Two injection paths**: Mail Send API (HTTP, SDKs in 7 languages) and SMTP relay (X-SMTPAPI header for batch/templating metadata).
- **Outcome machinery**: Event webhook (send/delivered/open/click/bounce-class events), Email Activity Feed (searchable per-message event log), Engagement Quality API (deliverability quality score).
- **Account structure**: API keys; Subusers (segmented child accounts); Teammates (team members); SSO.
- **Inbound**: Inbound Parse webhook (receive email, parse, POST to customer URL).
- **Marketing layer as a separate module**: Marketing Campaigns — contacts, lists, segmentation, custom fields, designs, automation. Structurally separate from the sending infrastructure docs.
- Link branding (CNAMEs routing click/open tracking through the customer's domain), SSL auto-provisioning for branded links, EU-pinning of domains (regional data residency).
- Product-specific limits observed: 3,000 authenticated domains and 3,000 link brandings per user/subuser.

## Product B — Mailgun (evidence layer A)

Docs root, user manual TOC, domain verification page.

- Product split: **Send** (APIs to "send, receive, and track email") / **Optimize** (InboxReady — deliverability) / **Validate** (email validation) / **Inspect**.
- User manual structure: API Key Management and Security; **Domains** (overview, sandbox domain, custom domains, domain verification); Sending Messages; Receiving Messages; Tracking Messages; Webhooks; Events; SMTP Protocol; Internationalization; Subaccounts; Reporting; Alerts; FAQ; Email Best Practices.
- **Domain verification is the gate**, with explicit reasons: prove authorized sender; lift the sandbox sending limit (300 emails/day for sandbox — product-specific); remove "sent via Mailgun.org" tagging; establish positive reputation for the customer's own domain; reduce likelihood of account disablement.
- Verification = install DNS records (TXT SPF, TXT DKIM, CNAME tracking, MX for receiving) → DNS propagation (24–48h documented) → auto-verify or trigger Verify API / control-panel verify. Multiple DKIM keys possible (rotation, Automatic Sender Security).
- **Sandbox domain** as a first-class testing object.
- Subaccounts for account segmentation; RBAC and API key management; Alerts; Reporting; SMTP protocol support alongside API.
- Validation (address quality) sold as an adjacent capability of the same platform.

## Product C — Amazon SES (evidence layer A, limited fetch)

Fetched page: "Set up email sending with Amazon SES".

- **Three sending paths**: AWS Console, SMTP interface, SES API (raw HTTP). Console typically for test emails and "manage your sending activity"; SMTP or API for programmatic/bulk sends.
- SMTP interface explicitly framed for integrating "with your existing mail server" — the utility posture: SES positions itself as infrastructure other systems relay through.
- All-or-nothing recipient semantics documented (multi-recipient API call failing rejects the whole message) — operational rule at the injection boundary.
- Per-message pricing referenced (utility business model).
- Not directly observed this pass (docs unreachable): identity verification mechanics, bounce/complaint notification configuration, dedicated IP/pool management, reputation dashboards. Assertions about SES beyond the fetched page are avoided.

## Product D — Postmark (evidence layer A)

Developer documentation root (full API/webhook/user-guide index) + product feature nav.

- Positioning: "delivers and tracks your application email — a fast, reliable, care-free replacement for SMTP".
- **Account structure**: Servers (top-level containers, create/edit/list/delete via API); Message Streams (separate transactional vs broadcast streams; docs state transactional and broadcast "travel on different IP infrastructure" so critical mail reaches the inbox).
- **Domains API**: list/get/create/edit/delete domains; **verify DKIM; verify Return-Path; verify SPF; rotate DKIM keys**. **Sender signatures**: verify individual from-addresses (address-level alternative to whole-domain auth); resend confirmation.
- **Injection**: Email API (single + batch), SMTP service, Bulk API (with request status tracking), Templates API (send with template, validate template, push templates between servers).
- **Outcome machinery**: Bounce API (get delivery stats, list bounces, single bounce, bounce dump, **activate a bounce** [un-suppress], bounce types taxonomy); Suppressions API (dump, create, delete suppression); Messages API (outbound/inbound search, message dumps, opens, clicks); Stats API (sent, bounces, spam complaints, opens, clicks, platform/client/browser usage).
- **Webhooks**: delivery, bounce, spam complaint, open, click, subscription change, inbound — with verification, retry attempts, statistics.
- **Inbound processing**: configure inbound server, inbound domain forwarding, parse email, inbound blocking rules, retry failed inbound.
- **Sandbox mode**: per-server sandbox; "generate fake bounces" for testing — test-first philosophy made explicit.
- IP allowlisting; Data Removal requests (compliance surface).
- Product-specific limits observed: 10 MB per email; 50 recipients per message.
- Deliberate product philosophy: transactional-first; broadcast supported but stream-separated; no contact-database/campaign-builder module in the feature list.

---

## Cross-product Comparison

| Dimension | SendGrid | Mailgun | Amazon SES | Postmark | Evidence layer |
|---|---|---|---|---|---|
| Sending identity gate | Domain authentication (generated DNS records, verify loop) | Domain verification (DNS records, verify API) | Not directly observed this pass | Domains (DKIM/Return-Path/SPF verify, key rotation) + sender signatures | B (3/4 direct; SES limited) |
| Authentication records managed | SPF, DKIM, DMARC (+return-path, link branding) | SPF, DKIM (+CNAME tracking, MX) | — | SPF, DKIM, Return-Path | B |
| Injection paths | Mail Send API + SMTP relay | Send API + SMTP Protocol | Console + SMTP interface + API | Email API + SMTP service (+Bulk API) | B (all 4) |
| Outcome events | Event webhook + Email Activity Feed | Events + Webhooks + Tracking | — | Bounce/delivery/complaint/open/click webhooks + Messages API | B (3/4 direct) |
| Bounce/suppression handling | Event machinery (bounce events) | Events/webhooks | — | Bounce API (activate bounce, dump, types) + Suppressions API | B (direct at Postmark; common-mature wording elsewhere) |
| Deliverability/health surfacing | Engagement Quality API | InboxReady (Optimize) + Alerts + Reporting | "manage your sending activity" (console) | Stats API (bounces, spam complaints); transactional/broadcast IP separation | B |
| Account segmentation | Subusers, Teammates, API keys, SSO | Subaccounts, RBAC, API keys | AWS account-native | Servers (+ per-server sandbox) | B |
| Templates | Dynamic Templates (Handlebars) | Templates (user manual) | — | Templates API (validate, push between servers) | B (3/4 direct) |
| Inbound/receiving | Inbound Parse webhook | Receiving Messages + MX records | — | Inbound processing (server, forwarding, parse, blocking, retry) | B (3/4 direct) |
| Testing | (docs reference sandbox flows) | Sandbox domain (300/day limit) | — | Sandbox mode + fake bounces | B (2/4 direct) |
| Marketing contacts/campaigns | Marketing Campaigns module (contacts, segments, designs, automation) | Not present | Not present | Not present (deliberately transactional-first) | A — product-specific to the suite pole |
| Address validation | — | Validate product | — | — | A — product-specific |
| Deliverability productization | Engagement Quality API | InboxReady (Optimize) as separate product | — | Message streams IP separation (philosophy, not product) | A — varies |
| Data residency | EU-pinned domains | — | — | — | A — product-specific |

### What repeats (candidate common structure)

1. Verified sending identity per domain as the production gate (unverified = restricted: tagging, daily limits, disablement risk).
2. DNS-record-based authentication (SPF/DKIM/DMARC-class) installed or hosted by the vendor, with vendor-side or customer-side maintenance.
3. Two programmatic injection paths: HTTP API and SMTP relay.
4. Delivery-outcome events (delivered/bounced/complaints) surfaced as webhooks/events/activity feeds.
5. Bounce and complaint feedback managed as first-class objects (lists, suppression, reactivation).
6. Deliverability treated as an ongoing operational responsibility (stats, alerts, quality scores, IP/stream separation).
7. Account segmentation constructs + scoped API keys for multi-tenant/multi-environment use.
8. Optional inbound path on the same infrastructure (receive, parse, forward).
9. Testing affordances (sandbox domains/servers, fake bounces).
10. Template/personalization machinery near the injection boundary.

### What does NOT repeat

- Contact databases, campaign builders, segmentation, marketing automation → only the suite pole (SendGrid) carries this; Postmark's structure pointedly separates broadcast without contact management.
- Address validation, inbox-placement productization → sold as separate products by some vendors only.
- Named numeric limits, vendor feature names, regional pinning → vary entirely by product.

---

## Canonical Model

### L0 — Defining Invariant (four jointly-held structures)

1. **The sending infrastructure as the managed subject.** A mail-transit system — relay or email-delivery service — operated on the organization's behalf, that accepts messages and delivers them onward to receiving mail systems on the public internet. Remove → there is no pipeline to manage (an email client, a marketing content tool, or an analytics surface instead).

2. **Sender identity & authentication establishment per sending domain.** The operator proves control of the domain it sends from and puts authentication machinery (SPF/DKIM/DMARC-class DNS records, return-path) in place so receiving systems can attribute and trust the mail. Remove → an unaccountable relay; and in the observed market the entire onboarding gate collapses (unverified senders are tagged, throttled, and disabled).

3. **Programmatic message injection.** Applications and systems hand messages into the pipeline through machine interfaces — an HTTP API and/or SMTP relay — not (only) through a human composing mail. Remove → this is someone's email client or mailbox service, not application email infrastructure.

4. **Delivery-outcome feedback.** What happened to each message downstream (accepted/delivered, bounced, spam-complained) is captured, surfaced, and made actionable — events/webhooks, activity feeds, bounce/suppression handling. Remove → a blind fire-and-forget pipe; the "management" half of the Type disappears.

Jointly-held checks:
- 1+2 without 3+4 → DNS/auth configuration tooling (DMARC-setup wizard territory), no pipeline.
- 3+4 without 2 → anonymous/open relay, unrecognizable as the managed-pipeline Type and blocked by every observed product's gate.
- 1+3 without 4 → blind relay; no management.
- 2+4 without 1 → authentication/compliance monitoring → that is the separate Email Authentication / DMARC Management Type.

### L1 — Common Mature Structure (standard, not definitional)

- templates & personalization machinery
- event webhooks + searchable per-message activity feeds
- bounce taxonomy, bounce dumps, suppression lists, re-activation ("activate bounce")
- delivery/open/click/complaint statistics and dashboards
- account segmentation (subusers / subaccounts / per-environment servers) + scoped API keys + SSO/RBAC
- inbound processing (receive, parse, forward, inbound rules)
- sandbox/testing affordances (sandbox domains, fake bounces)
- deliverability reporting and alerting
- dedicated IPs, reverse DNS, IP/stream separation (IP pools and warm-up practices are widely referenced in the class but were not directly observed in the fetched pages this pass — held unverified-common)
- SDKs, official libraries, integrations

### L2 — Variant / Optional Structure

- **Marketing/contact layer** (contacts, lists, segmentation, campaign designs, automation) — suite-pole only; marks the seam to Email Marketing Platform.
- **Email validation** as a sold capability of the same platform.
- **Deliverability productization** (inbox placement testing, deliverability suites sold as separate products).
- **Deployment posture**: managed cloud ESP (dominant commercial form) vs self-run/relay-adjacent operation (historical and some regulated deployments; SES explicitly frames SMTP integration "with your existing mail server").
- **Receiving depth**: from bare MX + store/forward to full parse/forward rule engines.
- **Regional pinning / data residency**; billing models (per-message utility vs packaged tiers); transactional-vs-broadcast separation as an opinionated product posture vs a mere feature.

### L3 — Vendor-specific (research notes only)

- SendGrid: "automated security" (vendor-maintained SPF/DKIM via CNAMEs), link branding + SSL auto-provisioning, EU-pinned domains, 3,000-domain/user limit, X-SMTPAPI header, Engagement Quality API, Subusers/Teammates naming.
- Mailgun: sandbox 300 emails/day limit, "sent via Mailgun.org" tagging behavior, Verify API endpoint, Automatic Sender Security, InboxReady/Validate/Inspect product naming, multiple-DKIM-key states.
- Amazon SES: console/SMTP/API triad framing, whole-message rejection on multi-recipient API failure, "existing mail server" integration framing, per-message pricing.
- Postmark: Message Streams (transactional vs broadcast IP separation), bounce "activation", fake-bounce generation, 10 MB / 50-recipient limits, sender signatures as address-level auth alternative, AI tooling (MCP server, CLI, llms.txt).

## Rejected Findings

- **"Email Infrastructure Management = email marketing with contacts and campaigns"** — rejected: 3 of 4 sampled products define the Type fully without any contact/campaign layer; the seam to Email Marketing Platform is visible exactly where the contact database appears.
- **"It is an inbound security product"** — rejected: threat filtering/quarantine of received mail (Email Security Gateway) is a different flow direction, different user, different object set. Inbound here means receive/parse/forward of application-addressed mail, not threat defense.
- **"It is DMARC report analysis"** — rejected: DMARC management products monitor authentication compliance across domains; this Type *operates* the sending pipeline that installs and hosts the records. Same DNS records, different object of work.
- **"API-first is definitional"** — rejected as L0 wording: the invariant is programmatic injection, historically and in the sample realized as SMTP relay or HTTP API. The historical check (below) drove this abstraction.
- **"Templates/webhooks/dashboards are part of the definition"** — rejected to L1: none of them is required to recognize the Type; older SMTP-relay-era infrastructure satisfies the core without them.

## Boundary Findings

| Neighboring Type | Relationship | Boundary criterion ("remove X and it becomes...") |
|---|---|---|
| Email Marketing Platform | adjacent downstream | Remove the audience layer (contact database, campaigns, segments, designs) and keep the pipeline → this Type. Remove the pipeline management and keep audience/campaign machinery → Email Marketing Platform. SendGrid literally realizes both sides of the seam in one account. |
| Email Security Gateway | adjacent, opposite flow direction | Gateway polices *inbound* mail for a *receiving* organization (threats, quarantine); this Type operates the *sending/transit* pipeline. Direction of mail flow + user (security team vs developer/deliverability ops) + core objects (threat policies vs sending domains/auth/events). |
| Email Authentication / DMARC Management | overlaps on one object set | Both touch SPF/DKIM/DMARC. The DMARC-management Type monitors/reports on authentication compliance across a domain portfolio and does not send; this Type installs/hosts the records and runs the pipeline they protect. Object of work: compliance posture vs delivery pipeline. |
| Email Client / Webmail / Shared Mailbox | different actor entirely | Those serve end users reading/composing personal mail; this Type serves technical operators running infrastructure. No mailbox is provisioned here. |
| Corporate mail estate administration (Exchange/Google admin consoles) | adjacent, partially overlapping users (IT ops) | That reading manages employee-facing mailbox service (mailboxes, licenses, mail-flow rules for internal users). This Type manages application-generated sending infrastructure. See taxonomy note below. |
| Newsletter Marketing Platform | adjacent downstream | Newsletter tools center publication/campaign creation; may ride on top of this infrastructure class. |
| CPaaS Management / Message Queue Management | sibling Types in the same infrastructure family | Same family shape (operate a message-transit infrastructure), different channel/protocol domain (SMS/voice; MQ queues/topics vs email). |
| Email validation services | optional capability inside the platform | Validation (address quality) appears as an optional sold capability (1 sampled vendor as separate product), not part of the core. |

**Taxonomy note (recorded, not self-remediated):** the leaf name admits the "corporate mail estate administration" reading; no dedicated directory leaf exists for that activity (Exchange/Google admin tooling). This pass resolved the leaf to the sending/delivery-infrastructure reading based on (a) section placement next to Message Queue Management and CPaaS Management, and (b) the commercial market's actual "email infrastructure" product class. The corporate-mail-admin reading is flagged in STATUS.md Boundary Issues rather than silently merged or split.

## Historical / market-sample check

- **Self-run relay era (Postfix/Exchange-class administration)**: fits the core — the relay is the managed subject (1), the admin maintains the domain's SPF/DKIM/return-path records (2), applications submit mail via SMTP (3), postmaster queues/bounces are processed by hand or scripts (4). The definition holds without any SaaS, webhooks, or dashboards.
- **Pre-API ESP era (SMTP-only delivery services)**: fits — injection is SMTP; outcomes arrive as bounces to the return-path.
- **Regional/regulatory deployments** (data-residency-pinned, self-hosted relays): fit — deployment posture is L2.
- Conclusion: the canonical core is not overfit to the modern API/ESP implementation. "Programmatic injection" (not "HTTP API"), "delivery-outcome feedback" (not "webhooks"), "sender identity & authentication" (not "DKIM specifically") are the right abstraction heights.

## Uncertainties

1. **Amazon SES depth**: identity verification, notification configuration, IP/reputation tooling not directly observed (docs unreachable this pass). The cross-product B-layer claim for the identity gate stands on 3/4 products; SES assertions limited to the fetched sending page.
2. **Suppression machinery**: direct API evidence at Postmark only; bounce-event machinery directly observed at SendGrid/Mailgun. Held as common-mature (L1) with moderate wording rather than universal.
3. **Corporate mail estate reading**: recorded as a taxonomy ambiguity (see Boundary Findings); whether the directory wants a separate leaf for it is a human decision.
4. **Inbound depth**: receiving is directly observed at 3/4 products; SES receiving capability not observed this pass. Inbound held as common-mature, not core.
5. **Market naming drift**: vendors name the class differently ("Email API", "Transactional Email", "Email delivery", "email infrastructure"); "Email Infrastructure Management" as a leaf name is the directory's, not a market-standard category label. Documented, not a defect.

## Final Synthesis

Email Infrastructure Management is the operator-facing Type whose system of record is the **organization's email delivery pipeline**: the sending domains it is trusted to speak for, the authentication that makes that trust machine-checkable, the injection interfaces through which applications hand it mail, and the outcome/feedback machinery through which the operator keeps delivery healthy. Its user is a technical operator (developer, DevOps, deliverability/email ops, platform team), not an end user reading mail and not a marketer building campaigns. The commercial center of the market is the managed email-delivery platform (Email API + SMTP relay class), with the self-run relay as the historical and deployment-variant pole. The Type is bounded from marketing platforms by the absent audience layer, from security gateways by flow direction and object set, and from DMARC management by the object of work (operating the pipeline vs monitoring its compliance).
