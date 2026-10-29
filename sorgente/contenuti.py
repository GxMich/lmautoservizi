"""Dati dell'attività usati dal generatore (sorgente/genera.py).
Fonti: biglietto da visita/PDF del cliente e testi già approvati del sito.
I valori None sono dati ancora da chiedere a Luca: il sito li omette e genera.py li elenca in materiali/da-completare.md."""
import datetime, os

QUI = os.path.dirname(os.path.abspath(__file__))

DOMINIO = "https://www.lmautoservizi.it"
TEL, TEL_TXT = "+393426436085", "342 643 6085"
WA = "https://wa.me/393426436085?text=Ciao%20Luca%2C%20vorrei%20informazioni."
EMAIL = "lucamiglietta4@gmail.com"
PEC = "lucamiglie@pec.it"
PIVA = "02625920067"
MAPS = "https://maps.app.goo.gl/MKwoz3CKAvCdeNwj8"
# Sede legale e officina coincidono (risposta di Luca al questionario, 29/10/2026).
SEDE_LEGALE = "Via Ticineto 15, 15040 Frassineto Po (AL)"
GEAR = open(os.path.join(QUI, "ingranaggio.txt"), encoding="utf-8").read().strip()
GEAR_PIENO = f"{GEAR} M197 0A197 197 0 1 0 -197 0A197 197 0 1 0 197 0Z"

# Officina: Via Ticineto 15, lo stesso indirizzo della sede legale. Frassineto Po ha un solo CAP (15040).
INDIRIZZO_OFFICINA = "Via Ticineto 15"
CAP_OFFICINA = "15040"
COMUNE_OFFICINA = "Frassineto Po"
PROVINCIA = "AL"
GEO = (45.1284713, 8.5431679)      # il punto della scheda Google (link MAPS), in gradi decimali
RAGGIO_KM = 20                     # ritiro, consegna e domicilio: raggio dall'officina, ritiro sempre gratis
# Frasi uniche, riusate in tutte le pagine: se cambiano, cambiano ovunque.
ZONA_TESTO = "entro 20 km dall'officina: Casale Monferrato, Valenza, Occimiano, San Salvatore Monferrato, Mede e i paesi vicini"
CORTESIA_TESTO = "Ho una sola vettura di cortesia, gratuita: se è libera, la tieni finché il tuo mezzo è pronto. Chiedila quando prenoti."
ANNO_INIZIO = 2006                 # inizio dell'esperienza di Luca: 20 anni nel 2026 (lo ha detto lui il 29/10/2026)
ANNI_ESPERIENZA = datetime.date.today().year - ANNO_INIZIO   # alla generazione; nella pagina lo ricalcola anche 00-base.js
REA = "AL-271409"
# Sezioni dell'abilitazione di autoriparazione (legge 122/1992, come modificata dalla legge 224/2012), confermate da Luca il 29/10/2026.
ABILITAZIONI = ["meccatronica", "carrozzeria", "gommista"]
# La pagina https://www.facebook.com/L.M.AUTOSERVIZI/ è di Luca, ma per scelta non va sul sito (28/10/2026).
# Instagram non c'è.
FACEBOOK = None
INSTAGRAM = None
RECENSIONI_GOOGLE = None           # link diretto "scrivi una recensione" della scheda Google
PREZZI = None                      # Luca non pubblica prezzi, solo preventivo (29/10/2026)
# Noleggio a lungo termine: il link dedicato del PDF «QR NOLEGGIO LUNGO TERMINE» che Luca ha mandato il 29/10/2026.
NOLEGGIO_LINK = None
NOLEGGIO_QR = "assets/img/noleggio-qr.png"   # il QR dello stesso PDF: compare accanto al link solo se il file c'è in docs/
RECENSIONI_CON_PERMESSO = None     # True quando Beatrice, Denise e Paolo hanno detto sì a vedere la loro recensione sul sito

# Spiegazione dei dati mancanti: genera.py la stampa per ogni valore rimasto None.
DA_COMPLETARE = {
    "CAP_OFFICINA": "CAP dell'officina.",
    "FACEBOOK": "la pagina è di Luca ma per scelta non va sul sito: resta None (non serve completarlo).",
    "INSTAGRAM": "Luca dice di non avere Instagram: resta None finché non apre un profilo.",
    "RECENSIONI_GOOGLE": "link diretto «scrivi una recensione» dal Profilo dell'attività su Google (Chiedi recensioni): aggiunge il pulsante sotto le recensioni.",
    "NOLEGGIO_LINK": "il link del noleggio a lungo termine, dal PDF «QR NOLEGGIO LUNGO TERMINE» di Luca (29/10/2026): con il link compaiono la casella in home e la scheda in Servizi. Il QR va salvato in docs/assets/img/noleggio-qr.png.",
    "PREZZI": "Luca preferisce solo il preventivo, senza prezzi sul sito (29/10/2026): resta None (non serve completarlo).",
    "RECENSIONI_CON_PERMESSO": "le tre recensioni in home vengono dalla scheda Google (29/10/2026): manca il sì di chi le ha scritte (Beatrice D., Denise F., Paolo C.), da chiedere con il modulo 07. Con True compare la nota del Codice del Consumo (nota_recensioni).",
}

# Recensioni vere della scheda Google (lette il 29/10/2026, tutte a 5 stelle), con nome e iniziale come ha detto Luca.
# Le tre di prima (Marco, Alessia, Giacomo) sulla scheda non ci sono: Luca non sapeva da dove venissero.
RECENSIONI = [("Trovare un meccanico bravo è difficile, ma trovare una persona di cui fidarsi CIECAMENTE è quasi impossibile. Lui è super attento, onesto e trasparente. "
               "Ormai gli lascio le chiavi della macchina e non ci penso più, sapendo che è in mani sicure. Un professionista serio e sincero come pochi. Consigliatissimo!", "Beatrice D."),
              ("Estremamente competente, gentile e disponibile. Ti spiega molto bene il lavoro che andrà a fare e come. Onesto ed esperto, consiglio a chiunque.", "Denise F."),
              ("Sostituzione batteria. Passaggio a casa e viceversa. Persona a mio avviso affidabile. Tutto ok", "Paolo C.")]

DETT = [
    ("manutenzione", "Tagliando e manutenzione", "Manutenzione ordinaria e straordinaria su auto di tutte le marche. Ti dico cosa serve e quanto costa prima di iniziare.",
     ["Assistenza e manutenzione programmata", "Riparazioni meccaniche, anche sul ponte", "Preventivo gratuito dopo la diagnosi"]),
    ("diagnosi", "Diagnosi centraline", "Una spia accesa sul cruscotto si legge subito, prima di decidere cosa fare. Software aggiornato ogni giorno.",
     ["Lettura degli errori e delle spie", "Programmazione delle centraline", "Diagnosi in officina o, nei casi semplici, da te"]),
    ("elettrauto", "Elettrauto", "Diagnosi e riparazione di ogni genere di difetto elettrico.",
     ["Problemi di avviamento e di ricarica", "Impianto luci, accessori e cablaggi", "Preventivo prima di iniziare"]),
    ("clima", "Climatizzatore", "Controllo e ricarica dell'impianto di climatizzazione. Ho la formazione per il recupero dei gas fluorurati nei veicoli.",
     ["Controllo dell'impianto", "Ricarica del gas", "Formazione sul recupero dei gas fluorurati (Reg. CE 307/2008)"]),
    ("gomme", "Gomme", "Il cambio dei pneumatici sul cerchio si fa in officina. Le forature e il cambio delle ruote già montate le faccio anche da te.",
     ["Sostituzione pneumatici, equilibratura, convergenza e campanatura", "Riparazione delle forature", "Cambio stagionale delle ruote montate"]),
    ("carrozzeria", "Carrozzeria", "Lavori di carrozzeria, verniciatura, saldatura e sistemazioni varie. Chiedi un preventivo gratuito e confronta i prezzi.",
     ["Carrozzeria e sistemazioni varie", "Verniciatura", "Saldatura"]),
    ("revisione", "Pre-revisione", "Non farti trovare impreparato: ti controllo l'auto gratis prima della revisione periodica e ti prenoto la revisione.",
     ["Controllo generale gratuito", "Prenotazione della revisione", "Sono abilitato come responsabile tecnico delle revisioni"]),
    ("aziende", "Consulenza alle imprese", "Consulenza per le imprese che operano nel settore automobilistico. Ne parliamo e capiamo insieme di cosa hai bisogno.",
     ["Un tecnico con vent'anni di esperienza multimarca", "Un confronto su misura per la tua attività"]),
]

FAQ_R = [("Quanto costa il ritiro?", "Niente: ritiro e riconsegna sono sempre gratis, entro 20 km dall'officina."),
         ("Fino a dove arrivi?", f"{ZONA_TESTO[0].upper()}{ZONA_TESTO[1:]}. Se non sei sicuro, chiamami."),
         ("Quanto costa la vettura di cortesia?", CORTESIA_TESTO),
         ("E se la riparazione richiede più giorni?", "Se la vettura di cortesia è libera, resta con te finché il tuo mezzo è pronto. Ti aggiorno io su come va il lavoro."),
         ("Come pago?", "In contanti, con carta o con bancomat, alla riconsegna.")]

# Spazi per le foto: rapporto (larghezza, altezza), foto stock di riserva, alt della foto stock e alt della foto vera.
# sorgente/foto.py ritaglia gli scatti su questi rapporti; appena esiste docs/assets/img/foto/<spazio>.webp
# il generatore usa quella al posto della stock.
FOTO_SLOT = {
    "eroe": ((2, 3), "eroe", "", ""),
    "luca": ((4, 5), "mani", "Foto di esempio: mani di un meccanico al lavoro sul motore", "Luca Miglietta al lavoro nella sua officina"),
    "officina": ((3, 2), "officina", "Foto di esempio: auto e attrezzature in un'officina", "L'interno dell'officina di L.M. Autoservizi a Frassineto Po"),
    "ingresso": ((3, 2), "officina", "Foto di esempio: ambiente di un'officina con auto e ponte sollevatore", "L'ingresso dell'officina di L.M. Autoservizi"),
    "officina-mobile": ((3, 2), "mobile", "Foto di esempio: un intervento sul motore all'aperto", "Luca al lavoro sul mezzo di un cliente, fuori dall'officina"),
    "ritiro": ((3, 2), "ritiro", "Foto di esempio: la consegna delle chiavi di un'auto", "Luca consegna le chiavi della vettura di cortesia"),
    "servizio-meccanica": ((3, 2), "meccanica", "", ""),
    "servizio-elettrauto": ((3, 2), "diagnosi", "", ""),
    "servizio-gommista": ((3, 2), "gomme", "", ""),
    "servizio-carrozzeria": ((3, 2), "riconsegna", "", ""),
    "servizio-diagnosi": ((3, 2), "officina", "", ""),
    "servizio-soccorso": ((3, 2), "mobile", "", ""),
    "servizio-ricambi": ((3, 2), "gomme", "", ""),
    "servizio-allestimenti": ((3, 2), "mobile", "Foto di esempio: un intervento su un mezzo all'aperto", "Il Ford Ranger attrezzato per il campeggio da Luca"),
    # Galleria della pagina Allestimenti: compaiono solo le foto vere (la stock non si mostra mai qui).
    **{f"allestimento-{n}": ((3, 2), "mobile", "", "Un allestimento camping e fuoristrada realizzato da Luca") for n in range(1, 7)},
}
# Dimensioni delle foto stock in docs/assets/img/campione/ (ognuna ha anche la versione -800).
STOCK = {"eroe": (1600, 2400), "officina": (1600, 1067), "mani": (1600, 2400), "meccanica": (1600, 1067),
         "diagnosi": (1600, 1067), "gomme": (1600, 1067), "ritiro": (1600, 1067), "riconsegna": (1600, 2001), "mobile": (1600, 1067)}

ATT = [("qualifica-professionale", "Operatore di riparazioni elettromeccaniche per l'autoveicolo", "Qualifica professionale, 400 ore, 2010"),
       ("responsabile-revisioni", "Responsabile tecnico delle revisioni periodiche", "Attestato di competenza abilitante"),
       ("gas-fluorurati", "Recupero gas fluorurati nei veicoli", "Climatizzatori auto, Reg. CE 307/2008, 2012"),
       ("diploma", "Diploma di liceo scientifico tecnologico", "IIS A. Sobrero, Casale Monferrato, 2009"),
       ("sicurezza-generale", "Sicurezza sul lavoro: formazione generale e specifica", "D.Lgs. 81/2008, 8 ore"),
       ("sicurezza-specifica", "Sicurezza sul lavoro: formazione specifica", "D.Lgs. 81/2008, 4 ore"),
       ("inglese", "Lingua inglese, livello 2", "Attestato di frequenza e profitto, 2011"),
       ("gran-turismo", "Guida di vetture gran turismo", "Puresport")]
