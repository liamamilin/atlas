# Research Notes — Disposable Email Service

Research date: 2026-09-07

## Research Goal

Understand what a Disposable Email Service actually is as an Application Type: what its defining structure is, how real products implement address issuance, receiving, inbox access, lifecycle and disposal, where the consumer "throwaway address" pole and the developer/QA pole diverge, and where the Type's boundaries sit against Webmail, email aliasing/forwarding services, and email-testing platforms.

## Initial Boundary (hypothesis before research)

- Core purpose hypothesis: provide a working email address that can be used once or briefly, without registration or personal identity, to protect the user's real mailbox from spam and tracking.
- Likely users: individuals doing one-off signups/downloads; developers/QA testing email flows.
- Nearest neighbors: Webmail Application (durable personal mailbox), Email Client, email aliasing/forwarding services (no directory leaf — potential taxonomy gap), Email Infrastructure Management / Email Marketing Platform (sender-side infrastructure), email-testing sandboxes (capture-style, adjacent).
- Expected boundary: disposable services receive mail into a self-contained inbox and are temporary; alias/forwarding services require an account and forward to a real mailbox with no inbox of their own.
- Unknowns going in: exact lifecycles per product, whether sending is ever allowed, how inbox access is protected, API depth on the dev pole.

## Research Questions

1. How is an address obtained? (instant-on-visit, self-chosen, random, API-created, bulk)
2. Does using the service require registration, a password, or any personal data?
3. Where does received mail live — a self-contained inbox in the service, or a forward into the user's real mailbox?
4. What is the address/inbox lifecycle? (countdown timer, session-bound, fixed retention window, kept until deleted)
5. Who can read the inbox? (anyone who knows the address / password holder / account owner / team)
6. Can users send mail from the disposable address, or is it receive-only?
7. What address controls exist? (custom name, domain choice, scramble/aliasing, sub-addressing, restore)
8. What interfaces exist? (web inbox, mobile app, browser extension, bot, developer API)
9. What rules/constraints matter? (spam filtering, abuse controls, no-reselling/API terms, external rejection of disposable domains)
10. Where does the consumer pole end and the developer/QA pole begin?

## Representative Products

Selected for market representativeness + documentation accessibility + different product philosophies + different customer tiers:

| Product | Pole / philosophy | Evidence |
|---|---|---|
| Guerrilla Mail | veteran consumer throwaway (since 2006), receive + compose sending, knowledge-based access, custom-domain paid tier | official site + About/FAQ page (fetched) |
| Maildrop | minimal consumer receive-only, self-chosen address, inbound spam filtering, GraphQL dev API | official site (fetched) |
| mail.tm | consumer + power users, auto-created password-protected mailbox, "kept forever or delete", REST API + SSE | official site + API docs (fetched) |
| DropMail.me | consumer, session-bound mailbox lifetime, permanent/rotating domains, optional forwarding, address restore, bot/app/API | official site (fetched) |
| Mailsac | developer/QA team platform, ad-hoc inboxes, private domains, CI/CD APIs, enterprise features | official site incl. FAQ (fetched) |

Boundary probes (not representative products):

- addy.io — email aliasing/forwarding service; API docs fetched to test the boundary (evidence: alias-centric object model, forward counters, no inbox/messages concept, account + API key required).
- mail7.io — historically a QA disposable email service; domain now serves unrelated content ("Mail Converter Hub") — recorded as Product Mismatch / market churn evidence.
- Temp-Mail.org, Mailinator — two of the most-cited names in this market; both returned 403 on all attempted URLs (root, FAQ, docs) — not directly verifiable this pass.

## Sources

All fetched 2026-09-07:

- Guerrilla Mail — root page https://www.guerrillamail.com/ ; About/FAQ https://www.guerrillamail.com/about (includes FAQ, Privacy, Technology sections; API page linked: GuerrillaMailAPI.html)
- Maildrop — root page https://maildrop.cc/ (includes how-it-works summary, developer section; developer docs at docs.maildrop.cc linked, not fetched)
- mail.tm — root page https://mail.tm/ (canonical https://mail.tm/en/) ; API docs https://docs.mail.tm/
- DropMail.me — root page https://dropmail.me/en/ (includes feature list, tips, forwarding, restore, domain policy)
- Mailsac — root page https://mailsac.com/ (includes FAQ); API docs https://mailsac.com/docs/api returned title only (JS-gated — limitation recorded)
- addy.io (boundary probe) — API documentation https://app.addy.io/docs/

Unreachable / failed sources (abandoned per retry discipline):

- https://temp-mail.org/en/ and /en/faq — 403 ×2
- https://www.mailinator.com/ and https://docs.mailinator.com/ — 403 ×2
- https://10minutemail.net/ — timeout; https://10minutemail.com/ — 403 (abandoned)
- https://mail7.io/ — serves unrelated content (domain no longer the product)
- https://www.guerrillamail.com/faq — 404 (FAQ content obtained via /about instead)

## Product Observations

### Guerrilla Mail (Layer A — directly observed)

- Self-description: "Guerrilla Mail gives you a disposable email address. There is no need to register, simply visit Guerrilla Mail and a random address will be given. You can also choose your own address."
- Use pattern as stated by vendor: "You can give your email address to whoever you do not trust. You can view the email on Guerrilla Mail, click on any confirmation link, then delete it. Any future spam sent to the disposable email will be zapped by Guerrilla Mail."
- Address issued immediately on page load (random local part), with ~11 selectable domains observed (sharklasers.com, guerrillamail.com/info/de/net/org/biz, grr.la, pokemail.net, spam4.me, guerrillamailblock.com).
- Controls observed: "Copy to clipboard", "Scramble Address", "Forget Me", "Refresh Inbox", "Inbox ID".
- Access model: "Since Guerrilla Mail doesn't require account registration, anyone who knows the Inbox ID may have access to that inbox." Scramble Address adds protection; scrambled addresses cannot be used as an Inbox ID.
- Lifecycle (vendor-stated): current version "keeps all incoming email for 1 hour… all addresses work all the time, they never expire." Quarantine → inbox pickup model; mail in inbox kept "1 hour more, or until the user deletes it"; undelivered mail marked abandoned. "The older version of Guerrilla Mail expired the address after 1 hour and bounced any inactive addresses." — direct evidence that both address-expiry and persistent-address models exist within one product's history.
- Privacy section: deletes all email delivered to an inbox after 1 hour; logs normally off; anonymized obvious-spam data used for anti-spam research; HTTPS only; session cookie.
- Sending: a Compose surface exists (/compose) — outbound mail capability observed.
- Custom domain feature: "Do you own a domain? Use it with Guerrilla Mail! Email arriving to your domain will be accessible only by you. Or, you may give access to everyone. Price: $9.99 USD / year." Payment via Bitcoin or PayPal. — vendor price, Layer A for this product, not generalizable.
- Webmaster/testing use named by vendor: "If you are a webmaster, Guerrilla Mail can also be used to test if your site sends the emails out correctly."
- No spam folder: "There is no spam folder / spam box. All emails that arrive at Guerrilla Mail are delivered to your inbox."
- API: documented API page linked; "our front-end uses this API for everything on this site."
- Tech: mail engine is open-source (go-guerrilla on GitHub); front-end PHP/JS with HTML fallback. Copyright 2006–2026 (veteran status). Multi-language site (10+ languages).

### Maildrop (Layer A — directly observed)

- Self-description: "Maildrop is a free disposable email address to use anytime." "No signup required — Maildrop is free for anyone to use when you need a quick, disposable email address."
- Three-step flow as presented: 1. "Make up your own email address" (suggestions offered, "Copied!" affordance); 2. "Give out the Maildrop address instead of your real email address… accepted everywhere — websites, apps, ecommerce stores"; 3. "Check your Maildrop inbox when you need… The sender will never send your real email address any messages."
- Use cases enumerated by vendor: signups where the site might share the address with advertisers; publishing an address where harvesting bots can find it; apps that shouldn't message you; companies with weak security; one-off ecommerce purchases; "receive exactly one email from a sender and then ignore every other email afterwards"; verifying a service that requires email confirmation; developer use: "automatically test the email sending capabilities of your own web application before launching" and "create mock test data for users in your own database."
- Inbound filtering: "Antispam by Heluna… The Heluna filters block almost all spam attempts before they even get to your Maildrop inbox." Live counters of blocked vs saved messages displayed.
- Developer API: "Easy HTTP access to email messages… one simple GraphQL interface… Send test email messages to Maildrop inboxes instead of regular users. The Maildrop API can help you automate retrieving and reading email messages." Docs at docs.maildrop.cc; curl example against api.maildrop.cc/graphql shown on page.
- Single domain (maildrop.cc) observed. Receive-focused; no sending surface observed.
- Operator context: "Created in California by Heluna"; build 4.0; privacy policy; public system-status page.

### mail.tm (Layer A — directly observed)

- Self-description: "A free service that gives you an email address and a password for it the moment you open the site, with no personal details required. The mailbox is created automatically, with no link to your identity… Receive messages and account activation codes without ever revealing your real address."
- Positioning pillars on page: Secure / Simple / Fast / Intuitive / Anonymous / Flexible / Smart / Free.
- Access model: "Every temporary mailbox is protected by a unique, automatically generated password. Nobody but you can see what's inside: not us, not other users, not would-be attackers." — per-mailbox password, contrasting knowledge-of-address products.
- Lifecycle: "The mailbox itself is kept forever; or delete it yourself, if that gives you more peace of mind." — direct evidence against auto-expiry being definitional.
- Scale: "an unlimited number of new ones… no limit on how many disposable addresses you create."
- Anti-ecosystem pitch: email as "digital passport" argument; use for "dubious websites, forums, chat rooms and social networks".
- Power users: "The latter get API access and a quick way to register disposable mailboxes in bulk. That opens up plenty of room for testing apps and services, or for running multiple accounts in online games, social networks and elsewhere."
- Surface: browser-based on any device; "Your browser can put it on the home screen in one tap" (installable web app posture).
- API (docs.mail.tm): REST, OpenAPI v3 spec; flow = get domains → create account (address+password) → get token → fetch messages; real-time via SSE; "No API key required"; free; rate limit stated as 8 QPS per IP; terms: no illegal activity, no reselling, no proxying/mirroring, attribution link required.
- Marketing self-description vs behavior: "we're not trying to pull you into an ecosystem."

### DropMail.me (Layer A — directly observed)

- Self-description: "Temporary email. Email for 10 minutes or more… disposable email for registrations" / "Our service offers you a disposable email address for anonymous registrations on distrusted services or websites."
- Lifetime model: "Your disposable mailbox is valid until you refresh this page. 10 minutes is not a limit any more!" and "Unlimited mailbox lifetime. Unlike 10minutemail com & others, email is valid for an unlimited time until you refresh/close this page. 10 minutes, 2 hours or an infinite amount of time are available to you — just keep the page open." — session-bound lifetime; also direct vendor-side attestation that the classic countdown-timer pole (10MinuteMail) exists in this market.
- Issuance: automatic address on load; "Unlimited number of disposable addresses: a new email address is created by one click"; "Additional address" control; random domain choice.
- Access model: "It is safe. Each temporary email address is unique and assigned once. You are the only person who can receive your emails." — exclusive-assignment claim (this product's posture).
- Domain strategy: "Some domains are permanent — always available, good for long-term use. Others are rotating ⏳ — they are periodically replaced with fresh ones, so they are less likely to be blocked by spam filters… For long-term use (creating accounts, subscriptions) choose a permanent domain; for short-term use (promo campaigns, downloads, software trials) a rotating domain may be a better choice." — domain lifecycle as product mechanic.
- Extended (sub-)addresses: `user-qweqwe@…`, `user.ololo@a.b.c.…` patterns deliver to the main inbox; "workaround when dropmail.me is banned or for the rapid creation of new addresses"; deleted together with main address; work with forwarding.
- Optional forwarding add-on: "Forwarding service forwards incoming emails from the temporary email to your real one… in case you forget your password"; enable/disable anytime; can be triggered by sending mail from the real mailbox to new@dropmail.me; forwarding stops when a rotating domain expires. — a disposable-inbox product with an alias-style capability attached (hybrid).
- Address restore: "Restore access" via saved passwords; "Get passwords"; "Last 20"; "It is only possible to restore email addresses, not emails. If you need your mails later, just download them before refreshing the page."
- Inbox features: attachments allowed; "Download all emails in .zip archive"; per-message HTML download; raw-mode fallback for undecodable mail; instant delivery claim.
- Surfaces: Telegram bot (@DropMailBot), Android app, API (beta) at /api/; 25+ language versions; captcha against scrapers ("Screen-scraping our website? Try our API instead!"); donations in crypto/PayPal.
- Ecosystem friction acknowledged in its own feedback form: problem options include "Email was not received", "Website rejects DropMail.me email address".

### Mailsac (Layer A — directly observed)

- Self-description: "Mailsac: Disposable Email Testing Platform" — "Immediately test your application's email delivery with our disposable email services. Designed to empower QA and Software teams with integrations throughout the testing process."
- Audience: QA/software teams; "trusted by thousands of teams"; "About half of mailsac's customers are enterprise scale."
- Ad-hoc issuance: "Ad-Hoc Inbox Creation — No need to create any of your inboxes ahead of time." FAQ: "You can send immediately to any address @mailsac.com or @ your custom domain. No need to create the inbox first." — addresses exist implicitly; the inbox materializes when used.
- Organization: "Create spontaneous inboxes based on whatever criteria you see fit: environment, role, or scenario. You can even create an inbox on each test case." "Unified Inbox View… multiple inboxes, recipients, and filters in a single view for you and your team."
- Access model: FAQ — "Email messages are private to your account when using a custom domain or custom private forwarding address. Sending to any address @mailsac.com works, but it's public and subject to throttling." — public-by-knowledge on shared domains vs private custom domains.
- Integration: "REST APIs… Web Sockets, and Webhooks… Jenkins, GitHub Actions, Selenium, GitLab CI, Bamboo"; API features listed: fetch body links, list messages, download attachments; custom forwarding to websocket/webhook/Slack requires reserving the address ("custom private forwarding address").
- Domain/namespace: "Zero Setup Subdomain service"; "BYOD — bring your own domain."
- Team/enterprise: SSO via SAML (business/enterprise plans), shared logins, team API keys, sub-accounts, enterprise billing, P.O. billing (enterprise), Information Assurance Program / security scanning / Vendor Risk Assessment support for finance/government/high-tech customers.
- Ecosystem-adjacent positioning: maintains comparison pages "Mailsac vs Temp Mail" and "Mailsac vs Mailtrap" (link titles observed on its own site; content not fetched — recorded as market-context only).
- Free account offered; sign-in/registration required for management features (unlike pure no-signup consumer poles).

### addy.io — boundary probe (Layer A — directly observed, API docs)

- Object model is alias-centric: Aliases (with active/inactive, pinned, labels, descriptions, restore-deleted, "forget"), Recipients (verified destination mailboxes), Domains, Usernames (with catch-all), Rules, Blocklist, Failed Deliveries.
- Counters per alias: emails_forwarded, emails_blocked, emails_replied, emails_sent; account-level totals for forwarded/blocked/replied/sent; bandwidth limits; alias/recipient/domain limits tied to subscription tier ("pro").
- Reply/send from alias supported (recipient allow-lists, from-name, PGP encryption options for recipients — protected headers, inline PGP, remove keys/signatures).
- Access: every endpoint requires an API key (Bearer token created in account settings) — account-bound, in contrast to mail.tm's key-less API and the no-account consumer poles.
- Crucially: there is no inbox/messages endpoint in the entire API surface — mail is forwarded to verified recipients, never held in a service-side inbox. This is the structural confirmation that alias/forwarding services are a different mechanism family from disposable-inbox services.

## Cross-product Comparison

| Dimension | Guerrilla Mail | Maildrop | mail.tm | DropMail.me | Mailsac |
|---|---|---|---|---|---|
| Registration required for issuance | No (visit → random address; custom name possible) | No (self-made name; suggestions) | No (auto-created mailbox + password on open) | No (auto on load; one-click more) | Free account for management; addresses on shared domain usable without setup |
| Address naming | random + self-chosen + scramble alias | self-chosen + suggestions | auto/local-part via API; domains endpoint | auto random + one-click + extended sub-addresses | arbitrary inbox names; subdomains; custom domains |
| Self-contained inbox | Yes (web inbox) | Yes (web inbox) | Yes (web inbox) | Yes (web inbox) | Yes (web unified inbox) |
| Inbox access model | anyone with Inbox ID (scramble mitigates) | anyone who knows address (single public domain) | unique generated password per mailbox | unique-assigned (vendor claim) + restore passwords | public on @mailsac.com; private on custom domains; account/team-scoped |
| Lifetime model | messages kept 1h; addresses never expire (current); older version expired addresses | not stated this pass | mailbox "kept forever; or delete it yourself" | valid until page refresh/close; restore addresses (not mail) w/ password | test-cycle; not stated this pass |
| Sending from address | Compose surface observed | none observed | none observed | none observed | none observed (receiving/testing focus) |
| Forwarding to real mailbox | — | — | — | optional add-on (enable/disable) | custom private forwarding (reserve required) |
| Developer API | documented API (front-end uses it) | GraphQL | REST + SSE, no API key, free w/ terms | beta API | REST + WebSockets + Webhooks, CI/CD-oriented |
| Custom/BYOD domain | paid ($9.99/yr observed) | — | domains endpoint (provider domains) | permanent vs rotating provider domains | zero-setup subdomains + BYOD |
| Spam/abuse posture | anti-spam research; no spam folder | Heluna inbound filtering | abuse protected framing; API terms | rotating domains to evade blocks; captcha for scrapers | throttling on public domain; enterprise security posture |
| Audience | consumer + webmasters | consumer + developers | consumer + power users | consumer + anonymous registrants | QA/software teams + enterprise |
| Surfaces | web (10+ languages) | web | web (installable) | web + Android + Telegram bot + API | web + API (docs, forums, status) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three properties; remove any one and the product stops being a Disposable Email Service:

1. **Identity-free address issuance** — a working email address obtainable without registration, personal details, or linkage to a durable personal account. (All five sampled products; addy.io fails this — requires account + verified recipients.)
2. **Self-contained receiving inbox** — mail sent to the address is received and read in the service's own inbox surface (web/app/API), not merely forwarded through to a real mailbox. (All five; addy.io fails — no inbox exists; DropMail's optional forwarding is an add-on on top of the inbox.)
3. **Disposability by design** — the address/inbox exists to be used briefly and then abandoned: lifetime is bounded by the product (session-bound, countdown, retention window) or terminable by the user (delete/forget/scramble), with no durable personal identity attached and no cost to walking away. (Guerrilla: 1-hour retention + Forget Me; DropMail: valid until refresh; mail.tm: kept forever but user-deletable and identity-free — the constant is walk-away-ability, not a fixed timer.)

Removal test: remove (1) → registration-gated durable mailbox = Webmail; remove (2) → alias/forwarding service; remove (3) → ordinary mailbox hosting.

### L1 — Common Mature Structure (common, not definitional)

- Instant, registration-free issuance; one-click additional addresses (all five).
- Inbox surface: message list (sender/subject/time) + message viewer with body rendering; refresh (all five).
- Copy-address affordance (Guerrilla, Maildrop, mail.tm observed).
- Address control: custom local part, domain choice, aliasing/scramble or sub-addressing (Guerrilla, Maildrop, DropMail, Mailsac).
- Deletion/destruction controls (Forget Me / delete / session end) (Guerrilla, mail.tm, DropMail).
- No-personal-data posture as an explicit pitch (mail.tm, Maildrop, Guerrilla).
- Developer API over the same inboxes (all five, varying maturity).
- Inbound spam/abuse handling (Maildrop/Heluna; Guerrilla; DropMail rotating domains; Mailsac throttling).
- Attachments + message download (DropMail, Mailsac).

### L2 — Variant / Optional Structure

- Inbox access model: knowledge-of-address (public-by-knowledge) vs generated password vs account-scoped private vs enterprise team-shared.
- Lifetime model: session-bound / countdown-timer / fixed retention / kept-until-deleted.
- Outbound capability: receive-only (most) vs compose/send (Guerrilla observed).
- Forwarding add-on (DropMail, Mailsac reserved addresses) vs pure inbox.
- Audience packaging: anonymous consumer registrations vs developer/QA testing platform vs enterprise QA with SSO/billing.
- Account layering: none vs free account vs paid tiers (custom domains, private inboxes, retention, teams).
- Surfaces: web page, installable web app, Android/iOS apps, browser extension (Guerrilla mask icon hints at alias masking; not confirmed), Telegram bot.
- Domain strategy: fixed domain set vs permanent vs rotating vs BYOD.
- Open-source / self-hostable engine (Guerrilla's go-guerrilla).

### L3 — Vendor-specific (research notes only)

- Guerrilla: Inbox ID + Scramble Address mechanics; 1-hour quarantine + 1-hour inbox retention; $9.99/yr custom domains with Bitcoin/PayPal; 11-domain set incl. guerrillamailblock.com; open-source go-guerrilla engine; 21.3B emails-processed counter.
- Maildrop: Heluna-powered filtering with live blocked/saved counters; GraphQL API with public curl example; "Created in California by Heluna"; build 4.0.
- mail.tm: unique auto-generated password; 8 QPS per-IP limit; attribution-required API terms; "digital passport" marketing frame.
- DropMail: restore-addresses-not-mail rule; "Last 20" password list; extended-address grammar (`name-suffix@`, `name.suffix@sub.domain@`); rotating vs permanent domain classes; crypto/PayPal donations; stand-with-Ukraine banner; @DropMailBot.
- Mailsac: zero-setup subdomains; Email Capture service; reserved "custom private forwarding address" concept; SAML SSO on business/enterprise; P.O. billing (enterprise, 2-year cycle recommended); Information Assurance Program / VRA support; comparison pages vs Temp Mail and Mailtrap.

## Evidence Notes

- All five representative products were verified from their own live pages on 2026-09-07 (Layer A). No numeric claims in the final document go beyond vendor-stated figures, and product-specific figures stay in these notes.
- Temp-Mail.org and Mailinator — among the most-cited market names — were unreachable (403). Their existence as major market participants is therefore supported only indirectly (DropMail's public comparison against 10minutemail; Mailsac's comparison page vs Temp Mail) and is not used to support any structural claim.
- The classic countdown-timer pole (10MinuteMail-style) is attested by DropMail's own page ("Unlike 10minutemail com & others… 10 minutes is not a limit any more") — vendor-side attestation, treated as evidence that the pole exists, not as a verified description of that product.
- Mailsac API docs page returned only its title (JS-gated); Mailsac's API surface is described from its homepage FAQ and feature links only.
- mail7.io no longer serves an email product (domain repurposed) — recorded as market-churn evidence supporting the Type's inherent impermanence, not as a structural finding.

## Boundary Findings

- **vs Webmail Application**: Webmail issues a durable personal mailbox behind a registered identity (folders, contacts, sending, long-term correspondence). Disposable services issue identity-free, disposable, receive-centric inboxes. Test: does obtaining and keeping the mailbox require a personal registration, and is the mailbox meant to persist as the user's address? If yes → Webmail. Both sampled poles pass the disposable side even with premium accounts (Mailsac) because address issuance itself remains identity-free and disposable.
- **vs email aliasing/forwarding services (addy.io, SimpleLogin-style; no directory leaf)**: those require an account, bind aliases to verified real recipients, forward mail through, and have no self-contained inbox (addy.io API has no inbox/messages concept — directly observed). Disposable services hold mail in their own inbox. Hybrid case: DropMail offers optional forwarding on top of its inbox — inbox remains primary, so it stays in this Type. The reverse (forwarding-primary, inbox-absent) is the other family. **Taxonomy observation: this alias/forwarding family has no leaf in §01.02** — flagged in STATUS Boundary Issues rather than silently merged here.
- **vs email-testing sandboxes (Mailtrap-style capture platforms; adjacent, no leaf)**: the developer/QA pole of this Type (Mailsac, Mailinator-class) still works by issuing real, receive-capable addresses. SMTP-capture sandboxes intercept an application's outgoing test mail before real delivery instead of issuing addresses for signups. Different mechanism, same buyer; vendors themselves maintain comparison pages between the two (link titles observed on Mailsac's site).
- **vs Email Marketing Platform / Email Infrastructure Management**: those operate the sending side (campaigns, deliverability infrastructure). Disposable services are a receiving/identity-shielding surface. No overlap in core objects.
- **External ecosystem rule (not a Type boundary but structurally load-bearing)**: recipients of disposable addresses (websites/services) commonly reject known disposable domains — directly evidenced by DropMail's own rotating-domain rationale, its feedback option "Website rejects DropMail.me email address", and Guerrilla's domain literally named guerrillamailblock.com. This adversarial dynamic shapes variant structures (rotating domains, extended sub-addresses, custom domains) and should appear in the final document as context, without asserting any specific site's behavior.
- **Historical / market-sample check**: the sampled veteran (Guerrilla Mail, ©2006) and the pre-modern structure (visit → address → inbox → discard) satisfy the definition with none of the modern conveniences (apps, APIs, premium tiers, installable web apps). Conversely, early forwarding-style "disposable email" services (account-based alias pools) fail the self-contained-inbox property — correctly excluded as a different mechanism family. Definition does not over-fit to any single era or implementation.

## Uncertainties

- Retention/lifetime numbers beyond Guerrilla's 1-hour are unknown; deliberately no numeric lifecycle claims in the final document.
- Sending capability: only Guerrilla observed with a compose surface; the rest of the sample is receive-focused. Outbound remains variant/optional, never definitional.
- Whether the two unreachable majors (Temp-Mail.org, Mailinator) exhibit any structure deviating from the synthesized model is unverified.
- Maildrop's inbox retention rules were not stated on the fetched page; no claim made.
- Browser-extension support was not directly confirmed for any sampled product (Guerrilla's "mask-alias" image suggests an alias-masking feature; not verified).
- Access-model taxonomy (knowledge-of-address vs password vs account) is well-evidenced within the sample but the market-wide distribution across these models is unknown.

## Final Synthesis

A Disposable Email Service is an email-receiving service whose defining core is: (1) identity-free issuance of a working email address, (2) a self-contained inbox in the service where mail to that address is received and read, and (3) disposability by design — the address/inbox is meant to be used briefly and abandoned, whether through auto-expiry, session-binding, retention windows, or user deletion. Everything else commonly seen — countdown timers, passwords, forwarding add-ons, custom/rotating domains, mobile apps, developer APIs, enterprise QA features, outbound sending — is common mature structure or variant structure, not definition. The nearest structural neighbors are Webmail (fails identity-free + disposability) and alias/forwarding services (fail self-contained inbox); the nearest audience neighbor is the email-testing sandbox (different mechanism, same buyer).
