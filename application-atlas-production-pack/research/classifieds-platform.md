# Research Notes — Classifieds Platform

Research date: 2026-09-07
Leaf: Classifieds Platform (DIRECTORY §05.03 Classified Commerce; sibling leaf: Listing Marketplace)

## Research Goal

Understand what a Classifieds Platform actually is as a class of software: what objects exist inside it (ads, categories, locations, posters, conversations), who posts and who responds, how an ad moves from posting to expiry or sale, how contact between the parties works, how trust and safety are handled, how optional transaction services (payment/shipping) relate to the core model, and where the Type's boundaries lie against marketplace, directory, and vertical Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a classifieds platform is a self-publishing ad board organized by category and locality, where the platform's role ends at connecting the interested party to the poster; the exchange itself is arranged between the parties.
- Nearest confusions: Online Marketplace / Multi-vendor Marketplace (mediated transaction), Resale Marketplace (in-platform order + payment + dispute machinery — the resale-marketplace pass explicitly flagged this seam for recheck), Listing Marketplace (sibling leaf), Directory Application / Listings Platform (§02.11), Job Board (§09), Property Listing Platform (§17), Review Platform (§02.10), Service Marketplace (§05.02).
- Prior passes to reconcile:
  - resale-marketplace (processed): "vs classifieds-platform (§05.03 sibling, unprocessed) — the seam is the mediated transaction (in-platform order + payment + dispute machinery vs contact-and-arrange-yourself) … the classifieds side rests on structural inference (Craigslist unreachable), recheck when the sibling is processed."
  - babysitting-marketplace (processed): removal test "strip caregiver profiles + two-sided roles → classifieds".
  - association-job-board (processed): "Keep only the listings without candidate machinery → classifieds".

## Research Questions

1. What is an ad composed of, and who authors it?
2. How are ads organized (categories, locations, search)?
3. What is the posting flow (account, verification, fees, moderation)?
4. What contact models exist (messaging, contact relays, phone/email restrictions)?
5. What is the ad lifecycle (duration, renewal, pause, mark-sold, restore)?
6. What trust/safety machinery exists (reporting, moderation, scam guidance, safe-exchange)?
7. How do in-platform payment/shipping services relate to the core ad-contact model?
8. What roles exist (private vs professional posters, dealer/business packages)?
9. What is free vs paid?
10. Boundary tests vs marketplace / directory / vertical Types.

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

| Product | Market | Owner family | Philosophy pole | Evidence depth |
|---|---|---|---|---|
| Leboncoin | France | Adevinta | mature hybrid: free C2C core + escrow transaction service + deep professional ecosystem | A (help center + ranking rules + homepage) |
| Kleinanzeigen | Germany | Adevinta (ex-eBay Kleinanzeigen) | classic free C2C board + optional escrow ("Sicher bezahlen") | A (help center + 2 full articles) |
| Subito | Italy | Adevinta | generalist with shipping service (TuttoSubito), shops, gamification | A/B (homepage + service structure) |
| Kijiji | Canada | eBay | North American classifieds with paid boosts, user reviews, community help | A/B (community help, admin-authored) |
| OLX Group | global (emerging markets core) | Prosus | multi-country local brands, "paying listers" monetization, vertical spin-offs | B (corporate site only) |

Attempted and unreachable (recorded per source-access limitation rules):
- Craigslist — 403 on /about/help/ and /about/ (2 failures → abandoned). Matches the resale-marketplace pass limitation ("Craigslist unreachable").
- Gumtree — help desk is a JS application (2 failures → abandoned).
- Marktplaats — help desk JS application (abandoned).
- OfferUp — support portal timeouts (2 failures → abandoned).
- OLX India (help.olx.in, olx.in) — transport error / 403 (abandoned).
- OLX South Africa — service discontinued; page now redirects to AutoTrader/Property24 (market fact, not mechanics).
- Avito — 429 rate limit (abandoned).
- Locanto — 403 (abandoned).
- Facebook Marketplace — not attempted (Meta help surfaces historically bot-blocked; no reliable access expected).

Sample-skew note: 3 of 4 product-level samples are Adevinta-family (Leboncoin, Kleinanzeigen, Subito). Compensated with Kijiji (eBay, North America) and OLX Group (Prosus, global/emerging markets) + corporate-level evidence. US mobile-first classifieds (OfferUp class) and social-graph classifieds (Facebook Marketplace class) are NOT directly observed; claims about them are kept at structural-inference strength or omitted.

## Sources

Tier 1 (official operational documentation):
- Leboncoin Help Centre — https://assistance.leboncoin.info/hc/fr (fetched 2026-09-07)
- Leboncoin — Règles de référencement, de déréférencement et de classement des annonces — https://www.leboncoin.fr/dc/rules (fetched 2026-09-07)
- Leboncoin homepage — https://www.leboncoin.fr/ (fetched 2026-09-07)
- Kleinanzeigen Help Center — https://hilfe.kleinanzeigen.de/hc/de (fetched 2026-09-07)
- Kleinanzeigen — "Anzeigen" category — https://hilfe.kleinanzeigen.de/hc/de/categories/17006957523740-Anzeigen (fetched 2026-09-07)
- Kleinanzeigen — "Was ist „Sicher bezahlen"" — https://hilfe.kleinanzeigen.de/hc/de/articles/17211553583388 (fetched 2026-09-07)
- Kleinanzeigen — "Wie lange ist meine Anzeige online?" — https://hilfe.kleinanzeigen.de/hc/de/articles/17082474526236 (fetched 2026-09-07)
- Subito homepage — https://www.subito.it/ (fetched 2026-09-07; help center at assistenza.subito.it referenced but not fetched)
- Kijiji Community Connect — https://help.kijiji.ca/ + /c/getting-started/9 + /c/my-account/14 (fetched 2026-09-07)

Tier 2 (official product/corporate pages):
- OLX Group — https://www.olxgroup.com/ (fetched 2026-09-07)

## Product Observations

### Product A — Leboncoin (France) — evidence layer A

Positioning (homepage): "site de petites annonces gratuites … de particulier à particulier et de professionnels" — a free classifieds site for individual-to-individual AND professional trade. "Déposez une annonce gratuite … pour vendre, rechercher, donner vos biens de seconde main ou promouvoir vos services." Secure payment + delivery offered "pour les annonces éligibles" (eligible ads only).

Category structure (homepage navigation): Immobilier (real estate), Véhicules (vehicles), Matériel pro (professional equipment), Emploi (jobs), Mode, Maison & Jardin, Famille, Électronique, Loisirs, Services, Autres, plus Locations de vacances (vacation rentals) and Animaux (animals). Deep subcategory trees with attribute filters (brand, furniture type, clothing type, baby age ranges…).

Location structure: region → department tree (l/rp_* URLs); ads browsable by region/department.

Help-center structure (particulier vs professionnel split):
- Pro side: Mon compte Pro (account creation, team management, subscription & billing, messaging); Vendre sur leboncoin Pro (Transaction sécurisée pro, shipping management, dispute resolution); Mes annonces Pro (create/post, manage, boost visibility); Tourisme & Emploi Pro (online shop management, recruiting + CVthèque — resume database); Professionnel de l'automobile; Professionnel de l'immobilier.
- Consumer side: Acheter sur leboncoin (search & browse ads, pay securely, choose payment method, receive order, cancel/dispute); Vendre sur leboncoin (use the secure transaction, verify identity & manage payments, ship items, manage returns/cancellations/disputes, understand tax obligations); Mon compte (account, personal info, messaging); Mes annonces (create & post ads, manage, boost visibility, animal-specific ads); Automobile (sell/buy vehicle); Immobilier (tenant dossier creation/sharing, Pass Locataire+ paid verification); Confiance et sécurité (identify suspicious behavior, report/block, protection tools, cyber-threat reflexes); Tourisme & Emploi (online booking for hosts/travelers, candidate profile).

Transaction sécurisée (help article): "vendre et acheter des articles dans toute la France, sans avoir à sortir de notre plateforme … votre argent est en sécurité jusqu'à la fin de la transaction et une équipe vous est dédiée en cas de problème. Vous êtes protégé des arnaques qui peuvent survenir via des échanges par email ou par téléphone." — escrow-style protection; explicitly framed as protection against off-platform (email/phone) scams.
- Seller steps with secure transaction + delivery: post ad & choose delivery mode → buyer pays → confirm availability → prepare & ship → funds released. In-person sale ("je vends en main propre, face à face") is a supported mode: payment validated on the meeting day inside the messaging. Payments land in the "porte-monnaie" (wallet). Dispute machinery: cancel order / open dispute; non-conforming product flow with photo evidence.
- Secure payment for used vehicles: buyer identity verified by the payment provider; funds held on a secure account before transfer to seller; free for the seller; seller can check the buyer has sufficient funds before the appointment.

Paid posting: "Pourquoi mon dépôt d'annonce est-il payant ?" — posting is paid in certain subcategories of Véhicules and Immobilier; free quota ("combien d'annonces gratuites il me reste") otherwise.

Trust & safety: report-ad button on every ad page; block; guidance to always use the secure messaging; warnings about off-platform contact requests; account-blocking article (causes, funds handling during ongoing transactions, "we will never call you about account blocking" anti-phishing note).

Ranking & posting rules (dc/rules — extensive, direct evidence):
- One ad = one item: "Le texte d'une même Annonce ne doit pas proposer plusieurs biens"; text must describe the actual product ("nombreux produits à vendre" generic ads rejected); photos must represent the item and not be reused across ads; max 5 exchange references and 5 keywords per ad.
- Professional identification: ads posted for a professional must carry a valid SIRET (business registration) number.
- Category + location binding: "L'Annonce doit être déposée dans une catégorie correspondant à l'objet de l'annonce"; "L'Annonce d'un bien à vendre doit être déposée dans la commune où le bien est localisé" (with a regulated exception for auto brokers/mandataires with disclosure obligations).
- Price: total TTC in the price field (VAT-exclusive allowed only for defined professional equipment categories); professional prices must be > 0 except donations.
- Duplicates: cannot run the same ad simultaneously in several categories; must delete the existing ad before posting a new one for the same item; tolerated multi-region duplicates only for professionals with large stock + national delivery (goods) or per-department (services), max 5 per department for jobs.
- Prohibited content: foreign-language-only ads; off-site links; email/phone numbers in title/description; premium-rate numbers; political content; promotional/advertising content; photos with children, bare logos, links, contact info; prompt-injection attempts against moderation/ranking systems (explicitly prohibited).
- Prohibited items (non-exhaustive): weapons, drugs, tobacco, dangerous substances, adult content/services, gambling, medicines/cosmetics/miracle products, counterfeits, CITES protected species, taxidermy, donation appeals, NFT/crypto, certain intangibles (pre-sales, e-tickets, QR codes), unverifiable artifacts ("poupée hantée"), person-search notices, most mass-produced consumer goods; vehicles without registration card (carte grise); wrecked vehicles.
- Category-specific rules: Jobs — OFFRE section professionals-only, DEMANDE (skill offers) individuals-only; French-language legal requirement; ads must be dated and name the employer; anti-discrimination mentions list; pyramid schemes/VDI/casting/escort prohibited; "pay to access a job offer" prohibited. Vehicles — max 3 concurrent ads for individuals (rising to 5 from 18 March 2025), professionals more via Pro account; used vehicle must be sold with its registration card; Crit'Air certificate; mileage disclosure rules; leasing ads professionals-only. Real estate — max 3 concurrent ads for individuals; only owners or duly mandated posters; licensed professional categories (loi Hoguet card, notaries, etc.); DPE energy-performance disclosure with detailed mandatory mentions; rent-control zone mentions; agency fee disclosure rules. Several categories closed to professionals (Billetterie, Cours particulier, Covoiturage, Autres).
- Report mechanism: "Signaler l'annonce" button; reported ads violating rules are dereferenced.

### Product B — Kleinanzeigen (Germany) — evidence layer A

Help-center top categories: Anzeigen (ads), Nutzerkonto (account), Sicherheit (security), Kaufen mit "Sicher bezahlen" (buying with secure payment), Verkaufen mit "Sicher bezahlen" (selling with secure payment). Separate help site for commercial users ("Hilfeseiten für gewerbliche Nutzer") and a "Kleinanzeigen PRO" product referenced in package articles.

Ad management (Anzeigen category):
- Edit, delete, extend ("Wie verlängere ich meine Anzeige?"), deactivate ("Wie und warum deaktiviere ich eine Anzeige?"), add images, image-upload troubleshooting.
- Drafts: "Anzeigen-Entwürfe speichern und jederzeit bearbeiten" (save drafts, edit anytime).
- Absence pause: "Abwesenheit einstellen: Anzeigen pausieren" (pause ads while away).
- Restore: "Wie kann ich eine gelöschte oder abgelaufene Anzeige wiederherstellen?" (deleted or expired ads can be restored — but the duration article says an expired ad cannot be reactivated; the restore article presumably covers a window; recorded as product-specific nuance, not generalized).
- States: "Bald online" (coming online soon — pre-publication state); "Meine Anzeige ist aufgegeben, aber sie erscheint nicht in der Suche" (posted but not yet in search); "Meine Anzeige erscheint nicht unter 'Meins'".
- Duration: "Deine Anzeige bleibt auf Kleinanzeigen 60 Tage online" — 60 days standard; reminder email one week before expiry; extend by another 60 days within an 8-day window; fees may apply; expiry date shown in the "Meins" overview with an "Verlängern" (extend) button; expired ads cannot be reactivated; real-estate agent ads posted via FTP feed have no expiry date (professional feed integration).
- Ad details: financing via Smava (third-party financing referral); "KI-Beschreibungsfunktion" (AI description feature); "Wieso kann ich meine Telefonnummer nicht mehr angeben?" (phone number in ads restricted); "Warum kann ich bei der Anzeigenaufgabe keinen Preis eingeben?" (some categories have no price field); heart = favorite; "Verkaufsschild" (sold sign).
- Highlighting (paid): packages for private vehicle ads, private real-estate ads, commercial vehicle ads (without PRO); paying for paid options; invoices.
- Posting principles: report inadmissible ads; "Warum wurde meine Anzeige gelöscht?"; "Was darf ich bei Kleinanzeigen anbieten und was nicht?"; USK/FSK 18 media ratings; brand-article authenticity guidance; no narcotics.
- Search & find: real estate on a map (new feature); radius search ("Warum sehe ich Anzeigen ausserhalb meiner Umkreissuche?"); ad number/ID; saved searches with automatic email alerts for new results; search & filter guidance.

"Sicher bezahlen" (secure payment — full article):
- "Unser Zahlungssystem, das deine Transaktionen schützt … Sobald du bezahlt hast, kann der Verkäufer deinen Artikel versenden." Payment first, then shipment.
- Buyer protection: "Dein Geld ist sicher verwahrt, bis du deine Ware erhältst" (funds held in safekeeping until goods received); Germany-wide trade; protection from email/phone fraud; data privacy.
- Costs: item price + shipping + service fee (0,50 € + 4,5 % of purchase price) — precise figures recorded here only, not for the final document.
- Buyer protection triggers: item not shipped; delivered goods significantly deviate from description; counterfeit received; wrong/incomplete item delivered.
- Scope: shipping with buyer protection only within Germany.
- Off-platform warning: "Sicher bezahlen" is integrated only in Kleinanzeigen messages; a PayPal payment offered to you happens OUTSIDE the protected payment process. (Mirrors the marketplace-side offsite-transaction warnings — but here framed as "you lose protection", not "you violate rules".)
- Protection does NOT apply: after buyer accepts and payout released; item installed/repaired/parts removed; digital goods (tickets, software); perishables; normal wear; minor deviation; non-original packaging but working; shipping outside Germany; buyer chose neighbor/drop-off delivery.
- Roles: Kleinanzeigen reviews reported problems (item not received / significant deviation) and decides on the payout; payment processing by Adyen (licensed by the Dutch central bank), which holds the amount in escrow until receipt is confirmed or Kleinanzeigen decides; report problems directly in the transaction's message thread.

### Product C — Subito (Italy) — evidence layer A/B (homepage + service structure)

Positioning: "Compra e vendi gratis in sicurezza" (buy and sell for free, safely).
- Four top-level universes: Motori (vehicles), Market (goods), Immobili (real estate), Lavoro (jobs). Deep category navigation (Auto, Moto, Accessori, Caravan, Veicoli commerciali, Nautica…).
- Location-structured URLs (annunci-italia, annunci-lazio, …/roma/) — city/region browsing.
- Logged-in area: "I tuoi annunci" (your ads), "I tuoi ordini" (your orders — a transaction list exists), "SubitoPiù" (premium subscription), "I tuoi badge" (badges/challenges — gamification), "Il tuo garage" (garage — saved vehicle space), Preferiti (favorites), Ricerche salvate (saved searches).
- Business side: "Negozi e Aziende" (shops & businesses — ImpresaPiù shops directory), "Subito per le Aziende" (Subito for businesses).
- "TuttoSubito" service: buy/sell with shipping handled by the platform ("Servizio TuttoSubito" + separate "TuttoSubito per Professionisti" terms) — the shipping/transaction service pole.
- "Promuovi annuncio" (promote ad — paid visibility), "Consigli per la vendita" (selling tips), Regole (posting rules), Sicurezza (security), Magazine (editorial content), schede-auto (car model reference pages), mobile apps.

### Product D — Kijiji (Canada) — evidence layer A/B (community help, admin-authored)

Self-description (About Kijiji): "Buy, sell, or trade locally with Kijiji, Canada's leading online classifieds platform. Find cars, real estate, jobs, electronics, home goods, and services near you."
- Getting Started: registration, posting, search and alerts, messaging, profile settings.
- My Kijiji Account: posting, editing, "why an ad isn't showing or was removed", messaging, reviews, technical questions.
- Trust & safety (dominant theme of admin posts): phishing alerts (fake account-verification pages), "Pay-to-Post Classified Ad Scam" alert, vehicle-certification scam, rental scams & landlord verification, deposit/get-paid scams, "Why Kijiji Limits High-Risk Private Browsing to Protect Community Safety", "Buy and Sell Safe Zones set by Police" (safe-exchange locations), report buyer fraud / fake seller, cooperation with local authorities, off-platform contact scam alerts ("fake buyer asking to contact outside Kijiji").
- Reviews: user-to-user review system exists ("Cannot Receive or Provide Reviews" support threads).
- Paid advertising: ad boosting/promotion is paid ("Refund for Ad boosted in the wrong category", "Ad not showing and i have paid for it", "purchased the wrong advertising for an ad").
- Account restrictions: restricted accounts, "logged out due to unusual activity", locked out / unable to edit postings — enforcement machinery.
- Location: "I posted an ad in the wrong location", "Cant change location on posted ad" — location is bound at posting and hard to change.
- Messaging: replies to ads; "Unable to Send or Receive Replies from other Users" support category.
- Category-specific policy: Pet Rules & Policies (rehoming/adoption fees, backyard-breeder guidance).
- Regional compliance: "Understanding Sales Tax and the UVIP" (Ontario used-vehicle information package).

### Product E — OLX Group (global) — evidence layer B (corporate site)

- Positioning: "Building AI-native marketplaces people trust. Helping millions of people buy, sell, find jobs, homes and cars with confidence, every day."
- Scale/monetization: "11 well-loved local brands", "2 M+ monthly paying listers" — a large paid-lister population implies freemium posting + paid options at scale.
- Brand portfolio structure: horizontal OLX brand plus dedicated vertical brands — cars (AutoTrader SA, Autovit.ro, La Centrale, Otomoto, Standvirtual, Otodim), real estate (Imovirtual, Otodom, Property24, Storia.ro). Structural observation: classifieds groups spin high-value verticals out into standalone brands while keeping the horizontal generalist.
- Offices across Europe/Africa; AI used across moderation/repetitive work (newsroom articles).

### Archetype reference — Craigslist (NOT directly verified)

Craigslist was unreachable (403) in this pass and in the resale-marketplace pass. It is commonly cited as the founding web-classifieds archetype (city-based boards, categories, anonymized email relay, community flagging, free individual posting with paid select categories, no in-platform transaction). These characteristics are recorded as structural inference from secondary knowledge, NOT as directly observed facts, and are not used to support any precise claim in the final document. The historical check instead relies on the print-newspaper classifieds analogy (general knowledge, no precise claims) plus the directly observed products.

## Cross-product Comparison

| Dimension | Leboncoin | Kleinanzeigen | Subito | Kijiji | OLX Group |
|---|---|---|---|---|---|
| Self-published ads as central object | Yes (déposer une annonce) | Yes (Anzeige aufgeben) | Yes (Vendi / tuoi annunci) | Yes (post an ad) | Yes (listers) |
| Multi-category breadth | Very broad (goods, vehicles, immo, jobs, services, vacation rentals, animals, pro equipment) | Broad (goods, vehicles, immo, jobs, services…) | 4 universes (Motori/Market/Immobili/Lavoro) | Broad (cars, real estate, jobs, electronics, home goods, services) | buy/sell/jobs/homes/cars |
| Category + locality filing | Category tree + region/department; ad must be in the item's commune | Categories + radius search + map (immo) | Categories + city/region URLs | Categories + local trade; location bound at posting | Local brands per country |
| Ad lifecycle machinery | Manage ads; paid categories; free quota | 60-day duration, renew (+60d), pause, drafts, restore, "coming soon" state, sold sign | Your ads management; orders list | Post, edit, removal reasons, visibility states | Paying listers (implies posting + paid options) |
| Contact model | Secure messaging (messagerie); off-platform contact discouraged | Messages (Nachrichtenbox); phone numbers restricted in ads | Messaggi | Replies/messaging; off-platform contact scam alerts | — |
| Optional transaction service | Transaction sécurisée (escrow + delivery, eligible ads; in-person payment validation; wallet) | Sicher bezahlen (escrow via licensed PSP, buyer protection, Germany-only) | TuttoSubito (shipping service; pro variant) | Not observed (safe-exchange-zone guidance instead) | — |
| Private vs professional roles | Particulier vs Pro (teams, subscriptions, SIRET, category restrictions) | Private vs gewerblich (+ PRO packages) | Private vs Aziende/ImpresaPiù shops | Private + paid advertisers | 2M+ paying listers |
| Paid visibility products | Booster ma visibilité | Highlight packages (private vehicle/immo, commercial) | Promuovi annuncio | Ad boosts (refund threads) | Paying listers |
| Trust & safety | Report/block, suspicious-behavior guidance, identity verification for payments, account blocking | Sicherheit category, phishing guidance, buyer protection, account restriction | Sicurezza, badges | Scam alerts, safe-exchange zones, police cooperation, account restrictions | "marketplaces people trust" |
| User reviews | Not observed in fetched pages | Not observed | Badges (gamification) instead | Yes (user reviews) | — |
| AI features | Prompt-injection prohibition in ad rules; (AI used operationally per corporate news) | AI description feature | Not observed | Not observed | "AI-native marketplaces" positioning |
| Vertical spin-offs | Deep vertical experiences inside the product (immo dossier/Pass Locataire+, vehicle secure payment, CVthèque) | Real-estate agent FTP feed | Subito Motori with advanced filters; schede-auto | — | Dedicated vertical brands (cars, real estate) |

## Canonical Abstraction

### Level 0 — Defining Invariant

Three properties; remove any one and the product stops being recognizable as a classifieds platform:

1. **Self-published ad as the central object.** The offering (or seeking) party authors a short advertisement describing one specific offer or want — text, photos, price (where applicable), attributes — and publishes it themselves. Ads are transient postings, not catalog entries: one ad = one item/offer, no inventory depth, no merchant catalog.
2. **Category-and-locality filing.** Ads are filed in a category vocabulary (goods, vehicles, real estate, jobs, services…) and carry a location context; browsing by category and locality (with search on top) is the primary discovery model.
3. **Contact-first interaction model.** The platform's defining role is to publish the ad and connect the interested party to the poster (via messaging/contact relay). The exchange itself — negotiation, payment, handover or shipping — is completed between the parties as the default; platform-operated transaction services, where offered, are optional add-ons attached to eligible ads, not the defining structure.

Historical/market-sample check: print-newspaper classifieds (self-published via the paper, categorized — For Sale / Situations Wanted / To Let — locality = circulation area, contact by phone/mail, exchange arranged privately) satisfy all three without any digital feature. Early web classifieds (city-board archetype) satisfy them without escrow, shipping, reviews, or apps. Regional products across Europe/Africa/Americas satisfy them. The modern escrow/shipping services observed at Leboncoin/Kleinanzeigen/Subito are optional layers on the same core. L0 stands.

### Level 1 — Common Mature Structure

Present across the researched sample (Layer B) but not definitional:

- Time-bound ad lifecycle: post → active for a defined/renewable period → renew/republish → expire; mark-as-sold; delete; pause/vacation mode; drafts; (product-dependent) restore of deleted ads; pre-publication states.
- In-platform messaging bound to the ad, as the sanctioned contact channel; off-platform contact actively discouraged (scam warnings; contact info in ad text prohibited).
- Saved searches with new-result alerts (email/push); favorites/watchlist.
- Search + filters over category facets, price, location/radius; map views in some categories.
- Moderation & reporting: report ad/user; posting rules; prohibited-item lists; ad removal/dereferencing; account restrictions.
- Paid visibility products: highlight/boost/top-of-list options.
- Private vs professional account distinction with different rules and tooling.
- Photos/media as standard ad components; price field with defined no-price categories (give-aways, services, jobs).
- Free posting for private ads as the base model, with paid categories/options layered on (moderate strength — varies by category and market).

### Level 2 — Variant / Optional Structure

- Platform-operated transaction services: escrow payment + shipping + buyer protection for eligible ads (Leboncoin Transaction sécurisée, Kleinanzeigen Sicher bezahlen, Subito TuttoSubito); in-person payment validation as a supported mode (Leboncoin); regional scope limits (Germany-only at Kleinanzeigen).
- Identity verification services (payment-related identity checks; tenant-verification products).
- Paid posting for select categories (vehicles/real-estate subcategories at Leboncoin; paid ad products at Kijiji; "paying listers" at OLX scale).
- Professional ecosystem: Pro accounts with team management, subscriptions, storefronts/shops, feed integrations (FTP for real-estate agents), resume databases, recruiting tools.
- Vertical spin-offs: cars/real-estate/jobs as standalone brands or deep vertical experiences.
- Value-added services: financing referral, vehicle valuation, tenant dossiers, vacation-rental booking, editorial content/magazine, car model reference pages.
- User reviews/ratings of counterparties (directly observed at Kijiji only; gamified badges at Subito) — product-dependent.
- Regional regulatory machinery embedded in posting rules (energy-performance disclosures, rent-control mentions, business-registration numbers, media age ratings, used-vehicle documents, sales-tax guidance).
- AI assistance (ad-description generation; AI moderation/ranking; "AI-native" positioning).
- Anonymized/restricted contact (phone numbers disallowed in ads; messaging-only contact).

### Level 3 — Vendor-specific (research notes only)

Kleinanzeigen: 60-day duration, 8-day renewal window, 0,50 € + 4,5 % service fee, Adyen as PSP, Smava financing, KA Pur ad-free subscription, "Bald online" state, Verkaufsschild, FTP real-estate feed without expiry, USK/FSK ratings.
Leboncoin: porte-monnaie wallet, Pass Locataire+, Cote Argus®, CVthèque, Mondial Relay carrier notice, SIRET requirement, carte grise/Crit'Air/DPE/loi Hoguet/rent-control machinery, max-3-concurrent-ads limits (→5 from 18 March 2025), 5-reference/5-keyword limits, "poupée hantée" prohibition, prompt-injection clause.
Subito: SubitoPiù, badges/challenges, garage, TuttoSubito pro terms, ImpresaPiù shops, schede-auto.
Kijiji: Community Connect (Discourse), UVIP/sales-tax guidance, pet policies, high-risk-browsing limits.
OLX Group: brand names (Otodom, Otomoto, Storia.ro…), "2M+ monthly paying listers" figure, AI-native positioning.

## Vendor-specific Findings

See Level 3 above. None of these are promoted to the canonical model. The escrow services deserve special note: they are the most consequential optional layer and are directly evidenced at three products, but they remain category-eligible add-ons ("annonces éligibles"; Germany-only; shipping-only scope), and the in-person/off-platform completion of exchanges remains a supported or at least tolerated default across the sample — which is exactly what separates the Type from marketplaces, where off-platform completion is a rule violation (Grailed evidence, resale-marketplace pass).

## Boundary Findings

1. **vs Resale Marketplace (§05.19, processed) — RESOLVED with classifieds-side evidence.** The resale pass recorded: "the seam is the mediated transaction … the classifieds side rests on structural inference (Craigslist unreachable), recheck when the sibling is processed." This pass supplies the classifieds side directly: Leboncoin supports in-person sales with payment validated at the meeting inside its messaging (the exchange completes between the parties, on the street, with the platform merely recording/validation); Kleinanzeigen explicitly frames off-platform payment (PayPal) as "outside our protected process" — a protection warning, not a violation; Kijiji publishes police safe-exchange-zone guidance for face-to-face meet-ups. The structural test holds from both sides: remove the mediated transaction (order + payment + dispute machinery as the defining center) → classifieds; add it as the mandatory center → marketplace. Both leaves stand.
2. **vs Online Marketplace / Multi-vendor Marketplace (§05.02, unprocessed).** Supply identity: classifieds run transient self-published ads (one ad = one offer, no inventory); marketplaces run merchant catalogs with inventory, carts, checkout. Horizontal marketplaces blur at the edges (the eBay heritage spans both). Joint awareness recommended when §05.02 is processed.
3. **vs Listing Marketplace (§05.03 sibling, unprocessed).** Same family. The observed market spans a pole where the ad-contact model is pure (Kijiji-class) and a pole where platform transaction services are heavily productized (Leboncoin/Kleinanzeigen/Subito-class). This pass defines the Type by the ad-contact model with transaction services as optional; the sibling leaf should be checked against this boundary at its own pass — if "Listing Marketplace" is meant as the transaction-first pole, the two leaves need an explicit division of labor; if it is a synonym, it is an Alias. Flagged for joint review.
4. **vs Directory Application / Listings Platform (§02.11).** Directories are persistent reference listings for lookup (businesses, points of interest); classifieds are transient trade offers with contact-to-transact intent. Remove the trade/contact intent and time-bound lifecycle → directory.
5. **vs Job Board (§09).** Jobs are historically a classifieds category (situations vacant); the dedicated Job Board adds candidate-side machinery (profiles/resumes, applications, employer tooling) — consistent with the association-job-board pass ("keep only the listings without candidate machinery → classifieds"). Leboncoin's Emploi section stays ad-shaped (employer posts offer; CVthèque as pro add-on).
6. **vs Property Listing Platform (§17).** Real estate is a classifieds category; dedicated property platforms add listing depth, agent tooling, and transaction support. The drift is visible inside the sample (Leboncoin's immo dossier/Pass Locataire+; Kleinanzeigen's agent FTP feed; OLX's Otodom/Imovirtual spin-offs) — vertical depth is the seam.
7. **vs Review Platform (§02.10).** Reviews are the object of a review platform; in classifieds, reviews (where present) are a trust layer over the ad-contact model, not the core.
8. **vs Service Marketplace / Babysitting Marketplace (§05.02/§29).** Consistent with the babysitting pass: classifieds have no persistent profiled supply — the ad IS the supply; service marketplaces center persistent provider profiles with booking/review machinery.
9. **vs Online Auction Platform (§05.18).** Auctions center price discovery (bidding) as the mechanism; classifieds center the ad with fixed/offer pricing. Bidding appears only as a pricing variant in some classifieds-adjacent products (not directly observed in this sample — reduced strength).

Removal tests ("去掉什么就变成另一个 Type"):
- Remove the contact-first model and make the mediated transaction mandatory → marketplace (resale/online).
- Remove transience + trade intent → directory.
- Remove the ad (keep persistent profiled supply + booking) → service marketplace.
- Keep only one category and add candidate-side machinery → job board; add agent/transaction depth → property platform.

## Uncertainties

- Craigslist, Gumtree, Marktplaats, OfferUp, OLX country sites, Avito, Locanto: unreachable (403/JS-app/timeout/429). The archetype pole (Craigslist-class) and the US mobile-first pole (OfferUp-class) are therefore NOT directly observed; claims about them are structural inference only.
- Sample skew: 3 of 4 product-level samples are Adevinta-family. Mitigated with Kijiji (eBay) and OLX Group (Prosus), but Latin American, Asian, and African product-level mechanics are unobserved.
- User reviews: directly observed at Kijiji only; their prevalence across the Type is uncertain — kept at reduced strength in the final document.
- Free-posting norms: the sample shows free base posting with paid categories/options (Leboncoin free quota + paid subcategories; Kleinanzeigen free posting + paid options; OLX "paying listers"; Kijiji paid boosts), but exact free/paid boundaries vary and were not exhaustively researched — stated at moderate strength.
- Ad durations: 60 days directly evidenced at Kleinanzeigen only; other products' durations not researched — no precise durations in the final document.
- Whether messaging is always the only sanctioned contact channel: Leboncoin/Kleinanzeigen restrict contact info in ads; older archetypes used anonymized email relays (unverified here) — stated as "common" not universal.
- Facebook Marketplace (social-graph distribution of classifieds): not attempted; mentioned only as market context at structural-inference strength, omitted from the final document's claims.

## Final Synthesis

A Classifieds Platform is a self-publishing advertisement board for local trade: the offering or seeking party authors a short, time-bound ad describing one specific offer or want; ads are filed in categories and tied to a locality; interested parties browse, search, and contact the poster through the platform; and the exchange itself is completed between the parties as the default — negotiation, payment, and handover happen person-to-person (meet-up and cash remain first-class outcomes), with platform-operated escrow/shipping/buyer-protection services offered as optional layers on eligible ads. The platform makes money not by intermediating the transaction but by renting attention and productivity: paid visibility (boosts/highlights), paid categories, professional subscriptions and tooling, and — increasingly — optional transaction-service fees. Trust and safety (moderation, reporting, scam education, safe-exchange guidance, account restrictions) is a first-class concern because the platform connects strangers for high-trust exchanges it does not control. The Type is distinguished from marketplaces by the contact-first model (no mandatory mediated transaction, no catalog/inventory), from directories by transience + trade intent, and from vertical platforms (job boards, property portals) by generality and the absence of candidate/agent-side machinery.
