# Official sources and limits

Existing technical-source review: 2026-10-24. This revision changes routing and routine design; it does not establish fresh country eligibility. These sources support the specific claims below; this is not a blanket certification of every menu, eligibility rule or country's protections. Recheck the official source at the time of action and check for superseding rules. No personal account was inspected. Cadences and response formats are product design choices, not official universal requirements.

| Source | Supported scope / limit |
| --- | --- |
| [Google compromised account](https://support.google.com/accounts/answer/6294825) | Recovery, activity/devices, recovery details, connected access, forwarding and filters. Follow the user's provider's process rather than applying Google menus to other services. |
| [Google passkeys](https://support.google.com/accounts/answer/13548313?hl=en) | Adding a passkey leaves existing authentication/recovery factors in place. It does not eliminate phone-number dependencies. Google warns against creating a passkey on a shared device: someone able to unlock it can access the account, even after sign-out. |
| [FTC two-factor guidance](https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts) | Two-factor login adds protection; available methods differ. Retain SMS when it is the only supported option. |
| [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) | Section 3.1.1.2 rejects arbitrary periodic password changes and calls for changes on evidence of compromise. This is a verifier standard, not a personal monthly-audit mandate. |
| [Apple lost device](https://support.apple.com/en-us/101593) and [Google lost Android](https://support.google.com/accounts/answer/6160491) | Remote finding, securing and erasing are distinct and depend on setup/device state. Follow current official recovery instructions before erasure. |
| [Apple SIM PIN](https://support.apple.com/en-us/118228) | Locks SIM/eSIM use on restart/removal. Never guess PIN/PUK. This is distinct from carrier-side number-transfer protection. |
| [Apple recovery key](https://support.apple.com/en-us/109345) | Optional key disables standard account recovery. Apple says not to store it in Apple Passwords, iCloud Photos, Notes or Drive; lost account access can block those stores. Not a default recommendation for everyone. |
| [FTC scam response](https://consumer.ftc.gov/articles/what-do-if-you-were-scammed) | Contact the payment provider promptly and ask about recovery; results vary. Reporting does not guarantee a refund. |
| [HIBP FAQ](https://haveibeenpwned.com/Faqs) | A lookup concerns recorded breaches, not comprehensive assurance. It submits an identifier to an independent service; get consent or use existing provider warnings privately. No identifiers were submitted during this review. |
| [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10) | Monthly recurrence syntax and start/timezone semantics; actual scheduler support, notification delivery and DST behavior require provider readback/tests. |
| [Apple Time Machine restore](https://support.apple.com/guide/mac-help/restore-items-backed-up-with-time-machine-mh11422/mac) | File restoration is a separate operation from backup configuration. Use the person's backup provider instructions for a harmless restore test; this review performed no restore. |

## Source-method lesson: official pages can outlive a service

The earlier country review found a reachable official enrollment page whose underlying rules had been repealed; [AAIP Resolución 180/2025](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-180-2025-418054/texto) is the primary-source example checked on 2026-10-24. That failure mode is retained here; the retired procedure, contact details and eligibility rules are no longer a maintained playbook. At use time, inspect the responsible authority's current service and governing updates before recommending enrollment. A repeal alone does not establish a replacement service or new duty.

## Verify at use time

Use [jurisdiction discovery](jurisdictions.md) for every local route. Carrier lock names, bank/token menus, foreign-address identity checks, device support and government protections vary. Official starting pages do not prove individual eligibility or successful configuration. Exact steps need a fresh source and user-side confirmation. Avoid broad negative claims about a country's protections without comprehensive current evidence.

Some official pages may block automated retrieval. This leaves a verification gap; it does not prove a service is unavailable. State the gap and use a verified official support route where available. Cadences here are design choices. Scheduler support, authorized access, execution and delivery each need their own evidence.
