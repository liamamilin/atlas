# Mobile Wallet

## Overview

A **Mobile Wallet** is the consumer's payment wallet carried on a personal mobile device. It holds the user's payment resources — card credentials, wallet value, or both — the wallet's home is the user's carried phone (or a wearable paired to it), and the payment act is executed on the device itself, verified by the device, with the device's identity — not the raw card number — presented to the payment.

The defining structure is small:

```text
Wallet (holder-side payment container)
└── Lives on the carried personal device (phone / wearable / phone line)
    └── Payment executed on the device at the point of exchange
        └── Verified by the device (PIN / biometric / device unlock)
            └── Transaction exposes the device identity, not the raw instrument
```

Everything commonly associated with modern mobile wallets — NFC tap, tokenization internals, express-checkout buttons, passes and digital IDs, watch companions, P2P money, QR codes — is widespread in current products but is not what makes the product a mobile wallet. Mid-2000s phone wallets that only tapped contactless terminals, and mobile-money wallets that run on basic phones over USSD menus, satisfy the same structure without any of those specifics.

When the wallet is instead an account container reachable from any surface (a web checkout account), the product belongs to the Digital Wallet territory; when its defining structure is a user-held prepaid balance, it belongs to the Stored Value Wallet territory. Products frequently carry several of these structures at once; the boundaries are structural, not per-product.

## Users & Context

The primary user is an individual consumer who pays for things in daily life — at checkout counters, transit gates, vending machines, in mobile apps, and on the web — and wants their payment capability available at the moment of exchange without carrying the corresponding physical instruments.

Typical moments of use:

- pay at a physical point of sale by presenting the phone or watch to a terminal
- pay inside an app or on a website with a one-tap wallet button
- check what the wallet holds, review recent transactions, or check a balance
- add a new card (or load value, where the wallet carries value)
- replace a lost device, or move the wallet's contents to a new one

A second actor always stands behind the wallet: the wallet operator — a device platform, a device maker, a fintech, or a mobile operator — which hosts the wallet and its security model. The acceptance side (terminals, QR stickers, checkout integrations) belongs to merchants and to other Application Types; the mobile wallet is the payer-side surface. The use context is inherently mobile: the wallet is carried on the body, which is precisely why it is available at the moment of payment.

## Core Model

### The Defining Core

Three properties together. Remove any one and the product is no longer recognizable as a mobile wallet:

- **The wallet as the holder's payment container** — it holds what pays: payment-instrument credentials (payment cards), wallet value (a balance inside the wallet), or both. Resources enter through provisioning (adding a card) or loading (adding value). Without held resources there is no wallet — just a device.
- **The carried device as the wallet's home** — the wallet lives on the user's personal mobile device: the phone itself, a wearable paired to it, or (in mobile-money variants) the phone line. The user carries it in daily life, so it is present at the moment of payment. A wallet that lives behind an account login on whatever computer is at hand is a different structure.
- **The device as the point of payment execution** — the payment act happens on the device: presenting it to a contactless terminal, displaying or scanning a code, choosing the payment in an app, or dialing the payment menu; and the act is verified by the device (device PIN, fingerprint, face, or device unlock). The transaction carries the device's payment identity — a device-specific number and transaction code — rather than the raw instrument number. A wallet that merely funds a payment executed elsewhere is a saved payment method, not this Type.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ on every axis:

```text
Concept:   Wallet's home
Implementations:  phone app embedded in the device platform (OS-native wallets),
                  device-maker wallet app, standalone finance app,
                  phone line identity (USSD / SIM-toolkit wallets), paired wearable

Concept:   What the wallet holds
Implementations:  tokenized card credentials, wallet balance, both,
                  plus companion credentials (passes, tickets, IDs, keys)

Concept:   Where the credential physically lives
Implementations:  on-device secure storage (the dominant OS/OEM implementation),
                  account store presented by the app,
                  operator-side account bound to the phone line

Concept:   Payment presentation
Implementations:  contactless tap, displayed or scanned QR code,
                  merchant payment codes / paybill numbers,
                  in-app and on-web express checkout, USSD payment menu

Concept:   User verification
Implementations:  device biometrics, device PIN/passcode, passkeys, wallet PIN
```

A reader who has only seen one implementation — say, the tap-to-pay OS wallet on a smartphone — should still be able to recognize a USSD-based mobile-money wallet or a mid-2000s tap-only phone wallet from the Core Model.

### Standard Capabilities of Mature Products

These are common across mature mobile wallets and expected by users, but they are not what makes the product a mobile wallet:

- **Card provisioning with issuer verification** — capture the card (camera, or tapping the card against the phone), then verify with the bank or card issuer before the credential becomes usable.
- **Device-specific credentialing** — for network cards, the wallet pays with a device-specific number and unique transaction code; merchants do not receive the raw card number. This is the dominant implementation in platform and OEM wallets.
- **Per-device lifecycle** — cards and credentials are managed per device: added to one or several of the user's devices, removed when a device is lost, and transferred to a replacement device.
- **Transaction history and balance views** — the wallet shows recent payments and, where applicable, card or wallet balances.
- **Express checkout on the web** — wallet buttons in apps and browsers that complete a purchase with one device-verified confirmation.
- **P2P money on the same wallet** — sending and requesting money between people, sometimes with device-to-device transfer gestures.
- **The passes container** — boarding passes, event tickets, loyalty and membership cards, digital IDs, and keys riding in the same app beside the payment cards.

## How It Works

### Provision the wallet

```text
Open the wallet on the device
→ add a payment card (capture it or enter details)
→ verify with the bank / card issuer
→ credential becomes active on that device
→ optionally repeat for other devices, or load value where the wallet carries it
```

Provisioning is gated: the issuer or operator confirms the user's claim to the instrument before the wallet may spend from it. From this point the wallet holds what pays.

### Pay at a physical point of sale

```text
Approach the terminal
→ wake the wallet (gesture or app)
→ the default card (or chosen card) is ready
→ verify on the device (fingerprint / face / PIN)
→ present the device (tap the terminal, or show / scan the code)
→ the transaction carries the device's payment identity
→ confirmation appears on the device
```

The verification and the presentation are both device acts. This is the signature loop of the Type: the instrument never leaves the wallet, and what the merchant's terminal receives is the device's tokenized payment identity, not the card.

### Pay in an app or on the web

```text
Checkout shows the wallet button
→ user selects it
→ the device verifies the user
→ the wallet supplies its payment identity to the checkout
→ done — no card entry, no forms
```

On surfaces where the wallet button is unavailable, some wallets hand off to the phone: a code shown at checkout is scanned with the phone, and the phone completes the purchase — the payment act returns to the device.

### Manage the wallet

```text
View cards / value / passes
→ set the default payment card
→ review transactions (and balances, where applicable)
→ add or remove cards per device
→ on a new device: transfer contents; on a lost device: suspend remotely
```

### Send money (where the wallet supports it)

Many mature wallets embed person-to-person money movement on the same container: pick a recipient (from contacts, a message thread, or another person's device nearby), verify, send — the funds arrive in the recipient's wallet, card, or account depending on the product.

## Interfaces

The surfaces below are described conceptually; exact layouts, gestures, and names vary by product.

### Wallet home

The user's primary surface — a stack or carousel of what the wallet holds: payment cards (one marked default), wallet value where present, and passes beneath. Primary actions: pay (gesture or button), open a card's details, add a card or pass.

### Payment presentation surface

The moment-of-payment state: the wallet wakes, the card is ready, verification is requested, and the device is presented to the terminal or shows its code. Designed to be fast, single-handed, and usable at a counter or gate.

### In-app / on-web payment sheet

The express-checkout surface: shipping and payment summarized from the wallet, confirmed with one device verification. Purpose: replace card entry and checkout forms with a device-verified one-tap act.

### Card / value detail

Per-resource detail: card art, device-specific number reference, transaction history, balance connection where the issuer supports it, billing address, and removal from this device. For wallet value: balance, load history, and spending history.

### Add-card / provisioning flow

Capture card details, communicate with the issuer, possibly a further verification step, then activation. The gate through which every instrument enters the wallet.

### Device / security settings

Default card, verification method, per-device management (which devices hold the wallet), remote suspension, and — in mobile-money variants — wallet PIN management and registration status.

### Passes area

Where present: tickets, boarding passes, loyalty cards, IDs, and keys, each displayed for presentation at its own point of use. A companion surface sharing the wallet's container and security.

## Important Rules / Behaviors

- **The device is the credential holder.** Whatever else is true, the wallet's resources are bound to the user's device or line — not to a card they carry or a login they type elsewhere. Losing the device means suspending or wiping the wallet on it, not canceling the underlying instruments.
- **What the merchant receives is the device's identity.** Mature platform and OEM wallets pay with a device-specific number and unique transaction code; the raw card number is not shared with the merchant. This is why wallet receipts in downstream systems typically reference wallet device numbers rather than card numbers.
- **Every payment is verified on the device.** The wallet does not pay without a device-bound verification act (biometric, PIN, passkey, or device unlock). The verification is the cardholder-verification layer of the payment.
- **Provisioning is issuer-gated.** A card only becomes usable in the wallet after the issuing bank verifies the user. The wallet cannot self-issue spending capability.
- **The wallet pays from what it holds, at points that accept its substrate.** A contactless wallet needs a contactless terminal; a QR wallet needs a scannable code; a paybill-rail wallet needs the merchant's payment code; an express-checkout wallet needs the wallet button at checkout. Where the substrate is absent, the wallet cannot pay there — acceptance is conditional.
- **Value inside the wallet is a distinct structure.** Where a wallet carries a balance (rather than instrument credentials), that balance behaves as a stored-value account inside the wallet container — funded by loading, drawn down by spending. The same product can carry both structures.
- **Wallet contents are per-device, the account is per-user.** The same wallet can exist on several of the user's devices with independent credentials; contents are added, transferred, and removed per device, while the user's underlying instruments and (where present) account persist.

## Variants

- **OS-native device wallet** — embedded in the device platform, holding tokenized payment cards alongside passes; the platform operator is not a bank and does not issue the instruments (e.g., Apple Pay, Google Wallet).
- **OEM wallet** — the device maker's wallet app with on-device encrypted credential storage, often extending further into IDs, keys, and passwords (e.g., Samsung Wallet).
- **Fintech account wallet** — an account-based container (linked cards and banks, optional balance) whose mobile app is the wallet surface; the credential store is the account, and the device is the verification and execution surface (e.g., PayPal).
- **Mobile money / line-identity wallet** — the wallet bound to the phone line, operated by a mobile operator, usable without a smartphone over USSD or SIM-toolkit menus; balance-centric, with agent and merchant-code rails (e.g., M-PESA).
- **Credential-container vs value-carrying** — wallets that only hold instrument credentials vs wallets that also carry spendable balance inside the container.
- **Wearable-companion shape** — cards provisioned to a watch or band alongside (or instead of) the phone.
- **Bank-provisioned shape** — bank apps that add their cards into the device wallet rather than executing payments themselves; the device wallet remains the credential holder at payment time.
- **Super-app embedding** — the mobile wallet as the payment core of a wider consumer app (shopping, investing, credit riding alongside).

A variant remains a variant while the Core Model still applies. Where the balance inside the wallet becomes the whole point of the product — a prepaid account loaded and drawn down, irrespective of device — the product's structure is that of a Stored Value Wallet; where the container is a general account reachable from any surface, it is a Digital Wallet structure.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Digital Wallet | the holder-side container reachable from any surface (web checkout accounts, cloud wallets); the payment act happens wherever the checkout happens, not necessarily on a carried device. Remove the carried-device home/execution from a mobile wallet → Digital Wallet. Products often carry both structures. |
| Stored Value Wallet | the user's own prepaid balance in an operator-maintained account as the defining structure; device-agnostic. A mobile wallet with a balance ships both structures; the seam is where the payment draws from vs where it is executed. |
| Mobile POS | the seller-side mirror: a carried device executing acceptance, not payment. The two meet at the same contactless/QR rails; one device can even host both shapes. |
| Peer-to-peer Payment Application | transfer between identified individuals as the core; in the current market almost always embedded inside wallet products as a capability, not the boundary. |
| Mobile Banking Application | manages a deposit relationship and banking products; a mobile wallet holds and spends payment resources at the point of exchange. Bank apps commonly provision cards into device wallets rather than being the wallet. |
| Card Issuing Platform / Card Management System | issuer-side creation and governance of the very credentials a mobile wallet stores; their wallet-provisioning capability is the mobile wallet's intake flow. |
| Payment Gateway / Payment Processing Platform | payee-side acceptance infrastructure; mobile wallets appear inside them as payment method types. |
| Crypto Wallet | same word, different asset class and custody: user-held blockchain keys vs device-hosted payment credentials/value. |
| Event Ticketing Platform | issues tickets as system records; the mobile wallet is one carrying surface for the resulting pass. Remove pass storage from a mobile wallet and it is still a payment wallet. |
| Campus Card Management / Cashless Venue Platform | institution- or venue-scoped closed loops with privileges and operator funding; the general-purpose carried wallet is the consumer-owned remainder outside such scopes. |

The most important boundary is the one with Digital Wallet: the two Types overlap in content (a holder-side container of payment resources) and differ in where the wallet lives and where the payment act happens. The wallet trio in this domain — Digital Wallet, Mobile Wallet, Stored Value Wallet — is best read as three structural seams (what holds the credential / where the wallet lives and pays / where the payment draws from) rather than three mutually exclusive product boxes; real products routinely combine them.

## Representative Products

- Apple Pay / Apple Wallet
- Google Wallet / Google Pay
- Samsung Wallet
- PayPal (mobile app)
- M-PESA (Safaricom)

These span the main shapes: platform-native device wallets, an OEM wallet, an account-container fintech wallet, and line-identity mobile money. The Core Model was checked against pre-smartphone shapes (mobile-FeliCa-era phone wallets; USSD/SIM-toolkit mobile money) to avoid over-fitting the definition to the current smartphone tap-to-pay pattern.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Apple — Apple Pay overview: https://www.apple.com/apple-pay/
- Samsung — Samsung Wallet: https://www.samsung.com/us/apps/samsung-wallet/
- PayPal — Digital Wallet / app overview: https://www.paypal.com/us/digital-wallet
- Safaricom — M-PESA services hub: https://www.safaricom.co.ke/personal/m-pesa

> Sourcing limitation: official pages for Google Wallet / Google Pay could not be fetched from the research environment on 2026-09-08 (repeated timeouts); that product is retained as a market anchor only and no operational detail is sourced from it. Operational specifics (numeric limits, fees, security-architecture internals, market availability) observed in vendor copy are intentionally not asserted in this document; they remain in the Research Notes. The Research Notes also record cross-references to adjacent Atlas passes (issuer-side provisioning, wallet device numbers on receipts, mobile acceptance mirrors) that corroborate the device-identity and provisioning structures described here.
