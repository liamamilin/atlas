# Research Notes — Private Market Investment Platform

## Research Goal

Understand what a "Private Market Investment Platform" actually is as an Application Type: what world it models, who uses it, how an investment actually happens inside it, and where its boundaries run against the neighboring private-markets leaves in the directory (Fund Administration Platform, Investor Portal, Deal Management for Private Equity / VC, Cap Table Management) and against public-market investing Types (Retail Trading Platform, Brokerage Platform).

## Initial Boundary

Working hypothesis before research:

- The leaf is the **investor-side access platform** for private-market assets: it lists private-market investment opportunities, qualifies investors, executes subscriptions, and services the resulting positions.
- The directory's sibling leaves already cover the **GP/company side**: Fund Administration (GP back office), Investor Portal (LP document slice of a fund relationship), Deal Management for PE/VC (GP pipeline), Cap Table Management (company equity records).
- Alternative reading to test: the leaf could mean **LP-side institutional investment management** for private markets (portfolio book + monitoring). This reading overlaps Portfolio Management System (already processed) and must be resolved in Boundary Findings.
- Public-market adjacency: Retail Trading Platform / Brokerage Platform differ by instrument liquidity and access gating — to be tested.

## Research Questions

1. What is the central object — offering, deal, vehicle, or portfolio?
2. How do investment opportunities enter the platform, and what state do they carry?
3. How are investors qualified (identity, accreditation, jurisdiction, limits)?
4. What is the subscription flow: interest → commitment → documents → funding → executed investment?
5. Where do capital flows live (one-shot funding vs capital calls; distributions)?
6. What ongoing servicing exists (valuations, statements, tax documents, notices)?
7. Is secondary liquidity part of the Type or a variant?
8. What roles exist (investor, advisor/relationship manager, GP/issuer, platform operator)?
9. What distinguishes this Type from fund administration, investor portals, cap table tools, and public-market brokerage?

## Representative Products

Selected for market representativeness, documentation quality, and spread of customer tier + product philosophy:

| Product | Tier / philosophy | Why selected |
|---|---|---|
| Moonfare | Professional/HNW direct; curated top-tier PE funds via feeder vehicles; EU/UK-centric | Fund-access pole; capital-call economics; secondary auction |
| EquityZen | Accredited investors; pre-IPO secondary marketplace; FINRA broker-dealer (Morgan Stanley subsidiary) | Secondary-marketplace pole; demand-sourcing model |
| Wefunder | Retail; open eligibility with limits; non-curated startup offerings (Reg CF / Reg D) | Retail pole; anti-curation philosophy; direct/SPV execution |

Boundary anchors (not primary samples, used to test edges):

- **Carta** — company-side equity + fund administration + LP analytics + CRM; its own support taxonomy demonstrates the GP-side slice structure.
- **AngelList** — GP-side investor management (data room, digital subscription paperwork, investor portal); demonstrates the opposite side of the same market.

Also commonly cited in this category but **not directly researched** (access blocked — see Sources): iCapital, Yieldstreet, Forge Global, Republic, Securitize, CAIS, Fundrise.

## Sources

Research date: **2026-09-06**. All evidence below is Tier-1 (official operational documentation) unless marked.

- Moonfare FAQ — https://www.moonfare.com/faq (fetched successfully)
- EquityZen Help Center — https://help.equityzen.com/ (fetched: types of deals, how to invest, how to sell)
- Wefunder Help Center — https://help.wefunder.com/ (llms.txt index + fetched articles: who can invest, investment timeline)
- Carta Support Center — https://support.carta.com/ (category taxonomy only)
- AngelList Investor Management Help Center — https://support.angellist.com/ (index + product structure)

**Source-access limitations (recorded per evidence rules):**

- iCapital (icapital.com) — HTTP 403 on two paths; abandoned.
- Yieldstreet (yieldstreet.com) — HTTP 403 on root and /faq; abandoned.
- Forge Global (forgeglobal.com, docs.forgeglobal.com) — HTTP 403 / transport error; abandoned.
- Republic (republic.com) — HTTP 403; abandoned.
- Securitize (securitize.io JS-only app; support.securitize.com transport errors ×2); abandoned.
- CAIS (caisgroup.com) — timeout; abandoned.
- Fundrise (support.fundrise.com) — transport error; abandoned.
- Carta help.carta.com transport error; support.carta.com reachable (taxonomy level only).

Consequence: the wealth-channel B2B2C tier (iCapital-style advisor-mediated distribution) is **not** evidenced by direct observation. No operational claims are made about any unreachable product anywhere in this research or the final document. Cross-product claims rest on the three researched products only.

## Product Observations

### Moonfare (evidence layer A — direct, official FAQ)

- **Who can invest**: eligibility defined by jurisdiction-specific regulatory categories — professional/semi-professional investors (Germany KAGB), professional investors (EU MiFID Annex II), certified HNW / self-certified sophisticated (UK COBS), qualified investors (Switzerland CISA), accredited/institutional (Singapore), wholesale clients (Australia), qualified investors (Israel). Criteria include minimum financial instrument portfolio and prior investment experience.
- **Investment structure**: "Moonfare investment vehicles pool interest in individual private equity funds. Capital calls, capital distributions and fees are all paid through the Moonfare investment vehicle." (feeder-vehicle model; third-party service partners named for admin/signing)
- **Product forms**: direct funds (individual funds), co-investments, secondaries, evergreens (semi-liquid), portfolio-of-funds.
- **Minimums**: portfolio funds from €50k, feeder funds from €100k, secondary fund from €25k (jurisdiction-dependent).
- **Capital calls**: schedule determined by underlying fund managers; typically 5–15% upfront, remainder drawn over the fund's investment period (~5–6 years).
- **Fund selection**: in-house due diligence ("FiveStar Diligence Method"), top-quartile focus; typical offered funds raising $1B+; typical fund maturity ~10 years.
- **NAV**: fund managers report NAV quarterly under valuation guidelines; investor-facing NAV includes feeder cash reserves and liabilities.
- **Secondary market**: buy/sell allocations before maturity; structured auction run semi-annually (spring/fall); NAV used as pricing reference; buyer assumes remaining unfunded commitment; seller-pays success fee (higher of 5% of total exposure or €5k minimum); identities disclosed to counterparty at execution, not during auction; transactions binding once agreements executed; minimum transaction size €100k; operated by Moonfare GmbH.
- **Advice posture**: no investment advice for regulatory reasons.
- **Tax/reporting**: quarterly investor reports, annual account statements, distribution notices, investor tax reporting (e.g., K-1/K-1-equivalent for US; country-specific deliverables with published delivery timelines).

### EquityZen (evidence layer A — direct, official help center)

- **Positioning**: pre-IPO private company shares; single-company and multi-company fund offerings; securities offered through EquityZen Securities LLC (SEC-registered broker-dealer, FINRA/SIPC member); subsidiary of Morgan Stanley.
- **Deal types**: single-company fund (investors become LPs in a vehicle that owns shares of one company; the fund "acts as a single entrant on each private company's capitalization table"); multi-company funds (investment-committee selected, ~5–7 year life); Direct Share Acquisition (direct ownership + cap table access, higher minimum, investor manages ongoing company interactions); Express Deals (resale of a fund interest previously bought through the platform); "Pending Acquisition" pre-commitment deals.
- **Investor flow**: verify accredited investor status (SEC definition) → browse companies → indicate interest with desired amount (watchlist-managed) → platform sources shares and confirms demand (Preview offerings gauge interest) → live offerings (launched Tuesdays and Thursdays 12pm ET) → reservation → complete investment paperwork → funds not required immediately → track in Portfolio.
- **Availability states**: Live, Waitlist, Preview.
- **Minimums/fees**: standard minimum $10k (select deals $5k); one-time sales fee through the broker-dealer, tiered (2.5% up to $1M, 2% above); typically no carried interest or recurring management fee on non-actively managed funds; fee structure uniform within a fund.
- **Closing mechanics**: after commitments complete, company holds Right of First Refusal (~30 days typical); transaction typically closes 8–11 weeks after the fund stops accepting commitments; investor must complete paperwork within one week of notification or allocation may be reallocated with a $500 termination fee.
- **Sell side (shareholders)**: free sign-up → electronic form (interest to sell, desired price, share count) → specialist outreach if market opportunity exists → buyers sourced from the accredited investor base → legal team works with issuer to close. Company criteria: later-stage tech, >$50M VC funding, Series C+.

### Wefunder (evidence layer A — direct, official help center)

- **Who can invest**: 18+; geography rules (Canada excluded; sanctioned countries excluded; EU residents welcome subject to local law); investment limits based on income, net worth, and prior Reg CF investments; accredited investors get access to more offerings; some issuers impose their own eligibility requirements.
- **Investment lifecycle** (portfolio page model): **Needs Action** (identity confirmation, tax ID, income/net worth, investment limits) → **In Progress** (fundraise launched → commitment received → payment received → fundraise closes → investment finalizes: subscription agreement fully executed, funds move to the company) → **Portfolio Investments** (confirmed; track value over time).
- **Curation posture**: explicitly non-curated — "It's not our role to choose what is worthy of investment. We screen companies for signs of fraud" only.
- **Execution structures**: SPV (investors aggregated into one entity on the company's cap table, e.g. a series LLC), Custodian, or Direct (company-managed); Lead Investor role represents investors on corporate actions.
- **Servicing**: portfolio value estimates (not market quotes), updates on corporate events (splits, IPOs), redemptions/buybacks/revenue-share payouts, K-1 tax documents for qualifying events, FMV letters for IRAs.
- **Money mechanics**: refunds/cancellations before disbursement; failed-round refunds; admin/service fees; minimum check sizes chosen by issuers (as low as $100).

### Carta (boundary anchor — evidence layer A, taxonomy level)

Support center categories: Login & user settings; **Company admins** (issuing equity, stakeholders, 409A); Employee resources (personal portfolio, exercise options); **Fund administration** (track, transact, manage your fund); Total Compensation; Legal; Carta Launch; LLCs; **LP Portfolio Analytics**; **Carta CRM** (deal flow, LP relationships, advisor networks).

Reading: the GP/company-side slices (equity issuance, fund administration, deal-flow CRM) are distinct product lines from investor-facing surfaces. Confirms the directory's sibling-leaf structure and supports the boundary between this leaf and Fund Administration / Cap Table / Deal Management.

### AngelList (boundary anchor — evidence layer A, product structure)

- **Investor Management Platform** (GP-side): "centralizes your prospecting, closing, and communication workflows"; Universal Directory of investor entities/people; bulk uploads.
- **Investor Portal** (GP-operated): "A Vehicle represents a fund or SPV entity within your Investor Portal… central hub for connecting relevant entities, documents, and key stakeholders"; document distribution to investors.
- **Digital Subscriptions** (GP-side): subscription paperwork as digital workflows — templates (PPMs, LPAs as reference documents), transactions with statuses, revisions, counter-signatures; investors fill and sign through it.
- **Data Room** (GP-side): fundraising material sharing with permission groups, NDA popups, watermarks, viewer analytics.

Reading: the GP-side stack (pipeline → data room → subscription paperwork → investor portal) is the mirror image of this leaf. The investor-side platform starts where the GP's distribution reach ends: it aggregates demand and lets investors discover and commit.

## Cross-product Comparison

| Dimension | Moonfare | EquityZen | Wefunder |
|---|---|---|---|
| Central listed object | Fund interests via feeder vehicles (funds, co-investments, secondaries, evergreens, portfolio funds) | Single-company / multi-company fund offerings; direct share acquisitions; express resales | Startup offerings (equity, SAFE, notes, revenue share) per company round |
| Who lists | Platform-curated (in-house diligence) | Platform-sourced (share sourcing + demand aggregation) | Issuers self-list (fraud screening only, no curation) |
| Eligibility gate | Jurisdiction-specific professional/HNW categories; minimum portfolio + experience | Accredited investor (SEC definition) verification | Age + geography + investment limits; accreditation for some offerings |
| Execution structure | Feeder vehicle pooling investor interest | Fund vehicle (SPV-like) or direct shares | SPV / custodian / direct |
| Funding model | Staged capital calls over investment period | One-shot (funds not required immediately; later close) | One-shot payment at commitment |
| Commitment lifecycle | Commitment → calls → funded position | Indicate interest → reservation → paperwork → close (weeks) | Needs action → in progress (launched→committed→paid→closed→finalized) → portfolio |
| Position record | Investor account with NAV, quarterly reports, statements | Portfolio page tracking investments | Portfolio with value estimates, statuses |
| Value basis | NAV reported quarterly by fund managers | Not market-quoted; deal-based | Estimated value, updated on events |
| Documents | Offering docs, subscription docs, quarterly reports, annual statements, tax reports (K-1 etc.) | Offering documents, term sheets, legal docs | Subscription agreements, K-1s, FMV letters |
| Liquidity | Semi-annual secondary auction (seller-pays fee; buyer assumes unfunded commitment) | Core business: sourcing buyers/sellers of pre-IPO shares; express resales | None (redemptions/buybacks only where issuer offers) |
| Advice posture | No investment advice | "Not investment advice" | Not investment advice |
| Regulatory posture | EU/UK/CH/SG/AU/IL investor categories | SEC/FINRA broker-dealer | SEC Reg CF/Reg D/Reg A+ exemptions |
| Intermediary layer | Relationship managers (human) | Private market specialists (sell side) | None (self-serve) |

**Stable across all three (cross-product commonality, layer B):**

1. A listed catalog of private-market investment opportunities, each with terms, documents, and an availability state.
2. A platform-enforced eligibility gate before an investor can invest (identity + financial/regulatory qualification).
3. A commitment-to-execution flow: interest → commitment → (subscription documents) → funding → finalized investment.
4. A persistent investor-side portfolio record of commitments and holdings with state.
5. A document layer (offering docs, subscription agreements, statements, tax documents).
6. Platform fees disclosed per offering.
7. No-investment-advice posture.
8. Value that is NOT continuously market-quoted (NAV, estimates, or deal-based).

**Present in some (variant, layer B→C):** pooling vehicles vs direct; capital calls vs one-shot; secondary liquidity; relationship managers; multi-jurisdiction eligibility matrices; issuer-side participation (EquityZen sell side; Wefunder issuers; Moonfare GP partners).

## Canonical Abstraction

### L0 — Defining Invariant

```text
Listed private-market investment opportunities
  (offering records: underlying asset, terms, documents, availability state)
+ Investor eligibility gate
  (platform-determined qualification controlling who may invest in what)
+ Commitment-to-execution flow
  (interest → commitment → funding → executed investment)
+ Persistent investor-side investment record
  (portfolio of commitments/holdings with state, value, documents)
```

Removal tests:

- Remove the listed opportunities → what remains is a portfolio tracker / fund admin / investor portal — not an investment platform.
- Remove the eligibility gate → what remains is a public brokerage / open marketplace — private-market investing is legally gated; every sampled product enforces a gate (the gate's strictness varies; its existence does not).
- Remove the commitment-to-execution flow → what remains is a listings/research surface (deal database), not an investment platform.
- Remove the persistent investment record → what remains is one-shot deal matching with no investment relationship — not recognizable as this Type.

### L1 — Common Mature Structure

- Pooling investment vehicles (feeder funds, SPVs, multi-company funds) as the standard execution structure, with the platform (or its partners) operating/administering them.
- Identity verification and investor onboarding (KYC-style prerequisites surfaced as blocking tasks).
- Eligibility tiers and investment limits (accreditation status, income/net-worth-based limits, jurisdiction categories).
- Portfolio value tracking (NAV or estimated value, updated periodically or on events).
- Document library: offering documents, subscription agreements, statements, tax documents.
- Fee machinery: platform/transaction fees, sometimes management fees/carry, disclosed per offering.
- Investor communications: updates, notices (capital calls, distributions, closings).
- Liquidity/secondary machinery (periodic auctions, resale matching, express resales) in a subset.
- Human intermediary layer (relationship managers, private market specialists) in a subset.

### L2 — Variant / Optional Structure

- Customer tier: retail (open eligibility + limits) / accredited / professional-HNW / wealth-channel (advisor-mediated).
- Asset focus: late-stage company shares, PE/VC fund interests, real assets, credit, art/collectibles.
- Liquidity model: none / periodic auction / deal-by-deal marketplace / evergreen semi-liquid.
- Regulatory regime: US (SEC exemptions, FINRA broker-dealer), EU (AIFMD/KAGB/MiFID), UK (FCA COBS), Switzerland, APAC.
- Curation posture: curated/diligence-gated vs open/fraud-screened.
- Execution structure: feeder / SPV / custodian / direct shares.
- Funding model: one-shot payment vs staged capital calls.
- Tax reporting machinery (K-1s, country-specific investor tax reporting).
- Issuer-side participation (shareholder sell-side intake; issuer listing requirements).

### L3 — Vendor-specific (kept out of final document)

- Moonfare: FiveStar Diligence Method; semi-annual auction mechanics (seller fee = higher of 5% of total exposure or €5k; €100k minimum transaction; spring/fall cadence); specific minimums (€25k/€50k/€100k); named service partners.
- EquityZen: Express Deals; "Pending Acquisition" security type; Live/Waitlist/Preview states; Tuesday/Thursday 12pm ET launch cadence; tiered sales fee (2.5%/2%); $500 termination fee; 8–11 week close; ~30-day ROFR; Morgan Stanley ownership.
- Wefunder: Lead Investor role; SPV/Custodian/Direct triad; XX Investments LLC; Wefunder Cash; Reg CF fee (7.9%); $100 minimum checks; VIP membership; llms.txt-first help center.
- AngelList: Digital Subscriptions templates/transactions; Data Room permission groups; Universal Directory; Vehicles.
- Carta: LP Portfolio Analytics; Carta CRM; 409A valuations.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The EquityZen launch cadence, the Moonfare auction fee formula, and the Wefunder fee percentage are all single-product facts.

## Rejected Findings

- **"Curated, diligence-vetted opportunities" as defining** — rejected: Wefunder explicitly does not curate. Curation is a posture (L2), not an invariant. The invariant is the *listed offering*, not its vetting depth.
- **"Feeder/SPV vehicle" as defining** — rejected: all three products also support direct execution (EquityZen DSA, Wefunder Direct, Moonfare co-investments are still vehicle-based but the pattern is not universal). Vehicles are L1.
- **"Capital calls" as defining** — rejected: only closed-end fund structures use calls; EquityZen and Wefunder are one-shot. L2.
- **"Secondary market" as defining** — rejected: Wefunder has none. L2.
- **"Accredited-investor-only" as defining** — rejected: Wefunder's Reg CF offerings are open to non-accredited investors within limits. The invariant is the *eligibility gate*, not accreditation specifically.
- **"Broker-dealer status" as defining** — rejected: regulatory posture varies by jurisdiction and product; Moonfare is not a US broker-dealer. L2.
- **"Advisor/wealth channel" as defining** — rejected: Wefunder is self-serve retail. L2.
- **"Continuous market pricing" as defining** — rejected: the opposite is true; non-market-quoted value is the cross-product stable.

## Boundary Findings

### vs Fund Administration Platform (sibling leaf)

Fund administration is the **GP-side back office**: fund accounting, NAV computation, capital-call processing, distribution processing, investor-reporting production. This leaf is the **investor-side access layer**: listing, qualification, subscription, position servicing. Evidence: Carta's own support taxonomy separates "Fund administration" from investor-facing product lines; Moonfare (a platform operator) *consumes* fund administration via third-party partners (Apex, Deloitte named) while Wefunder handles SPV taxes in-house — showing the platform sits above/alongside admin, sometimes absorbing it. Removal tests hold both ways: strip the offering catalog + subscription flow → fund admin remains; strip the fund accounting/NAV computation → the investment platform remains.

### vs Investor Portal (sibling leaf)

The investor portal is the **LP-facing document/statement slice of a GP-operated fund relationship** (AngelList: "A Vehicle represents a fund or SPV entity within your Investor Portal"; documents distributed by the GP). It has no discovery, no eligibility gating, no subscription execution. Conversely, this leaf's post-investment surface (documents, statements, value) converges toward portal functionality — the portal is a capability slice that this Type also tends to provide for the investments it originates. Probable capability relationship; flagged for the Investor Portal pass.

### vs Deal Management for Private Equity / VC (sibling leaf)

GP-side deal pipeline/CRM (Carta CRM: "deal flow, LP relationships"; AngelList Investor Management: "prospecting, closing"). Opposite side of the same market. No shared primary user or object.

### vs Cap Table Management (sibling leaf)

Company-side equity records. The relationship is complementary, not overlapping: platform vehicles appear **on** cap tables as single aggregated entries (EquityZen: fund "acts as a single entrant on each private company's capitalization table"; Wefunder: "All investors on Wefunder will be aggregated into SPVs"). Different user (company), different object (stakeholder equity).

### vs Retail Trading Platform / Brokerage Platform

Public-market platforms: continuous two-sided markets, any-instrument access without eligibility gating, market-quoted prices, instant settlement. This Type: discrete capacity-bound offerings, gated access, non-market-quoted values (NAV/estimates), long-dated illiquid positions, settlement measured in weeks. Even the secondary-marketplace variant (EquityZen) keeps the gate and the episodic, brokered character.

### vs Wealth Management Platform

Advisory-relationship-centric (client → advisor → portfolios across asset classes) vs offering-centric (investor → offering → position). A wealth platform may *distribute* private-market offerings through this Type's products (the wealth-channel variant), but the object models differ.

### vs Portfolio Management System (processed leaf)

The alternative reading of this leaf — LP-side institutional private-market investment management (portfolio book + monitoring) — is PMS-shaped and was already covered by the Portfolio Management System pass (book of record + management intent + forward loop). Market usage of the phrase "private market investment platform" (the reachable sample's self-descriptions: fund-access platform, pre-IPO marketplace, startup investing platform) is the investor-side access platform. **Naming hazard recorded for STATUS.**

### vs equity crowdfunding (no dedicated directory leaf)

Wefunder/Republic-style equity crowdfunding fits this Type as the retail variant: listed offerings + eligibility/limits + commitment flow + portfolio. The directory has no separate equity-crowdfunding leaf (the only crowdfunding leaves are nonprofit donation-shaped), so no conflict — recorded as an observation.

### "去掉什么就变成另一个 Type" 判据

- 去掉 listed offerings（只留持仓与文档）→ Investor Portal / fund admin
- 去掉 eligibility gate → 公开市场 Brokerage
- 去掉 commitment-to-execution → 研究型数据库（deal database）
- 去掉 persistent investment record → 一次性撮合（classifieds 式）
- 去掉 private-market 资产本身 → 普通 Brokerage / Trading Platform

## Uncertainties

1. **Wealth-channel tier unverified**: iCapital/CAIS unreachable; the advisor-mediated distribution variant is described only structurally (from the concept), never from direct observation. No operational claims made about it.
2. **Directory intent**: whether the taxonomy author intended this leaf to also absorb LP-side institutional suites — resolved as "no" based on market usage, but flagged for human review.
3. **Institutional LP usage**: some platforms serve institutional LPs too (not directly observed in the reachable sample); the Type definition does not depend on investor tier.
4. **Evergreen/semi-liquid structures**: observed at Moonfare (one product); treated as a liquidity-model variant, not generalized.
5. **Tokenized private markets** (Securitize): unreachable; assumed to fit the same core model but unverified — not claimed.

## Final Synthesis

A Private Market Investment Platform is the investor-side access layer for private-market assets. Its defining core is small: **listed private-market investment opportunities + a platform-enforced investor eligibility gate + a commitment-to-execution flow + a persistent investor-side investment record**. Everything else commonly associated with the category — pooling vehicles, capital calls, secondary auctions, relationship managers, tax-document machinery, curation — is standard mature structure or variant, not definition. The Type is cleanly separated from its GP-side siblings (fund administration, investor portal, deal management, cap table) by the side of the market it serves, and from public-market brokerage by the gate, the discrete offerings, and the non-market-quoted value model.
