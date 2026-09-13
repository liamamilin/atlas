# Research Notes — Self-service Support Portal

## Research Goal

Establish what a Self-service Support Portal is as an Application Type: what the customer-facing support self-service surface contains, who acts in it, what the customer does end to end, how the surface relates to the support operation behind it, and where the boundary lies against adjacent Types — especially Help Desk (§07, processed), Customer Portal (§07, unprocessed), Help Center / Knowledge Base Application (§02.06, unprocessed), Community Platform (§01.06, processed), Employee Service Portal (§09, processed), and Customer Service Platform (§07, unprocessed).

## Initial Boundary

- Working hypothesis: the customer-facing "self-service" side of the support relationship — self-help content + self-initiated requests + visibility of one's own requests — as opposed to the agent-side operating application (Help Desk).
- Prior passes describe this leaf from the outside:
  - help-desk (processed): "self-service portal with requester-visible own-request list" is a standard desk capability; Related-Types entry: "the requester-facing submission/tracking/KB surface; desks ship it as a component, and a portal without a desk behind it is not a desk."
  - employee-service-portal (processed): audience identity is the boundary (employees under employment identity vs external customers under customer accounts); "swap the population to external customers → customer self-service Type."
  - community-platform (processed): support communities are a segment variant of Community Platform; the portal centers organization-authored content plus case/ticket access, not member-generated discussion.
  - customer-identity-ciam (processed): the portal is a consuming surface — it delegates sign-in to CIAM.
  - returns-exchange-portal / investor-portal (processed): generic portals aggregate account/orders/tickets; specialized portals add a dedicated resolution workflow.
- Key risk to resolve: is this leaf an independent Type, or only a component of Help Desk / Customer Service Platform?

## Research Questions

1. What does a customer actually do in such a portal, start to finish?
2. Is the knowledge/answer layer definitional, or only common?
3. Is authentication required for the portal to be a portal?
4. What does the requester see of their own requests (statuses, conversation, history, org requests)?
5. How is intake shaped (forms, help topics, custom fields, deflection)?
6. What sits in the surface beyond KB + tickets (community, chatbots, service catalog, account data)?
7. How does the surface relate to the support operation behind it (ticket linkage, two-sided states)?
8. Where is the line against Help Center / KB products, Customer Portal, Community Platform, Employee Service Portal?

## Representative Products

- **Zendesk** (Suite + Guide) — market-defining customer-service stack; help center + customer portal as distinct named concepts; documentation reachable via Help Center API (HTML site is JS-rendered).
- **Freshdesk** (Freshworks) — SMB-to-mid tier; explicitly documents "Customer Portal" with a setup category; official support docs server-rendered (Tier 1).
- **Zoho Desk** — value tier; self-service documented via official feature/marketing pages and KB tutorial (help.zoho.com KB portal is JS-rendered → Tier 2 only).
- **osTicket** — open-source / minimal philosophy pole; official features page documents a "Customer Portal" feature (Tier 2 but precise).

Rejected as primary samples: ServiceNow (docs JS app, product page timed out ×2), Salesforce Experience Cloud (help site JS; product page generic CRM marketing), Microsoft Power Pages / Dynamics 365 self-service portal templates (guessed Learn URLs 404 ×2). The enterprise/CRM-suite pole is therefore under-sampled; noted in Uncertainties.

## Sources

Tier 1 (official operational documentation, directly observed):

- Freshdesk — "Overview of Freshdesk Portal", support.freshdesk.com/support/solutions/articles/50000003752 (fetched 2026-09-07)
- Freshdesk — "Portal Setup and Customization" category, support.freshdesk.com/support/solutions/45926 (fetched 2026-09-07)
- Zendesk — "Submitting and tracking requests in the help center Customer Portal", support.zendesk.com/hc/en-us/articles/4408846805530 (fetched 2026-09-07 via api/v2/help_center/articles JSON)
- Zendesk — "Help center guide for end users", support.zendesk.com/hc/en-us/articles/4408837910426 (fetched 2026-09-07 via API JSON)

Tier 2 (official product pages, positioning/feature level):

- Zoho Desk — "Empower your customers with self-service", zoho.com/desk/self-service-portal.html (fetched 2026-09-07)
- Zoho Desk — "Customer Service Resources", zoho.com/desk/help/ and KB tutorial zoho.com/desk/tutorials/knowledgebase/summary.html (fetched 2026-09-07)
- osTicket — "Features" (Customer Portal, Help Topics, Custom Fields), osticket.com/features/ (fetched 2026-09-07)

Unreachable / abandoned (per failure-limit rule):

- docs.servicenow.com (JS app) and servicenow.com product page (timeout ×2)
- help.zoho.com/portal KB (JS shell, empty ×2)
- support.zendesk.com HTML pages (JS shell; API JSON used instead)
- Salesforce: products page fetched but generic (no portal structure); help.salesforce.com not attempted after pattern of JS failures on sibling sites
- learn.microsoft.com portal-template pages (404 ×2)

## Product A — Zendesk

### Key observations (evidence layer A — official help articles, end-user guide + customer-portal article)

- The help center is explicitly described as "a complete self-service support option" for end users: find answers in the knowledge base, turn to the community "if available", and "if they can't find an answer, they can submit a request to an agent."
- Help center anatomy: knowledge base (categories → sections → articles) + community (posts organized by topics). Search runs across KB and community simultaneously; results in two columns. Content tags, search filters, AI/generative search answers exist.
- Request submission: "Submit a request" form; sign-in may or may not be required depending on setup; SSO can auto-sign users. As the user types a subject, suggested KB articles appear ("Encouraging end users to look for answers in the knowledge base can deflect tickets"); suggested articles are enabled by default.
- Form shaping: CC option, multiple organizations (select the org for the request), attachments, custom fields; default fields cannot be removed; request forms can be previewed; disclaimers per form possible.
- Tracking: profile → Requests; default columns Subject, ID, Created date, Updated date, Status, Requester; show/hide columns incl. custom fields (custom fields visible to customers only if field permission is "customers can edit/view"); filter (multi-select AND across filters, OR within), search requests; brand-scoped or cross-brand request visibility depending on account configuration.
- Organization requests: members of a shared organization can see and follow all organization tickets (admin-configured); subscribe/follow for notifications.
- Requester actions on a request: add comment, add CCs, change organization, mark as solved (only possible once the request is assigned to an agent), create a follow-up to a solved request (reopens as a linked new ticket), submit CSAT rating + comment on solved tickets.
- Service catalog (enterprise/IT flavor): a "Services" nav entry; services/assets can be requested with structured fields; a ticket is auto-generated; requests can be submitted on behalf of others (requester becomes CC).
- Statuses: a "customer portal ticket statuses" concept exists (article title observed; ladder not fetched — treated as generic "visible status").
- Multi-brand: request visibility across brands configurable; portals per brand implied (help center theme settings, brands).

## Product B — Freshdesk

### Key observations (evidence layer A — official admin docs)

- Explicit definition: "**Customer Portal**: This is the portal you can set up for your customers and enable complete self-service support. You can set up a customer portal that includes: Branded customer-facing support portal, where customers can raise and track support tickets; Knowledge Base with solution articles and FAQs; Community for customer collaboration."
- Sharp vendor-made distinction between **Agent Portal** (the operator side: respond to tickets, set up KB articles, reports, settings) and **Customer Portal** (the customer side). This corroborates the two-sided structure.
- Portal management: default portal per account; additional portals per product ("A portal is always associated with the product"); multi-product portal management from one place; portal name/URL/language settings; custom domain URL.
- Access control: allow users to sign up on the portal; sign-in via Google/Facebook credentials; CAPTCHA configuration.
- Sections management: "what you want to add to your ticket forms or who can access your Knowledge Base and Community" — i.e., visibility/access of sections configurable.
- Appearance: themes, multi-theme management (import up to 10 themes per portal — number recorded here only), WCAG accessibility theme out of the box, Liquid templating + code editor, collision detection for simultaneous admin editing.
- Ticket-related portal features: multiple ticket forms, advanced ticket filters, portal-specific ticket display ("shows tickets relevant to a specific portal"), article view counts ("tracks article popularity on the customer portal").
- Plan gating exists (multi-product portals from Pro plan) — plan detail, recorded here only.

## Product C — Zoho Desk

### Key observations (evidence layer B/Tier 2 — official feature pages + tutorial objectives; KB portal JS-blocked)

- Self-service framed as customer-initiated interactions through varied channels: knowledge base, chatbots, community forums, IVR (Gartner-style definition quoted on the page).
- Channels named: knowledge base; Zia (AI answer bot) and Guided Conversations (rule-based chatbot); community forums; IVR self-help.
- "Customer self-service portals" named as a category with high demand; Zoho Desk includes KB + ticketing + community + bots; self-service tools can be embedded in business websites via widget, browser extension, or mobile SDK ("one-stop destination approach").
- Self-service analytics: KB dashboard, community dashboard, Zia prediction — channel-performance reports (article performance, content gaps as tutorial objective).
- Employee self-service named as a supported variant (HR departments using the same machinery) — audience variant, corroborates the audience boundary.
- KB tutorial objective: plan content type/audience/strategy, set up KB, create articles, governance, article performance analysis "tailored for both humans and artificial intelligence."
- Structure of Zoho's own customer portal not directly observed (KB portal JS-blocked) — no product-specific structural claims made.

## Product D — osTicket

### Key observations (evidence layer B/Tier 2 — official features page; open-source/minimal pole)

- Named feature "**Customer Portal**": "All support requests and responses are archived online for end users. Users can login using their email address and a ticket number or they can register a profile for full access to all tickets they are associated with. Build out a robust knowledge base for users to self service their issues."
- Two access models: lightweight identity-pair access (email + ticket number → see that one request's archive) vs registered profile (full list of associated tickets). No branding/community/catalog machinery described.
- Intake shaping on the operator side feeds the portal: custom fields/forms/lists attached to web tickets; help topics route and can switch the form shown per topic ("design a specific form for each help topic").
- Confirms the minimal core: self-service request archive + request submission + KB. Everything else in bigger products is layered on.

## Cross-product Comparison

| Structure | Zendesk | Freshdesk | Zoho Desk | osTicket | Verdict |
|---|---|---|---|---|---|
| Organization-authored self-help content (KB/FAQ) | yes (KB categories/sections/articles) | yes ("Knowledge Base with solution articles and FAQs") | yes (KB channel) | yes ("knowledge base for users to self service") | definitional candidate (A×2, B×2) |
| Self-initiated request submission (no agent in the loop) | yes (Submit a request form) | yes ("customers can raise…support tickets") | yes (ticketing part of self-service) | yes (web tickets w/ forms+help topics) | definitional candidate (A×2, B×2) |
| Requester-visible own-request record (status + conversation) | yes (Requests list, per-request view) | yes ("raise and track") | implied by portal+tickets (B) | yes (online archive; login models) | definitional candidate (A×2, B×2) |
| Deflection at intake (suggested articles while typing) | yes, default-on | not directly fetched | bots/answer surfaces (B) | no | common (A×1 direct, B corroboration) |
| Search across content | yes (KB+community, tags, filters, AI answers) | implied (KB section) | yes (B) | not featured | common |
| Community forum as optional section | yes ("if available") | yes ("includes…community" as a section one manages) | yes (B) | no | common, optional |
| Branding/theming/custom domain | yes (theme settings) | yes (themes, Liquid, custom URL) | yes (B, embed/brand) | minimal | common |
| Access control (sign-up, social sign-in, SSO) | yes (sign-in optional, SSO) | yes (sign-up, Google/Facebook) | — (not fetched) | email+ticket# pair OR profile | common; posture varies |
| Visible per-request status | yes (status column, statuses article) | implied ("track") | — | archived thread | common; label sets vary |
| Organization/company request sharing | yes (shared organizations, follow) | portal-specific ticket display, per-product portals | — | — | variant (strong at one product, concept present elsewhere) |
| CSAT submission at resolution | yes | yes (CSAT configured in workflows; portal submission implied) | — | no | common |
| Service catalog (structured service requests) | yes (Services nav, auto-ticket) | no direct evidence | no direct evidence | no | variant, IT/enterprise flavored |
| Chatbot/AI answer surfaces in the surface | yes (generative search, AI agent answers exist) | era-standard (B) | yes (Zia, Guided Conversations) (B) | no | common, era-driven |
| Multi-brand / multi-product portals | yes (brand visibility config) | yes (portal per product) | — | no | common in suites |
| Embedded widget/SDK variant | yes (messaging widget exists in suite) | yes (B) | yes (widget/SDK) (B) | no | common |
| Anonymous vs authenticated access posture | sign-in may be required or not; unverified email gates Requests page | sign-up optional; public KB | — | email+ticket# pair without profile | posture varies; not definitional |
| Account/commerce data (orders, billing) | not in the portal surface (suite separates commerce) | not evidenced | not evidenced | no | belongs to Customer Portal, not here |

## Canonical Model

### Level 0 — Defining Invariant

A Self-service Support Portal is the organization's customer-facing self-service surface for support, and it needs exactly three structures:

1. **The self-help answer layer** — organization-authored support content (solution articles, FAQs, how-tos) published for customers to find answers themselves, organized and searchable. Remove → a bare "my tickets" page; the deflection purpose of the Type collapses; what remains is a request tracker, not a self-service portal.
2. **Self-initiated request intake** — the customer can submit a support request themselves through organization-shaped forms (request types/topics, structured fields), without an agent creating it. Remove → a pure published-content site, i.e., the Help Center / KB pole.
3. **The requester's own request record** — the customer can see and continue their own support requests: a persistent, identity-gated (or identity-paired) view of their requests with status and the request conversation, surviving across sessions. Remove → a content site with a contact form; the "relationship" leg disappears.

The organizing intent binding all three: **the customer resolves and manages support without an agent intermediary** — answers first, request fallback, tracked relationship view. This is the customer's side of the support relationship; the support team's side is a different Type (Help Desk).

### Level 1 — Common Mature Structure

- unified search over the answer content (and community where present), with filters/tags; AI answer surfaces in current products
- deflection at intake: suggested articles surfaced while the customer describes their problem
- structured request forms: multiple request types/topics, custom fields, attachments
- visible per-request status and change notifications; request conversation thread on the customer side
- CSAT/satisfaction capture at resolution
- access control: sign-up, social sign-in, SSO; public content vs gated personal views
- branding/theming/custom domain; multi-brand or multi-product portals in suite products
- community forum as an optional self-service section
- content-performance analytics (article views/popularity, content gaps) for the operators
- embeddable widget/SDK form factor alongside the full web portal

### Level 2 — Variant / Optional Structure

- service catalog with structured service/asset requests (IT/enterprise flavored; auto-creates tickets)
- shared-organization request visibility (see/follow the company's requests)
- community-led vs KB-led emphasis; chatbot-led self-service (guided conversations) as the dominant surface
- audience variant: same machinery pointed at employees (becomes the employee service pole — different Type in the directory)
- anonymous pair-access vs full-profile access (osTicket's two login models are a clean implementation illustration)
- headless/API portal construction; portal-builder platforms where the support surface is one template among many
- IVR/other self-service channels adjacent to (not inside) the portal

### Level 3 — Vendor-specific

- Zendesk: brand-scoped vs cross-brand request visibility configuration; "customer portal ticket statuses" ladder; request-list column show/hide incl. field-permission gating ("customers can edit/view"); follow-up-from-solved mechanics; services catalog nav details; unverified-email gate before showing requests.
- Freshdesk: Liquid templating + code editor; Marina WCAG theme; multi-theme import; collision detection in theme editor; portal–product binding; plan gating of multi-product portals.
- Zoho: ASAP embed platform; Zia; Guided Conversations; self-service BI dashboards (KB/community/Zia prediction).
- osTicket: email + ticket-number pair login.

## Rejected Findings

- "Self-service = AI chatbot" — rejected as definitional; bots are era-driven surfaces (present in 3 of 4 samples at marketing level, absent in the open-source sample; Zendesk documents the full portal working without any bot).
- "The portal is authenticated-only" — rejected; Zendesk may allow unsigned submission, osTicket offers pair-access, KB browsing is public in all samples.
- "The portal includes account/billing/order management" — rejected; that is the Customer Portal's center. No sampled portal surface centers commerce; support is the center.
- "Community is part of the definition" — rejected; explicitly optional ("if available") at Zendesk, section-managed at Freshdesk, absent at osTicket.
- "Every portal needs multi-brand/multi-product structure" — rejected; suite realization, not the Type.

## Historical / Market-Sample Check

- osTicket (open-source, minimal, older-generation) passes the three-structure core: KB + web request forms + online request archive with two access models. No community, no bots, no theming machinery.
- Web-1.0-era antecedents: static FAQ pages + mailto/contact forms existed, but without persisted requester-visible request records they are the ancestor of the Help Center pole, not of the portal. The Type's historical anchor is the era when vendors added the customer-visible request archive ("customer portal" naming in help-desk products).
- IVR self-service (a self-service channel, not a portal surface) is deliberately excluded from the core: the Type is web-surfaced.
- The three-structure core is therefore not over-fitted to the modern AI/SSO/cloud-suite pattern.

## Boundary Findings

1. **vs Help Desk (§07, processed)** — complementary sides of one relationship. The desk is the support team's operating application (queues, ownership, SLA, agent collaboration); the portal is the customer's side. Strip the desk machinery → the portal still stands (requests can be fulfilled by any means, even email); strip the portal → the desk still works (email intake). Every sampled suite ships the portal as a component; standalone portal-only products are rare. The help-desk pass's note ("a portal without a desk behind it is not a desk") holds — the portal is not a desk — but the customer-side structure is distinct enough to keep as its own Type.
2. **vs Help Center / Knowledge Base Application (§02.06, unprocessed)** — the content-only pole. Remove request intake + own-request visibility from this Type → a help center/KB product remains. The KB inside this Type is a deflection layer, not the managed corpus product.
3. **vs Customer Portal (§07, unprocessed)** — support-relationship center vs account-relationship center. A customer portal centers the account (orders, billing, subscriptions, profile) and may show tickets as one stream; this Type centers the support relationship (answers + requests). Swap the content from tickets/answers to orders/billing → Customer Portal.
4. **vs Community Platform (§01.06, processed)** — organization-authored help content + case access vs member-generated discussion. Support communities are a segment variant of Community Platform; a forum inside this Type is an optional section.
5. **vs Employee Service Portal (§09, processed)** — same machinery, audience flipped: external customers under customer identities requesting commercial support vs employees under employment identity requesting internal services. Swap the population → the other Type.
6. **vs Customer Support Chat / Customer Service Chatbot Platform (§07, unprocessed)** — live conversational surfaces vs asynchronous self-service surface. Bots may live inside the portal as a variant; the portal's center remains content + requests + own-request view.
7. **vs Customer Service Platform (§07, unprocessed)** — the broader operating suite; this surface is one of its customer-facing components.
8. **vs CIAM (§15, processed)** — the portal consumes identity machinery; it is not an identity system.

## Taxonomy Observations

- The Type is real but its market realization is overwhelmingly **as the requester-facing surface of a help desk / customer service suite**; standalone pure-plays are rare (the open-source pole ships it as a feature of the ticketing system; portal-builder platforms ship it as a template). Keep as an independent Type (own user, own core objects: content + own requests), record the packaging reality.
- Flag for the future customer-portal pass: the support-portal vs customer-portal seam (support relationship vs account relationship) — record explicitly there to prevent overlap drift.
- No conflict with the directory's placement (§07) found.

## Uncertainties

- Enterprise/CRM-suite pole under-sampled: ServiceNow unreachable (JS app + timeouts ×2), Salesforce structure not obtainable (generic marketing page only; help site JS), Microsoft portal templates 404. Enterprise-specific structures (deep service catalog, entitlement-based visibility, account hierarchies) are therefore asserted only from Zendesk's service-catalog/shared-organization evidence, with moderate wording.
- Zoho's customer-portal structure not directly observed (help.zoho.com JS-blocked ×2); Zoho findings kept at channel/positioning level (B).
- Exact requester-visible status ladders not fetched (Zendesk statuses article title observed only); kept generic in the final document.
- Whether suggested-articles-at-intake is universal could not be confirmed beyond Zendesk direct + Zoho bot corroboration; kept "common," moderate wording.
- CSAT-through-portal directly observed at Zendesk only (Freshdesk configures CSAT generally); kept "common," moderate wording.
- No precise numbers asserted in the final document (attachment limits, theme counts, CSAT windows, plan gating stay here).

## Final Synthesis

A Self-service Support Portal is best understood as **the organization's customer-facing front door for support self-service**: the customer comes to find an answer in the organization's help content, and when no answer fits, raises a support request through organization-shaped forms and then tracks and continues that request — seeing its status and conversation — without an agent intermediary. The surface deliberately presents only the requester's side of the relationship: the organization's published answers and the customer's own request records, never the support team's internal operation.

The defining core is small: self-help answer layer + self-initiated request intake + requester-visible own-request record, unified by the self-service intent (resolve without an agent). Everything else — search sophistication, deflection suggestions, SSO, theming, communities, bots, service catalogs, multi-brand structure, analytics — is mature structure layered on that core, and the market overwhelmingly realizes the Type as the customer-facing surface of a help desk or customer service suite.
