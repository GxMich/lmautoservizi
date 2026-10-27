"""Privacy e cookie (privacy/) e Garanzia e condizioni (garanzia-e-condizioni/).
I testi vengono da testi_legali.py, bozze da far rivedere a un professionista (materiali/testi-legali/LEGGIMI.md).
I loro commenti HTML ("DA VERIFICARE", "OPZIONALE") sono note interne: senza_commenti() li toglie prima di scrivere le pagine.
Con le statistiche accese (LM_GOATCOUNTER) l'informativa cambia le frasi su cookie e statistiche e aggiunge il paragrafo su GoatCounter."""
import datetime, re
import testi_legali as TL
from contenuti import PEC, PIVA, SEDE_LEGALE
from sito import (inizia, scrivi, head, testata, intro, piede, briciole, t, lingua, href, nome, slug, senza_commenti,
                  EMAIL, TEL, tel_txt, STATISTICHE)

# Data dell'ultima modifica dei testi legali, mostrata in cima all'informativa.
# Va cambiata a mano quando cambia testi_legali.py o quando si accendono le statistiche.
AGGIORNAMENTO = datetime.date(2026, 10, 27)
MESI = {"it": ("gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"),
        "en": ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")}
ESTERNO = 'target="_blank" rel="noopener"'


def data_in_parole(giorno):
    return f"{giorno.day} {MESI[lingua()][giorno.month - 1]} {giorno.year}"


def sostituisci(html, vecchio, nuovo):
    """Sostituzione che si ferma se il testo di partenza è cambiato: meglio un errore che un'informativa sbagliata."""
    if html.count(vecchio) != 1:
        raise SystemExit(f"legale.py: in testi_legali.py non trovo una sola volta {vecchio[:60]!r}: aggiornare le sostituzioni per le statistiche")
    return html.replace(vecchio, nuovo)


def con_statistiche(html):
    """Informativa con le statistiche senza cookie accese: versione definitiva del paragrafo che nella bozza è in commento."""
    if lingua() == "it":
        paragrafo = f'''<h3>Statistiche senza cookie</h3>
<p>Per capire quali pagine sono più utili uso <a href="https://www.goatcounter.com" {ESTERNO}>GoatCounter</a>. Lo strumento conta le visite in forma aggregata (pagina vista, sito di provenienza, tipo di dispositivo, Paese) e i clic sui pulsanti per chiamare o scrivere su WhatsApp, senza cookie, senza conservare l'indirizzo IP completo e senza creare profili. Non sa chi sei e non vede cosa scrivi nei messaggi. La base giuridica è il mio legittimo interesse a migliorare il sito (art. 6.1.f GDPR). Il fornitore tratta i dati per conto mio come responsabile del trattamento.</p>
'''
        coppie = [("Il sito non usa cookie né statistiche.", "Il sito non usa cookie e conta le visite solo in forma anonima e aggregata."),
                  ("<h3>Niente cookie, niente statistiche</h3>", "<h3>Niente cookie</h3>"),
                  ("Il sito non usa cookie, non usa strumenti di statistica e non carica contenuti da altri siti, come mappe, video, caratteri tipografici esterni o pulsanti dei social.",
                   "Il sito non usa cookie e non carica contenuti da altri siti, come mappe, video, caratteri tipografici esterni o pulsanti dei social, a parte il piccolo programma delle statistiche senza cookie descritto qui sotto."),
                  ("<h3>Link ad altri siti</h3>", paragrafo + "<h3>Link ad altri siti</h3>"),
                  ("il fornitore di hosting del sito;", "il fornitore di hosting del sito e il servizio di statistica GoatCounter;")]
    else:
        paragrafo = f'''<h3>Cookieless analytics</h3>
<p>To see which pages are most useful I use <a href="https://www.goatcounter.com" {ESTERNO}>GoatCounter</a>, which counts visits in aggregate form (page, referrer, device type, country) and clicks on the call and WhatsApp buttons, without cookies, without storing the full IP address and without profiling. It does not know who you are and does not see what you write in your messages. Legal basis: my legitimate interest in improving the website (Art. 6(1)(f) GDPR). The provider acts as my processor.</p>
'''
        coppie = [("The website uses no cookies and no analytics.", "The website uses no cookies and counts visits only in anonymous, aggregate form."),
                  ("The website uses no cookies and no analytics, and loads no content from other websites (maps, videos, external fonts, social buttons), so it shows no cookie banner.",
                   "The website uses no cookies and loads no content from other websites (maps, videos, external fonts, social buttons), apart from the small cookieless analytics script described below, so it shows no cookie banner."),
                  ("<p>Some buttons open external services", paragrafo + "<p>Some buttons open external services"),
                  ("the website hosting provider;", "the website hosting provider and the GoatCounter analytics service;")]
    for vecchio, nuovo in coppie:
        html = sostituisci(html, vecchio, nuovo)
    return html


def con_id(html):
    """Dà un id a ogni <h2> e restituisce (html, [(id, titolo)]) per l'indice."""
    voci, usati = [], {"contenuto", "menu", "scheda"}

    def numera(m):
        base = chiave = slug(m.group(1))
        n = 2
        while chiave in usati:
            chiave, n = f"{base}-{n}", n + 1
        usati.add(chiave)
        voci.append((chiave, re.sub(r"<[^>]+>", "", m.group(1))))
        return f'<h2 id="{chiave}">{m.group(1)}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", numera, html), voci


def indice(voci):
    """Indice della pagina: a lato sui computer, a tendina (details) su tablet e telefono. Il CSS ne mostra uno solo."""
    titolo = t("In questa pagina", "On this page")
    lista = "<ol>" + "".join(f'<li><a href="#{chiave}">{testo}</a></li>' for chiave, testo in voci) + "</ol>"
    lato = f'<nav class="documento-indice" aria-label="{titolo}"><p class="documento-indice-titolo">{titolo}</p>{lista}</nav>'
    tendina = f'<details class="documento-tendina"><summary>{titolo}</summary><nav aria-label="{titolo}">{lista}</nav></details>'
    return lato, tendina


def documento(corpo, voci=None):
    """Sezione di prosa; con le voci, indice a lato (computer) e a tendina prima del primo titolo (tablet e telefono)."""
    if not voci:  # prosa allineata a sinistra come il titolo della pagina
        return f'''
<section class="sezione">
  <div class="wrap">
    <div class="prosa">
{corpo}
    </div>
  </div>
</section>'''
    lato, tendina = indice(voci)
    primo = corpo.find("<h2")
    corpo = corpo[:primo] + tendina + "\n" + corpo[primo:]
    return f'''
<section class="sezione">
  <div class="wrap documento">
    {lato}
    <div class="prosa">
{corpo}
    </div>
  </div>
</section>'''


def costruisci():
    inizia("privacy")
    dati = {"titolare": "L.M. Autoservizi di Miglietta Luca", "sede_legale": SEDE_LEGALE, "piva": PIVA, "email": EMAIL, "pec": PEC,
            "telefono": f'<a href="tel:{TEL}">{tel_txt()}</a>', "aggiornamento": data_in_parole(AGGIORNAMENTO)}
    corpo = t(TL.PRIVACY_IT, TL.PRIVACY_EN).format(**dati)
    if STATISTICHE:
        corpo = con_statistiche(corpo)
    corpo, voci = con_id(senza_commenti(corpo).strip())
    scrivi(head(t("Privacy e cookie | L.M. Autoservizi", "Privacy and cookies | L.M. Autoservizi"),
                t("Informativa privacy di L.M. Autoservizi: quali dati tratto, perché e per quanto tempo, WhatsApp, vettura di cortesia, cookie e i tuoi diritti.",
                  "L.M. Autoservizi privacy notice: what data I process, why and for how long, WhatsApp, courtesy car, cookies and your rights."),
                [briciole()]) + testata()
           + intro(t("Privacy e cookie", "Privacy and cookies"),
                   t("Quali dati tratto, perché e per quanto tempo: sito, WhatsApp, lavori in officina e vettura di cortesia.",
                     "What data I process, why and for how long: website, WhatsApp, workshop jobs and courtesy car."))
           + documento(corpo, voci) + piede())
    condizioni()


def condizioni():
    """Garanzia e vettura di cortesia: i riassunti per il sito. I testi completi (file 03 e 04 di materiali/testi-legali)
    si firmano in officina, e il sito non deve promettere più di loro."""
    inizia("condizioni")
    garanzia = senza_commenti(t(TL.GARANZIA_SITO_IT, TL.GARANZIA_SITO_EN)).strip()
    vettura = senza_commenti(t(TL.VETTURA_CORTESIA_IT, TL.VETTURA_CORTESIA_EN)).strip()
    if lingua() == "it":
        corpo = f'''<h2 id="garanzia">Garanzia di legge e garanzia sul lavoro</h2>
{garanzia}
<h2 id="vettura-di-cortesia">Vettura di cortesia</h2>
<p>In breve, le regole del prestito:</p>
{vettura}
<h2 id="altre-informazioni">Altre informazioni</h2>
<p>Come tratto i dati della patente, del contratto e del verbale lo spiego nella pagina <a href="{href("privacy", frammento="vettura-di-cortesia")}">{nome("privacy")}</a>. Dove si trova l'officina e come lavoro lo trovi in <a href="{href("officina")}">{nome("officina")}</a>; come funzionano il ritiro dell'auto e la vettura di cortesia in <a href="{href("ritiro")}">{nome("ritiro")}</a>.</p>
<p>Per qualsiasi dubbio chiamami al <a href="tel:{TEL}">{tel_txt()}</a> o scrivimi a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
    else:
        corpo = f'''<h2 id="garanzia">Legal guarantee and warranty on my work</h2>
{garanzia}
<h2 id="vettura-di-cortesia">Courtesy car</h2>
<p>In short, the rules of the loan:</p>
{vettura}
<h2 id="altre-informazioni">More information</h2>
<p>How I process your driving licence details, the agreement and the hand-over report is explained on the <a href="{href("privacy", frammento="courtesy-car")}">{nome("privacy")}</a> page. Where the workshop is and how I work: <a href="{href("officina")}">{nome("officina")}</a>; how the pick-up and the courtesy car work: <a href="{href("ritiro")}">{nome("ritiro")}</a>.</p>
<p>If anything is unclear, call me on <a href="tel:{TEL}">{tel_txt()}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
    scrivi(head(t("Garanzia e condizioni | L.M. Autoservizi", "Warranty and terms | L.M. Autoservizi"),
                t("Garanzia di legge, garanzia sul lavoro e regole della vettura di cortesia gratuita: cosa sapere prima di lasciare l'auto a L.M. Autoservizi.",
                  "Legal guarantee, my own warranty on repairs and the free courtesy car rules: what to know before leaving your car at L.M. Autoservizi."),
                [briciole()]) + testata()
           + intro(t("Garanzia e condizioni", "Warranty and terms"),
                   t("Cosa copre la garanzia sui miei lavori e come funziona la vettura di cortesia.",
                     "What my warranty on repairs covers and how the courtesy car works."))
           + documento(corpo) + piede())
