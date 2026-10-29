"""Servizi: la pagina indice (servizi/) e le pagine dei cinque servizi principali, con i testi di testi_pagine.py.
La diagnosi ha anche il calcolo della scadenza della revisione (script/20-revisione.js), il gommista le date delle gomme invernali."""
from contenuti import TEL_TXT
from testi_pagine import SERVIZI_PAGINE, SERVIZI_HUB
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, azienda, briciole, griglia_servizi, svg,
                  href, url, nome, I, ICONE, VANTAGGI_ICO, SERVIZI, TEL, tel_txt, dati_servizio, apri)

CINQUE = ["meccanica", "elettrauto", "gommista", "carrozzeria", "diagnosi"]
CALENDARIO = svg('<rect x="3.5" y="5" width="17" height="15.5" rx="2.2"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path class="pieno" d="M7.5 13h3v3h-3z"/>')
MESI = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
        "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]


def servizio(chi):
    return next(s for s in SERVIZI if s[0] == chi)


def chiedi(chi, testo, classe="btn btn--arancio", extra=""):
    """Bottone della tendina WhatsApp per il servizio, con il suggerimento per le note scritto per la sua pagina."""
    s = servizio(chi)
    nota = SERVIZI_PAGINE[chi]["nota_mezzo"] if chi in SERVIZI_PAGINE else s[3]
    return f'<button type="button" class="{classe}" {dati_servizio(s[1], nota, s[4])}{extra}>{testo} {I["freccia"]}</button>'


def chiama(classe="btn btn--vuoto"):
    return f'<a class="{classe}" href="tel:{TEL}">{I["tel"]}Chiama {tel_txt()}</a>'


def faq(domande):
    return '<div class="faq">' + "".join(f'<details><summary>{d}</summary><div class="faq-risposta"><p>{r}</p></div></details>' for d, r in domande) + "</div>"


def schema_faq(domande):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": d, "acceptedAnswer": {"@type": "Answer", "text": r}} for d, r in domande]}


def elenco(voci, con_id=False):
    """Righe che portano alle pagine dei servizi: icona, nome, una riga di descrizione.
    Nell'indice ogni riga ha l'id del servizio, così restano validi i vecchi link servizi/#meccanica e simili."""
    righe = "".join(f'''
      <li{f' id="{chi}"' if con_id else ""}><a class="dettaglio" href="{href(chi)}">
        <span class="dettaglio-ico" aria-hidden="true">{ICONE[chi]}</span>
        <div class="dettaglio-testo"><h3>{SERVIZI_PAGINE[chi]["nome"]}</h3><p>{servizio(chi)[2]}</p></div>
        <span class="dettaglio-vai"><span>Scopri</span>{I["freccia"]}</span>
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
    altri = [("ricambi", ICONE["ricambi"], nome("gomme"), "Ricambi e pneumatici: chiedimi disponibilità e prezzo.",
              f'<a class="link" href="{href("gomme")}">Cerca per misura {I["freccia"]}</a>'),
             ("ritiro", VANTAGGI_ICO["rotta"], nome("ritiro"), "Passo a casa o al lavoro, riparo il mezzo in officina e te lo riporto dove vuoi.",
              f'<a class="link" href="{href("ritiro")}">Come funziona {I["freccia"]}</a>'),
             ("soccorso", VANTAGGI_ICO["mobile"], nome("mobile"), "Forature, cambio ruote, diagnosi e avviamento: quando si può, intervengo sul posto.",
              f'<a class="link" href="{href("mobile")}">Cosa faccio sul posto {I["freccia"]}</a>'),
             ("aziende", ICONE["aziende"], "Consulenza alle imprese",
              "Consulenza per le imprese che lavorano nel settore automobilistico, da un tecnico con più di dieci anni di esperienza multimarca. Ne parliamo e capiamo insieme di cosa hai bisogno.",
              apri("aziende", "Parliamone", "link link--bottone"))]
    voci_altri = "".join(f'''
      <li id="{id_}">{icona}<h3>{titolo}</h3><p>{testo}</p>{azione}</li>''' for id_, icona, titolo, testo, azione in altri)
    scrivi(head(SERVIZI_HUB["title"], SERVIZI_HUB["description"], [azienda(), briciole()]) + testata()
           + intro(SERVIZI_HUB["h1"], SERVIZI_HUB["intro"]) + f'''
<section class="sezione scelta" id="scegli" aria-labelledby="scegli-t">
  <div class="wrap">
    <div class="scelta-testa">
      <h2 id="scegli-t">Cosa ti serve?</h2>
      <p class="lead">Tocca il servizio, scegli il mezzo e scrivimi due righe. Ti rispondo io, di persona.</p>
    </div>
    {griglia_servizi()}
  </div>
</section>
<section class="sezione sezione--asfalto" aria-labelledby="dettaglio-t">
  <div class="wrap">
    <h2 id="dettaglio-t">I servizi nel dettaglio</h2>
    {elenco(CINQUE, con_id=True)}
  </div>
</section>
<div class="wrap fascia">{foto("officina", "(max-width: 1280px) 100vw, 1280px", "foto foto--fascia")}</div>
<section class="sezione" aria-labelledby="altri-t">
  <div class="wrap">
    <h2 id="altri-t">Altri servizi</h2>
    <ul class="altri">{voci_altri}
    </ul>
  </div>
</section>''' + finale() + piede())


# ---------------------------------------------------------------- pagina di un servizio
def pagina_servizio(chi):
    inizia(chi)
    p = SERVIZI_PAGINE[chi]
    schema_servizio = {"@context": "https://schema.org", "@type": "Service", "serviceType": p["nome"], "name": p["h1"], "description": p["description"],
                       "provider": {"@id": azienda()["@id"]}, "url": url(),
                       "areaServed": [{"@type": "City", "name": "Frassineto Po"}, {"@type": "City", "name": "Casale Monferrato"}]}
    comprende = "".join(f'<li>{I["check"]}<div><h3>{titolo}</h3><p>{testo}</p></div></li>' for titolo, testo in p["comprende"])
    perche = "".join(f'<li><span class="perche-n" aria-hidden="true">{i + 1:02d}</span><h3>{titolo}</h3><p>{testo}</p></li>' for i, (titolo, testo) in enumerate(p["perche"]))
    aggiunta = {"gommista": stagioni, "diagnosi": revisione}.get(chi, lambda: "")()
    scrivi(head(p["title"], p["description"], [azienda(), schema_servizio, schema_faq(p["faq"]), briciole()], immagine="servizio-" + chi) + testata()
           + intro(p["h1"], p["risposta"]) + f'''
<div class="servizio-cta">
  <div class="wrap">
    <div class="azioni">{chiedi(chi, "Chiedi un preventivo")}{chiama()}</div>
    <p class="piccolo">Scegli il mezzo e scrivimi due righe: il messaggio si apre su WhatsApp, già pronto.</p>
  </div>
</div>
<section class="sezione" aria-labelledby="comprende-t">
  <div class="wrap comprende">
    <div class="comprende-testa">
      <span class="comprende-ico" aria-hidden="true">{ICONE[chi]}</span>
      <h2 id="comprende-t">Cosa comprende</h2>
    </div>
    <ul class="comprende-lista">{comprende}</ul>
    {foto("servizio-" + chi, "(max-width: 899px) 100vw, 40vw", "foto comprende-foto")}
  </div>
</section>{aggiunta}
<section class="sezione sezione--asfalto" aria-labelledby="perche-t">
  <div class="wrap">
    <h2 id="perche-t">Perché da me</h2>
    <ul class="perche">{perche}</ul>
  </div>
</section>
<section class="sezione" id="domande" aria-labelledby="domande-t">
  <div class="wrap servizio-faq">
    <div><h2 id="domande-t">Domande frequenti</h2>{faq(p["faq"])}</div>
    <div class="riquadro">
      <h2>Chiedi un preventivo</h2>
      <p>Tocca il pulsante, scegli il mezzo e scrivimi due righe. Il preventivo è gratuito e arriva prima di iniziare.</p>
      {chiedi(chi, "Scrivimi su WhatsApp")}
      <a class="link" href="tel:{TEL}">{I["tel"]}Oppure chiama {tel_txt()}</a>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto" aria-labelledby="collegati-t">
  <div class="wrap">
    <h2 id="collegati-t">Servizi collegati</h2>
    {elenco(p["correlati"])}
    <a class="link collegati-tutti" href="{href("servizi")}">Tutti i servizi {I["freccia"]}</a>
  </div>
</section>''' + finale() + piede())


# ---------------------------------------------------------------- gommista: le date delle gomme invernali
def stagioni():
    date = [("Dal 15 ottobre", "Puoi montare le gomme invernali."),
            ("15 novembre – 15 aprile", "Dove le ordinanze lo prevedono, servono gomme invernali o catene a bordo."),
            ("Entro il 15 maggio", "Rimonti le gomme estive.")]
    voci = "".join(f'<li><strong>{quando}</strong><span>{cosa}</span></li>' for quando, cosa in date)
    return f'''
<section class="sezione sezione--stretta" aria-labelledby="stagioni-t">
  <div class="wrap">
    <div class="stagioni">
      <div class="stagioni-testa">
        <h2 id="stagioni-t">Gomme invernali: le date</h2>
        <p>Sono le date valide in generale: per le strade che fai contano le ordinanze locali.</p>
      </div>
      <ol class="stagioni-date">{voci}</ol>
      <div class="azioni">{chiedi("gommista", "Prenota il cambio gomme")}<a class="link" href="{href("gomme")}">Cerca le gomme per misura {I["freccia"]}</a></div>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- diagnosi: quando scade la revisione
def revisione():
    mesi = "".join(f'<option value="{i}">{m}</option>' for i, m in enumerate(MESI, 1))

    def data(chiave, legenda, di_cosa, aiuto=""):
        """Mese e anno: select nativi, l'elenco degli anni lo scrive lo script (dall'anno in corso al 1980)."""
        campi = "".join(f'''
            <div class="campo"><label class="sr" for="rev-{chiave}-{c}">{etichetta} {di_cosa}</label><select id="rev-{chiave}-{c}" name="{chiave}-{c}"{anni}><option value="">{etichetta}</option>{opzioni}</select></div>'''
                        for c, etichetta, anni, opzioni in (("m", "Mese", "", mesi), ("a", "Anno", " data-anni", "")))
        return f'''
        <fieldset class="calcolo-data" data-gruppo="{chiave}">
          <legend>{legenda}</legend>
          <div class="calcolo-campi">{campi}
          </div>{f'<p class="aiuto">{aiuto}</p>' if aiuto else ""}
        </fieldset>'''
    prenota = chiedi("diagnosi", "Prenota il controllo gratuito", extra=" data-prenota-revisione")
    return f'''
<section class="sezione sezione--stretta" id="revisione" aria-labelledby="revisione-t">
  <div class="wrap revisione">
    <div class="revisione-testo">
      <h2 id="revisione-t">Quando scade la revisione?</h2>
      <p class="lead">La prima revisione va fatta entro quattro anni dalla prima immatricolazione, poi ogni due anni.</p>
      <p>La scadenza è la fine del mese: un\'auto immatricolata a marzo 2023 va in revisione entro marzo 2027. Dopo, entro lo stesso mese dell\'ultima revisione, due anni più tardi.</p>
      <p class="piccolo">Vale per auto e mezzi fino a 3,5 tonnellate: per quelli più pesanti, come alcuni camper, la revisione è ogni anno.</p>
    </div>
    <form class="calcolo" data-revisione data-tel="+39 {TEL_TXT}" data-pagina="{url()}" novalidate hidden aria-labelledby="calcolo-t">
      <h3 id="calcolo-t">Calcola la tua scadenza</h3>{data("imm", "Prima immatricolazione", "della prima immatricolazione",
                                                                                         "È sulla carta di circolazione, al punto B.")}{data("ult", "Ultima revisione, se l'hai già fatta", "dell'ultima revisione")}
      <div class="calcolo-esito" data-esito-revisione aria-live="polite"></div>
      <div class="azioni calcolo-azioni" data-azioni-revisione hidden>
        {prenota}
        <button type="button" class="btn btn--vuoto" data-promemoria>{CALENDARIO}Aggiungi un promemoria al calendario</button>
      </div>
      <p class="nota" data-promemoria-esito role="status"></p>
      <p class="nota">Il calcolo resta sul tuo telefono: a me non arriva niente.</p>
    </form>
  </div>
</section>'''
