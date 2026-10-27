"""Servizi: la pagina indice (servizi/) e le pagine dei cinque servizi principali, con i testi di testi_pagine.py.
La diagnosi ha anche il calcolo della scadenza della revisione (script/20-revisione.js), il gommista le date delle gomme invernali."""
from contenuti import TEL_TXT
from testi_pagine import SERVIZI_PAGINE, SERVIZI_HUB
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, azienda, briciole, griglia_servizi, svg,
                  t, tt, href, url, nome, I, ICONE, VANTAGGI_ICO, SERVIZI, TEL, tel_txt, dati_servizio, apri)

CINQUE = ["meccanica", "elettrauto", "gommista", "carrozzeria", "diagnosi"]
CALENDARIO = svg('<rect x="3.5" y="5" width="17" height="15.5" rx="2.2"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path class="pieno" d="M7.5 13h3v3h-3z"/>')
MESI = [("Gennaio", "January"), ("Febbraio", "February"), ("Marzo", "March"), ("Aprile", "April"), ("Maggio", "May"), ("Giugno", "June"),
        ("Luglio", "July"), ("Agosto", "August"), ("Settembre", "September"), ("Ottobre", "October"), ("Novembre", "November"), ("Dicembre", "December")]


def servizio(chi):
    return next(s for s in SERVIZI if s[0] == chi)


def chiedi(chi, testo, classe="btn btn--arancio", extra=""):
    """Bottone della tendina WhatsApp per il servizio, con il suggerimento per le note scritto per la sua pagina."""
    s = servizio(chi)
    nota = SERVIZI_PAGINE[chi]["nota_mezzo"] if chi in SERVIZI_PAGINE else s[3]
    return f'<button type="button" class="{classe}" {dati_servizio(s[1], nota, s[4])}{extra}>{testo} {I["freccia"]}</button>'


def chiama(classe="btn btn--vuoto"):
    return f'<a class="{classe}" href="tel:{TEL}">{I["tel"]}{t("Chiama", "Call")} {tel_txt()}</a>'


def faq(domande):
    return '<div class="faq">' + "".join(f'<details><summary>{tt(d)}</summary><div class="faq-risposta"><p>{tt(r)}</p></div></details>' for d, r in domande) + "</div>"


def schema_faq(domande):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": tt(d), "acceptedAnswer": {"@type": "Answer", "text": tt(r)}} for d, r in domande]}


def elenco(voci, con_id=False):
    """Righe che portano alle pagine dei servizi: icona, nome, una riga di descrizione.
    Nell'indice ogni riga ha l'id del servizio, così restano validi i vecchi link servizi/#meccanica e simili."""
    righe = "".join(f'''
      <li{f' id="{chi}"' if con_id else ""}><a class="dettaglio" href="{href(chi)}">
        <span class="dettaglio-ico" aria-hidden="true">{ICONE[chi]}</span>
        <div class="dettaglio-testo"><h3>{tt(SERVIZI_PAGINE[chi]["nome"])}</h3><p>{tt(servizio(chi)[2])}</p></div>
        <span class="dettaglio-vai"><span>{t("Scopri", "Details")}</span>{I["freccia"]}</span>
      </a></li>''' for chi in voci)
    return f'<ul class="dettagli">{righe}\n    </ul>'


def costruisci():
    pagina_servizi()
    for chi in CINQUE:
        pagina_servizio(chi)


# ---------------------------------------------------------------- indice dei servizi
def pagina_servizi():
    inizia("servizi")
    # (id per i link già esistenti, icona, nome, testo, link o bottone)
    altri = [("ricambi", ICONE["ricambi"], nome("gomme"), ("Ricambi e pneumatici: chiedimi disponibilità e prezzo.", "Spare parts and tyres: ask me about availability and price."),
              f'<a class="link" href="{href("gomme")}">{t("Cerca per misura", "Search by size")} {I["freccia"]}</a>'),
             ("ritiro", VANTAGGI_ICO["rotta"], nome("ritiro"), ("Passo a casa o al lavoro, riparo il mezzo in officina e te lo riporto dove vuoi.",
                                                               "I collect from your home or workplace, repair the vehicle in the workshop and bring it back wherever you like."),
              f'<a class="link" href="{href("ritiro")}">{t("Come funziona", "How it works")} {I["freccia"]}</a>'),
             ("soccorso", VANTAGGI_ICO["mobile"], nome("mobile"), ("Forature, cambio ruote, diagnosi e avviamento: quando si può, intervengo sul posto.",
                                                                   "Punctures, wheel changes, diagnostics and starting problems: when possible, I fix it on the spot."),
              f'<a class="link" href="{href("mobile")}">{t("Cosa faccio sul posto", "What I do on site")} {I["freccia"]}</a>'),
             ("aziende", ICONE["aziende"], t("Consulenza alle imprese", "Business consulting"),
              ("Consulenza per le imprese che lavorano nel settore automobilistico, da un tecnico con più di dieci anni di esperienza multimarca. Ne parliamo e capiamo insieme di cosa hai bisogno.",
               "Consulting for businesses working in the automotive sector, from a technician with over ten years of multi-brand experience. Let's talk and work out together what you need."),
              apri("aziende", t("Parliamone", "Let's talk"), "link link--bottone"))]
    voci_altri = "".join(f'''
      <li id="{id_}">{icona}<h3>{titolo}</h3><p>{tt(testo)}</p>{azione}</li>''' for id_, icona, titolo, testo, azione in altri)
    scrivi(head(tt(SERVIZI_HUB["title"]), tt(SERVIZI_HUB["description"]), [azienda(), briciole()]) + testata()
           + intro(tt(SERVIZI_HUB["h1"]), tt(SERVIZI_HUB["intro"])) + f'''
<section class="sezione scelta" id="scegli" aria-labelledby="scegli-t">
  <div class="wrap">
    <div class="scelta-testa">
      <h2 id="scegli-t">{t("Cosa ti serve?", "What do you need?")}</h2>
      <p class="lead">{t("Tocca il servizio, scegli il mezzo e scrivimi due righe. Ti rispondo io, di persona.", "Tap the service, choose your vehicle and send me a couple of lines. I'll answer personally.")}</p>
    </div>
    {griglia_servizi()}
  </div>
</section>
<section class="sezione sezione--asfalto" aria-labelledby="dettaglio-t">
  <div class="wrap">
    <h2 id="dettaglio-t">{t("I servizi nel dettaglio", "Services in detail")}</h2>
    {elenco(CINQUE, con_id=True)}
  </div>
</section>
<div class="wrap fascia">{foto("officina", "(max-width: 1280px) 100vw, 1280px", "foto foto--fascia")}</div>
<section class="sezione" aria-labelledby="altri-t">
  <div class="wrap">
    <h2 id="altri-t">{t("Altri servizi", "Other services")}</h2>
    <ul class="altri">{voci_altri}
    </ul>
  </div>
</section>''' + finale() + piede())


# ---------------------------------------------------------------- pagina di un servizio
def pagina_servizio(chi):
    inizia(chi)
    p = SERVIZI_PAGINE[chi]
    schema_servizio = {"@context": "https://schema.org", "@type": "Service", "serviceType": tt(p["nome"]), "name": tt(p["h1"]), "description": tt(p["description"]),
                       "provider": {"@id": azienda()["@id"]}, "url": url(),
                       "areaServed": [{"@type": "City", "name": "Frassineto Po"}, {"@type": "City", "name": "Casale Monferrato"}]}
    comprende = "".join(f'<li>{I["check"]}<div><h3>{tt(titolo)}</h3><p>{tt(testo)}</p></div></li>' for titolo, testo in p["comprende"])
    perche = "".join(f'<li><span class="perche-n" aria-hidden="true">{i + 1:02d}</span><h3>{tt(titolo)}</h3><p>{tt(testo)}</p></li>' for i, (titolo, testo) in enumerate(p["perche"]))
    aggiunta = {"gommista": stagioni, "diagnosi": revisione}.get(chi, lambda: "")()
    scrivi(head(tt(p["title"]), tt(p["description"]), [azienda(), schema_servizio, schema_faq(p["faq"]), briciole()], immagine="servizio-" + chi) + testata()
           + intro(tt(p["h1"]), tt(p["risposta"])) + f'''
<div class="servizio-cta">
  <div class="wrap">
    <div class="azioni">{chiedi(chi, t("Chiedi un preventivo", "Ask for a quote"))}{chiama()}</div>
    <p class="piccolo">{t("Scegli il mezzo e scrivimi due righe: il messaggio si apre su WhatsApp, già pronto.", "Choose your vehicle and write me a couple of lines: the message opens in WhatsApp, ready to send.")}</p>
  </div>
</div>
<section class="sezione" aria-labelledby="comprende-t">
  <div class="wrap comprende">
    <div class="comprende-testa">
      <span class="comprende-ico" aria-hidden="true">{ICONE[chi]}</span>
      <h2 id="comprende-t">{t("Cosa comprende", "What's included")}</h2>
    </div>
    <ul class="comprende-lista">{comprende}</ul>
    {foto("servizio-" + chi, "(max-width: 899px) 100vw, 40vw", "foto comprende-foto")}
  </div>
</section>{aggiunta}
<section class="sezione sezione--asfalto" aria-labelledby="perche-t">
  <div class="wrap">
    <h2 id="perche-t">{t("Perché da me", "Why me")}</h2>
    <ul class="perche">{perche}</ul>
  </div>
</section>
<section class="sezione" id="domande" aria-labelledby="domande-t">
  <div class="wrap servizio-faq">
    <div><h2 id="domande-t">{t("Domande frequenti", "Frequently asked questions")}</h2>{faq(p["faq"])}</div>
    <div class="riquadro">
      <h2>{t("Chiedi un preventivo", "Ask for a quote")}</h2>
      <p>{t("Tocca il pulsante, scegli il mezzo e scrivimi due righe. Il preventivo è gratuito e arriva prima di iniziare.",
            "Tap the button, choose your vehicle and write me a couple of lines. The quote is free and comes before any work starts.")}</p>
      {chiedi(chi, t("Scrivimi su WhatsApp", "Message me on WhatsApp"))}
      <a class="link" href="tel:{TEL}">{I["tel"]}{t("Oppure chiama", "Or call")} {tel_txt()}</a>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto" aria-labelledby="collegati-t">
  <div class="wrap">
    <h2 id="collegati-t">{t("Servizi collegati", "Related services")}</h2>
    {elenco(p["correlati"])}
    <a class="link collegati-tutti" href="{href("servizi")}">{t("Tutti i servizi", "All services")} {I["freccia"]}</a>
  </div>
</section>''' + finale() + piede())


# ---------------------------------------------------------------- gommista: le date delle gomme invernali
def stagioni():
    date = [(("Dal 15 ottobre", "From 15 October"), ("Puoi montare le gomme invernali.", "Winter tyres can go on.")),
            (("15 novembre – 15 aprile", "15 November – 15 April"), ("Dove le ordinanze lo prevedono, servono gomme invernali o catene a bordo.",
                                                                     "Where ordinances require it, you need winter tyres or chains on board.")),
            (("Entro il 15 maggio", "By 15 May"), ("Rimonti le gomme estive.", "Summer tyres go back on."))]
    voci = "".join(f'<li><strong>{tt(quando)}</strong><span>{tt(cosa)}</span></li>' for quando, cosa in date)
    return f'''
<section class="sezione sezione--stretta" aria-labelledby="stagioni-t">
  <div class="wrap">
    <div class="stagioni">
      <div class="stagioni-testa">
        <h2 id="stagioni-t">{t("Gomme invernali: le date", "Winter tyres: the dates")}</h2>
        <p>{t("Sono le date valide in generale: per le strade che fai contano le ordinanze locali.", "These are the general dates: what counts is the local ordinances for the roads you drive on.")}</p>
      </div>
      <ol class="stagioni-date">{voci}</ol>
      <div class="azioni">{chiedi("gommista", t("Prenota il cambio gomme", "Book a tyre change"))}<a class="link" href="{href("gomme")}">{t("Cerca le gomme per misura", "Find tyres by size")} {I["freccia"]}</a></div>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- diagnosi: quando scade la revisione
def revisione():
    mesi = "".join(f'<option value="{i}">{tt(m)}</option>' for i, m in enumerate(MESI, 1))

    def data(chiave, legenda, di_cosa, aiuto=""):
        """Mese e anno: select nativi, l'elenco degli anni lo scrive lo script (dall'anno in corso al 1980)."""
        campi = "".join(f'''
            <div class="campo"><label class="sr" for="rev-{chiave}-{c}">{etichetta} {tt(di_cosa)}</label><select id="rev-{chiave}-{c}" name="{chiave}-{c}"{anni}><option value="">{etichetta}</option>{opzioni}</select></div>'''
                        for c, etichetta, anni, opzioni in (("m", t("Mese", "Month"), "", mesi), ("a", t("Anno", "Year"), " data-anni", "")))
        return f'''
        <fieldset class="calcolo-data" data-gruppo="{chiave}">
          <legend>{tt(legenda)}</legend>
          <div class="calcolo-campi">{campi}
          </div>{f'<p class="aiuto">{aiuto}</p>' if aiuto else ""}
        </fieldset>'''
    prenota = chiedi("diagnosi", t("Prenota il controllo gratuito", "Book the free check"), extra=" data-prenota-revisione")
    return f'''
<section class="sezione sezione--stretta" id="revisione" aria-labelledby="revisione-t">
  <div class="wrap revisione">
    <div class="revisione-testo">
      <h2 id="revisione-t">{t("Quando scade la revisione?", "When is your test due?")}</h2>
      <p class="lead">{t("La prima revisione va fatta entro quattro anni dalla prima immatricolazione, poi ogni due anni.",
                         "The first roadworthiness test (revisione) is due within four years of first registration, then every two years.")}</p>
      <p>{t("La scadenza è la fine del mese: un'auto immatricolata a marzo 2023 va in revisione entro marzo 2027. Dopo, entro lo stesso mese dell'ultima revisione, due anni più tardi.",
            "The deadline is the end of the month: a car first registered in March 2023 is due by March 2027. After that, by the same month as the last test, two years later.")}</p>
      <p class="piccolo">{t("Vale per auto e mezzi fino a 3,5 tonnellate: per quelli più pesanti, come alcuni camper, la revisione è ogni anno.",
                            "This applies to cars and vehicles up to 3.5 tonnes: heavier ones, such as some motorhomes, are tested every year.")}</p>
    </div>
    <form class="calcolo" data-revisione data-tel="+39 {TEL_TXT}" data-pagina="{url()}" novalidate hidden aria-labelledby="calcolo-t">
      <h3 id="calcolo-t">{t("Calcola la tua scadenza", "Work out your deadline")}</h3>{data("imm", ("Prima immatricolazione", "First registration"), ("della prima immatricolazione", "of first registration"),
                                                                                         t("È sulla carta di circolazione, al punto B.", "It's on the registration document (carta di circolazione), field B."))}{data("ult", ("Ultima revisione, se l'hai già fatta", "Last test, if you've had one"), ("dell'ultima revisione", "of the last test"))}
      <div class="calcolo-esito" data-esito-revisione aria-live="polite"></div>
      <div class="azioni calcolo-azioni" data-azioni-revisione hidden>
        {prenota}
        <button type="button" class="btn btn--vuoto" data-promemoria>{CALENDARIO}{t("Aggiungi un promemoria al calendario", "Add a reminder to your calendar")}</button>
      </div>
      <p class="nota" data-promemoria-esito role="status"></p>
      <p class="nota">{t("Il calcolo resta sul tuo telefono: a me non arriva niente.", "The calculation stays on your phone: nothing is sent to me.")}</p>
    </form>
  </div>
</section>'''
