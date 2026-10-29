"""Contatti: numero, WhatsApp, recapiti, orari e di nuovo le caselle dei servizi."""
from contenuti import PEC, PIVA, SEDE_LEGALE, REA
from sito import (inizia, scrivi, head, testata, intro, piede, orari, foto, griglia_servizi, azienda, briciole,
                  I, TEL, EMAIL, MAPS, tel_txt, wa, indirizzo_officina)


def costruisci():
    inizia("contatti")
    rea = f'\n        <div><dt>REA</dt><dd>{REA}</dd></div>' if REA else ""
    scrivi(head("Contatti | L.M. Autoservizi, Frassineto Po",
                "Chiama il 342 643 6085 o scrivi su WhatsApp. Officina a Frassineto Po, aperta dal lunedì al venerdì dalle 7:30 alle 19:30, orario continuato.",
                [azienda(), briciole()], immagine="ingresso") + testata()
           + intro("Contatti", "Chiamami o scrivimi su WhatsApp: ti rispondo io.") + f'''
<section class="sezione">
  <div class="wrap contatti-griglia">
    <div class="contatti-diretti">
      <a class="numerone" href="tel:{TEL}">{tel_txt()}</a>
      <p>Al telefono e su WhatsApp rispondo io, dal lunedì al venerdì.</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}Scrivi su WhatsApp</a>
        <a class="btn btn--vuoto" href="mailto:{EMAIL}">{I["mail"]}Email</a>
      </div>
      <dl class="recapiti">
        <div><dt>Telefono</dt><dd><a href="tel:{TEL}">{tel_txt()}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>PEC</dt><dd><a href="mailto:{PEC}">{PEC}</a></dd></div>
        <div><dt>Officina</dt><dd>{indirizzo_officina()}</dd></div>
        <div><dt>Sede legale</dt><dd>{SEDE_LEGALE}</dd></div>
        <div><dt>Partita IVA</dt><dd>{PIVA}</dd></div>{rea}
      </dl>
    </div>
    <div class="contatti-orari">
      <h2>Orari</h2>
      {orari()}
      <p class="stato" data-stato></p>
      <a class="link" href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps {I["esterno"]}</a>
      {foto("ingresso", "(max-width: 899px) 100vw, 45vw", "foto contatti-foto")}
      <p class="piccolo">Prima di passare chiamami: concordiamo l'intervento e ti do le indicazioni per arrivare.</p>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto" aria-labelledby="scegli-t">
  <div class="wrap">
    <h2 id="scegli-t">Oppure scegli il servizio</h2>
    <p class="lead">Scegli il mezzo, scrivi due righe e il messaggio parte già pronto su WhatsApp.</p>
    {griglia_servizi(False)}
  </div>
</section>''' + piede())
