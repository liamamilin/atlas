# Research Notes — EDI Platform

## Research Goal

Understand what an "EDI Platform" actually is as an Application Type: what objects exist inside it, what users do with it, how a business document flows from one organization's system to another's, and where its boundary sits against Managed File Transfer, Data Exchange Platform, Data Integration Platform, Manufacturing Supplier Collaboration, and e-invoicing products.

## Initial Boundary

Working hypothesis before research:

- EDI Platform = software for exchanging standardized business-transaction documents (purchase orders, invoices, ship notices) between trading partners in public standard formats (ANSI X12, EDIFACT, etc.), including translation, transport, and compliance tracking.
- Nearest neighbors: Managed File Transfer (file movement), Data Exchange Platform (dataset sharing), Data Integration Platform (intra-org pipelines), Manufacturing Supplier Collaboration (the collaboration loop that consumes EDI pipes), e-invoicing (regulatory invoice exchange), B2B e-commerce (storefronts).

Prior passes left flags for this pass:
- data-exchange-platform (§13, 2026-09-07): recorded three-way split — MFT = transfer-event file movement, EDI = standardized business-transaction documents, exchange = dataset offerings with entitlements; joint review recommended.
- manufacturing-supplier-collaboration (§16, 2026-09-09): EDI is transport/format machinery beneath that Type; the EDI pass should treat that Type as a consumer of its pipes.

## Research Questions

1. What is the unit of exchange — a file, a message, a document? What makes it "EDI"?
2. What is a "trading partner" in these systems, and what is held about each partner?
3. What does translation/mapping actually do, and who does it?
4. What transports exist (VAN, AS2, SFTP, API) and is any one definitional?
5. What is the document lifecycle — acknowledgment, validation, error handling, compliance?
6. How do products differ: network-centric vs managed-service vs API-first vs integration-platform?
7. Where is the seam vs MFT, data exchange, supplier collaboration, e-invoicing?
8. Would older (VAN-era, on-premise translator) products still fit the definition?

## Representative Products

Selected for market representation, different product philosophies, and different customer tiers:

1. **SPS Commerce** — retail-network pole; largest retail EDI network; full-service, supplier-facing Fulfillment product; network effects central.
2. **TrueCommerce** — managed-service + network pole; explicitly sells "EDI Platform" with fully-managed service tier; multi-industry (retail, manufacturing, wholesale, automotive, home furnishings); 35+ years heritage.
3. **Orderful** — API-first modern pole; developer-centric, cloud-native, self-service validation/rules engine; publishes full operational API documentation (docs.orderful.com).

Attempted and rejected: Cleo (both candidate URLs 404 ×2 — abandoned per network rule), IBM Sterling docs (403), Boomi (returned non-HTML). Sample is therefore 3 products; the integration-platform/on-premise pole is under-evidenced and noted in Uncertainties.

## Sources

- SPS Commerce — https://www.spscommerce.com/edi (Fulfillment product page), https://www.spscommerce.com/what-is-edi/ (EDI 101) — fetched 2026-09-10
- TrueCommerce — https://www.truecommerce.com/products/edi-software/ (EDI Platform overview, incl. FAQ explaining EDI process, VAN, mapping, standards) — fetched 2026-09-10
- Orderful — https://www.orderful.com/ , https://www.orderful.com/product/platform , https://docs.orderful.com/ (Quick Start), https://docs.orderful.com/v4.0/reference/order-to-cash.md (full O2C workflow) — fetched 2026-09-10

Evidence layers: A = directly observed on the cited page for that product; B = cross-product commonality; C = canonical inference.

## Product A — SPS Commerce

### Key observations

- (A) Positions EDI as "a common language of documents in the supply chain… between supplier and buyer"; documents named by number: EDI 850 (purchase order), EDI 856 (advance shipping notice), EDI 810 (invoice).
- (A) Fulfillment product: "All your necessary documents like orders, shipping notices, invoices and inventory updates from every channel… available through one easily-navigated dashboard… see what stage every order is in, right now." → a transaction dashboard over document flows.
- (A) "Fulfillment guides your team step-by-step through each trading partner's unique workflow" → per-partner requirement/guideline handling is a first-class concern.
- (A) Network framing: "world's largest retail network featuring 1,000,000+ connections, 46,000+ customers and 4,000+ retailers & distributors"; "Find a Retail Partner — search the largest retail network"; pre-built integrations to "over 100 ERP, WMS and other systems".
- (A) EDI Testing and Certification sold as a distinct product: "Meet the compliance requirements of your trading partners and customers" → partner-specific compliance testing is a market-visible function.
- (A) EDI 101 flow: business system generates document → converts to standardized EDI format → transmitted securely to partner's system → partner processes automatically → responds with its own EDI document.
- (A) Suite extensions beyond EDI core: Analytics, Assortment (product info), Revenue Recovery (deduction/chargeback), Relationship Management, Visibility Management, Performance Management (scorecards), E-Invoicing, Invoice Financing. These are separate products, not the EDI core.

## Product B — TrueCommerce

### Key observations

- (A) Sells the category name verbatim: "EDI Platform" is its own product line, separate from its E-Invoicing Platform, VMI Platform, and B2B eCommerce Platform → vendor-authored evidence that EDI platform ≠ e-invoicing ≠ VMI ≠ B2B storefront.
- (A) FAQ defines the EDI process in three steps: "preparation and organization of data, translation to the agreed EDI format, and the transmission of the EDI documents."
- (A) FAQ names the standards: "The most common EDI standards used globally include: EDIFACT, EDI XML, EANCOM, ANSI X12."
- (A) FAQ defines VAN: "A Value Added Network — or VAN — is a secure private network that acts as an intermediary to enable EDI connectivity between trading partners and other VANs"; transports: "files can be sent via a VAN or through direct connectivity methods such as FTP, SFTP, and AS2 depending on the requirements of the trading partner involved"; API access as an additional extension.
- (A) FAQ defines EDI integration: connecting the EDI system to ERP/back office "removing the need for manual re-keying"; defines EDI mailbox ("file storage area… where EDI messages are consolidated and stored for retrieval") and EDI hub (a buying organization sending orders electronically to suppliers, receiving electronic invoices).
- (A) Managed service tier: "A web-based EDI tool that translates your documents into the EDI format. EDI mapping to synchronize your system with your trading partners' systems. The EDI network that sends and receives electronic documents. Ongoing EDI support and maintenance services." → the four elements of a complete EDI solution per the vendor.
- (A) Capabilities: seamless business system (ERP) integration; global trading partner network ("over a million companies through a single connection"); EDI supplier portal (web form entry for suppliers without integration); expert support/managed service; "validated, production-ready transactions" as the go-live bar.
- (A) Industry-specific pre-configured platforms (TrueAuto automotive, TrueCommerce Home) → industry variant layer, explicitly packaged as add-ons.
- (A) Compliance framing: "Ensure 100% compliance with the specific EDI requirements to avoid chargebacks"; supplier onboarding "regardless of their technical capabilities".

## Product C — Orderful

### Key observations

- (A) Self-description: "unified EDI platform… from small businesses using Web EDI to global enterprises standardizing on an API-powered workflow. Connect once, automate your transactions, and trade with thousands of partners through a modern, scalable network."
- (A) Platform page: single API for every trading partner and transaction ("Integrate once to the Orderful API and access trade with any supply chain partner immediately"); guidelines validation ("tests your data against your trading partners' specific requirements, not just x12 standards"); rules engine for partner variance; network hosting "over 10,000 guidelines, communication channels, and testing scenarios".
- (A) API docs (Quick Start): transactions are first-class API objects — `GET /v3/transactions` returns items with `transactionType` ("850"), `direction` ("inbound"), `stream` ("test"/"live"), `createdAt`. → the transaction/document is the system's unit of record, with test vs live streams.
- (A) Integration formats table: Mosaic (simplified JSON schemas, "supported by our internal partner mapping and transformation platform… same integration for all of your partners without partner-specific logic"), OrderfulJSON (JSON modeled closely on X12/EDIFACT counterparts), X12 passthrough ("Upload X12 documents via traditional EDI communication Channels. AS2, SFTP, VAN etc") → the platform internally maps between partner-specific EDI and a normalized representation; passthrough bypasses the validation engine.
- (A) Order-to-cash workflow doc: full lifecycle 850 PO (inbound) → 855 PO acknowledgment (outbound, acceptance codes AC/RJ, line codes IA/IB/IC, backorder quantities) → 856 ASN (outbound, hierarchical shipment→order→pack→item structure, SSCC carton IDs matching GS1-128 labels) → 810 invoice (outbound); order change 860/865; delivery-state machinery (`deliveryState=pending`, `POST .../deliveries/{id}/approve`); test scenarios with a demo trading partner before going live.
- (A) Partner guidelines as managed content: "10,000+ trading partner guidelines already maintained in the network… Immediate access the moment a partner is published."
- (A) Web EDI product (Pixel) for partners without integration; shipping labels (GS1/UCC-128) as companion product; managed services as a tier.

## Cross-product Comparison

| Dimension | SPS Commerce | TrueCommerce | Orderful | Layer |
|---|---|---|---|---|
| Trading-partner relationship as managed record | per-partner workflows guided in-product; partner network directory | partner onboarding "regardless of technical capabilities"; pre-connected network | partner guidelines/channels/testing scenarios held in network; ISA-level addressing in API | B |
| Standardized business document as unit of exchange | 850/856/810 named; "common language of documents" | standards list: X12, EDIFACT, EANCOM, EDI XML | transactionType 850/855/856/810/860/865; X12/EDIFACT-modeled JSON | B |
| Translation/mapping internal↔standard | "data always gets mapped to the correct fields"; pre-built ERP integrations | translator + mapping as two of the four managed-service elements | internal mapping/transformation platform; Mosaic schemas remove per-partner logic | B |
| Managed transmission over multiple channels | network-mediated (VAN-class retail network) | VAN + FTP/SFTP/AS2 + API | AS2, SFTP, VAN channels + API | B |
| Document flow lifecycle & acknowledgment | order stage visible in dashboard; notifications on order changes | validated, production-ready transactions; monitoring by managed-service team | deliveryState pending→approved; 855/997-class acknowledgments; test→live streams; real-time monitoring | B |
| Per-partner compliance/validation | EDI Testing & Certification product | "100% compliance… avoid chargebacks"; ASN testing checklists | validation against partner-specific guidelines, not just X12 | B |
| Web EDI portal (form entry, no integration) | Fulfillment dashboard is supplier-facing web UI | EDI Supplier Portal explicit | Pixel (Web EDI) product | B |
| Retail-network effects (find/connect partners) | largest retail network, find-a-partner | 1M+ companies via network | 10,000+ guidelines, network grows | B |
| Managed service tier | full-service positioning | fully-managed service explicit | managed services as one solution | B |
| Suite extensions beyond EDI | analytics, assortment, deductions, e-invoicing, financing | VMI, e-invoicing, B2B ecommerce platforms | shipping labels, integration services | B (optional) |
| API-first self-service posture | Dev Center exists; sales-led | API access as extension | core identity | A (Orderful) |
| Industry pre-configured packages | retail/grocery verticals | TrueAuto, TrueCommerce Home | industry solutions pages | B (variant) |

## Canonical Model (L0–L3)

### L0 — Defining Invariant

An EDI Platform is the inter-organization document-exchange system of record whose defining core is exactly four jointly-held structures:

1. **The trading-partner relationship of record** — each partner held as an identified, configurable record carrying their connection setup and their document requirements/guidelines; exchange is always with a specific identified counterparty. Remove → anonymous file transfer or a generic API gateway.
2. **The standardized business document as the unit of exchange** — documents (purchase order, acknowledgment, ship notice, invoice, and their siblings) exchanged in a public, agreed standard format (X12, EDIFACT, EANCOM, EDI XML class) whose semantics both sides understand without private agreement on structure. Remove → custom point-to-point integration; the "standard" is what makes it EDI.
3. **Translation between internal representation and the standard** — mapping/conversion between the organization's own system data (ERP/accounting) and the standard format, in both directions, so documents flow without manual re-keying. Remove → passthrough file movement = MFT territory.
4. **The managed document flow with acknowledgment and compliance state** — each document instance tracked through delivery/acknowledgment/error state against the specific partner's requirements (acknowledgments, validation, test-vs-live promotion). Remove → a translator with a mail slot; no operable trading relationship.

Jointly-held load-bearing: (1 alone = partner CRM/contact list; 2 alone = a standards reference; 3 alone = a data-mapping tool; 4 without 1–3 = generic message monitoring; 1+2 without 3 = standards-compliant partners who still re-key by hand; 2+3 without 1 = a translator with nobody configured to talk to; 1+3 without 2 = custom B2B integration, not EDI).

### L1 — Common Mature Structure

- Trading-partner network with pre-connected partners (network effects; find-a-partner surfaces)
- Web EDI portal for partners without system integration (form-based order/invoice/ASN entry)
- ERP/accounting pre-built integrations (100+ systems at SPS; broad ERP catalogs at TrueCommerce/Orderful)
- Test environments / transaction testing / certification before go-live
- Real-time transaction monitoring dashboards, notifications, error resolution surfaces
- Managed-service tier (vendor staff performs mapping/onboarding/monitoring)
- API access alongside classic channels
- Document set breadth: orders, acknowledgments, ship notices, invoices, inventory, payment remittance class

### L2 — Variant / Optional

- Industry packaging: retail/grocery, automotive (OEM/EDI 830/862-class part-level flows), home furnishings, food & beverage (traceability/cold-chain), healthcare, logistics
- Standard-family emphasis: X12-dominant (North America retail) vs EDIFACT/EANCOM (Europe) vs regional e-invoicing mandates (Peppol)
- Transport posture: VAN-mediated vs direct (AS2/SFTP) vs API-native
- Operating model: fully-managed vs self-service vs hybrid
- Companion products riding the pipes: GS1/UCC-128 label generation, deduction/chargeback recovery, supplier scorecards, e-invoicing compliance, VMI
- AI-assisted mapping/rules suggestions (current-market era feature)

### L3 — Vendor-specific (Research Notes only)

- SPS: Fulfillment/Assortment/Analytics/Revenue Recovery/Relationship-Visibility-Performance Management product names; "1,000,000+ connections, 46,000+ customers, 4,000+ retailers" figures; Dev Center.
- TrueCommerce: TrueAuto, TrueCommerce Home branded industry platforms; "600M transactions each year", "3M+ accessible companies" figures; 35+ years heritage claim; ReplenishAI.
- Orderful: Mosaic vs Pixel vs Shipping Labels product names; "10,000+ guidelines", "50M+ transactions", "99.99% uptime" figures; ISA-id sender/receiver addressing; v3/v4 API versioning; learnedi.org.

## Historical / Market-Sample Check (§24 reasoning)

Would older, regional, platform-native products still fit? Yes:
- 1980s–90s VAN-era EDI: on-premise translator + VAN mailbox + paper partner agreements — satisfies all four L0 structures (partner setup, standard documents, translation, mailbox-based flow with functional acknowledgments). The modern API/network surfaces are L1, not L0.
- European EDIFACT-centric and Peppol-era e-invoicing exchanges fit with the standard-family axis abstracted (any public standard, not X12 specifically).
- Therefore L0 says "a public agreed standard format", not "ANSI X12", and "managed channels", not "VAN".

## Vendor-specific / Rejected Findings

- Retail document numbers (850/856/810) are the market's most common vocabulary but NOT definitional — EDIFACT, automotive, healthcare flows fit without them; L0 says "standardized business documents".
- VAN is NOT definitional (TrueCommerce FAQ itself lists VAN as one option among FTP/SFTP/AS2/API).
- Managed service is NOT definitional (Orderful's self-service API pole is clearly in-type).
- Network size claims, uptime figures, transaction volumes — vendor marketing numbers, L3 only.
- AI-native mapping/rules suggestions — era-specific current-market feature, L2 at most.

## Boundary Findings

1. **vs Managed File Transfer (§13)** — MFT's unit is the transfer event (a file moved reliably between points, format-agnostic); EDI's unit is the standardized business document whose content is semantically processed (validated against partner guidelines, acknowledged, mapped into business systems). Remove translation + partner-guideline semantics from an EDI platform → MFT. Remove file-movement generality from MFT and bind it to EDI standards → EDI. The data-exchange-platform pass's recorded split (MFT = transfer-event file movement, EDI = standardized business-transaction documents) is CONFIRMED from this side.
2. **vs Data Exchange Platform (§13)** — exchange = dataset offerings with entitlements (data products shared as datasets); EDI = transactional business documents exchanged per trading relationship. Different unit of record (dataset vs document instance), different access model (entitlement/catalog vs partner agreement), different cadence (query/bulk vs transaction stream). Keep-both.
3. **vs Data Integration Platform (§13)** — integration moves data inside one organization's estate; EDI's defining scope is inter-organization exchange under public standards between identified partners. ERP integration on the EDI platform is the bridge into the internal estate, not the defining act.
4. **vs Manufacturing Supplier Collaboration (§16)** — per that pass's flag: EDI is the transport/format machinery; collaboration products own the shared multi-step loop (demand record, supplier response, fulfillment closure) and treat EDI connectivity as one channel. From this side: the EDI platform's records are partner + document + guideline, not the collaboration loop's demand/response objects. The collaboration Type is a consumer of EDI pipes. Keep-both; boundary ratified on application-loop vs transport/format machinery.
5. **vs E-invoicing** — TrueCommerce ships EDI Platform and E-Invoicing Platform as separate products (vendor-authored seam): e-invoicing is regulatory/compliance-driven invoice exchange (often government-mandated, Peppol-class networks); EDI platform covers the whole business-document family under commercial trading-partner agreements. E-invoicing can be realized as a variant/overlay of EDI machinery but is positioned as its own Type. Keep-both; flag for the e-invoicing leaf's pass.
6. **vs B2B E-commerce Platform** — storefront/ordering portal vs document exchange; TrueCommerce ships both as separate platforms. Keep-both.
7. **vs API Management / Integration Platform (§12/§13)** — API management governs an organization's own APIs; EDI platform's API is one access mode to a partner-document exchange system whose defining content is EDI standards and partner guidelines, not API contracts.

## Uncertainties

- The integration-platform/on-premise pole (IBM Sterling B2B Integrator, Cleo, Boomi) could not be fetched (403/404). Claims about that pole's shape (deep mapping tooling, multi-format any-to-any translation, embedded-in-integration-suite packaging) are held at reduced confidence and not asserted in the final document beyond generic "some platforms" phrasing.
- Exact acknowledgment-type coverage (997/999 functional acknowledgments) was directly observed only as 855-class PO acknowledgment machinery at Orderful; the general "acknowledgment state" claim is kept at cross-product abstraction level.
- Precise timing rules (e.g., "855 within 24 hours") observed at Orderful are partner-specific guidance, not platform rules — excluded from the final document.
- Whether pure "EDI VAN services" (transport-only, no translation UI) count as this Type or a narrower service: not researched; noted as a possible taxonomy question.

## Final Synthesis

The EDI Platform is the system of record for inter-organization business-document exchange under public standards. Its center of gravity is the managed trading relationship: partner records carrying requirements, standard-format documents as the unit of exchange, translation binding internal systems to the standard, and a lifecycle that proves each document was delivered, acknowledged, and compliant. Everything else — networks, web portals, managed services, APIs, industry packages, companion analytics — is how mature products make that core operable at market scale.
