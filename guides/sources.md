# Official sources and limits

Reviewed 2026-10-24. These sources support the specific claims below; this is not a blanket certification of every menu, eligibility rule or country's protections. Recheck the official source at the time of action and check for superseding rules. No personal account was inspected. Cadences and response formats are product design choices, not official universal requirements.

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
| [FTC freezes/alerts](https://consumer.ftc.gov/articles/credit-freezes-and-fraud-alerts) | Free place/lift; no credit-score effect; freeze each bureau. New-credit protection has a different scope from existing-account security. |
| [TransUnion mail/phone freeze](https://www.transunion.com/credit-freeze/mail-or-phone) | Alternate request channels exist. This does not establish that every foreign document/address combination will pass verification. Check each bureau directly. |
| [IRS IP PIN](https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin) | Identity-verified SSN/ITIN holders can enroll. Calendar-year validity and one-time versus continuing choices matter. Alternative-method requirements need current review; fixed income thresholds are deliberately omitted here. |
| [AAIP Resolución 180/2025](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-180-2025-418054/texto) | Published 2025-09-30; repeals Disposición 24/2010 and Resolución 228/2023 for the lost-ID register/DOCUEST. Supersedes older enrollment pages. Do not infer replacement legal duties. |
| [RENAPER replacement DNI](https://www.argentina.gob.ar/servicio/tramitar-un-nuevo-ejemplar-de-dni) | Official replacement route; requirements differ by age and location. No agent handling of documents. |
| [BCRA record correction](https://www.bcra.gob.ar/corregir-datos-desactualizados-en-la-central-de-deudores/) | Records may lag or contain errors. Check the reporting period and complain first to the reporting institution. An unfamiliar debt is not proof of fraud. |
| [BCRA fraud complaint](https://www.bcra.gob.ar/realizar-un-reclamo-ante-el-banco-central-por-fraude-o-estafa/) | Immediate institution contact, then formal complaint; BCRA escalation requires at least ten business days and other eligibility/documentation. Do not delay urgent containment. |
| [AAIP data rights](https://www.argentina.gob.ar/aaip/datospersonales/derechos) | Free access every six months and ten calendar days for response. Verify current complaint requirements; user handles documents privately. |
| [ENACOM *910](https://www.enacom.gob.ar/denuncia-al-910_p4034) | Official stolen/lost-phone line/equipment blocking route. Network blocking is not erasure or a substitute for securing accounts. |
| [UFECI](https://www.mpf.gob.ar/ufeci/) | Agency's own contact page lists denunciasufeci@mpf.gov.ar. Verify there before sending a report; a domain suffix alone cannot establish authority. |
| [ARCA Clave Fiscal](https://www.afip.gob.ar/clavefiscal/) and [Mi Argentina FAQ](https://www.argentina.gob.ar/miargentina/preguntasfrecuentes) | Official starting points checked; exact current token activation and session/MFA menu behavior were not tested. No unsupported assertion about missing authenticator support. |
| [HIBP FAQ](https://haveibeenpwned.com/Faqs) | A lookup concerns recorded breaches, not comprehensive assurance. It submits an identifier to an independent service; get consent or use existing provider warnings privately. No identifiers were submitted during this review. |

| [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10) | Monthly recurrence syntax and start/timezone semantics; actual scheduler support, notification delivery and DST behavior require provider readback/tests. |
| [Apple Time Machine restore](https://support.apple.com/guide/mac-help/restore-items-backed-up-with-time-machine-mh11422/mac) | File restoration is a separate operation from backup configuration. Use the person's backup provider instructions for a harmless restore test; this review performed no restore. |

## Verify at use time

Carrier lock names, bank/token menus, foreign-address identity checks, SSA enrollment, device support, router settings and other-country protections vary. Links to official starting pages are not proof of individual eligibility or a successfully enabled setting. Exact provider steps need a fresh source and user-side confirmation. Broad negative claims such as “Argentina has no freeze” are intentionally not asserted without comprehensive current evidence.

Some official pages may block automated retrieval (CISA's general guide returned 403 during this review). Do not treat blocked retrieval as a verified claim or as proof a service is down. Use the sources successfully read above and mark unresolved gaps.
