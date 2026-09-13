# Virtual Phone Application

## Overview

A **Virtual Phone Application** lets a person or a small team hold and operate a **real telephone number as a software-managed line**: the number is acquired from the service's inventory or ported in, is dialable from any ordinary phone, and presents itself as caller ID — but it is not bound to a SIM card or a carrier subscription. Instead, the line lives in the application: calls (and, in every current product, text messages) are placed, answered, and managed inside the app over an internet connection, on devices the user already has.

The defining core is small:

```text
A real telephone number held by the service
└── operated as a line inside the app, over the internet
    └── persistent as a standing line, with its own accumulated history
        └── until it is released (deleted, expired, or ported out)
```

Everything else commonly associated with the category — texting, voicemail transcription, team sharing, extensions, call menus, compliance registration, AI answering — is widespread in current products but is not what makes the product a virtual phone line. The category's own ancestry makes the boundary visible: an older "virtual number" that merely forwards calls to your real phone holds a number but has no operating surface, so it is not this Type; an internet calling app that connects service users by account identity has an operating surface but no real telephone number, so it is not this Type either.

## Users & Context

Two broad audiences share one structure:

- **Individuals** who want an additional number alongside their personal one — for privacy (not giving out the real number to strangers, listings, or forms), for selling or dating, for travel, or to keep a category of contacts separate. For them the line is personal: multiple numbers may coexist in one account, each with its own history and settings.
- **Small businesses and small teams** who want a business line without buying hardware or signing a carrier contract — a number that presents a professional identity, separates business conversations from personal ones, and can be answered by more than one person. For them the line is a shared asset: team members share the number (or receive extensions under it), and inbound calls can be routed by schedule, menu, or group.

In both cases the usage context is the user's existing phone, tablet, or computer. The application explicitly does not replace the user's mobile carrier for their personal number; it adds a line on top. The work happens in moments that used to require a second handset or a second carrier plan: answering a business call from a personal phone, texting a customer from the company number, or letting a number lapse when a project ends.

## Core Model

### The defining core

**1. A real telephone number as the managed object.**
The center of the product is a telephone number that behaves like any ordinary phone number: anyone with a phone can dial it, and when the user calls or texts out, that number — not their personal number — is what the recipient sees. The number is chosen from the service's inventory (by area code, city, or number type such as local or toll-free) or brought in by porting from another provider. It is held by the service, not by a SIM card in the user's device. Without a real number, the product is an internet calling app with account identities; with nothing but a number and no operating surface, it is a forwarding service. The number is what makes this Type what it is.

**2. The app as the operating surface, over the internet.**
The line is operated inside the application: the user dials from the app, answers incoming calls in the app, and sends and receives messages in the app. The audio and messages travel over the internet (Wi-Fi or mobile data) rather than over the user's cellular voice plan — vendors across the sample describe this as making and receiving calls with "no landlines or cell service required." The line is independent of the device it lives on: uninstalling the app or switching devices does not affect the number, and the same line can be operated from a phone, a desktop app, or a browser. Without this surface, a held number is just a forwarding target; without the internet carriage, it is a second SIM.

**3. A standing line with its own record.**
The number persists as the user's addressable line between uses. It accumulates its own history — calls, messages, voicemails — organized per contact, and that record belongs to the number, not to a session. The line remains active under whatever terms the product defines (a subscription, a prepaid period, or an indefinite holding arrangement) until the user releases it: deleting it, letting it expire, or porting it out. Release ends the line; what happens to the history afterwards is product-defined (some products destroy the record with the number, others keep it viewable on a lapsed line while blocking new activity). Without persistence, the product would be a per-call relay rather than a phone line.

### What mature products add

These capabilities are standard across the researched sample. They make the line practical; they do not define the Type.

- **Texting on the number** — SMS and commonly MMS, so the number is a full communication identity, not a voice-only address.
- **Voicemail** — a greeting and mailbox per number; transcription of voicemails into text is common in business-oriented products.
- **A unified conversation view** — calls, texts, and voicemails with one contact gathered into one thread or inbox, with the line's history searchable.
- **A contacts layer** — the line's own contact book (separate from the device's personal address book in personal products; a shared team database in business products).
- **Control over who gets through** — blocking, muting, spam filtering, do-not-disturb, and auto-reply texts when a call is missed.
- **Multiple numbers** — more than one line in one account, each with its own identity, settings, and history; products commonly let users name and label their numbers.
- **Portability** — bringing an existing number in by porting is widely supported; moving a number out to another provider is documented in business-oriented products.
- **Multi-device operation** — the same line from mobile, desktop, and/or web.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:   a real telephone number
Realized as:   local, toll-free, or vanity numbers; chosen from inventory or ported in;
               country coverage varies sharply by product

Concept:   app-operated carriage
Realized as:   VoIP calling over Wi-Fi/data in mobile, desktop, and web apps;
               one product family also realizes the line on a second SIM card
               managed through the app

Concept:   the line's record
Realized as:   a per-number inbox and history; on release, the record is either
               destroyed with the number or retained on a lapsed line
```

A reader who has only seen one implementation — say, a business team sharing one number — should still be able to recognize a personal disposable-number app, and vice versa, from the core above.

## How It Works

### Get a number

```text
Sign up
→ choose a number from the service's inventory (search by area code, city, or type)
   or start a port of an existing number from another provider
→ the number becomes an active line in the account
→ optionally name it, set its greeting, and configure how it behaves
```

There is no hardware to buy and no carrier appointment; the line exists as soon as the service assigns the number. Porting an existing number instead of choosing a new one is the standard path for users who already have a number they depend on.

### Operate the line day to day

```text
Outbound:  dial or text from the app → the recipient sees the virtual number
Inbound:   someone calls or texts the number → the app rings / the message arrives
           → answer, reply, or let it go to voicemail / auto-reply
After:     the call, messages, and voicemail are recorded in the line's history,
           organized under the contact
```

The daily loop is ordinary telephony with one difference: everything is bound to the virtual number and its history rather than to the device's native dialer and message app. On a personal product the loop is single-user; on a business product any authorized teammate may perform it, and the team sees the same shared record.

### Keep or release the number

```text
Keep:      maintain the line's terms (subscription renewal, prepaid extension)
Release:   delete the number, let a prepaid term expire, or port it out
           → the line stops working; history handling is product-defined
```

This lifecycle is the category's distinctive maintenance work. A number is a held asset: business products attach it to a subscription (removing it may free a paid slot), while prepaid products give it a defined term that must be extended or the line goes inert. Porting out is the orderly exit that preserves the number itself.

### Share the line (business form)

```text
Add teammates to the account
→ share the number (or give members extensions under it)
→ configure how inbound calls are routed: ring the team, follow a schedule,
   offer a menu, or forward outward
→ members answer, reply, and leave internal notes on the shared record
```

Sharing is the business pole's defining extension of the core: one number, many operators, one shared history. Routing machinery (schedules, menus, ring groups, forwarding) exists to get an inbound call to the right person; it serves the line's owners rather than a managed agent workforce.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Number / line management

Where the lines themselves are administered.

- lists the account's numbers with their status and terms
- primary actions: add a number (search inventory or start a port), rename/label it, configure its greeting and behavior, delete it or let it lapse

### Dialer

The calling surface.

- keypad, recents, and access to the line's contacts
- primary actions: place a call from the virtual number, answer/ignore inbound calls, in-call controls (mute, hold, transfer in business products)

### Conversations / inbox

The line's communication record and the primary working surface.

- one thread per contact gathering calls, texts, and voicemails; unread and missed states; search across the history
- primary actions: send/reply with SMS or MMS, call back, play voicemail, block the contact, mark handled (in team products: assign, note, tag)

### Voicemail

- per-number greeting and mailbox; messages playable in the app, commonly also delivered onward (email or transcription in business products)

### Contacts

- the line's own addressable people, with per-contact history; import from the device or other sources; shared team contact databases in business products

### Routing / call configuration (business form)

- where inbound behavior is defined: business hours, call menus, ring groups, forwarding targets, greetings and announcements
- primary actions: build or edit the routing flow, set schedules, record greetings

### Team administration (business form)

- members and roles, shared-number assignment, analytics over the line's calls and messages

## Important Rules / Behaviors

- **The number is the identity.** Recipients see the virtual number — not the user's personal number — on outbound calls and texts; inbound callers reach the line, not the device. Personal products state this as the privacy guarantee; business products state it as the professional-presence guarantee. It is the same structural fact.
- **The line is independent of the device and the personal carrier plan.** It works over Wi-Fi or data, survives app reinstall and device changes, and has no effect on the user's real number. The virtual line and the personal line are separate estates that happen to share a handset.
- **A number is a held asset with terms.** Lines are maintained by subscription or prepaid terms; a lapsed term can end the line. What happens at release differs by product — deletion may destroy the number's history outright, while expiry may leave the history viewable but the line inert — so the safe general rule is: releasing the number ends the line, and the record's fate is product-defined.
- **Numbers can move.** Porting in is standard; porting out is the recognized way to leave with the number intact. A number's value (customer reachability, printed materials, directory listings) is exactly why portability exists.
- **Receiving third-party verification codes is not guaranteed.** At least the consumer pole of the sample documents that one-time codes and 2FA from other services generally do not work on its numbers. A virtual line is a communication line between people and businesses — not a reliable identity-verification endpoint.
- **Texting at business scale may be gated by carrier registration.** In markets that regulate business texting, products route number registration and compliance steps through the application; unregistered business texting risks filtering. This machinery is regional and segment-specific, not universal.
- **Routing serves the line's owners.** Menus, schedules, ring groups, and forwarding decide where an inbound call lands among the line's own users — they are not queue-and-agent machinery, and their depth varies from a simple auto-reply to a visual flow builder.

## Variants

- **Personal second number** — one user, one or a few numbers, kept for privacy, selling, dating, travel, or separating social circles; the number may be deleted or switched freely.
- **Temporary / prepaid numbers** — numbers bought for a defined term that expire unless extended; the extreme of the "line as held asset" behavior, oriented to short-lived needs.
- **Small-business line** — a professional number for a proprietor; voicemail transcription, greetings, business hours, and basic routing; usually a subscription.
- **Team-shared numbers** — one or more numbers operated by a team with roles, shared inboxes, internal notes, and routing machinery; the business pole's mature form.
- **Carrier-native second line** — a second line offered by the user's mobile carrier and operated through an app; the same core with the carrier as the service.
- **SIM-tied hybrid** — a second number realized on physical SIM hardware but managed through the application; documented as an alternative substrate by one sampled product, evidence that app-management, not the radio, is the Type's center.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Internet Calling Application | identity is a service account and calls connect service users; here the managed object is a real, publicly dialable telephone number, and the number is the identity |
| Softphone Application | a client of an organization's phone system — the number/extension belongs to the employer's telephony estate; here the line is provisioned directly by the service to an individual or small team, with no organizational phone system behind it |
| Conference Calling Application | centers a shared multi-party audio bridge with join addresses and host controls; here the line is a personal or small-team two-way line (conference capability may appear as an optional layer) |
| Push-to-Talk Application | centers hold-to-talk floor control over standing talk groups; here the structure is ordinary telephony-line semantics — numbers, calls, voicemail |
| Contact Center / Call Center Platform | distributes a queue of customer contacts across a managed agent workforce with routing, SLA, and workforce machinery; here routing serves the line's own owners, and the center is the line, not a queue operation |
| SMS Marketing Platform | organizes audiences and outbound campaigns; here the number is a standing two-way communication line with its own identity and history |
| Second-SIM products (device/carrier feature) | a second SIM is carrier hardware bound to the device; here the line is software-operated over the internet (a SIM-tied mode exists as a hybrid variant) |
| Telecom Number Management | carrier-side administration of number inventories; here the surface is the end user's operation of one line |

The most important boundary is with the **Internet Calling Application**, because both place calls over the internet from an app. The structural difference is the identity substrate: internet calling connects users of the service through service accounts (with dialing real phone numbers as an optional paid extra), while a virtual phone line's managed object is the real number itself — dialable by anyone, from any phone, as its primary property.

## Representative Products

- **Grasshopper** — the long-standing small-business "virtual phone system": business numbers with extensions, forwarding, and shared team answering
- **Quo (formerly OpenPhone)** — the modern shared-number business phone: team inboxes, call flows, and compliance machinery around one or more numbers
- **Burner** — the consumer second-number archetype: privacy-oriented numbers that can be created, switched, and deleted
- **Hushed** — consumer temporary and private numbers across many area codes, with a prepaid expiry lifecycle
- **Google Voice** — the largest consumer/prosumer virtual-number service; retained as a market anchor (see sourcing note below)

## Sources

Research date: **2026-09-09**

- Grasshopper — https://grasshopper.com/ , https://grasshopper.com/features/voip-phone-system
- Quo (formerly OpenPhone) — https://www.quo.com/ , https://support.quo.com/ , https://support.quo.com/core-concepts/phone-numbers/overview
- Burner — https://www.burnerapp.com/ , https://www.burnerapp.com/how-burner-works , https://support.burnerapp.com/
- Hushed — https://hushed.com/ , https://support.hushed.com/ , https://support.hushed.com/ (Numbers section, incl. the number-expiry article)

> Sourcing limitation: Google Voice (support.google.com/voice, voice.google.com) and TextNow (textnow.com) could not be fetched from the research environment (timeouts / access denied). Google Voice is listed as a market anchor only, with no operational claims made about it; TextNow's free-consumer-line economics are therefore not described. Precise vendor-specific figures (number caps, device limits, expiry spans, prices, group-size limits) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
