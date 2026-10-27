"""Testi legali per il generatore del sito lmautoservizi.it.

BOZZA per revisione professionale (27 ottobre 2026). Fonte completa e
commentata: materiali/testi-legali/ (01 informativa, 03 vettura di cortesia,
04 garanzia, 07 recensioni). Se cambi un testo qui, cambia anche il file .md.

Ogni costante e' un frammento HTML da passare a str.format(**dati) con questi
campi (i campi non usati da un testo vengono ignorati):

    {titolare} {sede_legale} {piva} {email} {pec} {telefono} {aggiornamento}

Tag usati: <h2>, <h3>, <p>, <ul><li>, <strong>, <a href>.
I punti da controllare sono commenti HTML "<!-- DA VERIFICARE: ... -->":
non si vedono nella pagina, ma restano nel sorgente pubblicato. Toglierli dopo
la revisione. Nei testi non ci sono parentesi graffe letterali.
"""

CAMPI = ("titolare", "sede_legale", "piva", "email", "pec", "telefono", "aggiornamento")

_EST = 'target="_blank" rel="noopener"'

# ---------------------------------------------------------------- privacy IT
PRIVACY_IT = f"""<p><strong>Ultimo aggiornamento:</strong> {{aggiornamento}}</p>
<p>In questa pagina ti spiego quali dati tratto, perché e per quanto tempo, come chiede il Regolamento europeo sulla protezione dei dati (GDPR, art. 13). In breve: uso i tuoi dati per risponderti, lavorare sulla tua auto e rispettare la legge. Il sito non usa cookie né statistiche. Promemoria e offerte su WhatsApp solo se mi rispondi SÌ.</p>

<h2>Chi sono</h2>
<p>Il titolare del trattamento è <strong>{{titolare}}</strong>, ditta individuale, {{sede_legale}}, P.IVA {{piva}}. Telefono e WhatsApp {{telefono}}, email <a href="mailto:{{email}}">{{email}}</a>, PEC <a href="mailto:{{pec}}">{{pec}}</a>.</p>
<!-- DA VERIFICARE: aggiungere l'indirizzo dell'officina se diverso dalla sede legale. -->
<p>Non ho nominato un responsabile della protezione dei dati (DPO), perché per un'officina come la mia non è obbligatorio. Per qualsiasi domanda sui tuoi dati scrivi o chiama direttamente me.</p>

<h2>Il sito</h2>
<h3>Niente cookie, niente statistiche</h3>
<p>Il sito non usa cookie, non usa strumenti di statistica e non carica contenuti da altri siti, come mappe, video, caratteri tipografici esterni o pulsanti dei social. Per questo non vedi un banner per i cookie.</p>
<!-- DA VERIFICARE prima di ogni pubblicazione: che il sito non carichi risorse da server esterni. -->
<p>Se scegli il tema chiaro o scuro, il browser ricorda la scelta nella sua memoria locale. È un'impostazione tecnica che chiedi tu: resta sul tuo dispositivo e io non la vedo.</p>
<h3>Dati tecnici del server</h3>
<p>Il sito è ospitato da un fornitore esterno (hosting). Quando apri una pagina, il server riceve dati tecnici come indirizzo IP, data e ora, pagina richiesta e tipo di browser. Servono a mostrarti la pagina e a proteggere il sito da abusi. La base giuridica è il mio legittimo interesse a tenere il sito sicuro e funzionante (art. 6.1.f GDPR). Non uso questi dati per sapere chi sei. Il fornitore li conserva per pochi giorni o settimane, secondo le sue condizioni.</p>
<!-- DA VERIFICARE: nome del fornitore di hosting, intestatario dell'account, Paese dei server, durata dei log, eventuale trasferimento fuori UE. -->
<!-- OPZIONALE: statistiche senza cookie. Rendere visibile solo se si attivano, scegliendo il fornitore e firmando l'accordo art. 28.
<h3>Statistiche senza cookie</h3>
<p>Per capire quali pagine sono più utili uso [Cloudflare Web Analytics oppure GoatCounter]. Lo strumento conta le visite in forma aggregata (pagina vista, sito di provenienza, tipo di dispositivo, paese), senza cookie, senza conservare l'indirizzo IP completo e senza creare profili. La base giuridica è il mio legittimo interesse a migliorare il sito (art. 6.1.f GDPR). Il fornitore tratta i dati per conto mio come responsabile del trattamento. [Solo per Cloudflare: Cloudflare, Inc. ha sede negli Stati Uniti; il trasferimento è coperto dall'EU-US Data Privacy Framework e dalle clausole contrattuali standard.]</p>
DA VERIFICARE: se uno script di statistica senza cookie richieda comunque il consenso (art. 122 Codice privacy e Linee guida EDPB 2/2023); sede e server di GoatCounter.
-->
<h3>Link ad altri siti</h3>
<p>Alcuni pulsanti aprono servizi esterni, come WhatsApp, Google Maps o le mie recensioni su Google. Quando li apri esci dal mio sito e valgono le regole privacy di quei servizi.</p>

<h2>Richieste con il pulsante WhatsApp</h2>
<p>Alcune pagine ti aiutano a preparare un messaggio: scegli il servizio, scrivi il problema e, se vuoi, la targa o il comune dove si trova l'auto. Il testo resta nel tuo browser: il sito non lo salva e non lo manda a nessun server. Quando premi il pulsante si apre WhatsApp con il messaggio già scritto. Lo puoi cambiare, e parte solo quando premi tu "Invia". Il link passa da WhatsApp, che tratta il testo secondo la sua informativa.</p>
<!-- DA VERIFICARE sul sito finale: che il modulo non salvi bozze e non mandi dati a servizi esterni. -->
<ul>
<li><strong>Che dati ricevo:</strong> il tuo numero, il nome e la foto del profilo WhatsApp, quello che scrivi (per esempio nome, targa, modello, problema, dove si trova l'auto) e le foto o la posizione, se me le mandi.</li>
<li><strong>Perché:</strong> per risponderti, farti un preventivo e organizzare il lavoro, il ritiro dell'auto o l'intervento con l'officina mobile.</li>
<li><strong>Base giuridica:</strong> la tua richiesta, cioè misure precontrattuali e contratto (art. 6.1.b GDPR). Non serve un consenso.</li>
<li><strong>Sei obbligato?</strong> No, ma senza questi dati non posso risponderti. La targa è facoltativa: mi aiuta a riconoscere il modello e a trovare i ricambi giusti.</li>
</ul>

<h2>Telefono, email e PEC</h2>
<p>Se mi chiami vedo il tuo numero e prendo nota di quello che mi dici sul lavoro. Se serve, salvo il numero nella rubrica del telefono dell'officina. Per l'email uso Gmail, un servizio di Google; per la PEC il servizio del mio gestore PEC. La base giuridica è la tua richiesta e il contratto (art. 6.1.b GDPR).</p>
<!-- DA VERIFICARE: gestore della PEC; accordo sul trattamento dei dati con Google se si usa un account Gmail gratuito. -->

<h2>Come uso WhatsApp</h2>
<ul>
<li><strong>Il titolare sono io.</strong> Le chat con i clienti le gestisco io, con l'app WhatsApp Business sul telefono dell'officina.</li>
<li><strong>Il servizio è di WhatsApp Ireland Limited</strong> (gruppo Meta). Per una parte dei dati che tratta per conto mio WhatsApp agisce come responsabile del trattamento, in base ai Termini sul trattamento dei dati di WhatsApp Business. Per i dati del tuo account WhatsApp decide in modo autonomo, secondo la sua informativa.</li>
<!-- DA VERIFICARE: qualificazione dei ruoli di WhatsApp per l'app WhatsApp Business. -->
<li><strong>Crittografia.</strong> I messaggi sono cifrati end-to-end: WhatsApp non può leggerne il contenuto, ma tratta altri dati, come numero, orari dei messaggi e informazioni sul dispositivo.</li>
<li><strong>Trasferimento negli Stati Uniti.</strong> Le società del gruppo Meta trattano dati anche negli USA. Il trasferimento è coperto dall'EU-US Data Privacy Framework (decisione della Commissione europea 2023/1795) e dalle clausole contrattuali standard (decisione 2021/914).</li>
<li><strong>Le regole di WhatsApp:</strong> <a href="https://www.whatsapp.com/legal/privacy-policy-eea" {_EST}>informativa sulla privacy</a>, <a href="https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App" {_EST}>termini di WhatsApp Business</a>, <a href="https://www.whatsapp.com/legal/business-data-processing-terms" {_EST}>termini sul trattamento dei dati</a>, <a href="https://www.whatsapp.com/legal/data-privacy-framework" {_EST}>Data Privacy Framework</a>.</li>
<li><strong>Come proteggo le chat.</strong> Il telefono è protetto da un codice e il backup delle chat è cifrato. Non ti aggiungo a gruppi: il tuo numero non lo vede nessun altro cliente.</li>
<!-- DA VERIFICARE: che Luca attivi il backup cifrato end-to-end di WhatsApp. -->
<li><strong>Non vuoi usare WhatsApp?</strong> Chiamami o scrivimi per email: il servizio è lo stesso.</li>
<li><strong>Cosa non mandarmi:</strong> dati della carta di pagamento, password, documenti che non ti ho chiesto. Non ti chiederò mai dati di pagamento su WhatsApp.</li>
</ul>

<h2>Messaggi sul tuo lavoro</h2>
<p>Durante un lavoro ti scrivo per il preventivo, per chiederti l'OK prima di lavori in più, per mandarti le foto del guasto e del lavoro finito, per gli orari di ritiro e consegna e per avvisarti che l'auto è pronta. Sono messaggi necessari per il servizio che mi hai chiesto (art. 6.1.b GDPR): non sono pubblicità e non serve un consenso. Se preferisci un altro canale, dimmelo.</p>

<h2>Promemoria e offerte: solo se mi dici SÌ</h2>
<p>Ti posso mandare due tipi di messaggi in più. Sono facoltativi e separati: puoi accettarne uno, tutti e due o nessuno.</p>
<ul>
<li><strong>Promemoria</strong> quando si avvicinano la revisione, il tagliando o il cambio gomme di stagione. Per farlo tengo nome, numero, modello e targa dell'auto, le scadenze e i chilometri dell'ultimo intervento.</li>
<li><strong>Offerte</strong> sui miei servizi e prodotti, per esempio sulle gomme.</li>
</ul>
<p>La base giuridica è il tuo consenso (art. 6.1.a GDPR e art. 130 del Codice privacy). Te lo chiedo a voce o nella chat del tuo lavoro: rispondi SÌ per i promemoria, SÌ OFFERTE per le offerte. Annoto data e testo della domanda in un registro. Se dici no, il servizio in officina è lo stesso. I promemoria arrivano solo quando si avvicina una scadenza e le offerte sono poche.</p>
<!-- DA VERIFICARE: aggiungere il numero massimo di messaggi quando Luca lo decide (proposta: promemoria al massimo 4 all'anno, offerte al massimo 2 al mese). -->
<p><strong>Per smettere scrivi STOP</strong> quando vuoi, oppure dimmelo a voce, per telefono o per email. Smetto subito. La revoca non rende illegittimi i messaggi mandati prima (art. 7.3 GDPR). Tengo questi dati finché non scrivi STOP e comunque non oltre 24 mesi dal tuo ultimo intervento in officina. Non creo profili.</p>
<!-- DA VERIFICARE: durata di 24 mesi, per analogia con il provvedimento del Garante sulle carte fedeltà del 24 febbraio 2005. -->

<h2>Lavori in officina, ritiro e consegna, officina mobile</h2>
<p>Tratto nome e contatti; l'indirizzo dove ritiro o riconsegno l'auto, o dove intervengo con l'officina mobile, e la posizione se me la mandi; i dati dell'auto (targa, telaio, chilometri, scadenze); il problema e i risultati della diagnosi; preventivo, ordine di lavoro e foto del lavoro; i dati per la fattura. Se l'auto me la porta o la ritira un'altra persona, anche il suo nome. La targa è un dato personale, perché collega l'auto a una persona.</p>
<ul>
<li>Per fare il lavoro che mi chiedi: contratto (art. 6.1.b GDPR).</li>
<li>Per fatture e contabilità: obbligo di legge (art. 6.1.c GDPR).</li>
<li>Per difendermi in caso di contestazioni, anche con le foto del prima e del dopo: legittimo interesse (art. 6.1.f GDPR).</li>
</ul>
<p>Durante la diagnosi leggo solo dati tecnici della centralina. Non guardo e non copio rubrica, telefoni collegati o indirizzi del navigatore. Se vuoi, cancellali prima di lasciarmi l'auto.</p>

<h2>Vettura di cortesia</h2>
<p>Se ti presto la vettura di cortesia firmiamo un contratto di comodato gratuito. Tratto nome, data e luogo di nascita, residenza, codice fiscale, telefono, i dati della patente e il verbale di consegna e riconsegna, con chilometri, carburante e foto dell'auto.</p>
<!-- DA VERIFICARE: se basta annotare i dati della patente o serve tenerne una copia. -->
<ul>
<li>Per prestarti l'auto: contratto (art. 6.1.b GDPR).</li>
<li>Per le multe: come proprietario dell'auto devo comunicare chi guidava all'organo di polizia entro 60 giorni dalla notifica (art. 126-bis del Codice della strada; obbligo di legge, art. 6.1.c GDPR).</li>
<li>Per sinistri, danni, pedaggi e ZTL, con l'assicurazione e gli enti interessati: contratto e legittimo interesse (art. 6.1.b e 6.1.f GDPR).</li>
</ul>
<!-- DA VERIFICARE: intestatario della vettura di cortesia; presenza di scatola nera o localizzatore GPS, da dichiarare qui se c'è. -->

<h2>Recensioni e foto</h2>
<ul>
<li><strong>Recensioni su Google:</strong> le tratta Google secondo le sue regole. Se ti rispondo, non scrivo dati tuoi, della tua auto o del lavoro.</li>
<li><strong>Richiesta di recensione:</strong> dopo il lavoro posso mandarti un solo messaggio per chiederla, uguale per tutti i clienti, senza premi né sconti. Va bene anche una recensione critica. Base giuridica: il mio legittimo interesse a far conoscere il mio lavoro (art. 6.1.f GDPR). Puoi opporti quando vuoi.</li>
<!-- DA VERIFICARE: se la richiesta di recensione via WhatsApp rientri nell'art. 130 del Codice privacy e richieda il consenso. -->
<li><strong>Recensioni sul mio sito:</strong> solo con il tuo permesso, con il nome e l'iniziale del cognome. Base giuridica: il tuo consenso (art. 6.1.a GDPR).</li>
<li><strong>Foto della tua auto:</strong> solo con il tuo permesso e sempre con la targa coperta. Persone riconoscibili solo con il loro permesso scritto (art. 96 della legge 633/1941). Base giuridica: il tuo consenso (art. 6.1.a GDPR).</li>
</ul>
<p>Tolgo recensioni e foto quando me lo chiedi.</p>

<h2>A chi possono arrivare i tuoi dati</h2>
<p>Solo a chi serve, e solo i dati che servono:</p>
<ul>
<li>commercialista, per fatture e contabilità;</li>
<li>Agenzia delle Entrate e Sistema di Interscambio, per le fatture elettroniche, e il fornitore del programma di fatturazione;</li>
<li>assicurazioni e periti, per sinistri e vettura di cortesia;</li>
<li>fornitori di ricambi e gomme: solo targa, telaio o modello, per ordinare il pezzo giusto;</li>
<li>altre officine o centri di revisione, solo se affido loro una parte del lavoro e te lo dico prima;</li>
<li>banca e gestore del POS, per i pagamenti;</li>
<li>fornitori di servizi informatici e di comunicazione: WhatsApp Ireland Limited, Google (Gmail), il gestore della PEC, il fornitore di hosting del sito;</li>
<li>il web designer che gestisce il sito, nominato responsabile del trattamento (art. 28 GDPR) se gestisce hosting, manutenzione o statistiche;</li>
<li>autorità pubbliche, quando la legge lo chiede, e un avvocato se devo far valere un mio diritto.</li>
</ul>
<!-- DA VERIFICARE: ruolo del commercialista (titolare autonomo o responsabile); programma di fatturazione; se Luca affida lavori ad altre officine o centri di revisione. -->
<p>Chi tratta dati per conto mio lo fa come responsabile del trattamento (art. 28 GDPR). Non vendo i tuoi dati. Non li pubblico, salvo recensioni e foto per cui mi hai dato il permesso.</p>

<h2>Dati fuori dall'Unione europea</h2>
<p>WhatsApp (gruppo Meta) e Google possono trattare dati negli Stati Uniti. Il trasferimento è coperto dall'EU-US Data Privacy Framework e dalle clausole contrattuali standard della Commissione europea (artt. 45 e 46 GDPR). Se vuoi informazioni su queste garanzie, scrivimi.</p>
<!-- DA VERIFICARE: Paese dei server del fornitore di hosting e garanzia usata se fuori UE. -->

<h2>Per quanto tempo tengo i dati</h2>
<ul>
<li>Richieste che non diventano un lavoro: 12 mesi dall'ultimo messaggio.</li>
<li>Chat, foto e documenti di un lavoro: 26 mesi dalla consegna dell'auto, il periodo della garanzia legale.</li>
<li>Fatture e documenti fiscali: 10 anni, come chiede la legge.</li>
<li>Vettura di cortesia: dati della patente 12 mesi dalla riconsegna; contratto e verbale 26 mesi.</li>
<li>Dati per promemoria e offerte: finché non scrivi STOP, al massimo 24 mesi dall'ultimo intervento. La prova del consenso e della revoca: 5 anni dalla revoca.</li>
<li>Recensioni e foto pubblicate: finché non mi chiedi di toglierle.</li>
<li>Dati tecnici del server: secondo le condizioni del fornitore di hosting.</li>
</ul>
<!-- DA VERIFICARE: tutti i tempi di conservazione di questo elenco, tranne i 10 anni dei documenti fiscali. -->
<p>Se c'è una contestazione o una causa, tengo i dati che servono fino a quando è chiusa.</p>

<h2>I tuoi diritti</h2>
<p>Puoi chiedermi in ogni momento di vedere i tuoi dati e averne una copia, correggerli, cancellarli, limitarne l'uso, riceverli in un formato leggibile da un computer, opporti ai trattamenti basati sul mio legittimo interesse e sempre ai messaggi promozionali, e ritirare un consenso (artt. 7 e 15–21 GDPR).</p>
<p>Scrivimi su WhatsApp, per email o PEC, oppure dimmelo in officina. Ti rispondo gratis entro un mese. Se la richiesta è complicata posso arrivare a tre mesi, ma te lo dico entro il primo mese. Se ho dubbi su chi sei, posso chiederti di identificarti.</p>
<p>Se pensi che io tratti i tuoi dati in modo scorretto, puoi fare reclamo al <a href="https://www.garanteprivacy.it" {_EST}>Garante per la protezione dei dati personali</a> o all'autorità del Paese europeo dove vivi o lavori, oppure rivolgerti al giudice.</p>

<h2>Nessuna decisione automatica</h2>
<p>Non prendo decisioni basate solo su sistemi automatici e non faccio profilazione (art. 22 GDPR).</p>

<h2>Devi darmi i dati?</h2>
<p>I dati per preventivo, lavoro, fattura e vettura di cortesia sono necessari: senza, non posso fare il lavoro o prestarti l'auto. Alcuni li chiede la legge. I consensi per promemoria, offerte, recensioni sul sito e foto sono facoltativi.</p>

<h2>Modifiche</h2>
<p>Se cambio questa informativa aggiorno la data in alto. Se cambia qualcosa di importante, te lo dico prima.</p>"""

# ---------------------------------------------------------------- privacy EN
PRIVACY_EN = f"""<p><strong>Last updated:</strong> {{aggiornamento}}</p>
<p>This page explains what personal data I process, why and for how long, as required by the EU General Data Protection Regulation (GDPR, Art. 13). In short: I use your data to reply to you, work on your car and comply with the law. The website uses no cookies and no analytics. Reminders and offers on WhatsApp only if you reply SÌ (yes). This is a translation: if in doubt, the Italian version prevails.</p>

<h2>Who I am</h2>
<p>The data controller is <strong>{{titolare}}</strong>, sole proprietorship, {{sede_legale}}, Italy, VAT no. {{piva}}. Phone and WhatsApp {{telefono}}, email <a href="mailto:{{email}}">{{email}}</a>, certified email (PEC) <a href="mailto:{{pec}}">{{pec}}</a>. I have not appointed a Data Protection Officer, as one is not required for a workshop like mine.</p>
<!-- DA VERIFICARE: add the workshop address if different from the registered office. -->

<h2>The website</h2>
<p>The website uses no cookies and no analytics, and loads no content from other websites (maps, videos, external fonts, social buttons), so it shows no cookie banner. If you choose the light or dark theme, your browser remembers the choice in its local storage: a technical setting that stays on your device.</p>
<p>The website is hosted by an external provider. When you open a page, its server receives technical data such as IP address, date and time, page requested and browser type, to deliver the page and protect the site from abuse. Legal basis: my legitimate interest in a secure, working website (Art. 6(1)(f) GDPR). I do not use this data to identify you. The provider keeps it for a few days or weeks under its own terms.</p>
<!-- DA VERIFICARE: hosting provider, server location, log retention, transfers outside the EU. -->
<!-- OPTIONAL: cookieless analytics. Make visible only if activated.
<h3>Cookieless analytics</h3>
<p>To see which pages are most useful I use [Cloudflare Web Analytics or GoatCounter], which counts visits in aggregate form (page, referrer, device type, country) without cookies, without storing the full IP address and without profiling. Legal basis: my legitimate interest in improving the website (Art. 6(1)(f) GDPR). The provider acts as my processor. [Cloudflare only: Cloudflare, Inc. is based in the USA; transfers rely on the EU-US Data Privacy Framework and standard contractual clauses.]</p>
-->
<p>Some buttons open external services (WhatsApp, Google Maps, my Google reviews), whose own privacy rules apply.</p>

<h2>Requests via the WhatsApp button</h2>
<p>Some pages help you prepare a message. What you type stays in your browser: the website does not store it or send it to any server. WhatsApp then opens with the message ready, and it is sent only when you tap "Send". I receive your number, your WhatsApp profile name and photo, what you write (for example name, number plate, model, problem, where the car is) and any photos or location you send. I use them to reply, prepare a quote and organise the job, the pick-up or the mobile service. Legal basis: your request (pre-contractual measures and contract, Art. 6(1)(b) GDPR); no consent is needed. The number plate is optional.</p>

<h2>Phone, email and PEC</h2>
<p>If you call me, I see your number and note what you tell me about the job; if needed, I save your number in the workshop phone. For email I use Gmail, a Google service; for certified email my PEC provider. Legal basis: your request and the contract (Art. 6(1)(b) GDPR).</p>

<h2>How I use WhatsApp</h2>
<ul>
<li>I am the controller of my chats with customers, which I manage with the WhatsApp Business app on the workshop phone.</li>
<li>The service is provided by WhatsApp Ireland Limited (Meta group). For some data it processes on my behalf it acts as my processor under the WhatsApp Business Data Processing Terms; for your WhatsApp account data it acts as an independent controller.</li>
<li>Messages are end-to-end encrypted: WhatsApp cannot read their content, but it processes other data such as numbers, message times and device information.</li>
<li>Meta group companies also process data in the USA. Transfers rely on the EU-US Data Privacy Framework (Commission Decision 2023/1795) and standard contractual clauses (Decision 2021/914).</li>
<li>WhatsApp's rules: <a href="https://www.whatsapp.com/legal/privacy-policy-eea" {_EST}>privacy policy</a>, <a href="https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App" {_EST}>WhatsApp Business terms</a>, <a href="https://www.whatsapp.com/legal/business-data-processing-terms" {_EST}>data processing terms</a>, <a href="https://www.whatsapp.com/legal/data-privacy-framework" {_EST}>Data Privacy Framework</a>.</li>
<li>My phone is locked with a code and chat backups are encrypted. I never add customers to groups. Don't want to use WhatsApp? Call or email me: the service is the same. Never send me card details or passwords: I will never ask for payment data on WhatsApp.</li>
</ul>

<h2>Messages about your job</h2>
<p>During a job I write to you about the quote, to ask your approval before extra work, to send photos of the fault and of the finished work, about pick-up and delivery times and to tell you the car is ready. These messages are needed for the service you asked for (Art. 6(1)(b) GDPR): they are not advertising and need no consent.</p>

<h2>Reminders and offers: only if you say yes</h2>
<p>I can send you two optional, separate kinds of messages: <strong>reminders</strong> when your MOT (revisione), service or seasonal tyre change is due, for which I keep your name, number, car model and plate, due dates and mileage; and <strong>offers</strong> on my services and products. Legal basis: your consent (Art. 6(1)(a) GDPR and Art. 130 of the Italian Privacy Code). I ask in person or in your job chat: reply SÌ for reminders, SÌ OFFERTE for offers. I record the date and wording. Saying no does not change the service.</p>
<p><strong>To stop, write STOP</strong> at any time, or tell me in person, by phone or by email. I stop at once; withdrawal does not affect earlier messages. I keep this data until you write STOP, and no longer than 24 months after your last job at the workshop. No profiling.</p>

<h2>Workshop jobs, pick-up and delivery, mobile service</h2>
<p>I process your name and contact details, the address for pick-up, delivery or mobile service (and your location if you share it), car data (plate, VIN, mileage, due dates), the problem and diagnostic results, quote, job sheet, photos of the work and invoicing data, plus the name of anyone who drops off or collects the car for you. A number plate is personal data. Legal bases: the contract (Art. 6(1)(b) GDPR); legal obligations for invoices and accounts (Art. 6(1)(c)); my legitimate interest in defending myself against claims, also with before-and-after photos (Art. 6(1)(f)). During diagnostics I read only technical data from the car's control units; I do not look at or copy your contacts, paired phones or navigation addresses.</p>

<h2>Courtesy car</h2>
<p>If I lend you the courtesy car, we sign a free loan agreement (comodato). I process your name, date and place of birth, address, tax code, phone, driving licence details and the hand-over and return report (mileage, fuel, photos of the car). Legal bases: the contract (Art. 6(1)(b) GDPR); the legal obligation, as the car's owner, to tell the police who was driving within 60 days of a fine being notified (Art. 126-bis of the Italian Highway Code; Art. 6(1)(c) GDPR); the contract and my legitimate interest for accidents, damage, tolls and limited traffic zones (Art. 6(1)(b) and (f)).</p>

<h2>Reviews and photos</h2>
<ul>
<li>Google reviews are processed by Google under its own rules. When I reply, I never mention your data, your car or the job.</li>
<li>After a job I may send you one message asking for a review: the same for every customer, with no rewards or discounts, and critical reviews are welcome. Legal basis: my legitimate interest (Art. 6(1)(f) GDPR); you can object at any time.</li>
<li>I republish a review on my website, with your first name and initial, and publish photos of your car, with the plate covered, only with your permission (Art. 6(1)(a) GDPR). Recognisable people only with their written permission. I remove them whenever you ask.</li>
</ul>

<h2>Who may receive your data</h2>
<ul>
<li>my accountant; the Italian Revenue Agency and e-invoicing system, and my invoicing software provider;</li>
<li>insurers and loss adjusters; parts and tyre suppliers (only plate, VIN or model); other workshops or MOT centres only if I subcontract part of the job and tell you first;</li>
<li>my bank and card terminal provider;</li>
<li>IT and communication providers: WhatsApp Ireland Limited, Google (Gmail), my PEC provider, the website hosting provider;</li>
<li>the web designer who manages the website, appointed as my processor (Art. 28 GDPR) if he manages hosting, maintenance or analytics;</li>
<li>public authorities when required by law, and a lawyer if I need to enforce my rights.</li>
</ul>
<p>I never sell your data, and I publish nothing about you without your permission.</p>

<h2>Transfers outside the EU</h2>
<p>WhatsApp (Meta group) and Google may process data in the USA, under the EU-US Data Privacy Framework and the European Commission's standard contractual clauses (Arts. 45 and 46 GDPR). Write to me for details.</p>

<h2>How long I keep data</h2>
<ul>
<li>Requests that don't become a job: 12 months from the last message.</li>
<li>Chats, photos and documents of a job: 26 months from delivery of the car, the legal guarantee period.</li>
<li>Invoices and tax records: 10 years, as required by law.</li>
<li>Courtesy car: licence details 12 months from return; agreement and report 26 months.</li>
<li>Reminder and offer data: until you write STOP, at most 24 months from your last job. Proof of consent and withdrawal: 5 years from withdrawal.</li>
<li>Published reviews and photos: until you ask me to remove them.</li>
<li>Server technical data: as set by the hosting provider.</li>
</ul>
<!-- DA VERIFICARE: all retention periods above except the 10 years for tax records. -->
<p>If there is a dispute, I keep the data needed until it is settled.</p>

<h2>Your rights</h2>
<p>You can ask me at any time to access your data and get a copy, correct it, erase it, restrict its use, receive it in a machine-readable format, object to processing based on my legitimate interest (and always to promotional messages) and withdraw consent (Arts. 7 and 15–21 GDPR). Write to me on WhatsApp, by email or PEC, or tell me at the workshop. I reply free of charge within one month (up to three months for complex requests, in which case I tell you within the first month). You can also lodge a complaint with the Italian <a href="https://www.garanteprivacy.it" {_EST}>Garante per la protezione dei dati personali</a> or the supervisory authority where you live or work, or go to court.</p>

<h2>No automated decisions</h2>
<p>I make no decisions based solely on automated processing and do no profiling (Art. 22 GDPR).</p>

<h2>Do you have to give me your data?</h2>
<p>Data for quotes, jobs, invoices and the courtesy car is necessary: without it I cannot do the job or lend you the car. Some of it is required by law. Consent for reminders, offers, reviews on the website and photos is optional.</p>

<h2>Changes</h2>
<p>If I change this notice, I update the date at the top. If something important changes, I tell you first.</p>"""

# ------------------------------------------------- vettura di cortesia (sito)
VETTURA_CORTESIA_IT = """<ul>
<li>È gratuita per tutto il tempo della riparazione: non paghi il prestito. Te la lascio con il pieno: riportala con lo stesso carburante.</li>
<li>Serve una patente valida: la guardo alla consegna e annoto i dati. Guidi tu, o la persona che indichi nel contratto.</li>
<li>Alla consegna e alla riconsegna compiliamo insieme un verbale con chilometri, carburante e foto dell'auto.</li>
<li>L'auto è assicurata. Se causi un danno, potresti pagare al massimo la franchigia scritta nelle condizioni.</li>
<!-- DA VERIFICARE con l'assicuratore: coperture e importo della franchigia; se la parola "gratuita" resta corretta con carburante e franchigia a carico del cliente. -->
<li>Multe, ZTL, pedaggi e parcheggi durante il prestito sono a carico di chi guida: per legge comunico i dati del conducente all'autorità che fa la multa.</li>
<li>Le condizioni complete le leggi e le firmi quando ti consegno l'auto.</li>
</ul>"""

VETTURA_CORTESIA_EN = """<ul>
<li>It is free for as long as the repair takes: you pay nothing for the loan. I give it to you with a full tank: please return it with the same fuel level.</li>
<li>You need a valid driving licence: I check it at hand-over and note its details. Only you, or the person named in the agreement, may drive.</li>
<li>At hand-over and return we fill in a report together, with mileage, fuel and photos of the car.</li>
<li>The car is insured. If you cause damage, you may have to pay up to the excess stated in the conditions.</li>
<!-- DA VERIFICARE with the insurer: cover and excess amount. -->
<li>Fines, limited traffic zones, tolls and parking during the loan are the driver's responsibility: by law I give the driver's details to the authority issuing the fine.</li>
<li>You read and sign the full conditions when I hand over the car.</li>
</ul>"""

# ----------------------------------------------------------- garanzia (sito)
GARANZIA_SITO_IT = """<p>Se sei un consumatore hai sempre la <strong>garanzia di legge</strong>: per i ricambi che monto vale 2 anni dalla consegna dell'auto, come prevede il Codice del Consumo.</p>
<p>In più ti do una <strong>garanzia mia sul lavoro</strong>: se un intervento che ho fatto non funziona come deve, lo sistemo gratis, ricambi e manodopera compresi. Vale anche per chi ha la partita IVA.</p>
<!-- DA VERIFICARE: togliere "Vale anche per chi ha la partita IVA" se Luca non estende la garanzia ai clienti con P.IVA. Il sito non deve promettere più del testo completo (file 04). -->
<p>La durata della garanzia sul lavoro te la scrivo sul preventivo, insieme alle condizioni. Quando ritiri l'auto ti do le condizioni complete per iscritto.</p>
<p>La mia garanzia si aggiunge a quella di legge: non la sostituisce e non la riduce.</p>"""

GARANZIA_SITO_EN = """<p>If you are a consumer, you always have the <strong>legal guarantee</strong>: for the parts I fit, it lasts 2 years from delivery of the car, as set by the Italian Consumer Code.</p>
<p>On top of that I give you <strong>my own guarantee on the work</strong>: if a repair I did doesn't work as it should, I fix it free of charge, parts and labour included. It also applies to business customers.</p>
<p>I write the length of the work guarantee on your quote, together with its conditions, and give you the full conditions in writing when you collect the car.</p>
<p>My guarantee is in addition to the legal one: it does not replace or reduce it.</p>"""

# -------------------------------------------- nota sotto le recensioni (sito)
RECENSIONI_NOTA_IT = """<p>Queste recensioni vengono dal mio profilo Google e le pubblico qui con il permesso di chi le ha scritte. Sono di clienti per cui ho fatto un lavoro: le confronto con i miei lavori prima di pubblicarle. Non pago e non premio nessuno per le recensioni. Le trovi tutte, anche quelle critiche, sul mio profilo Google.</p>
<!-- DA VERIFICARE: art. 22, comma 5-bis, Codice del Consumo; che Luca controlli davvero ogni recensione con i suoi lavori. -->"""

RECENSIONI_NOTA_EN = """<p>These reviews come from my Google profile and are published here with their authors' permission. They are from customers I have worked for: I check them against my jobs before publishing. I never pay or reward anyone for reviews. You can read them all, critical ones included, on my Google profile.</p>"""

__all__ = [
    "CAMPI",
    "PRIVACY_IT", "PRIVACY_EN",
    "VETTURA_CORTESIA_IT", "VETTURA_CORTESIA_EN",
    "GARANZIA_SITO_IT", "GARANZIA_SITO_EN",
    "RECENSIONI_NOTA_IT", "RECENSIONI_NOTA_EN",
]


if __name__ == "__main__":
    # Controllo rapido: ogni testo si formatta con i campi previsti e non
    # lascia graffe; "DA VERIFICARE" compare solo dentro commenti HTML.
    import re

    prova = {c: f"<{c}>" for c in CAMPI}
    for nome in __all__[1:]:
        html = globals()[nome].format(**prova)
        assert "{" not in html and "}" not in html, nome
        visibile = re.sub(r"<!--.*?-->", "", html, flags=re.S)
        assert "DA VERIFICARE" not in visibile, nome
        assert "OPZIONALE" not in visibile and "OPTIONAL" not in visibile, nome
        for commento in re.findall(r"<!--(.*?)-->", html, flags=re.S):
            assert "--" not in commento, nome
        print(f"ok  {nome:22} {len(html):6} caratteri")
