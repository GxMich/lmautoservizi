"""Dati dell'attività usati dal generatore (sorgente/genera.py).
Fonti: biglietto da visita/PDF del cliente e testi già approvati del sito.
I valori None sono dati ancora da chiedere a Luca: il sito li omette e genera.py li elenca in materiali/da-completare.md."""
import os

QUI = os.path.dirname(os.path.abspath(__file__))

DOMINIO = "https://www.lmautoservizi.it"
TEL, TEL_TXT = "+393426436085", "342 643 6085"
WA = "https://wa.me/393426436085?text=Ciao%20Luca%2C%20vorrei%20informazioni."
EMAIL = "lucamiglietta4@gmail.com"
PEC = "lucamiglie@pec.it"
PIVA = "02625920067"
MAPS = "https://maps.app.goo.gl/MKwoz3CKAvCdeNwj8"
# Il biglietto conferma questo indirizzo come sede legale, non come officina.
SEDE_LEGALE = "Via Ticineto 15, 15040 Frassineto Po (AL)"
GEAR = open(os.path.join(QUI, "ingranaggio.txt"), encoding="utf-8").read().strip()
GEAR_PIENO = f"{GEAR} M197 0A197 197 0 1 0 -197 0A197 197 0 1 0 197 0Z"

# Officina: l'indirizzo esatto va confermato da Luca. Frassineto Po ha un solo CAP (15040).
INDIRIZZO_OFFICINA = None          # via e numero civico
CAP_OFFICINA = "15040"
COMUNE_OFFICINA = "Frassineto Po"
PROVINCIA = "AL"
GEO = None                         # (latitudine, longitudine) in gradi decimali
REA = None                         # nella forma "AL-numero"
FACEBOOK = "https://www.facebook.com/L.M.AUTOSERVIZI/"
INSTAGRAM = None
RECENSIONI_GOOGLE = None           # link diretto "scrivi una recensione" della scheda Google
PREZZI = None                      # fascia di prezzo per i dati strutturati, es. "€€"
RECENSIONI_CON_PERMESSO = None     # True quando Luca conferma che le recensioni vengono da Google e chi le ha scritte è d'accordo

# Spiegazione dei dati mancanti: genera.py la stampa per ogni valore rimasto None.
DA_COMPLETARE = {
    "INDIRIZZO_OFFICINA": "via e numero civico dell'officina (il biglietto riporta solo la sede legale): va in Contatti, nel piede e nei dati strutturati per Google.",
    "CAP_OFFICINA": "CAP dell'officina.",
    "GEO": "coordinate dell'officina (latitudine, longitudine), da Google Maps: tasto destro sul punto e clic sui numeri.",
    "REA": "numero REA della Camera di Commercio (visura camerale), da mostrare nel piede accanto alla partita IVA.",
    "INSTAGRAM": "indirizzo del profilo Instagram, se esiste; se non c'è resta None e il sito non lo mostra.",
    "RECENSIONI_GOOGLE": "link diretto «scrivi una recensione» dal Profilo dell'attività su Google (Chiedi recensioni): aggiunge il pulsante sotto le recensioni.",
    "PREZZI": "fascia di prezzo o listino indicativo: per ora il sito non mostra prezzi.",
    "RECENSIONI_CON_PERMESSO": "conferma che le recensioni in home vengono da Google e che gli autori sono d'accordo: con True compare la nota del Codice del Consumo (nota_recensioni).",
}

RECENSIONI = [("Un servizio inimitabile! Ritira la tua auto direttamente da casa tua e te la riporta riparata e sanificata. Stupendo!", "Marco"),
              ("Dovevo fare un cambio gomme e mi sono affidata a LM Autoservizi. Luca è molto gentile e ha fatto un buon lavoro, senza che io gli portassi l'auto.", "Alessia"),
              ("Adoro il suo modo di lavorare, sempre impeccabile, grazie!", "Giacomo")]

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
     ["Un tecnico con esperienza decennale multimarca", "Un confronto su misura per la tua attività"]),
]

FAQ_R = [("Quanto costa il ritiro?", "Dimmi dove si trova l'auto: ti dico subito se e quanto costa, prima di muovermi."),
         ("Fino a dove arrivi?", "Ritiro e riconsegno a Casale Monferrato e nei paesi vicini. Chiama per sapere se passo anche da te."),
         ("Quanto costa la vettura di cortesia?", "Niente: è sempre gratuita. Te la lascio con il pieno, pulita e igienizzata, per tutto il tempo che serve."),
         ("E se la riparazione richiede più giorni?", "La vettura di cortesia resta con te per tutto il tempo della riparazione. Ti aggiorno io sull'avanzamento."),
         ("Come pago?", "In contanti, con carta o con bancomat, alla riconsegna.")]

# Spazi per le foto: rapporto (larghezza, altezza), foto stock di riserva, alt della foto stock e alt della foto vera.
# sorgente/foto.py ritaglia gli scatti su questi rapporti; appena esiste docs/assets/img/foto/<spazio>.webp
# il generatore usa quella al posto della stock.
FOTO_SLOT = {
    "eroe": ((2, 3), "eroe", "", ""),
    "luca": ((4, 5), "mani", "Foto di esempio: mani di un meccanico al lavoro sul motore", "Luca Miglietta al lavoro nella sua officina"),
    "officina": ((3, 2), "officina", "Foto di esempio: auto e attrezzature in un'officina", "L'interno dell'officina di L.M. Autoservizi a Frassineto Po"),
    "ingresso": ((3, 2), "officina", "Foto di esempio: ambiente di un'officina con auto e ponte sollevatore", "L'ingresso dell'officina di L.M. Autoservizi"),
    "officina-mobile": ((3, 2), "mobile", "Foto di esempio: un intervento sul motore all'aperto", "Il furgone dell'officina mobile di L.M. Autoservizi"),
    "ritiro": ((3, 2), "ritiro", "Foto di esempio: la consegna delle chiavi di un'auto", "Luca consegna le chiavi della vettura di cortesia"),
    "servizio-meccanica": ((3, 2), "meccanica", "", ""),
    "servizio-elettrauto": ((3, 2), "diagnosi", "", ""),
    "servizio-gommista": ((3, 2), "gomme", "", ""),
    "servizio-carrozzeria": ((3, 2), "riconsegna", "", ""),
    "servizio-diagnosi": ((3, 2), "officina", "", ""),
    "servizio-soccorso": ((3, 2), "mobile", "", ""),
    "servizio-ricambi": ((3, 2), "gomme", "", ""),
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
