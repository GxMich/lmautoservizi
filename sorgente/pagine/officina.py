"""L'officina a Frassineto Po: il centro del sito. Dove siamo e orari, cosa trovi, la vettura di cortesia passo per passo,
le condizioni in breve e le domande frequenti. Testi approvati in testi_pagine.OFFICINA_PAGINA.
Niente mappa incorporata (privacy): solo il link a Google Maps."""
import re
from html import escape
from contenuti import PEC, PIVA, SEDE_LEGALE
from testi_pagine import OFFICINA_PAGINA as P
from sito import (inizia, scrivi, head, testata, intro, finale, piede, orari, foto, foto_info, azienda, briciole, svg,
                  t, tt, href, I, ICONE, VANTAGGI_ICO, TEL, EMAIL, MAPS, tel_txt, wa, indirizzo_officina)

try:  # i testi legali li cura un altro modulo: se mancano, resta solo il link alla pagina delle condizioni
    from testi_legali import VETTURA_CORTESIA_IT, VETTURA_CORTESIA_EN
except Exception:
    VETTURA_CORTESIA_IT = VETTURA_CORTESIA_EN = None

# Icone dell'officina, usate anche dalla home: stesso tratto dei vantaggi, si disegnano entrando nello schermo.
ICO = {
    "orario": svg('<circle cx="12" cy="12" r="9.5"/><path d="M12 6.8V12l3.6 2.2"/>'),
    "cortesia": VANTAGGI_ICO["cortesia"],
    "preventivo": svg('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M8.8 14.3l2.2 2.2 4.4-4.6"/>'),
    "pagamenti": svg('<rect x="2.5" y="5.5" width="19" height="13" rx="2.2"/><path d="M2.5 10h19M6 14.8h4.5"/>'),
    "attrezzi": ICONE["meccanica"],
}
# Icona e rimando (pagina, frammento, testo) di ognuna delle quattro sezioni di OFFICINA_PAGINA["sezioni"], nello stesso ordine.
SEZIONI_EXTRA = [("attrezzi", ("servizi", "", ("Tutti i servizi", "All services"))),
                 ("orario", None),
                 ("cortesia", ("officina", "cortesia", ("Come funziona", "How it works"))),
                 ("pagamenti", ("condizioni", "", ("Garanzia e condizioni", "Warranty and terms")))]


class _Campi(dict):
    """Campi dei testi legali ({telefono}, {piva}...): quelli che qui non servono restano come sono."""
    def __missing__(self, chiave):
        return "{" + chiave + "}"


def condizioni_cortesia():
    """Le condizioni della vettura di cortesia in breve, da testi_legali, senza le note per la revisione."""
    testo = t(VETTURA_CORTESIA_IT, VETTURA_CORTESIA_EN)
    if not testo or "<li>" not in testo:
        return f'<p>{t("Le condizioni te le spiego alla consegna.", "I explain the conditions when I hand it over.")}</p>'
    testo = re.sub(r"\s*<!--.*?-->", "", testo, flags=re.S)
    if "{" in testo:
        try:
            testo = testo.format_map(_Campi(titolare="L.M. Autoservizi di Miglietta Luca", sede_legale=SEDE_LEGALE, piva=PIVA,
                                            email=EMAIL, pec=PEC, telefono=tel_txt()))
        except (IndexError, ValueError):
            pass
    return testo


def rimando(extra):
    if not extra:
        return ""
    pagina, frammento, testo = extra
    return f'<a class="link" href="{href(pagina, frammento=frammento)}">{tt(testo)} {I["freccia"]}</a>'


def costruisci():
    inizia("officina")
    domande = [(tt(d), tt(r)) for d, r in P["faq"]]
    faq = "".join(f'<details><summary>{escape(d, False)}</summary><div class="faq-risposta"><p>{escape(r, False)}</p></div></details>' for d, r in domande)
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": d, "acceptedAnswer": {"@type": "Answer", "text": r}} for d, r in domande]}

    # Fascia di foto: l'interno e, quando c'è uno scatto diverso, l'ingresso accanto (oggi le due foto di esempio coincidono).
    if foto_info("ingresso")[0] != foto_info("officina")[0]:
        fascia = (f'<div class="wrap fascia officina-fascia">{foto("officina", "(max-width: 899px) 100vw, 62vw", "foto")}'
                  f'{foto("ingresso", "(max-width: 899px) 100vw, 36vw", "foto")}</div>')
    else:
        fascia = f'<div class="wrap fascia">{foto("officina", "(max-width: 1280px) 100vw, 1280px", "foto foto--fascia")}</div>'

    sezioni = "".join(f'<li>{ICO[ico]}<h2>{tt(titolo)}</h2><p>{tt(testo)}</p>{rimando(extra)}</li>'
                      for (titolo, testo), (ico, extra) in zip(P["sezioni"], SEZIONI_EXTRA))
    tappe = "".join(f'<li class="tappa"><span class="tappa-n">{i + 1}</span><div><h3>{tt(titolo)}</h3><p>{tt(testo)}</p></div></li>'
                    for i, (titolo, testo) in enumerate(P["cortesia_passi"]))

    scrivi(head(tt(P["title"]), tt(P["description"]), [azienda(), briciole(), faq_schema], immagine="officina") + testata()
           + intro(tt(P["h1"]), tt(P["intro"])) + fascia + f'''
<section class="sezione" id="dove" aria-labelledby="dove-t">
  <div class="wrap officina-dove">
    <div class="officina-dove-testo">
      <h2 id="dove-t">{t("Dove siamo e orari", "Location and opening hours")}</h2>
      <p class="officina-indirizzo">{indirizzo_officina()}<span>{t("A pochi chilometri da Casale Monferrato", "A few kilometres from Casale Monferrato")}</span></p>
      <p>{t("Prima di passare chiamami: concordiamo l'intervento e ti do le indicazioni per arrivare.", "Before coming, give me a call: we'll agree on the job and I'll give you directions.")}</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="tel:{TEL}">{I["tel"]}{t("Chiama", "Call")} {tel_txt()}</a>
        <a class="btn btn--vuoto" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}{t("Scrivi su WhatsApp", "Message on WhatsApp")}</a>
      </div>
      <a class="link" href="{MAPS}" target="_blank" rel="noopener">{t("Apri in Google Maps", "Open in Google Maps")} {I["esterno"]}</a>
    </div>
    <div class="officina-orari">
      <h3>{t("Orari", "Opening hours")}</h3>
      <p class="stato" data-stato></p>
      {orari()}
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto" aria-label="{t("L'officina in breve", "The workshop at a glance")}">
  <div class="wrap">
    <ul class="vantaggi-lista officina-sezioni">{sezioni}</ul>
  </div>
</section>
<section class="sezione" id="cortesia" aria-labelledby="cortesia-t">
  <div class="wrap officina-cortesia">
    <div class="officina-cortesia-passi">
      <h2 id="cortesia-t">{t("La vettura di cortesia, passo per passo", "The courtesy car, step by step")}</h2>
      <div class="percorso" data-percorso><span class="percorso-linea" aria-hidden="true"><span></span></span><ol class="percorso-tappe">{tappe}</ol></div>
    </div>
    <div class="riquadro officina-condizioni">
      <h2>{t("Le condizioni in breve", "The terms in brief")}</h2>
      {condizioni_cortesia()}
      <a class="link" href="{href("condizioni")}">{t("Leggi le condizioni complete", "Read the full terms")} {I["freccia"]}</a>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto" id="domande" aria-labelledby="domande-t">
  <div class="wrap officina-faq">
    <div class="officina-faq-testa">
      <h2 id="domande-t">{t("Domande frequenti", "Frequently asked questions")}</h2>
      <p class="lead">{t("Non trovi la risposta? Chiamami o scrivimi: ti rispondo io.", "Can't find the answer? Call or message me: I'll answer personally.")}</p>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>''' + finale(t("Porta il tuo mezzo in officina.", "Bring your vehicle to the workshop."),
                       t("Chiamami o scrivimi: ti dico quando portarlo. Se ti serve la vettura di cortesia, dimmelo subito.",
                         "Call or message me: I'll tell you when to bring it in. If you need the courtesy car, let me know straight away.")) + piede())
