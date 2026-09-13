# Research Notes — Account Abuse Protection

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what "Account Abuse Protection" (Directory §15, Cybersecurity, Identity & Trust) is as an Application Type: what object it protects, what its core operating loop is, who operates it, and where its boundaries lie against neighboring Types (Fraud Prevention Platform, Bot Management/DDoS, MFA, CIAM, Identity Verification, SIEM, Insider Risk Management, Digital Risk Protection).

## Initial Boundary

Working hypothesis before research:

- The protected object is the **user account** of a digital service (consumer or customer-facing, possibly also workforce).
- "Abuse" covers at least: account takeover (credential stuffing, password spraying, brute force, session/MFA compromise), fake/bot account creation and multi-accounting, and abuse of account-linked privileges (account sharing, promo/referral/trial abuse, excessive usage).
- The core loop is: account-lifecycle event → signal-based risk evaluation → enforcement decision (allow / challenge / block / review).
- Nearest confusions: Fraud Prevention Platform (transaction-centered), Bot Management (traffic-centered), MFA (a challenge factor, not a decision system), CIAM (identity administration, not risk enforcement).

## Research Questions

1. Which attack types define the category (abuse typology)?
2. What are the core objects: events, signals, scores, decisions, cases, lists?
3. What is the canonical enforcement loop, and where does enforcement live (product vs application)?
4. What signal families exist across products?
5. How is the product integrated (SDK/API/edge) and what happens on failure (fail-open vs fail-closed)?
6. Who operates it day-to-day (analysts, rule authors, developers)?
7. How do challenge/step-up mechanisms relate to MFA?
8. What varies by population (consumer vs workforce), deployment, and product philosophy?

## Representative Products

| Product | Why selected | Evidence tier reached |
|---|---|---|
| Castle | Pure-play account security / bot & abuse prevention API; developer-first; mid-market | Tier 1 (full docs) |
| DataDome (Account Protect) | Edge bot-management vendor with a dedicated account-protection product; enterprise | Tier 1 (full docs for Account Protect) |
| Arkose Labs | Challenge-centric account-fraud defense; enterprise; strong "drain attacker ROI" philosophy | Tier 2 (marketing/solution pages; docs portal not fetched) |
| Sift | Broad "Digital Trust & Safety" decision platform spanning account + payment fraud; enterprise | Tier 2 (homepage only; docs 403) |
| Microsoft Entra ID Protection | Workforce-side structural analog (risk-based sign-in decisions inside an identity platform); used for the historical/market-sample check | Tier 1 (Microsoft Learn) |

Selection covers: pure-play vs suite, recommendation-only vs enforced-challenge, consumer vs workforce population, API-first vs edge-first.

## Sources

Fetched 2026-09-06:

- Castle docs root + llms.txt index — https://docs.castle.io/ , https://docs.castle.io/llms.txt
- Castle: Overview — https://docs.castle.io/docs/an-introduction-to-castle.md
- Castle: Risk scoring — https://docs.castle.io/docs/risk-scoring.md
- Castle: Signals — https://docs.castle.io/docs/signals.md
- Castle: Policies — https://docs.castle.io/docs/creating-a-policy.md
- Castle: Review suspicious user behavior — https://docs.castle.io/docs/review-suspicious-user-behavior.md
- Castle: Protecting the login — https://docs.castle.io/docs/login-activity.md
- DataDome docs root — https://docs.datadome.co/
- DataDome: Account Protect — https://docs.datadome.co/docs/account-protect.md
- DataDome: SDK integration for login — https://docs.datadome.co/docs/account-protect-login
- DataDome: Explore your Account data — https://docs.datadome.co/docs/explore-your-fraud-data
- Arkose Labs homepage — https://www.arkoselabs.com/
- Arkose Labs: Account Takeover solution — https://www.arkoselabs.com/solutions/account-takeover/
- Sift homepage — https://sift.com/
- Microsoft Entra ID Protection overview — https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection

### Source-access Limitations

- docs.sift.com and developers.sift.com returned transport errors / 403 (2 attempts each); sift.com product/solution subpages returned 403 (2 attempts). Sift evidence is therefore limited to its homepage (Tier 2). All Sift-specific claims below are marked accordingly; no precise Sift operational details are asserted.
- docs.arkoselabs.com returned a transport error (1 attempt); Arkose evidence is Tier 2 (homepage + ATO solution page). No precise Arkose operational details are asserted.
- Castle and DataDome (Account Protect) and Microsoft Entra ID Protection have Tier 1 documentation evidence.

## Product Observations

### Castle (Tier 1)

Evidence layer: A (direct observation of official docs).

- Self-description: "a suite of APIs for bot detection and abuse prevention"; "stops bots and fraud through behavioral analysis — no puzzles for your users to solve."
- Three named ML risk scores, computed in real time from Risk/Filter APIs and client-side SDK events, returned as 0.0–1.0 (0–100 in dashboard):
  - **Account Abuse Score** — probability a user is trying to abuse the service: fake accounts, multi-accounting, account sharing, excessive usage; typically on registration, also in-app events.
  - **Account Takeover Score** — risk that an account is accessed via stolen credentials (human ATO or automated credential stuffing); typically on login, also profile updates/transactions.
  - **Bot Score** — request from an automated script; typically pre-authentication on public forms.
- Score inputs (per docs): pre/post-authentication status, device history, suspicious behavior (high entropy in user/device traits), historical statistics of the customer's user population, real-time IP/ISP/email reputation; "hundreds of features" from device and interactions; bot behavioral tells (e.g. straight-vector mouse movements, interaction timing patterns); IP/ISP reputation that changes over time; failed-to-successful ratios; multiple-account access attempts.
- **Signals**: exposed in the API response, grouped into categories: Automated activity, Anomalous behavior, Device data error, Device intelligence, Email intelligence, IP intelligence, Unobserved characteristics, Unapproved characteristics. Signals are explanatory inputs to the score and can drive standalone logic.
- **Policies**: rules engine with Trigger (event type, list membership, risk score/signal conditions) and Action (inline API action `allow` / `challenge` / `deny`; add/remove list entries). Policies grouped by event name (registrations, logins, profile updates, transactions, password resets) plus "before/after all events" groups. Evaluated top-down; ordering matters (deny above challenge). **Pass-through / Log-only mode** for monitoring before enforcement. Default policies: deny at score 90–100, challenge at 60–100.
- **Events**: `$login` (succeeded/failed), `$logout`, `$registration`, `$transaction`, `$profile_update`, password resets, anonymous activity (pre-auth forms), account verification/challenge events. Failed logins go to the Filter API to enrich detection. Successful login goes to the Risk API *before* any app-triggered MFA. User object carries id (required), email, phone, registered_at, traits.
- **Client-side**: Browser SDK and mobile SDKs generate per-request "request tokens" (device fingerprinting); invalid/missing token → deny (bad actor bypassing fingerprinting); API error/timeout → allow (fail-open).
- **Taking action** (app-side): on `deny` block and redirect to login; on `challenge` prompt additional verification (email/2FA).
- **Lists**: Trusted Users, Blocked Users, review lists; primary field user ID, optional secondary device fingerprint; auto-archivation; CSV export.
- **Review workflow** (documented tutorial): policy adds suspicious users (e.g. Abuse Score > 60 on transactions > $500) to a review list → analyst opens user profile view → reviews activity → moves user to Trusted or Blocked list, with a comment for teammates.
- **Webhooks**: triggered on first `challenge`/`deny` verdict for a device; enable automation (e.g. auto-suspend accounts).
- **Dashboard**: overview, metrics, policies, lists, user profiles; team management, SSO, 2FA for the console itself.
- Tutorials confirm abuse typology: detect account sharing; challenge logins from new country/device; block signups with spam emails; CAPTCHA integration; challenging users without CAPTCHAs.

### DataDome — Account Protect (Tier 1)

Evidence layer: A.

- Positioning: "Prevent account fraud. Trust every login and account creation." Account Protect is a **separate product from Bot Protect** (dedicated API key, enabled by account manager) inside the DataDome platform (which also has Bot Protect, DDoS Protect, Ad Protect, Priority Protect, Page Protect, Agentic Trust).
- **Instrumented events** via backend SDKs (Java, Node, .NET, Symfony, Laravel, Python, Ruby, Go): login, registration, account update, password update, custom events.
- **Login flow**: on successful login (valid credentials), SDK sends a `LoginEvent` to the Account Protect API, which replies with a **recommendation**: `allow` / `deny` / `challenge` / `review` (response `action` field). "A recommendation means that your application will still make the final decision." Documented mitigation examples: block the login; add user to a watchlist; require MFA; reset the user password; send data to an internal fraud tool. On failed login, the SDK `collect`s the event to enrich detection models.
- **Event schema** (LoginEvent): account identifier; user.id (required, consistent across events); authentication (mode: biometric/mail mfa/otp/password; type: local/social; socialProvider); accountType (guest/staff/external/partner/customer/merchant/vip/test/other); accountCreationDate; session (id, createdAt); failReason (unknownAccount, wrongPassword, expiredPassword, disabledAccount, blockedAccount, invalidMfa, internalBusinessRule, technicalIssue, other); customFields (up to 10, with PII flag); partnerId.
- **Response**: action; reasons (e.g. `brute_force`, `teleportation`); score (confidence level); eventId; ip; location (city/country); status (ok/failure/timeout).
- **Failure posture**: on timeout (default 1500 ms), API error, or invalid API key → SDK returns `allow` (fail-open) so the application is never blocked by the protection layer.
- **Feedback**: a `/feedback` decision-feedback API enables an automated feedback loop.
- **Dashboard**: Explore view (events grouped by event list or by account; search by IP/email/account/last name; 6-month activity timeline of Allow / Denied / No-action-taken counts; per-event detail); Login overview and Registration overview pages.

### Arkose Labs (Tier 2)

Evidence layer: A for what the pages literally claim; treated as Tier 2 because operational docs were not reachable.

- Platform: **Arkose Titan** — "unifies bot detection, account security, and adaptive enforcement"; products: Bot Manager, Agent Trust Manager (AI-agent classification), Arkose Edge, Device ID, Email Intelligence, Phishing Protection.
- Solutions: Account Takeover ("block credential stuffing and brute force attacks"), Fake Account Creation ("stop fake signups and bonus abuse"), SMS Toll Fraud, API Security, MFA Compromise (reverse-proxy phishing), Human Fraud Farms.
- ATO mechanism (as described): real-time risk assessment via the "Arkose Global Intelligence Network" (claimed 175+ risk assessment signals); **adaptive challenges** that "adapt to attack types"; true/false API results plus a data payload for downstream decisioning; 24/7 SOC and threat-research unit (ACTIR) tuning protections with the customer.
- Philosophy: "offensive protection, not passive blocking — drain attacker ROI until attacks become economically unviable"; challenges positioned as generations beyond basic CAPTCHAs; "good users get through."
- Industries: banking/fintech, gaming/iGaming, travel/hospitality, e-commerce, technology/telco.

### Sift (Tier 2 — homepage only)

Evidence layer: A for homepage claims; Tier 2 limitation recorded.

- Positioning: "Fraud Prevention Platform for Digital Business"; "real-time visibility into payment fraud, account takeover, and account abuse."
- Use cases: Payment Fraud, **Account Takeover** ("block unauthorized access in real time"), **Fake Account Creation** ("stop fraudulent signups at the door").
- Products: Payment Protection, **Account Defense** ("stop account takeover before it turns into revenue loss"), Sift Score API ("bring Sift intelligence into your own risk models"), Expert Services.
- Platform components: **Decisioning Engine** ("build rules and adapt risk strategy in real time"), **Network Intelligence** (global data network, claimed 1T+ annual events; "new-to-you users are often not new to Sift"), **Automation & Workflows** ("automate review, routing, and repetitive fraud ops work").
- Consumer journey model (homepage diagram): **Signup → Login → Account activity → Transaction → Post-transaction**.
- Console (homepage mock): workflows with block rates/accuracy (e.g. an "ATO" workflow), queues, manual decisions (Accept / Block / Watch), per-analyst review stats.

### Microsoft Entra ID Protection (Tier 1) — workforce-side structural analog

Evidence layer: A. Included for the historical/market-sample check and the consumer-vs-workforce variant, not as a primary sample.

- "Helps organizations detect, investigate, and remediate identity-based risks." Risks feed **Conditional Access** for access decisions or a SIEM.
- **Detect**: catalog of detections (anonymous IP address usage, password spray attacks, leaked credentials, ...); during each sign-in, real-time detections generate a **sign-in session risk level**; policies are applied based on risk level.
- **Investigate**: reports — risk detections, risky sign-ins, risky users.
- **Remediate**: automatic (risk-based Conditional Access: require strong authentication method, MFA, or secure password reset based on risk level; successful completion auto-remediates) or manual (admin reviews in portal/API/Defender XDR; dismiss / confirm safe / confirm compromise).
- **Export**: Graph APIs to SIEM (Sentinel), Log Analytics, storage, Event Hubs.
- Admin roles (Global Reader, Security Operator, etc.) gate report and policy capabilities; license tiers gate features.

## Cross-product Comparison

| Dimension | Castle | DataDome Account Protect | Arkose Labs | Sift | Entra ID Protection |
|---|---|---|---|---|---|
| Protected object | user accounts of an app (login/registration/transaction/profile events) | user accounts (login/registration/account-update/password-update events) | account integrity across user journey (login, signup) | accounts across consumer journey (signup→login→activity→transaction) | workforce identities (sign-ins, users) |
| Event model | typed events with statuses ($login succeeded/failed, $logout, $registration, $transaction...) | typed events with status + rich schema (authentication, failReason, session, accountType) | login/signup flows (via platform integration) | journey-stage events (Tier 2) | sign-in events + user risk detections |
| Risk evaluation | 3 ML scores (Abuse / ATO / Bot) + explanatory signals | score + reasons + recommended action | risk assessment from global signal network + adaptive challenges | scores + decisioning rules (Tier 2) | sign-in risk level + detection catalog |
| Decision vocabulary | allow / challenge / deny (+ log-only pass-through) | allow / deny / challenge / review (recommendation; app decides) | challenge-enforced + API true/false + payload | automated decisions + manual Accept/Block/Watch (Tier 2) | risk-based access policy (require MFA/strong auth/password reset) or admin confirm/dismiss |
| Who enforces | application implements the returned action | application implements the recommendation | product enforces challenges inline | application + console workflows (Tier 2) | identity platform enforces at sign-in (Conditional Access) |
| Signal families | device fingerprint, IP/ISP reputation, email intelligence, behavioral/bot traits, velocity, population history | request/device metadata via SDK, model reasons (brute_force, teleportation) | device ID, email intelligence, global network signals (claimed 175+) | global network intelligence (Tier 2) | Microsoft-wide signals (AD, consumer accounts, Defender products) |
| Analyst surface | dashboard: policies, lists, user profile review flow, metrics, webhooks | dashboard: event explorer, login/registration overviews, timelines | customer portal + 24/7 SOC | console: queues, workflows, analyst stats (Tier 2) | portal reports: risky users / sign-ins / detections |
| Feedback loop | webhooks + lists + labels; failed logins enrich models | /feedback decision API; failed logins collected | data-sharing loop across customer network | network intelligence (Tier 2) | remediation updates risk state; Graph export |
| Failure posture | fail-open on API error/timeout; deny on invalid request token | fail-open on timeout/error/invalid key | n/a (Tier 2) | n/a | n/a |
| Population | consumer/customer apps | consumer/customer apps | consumer/customer apps (banking, gaming, travel, e-commerce) | consumer digital businesses | workforce |

### Stable commonalities (evidence layer B)

Across all five sampled systems:

1. **Account-lifecycle events are the monitored object** — every product instruments a defined set of account events (sign-in, registration, credential/profile changes; Castle and DataDome document the exact event schemas).
2. **Per-event risk evaluation** — every product produces a risk assessment (score, level, or detection) for each event, from technical/behavioral/network signals plus history.
3. **A decision vocabulary of allow / challenge (step-up) / block, plus review** — every product's output maps to this vocabulary, whether as a returned action (Castle), a recommendation (DataDome), an enforced challenge (Arkose), a workflow decision (Sift), or a risk-based access policy (Entra).
4. **The application (or identity platform) retains final enforcement** in the recommendation-style products; the protection layer advises or, in challenge-style products, interposes a verification step.
5. **Analyst operations surface** — dashboards with event exploration, review queues/lists, user-level investigation views exist in all products with documented consoles.
6. **Feedback loop** — decisions and outcomes (failed logins, confirm-compromise, decision feedback APIs) flow back to improve detection.
7. **Signal families recur**: device intelligence, network/IP reputation, identity-attribute intelligence (email/phone), behavioral automation detection, velocity/anomaly, cross-account correlation (one device/one IP across many accounts), credential-exposure signals (leaked credentials, password spray).
8. **Challenge/step-up as the friction valve** — between allow and block, all products support an intermediate verification step (MFA, email/2FA verification, CAPTCHA-style or adaptive challenges).

### Canonical inference (evidence layer C)

The Type can be modeled as a **risk-decision loop over account lifecycle events**:

```text
Account population
  └── Account-lifecycle events (registration / sign-in / credential & profile changes / sensitive actions)
        └── Signal enrichment (device, network, identity attributes, behavior, history)
              └── Risk evaluation (score / level / detections)
                    └── Decision (allow / challenge / block / review)
                          ├── enforced by the application (recommendation model)
                          ├── enforced by the product (challenge model)
                          └── enforced by the access layer (policy model)
                              └── Feedback (outcomes, analyst labels) → improved evaluation
```

## Abstraction Levels

### L0 — Defining Invariant

Minimal structure without which the Type is not recognizable:

1. **Monitored account-lifecycle events** on a population of user accounts (at minimum: sign-in and account creation; typically also credential/profile changes and sensitive actions).
2. **Per-event risk evaluation** of those events using technical/behavioral signals and history.
3. **Per-event enforcement decision** — an actionable output in an allow / challenge / block / review vocabulary that the application, product, or access layer acts on.

Remove the account-event framing → generic traffic/network security (Bot Management) or transaction fraud tooling. Remove risk evaluation → plain authentication logging. Remove the actionable decision → passive security analytics (SIEM-like), not protection.

### L1 — Common Mature Structure

Present in essentially all mature products, but not definitional:

- device fingerprinting / device intelligence
- IP/network reputation intelligence
- email/phone identity-attribute intelligence
- behavioral automation (bot) detection
- credential-exposure and attack-pattern detections (leaked credentials, password spray, brute force)
- velocity / anomaly / cross-account correlation rules
- ML risk scoring with explanatory signals/reasons
- custom rules/policy engine (trigger conditions → actions)
- allow/block lists and watchlists
- challenge orchestration (step-up to MFA / verification / CAPTCHA-style challenges)
- manual review queues / case lists / user-profile investigation views
- dashboards and attack analytics (timelines, overviews per flow)
- feedback APIs / webhooks / labeling that improve models
- automation hooks (webhooks, APIs) into adjacent security workflows
- configurable failure posture (fail-open vs fail-closed)

### L2 — Variant / Optional Structure

- **Population**: consumer/customer accounts (Castle, DataDome, Arkose, Sift) vs workforce identities (Entra ID Protection) — same loop, different population and enforcement locus.
- **Enforcement locus**: recommendation-only (application decides; DataDome explicitly, Castle effectively) vs product-enforced challenges (Arkose) vs access-policy enforcement (Entra Conditional Access).
- **Deployment/integration**: backend SDK/API instrumentation (Castle, DataDome) vs edge/CDN-embedded (DataDome platform heritage; Arkose Edge) vs native to the identity platform (Entra).
- **Product philosophy**: behavioral/no-puzzle (Castle) vs adaptive-challenge economics (Arkose) vs broad decision platform spanning payment fraud (Sift) vs identity-platform-native (Entra).
- **Scope**: account-focused point product vs full trust-&-safety suite (payments, content, ads — Sift, DataDome platform).
- **Managed service depth**: self-serve consoles vs vendor SOC co-tuning (Arkose claims 24/7 SOC).
- **Data network**: single-tenant models vs cross-customer consortium intelligence (Sift and Arkose claim global networks; single-tenant evidence for Castle's per-customer population statistics).

### L3 — Vendor-specific (Research Notes only)

- Castle: three named scores (Account Abuse / Account Takeover / Bot); `$`-prefixed event names; request-token mechanism; default policy thresholds (deny 90–100, challenge 60–100); specific signal category names; list auto-archivation.
- DataDome: Account Protect as a separate SKU from Bot Protect with its own API key; default 1500 ms timeout with fail-open; custom fields capped at 10 with PII flag; specific reason enums (`brute_force`, `teleportation`); failReason enum values.
- Arkose: Arkose Titan branding; Agent Trust Manager (AI-agent classification); challenge "generations"; ACTIR threat research unit; claimed signal counts (175+) and customer-story metrics.
- Sift: "Digital Trust & Safety" positioning; Sift Score API; Decisioning Engine / Network Intelligence / Automation & Workflows module names; claimed 1T+ annual events; FIBR benchmarking.
- Entra: Conditional Access integration; license-tier gating (Entra ID P2); specific role model; Defender-sourced detections.

## Vendor-specific Findings

See L3 above. None of these were promoted to the canonical model. Notably:

- The **three-score decomposition** (abuse vs takeover vs bot) is Castle-specific naming; DataDome expresses the same space as event types + reasons; Arkose as solutions; Entra as detection categories. The canonical space is the abuse typology (takeover / fake-account / privilege-abuse / automation), not any vendor's score names.
- **Fail-open on protection-layer failure** is documented for Castle and DataDome; treated as a common design posture (both documented it) but not universal — challenge-enforced products may differ. Kept in L1 as "configurable failure posture" with moderate wording.

## Boundary Findings

| Neighboring Type | Relationship | Distinction test |
|---|---|---|
| Fraud Prevention Platform | adjacent, heavily overlapping (Sift spans both) | Fraud prevention centers on **transactions/payments** (order fraud, chargebacks, cash-out). Account abuse protection centers on the **account lifecycle** (access, creation, account-linked privileges). Remove transaction/payment fraud focus → account abuse protection remains; remove account-lifecycle focus → generic fraud platform. Same event→score→decision loop, different protected object. |
| Bot Management / DDoS Protection Platform | adjacent; bot engines often feed account protection (DataDome, Arkose) | Bot management is **traffic-centric and account-agnostic** (protects availability, scraping, forms at the edge). Account abuse protection is **account-centric** (events tied to identified accounts). Remove the account/event model → bot management remains. |
| Multi-factor Authentication / MFA | capability relationship | MFA is a **challenge factor**; account abuse protection is the decision system that determines *when* step-up is warranted and orchestrates it. An MFA product does not evaluate account-event risk. |
| Customer Identity / CIAM | adjacent; suites increasingly bundle both | CIAM **administers** customer identity (registration, profile, consent, sessions). Account abuse protection is the **risk/enforcement layer over account events**. Remove risk evaluation/decision → CIAM remains. |
| Identity Verification | adjacent, both sit at onboarding | Identity verification is **point-in-time real-world identity proofing** (documents, biometrics). Account abuse protection is **continuous behavioral/technical risk evaluation** of account events. |
| SIEM | adjacent | SIEM is **log-centric, estate-wide, detection + alerting** without inline per-event enforcement in the user flow. Account abuse protection is **inline, account-event-centric, decision-producing**. |
| Insider Risk Management | adjacent (workforce) | Insider risk addresses **trusted users' behavior** (data exfiltration, policy violations). Account abuse protection addresses **external attackers and abusers** hitting accounts (stolen credentials, bots, fraud farms). Different threat model, same population in the workforce case. |
| Digital Risk Protection | distinct | Digital risk protection monitors the **external threat landscape** (brand abuse, phishing infrastructure). No account-event enforcement loop. |
| Threat Intelligence Platform | input relationship | Threat intel feeds signals/reputation; it does not itself evaluate account events or issue per-event decisions. |

Historical / market-sample check (per §24):

- **Precursors**: standalone CAPTCHA services, IP blocklists, WAF rate-limit rules lack per-event account risk evaluation and an account-centric decision loop → they are components/precursors, not the Type. The L0 correctly excludes them.
- **Workforce-side products** (Entra ID Protection): satisfy the L0 (sign-in events → risk level → risk-based access decision) with a different population → the canonical model must not be consumer-only; population is L2.
- **Bank risk-based authentication** (older pattern): same loop (sign-in risk → step-up decision) → fits L0; confirms the Type predates current vendor branding.
- **Abuse-desk / content-abuse tooling** (email spam handling at providers): content/traffic abuse, not account-lifecycle events → does not fit, correctly a different Type.

## Uncertainties

1. **Sift operational model** is inferred from Tier 2 homepage material only (journey model, product names, console mock). Its documented event/decision API shape could not be verified. All Sift-specific structure is marked Tier 2.
2. **Arkose enforcement details** (how challenges integrate into login flows, API shape) could not be verified from docs; only the vendor's own description (Tier 2).
3. **Category naming**: the market uses many labels — "account takeover protection", "account security", "bot & abuse prevention", "Digital Trust & Safety", "identity threat protection". Whether the market treats this as one category or as a bundle of capabilities is a positioning question; structurally the sampled products share the L0 loop.
4. **Fail-open vs fail-closed**: documented fail-open for two products; whether challenge-enforced products also fail open is unverified.
5. **Workforce variant boundary**: Entra ID Protection is structurally isomorphic but lives inside an identity platform; whether workforce-side "identity threat protection" should eventually be a separate leaf or a variant is left to the joint review with IAM/ITDR leaves.

## Final Synthesis

**Account Abuse Protection** is an application that protects a digital service's user accounts from abuse by running a continuous risk-decision loop over account-lifecycle events: it instruments account events (sign-in, registration, credential/profile changes, sensitive actions), enriches each event with device, network, identity-attribute, behavioral, and historical signals, evaluates an account-related risk (takeover, fake-account, privilege-abuse, automation), and produces an actionable per-event decision — allow, challenge (step-up verification), block, or flag for human review — which the application, the product, or the access layer then enforces, with analyst review and outcome feedback closing the loop.

The defining core is the loop itself (account events → risk evaluation → enforcement decision). Device fingerprinting, reputation networks, ML scoring, rules engines, review queues, and challenge mechanisms are the common mature machinery that makes the loop effective but do not define the Type. Population (consumer vs workforce), enforcement locus (recommendation vs enforced challenge vs access policy), and deployment (API vs edge vs identity-platform-native) are variants.
