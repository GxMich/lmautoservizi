"""Contatti: numero, WhatsApp, recapiti, orari e di nuovo le caselle dei servizi."""
from contenuti import PEC, PIVA, SEDE_LEGALE, REA
from sito import (inizia, scrivi, head, testata, intro, piede, orari, foto, griglia_servizi, azienda, briciole,
                  t, I, TEL, EMAIL, MAPS, tel_txt, wa, indirizzo_officina)


def costruisci():
    inizia("contatti")
    rea = f'\n        <div><dt>REA</dt><dd>{REA}</dd></div>' if REA else ""
    scrivi(head(t("Contatti | L.M. Autoservizi, Frassineto Po", "Contact | L.M. Autoservizi, Frassineto Po"),
                t("Chiama il 342 643 6085 o scrivi su WhatsApp. Officina a Frassineto Po, aperta dal lunedì al venerdì dalle 7:30 alle 19:30, orario continuato.",
                  "Call +39 342 643 6085 or message on WhatsApp. Workshop in Frassineto Po, open Monday to Friday from 7:30 to 19:30, no lunch break."),
                [azienda(), briciole()], immagine="ingresso") + testata()
           + intro(t("Contatti", "Contact"), t("Chiamami o scrivimi su WhatsApp: ti rispondo io.", "Call me or message me on WhatsApp: I'll answer personally.")) + f'''
<section class="sezione">
  <div class="wrap contatti-griglia">
    <div class="contatti-diretti">
      <a class="numerone" href="tel:{TEL}">{tel_txt()}</a>
      <p>{t("Al telefono e su WhatsApp rispondo io, dal lunedì al venerdì.", "I answer the phone and WhatsApp myself, Monday to Friday. WhatsApp is the easiest way to reach me if you don't speak Italian.")}</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}{t("Scrivi su WhatsApp", "Message on WhatsApp")}</a>
        <a class="btn btn--vuoto" href="mailto:{EMAIL}">{I["mail"]}Email</a>
      </div>
      <dl class="recapiti">
        <div><dt>{t("Telefono", "Phone")}</dt><dd><a href="tel:{TEL}">{tel_txt()}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>{t("PEC", "Certified email (PEC)")}</dt><dd><a href="mailto:{PEC}">{PEC}</a></dd></div>
        <div><dt>{t("Officina", "Workshop")}</dt><dd>{indirizzo_officina()}</dd></div>
        <div><dt>{t("Sede legale", "Registered office")}</dt><dd>{SEDE_LEGALE}</dd></div>
        <div><dt>{t("Partita IVA", "VAT number")}</dt><dd>{PIVA}</dd></div>{rea}
      </dl>
    </div>
    <div class="contatti-orari">
      <h2>{t("Orari", "Opening hours")}</h2>
      {orari()}
      <p class="stato" data-stato></p>
      <a class="link" href="{MAPS}" target="_blank" rel="noopener">{t("Apri in Google Maps", "Open in Google Maps")} {I["esterno"]}</a>
      {foto("ingresso", "(max-width: 899px) 100vw, 45vw", "foto contatti-foto")}
      <p class="piccolo">{t("Prima di passare chiamami: concordiamo l'intervento e ti do le indicazioni per arrivare.", "Before coming, give me a call: we'll agree on the job and I'll give you directions.")}</p>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto" aria-labelledby="scegli-t">
  <div class="wrap">
    <h2 id="scegli-t">{t("Oppure scegli il servizio", "Or choose the service")}</h2>
    <p class="lead">{t("Scegli il mezzo, scrivi due righe e il messaggio parte già pronto su WhatsApp.", "Choose your vehicle, write a couple of lines and the message is ready on WhatsApp.")}</p>
    {griglia_servizi(False)}
  </div>
</section>''' + piede())
