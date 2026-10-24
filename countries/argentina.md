# Argentina module

Load this if the user lives in Argentina or has an Argentine DNI, CUIL/CUIT, or Argentine bank and payment accounts. Facts here were checked on official sites in October 2026. If a screen looks different, trust the official site and adjust. Spanish menu names are in quotes.

The user types their DNI number, número de trámite, Clave Fiscal, PINs, and passwords directly into the official site or app. Never in chat.

## Credit freeze: it doesn't exist here
Argentina has no credit freeze. Nobody can lock their file at the bureaus the way US residents can. The closest real protections are:

1. **Check your record at the BCRA Central de Deudores** (central bank debtor registry). Free, online, by CUIT/CUIL/CDI. Shows every loan or card reported in your name by banks, card issuers, fintech lenders, and other regulated providers, plus rejected checks, with 24 months of history. A loan you don't recognize = identity theft. https://www.bcra.gob.ar/situacion-crediticia/
2. **Ask for your free Veraz (Equifax) report.** Under the personal data law (Ley 25.326) you can get your report free once every six months ("Derecho de Acceso"). The bureau has 10 calendar days to answer; if it doesn't, you can complain to the data-protection authority (AAIP). Request it on Veraz's own site: https://www.veraz.com.ar/ECOMMERCE/individuos.ecom. Other private bureaus such as Nosis are covered by the same law; request access on their own sites. Your rights: https://www.argentina.gob.ar/aaip/datospersonales/derechos
3. **If your DNI is lost or stolen, flag it in the Registro de Documentos de Identidad Cuestionados.** Banks and financial companies are required to check this register before giving out loans or cards. Free, online, needs the police/fiscalía report and proof of identity. https://www.argentina.gob.ar/servicio/inscribir-un-documento-perdido-o-robado-en-el-registro-de-documentos-de-identidad
   Then get a new DNI copy ("nuevo ejemplar") at a RENAPER Documentation Center (turno in Mi Argentina) or the Registro Civil. Once the new copy is issued, only it is valid. https://www.argentina.gob.ar/servicio/tramitar-un-nuevo-ejemplar-de-dni

## ARCA (ex-AFIP) Clave Fiscal
The Clave Fiscal is the login for the tax agency, and with it someone can file, register for taxes, invoice, and appoint other people to act in your name. Treat it like a bank password.
- **Security levels.** Level 2 comes from home banking ("Servicios ARCA"). Level 3 comes from the ARCA Móvil app (needs an Argentine DNI card and a selfie/gesture check, menu "Solicitud y/o recupero de clave fiscal") or in person. Level 4 = turning on the Token ARCA app. https://www.argentina.gob.ar/servicio/obtener-la-clave-fiscal
- **Turn on Token ARCA (second factor, level 4).** Install "Token ARCA" (Android/iOS), choose "Activar en cajero automático", then at an ATM with your debit card go to "Gestionar Claves" > "Gestionar Clave ARCA" and type the code into the app within 48 hours. Or book a turno for "Soft token - Activación de claves". It needs level 3 first. The app makes an 8-digit code at each login. https://www.afip.gob.ar/clavefiscal/ayuda/token.asp
- **Change it to a unique, long password** (icon at top right > "Cambiar clave"). ARCA says not to reuse it for email or home banking. https://www.arca.gob.ar/guias/paso-a-paso/Guia-cambio-CF.pdf
- **Check who can act for you.** In the "Administrador de Relaciones" service, review the people and services you've delegated, and remove anyone you don't recognize or no longer use (for example an old accountant). https://www.afip.gob.ar/clavefiscal/ayuda/administrador-de-relaciones.asp
- Living abroad? ARCA allows an "administrador de relaciones apoderado" for people resident abroad who can't go to an office. Only set this up with someone fully trusted.

## Mi Argentina (national digital ID app)
Holds the digital DNI, driver's license, car documents, and your turnos.
- Validate your identity (biometric check in the app, or at a Punto Digital). Use a unique password (min. 8 characters, upper/lower case, number, symbol).
- **Verify your phone number** in your profile ("Validar teléfono"). It adds a recovery path. Mi Argentina doesn't offer an authenticator-app second factor, so the password and your email account's security are what protect it.
- **Review active sessions:** on the web version, "Mi cuenta" > "Seguridad" shows active sessions and lets you close them. Do it after losing a phone.
- Never share the account. It's personal by design.
https://www.argentina.gob.ar/miargentina/preguntasfrecuentes

## Phone line and carrier (Personal, Claro, Movistar)
- Every line must be registered to the holder's DNI (DNI number, sex as on the DNI, and the 11-digit número de trámite), validated against RENAPER. Since March 17, 2025 carriers must check this to open a line, and for sensitive changes like a SIM swap they can require RENAPER biometric validation or multi-factor checks. https://www.enacom.gob.ar/institucional/nuevos-requisitos-para-dar-de-alta-una-linea-de-telefonia-movil_n4759
- **Porting a number** to another carrier is done with your DNI at the new carrier, which texts a PIN to the line to confirm. If you ever get a portability PIN you didn't ask for, someone is trying to steal your number: don't share it, and call your carrier right away. https://www.enacom.gob.ar/portabilidad/
- Ask your carrier which lines are registered in your name. ENACOM says you can request this; there's no single government lookup. https://enacom.gob.ar/nominatividad-y-validacion-de-identidad_p6422
- Ask your carrier (app, store, or customer service) whether it offers an account PIN or extra SIM-change checks and turn them on. Each carrier's options differ and weren't verified here.
- Set a SIM PIN on the phone itself.

## Stolen or lost phone
- **Call \*910** (free, 24 hours, from any phone). It blocks the phone and the line, and the IMEI goes on a blacklist so it can't be used on Argentine networks. https://enacom.gob.ar/denuncia-al-910_p4034
- Lock or wipe it remotely (icloud.com/find or google.com/android/find), close Mi Argentina sessions, change your email password, and contact each bank/wallet (below).

## WhatsApp account takeover (very common here)
The scam: someone (often from a hijacked friend's or group account) gets you to share the 6-digit SMS code WhatsApp sends you, then takes over your account and asks your contacts for money. Argentina's federal cybercrime prosecutors (UFECI) have warned about it.
- **Turn on two-step verification now:** WhatsApp > "Ajustes" > "Cuenta" > "Verificación en dos pasos" > "Activar", choose a 6-digit PIN, and add a recovery email. https://www.argentina.gob.ar/justicia/convosenlaweb/situaciones/como-configurar-la-seguridad-en-whatsapp
- Never share a WhatsApp code or a screenshot of it, with anyone, for any reason. WhatsApp never asks for it.
- Check "Dispositivos vinculados" for WhatsApp Web sessions you don't recognize and close them.
- If it happens: warn your contacts by another channel, reinstall WhatsApp and re-register your number, and report it (below). https://www.fiscales.gob.ar/ciberdelincuencia/consejos-de-la-ufeci-para-evitar-maniobras-que-toman-el-control-de-las-cuentas-de-whatsapp/
- A "money request" from a relative on WhatsApp: call them on their known number or ask the family code word first.

## Banks and wallets
Install apps only from the official App Store / Google Play. No bank, wallet, or the BCRA asks for your password, token, PIN, or codes by phone, social media, email, or chat.
- **Banco Nación (BNA+):** turn on the app's Token ("Tu banco" > "Token"); it's the 6-digit second factor for home banking. https://bna.com.ar/Personas/BNAMas/PreguntasFrecuentesBNAmas. Other banks have their own token in the app; turn it on and keep it on one trusted phone.
- **Mercado Pago:** turn on two-step verification and add an authenticator app (Google Authenticator) as the method; turn on biometrics. Help article: https://www.mercadopago.com.ar/ayuda/Como-configuro-Google-Authenticator-como-metodo-de-verificacion_31092
- **Ualá:** turn on fingerprint/Face ID ("Configuración" > "Claves y seguridad"). You can freeze cards instantly in the app ("Congelar"). If you lose account access: recuperarmicuenta@uala.com.ar. https://www.uala.com.ar/aula-uala/blog/categorias/seguridad/que-hacer-robo-celular
- **Brubank:** biometrics and notifications on; pause the card when you're not using it. If your phone is lost or stolen, report it at https://brubank.com/report so they unlink it from your account. Change password: "Mi Cuenta" > "Seguridad" > "Cambiar clave". https://www.brubank.com/seguridad
- For every bank and wallet: push notifications for every movement, know where "freeze card" is, and check linked devices.

## Registro Nacional No Llame (do-not-call)
- Free. Register mobile and landlines at https://nollame.aaip.gob.ar. Covers calls, SMS, and messaging apps like WhatsApp for advertising. Companies have up to 30 days to stop. It doesn't stop scammers, surveys, or companies you already have a contract with. You can file a complaint on the same site if calls continue.

## Where to report fraud
1. **Your bank or wallet first:** call right away, ask to block access and cards, and get a claim number ("número de reclamo").
2. **Police or fiscalía report** for theft, identity theft, or online fraud. Federal cybercrime unit UFECI: denunciasufeci@mpf.gov.ar, (+54 11) 5071-0040 / 0041.
3. **BCRA, if the bank doesn't solve it:** after at least 10 business days, file a "Reclamo por fraude o estafa" with your claim number, the bank's reply, DNI images, and the transactions. https://www.bcra.gob.ar/realizar-un-reclamo-ante-el-banco-central-por-fraude-o-estafa/
4. **Defensa del Consumidor:** 0800-666-1518, consultas@consumidor.gob.ar.
5. Fake BCRA messages can be forwarded to ayudaenlinea@bcra.gob.ar.

## Monthly
- BCRA Central de Deudores check (takes one minute); Veraz free report every six months; bank/wallet notifications reviewed; WhatsApp linked devices; Mi Argentina active sessions.
