"""Nucleo del sito di L.M. Autoservizi: configurazione, link, icone e pezzi comuni delle pagine.
Il sito è solo in italiano: la versione inglese è stata tolta il 29/10/2026 su richiesta di Luca.

Ogni modulo in sorgente/pagine/ espone costruisci() e scrive le sue pagine così:

    from sito import inizia, scrivi, head, testata, intro, finale, piede, href, ...
    def costruisci():
        inizia("contatti")                      # pagina corrente: id del registro PAGINE
        scrivi(head(titolo, descrizione, [azienda(), briciole()]) + testata() + intro(...) + corpo + finale() + piede())

genera.py chiama costruisci() di ogni modulo.

API per i moduli delle pagine
- Stato: inizia(id). Non importare PAGINA: usare la funzione.
- Testi: attr(testo) per gli attributi HTML.
- Registro: PAGINE {id: (percorso, nome)}; nome(id) dà il nome della pagina.
- Link: href(id, frammento="") relativo alla pagina corrente (sulla stessa pagina diventa "#frammento");
  risorsa("assets/...") per file in docs/; url(id) e URL per gli indirizzi assoluti (canonical, schema).
  Le pagine in ASSOLUTE (la 404) ricevono sempre indirizzi assoluti.
- Contatti: TEL, tel_txt(), wa(), EMAIL, MAPS, indirizzo_officina(); anni_esperienza() per gli anni di lavoro di Luca, abilitazioni() per le sezioni della legge 122/1992.
- Icone: I (interfaccia), ICONE (servizi), VANTAGGI_ICO, veicolo(id).
- Tendina WhatsApp: SERVIZI, EXTRA, dati_servizio(), apri(chiave, testo), apri_servizio(id, testo); scheda() è già nel piede.
- Foto: foto_info(spazio), img(spazio, sizes, ...), foto(spazio, sizes, classe), nota_foto(spazio).
- Pezzi: head(titolo, descrizione, schema=(), immagine="officina", noindex=False), testata(), intro(titolo, testo),
  orari(), spunte(voci), casella(s), griglia_servizi(con_foto=True), sezione_servizi(id, link), finale(titolo=None, testo=None, pulsante=None), piede(extra=""), lightbox() da passare a piede().
- Dati strutturati: azienda(), briciole(nome=None); sito_web() (WebSite) head() lo aggiunge da sé alla home.
  ZONA e zona_servita(): comuni serviti e areaServed; SERVIZI_PAGINE: le pagine dei servizi (catalogo nei dati strutturati, Servizi evidenziato nel menu).
- Testi legali: senza_commenti(html) toglie le note interne <!-- ... --> dei testi di testi_legali.py;
  nota_recensioni() è la nota da mettere sotto le recensioni; slug(testo) dà un id per i titoli.
- Statistiche: STATISTICHE è il codice GoatCounter (variabile LM_GOATCOUNTER) o None; con None il sito non ha statistiche.
- Scrittura: scrivi(html) scrive la pagina corrente in docs/<percorso>/index.html.
- Pacchetti: CSS e JS (tutti i file di sorgente/stile e sorgente/script in ordine di nome), V_CSS e V_JS per la cache."""
import hashlib, json, math, os, posixpath, re, unicodedata
from html import escape
from contenuti import (DOMINIO, TEL, TEL_TXT, WA, EMAIL, PEC, PIVA, MAPS, SCHEDA_GOOGLE, SEDE_LEGALE, GEAR_PIENO, FOTO_SLOT, STOCK, ANNO_INIZIO, ANNI_ESPERIENZA, ABILITAZIONI,
                       INDIRIZZO_OFFICINA, CAP_OFFICINA, COMUNE_OFFICINA, PROVINCIA, GEO, RAGGIO_KM, REA, FACEBOOK, INSTAGRAM, PREZZI, NOLEGGIO_LINK)
import testi_legali

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DOCS = os.path.join(RADICE, "docs")
PRODUZIONE = os.environ.get("LM_PRODUZIONE") == "1"
# In produzione l'indirizzo predefinito è il dominio vero: senza LM_URL canonical, sitemap e schema non puntano più all'anteprima.
URL = os.environ.get("LM_URL", DOMINIO if PRODUZIONE else "https://gxmich.github.io/lmautoservizi/").rstrip("/") + "/"
# Statistiche senza cookie (GoatCounter): spente se LM_GOATCOUNTER manca. Il codice è il nome del sito su goatcounter.com.
STATISTICHE = os.environ.get("LM_GOATCOUNTER", "").strip().lower() or None
if STATISTICHE and not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,62}", STATISTICHE):
    raise SystemExit(f"LM_GOATCOUNTER non valido: {STATISTICHE!r} (serve solo il codice, per esempio lmautoservizi)")

# Registro delle pagine: id -> (percorso dalla radice del sito, nome).
PAGINE = {
    "home": ("", "Home"),
    "servizi": ("servizi/", "Servizi"),
    "meccanica": ("servizi/meccanica/", "Meccanica"),
    "elettrauto": ("servizi/elettrauto/", "Elettrauto"),
    "gommista": ("servizi/gommista/", "Gommista"),
    "carrozzeria": ("servizi/carrozzeria/", "Carrozzeria"),
    "diagnosi": ("servizi/diagnosi-e-pre-revisione/", "Diagnosi e pre-revisione"),
    "allestimenti": ("servizi/allestimenti-camping-fuoristrada/", "Allestimenti camping e fuoristrada"),
    "officina": ("officina/", "L'officina"),
    "ritiro": ("ritiro-e-consegna/", "Ritiro e consegna"),
    "mobile": ("assistenza-a-domicilio/", "Assistenza a domicilio"),
    "gomme": ("gomme-e-ricambi/", "Gomme e ricambi"),
    "chi": ("chi-sono/", "Chi sono"),
    "contatti": ("contatti/", "Contatti"),
    "privacy": ("privacy/", "Privacy e cookie"),
    "condizioni": ("garanzia-e-condizioni/", "Garanzia e condizioni"),
    "404": ("404.html", "Pagina non trovata"),
}
# Menu: officina, ritiro e domicilio alla pari (Luca, 29/10/2026). NAV_NOMI accorcia le voci lunghe; il menu del telefono ha anche Home e Chi sono.
# Menu a cinque voci (scelta dell'utente, 29/10/2026): ritiro e domicilio stanno in una voce sola, che porta al ritiro
# e resta evidenziata anche nella pagina del domicilio. Home è il marchio, Chi sono sta nel piede. Lo stesso menu sul telefono.
NAV = ["servizi", "officina", "ritiro", "gomme", "contatti"]
NAV_NOMI = {"ritiro": "Ritiro e domicilio"}
NAV_ANCHE = {"ritiro": ["mobile"]}
MENU = NAV
# Piede: una colonna con le pagine dei servizi, una con il resto (le pagine legali stanno nella riga in fondo).
PIEDE_OFFICINA = ["officina", "ritiro", "mobile", "gomme", "chi", "contatti"]
ASSOLUTE = {"404"}          # servite a indirizzi qualsiasi: link e risorse assoluti
NON_INDICIZZATE = {"404"}   # fuori dalla sitemap, sempre noindex
# Le pagine dei servizi principali (sotto servizi/): catalogo nei dati strutturati
SERVIZI_PAGINE = ["meccanica", "elettrauto", "gommista", "carrozzeria", "diagnosi", "allestimenti"]
# Comuni serviti (dati strutturati e llms.txt): i principali entro RAGGIO_KM in linea d'aria dall'officina (calcolati il 29/10/2026)
ZONA = ["Frassineto Po", "Casale Monferrato", "Valenza", "Ticineto", "Borgo San Martino", "Valmacca", "Occimiano", "Giarole",
        "Villanova Monferrato", "Mirabello Monferrato", "San Salvatore Monferrato", "Pomaro Monferrato", "Bozzole", "Terruggia",
        "Balzola", "Breme", "Candia Lomellina", "Sartirana Lomellina", "Mede"]

# Stato: la pagina che si sta costruendo.
PAGINA = None
SCRITTE, FILE_SCRITTI = [], set()


def inizia(pagina):
    """Pagina corrente: da qui in poi link e risorse sono relativi alla sua cartella."""
    global PAGINA
    if pagina not in PAGINE:
        raise KeyError(f"pagina non registrata in PAGINE: {pagina}")
    PAGINA = pagina


def attr(testo):
    return escape(testo, quote=True)


def nome(pagina):
    return PAGINE[pagina][1]


# ---------------------------------------------------------------- testi legali
def senza_commenti(html):
    """Toglie i commenti HTML (le note interne "DA VERIFICARE" e "OPZIONALE" dei testi legali): non devono finire nel sorgente pubblicato."""
    return re.sub(r"[ \t]*<!--.*?-->[ \t]*\n?", "", html, flags=re.S)


def slug(testo):
    """Id per un titolo: minuscole senza accenti né tag, parole unite da trattini ("Promemoria e offerte: solo se mi dici SÌ" -> promemoria-e-offerte-solo-se-mi-dici-si)."""
    testo = unicodedata.normalize("NFKD", re.sub(r"<[^>]+>", "", testo)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", testo.lower()).strip("-") or "sezione"


def nota_recensioni():
    """Nota sotto le recensioni (Codice del Consumo, art. 22, comma 5-bis) come <p class="piccolo">."""
    nota = senza_commenti(testi_legali.RECENSIONI_NOTA_IT).strip()
    return nota.replace("<p>", '<p class="piccolo nota-recensioni">')


# ---------------------------------------------------------------- indirizzi
def percorso(pagina):
    """Percorso della pagina dalla radice di docs/, per esempio servizi/meccanica/."""
    return PAGINE[pagina][0]


def url(pagina=None):
    """Indirizzo pubblico assoluto della pagina (canonical, sitemap, schema)."""
    return URL + percorso(pagina or PAGINA)


def _relativo(destinazione):
    """Da un percorso dalla radice di docs/ al link relativo alla cartella della pagina corrente."""
    if PAGINA in ASSOLUTE:
        return URL + destinazione
    cartella = posixpath.dirname(percorso(PAGINA)) or "."
    r = posixpath.relpath(destinazione.rstrip("/") or ".", cartella)
    if destinazione == "" or destinazione.endswith("/"):
        return "./" if r == "." else r + "/"
    return r


def href(pagina, frammento=""):
    if frammento and pagina == PAGINA and PAGINA not in ASSOLUTE:
        return "#" + frammento
    return _relativo(percorso(pagina)) + ("#" + frammento if frammento else "")


def risorsa(file):
    """File dentro docs/, per esempio risorsa("assets/img/favicon-32.png")."""
    return _relativo(file)


def anni_esperienza():
    """Gli anni di esperienza di Luca: il numero della generazione, che 00-base.js ricalcola nel browser ogni anno."""
    return f'<span data-anni-da="{ANNO_INIZIO}">{ANNI_ESPERIENZA}</span>'


def abilitazioni():
    """"meccatronica, carrozzeria e gommista": le sezioni dell'abilitazione di autoriparazione, per i testi."""
    return ", ".join(ABILITAZIONI[:-1]) + " e " + ABILITAZIONI[-1]


def tel_txt():
    return TEL_TXT


def wa():
    return WA


def indirizzo_officina():
    """Indirizzo dell'officina con i soli dati noti: senza via resta "Frassineto Po (AL)"."""
    luogo = f"{COMUNE_OFFICINA} ({PROVINCIA})"
    if INDIRIZZO_OFFICINA:
        return f"{INDIRIZZO_OFFICINA}, {CAP_OFFICINA + ' ' if CAP_OFFICINA else ''}{luogo}"
    return luogo


# ---------------------------------------------------------------- icone (disegnate per questo sito)
def svg(corpo, classe="", vb="0 0 24 24"):
    return f'<svg class="ico {classe}" viewBox="{vb}" aria-hidden="true" focusable="false">{corpo}</svg>'


def punti_cerchio(cx, cy, r1, r2, n, inizio=0):
    righe = []
    for k in range(n):
        a = math.radians(inizio + k * 360 / n)
        righe.append(f"M{cx + r1 * math.cos(a):.2f} {cy + r1 * math.sin(a):.2f}L{cx + r2 * math.cos(a):.2f} {cy + r2 * math.sin(a):.2f}")
    return "".join(righe)


I = {
    "tel": svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'),
    "chat": svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.5 8.5 0 1 1 21 11.5z"/>'),
    "mail": svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
    "check": svg('<path d="m5 12.5 4.5 4.5L19 7.5"/>'),
    "freccia": svg('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "giu": svg('<path d="M12 5v14M6 13l6 6 6-6"/>'),
    "chiudi": svg('<path d="M6 6l12 12M18 6 6 18"/>'),
    "esterno": svg('<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>'),
    "sole": svg(f'<circle cx="12" cy="12" r="4.2"/><path d="{punti_cerchio(12, 12, 7, 9.4, 8)}"/>', "ico-sole"),
    "luna": svg('<path d="M20.5 14.3A8.5 8.5 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8z"/>', "ico-luna"),
}

# Servizi: tratto unico, un dettaglio pieno; ogni icona ha la sua piccola animazione (vedi stile/00-base.css).
_gomma = (f'<g class="gira"><circle cx="12" cy="12" r="9.5"/><circle cx="12" cy="12" r="5.6"/>'
          f'<path d="{punti_cerchio(12, 12, 8.1, 9.5, 12)}{punti_cerchio(12, 12, 2.3, 5.6, 5, -90)}"/>'
          f'<circle class="pieno" cx="12" cy="12" r="1.7"/></g>')
ICONE = {
    "meccanica": svg('<path class="chiave" d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'
                     '<path class="dado" d="M19.8 16.25 21.1 18.5 19.8 20.75H17.2L15.9 18.5 17.2 16.25Z"/><circle class="pieno dado" cx="18.5" cy="18.5" r="1"/>', "ico-meccanica"),
    "elettrauto": svg('<rect x="2.5" y="7" width="19" height="13" rx="2.2"/><path d="M6.5 7V4.8h3V7M14.5 7V4.8h3V7M5.6 10.6h2.6M15.8 10.6h2.6M17.1 9.3v2.6"/>'
                      '<path class="pieno fulmine" d="M12.9 9.4 9.6 14.2h2.6l-.9 4.4 3.3-5h-2.6z"/>', "ico-elettrauto"),
    "gommista": svg(_gomma, "ico-gommista"),
    "ricambi": svg('<path d="M4 7.5 12 3l8 4.5v9L12 21l-8-4.5z"/><path d="M4.5 7.8 12 12l7.5-4.2M12 12v8.5"/><path class="pieno" d="M10 8h4v4h-4z"/>', "ico-ricambi"),
    "carrozzeria": svg('<path d="M2.6 19.4v-2.6c0-.8.5-1.5 1.3-1.8l2.2-.8 2.6-3.3c.4-.5 1-.8 1.6-.8h4.3c.6 0 1.2.3 1.6.7l3 3.3 1.8.4c.9.2 1.5 1 1.5 1.9v3"/>'
                       '<path d="M2.6 19.4h1.7M9.1 19.4h5.6M19.6 19.4h2.9M7 14.3h11.8M12.4 10.9v3.4"/><circle cx="6.7" cy="19.6" r="2.3"/><circle cx="17.2" cy="19.6" r="2.3"/>'
                       '<path class="pieno scintilla" d="M19.5 1.6l.75 1.85 1.85.75-1.85.75-.75 1.85-.75-1.85-1.85-.75 1.85-.75z"/>', "ico-carrozzeria"),
    "diagnosi": svg('<path class="spia" d="M6.5 9.5h3L11 8h3.5l1 1.5H18v2h1.5v-2H21V18h-1.5v-2.5H18V18h-3.5L13 19.5H8.5l-2-2z"/>'
                    '<path d="M10.5 5h4M12.5 5v3M3 10.5v6M3 13.5h3.5"/>', "ico-diagnosi"),
    "soccorso": svg('<path d="m2.5 10 9.5-7.5 9.5 7.5M5.5 8v12h13V8M9 20v-6h6v6"/>', "ico-domicilio"),
    "aziende": svg('<rect x="3" y="7.5" width="18" height="12.5" rx="2"/><path d="M8.5 7.5V5.8c0-1 .8-1.8 1.8-1.8h3.4c1 0 1.8.8 1.8 1.8v1.7M3 12.5h18"/>'
                   '<path class="pieno" d="M10.8 11.3h2.4v2.4h-2.4z"/>', "ico-aziende"),
    "allestimenti": svg('<path d="M2.6 19.4v-3.1c0-.8.6-1.5 1.4-1.6l2.9-.4 2.3-3.4c.3-.4.8-.7 1.3-.7h3.1v4.1h6.9c.8 0 1.5.7 1.5 1.5v3.6"/>'
                        '<path d="M2.6 19.4h1.8M9.1 19.4h6.2M19.7 19.4h1.8"/><circle cx="6.8" cy="19.6" r="2.3"/><circle cx="17.5" cy="19.6" r="2.3"/>'
                        '<path d="M14.3 14.3V8.9l3.3-4.4 3.9 4.4v5.4"/><path class="pieno tenda" d="M17.6 9.6l1.6 1.9v2.8h-3.2v-2.8z"/>', "ico-allestimenti"),
    "acquisto": svg('<circle cx="10.5" cy="10.5" r="6.8"/><path d="m15.4 15.4 5.3 5.3"/><path class="spunta" d="m7.6 10.7 2 2 3.8-3.9"/>', "ico-acquisto"),
    "noleggio": svg('<circle cx="8" cy="15.6" r="4.6"/><path d="m11.3 12.3 8.4-8.4M16.6 6.9l2.6 2.6M14.3 9.2l2 2"/><circle class="pieno" cx="8" cy="15.6" r="1.4"/>', "ico-noleggio"),
    "altro": svg('<circle cx="12" cy="12" r="9.5"/><path d="M9.3 9.3a2.8 2.8 0 1 1 3.9 2.6c-.7.3-1.2 1-1.2 1.8v.6"/><circle class="pieno" cx="12" cy="17.2" r="1"/>', "ico-altro"),
}
# Vantaggi (si disegnano a tratto entrando nello schermo)
VANTAGGI_ICO = {
    "cortesia": svg('<path d="M2.6 18.4v-2.6c0-.8.5-1.5 1.3-1.8l2.2-.8 2.6-3.3c.4-.5 1-.8 1.6-.8h4.3c.6 0 1.2.3 1.6.7l3 3.3 1.8.4c.9.2 1.5 1 1.5 1.9v3"/>'
                    '<path d="M2.6 18.4h1.7M9.1 18.4h5.6M19.6 18.4h2.9M7 13.3h11.8M12.4 9.9v3.4"/><circle cx="6.7" cy="18.6" r="2.3"/><circle cx="17.2" cy="18.6" r="2.3"/>'),
    "rotta": svg('<circle cx="5.5" cy="18.5" r="2.2"/><circle cx="18.5" cy="5.5" r="2.2"/><path d="M7.7 18.5h8.1a3.2 3.2 0 0 0 0-6.4H8.2a3.2 3.2 0 0 1 0-6.4h8.1"/>'),
    "mobile": svg('<path d="M2 17V7.5C2 6.7 2.7 6 3.5 6H14v11"/><path d="M14 9.5h4.2c.4 0 .8.2 1 .5l2.5 3.5c.2.2.3.5.3.8V17h-1.8M8.5 17h7.2"/>'
                  f'<circle cx="6.5" cy="17.5" r="2"/><circle cx="17.7" cy="17.5" r="2"/><circle cx="8" cy="11.3" r="1.6"/><path d="{punti_cerchio(8, 11.3, 2.5, 3.4, 6, -90)}"/>'),
    "aziende": svg('<rect x="3" y="7.5" width="18" height="12.5" rx="2"/><path d="M8.5 7.5V5.8c0-1 .8-1.8 1.8-1.8h3.4c1 0 1.8.8 1.8 1.8v1.7M3 12.5h18M10.8 11.3h2.4v2.4h-2.4z"/>'),
}


def ruota(cx, r, cy):
    return f'<g class="ruota"><circle cx="{cx}" cy="{cy}" r="{r}"/><circle class="pieno" cx="{cx}" cy="{cy}" r="1.6"/></g>'


# Sagome laterali dei mezzi: tratto pieno, pochi dettagli, tutte appoggiate sulla stessa linea di terra (y = 32).
VEICOLI = {
    "auto": ('<path d="M6 27.4V22.8c0-1.5 1-2.8 2.4-3.2L15.2 17.6l6.1-5.6c.8-.7 1.8-1.1 2.9-1.1h11.6c1.2 0 2.3.5 3.1 1.3l5.9 5.6 9.4 1.6c2 .3 3.5 2.1 3.5 4.1v3.9"/>'
             '<path d="M6 27.4h4.9M22.1 27.4h19.8M53.1 27.4h4.6"/>'
             '<path d="M18.6 17.6l4.1-3.8c.5-.4 1.1-.7 1.8-.7H31v4.5zM33.6 13.1h2.7c.7 0 1.3.3 1.8.7l4.1 3.8h-8.6z"/>'
             + ruota(16.5, 4.6, 27.4) + ruota(47.5, 4.6, 27.4)),
    "fuoristrada": ('<path d="M5.5 26.7V9.6c0-1.4 1.1-2.5 2.5-2.5h28.9c.8 0 1.6.4 2.1 1l5.6 7.2 9.1 1.3c1.9.3 3.3 1.9 3.3 3.8v6.3"/>'
                    '<path d="M5.5 26.7h4.2M22.3 26.7h18.4M53.3 26.7h3.7M12 4.4h21M14.5 4.4v2.7M30.5 4.4v2.7"/>'
                    '<path d="M11 10.6h8.5a1 1 0 0 1 1 1v2.7a1 1 0 0 1-1 1H11a1 1 0 0 1-1-1v-2.7a1 1 0 0 1 1-1zM23.5 10.6h11.2c.5 0 .9.2 1.2.6l3.3 4.1H23.5z"/>'
                    + ruota(16, 5.3, 26.7) + ruota(47, 5.3, 26.7)),
    "pickup": ('<path d="M5 26.7V16.5h25V10c0-1.1.9-2 2-2h9.6c.7 0 1.4.4 1.7 1l4.2 7.5 8.3 1.3c1.9.3 3.2 1.9 3.2 3.8v5.1"/>'
               '<path d="M5 26.7h5.5M21.1 26.7h21.2M53 26.7h4M5 19.6h25"/>'
               '<path d="M33.6 10.8h6.6c.4 0 .8.2 1 .6l3 5.1H33.6z"/>'
               + ruota(15.8, 5.1, 26.7) + ruota(47.6, 5.1, 26.7)),
    "furgone": ('<path d="M5 27.4V9.4C5 8 6.1 6.9 7.5 6.9h29.7c1.1 0 2.1.5 2.7 1.4l5.9 8.6 7.6 1.7c1.8.4 3.1 2 3.1 3.9v4.9"/>'
                '<path d="M5 27.4h4.9M21.1 27.4h20.8M53.1 27.4h3.4M24 9.4v15"/>'
                '<path d="M38.8 10.6h.4c.5 0 .9.2 1.2.6l3.6 5.7h-5.2z"/>'
                + ruota(15.5, 4.6, 27.4) + ruota(47.5, 4.6, 27.4)),
    "camper": ('<path d="M5 27.4V7c0-1.1.9-2 2-2h37.6c1.1 0 2 .9 2 2v4.6h-5.4v1.6h4.2c.6 0 1.1.3 1.5.7l3.9 4.9 2.9.7c1.6.4 2.7 1.8 2.7 3.4v4.5"/>'
               '<path d="M5 27.4h4.9M21.1 27.4h21.3M53.6 27.4h2.8"/>'
               '<path d="M10.8 9.6h9.4a1.2 1.2 0 0 1 1.2 1.2v3.2a1.2 1.2 0 0 1-1.2 1.2h-9.4a1.2 1.2 0 0 1-1.2-1.2v-3.2a1.2 1.2 0 0 1 1.2-1.2zM42 16h2.4c.4 0 .8.2 1 .5l2.2 2.8H42z"/>'
               + ruota(15.5, 4.6, 27.4) + ruota(48, 4.6, 27.4)),
    "ciclomotore": ('<g transform="translate(0 3)">'
                    '<path d="M7.5 21c0-5 3.6-8.5 9-8.5H27c.8 0 1.5.7 1.5 1.5v2.5c0 2.5-1.8 4.5-4.3 4.5h-4.4a5.5 5.5 0 0 0-7.6 0z"/>'
                    '<path d="M15 12.5c.4-1.7 1.7-2.8 3.5-2.8h7.5c.8 0 1.5.7 1.5 1.5v1.3"/>'
                    '<path d="M24.2 21h13.3c1.8-3.8 3.2-8.4 4-13.5M38.5 6.5h6.5M42 8l5 16.5M43.4 19.6c1.9-1.3 4.6-1.3 6.6.2"/>'
                    + ruota(16, 4, 25) + ruota(47, 4, 25) + '</g>'),
    "altro": ('<circle cx="32" cy="18.5" r="12"/><path d="M28.4 15a3.7 3.7 0 1 1 5.2 3.4c-.9.4-1.6 1.3-1.6 2.3v.9"/>'
              '<circle class="pieno" cx="32" cy="25.6" r="1.4"/>'),
}
# (id, nome, valore per il messaggio, aiuto sotto le note)
MEZZI = [("auto", "Auto", "Auto",
          "Marca e modello aiutano, per esempio Fiat Panda 2015."),
         ("fuoristrada", "Fuoristrada", "Fuoristrada",
          "Marca e modello aiutano, per esempio Suzuki Jimny 2019."),
         ("furgone", "Furgone", "Furgone",
          "Marca e modello aiutano, per esempio Fiat Ducato 2017."),
         ("pickup", "Pick-up", "Pick-up",
          "Marca e modello aiutano, per esempio Ford Ranger 2020."),
         ("camper", "Camper", "Camper",
          "Marca e modello aiutano, per esempio mansardato su Ducato, 2016."),
         ]
# Mezzi che la tendina propone: quelli di base, o quelli del servizio (allestimenti: furgoni, pick-up e camper, come dice Luca).
MEZZI_BASE = "auto,fuoristrada,furgone,camper"
MEZZI_SERVIZIO = {"allestimenti": "furgone,pickup,camper"}


def veicolo(chi):
    return svg(VEICOLI[chi], f"veicolo veicolo--{chi}", "0 0 64 36")


# ---------------------------------------------------------------- servizi (le caselle della home e la tendina)
# (id, nome, descrizione breve, suggerimento per le note, opzioni)
SERVIZI = [
    ("meccanica", "Meccanica",
     "Tagliandi, riparazioni, manutenzione ordinaria e straordinaria",
     "Es. tagliando, rumore in frenata, perdita d'olio.", ""),
    ("elettrauto", "Elettrauto",
     "Avviamento, batteria e ricarica, luci, climatizzatore",
     "Es. non parte, la batteria si scarica, il clima non raffredda.", ""),
    ("gommista", "Gommista",
     "Cambio, equilibratura, convergenza, deposito e vendita di pneumatici",
     "Es. cambio stagionale o foratura. La misura è scritta sul fianco della gomma.", ""),
    ("carrozzeria", "Carrozzeria",
     "Carrozzeria, verniciatura e saldatura",
     "Es. urto sul paraurti, graffio sulla portiera. Le foto del danno puoi mandarmele su WhatsApp.", ""),
    ("diagnosi", "Diagnosi e pre-revisione",
     "Spie accese, centraline, controllo gratuito prima della revisione",
     "Es. spia del motore accesa, revisione in scadenza a marzo.", ""),
    ("soccorso", "Assistenza a domicilio",
     "Auto ferma? Batteria, diagnosi e gomma bucata: arrivo io",
     "Dimmi dove si trova il mezzo e di che intervento hai bisogno.", ""),
    ("ricambi", "Gomme e ricambi",
     "Ricambi, gomme, lubrificanti e accessori: chiedimi disponibilità e prezzo",
     "Scrivimi marca, modello e anno del mezzo; per le gomme, anche la misura.", "vendita"),
    ("allestimenti", "Allestimenti camping e fuoristrada",
     "Furgoni, pick-up e camper: progettati e costruiti da me",
     "Dimmi che mezzo hai e cosa vorresti realizzare.", ""),
    ("acquisto", "Consulenza acquisto auto",
     "Controllo dell'usato prima di comprarlo e consigli sulla scelta",
     "Mandami il link dell'annuncio, oppure marca, modello, anno e chilometri.", ""),
]
# Pagina di approfondimento di ogni servizio (id del registro PAGINE)
PAGINA_SERVIZIO = {"meccanica": "meccanica", "elettrauto": "elettrauto", "gommista": "gommista", "carrozzeria": "carrozzeria",
                   "diagnosi": "diagnosi", "soccorso": "mobile", "ricambi": "gomme", "allestimenti": "allestimenti", "acquisto": "servizi"}
# Richieste che non sono caselle: (nome, suggerimento, opzioni, titolo della tendina)
EXTRA = {
    "ritiro": ("Ritiro e consegna",
               "Dove si trova il mezzo e cosa non va. Entro 20 km da Frassineto Po il ritiro è gratis.", "", None),
    "aziende": ("Consulenza alle imprese",
                "Che attività hai e di cosa avresti bisogno.", "senza-mezzo", None),
    "altro": ("Non so quale sia il problema",
              "Raccontami cosa fa il mezzo: rumori, spie accese, quando succede.", "",
              "Descrivimi il problema"),
}


def dati_servizio(nome, nota, opzioni="", titolo=None, mezzi=None):
    """Attributi della tendina: nome del servizio, suggerimento per le note, opzioni e titolo se diverso dal nome."""
    a = f'aria-haspopup="dialog" data-servizio="{attr(nome)}" data-nota="{attr(nota)}"'
    if titolo:
        a += f' data-titolo="{attr(titolo)}"'
    if mezzi:
        a += f' data-mezzi="{mezzi}"'
    if "senza-mezzo" in opzioni:
        a += " data-senza-mezzo"
    if "vendita" in opzioni:
        a += " data-vendita"
    return a


def apri(chiave, testo, classe="btn btn--arancio", icona="freccia"):
    nome, nota, opzioni, titolo = EXTRA[chiave]
    return f'<button type="button" class="{classe}" {dati_servizio(nome, nota, opzioni, titolo)}>{testo} {I[icona] if icona else ""}</button>'


def apri_servizio(chi, testo, classe="btn btn--arancio"):
    s = next(x for x in SERVIZI if x[0] == chi)
    return f'<button type="button" class="{classe}" {dati_servizio(s[1], s[3], s[4], mezzi=MEZZI_SERVIZIO.get(chi))}>{testo} {I["freccia"]}</button>'


# ---------------------------------------------------------------- foto
def foto_info(spazio):
    """(percorso senza estensione dalla radice di docs/, larghezza, altezza, alt, è stock)."""
    (rw, rh), stock, alt_stock, alt_vero = FOTO_SLOT[spazio]
    if os.path.exists(os.path.join(DOCS, "assets", "img", "foto", spazio + ".webp")):
        return "assets/img/foto/" + spazio, 1600, round(1600 * rh / rw), alt_vero, False
    w, h = STOCK[stock]
    return "assets/img/campione/" + stock, w, h, alt_stock, True


def img(spazio, sizes, lazy=True, alt=None, priorita=False, piccola=False):
    base, w, h, alt_def, _ = foto_info(spazio)
    testo_alt = attr(alt_def if alt is None else alt)
    grande, media = risorsa(base + ".webp"), risorsa(base + "-800.webp")
    if piccola:
        return f'<img src="{media}" width="800" height="{round(800 * h / w)}" alt="{testo_alt}" loading="lazy" decoding="async">'
    carica = ' fetchpriority="high"' if priorita else (' loading="lazy" decoding="async"' if lazy else "")
    return (f'<img src="{grande}" srcset="{media} 800w, {grande} {w}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{testo_alt}"{carica}>')


def nota_foto(spazio):
    return f'<span class="nota-foto">Foto di esempio</span>' if foto_info(spazio)[4] else ""


def foto(spazio, sizes, classe="foto", iride=True):
    return f'<figure class="{classe}"{" data-iride" if iride else ""}>{img(spazio, sizes)}{nota_foto(spazio)}</figure>'


def ci_sono_foto_stock():
    return any(foto_info(s)[4] for s in FOTO_SLOT)


# ---------------------------------------------------------------- dati strutturati
def zona_servita():
    """areaServed: i comuni di ZONA e, con le coordinate, il cerchio di RAGGIO_KM attorno all'officina."""
    zona = [{"@type": "City", "name": comune} for comune in ZONA]
    if GEO:
        zona.append({"@type": "GeoCircle", "geoMidpoint": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
                     "geoRadius": RAGGIO_KM * 1000})
    return zona


def azienda():
    """AutoRepair per Google e per gli assistenti di ricerca. Niente Review né AggregateRating: le recensioni
    pubblicate dall'officina stessa non danno stelle e Google le considera autoreferenziali."""
    indirizzo = {"@type": "PostalAddress", "streetAddress": INDIRIZZO_OFFICINA, "addressLocality": COMUNE_OFFICINA,
                 "postalCode": CAP_OFFICINA, "addressRegion": PROVINCIA, "addressCountry": "IT"}
    descrizioni = {s[0]: s[2] for s in SERVIZI}
    descrizioni.update({"ritiro": "Ritiro e riconsegna del mezzo, gratis entro 20 km dall'officina",
                        "mobile": descrizioni["soccorso"], "gomme": descrizioni["ricambi"]})
    # Nel catalogo anche ritiro, domicilio e gomme e ricambi: sono i servizi che distinguono l'officina.
    catalogo = [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": nome(p), "url": url(p),
                                                    **({"description": descrizioni[p]} if p in descrizioni else {})}}
                for p in SERVIZI_PAGINE + ["ritiro", "mobile", "gomme"]]
    dati = {"@context": "https://schema.org", "@type": "AutoRepair", "@id": URL + "#azienda",
            "name": "L.M. Autoservizi di Miglietta Luca",
            "alternateName": "L.M. Autoservizi",
            "description": "Officina multimarca a Frassineto Po: meccanica, elettrauto, gommista, carrozzeria, diagnosi centraline e pre-revisione. Ritiro e consegna gratis entro 20 km, assistenza a domicilio, vettura di cortesia gratuita.",
            "url": url("home"), "telephone": TEL, "email": EMAIL, "vatID": "IT" + PIVA,
            "logo": URL + "assets/img/favicon-192.png",
            "founder": {"@type": "Person", "name": "Luca Miglietta"},
            "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Abilitazione di autoriparazione (legge 122/1992)",
                               "name": f"Autoriparazione: {sezione}"} for sezione in ABILITAZIONI],
            "address": {k: v for k, v in indirizzo.items() if v},
            "hasMap": SCHEDA_GOOGLE,
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:30", "closes": "19:30"}],
            "paymentAccepted": "Contanti, carta di credito, bancomat",
            "currenciesAccepted": "EUR",
            "areaServed": zona_servita(),
            "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servizi dell'officina", "itemListElement": catalogo}}
    if GEO:
        dati["geo"] = {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]}
    if PREZZI:
        dati["priceRange"] = PREZZI
    # La foto dell'officina solo quando è vera: una foto di esempio nei dati per Google sarebbe ingannevole.
    officina, *_, officina_stock = foto_info("officina")
    if not officina_stock:
        dati["image"] = URL + officina + ".webp"
    dati["sameAs"] = [SCHEDA_GOOGLE] + [p for p in (FACEBOOK, INSTAGRAM) if p]
    return dati


def briciole(nome_pagina=None):
    """Percorso Home > (pagina madre) > pagina corrente, ricavato dalle cartelle del registro."""
    voci, cartella = [PAGINA], PAGINE[PAGINA][0].rstrip("/")
    while "/" in cartella:
        cartella = cartella.rsplit("/", 1)[0]
        madre = next((p for p, (perc, _) in PAGINE.items() if perc == cartella + "/"), None)
        if madre:
            voci.insert(0, madre)
    voci.insert(0, "home")
    elementi = [{"@type": "ListItem", "position": i + 1, "name": nome(p), "item": url(p)} for i, p in enumerate(voci)]
    if nome_pagina:
        elementi[-1]["name"] = nome_pagina
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elementi}


def sito_web():
    """WebSite: head() lo aggiunge da solo ai dati strutturati della home."""
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": url("home") + "#sito",
            "name": "L.M. Autoservizi di Miglietta Luca", "alternateName": "L.M. Autoservizi",
            "url": url("home"), "inLanguage": "it", "publisher": {"@id": URL + "#azienda"}}


# ---------------------------------------------------------------- pacchetti CSS e JS
def pacchetto(cartella, estensione):
    """Tutti i file di sorgente/<cartella> con quell'estensione, in ordine di nome, uniti in un solo testo."""
    nomi = sorted(f for f in os.listdir(os.path.join(QUI, cartella)) if f.endswith(estensione))
    return "\n".join(open(os.path.join(QUI, cartella, f), encoding="utf-8").read() for f in nomi)


CSS, JS = pacchetto("stile", ".css"), pacchetto("script", ".js")
V_CSS, V_JS = (hashlib.sha256(x.encode("utf-8")).hexdigest()[:10] for x in (CSS, JS))


# ---------------------------------------------------------------- pezzi comuni
def head(titolo, descrizione, schema=(), immagine="officina", noindex=False):
    indirizzo = url()
    base, w, h, alt, stock = foto_info(immagine)
    # In produzione l'anteprima social usa solo foto vere: con una foto di esempio niente immagine (si vede il logo del sito).
    if PRODUZIONE and stock:
        anteprima = '<meta name="twitter:card" content="summary">'
    else:
        anteprima = (f'<meta property="og:image" content="{URL + base}.webp">\n<meta property="og:image:width" content="{w}">\n'
                     f'<meta property="og:image:height" content="{h}">\n'
                     f'<meta property="og:image:alt" content="{attr(alt or "L.M. Autoservizi, officina a Frassineto Po")}">\n'
                     '<meta name="twitter:card" content="summary_large_image">')
    noindex = noindex or PAGINA in NON_INDICIZZATE
    robots = f'<link rel="canonical" href="{indirizzo}">' if PRODUZIONE and not noindex else '<meta name="robots" content="noindex, nofollow">'
    schema = list(schema)
    if PAGINA == "home" and not any(s.get("@type") == "WebSite" for s in schema):
        schema.append(sito_web())
    # "</" dentro una stringa JSON chiuderebbe lo <script>: si scrive "<\/", che resta JSON valido
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False).replace("</", "<\\/")}</script>\n' for s in schema)
    if STATISTICHE:  # statistiche senza cookie: lo script conta la pagina, 40-statistiche.js i clic su Chiama e WhatsApp
        ld += f'<script data-goatcounter="https://{STATISTICHE}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n'
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titolo}</title>
<meta name="description" content="{attr(descrizione)}">
{robots}
<meta name="theme-color" content="#0b0d10">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="L.M. Autoservizi di Miglietta Luca">
<meta property="og:title" content="{attr(titolo)}">
<meta property="og:description" content="{attr(descrizione)}">
<meta property="og:url" content="{indirizzo}">
{anteprima}
<link rel="icon" type="image/png" sizes="32x32" href="{risorsa("assets/img/favicon-32.png")}">
<link rel="icon" type="image/png" sizes="192x192" href="{risorsa("assets/img/favicon-192.png")}">
<link rel="apple-touch-icon" href="{risorsa("assets/img/favicon-180.png")}">
<link rel="manifest" href="{risorsa("site.webmanifest")}">
<script>(function(d){{d.classList.add("js");try{{if(localStorage.getItem("lm-tema")==="chiaro"){{d.setAttribute("data-tema","chiaro");document.querySelector('meta[name="theme-color"]').content="#f3f4f6"}}}}catch(e){{}}try{{if(!matchMedia("(prefers-reduced-motion: reduce)").matches)d.classList.add("mo")}}catch(e){{}}setTimeout(function(){{d.classList.remove("mo")}},1500)}})(document.documentElement);</script>
<link rel="preload" href="{risorsa("assets/fonts/archivo-latin.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{risorsa("assets/sito.css")}?v={V_CSS}">
{ld}</head>
<body class="p-{PAGINA}">
<a class="salta-link" href="#contenuto">Vai al contenuto</a>
'''


def corrente(pagina):
    """aria-current di una voce di menu: "page" sulla pagina stessa, "true" sulla sezione che la contiene
    (Servizi è evidenziato anche in servizi/meccanica/ e nelle altre pagine dei servizi)."""
    if pagina == PAGINA:
        return ' aria-current="page"'
    if PAGINA in NAV_ANCHE.get(pagina, []):
        return ' aria-current="true"'
    cartella = PAGINE[pagina][0]
    if PAGINA and cartella.endswith("/") and PAGINE[PAGINA][0].startswith(cartella):
        return ' aria-current="true"'
    return ""


def testata():
    def voci(lista, freccia=""):
        return "".join(f'<li><a href="{href(p)}"{corrente(p)}><span>{NAV_NOMI.get(p, nome(p))}</span>{freccia}</a></li>' for p in lista)
    etichetta_tema = "Passa al tema chiaro"
    return f'''<header class="testata">
  <div class="wrap testata-riga">
    <a class="marchio" href="{href("home")}"><img src="{risorsa("assets/img/logo-arancio-84.png")}" width="40" height="40" alt=""><span>L.M. Autoservizi<small>Officina a Frassineto Po</small></span></a>
    <nav class="nav" aria-label="Principale"><ul>{voci(NAV)}</ul></nav>
    <div class="testata-azioni">
      <button class="tema-bottone" type="button" data-tema-bottone aria-label="{etichetta_tema}">{I["sole"]}{I["luna"]}</button>
      <a class="btn btn--arancio btn--piccolo testata-chiama" href="tel:{TEL}" aria-label="Chiama Luca al {tel_txt()}">{I["tel"]}<span>Chiama</span></a>
      <button class="menu-bottone" type="button" aria-expanded="false" aria-controls="menu" aria-label="Apri il menu"><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <div class="menu-ingranaggio" aria-hidden="true"><svg viewBox="-300 -300 600 600"><path fill="currentColor" fill-rule="evenodd" d="{GEAR_PIENO}"/></svg></div>
  <nav aria-label="Menu"><ul>{voci(MENU, I["freccia"])}</ul></nav>
  <div class="menu-piede" role="region" aria-label="Contatti">
    <p class="stato" data-stato></p>
    <div class="azioni">
      <a class="btn btn--arancio" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}Scrivimi su WhatsApp</a>
    </div>
  </div>
</div>
<main id="contenuto">
'''


def scheda():
    scelte = []
    for i, (chi, nome_mezzo, valore, aiuto) in enumerate(MEZZI):
        dati = f'value="{attr(valore)}" data-consiglio="{attr(aiuto)}"'
        nascosto = "" if chi in MEZZI_BASE.split(",") else " hidden"
        scelte.append(f'<label data-mezzo="{chi}"{nascosto}><input type="radio" name="mezzo" {dati}{" checked" if i == 0 else ""}><span>{veicolo(chi)}<b>{nome_mezzo}</b></span></label>')
    return f'''<dialog class="scheda" id="scheda" aria-labelledby="scheda-t">
  <form class="scheda-form" novalidate>
    <div class="scheda-maniglia" aria-hidden="true"></div>
    <header class="scheda-testa">
      <h2 id="scheda-t" tabindex="-1">{SERVIZI[0][1]}</h2>
      <button type="button" class="scheda-chiudi" data-chiudi aria-label="Chiudi">{I["chiudi"]}</button>
    </header>
    <div class="scheda-corpo">
      <fieldset class="mezzi" data-mezzi="{MEZZI_BASE}">
        <legend>Che mezzo è?</legend>
        <div>{"".join(scelte)}</div>
      </fieldset>
      <div class="scheda-vendita" data-vendita-campi hidden>
        <div class="campo" data-campo-tipo><label for="scheda-tipo">Cosa cerchi?</label><select id="scheda-tipo" name="tipo"><option value="gomme">Gomme</option><option value="ricambi">Ricambi</option></select></div>
        <div data-pannello-vendita="gomme">
          <fieldset class="campo misura-scheda"><legend>Misura della gomma</legend><div class="misura">
            <label><span class="sr">Larghezza</span><input name="larghezza" inputmode="numeric" maxlength="3" placeholder="205" autocomplete="off"></label><i aria-hidden="true">/</i>
            <label><span class="sr">Spalla</span><input name="spalla" inputmode="numeric" maxlength="2" placeholder="55" autocomplete="off"></label><i aria-hidden="true">R</i>
            <label><span class="sr">Cerchio in pollici</span><input name="cerchio" inputmode="numeric" maxlength="2" placeholder="16" autocomplete="off"></label>
          </div><p class="errore" data-errore-misura aria-live="polite"></p></fieldset>
          <div class="campo"><label for="scheda-stagione">Che gomme cerchi</label><select id="scheda-stagione" name="stagione"><option>Estive</option><option>Invernali</option><option>Quattro stagioni</option><option>Non lo so, consigliami tu</option></select></div>
          <div class="campo"><label for="scheda-targa-gomme">Targa <span>(se non trovi la misura)</span></label><input id="scheda-targa-gomme" name="targa-gomme" maxlength="8" placeholder="AB123CD" autocomplete="off" autocapitalize="characters"></div>
        </div>
        <div data-pannello-vendita="ricambi" hidden>
          <div class="campo"><label for="scheda-targa-ricambi">Targa <span>(facoltativa)</span></label><input id="scheda-targa-ricambi" name="targa-ricambi" maxlength="8" placeholder="AB123CD" autocomplete="off" autocapitalize="characters"></div>
          <div class="campo"><label for="scheda-pezzo">Cosa ti serve</label><input id="scheda-pezzo" name="pezzo" placeholder="Es. pastiglie dei freni anteriori"><p class="errore" data-errore-pezzo aria-live="polite"></p></div>
          <div class="campo"><label for="scheda-mezzo-ricambi">Mezzo <span>(facoltativo)</span></label><input id="scheda-mezzo-ricambi" name="mezzo-ricambi" placeholder="Es. Fiat Panda 2015"></div>
        </div>
        <p class="aiuto">Non faccio spedizioni: paghi in officina, ordino il pezzo e lo ritiri qui.</p>
      </div>
      <div class="campo">
        <label for="scheda-note">Scrivimi due righe <span>(facoltativo)</span></label>
        <textarea id="scheda-note" name="note" rows="3" maxlength="600" aria-describedby="scheda-aiuto"></textarea>
        <p class="aiuto" id="scheda-aiuto" data-aiuto></p>
      </div>
      <div class="scheda-azioni">
        <button type="submit" class="btn btn--arancio" data-invia>{I["chat"]}Invia su WhatsApp</button>
        <a class="btn btn--vuoto" href="tel:{TEL}" data-chiama>{I["tel"]}Chiama {tel_txt()}</a>
      </div>
      <p class="scheda-nota" data-esito role="status">Si apre WhatsApp con il messaggio già scritto: l'invio lo confermi tu.</p>
    </div>
  </form>
</dialog>
'''


def orari():
    return f'''<table class="orari"><caption class="sr">Orari di apertura</caption>
  <tr data-giorni="1,2,3,4,5"><th scope="row">Lunedì – venerdì</th><td>7:30 – 19:30, continuato</td></tr>
  <tr data-giorni="6,0"><th scope="row">Sabato e domenica</th><td>Chiuso</td></tr>
</table>'''


def piede(extra=""):
    servizi = "".join(f'<li><a href="{href(p)}">{nome(p)}</a></li>' for p in SERVIZI_PAGINE)
    pagine_officina = "".join(f'<li><a href="{href(p)}">{nome(p)}</a></li>' for p in PIEDE_OFFICINA)
    nota = f'<span>Le fotografie sono di esempio: verranno sostituite con quelle dell’officina.</span>' if ci_sono_foto_stock() else ""
    social = "".join(f'\n      <li><a href="{p}" target="_blank" rel="noopener">{n}</a></li>' for p, n in ((FACEBOOK, "Facebook"), (INSTAGRAM, "Instagram")) if p)
    officina = f'\n      <li><a href="{MAPS}" target="_blank" rel="noopener">Officina: {indirizzo_officina()}</a></li>' if INDIRIZZO_OFFICINA else ""
    # Dati obbligatori in ogni pagina (D.Lgs. 70/2003, art. 7; P.IVA: DPR 633/1972, art. 35): vedi materiali/testi-legali/05.
    # Ogni dato è un pezzo che non si spezza; il REA compare appena è in contenuti.py.
    dati_legali = [f'© <span data-anno>2026</span> L.M. Autoservizi di Miglietta Luca, ditta individuale',
                   f'{"Sede legale e officina" if indirizzo_officina() == SEDE_LEGALE else "Sede legale"}: {SEDE_LEGALE}',
                   f'P.IVA {PIVA}'] + ([f"REA {REA}"] if REA else []) + [f'PEC <a href="mailto:{PEC}">{PEC}</a>']
    legale = " · ".join(f'<span class="piede-dato">{d}</span>' for d in dati_legali)
    return f'''</main>
<footer class="piede">
  <div class="wrap piede-griglia">
    <div class="piede-marchio">
      <img src="{risorsa("assets/img/logo-arancio-84.png")}" width="52" height="52" alt="" loading="lazy">
      <p><strong>L.M. Autoservizi di Miglietta Luca</strong><br>Officina multimarca a Frassineto Po. Ritiro e consegna gratis entro 20 km, assistenza a domicilio e vettura di cortesia gratuita.</p>
    </div>
    <div><h2>Servizi</h2><ul>{servizi}</ul></div>
    <div><h2>L'officina</h2><ul>{pagine_officina}</ul></div>
    <div><h2>Contatti</h2><ul>
      <li><a href="tel:{TEL}">{tel_txt()}</a></li>
      <li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="mailto:{PEC}">PEC: {PEC}</a></li>{social}{officina}</ul></div>
    <div><h2>Orari</h2><ul>
      <li>Lunedì – venerdì<br>7:30 – 19:30, continuato</li>
      <li>Sabato e domenica chiuso</li>
      <li><span class="stato" data-stato></span></li></ul></div>
  </div>
  <div class="wrap piede-basso">
    <p class="piede-legale">{legale}</p>
    {nota}
    <ul class="piede-note"><li><a href="{href("condizioni")}">{nome("condizioni")}</a></li><li><a href="{href("privacy")}">{nome("privacy")}</a></li></ul>
  </div>
</footer>
<nav class="barra" aria-label="Azioni rapide">
  <a href="tel:{TEL}">{I["tel"]}Chiama</a>
  <a href="{href("home", frammento="servizi")}">{ICONE["meccanica"]}Cosa ti serve</a>
  <a href="{wa()}" target="_blank" rel="noopener">{I["chat"]}WhatsApp</a>
</nav>
{scheda()}{extra}<script src="{risorsa("assets/js/vendor/gsap.min.js")}" defer></script>
<script src="{risorsa("assets/js/vendor/ScrollTrigger.min.js")}" defer></script>
<script src="{risorsa("assets/sito.js")}?v={V_JS}" defer></script>
</body>
</html>
'''


def intro(titolo, testo):
    """Apertura delle pagine interne. Sotto servizi/ c'è anche il percorso visibile, "Servizi" con il link all'indice."""
    madre = PAGINE[PAGINA][0].startswith("servizi/") and PAGINA != "servizi"
    percorso_pagina = f'<nav class="percorso-pagina" aria-label="Sei in"><a href="{href("servizi")}">Servizi</a> <span aria-hidden="true">›</span></nav>' if madre else ""
    return f'''
<section class="intro">
  <div class="intro-ingranaggio" aria-hidden="true"><svg viewBox="-300 -300 600 600"><path fill="currentColor" fill-rule="evenodd" d="{GEAR_PIENO}"/></svg></div>
  <div class="wrap">{percorso_pagina}<h1><span class="riga"><span>{titolo}</span></span></h1><p class="lead intro-lead">{testo}</p></div>
</section>
'''


def casella(s, con_foto=True):
    chi, nome_servizio, desc, nota, opzioni = s
    # la foto che si apre al passaggio del mouse, solo per i servizi che hanno il loro spazio in FOTO_SLOT
    foto_html = f'<span class="servizio-foto" aria-hidden="true">{img("servizio-" + chi, "", piccola=True, alt="")}</span>' if con_foto and "servizio-" + chi in FOTO_SLOT else ""
    return f'''<li><button type="button" class="servizio servizio--{chi}" {dati_servizio(nome_servizio, nota, opzioni, mezzi=MEZZI_SERVIZIO.get(chi))}>
  {foto_html}<span class="servizio-ico" aria-hidden="true">{ICONE[chi]}</span>
  <span class="servizio-nome">{nome_servizio}</span><span class="servizio-desc">{desc}</span>
</button></li>'''


def griglia_servizi(con_foto=True):
    nome_altro, nota, opzioni, titolo = EXTRA["altro"]
    altro = f'''<li><button type="button" class="servizio" {dati_servizio(nome_altro, nota, opzioni, titolo)}>
  <span class="servizio-ico" aria-hidden="true">{ICONE["altro"]}</span>
  <span class="servizio-nome">Non so cos'ha</span><span class="servizio-desc">Descrivimi il problema e lo capiamo insieme</span>
</button></li>'''
    # Il noleggio a lungo termine non apre la tendina: porta al sito dell'offerta, in una nuova scheda.
    noleggio = f'''<li><a class="servizio servizio--link" href="{NOLEGGIO_LINK}" target="_blank" rel="noopener">
  <span class="servizio-ico" aria-hidden="true">{ICONE["noleggio"]}</span>
  <span class="servizio-nome">Noleggio a lungo termine</span><span class="servizio-desc">Auto e furgoni con un canone mensile: guarda le offerte {I["esterno"]}</span>
</a></li>''' if NOLEGGIO_LINK else ""
    # Prima le due caselle per chi è in difficoltà: non sa cos'ha, o ha il mezzo fermo. Poi i servizi dell'officina.
    domicilio = next(s for s in SERVIZI if s[0] == "soccorso")
    resto = "".join(casella(s, con_foto) for s in SERVIZI if s is not domicilio)
    return f'<ul class="servizi-griglia">{altro}{casella(domicilio, con_foto)}{resto}{noleggio}</ul>'


def sezione_servizi(id_sezione, link):
    """La sezione "Cosa ti serve?" con la griglia dei servizi: la stessa in home e nella pagina Servizi
    (sugli schermi abbastanza alti sta in una schermata). link: il collegamento accanto al testo."""
    return f'''
<section class="servizi" id="{id_sezione}" aria-labelledby="{id_sezione}-t">
  <div class="wrap">
    <div class="servizi-testa">
      <h2 id="{id_sezione}-t">Cosa ti serve?</h2>
      <div class="servizi-testa-lato">
        <p class="lead">Tocca il servizio, scegli il mezzo e scrivimi due righe. Ti rispondo io, di persona.</p>
        {link}
      </div>
    </div>
    {griglia_servizi()}
  </div>
</section>'''


def finale(titolo=None, testo=None, pulsante=None):
    """Chiusura della pagina: il numero grande, il pulsante principale (di norma la scelta del servizio in home) e WhatsApp."""
    titolo = titolo or "Ti serve una mano con il tuo mezzo?"
    pulsante = pulsante or f'<a class="btn btn--arancio" href="{href("home", frammento="servizi")}">Scegli il servizio {I["freccia"]}</a>'
    testo = testo or "Chiamami o scrivimi: ti dico quando puoi portarmelo in officina, o quando posso passare a ritirarlo."
    return f'''
<section class="finale">
  <div class="wrap finale-riga">
    <div><h2>{titolo}</h2><p>{testo}</p></div>
    <div class="finale-azioni">
      <a class="numerone" href="tel:{TEL}">{tel_txt()}</a>
      <div class="azioni">{pulsante}<a class="btn btn--vuoto" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}WhatsApp</a></div>
    </div>
  </div>
</section>
'''


def lightbox():
    """La finestra che mostra le foto a grandezza piena: si passa a piede(extra) nelle pagine con i pulsanti data-lightbox."""
    return f'''<dialog class="lightbox" id="lightbox" aria-labelledby="lightbox-t">
  <figure><figcaption id="lightbox-t"></figcaption></figure>
  <button class="lightbox-chiudi" type="button" aria-label="Chiudi" data-chiudi>{I["chiudi"]}</button>
</dialog>
'''


def spunte(voci):
    return '<ul class="spunte">' + "".join(f"<li>{I['check']}<span>{v}</span></li>" for v in voci) + "</ul>"


def scrivi(contenuto):
    """Scrive la pagina corrente: docs/<percorso>/index.html (la 404 è un file a sé)."""
    relativo = percorso(PAGINA)
    if relativo == "" or relativo.endswith("/"):
        relativo += "index.html"
    file = os.path.join(DOCS, *relativo.split("/"))
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenuto)
    SCRITTE.append(PAGINA)
    FILE_SCRITTI.add(os.path.normpath(file))
    print("scritto", relativo, len(contenuto))
