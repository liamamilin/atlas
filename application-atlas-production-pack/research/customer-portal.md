# Research Notes — Customer Portal

## Research Goal

Establish what a Customer Portal is as an Application Type: what the customer actually sees and does in it, what structures define it, how it relates to the organization's back-office systems, and where its boundary lies against adjacent Types — especially Self-service Support Portal (§07, processed, which flagged this pass as its boundary counterparty and prescribed a swap test), Help Desk (§07, processed), E-commerce Storefront (§05.01), the family of industry/audience-specific portals (banking, patient, tenant, member, investor, employee, government — all processed as separate Types), Partner/Seller/Supplier portals, and CIAM (§15, processed).

## Initial Boundary

- Working hypothesis (inherited from prior passes): the customer's general account/aggregation surface — orders, billing, subscriptions, documents, profile, with support requests as one stream — as opposed to the support-relationship center (answers + requests) documented by the self-service-support-portal pass.
- Prior passes describe this leaf from the outside:
  - help-desk (processed): "the customer's general account/aggregation surface (orders, documents, requests); support requests are one slice."
  - self-service-support-portal (processed): "support-relationship center (answers + requests + own-request tracking) vs account-relationship center (orders/billing/subscriptions/profile with tickets as one stream); the customer-portal pass should treat this document as its boundary counterparty and apply the swap test."
  - investor-portal (processed): same family shape (authenticated external parties, per-party scoped view, operator-published content) but for investment positions with regulated reporting content.
  - b2b-e-commerce-platform (processed): "self-service views (orders, invoices, balances) exist in both; here they are secondary surfaces of the commerce flow, there they are the whole."
  - information-portal (processed): "a company's authenticated self-service surface for its own customers' accounts and requests."
- Key risks to resolve:
  1. Naming collision: several support suites name their support-centered surface "customer portal" (Freshdesk explicitly; Zendesk's help-center "Customer Portal"; HubSpot's Service Hub feature). Does the Type collapse into the support portal?
  2. Center-of-gravity question: is the defining content "orders/billing" specifically, or the customer's account relationship more abstractly (which for service firms means files/tasks/approvals, not orders)?

## Research Questions

1. Who uses the portal, and what identity posture gates it (full accounts, SSO, lighter mechanisms)?
2. What records does the surface present, and how are they scoped (per person, per company/account)?
3. What can the customer DO without staff mediation?
4. How does the surface relate to back-office systems (CRM, ERP, billing, help desk) — window, store, or both?
5. Which capabilities are definitional vs common vs variant (KB, branding, notifications, company views, commerce actions)?
6. Where is the line against Self-service Support Portal, E-commerce storefront, industry portals, partner portals, CIAM?
7. Does the market's use of the name "customer portal" for support-centered surfaces break the Type, or is it a naming overlap?

## Representative Products

- **Microsoft Dynamics 365 / Power Pages** (enterprise portal-platform pole) — the SCM "Customer portal" template (B2B order processing) plus the Dynamics 365 template family (customer self-service, field service customer, order returns, partner, employee self-service). Tier 1 documentation reachable on learn.microsoft.com.
- **HubSpot Service Hub** (mid-market suite pole) — ships a feature literally named "Customer Portal" (recently renamed "support portal" in its documentation — key naming-collision evidence). Tier 1 KB articles reachable.
- **Oracle NetSuite** (ERP/CRM suite pole) — "Customer Portal" as a named CRM module: login + tickets + KB + order history/status + new orders + profile. Tier 2 official product page (Chinese site, server-rendered).
- **Clinked** (white-label client portal pure-play, SMB service-business pole) — files, tasks, approvals, messages, per-client branded spaces. Tier 2 official product page.

Secondary observations (positioning level): **Moxo** (repositioned as human-AI workflow orchestration; portals as one component; "no logins" magic-link participation posture), and real-world deployed portals surfaced by search (WIKA, BSC One, Britam, UiPath customer portals — existence-level only).

Rejected as primary samples (recorded per source-access limitation): Salesforce Experience Cloud (help site JS-rendered; product URL redirected to generic homepage — same limitation as the self-service-support-portal pass), Copilot the client-portal pure-play (docs transport error ×2; copilot.com now redirects to Microsoft's AI assistant), Zoho (URL guesses 404 ×2; help.zoho.com JS-blocked per prior pass), ServiceNow (not attempted after prior pass documented JS app + timeouts ×2).

## Sources

Tier 1 (official operational documentation, directly observed, fetched 2026-09-08):

- Microsoft Learn — "Dynamics 365 templates" (Power Pages): https://learn.microsoft.com/en-us/power-pages/templates/dynamics-365-templates (customer self-service, SCM customer site, field service customer, order returns, partner, employee self-service, community templates)
- Microsoft Learn — "Customer portal for Dynamics 365 Supply Chain Management overview": https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/customer-portal-overview
- Microsoft Learn — "Power Pages Templates" index: https://learn.microsoft.com/en-us/power-pages/templates/
- HubSpot Knowledge Base — "Set up a support portal" (updated experience, replaces the legacy customer portal): https://knowledge.hubspot.com/inbox/set-up-a-customer-portal (served under the new title)
- HubSpot Knowledge Base — "Manage customer portal settings (legacy)": https://knowledge.hubspot.com/inbox/manage-customer-portal-settings

Tier 2 (official product pages, positioning/feature level):

- HubSpot — Customer Portal feature page: https://www.hubspot.com/products/service/customer-portal
- Oracle NetSuite (China) — 客户门户软件 (Customer Portal software, under CRM > Customer Service Management): https://www.netsuite.cn/products/crm/customer-service-management/portal.shtml
- Clinked — White-Label Client Portal: https://www.clinked.com/
- Moxo — homepage (portals as component of workflow orchestration): https://www.moxo.com/

Unreachable / abandoned (failure-limit rule):

- Salesforce: help.salesforce.com not attempted (JS pattern documented by prior pass); salesforce.com/experience-cloud/overview redirected to the generic corporate homepage (no portal structure)
- Copilot (client portal): docs.copilot.com transport error ×2; copilot.com redirects to Microsoft Copilot (AI assistant) — product identity collision
- Zoho: zoho.com/subscriptions/customer-portal/ and .html 404 ×2
- Bing worked as a search aid (geo-localized, noisy); DuckDuckGo timed out ×2

## Product A — Microsoft Dynamics 365 / Power Pages

### Key observations (evidence layer A — official docs)

- The SCM **Customer portal** is "a Power Apps portals template that lets companies create an externally facing business-to-business (B2B) website for scenarios that are related to sales order processing," enabling "external enterprise customers to view and create data from the company's Dynamics 365 environment."
- Purpose statement: "communicates order processing information (such as order status or account information) directly from their Supply Chain Management system to their enterprise customers."
- Architecture: the portal is a **window onto back-office records** — it "depends on Power Apps portals and dual-write"; data must be synced (dual-write) from Supply Chain Management before it "can be surfaced in the Customer portal." The template "isn't expected to be completely functional. It just serves as an enabler."
- Vendor-stated boundary vs e-commerce: companies wanting a site "for non-enterprise customers… should consider creating a Dynamics 365 Commerce e-commerce website." The portal is for the enterprise-customer relationship; the storefront for consumer acquisition.
- Historical continuity: designed for companies "transitioning from Dynamics AX 2012… who previously used the AX 2012 Customer self-service portal" — the Type predates the current cloud suite.
- The **template family** shows the same machinery pointed at different relationships, each a separate template: customer self-service ("self-service knowledge and support resources… view the progress of their cases and provide feedback"), SCM customer site ("customers can create and view orders"), field service customer ("book new appointments, manage existing appointments, track their technician… automated service reminders… estimated technician arrival times"), order returns ("return their orders, view the status of their return request, view return history, and monitor their refund status"), partner (resellers/distributors/suppliers — different audience), employee self-service (different audience), community (peer-to-peer).
- Audience separation is vendor-structural: partner and employee surfaces are distinct templates, not configurations of the customer one.

## Product B — HubSpot Service Hub

### Key observations (evidence layer A — official KB + Tier 2 product page)

- Product-page definition: "A customer portal is a web page behind a login where customers can view, open, and reply to their support tickets." Portal = tickets + knowledge base; integrates with the CRM; portal access managed by assigning users to groups; theme editor (brand colors/logo/font/favicon) without code; 40+ languages; requires tickets; gated to Service Hub Professional/Enterprise (plan detail recorded here only).
- **Naming-collision evidence (strong)**: the KB article once named "set up a customer portal" is now titled "**Set up a support portal**" and states it "applies to the updated support portal experience, which **replaces the legacy customer portal**." The settings article is titled "Manage customer portal settings **(legacy)**" and recommends migrating to "the updated support portal experience." A vendor that named its tickets-only surface "customer portal" has renamed it "support portal" — the market itself is resolving the naming collision toward the support/account seam drawn by the prior pass.
- Setup anatomy (legacy article): portal name; portal domain + slug (dedicated domain with "customer portal" as primary content type); language follows the domain; support form (button text, form title) that "automatically creates a ticket associated with the logged-in user" (no email field needed); default inbox/help desk receiving portal tickets.
- **Scoped visibility as configuration**: customer ticket permissions — "Only tickets they're associated with" / "All tickets from their company" (primary company record) / "Selected customers can see company tickets" (contact-property criteria with AND/OR filters). Customers switch between "My view" and "Organization view" tabs.
- **Internal/external separation**: "To keep internal discussions private, use notes and comments for internal communication"; filtering rules can prevent internal emails from appearing in threads; "Any communication included in a conversation thread is visible in the customer portal."
- **Customer actions**: view open+closed tickets (listing with filter/search), open ticket detail with conversation threads (tabs per thread), reply with attachments (not in the initial message if the ticket has no messages yet), file a new ticket via the support form, **export the visible view to CSV**, close tickets themselves (configurable, with a closed stage per pipeline), reply to closed conversations (configurable).
- **Display is curated**: "Customers only see the ticket properties you choose to display"; columns selectable (up to 10 — number recorded here only); owner display name configurable; **the ticket label itself is renamable — "you can change the label to Orders, Cases, or Requests"** (direct vendor evidence that the same surface is repurposed across record types).
- Access machinery: access-group membership (registration emails) vs self-registration; authentication method incl. passwordless; consent notice (GDPR-style); idle session timeouts; system pages (register, sign-in, sign-out, access denied, password reset) editable.
- Sensitive-data setting: when enabled, "customers won't be able to view sensitive files in the support portal."
- Messages sent from the portal "will appear in the conversations inbox and be logged as an email engagement on the record's timeline" — the portal feeds the back-office record.

## Product C — Oracle NetSuite

### Key observations (evidence layer B/Tier 2 — official product page, Chinese site)

- Positioning: 客户门户 (Customer Portal) as a module under CRM > Customer Service Management: "在网络上为客户提供高度个性化的交互式服务" (highly personalized interactive service on the web). Customers can: 收到问题解答 (get answers), 完成交易 (complete transactions), 提交支持问题 (submit support issues), 查询知识库 (search the knowledge base).
- Key benefits list — the fullest single-surface account aggregation in the sample:
  - customers log in to the company's website to enter trouble tickets and access personalized content and relevant support documents;
  - password-protected access to support tools such as the Net Answers knowledge base;
  - **customers can update their own profile, view order history, check order status, and place new orders at any time**;
  - automatic receipt confirmation with a case number for service requests.
- This is the account-relationship center in one product: identity + profile + orders + cases + KB + transactions.

## Product D — Clinked

### Key observations (evidence layer B/Tier 2 — official product page)

- Definition (vendor FAQ): "A white-label client portal is a secure online workspace that clients access under your brand. It allows clients to share files, view updates, communicate with your team, and manage work in one branded place."
- "Instead of digging through email threads, scattered links, and disconnected tools, clients can log into one branded space to share documents, track progress, approve work, and stay in the loop."
- Per-client scoping: "separate client spaces so each client can access the files, conversations, and updates relevant to them."
- Feature inventory: group & 1-on-1 chat, @mention messaging, content following, guest share, file approvals, file uploading, file requests, version control, configurable dashboard widgets, white-label (logo/colors/domain/branded mobile app/custom email domain), email notifications, reachouts (announcements/newsletters to groups), granular permissions, task management, document management, integrations (Google Workspace, Microsoft 365, Zapier, Docusign, Jotform), mobile app.
- **No commerce records**: no orders, invoices, or billing center on the fetched page — the "account relationship" here is a service-delivery workspace (files + tasks + approvals + messages). This is the strongest single piece of evidence that the Type's content cannot be defined as "orders/billing" specifically.
- Industries named: accounting, agency, finance, insurance, legal, investment, M&A, real estate, healthcare, government, HR — the same machinery sold into verticals that the directory treats as separate portal Types (investor portal, patient portal, employee portal) when the domain object becomes specialized.
- Vendor-stated internal distinction: Clinked sells **Client Portal** and **Virtual Data Room** as separate solutions — deal-time confidential exchange vs standing client workspace.

## Secondary observations

- **Moxo** (Tier 2): repositioned as "human-AI workflow automation"; portals are one component ("Clients, vendors, and teams each get their own front door"). Participation posture: "Flow participants can take action easily. **No logins**, no set up, no email threads needed" — magic-link-style lightweight access coexisting with enterprise SAML SSO/role-based access. Evidence that the identity posture is a variant axis (full accounts ↔ lightweight links), not a fixed password-login requirement.
- **Deployed portals** (existence-level, via search): WIKA ("The Customer Portal is WIKA's online platform for enquiries and orders… your customer details…"), BSC One supply-chain portal, Britam insurance portal, UiPath customer portal — all login-gated, all named "Customer Portal" by their operators. Confirms the Type's real-world shape but no structural detail claimed.

## Cross-product Comparison

| Structure | Microsoft (SCM/Power Pages) | HubSpot | NetSuite | Clinked | Verdict |
|---|---|---|---|---|---|
| Identity-gated customer access | yes ("people from outside the organization can sign in to") | yes ("web page behind a login"; access groups / self-registration / passwordless) | yes ("客户可以登录您的网站") | yes ("clients can log into one branded space") | definitional (A×2, B×2); posture varies (Moxo no-login links) |
| Customer's own records, scoped to their account | yes (order status, account info from the company's SCM; per-enterprise-customer data) | yes (own tickets / company tickets; My vs Organization views) | yes (own profile, order history/status, own cases) | yes (per-client spaces: "files, conversations, and updates relevant to them") | definitional (A×2, B×2) |
| Self-service action on those records | yes (create/view orders; book appointments; return orders) | yes (open/reply/close tickets, submit form, export CSV) | yes (submit tickets, update profile, place new orders, complete transactions) | yes (upload, approve, comment, message, tasks) | definitional (A×2, B×2) |
| Support requests as one stream | yes (customer self-service template: cases) | yes (tickets are the center of their portal surface) | yes (cases with case numbers) | not featured (messages/tasks instead) | common, not definitional |
| Orders/commerce records | yes (SCM: create/view orders; order returns template) | absent | yes (order history, status, new orders) | absent | variant by business model |
| Documents/files | not evidenced in fetched pages | ticket attachments | personalized content + support documents | central (files, versions, approvals, requests) | variant by business model |
| Profile/account self-maintenance | account info view | underlying contact record | explicit ("update their own profile") | not directly evidenced | common |
| KB/help content | yes (self-service template) | yes (KB linked via portal) | yes (password-protected KB) | absent | common, not definitional |
| Branding/white-label/custom domain | yes ("modified to represent the company's brand") | yes (theme editor, brand assets, domain+slug) | implied (on the company's own website) | yes (white-label is the pitch: logo, colors, domain, mobile app, email domain) | common |
| Company/organization-scoped visibility | yes (enterprise customers; B2B framing) | yes (company tickets, My/Organization tabs, criteria-based) | implied (B2B) | yes (client spaces; guest share) | common; depth varies |
| Notifications | yes (service reminders, technician ETAs) | registration emails; portal messages logged to timeline | auto receipt confirmation with case number | email notifications, content following, reachouts | common |
| Back-office linkage | explicit (dual-write sync from ERP; portal "surfaces" data) | explicit (tickets from inbox/help desk; messages logged on CRM records) | explicit (CRM suite module) | integrations (Google/M365/Zapier/Docusign) | common; realization varies (window vs workspace-store) |
| Audience variants named by the vendor | partner / employee self-service / community as separate templates | — | partner relationship management as separate module | same machinery sold into investor/patient/employee verticals | structural: audience flip = different Type |
| Display curation | template customization | explicit (choose properties/columns; rename record label to Orders/Cases/Requests) | — | configurable widgets | common |

## Canonical Model

### Level 0 — Defining Invariant

A Customer Portal is the organization's authenticated, customer-facing surface over the customer's own account relationship, and it needs exactly three jointly-held structures:

1. **Identified external customers of the operating organization** — the user is a customer of the organization, gated by an identity mechanism (login accounts, federated SSO, or lighter identity pairing); never an anonymous visitor, never internal staff. Remove → the public website / marketing site.
2. **The customer's own account space** — a persistent, per-customer scoped presentation of the records the organization holds about this customer's relationship: their purchases and orders, money and billing, entitlements and subscriptions, documents, requests, and profile — visible to them (and to colleagues on the same customer account where configured), never to other customers. Remove → generic published content with no relationship leg.
3. **Self-service action on those records** — the customer acts on their own records without staff mediation: view, download, pay, update, submit, approve, manage. Remove → a static statement/report delivery, not a portal.

The jointly-held intent: **the customer manages their side of the relationship themselves, in one place.** The organization curates what appears and what actions are allowed; the customer operates the surface.

Load-bearing jointness: identity without scoping = a login wall over generic content; scoping without identity = impossible to deliver; visibility without action = a statement viewer. All three are needed for the Type.

### Level 1 — Common Mature Structure

- Branding/white-label and custom domains — the portal presents as the organization's own front door (all four samples; deepest at the pure-play)
- Support requests/cases as one stream among several, with customer-visible status and conversation (3 of 4 samples; absent at the pure-play)
- Knowledge base / help content reachable in or through the portal (3 of 4)
- Notifications (registration, change alerts, reminders; content-following)
- Organization/company-scoped visibility: multiple users per customer account, "my" vs "our company's" views, criteria-based access
- Back-office linkage: the portal surfaces records kept in CRM/ERP/billing/help-desk systems (window posture), or hosts the working records itself (workspace-store posture at the pure-play)
- Search/filter over one's own records; export of the visible view
- Access administration: access groups, self-registration, consent notices, session timeouts, editable sign-in system pages
- Display curation: which record types, which fields, which labels the customer sees

### Level 2 — Variant / Optional Structure

- Record-type emphasis by business model: orders/order-status (B2B commerce & supply chain), files+tasks+approvals+messages (service firms), cases+entitlements (support-heavy), subscriptions/billing (recurring-revenue)
- Commerce actions in-portal (order creation, returns, payments) vs view-only account information
- B2B account hierarchies (enterprise customers, company views) vs individual-consumer portals
- Realization packaging: platform templates (portal-builder), suite component, standalone pure-play
- Identity posture: full accounts / federated SSO / passwordless / magic-link lightweight access
- Embedded widget and branded mobile app form factors alongside the web portal
- Community/forum sections; AI assistants as era-driven surfaces
- Industry realizations (banking, patient, tenant, member, investor, student, government) — same family shape, specialized objects; separate directory Types

### Level 3 — Vendor-specific

- Microsoft: dual-write dependency; template-per-scenario packaging (customer self-service / SCM customer site / field service customer / order returns / partner / employee); one-site-per-environment limits; AX 2012 Customer self-service portal lineage; explicit "not for non-enterprise customers" boundary statement.
- HubSpot: legacy "customer portal" → "support portal" rename and migration path; ticket-label renamable to Orders/Cases/Requests; My view/Organization view tabs; property-criteria company-ticket visibility; portal messages logged as email engagements on the record timeline; sensitive-data setting blocks attachment viewing; plan gating (Professional/Enterprise); 40+ languages claim.
- NetSuite: Net Answers KB behind password protection; case-number auto-acknowledgment; portal positioned under CRM customer service management.
- Clinked: white-label depth (branded mobile app, custom email domain), reachouts, guest share, file requests/approvals, version control, ISO 27001/HIPAA/GDPR/SOC 2 posture; client portal vs virtual data room as separate products.
- Moxo: no-login magic-link participation; repositioning toward human-AI workflow orchestration with portals as one component.

## Rejected Findings

- **"Customer portal = support ticket portal"** — rejected. That is the Self-service Support Portal's center. HubSpot itself renamed its tickets-only surface from "customer portal" to "support portal" (documented above). In this Type, support requests are one stream; at the pure-play sample they are absent entirely.
- **"Customer portal = orders/billing only"** — rejected. Clinked's client portal has no commerce records; NetSuite's aggregates orders + cases + KB + profile. The record mix follows the business model; the invariant is the scoped account space, not any specific record type.
- **"A KB is definitional"** — rejected (absent at Clinked; present at 3 of 4).
- **"Password login is definitional"** — rejected as a rigid requirement; identity-gating is the invariant, realized through accounts, SSO, passwordless, or magic-link mechanisms (Moxo).
- **"White-label branding is definitional"** — rejected; it is presentation, universal in the sample but not load-bearing for the Type's structure.
- **"The portal is the organization's website"** — rejected; the portal is the authenticated, scoped layer behind/alongside the public site.
- **"AI agents/chatbots are definitional"** — rejected; era-driven surfaces.

## Historical / Market-Sample Check

- **AX 2012 Customer self-service portal** (named by Microsoft as the predecessor): order status and account information for enterprise customers, pre-cloud-suite — satisfies the core with none of the modern machinery.
- **NetSuite's portal** (2010s CRM-suite generation): login + tickets + password-protected KB + order history/status + new orders + profile update — satisfies the core.
- **Early-2000s "customer login" areas** on company websites (account details, downloads, invoice copies, ticket submission) — satisfy the core; the Type long predates modern suites and AI.
- The Type is inherently a web/digital surface; no meaningful pre-web antecedent exists (phone/IVR self-service is a different channel, not a portal). The historical anchor is the web-era authenticated account area.
- The three-structure core is therefore not over-fitted to the modern cloud-suite/AI pattern.

## Boundary Findings

1. **vs Self-service Support Portal (§07, processed) — the sharpest seam, swap test applied both directions.** The support portal centers the support relationship (organization-authored answers + self-initiated requests + own-request tracking) and deliberately presents only the requester's side of support. This Type centers the account relationship as a whole (purchases, money, entitlements, documents, profile, requests as one stream). Swap the content from tickets/answers to orders/billing/documents → Customer Portal; swap back → Self-service Support Portal. **Naming collision recorded**: support suites (Freshdesk explicitly, Zendesk's help-center surface, HubSpot legacy) market their support-centered surface under the name "customer portal"; HubSpot has since renamed it "support portal." The name does not determine Type membership; the structural center does. A surface holding only answers + requests is a Self-service Support Portal however it is named; a surface aggregating the account is a Customer Portal even if it also shows cases.
2. **vs E-commerce Storefront (§05.01)** — acquisition vs relationship. The storefront serves any visitor through catalog → cart → checkout; the portal serves identified existing customers over their standing relationship. Vendor-stated at Microsoft: non-enterprise customers → Commerce e-commerce website, not the customer portal. In-portal order creation is repeat-ordering inside an existing relationship, not storefront acquisition.
3. **vs industry/audience-specific portals (Online Banking, Patient, Tenant/Resident, Member, Student Services, Government Service, Investor, Mortgage Borrower, Employee Service — all separate directory Types)** — same family shape (authenticated external parties, scoped own-records view, self-service), but each carries a domain-specific object and regulatory posture (bank account, health record, lease, membership, investment position, employment, statutory services). Swap the domain object for the generic commercial relationship → this Type; swap it back → the specialized Type.
4. **vs Partner/Dealer/Seller/Supplier portals (PRM, Channel Sales, Seller Portal, Supplier Portal, Dealer Commerce Portal)** — audience flip: channel partners/sellers/suppliers vs end customers. Microsoft ships the partner surface as a separate template; NetSuite sells partner relationship management as a separate module; Clinked lists partner portal as a distinct use case.
5. **vs Help Desk / Customer Service Platform (§07)** — the staff-side operating application vs the customer-side surface. The portal consumes the desk's records (tickets, statuses); the desk consumes the portal's submissions. help-desk pass's framing confirmed from this side.
6. **vs Customer Identity / CIAM (§15, processed)** — the portal consumes identity machinery (sign-in, registration, SSO); it is not an identity system.
7. **vs Customer Communication Management (§07, processed)** — CCM produces and delivers the organization's outbound documents; the portal is the customer-initiated access surface where those documents are typically archived and retrieved.
8. **vs Customer Success / Customer Onboarding platforms (§07)** — vendor-side management of the relationship vs the customer's own surface onto it; a portal may be one of their surfaces, not the managed engagement itself.
9. **vs Virtual Data Room (§11)** — deal-time confidential document exchange vs the standing account relationship; Clinked sells them as separate products.
10. **vs Information Portal (§02.11, processed)** — public aggregation of information vs authenticated per-customer account surface; the information-portal pass drew the same line from its side.

## Taxonomy Observations

- The Type is real and independent: own user (the customer), own core objects (the account space and its record streams), own workflow (self-service management of the relationship). Keep as an independent Type.
- **Boundary issue to record**: the market name "customer portal" is contested — support suites apply it to support-centered surfaces (Self-service Support Portal Type). The structural center (account relationship vs support relationship), not the name, determines Type membership. HubSpot's rename is direct evidence of the market itself resolving this.
- Realization packaging spans platform templates (Microsoft), suite components (HubSpot, NetSuite), and standalone pure-plays (Clinked; Copilot unreachable). No conflict with the directory's §07 placement found.

## Uncertainties

- Salesforce Experience Cloud unreachable (JS help site; product URL redirected to the generic homepage) — the CRM-platform pole is covered by Microsoft's platform evidence instead; Salesforce-specific structures (Experience Builder, permission sets per audience) not observed.
- Copilot (client-portal pure-play) unreachable — the pure-play pole rests on Clinked alone plus Moxo at positioning level; invoice/payment modules common in that pole (per market knowledge) are NOT asserted.
- Zoho's customer/client portal structure not directly observed (URL 404s; help site JS-blocked per prior pass).
- ServiceNow CSM portal not attempted (prior pass documented JS app + timeouts ×2).
- Precise numbers observed at product level only (HubSpot column limit, language count, plan gating; Clinked claims) — kept here, not in the final document.
- Whether "profile self-maintenance" is universal could not be confirmed beyond NetSuite (explicit) and HubSpot (underlying contact record); kept "common," moderate wording.
- The pure-play pole's billing/invoice modules (Copilot-class products) are unverified this pass; the final document does not claim them.

## Final Synthesis

A Customer Portal is best understood as **the organization's authenticated front door to the customer's own side of the relationship**: the identified customer signs in and finds one persistent place holding their own records with the organization — what they bought, what they owe, what they're entitled to, their documents, their requests, their profile — and acts on those records themselves, within actions the organization has curated. The organization decides what appears and what is allowed; the customer operates.

The defining core is small: identified external customers + the customer's own account space + self-service action on it. Everything else — branding, KB, notifications, company views, commerce actions, back-office integration depth, AI surfaces — is mature structure layered on that core. The market realizes the Type as platform templates, suite components, and standalone pure-plays; the record mix inside the account space follows the business model (orders for commerce, files/tasks for service firms, cases for support-heavy businesses), which is why the core must be abstracted above any single record type. The name "customer portal" is also applied by support suites to their support-centered surfaces; structurally those belong to the Self-service Support Portal Type, and one sampled vendor has itself renamed that surface "support portal."
