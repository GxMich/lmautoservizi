"""Testi delle pagine nuove (servizi, officina, home), in italiano.
Fonti dei fatti: contenuti.py, biglietto da visita, versione semplice approvata. Niente prezzi né dati da confermare."""

# Note per chi impagina:
# - "title" finisce sempre con " | L.M. Autoservizi" e resta entro 65 caratteri; "description" entro 155.
# - "risposta" è il paragrafo che apre la pagina: è pensato per essere citato così com'è da Google e dagli assistenti AI.
# - Le FAQ sono adatte anche al dato strutturato FAQPage (testo semplice, senza HTML).
# - L'officina è in Via Ticineto 15 (confermato da Luca il 29/10/2026); nei testi brevi basta "a Frassineto Po".
# - Gli anni di esperienza vengono da contenuti.ANNI_ESPERIENZA: si aggiornano da soli a ogni generazione.

from contenuti import ANNI_ESPERIENZA

SERVIZI_PAGINE = {
    # ------------------------------------------------------------------ MECCANICA
    "meccanica": {
        "nome": "Meccanica",
        "title": "Meccanico a Frassineto Po, vicino a Casale | L.M. Autoservizi",
        "description": "Tagliandi, manutenzione e riparazioni meccaniche sul ponte, su tutte le marche. Officina a Frassineto Po, vicino a Casale. Chiedi un preventivo gratuito.",
        "h1": "Meccanico a Frassineto Po",
        "risposta": ("Sono Luca Miglietta, di L.M. Autoservizi. Lavoro da solo nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Faccio tagliandi, manutenzione ordinaria e straordinaria e riparazioni meccaniche, anche sul ponte, su tutte le marche. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo è gratuito e arriva prima di iniziare."),
        "comprende": [
            ("Tagliandi",
             "Tagliando secondo il piano di manutenzione della casa, su auto, fuoristrada, furgoni e camper."),
            ("Manutenzione ordinaria e straordinaria",
             "Dai controlli periodici ai lavori più impegnativi. Prima ti dico cosa serve e quanto costa."),
            ("Riparazioni sul ponte",
             "Con il ponte lavoro sotto il mezzo e vedo bene cosa c'è da fare."),
            ("Freni, rumori e vibrazioni",
             "Un rumore in frenata o una vibrazione nuova vanno controllati. Cerco la causa e ti spiego cosa ho trovato."),
            ("Ricambi",
             "Vendo ricambi per tutte le marche. Se vuoi, il pezzo lo monto io in officina."),
        ],
        "perche": [
            ("Preventivo prima di iniziare",
             "Prima ascolto il problema, poi ti dico cosa serve e quanto costa. Inizio solo quando ti va bene."),
            ("Un solo riferimento",
             "Lavoro da solo: la tua auto la segue la stessa persona, dalla prima telefonata alla riconsegna."),
            ("Vettura di cortesia gratuita",
             "Ti lascio un'auto con il pieno, pulita e igienizzata. Ne ho una: chiedila quando prenoti."),
        ],
        "faq": [
            ("Fai il tagliando su auto di tutte le marche?",
             "Sì, lavoro su auto, fuoristrada, furgoni e camper di tutte le marche. Scrivimi marca, modello e chilometri e ti preparo il preventivo."),
            ("Posso fare il tagliando da te se l'auto è in garanzia?",
             ("In generale sì: per le regole europee la garanzia resta valida se segui il piano di manutenzione della casa. "
              "Riparazioni in garanzia e richiami restano invece alla rete ufficiale. Se hai dubbi, portami il libretto e lo guardiamo insieme.")),
            ("Sento un rumore quando freno: è grave?",
             "Un rumore in frenata va controllato presto, senza aspettare. Portami l'auto: la guardo sul ponte e ti dico cosa serve e quanto costa."),
            ("E se durante il lavoro trovi altro da sistemare?",
             "Ti chiamo e ti spiego cosa ho trovato. I lavori in più li faccio solo dopo il tuo ok."),
            ("Quanto tempo resta in officina l'auto per il tagliando?",
             ("Dipende dal mezzo e da cosa prevede il tagliando. Quando ci accordiamo ti dico quando portarla e quando riprenderla. "
              "Con l'orario continuato puoi lasciarla prima del lavoro e passare a prenderla dopo.")),
        ],
        "nota_mezzo": "Es. tagliando in scadenza, rumore in frenata, perdita d'olio. Scrivi anche i chilometri.",
        "correlati": ["elettrauto", "diagnosi"],
    },

    # ------------------------------------------------------------------ ELETTRAUTO (con climatizzatore)
    "elettrauto": {
        "nome": "Elettrauto",
        "title": "Elettrauto a Frassineto Po, vicino a Casale | L.M. Autoservizi",
        "description": "Avviamento, batteria, luci, cablaggi e climatizzatore: trovo e riparo i difetti elettrici. Officina a Frassineto Po, vicino a Casale. Scrivimi su WhatsApp.",
        "h1": "Elettrauto a Frassineto Po",
        "risposta": ("Sono Luca Miglietta e lavoro da solo nella mia officina, L.M. Autoservizi, a Frassineto Po, vicino a Casale Monferrato. "
                     "Mi occupo di avviamento, batteria e ricarica, impianto luci, accessori e cablaggi. "
                     "Controllo e ricarico anche il climatizzatore. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo è gratuito e arriva prima di iniziare."),
        "comprende": [
            ("Avviamento",
             "Se l'auto fatica a partire, controllo avviamento, batteria e ricarica e trovo dov'è il problema."),
            ("Batteria e ricarica",
             "Verifico lo stato della batteria e dell'impianto di ricarica. La sostituisco solo se serve."),
            ("Impianto luci",
             "Fari, frecce, luci di stop e luci interne: trovo il guasto e lo riparo."),
            ("Accessori e cablaggi",
             "Monto accessori e sistemo cablaggi, anche su furgoni e camper."),
            ("Difetti elettrici",
             "Ogni genere di difetto elettrico, anche quelli che vanno e vengono. Prima cerco la causa, poi ti dico cosa serve."),
            ("Climatizzatore",
             "Controllo dell'impianto e ricarica del gas. Ho la formazione per il recupero dei gas fluorurati (Reg. CE 307/2008)."),
        ],
        "perche": [
            ("Qualifica in elettromeccanica",
             f"Ho la qualifica di operatore di riparazioni elettromeccaniche per l'autoveicolo. Lavoro su tutte le marche da {ANNI_ESPERIENZA} anni."),
            ("Formazione sui gas fluorurati",
             "Per il climatizzatore ho la formazione sul recupero dei gas fluorurati nei veicoli, secondo il Reg. CE 307/2008."),
            ("Prima il preventivo",
             "Ti dico cosa ho trovato e quanto costa la riparazione. Se trovo altro, ti chiamo prima di procedere."),
        ],
        "faq": [
            ("L'auto fatica a partire la mattina: è la batteria?",
             "Può essere la batteria, ma anche la ricarica o l'avviamento. Con un controllo capisco da dove viene il problema e ti dico cosa serve prima di cambiare qualcosa."),
            ("La batteria si scarica anche con l'auto ferma: perché?",
             "Può esserci qualcosa che consuma corrente a motore spento, oppure un difetto nella ricarica. Lo cerco controllando l'impianto elettrico, poi ti dico cosa serve e quanto costa."),
            ("Il climatizzatore raffredda poco: basta ricaricarlo?",
             "A volte sì, ma prima controllo l'impianto. Se il gas è calato, conviene capire anche perché. Ti dico cosa serve prima di ricaricare."),
            ("Monti anche accessori sull'auto?",
             "Sì, monto accessori e sistemo cablaggi e luci. Dimmi cosa vuoi installare e su che mezzo, e ti preparo il preventivo."),
            ("Lavori anche su furgoni e camper?",
             "Sì: auto, fuoristrada, furgoni e camper, di tutte le marche. Per i mezzi più grandi scrivimi prima, così ti dico quando portarli."),
        ],
        "nota_mezzo": "Es. fatica a partire, la batteria si scarica, il clima raffredda poco. Scrivi anche quando succede.",
        "correlati": ["mobile", "diagnosi", "meccanica"],
    },

    # ------------------------------------------------------------------ GOMMISTA
    "gommista": {
        "nome": "Gommista",
        "title": "Gommista a Frassineto Po, vicino a Casale | L.M. Autoservizi",
        "description": "Cambio gomme, equilibratura, convergenza e forature a Frassineto Po, vicino a Casale. Gomme estive, invernali e quattro stagioni: scrivimi la misura.",
        "h1": "Gommista a Frassineto Po",
        "risposta": ("Sono Luca Miglietta e faccio il gommista nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Lavoro da solo, con le attrezzature per montaggio, equilibratura e convergenza. "
                     "Riparo forature, faccio il cambio stagionale con il deposito delle gomme e vendo gomme estive, invernali e quattro stagioni. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo è gratuito e arriva prima di iniziare."),
        "comprende": [
            ("Sostituzione pneumatici",
             "Smonto e monto le gomme sul cerchio, in officina."),
            ("Equilibratura",
             "Equilibro le ruote quando monto le gomme, o se il volante vibra in velocità."),
            ("Convergenza e campanatura",
             "Controllo e regolo l'assetto delle ruote. È utile se l'auto tira da un lato."),
            ("Riparazione forature",
             "Se il foro si può riparare in sicurezza, lo riparo. Altrimenti ti dico quale gomma conviene montare."),
            ("Cambio stagionale",
             "Monto le invernali in autunno e le estive in primavera, nei periodi previsti."),
            ("Deposito gomme",
             "Le gomme della stagione che non usi restano da me, al riparo, fino al prossimo cambio."),
            ("Vendita pneumatici",
             "Estive, invernali e quattro stagioni. Dimmi la misura o la targa e ti rispondo con disponibilità e prezzo."),
        ],
        "perche": [
            ("Tutto nella stessa officina",
             "Montaggio, equilibratura e convergenza li faccio qui, con le attrezzature giuste."),
            ("La gomma adatta al tuo uso",
             "Estive, invernali o quattro stagioni: ti aiuto a scegliere in base a come usi il mezzo."),
            ("Aperto dalle 7:30 alle 19:30",
             "Dal lunedì al venerdì, orario continuato: lasci l'auto prima del lavoro e la riprendi dopo."),
        ],
        "faq": [
            ("Quando si montano le gomme invernali?",
             ("Dove previsto dalle ordinanze, servono gomme invernali o catene a bordo, di solito dal 15 novembre al 15 aprile. "
              "Le invernali si possono montare dal 15 ottobre. Le estive si rimontano entro il 15 maggio.")),
            ("Ogni quanto si fa la convergenza?",
             ("Dipende dall'auto e da come la usi. Conviene controllarla quando monti gomme nuove o dopo un colpo forte contro una buca o un marciapiede. "
              "Anche se l'auto tira da un lato o le gomme si consumano in modo irregolare.")),
            ("Si può riparare una foratura o devo cambiare la gomma?",
             "Dipende da dove si trova il foro e da quanto è grande. La guardo e ti dico se si ripara in sicurezza o se conviene cambiarla."),
            ("Vendi anche le gomme?",
             ("Sì, estive, invernali e quattro stagioni. Scrivimi la misura che trovi sul fianco della gomma, per esempio 205/55 R16, oppure la targa. "
              "Ti rispondo con disponibilità e prezzo.")),
            ("Mi tieni tu le gomme che non uso?",
             "Sì, faccio il deposito: le gomme della stagione che non usi restano da me fino al prossimo cambio. Chiedimi il prezzo quando prenoti."),
            ("Fai anche equilibratura e convergenza?",
             "Sì, in officina ho le attrezzature per montaggio, equilibratura e convergenza. Se la convergenza serve, te lo dico prima di farla."),
        ],
        "nota_mezzo": "Es. cambio stagionale, foratura, gomme nuove. Scrivi la misura: la trovi sul fianco della gomma.",
        "correlati": ["gomme", "mobile", "meccanica"],
    },

    # ------------------------------------------------------------------ CARROZZERIA
    "carrozzeria": {
        "nome": "Carrozzeria",
        "title": "Carrozzeria a Frassineto Po, vicino a Casale | L.M. Autoservizi",
        "description": "Carrozzeria, verniciatura, saldatura e sistemazioni varie a Frassineto Po, vicino a Casale. Mandami le foto del danno su WhatsApp per una prima idea.",
        "h1": "Carrozzeria a Frassineto Po",
        "risposta": ("Sono Luca Miglietta e lavoro da solo nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Faccio carrozzeria, verniciatura, saldatura e sistemazioni varie, su mezzi di tutte le marche. "
                     "Per una prima idea mandami le foto del danno su WhatsApp, oppure chiamami. "
                     "Il preventivo è gratuito e arriva prima di iniziare. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato."),
        "comprende": [
            ("Carrozzeria",
             "Ammaccature e urti su paraurti, portiere e fiancate."),
            ("Verniciatura",
             "Vernicio le parti riparate o rovinate, come una portiera graffiata."),
            ("Saldatura",
             "Saldature sulla carrozzeria, anche su furgoni e camper."),
            ("Sistemazioni varie",
             "Anche i lavori piccoli. Mandami una foto e ti dico come la vedo."),
            ("Prima idea dalle foto",
             "Mandami le foto del danno su WhatsApp. Il preventivo preciso te lo faccio quando vedo il mezzo."),
        ],
        "perche": [
            ("Preventivo gratuito",
             "Sai quanto costa prima che inizi. Così puoi confrontare i prezzi con calma."),
            ("Un solo riferimento",
             "Parli sempre con me, dalla prima foto alla riconsegna. Ti aggiorno io su come va il lavoro."),
            ("Vettura di cortesia gratuita",
             "Se il lavoro richiede più giorni, hai un'auto con il pieno, pulita e igienizzata."),
        ],
        "faq": [
            ("Posso mandarti le foto del danno?",
             "Sì, mandale su WhatsApp e ti do una prima idea. Il preventivo preciso te lo faccio quando vedo il mezzo."),
            ("Sistemi anche un graffio o una piccola ammaccatura?",
             "Sì, faccio anche i lavori piccoli. Mandami una foto e ti dico come la vedo."),
            ("Ripari anche ruggine e parti da saldare?",
             "Faccio saldature e sistemazioni varie, anche su furgoni e camper. Mandami una foto della zona e ti dico se conviene intervenire."),
            ("Quanto resta in officina il mezzo?",
             "Dipende dal lavoro: ne parliamo quando ti do il preventivo. Intanto puoi avere la vettura di cortesia gratuita: dimmelo quando prenoti."),
            ("Quando e come pago?",
             "Paghi alla riconsegna, in contanti, con carta o con bancomat."),
        ],
        "nota_mezzo": "Es. urto sul paraurti, graffio sulla portiera. Mandami anche le foto del danno su WhatsApp.",
        "correlati": ["meccanica", "diagnosi"],
    },

    # ------------------------------------------------------------------ DIAGNOSI E PRE-REVISIONE
    "diagnosi": {
        "nome": "Diagnosi e pre-revisione",
        "title": "Diagnosi auto e pre-revisione a Frassineto Po | L.M. Autoservizi",
        "description": "Spie, errori e programmazione centraline con software aggiornato ogni giorno, a Frassineto Po. Controllo gratuito prima della revisione: scrivimi.",
        "h1": "Diagnosi e pre-revisione a Frassineto Po",
        "risposta": ("Sono Luca Miglietta e lavoro da solo nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Leggo errori e spie e programmo centraline con software aggiornato ogni giorno. "
                     "Prima della revisione controllo gratis il mezzo e te la prenoto. "
                     "La fanno solo la Motorizzazione o i centri autorizzati. "
                     "Sono aperto dal lunedì al venerdì, 7:30–19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo gratuito arriva prima di iniziare."),
        "comprende": [
            ("Lettura di errori e spie",
             "Collego la diagnosi e leggo cosa segnala la centralina, prima di decidere cosa fare."),
            ("Programmazione centraline",
             "Programmo le centraline quando serve. Dimmi marca, modello e anno e ti dico se posso farlo."),
            ("Controllo pre-revisione gratuito",
             "Prima della revisione periodica controllo il mezzo gratis. Se trovo qualcosa, ti dico cosa serve e quanto costa."),
            ("Prenotazione della revisione",
             "Ti prenoto io la revisione presso la Motorizzazione o un centro autorizzato."),
            ("Riparazioni dopo la diagnosi",
             "Se la diagnosi trova un guasto, ti spiego cosa serve. Riparo solo dopo il tuo ok."),
        ],
        "perche": [
            ("Software aggiornato ogni giorno",
             "Leggo errori e spie con un software di diagnosi aggiornato ogni giorno."),
            ("Responsabile tecnico delle revisioni",
             "Ho l'abilitazione di responsabile tecnico delle revisioni periodiche. Conosco i controlli che aspettano il tuo mezzo."),
            ("Controllo gratuito e prenotazione",
             "Ti controllo il mezzo gratis prima della revisione e ti prenoto io l'appuntamento."),
        ],
        "faq": [
            ("La spia del motore è accesa: posso continuare a guidare?",
             ("Dipende dalla spia e da come si comporta l'auto. Se la spia è rossa o lampeggia, o l'auto cambia comportamento, fermati appena puoi in sicurezza e chiamami. "
              "Negli altri casi fai leggere l'errore presto.")),
            ("La revisione la fai tu?",
             "La revisione la fanno solo la Motorizzazione o i centri autorizzati. Io controllo il mezzo gratis prima, ti dico se c'è qualcosa da sistemare e ti prenoto la revisione."),
            ("Ogni quanto va fatta la revisione?",
             "La prima revisione va fatta entro quattro anni dalla prima immatricolazione, poi ogni due anni. Scrivimi la scadenza e ti organizzo il controllo gratuito prima."),
            ("Cosa controlli nella pre-revisione?",
             "Guardo i punti che si verificano in revisione, come luci, freni, gomme e spie. Se trovo qualcosa ti dico cosa serve e quanto costa, e decidi tu."),
            ("Mi hanno detto che va programmata la centralina: lo fai?",
             "Programmo le centraline con software aggiornato ogni giorno. Scrivimi marca, modello e anno del mezzo e ti dico se posso farlo e quanto costa."),
            ("La diagnosi si può fare anche fuori dall'officina?",
             "Di solito la faccio in officina. Nei casi semplici leggo le spie anche sul posto, con l'assistenza a domicilio, entro 20 km da Frassineto Po."),
        ],
        "nota_mezzo": "Es. spia del motore accesa, revisione in scadenza a marzo. Se puoi, fai una foto della spia.",
        "correlati": ["mobile", "elettrauto", "meccanica"],
    },
    # ------------------------------------------------------------------ ALLESTIMENTI (richiesta di Luca, 29/10/2026)
    # Fatti certi: il Ford Ranger attrezzato per il campeggio, progettato e costruito da Luca da zero; lavora su auto,
    # fuoristrada, furgoni e camper. Niente elenchi di prodotti o modifiche specifiche finché Luca non li conferma.
    "allestimenti": {
        "nome": "Allestimenti camping e fuoristrada",
        "title": "Allestimenti camping e 4x4 a Frassineto Po | L.M. Autoservizi",
        "description": "Allestimenti su misura per il campeggio e il fuoristrada, progettati e costruiti in officina a Frassineto Po. Raccontami il tuo mezzo e cosa vorresti fare.",
        "h1": "Allestimenti camping e fuoristrada",
        "risposta": ("Sono Luca Miglietta e nella mia officina a Frassineto Po progetto e costruisco allestimenti per il campeggio e il fuoristrada. "
                     "Il mio Ford Ranger attrezzato per il campeggio l'ho progettato e costruito da zero. "
                     "Lo stesso lavoro lo posso fare sul tuo pick-up, fuoristrada, furgone o camper: partiamo da come lo usi e da cosa vorresti fare. "
                     "Il preventivo è gratuito e arriva prima di iniziare."),
        "comprende": [
            ("Allestimenti per il campeggio",
             "Soluzioni per dormire e campeggiare con il tuo mezzo, pensate sul tuo modo di viaggiare."),
            ("Allestimenti per il fuoristrada",
             "Modifiche e accessori per usare il mezzo fuori strada, con la stessa cura che metto in officina."),
            ("Progetto su misura",
             "Ascolto cosa ti serve, ti propongo una soluzione e ti dico quanto costa prima di iniziare."),
            ("Costruito in officina",
             "Il lavoro lo faccio io, nella mia officina a Frassineto Po, dall'inizio alla fine."),
        ],
        "perche": [
            ("L'ho fatto prima sul mio mezzo",
             "Il mio Ford Ranger l'ho allestito da zero: so cosa vuol dire usarlo davvero, in campeggio e fuori strada."),
            (f"{ANNI_ESPERIENZA} anni di meccanica",
             "Conosco il mezzo che sta sotto l'allestimento: lavoro su auto, fuoristrada, furgoni e camper di tutte le marche."),
            ("Vicino a casa",
             "Non serve andare lontano: lo progetto e lo costruisco a Frassineto Po, vicino a Casale Monferrato."),
        ],
        "faq": [
            ("Su che mezzi lavori?",
             "Pick-up, fuoristrada, furgoni e camper. Scrivimi marca, modello e anno, e cosa vorresti realizzare: ti dico se si può fare."),
            ("Quanto costa un allestimento?",
             "Dipende da cosa vuoi realizzare e dal mezzo. Dopo che ne abbiamo parlato ti preparo un preventivo gratuito, prima di iniziare."),
            ("Posso vedere un lavoro che hai fatto?",
             "Sì: le foto del mio Ford Ranger sono anche sul mio profilo Google, e se passi in officina te lo faccio vedere."),
        ],
        "nota_mezzo": "Dimmi che mezzo hai e cosa vorresti realizzare: per dormire, per il fuoristrada o tutti e due.",
        "correlati": ["meccanica", "carrozzeria"],
    },
}

SERVIZI_HUB = {
    "title": "Servizi auto a Frassineto Po, vicino a Casale | L.M. Autoservizi",
    "description": "Meccanica, elettrauto e clima, gommista, carrozzeria, diagnosi e pre-revisione su tutte le marche, a Frassineto Po. Chiedi un preventivo gratuito.",
    "h1": "Servizi auto a Frassineto Po",
    "intro": ("Nella mia officina a Frassineto Po, vicino a Casale Monferrato, seguo auto, fuoristrada, furgoni e camper. "
              "Lavoro su tutte le marche, da solo, dalla prima telefonata alla riconsegna. "
              "Scegli il servizio: per ognuno trovi cosa comprende e le domande più frequenti. "
              "Il preventivo è gratuito e arriva prima di iniziare."),
}

OFFICINA_PAGINA = {
    "title": "Officina a Frassineto Po, orario continuato | L.M. Autoservizi",
    "description": "Officina multimarca a Frassineto Po, vicino a Casale. Aperta lun–ven 7:30–19:30, orario continuato. Vettura di cortesia gratuita. Chiamami o scrivimi.",
    "h1": "L'officina a Frassineto Po",
    "intro": ("La mia officina è a Frassineto Po, a pochi chilometri da Casale Monferrato. "
              "Qui trovi me, il ponte e le attrezzature per lavorare bene sul tuo mezzo. "
              "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, senza pausa pranzo."),
    "sezioni": [
        ("Cosa trovi in officina",
         ("Il ponte, per lavorare sotto il mezzo. La diagnosi, con software aggiornato ogni giorno. "
          "Le attrezzature per le gomme: montaggio, equilibratura e convergenza. "
          "L'officina è abilitata per meccatronica, carrozzeria e gommista, come chiede la legge 122/1992. "
          "E ci sono io, che seguo il tuo mezzo dall'inizio alla fine.")),
        ("Orario continuato, dal lunedì al venerdì",
         ("Sono aperto dalle 7:30 alle 19:30, senza pausa pranzo. "
          "Puoi lasciare l'auto prima di andare al lavoro e riprenderla quando esci. "
          "Sabato e domenica sono chiuso.")),
        ("Vettura di cortesia gratuita",
         ("Mentre riparo il tuo mezzo, ti lascio una vettura di cortesia gratuita, per tutta la riparazione. "
          "Ne ho una sola, quindi chiedila quando prenoti. Te la consegno con il pieno, pulita e igienizzata, e le condizioni te le spiego alla consegna.")),
        ("Pagamenti",
         ("Paghi alla riconsegna, in contanti, con carta o con bancomat. "
          "Il preventivo è gratuito e i lavori in più li faccio solo dopo il tuo ok.")),
    ],
    "cortesia_passi": [
        ("Me lo dici quando prenoti",
         "Quando mi chiami o mi scrivi, dimmi che ti serve la vettura di cortesia."),
        ("La trovi pronta",
         "Quando porti il tuo mezzo, la trovi con il pieno, pulita e igienizzata. Ti spiego le condizioni alla consegna."),
        ("La usi per tutta la riparazione",
         "Resta a te finché il tuo mezzo è pronto. Ti aggiorno io su come va il lavoro."),
        ("Fai cambio alla riconsegna",
         "Mi riporti la vettura di cortesia e riprendi il tuo mezzo. Paghi la riparazione alla riconsegna."),
    ],
    "faq": [
        ("Quali sono gli orari dell'officina?",
         "Dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. Sabato e domenica sono chiuso."),
        ("Serve l'appuntamento?",
         "Meglio chiamare o scrivere prima, così ti dico quando portarla. Se ti serve la vettura di cortesia, dimmelo subito."),
        ("Come funziona la vettura di cortesia?",
         "È gratuita e la tieni per tutta la riparazione. Ne ho una: chiedila quando prenoti. Te la consegno con il pieno, pulita e igienizzata, e ti spiego le condizioni alla consegna."),
        ("Come posso pagare?",
         "Paghi alla riconsegna, in contanti, con carta o con bancomat."),
        ("Se faccio il tagliando da te, perdo la garanzia della casa?",
         ("In generale, secondo le regole europee, il tagliando in un'officina indipendente non fa decadere la garanzia del costruttore. "
          "Conta seguire il piano di manutenzione previsto dalla casa. Riparazioni in garanzia e richiami restano alla rete ufficiale.")),
    ],
}

HOME = {
    # Sezione subito dopo la griglia dei servizi: l'officina al centro.
    "officina_titolo": "Ti aspetto in officina, a Frassineto Po.",
    "officina_testo": ("La mia officina è a pochi chilometri da Casale Monferrato. "
                       "Sono aperto dal lunedì al venerdì con orario continuato: lasci l'auto prima del lavoro e la riprendi dopo. "
                       "Se ti serve, hai una vettura di cortesia gratuita: dimmelo quando prenoti."),
    "officina_punti": [
        ("Orario continuato 7:30–19:30",
         "Dal lunedì al venerdì, senza pausa pranzo. Sabato e domenica chiuso."),
        ("Vettura di cortesia gratuita",
         "Con il pieno, pulita e igienizzata. Ne ho una: chiedila quando prenoti."),
        ("Preventivo gratuito prima di iniziare",
         "Ti dico cosa serve e quanto costa. Si parte solo quando ti va bene."),
    ],
    # Subito dopo la griglia dei servizi: officina, ritiro e domicilio sullo stesso piano (Luca, 29/10/2026).
    # Ogni voce: (titolo, etichetta breve, testo).
    "modi_titolo": "In officina, con il ritiro o a domicilio.",
    "modi_testo": "Scegli come ti è più comodo. Dall'altra parte trovi sempre me, e il preventivo è sempre gratuito.",
    "modi_voci": [
        ("In officina", "Lun–ven 7:30–19:30",
         "Porti il mezzo in Via Ticineto 15, a Frassineto Po. Lavoro con il ponte e le attrezzature giuste, e se la riparazione è lunga ti lascio la vettura di cortesia."),
        ("Ritiro e consegna", "Gratis entro 20 km",
         "Passo a prendere il mezzo a casa o al lavoro, lo riparo in officina e te lo riporto dove vuoi."),
        ("A domicilio", "Interventi veloci",
         "Cambio della batteria, diagnosi con il computer, riparazione della gomma bucata: arrivo io, dove sei."),
    ],
}
