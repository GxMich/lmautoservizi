"""Testi legali per il generatore del sito lmautoservizi.it.

BOZZA per revisione professionale (27 ottobre 2026). Fonte completa e
commentata: materiali/testi-legali/ (01 informativa, 03 vettura di cortesia,
04 garanzia, 07 recensioni). Se cambi un testo qui, cambia anche il file .md.
Solo italiano: le versioni inglesi sono state tolte con la versione inglese del sito (29/10/2026).

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
<!-- DA VERIFICARE: la vettura è a noleggio con Ayvens (Luca, 29/10/2026): con le multe notificate ad Ayvens cambia la procedura dell'art. 126-bis; presenza di scatola nera o localizzatore GPS, da dichiarare qui se c'è. -->

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
<li>la società di noleggio della vettura di cortesia (Ayvens), per sinistri, multe e pedaggi;</li>
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

# ------------------------------------------------- vettura di cortesia (sito)
VETTURA_CORTESIA_IT = """<ul>
<li>È gratuita per tutto il tempo della riparazione: non paghi il prestito. Te la lascio con il pieno: riportala con lo stesso carburante.</li>
<li>Ne ho una sola: chiedila quando prenoti il lavoro.</li>
<li>Serve una patente valida: la guardo alla consegna e annoto i dati. Guidi tu, o la persona che indichi nel contratto.</li>
<li>Alla consegna e alla riconsegna compiliamo insieme un verbale con chilometri, carburante e foto dell'auto.</li>
<li>È un'auto a noleggio, assicurata anche con la kasko. Se causi un danno, potresti pagare al massimo la franchigia scritta nelle condizioni.</li>
<!-- DA VERIFICARE: Luca (29/10/2026) dice che è tutto coperto, kasko, contratto di noleggio con Ayvens. Restano da sapere: importo della franchigia; che il contratto Ayvens permetta di prestare l'auto ai clienti; se la parola "gratuita" resta corretta con carburante e franchigia a carico del cliente. -->
<li>Multe, ZTL, pedaggi e parcheggi durante il prestito sono a carico di chi guida: per legge comunico i dati del conducente all'autorità che fa la multa.</li>
<li>Le condizioni complete le leggi e le firmi quando ti consegno l'auto.</li>
</ul>"""

# ----------------------------------------------------------- garanzia (sito)
GARANZIA_SITO_IT = """<p>Se sei un consumatore hai sempre la <strong>garanzia di legge</strong>: per i ricambi che monto vale 2 anni dalla consegna dell'auto, come prevede il Codice del Consumo.</p>
<p>In più ti do una <strong>garanzia mia sul lavoro</strong>: se un intervento che ho fatto non funziona come deve, lo sistemo gratis, ricambi e manodopera compresi. Vale anche per chi ha la partita IVA.</p>
<!-- DA VERIFICARE: togliere "Vale anche per chi ha la partita IVA" se Luca non estende la garanzia ai clienti con P.IVA. Il sito non deve promettere più del testo completo (file 04). -->
<p>La garanzia sul lavoro dura <strong>12 mesi</strong> dalla riconsegna del mezzo. Le condizioni te le scrivo sul preventivo e, quando ritiri l'auto, te le do complete per iscritto.</p>
<!-- DA VERIFICARE: Luca ha risposto «12 mesi per legge» (29/10/2026). Per i consumatori la garanzia di legge sui ricambi resta di 2 anni (Codice del Consumo): i 12 mesi qui sono la garanzia di Luca sul lavoro. Confermare con lui che è questo che intende. -->
<p>La mia garanzia si aggiunge a quella di legge: non la sostituisce e non la riduce.</p>"""

# -------------------------------------------- nota sotto le recensioni (sito)
RECENSIONI_NOTA_IT = """<p>Queste recensioni vengono dal mio profilo Google e le pubblico qui con il permesso di chi le ha scritte. Sono di clienti per cui ho fatto un lavoro: le confronto con i miei lavori prima di pubblicarle. Non pago e non premio nessuno per le recensioni. Le trovi tutte, anche quelle critiche, sul mio profilo Google.</p>
<!-- DA VERIFICARE: art. 22, comma 5-bis, Codice del Consumo; che Luca controlli davvero ogni recensione con i suoi lavori. -->"""

__all__ = [
    "CAMPI",
    "PRIVACY_IT",
    "VETTURA_CORTESIA_IT",
    "GARANZIA_SITO_IT",
    "RECENSIONI_NOTA_IT",
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
